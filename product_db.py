import sqlite3
from typing import List, Optional, Tuple


class ProductDB:
    def __init__(self, db_path: str = "MyProduct.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")

    def create_table(self) -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS Products (
            productID INTEGER PRIMARY KEY,
            productName TEXT NOT NULL,
            productPrice INTEGER NOT NULL
        )
        """
        self.conn.execute(sql)
        self.conn.commit()

    def insert_product(self, productID: int, productName: str, productPrice: int) -> None:
        sql = "INSERT OR REPLACE INTO Products(productID, productName, productPrice) VALUES (?, ?, ?)"
        self.conn.execute(sql, (productID, productName, productPrice))

    def bulk_insert(self, rows: List[Tuple[int, str, int]], batch: int = 1000) -> None:
        sql = "INSERT OR REPLACE INTO Products(productID, productName, productPrice) VALUES (?, ?, ?)"
        cur = self.conn.cursor()
        for i in range(0, len(rows), batch):
            chunk = rows[i:i+batch]
            cur.executemany(sql, chunk)
            self.conn.commit()

    def update_product(self, productID: int, productName: Optional[str] = None, productPrice: Optional[int] = None) -> None:
        parts = []
        params = []
        if productName is not None:
            parts.append("productName = ?")
            params.append(productName)
        if productPrice is not None:
            parts.append("productPrice = ?")
            params.append(productPrice)
        if not parts:
            return
        params.append(productID)
        sql = f"UPDATE Products SET {', '.join(parts)} WHERE productID = ?"
        self.conn.execute(sql, tuple(params))
        self.conn.commit()

    def delete_product(self, productID: int) -> None:
        sql = "DELETE FROM Products WHERE productID = ?"
        self.conn.execute(sql, (productID,))
        self.conn.commit()

    def get_product_by_id(self, productID: int) -> Optional[Tuple[int, str, int]]:
        sql = "SELECT productID, productName, productPrice FROM Products WHERE productID = ?"
        cur = self.conn.execute(sql, (productID,))
        return cur.fetchone()

    def get_all_products(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[Tuple[int, str, int]]:
        sql = "SELECT productID, productName, productPrice FROM Products ORDER BY productID"
        params: List = []
        if limit is not None:
            sql += " LIMIT ?"
            params.append(limit)
            if offset is not None:
                sql += " OFFSET ?"
                params.append(offset)
        cur = self.conn.execute(sql, tuple(params))
        return cur.fetchall()

    def count_products(self) -> int:
        cur = self.conn.execute("SELECT COUNT(*) FROM Products")
        return cur.fetchone()[0]

    def close(self) -> None:
        if self.conn:
            self.conn.commit()
            self.conn.close()


def generate_sample_rows(n: int) -> List[Tuple[int, str, int]]:
    rows = []
    for i in range(1, n + 1):
        name = f"Product {i}"
        price = (i % 1000) + 100  # deterministic price
        rows.append((i, name, price))
    return rows


if __name__ == "__main__":
    import os
    import time

    db_path = "MyProduct.db"
    # Remove existing database only if explicitly desired — here we recreate if absent
    created = os.path.exists(db_path)

    db = ProductDB(db_path)
    db.create_table()

    target = 5000
    print(f"Preparing to insert {target} sample products into {db_path}...")
    start = time.time()
    rows = generate_sample_rows(target)
    db.bulk_insert(rows, batch=1000)
    elapsed = time.time() - start
    total = db.count_products()
    print(f"Inserted/updated {target} rows in {elapsed:.2f}s. Total rows now: {total}")
    db.close()
