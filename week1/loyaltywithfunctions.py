# Constants for readability and easy updates
LOYALTY_DISCOUNT_RATE = 0.20
STANDARD_DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 100
SERVICE_CHARGE_RATE = 0.05

def calculate_discount(total_bill, loyalty_customer):
    """
    Calculate the discount based on loyalty status and total bill.
    Returns the new total bill after applying discount and the discount message.
    """
    if total_bill > DISCOUNT_THRESHOLD:
        if loyalty_customer:
            discount_rate = LOYALTY_DISCOUNT_RATE
            discount_message = "20% loyalty discount applied."
        else:
            discount_rate = STANDARD_DISCOUNT_RATE
            discount_message = "10% discount applied."
        total_bill -= total_bill * discount_rate
    else:
        # No discount, so returning the original bill without modifications
        discount_rate = 0
        discount_message = None
    return total_bill, discount_message

def apply_service_charge(total_bill, discount_message):
    """
    Apply a service charge if no discount was applied.
    Returns the final total bill and any additional messages.
    """
    if discount_message is None:
        total_bill += total_bill * SERVICE_CHARGE_RATE
        return total_bill, 'Sorry, no discount. 5% service charge applied.'
    else:
        return total_bill, discount_message

def print_bill(total_bill, message):
    """
    Print the final bill and any relevant messages.
    """
    if message:
        print(message)
    print('Total Bill: {:.2f}'.format(total_bill))

def main():
    # Inputs
    loyalty_customer = True
    total_bill = 200

    # Calculate discount
    total_bill, discount_message = calculate_discount(total_bill, loyalty_customer)
    
    # Apply service charge if needed
    total_bill, service_message = apply_service_charge(total_bill, discount_message)
    
    # Print the final bill
    print_bill(total_bill, service_message)

if __name__ == "__main__":
    main()
