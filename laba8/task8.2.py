from PIL import Image



holidays = {'Новый год': Image.open('C:/Users/user/Desktop/laba8/новыйгод.jpg'),
            '23 февраля': Image.open('C:/Users/user/Desktop/laba8/23Февраля.jpg'),
            '14 февраля': Image.open('C:/Users/user/Desktop/laba8/14февраля.jpg'), '8 марта': Image.open(
        'C:/Users/user/Desktop/laba8/8марта.jpg'),
            '1 сентября': Image.open('C:/Users/user/Desktop/laba8/1сентября.jpg')}

user = input("Введите праздник ")
for (k, v) in holidays.items():
    if k in user:
        print("Открываю...")
        v.show()



