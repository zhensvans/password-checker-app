import hashlib
import sqlite3
import requests

conn = sqlite3.connect('data/breached_passwords.db')


def create_table():
    cursor = conn.cursor()
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS breached_passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password_hash TEXT NOT NULL UNIQUE,
        breach_count INTEGER NOT NULL
    );
    '''
    cursor.execute(create_table_sql)
    conn.commit()
    cursor.close()


def insert_breached_password(password_hash, breach_count):
    cursor = conn.cursor()
    insert_sql = '''
    INSERT INTO breached_passwords (password_hash, breach_count)
    VALUES (?, ?);
    '''
    cursor.execute(insert_sql, (password_hash, breach_count))
    conn.commit()
    cursor.close()


def populate_database_from_api():
    for prefix in range(0, 16 ** 5):
        hex_prefix = f'{prefix:05X}'
        response = requests.get(f'https://api.pwnedpasswords.com/range/{hex_prefix}')
        if response.status_code == 200:
            data = response.text.split('\n')
            for line in data:
                parts = line.split(':')
                if len(parts) >= 2:
                    password_hash = hex_prefix + parts[0].upper()
                    breach_count = int(parts[1])
                    # Check if the password hash already exists in the database
                    if not is_password_hash_exists(password_hash):
                        insert_breached_password(password_hash, breach_count)
                    else:
                        print(f"Password hash {password_hash} already exists in the database. Skipping insertion.")
                else:
                    print(f"Ignoring invalid line: {line}")
        else:
            print(f'Failed to fetch data from API for prefix {hex_prefix}: {response.status_code}')


def is_password_hash_exists(password_hash):
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM breached_passwords WHERE password_hash = ?", (password_hash,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def is_password_breached(password):
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM breached_passwords WHERE password_hash = ?", (hashed_password,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def get_breached_count(password):
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    cursor = conn.cursor()
    cursor.execute("SELECT breach_count FROM breached_passwords WHERE password_hash = ?", (hashed_password,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else 0


create_table()
