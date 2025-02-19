# Sample data list
data_list = ["apple", "banana", "cherry", "date", "grape"]

# User input for search
search_item = input("Enter an item to search: ").lower()

# Check if the item exists
if search_item in data_list:
    print(f"✅ '{search_item}' found in the list!")
else:
    print(f"❌ '{search_item}' not found.")
