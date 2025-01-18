def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

while True:
    exp = input("calculator: ")
    if not exp:
        break
    print(f"hasil: {calculator(exp)}")
    