import pyvisa
import time
import matplotlib.pyplot as plt



multimeter = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')
# Set the keithley to measure channel 1 of card 1
multimeter.write(":ROUTe:CLOSe (@101)")
# Set the keithley to measure voltage.
multimeter.write(":SENSe:FUNCtion 'VOLTage:DC'")
timeList = [] 
voltageList = []
startTime = time.time()


# Setup the plot
plt.figure(figsize=(10, 10))
plt.xlabel('Elapsed Time (s)', fontsize=18)
plt.xticks(fontsize=18)
plt.ylabel('Voltage (mV)', fontsize=18)
plt.yticks(fontsize=18)
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Create a while loop that continuously measures and plots data from the keithley forever.
while True:
    # Read and process data from the keithley.
    voltageReading = float(multimeter.query(
        ':SENSe:DATA:FRESh?').split(',')[0][:6])
    voltageList.append(voltageReading)
    timeList.append(float(time.time() - startTime))
    time.sleep(0.1)
    plt.plot(timeList, voltageList, color='blue', linewidth=3)
    plt.pause(0.01)
