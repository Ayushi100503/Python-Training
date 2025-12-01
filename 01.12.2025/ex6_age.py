class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age<18:
        raise InvalidAgeError("Age must be more than 18 years old")
    else:
        print("Age accepted")
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(e)