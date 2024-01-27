########################################################################################################
#                                           Library
########################################################################################################
import string
import time
import uvicorn
import logging
import random
from fastapi import FastAPI, Request
from routes.api import router as api_router
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from fastapi.staticfiles import StaticFiles
from routes.limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
import platform

#############################  Paths  ##########################################
if platform.system().lower() == 'windows':
    path = "../"
else:
    path = ""

########################################################################################################
#                                               Main
########################################################################################################
path_logfile = '{}config/logging.conf'.format(path)
logging.config.fileConfig(path_logfile, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
app = FastAPI(title="IT Hub",
              version="0.0.1",
              description="IT Services Via API",
              docs_url=None, redoc_url=None,
              )

path_static_file = '{}static'.format(path)
app.mount("/static", StaticFiles(directory=path_static_file), name="static")
app.add_middleware(SlowAPIMiddleware)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler, )


########################################################################################################
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


########################################################################################################
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


########################################################################################################
@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )

app.include_router(api_router)


########################################################################################################
@app.middleware("http")
async def log_requests(request: Request, call_next):
    ip = request.client.host
    method = request.method
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} - request --  ip={ip} - method={method} - path={request.url.path}")
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:2f}'.format(process_time)
    logger.info(
        f"rid={idem} - response - ip={ip} - completed_in={formatted_process_time}ms - status_code={response.status_code}")
    return response


# ########################################################################################################
# ########################################################################################################
# if __name__ == "__main__":
#     print("\n ###. IT Hub Project .###\n")
#     uvicorn.run("main:app", host="127.0.0.1", port=8000,
#                 reload=True)