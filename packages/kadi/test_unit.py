import warnings
import testr

with warnings.catch_warnings():
    warnings.simplefilter('ignore', FutureWarning)
    import kadi.commands.commands_v1  # noqa

testr.testr()
