import json
import ast
print(chr(27) + "[2J")
msg = {'sample_rate':200, 'station_number':4}
print(msg)
print(type(msg))

msg = '[{\"sample_rate\":200, \"station_number\":4}]'
print(msg)
print(type(msg))
msg=str.encode(msg)
print(msg)
print(type(msg))

msg=msg.decode('utf8')
print(msg)
print(type(msg))

msg=msg[1:-1]
print(msg)
print(type(msg))

# msg=json.loads(msg)
msg = ast.literal_eval(msg)
# msg=msg[-1:]
print(msg)
# msg=msg[:-1]
# print(msg)

print(type(msg))

# msg={'sample_rate':400}
print(msg['sample_rate'])
# print(msg['sample_rate'])
# print(f'dictionary sample rate is {msg["sample_rate"]}')

# msg=msg.encode('UTF-8')

# print(f'test message {msg}')