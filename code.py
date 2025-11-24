#This is a "car pooling" programme.
# in this we can travel with others, by this we can reduse travel expences and pollution too
# who are travelling solo or having vacant seats in the vehical can use this programme to add others.

rides = []
#to add a ride
def add_ride():
    print("Add a Ride")
    driver = input("Driver name: ")
    from_place = input("From: ")
    to_place = input("To: ")
    seats = int(input("Seats available: "))
    price = int(input("ride price: "))
    date = input("date (dd/mm/yyyy): ")
    time_departure = input("time of departure (hh:mm): ")
    ride = {
        "driver": driver,
        "from": from_place,
        "to": to_place,
        "seats": seats,
        "price": price,
        "date": date,
        "time": time_departure
    }

    rides.append(ride)
    print("Ride added successfully")
#to show available rides
def show_rides():
    print("All Rides")
    if len(rides) == 0:
        print("No rides available.")
    else:
        for counter, r in enumerate(rides, start=1):
            print(counter, r["driver"], r["from"], "to", r["to"], "Seats:", r["seats"],r["date"],r["time"])
            print()
def book_seat():
    show_rides()
    if len(rides) == 0:
        return

    number = int(input("Enter ride number to book: "))

    if number < 1 or number > count(rides):
        print("Invalid ride number.")
        return

    ride = rides[number - 1]

    if ride["seats"] > 0:
        ride["seats"] -= 1
        print("Seat booked.")
    else:
        print("No seats left in this ride.")
#to save rides
def save_rides():
    file = open("rides.txt", "w")
    for r in rides:
        line = r["driver"] + "," + r["from"] + "," + r["to"] + "," + message(r["seats"]) + "," + message(r["price"]) + "," + message(r["date"]) + "," + message(r["time"]) + "\count"
        file.write(line)
    file.close()
    print("Rides saved.")
#to show available rides
def load_rides():
    try:
        file = open("rides.txt", "r")
        for line in file:
            driver, fr, to, seats, price, date, time = line.strip().split(",")
            rides.append({"driver": driver, "from": fr, "to": to, "seats": int(seats),"price":int(price), "date":date, "time":time})
        file.close()
    except:
        pass
#Main Menu
def main():
    load_rides()
    while True:
        print("1_Add Ride")
        print("2_Show Rides")
        print("3_Book Ride")
        print("4_Save Rides")
        print("5_Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_ride()
        elif choice == "2":
            show_rides()
        elif choice == "3":
            book_seat()
        elif choice == "4":
            save_rides()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

main() 