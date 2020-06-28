import testr
import warnings

# Importing Chandra.cmd_states triggers a FutureWarning from the deprecated
# Ska.ParseCM being imported. Chandra.cmd_states is itself deprecated, so
# just hide that particular warning in testing.
with warnings.catch_warnings():
    warnings.simplefilter('ignore', FutureWarning)
    import Ska.ParseCM  # noqa

testr.testr()
