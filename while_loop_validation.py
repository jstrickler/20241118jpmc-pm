start_letter = "a"
min_length = 5

while True:
    word = input(f"Please enter word (len >= 5, starts with {start_letter}) ")
    if not word.startswith(start_letter):
        print(f"word must start with {start_letter}")
        continue # go back to top of loop
    elif len(word) < min_length:
        print(f"word must be at least {min_length} characters long")
        continue
    else:
        break

print(f"word is >{word}<")