# code for calculate addition, substraction, multiplicaton and divison 
num1=input()
num2=input()
def calc(add,sub,mul,div):
     if num1>num2:
          print(num1,add,num2,"=",num1+num2)
   #       print(num1,sub,num2,"=",num1-num2)
          print(num1,mul,num2,"=",num1*num2)
          print(num1,div,num2,"=",num1/num2)
     elif num1<num2:
          print(num1,add,num2,"=",num1+num2)
          print(num1,sub,num2,"=",num1-num2)
          print(num1,mul,num2,"=",num1*num2)
          print(num1,div,num2,"=",num1/num2)
     else:
          print(num1,add,num2,"=",num1+num2)
          print(num1,sub,num2,"=",num1-num2)
          print(num1,mul,num2,"=",num1*num2)
          print(num1,div,num2,"=",num1/num2)
          
calc('+','-','*','/')
