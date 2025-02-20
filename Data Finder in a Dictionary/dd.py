# Sample data dictionary
data_dict = {
    "101": "Alice",
    "102": "Bob",
    "103": "Charlie",
    "104": "David"
}

# User input for search
search_key = input("Enter an ID to search: ")
# Check if the key exists
if search_key in data_dict:
    print(f"✅ ID {search_key} belongs to {data_dict[search_key]}.")