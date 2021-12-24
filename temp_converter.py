inp = input("\nWhich system do you have a measurement for?\n\nType C for Celcius, F for Fahrenheit: ")

if inp == "F" or inp == "f":
    print("\nYou have entered Fahrenheit\n")
    freading = input("Enter your Fahrenheit temperature reading: ")
    try: 
        int(freading)
        fconvert = float(freading)
        cresult = (fconvert-32)*5/9
        print(f"The Temperature in Celcius is: {cresult}\n")
    except:
        print("Enter a valid number!")

elif inp == "C" or inp == "c":
    print("\nYou have entered Celcius\n")
    creading = input("Enter your Celcius temperature reading: ")
    try:
        int(creading)
        cconvert = float(creading)
        fresult = (cconvert*9/5)+32
        print(f"The Temperature in Farenheit is: {fresult}\n")
    except:
        print("Enter a valid number!")
else:
    print("Please type either C or F!")