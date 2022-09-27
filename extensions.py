nome = input('Qual é o nome de seu arquivo? ').lower().strip()
if '.gif' in nome:
    print('image/gif')
elif '.jpeg' in nome:
    print('image/jpeg')
elif '.png' in nome:
    print('image/png')
elif '.pdf' in nome:
    print('application/pdf')
elif '.txt' in nome:
    print('text/plain')
elif '.zip' in nome:
    print('application.zip')
elif 'myfile' in nome:
    print('application/octet-stream')