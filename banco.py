oi = str(input('Greeting: ')).lower().strip()
if 'hello' in oi:
    print(f'$0')
elif 'h' == oi[0]:
    print(f'$20')
else:
    print('$100')
