payrate = 10.0
paycheck = 0

try:     
    answer = float(input("How many hours did you work?"))
    
except: 
    print("There was an error.")
else: 
    paycheck = answer * payrate

print(f"Your paycheck is ${paycheck:,.2f}")