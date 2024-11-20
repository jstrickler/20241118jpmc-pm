import sys

FIRST_LETTER = sys.argv[1]
FILE_PATHS = sys.argv[2:]

for file_path in FILE_PATHS:
    count = 0
    with open(file_path) as file_in:
        for raw_line in file_in:
            if raw_line.startswith(FIRST_LETTER):
                count += 1
    print(f"{file_path} contains {count} lines that start with {FIRST_LETTER}")