objects = [[], []]


def add_object(o, depth = 0):
    objects[depth].append(o)

def add_object(ol, depth = 0):
    objects[depth] += ol

def update():
    for layer in objects:
        for o in objects:
            o.update()


def render():
    for layer in objects:
        for o in objects:
            o.draw()


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')
