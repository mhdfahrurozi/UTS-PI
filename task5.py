with open("input.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

formatted_numbers = ",".join([f"{num:03d}" for num in numbers])
print(" UTS Pemrograman Integratif -  Task 5 ".center(50, "="))
print("Jumlah angka:", formatted_numbers)