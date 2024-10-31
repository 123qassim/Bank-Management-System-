withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
bonus = 0
if withdrawal_amount > 10000:
    bonus = 0.10 * withdrawal_amount
    print("You've qualified for a 10% bonus!")
elif withdrawal_amount > 5000:
    bonus = 0.05 * withdrawal_amount
    print("You've qualified for a 5% bonus!")
else:
    print("No bonus available for this withdrawal amount.")

total_amount = withdrawal_amount + bonus
print("Withdrawal Amount: %.2f" % withdrawal_amount)
print("Bonus Amount: %.2f" % bonus)
print("Total Amount Given: %.2f" % total_amount)


