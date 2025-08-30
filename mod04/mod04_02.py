positiivinen = True
while positiivinen:
    tuuma = int(input("Anna luku tuumina: "))
    sentti = float(int(tuuma) * 2.54)
    print(f"luku sentteinä on: {sentti}cm")
    if tuuma < 0:
        positiivinen = False
