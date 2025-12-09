# R. Age in Days

N=int(input())
years=N//365
print(years,"years")
remaining_days=N%365
months=remaining_days//30
print(months,"months")
days=(remaining_days%30)
print(days,"days")