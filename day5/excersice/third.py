
def repeated_number( *args ):
    zeros = []
    list_of_numbers = list( args )
    for num in list_of_numbers:
        if num == 0:
            zeros.append( num )
            if len( zeros ) == 2:
                return True
            else:
                pass
    return False        
    
print( repeated_number( 1,2,3,0,0 ) )