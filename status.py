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
    print(Fore.YELLOW + "Что бы включить Авто-Статус, надо ввести токен!\nP.S восле того как ввели, надо подождать 60 сек.")
    while True:
      try:  	
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
if xz == "2":
   print(Fore.GREEN + "в этой инструкции расказуется, как взять токен. В этом скрипте нужен только токен.\nчто бы взять токен перейдите, по этой ссылке https://vkhost.github.io/ \n и нажмите на Vk Admin, после разрешите, что просят. (данные никто не украдет)\nПотом скопируйте ссылку от = до &\n Это и будет ваш токен.")
if xz == "3":
   print(Fore.BLUE + "Ошибки могут быть разные, если Авто-Статус не работает, то скорей всего вы ввели не правильный токен. В редких случаях, это капча.")
if xz == "4":
	print("Comming soon...")
else:
   print(Fore.RED + "[!]Выбрана неверная опция.")
