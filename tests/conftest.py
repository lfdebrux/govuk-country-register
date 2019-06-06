
import pytest

import locale

@pytest.fixture
def ascii_locale():
    old = locale.setlocale(locale.LC_ALL)
    locale.setlocale(locale.LC_ALL, "C")
    yield
    locale.setlocale(locale.LC_ALL, old)
