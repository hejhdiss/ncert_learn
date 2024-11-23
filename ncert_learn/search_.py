def binary_search(arr, target):
    """Performs binary search to find the target in a sorted list."""
    try:
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Check if the target is at the middle
            if arr[mid] == target:
                return mid  # Return the index of the target
            # If target is smaller, ignore the right half
            elif arr[mid] > target:
                high = mid - 1
            # If target is larger, ignore the left half
            else:
                low = mid + 1
        return -1  # Target is not present in the list
    except Exception as e:
        return f"Error: {e}"

def linear_search(arr, target):
    """Performs linear search to find the target in an unsorted list."""
    try:
        for index, element in enumerate(arr):
            if element == target:
                return index  # Return the index where the target is found
        return -1  # Target is not present in the list
    except Exception as e:
        return f"Error: {e}"

def jump_search(arr, target):
    """Performs jump search on a sorted list."""
    try:
        n = len(arr)
        step = int(n ** 0.5)  # Optimal step size
        prev = 0
        
        # Jump forward to find a block where the target might be present
        while arr[min(step, n) - 1] < target:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1  # Target is not present in the list
        
        # Perform linear search within the identified block
        for i in range(prev, min(step, n)):
            if arr[i] == target:
                return i
        return -1  # Target is not present in the list
    except Exception as e:
        return f"Error: {e}"

def exponential_search(arr, target):
    """Performs exponential search on a sorted list."""
    try:
        n = len(arr)
        
        # If the target is the first element
        if arr[0] == target:
            return 0
        
        # Find the range where the element may be present
        index = 1
        while index < n and arr[index] <= target:
            index *= 2
        
        # Perform binary search within the range found
        return binary_search(arr[index // 2: min(index, n)], target)
    except Exception as e:
        return f"Error: {e}"

def ternary_search(arr, target):
    """Performs ternary search on a sorted list."""
    try:
        low = 0
        high = len(arr) - 1
        
        while high >= low:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3
            
            if arr[mid1] == target:
                return mid1
            elif arr[mid2] == target:
                return mid2
            elif target < arr[mid1]:
                high = mid1 - 1
            elif target > arr[mid2]:
                low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1
        return -1  # Target is not present in the list
    except Exception as e:
        return f"Error: {e}"

def interpolation_search(arr, target):
    """Performs interpolation search on a sorted list."""
    try:
        low = 0
        high = len(arr) - 1
        
        while low <= high and arr[low] != arr[high]:
            pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
            
            # If target is found at the position
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        if arr[low] == target:
            return low
        return -1  # Target is not present in the list
    except Exception as e:
        return f"Error: {e}"

# Example usage of the search functions
