from db_functions import (
    createUser, createAgent, createRenter,
    createAddress, createCC,
    listAvailableProperties, bookProperty
)

def pause():
    input("\nPress Enter to continue…")

def register():
    print("\n Register a new user")
    email = input(" Email: ")
    name = input(" Name: ")
    utype = input(" Type (AGENT/RENTER): ").upper()
    if not createUser(email, name, utype):
        print("ERROR: Failed to create user.")
        return

    if utype == "AGENT":
        print("Create agent profile")
        job = input(" Job title: ")
        agency = input(" Agency: ")
        phone = input(" Phone [+X…]: ")
        createAgent(email, job, agency, phone) and print(" ✓ Agent created")
    else:
        print("…now create renter profile")
        date = input(" Move-in date (YYYY-MM-DD): ")
        loc = input(" Preferred location: ")
        budg = float(input(" Budget: "))
        createRenter(email, date, loc, budg) and print(" ✓ Renter created")

def addAddress():
    print("\n Add an address")
    email = input(" User email to attach to: ")
    city = input(" City: ")
    state = input(" State: ")
    zipc = input(" ZIP: ")
    createAddress(email, city, state, zipc) and print(" ✓ Address created")

def addCC():
    print("\n Add a credit card")
    email = input(" User email: ")
    aid = int(input(" Billing Address ID: "))
    num = input(" Card number (16): ")
    exp = input(" Expiration (YYYY-MM-DD): ")
    ctype = input(" Type (Visa/MasterCard…): ")
    createCC(email, aid, num, exp, ctype) and print("Card created")

def booking():
    print("\n▶ Available properties:\n")
    props = listAvailableProperties()
    if not props:
        print(" (none)")
        return

    for p in props:
        print(f"[{p['propertyID']}] {p['description']} — ${p['rentalPrice']}/mo — {p['neighborhood']}")

    pid = int(input("\nEnter propertyID to book: "))
    renter = input("Your renter email: ")
    card = int(input("Which cardID to use: "))
    if bookProperty(pid, renter, card):
        print("Booking successful!")
    else:
        print("Booking failed.")

def main():
    actions = {
        "1": ("Register user", register),
        "2": ("Add address", addAddress),
        "3": ("Add card", addCC),
        "4": ("Browse & book", booking),
        "5": ("Exit", exit)
    }

    while True:
        print("\n RENTALAPP ")
        for k,(desc,_) in actions.items():
            print(f" {k}) {desc}")
        choice = input("> ").strip()
        action = actions.get(choice)
        if action:
            action[1]()
            if choice != "5":
                pause()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
