directory = "18_files"

file_t = "file.txt"
file_b = "file.dat"
file_j = "file.json"


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

list_ = ["red", "green", "yellow", "pupple", "pink", "gold"]

item = {
    'name': 'program Python',
    'price': 9.5,
    'number': 18
}


group = [{
  "name": "Kameko",
  "last_name": "Beldon",
  "email": "kbeldon0@bbc.co.uk",
  "date": "31/08/2001"
}, {
  "name": "Faulkner",
  "last_name": "Hyams",
  "email": "fhyams1@arstechnica.com",
  "date": "19/09/2008"
}, {
  "name": "Northrop",
  "last_name": "Edgecumbe",
  "email": "nedgecumbe2@va.gov",
  "date": "08/02/2005"
}, {
  "name": "Hector",
  "last_name": "Keune",
  "email": "hkeune3@ustream.tv",
  "date": "08/03/2003"
}, {
  "name": "Reggy",
  "last_name": "Misson",
  "email": "rmisson4@china.com.cn",
  "date": "06/07/2003"
}, {
  "name": "Mill",
  "last_name": "Balint",
  "email": "mbalint5@patch.com",
  "date": "09/03/2003"
}, {
  "name": "Blondie",
  "last_name": "Jochanany",
  "email": "bjochanany6@shutterfly.com",
  "date": "23/11/2005"
}, {
  "name": "Babbie",
  "last_name": "Oppery",
  "email": "boppery7@boston.com",
  "date": "07/09/2000"
}, {
  "name": "Manuel",
  "last_name": "Kerrey",
  "email": "mkerrey8@census.gov",
  "date": "22/05/2010"
}, {
  "name": "Rriocard",
  "last_name": "Reagan",
  "email": "rreagan9@friendfeed.com",
  "date": "24/12/2007"
}]

# with open(f"{directory}/{file_t}", 'w') as file:
#     file.write(text)

# with open(f"{directory}/{file_t}", 'w') as file:
#     file.writelines(list_)

# with open(f"{directory}/{file_t}", 'w') as file:
#     file.writelines(item)


import pickle

# with open(f"{directory}/{file_b}", "wb") as file:
    # res = pickle.dumps(text)
    # file.write(res)
    # pickle.dump(text,file)

# with open(f"{directory}/{file_b}", "rb") as file:
#     res = file.read()
#     print(pickle.load(file))



# with open(f"{directory}/{file_b}", "wb") as file:
#     pickle.dump(list_,file)

# with open(f"{directory}/{file_b}", "rb") as file:
#   res = pickle.load(file)  
#   print(type(res), res, "\n", res[2])



# with open(f"{directory}/{file_b}", "wb") as file:
#     pickle.dump(list_,file)

# with open(f"{directory}/{file_b}", "rb") as file:
#   res = pickle.load(file)  
#   print(type(res), res, "\n", res['name'])



# with open(f"{directory}/{file_b}", "wb") as file:
#     pickle.dump(group,file)

# with open(f"{directory}/{file_b}", "rb") as file:
#     res = pickle.load(file) 
#     print(type(res), res, "\n", res[2]['name'])


# with open(f'{directory}/{file_b}', 'rb') as file:
#     students = pickle.load(file)

# new_st = {
#   "name": "Kameko",
#   "last_name": "Beldon",
#   "email": "kbeldon0@bbc.co.uk",
#   "date": "31/08/2001"
# }

# students = list(students)
# students.append(new_st)
# print(students)

# with open(f'{directory}/{file_b}', 'wb') as file:
#     pickle.dump(students, file)


import requests
import json
response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
res = response.content
res = json.loads(res)
# print(type(res), res, res[0]['buy'])
# print(res[0]['buy'])

# with open(f'{directory}/{file_j}', 'w') as file:
#     json.dump(group, file)

# with open(f'{directory}/{file_j}', 'r') as file:
#     print(json.load(file))

def func():
    response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
    res = response.content
    res = json.loads(res)
    while True:
        num = int(input('''Choose conversetion
        1 - eur->grn
        2 - grn->eur
        3 - dol->grn
        4 - grn->dol
        0 - end
        Enter :: '''))
        sum = int(input("Enter sum : "))
        result = 0
        match num:
            case 1:
                result = float(res[0]['sale'])*sum
            case 2:
                result = float(res[0]['buy'])/sum
            case 3:
                result = float(res[1]['sale'])*sum
            case 4:
                result = float(res[0]['buy'])/sum
            case 0:
                break
        print(f"Result = {result}")

