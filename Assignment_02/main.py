from rental import Vehicle, Renter, ElectricCar, Motorbike


def main():
    # Create vehicles
    car = Vehicle("Toyota", "Yaris", "1AB234")
    electric_car = ElectricCar("Tesla", "Model 3", "2EV567", 60)
    motorbike = Motorbike("Honda", "Click", "3MB890", 125)

    # Create a renter
    renter = Renter("Alex", 12345)

    print("=== Vehicles ===")
    print(car)
    print(electric_car)
    print(motorbike)

    # Rent and return a vehicle
    print("\n=== Rent and Return ===")
    car.rent()
    renter.rented.append(car)
    print("After renting:")
    print(car)

    car.return_vehicle()
    if car in renter.rented:
        renter.rented.remove(car)
    print("After returning:")
    print(car)

    # Show the renter's rented list
    print("\n=== Renter ===")
    print(f"Name: {renter.name}")
    print(f"License: {renter.license_no}")
    print(f"Rented vehicles: {renter.rented}")

    # Demonstrate ValueError for bad renter data
    print("\n=== Error Handling ===")

    try:
        Renter("", 12345)
    except ValueError as error:
        print(f"Bad name caught: {error}")

    try:
        Renter("Alex", 0)
    except ValueError as error:
        print(f"Bad license caught: {error}")

    try:
        renter.name = ""
    except ValueError as error:
        print(f"Bad name change caught: {error}")

    try:
        renter.license_no = -10
    except ValueError as error:
        print(f"Bad license change caught: {error}")

    # Demonstrate inheritance and polymorphism
    print("\n=== Polymorphism ===")
    vehicles = [
        Vehicle("Toyota", "Corolla", "4AB111"),
        ElectricCar("Nissan", "Leaf", "5EV222", 40),
        Motorbike("Yamaha", "NMAX", "6MB333", 155),
    ]

    for vehicle in vehicles:
        print(vehicle)


if __name__ == "__main__":
    main()
