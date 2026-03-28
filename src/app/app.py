import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model("modelo_digitos.keras")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara. Revisa los permisos o el índice.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret: break

    cv2.rectangle(frame, (200, 150), (450, 400), (0, 255, 0), 2)
    roi = frame[150:400, 200:450]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY_INV)

    resized = cv2.resize(thresh, (28, 28), interpolation=cv2.INTER_AREA)
    
    img_input = resized.reshape(1, 28, 28, 1).astype('float32') / 255.0

    prediction = model.predict(img_input, verbose=0)
    clase_predicha = np.argmax(prediction)
    confianza = np.max(prediction)

    texto = f"Numero: {clase_predicha} ({confianza*100:.1f}%)"
    cv2.putText(frame, texto, (200, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('Lo que ve la cámara ve', frame)
    cv2.imshow('Lo que la IA ve (28x28)', thresh)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()