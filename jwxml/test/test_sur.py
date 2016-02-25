import os.path
import pkg_resources

FOCUS_SAMPLE_PATH = pkg_resources.resource_filename('jwxml.test', 'test_surs/sm_defocus.xml')

from jwxml.jwxml import SUR


def test_read():
    with open(FOCUS_SAMPLE_PATH):
        pass


def test_load():
    sur = SUR(FOCUS_SAMPLE_PATH)


def test_xmltext():
    sur = SUR(FOCUS_SAMPLE_PATH)
    print(sur.xmltext)


