import pyvisa
import time
import keyboard 

# Initialize PyVISA resource manager
rm = pyvisa.ResourceManager()

# Connect to the Keithley multimeter (update GPIB address if needed)
keithley = rm.open_resource('GPIB0::1::INSTR')

# Configure Keithley to measure voltage on channel 1
keithley.write(":ROUTe:CLOSe (@101)")
keithley.write(":SENSe:FUNCtion 'VOLTage:DC'")

# Initialize data storage lists
timeList = []  # Store time values
voltageList = []  # Store voltage readings
startTime = time.time()  # Capture the initial timestamp

print("Starting voltage measurements. Press 'Esc' to stop.")

# Continuous measurement loop (stops when 'Esc' is pressed)
try:
    while not keyboard.is_pressed('esc'):
        # Read voltage from the Keithley device
        voltageReading = float(keithley.query(":SENSe:DATA:FRESh?").split(',')[0][:6])
        
        # Append data to lists
        voltageList.append(voltageReading)
        timeList.append(time.time() - startTime)
        
        # Display the reading
        print(f"Voltage: {voltageReading} V")
        
        # Wait before the next reading
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement interrupted by user.")
finally:
    # Ensure the connection is closed properly
    keithley.close()
    print("Keithley connection closed.")
