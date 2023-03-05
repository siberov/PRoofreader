import pytest
import pytest_mock
from proofreader.proofreader import Proofreader

def test_main(mocker):
    #mocker.patch('proofreader.proofreader.__init__', return_value=2)
    Proofreader.__init__ = mocker.Mock(return_value=2)
    Proofreader.get_user = mocker.Mock(return_value="test")
    assert Proofreader.get_user() == "test"
    assert Proofreader.__init__() == 2