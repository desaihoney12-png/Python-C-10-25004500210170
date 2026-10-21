import CURD as c1

while True:

    print("\n========== MOVIE MANAGEMENT SYSTEM ==========")
    print("1) Add Movie")
    print("2) Display Movie")
    print("3) Search Movie")
    print("4) Sort Movie")
    print("5) Update Movie")
    print("6) Delete Movie")
    print("7) Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Adding Movie")
        c1.add()

    elif choice == 2:
        print("Displaying Movies")
        c1.display()

    elif choice == 3:
        print("Searching Movie")
        c1.search()

    elif choice == 4:
        print("Sorting Movies")
        c1.sort()

    elif choice == 5:
        print("Updating Movie")
        c1.update()

    elif choice == 6:
        print("Deleting Movie")
        c1.delete()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Wrong Choice")