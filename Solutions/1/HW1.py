deposit_amount = float(input('Please enter the one-time investment deposit amount : \n'))
fee_percentage = float(input('Please enter the one-time investment fee percentage :\n'))
annual_interest_rate = float(input('Please enter annual interest rate :\n'))
num_of_years = int(input('Please enter number of years the investment will be held :\n'))

fee_amount = deposit_amount *(fee_percentage/100)
initial_investment = deposit_amount - fee_amount

future_value = initial_investment * ((1 + annual_interest_rate / 100) ** num_of_years)

print(f"Present Value: ${initial_investment:.2f}")
print(f"Future Value: ${future_value:.2f}")

withdrawal_fee = num_of_years * 74
print(f"Withdrawal Fee: ${withdrawal_fee:.2f}")

future_value_withdrawal = future_value - withdrawal_fee
print(f"Future Value after Withdrawal Fee: ${future_value_withdrawal:.2f}")

growth_amount = future_value_withdrawal - initial_investment
print(f"Growth Amount : {growth_amount:.2f}")

growth_percentage = (growth_amount/initial_investment) * 100
print(f"Growth Percentage : {growth_percentage:.2f}")