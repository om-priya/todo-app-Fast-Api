from fastapi import APIRouter, Request, Response
from fastapi import Form

from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import shortuuid
from controllers import auth_controller
from utils.jwt_handler import JwtHandler

auth_routes = APIRouter()

templates = Jinja2Templates(directory="templates")

user_email = Annotated[str, Form()]
user_password = Annotated[str, Form()]


@auth_routes.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@auth_routes.post("/login")
async def post_login(
    request: Request, email: user_email, password: user_password, response: Response
):
    print(email, password)
    user_id = auth_controller.check_credentials(email, password)
    if not user_id:
        return RedirectResponse(url=request.url_for("get_login"), status_code=302)

    claims = {"user_id": user_id}
    access_token = JwtHandler.generate_token(claims)
    response = RedirectResponse(url=request.url_for("todos"), status_code=302)
    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True, samesite="strict")
    return response


@auth_routes.get("/sign-up")
async def sign_up(request: Request):
    return templates.TemplateResponse("sign-up.html", {"request": request})


@auth_routes.post("/sign-up")
async def create_user(
    request: Request, email: Annotated[str, Form()], password: Annotated[str, Form()]
):
    user_id = shortuuid.ShortUUID().random(length=8)
    auth_controller.sign_up(user_id, email, password)
    return RedirectResponse(url=request.url_for("get_login"), status_code=302)
