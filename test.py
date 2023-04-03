pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list,
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print(topping)
    print('After 1st if statement')
    if topping == 'Olives':
        break