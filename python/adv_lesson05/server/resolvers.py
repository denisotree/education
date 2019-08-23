from functools import reduce

from settings import INSTALLED_APPS


def get_server_action():
    applications = reduce(
        lambda value, item: value + [__import__(f'{item}.routes')],
        INSTALLED_APPS,
        []
    )

    routes = reduce(
        lambda value, item: value + [getattr(item, 'routes', None)],
        applications,
        []
    )

    actions = reduce(
        lambda value, item: value + getattr(item, 'actionmapping', None),
        routes,
        []
    )

    print(actions)

    return actions


def resolve(action):
    actionmapping = {
        item.get('action'): item.get('controller')
        for item in get_server_action()
        if item
    }

    print(actionmapping)

    return actionmapping.get(action)
