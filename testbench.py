import compressor
import hvac
import valve
import flowmeter
from MX100QP import *
from time import sleep
from setup import *
import threads


def set_bench():
    while True:

        command = input("Do you want to activate inhouse? ")
        if command == "yes":
            print("setting all devices this might take 1min")


            print("Connecting to flowmeter")
            flowmeter.flowmeter_connect()

            # Valve
            print("Current valve position", valve.getValvePos())
            print("Setting valve")
            valve.setValvePos(25)

            print("New valve position", valve.getValvePos())

            # fans
            print("Enabling fans")
            fan_set_var.insert(0, ttiPsu.setTargetVolts(1, 12))
            ttiPsu.setOutputEnable(1, True)

            # HVAC
            print("Enabling HVAC")
            hvac_set_var.insert(0, hvac.setHVAC(2.01))
            comp_set_var.insert(0, compressor.setCompressor(3))

            # compressor
            print("Enabling compressor")
            compressor.setQPX1200SP_1(28, 1)
            comp_enable_var.insert(0, (compressor.setEnable(True)))

            threads.update_monitor.start()
            break
