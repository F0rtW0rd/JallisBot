import telebot
import time



bot = telebot.TeleBot("6695149691:AAFKLaL51XbcsMpp-DE_Dw6V9q0VRS7_yrY")

user_id = {}

admins = [1145257758]

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■》》

@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(message.chat.id, 'Привет, для подробной информации о боте напиши /help')

#▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎》
    
    if message.chat.id in user_id:
        if message.chat.username == None:
            if message.chat.last_name == None:
                print(f'Повторный запуск у {message.chat.first_name}')
            else:
                print(f'Повторный запуск у {message.chat.first_name} {message.chat.last_name}')
        else:
            print(f'Повторный запуск у {message.chat.username}')
    else:
        user_id[message.chat.id] = 0
        print(user_id)
        if message.chat.username == None:
            if message.chat.last_name == None:
                print(f'Бот был запущен у {message.chat.first_name}')
            else:
                print(f'Бот был запущен у {message.chat.first_name} {message.chat.last_name}')
        else:
            print(f'Бот был запущен у {message.chat.username}')
        
#▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎》
        
        if message.chat.id in admins:
            pass
        else:
            if message.chat.username == None:
                if message.chat.last_name == None:
                    bot.send_message(admins[0], f'Бот был запущен у {message.chat.first_name}')
                else:
                    bot.send_message(admins[0], f'Бот был запущен у {message.chat.first_name} {message.chat.last_name}\r Новобранец: {message.chat.id}')
            else:
                bot.send_message(admins[0], f'Бот был запущен у {message.chat.username}')
        
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■》》

@bot.message_handler(commands=['help'])

def help(message):
    
    if message.chat.id in user_id:

        bot.send_message(message.chat.id, '*ЗОЛОТОЕ ДНО*', parse_mode = 'Markdown')
        bot.send_message(message.chat.id, '')
        
#▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎》
        
        if message.chat.username == None:
            if message.chat.last_name == None:
                print(f'Информация о боте показана у {message.chat.first_name}')
            else:
                print(f'Информация о боте показана у {message.chat.first_name} {message.chat.last_name}')
        else:
            print(f'Информация о боте показана у {message.chat.username}')
        
        print(f'Информация о боте показана у {message.chat.first_name} {message.chat.last_name}')
    else:
        bot.send_message(message.chat.id, 'Ошибка. попробуйте ещё раз')
        user_id[message.chat.id] = 0
        print(user_id)
    
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■》》

@bot.message_handler(commands=['down'])
def down(message):
    
    if message.chat.id in user_id:

        user_id[message.chat.id] += 1
        
        print(user_id[message.chat.id])
        bot.send_message(message.chat.id, f'Теперь вы находитесь на {user_id[message.chat.id]} уровне под землей!')
        print(f'Уровень повышен у {message.chat.first_name} {message.chat.last_name}')
    else:
        bot.send_message(message.chat.id, 'Ошибка. попробуйте ещё раз')
        user_id[message.chat.id] = 0
        print(user_id)

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■》》

@bot.message_handler(commands=['info'])
def info(message):
    
    if message.chat.id in user_id:
        bot.send_message(message.chat.id, f'Вы находитесь на {user_id[message.chat.id]} уровне под землей!')
        print(f'Уровень {user_id[message.chat.id]} показан у {message.chat.first_name} {message.chat.last_name}')
    else:
        bot.send_message(message.chat.id, 'Ошибка. попробуйте ещё раз')
        user_id[message.chat.id] = 0
        print(user_id)
        
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■》》

@bot.message_handler(commands=['admin'])
def admin(message):
        
        if message.chat.id in user_id:
            if message.chat.id in admins:
                bot.send_message(message.chat.id, f'Id пользователей: {user_id}')
                print('Админ получил информацию о боте')
            else:
                bot.send_message(message.chat.id, 'Ошибка. Вы не являетесь администратором!')
                print(f'{message.chat.id} {message.chat.first_name} {message.chat.last_name} попытка взлома!')
        else:
            bot.send_message(message.chat.id, 'Ошибка. Попробуйте ещё раз')
            user_id[message.chat.id] = 0
            print(user_id)
        
bot.polling(none_stop = True)
