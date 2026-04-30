menu = {"pizza": 22.0,
        "burger":32.0,
        "chips":22.0,
        "fries":12.0,
        "soda":10.0}
cart=[]
total=0

print("--------menu--------")
for key,value in menu.items():
    print(f"{key}: ${value:.2f}")
print("--------------------")

while True:
    food=input("select an item(q to quite):").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------your order-----")
for food in cart:
   total+= menu.get(food)
   print(food,end=" ")
  
print()
print(f"total is: ${total:.2f}")