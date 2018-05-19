c=input('''press one number 
1 for add ,
2 for subtract, 
3 for multiply, 
4 for divide
 ''')
a=int(input("\n\n press enter first number"))
b=int(input("\n\n press enter second number"))
if c == '1':
     print(a+b)
	 
elif c == '2':
   print(a-b)
   
elif c == '3':
    print(a*b)
	
elif c == '4':
    print(a/b)
	
else:
    print("ok")
	