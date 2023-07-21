from datetime import *
from dateutil.relativedelta import *
import time
import random

now = datetime.now()
print(now)

#now = now + relativedelta(months=1, weeks=1, hour=10)
time.sleep(random.randint(0, 20000)/10000)
now = datetime.now()

print(now)