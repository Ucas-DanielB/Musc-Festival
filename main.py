# Daniel code :D 

# Ticket and Attendee Management System for a Music Festival

# Ticket storage and attendees
bought_tickets = {"1-day": 0, "3-day": 0, "vip": 0}
unbought_tickets = {"1-day": 200, "3-day": 100, "vip": 40}
attendees = {"people attending total": 340}

# Function to display available tickets
def display_tickets():
    print("\nAvailable Tickets:")
    for ticket_type, count in unbought_tickets.items():
        print(f"{ticket_type.capitalize()} Tickets: {count}")
    
    print("\nBought Tickets:")
    for ticket_type, count in bought_tickets.items():
        print(f"{ticket_type.capitalize()} Tickets: {count}")
    print(f"{attendees}")

# Function to buy tickets
def buy_ticket():
    ticket_type = input("Enter ticket type (1-day, 3-day, vip): ").strip().lower()
    
    if ticket_type not in unbought_tickets:
        print("\nInvalid ticket type.")
        return

    try:
        quantity = int(input("Enter number of tickets: "))
        if quantity <= 0:
            print("\nInvalid quantity.")
            return

        if unbought_tickets[ticket_type] >= quantity:
            unbought_tickets[ticket_type] -= quantity
            bought_tickets[ticket_type] += quantity
            print(f"\nSuccessfully bought {quantity} {ticket_type} tickets.")
        else:
            print("\nNot enough tickets available.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

# Function to refund tickets
def refund_ticket():
    display_tickets()
    ticket_type = input("Enter ticket type to refund: ").strip().lower()
    
    if ticket_type not in bought_tickets or bought_tickets[ticket_type] == 0:
        print("\nYou have no tickets of this type to refund.")
        return

    try:
        quantity = int(input("Enter number of tickets to refund: "))
        if quantity <= 0 or bought_tickets[ticket_type] < quantity:
            print("\nRefund failed: Insufficient tickets.")
            return

        bought_tickets[ticket_type] -= quantity
        unbought_tickets[ticket_type] += quantity
        print(f"\nSuccessfully refunded {quantity} {ticket_type} tickets.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

# Function to upgrade tickets
def upgrade_ticket():
    display_tickets()
    old_ticket = input("Enter current ticket type: ").strip().lower()
    new_ticket = input("Enter ticket type to upgrade to: ").strip().lower()

    if old_ticket not in bought_tickets or bought_tickets[old_ticket] == 0:
        print("\nYou have no tickets of this type to upgrade.")
        return

    if new_ticket not in unbought_tickets:
        print("\nInvalid ticket type.")
        return

    try:
        quantity = int(input("Enter number of tickets to upgrade: "))
        if quantity <= 0 or bought_tickets[old_ticket] < quantity:
            print("\nUpgrade failed: Insufficient tickets.")
            return

        if unbought_tickets[new_ticket] < quantity:
            print("\nUpgrade failed: Not enough new ticket type available.")
            return

        bought_tickets[old_ticket] -= quantity
        unbought_tickets[old_ticket] += quantity
        unbought_tickets[new_ticket] -= quantity
        bought_tickets[new_ticket] += quantity
        print(f"\nSuccessfully upgraded {quantity} {old_ticket} tickets to {new_ticket} tickets.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

# Main function
def main():
    while True:
        print("\n1. View Tickets\n2. Buy Ticket\n3. Refund Ticket\n4. Upgrade Ticket\n5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tickets()
        elif choice == "2":
            buy_ticket()
        elif choice == "3":
            refund_ticket()
        elif choice == "4":
            upgrade_ticket()
        elif choice == "5":
            print("\nExiting ticket system.")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

