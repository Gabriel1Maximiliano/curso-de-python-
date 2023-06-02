
def repeated_number( *args ):
    zero_index = 0
    list_of_numbers = list( args )
    if zero_index <= len( list_of_numbers ):
        for num in list_of_numbers:
            if args[ zero_index ] == 0 and args[ zero_index ] == 0:
                return True
            else:
                zero_index +=1
        return False        
    
print( repeated_number( 1,2,3,0,0 ) )