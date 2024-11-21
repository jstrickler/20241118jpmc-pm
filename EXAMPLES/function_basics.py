def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None

x = say_hello()  # Call function (arguments, if any, in () )
print(f"{x = }")

def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print(f"m is {m:.3f} n is {n:.3f}")

def hello():
    print("hello")

def doit(func):
    func()  # calls the func obj

doit(hello)

f = lambda x: 2 * x
print(f"{f(10) = }")
print('-' * 60)

def process_files(search_term, folder, *file_paths, ignore_case=False):
    print(f"{search_term = }")
    print(f"{file_paths = }")
    
    for file_path in file_paths:
        print(file_path)

process_files('pig', 'DATA', 'alice.txt', 'parrot.txt', ignore_case=True)
process_files('pig', 'DATA', 'alice.txt', 'parrot.txt')

def create_report(server, *extra, db, table, start_date, end_date, format):
    pass

#                    positional        | named
create_report("foo.bar.com", "wombat", "abc", db="customers", start_date="2022-01-01", end_date="2022-01-31",