cust = input("Customer   : ")
cont = int(input("Contact No : "))
time = input("Time       : ")
addr = input("Address    : ")
print("\n")

item=[]
price=[]
qty=[]

def Order ():
    if len(item)<= 0:
        print("Belum Ada Pesanan")
        print("\n")
    else:
        print("\n")
        print("Here's Ur Order :")
        for i in range(len(item)):
            print("[%d] %s"%(i+1,item[i]))
        for i in range(len(qty)):
            print("[%d] %s"%(i+1,qty[i]))
        for i in range(len(price)):
            print("[%d] %s"%(i+1,price[i]))
    print("\n")
    menu()

            
def Brownies ():
    print("\n")
    print("~Brownies~")
    print("1. Classic European Brownie")
    print("2. Chocolate Swirl Cheesecake Brownie")
    print("3. Smores Brownie")
    print("4. Back Menu")
    x=int(input("Choose Ur Brownies :"))
    if x == 1:
        print("\n")
        item.append("Classic European Brownie")
        print("~Classic European Brownie~")
        print("Fudgy Chocolate Brownie with mixes of European Chocolate")
        print("1 Box = 16 pcs = 160 IDR")
        y=int(input("Jumlah Qty :"))
        qty.append(y)
        harga= 160
        h= 160*y
        print("Harga :",h,"IDR")
        price.append(harga)
        print("\n")
        Brownies()

        
    elif x == 2:
        print("\n")
        item.append("Chocolate Swirl Cheesecake Brownie")
        print("~Chocolate Swirl Cheesecake Brownie~")
        print("Buttery Biscuit base and Cheesecake layers compliment Brownie in a sweet and salty feeling.")
        print("1 Box = 16 pcs = 240 IDR")
        y=int(input("Jumlah Qty :"))
        qty.append(y)
        harga= 240
        h= 240*y
        print("Harga :",h,"IDR")
        price.append(harga)
        print("\n")
        Brownies()
        
    elif x == 3:
        print("\n")
        item.append("Smores Brownie")
        print("~Smores Brownie~")
        print("Bringing you treat from the USA. Campfire S'mores inspired us to create S'mores but in a Brownie form.")
        print("1 Box = 16 pcs = 200 IDR")
        y=int(input("Jumlah Qty :"))
        qty.append(y)
        harga= 200
        h= 200*y
        print("Harga :",h,"IDR")
        price.append(harga)
        print("\n")
        Brownies()
        
    elif x == 4:
        print("\n")
        menu()

    else:
        print("Ooops !!! The Number U choese Doesn't Exist")
        Brownies()

        
def Cookies ():
    print("\n")
    print("~Cookies~")
    print("1. Amour Cookies")
    print("2. Dark Amour Cookies")
    print("3. Back Menu")
    
    x=int(input("Choose Ur Cookies :"))
    if x == 1:
        print("\n")
        item.append("Amour Cookies")
        print("~Amour Cookies~")
        print("Cookie dough with generous amount of semi-sweet and bittersweet chocolate folded inside")
        print("1 pcs = 12 IDR")
        y=int(input("Jumlah Qty :"))
        qty.append(y)
        harga= 12
        h= 12*y
        print("Harga :",h,"IDR")
        price.append(harga)
        print("\n")
        Cookies()
        
    elif x == 2:
        print("\n")
        item.append("Dark Amour Cookies")
        print("~Dark Amour Cookies~")
        print("Cookie dough with generous amount of semi-sweet and bittersweet chocolate folded inside and typical taste is a little bitter")
        print("1 pcs = 14 IDR")
        y=int(input("Jumlah Qty :"))
        qty.append(y)
        harga= 14
        h= 14*y
        print("Harga :",h,"IDR")
        price.append(harga)
        print("\n")
        Cookies()
        
    elif x == 3:
        print("\n")
        menu()

    else:
        print("Ooops !!! The Number U choese Doesn't Exist")
        Cookies()

        
def Tea ():
    print("\n")
    print("~Tea~")
    print("1. Chamomile")
    print("2. Peppermint")
    print("3. English Black")
    print("4. Back Menu")
    
    x=int(input("Choose Ur Tea :"))
    if x == 1:
        print("\n")
        item.append("Chamomile")
        print("~Chamomile~")
        print("Scothing and Calming Tea.")
        print("1 cup = 22 IDR")
        y=int(input("Jumlah Qty :"))
        qty.append(y)
        harga= 22
        h= 22*y
        print("Harga :",h,"IDR")
        price.append(harga)
        print("\n")
        Tea()
        
    elif x == 2:
        print("\n")
        item.append("Peppermint")
        print("~Peppermint~")
        print("Cool and Refreshing Tea.")
        print("1 cup = 20 IDR")
        y=int(input("Jumlah Qty :"))
        qty.append(y)
        harga= 20
        h= 20*y
        print("Harga :",h,"IDR")
        price.append(harga)
        print("\n")
        Tea()
        
    elif x == 3:
        print("\n")
        item.append("English Black")
        print("~English Black~")
        print("Traditional Black Tea Blend.")
        print("1 cup = 25 IDR")
        y=int(input("Jumlah Qty :"))
        qty.append(y)
        harga= 25
        h= 25*y
        print("Harga :",h,"IDR")
        price.append(harga)
        print("\n")
        Tea()
        
    elif x == 4:
        print("\n")
        menu()

    else:
        print("Ooops !!! The Number U choese Doesn't Exist")
        Tea()

        
def Quit ():
    quit=input("Apakah Anda Sudah Mau Bayar ? [Y/N] :")
    print("\n")
    if quit == "Y":
        struk()
    elif quit == "N":
        menu()
    else:
        Quit()
        
def struk ():
    print("                     ~~~AMOUREUX PATISSERIE~~~                    ")
    print("                **WE WANT YOU TO TASTE LUXURY HERE**              ")
    print("                              MEDAN                               ")
    print("HP/WA          : 085922877651")
    print("Line           : amoureuxpatisserie")
    print("Instagram      : @amoureuxpatisserie")
    print("NB             : ORDER 2 DAYS PRIOR TO DELIVERY")
    print("Customer       :",cust)
    print("Contact No     :",cont)
    print("Time           :",time)
    print("Address        :",addr)
    print("------------------------------------------------------------------")
    print("|    ITEM     |      PRICE    |       QTY       |      TOTAL     |")
    print("------------------------------------------------------------------")
    total=0
    QTY=0
    for i in range(len(item)):
        print("|",item[i],"|",price[i],"|",qty[i],"|",price[i]*qty[i],"|")
        total += price[i]*qty[i]
    print("------------------------------------------------------------------")
    print("Total          :",total,"IDR")
    cash=int(input("Cash           : "))
    ChangeB = cash-total
    print("Change Back    :",ChangeB,"IDR")
    print("==================================================================")
    for i in range(len(item)):
        QTY += qty[i]
    print("Total Quantity : ",QTY)
    print("==================================================================")
    print("Thank You For Shopping with US! HAVE A GOOD DAY")
    False;
    



def menu ():
    print ("Menu :       ")
    print ("1. Brownies  ")
    print ("2. Cookies   ")
    print ("3. Tea       ")
    print ("4. Quit      ")
    print ("5. Order   ")
    print ("\n")
    pilih =int(input("Choose Ur Menu :"))
    if pilih == 1:
        Brownies()
    elif pilih == 2:
        Cookies()
    elif pilih == 3:
        Tea()
    elif pilih == 4:
        Quit()
    elif pilih == 5:
        Order()
    else:
        print("Ooops !!! The Number U choese Doesn't Exist")
        print("\n")
        menu()
    
Cek = True
while (Cek): 
    menu()
    Cek = False
