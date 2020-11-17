from linked_list.linked_list import Linked_list


def test_version():
    assert __version__ == '0.1.0'

def test_linked_list_kth_from_end():
    ll = Linked_list()
    ll.insert(5)
    ll.insert(9)
    ll.insert(3)
    ll.insert(7)
    actual = ll.kth_from_end(1)
    expected = 9
    assert actual == expected

