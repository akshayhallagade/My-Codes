month_hovercrafts = 10
hovercraft_build_price = 2000000
hovercraft_selling = 3000000
monthly_insurance = 1000000
items_making = 10
sales_that_month = int(input())
if ((items_making*hovercraft_build_price) + monthly_insurance) < sales_that_month*hovercraft_selling:
    print("Profit")
elif ((items_making*hovercraft_build_price) + monthly_insurance) > sales_that_month*hovercraft_selling:
    print("Loss")
else:
    print("Broke Even")
