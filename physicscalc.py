import sys
print("""█▀▀█ █░░█ █░░█ █▀▀ ░▀░ █▀▀ █▀▀   █▀▀ █▀▀█ █░░ █▀▀ █░░█ █░░ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█
█░░█ █▀▀█ █▄▄█ ▀▀█ ▀█▀ █░░ ▀▀█   █░░ █▄▄█ █░░ █░░ █░░█ █░░ █▄▄█ ░░█░░ █░░█ █▄▄▀
█▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀   ▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ░▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀░▀▀""")
print("Made by n3oo, 2019")
options = input("""1. Average speed calculator
2. Acceleration
3. Speed
4. Resistance
5. Current
6. Voltage
 """)
if options == "1":
    print("Average speed calculator: ")
    print("Average speed = total distance/total time ")
    print("v = d/t")
    d = int(input("(meters) Total distance: "))
    t = int(input("(seconds) Total time: "))
    v = d/t
    print(v, "m/s")
    sys.exit()
if options == "2":
    print("Acceleration calculator: ")
    print("Acceleration = change in speed/time ")
    print("a = v/t ")
    v = int(input("(Meters) Change in speed: "))
    t = int(input("(Seconds) Time: "))
    a = v/t
    print(a,"m/s^2")
    sys.exit()
if options == "3":
    print("Speed calculator: ")
    print("Speed = distance/time")
    print("v = s/t ")
    s = int(input("(Kilometers) Distance: "))
    t = int(input("(Minutes) Time: "))
    v1 = s/t
    print(v1, "km/h")
    sys.exit()
if options == "4":
    print("Resistance calculator: ")
    print("Resistance = voltage/current ")
    print(" r = v/i ")
    v2 = int(input("(Volts) Voltage: "))
    i = int(input("(Amperes) Current: "))
    r = v2/i
    print(r, "Ω")
    sys.exit()
if options =="5":
    print("Current calculator: ")
    print("Current = voltage/resistance ")
    print("i = v/r ")
    v3 = int(input("(Volts) Voltage: "))
    r1 = int(input("(Ohms) Resistance: "))
    i1 = v3/r1
    print(i1, "amperes")
    sys.exit()
if options == "6":
    print("Voltage calculator: ")
    print("Voltage = current*resistance ")
    print("v = i*r ")
    i2 = int(input("(amperes) Current: "))
    r2 = int(input("(ohms) Resistance "))
    v4 = i2*r2
    print(v4, "V")
    sys.exit()
