class Order():
    """Class that defines the properties for a order object"""

    def __init__(self, id, metalId, styleId, sizeId, timestamp):
        self.id = id
        self.metalId = metalId
        self.styleId = styleId
        self.sizeId = sizeId
        self.timestamp = timestamp