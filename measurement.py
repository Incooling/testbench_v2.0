import os
import datalog
import flowmeter
import hvac
from saturation_curve import *

import valve
from time import sleep
from setup import *
import sensors
import compressor
import MX100QP

i = 1

fan_set_var.insert(1, "Not set")
comp_set_var.insert(0, "Not set")
comp_enable_var.insert(0, "Off")
hvac_set_var.insert(0, "Not set")


# def get_data_hvac():
#     while True:
#
#         hvac_volt_update.insert(0, round(hvac.getHeatVolt(), 3))
#         hvac_cur_update.insert(0, round(hvac.getHeatAmp(), 3))
#         sleep(2)


def update_data():
    global i
    i = 1

    while True:
        try:
            # Pressure
            p_evap_out.insert(0, sensors.getPressure(105))  # pressure 2
            p_cond_in.insert(0, sensors.getPressure(106))  # pressure 3
            p_flow_out.insert(0, sensors.getPressure(107))  # pressure 4

            pressure_data = {"p_evap_out": p_evap_out[0],
                             "p_cond_in": p_cond_in[0],
                             "p_flow_out": p_flow_out[0]}

            # Temperature
            t_evap_in.insert(0, round(sensors.getTemp(101), 1))
            t_evap_out_mid.insert(0, round(sensors.getTemp(116), 1))
            t_cond_in.insert(0, round(sensors.getTemp(103), 1))
            t_cond_out.insert(0, round(sensors.getTemp(104), 1))
            t_cond_out_flow.insert(0, round(sensors.getTemp(114), 1))
            t_flow_out.insert(0, round(sensors.getTemp(115), 1))
            t_load_inlet.insert(0, round(sensors.getTempLoad(108), 1))
            t_load_middle.insert(0, round(sensors.getTempLoad(109), 1))
            t_load_out.insert(0, round(sensors.getTempLoad(110), 1))
            t_load_ambient.insert(0, round(sensors.getTempLoad(111), 1))
            t_evap_out.insert(0, round(sensors.getTemp(102), 1))
            t_sat_evap_in.insert(0, sat_temp(sensors.getPressure(105)))

            temp_data = {"t_evap_in": t_evap_in[0],
                         "t_evap_out": t_evap_out[0],
                         "t_evap_out_mid": t_evap_out_mid[0],
                         "t_cond_in": t_cond_in[0],
                         "t_cond_out": t_cond_out[0],
                         "t_cond_out_flow": t_cond_out_flow[0],
                         "t_load_inlet": t_load_inlet[0],
                         "t_load_middle": t_load_middle[0],
                         "t_load_out": t_load_out[0],
                         "t_ambient": t_load_ambient[0],
                         "t_flow_out": t_flow_out[0]}

            # Humidity sensor
            humidity.insert(0, "Not used") # round(sensors.asyncio.run(sensors.read_once()))
            humidity_data = {"humidity": humidity[-1]}

            # Log fan data
            fan_freq.insert(0, round(sensors.getFrequency(113), 1))
            fan_volt.insert(0, fan_set_var[0])  # voltage fans
            fan_cur.insert(0, MX100QP.ttiPsu.getOutputAmps(1))


            fan_data = {"fan_freq": fan_freq[0],
                        "fan_volt": fan_volt[0],
                        "fan_cur": fan_cur[0]}



            # Flowmeter
            flowmeter_flow.insert(0, round(flowmeter.get_flow(), 2))
            flowmeter_temp.insert(0, flowmeter.get_flow_temp())
            flowmeter_density.insert(0, round(flowmeter.get_flow_density(), 2))
            flowmeter_pressure.insert(0, "none")
            # flowmeter_setting.append(flowmeter.get_setting())
            # flowmeter_unipolair.append(flowmeter.get_measure_unipolair())
            # flowmeter_setpoint.append(flowmeter.get_Setpoint())
            # flowmeter_fsetpoint.append(flowmeter.get_Fsetpoint())
            # flowmeter_setp_monitor.append(flowmeter.get_setpoint_monitor_mode())
            # flowmeter_setp_filter.append(flowmeter.get_setpoint_exp_filter())
            # flowmeter_setp_slope.append(flowmeter.get_setpoint_slope())
            # flowmeter_control.append(flowmeter.get_control_mode())
            # flowmeter_slave_factor.append(flowmeter.get_slave_factor())
            # flowmeter_fluid_num.append(flowmeter.get_fluid_number())
            # flowmeter_fluid_name.append(flowmeter.get_fluid_name())
            # flowmeter_valve_outp.append(flowmeter.get_valve_output())
            # flowmeter_sensor.append(flowmeter.get_sensor_type())
            # flowmeter_capacity_100.append(flowmeter.get_capacity_100())
            # flowmeter_capacity_0.append(flowmeter.get_capacity_0())
            # flowmeter_cap_index.append(flowmeter.get_capacity_unit_index())
            # flowmeter_cap_unit.append(flowmeter.get_capacity_unit())
            # flowmeter_stable_resp.append(flowmeter.get_stable_resp())
            # flowmeter_sens_filter.append(flowmeter.get_sens_filer())
            # flowmeter_valve_state.append(flowmeter.get_valve_safe_state())
            # flowmeter_counter.append(flowmeter.get_counter_mode())
            # flowmeter_serial.append(flowmeter.get_serial_number())
            # flowmeter_BHTModel.append(flowmeter.get_BHTModel())
            # flowmeter_firmware.append(flowmeter.get_firmware())
            # flowmeter_cust_model.append(flowmeter.get_customer_model())
            # flowmeter_ind_number.append(flowmeter.get_ind_number())
            # flowmeter_device_type.append(flowmeter.get_device_type())

            #
            flowmeter_data = {"flow": flowmeter_flow[0],
                              "temp": flowmeter_temp[0],
                              "density": flowmeter_density[0],
                              "pressure": flowmeter_pressure[0]}
            #                   "setting": flowmeter_setting[-1],
            #                   "unipoliar": flowmeter_unipolair[-1],
            #                   "Setpoint": flowmeter_setpoint[-1],
            #                   "Fsetpoint": flowmeter_fsetpoint[-1],
            #                   "setpoint_monitor": flowmeter_setp_monitor[-1],
            #                   "setpoint_filter": flowmeter_setp_filter[-1],
            #                   "setpoint_slope": flowmeter_setp_slope[-1],
            #                   "control_mode": flowmeter_control[-1],
            #                   "slave_factor": flowmeter_slave_factor[-1],
            #                   "fluid_number": flowmeter_fluid_num[-1],
            #                   "fluid_name": flowmeter_fluid_name[-1],
            #                   "valve_output": flowmeter_valve_outp[-1],
            #                   "sensor_type": flowmeter_sensor[-1],
            #                   "capacity_100": flowmeter_capacity_100[-1],
            #                   "capacity_0": flowmeter_capacity_0[-1],
            #                   "capacity_index": flowmeter_cap_index[-1],
            #                   "capacity_unit": flowmeter_cap_unit[-1],
            #                   "stable_response": flowmeter_stable_resp[-1],
            #                   "sensor_filter": flowmeter_sens_filter[-1],
            #                   "valve_state": flowmeter_valve_state[-1],
            #                   "counter": flowmeter_counter[-1],
            #                   "serial": flowmeter_serial[-1],
            #                   "BHTModel": flowmeter_BHTModel[-1],
            #                   "firmware": flowmeter_firmware[-1],
            #                   "customer_model": flowmeter_cust_model[-1],
            #                   "inden_number": flowmeter_ind_number[-1],
            #                   "device_type": flowmeter_device_type[-1]
            #                   }

            # Valve
            valve_position.insert(0, valve.getValvePos())
            valve_data = {"position": valve_position[0]}


            # Compressor
            comp_status.insert(0, compressor.getStatus())  # status
            comp_overheat.insert(0, compressor.getOverheat())  # overheat
            comp_cur_board.insert(0, compressor.getCurrentComp())
            comp_cur_supp.insert(0, compressor.getCurrentSupply())
            comp_volt_supp.insert(0, compressor.getVoltageSupply())
            comp_set_speed.insert(0, comp_set_var[0])  # speed voltage compressor
            comp_enable.insert(0, comp_enable_var[0])  # enable data
            # comp_freq.append(compressor.get_comp_freq())
            # comp_max_freq.append(compressor.getMaxCompSpeed())
            # comp_min_freq.append(compressor.getMinCompSpeed())
            # com_avg_freq.append(compressor.getAvgCompSpeed())



            compressor_data = {"comp_status": comp_status[0],
                               "comp_overheat": comp_overheat[0],
                               "comp_cur_board": comp_cur_board[0],
                               "comp_cur_supply": comp_cur_supp[0],
                               "comp_volt_supply": comp_volt_supp[0],
                               "comp_set_speed": comp_set_speed[0],
                               "comp_enable": comp_enable[0],
                               "comp_freq": "None",
                               "comp_max_freq": "None",
                               "comp_min_freq": "None",
                               "comp_avg_freq": "None"}

            welco_time.insert(0, compressor.get_comp_data()[0])
            welco_cst.insert(0, compressor.get_comp_data()[1])
            welco_imc.insert(0, compressor.get_comp_data()[2])
            welco_speed.insert(0, compressor.get_comp_data()[3])
            welco_curr.insert(0, compressor.get_comp_data()[4])
            welco_pin.insert(0, compressor.get_comp_data()[5])
            welco_st.insert(0, compressor.get_comp_data()[6])
            welco_stat.insert(0, compressor.get_comp_data()[7])
            welco_error.insert(0, compressor.get_comp_data()[8])


            welco_data = {"time": welco_time[0],
                          "cst": welco_cst[0],
                          "imc": welco_imc[0],
                          "speed": welco_speed[0],
                          "curr": welco_curr[0],
                          "pin": welco_pin[0],
                          "st": welco_st[0],
                          "stat:": welco_stat[0],
                          "error": welco_error[0]}

            # compressor.refresh_scope()

            hvac_volt.insert(0, round(hvac.getHeatVolt(), 3))
            hvac_cur.insert(0, round(hvac.getHeatAmp(), 3))
            hvac_set.insert(0, hvac_set_var[0])  # set voltage HVAC

            hvac_data = {"hvac_volt": hvac_volt[0],
                         "hvac_cur": hvac_cur[0],
                         "hvac_set": hvac_set[0]}

            # add data to excel log
            datalog.log_data(i, temp_data, pressure_data, fan_data, valve_data, flowmeter_data,
                             hvac_data, compressor_data, humidity_data)

            i += 1

            sleep(1)

        except (pyvisa.VisaIOError, ConnectionError, KeyboardInterrupt, RuntimeError):
            hvac.setHVAC(0)
            compressor.setCompressor(0)
            MX100QP.ttiPsu.setOutputEnable(1, False)
            MX100QP.ttiPsu.setOutputEnable(2, False)
            valve.setValvePos(0)
            MX100QP.ttiPsu.setOutputEnable(3, False)
            print("Error occurred, stopping test")

            os._exit(0)

        # except Exception:
        #     pass
