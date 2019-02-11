
import jinja2
import govuk_country_register

def test_govuk_country_register_jinja_filter():

    jinja_env = jinja2.Environment()
    jinja_env.filters["to_country"] = govuk_country_register.to_country

    template = jinja_env.from_string("""{{ country_code|to_country }}""")

    output = template.render(country_code="GB")

    assert output == "United Kingdom"
