option = int(input(f"What operator would you like to use?: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Floor Division \n 6. Modulus \n"))
if option == 1:
    def add():
        x = int(input(f"x = "))
        y = int(input(f"y = "))
        z = (x) + (y)
    
        print(f"{x} + {y} = {z}")
    
    add()
elif option == 2:
    def sub():
        x = int(input(f"x = "))
        y = int(input(f"y = "))
        z = (x) - (y)

        print(f"{x} - {y} = {z}")

    sub()
elif option == 3:
    def multi():
        x = int(input(f"x = "))
        y = int(input(f"y = "))
        z = (x) * (y)

        print(f"{x} * {y} = {z}")
    multi()
elif option == 4:
    def div():
        x = int(input(f"x = "))
        y = int(input(f"y = "))
        z = (x) / (y)

        print(f"{x} / {y} = {z}")
    div()
elif option == 5:
    def flr():
        x = int(input(f"x = "))
        y = int(input(f"y = "))
        z = (x) // (y)

        print(f"{x} // {y} = {z}")
    flr()
elif option == 6:
    def mod():
        x = int(input(f"x = "))
        y = int(input(f"y = "))
        z = (x) % (y)

        print(f"{x} % {y} = {z}")
    mod()

