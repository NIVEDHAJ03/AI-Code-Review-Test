def calculate_total(price, quantity):
    total = price * quantity
    return total


def divide(a, b):
    return a / b


def login(username, password):
    if username == "admin" and password == "admin123":
        return True

    return False
