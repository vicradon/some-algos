import json

class TrieNode():
    def __init__(self):
        self.children = {}

class PrefixTree():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        ptr = self.root

        for char in string:
            # if this character is not in the tree, initialize this character as a new node
            if char not in ptr.children:
                ptr.children[char] = TrieNode()

            # then go one step into the node
            ptr = ptr.children[char]

    def search(self, string):
        ptr = self.root

        for char in string:
            if char in ptr.children:
                ptr = ptr.children[char]
            else:
                return False
            
        return True
            

    def dictrep(self, node):
        rep = dict()

        if not node.children:
            return {}

        for key in node.children:
            rep[key] = self.dictrep(node.children[key])

        return rep
    
    def pretty_print(self, indent=1):
        '''
        pretty-print rep
        {
            "a": {
                "p": {
                    "p": {}
                }
            }
        }
        '''
        out = self.dictrep(self.root)
        print(json.dumps(out, indent=indent))
    

        

if __name__ == "__main__":
    tree = PrefixTree()

    tree.insert("boy")
    tree.insert("brother")
    tree.insert("man")
    tree.insert("masculine")

    tree.pretty_print()

    print(tree.search("man")) # True
    print(tree.search("manny")) # False
    print(tree.search("da-boss")) # False

