# • Reads 2 csv files: ”stores.csv” and ”shopping list.csv” (”stores.csv” will contain 3 columns: the store, the product
# and the quantity, ex: ”Lidl”, ”donuts” and ”7”; ”shopping list.csv” will contain 2 columns: the product and the
# quantity, ex: ”donuts”, ”12”) → 5 pts
# • Displays a list of all unique stores, sorted by their frequency. In case of a tie it will be sorted by sum of the quantities
# of all products, and then in case of a tie again, in reverse alphabetical order → 10 pts
# • Helps you by doing the following task: visit the shops exactly in the order of the list above, and when a product
# from your list is found, buy it (pay attention to the quantity, and to the fact that you can buy a certain product
# from several shops). Create a dictionary as ”key: value”, where the key will be the product and the value will be
# the shop and the quantity taken from that shop → 15 pts


import os
import sys
def list(stores,shopping_list)

    counter = {}
    for root, files in os.walk(stores):
        for file in files:
            counter = os.path.splitext(stores)[1]
            if counter==''
              if number in counter:
                            counter[number] += 1
               else:
                            counter[number] = 1
                for number, count in counter.items():
                    print(f"{number}: {count}")

def main():
    stores = 'store.csv'
    shopping_list = 'shopping list.csv'
    try:
        if not os.path.exists(stores):
            print(f"Error: The file does not exist.")
            return
        if not os.path.exists(shopping_list):
            print(f"Error: The file does not exist")
            return

    except Exception as e:
        print(f"Error: {str(e)}")
        return

 if __name__ == "__main__":
     if len(sys.argv) != 2:
         print("Usage: python one.py")
     else:
         list(sys.argv[1])
