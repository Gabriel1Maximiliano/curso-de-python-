def devolver_distintos( *args ):
    add = 0
    list_of_numbers = list( args )
    list_of_numbers.sort()
    for num in list_of_numbers:
        add += num
    if add > 15:
        the_bigger_number = list_of_numbers.pop()
        print(f"The biggest number of the list is: { the_bigger_number }")
    if add < 10:
        the_smallest_number = list_of_numbers[0]
        print(f"The smallest number of the list is: { the_smallest_number }") 
    if add in range(10,16):
        middle_value = list_of_numbers[1]
        print(f"The middle value is { middle_value }")
devolver_distintos(1,2,8)

 
    