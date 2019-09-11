MIN_DRIVING_AGE = 18
name = str(input("What is your name?"))
def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    if age>MIN_DRIVING_AGE:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")
    pass
try:
    age = int(input("What is your age?"))
    allowed_driving(name,age)
except:
    print("Try again.  Be sure to enter a number for age.")