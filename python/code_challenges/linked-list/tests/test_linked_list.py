import pytest
from linked_list.linked_list import Linked_list, zip_lists

def test_linked_list_kth_from_end():
    ll = Linked_list()
    ll.insert(5)
    ll.insert(9)
    ll.insert(3)
    ll.insert(7)
    actual = ll.kth_from_end(1)
    expected = 9
    assert actual == expected

def test_zip_lists(the_list_a, the_list_b):
    zip_ll = zip_lists(the_list_a, the_list_b)
    actual = zip_ll.__str__()
    expected = '4 -> 8 -> 12 -> 16 -> 20 -> None'
    assert actual == expected

@pytest.fixture
def the_list_b():
    ll = Linked_list()
    ll.append(8)
    ll.append(16)
    return ll

@pytest.fixture
def the_list_a():
    ll = Linked_list()
    ll.append(4)
    ll.append(12)
    ll.append(20)
    return ll
