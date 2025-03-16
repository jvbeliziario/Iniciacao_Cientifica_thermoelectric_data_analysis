import pyvisa
import time
import keyboard 

rm = pyvisa.ResourceManager()
keithley = rm.open_resource('GPIB0::1::INSTR')

# Configure Keithley to measure voltage on channel 1
keithley.write(":ROUTe:CLOSe (@101)")
keithley.write(":SENSe:FUNCtion 'VOLTage:DC'")


timeList = [] 
voltageList = []  
startTime = time.time() 

print("Starting voltage measurements. Press 'Esc' to stop.")

# Continuous measurement loop (stops when 'Esc' is pressed)
try:
    while not keyboard.is_pressed('esc'):
        # Read voltage from the Keithley device
        voltageReading = float(keithley.query(":SENSe:DATA:FRESh?").split(',')[0][:6])
        
        voltageList.append(voltageReading)
        timeList.append(time.time() - startTime)
        
        print(f"Voltage: {voltageReading} V")
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement interrupted by user.")
finally:
    # Ensure the connection is closed properly
    keithley.close()
    print("Keithley connection closed.")
