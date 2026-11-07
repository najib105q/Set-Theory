while True:
    print("\nSet Operations")
    print("--------------")
    print("1. Enter sets")
    print("2. Quit")

    choice = input("\nChoice: ").strip().lower()

    if choice == "2":
        print("\nGoodbye!")
        break

    if choice != "1":
        print("\nInvalid choice")
        continue

    print()

    a = set(input("Set A: ").split())
    b = set(input("Set B: ").split())

    print("\nUnion:", a | b)
    print("Intersection:", a & b)
    print("A without B:", a - b)
    print("B without A:", b - a)
    print("Symmetric Difference:", a ^ b)
    print("A subset of B:", a <= b)
    print("A superset of B:", a >= b)
    print("Disjoint:", a.isdisjoint(b))
    print("Cartesian Product:", {(x, y) for x in a for y in b})