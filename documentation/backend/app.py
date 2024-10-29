from pathlib import Path
from typing import Optional

import jinjax
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from jinja2.ext import DebugExtension
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette_wtf import CSRFProtectMiddleware
from starlette_wtf import StarletteForm
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    SelectField,
    FileField,
    BooleanField,
    RadioField,
    IntegerField,
    validators,
)

# project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,  #
    allow_origins=["https://basicmachines-co.github.io", "http://localhost:8000", "http://127.0.0.1:8000"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

print(f"BASE_DIR={BASE_DIR}")
templates = Jinja2Templates(directory=f"{BASE_DIR}/documentation/backend/templates")
templates.env.add_extension(DebugExtension)

templates.env.add_extension(jinjax.JinjaX)
catalog = jinjax.Catalog(jinja_env=templates.env)
catalog.add_folder(f"{BASE_DIR}/components")
catalog.add_folder(f"{BASE_DIR}/components/ui")
catalog.add_folder(f"{BASE_DIR}/components/icons")
catalog.add_folder(f"{BASE_DIR}/demo/examples")

# Serve static files (CSS, etc.) from shad-cn
app.mount("/dist", StaticFiles(directory=f"{BASE_DIR}/documentation/docs/dist"), name="dist")

# CSRF Middleware for form handling
app.add_middleware(SessionMiddleware, secret_key="session_key")
app.add_middleware(CSRFProtectMiddleware, csrf_secret="your_secret_key_here")


@app.get("/", response_class=HTMLResponse)
async def components(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/components/{component_name}", response_class=HTMLResponse)
async def render_component(request: Request, component_name: str, option: Optional[str] = None):
    return templates.TemplateResponse(
        request=request,
        name="component.html",
        context={
            "component_name": component_name,
            "option": option
        }
    )


@app.get("/table", response_class=HTMLResponse)
async def table_sort(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="table_sorting.html",
    )


class SampleForm(StarletteForm):
    username = StringField(
        "Username",
        [validators.InputRequired(), validators.Length(min=4, max=25)],
        id="username",
        render_kw={"placeholder": "username"},
        description="Enter a unique username.",
    )
    email = StringField(
        "Email",
        [validators.InputRequired(), validators.Email()],
        id="email",
        default="example@example.com",
        description="Your primary email address.",
    )
    password = PasswordField(
        "Password",
        [validators.InputRequired(), validators.Length(min=6)],
        id="password",
        description="Must be at least 6 characters.",
    )
    bio = TextAreaField(
        "Bio",
        [validators.Optional(), validators.Length(max=200)],
        id="bio",
        description="Write a brief bio about yourself.",
        default="I love coding and coffee.",
    )
    age = IntegerField(
        "Age",
        [validators.Optional(), validators.NumberRange(min=18, max=100)],
        id="age",
        default=25,
        description="Your age (must be between 18 and 100).",
    )
    gender = RadioField(
        "Gender",
        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
        id="gender",
        description="Select your gender.",
        default="M",
    )
    country = SelectField(
        "Country",
        choices=[("US", "United States"), ("CA", "Canada"), ("UK", "United Kingdom")],
        id="country",
        default="US",
        description="Choose your country.",
    )
    agree_terms = BooleanField(
        "I agree to the terms and conditions",
        [validators.InputRequired()],
        id="agree_terms",
        description="You must agree before submitting.",
    )
    profile_picture = FileField(
        "Profile Picture",
        [validators.Optional()],
        id="profile_picture",
        description="Upload your profile picture (optional).",
    )


@app.get("/wtform", response_class=HTMLResponse)
async def display_wtform(request: Request):
    form = SampleForm(request)
    return templates.TemplateResponse(
        request=request,
        name="component.html",
        context={
            "component_name": "wtform",
            "form": form
        }
    )


@app.post("/wtform", response_class=HTMLResponse)
async def post_wtform(request: Request):
    form = await SampleForm.from_formdata(request)
    if await form.validate():
        # Form is valid, process the form data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Log or handle the data as needed (e.g., save to a database)
        print(f"Name: {username}, Email: {email}, Password: {password}")

        # Redirect to a success page or any other action
        return RedirectResponse(url="/success", status_code=303)
    else:
        # If form validation fails, re-render the form with errors
        return templates.TemplateResponse(
            request=request,
            name="component.html",
            context={
                "component_name": "wtform",
                "form": form
            }
        )


# Success endpoint
@app.get("/success")
async def success(request: Request):
    return {"message": "Form submitted successfully!"}
