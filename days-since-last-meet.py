from datetime import datetime

while True:
    last_date_input = input("Enter the last date we met (YYYY-MM-DD): ").strip()

    try:
        specific_date = datetime.strptime(last_date_input, "%Y-%m-%d").date()
        today = datetime.today().date()

        if specific_date > today:
            print("⚠️ The date you entered is in the future. Please enter a past date.")
        else:
            days_difference = (today - specific_date).days
            print(f"\nIt has been {days_difference} day{'s' if days_difference != 1 else ''} since we last met. Hope you're doing well. 🙃")
            break  # Exit the loop when a valid date is entered

    except ValueError:
        print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
