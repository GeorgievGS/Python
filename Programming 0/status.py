def status_count(students):

    result = {
        "finalized": [],
        "not_finalized": []
    }

    for student in students:
        if student["status"] is "finalized":
            result["finalized"] += [student["name"]]
        elif student["status"] is "not_finalized" :
            result["not_finalized"] += [student["name"]]

    return result
##def status_count(students):
##    result = {
##      "finalized": [],
##      "not_finalized": []
##    }
##    
##    for student in students:
##        if student["status"] is "finalized":
##            result["finalized"] += [student["name"]]
##        elif student["status"] is "not_finalized":
##            result["not_finalized"] += [student["name"]]
##
##    return result
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
