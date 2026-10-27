#Task 1: Writing and Testing a Decorator
import logging
import functools

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    """Log the function name, parameters, and return value to ./decorator.log."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(
            logging.INFO,
            f"positional parameters: {list(args) if args else 'none'}",
        )
        logger.log(
            logging.INFO,
            f"keyword parameters: {kwargs if kwargs else 'none'}",
        )
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "")  
        return result

    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")


@logger_decorator
def positional_only(*args):
    return True


@logger_decorator
def keyword_only(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    say_hello()
    positional_only(1, 2, "three")
    keyword_only(name="Joan", city="Dallas")