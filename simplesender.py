import serial
import time

def main():
    port = 'COM4'  
    
    ser = serial.Serial(
        port=port,
        baudrate=115200, 
        #bytesize=serial.EIGHTBITS,
        #parity=serial.PARITY_NONE,
        #stopbits=serial.STOPBITS_ONE,
        timeout=2
    )
    
    print(f"Connected to {port}")

    counter = 0
    
    try:
        while True:
            message = f"123\r\n"
            ser.write(message.encode('utf-8'))
            print(f"Sent: {message.strip()}")
            print(f"Count: {counter}\n")
            counter += 1
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nStopping serial transmission")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    finally:
        if ser.is_open:
            ser.close()
            print("Serial port closed")

if __name__ == "__main__":
    main()