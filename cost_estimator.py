def main():
    print("=======================================")
    print("   Welcome to the Cloud Cost Estimator ")
    print("=======================================")
    
    # This while loop keeps the program running until the user types 'no'
    calculate_again = 'yes'
    
    while calculate_again.lower() == 'yes':
        print("\nWhich cloud service would you like to estimate?")
        print("1. Virtual Server (Compute)")
        print("2. Storage (Object Storage)")
        print("3. Database")
        
        # Get user's choice
        choice = input("Enter the number of your choice (1, 2, or 3): ")
        
        # Variables to store the final calculation details
        service_name = ""
        monthly_cost = 0.0
        
        #  LOGIC FOR VIRTUAL SERVER 
        if choice == '1':
            service_name = "Virtual Server"
            
            servers = int(input("How many servers do you need? "))
            hours_per_day = int(input("How many hours per day will they run? "))
            
            # Calculate cost: $0.05 per hour * hours per day * 30 days in a month * number of servers
            monthly_cost = 0.05 * hours_per_day * 30 * servers
            
        #  LOGIC FOR STORAGE 
        elif choice == '2':
            service_name = "Storage"
            
            gb_amount = int(input("How much storage do you need in GB? "))
            
            # Calculate cost: $0.02 per GB per month
            monthly_cost = 0.02 * gb_amount
            
        #  LOGIC FOR DATABASE 
        elif choice == '3':
            service_name = "Database"
            
            databases = int(input("How many databases do you need? "))
            hours_per_day = int(input("How many hours per day will they run? "))
            
            # Calculate cost: $0.08 per hour * hours per day * 30 days * number of databases
            monthly_cost = 0.08 * hours_per_day * 30 * databases
            
        # ERROR HANDLING FOR INVALID INPUT 
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue 
            
        # OUTPUT 
        print("\n---------------------------------------")
        print(f"Selected Service: {service_name}")
        # The :.2f formats the number to always show 2 decimal places (like money)
        print(f"Estimated Monthly Cost: ${monthly_cost:.2f}")
        print("---------------------------------------")
        
        # The requested extra feature tip
        print("Tip: Reduce usage hours or scale down resources to save costs!")
        
        # Ask if they want to run it again
        calculate_again = input("\nWould you like to calculate another service? (yes/no): ")

    print("\nThank you for using the Cloud Cost Estimator. Goodbye!")

# This line starts the program
main()