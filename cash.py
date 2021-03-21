try:
    amount = input("Enter the amount:")
    amount = float(amount)
except:  
    amount = input("Enter the amount:")
    amount = float(amount)


#Coin Values    
coinsUsed = 0
quarter = 0.25
dime = .10
nickel = .05
penny = .01



#Input Checking
numDecimals = 0
stringAmount = str(amount)
for i in stringAmount:
    if "." in i:
        numDecimals = numDecimals +1

while numDecimals > 1:
    amount = input("Enter the amount:")
    amount = float(amount)  

while amount < 0:
    amount = input("Enter the amount:")
    amount = float(amount)



#Quarter
while amount >= quarter:
    amount = amount - quarter
    coinsUsed = coinsUsed+1
amount = round(amount,2)

#Dime
while amount < quarter and amount >= dime:
    amount = amount - dime
    round(amount)
    coinsUsed = coinsUsed +1
amount = round(amount,2)

#Nickel
while amount < dime and amount >= nickel:
    amount = amount - nickel
    round(amount)
    coinsUsed = coinsUsed +1
amount = round(amount,2)

#Penny
while amount < nickel and amount >= 0.01:
    amount = amount - penny
    coinsUsed = coinsUsed +1
amount = round(amount,2)

    
if amount == 0.01:
    amount = amount - penny
    coinsUsed = coinsUsed +1



print(coinsUsed, "coins were used")





