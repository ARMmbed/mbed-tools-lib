#
# Copyright (C) 2020 Arm Mbed. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""Helpers for logging errors according to severity of the exception."""
import logging

LOGGING_FORMAT = "%(levelname)s: %(message)s"


def log_exception(logger: logging.Logger, exception: Exception, show_traceback: bool = False) -> None:
    """Logs an exception in both normal and verbose forms.

    Args:
        logger: logger
        exception: exception to log
        show_traceback: show the full traceback.
    """
    logger.error(exception, exc_info=show_traceback)


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
