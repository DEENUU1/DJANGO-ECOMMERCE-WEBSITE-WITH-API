from .saved import Saved


# That file and code allows list of saved products works
def cart(request):
    return {'cart': Saved(request)}
