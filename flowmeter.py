# Import the propar module
import propar

# Connect to the local instrument, when no settings provided
# defaults to locally connected instrument (address=0x80, baudrate=38400)
import pyvisa
from setup import QPX1200SP_2

# # Setup connection
# rm = pyvisa.ResourceManager()
# QPX1200SP_2 = rm.open_resource(QPX1200SP_2)
#
# # Power supply 1
# QPX1200SP_2.timeout = 5000  # set a delay
# QPX1200SP_2.read_termination = '\r'


def flowmeter_connect():
    el_flow = propar.instrument('COM4')

    return el_flow

#
# def setQPX1200SP_2(voltage, state):
#     QPX1200SP_2.write(f"V1 {voltage}\r")
#     QPX1200SP_2.write(f"OP1 {state}\r")

#
# def set_flowmeter():
#     flowmeter_connect().write(0, 10, propar.PP_TYPE_FLOAT, 64)
#     flowmeter_connect().write(1, 13, propar.PP_TYPE_FLOAT, 100)
#     # flowmeter_connect().write(1, 14, propar.PP_TYPE_INT8, 2)
#     flowmeter_connect().write(1, 14, propar.PP_TYPE_INT8, 130)
#     flowmeter_connect().write(1, 15, propar.PP_TYPE_INT8, 5)
#     flowmeter_connect().write(1, 4, propar.PP_TYPE_INT8, 8)
#     flowmeter_connect().write(1, 1, propar.PP_TYPE_INT16, 32000)
#     flowmeter_connect().write(0, 10, propar.PP_TYPE_FLOAT, 82)


def get_flow():

    # flowmeter_connect().write(1, 15, propar.PP_TYPE_INT8, 2)
    # flowmeter_connect().write(1, 31, propar.PP_TYPE_INT8, "g/s")
    flow = flowmeter_connect().read(33, 0, propar.PP_TYPE_FLOAT)

    return flow

def get_flow_temp():
    temp = flowmeter_connect().read(33, 7, propar.PP_TYPE_FLOAT)

    return temp


def get_flow_density():
    density = flowmeter_connect().read(116, 15, propar.PP_TYPE_FLOAT)

    return density

#
# def get_flow_setpoint():
#     set_point = flowmeter_connect().read(115, 23, propar.PP_TYPE_INT8)
#
#     return set_point
#
#
# def get_flow_pressure():
#     pressure = flowmeter_connect().read(33, 8, propar.PP_TYPE_FLOAT)
#
#     return pressure
#
#
# def dissable_valve_flow():
#     flowmeter_connect().write(1, 4, propar.PP_TYPE_INT8, 8)
#
#
# def get_setting():
#     setting = flowmeter_connect().read(1, 4, propar.PP_TYPE_INT8)
#     return setting
#
#
# def get_measure_unipolair():
#     unipolair = flowmeter_connect().read(1, 0, propar.PP_TYPE_INT16)
#     return unipolair
#
#
# def get_Setpoint():
#     set_point = flowmeter_connect().read(1, 1, propar.PP_TYPE_INT16)
#     return set_point
#
#
# def get_Fsetpoint():
#     fet_point = flowmeter_connect().read(33, 3, propar.PP_TYPE_FLOAT)
#     return fet_point
#
#
# def get_setpoint_monitor_mode():
#     set_point_monitor = flowmeter_connect().read(115, 23, propar.PP_TYPE_INT8)
#     return set_point_monitor
#
#
# def get_setpoint_exp_filter():
#     set_point_filter = flowmeter_connect().read(117, 3, propar.PP_TYPE_FLOAT)
#     return set_point_filter
#
#
# def get_setpoint_slope():
#     set_point_slope = flowmeter_connect().read(1, 2, propar.PP_TYPE_INT16)
#     return set_point_slope
#
#
# def get_control_mode():
#     control_mode = flowmeter_connect().read(1, 4, propar.PP_TYPE_INT8)
#     return control_mode
#
#
# def get_slave_factor():
#     slave_factor = flowmeter_connect().read(33, 1, propar.PP_TYPE_FLOAT)
#     return slave_factor
#
#
# def get_fluid_number():
#     fluid_number = flowmeter_connect().read(1, 16, propar.PP_TYPE_INT8)
#     return fluid_number
#
#
# def get_fluid_name():
#     fluid_name = flowmeter_connect().read(1, 17, propar.PP_TYPE_STRING)
#     return fluid_name
#
#
# def get_valve_output():
#     valve_output = flowmeter_connect().read(114, 1, propar.PP_TYPE_INT32)
#     return valve_output
#
#
# def get_sensor_type():
#     sensor_type = flowmeter_connect().read(1, 14, propar.PP_TYPE_INT8)
#     return sensor_type
#
#
# def get_capacity_100():
#     capacity = flowmeter_connect().read(1, 13, propar.PP_TYPE_FLOAT)
#     return capacity
#
#
# def get_capacity_0():
#     capacity = flowmeter_connect().read(33, 22, propar.PP_TYPE_FLOAT)
#     return capacity
#
#
# def get_capacity_unit_index():
#     capacity_unit = flowmeter_connect().read(1, 15, propar.PP_TYPE_INT8)
#     return capacity_unit
#
#
# def get_capacity_unit():
#     capacity_unit = flowmeter_connect().read(1, 31, propar.PP_TYPE_STRING)
#     return capacity_unit
#
#
# def get_stable_resp():
#     response = flowmeter_connect().read(114, 17, propar.PP_TYPE_INT8)
#     return response
#
#
# def get_sens_filer():
#     filter = flowmeter_connect().read(117, 4, propar.PP_TYPE_FLOAT)
#     return filter
#
#
# def get_valve_safe_state():
#     valve = flowmeter_connect().read(115, 31, propar.PP_TYPE_INT8)
#     return valve
#
#
# def get_counter_mode():
#     counter = flowmeter_connect().read(104, 8, propar.PP_TYPE_INT8)
#     return counter
#
#
# def get_serial_number():
#     serial = flowmeter_connect().read(113, 3, propar.PP_TYPE_STRING)
#     return serial
#
#
# def get_BHTModel():
#     BHTM = flowmeter_connect().read(113, 2, propar.PP_TYPE_STRING)
#     return BHTM
#
#
# def get_firmware():
#     firmware = flowmeter_connect().read(113, 5, propar.PP_TYPE_STRING)
#     return firmware
#
#
# def get_customer_model():
#     model = flowmeter_connect().read(113, 4, propar.PP_TYPE_STRING)
#     return model
#
#
# def get_ind_number():
#     number = flowmeter_connect().read(113, 2, propar.PP_TYPE_INT8)
#     return number
#
#
# def get_device_type():
#     type = flowmeter_connect().read(113, 1, propar.PP_TYPE_STRING)
#     return type
#
