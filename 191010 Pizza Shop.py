PIZZA SHOP

pizzas = [800, 850, 900]
toppings = [100, 150]
x = 1000


def find_price(pizzas, toppings, x):

    find_closest = []
    absolute_values = []

    for pizza in pizzas:
        #1100
        if pizza == x:
            return pizza

        elif pizza != x:

            difference = x - pizza
            find_closest.append(difference)
            absolute_values.append(abs(difference))
            
            for topping in toppings:
                #100
                if pizza + topping == x:
                    return pizza + topping
                else: 
                    difference = x - pizza - topping
                    find_closest.append(difference)
                    absolute_values.append(abs(difference))
        
        two_values = []
        for value in find_closest:
            if abs(value) == min(absolute_values):
                possible_value = value 
                two_values.append(possible_value)

    return x - max(two_values)
