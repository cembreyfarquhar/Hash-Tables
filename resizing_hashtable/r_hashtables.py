

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.filled = 0
 

# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (( hash << 5) + hash) + ord(x)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    if hash_table.filled >= hash_table.capacity:
        print('doubling!')
        hash_table = hash_table_resize(hash_table)
    index = hash(key, hash_table.capacity)
    new_pair = LinkedPair(key, value)

    if hash_table.storage[index] is None:
        hash_table.storage[index] = new_pair
    else:
        next_link = hash_table.storage[index].next
        while next_link is not None:
            next_link = next_link.next
        next_link = value
    hash_table.filled += 1

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] != None:
        hash_table.storage[index] = None
    else:
        print('Error, that key does not exist')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        return None
    
    return hash_table.storage[index].value


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    # second_storage = [None] * hash_table.capacity
    
    ht = HashTable(hash_table.capacity * 2)

    for i in range(0, hash_table.capacity):
        print(hash_table.storage[i].key)
        ht.storage[i] = hash_table.storage[i]
    return ht


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)


    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
