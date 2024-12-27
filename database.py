import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def crate_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS complaints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone_or_instagram  TEXT NUT NULL,
                    complaint_comment TEXT NUT NULL

                )
            """)
            conn.commit()

    def save_dialog(self, data):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
            """
                INSERT INTO complaints (name, phone_or_instagram, complaint_comment)
                VALUES (?, ?, ?)
            """,
            (data["name"], data["phone_or_instagram"],
             data["complaint_comment"])
            )
