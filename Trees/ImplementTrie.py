'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 

There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

'''

class TrieNode:
    def __init__(self):
        #stores the children nodes
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            #not in hashmap yet, create a new node for it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            #move node pointer to child node
            cur = cur.children[c]
        
        #mark the end of the word
        cur.end_of_word = True
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children
        #will return True if the word exists within trie
        return cur.end_of_word

    def startsWith(self, prefix):
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
