"""
Main runner for algorithms and data structures learning 

"""
import time

def linear_search(list, target):
    """
    Returns the index position of target if found in list, else returns None
    """
    for i in range (0, len(list)):
        if list[i] == target:
            return i


    return None

def binary_search(list, target):
    """
    Returns the index position of target if found in list, else returns None
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last) // 2 # floor division
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return None

def recursive_binary_search(list, target):
    if len(list) == 0:
        return None
    
    mid = len(list)//2
    
    if list[mid] == target:
        return mid

    if list[mid] < target:
        return recursive_binary_search(list[mid+1:], target)
    else:
        return recursive_binary_search(list[:mid], target)

def verify_search(index, i):
    if index is not None:
        if index != i:
            print(index, i)
            print("ERROR")
    else:
        print(f"Target not found in list")



def test_search(search):
    array_size = 100000
    print(f"using array of size: {array_size}")
    num_runs = array_size + 2
    l = [x for x in range(array_size)]

    count = 0 
    total_time = 0.0
    for i in range(0, num_runs, 100):
        count += 1
        index = search(l, i)
        verify_search(index, i)
        tic = time.time()
        #verify_search(index)
        total_time += time.time() - tic

    print(f"Average time for {count} runs is: {total_time / count}")


def main():
    print("testing linear search...")
    test_search(linear_search)

    print("\ntesting binary search...")
    test_search(binary_search)

    #print("\ntesting recursive binary search...")
    #test_search(recursive_binary_search)

if __name__ == "__main__":
    main()
