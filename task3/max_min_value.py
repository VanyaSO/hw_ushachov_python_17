def max_min_value(arr, find_value):
    max = arr[0]
    min = arr[0]
    
    for i in arr:
        if i > max:
            max = i
        elif i < min:
            min = i
            
    if find_value == "max":
        print(f"Max value {max}")
    elif find_value == "min":
        print(f"Max value {min}")