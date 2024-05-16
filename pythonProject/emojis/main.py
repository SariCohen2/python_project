import Handling_icons as Handling


def main():
    print("◀ Welcome to the coolest Python program ever ▶")
    print("please follow the instructions---")
    print("Select an option:")
    print("\t1: Print all icons.")
    print("\t2: Search icons by keyword.")
    choice = int(input("Enter your option "))
    print(choice)
    if choice == 1:
        Handling.print_all_icons_names()
    elif choice == 2:
        keyword = input("Enter keyword: ")
        Handling.search_icons_by_keyword(keyword)
    else:
        print("Invalid input!\n ")
        main()
    icon_name = input("\nEnter icon name to display: ")
    Handling.display_icon(icon_name)


if __name__ == "__main__":
    main()
