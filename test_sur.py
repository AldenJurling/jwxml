import os.path


#FOCUS_SAMPLE_PATH = './test_surs/sm_defocus.xml'

SUR_ROOT = os.path.join(os.path.dirname(__file__), 'test_surs')
FOCUS_SAMPLE_PATH = os.path.join(SUR_ROOT, 'sm_defocus.xml')

from jwxml import SUR


def test_read():
    with open(FOCUS_SAMPLE_PATH):
        pass


def test_load():
    sur = SUR(FOCUS_SAMPLE_PATH)


def test_xmltext():
    sur = SUR(FOCUS_SAMPLE_PATH)
    print(sur.xmltext)


