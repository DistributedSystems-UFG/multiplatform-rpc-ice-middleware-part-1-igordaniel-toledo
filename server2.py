import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def __init__(self, t):
        self.t = t
        
    def printString(self, s, current=None):
        print(self.t, s)
        return s + "*"
    
    def somar(self, a, b, current=None):
        print(self.t, f"Somando {a} + {b}")
        return a + b

    def inverter(self, s, current=None):
        print(self.t, f"Invertendo {s}")
        return s[::-1]

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object1 = PrinterI("Object1 says:")
object2 = PrinterI("Object2 says:")
adapter.add(object1, communicator.stringToIdentity("SimplePrinter1"))
adapter.add(object2, communicator.stringToIdentity("SimplePrinter2"))
adapter.activate()

communicator.waitForShutdown()
