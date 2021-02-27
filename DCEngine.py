import RPi.GPIO as GPIO
from Engine import Engine


class DCEngine(Engine):
    __port_in1 = 24
    __port_in2 = 23
    __port_enA = 25
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(__port_enA, GPIO.OUT)
    __pwm = GPIO.PWM(__port_enA, 1000)

    def __init__(self) -> None:
        super().__init__()
        self.setup()

    def setup(self) -> None:
        super().setup()
        GPIO.setwarnings(False)
        GPIO.setup(self.__port_in1, GPIO.OUT)
        GPIO.setup(self.__port_in2, GPIO.OUT)
        GPIO.output(self.__port_in1, GPIO.LOW)
        GPIO.output(self.__port_in2, GPIO.LOW)
        self.__pwm.start(70)

    def start(self) -> None:
        super().start()
        GPIO.output(self.__port_in1, GPIO.HIGH)
        GPIO.output(self.__port_in2, GPIO.LOW)

    def stop(self) -> None:
        super().stop()
        GPIO.output(self.__port_in1, GPIO.LOW)
        GPIO.output(self.__port_in2, GPIO.LOW)

    def getstatus(self) -> object:
        return super().getstatus()

    def setSpeed(self, speed):
        super().setSpeed(speed)
        self.__pwm.ChangeDutyCycle(speed)
