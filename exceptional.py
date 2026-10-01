class OutOfIngredientError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientError("Milk or sugar is missing")
    print("Chai is ready")

make_chai(0,1)