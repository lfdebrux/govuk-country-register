import setuptools

setuptools.setup(
    name="govuk-country-register",
    version="0.2.1",
    author="Laurence de Bruxelles",
    author_email="laurence.debruxelles@digital.cabinet-office.gov.uk",
    description="Jinja2 filter to look up country codes using the GOV.UK country and territory registers",
    package_data={
        "govuk_country_register": ["country.csv"],
    },
    packages=setuptools.find_packages(),
)
