#create a password
password= input("Create a password : ")
x = True 
while x:  
  if (len(password)<8 or len(password)>16): 
    print("Password length between 6 and 12 please")     
    break   
  elif not re.search("[a-z]",password): 
    print("You need at least one lower case letter")
  break
  elif not re.search("[0-9]",password): 
    print("You need at least one number")
    break
  elif not re.search("[A-Z]",password): 
    print("You need at least one upper case character")
    break
  elif not re.search("[$#@]",password): 
    print("You need at least one special character")
    break
  elif re.search("\s",password): 
    print("You cannot have blank spaces in your password...")
    break
else:
    print("Valid Password")
x=False
break