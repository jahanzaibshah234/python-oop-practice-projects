# Inventory Management

A simple command-line Inventory Management application in Python for tracking products, quantities, and value. Data is persisted to a CSV file (`inventory.csv`) between runs.

---

## Features

- Add, remove, and search products by ID
- Display all products
- Compute total inventory value
- Low-stock report (default threshold: 5)
- Save/load inventory from `inventory.csv`
- Minimal dependencies — uses Python standard library only

---

## Requirements

- Python 3.10.0+
- No external packages required

---

## Files

- `inventory_management_system.py` — main program (save your provided code to this file)
- `inventory.csv` — auto-created/updated by the program for persistence

---

## Installation

1. Clone or copy the repository (or create a new folder).
2. Place the provided code into a file named `inventory_management_system.py`.

---

## Usage

Run the program from the command line:

```bash
python inventory_management_system.py
```

When launched, a numeric menu will be shown:

1. Add Product
2. Remove Product
3. Search Product
4. Display Product
5. Total Inventory Value
6. Low Stock Report
7. Save & Exit

Follow the prompts to interact with the inventory. Enter the requested IDs, names, categories, prices, and quantities.

---

## CSV Persistence

- On startup the program looks for `inventory.csv` in the current directory and loads products from it if present.
- On "Save & Exit" the program writes current inventory to `inventory.csv` with the header:
  ```
  product_id,name,category,price,quantity
  ```
- Example `inventory.csv` content:
  ```
  product_id,name,category,price,quantity
  1,Pen,Stationery,1.5,100
  2,Notebook,Stationery,3.0,50
  ```

---

## Design Notes

- Product is represented by the `Product` class with:
  - Attributes: `product_id`, `name`, `category`, `price`, `quantity`
  - Methods: `update_quantity`, `get_value`, `is_low_stock`, `to_csv`, and `__str__`
- Inventory is represented by the `Inventory` class which:
  - Maintains an in-memory list of `Product` objects
  - Implements add/remove/search/display/total/low-stock/save/load operations
- The low-stock threshold defaults to 5 but can be changed by modifying the `low_stock_report` call.

---

## Example Session

1. Run:
   ```bash
   python inventory.py
   ```
2. Add a product:
   - Choose `1`
   - Enter ID: `101`
   - Name: `Water Bottle`
   - Category: `Home`
   - Price: `12.5`
   - Quantity: `20`
3. View inventory with option `4`
4. Save & Exit with option `7` — this writes `inventory.csv`

---
