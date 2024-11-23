class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def bst_insert(root, key):

    """
    Inserts a key into a binary search tree.

    Args:
        root (BSTNode or None): The root node of the tree.
        key: The key to insert.

    Returns:
        BSTNode: The new root node after insertion.
    """

    if root is None:
        return BSTNode(key)
    if key < root.value:
        root.left = bst_insert(root.left, key)
    else:
        root.right = bst_insert(root.right, key)
    return root

def bst_search(root, key):

    """
    Searches for a key in a binary search tree.

    Args:
        root (BSTNode or None): The root node of the tree.
        key: The key to search for.

    Returns:
        bool: True if the key exists, False otherwise.
    """

    if root is None:
        return False
    if root.value == key:
        return True
    elif key < root.value:
        return bst_search(root.left, key)
    else:
        return bst_search(root.right, key)

def bst_inorder(root):
    """
    Performs an inorder traversal of a binary search tree.

    Args:
        root (BSTNode or None): The root node of the tree.

    Returns:
        list: The values in the tree in inorder.
    """

    if root is None:
        return []
    return bst_inorder(root.left) + [root.value] + bst_inorder(root.right)
class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

def avl_insert(root, key):

    """
    Inserts a key into an AVL tree.

    Args:
        root (AVLNode or None): The root node of the tree.
        key: The key to insert.

    Returns:
        AVLNode: The new root node after insertion.
    """


    if root is None:
        return AVLNode(key)
    
    if key < root.value:
        root.left = avl_insert(root.left, key)
    else:
        root.right = avl_insert(root.right, key)

    root.height = 1 + max(avl_get_height(root.left), avl_get_height(root.right))

    balance = avl_get_balance(root)

    if balance > 1 and key < root.left.value:
        return avl_right_rotate(root)
    if balance < -1 and key > root.right.value:
        return avl_left_rotate(root)
    if balance > 1 and key > root.left.value:
        root.left = avl_left_rotate(root.left)
        return avl_right_rotate(root)
    if balance < -1 and key < root.right.value:
        root.right = avl_right_rotate(root.right)
        return avl_left_rotate(root)

    return root

def avl_get_height(node):

    """
    Gets the height of the node in the AVL tree.

    Args:
        node (AVLNode or None): The node to get the height of.

    Returns:
        int: The height of the node.
    """

    if node is None:
        return 0
    return node.height

def avl_get_balance(node):

    """
    Calculates the balance factor of a node in the AVL tree.

    Args:
        node (AVLNode or None): The node to calculate the balance factor for.

    Returns:
        int: The balance factor of the node, which is the difference in height 
        between the left and right subtrees.
    """

    if node is None:
        return 0
    return avl_get_height(node.left) - avl_get_height(node.right)

def avl_left_rotate(z):

    """
    Performs a left rotation on the given node in an AVL tree.

    Args:
        z (AVLNode): The node to perform the left rotation on.

    Returns:
        AVLNode: The new root node after the rotation.
    """

    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(avl_get_height(z.left), avl_get_height(z.right))
    y.height = 1 + max(avl_get_height(y.left), avl_get_height(y.right))
    return y

def avl_right_rotate(y):

    """
    Performs a right rotation on the given node in an AVL tree.

    Args:
        y (AVLNode): The node to perform the right rotation on.

    Returns:
        AVLNode: The new root node after the rotation.
    """

    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(avl_get_height(y.left), avl_get_height(y.right))
    x.height = 1 + max(avl_get_height(x.left), avl_get_height(x.right))
    return x
class RBTreeNode:
    def __init__(self, key):
        self.key = key
        self.color = 'RED'
        self.left = None
        self.right = None
        self.parent = None

def rb_insert(root, key):

    """
    Inserts a key into a red-black tree.

    Args:
        root (RBTreeNode or None): The root node of the tree.
        key: The key to insert.

    Returns:
        RBTreeNode: The root node after insertion.
    """

    node = RBTreeNode(key)
    if root is None:
        root = node
    else:
        root = rb_insert_fixup(root, node)
    return root

def rb_insert_fixup(root, node):

    """
    Fixes up the tree after inserting a new node.

    After a new node is inserted, this function is called to fix up the tree.
    It ensures that the tree remains a valid red-black tree. This is done by
    performing rotations and color changes on the tree nodes.

    Args:
        root (RBTreeNode): The root node of the tree.
        node (RBTreeNode): The newly inserted node.

    Returns:
        RBTreeNode: The root node after the fix up.
    """


    while node != root and node.parent.color == 'RED':
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            if uncle and uncle.color == 'RED':
                node.parent.color = 'BLACK'
                uncle.color = 'BLACK'
                node.parent.parent.color = 'RED'
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    node = node.parent
                    rb_left_rotate(node)
                node.parent.color = 'BLACK'
                node.parent.parent.color = 'RED'
                rb_right_rotate(node.parent.parent)
        else:
            if node == node.parent.left:
                node = node.parent
                rb_right_rotate(node)
            node.parent.color = 'BLACK'
            node.parent.parent.color = 'RED'
            rb_left_rotate(node.parent.parent)
    root.color = 'BLACK'
    return root

def rb_left_rotate(node):

    """
    Performs a left rotation on the given node in a red-black tree.

    Args:
        node (RBTreeNode): The node on which to perform the left rotation.

    This rotation shifts the node's right child up to take its place, 
    making the node the left child of its original right child. 
    This operation is used to maintain the properties of the 
    red-black tree during insertion and deletion.
    """

    y = node.right
    node.right = y.left
    if y.left:
        y.left.parent = node
    y.parent = node.parent
    if node.parent is None:
        root = y
    elif node == node.parent.left:
        node.parent.left = y
    else:
        node.parent.right = y
    y.left = node
    node.parent = y

def rb_right_rotate(node):

    """
    Performs a right rotation on the given node in a red-black tree.

    Args:
        node (RBTreeNode): The node on which to perform the right rotation.

    This rotation shifts the node's left child up to take its place, 
    making the node the right child of its original left child. 
    This operation is used to maintain the properties of the 
    red-black tree during insertion and deletion.
    """

    x = node.left
    node.left = x.right
    if x.right:
        x.right.parent = node
    x.parent = node.parent
    if node.parent is None:
        root = x
    elif node == node.parent.right:
        node.parent.right = x
    else:
        node.parent.left = x
    x.right = node
    node.parent = x

class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        """
        Transforms the input array into a heap, in-place.

        Args:
            arr (list): The list of elements to be heapified.

        This method initializes the heap with the given array and 
        ensures the heap property is satisfied by calling 
        '_heapify_down' on each non-leaf node, starting from the 
        last non-leaf node up to the root.
        """

        self.heap = arr
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):

        """
        Maintains the min-heap property by recursively swapping the element at
        index with its smallest child if it is greater.

        Args:
            index (int): The index of the element to be swapped.

        This method is a helper function for 'heapify' and is called on each
        non-leaf node in the heap. If the element at index is greater than one
        of its children, it is swapped with the smallest child and the method
        is recursively called on the affected sub-tree to maintain the
        min-heap property.
        """

        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
class BTreeNode:
    def __init__(self, t):
        self.t = t
        self.keys = []
        self.children = []
        self.leaf = True

def btree_insert(root, key, t):
    """
    Inserts a key into a B-tree of order t.

    Args:
        root (BTreeNode): The root node of the tree.
        key: The key to insert.
        t (int): The order of the tree.

    Returns:
        BTreeNode: The root node after insertion.
    """

    if len(root.keys) == 2 * t - 1:
        s = BTreeNode(t)
        s.children.append(root)
        btree_split(s, 0)
        root = s
    btree_insert_non_full(root, key)
    return root

def btree_insert_non_full(node, key):

    """
    Inserts a key into a B-tree node that is not full.

    Args:
        node (BTreeNode): The node to insert into.
        key: The key to insert.

    Returns:
        BTreeNode: The node after insertion.
    """
    

    i = len(node.keys) - 1
    if node.leaf:
        node.keys.append(None)
        while i >= 0 and key < node.keys[i]:
            node.keys[i + 1] = node.keys[i]
            i -= 1
        node.keys[i + 1] = key
    else:
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        if len(node.children[i].keys) == 2 * node.t - 1:
            btree_split(node, i)
            if key > node.keys[i]:
                i += 1
        node.children[i] = btree_insert_non_full(node.children[i], key)

def btree_split(parent, i):

    """
    Splits a B-tree node into two nodes when it is full.

    Args:
        parent (BTreeNode): The parent node of the node to split.
        i (int): The index of the node to split in the parent's children list.

    This method is a helper function for 'btree_insert' and is called when a
    node is full. It splits the node into two nodes and adds a new key to the
    parent node. It also updates the children and leaf status of the affected
    nodes.
    """

    t = parent.t
    node = parent.children[i]
    new_node = BTreeNode(t)
    parent.children.insert(i + 1, new_node)
    parent.keys.insert(i, node.keys[t - 1])
    new_node.keys = node.keys[t:(2 * t - 1)]
    node.keys = node.keys[0:t - 1]
    if not node.leaf:
        new_node.children = node.children[t:(2 * t)]
        node.children = node.children[0:t - 1]
    new_node.leaf = node.leaf
class TrieNode:
    """
    A TrieNode represents a single node in the Trie data structure.
    It contains a dictionary to store child nodes and a boolean to mark the end of a word.
    """
    def __init__(self):
        """
        Initializes a TrieNode with an empty children dictionary and a flag for word termination.
        """
        self.children = {}  # Dictionary to hold child nodes
        self.is_end_of_word = False  # Flag to mark the end of a word

    def trie_insert(self, word):
        """
        Insert a word into the Trie.
        
        Args:
            word (str): The word to insert into the Trie.
        
        Time Complexity: O(n), where n is the length of the word.
        """
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def trie_search(self, word):
        """
        Search for a word in the Trie.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            bool: True if the word exists in the Trie, False otherwise.
        
        Time Complexity: O(n), where n is the length of the word.
        """
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def trie_starts_with(self, prefix):
        """
        Check if there is any word in the Trie that starts with the given prefix.
        
        Args:
            prefix (str): The prefix to check for.
        
        Returns:
            bool: True if there is any word in the Trie that starts with the given prefix, False otherwise.
        
        Time Complexity: O(n), where n is the length of the prefix.
        """
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def trie_delete(self, word):
        """
        Delete a word from the Trie.
        
        Args:
            word (str): The word to delete from the Trie.
        
        Returns:
            bool: True if the word was successfully deleted, False if the word does not exist.
        
        Time Complexity: O(n), where n is the length of the word.
        """
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            child_node = node.children[char]
            should_delete_child = _delete(child_node, word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0
            return False

        return _delete(self, word, 0)

    def trie_autocomplete(self, prefix):
        """
        Generate all words in the Trie that start with a given prefix.
        
        Args:
            prefix (str): The prefix to search for autocompletion.
        
        Returns:
            list: A list of words that start with the given prefix.
        
        Time Complexity: O(n), where n is the length of the prefix, plus O(m) for generating the autocomplete words.
        """
        def _autocomplete(node, prefix, results):
            if node.is_end_of_word:
                results.append(prefix)
            for char, child_node in node.children.items():
                _autocomplete(child_node, prefix + char, results)

        node = self
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        _autocomplete(node, prefix, results)
        return results

    def trie_print(self):
        """
        Print all words in the Trie.
        
        This function helps visualize the structure of the Trie.
        """
        def _print(node, word):
            if node.is_end_of_word:
                print(word)
            for char, child_node in node.children.items():
                _print(child_node, word + char)

        _print(self, "")
def trie_insert(root, word):

    """
    Inserts a word into a trie.

    Args:
        root (TrieNode): The root node of the trie.
        word (str): The word to insert.

    This method inserts a word into the trie by traversing the trie and
    inserting new nodes for each character in the word. It marks the last node
    as an end of word node.

    Time complexity: O(m), where m is the length of the word.
    Space complexity: O(m), where m is the length of the word.
    """

    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)

    def segment_build(self, arr):
        """
        Builds the segment tree using the provided array.

        Args:
            arr (list): The input array used to build the segment tree.

        This method initializes the segment tree by storing the elements of the
        input array in the leaf nodes and then computes the sums for internal nodes
        in a bottom-up manner. The segment tree is stored in a flattened array
        format, where index n represents the start of the leaf nodes.
        """

        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def segment_query(self, l, r):

        """
        Queries the segment tree for a range sum.

        Args:
            l (int): The start index of the range.
            r (int): The end index of the range.

        Returns:
            int: The sum of the elements in the range [l, r] inclusive.

        This method uses a bottom-up approach to compute the sum of the elements
        in the range [l, r] by traversing the segment tree. It first adds the
        elements at the leaf nodes to the result, then moves up the tree and adds
        the sums of the internal nodes that overlap with the range. The result
        is returned as the sum of the elements in the range.

        Time complexity: O(log n), where n is the size of the segment tree.
        Space complexity: O(1), as it only uses a small amount of extra memory
        to store the result.
        """

        l += self.n
        r += self.n
        result = 0
        while l <= r:
            if l % 2 == 1:
                result += self.tree[l]
                l += 1
            if r % 2 == 0:
                result += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return result

### 8. **Quad Tree**


class QuadTreeNode:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.children = None
        self.points = []

    def quad_subdivide(self):

        """
        Subdivides the quad tree node into four sub-nodes by dividing its
        area into four equal parts. The sub-nodes are stored in the
        `children` attribute of the node.

        The sub-nodes are divided as follows:

        - top-left: `x, y, width // 2, height // 2`
        - top-right: `mid_x, y, width // 2, height // 2`
        - bottom-left: `x, mid_y, width // 2, height // 2`
        - bottom-right: `mid_x, mid_y, width // 2, height // 2`

        The original node is not modified except for having its `children`
        attribute set to the list of new sub-nodes.

        Time complexity: O(1), as it only creates four new nodes.
        Space complexity: O(1), as it only uses a small amount of extra memory
        to store the new nodes.
        """


        mid_x = self.x + self.width // 2
        mid_y = self.y + self.height // 2
        self.children = [
            QuadTreeNode(self.x, self.y, self.width // 2, self.height // 2),  # top-left
            QuadTreeNode(mid_x, self.y, self.width // 2, self.height // 2),  # top-right
            QuadTreeNode(self.x, mid_y, self.width // 2, self.height // 2),  # bottom-left
            QuadTreeNode(mid_x, mid_y, self.width // 2, self.height // 2)   # bottom-right
        ]

    def quad_insert(self, point):

        """
        Inserts a point into the quad tree node.

        Args:
            point (tuple): The point to insert, given as a tuple (x, y).

        Returns:
            bool: False if the point is inserted into the node or one of its
            descendants, True if the point is not inserted (which should not
            happen unless the point is outside the node's area).

        This method inserts the point into the node or one of its descendants
        if the point is within the node's area. If the node already contains
        four points, it subdivides itself into four sub-nodes by calling
        `subdivide` and then inserts the point into one of the sub-nodes by
        calling `insert` on the appropriate sub-node. If the point is not
        inserted into the node or one of its descendants, False is returned.
        Otherwise, True is returned.

        Time complexity: O(log n), where n is the number of nodes in the quad
        tree.
        Space complexity: O(1), as it only uses a small amount of extra memory
        to store the new nodes.
        """

        if len(self.points) < 4:
            self.points.append(point)
            return False

        if self.children is None:
            self.subdivide()

        for child in self.children:
            if child.contains(point):
                return child.insert(point)
        return False

    def quad_contains(self, point):

        """
        Checks if a point is contained within the node's area.

        Args:
            point (tuple): The point to check, given as a tuple (x, y).

        Returns:
            bool: True if the point is within the node's area, False otherwise.
        """

        return self.x <= point[0] < self.x + self.width and self.y <= point[1] < self.y + self.height
class OctreeNode:
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
        self.children = None
        self.points = []

    def oct_subdivide(self):

        """
        Subdivides the oct tree node into eight sub-nodes by dividing its
        volume into eight equal parts. The sub-nodes are stored in the
        `children` attribute of the node.

        The sub-nodes are divided as follows:

        - 1: `x, y, z, width // 2, height // 2, depth // 2`
        - 2: `mid_x, y, z, width // 2, height // 2, depth // 2`
        - 3: `x, mid_y, z, width // 2, height // 2, depth // 2`
        - 4: `mid_x, mid_y, z, width // 2, height // 2, depth // 2`
        - 5: `x, y, mid_z, width // 2, height // 2, depth // 2`
        - 6: `mid_x, y, mid_z, width // 2, height // 2, depth // 2`
        - 7: `x, mid_y, mid_z, width // 2, height // 2, depth // 2`
        - 8: `mid_x, mid_y, mid_z, width // 2, height // 2, depth // 2`

        The original node is not modified except for having its `children`
        attribute set to the list of new sub-nodes.

        Time complexity: O(1), as it only creates eight new nodes.
        Space complexity: O(1), as it only uses a small amount of extra memory
        to store the new nodes.
        """

        mid_x = self.x + self.width // 2
        mid_y = self.y + self.height // 2
        mid_z = self.z + self.depth // 2
        self.children = [
            OctreeNode(self.x, self.y, self.z, self.width // 2, self.height // 2, self.depth // 2),  # 1
            OctreeNode(mid_x, self.y, self.z, self.width // 2, self.height // 2, self.depth // 2),  # 2
            OctreeNode(self.x, mid_y, self.z, self.width // 2, self.height // 2, self.depth // 2),  # 3
            OctreeNode(mid_x, mid_y, self.z, self.width // 2, self.height // 2, self.depth // 2),  # 4
            OctreeNode(self.x, self.y, mid_z, self.width // 2, self.height // 2, self.depth // 2),  # 5
            OctreeNode(mid_x, self.y, mid_z, self.width // 2, self.height // 2, self.depth // 2),  # 6
            OctreeNode(self.x, mid_y, mid_z, self.width // 2, self.height // 2, self.depth // 2),  # 7
            OctreeNode(mid_x, mid_y, mid_z, self.width // 2, self.height // 2, self.depth // 2)   # 8
        ]

    def oct_insert(self, point):

        """
        Inserts a point into the octree node.

        Args:
            point (tuple): The point to insert, given as a tuple (x, y, z).

        Returns:
            bool: False if the point is inserted into the node or one of its
            descendants, True if the point is not inserted (which should not
            happen unless the point is outside the node's area).

        This method inserts the point into the node or one of its descendants
        if the point is within the node's area. If the node already contains
        eight points, it subdivides itself into eight sub-nodes by calling
        `subdivide` and then inserts the point into one of the sub-nodes by
        calling `insert` on the appropriate sub-node. If the point is not
        inserted into the node or one of its descendants, False is returned.
        Otherwise, True is returned.

        Time complexity: O(log n), where n is the number of nodes in the octree.
        Space complexity: O(1), as it only uses a small amount of extra memory
        to store the new nodes.
        """
        

        if len(self.points) < 8:
            self.points.append(point)
            return False

        if self.children is None:
            self.subdivide()

        for child in self.children:
            if child.contains(point):
                return child.insert(point)
        return False

    def oct_contains(self, point):

        """
        Checks if a point is contained within the node's area.

        Args:
            point (tuple): The point to check, given as a tuple (x, y, z).

        Returns:
            bool: True if the point is within the node's area, False otherwise.
        """

        return (self.x <= point[0] < self.x + self.width and
                self.y <= point[1] < self.y + self.height and
                self.z <= point[2] < self.z + self.depth)
