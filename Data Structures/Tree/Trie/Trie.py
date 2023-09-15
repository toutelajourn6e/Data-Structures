class Node:
    def __init__(self):
        self.children = [None] * 52
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def is_empty(self, node):
        for i in range(52):
            if node.children[i]:
                return False
        return True

    def insert(self, key):
        cur = self.root
        for i in range(len(key)):
            idx = ord(key[i]) - ord('A') if key[i].isupper() else ord(key[i]) - ord('a') + 26
            if cur.children[idx] is None:
                cur.children[idx] = Node()
            cur = cur.children[idx]
        cur.is_end = True

    def search(self, key):
        if self.root is None:
            print("Trie is empty")
            return

        cur = self.root
        for i in range(len(key)):
            idx = ord(key[i]) - ord('A') if key[i].isupper() else ord(key[i]) - ord('a') + 26
            if cur.children[idx] is None:
                print(f"\"{key}\" is not in Trie")
                return False
            cur = cur.children[idx]

        if cur.is_end:
            print(f"\"{key}\" is in Trie")
            return True
        else:
            print(f"\"{key}\" is not in Trie")
            return False

    def remove(self, node, key, depth=0):
        if node is None:
            return None

        if depth == len(key):
            node.is_end = False
            if self.is_empty(node):
                del node
                node = None
            return node

        idx = ord(key[depth]) - ord('A') if key[depth].isupper() else ord(key[depth]) - ord('a') + 26
        node.children[idx] = self.remove(node.children[idx], key, depth + 1)

        if node != self.root:
            if self.is_empty(node) and not node.is_end:
                del node
                node = None
            return node



if __name__ == '__main__':
    words = ["Mercury", "Venus", "Earth", "Mars", "Jupyter", "Saturn", "Uranus", "Neptune", "Earthquake"]
    trie = Trie()
    print(trie.is_empty(trie.root))

    for word in words:
        trie.insert(word)

    trie.search("Neptune")
    trie.search("Earth")
    trie.search("Earthquake")
    trie.search("Venus")
    trie.search("Jupyter")
    print("-----------------------")
    trie.remove(trie.root, "Venus")
    trie.remove(trie.root, "Earth")
    trie.search("Venus")
    trie.search("Earth")
    trie.search("Earthquake")


# True
# "Neptune" is in Trie
# "Earth" is in Trie
# "Earthquake" is in Trie
# "Venus" is in Trie
# "Jupyter" is in Trie
# -----------------------
# "Venus" is not in Trie
# "Earth" is not in Trie
# "Earthquake" is in Trie
