from collections import deque

def set_create():
    """
    Creates an empty set.
    
    Returns:
        set: An empty set.
    """
    return set()

def set_add(s, element):
    """
    Adds an element to the set.
    
    Args:
        s (set): The set to which the element is added.
        element: The element to be added to the set.

    Returns:
        None
    """
    if not isinstance(s, set):
        raise TypeError("The provided set is not a valid set.")
    s.add(element)

def set_remove(s, element):
    """
    Removes an element from the set.
    
    Args:
        s (set): The set from which the element is removed.
        element: The element to be removed.

    Returns:
        None
    """
    if not isinstance(s, set):
        raise TypeError("The provided set is not a valid set.")
    if element in s:
        s.remove(element)
    else:
        raise KeyError(f"Element {element} not found in the set.")

def set_discard(s, element):
    """
    Discards an element from the set if it exists, without raising an error if it doesn't.
    
    Args:
        s (set): The set from which the element is discarded.
        element: The element to be discarded.

    Returns:
        None
    """
    if not isinstance(s, set):
        raise TypeError("The provided set is not a valid set.")
    s.discard(element)

def set_is_member(s, element):
    """
    Checks if an element is a member of the set.
    
    Args:
        s (set): The set to check membership in.
        element: The element to check.

    Returns:
        bool: True if the element is a member of the set, False otherwise.
    """
    if not isinstance(s, set):
        raise TypeError("The provided set is not a valid set.")
    return element in s

def set_size(s):
    """
    Returns the size of the set (the number of elements in the set).
    
    Args:
        s (set): The set to measure.

    Returns:
        int: The number of elements in the set.
    """
    if not isinstance(s, set):
        raise TypeError("The provided set is not a valid set.")
    return len(s)

def set_clear(s):
    """
    Clears all elements from the set.
    
    Args:
        s (set): The set to clear.

    Returns:
        None
    """
    if not isinstance(s, set):
        raise TypeError("The provided set is not a valid set.")
    s.clear()

def queue_create():
    """
    Creates an empty queue using deque.
    Returns:
        deque: An empty queue.
    """
    return deque()

def queue_enqueue(queue, item):
    """
    Adds an item to the queue.
    
    Args:
        queue (deque): The queue to which the item is added.
        item: The item to be added to the queue.

    Returns:
        None
    """
    if not isinstance(queue, deque):
        raise TypeError("The provided queue is not a valid deque.")
    queue.append(item)

def queue_dequeue(queue):
    """
    Removes and returns the front item from the queue.
    
    Args:
        queue (deque): The queue from which the item is removed.

    Returns:
        item: The removed item or None if the queue is empty.
    """
    if not isinstance(queue, deque):
        raise TypeError("The provided queue is not a valid deque.")
    if len(queue) > 0:
        return queue.popleft()
    return None

def queue_peek(queue):
    """
    Returns the front item of the queue without removing it.
    
    Args:
        queue (deque): The queue to peek from.

    Returns:
        item: The front item or None if the queue is empty.
    """
    if not isinstance(queue, deque):
        raise TypeError("The provided queue is not a valid deque.")
    if len(queue) > 0:
        return queue[0]
    return None

def queue_is_empty(queue):
    """
    Checks if the queue is empty.
    
    Args:
        queue (deque): The queue to check.

    Returns:
        bool: True if the queue is empty, False otherwise.
    """
    if not isinstance(queue, deque):
        raise TypeError("The provided queue is not a valid deque.")
    return len(queue) == 0

def queue_size(queue):
    """
    Returns the size of the queue.
    
    Args:
        queue (deque): The queue to measure.

    Returns:
        int: The size of the queue.
    """
    if not isinstance(queue, deque):
        raise TypeError("The provided queue is not a valid deque.")
    return len(queue)

def queue_clear(queue):
    """
    Clears all items from the queue.
    
    Args:
        queue (deque): The queue to clear.

    Returns:
        None
    """
    if not isinstance(queue, deque):
        raise TypeError("The provided queue is not a valid deque.")
    queue.clear()

def dict_create():
    """
    Creates an empty dictionary.
    
    Returns:
        dict: An empty dictionary.
    """
    return {}

def dict_add(dictionary, key, value):
    """
    Adds a key-value pair to the dictionary.
    
    Args:
        dictionary (dict): The dictionary to which the key-value pair is added.
        key: The key to add.
        value: The value to associate with the key.

    Returns:
        None
    """
    if not isinstance(dictionary, dict):
        raise TypeError("The provided dictionary is not a valid dict.")
    dictionary[key] = value

def dict_get(dictionary, key):
    """
    Retrieves a value by key from the dictionary.
    
    Args:
        dictionary (dict): The dictionary to retrieve the value from.
        key: The key whose value is to be retrieved.

    Returns:
        value: The value associated with the key, or None if the key doesn't exist.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("The provided dictionary is not a valid dict.")
    return dictionary.get(key, None)

def dict_remove(dictionary, key):
    """
    Removes a key-value pair from the dictionary.
    
    Args:
        dictionary (dict): The dictionary from which the key-value pair is removed.
        key: The key to remove.

    Returns:
        None
    """
    if not isinstance(dictionary, dict):
        raise TypeError("The provided dictionary is not a valid dict.")
    if key in dictionary:
        del dictionary[key]

def dict_key_exists(dictionary, key):
    """
    Checks if a key exists in the dictionary.
    
    Args:
        dictionary (dict): The dictionary to check.
        key: The key to check for existence.

    Returns:
        bool: True if the key exists, False otherwise.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("The provided dictionary is not a valid dict.")
    return key in dictionary

def dict_get_keys(dictionary):
    """
    Retrieves all keys from the dictionary.
    
    Args:
        dictionary (dict): The dictionary to retrieve keys from.

    Returns:
        list: A list of keys in the dictionary.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("The provided dictionary is not a valid dict.")
    return list(dictionary.keys())

def dict_get_values(dictionary):
    """
    Retrieves all values from the dictionary.
    
    Args:
        dictionary (dict): The dictionary to retrieve values from.

    Returns:
        list: A list of values in the dictionary.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("The provided dictionary is not a valid dict.")
    return list(dictionary.values())

def dict_size(dictionary):
    """
    Returns the size (number of key-value pairs) of the dictionary.
    
    Args:
        dictionary (dict): The dictionary to measure.

    Returns:
        int: The number of key-value pairs in the dictionary.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("The provided dictionary is not a valid dict.")
    return len(dictionary)

def dict_clear(dictionary):
    """
    Clears all key-value pairs from the dictionary.
    
    Args:
        dictionary (dict): The dictionary to clear.

    Returns:
        None
    """
    if not isinstance(dictionary, dict):
        raise TypeError("The provided dictionary is not a valid dict.")
    dictionary.clear()

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def tree_insert(root, key):
    """
    Inserts a key into the binary search tree.
    
    Args:
        root (TreeNode): The root node of the tree.
        key: The key to insert.

    Returns:
        TreeNode: The root node after insertion.
    """
    if not isinstance(root, (TreeNode, type(None))):
        raise TypeError("The root must be a TreeNode or None.")
    if root is None:
        return TreeNode(key)
    if key < root.value:
        root.left = tree_insert(root.left, key)
    else:
        root.right = tree_insert(root.right, key)
    return root

def tree_inorder(root):
    """
    Performs an inorder traversal of the tree (Left, Root, Right).
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        list: The values in the tree in inorder.
    """
    if root is None:
        return []
    return tree_inorder(root.left) + [root.value] + tree_inorder(root.right)

def tree_search(root, key):
    """
    Searches for a key in the binary search tree.
    
    Args:
        root (TreeNode): The root node of the tree.
        key: The key to search for.

    Returns:
        bool: True if the key exists, False otherwise.
    """
    if root is None:
        return False
    if key == root.value:
        return True
    elif key < root.value:
        return tree_search(root.left, key)
    else:
        return tree_search(root.right, key)

def tree_minimum(root):
    """
    Finds the minimum value in the binary search tree.
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        TreeNode: The node with the minimum value.
    """
    current = root
    while current and current.left:
        current = current.left
    return current

def tree_maximum(root):
    """
    Finds the maximum value in the binary search tree.
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        TreeNode: The node with the maximum value.
    """
    current = root
    while current and current.right:
        current = current.right
    return current

def tree_size(root):
    """
    Returns the number of nodes in the binary search tree.
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        int: The number of nodes in the tree.
    """
    if root is None:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)

def tree_height(root):
    """
    Calculates the height of the binary tree.
    The height is the length of the longest path from the root to a leaf node.
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        int: The height of the tree.
    """
    if root is None:
        return 0
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return max(left_height, right_height) + 1

def tree_level_order(root):
    """
    Performs level-order traversal (Breadth First Search) of the tree.
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        list: A list of values in level-order.
    """
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def tree_postorder(root):
    """
    Performs a postorder traversal of the tree (Left, Right, Root).
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        list: The values in the tree in postorder.
    """
    if root is None:
        return []
    return tree_postorder(root.left) + tree_postorder(root.right) + [root.value]

def tree_preorder(root):
    """
    Performs a preorder traversal of the tree (Root, Left, Right).
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        list: The values in the tree in preorder.
    """
    if root is None:
        return []
    return [root.value] + tree_preorder(root.left) + tree_preorder(root.right)

def tree_breadth_first(root):
    """
    Performs a breadth-first traversal of the tree.
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        list: A list of values visited in breadth-first order.
    """
    return tree_level_order(root)

def tree_depth_first(root):
    """
    Performs a depth-first traversal of the tree.
    
    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        list: A list of values visited in depth-first order.
    """
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def tree_delete(root, key):
    """
    Deletes a node from the binary search tree with the given key.
    
    Args:
        root (TreeNode): The root node of the tree.
        key: The key of the node to delete.

    Returns:
        TreeNode: The new root node after deletion.
    """
    if root is None:
        return root

    if key < root.value:
        root.left = tree_delete(root.left, key)
    elif key > root.value:
        root.right = tree_delete(root.right, key)
    else:
        # Node to be deleted has one or no children
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Node to be deleted has two children
        min_node = tree_minimum(root.right)
        root.value = min_node.value
        root.right = tree_delete(root.right, min_node.value)
    
    return root
