from flask import Flask, render_template, request, redirect
import sqlite3 as sql



DB_path = "Database/data_source.db"

def get_connection():
    con = sql.connect(DB_path)
    return con

def list_moodboards():
    conn = get_connection()
    cursor = conn.cursor()
    # Run query
    cursor.execute("SELECT Moodboard_name, favourite, recent, Moodboard_picture FROM moodboards")
    rows = cursor.fetchall()     
    conn.close()
    return rows

def add_moodboard(name, favourite, recently_opened, image):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO moodboards (Moodboard_name, favourite, recent, Moodboard_picture) VALUES (?, ?, ?, ?)",
        (name, bool(favourite), bool(recently_opened), image)
    )
    conn.commit()
    conn.close()
