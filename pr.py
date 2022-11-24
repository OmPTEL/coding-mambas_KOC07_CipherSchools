print("WELCOME TO CURRENCY CONVERTER WHERE YOU CAN CONVERT YOUR DESIRED CURRENCY INTO OTHER CURRENCYS'S\n")

print("Enter the following currency from the below list as shown\n"
      "1.indianrupee\n"
      "2.usdollars\n"
      "3.euros\n"
      "4.canadiandollars\n"
      "5.pounds\n"
      "6.chineseyuan\n"
      "7.russiaruble\n")

print("NOTE:- enter the currency in words as shown above not the numbers\n")



a=str(input("Enter the currency you want to convert: "))
b=float(input("Enter the amount you want to convert: "))


#converison rate for indian rupee
pounds=97.40
euros=84.42
usdollars=81.81
canadiandollars=61.10
chineseyuan=11.43
russiaruble=1.35

if(a=="indianrupee"):
    print("Pounds=","{:.2f}".format(b*pounds),"£")
    print("Euros=","{:.2f}".format(b*euros),"€")
    print("US Dollars=","{:.2f}".format(b*usdollars),"$")
    print("Canadian Dollars=","{:.2f}".format(b*canadiandollars),"$")
    print("Chinese Yuan=","{:.2f}".format(b*chineseyuan),"¥")
    print("Russian Ruble=","{:.2f}".format(b*russiaruble),"₽")


#conversion rate for us dollars
indianrupee1=81.81
euros1=0.97
pounds1=0.85
canadiandollars1=1.337505
chineseyuan1=7.16542
russiaruble1=60.54

if(a=="usdollars"):
    print("Indian Rupee=","{:.2f}".format(b*indianrupee1),"₹")
    print("Euros=","{:.2f}".format(b*euros1),"€")
    print("Pounds=","{:.2f}".format(b*pounds1),"£")
    print("Canadian Dollars=","{:.2f}".format(b*canadiandollars1),"$")
    print("Chinese yuan=","{:.2f}".format(b*chineseyuan1),"¥")
    print("Russian Ruble=","{:.2f}".format(b*russiaruble1),"₽")

#converison rate for euros
indianrupee2=84.37
usdollars2=1.03
canadiandollars2=1.38
chineseyuan2=7.38
russiaruble2=62.82
pounds2=0.87

if(a=="euros"):
    print("Indian Rupee=","{:.2f}".format(b*indianrupee2),"₹")
    print("Pounds=","{:.2f}".format(b*pounds2),"£")
    print("US Dollars=","{:.2f}".format(b*usdollars2),"$")
    print("Canadian Dollars=","{:.2f}".format(b*canadiandollars2),"$")
    print("Chinese yuan=","{:.2f}".format(b*chineseyuan2),"¥")
    print("Russian Ruble=","{:.2f}".format(b*russiaruble2),"₽")


#conersion rate for pounds
indianrupee3=97.47
usdollars3=1.19
canadiandollars3=1.60
chineseyuan3=8.52
russiaruble3=72.10
euros3=1.16

if(a=="pounds"):
    print("Indian Rupee=","{:.2f}".format(b*indianrupee3),"₹")
    print("Euros=","{:.2f}".format(b*euros3),"€")
    print("US Dollars=","{:.2f}".format(b*usdollars3),"$")
    print("Canadian Dollars=","{:.2f}".format(b*canadiandollars3),"$")
    print("Chinese yuan=","{:.2f}".format(b*chineseyuan3),"¥")
    print("Russian Ruble=","{:.2f}".format(b*russiaruble3),"₽")


#conersion rate for canadian dollars
indianrupee4=61.08
usdollars4=0.75
pounds4=0.63
chineseyuan4=5.34
russiaruble4=45.18
euros4=0.72

if(a=="canadiandollars"):
    print("Indian Rupee=","{:.2f}".format(b*indianrupee4),"₹")
    print("Euros=","{:.2f}".format(b*euros4),"€")
    print("US Dollars=","{:.2f}".format(b*usdollars4),"$")
    print("Pounds=","{:.2f}".format(b*pounds4),"£")
    print("Chinese yuan=","{:.2f}".format(b*chineseyuan4),"¥")
    print("Russian Ruble=","{:.2f}".format(b*russiaruble4),"₽")


#conersion rate for chineseyuan
indianrupee5=11.44
usdollars5=0.14
pounds5=0.12
canadiandollars5=0.19
russiaruble5=8.485081
euros5=0.187111

if(a=="chineseyuan"):
    print("Indian Rupee=","{:.2f}".format(b*indianrupee5),"₹")
    print("Euros=","{:.2f}".format(b*euros5),"€")
    print("US Dollars=","{:.2f}".format(b*usdollars5),"$")
    print("Pounds=","{:.2f}".format(b*pounds5),"£")
    print("Canadian Dollars=","{:.2f}".format(b*canadiandollars5),"$")
    print("Russian Ruble=","{:.2f}".format(b*russiaruble5),"₽")

#conversion rate for ruusain ruble
indianrupee6=1.35
usdollars6=0.017
pounds6=0.014
canadiandollars6=0.022
chineseyuan6=0.12
euros6=0.016

if(a=="russiaruble"):
    print("Indian Rupee=","{:.2f}".format(b*indianrupee6),"₹")
    print("Euros=","{:.2f}".format(b*euros6),"€")
    print("US Dollars=","{:.2f}".format(b*usdollars6),"$")
    print("Pounds=","{:.2f}".format(b*pounds6),"£")
    print("Canadian Dollars=","{:.2f}".format(b*canadiandollars6),"$")
    print("Chinese Yuan=","{:.2f}".format(b*chineseyuan6),"¥")
