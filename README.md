# Processo Seletivo – Intensivo Maker | AI

## 📝 Relatório do Candidato

👤 Identificação: LUCAS DO NASCIMENTO SOUZA


### 1️⃣ Resumo da Arquitetura do Modelo

Descreva, em palavras, a arquitetura da **CNN** implementada no arquivo
`train_model.py`.
A arquitetura é básica, simples e de muito facil uso. Ela é dividida em duas partes principais:
1. Extração de características das imagens
Camadas convolucionais + pooling
2. Classificação
Camadas densas

As imagens do dataset tem uma resolução de 28x28 px com um canal de cores. O que viabiliza criar um modelo mais leve ainda.
As principais camadas usadas foram Conv2D e MaxPooling. Que servem para detectar padrões simples (bordas, curvas, traços) e capturar padrões mais complexos.
Também foi usado a camada Flatten que serve para converte os mapas de características 2D em vetor 1D e assim preparar os dados para a parte de classificação.
As camadas Dense estão ali para interpretar as features extraídas e realizar a classificação final.
Este é o fluxo completo da rede:
```text
Imagem (28x28x1)
   ↓
Conv2D (32) + ReLU
   ↓
MaxPooling
   ↓
Conv2D (64) + ReLU
   ↓
MaxPooling
   ↓
Flatten
   ↓
Dense (64) + ReLU
   ↓
Dense (10) + Softmax
   ↓
Probabilidades das classes
```


### 2️⃣ Bibliotecas Utilizadas

Lista das principais bibliotecas utilizadas no projeto com suas versões:
```text
Package            Version
------------------ ---------
keras              3.12.1
numpy              2.2.6
pip                26.0.1
tensorflow         2.21.0
```

### 3️⃣ Técnica de Otimização do Modelo

Explicação da técnica utilizada para otimizar o modelo no arquivo
`optimize_model.py`.<br>
1- Inicialmente o modelo é carregado, observando a arquitetura da CNN, pesos treinados e a configuração de treino.<br>
2- Depois criamos o conversor para traduzir o modelo para um formato leve que seja utilizavel em dispositivos móveis/embarcados.<br>
3- Configuração da otimização que é o mais impactante. Ele converte um numero <br>
```text 
Peso = 0.123456789
```
Para 
```text
Peso = 0.12
```
4- A precisão é reduzida. Mas o desempenho e a velocidade aumentam consideravelmente em dispositivos menos robustos.
5- Depois vem a criação do arquivo já no formato 
```text
.tflite
```


### 4️⃣ Resultados Obtidos

O principal resultado obtido após o treinamento do modelo e otimização é a redução do modelo. Isso possibilita "rodar" o projeto inteiro em simples embarcados.
Tamanho do arquivo:
```text
.h5: 1.4 Mb
   ↓
.tflite: 129 KB
```
Uma redução de 88% no tamanho do arquivo do modelo.
