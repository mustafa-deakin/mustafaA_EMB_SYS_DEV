#Library
import RPi.GPIO as GPIO
import time
import requests

#Pin connections
led1 = 27
buzzer = 3
Ping_Pin = 23
Echo_Pin = 24

#State variables
LED_State = False
distance = 0

#GPIO setups
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(Ping_Pin, GPIO.OUT)
GPIO.setup(Echo_Pin, GPIO.IN)
Buzzer_Pwm = GPIO.PWM(buzzer, 100)
Buzzer_Pwm.start(0)

#Methods
def Light_Show():
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(2)
    
def Send_Alert(event_name):
    url = f"https://maker.ifttt.com/trigger/{event_name}/json/with/key/k6WPz-nxslD-pOL8koIst8HO4lWFPe8kcQ46vcpyyWk"
    requests.post(url)

def Buzzer_Cycle():
    Buzzer_Pwm.ChangeDutyCycle(25)
    time.sleep(1)
    Buzzer_Pwm.ChangeDutyCycle(0)

def Read_Ultrasonic_Sensor():
    GPIO.output(Ping_Pin, True)
    time.sleep(0.00001)
    GPIO.output(Ping_Pin, False)
    while GPIO.input(Echo_Pin) == 0:
        SonicP_Start = time.time()
    while GPIO.input(Echo_Pin) == 1:
        SonicP_end = time.time()
    SonicP_Duration = SonicP_end - SonicP_Start
    distance = SonicP_Duration * (40000 / 2)
    return distance
    
try:
    while True:
            USSensor = Read_Ultrasonic_Sensor()
            if USSensor < 10:
                print("Motion Detected!")
                Light_Show()
                Buzzer_Cycle()
                Send_Alert("intruder_detected")               
                time.sleep(0.03)
            else:
                GPIO.output(led1, GPIO.LOW)

#Reset GPIO pins
except KeyboardInterrupt: 
    GPIO.cleanup()
    Buzzer_Pwm.stop()