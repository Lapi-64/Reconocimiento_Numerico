import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se puede recibir el frame. Saliendo...")
        break
        
    cv2.imshow('Prueba de Camara', frame)
    
    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()