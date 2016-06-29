def create_matrix(x,y):
    x = int(x)
    y = int(y)
    matrix = []

    for row in range(0,x):
        matrix.append([])
        for column in range (0,y):
            matrix[row].append(0)  
    
    return matrix

def view_matrix(matrix):
    for row in range(0,len(matrix)):
        print(matrix[row])
    print("Местата с '0' са свободни, а с 'z'-заети")
       
def book_place(x,y, matrix):
    matrix[x - 1][y - 1] = 'z'
        
    return  create_matrix(x,y)

def realise_place(x,y, matrix):
    matrix[x - 1][y - 1] = 0
    return create_matrix(x,y)


    





        
        

    
                        
    


