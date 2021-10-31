# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:50:03 2021

@author: ИнтелАв
"""

#lesson_3

#Задание 1

def dev(delimoe, delitel):
    return delimoe/delitel if delitel != 0 else "Нельзя делить на 0"

delimoe = int(input("Введите делимое: "))
delitel = int(input("Введите делитель: "))

print("Результат деления: {0}".format(dev(delimoe, delitel)))


#Задание 2

def UserData(Name = "", Family = "", Birthday = "", LiveSity = "", email = "", telephone = ""):
    print("Name = {0}, Family = {1}, Birthday = {2}, LiveSity = {3}, email = {4}, telephone = {5}".format(Name, Family, Birthday, LiveSity, email, telephone))
    
UserData(email = "1@1.ru", Name = "Имя", Family = "Фамилия", Birthday = "2020", LiveSity = "Москва",  telephone = "89675655452")

#Задание 3
def my_func(num1, num2, num3):
    return num1 + num2 + num3 - min(num1, num2, num3)

print(my_func(5, 9, 7))

#Задание 4
def my_func1(x, y):
    return x**y
def my_func2(x, y):
    result = 1
    for i in range(0, y):
        result *= x    
    return result
print(my_func1(5, 4))
print(my_func2(5, 4))

#Задание 5
def addcount(Count):
    return  sum(map(int, Count))    

summa = 0
last = 0
while last != "end":
    Count = input("Введите числе через пробел, для окончания ввода последним введите 'end': ").split()
    if Count[len(Count)-1] == "end":
        last = "end"
        Count.remove("end")
    summa += addcount(Count) 
    print("Сумма {0}".format(summa))     
    
#Задание 6
def int_func(string):
    return string.capitalize()

print(int_func(input("Введите слово: ")))
    
  
Predlojenie = int_func(input("Введите предложение: ")).split()
summa = ""
for i in range(0, len(Predlojenie)):
    summa += " " + int_func(Predlojenie[i]) 
print(summa)    
    
    
    
    
    
    