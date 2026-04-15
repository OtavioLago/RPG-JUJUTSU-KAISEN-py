import time 
import random
print (30*"-")
print ("RPG de mesa")
print (30*"-")
turno = " " 
acao = " "
porta_aberta = False
porta_sala2 = False
pergaminho_vermelho = False
#dados do jogador
habilidades = ["soco", "chute"]
mochila = [""]
print ("\nSALA 1")
while porta_aberta == False :
    print ("\nVoce esta em uma sala com um armario e uma porta, oque voce faz? (Abro a porta/Mexo no armario)")
    acao = (input("\ndiga sua açao: "))
    #armario
    if acao == "Mexo no armario".lower() .strip() :
        if "Pergaminho_azul" in mochila :
            print ("\no armario esta vazio agora, sua unica opção é sair da sala")
        else :
            print ("voce encontrou um pergaminho azul, deseja pegar? (S/N)")
            pegar = input("\nvoce pega?(S/N)") .lower() .strip()
            if pegar == "s" :
                mochila.append("Pergaminho_azul")
                print (f"\nsua mochila agora possui {mochila}")
            elif pegar == "n" :
                print ("voce deixa ele la, que estranho, voce sente que deveria ter pego")
            else :
                print ("comando invalido!, voce se atrapalhou e nao pegou nada")
    #sala 2
    elif acao == "Abro a porta".lower() .strip() :
        time.sleep(1)
        print ("\nSALA 2")
        print ("\nVoce abre a porta e ve uma outra sala com um simbolo no chao e mais um armario com gavetas ao lado, e uma porta, ela parece sombria")
        porta_aberta = True
    else :
        print ("\nCOMANDO INVALIDO")
    #turno simbolo
evento_simbolo = False
while porta_sala2 == False :
    turno = (input("o que voce faz? \n(me aproximo do simbolo/abro as gavetas e o armario/abro a porta sombria)"))
        #troca confirmada
    if turno == "me aproximo do simbolo" :
        if evento_simbolo == False :
            print ("\nUma criatura aparece e pergunta se voce quer fazer uma troca")
            print ("\nela disse que essa troca consiste em um poder absurdamente forte, porem voce perdera algo em troca")
            troca = (input("voce aceita essa troca? (S/N)")).lower() .strip()
            if troca == "s" :
                gojo = ["azul", "vermelho", "roxo", "expansao", "energia reversa"]
                print (f"voce recebe os seguintes poderes: {gojo}, porem, voce se sente muito triste de uma vez")
                habilidades.extend (gojo)
                print(f"Suas habilidades agora são: {', '.join(habilidades)}")
                evento_simbolo = True
        #troca negada
            elif troca == "n" :
                print ("troca recusada, a criatura some juntamente com o simbolo")
                print ("logo apos ela sumir, aparece uma porta sombria")
                evento_simbolo = True
        #resposta invalida
            else :
                print ("comando invalido, digite as opcoes possiveis")
        else :
            print ("o simbolo sumiu")
    elif turno == "abro as gavetas e o armario" :
        if pergaminho_vermelho == True :
            print ("\nesta vazio")
        else :
            print ("\nvoce encontrou um pergaminho vermelho!")
            pergaminho_vermelho = input("\nvoce pega? (S/N)") .lower() .strip()
            if pergaminho_vermelho == "s" :
                mochila.append ("Pergaminho_vermelho")
                print ("voce pegou esse pergaminho")
                print (f"agora na sua mochila possui: {mochila}")
                pergaminho_vermelho = True
            elif pergaminho_vermelho == "n" :
                if "Pergaminho_azul" in mochila :
                    print ("voce o deixa la, mas o pergaminho azul pulsa e voce sente que devia ter pego")
                else :
                    print ("voce o deixa la")
            else :
                print ("comando invalido")
    #resposta da 1 sala invalida
    elif turno == "abro a porta sombria" :
        print ("voce abre a porta e sente um peso gigantesco sobre seus ombros \nvoce ve uma criatura sombria de 3 metros exalando vontade de matar")
        print ("\nO COMBATE COMECOU")
        porta_sala2 = True 
    else :
        print ("COMANDO INVALIDO, escreva exatamente do jeito que esta")
V_jogador = 1
V_monstro = 1
itadori = ["punho_divergente", "desmantelar", "sangue_perfurante"]
if "roxo" in habilidades or "punho_divergente" in habilidades :
    V_jogador = 250
    V_monstro = 750
    dano_monstro = 45
    soco_monstro = 10
    dano_soco = 15
    dano_chute = 20
    dano_azul = 50
    dano_vermelho = 50
    dano_roxo = 100
    dano_expansao = 150
    ea_max = 150
    ea_atual = 150
    ea_monstro = 200
    ea_maxmonstro = 200
    print ("\na criatura sente seu poder e ruge muito alto com uma vontade de matar exalando dela")
    print ("\nnome da criatura: ENTITY (FORMA ABSOLUTA)")
else :
    V_jogador = 100
    V_monstro = 200
    dano_monstro = 20
    ea_max = 0
    ea_atual = 0
    ea_monstro = 0
    ea_maxmonstro = 0
    dano_soco = 15
    dano_chute = 20
    print ("a criatura te subestima por sem um ser humano comum, ela apenas se posiciona em reacao superior")
    print ("nome da entidade ENTITY (FORMA CONTIDA)")
usou_azul = False
usou_vermelho = False
while V_jogador > 0 and V_monstro > 0 :
    print (30*"=")
    print (f"Sua vida: {V_jogador} Sua EA: {ea_atual} \nVida do boss: {V_monstro} EA do monstro: {ea_monstro}")
    ataque = input(f"qual ataque voce vai usar?, ataques : {habilidades}")
    if ataque == "soco":
        sorte = random.randint(1, 5)
        if sorte == 5:
            dano_k = int(dano_soco * 2.5)
            print(f" O monstro recebeu {dano_k} de dano e ficou com {V_monstro} de vida.")
            print ("Por um segundo voce enxerga preto e vermelho, e seu corpo automaticamente grita: KOKUSEEEN")
            V_monstro -= dano_k
            ea_atual = min(ea_max, ea_atual + 20)
            if "roxo" not in habilidades and "punho_divergente" not in habilidades:
                print ("modo FLUXO, voce despertou poderes apos descobrir a essencia da energia amaldicoada")
                habilidades.extend(itadori)
                ea_max = 150
                ea_atual = 150
                dano_soco = 25
                V_jogador = 400
                V_monstro = 1000 - dano_k
                ea_monstro = 200
                ea_maxmonstro = 200
                dano_monstro = 45
        else :
            print (f"voce acertou um soco, causou {dano_soco} de dano")
            V_monstro -= dano_soco
            ea_atual = min(ea_max, ea_atual + 10)
    elif ataque == "punho_divergente" and "punho_divergente" in habilidades :
        if ea_atual >= 20:
            if random.randint(1, 3) == 1:
                dano_k = int(45 * 2)
                print ("KOKUSEEN")
                V_monstro -= dano_k
                ea_atual -= 15
            else :
                print ("impacto duplo, dano 45")
                V_monstro -= 45
                ea_atual -= 20
        else :
            print ("ea insuficiente!")
        if ea_atual > ea_max :
            ea_atual = ea_max
    elif ataque == "desmantelar" and "desmantelar" in habilidades :
        if ea_atual >= 50 :
            if random.randint(1, 5) == 1 :
                corte_m = int(50 * 10)
                print ("voce libera energia pura")
                time.sleep(2)
                print ("\ntwin meteors, two recoil!, scale of DRAGON!")
                time.sleep(2)
                print ("CORTE MUNDIAL, 500 de dano")
                V_monstro -= 500
                ea_atual -= 75
            else :
                print ("\nDESMANTELAR, 50 de dano")
                V_monstro -= 50
                ea_atual -= 50
        else : 
            print ("EA insuficiente, voce falha o ataque")
    elif ataque == "sangue_perfurante" and "sangue_perfurante" in habilidades :
        if ea_atual >= 25 :
            print ("\nsangue perfurante, voce causa 50 de dano")
            V_monstro -= 50
            ea_atual -= 25
        else :
            print ("EA insuficiente, voce falhou o ataque")
    elif ataque == "chute" :
        print ("voce acertou um chutao nele, tirou 20 de vida e recuperou 5 de EA")
        V_monstro -= 20
        ea_atual += 5
        if ea_atual > ea_max :
            ea_atual = ea_max
    elif ataque == "azul" and "azul" in habilidades :
        custo_azul = 35
        if ea_atual >= custo_azul :
            print ("\nAMPLIFICACAO DE FEITICO, AZUL")
            print ("voce tirou 50 de vida")
            V_monstro -= 50
            ea_atual -= 35
            usou_azul = True
        else :
            print ("voce é incapaz de usar isto, te falata EA")
    elif ataque == "vermelho" and "vermelho" in habilidades :
        custo_vermelho = 35
        if ea_atual >= custo_vermelho :
            print ("\nREVERSAO DE FEITICO, VERMELHO")
            print ("voce tirou 50 de vida")
            V_monstro -= 50
            ea_atual -= 35
            usou_vermelho = True 
        else : 
            print ("voce nao pode usar isto, te falta EA")
    elif ataque == "roxo" and "roxo" in habilidades :
        custo_roxo = 50
        if ea_atual >= custo_roxo :
            print ("\nKYOSHIKI, MURASAKI ")
            print ("voce tirou 100 de vida da criatura")
            V_monstro -= 100
            ea_atual -= 50
        else : 
            print ("voce nao pode usar isto, te falta EA")
    elif ataque == "expansao" and "expansao" in habilidades :
        custo_expansao = 100
        if ea_atual >= custo_expansao :
            print ("RYOIKI TENKAI, MURYO KUSHO")
            print ("voce expande seu dominio e causa 150 de dano")
            V_monstro -= 150
            ea_atual -= 100
        else :
            print ("voce é incapaz de usar isto agora, recupere EA")
    elif ataque == "energia reversa" and "energia reversa" in habilidades :
        custo_energia_reversa = 25
        if ea_atual >= custo_energia_reversa :
            print ("voce se cura utilizando energia positiva")
            V_jogador += 35
            ea_atual -= 25
        else :
            print ("voce é incapaz de se curar no momento")
    else :
        print ("nao existe ataque assim, escreva corretamente o golpe que quer utilizar")
    if usou_azul and usou_vermelho :
        if "Pergaminho_azul" in mochila and "Pergaminho_vermelho" in mochila:
            print ("\no espaco tempo distorce por meio segundo, e brilha em roxo de novo...")
            time.sleep (1.5)
            print ("\nVoce comeca a falar: nice ropes polarized light crow and declaration between front and back")
            time.sleep (1.5)
            print ("\no mundo passa em camera lenta, e de repente brilha em roxo")
            time.sleep (1.5)
            print ("\nHollow Technique: Hollow purple")
            print ("Voce acerta um roxo, mas voce nao sabe como fez aquilo, porem, liberou o dobro de seu poder original")
            print ("\nVOCE PULVERIZA ATE O ULTIMO ATOMO DA CRIATURA")
            V_monstro -= 800
    if V_monstro > 0 :
        escolha_monstro = random.randint(1, 2)
        if escolha_monstro == 1 :
            print ("ela desfere um soco em voce, causando 10 de dano")
            V_jogador -= 10
            ea_monstro += 35
        elif escolha_monstro == 2:
            custo_garras = 50
            if ea_monstro >= custo_garras :
                print ("ela te ataca com garras e te perfura, causando 40 de dano")
                V_jogador -= 40
                ea_monstro -= 50
            else :
                print ("ela tenta te atacar, porem ela nao possui EA suficiente, ela apenas te empurra")
                V_jogador -= 5
        if ea_monstro > ea_maxmonstro :
            ea_monstro = ea_maxmonstro
if V_jogador <= 0 :
    print ("Voce morreu, foi rasgado ao meio pelas garras")
elif V_monstro <= 0 :
    if "roxo" in habilidades :
        print ("voce venceu, se tornando o mais honrado, porem, agora voce carrega o fardo de ser o mais forte ate a sua morte")
    elif "desmantelar" in habilidades :
        print ("voce venceu, se tornando o feiticeiro mais forte de toda a historia mundial")
    else :
        print ("voce venceu sendo um ser humano comum!, parabens!")
