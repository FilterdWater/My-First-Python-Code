def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label(
    "Dr.",
    "Doctor",
    "Amazing",
    "III",
    street="123 Fake St.",
    pobox="1001",
    apt="100",
    city="Detroit",
    state="MI",
    zip="12345",
)
