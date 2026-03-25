def get(url,fun,endpoint,app):
    app.add_url_rule(rule=url,view_func=fun,endpoint=endpoint,methods=['GET'],strict_slashes=False)

def post(url,fun,endpoint,app):
    app.add_url_rule(rule=url,view_func=fun,endpoint=endpoint,methods=['POST'],strict_slashes=False)

def patch(url,fun,endpoint,app):
    app.add_url_rule(rule=url,view_func=fun,endpoint=endpoint,methods=['PATCH'],strict_slashes=False)

def delete(url,fun,endpoint,app):
    app.add_url_rule(rule=url,view_func=fun,endpoint=endpoint,methods=['DELETE'],strict_slashes=False)


def resource(url,controller,app):
    url = url.strip("/")
    get(f"/{url}",controller.index,f"{url}.index",app)
    get(f"/{url}/create",controller.create,f"{url}.create",app)
    post(f"/{url}",controller.store,f"{url}.store",app)
    get(f"/{url}/<id>",controller.show,f"{url}.show",app)
    get(f"/{url}/user_id/edit",controller.edit,f"{url}.edit",app)
    patch(f"/{url}/<id>",controller.update,f"{url}.update",app)
    delete(f"/{url}/<id>",controller.delete,f"{url}.delete",app)