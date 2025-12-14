try:
    num = int(input("Enter number: "))
    if num < 0:
        raise ValueError("Negative number not allowed")
    result = 10 / num

except ValueError as e:
    print("Value error:", e)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program completed")
