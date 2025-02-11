import serial
import time
import matplotlib.pyplot as plt

# Serial port configuration
arduino_port = 'COM3'  # Change to the correct port
baud_rate = 9600  # Must match the Arduino's baud rate

# Initialize serial connection with Arduino
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Wait for the serial connection to establish

print(f"Connected to Arduino on port {arduino_port}")

# Lists to store time and temperature values
time_list = []  # Store time values
temperature_list_1 = []  # Store temperature values from sensor 1
temperature_list_2 = []  # Store temperature values from sensor 2
start_time = time.time()  # Initial timestamp

# Configure the plot
plt.figure(figsize=(10, 10))
plt.xlabel('Time (s)', fontsize=18)
plt.xticks(fontsize=18)
plt.ylabel('Temperature (°C)', fontsize=18)
plt.yticks(fontsize=18)
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')


def read_temperatures():
    """Reads temperature data from the Arduino via serial communication."""
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        data = line.split(',')
        try:
            temp1 = float(data[0])
            temp2 = float(data[1])
            return temp1, temp2
        except (ValueError, IndexError):
            pass  # Ignore invalid or incomplete data
    return None, None


# Continuous loop to read and plot data in real-time
while True:
    temp1, temp2 = read_temperatures()
    if temp1 is not None and temp2 is not None:
        current_time = time.time() - start_time
        temperature_list_1.append(temp1)
        temperature_list_2.append(temp2)
        time_list.append(current_time)

        # Update the plot
        plt.clf()  # Clear the current figure
        plt.plot(time_list, temperature_list_1, label='Sensor 1', color='blue')
        plt.plot(time_list, temperature_list_2, label='Sensor 2', color='red')
        plt.legend()
        plt.pause(0.01)  # Pause to update the plot

    time.sleep(0.1)  # Interval between data collection
