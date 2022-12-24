# from fastapi import Request, status
# from fastapi.responses import JSONResponse

# from main import app
# from utils.exceptions import HelloException


# @app.exception_handler(HelloException)
# def hello_exception_handler(request: Request, exc: HelloException):
#     return JSONResponse(
#         status_code=status.HTTP_418_IM_A_TEAPOT,
#         content={'detail': exc.title}
#     )
