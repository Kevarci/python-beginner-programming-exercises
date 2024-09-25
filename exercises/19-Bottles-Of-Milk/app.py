def number_of_bottles():
    for i in range(99, 0, -1):
        if i > 1:
            print(f"{i} bottles of milk on the wall, {i} bottles of milk.")
            print(f"Take one down, pass it around, {i-1} bottles of milk on the wall.\n")
        elif i == 1:
            print(f"{i} bottle of milk on the wall, {i} bottle of milk.")
            print("Take one down, pass it around, no more bottles of milk on the wall.\n")
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.")

# Llamada a la función
number_of_bottles()