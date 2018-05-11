from apistar import ASyncApp
from apistar import Route
from apistar import http
from apistar import Include

from controller import users


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', method='GET', handler=welcome),
    Include('/users', name='users', routes=users.routes),
]

print(routes)

app = ASyncApp(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
