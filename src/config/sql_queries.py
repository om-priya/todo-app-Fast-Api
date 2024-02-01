class SqlQuery:
    CREATE_CRED_TABLE = """CREATE TABLE IF NOT EXISTS credentials (
    user_id TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
    )"""
    INSERT_CRED_TABLE = """INSERT INTO credentials (user_id, email, password)
    VALUES (?,?,?)"""
    FETCH_USER = """SELECT user_id FROM credentials WHERE email = ? AND password = ?"""
    CREATE_TODO_TABLE = """CREATE TABLE IF NOT EXISTS todo (
    todo_id TEXT NOT NULL UNIQUE,
    priority TEXT NOT NULL,
    description TEXT,
    user_id TEXT NOT NULL,
    title TEXT NOT NULL
    )"""
    INSERT_TODO_TABLE = """INSERT INTO todo (todo_id, priority, description, user_id, title)
    VALUES (?,?,?,?,?)"""
    GET_ALL_TODO = """SELECT * FROM todo WHERE user_id = ?"""
    UPDATE_TODO = (
        """UPDATE todo SET title = ?, priority = ?, description = ? WHERE todo_id = ?"""
    )
