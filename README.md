TripMate – Carpooling Management System

                                A simple, beginner-friendly carpooling application built using Python. TripMate allows users to add rides, search for rides, view available rides, and optionally book seats. This project demonstrates basic data handling, modular programming, and environmental sustainability concepts.



 Table of Contents

About the Project
Features
Tech Stack
Project Structure
Setup Instructions
How to Run
Code Explanation
Sample Input & Output
Future Enhancement
screenshots
Contributing
License




About the Project

TripMate is a Python-based carpooling system developed as part of an academic EVS project.
The application aims to reduce pollution and travel costs by helping users share rides.
It provides a simple text-based menu through which users can:

Offer a ride
 Search for rides
View all rides
 Book a seat
This project is perfect for beginners learning Python functions, dictionaries, lists, and modular design.


 Features

Add a new ride with driver name, source, destination, price, and available seats.
Search rides by destination.
View all available rides.
Book seats 
Clean and simple menu-driven interface.
Beginner-friendly code structure.


Tech Stack

Component	Technology

Language	Python 3
Architecture	Modular, Menu-driven
Storage	List & Dictionary (In-memory)
Platform	Works on any device with Python installed



 Project Structure

TripMate/
│── tripmate.py
│── README.md
│── screenshots/
│     ├── add_ride_output.png
│     ├── view_rides_output.png
│     └── search_ride_output.png
└── requirements.txt (optional)



 Setup Instructions

1. Install Python

Download Python 3.8+ from:
https://www.python.org/downloads/

2. Clone the Repository

git clone https://github.com/yourusername/TripMate.git
cd TripMate

3. Run the Program

python tripmate.py

That's it! No external libraries required.



▶ How to Run

When you run the program, you will see:

1. Add Ride
2. View Rides
3. Search Ride
4. Exit
Enter your choice:

Choose an option and enter details when prompted.


 Code Explanation
1. Data Structure

Rides are stored as a list of dictionaries:

rides = [
    {
        "driver": "Karthik",
        "from": "Bhopal",
        "to": "Indore",
        "seats": 3,
        "price": 150
    }
]

2. Adding a Ride

def add_ride():
    driver = input("Driver name: ")
    from_place = input("From: ")
    to_place = input("To: ")
    seats = int(input("Seats available: "))
    price = int(input("Ride price: "))

    ride = {
        "driver": driver,
        "from": from_place,
        "to": to_place,
        "seats": seats,
        "price": price
    }
    rides.append(ride)

3. Viewing Rides

def view_rides():
    for i, ride in enumerate(rides, start=1):
        print(f"\nRide {i}:")
        print(f"Driver: {ride['driver']}")
        print(f"From: {ride['from']}")
        print(f"To: {ride['to']}")
        print(f"Seats: {ride['seats']}")
        print(f"Price: {ride['price']}")

4. Searching for a Ride

def search_ride():
    destination = input("Enter destination: ")
    found = False
    for ride in rides:
        if ride["to"].lower() == destination.lower():
            print("\nRide Found:")
            print(f"Driver: {ride['driver']}")
            print(f"From: {ride['from']}")
            print(f"Seats: {ride['seats']}")
            print(f"Price: {ride['price']}")
            found = True

    if not found:
        print("No rides available to this destination.")

5. Main Menu Loop

while True:
    print("\n1. Add Ride")
    print("2. View Rides")
    print("3. Search Ride")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_ride()
    elif choice == "2":
        view_rides()
    elif choice == "3":
        search_ride()
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again.")

 Sample Input / Output

Add Ride Example

Add a Ride
Driver name: Karthik
From: VIT Bhopal
To: Indore
Seats available: 3
Ride price: 150
Ride added successfully!

Search Ride

Enter destination: Indore
Ride Found:
Driver: Karthik
From: VIT Bhopal
Seats: 3
Price: 150

Future Enhancements

User login & authentication
Real database (MySQL / Firebase)
Mobile app version
OTP verification
Live location tracking
Ratings & reviews
Online payment gateway


Contributing

Pull requests are welcome!
Follow best coding practices and include meaningful commit messages.



 License

This project is released under the MIT License.
