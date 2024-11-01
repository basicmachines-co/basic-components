---
title: WTForm
description: Render a WTForm with validation, error handling and csrf protection.
component: wtform
---

## Usage

```html
--8<-- "docs/templates/examples/wtform.html"
```

The WTForm component makes it very easy to render, validate and handle form processing when using a form instance from  the [startlette-wtf](https://github.com/kubetail-org/starlette-wtf) lib. 
Using `starlette-wtf` you can add CSRF protection and declaritive validation to your forms.
## Code

/// tab | WTForm.jinja
```html
--8<-- "components/ui/WTForm.jinja"
```
///

/// tab | SampleForm.py
```python
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
```
///

