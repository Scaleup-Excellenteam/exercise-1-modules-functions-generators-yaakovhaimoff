def get_recipe_price(prices, optionals, *ingredients):
    # Loop through the items (key-value pairs) of the dictionary
    price, i = 0, 0
    for key, value in prices.items():
        if key in optionals:
            continue
        else:
            price += value * ingredients[i]
        i += 1
    print(int(price/100))


if __name__ == '__main__':
    optionals = []
    chocolate, milk = 200, 100
    get_recipe_price({'chocolate': 18, 'milk': 8}, optionals, chocolate, milk)
    optionals = ['milk']
    chocolate = 300
    get_recipe_price({'chocolate': 18, 'milk': 8}, optionals, chocolate)
    get_recipe_price({}, [])
