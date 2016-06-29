import function
 
loop = 1

while loop == 1:

    print()
    print("Добре дошли в програмата Cinema hall!")
    print()
    print("1.Добави кино зала")
    print("2.Виж залата")
    print("3.Резервирай място")
    print("4.Отмени резервация")
    print("5.Изтрии кино залата")
    print("6. Изход")
    print()

    number = input("Избери опция:")
    
    if number == "1":
        x = input("Въведете колко реда има в залата")
        x = int(x)
        y = input("Въведете колко места има на ред в залата")
        y = int(y)
        matrix = function.create_matrix(x,y)
        

    elif number == "2":
        try:
            print(function.view_matrix(matrix))
            matrix1 = function.create_matrix(x,y)
        except:
            print("Не съществува кино зала, моля създайте зала!")

   

    elif number == "3":
        x = input("Въведете реда в залата, който искате да резервирате")
        y = input("Въведете място на реда, което искате да резервирате")
        x = int(x)
        y = int(y) 
        matrix1 = function.book_place(x,y,matrix)
        print("Всичко мина успешно")
            
    
   
    elif number == "4":
        x = input("Въведете реда в залата, където е мястото, за което искате да отмените резервация")
        y = input("Въведете място на реда, за което искате да отмените резервация")
        x = int(x)
        y = int(y)
        matrix1 = function.realise_place(x,y, matrix)
        print("Всичко мина успешно")   
        
    
    

    elif number == "5":
        del(matrix)
    
    elif number == "6":
        loop = 0


    else:
        print("Грешна опция!")
        print("Моля въведете една от 5-те опции!")
    
