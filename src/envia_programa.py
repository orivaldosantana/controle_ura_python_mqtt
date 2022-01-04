# Tk 
import tkinter as tk
from tkinter import ttk

# MQTT 
import random
from paho.mqtt import client as mqtt_client

# Variáveis para MQTT 
broker = 'broker.emqx.io'
port = 1883
topic = "URA001/input"
client_id = f'ura-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker: ", broker)
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client,msg):
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def toFoward():
    print("Para frente!") 
    publish(clientMQTT,"FRT") 

def toBackward():
    print("Para trás!") 
    publish(clientMQTT,"TRS") 

def toLeft():
    print("Para esquerda!") 
    publish(clientMQTT,"ESQ") 

def toStop():
    print("Parar!") 
    publish(clientMQTT,"PAR") 

def toRight():
    print("Para direita!")  
    publish(clientMQTT,"DIR") 

def toSend():
    print("Enviar um programa!")  
    msg = eProgram.get()
    print(msg)
    publish(clientMQTT,msg) 
    
master = tk.Tk()
master.title("Controle MQTT URA")


frm = ttk.Frame(master, padding=6)
frm.grid() 

tk.Button(frm, width=15, text='Frente', command=toFoward).grid(row=1, column=1, pady=4) 
tk.Button(frm, width=15, text='Esquerda', command=toLeft).grid(row=2, column=0, pady=4) 
tk.Button(frm, width=15, text='Parar', command=toStop).grid(row=2, column=1, pady=4) 
tk.Button(frm, width=15, text='Direita', command=toRight).grid(row=2, column=2, pady=4) 
tk.Button(frm, width=15, text='Trás', command=toBackward).grid(row=3, column=1, pady=4) 
tk.Button(frm, width=10, text='Enviar', command=toSend).grid(row=4, column=2, pady=4) 

varProgram = tk.StringVar() 
varProgram.set("")  

eProgram = tk.Entry(frm, width=37,justify=tk.LEFT, textvariable=varProgram)  
eProgram.grid(row=4, columnspan=2,pady=4)

clientMQTT = connect_mqtt()
clientMQTT.loop_start()

master.mainloop()