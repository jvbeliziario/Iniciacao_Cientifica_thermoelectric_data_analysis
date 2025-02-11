import pyvisa

# Initialize PyVISA resource manager
rm = pyvisa.ResourceManager()

# List available VISA resources (connected devices)
print("Available VISA devices:", rm.list_resources())
