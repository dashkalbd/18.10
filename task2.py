def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик: {func.__name__}")
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        print()
        return result
    return wrapper


class OrderService:
    @log_operation
    def create_order(self, product, quantity, price):
        return f"{product} x {quantity} = {quantity * price} грн"


@log_operation
def delivery_cost(weight, express=False):
    cost = weight * 10
    if express:
        cost = cost * 2
    return cost


service = OrderService()
service.create_order("Книга", 2, price=300)

delivery_cost(3)
delivery_cost(3, express=True)