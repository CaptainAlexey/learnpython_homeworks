import random

def ask_user():
    all_question_list = {"Привет":"Привет", "Как дела?":"Хорошо", "Что делаешь?":"Программирую", 
    "Как тебя зовут?":["Алексей", "Михаил", "Дарья", "Маргарита"]}
    
    while True:
        try:
            ask_programm = input("Как дела?: ")

            if ask_programm.capitalize() != "Пока":
                if ask_programm.capitalize() == all_question_list["Как дела?"]:
                    print("Отлично! У меня тоже.")
                    quest_programm = input("У тебя есть вопрос?")
                    if quest_programm.capitalize() == "Да":
                        quest_user = input()
                        quest_user = quest_user.capitalize()
                        if quest_user in all_question_list:
                            if quest_user == "Как тебя зовут?":
                                print(random.choice(all_question_list["Как тебя зовут?"]))
                            else:
                                print(all_question_list[quest_user])
                        else:
                            print("Я не понимаю тебя.")
                    else:
                        print("Пока!")
                        break      
                else:
                    print("У тебя должно быть все хорошо. Давай попробуем еще раз.")
            
            else:
                print("Пока!")
                break
        except KeyboardInterrupt:
            print("Пока!")
            break

ask_user()