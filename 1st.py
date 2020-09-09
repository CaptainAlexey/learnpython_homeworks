def life_answer(age):
    if 1 < age < 7:
        return "Вы еще ребенок. Вы должны быть в детском саду."
    elif 7 <= age < 18:
        return "Вы школьник. Вы должны быть в школе."
    elif 18 <= age < 24:
        return "Вы студент. Вы должны быть в ВУЗе."
    else:
        return "Вы прошли все подготовительные этапы. Вы должны работать."


user_age = int(input("Введите ваш возраст: "))
your_destination = life_answer(user_age)
print(your_destination)