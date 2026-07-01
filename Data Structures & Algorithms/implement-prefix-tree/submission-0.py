class TrieNode:
    def __init__(self):
            self.children = [None] * 26
            self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            index = ord(w) - ord('a')

            if not curr.children[index]:
                node = TrieNode()
                curr.children[index] = node
            
            curr = curr.children[index]

        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            index = ord(w) - ord('a')

            if not curr.children[index]:
                return False
            
            curr = curr.children[index]

        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for p in prefix:
            index = ord(p) - ord('a')

            if not curr.children[index]:
                return False

            curr = curr.children[index]

        return True
        