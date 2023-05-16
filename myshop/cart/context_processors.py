from .cart import Cart


# That file and code allows cart works
def cart(request):
    return {"cart": Cart(request)}
