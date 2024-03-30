# Constants for readability and easy updates
from calendar import c


LOYALTY_DISCOUNT_RATE = 0.20
STANDARD_DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 100
SERVICE_CHARGE_RATE = 0.05

# Inputs
loyalty_customer = True
total_bill = 200

# Initial calculations for discounts
if total_bill > DISCOUNT_THRESHOLD:
    if loyalty_customer:
        # Applying loyalty discount
        discount = LOYALTY_DISCOUNT_RATE
        discount_message = "20% loyalty discount applied."
    else:
        # Applying standard discount
        discount = STANDARD_DISCOUNT_RATE
        discount_message = "10% discount applied."
    
    total_bill -= total_bill * discount
    print(discount_message)
else:
    # Applying service charge for bills not eligible for discount
    total_bill += total_bill * SERVICE_CHARGE_RATE
    print('Sorry, no discount. 5% service charge applied.')

# Printing the final bill
print('Total Bill: {:.2f}'.format(total_bill))
