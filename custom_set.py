class CustomSet():
   
    def __init__(self):
        self.items = []

    def add(self, single_item: str):
        self.single_item = single_item
        self.items.append(single_item)
    def remove(self, single_item: str):
        pass
    def as_list(self) -> list:
        return self.items
    def clear(self):
        pass

def main():

    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    print(my_set.as_list())


if __name__ == "__main__":
    main()
