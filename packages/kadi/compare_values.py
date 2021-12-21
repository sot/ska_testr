#!/usr/bin/env python

import os
import argparse
import shutil
from pathlib import Path
import difflib
import sys

import kadi.events
import kadi.cmds
import kadi.paths
from Chandra.Time import DateTime


def get_opt(args=None):
    parser = argparse.ArgumentParser(
        description='Generate new events and cmd data and compare with regression version')
    parser.add_argument("--start",
                        default='2015:001:12:00:00',
                        help=("Processing start date (default=2015:001:12:00:00"))
    parser.add_argument("--stop",
                        default='2015:030:12:00:00',
                        help="Processing stop date (default=2015:030:12:00:00)")
    parser.add_argument("--data-root",
                        default='events_cmds',
                        help="Root data directory  (default='events_cmds')")
    opt = parser.parse_args(args)
    return opt


def write_events(start, stop):
    print('Using events file {}'.format(kadi.paths.EVENTS_DB_PATH()))

    for attr in dir(kadi.events):
        evt = getattr(kadi.events, attr)
        if type(evt) is not kadi.events.EventQuery:
            continue

        # These event types are frequently updated after ingest.  See
        # https://github.com/sot/kadi/issues/85.  For now just ignore.
        if attr in ('caps', 'dsn_comms', 'major_events'):
            continue

        dat = evt.filter(start, stop).table

        # Standardize all float output to 3 decimal places. This is mostly tstart/tstop.
        for col in dat.itercols():
            if col.info.dtype.kind == 'f':
                col.info.format = '.3f'

        if len(dat) > 0:
            filename = os.path.join(opt.data_root, attr + '.txt')
            print('Writing event {}'.format(filename))
            dat.write(filename, format='ascii.fixed_width', overwrite=True)
        else:
            filename = os.path.join(opt.data_root, attr + '.ecsv')
            print('Writing event {}'.format(filename))
            dat.write(filename, format='ascii.ecsv', overwrite=True)


def write_cmds(start, stop):
    print('Using commands file {}'.format(kadi.paths.IDX_CMDS_PATH()))
    cmds = kadi.cmds.filter(start, stop)
    out = repr(cmds)
    filename = os.path.join(opt.data_root, 'cmds.txt')
    print('Writing commands {}'.format(filename))
    with open(filename, 'w') as fh:
        fh.write(out)


def compare_outputs():
    shutil.unpack_archive('events_cmds_regress.tar.bz2')

    files_a = sorted(Path('events_cmds_regress').glob('*'))
    files_b = sorted(Path('events_cmds').glob('*'))

    if [fn.name for fn in files_a] != [fn.name for fn in files_b]:
        raise ValueError('output files mismatch')

    has_diff = False
    for file_a, file_b in zip(files_a, files_b):
        print(f'Comparing files {file_a} {file_b}')
        lines_a = file_a.read_text().splitlines()
        lines_b = file_b.read_text().splitlines()
        # ecsv includes the format version in the first line, which should not be checked
        if file_a.suffix == '.ecsv':
            lines_a = lines_a[1:]
            lines_b = lines_b[1:]

        diffs = difflib.unified_diff(
            lines_a, lines_b,
            fromfile=str(file_a), tofile=str(file_b))

        diff_str = '\n'.join(diffs)
        if diff_str:
            print(f'**** DIFFS {file_a.name} ****')
            print(diff_str)
            print()
            has_diff = True

    return has_diff


if __name__ == '__main__':
    opt = get_opt()
    if not os.path.exists(opt.data_root):
        os.makedirs(opt.data_root)
    start = DateTime(opt.start) + 3
    stop = DateTime(opt.stop) - 3

    write_events(start, stop)
    write_cmds(start, stop)

    has_diff = compare_outputs()
    if has_diff:
        sys.exit(1)
