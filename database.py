import sqlite3

DATABASE = "chatbot.db"


def init_db():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_logs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_message TEXT,

        bot_response TEXT,

        sentiment TEXT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_chat(user_message, bot_response, sentiment):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_logs
    (user_message, bot_response, sentiment)

    VALUES (?, ?, ?)
    """,
    (user_message, bot_response, sentiment))

    conn.commit()
    conn.close()


def get_all_chats():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM chat_logs
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_chat_count():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM chat_logs
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count