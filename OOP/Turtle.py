from turtle import *
from random import randint
from time import *

finish = 200   #РґРёСЃС‚Р°РЅС†РёСЏ РіРѕРЅРєРё

t1=Turtle()  #СЃРѕР·РґР°Р»Рё РѕР±СЉРµРєС‚ РєР»Р°СЃСЃР° С‡РµСЂРµРїР°С…Рё
t1.shape("turtle")  #РїРѕРјРµРЅСЏР»Рё С„Рѕrandint(0,255)СЂРјСѓ РѕР±СЉРµРєС‚Р°
t1.color("red")    #РјРµРЅСЏРµРј С†РІРµС‚ РѕР±СЉРµРєС‚Р°
t1.penup()  #РїРѕРґРЅРёРјР°РµРј С‡РµСЂРµРїР°С€РєСѓ С‡С‚РѕР± РЅРµ СЂРёСЃРѕРІР°Р»Р°
t1.goto (-200,20) #РїРµСЂРµРјРµС‰Р°РµРј С‡РµСЂРµРїР°С€РєСѓ РїРѕ РєРѕРѕСЂРґРёРЅР°С‚Р°Рј
t1.pendown () # РѕРїСѓСЃРєР°РµРј С‡РµСЂРµРїР°С€РєСѓ С‡С‚РѕР± РїРѕС‚РѕРј СЂРёСЃРѕРІР°Р»Р°
t1.speed(3)

t2=Turtle()  #СЃРѕР·РґР°Р»Рё РѕР±СЉРµРєС‚ РєР»Р°СЃСЃР° С‡РµСЂРµРїР°С…Рё
t2.shape("turtle")  #РїРѕРјРµРЅСЏР»Рё С„РѕСЂРјСѓ РѕР±СЉРµРєС‚Р°
t2.color("blue")    #РјРµРЅСЏРµРј С†РІРµС‚ РѕР±СЉРµРєС‚Р°
t2.penup()  #РїРѕРґРЅРёРјР°РµРј С‡РµСЂРµРїР°С€РєСѓ С‡С‚РѕР± РЅРµ СЂРёСЃРѕРІР°Р»Р°
t2.goto (-200,-20) #РїРµСЂРµРјРµС‰Р°РµРј С‡РµСЂРµРїР°С€РєСѓ РїРѕ РєРѕРѕСЂРґРёРЅР°С‚Р°Рј
t2.pendown () # РѕРїСѓСЃРєР°РµРј С‡РµСЂРµРїР°С€РєСѓ С‡С‚РѕР± РїРѕС‚РѕРј
t2.speed(3)

def razmetka():   #С„СѓРЅРєС†РёСЏ СЂРёСЃСѓРµС‚ СЂР°Р·РјРµС‚РєСѓ РїРѕР»РЅСЏ
    t=Turtle()
    t.speed(0)
    for i in range (1,21):
        t.penup()
        t.goto(-200+i*20, 50)
        t.pendown()
        t.goto(-200+i*20, -100)
    t.hideturtle()

razmetka()

def catch1(x,y):   #СЌС‚Рѕ РѕР±СЂР°Р±РѕС‚С‡РёРє СЃРѕР±С‹С‚РёСЏ РЅР°Р¶Р°С‚РёСЏ 
  t1.write('Ouch!', font=('Arial', 14, 'normal'))    #РїРёС€РµРј РЅР° СЌРєСЂР°РЅРµ РђСѓС‡
  t1.fd(randint(10,15))      #С‡РµСЂРµРїР°С€РєР° РґРµР»Р°РµРј СЃР»СѓС‡Р°Р№РЅС‹Р№ С€Р°Рі РѕС‚ 10 РґРѕ 15

t1.onclick(catch1)    #Р·РґРµСЃСЊ СЏ РїСЂРёРєСЂРµРїР»СЏСЋ РѕР±СЂР°Р±РѕС‚С‡РёРє Рє СЃРѕР±С‹С‚РёСЋ РЅР°Р¶Р°С‚РёСЏ РЅР° 1 С‡РµСЂРµРїР°С€РєСѓ

def catch2(x, y):   #СЌС‚Рѕ РѕР±СЂР°Р±РѕС‚С‡РёРє СЃРѕР±С‹С‚РёСЏ РЅР°Р¶Р°С‚РёСЏ 
  t2.write('123',  font=('Arial', 14, 'normal'))    #РїРёС€РµРј РЅР° СЌРєСЂР°РЅРµ РђСѓС‡
  t2.fd(randint(10,15))      #С‡РµСЂРµРїР°С€РєР° РґРµР»Р°РµРј СЃР»СѓС‡Р°Р№РЅС‹Р№ С€Р°Рі РѕС‚ 10 РґРѕ 15

t2.onclick(catch2)    #Р·РґРµСЃСЊ СЏ РїСЂРёРєСЂРµРїР»СЏСЋ РѕР±СЂР°Р±РѕС‚С‡РёРє Рє СЃРѕР±С‹С‚РёСЋ РЅР°Р¶Р°С‚РёСЏ РЅР° 1 С‡РµСЂРµРїР°С€РєСѓ

while t1.xcor()<finish and t2.xcor()<finish:
    t1.forward(randint(2,7))  #Р·РґРµСЃСЊ С‡РµСЂРµРїРµР°С…Р° РґРІРёРіР°РµС‚СЃСЏ РІРїРµСЂРµРґ Рё СЂРёСЃСѓРµС‚ С‚РѕР¶Рµ РЅР° СЃР»СѓС‡Р°Р№РЅРѕРµ С‡РёСЃР»Рѕ РІ РґРёР°РїР°Р·РѕРЅРµ РѕС‚ 2 Рѕ 7
    t2.forward(randint(2,7))
    sleep(0.05)