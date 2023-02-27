import cv2
from time import sleep

# Cores
B = '\033[0m'  # branco
V = '\033[31m'  # vermelho
A = '\033[34m'  # azul
R = '\033[35m'  # roxo

contador = 1

cam1 = {'lugar' : 'do Canal 6' , 'url' : "https://egov.santos.sp.gov.br/santosmapeada/css/img/cameras/cam1593/snap_c1.jpg?1677157043869"}
cam2 = {'lugar' : 'da Canoagem', 'url' : "https://egov.santos.sp.gov.br/santosmapeada/css/img/cameras/cam1464/snap_c1.jpg?1677191520757"}
cam3 = {'lugar' : 'da Praça do Sapo', 'url' : 'https://egov.santos.sp.gov.br/santosmapeada/css/img/cameras/cam1517/snap_c1.jpg?1677240440260'}
cam4 = {'lugar': 'da Travessia da balsa', 'url': 'https://egov.santos.sp.gov.br/santosmapeada/css/img/cameras/cam1455/snap_c1.jpg?1677248602110'}
cam5 = {'lugar': 'da Epitácio Pessoa com Oswaldo Chocrane', 'url': 'https://egov.santos.sp.gov.br/santosmapeada/css/img/cameras/cam1584/snap_c1.jpg?1677311079649'}
cam6 = {'lugar': 'da Epitacio Pessoa', 'url': 'https://egov.santos.sp.gov.br/santosmapeada/css/img/cameras/cam1578/snap_c1.jpg?1677311184499'}
cam7 = {'lugar': 'do CPE', 'url': 'https://egov.santos.sp.gov.br/santosmapeada/css/img/cameras/cam1561/snap_c1.jpg?1677311246793'}
cam8 = {'lugar': 'do Canal 4', 'url': 'https://egov.santos.sp.gov.br/santosmapeada/css/img/cameras/cam1591/snap_c1.jpg?1677311286046'}
cam9 = {'lugar': 'do porto', 'url': 'https://www.youtube.com/c45f81cd-39f3-465e-83a3-c0dad6173779'}

cameras = [cam1, cam2, cam3, cam4, cam5, cam6, cam7, cam8, cam9]

print(R + '-' * 54)
print(V + """⠀⠀⠀⠀⠀⠀⠈⣷⣄⠀⠀⠀⠀⣾⣷⠀⠀⠀⠀⣠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀   
⠀⠀⠀⠀⠀⠀⠀⢿⠿⠃⠀⠀⠀⠉⠉⠁⠀⠀⠐⠿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀      O V1G1L4NTE 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀    Acesso a cameras
⠀⠀⠀⣠⣶⣿⣿⡿⣿⣿⣿⡿⠋⠉⠀⠀⠉⠙⢿⣿⣿⡿⣿⣿⣷⣦⡀⠀⠀⠀        de Santos
⠀⢀⣼⣿⣿⠟⠁⢠⣿⣿⠏⠀⠀⢠⣤⣤⡀⠀⠀⢻⣿⣿⡀⠙⢿⣿⣿⣦⠀⠀       
⣰⣿⣿⡟⠁⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣿⡟⠀⠀⠈⣿⣿⡇⠀⠀⠙⣿⣿⣷⡄   
⠈⠻⣿⣿⣦⣄⠀⠸⣿⣿⣆⠀⠀⠀⠉⠉⠀⠀⠀⣸⣿⣿⠃⢀⣤⣾⣿⣿⠟⠁
⠀⠀⠈⠻⣿⣿⣿⣶⣿⣿⣿⣦⣄⠀⠀⠀⢀⣠⣾⣿⣿⣿⣾⣿⣿⡿⠋⠁⠀⠀    por Heric M. 2023  
⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣷⡦⠀⠀⠀⢀⣀⣀⠀⠀⠀⢴⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠙⢷⠀⠀⠀⠀⠀⠀⠀⠀""")
print(R + ' --------------->  Escolha o local  <-----------------')

while True:
    entrada = int(input(V + ' [0] Canal 6 \n [1] Canoagem \n [2] Praça do sapo \n [3] Travessia da balsa '
                        '\n [4] Epitácio Pessoa e Oswaldo Cochrane (sentido c5) \n [5] Canal 4 (sentido SV) '
                        '\n [6] Centro de Paquera do Embaré \n [7] Canal 4 sentido (Epitácio Pessoa) \n'))

    if entrada == 8:
        print(R + 'saindo...')
    break

while True:
    print(R + f'Abrindo frame {contador} da camera {cameras[entrada]["lugar"]} em tempo real ')
    cap = cv2.VideoCapture(cameras[entrada]["url"])
    sleep(6)
    ret, img = cap.read()
    cv2.imshow(f'Vigilante Santos - Exibindo cam {cameras[entrada]["lugar"]} ', img)
    contador += 1

    if cv2.waitKey(1) == ord('q'):
        exit(0)
cv2.destroyAllWindows()
