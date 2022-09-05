"""Berilgan son bo`yicha faktorial
hisoblovchi dastur
Tuzuvchi: Mukhtorjon Tuychiev
Sana: 05.09.2022 yil"""
def faktorial(n):
   m=1
   for i in range(1,n+1):
       m*=i
   return m
   
n=int(input("Enter number: "))
print(f"{n}!={faktorial(n)}")
