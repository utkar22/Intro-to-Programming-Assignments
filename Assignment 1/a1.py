'''
Name: Utkarsh Arora
Roll No: 2020143
'''


class Item:
    def __init__(self,code,description,category,cost):
        '''
        Description: Initialisation of class Item.

        Parameters: Item Code, Item Description, Item Category, Item Cost

        Returns: No return value
        '''
        self.code=code
        self.description=description
        self.category=category
        self.cost=cost

def get_items():
    '''
    Description: Creates a list of Items. This can be called any time from any
    function.

    Parameters: No parameters

    Returns: A list of objects of the class Iten
    '''
    
    list_of_items=[]

    list_of_items.append(Item(0,"Tshirt","Apparels",500))
    list_of_items.append(Item(1,"Trousers","Apparels",600))
    list_of_items.append(Item(2,"Scarf","Apparels",250))
    list_of_items.append(Item(3,"Smartphone","Electronics",20000))
    list_of_items.append(Item(4,"iPad","Electronics",30000))
    list_of_items.append(Item(5,"Laptop","Electronics",50000))
    list_of_items.append(Item(6,"Eggs","Eatables",5))
    list_of_items.append(Item(7,"Chocolate","Eatables",10))
    list_of_items.append(Item(8,"Juice","Eatables",100))
    list_of_items.append(Item(9,"Milk","Eatables",45))

    return (list_of_items)

def get_dash():
    '''Returns a dashed line for seperator'''
    return ("-------------------------------------------------")

def get_dash2():
    '''Returns a dashed line with equal to symbol for seperator'''
    return ("=================================================")


def show_menu():
    '''
    Description: Prints the menu as shown in the PDF
	
    Parameters: No paramters
	
    Returns: No return value
    '''

    print (get_dash2())
    print ("MY BAZAAR")
    print (get_dash2())
    print ("Hello! Welcome to my grocery store!")
    print ("Following are the products available in the shop:")
    print ()
    print (get_dash())
    print ("CODE | DESCRIPTION |   CATEGORY   | COST (Rs)")
    print (get_dash())

    list_of_items=get_items()

    for item in list_of_items:
        s=""
        s+=f"  {item.code}  |"
        s+=" "+item.description+(12-len(item.description))*" "+"|"
        s+=" "+item.category+(13-len(item.category))*" "+"|"
        s+=" "+str(item.cost)

        print (s)

    print (get_dash())
    print ()
    

def check_if_bulk():
    '''
    Description: Asks the user if the order is bulk or not.
    Calls the relevant function accordingly.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    while True:
        x=input("Would you like to buy in bulk? (y or Y / n or N): ")

        if x in ("y","Y"):
            bulk=True
            break
        elif x in ("n","N"):
            bulk=False
            break

    print ()

    if bulk:
        return (get_bulk_input())
    else:
        return (get_regular_input())

def get_regular_input():
    '''
    Description: Takes space separated item codes (only integers allowed). 
    Include appropriate print statements to match the output with the 
    screenshot provided in the PDF.
	
    Parameters: No parameters
	
    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i. 
    '''

    print (get_dash())
    print ("ENTER ITEMS YOU WISH TO BUY")
    print (get_dash())

    x=input("Enter the item codes (space-separated): ")
    codes=x.split()

    d=dict()
    for a in range(10):
        d[a]=0

    for b in codes:
        b=int(b)
        if b in range(10):
            d[b]+=1
        else:
            print (f"{b} is an invalid code.")

    l=[]
    for a in range(10):
        l.append(d[a])

    return (l)
        
        

def get_bulk_input():
    '''
    Description: Takes inputs (only integers allowed) from a bulk buyer. 
    For details, refer PDF. Include appropriate print statements to match 
    the output with the screenshot provided in the PDF.
	
    Parameters: No parameters
	
    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''

    list_of_items=get_items()

    print (get_dash())
    print ("ENTER ITEM AND QUANTITIES")
    print (get_dash())

    d=dict()
    for a in range(10):
        d[a]=0

    while True:
        x=input("Enter code and quantity (leave blank to stop): ")
        y=x.split()

        if len(y)==2:
            y[0]=int(y[0])
            y[1]=int(y[1])
            
            if y[0] in range(10):
                if y[1]>0:
                    d[y[0]]+=y[1]
                    print (f"You added {y[1]} {list_of_items[y[0]].description}")
                else:
                    print ("Invalid quantity. Try again.")
            else:
                if y[1]>0:
                    print ("Invalid code. Try again.")
                else:
                    print ("Invalid code and quantity. Try again.")
        elif x=="":
            print ("Your order has been finalized.")
            break

        else:
            print ("Invalid Syntax.")

    l=[]
    for a in range(10):
        l.append(d[a])

    return (l)
                           

def print_order_details(quantities):
    '''
    Description: Prints the details of the order in a manner similar to the
    sample given in PDF.
    
    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    
    Returns: No return value
    '''
    list_of_items=get_items()

    print (get_dash())
    print ("ORDER DETAILS")
    print (get_dash())

    counter=0
    total_cost=0

    for a in range(10):
        if quantities[a]>0:
            counter+=1
            item=list_of_items[a]
            cost=quantities[a]*item.cost

            total_cost+=cost

            print (f"[{counter}] {item.description} * {quantities[a]} = Rs {item.cost} * {quantities[a]} = Rs {cost}")

    print ()
    print (f"TOTAL COST = Rs {total_cost}")
    print ()
    print ()


def calculate_category_wise_cost(quantities):
    '''
    Description: Calculates the category wise cost using the quantities
    provided. Include appropriate print statements to match the output with the
    screenshot provided in the PDF.
    
    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    
    Returns: A 3-tuple of integers in the following format: 
    (apparels_cost, electronics_cost, eatables_cost)
    '''

    list_of_items=get_items()
    

    apparels_cost=0
    for a in range(0,3):
        item=list_of_items[a]
        cost=quantities[a]*item.cost
        apparels_cost+=cost


    electronics_cost=0
    for a in range(3,6):
        item=list_of_items[a]
        cost=quantities[a]*item.cost
        electronics_cost+=cost

    eatables_cost=0
    for a in range(6,10):
        item=list_of_items[a]
        cost=quantities[a]*item.cost
        eatables_cost+=cost

    print (get_dash())
    print ("CATEGORY-WISE COST")
    print (get_dash())

    if apparels_cost:
        print (f"Apparels = Rs {apparels_cost}")
    if electronics_cost:
        print (f"Electronics = Rs {electronics_cost}")
    if eatables_cost:
        print (f"Eatables = Rs {eatables_cost}")

    return ((apparels_cost,electronics_cost,eatables_cost))    


def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS. 
    This function must be used whenever you are calculating discounts.
    
    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the discounted category-wise price, if applicable. 
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.
    
    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'
    
    Returns: A 3-tuple of integers in the following format: 
    (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
    '''

    print (get_dash())
    print ("DISCOUNTS")
    print (get_dash())

    if apparels_cost>=2000:
        discounted_apparels_cost=apparels_cost - get_discount(apparels_cost, 0.1)
        print (f"[APPAREL] Rs {apparels_cost} - Rs {apparels_cost*0.1} = Rs {discounted_apparels_cost}")
    else:
        discounted_apparels_cost=apparels_cost

    if electronics_cost>=25000:
        discounted_electronics_cost=electronics_cost - get_discount(electronics_cost, 0.1)
        print (f"[ELECTRONICS] Rs {electronics_cost} - Rs {electronics_cost*0.1} = Rs {discounted_electronics_cost}")
    else:
        discounted_electronics_cost=electronics_cost

    if eatables_cost>=500:
        discounted_eatables_cost=eatables_cost - get_discount(eatables_cost, 0.1)
        print (f"[EATABLES] Rs {eatables_cost} - Rs {eatables_cost*0.1} = Rs {discounted_eatables_cost}")
    else:
        discounted_eatables_cost=eatables_cost

    return (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)

    


def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS. 
    This function must be used whenever you are calculating discounts.
    
    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax: 	Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the total cost including taxes.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.
    
    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables' 
    
    Returns: A 2-tuple of integers in the following format: 
    (total_cost_including_tax, total_tax)
    '''

    print (get_dash())
    print ("TAX")
    print (get_dash())

    total_tax=0
    total_cost=0

    tax_on_apparels=get_tax(apparels_cost,0.10)
    tax_on_electronics=get_tax(electronics_cost,0.15)
    tax_on_eatables=get_tax(eatables_cost,0.05)

    print (f"[APPAREL] Rs {apparels_cost} * 0.10 = Rs {tax_on_apparels}")
    print (f"[ELECTRONICS] Rs {electronics_cost} * 0.15 = Rs {tax_on_electronics}")
    print (f"[EATABLES] Rs {eatables_cost} * 0.05 = Rs {tax_on_eatables}")

    total_tax=tax_on_apparels + tax_on_electronics + tax_on_eatables
    total_cost=(apparels_cost + electronics_cost + eatables_cost) + total_tax

    print (f"TOTAL TAX = Rs {total_tax}")
    print (f"TOTAL COST = Rs {total_cost}")

    return (total_cost, total_tax)


def apply_coupon_code(total_cost):
    '''
    Description: Takes the coupon code from the user as input (case-sensitive). 
    For details, refer the PDF. Include appropriate print statements to match 
    the output with the screenshot provided in the PDF.
    
    Parameters: The total cost (integer) on which the coupon is to be applied.
    
    Returns: A 2-tuple of integers:
    (total_cost_after_coupon_discount, total_coupon_discount)
    '''

    print (get_dash())
    print ("COUPON CODE")
    print (get_dash())

    discount=0

    while True:
        print ()
        x=input("Enter coupon code (else leave blank): ")

        if x == "HELLE25":
            if total_cost>=25000:
                if total_cost*0.25<5000:
                    discount=total_cost*0.25
                else:
                    discount=5000
            print (f"[HELLE25] min(5000, Rs {total_cost} * 0.25")
            break
        elif x == "CHILL50":
            if total_cost>=50000:
                if total_cost*0.5<10000:
                    discount=total_cost*0.5
                else:
                    discount=10000
            print (f"[CHILL50] min(10000, Rs {total_cost} * 0.5)")
            break

        elif x == "":
            print ("No coupon code applied.")
            break

        else:
            print ("Invalid coupon code. Try again.")

        

    print (f"TOTAL COUPON DISCOUNT = Rs {discount}")
    print (f"TOTAL COST = Rs {total_cost-discount}")
    print ()

    return (total_cost-discount, discount)
        


def main():
    '''
    Description: This is the main function. All production level codes usually
    have this function. This function will call the functions you have written
    above to design the logic. You will see how splitting your code into specialised
    functions makes the code easier to read, write and debug. Include appropriate 
    print statements to match the output with the screenshots provided in the PDF.
    
    Parameters: No parameters
    
    Returns: No return value
    '''
    show_menu()

    quantities=check_if_bulk()
    print_order_details(quantities)

    apparels_cost,electronics_cost,eatables_cost=calculate_category_wise_cost(quantities)
    apparels_cost,electronics_cost,eatables_cost=calculate_discounted_prices(apparels_cost,electronics_cost,eatables_cost)
    total_cost,total_tax=calculate_tax(apparels_cost,electronics_cost,eatables_cost)

    apply_coupon_code(total_cost)

    print ("Thank you for visiting!")

	


if __name__ == '__main__':
    main()
