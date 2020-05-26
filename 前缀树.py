class TrieNode:
    def __init__(self):
        self.p = 0
        self.e = 0 
        self.nexts = [None]*26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        node = self.root
        node.p += 1
        path = 0
        for ch in word:
            path = ord(ch) - ord('a')
            if not node.nexts[path]:
                node.nexts[path] =  TrieNode()
            node = node.nexts[path]
            node.p += 1
        node.e += 1

    def search(self, word):
        if not word:
            return
        node = self.root
        path = 0
        for ch in word:
            path = ord(ch) - ord('a')
            if not node.nexts[path]:
                return 0
            node = node.nexts[path]
        return node.e

    def prefixNumber(self, word):
        if not word:
            return
        node = self.root
        path = 0
        for ch in word:
            path = ord(ch) - ord('a')
            if not node.nexts[path]:
                return 0
            node = node.nexts[path]
        return node.p
            
    def delete(self, word):
        if self.search(word):
            node = self.root
            node.p -= 1
            path = 0
            for ch in word:
                path = ord(ch) - ord('a')
                node.nexts[path].p -= 1
                if node.nexts[path] == 0:
                    node.nexts[path] = None
                    return
                node = node.nexts[path]
            node.e -= 1
            

if __name__ == "__main__":
    node = Trie()
    data = ['abc','abc','ab','bks']
    for word in data:
        node.insert(word)
    node.delete('abc')
    print(node.prefixNumber('ab'))