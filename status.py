import time,vk_api,datetime,init,colorama
from vk_api.longpoll import VkLongPoll, VkEventType, datetime
from colorama import Fore, Back, Style
priva = [
"""


████─█─█─███─████─────███─███─████─███─█─█─███
█──█─█─█──█──█──█─────█────█──█──█──█──█─█─█
████─█─█──█──█──█─███─███──█──████──█──█─█─███
█──█─█─█──█──█──█───────█──█──█──█──█──█─█───█
█──█─███──█──████─────███──█──█──█──█──███─███


"""
]
colorama.init()


priva2 = Fore.RED + 'Создатель: Chmotie\nВерсия: 1.0'
vibor = Fore.RED + '1.Включить Авто-Статус\n2.Инструкция\n3.Возможные ошибки\n4.В разработке...'
print(Fore.GREEN + priva[0])
print(Style.RESET_ALL)
print("-" * 120)
print(priva2)
print(vibor)
print(Style.RESET_ALL)
print("-" * 120)
xz = input("->")

if xz == "1":
    token = input("Введите токен:") 
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    while True:
      try:  	
          print(Fore.YELLOW + "Что бы включить Авто-Статус, надо ввести токен!\nP.S восле того как ввели, надо подождать 60 сек.")
          time.sleep(60)
          vk.account.setOnline(voip=0)
          account = vk.account.getBanned()
          getBan = account['count']
          getOnline = len(vk.friends.getOnline())
          stats = "✅ Only Online | 👥 Друзья онлайн: " + str(getOnline) + " | 🚫 ЧС: " + str(getBan) + " | ⌚ Время " + str(datetime.strftime(datetime.now(), "%D, %H:%M"))
          vk.status.set(text=stats)
          print("Авто-Статус успешно включён!")
      except vk_api.exceptions.Captcha as captcha:
          continue
