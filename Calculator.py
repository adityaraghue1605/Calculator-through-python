# greetings 

print("Namaste sir, hope your are doing well")

# command selection

print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Average")

select = (eval((input("Please select the option give above to perform any one command :"))))

#  command designing 

if(select in [1,2,3,4,5]):
    Num1 = (eval(input("enter the first number :")))
    Num2 = (eval(input("enter the second number :")))
    
    if (select==1):
        result = (Num1 + Num2)
    elif (select==2):
        result = (Num1 - Num2)
    elif (select==3):
        result = (Num1 * Num2)
    elif (select==4):
        result = (Num1 // Num2)
    elif (select==5):
        result = ((Num1 + Num2)/2)

else:
    print ("not valid")

print("the result of the operation is {}".format(result))
print("thank you for using")














