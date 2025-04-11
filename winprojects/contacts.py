contacts={'number' : 4,
          'students' : [{'name':'graeme', 'email':'graeme@gmail.com'},
                        {'name':'dave', 'email':'dave@yahoo.com'},
                        {'name':'sarah', 'email':'sarah@msn.com'},
                        {'name':'tom', 'email':'tom@hotmail.com'}]
          }

print('Students email:')          
for student in contacts['students']:
    print(student['name'], "'s email is: ", student['email'])




#for number,students in contacts.items():
 #   print(number, ':',students)



