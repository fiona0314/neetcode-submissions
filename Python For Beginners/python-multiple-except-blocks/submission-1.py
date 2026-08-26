def divide_numbers(a: str, b: str) -> None:
    try:
        result = int(a) / int(b)
    except ValueError:
        result = "Error: Invalid value!"
    except ZeroDivisionError:
        result = "Error: Division by zero!"
    except Exception as error: 
        result = f"An error occurred: {error}"
    print(result)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
