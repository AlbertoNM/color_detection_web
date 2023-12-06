import cv2

from .cv_tools import color_detection, colors_pixels

def generate():

    # Asignación de cámara
    cap = cv2.VideoCapture(0)

    while True:

        #Leyendo frame de cámara
        ret, frame = cap.read()
        # Volteamos el frame para vernos como espejo
        frame = cv2.flip(frame, 1)

        # Si existe ret que continúe con el proceso del video
        if ret:

            # Hacemos la detección de colores
            color_detection(frame, 5000)

            # Creamos una bandera para comprimir y codificar la imagen
            (flag, encodeImage) = cv2.imencode('.jpg', frame)

            # Si la imagen no se condifica que continue a la siguiente iteración
            # Esto hará que la imagen se descarte en caso de no ser codificada
            if not flag:
                continue

            # Creación de la matriz de bytes para que la consuma el browser
            yield(b'--frame\r\n' b'Conten-Type: image\jpeg\r\n\r\n' + bytearray(encodeImage) + b'\r\n')
