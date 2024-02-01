"""Server config"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from routers.todos_routes import todos_routes
from routers.auth_routes import auth_routes
from database.db_access import DatabaseAccess
from config.sql_queries import SqlQuery


DatabaseAccess.execute_non_returning_query(SqlQuery.CREATE_CRED_TABLE)
DatabaseAccess.execute_non_returning_query(SqlQuery.CREATE_TODO_TABLE)
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(todos_routes)
app.include_router(auth_routes)
