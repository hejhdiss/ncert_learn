# fastapi_like_module.py

# Simulated Data Store (for demo purposes)
data_store = {
    "items": {1: {"name": "Item 1", "value": 100}, 2: {"name": "Item 2", "value": 200}},
    "users": {1: {"name": "John Doe", "email": "john@example.com", "token": "abc123"}},
    "files": {}
}


# -------------------------
# CRUD Operations
# -------------------------

def api_create_item(item_id: int, name: str, value: float) -> dict:
    """
    Creates an item.
    """
    if item_id in data_store["items"]:
        return {"error": "Item with this ID already exists."}
    data_store["items"][item_id] = {"name": name, "value": value}
    return {"status": "success", "item_id": item_id, "data": data_store["items"][item_id]}


def api_read_item(item_id: int) -> dict:
    """
    Reads an item by ID.
    """
    return data_store["items"].get(item_id, {"error": "Item not found"})


def api_update_item(item_id: int, name: str = None, value: float = None) -> dict:
    """
    Updates an item.
    """
    if item_id not in data_store["items"]:
        return {"error": "Item not found"}
    if name:
        data_store["items"][item_id]["name"] = name
    if value:
        data_store["items"][item_id]["value"] = value
    return {"status": "success", "updated_data": data_store["items"][item_id]}


def api_delete_item(item_id: int) -> dict:
    """
    Deletes an item.
    """
    if item_id not in data_store["items"]:
        return {"error": "Item not found"}
    del data_store["items"][item_id]
    return {"status": "success", "message": f"Item {item_id} deleted."}


# -------------------------
# User Management
# -------------------------

def api_create_user(user_id: int, name: str, email: str, token: str) -> dict:
    """
    Creates a user.
    """
    if user_id in data_store["users"]:
        return {"error": "User with this ID already exists."}
    data_store["users"][user_id] = {"name": name, "email": email, "token": token}
    return {"status": "success", "user_id": user_id, "data": data_store["users"][user_id]}


def api_read_user(user_id: int) -> dict:
    """
    Reads a user by ID.
    """
    return data_store["users"].get(user_id, {"error": "User not found"})


def api_delete_user(user_id: int) -> dict:
    """
    Deletes a user.
    """
    if user_id not in data_store["users"]:
        return {"error": "User not found"}
    del data_store["users"][user_id]
    return {"status": "success", "message": f"User {user_id} deleted."}


# -------------------------
# Authentication
# -------------------------

def api_authenticate_user(token: str) -> dict:
    """
    Simulates user authentication.
    """
    for user_id, user in data_store["users"].items():
        if user["token"] == token:
            return {"status": "authenticated", "user_id": user_id, "user_data": user}
    return {"error": "Authentication failed. Invalid token."}


# -------------------------
# File Management
# -------------------------

def api_upload_file(filename: str, content: str) -> dict:
    """
    Uploads a file.
    """
    data_store["files"][filename] = content
    return {"status": "success", "filename": filename, "message": "File uploaded successfully."}


def api_download_file(filename: str) -> dict:
    """
    Downloads a file.
    """
    if filename in data_store["files"]:
        return {"status": "success", "filename": filename, "content": data_store["files"][filename]}
    return {"error": "File not found."}


# -------------------------
# Bulk Operations
# -------------------------

def api_bulk_insert_items(items: list) -> dict:
    """
    Inserts multiple items.
    """
    errors = []
    for item in items:
        item_id = item.get("id")
        if item_id in data_store["items"]:
            errors.append({"error": f"Item ID {item_id} already exists"})
        else:
            data_store["items"][item_id] = {"name": item.get("name"), "value": item.get("value")}
    if errors:
        return {"status": "partial_success", "errors": errors}
    return {"status": "success", "message": "All items inserted successfully."}


# -------------------------
# Query Processing
# -------------------------

def api_filter_items(filter_key: str, filter_value: str) -> dict:
    """
    Filters items based on a key-value pair.
    """
    results = [
        {k: v for k, v in item.items()}
        for item in data_store["items"].values()
        if filter_key in item and str(item[filter_key]) == str(filter_value)
    ]
    return {"filter_key": filter_key, "filter_value": filter_value, "results": results or "No matches found"}


# -------------------------
# Data Export
# -------------------------

def api_export_data() -> dict:
    """
    Exports all data in the store.
    """
    return {"status": "success", "data": data_store}


# -------------------------
# Interactive User Interface
# -------------------------

def api_user_interface():
    """
    Interactive interface for module users.
    """
    while True:
        print("\nChoose an operation:")
        print("1. Create Item")
        print("2. Read Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Create User")
        print("6. Read User")
        print("7. Delete User")
        print("8. Authenticate User")
        print("9. Upload File")
        print("10. Download File")
        print("11. Bulk Insert Items")
        print("12. Filter Items")
        print("13. Export Data")
        print("14. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            item_id = int(input("Enter Item ID: "))
            name = input("Enter Item Name: ")
            value = float(input("Enter Item Value: "))
            print(api_create_item(item_id, name, value))
        elif choice == "2":
            item_id = int(input("Enter Item ID: "))
            print(api_read_item(item_id))
        elif choice == "3":
            item_id = int(input("Enter Item ID: "))
            name = input("Enter new name (leave blank to skip): ")
            value = input("Enter new value (leave blank to skip): ")
            print(api_update_item(item_id, name if name else None, float(value) if value else None))
        elif choice == "4":
            item_id = int(input("Enter Item ID: "))
            print(api_delete_item(item_id))
        elif choice == "5":
            user_id = int(input("Enter User ID: "))
            name = input("Enter User Name: ")
            email = input("Enter User Email: ")
            token = input("Enter User Token: ")
            print(api_create_user(user_id, name, email, token))
        elif choice == "6":
            user_id = int(input("Enter User ID: "))
            print(api_read_user(user_id))
        elif choice == "7":
            user_id = int(input("Enter User ID: "))
            print(api_delete_user(user_id))
        elif choice == "8":
            token = input("Enter User Token: ")
            print(api_authenticate_user(token))
        elif choice == "9":
            filename = input("Enter Filename: ")
            content = input("Enter File Content: ")
            print(api_upload_file(filename, content))
        elif choice == "10":
            filename = input("Enter Filename: ")
            print(api_download_file(filename))
        elif choice == "11":
            num_items = int(input("Enter number of items to insert: "))
            items = []
            for _ in range(num_items):
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Item Name: ")
                value = float(input("Enter Item Value: "))
                items.append({"id": item_id, "name": name, "value": value})
            print(api_bulk_insert_items(items))
        elif choice == "12":
            filter_key = input("Enter Filter Key: ")
            filter_value = input("Enter Filter Value: ")
            print(api_filter_items(filter_key, filter_value))
        elif choice == "13":
            print(api_export_data())
        elif choice == "14":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
