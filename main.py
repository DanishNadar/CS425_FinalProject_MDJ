from db_functions import (
    create_user, create_agent, create_renter,
    create_address, create_cc, get_user,
    list_available_properties,
    create_property
)

def pause():
    input("\nPress Enter to continue...")

def register():
    print("\nRegister a new user")
    email = input("Email: ")
    name = input("Name: ")
    utype = input("Type (AGENT/RENTER): ").upper()
    
    if not create_user(email=email, name=name, user_type=utype):
        print("ERROR: Failed to create user.")
        return

    if utype == "AGENT":
        print("\nCreate agent profile")
        job = input("Job title: ")
        agency = input("Agency: ")
        phone = input("Phone [+X...]: ")
        if create_agent(agent_email=email, job_title=job, agency=agency, phone_number=phone):
            print("✓ Agent created")
    else:
        print("\nCreate renter profile")
        date = input("Move-in date (YYYY-MM-DD): ")
        loc = input("Preferred location: ")
        budg = float(input("Budget: "))
        if create_renter(renter_email=email, 
                        desired_move_in_date=date,
                        preferred_location=loc,
                        budget=budg):
            print("✓ Renter created")

def add_address():
    print("\nAdd an address")
    email = input("User email to attach to: ")
    city = input("City: ")
    state = input("State: ")
    zipc = input("ZIP: ")
    
    # Check if user is an agent
    user = get_user(email)
    if user and user['user_type'] == 'AGENT':
        print("\nAgent detected - creating property listing")
        # Get property details
        rental_price = float(input("Rental price: "))
        description = input("Property description: ")
        sq_footage = int(input("Square footage: "))
        property_type = input("Property type (House/Apartment/Commercial_Building/Vacation_Home/Land): ")
        
        # First create the address
        if create_address(user_email=email, city=city, state=state, zip_code=zipc):
            print("✓ Address created")
            # Then create the property
            if create_property(agent_email=email, city=city, state=state, zip_code=zipc,
                             rental_price=rental_price, description=description,
                             sq_footage=sq_footage, property_type=property_type):
                print("✓ Property listing created")
        else:
            print("Failed to create address")
    else:
        # Regular address creation for non-agents
        if create_address(user_email=email, city=city, state=state, zip_code=zipc):
            print("✓ Address created")

def add_cc():
    print("\nAdd a credit card")
    email = input("User email: ")
    aid = int(input("Billing Address ID: "))
    num = input("Card number (16 digits): ")
    exp = input("Expiration (YYYY-MM-DD): ")
    ctype = input("Type (Visa/MasterCard/Amex/Discover): ").capitalize()
    if create_cc(user_email=email,
               billing_address_id=aid,
               card_number=num,
               expiration_date=exp,
               card_type=ctype):
        print("✓ Card created")

def booking():
    print("\nAvailable properties:\n")
    props = list_available_properties()
    if not props:
        print("(No available properties)")
        return

    for p in props:
        print(f"[{p['property_id']}] {p['description']} — ${p['rental_price']}/mo — {p['neighborhood']}")


def main():
    actions = {
        "1": ("Register user", register),
        "2": ("Add address", add_address),
        "3": ("Add credit card", add_cc),
        "4": ("Browse & book properties", booking),
        "5": ("Exit", exit)
    }

    while True:
        print("\nRENTALAPP MENU")
        for key, (desc, _) in actions.items():
            print(f"{key}) {desc}")
        
        choice = input("> ").strip()
        action = actions.get(choice)
        
        if action:
            action[1]()
            if choice != "5":
                pause()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()