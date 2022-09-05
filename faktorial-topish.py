"""Berilgan son bo`yicha faktorial
hisoblovchi dastur
Tuzuvchi: Mukhtorjon Tuychiev
Sana: 05.09.2022 yil"""
def faktorial(n):
   sonlar=[]
   m=1
   kupaytma=1
   while m<=n:
        sonlar.append(m)
        m+=1        
   for son in sonlar:
       kupaytma*=son
   return kupaytma
   
n=int(input("Faktoral uchun son kiriting: "))
print(f"{n}!={faktorial(n)}")
