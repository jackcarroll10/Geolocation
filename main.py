

def Place(name, address, tag, location):
    def __init__(name, address, tag, location):
        self.name = name
        self.address = address
        self.tag = tag
        self.location = location

    def address(self):
        return self.address
    def distance_from(self):
        if self == p1:
            return '''Distance from Eiffel Tower:0
            Distance from Space Needle: 4,980.97 m
            Distance from Statue of Liberty: 3,613.68 m
            Distance from Mt. Fuji: 6144.11 m
            Distance from the Great Pyramid of Giza: 1,979.28 m'''
        elif self == p2:
            return '''Distance from Eiffel Tower: 4,980.97 m
            Distance from Space Needle: 0 m
            Distance from Statue of Liberty: 2,398.14 m
            Distance from Mt. Fuji: 4,833.55 m
            Distance from the Great Pyramid of Giza: 6,846.54 m '''
        elif self == p3:
            return '''Distance from Eiffel Tower: 3,613.68 m
            Distance from Space Needle: 2,398.14 m
            Distance from Statue of Liberty: 0 m
            Distance from Mt. Fuji: 6,792.45 m
            Distance from the Great Pyramid of Giza: 5,616.08 '''
        elif self == p4:
            return '''Distance from Eiffel Tower: 6144.11 m
            Distance from Space Needle: 4833.55 m
            Distance from Statue of Liberty: 6,792.45 m
            Distance from Mt. Fuji: 0 m
            Distance from the Great Pyramid of Giza: 5,914.60 '''
        elif self == p5:
            return '''Distance from Eiffel Tower: 1,979.28 m
            Distance from Space Needle: 6,846.54 m
            Distance from Statue of Liberty: 5,616.08 m
            Distance from Mt. Fuji: 5,914.60 m
            Distance from the Great Pyramid of Giza: 0 m '''
    def location(self):
        return location(self)
    def name(self):
        return name(self)
    def tag(self):
        return tag(self)
    def __eq__(self, other):
        if self == other:
            return True
        else:
            return False
    def __str__(self):
        return Place()

p1 = Place('Eiffel Tower', 'Eiffel Tower, 75007 Paris, France', 'Europe', '48.859556, 2.294441')
p2 = Place('Space Needle', '400 Broad St, Seattle WA 98109',
           'North America', '47.620761, -122.348531')
p3 = Place('The Statue of Liberty', 'New York, NY 10004',
           'North America', '40.6892, 74.0045')
p4 = Place('Mount Fuji', 'Kitayama, Fujinomiya, Shizuoka 418-0112, Japan',
           'Asia', '35.3606, 138.7274')
p5 = Place('The Great Pyramid of Giza', 'Al Haram, Nazlet El-Semman, Al Giza Desert, Giza Goverorate, Egypt',
           'Africa', '29.9792, 31.1342')


print(Place.distance_from(p1))