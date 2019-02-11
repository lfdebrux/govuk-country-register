
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
