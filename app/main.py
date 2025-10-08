from app import calculator


def main():
    print("Scientific Calculator (Python)")
    while True:
        print("\nMenu:")
        print("1) sqrt(x)")
        print("2) factorial(n)")
        print("3) ln(x)")
        print("4) x^a")
        print("5) Exit")

        choice = input("Choose (1-5): ").strip()
        try:
            if choice == "1":
                x = float(input("Enter x (>=0): "))
                print(f"sqrt({x}) = {calculator.sqrt(x)}")
            elif choice == "2":
                n = int(input("Enter n (>=0): "))
                print(f"{n}! = {calculator.factorial(n)}")
            elif choice == "3":
                x = float(input("Enter x (>0): "))
                print(f"ln({x}) = {calculator.ln(x)}")
            elif choice == "4":
                x = float(input("Enter base x: "))
                b = float(input("Enter exponent b: "))
                print(f"{x}^{b} = {calculator.power(x, b)}")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Pick 1–5.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
