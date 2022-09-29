# try, except, else and finally example on exception
try:
     print('hello')
except:
     print('variable x is not defined')
else:
     print('declare varibale x first')
finally:
     print('so this is a output')

x='hello'
if x is not int:
     raise Exception('x cant be greater than 1')

#input method example
user=input("Enter name of user")
print("name of user is"+user)

# placeholders example
cost=70
txt="the cost of object is {}"
print(txt.format(cost))
