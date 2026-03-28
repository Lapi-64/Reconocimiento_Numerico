# Reconocimiento Numérico

Este proyecto implementa un sistema de reconocimiento de dígitos manuscritos utilizando aprendizaje profundo (Deep Learning) con TensorFlow y OpenCV. El modelo se entrena con el dataset MNIST y luego se utiliza la cámara del dispositivo para reconocer en tiempo real los números escritos a mano.

## Estructura del proyecto

```
Reconocimiento_Numerico/
│   modelo_digitos.keras         # Modelo entrenado guardado
│   prueba.py                   # Prueba de la cámara
│   README.md                   # Este archivo
│
└───src/
	├───app/
	│       app.py              # App de reconocimiento en tiempo real
	└───Modelo/
			Entrenamiento.py    # Entrenamiento del modelo
```

## Dependencias

- Python 3.8+
- TensorFlow
- OpenCV
- NumPy

Puedes instalar las dependencias principales con:

```bash
pip install tensorflow opencv-python numpy
```

## Uso

### 1. Entrenar el modelo

Ejecuta el script de entrenamiento para crear el modelo:

```bash
python src/Modelo/Entrenamiento.py
```

Esto generará el archivo `modelo_digitos.keras`.

### 2. Probar la cámara (opcional)

Puedes probar que la cámara funciona con:

```bash
python prueba.py
```

### 3. Ejecutar el reconocimiento en tiempo real

Ejecuta la aplicación principal:

```bash
python src/app/app.py
```

Coloca un número manuscrito dentro del recuadro verde que aparece en la ventana de la cámara. El modelo predecirá el dígito y mostrará la confianza.

## Notas

- El modelo utiliza el dataset MNIST, que se descarga automáticamente la primera vez.
- El reconocimiento funciona mejor con números escritos en fondo claro y gruesos.
- Presiona la tecla `x` para cerrar la aplicación de cámara.
