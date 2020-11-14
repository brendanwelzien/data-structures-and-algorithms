import pytest
from linked_list.linked_list import LinkedList

def test_instance(): #instance check
    assert LinkedList()

def test_LinkedList_insert():
    L = LinkedList()
    L.insert("a")
    L.insert("b")
    assert L.head.value == "b"
    assert L.head.next_n.value == "a"

def test_LinkedList_head():
    L = LinkedList()
    assert L.head == None

def test_LinkedList_multiple():
    L = LinkedList()
    L.insert("c")
    L.insert("b")
    L.insert("a")

    actual = str(L)
    expected =" { a } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_LinkedList_true():
    L = LinkedList()
    L.insert("a")
    L.insert("b")
    L.insert("c")
    actual = L.includes("c")
    expected = True
    assert actual == expected

def test_LinkedList_false():
    L = LinkedList()
    L.insert("a")
    L.insert("b")
    L.insert("c")
    actual = L.includes("d")
    expected = False
    assert actual == expected

def test_LinkedList_collection():
    L = LinkedList()
    L.insert("a")
    L.insert("b")
    L.insert("c")
    return L
