# FEEDWATER PUMP MALFUNCTION TESTER
# stuff
import math
print('THIS IS A VERY HIGH TECH TESTER TOTALLY!')
print('ONLY INPUT NUMBERS UNLESS SAID OTHERWISE')

#variables
full_flow = 1000
pump_flow = int(input("Current pump flow: "))
pump_perc = int(input("Current pump percentage setpoint: "))
perc_1 = 10


#math
result = perc_1*pump_perc

if result != full_flow/pump_perc:
    print("You have a malfunction!")
else:
    print("There is no malfunction on the pump!")