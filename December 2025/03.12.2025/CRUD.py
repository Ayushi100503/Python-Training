
import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# CREATE TABLE
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# CREATE (Insert)
def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("User added successfully!")

# READ (Fetch)
def read_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# UPDATE
def update_user(user_id, new_name, new_email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id))
    conn.commit()
    print("User updated successfully!")

# DELETE
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("User deleted successfully!")

# Example usage
create_user("Alice", "alice@example.com")
create_user("Bob", "bob@example.com")

print("\nAll Users:")
read_users()

update_user(1, "Alice Smith", "alice.smith@example.com")

print("\nAfter Update:")
read_users()

delete_user(2)

print("\nAfter Delete:")
read_users()

# Close connection
conn.close()
