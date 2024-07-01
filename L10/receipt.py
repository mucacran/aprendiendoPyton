import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()
    return dictionary

def apply_discount(price, day):
    """Apply a 10% discount if today is Tuesday or Wednesday."""
    if day in ['Tuesday', 'Wednesday']:
        return price * 0.9
    return price

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        print("Inkom Emporium\n")
        
        subtotal = 0.0
        total_items = 0

        current_date_and_time = datetime.now()
        day_of_week = current_date_and_time.strftime('%A')
        
        with open('request.csv', mode='r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                prod_num = row[0]
                quantity = int(row[1])
                
                if prod_num in products_dict:
                    product_info = products_dict[prod_num]
                    product_name = product_info[1]
                    product_price = float(product_info[2])

                    discounted_price = apply_discount(product_price, day_of_week)
                    
                    print(f"{product_name}: {quantity} @ {discounted_price:.2f}")
                    
                    subtotal += discounted_price * quantity
                    total_items += quantity
                else:
                    raise KeyError(f"Error: unknown product ID in the request.csv file '{prod_num}'")
        
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax
        
        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        
        print("\nThank you for shopping at the Inkom Emporium.")
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
    
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()