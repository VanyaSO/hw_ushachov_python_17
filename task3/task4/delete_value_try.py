def delete_value2(arr, index):
        print(f"You delete value {arr.pop(int(index))}")
     
def delete_value_try(arr):
    
    while True:
        index = input("Enter index: ")
            
        try:
            if not index.isdigit():
                raise TypeError("Need enter a number")
            delete_value2(arr, index)
            break
        except IndexError:
            print("Index not found")
        except TypeError as e:
            print(e)