class Order():
    """Class that defines the properties for a order object"""

    def __init__(self, id, metal_id, style_id, size_id, timestamp):
        self.id = id
        self.metal_id = metal_id
        self.style_id = style_id
        self.size_id = size_id
        self.timestamp = timestamp
        self.style = None
        self.metal = None
        self.size = None