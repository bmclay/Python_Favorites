def computepay(hrs, rate):
    if float(hrs) <= float(40) :
        pay = float(hrs) * float(rate)
    else:
        othrs = float(hrs) - 40
        otrate = float(rate) / 2 + float(rate)
        pay = float(othrs) * float(otrate) + 40 * float(rate)
    return(pay)

hrs = input("Enter Hours Worked: ")
rate = input("Enter Hourly Rate: ")
p = computepay(hrs, rate)
print("Gross pay is", round(p, 3))