import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

# Inicializa a captura de vídeo a partir da câmera padrão (índice 0)
cap = cv2.VideoCapture(0)

# Define a largura e altura do quadro de vídeo capturado
cap.set(3, 1280)
cap.set(4, 720)

# Inicializa o controlador do teclado
kb = Controller()

# Inicializa o detector de mãos com um limiar de confiança de detecção de 0.8
detector = HandDetector(detectionCon=0.8)

# Lista que armazena o estado atual dos dedos da mão (0 para fechado, 1 para aberto)
estadoAtual = [0, 0, 0, 0, 0]

# Loop principal
while True:
    # Lê um quadro do vídeo capturado
    _, img = cap.read()

    # Encontra as mãos no quadro usando o detector
    hands, img = detector.findHands(img)

    # Verifica se mãos foram detectadas
    if hands:
        # Obtém o estado dos dedos da primeira mão detectada
        estado = detector.fingersUp(hands[0])

        # Verifica se o estado atual dos dedos é diferente do estado anterior e todos os dedos estão abertos
        if estado != estadoAtual and estado == [1, 1, 1, 1, 1]:
            print('Comandando para frente')

            # Simula a pressão e liberação da tecla de seta para a direita
            kb.press(Key.right)
            kb.release(Key.right)

        # Verifica se o estado atual dos dedos é diferente do estado anterior e somente o dedo médio está aberto
        if estado != estadoAtual and estado == [0, 1, 0, 0, 0]:
            print('Comandando para trás')

            # Simula a pressão e liberação da tecla de seta para a esquerda
            kb.press(Key.left)
            kb.release(Key.left)

        # Atualiza o estado atual dos dedos
        estadoAtual = estado

    # Mostra o quadro com as anotações de rastreamento das mãos em uma janela redimensionada
    cv2.imshow('img', cv2.resize(img, (640, 420)))

    # Aguarda 1 milissegundo por uma tecla antes de prosseguir para a próxima iteração
    cv2.waitKey(1)



