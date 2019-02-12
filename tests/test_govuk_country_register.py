
import pytest

import govuk_country_register

def test_to_country():
    assert govuk_country_register.to_country("GB") == "United Kingdom"

def test_register():
    assert govuk_country_register.country.register.find("GB") == {
        "country": "GB",
        "name": "United Kingdom",
        "official-name": "The United Kingdom of Great Britain and Northern Ireland",
        "citizen-names": "Briton;British citizen",
    }

    with pytest.raises(KeyError):
        govuk_country_register.country.register.find("XY") is None

def test_register_find_returns_latest_item():
    # The Republic of Côte D’Ivoire has two entries
    # The first entry's item is missing the circumflex above the o
    # The second entry's item is corrected
    assert govuk_country_register.country.register.find("CI")["official-name"] \
            == "The Republic of Côte D’Ivoire"
