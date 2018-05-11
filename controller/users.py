from apistar import App, Route, exceptions


USERS = {1: 'hazel', 2: 'james', 3: 'ana'}


def list_users(app: App) -> list:
    return [
        {
            'username': username,
            'url': app.reverse_url('users:get_user', user_id=user_id)
        } for user_id, username in USERS.items()
    ]


def get_user(app: App, user_id: int) -> dict:
    if user_id not in USERS:
        raise exceptions.NotFound()
    return {
        'username': USERS[user_id],
        'url': app.reverse_url('users:get_user', user_id=user_id)
    }

routes = [
    # Route('/', method='GET', handler=list_users),
    Route('/{user_id}', method='GET', handler=get_user),
]