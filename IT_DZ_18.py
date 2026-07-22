import requests
import json

# data_base = [{
#     'type':'audio',
#     'mark':'SONY',
#     'name':'q-234',
#     'price':10
# }, {
#     'type':'audio',
#     'mark':'SONY',
#     'name':'q-234',
#     'price':10
# }]

data_base = []

def Program():
    while True:
        showMenu()
        flag = True
        while flag:
            num = input("Input :: ")
            try:
                num = int(num)
                flag = False
            except ValueError:
                print("Enter number")

        match num:
            case 1:
                fillDataBase()
            case 2:
                viewDataBase()
            case 3:
                addElement()
            case 4:
                deleteElement()
            case 5:
                editElement()
            case 6:
                sortElements()
            case 7:
                searchElement()
            case 8:
                selectByTypeAndPrice()
            case 9:
                averageOfType()
            case 10:
                changePrice()
            case 11:
                tableReport()
            case 0:
                break
                    
                

def showMenu():
    print("""
Choose action in Library:
1 - fillDataBase
2 - viewDataBase
3 - addElement
4 - deleteElement
5 - editElement
6 - sortElements
7 - searchElement
8 - selectByTypeAndPrice
9 - averageOfType
10 - changePrice
11 - tableReport
0 - Exit
""")

    

directory = "18_DZ_files"

file_t = "file.txt"
file_b = "file.dat"
file_j = "file.json"

def fillDataBase():
    num = int(input('''Choose 
1 - fill with template
2 - add manually
0 - if you want to end
        Input :: '''))
    
    match num:
        case 1:
            data_base.append({
                'type':'audio',
                'mark':'SONY',
                'name':'q-234',
                'price':13
            })
            data_base.append({
                'type':'video',
                'mark':'Apple',
                'name':'a-111',
                'price':12
            })
            data_base.append({
                'type':'video',
                'mark':'Apple',
                'name':'s-111',
                'price':11
            })
        case 2:
            while True:
                type_ = input("Enter 'type' :: ")
                mark = input("Enter 'mark' :: ")
                name = input("Enter 'name' :: ")
                price = input_positive_int("Enter 'price' :: ")
                data_base.append({
                    'type': type_,
                    'mark': mark,
                    'name': name,
                    'price': price
                })
                cont = int(input("Add another? (1 - yes/0 - no) :: "))
                if not cont:
                    break
        case 0:
            return

    with open(f'{directory}/{file_j}', 'w') as file:
        json.dump(data_base, file)

        


def viewDataBase():
    print("\n\t\tDataBase\n")
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file) 
    for i in data_base:
        for key, val in i.items():
            print(f"{key} :: {val}")
        print()
            

def addElement():
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file) 
    type = input("Enter 'type' :: ")
    mark = input("Enter 'mark' :: ")
    name = input("Enter 'name' :: ")
    price = input_positive_int("Enter 'price' :: ")
    data_base.append({
    'type':type,
    'mark':mark,
    'name':name,
    'price':price
    })
    with open(f'{directory}/{file_j}', 'w') as file:
        json.dump(data_base, file)

def deleteElement():
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file) 
    type = input("Enter 'type' :: ")
    mark = input("Enter 'mark' :: ")
    name = input("Enter 'name' :: ")
    price = input_positive_int("Enter 'price' :: ")
    to_delete = {
    'type': type,
    'mark': mark,
    'name': name,
    'price': price
    }
    if to_delete in data_base:
        data_base.remove(to_delete)
        print("Element deleted!")
    else:
        print("No such elements in data base")
    with open(f'{directory}/{file_j}', 'w') as file:
        json.dump(data_base, file)

def editElement():
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file)
    while True:
        type = input("Enter 'type' to edit :: ")
        mark = input("Enter 'mark' to edit :: ")
        name = input("Enter 'name' to edit :: ")
        price = input_positive_int("Enter 'price' to edit :: ")
        to_edit = {
        'type': type,
        'mark': mark,
        'name': name,
        'price': price
        }
        if to_edit in data_base:
            break
        else:
            print("No such elements in data base\n")
    new_type = input("Enter new 'type' :: ")
    new_mark = input("Enter new 'mark' :: ")
    new_name = input("Enter new 'name' :: ")
    new_price = input_positive_int("Enter new 'price' :: ")
    for item in data_base:
        if item == to_edit:
            item["type"] = new_type
            item["mark"] = new_mark
            item["name"] = new_name
            item["price"] = new_price
            break

    with open(f'{directory}/{file_j}', 'w') as file:
        json.dump(data_base, file)
    print("Item successfully edited!")
def sortElements():
    num = int(input('''Choose 
1 - Sort by name
2 - Sort by price
0 - if you want to end
        Input :: '''))
    match num:
        case 1:
            Sorted = (sorted(data_base, key=lambda x: x['name']))
        case 2:
            Sorted = (sorted(data_base, key=lambda x: x['price']))
        case 0:
            return
    with open(f'{directory}/{file_j}', 'w') as file:
        json.dump(Sorted, file)
        
def searchElement():
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file)
    query = input("Enter mark for search :: ").lower()
    results = []
    for item in data_base:
        text = " ".join(str(v).lower() for v in item.values())
        if query in text:
            results.append(item)
    if results:
        print("\nAll Results:\n")
        for i in results:
            for key, val in i.items():
                print(f"{key} :: {val}")
            print()
    else:
        print("No such results")

def selectByTypeAndPrice():
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file)
    type_query = input("Enter type of element :: ").lower()
    start_price = input_positive_int("Enter start price (including):: ")
    end_price = input_positive_int("Enter end price (including):: ")
    results = []
    for item in data_base:
        if item['type'].lower() == type_query.lower() and start_price <= item["price"] <= end_price:
            results.append(item)
    if results:
        print("\nAll Results:\n")
        for i in results:
            for key, val in i.items():
                print(f"{key} :: {val}")
            print()
    else:
        print("No such results")

def averageOfType():
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file)
    type_query = input("Enter type of element :: ").lower()
    sum = 0
    count = 0
    for item in data_base:
        if item['type'].lower() == type_query.lower():
            sum+=item['price']
            count+=1
    if sum:
        print(f"Average price of {type_query} = {sum/count}")
    else:
        print("\nNo such results")

def changePrice():
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file)
    type_query = input("Enter type of element :: ").lower()
    type_mark = input("Enter mark for search :: ").lower()
    increase_reduce = int(input("Enter 1 - increase, 2 - reduce :: "))
    percent = int(input("Enter percent to change :: "))
    results = []
    for item in data_base:
        if item['type'].lower() == type_query.lower()and item['mark'].lower() == type_mark.lower():
            if increase_reduce==1:
                item['price']+=(item['price']*percent/100)
            else:
                item['price']-=(item['price']*percent/100)
            results.append(item)
    if results:
        print("\nAll Results:\n")
        for i in results:
            for key, val in i.items():
                print(f"{key} :: {val}")
            print()
    else:
        print("No such results")
    with open(f'{directory}/{file_j}', 'w') as file:
        json.dump(data_base, file)

def tableReport():
    with open (f'{directory}/{file_j}', 'r') as file:
        data_base = json.load(file)
    type_query = input("Enter type of elements for report :: ").lower()

    items = [item for item in data_base if item['type'].lower() == type_query]
    
    items.sort(key=lambda x: x['name'])
    
    if not items:
        print("\nNo such elements found\n")
        return
    print("\nReport:\n")
    print("mark | price | name")
    print("-------------------")
    for item in items:
        print(item['mark'], "|", item['price'], "|", item['name'])

def input_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Price cannot be negative. Enter again.")
            else:
                return value
        except ValueError:
            print("Enter a valid number.")

Program()

