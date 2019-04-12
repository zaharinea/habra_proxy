import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def html():
    with open("tests/test.html") as fd:
        return fd.read()


@pytest.fixture
def get_soup(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup, html


@pytest.fixture
def expected_html():
    with open("tests/expected.html") as fd:
        return fd.read()


@pytest.fixture
def get_expected_soup(expected_html):
    soup = BeautifulSoup(expected_html, "html.parser")
    return soup, expected_html
