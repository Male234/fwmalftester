# FEEDWATER PUMP MALFUNCTION TESTER
# stuff
import math
print('THIS IS A VERY HIGH TECH TESTER TOTALLY!')
print('ONLY INPUT NUMBERS UNLESS SAID OTHERWISE')
print('DISCLAIMER: THIS IS NOT VERY ACCURATE AND YOU SHOULD SCRAM THE REACTOR TO TEST IT PROPERLY (if very very needed tho) \n IF THE NUMBER YOU INPUT IS NOT A MULTIPLY OF 10 THEN IT WILL NOT WORK PROPERLY')

#variables
full_flow = 1000
pump_flow = int(input("Current pump flow: "))
pump_perc = int(input("Current pump percentage setpoint: "))
perc_1 = 10


#math
result = pump_flow/pump_perc

if result != pump_flow/pump_perc*100:
    print("You have a malfunction!")
else:
    print("There is no malfunction on the pump!")
