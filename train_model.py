# Developed by @lucns

from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Carregamento do pre processo
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# Construir o modelo CNN
model = models.Sequential([                                                                     # EXPLICAÇÃO DAS CAMADAS
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),      # "relu" = função de ativação (remove valores negativos)
    layers.MaxPooling2D((2, 2)),                                                                # Camada de redução (reduz a imagem pegando o maior valor de cada bloco 2x2)
    layers.Conv2D(64, (3, 3), activation='relu'),                              # 64 mais filtros (modelo mais profundo) e 3x3 mesmo tabamho de janela
    layers.MaxPooling2D((2, 2)),                                                                # Outra redução
    layers.Flatten(),                                                                           # Transforma a matriz 2D em vetor 1D
    layers.Dense(64, activation='relu'),                                                  # 64 é o número de neurônios e "relu' é a ativação
    layers.Dense(10, activation='softmax')                                                # 10 é o numero de classes e "softmax" transforma saída em probabilidades
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=3, batch_size=64)

model.save('model.h5')
print("Modelo salvo em model.h5")
