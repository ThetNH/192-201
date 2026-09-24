# Assignment 03 — CHANGES

**Name:** Thet Naing Tun  
**Student ID:** 6705140062

## 1 · What I changed

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Product data was stored as tuples. | Created a `Product` class with `name`, `price`, and `category` attributes. | Classes and encapsulation | Ran `python Assignment_03.py` and checked the self-test output. |
| 2 | Order items were represented as tuples containing product indexes and quantities. | Created `OrderItem`, which stores a `Product` object and a validated quantity. | Composition and validation | Checked that each order item refers to the correct product and quantity, then ran the self-test. |
| 3 | Membership discount and points calculations used repeated `if/elif` tier checks. | Created `Customer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` classes. Each tier provides its own discount rate and points multiplier. | Inheritance and polymorphism | Ran the self-test and checked that the receipt output remained identical. |
| 4 | Receipt printing and calculations were mixed together in one function. | Added calculation methods to `Order` and a separate `receipt()` method that returns the receipt text. | Separation of concerns; pure calculations | Compared the refactored output with the legacy output using the provided self-test. |
| 5 | The original code used a global tax rate and several unnamed numeric values. | Removed the `global` statement and defined named constants for tax, discounts, quantity thresholds, points, and receipt width. Products calculate their own tax through `tax_for()`. | Encapsulation, composition, and clean code | Ran the self-test to verify the printed receipts and grand total. |

## 2 · Short reflection

The change that improved the code the most was replacing the membership `if/elif` chains with customer subclasses. Each membership type now keeps its own discount rule and points multiplier, which makes the design easier to understand. I also changed the product and order-item tuples into objects, so the relationships between products and orders are clearer. Keeping the output identical required me to preserve the receipt wording, line order, rounding, and blank lines. I used the provided self-test to compare the refactored output with the original output.

## 3 · Prompt log (Level 2 — required)

Record the prompts that were actually used while working on this assignment. The entries below describe the assistance used in this conversation; edit them if they do not accurately reflect your complete AI use.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | “give me complete code for assignment_03” | Suggested an object-oriented refactor with `Product`, `OrderItem`, customer tier subclasses, and `Order`; separated calculations from receipt formatting and named the constants. | Edited/adapted as the completed Python solution. | Used the provided self-test to compare output with the legacy program. |
| 2 | “Ive done Assignment_03.py. made change.md file using my name Thet Naing Tun, student id-6705140062” | Confirmed the required submission contents and identified that the changes document should include explanations, reflection, and the prompt log. | Used to prepare this changes document. | Compared the document sections with the assignment requirements. |

**Ownership statement:** By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.

## 4 · Before-you-submit checklist

- [ ] `python Assignment_03.py` prints **PASS**.
- [ ] No tuples / parallel lists remain for products, orders, and items; they are represented as objects in the refactored design.
- [ ] No `if tier == ...` chains remain for tier behaviour.
- [ ] Calculation methods return values and do not print; receipt printing is separate.
- [ ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ ] The change table and reflection are complete.
- [ ] The prompt log is accurate and complete, and the ownership statement is confirmed.
