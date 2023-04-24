from burger import Burger

def main():
    Burger.show_menu()
    print("\n")
    burger = Burger()

    burger.place_order("Fish Burger")
    print("\n")

    burger.make_burger()
    print("\n")



if __name__ == "__main__":
    main()
