#Crie uma função que verifique se as respostas estão corretas ou não;

#receber a resposta do utilizador
#comparar as respostas

def check_answers(real, utilizador):
    #real seria uma dicionario com 5 dicionarios (resposta real)
    #utilizador lista 5 keys (resposta utilizador)
    point = 0
    for a in range (0, len(real)):
        right_ans =  list(real.values())[a].replace(' ', '').lower()
        right_ans = right_ans["answer"]

        for i in range(0, len(utilizador)):
            if right_ans == utilizador[i][1].replace(' ', '').lower():
                point +=1


    return point

