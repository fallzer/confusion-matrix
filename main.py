import random #para gerar números aleatórios
import os # para limpar o terminal (cls para Windows, clear para Linux/Mac)
from sklearn.metrics import confusion_matrix
import seaborn as sns # para criar gráficos de matriz de confusão mais bonitos
import matplotlib.pyplot as plt # para mostrar os gráficos


#================ MENU INICIAL =========================================================================

def menu():
    print("=" * 50 )
    print("MATRIZ DE CONFUSÃO")
    print("=" * 50)
    print("1 - AMOSTRA PRESETADA")
    print("2 - QUANTIDADE DE AMOSTRAS ALEATÓRIAS")
    print("3 - AMOSTRA PERSONALIZADA")
    print("=" * 50)

    opcao = input("Escolha uma opção: ")
    return opcao

opcao = menu()

#================ OPÇÃO 1 =========================================================================

if opcao == "1":
    os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

    print("AMOSTRA PRESETADA\n")
    
    print("Escolha a opção de amostra presetada\n")
    print("1 - Opção de 10 amostras")
    print("2 - Opção de 200 amostras")

    sub_opcao = input("Escolha uma opção: ")

    if sub_opcao == "1":
        os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

        lista_prev = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
        lista_real = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]

        print(f"previsto = {lista_prev}")
        print(f"real     = {lista_real}")



    elif sub_opcao == "2":
        os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

        lista_prev = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
        lista_real = [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]

        print(f"previsto = {lista_prev}")
        print(f"real     = {lista_real}")


    #SE NAO ESCOLHER NENHUMA DAS AMOSTRAS DISPONIVEIS ELE CAI AQUI ==================================
    else:
        os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

        print("opção inválida")

#================ OPÇÃO 2 =========================================================================

elif opcao == "2":
    os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

    print("AMOSTRA ALEATÓRIA\n")

    try:

        quantidade = int(input("Quantas amostras você quer? "))

   
        # random.randint(0, 1) >>> sorteia um número inteiro aleatório entre 0 e 1
        # for _ in >>> o _ é uma variável descartável, usada quando você não precisa do valor do contador, só da repetição
        # range(quantidade) >>> repete o processo X vezes (o número que você digitou)
        lista_prev = [random.randint(0, 1) for _ in range(quantidade)]
        lista_real = [random.randint(0, 1) for _ in range(quantidade)]
        #lista_prev = [sorteia 0 ou 1, repita isso X vezes]

        # valor = random.choice([True, False])
        # valor = random.choice(["verdadeiro", "falso"])

        print(f"\nprevisto = {lista_prev}")
        print(f"real = {lista_real}")

    except ValueError: #caso o usuário digite algo que não seja um número inteiro
        os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

        print("Por favor, digite um número inteiro válido.")

#================ OPÇÃO 3 =========================================================================

elif opcao == "3":
    os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

    print("AMOSTRA PERSONALIZADA\n")

    try:
        quantidade = int(input("Quantas amostras você quer? "))

        lista_prev = []
        lista_real = []

        for i in range(quantidade):
            valor_prev = int(input(f"Digite o valor PREVISTO para a amostra {i+1} (0 ou 1): "))
            if valor_prev not in [0, 1]:
                raise ValueError("Os valores devem ser 0 ou 1.")
            lista_prev.append(valor_prev)

        for i in range(quantidade):
            valor_real = int(input(f"Digite o valor REAL para a amostra {i+1} (0 ou 1): "))
            if valor_real not in [0, 1]:
                raise ValueError("Os valores devem ser 0 ou 1.")
            lista_real.append(valor_real)

        print(f"\nprevisto = {lista_prev}")
        print(f"real = {lista_real}")

    except ValueError: #caso o usuário digite algo errado
        os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

        print("opção invalida")


# SE NAO ESCOLHER NENHUMA DAS OPÇÕES DO MENU INICIAL ELE CAI AQUI ==================================
else:
    os.system('cls' if os.name == 'nt' else 'clear') #limpa terminal

    print("opção inválida")


#==== aqui faz funcionar o grafico ===========================================================================


mc = confusion_matrix(lista_real, lista_prev)


#CALCULANDO METRICAS
TP = mc[1][1] # Verdadeiro Positivo
TN = mc[0][0] # Verdadeiro Negativo
FP = mc[0][1] # Falso Positivo
FN = mc[1][0] # Falso Negativo

acuracia = (TP + TN) / sum(sum(mc)) #ACURÁCIA
precisao = TP / (TP + FP) #PRECISÃO
recall = TP / (TP + FN) #RECALL
f1_score = 2 * (precisao * recall) / (precisao + recall) #F1-SCORE

# CRIA OS DOIS ESPAÇOS LADO A LADO
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# GRAFICO MATRIZ CONFUSÃO
labels_mc = [['TN', 'FP'], ['FN', 'TP']]
annot_mc = [[f"{labels_mc[i][j]}\n{mc[i][j]}" for j in range(2)] for i in range(2)]
sns.heatmap(mc, annot=annot_mc, cmap='Greens', fmt='', cbar=False, ax=ax1)
ax1.set_xlabel('Preditos')
ax1.set_ylabel('Reais')
ax1.set_title('Matriz de Confusão')

# GRAFICO DE PIZZA
labels = ['TP', 'TN', 'FP', 'FN']
valores = [TP, TN, FP, FN]
cores = ['#2ECC71', '#3498DB', '#E67E22', '#E74C3C']
ax2.pie(valores, labels=labels, autopct='%1.1f%%', colors=cores)
ax2.set_title('Gráfico de pizza')

# METRICAS
metricas = f"Acurácia: {acuracia:.2f}  |  Precisão: {precisao:.2f}  |  Recall: {recall:.2f}  |  F1-Score: {f1_score:.2f}"
plt.figtext(0.5, 0.01, metricas, ha='center', fontsize=10)
plt.tight_layout()
plt.show()