password = input("Enter Password : ").strip()
score = 0
if len(password) > 8:
    score += 1
for i in range(len(password)):
    if password[i].isupper():
        score += 1
        break
        
for i in range(len(password)):
    if password[i].islower():
        score +=1
        break
for i in range(len(password)):
    if password[i].isdigit():
        score +=1
        break
    
for i in range(len(password)):
    if password[i].isupper():
        pass
    elif password[i].islower():
        pass
    elif password[i].isdigit():
        pass
    else:
        score +=1
if score >=4:
    print("Password Is Strong \n")
elif score <= 3:
    print("Password Strength Is Weak \n")
    
    
    

        
    
    