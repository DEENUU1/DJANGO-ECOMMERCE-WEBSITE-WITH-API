from .cart import Cart


# This function allows to hook cart to context_processors in settings
def cart(request):
    return {'cart': Cart(request)}