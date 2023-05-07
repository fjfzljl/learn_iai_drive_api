import sys
import logging
import pytest
from py.xml import html

import invertedai as iai


logger = logging.getLogger("drive test")


def pytest_configure(config):
    config._metadata["test software version"] = "0.1"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("Description"))
    cells.pop()


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(1, html.td(report.description))
    except AttributeError as error:
        logging.info("AttributeError trying to pytest_html_results_table_row - start")
        logging.error(error)
        logging.info("AttributeError trying to pytest_html_results_table_row - end")
    except Exception as e:
        logging.error(
            f"Unknown Exception trying to pytest_html_results_table_row : {e}"
        )
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


@pytest.fixture(scope="module")
def suite_setupteardown():
    logging.info("suite_setupteardown fixture start...")

    # API key:
    iai.add_apikey("mZHY4zRJkJ557Aut85Q8T2pSFELU05Tn7LMrqxgu")

    yield

    logging.info("suite_setupteardown fixture end...")
