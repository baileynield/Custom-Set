class CustomSet():
   
    def __init__(self):
        self.items = []

    def add(self, single_item: str):
        self.single_item = single_item
        if single_item not in self.items: 
            self.items.append(single_item)
        
    def remove(self, single_item: str):
        self.single_item = single_item
        if single_item in self.items:
            self.items.remove(single_item
)
    def as_list(self) -> list:
        return self.items
    def clear(self):
        pass

def main():

    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")
    my_set.remove("item 2")
    print(my_set.as_list())


if __name__ == "__main__":
    main()
