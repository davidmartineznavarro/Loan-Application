A = 18800
r = 0.05
n = 48
p = A*(r/12/(1-(1+r/12)**(-1*n)))
print(p)

age_str = input("your age:")
age_int = int(age_str)

if age_int<=40:
  inc_str = input("income:")
  inc_int = int(inc_str)
  if inc_int > 166000:
    print("Loan Approved!")
  else:
    sav_str = input("savings:")
    sav_int = int(sav_str)
    if sav_int > 657:
      print("Loan Approved!")
    else:
      print("NOT Approved")
else:
  sav_str = input("savings:")
  sav_int = int(sav_str)
  if sav_int > 433:
    print("Loan Approved!")
  else:
    print("NOT Approved")
