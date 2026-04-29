email= input("enter the email: ")

index = email.index("@")
username =email[:index]
domain = email[index:]
print(f" your username is {username} and domain is {domain} ")
