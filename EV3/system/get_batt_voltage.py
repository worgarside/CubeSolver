voltage_file = open('/sys/class/power_supply/legoev3-battery/current_now', 'r')
voltage = voltage_file.read()
print(voltage)
voltage_file.close()