
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from docs.templates import templates, hotreload


class HTMLRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()

router.add_websocket_route("/hot-reload", endpoint=hotreload, name="hot-reload")

@router.get(
    "/",
)
async def index(
    request: Request,
):
    return templates.TemplateResponse(
        "pages/index.html",
        dict(
            request=request,
        ),
    )
