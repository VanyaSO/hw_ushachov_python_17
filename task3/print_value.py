def print_value(arr):
    while True:
        index = input("Enter index: ")
        
        try:
            # Chek if value index is number
            if not index.isdigit():
                raise TypeError("Need enter a number")
            
            print(arr[int(index)])
            break
        except IndexError:
            print("Index not found")
        except TypeError as e:
            print(e)