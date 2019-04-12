from proxy.handlers import proxy


def setup_routes(app):
    app.router.add_route("*", "/{path:.*}", proxy)
