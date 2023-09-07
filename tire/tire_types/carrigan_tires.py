from abc import ABC

from tire.tire import Tires

class CarriganTires(Tires, ABC):

    def needs_service(self):
        for w in self.wear:
            if w >= 0.9:
                return True
            
        return False
