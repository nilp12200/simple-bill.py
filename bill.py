y="Grossary bill "
print(y.center(50))
print("-------------------------------------------------")
x=str(input("enter the name of customer "))
print(x.upper())
print("------------------------------------------------ ")

productname=["sugar","salt","oil"]

v=(input("enter the product name "))
print(v.capitalize())
print("------------------------------------------------ ")

i=int(input("quanty of product kg"))
print("------------------------------------------------ ")

if(v==productname[0]):
 b=45*i
 print(b)
 print("------------------------------------------------ ")
  
elif(v==productname[1]):
  b= 10*i
  print(b)
  print("------------------------------------------------ ")
  
  
elif(v==productname[2]):
  b=120 *i 
  print(b)
  print("------------------------------------------------ ")
  
else:
    print("not vailable")
    print("------------------------------------------------ ")
    
    
v=(input("enter the product name "))
print(v.capitalize())
print("------------------------------------------------ |")
i=int(input("quanty of product kg"))
print("------------------------------------------------ ")

if(v==productname[0]):
  c=45*i
  print(c)
  print("------------------------------------------------ ")
  
   
elif(v==productname[1]):
  c= 10*i
  print(c)
  print("------------------------------------------------ ")
  
elif(v==productname[2]):
  c=120 *i 
  print(c)
  print("------------------------------------------------ ")
  
else:
    print("not vailable")    
    print("------------------------------------------------ ")

print(f"       ** PAY THE PAYMENT {x}",b+c ,"RUPEES **")
print("------------------------------------------------ ")


print(f"        🙏🙏 Thank You For Visit Again 🙏🙏")
