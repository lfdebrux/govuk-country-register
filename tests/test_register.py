
import pytest

from io import StringIO

from govuk_country_register.register import Register


def test_register_object_can_be_constructed_from_csv_file_using_path(shared_datadir):
    register = Register.from_csv(shared_datadir / "letter.csv")
    assert register.find("A")

def test_register_object_can_be_constructed_from_csv_file_using_string_io(shared_datadir):
    contents = (shared_datadir / "letter.csv").read_text()
    register = Register.from_csv(StringIO(contents))
    assert register.find("A")

def test_register_object_can_be_constructed_from_csv_file_using_list_of_strings(shared_datadir):
    contents = (shared_datadir / "letter.csv").read_text().splitlines(keepends=True)
    register = Register.from_csv(contents)
    assert register.find("A")

def test_register_csv_can_contain_unicode_characters(shared_datadir, ascii_locale):
    register = Register.from_csv(shared_datadir / "letter.csv")
    assert register.find("Ñ")
