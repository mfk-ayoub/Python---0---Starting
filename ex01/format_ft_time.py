import time
from datetime import datetime

current_time_seconds = time.time()
current_time_scientific = f"{current_time_seconds:.2e}"

current_date = datetime.now()
formatted_date = current_date.strftime("%b %d %Y")


print(f"Seconds since January 1, 1970: {current_time_seconds:.2f} or {current_time_scientific} in scientific notation")
print(f"{formatted_date}")
