# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>


import time
import datetime


#locale.setlocale(locale.LC_ALL, '')

seconds = time.time()
seconds_formatted = f"{seconds:,.4f}"
print ("Seconds since January 1, 1970:", seconds_formatted, "or " "{:.2e}".format(seconds), "in scientific notation")

date = datetime.datetime.now()
print(date.strftime("%b %d %Y"))