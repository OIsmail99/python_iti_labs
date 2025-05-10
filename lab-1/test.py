from datetime import datetime

startDate = datetime.strptime(input("Enter start date (yyyy/mm/dd): "), "%Y-%m-%d").date()
endDate = datetime.strptime(input("Enter start date (yyyy/mm/dd): "), "%Y-%m-%d").date()
difference = abs(endDate - startDate).days
print(difference)
