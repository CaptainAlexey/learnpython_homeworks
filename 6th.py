def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    
    except TypeError:
        print("Должно быть минимум 2 и не больше 3-х аргументов")
    except ValueError:
        print("В функцию можно передать только числовые значения.")

discounted("ff", 4)