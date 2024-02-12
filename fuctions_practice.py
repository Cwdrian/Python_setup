def hello():
    print("Hello, Me, its me again")

def pack(item1, item2, item3):
    """Packs three items into a list."""
    return [item1, item2, item3]

def eat_lunch(items):
    """Prints out the lunch items."""
    if len(items) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat", items[0])
        for item in items[1:]:
            print("Next I eat", item)


hello()
packed_items = pack("sandwich", "apple", "chips")
print(packed_items)
eat_lunch(packed_items)