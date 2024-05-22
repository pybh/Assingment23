strr=str(input("enter a string :"))
if len(strr)==3:
  x=list(strr)
  x.append("ing")
  strr="".join(x)
  print(strr)
elif (strr[::-1]):
      x=strr.replace("ing","ly")
      print(x)  
elif (strr <3):
    print(strr)