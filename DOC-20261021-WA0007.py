movie = []

def add():
    mid = int(input("Enter Movie Id: "))
    name = input("Enter Movie Name: ")
    theater = input("Enter Theater Name: ")
    show = input("Enter Show Time: ")
    price = int(input("Enter Ticket Price: "))

    m1 = {
        "MID": mid,
        "MNAME": name,
        "THEATER": theater,
        "SHOW": show,
        "PRICE": price
    }

    movie.append(m1)
    print("Movie Added Successfully")


def display():
    print("\n==============================================================")
    print("MOVIE ID    MOVIE NAME    THEATER NAME    SHOW TIME    PRICE")
    print("==============================================================")

    for m in movie:
        print(m["MID"], "      ", m["MNAME"], "      ",
              m["THEATER"], "      ", m["SHOW"], "      ",
              m["PRICE"])

    print("==============================================================")


def search():
    mid = int(input("Enter Movie Id to Search: "))

    for m in movie:
        if m["MID"] == mid:
            print("\nMovie Found")
            print("Movie Id :", m["MID"])
            print("Movie Name :", m["MNAME"])
            print("Theater Name :", m["THEATER"])
            print("Show Time :", m["SHOW"])
            print("Ticket Price :", m["PRICE"])
            return

    print("Movie Not Found")


def sort():
    movie.sort(key=lambda x: x["MNAME"])
    print("Movies Sorted Successfully")
    display()


def update():
    mid = int(input("Enter Movie Id to Update: "))

    for m in movie:
        if m["MID"] == mid:

            m["MNAME"] = input("Enter New Movie Name: ")
            m["THEATER"] = input("Enter New Theater Name: ")
            m["SHOW"] = input("Enter New Show Time: ")
            m["PRICE"] = int(input("Enter New Ticket Price: "))

            print("Movie Updated Successfully")
            return

    print("Movie Not Found")


def delete():
    mid = int(input("Enter Movie Id to Delete: "))

    for m in movie:
        if m["MID"] == mid:
            movie.remove(m)
            print("Movie Deleted Successfully")
            return

    print("Movie Not Found")