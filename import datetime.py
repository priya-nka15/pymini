import datetime
import uuid

class Hotel:
    def __init__(self):
        # Initialize with some default data
        self.rooms = {
            "101": {"type": "Standard", "price": 100, "available": True},
            "102": {"type": "Standard", "price": 100, "available": True},
            "201": {"type": "Deluxe", "price": 200, "available": True},
            "202": {"type": "Deluxe", "price": 200, "available": True},
            "301": {"type": "Suite", "price": 300, "available": True}
        }
        
        self.menu = {
            "F1": {"name": "Burger", "price": 15, "category": "Food"},
            "F2": {"name": "Pizza", "price": 20, "category": "Food"},
            "F3": {"name": "Pasta", "price": 18, "category": "Food"},
            "D1": {"name": "Water", "price": 2, "category": "Drink"},
            "D2": {"name": "Soda", "price": 3, "category": "Drink"},
            "D3": {"name": "Coffee", "price": 4, "category": "Drink"},
            "S1": {"name": "Laundry", "price": 25, "category": "Service"},
            "S2": {"name": "Room Cleaning", "price": 15, "category": "Service"}
        }
        
        self.guests = {}
        self.bookings = {}
        self.orders = {}
        self.bills = {}

    def register_guest(self, name, phone):
        """Register a new guest and return guest_id"""
        guest_id = str(uuid.uuid4())[:8]
        self.guests[guest_id] = {
            "name": name,
            "phone": phone
        }
        return guest_id

    def available_rooms(self, room_type=None):
        """Get list of available rooms, optionally filtered by type"""
        available = []
        for room_no, room in self.rooms.items():
            if room["available"] and (room_type is None or room["type"] == room_type):
                available.append(room_no)
        return available

    def check_in(self, guest_id, room_no, days):
        """Check in a guest to a room"""
        if guest_id not in self.guests:
            return False, "Guest not found"
            
        if room_no not in self.rooms:
            return False, "Room not found"
            
        room = self.rooms[room_no]
        if not room["available"]:
            return False, "Room not available"
            
        # Create booking
        booking_id = str(uuid.uuid4())[:8]
        check_in_date = datetime.datetime.now()
        check_out_date = check_in_date + datetime.timedelta(days=days)
        
        self.bookings[booking_id] = {
            "guest_id": guest_id,
            "room_no": room_no,
            "check_in": check_in_date,
            "check_out": check_out_date,
            "days": days,
            "active": True
        }
        
        # Update room status
        self.rooms[room_no]["available"] = False
        
        return True, booking_id

    def check_out(self, booking_id):
        """Check out a guest and generate bill"""
        if booking_id not in self.bookings:
            return False, "Booking not found"
            
        booking = self.bookings[booking_id]
        if not booking["active"]:
            return False, "Booking already closed"
            
        room_no = booking["room_no"]
        guest_id = booking["guest_id"]
        days = booking["days"]
        
        # Calculate room charges
        room_charge = self.rooms[room_no]["price"] * days
        
        # Calculate food and service charges
        food_charge = 0
        service_charge = 0
        
        for order_id, order in self.orders.items():
            if order["booking_id"] == booking_id:
                item = self.menu[order["item_id"]]
                if item["category"] in ["Food", "Drink"]:
                    food_charge += item["price"] * order["quantity"]
                else:
                    service_charge += item["price"] * order["quantity"]
        
        # Create bill
        bill_id = str(uuid.uuid4())[:8]
        total = room_charge + food_charge + service_charge
        
        self.bills[bill_id] = {
            "booking_id": booking_id,
            "guest_id": guest_id,
            "room_no": room_no,
            "room_charge": room_charge,
            "food_charge": food_charge,
            "service_charge": service_charge,
            "total": total,
            "date": datetime.datetime.now(),
            "paid": False
        }
        
        # Close booking and make room available
        booking["active"] = False
        self.rooms[room_no]["available"] = True
        
        return True, bill_id

    def place_order(self, booking_id, item_id, quantity=1):
        """Place an order for food or service"""
        if booking_id not in self.bookings:
            return False, "Booking not found"
            
        booking = self.bookings[booking_id]
        if not booking["active"]:
            return False, "Booking is not active"
            
        if item_id not in self.menu:
            return False, "Item not found"
            
        order_id = str(uuid.uuid4())[:8]
        self.orders[order_id] = {
            "booking_id": booking_id,
            "item_id": item_id,
            "quantity": quantity,
            "time": datetime.datetime.now()
        }
        
        return True, order_id

    def get_bill_details(self, bill_id):
        """Get detailed bill information"""
        if bill_id not in self.bills:
            return None
            
        bill = self.bills[bill_id]
        guest = self.guests[bill["guest_id"]]
        
        details = {
            "bill_id": bill_id,
            "guest_name": guest["name"],
            "room_no": bill["room_no"],
            "room_charge": bill["room_charge"],
            "food_charge": bill["food_charge"],
            "service_charge": bill["service_charge"],
            "total": bill["total"],
            "date": bill["date"].strftime("%Y-%m-%d %H:%M"),
            "paid": bill["paid"]
        }
        
        return details

    def pay_bill(self, bill_id):
        """Mark a bill as paid"""
        if bill_id not in self.bills:
            return False, "Bill not found"
            
        self.bills[bill_id]["paid"] = True
        return True, "Payment successful"

    def display_menu(self):
        """Display all menu items"""
        print("\n===== MENU =====")
        print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Item", "Price", "Category"))
        print("-" * 40)
        for item_id, item in self.menu.items():
            print("{:<5} {:<15} ${:<9.2f} {:<10}".format(
                item_id, item["name"], item["price"], item["category"]))


# Example usage
def main():
    hotel = Hotel()
    
    # Display welcome message
    print("===== HOTEL MANAGEMENT SYSTEM =====")
    
    # Display menu
    hotel.display_menu()
    
    # Register a guest
    guest_name = input("\nEnter guest name: ")
    guest_phone = input("Enter guest phone: ")
    guest_id = hotel.register_guest(guest_name, guest_phone)
    print(f"Guest registered with ID: {guest_id}")
    
    # Show available rooms
    available = hotel.available_rooms()
    print("\nAvailable Rooms:")
    for room_no in available:
        room = hotel.rooms[room_no]
        print(f"Room {room_no}: {room['type']} - ${room['price']}/night")
    
    # Check in
    room_choice = input("\nEnter room number to book: ")
    days = int(input("Enter number of days to stay: "))
    success, result = hotel.check_in(guest_id, room_choice, days)
    
    if success:
        booking_id = result
        print(f"Check-in successful! Booking ID: {booking_id}")
        
        # Place some orders
        while True:
            order_choice = input("\nPlace an order? (y/n): ").lower()
            if order_choice != 'y':
                break
                
            hotel.display_menu()
            item_id = input("Enter item ID: ")
            quantity = int(input("Enter quantity: "))
            
            success, result = hotel.place_order(booking_id, item_id, quantity)
            if success:
                print(f"Order placed successfully! Order ID: {result}")
            else:
                print(f"Error: {result}")
        
        # Check out
        checkout_choice = input("\nProceed to check out? (y/n): ").lower()
        if checkout_choice == 'y':
            success, bill_id = hotel.check_out(booking_id)
            
            if success:
                print("\n===== BILL =====")
                bill = hotel.get_bill_details(bill_id)
                print(f"Bill ID: {bill['bill_id']}")
                print(f"Guest: {bill['guest_name']}")
                print(f"Room: {bill['room_no']}")
                print(f"Room Charges: ${bill['room_charge']:.2f}")
                print(f"Food & Beverage: ${bill['food_charge']:.2f}")
                print(f"Services: ${bill['service_charge']:.2f}")
                print(f"Total: ${bill['total']:.2f}")
                
                # Pay bill
                payment = input("\nPay bill now? (y/n): ").lower()
                if payment == 'y':
                    hotel.pay_bill(bill_id)
                    print("Payment successful! Thank you for staying with us.")
    else:
        print(f"Error: {result}")


if __name__ == "__main__":
    main()