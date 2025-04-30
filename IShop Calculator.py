# range 
#  range (start, stop)
# range (stop)
# range(start, stop, step)

# ----------------- 1 ---------------
# print("*** Welcome to the multiplication table ***")
# number = int(input("Enter a number: "))
# print(f"\nMultiplicatio table for {number}:\n")
# for number_range in range(1,11) :
#     multiple = number * number_range
#     print(f"{number_range} X {number}  = {multiple}")

name_item_list = []
item_price = []
print("\n***** Welcome to iShop calculator ****\n")
items_list = int(input("How many items are there in your basket today? "))
print("\nLet's get to counting them .... ")
for number in range(1,items_list+1):
    name_item = input(f"Please tell me the name of the item number {number} ")
    name_item_list.append(name_item)
    price = float(input(f"What is the price of {name_item}\n$"))
    item_price.append(price)
basket_items = input("Would you like to see your entire basket items? ").lower()
if basket_items == "yes":
    print(name_item_list)
    item_cost = input("Would you like to see how much it'll cost? ").lower()
    if item_cost == "yes":
        print("Buying these items will cost:")
        print(sum(item_price))
    else:
        input("type enter to exit ....")
else:
    input("type enter to exit ....")















