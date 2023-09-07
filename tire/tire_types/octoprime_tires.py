from abc import ABC

from tire.tire import Tires

class OctoprimeTires(Tires, ABC):

    def needs_service(self):
        sum = 0
        for w in self.wear:
            sum += w
            
        return sum >= 3.0
