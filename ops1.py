# Arth operators
print(10+2)
print(10/2)
print(10%3)
print(10*2)

# comparesion operators
# ==, !=  < > <= >=

print(10==2)
print(10!=20)
print(20 != 10)
print(10>100)
print(10000<=(-10))
print(10<=100)
print(100>=1000)


# assigemant operators

# assignment operators are used to assign values to variables.
#  The basic assignment operator is the equal sign (=),
#  but there are also compound assignment operators 
# that combine an operation with assignment.     

cartitems=0
cartitems+=1
cartitems =cartitems+1 #1
cartitems = cartitems+2 # 1+2 =3
cartitems=cartitems-1 # 3-1 =2

account_Balance = 5000
acount_Blance = account_Balance+200  # 5200
print(acount_Blance) # 5200

cartitems =0
cartitems+=10
Cartiitems-=5 # 5
cartitems*=10 # 5*10 =50
print(cartitems) # 50

cartitems =10
cartitems%5 # 10 % 5 =0
print(cartitems)


# membership operators

print(10 in [1,2,34,]) # False
print(100 in [100,200,300]) # True
print("v" in "vamsi") # True
print( "id" in {"id":1, "name: "sai"} ) # True
print("1"in [1,2,3]) # False
print( "1"in [1,2,3]) # False
print([1,2] in [1,2,3,4,5,[1,2]]) # True



  print("v" not in "vamsi") # False
  print("1" not in "123vamsi") # False
  print("vamsi" not in "123vamsiEnduri") # False
