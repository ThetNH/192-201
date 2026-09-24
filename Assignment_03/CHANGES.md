# Assignment 03 — CHANGES

**Name:** Thet Naing Tun  **Student ID:** 6705140062

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Product data stored as a bare tuple | A `Product` class with validated attributes and a `tax_for()` method | Classes / encapsulation | Compared the refactored output with the original expected output |
| 2 | Order items represented with separate values | An `OrderItem` class that stores a product and quantity and calculates its line total | Classes / composition | Checked line totals and order totals against the expected calculations |
| 3 | Customer tiers handled with repeated conditional logic | A `Customer` base class with `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses | Inheritance / polymorphism | Checked that each tier applies its correct discount and points multiplier |
| 4 | Calculation logic mixed with printing | Calculation methods return values; receipt and main functions handle display | Separation of concerns / encapsulation | Checked that calculations return the expected values and receipt output remains consistent |
| 5 | Magic numbers and loosely validated state | Named constants and constructor validation for products, items, and customers | Encapsulation / validation | Reviewed the constants and validation rules and checked valid inputs still work |

## 2 · Short reflection (4–6 sentences)

The change that improved the code the most was using customer subclasses for the membership tiers. It keeps tier-specific rules in the correct classes and makes the code easier to understand and extend. Using `Product` and `OrderItem` objects also makes the relationship between products and orders clearer. Keeping the behaviour identical meant I had to be careful not to change the discount, tax, total, or points calculations. I also needed to keep calculation methods separate from printing so their returned values could be checked.

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | “Help me complete Assignment 03 and follow the instructions.” | Helped me change the original code into classes for products, customers, orders, and order items. | Edited | I checked the code and compared it with the assignment requirements. |
| 2 | “Help me change the customer membership system using classes.” | Suggested using different customer classes for different membership levels and their discounts and points. | Edited | I checked the discount and points rules for each membership level. |
| 3 | “Help me organize the code and make sure it follows the assignment requirements.” | Helped separate the calculations from printing, add input checks, and use named constants instead of magic numbers. | Edited | I reviewed the code and will run the program to check that it works as expected. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.

