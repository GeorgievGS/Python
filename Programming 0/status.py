##Радо е изпаднал в затруднение с курса по Ruby on Rails.
##
##Системата му е дала списък с всички кандидатствали курсисти и техния статус -
##дали са си предали задачите или не.
##Обаче Радо се е объркал и не може да разбере колко са финализираните
##кандидатури и колко не са.





def status_count(students):

    result = {
    "finalized": [],
    "not_finalized": []
        }

    for student in students:
        if student["status"] is "finalized":
            result["finalized"] += [student["name"]]
        elif student["status"] is "not_finalized":
            result["not_finalized"] +=[student["name"]]
    
    return result

students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]
print(status_count(students))
