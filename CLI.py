import mysql.connector as ms
db=ms.connect(host="localhost",user="root",passwd="admin",database="onlineretail")

cursor = db.cursor()

def place_order():
    while(True):
        print()
        print("1. Increase quantity of existing product")
        print("2. Add new Product")
        print("3. Return")
        ch=int(input())
        if(ch==1):
            print("\nEnter Product_ID:")
            pid=int(input())
            print("Enter new quantity:")
            q=int(input())
            cursor.execute(f"update inventory set Quantity = {q} where Product_ID={pid};")
            print("\n\nUPDATED\n\n")
        elif(ch==2):
            print("Enter product ID: ")
            pid=int(input())
            print("Enter quantity:")
            q=int(input())
            cursor.execute(f"insert into inventory(Product_ID, Quantity) values ({pid},{q})")
            print("\n\nUPDATED\n\n")
        elif(ch==3):
            return


def Add_product():
    while(True):
        print()
        print("1. Increase quantity of existing product")
        print("2. Add new Product")
        print("3. Return")
        ch=int(input())
        if(ch==1):
            print("\nEnter Product_ID:")
            pid=int(input())
            print("Enter new quantity:")
            q=int(input())
            cursor.execute(f"update inventory set Quantity = {q} where Product_ID={pid};")
            print("\n\nUPDATED\n\n")
        elif(ch==2):
            print("Enter product ID: ")
            pid=int(input())
            print("Enter quantity:")
            q=int(input())
            cursor.execute(f"insert into inventory(Product_ID, Quantity) values ({pid},{q})")
            print("\n\nUPDATED\n\n")
        elif(ch==3):
            return


def revenue():
    #total revenue between time periods
    while(True):
        print()
        print("1. See total Revenue")
        print("2. See revenue from a specific customer")
        print("3. return")
        ch=int(input())
        if(ch==1):
            cursor.execute("select SUM(Amount) from orders")
            out=cursor.fetchall()
            print("Total revenue: ")
            for i in out:
                print(*i)
        elif(ch==2):
            print("Enter Customer ID: ")
            cid=int(input())
            cursor.execute(f"select SUM(Amount) from orders where Customer_ID={cid}")
            out=cursor.fetchall()
            if(len(out)==0):
                print("No order placed from The given customer")
                return
            print(f"Total revenue from customer:{cid}: ")
            for i in out:
                print(*i)
        elif(ch==3):
            return
        else:
            print("\nWrong Choice\n\n")

    out=cursor.fetchall()
    for i in out:
        print(*i)

def inventory():
    #inventory print
    while(True):
        print()
        print("1. See Total inventory")
        print("2. See inventory for a Specific product")
        print("3. Return")
        ch=int(input())
        if(ch==1):
            cursor.execute("select * from inventory")
            out=cursor.fetchall()
            print("Product_ID  Quantity")
            for i in out:
                print(*i)
        elif(ch==2):
            print("Enter Product ID: ")
            pid=int(input())
            cursor.execute(f"select * from inventory where Product_ID={pid}")
            out=cursor.fetchall()
            if(len(out)==0 or out[0][0]=="None"):
                print("\nNo such Product found\n")
                return
            print(f"Quantity of product {pid}: ")
            for i in out:
                print(*i)
        elif(ch==3):
            return
        else:
            print("\nWrong Choice\n\n")


def del_agents():
   while(True):
        print("1. See all delivery agents")
        print("2. See delivery agent for a specific order")
        ch=int(input())
        if(ch==1):
            cursor.execute("select * from agents")
            out=cursor.fetchall()
            print("Agent_ID  Contact_number Oder_ID")
            for i in out:
                print(*i)
        elif(ch==2):
            print("Enter order ID:")
            oid=int(input())
            cursor.execute(f"select Agent_ID, Contact_Number from agents where Order_ID={oid}")
            out=cursor.fetchall()
            if(len(out)==0 or out[0][0]=="None"):
                print("No such delivery Agents found")
                return
            print("Agent_ID  Contact_number")
            for i in out:
                print(*i)
        elif(ch==3):
            return
        else:
            print("\nWrong choice\n")


def list_of_dist():
    while(True):
        print("1. See all Distributors")
        print("2. See Distributors for a specific product")
        ch=int(input())
        if(ch==1):
            cursor.execute("select * from distributors")
            out=cursor.fetchall()
            print("Dist_ID  Location  Email")
            for i in out:
                print(*i)
        elif(ch==2):
            print("Enter product ID:")
            pid=int(input())
            cursor.execute(f"select * from distributors as d join distributors_products as dp on dp.distributor_ID=d.distributor_ID where dp.product_ID={pid}")
            out=cursor.fetchall()
            if(len(out)==0 or out[0][0]=="None"):
                print("No such Distributors found")
                return
            print("Dist_ID  Location  Email")
            for i in out:
                print(*i)
        elif(ch==3):
            return
        else:
            print("\nWrong choice\n")

def browse_products(cid):
    cursor.execute("select * from products")
    out=cursor.fetchall()
    print("product_id  product  price")
    for i in out:
        print(*i)
    print("Do you want to add any product to your cart?(y/n)")
    ch=input()
    if(ch=='n' or ch=='N'):
        return
    elif(ch=='y' or ch=='Y'):
        print("\nEnter Product ID: ")
        id=int(input())
        print("Enter The Quantity: ")
        q= int(input())
        cursor.execute(f"insert into cart(Product_ID,Amount,cart_id) values ({id},{q},{cid})")
    else:
        print("Wrong Choice\n")

    #list the products and give option to add to the cart   

def check_cart(cid):
    cursor.execute(f"select Product_ID, Amount from cart where cart_id={cid}")
    out=cursor.fetchall()
    if(len(out)==0):
        print("\nYour Cart is empty!\n\n")
        return
    print("Product_ID Amount")
    for i in out:
        print(*i)
    #print the cart items and give option to place the order and set quantity of item

def order_status(cid):
    cursor.execute(f"select Order_ID, Amount, Order_Date, Delivery_Date from orders where Customer_ID={cid}")
    out=cursor.fetchall()
    if(len(out)==0):
        print("\nNo orders found\n\n")
        return
    print("Order_ID  amount  Order_date  Delivery_date")
    for i in out:
        print(*i)

def customer():
    print()
    print("Enter Customer ID: ")
    cust_ID= int(input())
    print("Enter Password:")
    pswd=input()
    while(True):
        print()
        print("1. Check Cart")
        print("2. Check order status")
        print("3. Browse Products")
        print("4. Place Order")
        print("5. return")
        choice=int(input())
        if(choice==1):
            check_cart(cust_ID)
        elif(choice==2):
            order_status(cust_ID)
        elif(choice==3):
            browse_products(cust_ID)
        elif(choice==4):
            place_order()
        elif(choice==5):
            return
        else:
            print("WRONG CHOICE!\n")
        


def admin():
    while(True):
        print()
        print("1. Check Inventory")
        print("2. See Delivery Agents")
        print("3. See list of Distributors")
        print("4. Check revenue")
        print("5. Add product to inventory")
        print("6. Return")
        choice= int(input())
        if(choice==1):
            inventory()
        elif(choice==2):
            del_agents()
        elif(choice==3):
            list_of_dist()
        elif(choice==4):
            revenue()
        elif(choice==5):
            Add_product()
        elif(choice==6):
            return
        else:
            print("\nWrong Choice\n")

        


def main():
    while(True):
        print("---------------Welcome to Online retail Store---------------")
        print()
        print("1. Login As Admin")
        print("2. Login As Customer")
        print("3. Exit")
        choice=int(input())
        if(choice==1):
            admin()
        elif(choice==2):
            customer()
        elif(choice==3):
            exit()
        else:
            print("WRONG CHOICE!")

main()