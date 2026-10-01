def brew_chai(flavour):
    if flavour not in ["masala","ginger","elaichi"]:
        raise ValueError(f"{flavour} not in menu")
    print(f"{flavour} chai brewed")

brew_chai("mint")