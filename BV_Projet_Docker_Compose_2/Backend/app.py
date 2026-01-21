from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_PATH = '/app/data/database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists('/app/data'):
        os.makedirs('/app/data')
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
    conn.close()

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(row) for row in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (data['username'], data['password']))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    conn = get_db_connection()
    conn.execute('UPDATE users SET username = ?, password = ? WHERE id = ?', (data['username'], data['password'], id))
    conn.commit()
    conn.close()
    return jsonify({"status": "updated"})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)