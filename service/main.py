from kivy.lib import osc
from time import sleep
from plyer import vibrator,notification,battery
import pyjokes
def ping(*args):
    print("hello world")
    #vibrator.vibrate(.5)
    #notification.notify(title="love",message="pyconGH")
    joke = pyjokes.get_joke()
    print(battery.get_state()['percentage'],joke)

if __name__ == "__main__":
    osc.init()
    oscid = osc.listen(ipAddr="0.0.0.0",port=3000)
    osc.bind(oscid,ping,"/ping")

    while True:
        osc.readQueue(oscid)
        ping()
        sleep(10)
