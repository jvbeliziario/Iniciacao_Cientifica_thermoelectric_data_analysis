# Automação e Análise de Dados para Medição da Constante de Seebeck  

Este repositório contém scripts desenvolvidos para a automação laboratorial e análise de dados no contexto da medição da **Constante de Seebeck** em filmes condutores impressos. O projeto está vinculado a pesquisas acadêmicas em um projeto de iniciação científica em colaboração com a **Universidade Paulista Julio de Mesquita Filho (Unesp)**, o **Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPQ)** e a **Indústria de Tintas Condutivas TICON**, visando o desenvolvimento de novos materiais eletrônicos e aprimoramento de técnicas de caracterização termoelétrica.  

##  Objetivo do Projeto  
O projeto tem como foco:  
✅ Desenvolvimento de algoritmos para **automação laboratorial** na aquisição de dados.  
✅ Implementação de **ferramentas de Ciência de Dados** para análise descritiva, preditiva e diagnóstica.  
✅ Integração de equipamentos de medição como **Keithley 2001 e Arduino Uno** para coleta eficiente de dados.  
✅ Visualização em **tempo real** e exportação de dados para posterior análise.  

---

##  Tecnologias Utilizadas  
Os scripts foram desenvolvidos em **Python** e utilizam as seguintes bibliotecas:  
📌 `pyvisa` → Comunicação com instrumentos via GPIB.  
📌 `serial` → Comunicação via USB com o Arduino.  
📌 `matplotlib` → Geração de gráficos para visualização dos dados.  
📌 `pandas` → Estruturação e exportação de dados para Excel.  
📌 `numpy` → Processamento matemático e tratamento de dados.  
📌 `keyboard` → Controle de interrupção do programa via teclado.  

---

##  Descrição dos Programas  

 **1. `list_devices.py`**  
 **Objetivo:** Lista todos os dispositivos conectados via PyVISA, verificando a comunicação com instrumentos como o Keithley 2001.  

 **2. `keithley2001_voltage_live_monitor.py`**  
 **Objetivo:** Mede a voltagem utilizando a **Keithley 2001** e exibe o valor no terminal.  
🔹 Configura o equipamento via GPIB.  
🔹 Faz medições contínuas até interrupção manual.  

**3. `keithley2001_liveplot.py`**  
 **Objetivo:** Mede a voltagem e exibe um gráfico em **tempo real** da variação da tensão.  
🔹 Plota os dados adquiridos ao longo do tempo.  
🔹 Permite interrupção com a tecla **Esc**.  

 **4. `arduino_dual_temp_plot.py`**  
 **Objetivo:** Lê a temperatura de **dois sensores conectados ao Arduino Uno** e plota os valores em tempo real.  
🔹 Comunicação via porta **USB (Serial)**.  
🔹 Visualização gráfica contínua das medições de temperatura.  

 **5. `keithley2410_voltage_liveplot_datexport.py`**  
 **Objetivo:** Mede a voltagem e exibe um gráfico em **tempo real** da variação da tensão e também exporta dados em formato .dat para análise posterior em Origin.  
🔹 Plota os dados adquiridos ao longo do tempo.  
🔹 Permite interrupção com a tecla **Esc**.   


---


