import pyvisa
import time
import matplotlib.pyplot as plt
import msvcrt  
import os


rm = pyvisa.ResourceManager()
keithley = rm.open_resource('GPIB0::28::INSTR')  # Alter GPIB address if necessary


keithley.baud_rate = 57600
keithley.timeout = 10000
keithley.write_termination = '\n'
keithley.read_termination = '\n'

#Keithley instructions
keithley.write("*RST")
keithley.write(":SOUR:FUNC VOLT")           
keithley.write(":SOUR:VOLT 0")              
keithley.write(":OUTP ON")                 
keithley.write(":SENS:FUNC 'CURR'")         
keithley.write(":SENS:CURR:RANG:AUTO ON")   
keithley.write(":FORM:ELEM CURR")           

#Lists
time_list = []
current_list = []
start_time = time.time()


plt.ion()
fig, ax = plt.subplots()
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Corrente (A)")
ax.grid(True)

print("Leitura em andamento. Pressione ESC para parar...\n")

try:
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':  # ESC
            print("Interrupção detectada.")
            break

        current = float(keithley.query(":READ?"))
        elapsed_time = time.time() - start_time

        time_list.append(elapsed_time)
        current_list.append(current)

        ax.clear()
        ax.plot(time_list, current_list, color='blue')
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Corrente (A)")
        ax.grid(True)

        plt.pause(0.05)
        time.sleep(0.1)

except Exception as e:
    print(f"Erro durante leitura: {e}")

finally:
    keithley.write(":OUTP OFF")
    keithley.close()
    plt.ioff()
    plt.show()
    print("Conexão encerrada.")

   #.dat export
    base_name = "corrente_tempo"
    ext = ".dat"
    filename = base_name + ext
    counter = 1
    while os.path.exists(filename):
        filename = f"{base_name}_{counter}{ext}"
        counter += 1

    with open(filename, mode='w') as f:
        f.write("Tempo (s)\tCorrente (A)\n")
        for t, c in zip(time_list, current_list):
            f.write(f"{t:.2f}\t{c:.6e}\n")

    print(f"Dados exportados para: {filename}")
