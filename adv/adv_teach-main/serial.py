import serial
ser = serial.Serial()
ser.port = 2      #actually COM3
ser.baudrate = 115200
ser.open()
ser.write("Hello")
ser.close()