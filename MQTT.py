import serial
import paho.mqtt.publish as publish


channelID = "   "
apiKey = "   "

mqttHost = "mqtt.thingspeak.com"
tTransport = "tcp"
tPort = 1883
tTLS = None

#Topic String
topic = "channels/" + channelID + "/publish/" + apiKey



ser = serial.Serial('COM2', 9600, timeout=1)
ser.flushInput()
while True:
    data = ser.readline()
    if (len(data)>0):
        strData = data.decode("utf-8")
        strData = strData.rstrip("\r\n")
        values = strData.split(",")

        if(len(values) == 2):
            print("Temperature: ",values[0])
            print("Episode: ",values[1])
            
            
            #mqtt string
            T_data = "field1=" + values[0] + "&field2=" + values[1]
            
            try:
                publish.single(topic, payload=T_data, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
                
            except (KeyboardInterupt):
                break
            
            except:
                print("There was an error while publishing the data.")
            
            
            
            
            
            
            