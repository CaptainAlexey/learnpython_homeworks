import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime


logging.basicConfig(filename='bot2.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start.')
    update.message.reply_text('Положение какой планеты ты хочешь узнать на данный момент?\
         \n/Mercury \n/Venus \n/Earth \n/Mars \n/Jupiter \n/Saturn \n/Uranus \n/Neptune') 
    update.message.reply_text("Также ты можешь ввести в формате 'planet \"название планеты\"'")      

def planet_coor(update, context):
     
    if update.message.text == "/Mercury":
        date = datetime.date.today()
        coordinates_planet = ephem.Mars(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Venus":
        date = datetime.date.today()
        coordinates_planet = ephem.Venus(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Earth":
        date = datetime.date.today()
        coordinates_planet = ephem.Earth(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Mars":
        date = datetime.date.today()
        coordinates_planet = ephem.Mars(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)    
    elif update.message.text == "/Jupiter":
        date = datetime.date.today()
        coordinates_planet = ephem.Jupiter(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Saturn":
        date = datetime.date.today()
        coordinates_planet = ephem.Saturn(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Uranus":
        date = datetime.date.today()
        coordinates_planet = ephem.Uranus(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    elif update.message.text == "/Neptune":
        date = datetime.date.today()
        coordinates_planet = ephem.Neptune(f'{date}')
        constellation = ephem.constellation(coordinates_planet)
        update.message.reply_text(constellation)
        update.message.reply_text(coordinates_planet)
    else:
        update.message.reply_text("Я не знаю такой планеты")




def name_planet(update, context):
    user_text = update.message.text
    planet = user_text.split()
    if len(planet) < 3:
        planet = planet[-1] 
        date = datetime.date.today()
        if planet == "Mercury":
            date = datetime.date.today()
            coordinates_planet = ephem.Mars(f'{date}')
            constellation = ephem.constellation(coordinates_planet)
            update.message.reply_text(constellation)
            update.message.reply_text(coordinates_planet)
        elif planet == "Venus":
            date = datetime.date.today()
            coordinates_planet = ephem.Venus(f'{date}')
            constellation = ephem.constellation(coordinates_planet)
            update.message.reply_text(constellation)
            update.message.reply_text(coordinates_planet)
        elif planet == "Earth":
            date = datetime.date.today()
            coordinates_planet = ephem.Earth(f'{date}')
            constellation = ephem.constellation(coordinates_planet)
            update.message.reply_text(constellation)
            update.message.reply_text(coordinates_planet)
        elif planet == "Mars":
            date = datetime.date.today()
            coordinates_planet = ephem.Mars(f'{date}')
            constellation = ephem.constellation(coordinates_planet)
            update.message.reply_text(constellation)
            update.message.reply_text(coordinates_planet)    
        elif planet == "Jupiter":
            date = datetime.date.today()
            coordinates_planet = ephem.Jupiter(f'{date}')
            constellation = ephem.constellation(coordinates_planet)
            update.message.reply_text(constellation)
            update.message.reply_text(coordinates_planet)
        elif planet == "Saturn":
            date = datetime.date.today()
            coordinates_planet = ephem.Saturn(f'{date}')
            constellation = ephem.constellation(coordinates_planet)
            update.message.reply_text(constellation)
            update.message.reply_text(coordinates_planet)
        elif planet == "Uranus":
            date = datetime.date.today()
            coordinates_planet = ephem.Uranus(f'{date}')
            constellation = ephem.constellation(coordinates_planet)
            update.message.reply_text(constellation)
            update.message.reply_text(coordinates_planet)
        elif planet == "Neptune":
            date = datetime.date.today()
            coordinates_planet = ephem.Neptune(f'{date}')
            constellation = ephem.constellation(coordinates_planet)
            update.message.reply_text(constellation)
            update.message.reply_text(coordinates_planet)
        else:
            update.message.reply_text("Я не знаю такой планеты")
        

    else:
        print("Необходимо ввести в формате 'planet \"название планеты\"'")
        update.message.reply_text("Необходимо ввести в формате 'planet \"название планеты\"'")

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("Mercury", planet_coor))
    dp.add_handler(CommandHandler("Venus", planet_coor))
    dp.add_handler(CommandHandler("Earth", planet_coor))
    dp.add_handler(CommandHandler("Mars", planet_coor))
    dp.add_handler(CommandHandler("Jupiter", planet_coor))
    dp.add_handler(CommandHandler("Saturn", planet_coor))
    dp.add_handler(CommandHandler("Uranus", planet_coor))
    dp.add_handler(CommandHandler("Neptune", planet_coor))
    dp.add_handler(MessageHandler(Filters.text, name_planet))

    logging.info("Бот стартовал")
 
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()