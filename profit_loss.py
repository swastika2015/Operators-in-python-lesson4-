Actual_cost = float(input("actual cost of the product:"))
Sales_amount = float(input("sale amount of the product:"))

if Sales_amount > Actual_cost:
    amount= Sales_amount-Actual_cost
    print("Total profit = {0}". format (amount))
else:
  print("NO  PROFIT!!!!")