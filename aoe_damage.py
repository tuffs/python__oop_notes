class Unit:
    def __init__(self, name, pos_x, pos_y, pos_z):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z

    def in_area(self, x_1, y_1, z_1, x_2, y_2, z_2):
        # Check the boundaries (inclusive) of an area by:
        # Insuring that the position of the
        # unit is inclusively in the area of effect

        return x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2 and z_1 <= self.pos_z <= z_2

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, pos_z, fire_range):
        super().__init__(name, pos_x, pos_y, pos_z)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, z, units):
        # Based on each units location, which units are hit by fire
        units_hit = []

        # Create a boundary box (left, bottom, right, top, floor, ceiling)
        left, bottom = x - self.__fire_range, y - self.__fire_range
        right, top = x + self.__fire_range, y + self.__fire_range
        floor, ceiling = z - self.__fire_range, z + self.__fire_range

        # Use in_area for response and add unit to units_hit if True
        for unit in units:
            if unit.in_area(left, bottom, right, top, floor, ceiling):
                units_hit.append(unit)

        # give em the list!
        return units_hit
