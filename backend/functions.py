import sqlite3
# from cs50 import SQL
from flask import request,session

def execute_query(database,query, data=None, fetch=False, return_id=None, is_dict=False):
    # Create a connection to the database
    # with sqlite3.connect('optica.db') as conn:
    with sqlite3.connect(database) as conn:

        # Set row factory for dictionary-like access to rows, if needed
        if is_dict:
            conn.row_factory = sqlite3.Row

        # Create a cursor object from the connection
        cur = conn.cursor()
        
        # Execute query with or without data
        if data is None:
            cur.execute(query)
        elif isinstance(data, (tuple, list)):
            cur.execute(query, data)  # `data` is already a tuple or list
        else:
            cur.execute(query, (data,))  # Single value, wrap in a tuple
        
        # Commit changes if it's an INSERT, UPDATE, or DELETE operation
        if not fetch:
            conn.commit()

        # For SELECT queries, fetch results if `fetch` is True
        if fetch:
            rows = cur.fetchall()
            if is_dict:
                return [dict(row) for row in rows]  # Convert Row objects to dictionaries
            return rows if rows else []

        # For INSERT queries, return the last inserted row ID if `return_id` is True
        if return_id:
            return cur.lastrowid
        
        # For UPDATE and DELETE, or queries that don’t need to return data
        return None