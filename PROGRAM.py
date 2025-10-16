import mysql.connector
from mysql.connector import Error

# Function to create a MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       
            password="2007",  
            database="HotelDB" 
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL:", e)
        exit()

# Function to fetch staff details from the database
def fetch_staff():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Staff"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

# Function to fetch room availability details from the database
def fetch_room_availability():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Rooms WHERE available = 1"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

# Function to fetch booking details
def fetch_bookings():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Booking")
    results = cursor.fetchall()
    connection.close()
    return results

# Function to add booking to the database
def add_booking(data):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO Booking (name, phno, address, checkin, checkout, room_type, price, room_number, custid, days)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)
    connection.commit()
    connection.close()

# Function to generate a bill
def generate_bill(booking_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM Booking WHERE id = {booking_id}"
    cursor.execute(query)
    booking = cursor.fetchone()
    if booking:
        name, phno, address, checkin, checkout, room_type, price, room_number, custid, days = booking[1:]
        total_price = price * days
        print(f"\nBill for {name}:")
        print(f"Room Number: {room_number}")
        print(f"Check-in: {checkin}, Check-out: {checkout}")
        print(f"Price per Night: {price}")
        print(f"Total Amount: {total_price}")
    else:
        print("Booking not found!")
    connection.close()

# Function to delete a booking
def delete_booking(booking_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = f"DELETE FROM Booking WHERE id = {booking_id}"
    cursor.execute(query)
    connection.commit()
    connection.close()
    print("Booking deleted successfully.")

# Function to display header
def print_header(title):
    print("\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

# Login Function
def login():
    print_header("SHUBH & AMAN HOTEL LOGIN PAGE")
    password = "KVBHEL"
    attempts = 3
    
    while attempts > 0:
        print("\nOptions:")
        print("1. Enter Password")
        print("2. Forget Password")
        print("3. Contact Us")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            entered_password = input("\nEnter Password: ").strip()
            if entered_password == password:
                print("\nAccess Granted! Redirecting to Home Page...\n")
                home_page()
                return
            else:
                attempts -= 1
                print(f"Incorrect Password. {attempts} attempt(s) remaining.\n")
        elif choice == "2":
            print("\nForgot your password? Hint: The password is 'KVBHEL'.\n")
        elif choice == "3":
            print("\nContact Us:")
            print("Email: support@S&AHOTEL.com")
            print("Phone: +91 8840068892, +91 9670793634 \n")
        elif choice == "4":
            print("\nExiting the program. Goodbye!")
            exit()
        else:
            print("\nInvalid choice. Please try again.")
    
    print("\nToo many incorrect attempts! Exiting the program.")
    exit()

# Home Page Function
def home_page():
    print_header("SHUBH & AMAN HOTEL HOME PAGE")
    print("1. Booking")
    print("2. Rooms Info")
    print("3. Room Service (Menu Card)")
    print("4. Payment")
    print("5. Record")
    print("6. Generate Bill")
    print("7. Customer Details")
    print("8. Delete a Booking")
    print("9. Staff Information")
    print("10. Check Room Availability")
    print("0. Exit")
    
    choice = input("\nChoose an option (0-10): ").strip()
    
    if choice == "1":
        booking()
    elif choice == "2":
        rooms_info()
    elif choice == "3":
        restaurant()
    elif choice == "4":
        payment()
    elif choice == "5":
        record()
    elif choice == "6":
        booking_id = int(input("Enter Booking ID to generate bill: "))
        generate_bill(booking_id)
    elif choice == "7":
        customer_details()
    elif choice == "8":
        booking_id = int(input("Enter Booking ID to delete: "))
        delete_booking(booking_id)
    elif choice == "9":
        staff_info()
    elif choice == "10":
        check_room_availability()
    elif choice == "0":
        print("\nThank you for visiting SHUBH & AMAN HOTEL !")
        exit()
    else:
        print("\nInvalid choice. Returning to Home Page...")
        home_page()

# Fetch and display staff information
def staff_info():
    print_header("STAFF INFORMATION")
    staff_list = fetch_staff()
    
    if not staff_list:
        print("\nNo staff information available.\n")
        return
    
    for staff in staff_list:
        print(f"ID: {staff[0]}, Name: {staff[1]}, Role: {staff[2]}, Salary: ${staff[3]}")
        print("-" * 50)

# Check room availability
def check_room_availability():
    print_header("ROOM AVAILABILITY")
    available_rooms = fetch_room_availability()
    
    if not available_rooms:
        print("\nNo available rooms at the moment.\n")
        return
    
    print("\nAvailable Rooms:")
    for room in available_rooms:
        print(f"Room Number: {room[0]}, Type: {room[1]}, Price: ${room[2]}")
        print("-" * 50)

# Booking Function
def booking():
    print_header("BOOKING PAGE")
    name = input("Enter Name: ")
    phno = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    checkin = input("Enter Check-in Date (YYYY-MM-DD): ")
    checkout = input("Enter Check-out Date (YYYY-MM-DD): ")
    room = int(input("Enter Room Type (1, 2, 3, etc.): "))
    price = float(input("Enter Price per Night: "))
    roomno = int(input("Enter Room Number: "))
    custid = input("Enter Customer ID: ")
    days = int(input("Enter Number of Days: "))
    
    # Store booking in the database
    booking_data = (name, phno, address, checkin, checkout, room, price, roomno, custid, days)
    add_booking(booking_data)
    print("\nBooking successfully added!")

# Function to display all booking records
def record():
    print_header("RECORD PAGE")
    bookings = fetch_bookings()
    if not bookings:
        print("No bookings found.\n")
        return
    
    for booking in bookings:
        print(f"ID: {booking[0]}, Name: {booking[1]}, Phone: {booking[2]}, Address: {booking[3]}")
        print(f"Check-in: {booking[4]}, Check-out: {booking[5]}, Room: {booking[6]}, Price: {booking[7]}")
        print(f"Room Number: {booking[8]}, Customer ID: {booking[9]}, Days: {booking[10]}")
        print("-" * 50)

# Placeholder Functions
def rooms_info():
    print_header("ROOMS INFORMATION")
    print("Room Types and Prices:")
    print("1. Single Room - Rs1000 per night")
    print("2. Double Room - Rs2000 per night")
    print("3. Suite - Rs3000 per night")
    print("4. DELUX Suite - Rs5000 per night")
    print("Contact the front desk for more details.\n")

def restaurant():
    print_header("ROOM SERVICE - MENU CARD")
    print("Menu:")
    print("1. Pasta - Rs200")
    print("2. Indian Thali - Rs900")
    print("3. Chinese Thali - Rs500")
    print("4. Salad - Rs100")
    print("For orders, call room service.\n")

def payment():
    print_header("PAYMENT PAGE")
    print("Payments can be made at the front desk or through online portals.\n")
    print("We accept cash, credit card, and UPI.\n")

def customer_details():
    print_header("CUSTOMER DETAILS")
    customer_id = input("Enter Customer ID to fetch details: ")
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Booking WHERE custid = '{customer_id}'")
    result = cursor.fetchone()
    if result:
        print(f"Customer Name: {result[1]}, Phone: {result[2]}, Address: {result[3]}")
        print(f"Booking Dates: {result[4]} to {result[5]}, Room: {result[6]}")
    else:
        print("No customer found with the given ID.")
    connection.close()

# Start the program with the login function
if __name__ == "__main__":
    login()
