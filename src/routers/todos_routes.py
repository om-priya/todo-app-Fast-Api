from fastapi import APIRouter, Request, Path, Form, Cookie, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from controllers.todo_controller import create_todo, get_all_todo, update_todo
from utils.jwt_handler import JwtHandler


todos_routes = APIRouter()

templates = Jinja2Templates(directory="templates")

todo_title = Annotated[str, Form()]
todo_desc = Annotated[str, Form()]
todo_priority = Annotated[str, Form()]


def get_user_id(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        return None
    print(token)
    claims = JwtHandler.decode_token(token)
    return claims["user_id"]


@todos_routes.get("/todos")
async def todos(request: Request, user_id: Annotated[str | None, Depends(get_user_id)]):
    if not user_id:
        return RedirectResponse(url=request.url_for("get_login"), status_code=302)
    todos = get_all_todo(user_id)
    return templates.TemplateResponse("home.html", {"request": request, "todos": todos})


@todos_routes.get("/add-todo")
async def get_add_todo(request: Request):
    return templates.TemplateResponse("add-todo.html", {"request": request})


@todos_routes.post("/add-todo")
async def add_todo(
    request: Request,
    title: todo_title,
    description: todo_desc,
    priority: todo_priority,
    user_id: Annotated[str | None, Depends(get_user_id)],
):
    if not user_id:
        return RedirectResponse(url=request.url_for("get_login"), status_code=302)
    create_todo(title, description, priority, user_id)
    return RedirectResponse(url=request.url_for("todos"), status_code=302)


@todos_routes.get("/edit-todo/{todo_id}")
async def edit_todo(request: Request, todo_id: Annotated[str, Path()]):
    return templates.TemplateResponse("edit-todo.html", {"request": request})


@todos_routes.post("/edit-todo/{todo_id}")
async def post_edit_todo(
    request: Request,
    todo_id: Annotated[str, Path()],
    title: todo_title,
    description: todo_desc,
    priority: todo_priority,
    user_id: Annotated[str | None, Depends(get_user_id)],
):
    if not user_id:
        return RedirectResponse(url=request.url_for("get_login"), status_code=302)
    update_todo(title, description, priority, todo_id)
    return RedirectResponse(url=request.url_for("todos"), status_code=302)
