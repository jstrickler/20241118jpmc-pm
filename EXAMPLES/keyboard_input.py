
user_name = input("What is your name: ")
quest = input("What is your quest? ")
print(f"{user_name} seeks {quest}")

raw_num = input("Enter number: ")  # input is always a string
print(raw_num)

try:
    num = float(raw_num)  # convert to numbers as needed
except ValueError as err:
    print(err)
else:
    print(f"2 times {num} is {num * 2}")

# raw_bd = input("Enter DOB (YYYY-MM-DD): ")
# year, month, day = raw_bd.split('-')
