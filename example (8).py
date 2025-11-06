# Created on iPad.
def unit_conversion():
    value = float(input("Enter your temperature: "))
    unit = input("Please enter your unit (celsius or fahrenheit): ")

    if unit == "celsius":
        print((value * 9/5) + 32, "fahrenheit")
    elif unit == "fahrenheit":
        print((value - 32) * 5/9, "celsius")
    else:
        print("Please enter a proper unit (celsius or fahrenheit)")

unit_conversion()
!