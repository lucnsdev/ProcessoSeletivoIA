def runApp():
    with open("train_model.py") as f: exec(f.read())        # executa o arquivo de treino e gera o modelo.h5
    with open("optimize_model.py") as f: exec(f.read())     # executa o arquivo de optimizacao e gera o modelo.tflite

if __name__ == '__main__':
    print("Este arquivo executa os dois scripts de forma sequencial. Foi criado para ser usado pelo Github Actions.")
    runApp()