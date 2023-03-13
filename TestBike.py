from libraries.StreetBikeWithCCU import StreetBikeWithCCU
class TestBike(StreetBikeWithCCU):
 
    def __init__(self, name, vin, color):
          super().__init__(name, vin, color)

    def start_navigation(self):
        print(self.name + " started the Navigation!")