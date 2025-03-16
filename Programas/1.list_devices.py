import pyvisa

# Initialize PyVISA resource manager and list available connected devices.

rm = pyvisa.ResourceManager()
print("Available VISA devices:", rm.list_resources())
