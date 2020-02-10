import logging
from unittest import TestCase, mock

from mbed_tools_lib.logging import log_exception, set_log_level, LOGGING_FORMAT


class TestLogException(TestCase):
    def test_log_exception_error(self):
        mock_logger = mock.Mock(spec_set=logging.Logger)
        mock_exception = mock.Mock(spec_set=Exception)

        log_exception(mock_logger, mock_exception)

        mock_logger.error.assert_called_once_with(mock_exception)
        mock_logger.debug.assert_called_once_with(mock_exception, exc_info=True)


@mock.patch("mbed_tools_lib.logging.logging", return_value=mock.Mock(spec_set=logging))
class TestSetLogLevel(TestCase):
    def test_debug(self, mocked_logging):
        set_log_level(verbose_count=3)
        mocked_logging.basicConfig.assert_called_once_with(level=mocked_logging.DEBUG, format=LOGGING_FORMAT)

    def test_info(self, mocked_logging):
        set_log_level(verbose_count=2)
        mocked_logging.basicConfig.assert_called_once_with(level=mocked_logging.INFO, format=LOGGING_FORMAT)

    def test_warning(self, mocked_logging):
        set_log_level(verbose_count=1)
        mocked_logging.basicConfig.assert_called_once_with(level=mocked_logging.WARNING, format=LOGGING_FORMAT)

    def test_error(self, mocked_logging):
        set_log_level(verbose_count=0)
        mocked_logging.basicConfig.assert_called_once_with(level=mocked_logging.ERROR, format=LOGGING_FORMAT)
