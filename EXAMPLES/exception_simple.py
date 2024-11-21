x = 5
y = "cheese"
try:  # Execute code that might have a problem
    z = x + y
    print("Bottom of try")

except TypeError as err:    # Catch the expected error; assign error object to err
    print("Naughty programmer! ", err)
    raise  # re-raise exception

print("After try-except")  # Get here whether or not exception occurred
