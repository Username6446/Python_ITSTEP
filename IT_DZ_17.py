
Library = [
    {
        'index':1,
        'Name':'Silent Sky',
        'Author':'J. Reed',
        'Publisher':'Nova',
        'Genre':'Sci-Fi',
        'Price':12,
        'Rating':8
    },
    {
        'index':2,
        'Name':'Dark Path',
        'Author':'L. Cole',
        'Publisher':'Orion',
        'Genre':'Thriller',
        'Price':10,
        'Rating':7
    },
    {
        'index':3,
        'Name':'Last Light',
        'Author':'A. Snow',
        'Publisher':'Vega',
        'Genre':'Mystery',
        'Price':11,
        'Rating':8
    },
    {
        'index':4,
        'Name':'Hidden Fire',
        'Author':'M. Gray',
        'Publisher':'Echo',
        'Genre':'Romance',
        'Price':9,
        'Rating':6
    },
    {
        'index':5,
        'Name':'Cold Storm',
        'Author':'R. Hunt',
        'Publisher':'Axis',
        'Genre':'Action',
        'Price':13,
        'Rating':7
    },
    {
        'index':6,
        'Name':'Broken Moon',
        'Author':'T. Vale',
        'Publisher':'Flux',
        'Genre':'Fantasy',
        'Price':14,
        'Rating':9
    },
    {
        'index':7,
        'Name':'Red Dust',
        'Author':'S. King',
        'Publisher':'Argo',
        'Genre':'Horror',
        'Price':12,
        'Rating':8
    },
    {
        'index':8,
        'Name':'Silent Room',
        'Author':'K. Ward',
        'Publisher':'Nova',
        'Genre':'Drama',
        'Price':10,
        'Rating':7
    },
    {
        'index':9,
        'Name':'Iron Gate',
        'Author':'P. Lane',
        'Publisher':'Orion',
        'Genre':'Adventure',
        'Price':11,
        'Rating':8
    },
    {
        'index':10,
        'Name':'Blue Shore',
        'Author':'D. West',
        'Publisher':'Echo',
        'Genre':'Fiction',
        'Price':9,
        'Rating':7
    }
]

def show_menu():
    print("""
Choose action in Library:
1 - Edit a book
2 - Print all books
3 - Search books by author
4 - Search book by name
5 - Sort list by book name
6 - Sort list by author
7 - Sort list by publisher
8 - Sort list by price
9 - Sort list by rating
0 - Exit
""")

def Program_Library():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        print()
        match choice:
            case 1:
                edit()
            case 2:
                printAll(Library)
            case 3:
                search_Author()
            case 4:
                search_Name()
            case 5:
                sort_Name()
            case 6:
                sort_Author()
            case 7:
                sort_Publisher()
            case 8:
                sort_Price()
            case 9:
                sort_Rating()
            case 0:
                print("Exiting...")
                break
            case _:
                print("Invalid choice! Please try again.")



def edit():
    printAll(Library)
    ind = int(input("Enter index :: "))
    flag = True
    try:    
        for books in Library:
            if books['index'] == ind:
                for key, val in books.items():
                    if key=='index':
                        continue
                    print(f"Change {key} with previously value {val}")
                    new_val = input("Enter :: ")
                    if new_val.strip() == "":
                        continue
                    if isinstance(val, int):
                        if int(new_val)<0 and key=='Price':
                            raise ValueError("Price can not be negative")
                        elif (int(new_val)<0 and int(new_val)>10) and key=='Rating':
                            raise ValueError("Rating must be in range(1-10)")
                        books[key] = int(new_val)
                    else:
                        books[key] = new_val
                flag = False
        if flag:
            raise Exception("Index not found exception")
    except ValueError as msg:
        print(msg)
    except Exception as msg:
        print(msg)


def printAll(Library):
    for books in Library:
        for key, val in books.items():
            print(f"{key} :: {val}")
        print()

def search_Author():
    author = input("Enter author name: ")
    for books in Library:
        for key, val in books.items():
            if key=="Author" and val==author:
                for key, val in books.items():
                    print(f"{key} :: {val}")
                print()


def search_Name():
    name = input("Enter book name: ")
    for books in Library:
        for key, val in books.items():
            if key=="Name" and val==name:
                for key, val in books.items():
                    print(f"{key} :: {val}")
                print()

def sort_Name():
    Sorted = (sorted(Library, key=lambda x: x['Name']))
    printAll(Sorted)

def sort_Author():
    Sorted = (sorted(Library, key=lambda x: x['Author']))
    printAll(Sorted)

def sort_Publisher():
    Sorted = (sorted(Library, key=lambda x: x['Publisher']))
    printAll(Sorted)
def sort_Price():
    Sorted = (sorted(Library, key=lambda x: x['Price']))
    printAll(Sorted)
def sort_Rating():
    Sorted = (sorted(Library, key=lambda x: x['Rating']))
    printAll(Sorted)




Program_Library()
