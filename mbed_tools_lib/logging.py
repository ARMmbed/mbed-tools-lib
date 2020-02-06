"""Helpers for logging errors according to severity of the exception."""
import logging

LOGGING_FORMAT = "%(levelname)s: %(message)s"


def log_exception(logger: logging.Logger, exception: Exception) -> None:
    """Logs an exception in both normal and verbose forms.

    Args:
        logger: logger
        exception: exception to log
    """
    logger.error(exception)
    logger.debug(exception, exc_info=True)


def set_log_level(verbose_count: int) -> None:
    """Sets the log level.

    Args:
        verbose_count: number of `-v` flags used
    """
    if verbose_count > 2:
        log_level = logging.DEBUG
    elif verbose_count == 2:
        log_level = logging.INFO
    elif verbose_count == 1:
        log_level = logging.WARNING
    else:
        log_level = logging.ERROR
    logging.basicConfig(level=log_level, format=LOGGING_FORMAT)
