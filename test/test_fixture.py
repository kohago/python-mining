from io import  StringIO
import  time
import  pytest

@pytest.fixture(scope="module",autouse=True)
def use_aa():
    sio = StringIO("12345")
    time.sleep(1)
    print("StringIO has been created!!")
    yield(sio)
    time.sleep(1)
    sio.close()
    print("close StringIO")

def test_1(use_aa):
    assert use_aa.getvalue() == "2345"

def test_2(use_aa):
    assert use_aa.getvalue() == "3456"

#only when all failed go to yield
#def test_3(use_aa):
#    assert use_aa.getvalue() == "12345"
