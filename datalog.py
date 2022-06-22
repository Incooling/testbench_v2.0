from setup import *
import datetime

file

def log_data(i, temp_data, pressure_data, fan_data, valve_data, flowmeter_data, hvac_data, compressor_data, humidity_data):
    date.insert(0, datetime.datetime.now().strftime("%d-%b-%Y"))  # file[2]
    date.insert(1, datetime.datetime.now().strftime("%H:%M:%S"))  # file[3]

    # # Input data into columns
    sheet1.write(i, date_colm, date[0])
    sheet1.write(i, time_colm, date[1])
    sheet1.write(i, name_colm, file[0])
    sheet1.write(i, desciption_colm, file[1])
    sheet1.write(i, mac_qpx1200sp1, QPX1200SP1_mac)
    sheet1.write(i, mac_qpx1200sp2, QPX1200SP2_mac)
    sheet1.write(i, mac_mx1000qp_colm, MX100QP_mac)
    sheet1.write(i, mac_nanotec_colm, nanoTec_mac)
    sheet1.write(i, mac_tektronix_colm, MDO3024_mac)
    sheet1.write(i, mac_daq970_colm, DAQ970A_mac)
    sheet1.write(i, mac_bronkhorst_colm, 1)
    sheet1.write(i, mac_omega_colm, 1)  # setup.ttiPsu.getOutputVolts(3))
    sheet1.write(i, iteration_colm, i)
    sheet1.write(i, fan_volt_colm, fan_data['fan_volt'])
    sheet1.write(i, fan_cur_colm, fan_data['fan_cur'])
    sheet1.write(i, fan_speed_colm, fan_data['fan_freq'])
    sheet1.write(i, t_evap_in_colm, temp_data['t_evap_in'])
    sheet1.write(i, t_evap_out_colm, temp_data['t_evap_out'])
    sheet1.write(i, t_evap_out_mid_colm, temp_data['t_evap_out_mid'])
    sheet1.write(i, t_cond_in_colm, temp_data['t_cond_in'])
    if flowmeter_use[0]:
        sheet1.write(i, t_cond_out_colm, temp_data['t_cond_out_flow'])
    else:
        sheet1.write(i, t_cond_out_colm, temp_data['t_cond_out'])
    sheet1.write(i, t_flow_out_colm, temp_data['t_flow_out'])
    sheet1.write(i, press4_colm, pressure_data['p_flow_out'])
    sheet1.write(i, press3_colm, pressure_data['p_cond_in'])
    sheet1.write(i, press2_colm, pressure_data['p_evap_out'])
    sheet1.write(i, valve_pos_colm, valve_data['position'])
    sheet1.write(i, mass_flow_colm, flowmeter_data['flow'])
    sheet1.write(i, temp_flow_colm, flowmeter_data['temp'])
    sheet1.write(i, dens_flow_colm, flowmeter_data['density'])
    sheet1.write(i, press_flow_colm, 1)
    sheet1.write(i, heat_diss_vol_colm, hvac_data['hvac_volt'])
    sheet1.write(i, heat_diss_cur_colm, hvac_data['hvac_cur'])
    sheet1.write(i, heat_diss_power_colm, "")
    sheet1.write(i, comp_volt_colm, compressor_data['comp_volt_supply'])
    sheet1.write(i, comp_cur_in_colm, compressor_data['comp_cur_supply'])
    sheet1.write(i, comp_power_colm, "")
    sheet1.write(i, comp_rpm_colm, 1)
    sheet1.write(i, comp_rpm_max_colm, 1)
    sheet1.write(i, comp_rpm_min_colm, 1)
    sheet1.write(i, comp_rpm_avg_colm, 1)
    sheet1.write(i, comp_rpm_dev_colm, "")
    sheet1.write(i, comp_status_colm, compressor_data['comp_status'])
    sheet1.write(i, comp_overheat_colm, compressor_data['comp_overheat'])
    sheet1.write(i, comp_enable_colm, compressor_data['comp_enable'])
    sheet1.write(i, comp_cur_out_colm, compressor_data['comp_cur_board'])
    sheet1.write(i, comp_speed_in_colm, compressor_data['comp_set_speed'])
    sheet1.write(i, humidity_colm, humidity_data['humidity'])
    sheet1.write(i, ambient_temp_colm, temp_data['t_ambient'])
    sheet1.write(i, temp_load_1_colm, temp_data['t_load_inlet'])
    sheet1.write(i, temp_load_2_colm, temp_data['t_load_middle'])
    sheet1.write(i, temp_load_3_colm, temp_data['t_load_out'])
    sheet1.write(i, set_heat_load_colm, hvac_data['hvac_set'])
    sheet1.write(i, flowmeter_setting_colm, 1) # flowmeter_data['setting']

    wb1.save(f'{file[0]}.xls')

# def log_flowmeter_data(i, flowmeter_data):
#     date.insert(0, datetime.datetime.now().strftime("%d-%b-%Y"))  # file[2]
#     date.insert(1, datetime.datetime.now().strftime("%H:%M:%S"))  # file[3]
#
#     # # Input data into columns
#     sheet2.write(i, date_colm, date[0])
#     sheet2.write(i, time_colm, date[1])
#     sheet2.write(i, meas_unipolair_colm, flowmeter_data["unipoliar"])
#     sheet2.write(i, fmeas_colm, flowmeter_data["flow"])
#     sheet2.write(i, setpoint_colm, flowmeter_data["Setpoint"])
#     sheet2.write(i, fsetpoint_colm, flowmeter_data["Fsetpoint"])
#     sheet2.write(i, setpoint_mon_colm, flowmeter_data["setpoint_monitor"])
#     sheet2.write(i, setpoint_filter_colm, flowmeter_data["setpoint_filter"])
#     sheet2.write(i, setpoint_slope_colm, flowmeter_data["setpoint_slope"])
#     sheet2.write(i, controlmode_colm, flowmeter_data["control_mode"])
#     sheet2.write(i, slave_fac_colm, flowmeter_data["slave_factor"])
#     sheet2.write(i, fluid_num_colm, flowmeter_data["fluid_number"])
#     sheet2.write(i, fluid_name_colm, flowmeter_data["fluid_name"])
#     sheet2.write(i, valve_outp_colm, flowmeter_data["valve_output"])
#     sheet2.write(i, temp_colm, flowmeter_data["temp"])
#     sheet2.write(i, density_colm, flowmeter_data["density"])
#     sheet2.write(i, sensor_type_colm, flowmeter_data["sensor_type"])
#     sheet2.write(i, capacity_100_colm, flowmeter_data["capacity_100"])
#     sheet2.write(i, capacity_0_colm, flowmeter_data["capacity_0"])
#     sheet2.write(i, capacity_index_colm, flowmeter_data["capacity_index"])
#     sheet2.write(i, capacity_unit_colm, flowmeter_data["capacity_unit"])
#     sheet2.write(i, stable_resp_colm, flowmeter_data["stable_response"])
#     sheet2.write(i, sens_filter_colm, flowmeter_data["sensor_filter"])
#     sheet2.write(i, valve_safe_state_colm, flowmeter_data["valve_state"])
#     sheet2.write(i, counter_mode_colm, flowmeter_data["counter"])
#     sheet2.write(i, serial_colm, flowmeter_data["serial"])
#     sheet2.write(i, BHTModel_colm, flowmeter_data["BHTModel"])
#     sheet2.write(i, firmware_colm, flowmeter_data["firmware"])
#     sheet2.write(i, customer_model_colm, flowmeter_data["customer_model"])
#     sheet2.write(i, inden_number_colm, flowmeter_data['inden_number'])
#     sheet2.write(i, device_type_colm, flowmeter_data['device_type'])
#
#     wb2.save(f'{file[2]}.xls')
