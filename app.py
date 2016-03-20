import serial, time, glob

ser = serial.Serial()
ser.port = '/dev/tty.usbmodem14111'
ser.baudrate = 115200
ser.timeout = 1

ser.open()

def _parse_cpbr_row(s):
    """Parses a cpbr row data into a dictionary."""
    index, number, type, name = s.strip('+CPBR: ').split(',')
    return {
        'index': int(index),
        'number': number.replace('"', '').rstrip(),
        'type': int(type),
        'name': name.replace('"', '').rstrip(),
    }

def _parse_cpbr(s):
    """Parses cpbr response."""
    s = s.strip().rstrip()
    _numbers = []
    for l in s.split('\n'):
        if l[:6] == '+CPBR:':
            _numbers.append(_parse_cpbr_row(l))
    return _numbers


def sim_msisdn():
	ser.write('AT+CPBS=SM\r')

	time.sleep(0.5)
	ser.write('AT+CPBR=1,100\r')



	time.sleep(0.5)

	res = ser.readall()
	numbers = _parse_cpbr(res)

	for num in numbers:
	    if num['name'] == 'My Number':
	        return num['number']


print sim_msisdn()