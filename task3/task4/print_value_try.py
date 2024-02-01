def print_value2(arr, index):
        print(arr[int(index)])
     
def print_value_try(arr):
    
    while True:
        index = input("Enter index: ")
            
        try:
            if not index.isdigit():
                raise TypeError("Need enter a number")
            print_value2(arr, index)
            break
        except IndexError:
            print("Index not found")
        except TypeError as e:
            print(e)