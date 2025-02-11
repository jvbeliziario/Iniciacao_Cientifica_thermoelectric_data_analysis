import pyvisa
import time
import matplotlib.pyplot as plt


# Initialize the keithley and create some useful variables
# Connect to the keithley and set it to a variable named multimeter.
multimeter = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')
# Set the keithley to measure channel 1 of card 1
multimeter.write(":ROUTe:CLOSe (@101)")
# Set the keithley to measure voltage.
multimeter.write(":SENSe:FUNCtion 'VOLTage:DC'")
timeList = []  # Create an empty list to store time values in.
voltageList = []  # Create an empty list to store voltage values in.
startTime = time.time()  # Create a variable that holds the starting timestamp.


# Setup the plot
plt.figure(figsize=(10, 10))  # Initialize a matplotlib figure
# Create a label for the x axis and set the font size to 24pt
plt.xlabel('Elapsed Time (s)', fontsize=18)
plt.xticks(fontsize=18)  # Set the font size of the x tick numbers to 18pt
# Create a label for the y axis and set the font size to 24pt
plt.ylabel('Voltage (mV)', fontsize=18)
# Set the font size of the y tick numbers to 18pt
plt.yticks(fontsize=18)
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Create a while loop that continuously measures and plots data from the keithley forever.
while True:
    # Read and process data from the keithley.
    voltageReading = float(multimeter.query(
        ':SENSe:DATA:FRESh?').split(',')[0][:6])
    # Append processed data to the voltage list
    voltageList.append(voltageReading)
    # Append time values to the time list
    timeList.append(float(time.time() - startTime))
    time.sleep(0.1)  # Interval to wait between collecting data points.
    # Plot the collected data with time on the x axis and voltage on the y axis.
    plt.plot(timeList, voltageList, color='blue', linewidth=3)
    # This command is required for live plotting. This allows the code to keep running while the plot is shown.
    plt.pause(0.01)
