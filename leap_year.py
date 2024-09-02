def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorian calendar period")
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def days_in_month(year, month):
    month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_year_leap(year):
        month_len[1] = 29
    
    if 1 <= month <= 12:
        return month_len[month - 1]


def day_of_year(year, month, day):
    
    if month < 1 or month > 12:
        return
    
    if day < 1 or day > days_in_month(year, month):
        return
    
    days_upto_last_month = sum(days_in_month(year, m) for m in range(1, month))
        
    total_days = day + days_upto_last_month
    
    return total_days

# print(day_of_year(1900,2,29))

test_years = [2000, 1900, 2024, 2023, 2021, 2019]
test_months = [2, 4, 8, 1, 12, 13]
test_days = [29, 13, 19, 1, 32, 29]
test_results = [60, 103, 232, 1, None, None]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	da = test_days[i]
	print(yr, mo, da, "->", end="")
	result = day_of_year(yr, mo, da)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
          








