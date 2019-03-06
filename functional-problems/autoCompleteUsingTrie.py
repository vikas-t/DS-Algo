#!/usr/bin/python3
# https://www.geeksforgeeks.org/auto-complete-feature-using-trie/


"""
Trie is a tree that stores strings. Maximum number of children of a 
node is equal to size of alphabet. Trie supports search, insert and delete 
operations in O(L) time where L is length of key.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.wordList = []
        # To fetch autosuggestion words
    
    def insert(self, key):
        node = self.root
        
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.last = True
    
    def search(self, key):
        node = self.root

        for ch in key:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return node and node.last
        # If the iteration ends,the last node should end in a word
    
    def suggest(self, node, key):
        if node.last:
            self.wordList.append(key)
        # Append the list of characters if they end in a word
        
        for ch, nextNode in node.children.items():
            self.suggest(nextNode, key+ch)
        # Recurse all the words for a given node
    
    def printAutoSuggest(self, key):
        notFound = False
        node = self.root
        
        for ch in key:
            if ch not in node.children:
                notFound = True
                break
            node = node.children[ch]

        if notFound:
            return 0
        # Return 0 if suggestions are not found
        elif node.last and not node.children:
            return 0
        # If there are no more children, we cannot suggest
        else:
            self.suggest(node, key)
        
        for word in self.wordList:
            print(word, end=" ")
        print()
        return 1
    
######## Driver code ######################################################
words = ["hello", "dog", "hell", "cat", "a",  "hel", "help", "helps", "helping"]

t = Trie()
for word in words:
    t.insert(word)

t.printAutoSuggest("hel")
t.wordList = [] # Reset the previous suggested words
t.printAutoSuggest("help")


    


    



