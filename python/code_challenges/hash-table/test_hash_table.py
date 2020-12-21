from hash_table import Node, LinkedList, HashTable

def test_table():
    hashtable = HashTable()
    assert hashtable

def test_key():
    hashtable = HashTable()
    initial = hashtable._hash('a')
    second = hashtable._hash('b')
    assert initial != second

def test_add_hash_table():
    hashtable = HashTable()
    hashtable.add('spam', "fried egg")
    actual = hashtable.get('spam')
    expected ='fried egg'
    assert actual == expected

def test_get_key():
    hashtable = HashTable()
    hashtable.add('reeses puffs', '9 out of 10 rating')
    actual = hashtable.get('reeses puffs')
    expected = '9 out of 10 rating'
    assert actual == expected

def test_get_value_from_key():
    hashtable = HashTable()
    hashtable.add('cheerios', '1 out of 10 rating')
    hashtable.add('ct crunch', '8 out of 10 rating')
    assert hashtable.get('ct crunch') == '8 out of 10 rating'
    assert hashtable.get('cheerios') == '1 out of 10 rating'

