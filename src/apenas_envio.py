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
    msg_count = 0


    #msg = f"counter: {msg_count}"
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    msg_count += 1


def toFoward():
    print("Para frente!") 
    publish(clientMQTT,"FRT") 

def toBackward():
    print("Para trás!") 
    publish(clientMQTT,"TRS") 

def toLeft():
    print("Para esquerda!") 
    publish(clientMQTT,"ESQ") 

def toRight():
    print("Para direita!")  
    publish(clientMQTT,"DIR") 


master = tk.Tk()

frm = ttk.Frame(master, padding=6)
frm.grid() 

tk.Label(frm, text="Controle URA").grid(row=0, columnspan=3) 
tk.Button(frm, width=20, text='Frente', command=toFoward).grid(row=1, column=1, pady=4) 
tk.Button(frm, width=20, text='Esquerda', command=toLeft).grid(row=2, column=0, pady=4) 
tk.Button(frm, width=20, text='Direita', command=toRight).grid(row=2, column=2, pady=4) 
tk.Button(frm, width=20, text='Trás', command=toBackward).grid(row=3, column=1, pady=4) 


clientMQTT = connect_mqtt()
clientMQTT.loop_start()
master.mainloop()