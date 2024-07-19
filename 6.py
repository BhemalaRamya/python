price=int(input("enter the price of a bike:"))
if price>72000 and price<150000:
    tax=(10/100)*price
    insurance=(15/100)*price
elif price>150000 and price<200000:
    tax=(25/100)*price
    insurance=(20/100)*price
elif price>200000:
    tax=(35/100)*price
    insurance=(28/100)*price
else:
    print("minimum bike starts with us from 72000")
print(price+tax+insurance)
