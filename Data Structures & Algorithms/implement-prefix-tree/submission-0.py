class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.children:
                temp.children[char] = Node()
            temp = temp.children[char]
        temp.endOfWord = True


    def search(self, word: str) -> bool:
        temp = self.root
        for char in word:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return temp.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for char in prefix:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return True
        