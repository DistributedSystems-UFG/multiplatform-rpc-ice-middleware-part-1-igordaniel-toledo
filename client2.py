import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 98.90.53.6 -p 11000")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 98.90.53.6 -p 11000")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print(rep)
rep = printer2.printString("Hello World from printer2!")
print(rep)
print("Soma printer1:", printer1.somar(10, 5))
print("Soma printer2:", printer2.somar(3, 7))
print("Invertida printer1:", printer1.inverter("Igor"))
print("Invertida printer2:", printer2.inverter("Sistemas Distribuidos"))

communicator.waitForShutdown()
