class Trie:
    
    class Node:
        def __init__(self,val=None):
            self.val = val
            self.is_word = False
            self.next = {}
        
    def __init__(self):
        self.root=self.Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.next:
                cur.next[w]=self.Node(w)
            cur = cur.next[w]
        cur.is_word = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.next:
                return False
            cur = cur.next[w]
        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.next:
                return False
            cur = cur.next[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)