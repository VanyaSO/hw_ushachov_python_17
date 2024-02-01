from print_list import print_list
from max_min_value import max_min_value
from print_value import print_value
from delete_value import delete_value
from task4.delete_value_try import delete_value_try
from task4.print_value_try import print_value_try

def actions(arr):
    
    while True:
        try:
            action = int(input("Choose action: 1-print list | 2-max value in list | 3-min value in list | 4-print value | 5-delete value: "))
  
            match action:
                case 1: print_list(arr)
                case 2: max_min_value(arr, "max")
                case 3: max_min_value(arr, "min") 
                case 4: print_value(arr), print_value_try(arr)
                case 5: delete_value(arr), delete_value_try(arr)
                case _: raise ValueError ("Invalid action selected.") # throw error if action not = 1,2,3,4,5 
        except ValueError:
            print("There are no such options") 