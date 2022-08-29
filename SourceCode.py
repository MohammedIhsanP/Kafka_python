import datetime
from time import sleep
import random

while True:
    period = datetime.datetime.now()
    if((period.second % 5) == 0):
        temp = random.randrange(10, 40, 3)
        print(temp)
        sleep(1)