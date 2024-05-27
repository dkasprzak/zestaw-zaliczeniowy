import functools
import inspect


def log_params(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_signature = inspect.signature(func)
        bound_args = func_signature.bind(*args, **kwargs)
        bound_args.apply_defaults()

        param_types = {name: type(value).__name__ for name, value in bound_args.arguments.items()}

        print(f"{func.__name__} params: {param_types}")

        return func(*args, **kwargs)

    return wrapper


@log_params
def user_data(name, surname, age, positions):
    return f"name: {name}, surname: {surname}, age: {age}, positions: {positions}"

test1 = user_data("Adam", "Kowlaski", 32, ["DevOps", ".NET Developer"])
test2 = user_data("Ewa", "Nowak", 28, ["Data Scientist", "Machine Learning Engineer"])
test3 = user_data("Jan", "Wiśniewski", 45, ["Project Manager", "Business Analyst"])
test4 = user_data("Maria", "Kowalczyk", 22, ["Frontend Developer", "UX Designer"])

