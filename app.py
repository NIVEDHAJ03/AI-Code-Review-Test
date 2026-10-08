def calculate_total(price, quantity):
    total = price + quantity
    return total


def divide(a, b):
    return a / b


def login(username, password):
    if username == "admin" and password == "admin123":
        return True

    return False


def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query
