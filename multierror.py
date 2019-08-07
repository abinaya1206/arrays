try:
    a=3
    if a<4:
        b=a/(a-3)
    print("value of b=",b)
except (ZeroDivisionError,NameError):
    print("\n Error ocurred and handled")
