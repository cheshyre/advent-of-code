def make_differences(arr):
    diff_arr = [0] * (len(arr) - 1)
    for i in range(1, len(arr)):
        diff_arr[i - 1] = arr[i] - arr[i - 1]
        
    return diff_arr


def paths_reconstruction(arr):
    num_paths_arr = [0] * len(arr)
    num_paths_arr[-1] = 1
    
    for i in range(len(arr) - 2, -1, -1):
        num_paths = 0
        for j in range(1, 4):
            if i + j >= len(arr):
                break
            if arr[i+j] - arr[i] > 3:
                break
            num_paths += num_paths_arr[i + j]
        num_paths_arr[i] = num_paths
        
    return num_paths_arr[0]
