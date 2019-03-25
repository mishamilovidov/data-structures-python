#!/usr/bin/env python3
from collections import deque

class BinaryTree(object):
    '''
    A binary tree.
    '''
    def __init__(self):
        self.root = None


    def __repr__(self):
        return repr(self.root)


    def set(self, key, value):
        '''
        Adds the given key=value pair to the tree.
        '''
        if self.root is None:
            self.root = Node(None, key, value)
        else:
            self._insert(key, value, self.root)


    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        if self.root is None:
            return None
        else:
            return self._get(key, self.root)


    def remove(self, key):
        '''
        Removes the given key from the tree.
        Returns silently if the key does not exist.
        '''
        #TODO


    def walk_dfs_inorder(self, node=None):
        '''
        An iterator that walks the tree in DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        if node is None: node = self.root

        if node.left: yield from self.walk_dfs_inorder(node.left)
        yield (node.key, node.value)
        if node.right: yield from self.walk_dfs_inorder(node.right)



    def walk_dfs_preorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in preorder DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        if node is None: node = self.root

        yield (node.key, node.value)
        if node.left: yield from self.walk_dfs_preorder(node.left)
        if node.right: yield from self.walk_dfs_preorder(node.right)


    def walk_dfs_postorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in inorder DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        if node is None: node = self.root

        if node.left: yield from self.walk_dfs_postorder(node.left)
        if node.right: yield from self.walk_dfs_postorder(node.right)
        yield (node.key, node.value)


    def walk_bfs(self):
        '''
        An iterator that walks the tree in BFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        q = [] 
    
        # Enqueue Root and initialize height 
        q.append(self.root) 
    
        while(len(q) > 0): 
            yield (q[0].key, q[0].value) 
            node = q.pop(0) 
    
            if node.left is not None: 
                q.append(node.left) 
    
            if node.right is not None: 
                q.append(node.right) 


    ##################################################
    ###   Helper methods

    def _insert(self, key, value, current_node):
        '''
        Internal method to insert a node into tree
        '''
        if current_node.key > key:
            if current_node.left is None:
                current_node.left = Node(current_node, key, value)
            else:
                self._insert(key, value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(current_node, key, value)
            else:
                self._insert(key, value, current_node.right)
    
    def _get(self, key, current_node):
        '''
        Internal method to get a node by key
        '''
        if current_node.key == key:
            return current_node.value
        elif current_node.key > key:
            if current_node.left.key == key:
                return current_node.left.value
            else:
                return self._get(key, current_node.left)
        else:
            if current_node.right.key == key:
                return current_node.right.value
            else:
                return self._get(key, current_node.right)

    def _replace_node(self, oldnode, newnode):
        '''
        Internal method to remove a node from its parent
        '''
        #TODO: feel free to use or remove this method


    def _find(self, key):
        '''
        Internal method to find a node by key.
        Returns (parent, node).
        '''
        if self.root is None or self.root.key == key: 
            return self.root 
    
        if self.root.key < key: 
            return self._find(self.root.right.key) 
        
        return self._find(self.root.left.key)



class Node(object):
    '''
    A node in a binary tree.
    '''
    def __init__(self, parent, key, value):
        '''Creates a linked list.'''
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        result = []
        def recurse(node, prefix1, side, prefix2):
            if node is None:
                return
            result.append(prefix1 + node.key + side)
            if node.right is not None:
                recurse(node.left, prefix2 + '\u251c\u2500\u2500 ', ' \u2c96', prefix2 + '\u2502   ')
            else:
                recurse(node.left, prefix2 + '\u2514\u2500\u2500 ', ' \u2c96', prefix2 + '    ')
            recurse(node.right, prefix2 + '\u2514\u2500\u2500 ', ' \u1fe5', prefix2 + '    ')
        recurse(self, '', '', '')
        return '\n'.join(result)
