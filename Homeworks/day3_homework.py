#!/usr/bin/env python
# coding: utf-8

# In[15]:


# DAY3 HOMEWORK

midterm1=int(input("Lütfen 1. öğrenci için arasınav notunu giriniz: "))
final1=  int(input("Lütfen 1. öğrenci için final notunu giriniz: "))
hw1=     int(input("Lütfen 1. öğrenci için ödev notunu giriniz: "))

midterm2=int(input("Lütfen 2. öğrenci için arasınav notunu giriniz: "))
final2=  int(input("Lütfen 2. öğrenci için final notunu giriniz: "))
hw2=     int(input("Lütfen 2. öğrenci için ödev notunu giriniz: "))

midterm3=int(input("Lütfen 3. öğrenci için arasınav notunu giriniz: "))
final3=  int(input("Lütfen 3. öğrenci için final notunu giriniz: "))
hw3=     int(input("Lütfen 3. öğrenci için ödev notunu giriniz: "))

midterm4=int(input("Lütfen 4. öğrenci için arasınav notunu giriniz: "))
final4=  int(input("Lütfen 4. öğrenci için final notunu giriniz: "))
hw4=     int(input("Lütfen 4. öğrenci için ödev notunu giriniz: "))

midterm5=int(input("Lütfen 5. öğrenci için arasınav notunu giriniz: "))
final5=  int(input("Lütfen 5. öğrenci için final notunu giriniz: "))
hw5=     int(input("Lütfen 5. öğrenci için ödev notunu giriniz: "))

isim1=input("Lütfen 1. Öğrenci İçin Ad Soyad Giriniz: ")
isim2=input("Lütfen 2. Öğrenci İçin Ad Soyad Giriniz: ")
isim3=input("Lütfen 3. Öğrenci İçin Ad Soyad Giriniz: ")
isim4=input("Lütfen 4. Öğrenci İçin Ad Soyad Giriniz: ")
isim5=input("Lütfen 5. Öğrenci İçin Ad Soyad Giriniz: ")
          
#list1 = [midterm1,final1,hw1,midterm2,final2,hw2,midterm3,final3,hw3,midterm4,final4,hw4,midterm5,final5,hw5]
#list2= [isim1,isim2,isim3,isim4,isim5]

info = { 'isim1' : {'midterm1': midterm1, 'final1': final1, 'hw1': hw1},'isim2' : {'midterm2': midterm2, 'final2': final2, 'hw2': hw2},'isim3' : {'midterm3': midterm3, 'final3': final3, 'hw3': hw3},'isim4' : {'midterm4': midterm4, 'final4': final4, 'hw4': hw4},'isim5' : {'midterm5': midterm5, 'final5': final5, 'hw5': hw5}}

#dectionary içinden bilgi almak için örneğin;  info['isim1']['final1']

ort1=(midterm1+final1+hw1)/3
ort2=(midterm2+final2+hw2)/3
ort3=(midterm3+final3+hw3)/3
ort4=(midterm4+final4+hw4)/3
ort5=(midterm5+final5+hw5)/3

lst=[ort1,ort2,ort3,ort4,ort5]

if max(lst)==ort1:
    print("Tebrikler En Yüksek Not Ortalamasına Sahip Olan Öğrencisiniz!", isim1)
if max(lst)==ort2:
    print("Tebrikler En Yüksek Not Ortalamasına Sahip Olan Öğrencisiniz!", isim2)
if max(lst)==ort3:
    print("Tebrikler En Yüksek Not Ortalamasına Sahip Olan Öğrencisiniz!", isim3)
if max(lst)==ort4:
    print("Tebrikler En Yüksek Not Ortalamasına Sahip Olan Öğrencisiniz!", isim4)
if max(lst)==ort5:
    print("Tebrikler En Yüksek Not Ortalamasına Sahip Olan Öğrencisiniz!", isim5)







