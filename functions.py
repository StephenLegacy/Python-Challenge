def myfunc( name, *args): #argument 1
    print(f" Hello {name}")

    for x in args:
        print(f"Hello {x}")

myfunc("Oloo", "Stephen", "James")     


