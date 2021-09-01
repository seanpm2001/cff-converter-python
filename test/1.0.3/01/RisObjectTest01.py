import os
import pytest
from test.contracts.RisObject import Contract
from cffconvert import RisObject
from cffconvert import Citation


@pytest.fixture
def ris_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r", encoding="utf8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return RisObject(citation.cffobj, initialize_empty=True)


class RisObjectTest(Contract):

    def test_abstract(self, ris_object):
        ris_object.add_abstract()
        assert ris_object.abstract is None

    def test_author(self, ris_object):
        ris_object.add_author()
        assert ris_object.author == 'AU  - Spaaks, Jurriaan H.\nAU  - Klaver, Tom\n'

    def test_check_cff_object(self, ris_object):
        ris_object.check_cff_object()
        # doesn't need an assert

    def test_date(self, ris_object):
        ris_object.add_date()
        assert ris_object.date == 'DA  - 2018-01-16\n'

    def test_doi(self, ris_object):
        ris_object.add_doi()
        assert ris_object.doi == 'DO  - 10.5281/zenodo.1162057\n'

    def test_keywords(self, ris_object):
        ris_object.add_keywords()
        assert ris_object.keywords == 'KW  - citation\nKW  - bibliography\nKW  - cff\nKW  - CITATION.cff\n'

    def test_print(self, ris_object):
        actual_ris = ris_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "ris.txt")
        with open(fixture, "r", encoding="utf8") as f:
            expected_ris = f.read()
        assert actual_ris == expected_ris

    def test_title(self, ris_object):
        ris_object.add_title()
        assert ris_object.title == 'TI  - cff-converter-python\n'

    def test_url(self, ris_object):
        ris_object.add_url()
        assert ris_object.url == 'UR  - https://github.com/citation-file-format/cff-converter-python\n'

    def test_year(self, ris_object):
        ris_object.add_year()
        assert ris_object.year == 'PY  - 2018\n'
