###   JORDAN VICENTE-LACHAPELLE /-/ 11-2-23 /-/CTI-110  -  P4HW2 - Salary Calculator   ###
import os
os.system('cls')
Name = ""
InNum = 0
OutList = []
TOTPay = 0
TRegPay = 0
while Name.lower() != "done":
    # Get employee name from user
    Name = input("Enter employee's name: \n  ")
    if Name.lower() != "done":
        # Get number of hours from user
        Hours = int(input("Enter number of hours worked: \n  "))
        # Get pay rate per hour from user
        PayRate = float(input("Enter employee's pay rate: \n  "))
        InNum += 1
        # Determine if employee worked more than 40 hours
        if Hours > 40:
            # Calculate OT hours
            OTHours = Hours - 40
            # Calculate reg hours worked
            RegHours = Hours - OTHours
            # Calculate pay for reg hours
            RegPay = RegHours * PayRate
            TRegPay += RegPay
            # Calculate OT pay
            OTPay = OTHours * (PayRate * 1.5)
            TOTPay += OTPay
            ## Calculate gross pay
            GrossPay = RegPay + OTPay
            # Display name, payrate, reg hours. OT hours, OT pay, gross pay
            OutList.append(f"     {InNum}       |     {Name}       |     {Hours}       |     {PayRate}    |     {OTHours}     |    ${OTPay}     |    ${RegPay}     |    ${GrossPay}\n")

print("----------------------------------------------------------------------------------------------------------------------------")
print("  Input Number  |  Employee Name  |  Hours Worked  |  Pay Rate  |  OverTime  |  OverTime Pay  |  RegHour Pay  |  Gross Pay")
print("----------------------------------------------------------------------------------------------------------------------------")
for i in OutList:
    print(i)
print("----------------------------------------------------------------------------------------------------------------------------")
print(f"Total RegHour Pay: ${TRegPay}")
print(f"Total OverTime Pay: ${TOTPay}")
print(f"Total Gross Pay: ${TRegPay + TOTPay}")