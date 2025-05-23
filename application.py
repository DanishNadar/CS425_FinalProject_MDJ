from db_functions import *

def main():

    # Create a user
    email = input("Enter your email: ")
    name = input("Enter your name: ")
    user_type = input("Are you an AGENT or RENTER? ").upper()
    
    if create_user(email, name, user_type):
        print("User created successfully!")
        
        if user_type == "AGENT":
            # Create agent profile
            job_title = input("Enter your job title: ")
            agency = input("Enter your agency: ")
            phone = input("Enter your phone number (e.g., +1234567890): ")
            
            if create_agent(email, job_title, agency, phone):
                print("Agent profile created successfully!")
            else:
                print("Failed to create agent profile.")
        
        elif user_type == "RENTER":
            # Create renter profile
            move_in_date = input("Enter desired move-in date (YYYY-MM-DD): ")
            location = input("Enter preferred location: ")
            budget = float(input("Enter your budget: "))
            
            if create_renter(email, move_in_date, location, budget):
                print("Renter profile created successfully!")
            else:
                print("Failed to create renter profile.")
    else:
        print("Failed to create user.")
