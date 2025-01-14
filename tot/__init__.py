import logging

# make version number accessible
from ._version import __version__  # noqa: F401 to evade flake8
from .benchmark import (  # noqa: F401 to evade flake8
    CrossValidationBenchmark,
    ManualBenchmark,
    ManualCVBenchmark,
    SimpleBenchmark,
)

# make classes available upon package import
from .experiment import SimpleExperiment  # noqa: F401

# logger handling
log = logging.getLogger("dv")
log.setLevel("INFO")

c_handler = logging.StreamHandler()
c_handler.setLevel("WARNING")
c_format = logging.Formatter("%(levelname)s - (%(name)s.%(funcName)s) - %(message)s")
c_handler.setFormatter(c_format)
log.addHandler(c_handler)

logging.captureWarnings(True)
warnings_log = logging.getLogger("py.warnings")
warnings_log.addHandler(c_handler)

# enable write log files
write_log_file = False
if write_log_file:
    f_handler = logging.FileHandler("logs.log", "w+")
    # f_handler.setLevel("ERROR")
    f_format = logging.Formatter("%(asctime)s; %(levelname)s; %(name)s; %(funcName)s; %(message)s")
    f_handler.setFormatter(f_format)
    log.addHandler(f_handler)
    warnings_log.addHandler(f_handler)
