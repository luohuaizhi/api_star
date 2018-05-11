from apistar import http


class ErrorHandlingHook:

    def on_response(self, response: http.Response, exc: Exception):
        if exc is None:
            print("Handler returned a response")
        else:
            print("Exception handler returned a response")

    def on_error(self, response: http.Response):
        print("An unhandled error was raised")

    def on_request(self, request: http.Request):
        print("some request")

