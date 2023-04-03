num1 = 42 #variable declaration,  Numbers
num2 = 2.3 #variable declaration, Numbers
boolean = True #variable declaration, Boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list,
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary,
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize Tuples
print(type(fruit)) #type check Tuples, log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #List add value
print(person['name'])#Dictionary access value
person['name'] = 'George' #Dictionary change value
person['eye_color'] = 'blue' #Dictionary add value
print(fruit[2])#log statement

if num1 > 45: #conditional if
    print("It's greater") #log statement
else: #conditional else
    print("It's lower") #log statement

if len(string) < 5: #conditional if,length check
    print("It's a short word!") #log statement
elif len(string) > 15: #conditional else if,length check
    print("It's a long word!") #log statement
else: #conditional else
    print("Just right!") #log statement

for x in range(5):#for loop,
    print(x)#log statement
for x in range(2,5):#for loop, start at 2, stop at 5
    print(x)#log statement
for x in range(2,10,3):#for loop,start at 2, stop at 10, increment of 3
    print(x)#log statement
x = 0 #variable declaration,  Numbers
while(x < 5): #while loop, start at x, end if x = 5, 
    print(x)
    x += 1

pizza_toppings.pop()#list delete value
pizza_toppings.pop(1)#list delete value at index 1 or 'Sausage'

print(person)# dictionary access value
person.pop('eye_color')#Dictionary delete value
print(person)# dictionary access value

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni':#conditional if
        continue #continue
    print('After 1st if statement')#log
    if topping == 'Olives':#conditional if
        break #break

def print_hello_ten_times():#function
    for num in range(10):#for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)