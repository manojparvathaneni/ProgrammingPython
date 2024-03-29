loyalty_customer = True
total_bill = 200

#refactor the code to make discount calculation more readable
if loyalty_customer and total_bill > 100:
    #give 20% discount
   total_bill -= total_bill * 0.20
elif total_bill > 100:
    #give 10% discount
    total_bill -= total_bill * 0.10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))