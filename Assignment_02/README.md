# Assignment_02 — CampusWheels

## Files

- `rental.py` — contains the `Vehicle`, `Renter`, `ElectricCar`, and `Motorbike` classes.
- `main.py` — demonstrates that the classes and methods work.

## How to Run

Make sure Python 3 is installed.

Open a terminal in this folder and run:

```bash
python main.py
```

If your computer uses `python3`, run:

```bash
python3 main.py
```

## What the Program Demonstrates

- A new vehicle starts as available.
- `rent()` changes a vehicle to rented.
- `return_vehicle()` changes it back to available.
- `Renter` validates the name and license number with properties.
- Invalid renter data raises and catches `ValueError`.
- `ElectricCar` and `Motorbike` inherit from `Vehicle`.
- A mixed list demonstrates polymorphism because each vehicle type has its own `__str__()`.
