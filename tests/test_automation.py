from automation import __version__
from automation.automation import *

def test_version():
    assert __version__ == '0.1.0'


def test_phones():
    assert extract_phones("001-x909-344 is my phone number")==['001-x909-344']

def test_emails():
    assert extract_emails("omarzadyab@gmail.com is my email")==['omarzadyab@gmail.com']

