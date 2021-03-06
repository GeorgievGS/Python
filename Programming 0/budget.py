##Иванчо събира пари за книги по програмиране.
##Има и списък с книгите, които иска да вземе, обаче не е сигурен в две неща:
##
##Колко най-много книги ще може да вземе със своя бюджет
##Колко кредит ще трябва да изтегли, за да може да вземе останалите книги,
##извън бюджета му.




def on_budget(books, budget):

    result = {
        "books_on_budget": 0,
        "loan": 0
        }

    books = sorted(books)
    total_book = sum(books)
    count = 0

    for book in books:
        if budget - book < 0:
            break
        count += 1
        budget -= book
        total_book -= book

    result["books_on_budget"] = count
    result["loan"] = max(0, total_book - budget)
    
    return result


print(on_budget([0, 0, 0], 10))
print(on_budget([50, 60, 10], 20))
print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))

