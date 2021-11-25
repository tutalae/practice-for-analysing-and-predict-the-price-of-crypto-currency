status = True

print('start : insert money')
product_b = float(input())
print(f'start with {product_b}')
print('start : insert price')
price = float(input())

product_a = product_b/2/price
product_b = product_b/2

print(f'total product_a : {product_a}, total product_b : {product_b}')

percentage = 0.5
minimum_action = 0.05

while status:
    try:
        print('start : insert price')
        price = float(input())

        total = (product_a * price) + product_b
        target = total * percentage

        print(f'port value = {total}, target = {target}')
        target_value = target/price

        if price == -1:
            print('#### input deposite ####')
            deposite = float(input())
            print(f'deposite money = {deposite}')
            product_b += deposite
            print(f'product_a = {product_a}, product_b = {product_b}')

        elif product_a*price > target:
            action = target_value - product_a
            product_a += action
            product_b += -(action*price)

            print(f'sell : pruduct_a {action}, value : {-(action*price)}')
            print(f'product_a = {product_a}, product_b = {product_b}')
        elif product_a*price < target:
            action = target_value - product_a
            product_a += action
            product_b += -(action * price)

            print(f'buy : pruduct_a {action}, value : {-(action * price)}')
            print(f'product_a = {product_a}, product_b = {product_b}')

        elif price == -1:
            deposite = float(input())
            print(f'deposite money = {deposite}')
            product_b += deposite
            print(f'product_a = {product_a}, product_b = {product_b}')

        last_price = price

    except ZeroDivisionError as err:
        print()
        print('#' * 20)
        print('Nobody trade this product, stop program')
        print('#' * 20)
        break