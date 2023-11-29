ips = ['100.122.133.105', '100.122.133.111']
for i, j, in enumerate(ips):
    print(f'{i}-{j}')
index = int(input('Your ip is: '))
message = f'You Chose: {ips[index]}'
print(message)