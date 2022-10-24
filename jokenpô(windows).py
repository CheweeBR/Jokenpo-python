kik = False
while not kik:
    c = False
    vit = 0
    der = 0
    emp = 0
    z=0
    qtd=0
    import os
    import time
    import random
    from datetime import datetime
    import webbrowser
    os.system('mode 105,14') or None
    print('\n')
    print('                                         \033[1mVamos jogar \033[1;43mJokenpô!\033[m ')  
    print('')
    print('                                           ■——————————————■')
    print("                                           |  \033[1mMelhor de\033[m   | ")
    print('                                           ■——————————————■')
    print('                                           | [\033[1;35m3\033[m] \033[1mPartidas\033[m |')
    print('                                           | [\033[1;35m5\033[m] \033[1mPartidas\033[m |')
    print('                                           | [\033[1;35m7\033[m] \033[1mpartidas\033[m |')
    print('                                           ■——————————————■')
    print('')
    qtdp=int(input('                                        \033[1mQuantidade de partidas: \033[m'))
    while not c:
        i = 0
        fd1=datetime.now()
        hora=fd1.hour
        os.system('mode 105,14') or None
        os.system('cls') or None
        print()
        print('''                                          \033[1mVamos jogar \033[1;43mJokenpô!\033[m                               \033[7;1;45mPlacar:\033[m
                                                                                              |\033[1;32mV:{}\033[m|
                                                                                              |\033[1;31mD:{}\033[m|
                                                                                              |\033[1;37mE:{}\033[m|
                                            \033[1;4mTABELA DE OPÇÃO\033[m                                   □---□'''.format(vit,der,emp))
        print('''                                            ■—————————————■   	
                                            | [1] \033[1;35mPedra\033[m.  |
                                            | [2] \033[1;37mPapel\033[m.  |
                                            | [3] \033[1;36mTesoura\033[m.|
                                            ■—————————————■
       ''')
        dfd=4
        r=input('                                           \033[1mEscolha um número:\033[m ')
        os.system('cls') or None
        print('\n \n \n \n \n ')
        print('                                                \033[43m J \033[m \033[43m o \033[m')
        time.sleep(0.6)
        print('                                              \033[43m K \033[m \033[43m e \033[m \033[43m n \033[m')
        time.sleep(0.5)
        print('                                                \033[43m P \033[m \033[43m ô \033[m')
        time.sleep(0.5)
        os.system('cls') or None
        p= 'Pedra'
        pa= 'Papel'
        t= 'Tesoura'
        list=[p,pa,t]
        a=random.choice(list)
        if r == '1':
            if hora < 18:
                os.system('cls') or None
                print()
                print()
                print('      Sua escolha foi:\033[1;35mpedra\033[m.')
                print()
                if a == p:
                    print('                                                \033[1;37mEmpatamos!\033[m\n \n                                       Pois eu também escolhi \033[1;35mpedra\033[m!')
                    print()
                    print('                                          \033[1;4;37mBom dia invejosinho(a).\033[m')
                    emp += 1 
                    z=3      
                elif a == pa:
                    print('                                                 \033[1;31mPerdeu!\033[m\n \n                                   Pois escolhi \033[1;37mpapel\033[m, voce é uma falha!')
                    print()
                    print('                                       \033[1;4;31mBom dia derrotado(a) hehe...\033[m')
                    der += 1
                    z=1
                    qtd += 1
                elif a == t:
                    print('                                                   \033[1;32mVenceu!\033[m\n \n                                         Escolhi \033[1;36mtesoura\033[m, trapaceiro.')
                    print()
                    print('                                                 \033[1;4;32mPessimo dia.\033[m')
                    vit += 1
                    z=2
                    qtd += 1
            else:
                               
                os.system('cls') or None
                print()
                print()
                print('      Sua escolha foi:\033[1;35mpedra\033[m.')
                print()
                if a == p:
                    print('                                                 \033[1;37mEmpatamos!\033[m\n \n                                        Pois eu também escolhi \033[1;35mpedra\033[m!')
                    print()
                    print('                                          \033[1;4;37mBoa noite invejosinho(a).\033[m')
                    emp += 1
                    z=3
                elif a == pa:
                    print('                                                 \033[1;31mPerdeu!\033[m\n \n                                   Pois escolhi \033[1;37mpapel\033[m, voce é uma falha!')
                    print()
                    print('                                       \033[1;4;31mBoa noite derrotado(a) hehe...\033[m')
                    der += 1
                    z=1
                    qtd += 1
                elif a == t:
                    print('                                                 \033[1;32mVenceu!\033[m\n \n                                       Escolhi \033[1;36mtesoura\033[m, trapaceiro.')
                    print()
                    print('                                              \033[1;4;32mPessima noite.\033[m')    
                    vit += 1
                    z=2
                    qtd += 1
        elif r == '2': 
               if hora < 18:
                   os.system('cls') or None
                   print()
                   print()
                   print('      Sua escolha foi:\033[1;37mpapel\033[m.')
                   print()
                   if a == p:              
                     vit += 1
                     z=2
                     qtd += 1
                     print('                                                 \033[1;32mVenceu!\033[m\n \n                                  Eu escolhi \033[1;35mpedra\033[m, sorte não habilidade.')
                     print()
                     print('                                               \033[1;4;32mPessimo dia.\033[m')
                   elif a == pa:
                     z=3
                     emp += 1
                     print('                                               \033[1;37mEmpatamos!\033[m\n \n                                 Pois eu também escolhi \033[1;37mpapel\033[m(invejoso)!')
                     print()
                     print('                                         \033[1;4;37mBom dia invejosinho(a).\033[m')
                   elif a == t: 
                     z=1
                     der += 1
                     qtd += 1
                     print('                                                 \033[1;31mPerdeu!\033[m\n \n                                          Pois te \033[1;36mtesourei\033[m haha!')
                     print()
                     print('                                       \033[1;4;31mBom dia derrotado(a) hehe...\033[m')
               else:
                   os.system('cls') or None
                   print()
                   print()
                   print('      Sua escolha foi:\033[1;37mpapel\033[m.')
                   print()
                   if a == p:
                       z=3
                       emp += 1
                       print('                                                \033[1;37mEmpatamos!\033[m\n \n                                  Pois eu também escolhi \033[1;37mpapel\033[m(invejoso)!')
                       print()
                       print('                                         \033[1;4;37mBoa noite invejosinho(a).\033[m')
                   elif a == pa:               
                       der += 1
                       z=1
                       qtd += 1
                       print('                                                 \033[1;31mPerdeu!\033[m\n \n                                          Pois te \033[1;36mtesourei\033[m haha!')
                       print()
                       print('                                       \033[1;4;31mBoa noite derrotado(a) hehe...\033[m')
                   elif a == t:
                       z=2
                       vit += 1
                       qtd += 1
                       print('                                                 \033[1;32mVenceu!\033[m\n \n                                  Eu escolhi \033[1;35mpedra\033[m, sorte não habilidade.')
                       print()
                       print('                                              \033[1;4;32mPessima noite.\033[m')         
        elif r == '3':
            if hora < 18:
                os.system('cls') or None
                print()
                print()
                print('      Sua escolha foi:\033[1;36mtesoura\033[m.')
                print()
                if a == p:
                    der += 1
                    z=1
                    qtd += 1
                    print('                                                 \033[1;31mPerdeu!\033[m\n \n                                  Pois eu dei uma \033[1;35mpedrada\033[m em sua \033[1;36mtesoura\033[m!')
                    print()
                    print('                                       \033[1;4;31mBom dia derrotado(a) hehe...\033[m')
                elif a == pa:
                    vit += 1
                    z=2
                    qtd += 1
                    print('                                                 \033[1;32mVenceu!\033[m\n \n                                    Fiz \033[1;37mpapel\033[m, sorte de principiante...')
                    print()
                    print('                                               \033[1;4;32mPessimo dia.\033[m')
                elif a == t:
                    z=3
                    emp += 1
                    print('                                                \033[1;37mEmpatamos.\033[m\n \n                                 Eu também fiz \033[1;36mtesoura\033[m, inveja mata sabia?')
                    print()
                    print('                                         \033[1;4;37mBom dia invejosinho(a).\033[m')
            else:
                os.system('cls') or None
                print()
                print()
                print('      Sua escolha foi:\033[1;36mtesoura\033[m.')
                print()
                if a == p:
                    z=3
                    emp += 1
                    print('                                                \033[1;37mEmpatamos.\033[m\n \n                                 Eu também fiz \033[1;36mtesoura\033[m, inveja mata sabia?')
                    print()
                    print('                                         \033[1;4;37mBoa noite invejosinho(a).\033[m')
                elif a == pa:
                    z=1
                    der += 1
                    qtd += 1
                    print('                                                 \033[1;31mPerdeu!\033[m\n \n                                  Pois eu dei uma \033[1;35mpedrada\033[m em sua \033[1;36mtesoura\033[m!')
                    print()
                    print('                                       \033[1;4;31mBoa noite derrotado(a) hehe...\033[m')
                elif a == t:
                    vit += 1
                    z=2
                    qtd += 1
                    print('                                                 \033[1;32mVenceu!\033[m\n \n                                    Fiz \033[1;37mpapel\033[m, sorte de principiante...')
                    print()
                    print('                                              \033[1;4;32mPessima noite.\033[m')
        elif r == '49':
            os.system('cls') or None
            print()
            print()
            print()
            print()
            print()
            print()
            print('                              \033[1;4mEsse é o valor de 7 X 7, não uma das opções...\033[m')
            print()
            print()

            print()
        elif r == '22':
            print()
            pato=str(input('O que o pato disse para pata? ')).upper()
            if pato ==  'VEM QUA' or pato == 'QUACK' or pato == 'QUAK' or pato ==  'VEM QUACK':
                print('Resposta correta! receba 100 pontos de vitoria!')
                vit+=100
                qtd+=1
            else:
                print('Resposta errada ;-; receba 100 pontos de derrota!')
                der+=100
                qtd+=1 
            print('\n \n \n \n \n')
        elif r == '666':
            g1 = 999999
            while g1 != 1:
                print('                                   \033[1;33;41mSATANÁS TE GUIARÁ FILHA DA PUTA!!!')
        elif r == '3301':  
            print('A não...\nNão somos da cicada...\nVocê está engana...')
            print()
            i=str(input('...'))
            os.system('cls') or None        	
            print('Apagando o jogo...')
            for hhh in range(1,100+1):
                time.sleep(0.05)
                print('{}...'.format(hhh)) 
            c = 'N'
            os.system('cls') or None  
            c = True
        elif r == '69':
            os.system('cls') or None
            for g3 in range(1,9999999999):
                print('\033[45m   ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)   ')
        elif r == '51':
            print('\n \n \n \n \n')
            print('                                   A vida está tão difícil assim amigão?')
            webbrowser.open_new('https://www.youtube.com/watch?v=HeMEMkgnbng&ab_channel=SandraCristinaPeripato%28RecantoCaipira%29')

        else:
            print()
            print()
            print()
            print()
            print() 
            print('                                         \033[4;37mReeleia a aba de opções!\033[m\n                                        \033[4;37mPois a desejada não existe.\033[m')
            #print(len('Reeleia a aba de opções, pois a desejada não existe'))
            z=3
        time.sleep(1)
        print()
        c1=str(input('                                         Tentar novamente (\033[1;32menter\033[m) ')).strip().capitalize()
        if qtd != qtdp:
            if z == 3:
                os.system('cls') or None
                for v in range(1):
                    os.system('cls')
                    print('\n \n \n \n \n ')
                    print('■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')       
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                    time.sleep(0.035)
                    c = False
            elif z == 2:
                os.system('cls') or None
                for v in range(1):
                    os.system('cls')
                    print('\n \n \n \n \n ')
                    print('\033[32;1m■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')       
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                    time.sleep(0.035)
                print('\033[m')
                c = False
            elif z == 1:
                os.system('cls') or None
                for v in range(1):
                    os.system('cls')
                    print('\n \n \n \n \n ')
                    print('\033[31;1m■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')       
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□')
                    time.sleep(0.035)
                    os.system('cls') or None
                    print('\n \n \n \n \n ')
                    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                    time.sleep(0.035)
                print('\033[m')
                c = False
        else:
            c = True
            os.system('cls') or None
    print()
    print()
    s1 = vit
    s2 = der
    s3 = emp
    if s1 > s2:    
        print('                                            \033[1;32mVocê é o campeão!\033[m')   
    elif s2 == s1:
        print('                                              \033[37;1mVocê empatou!\033[m')
    elif s2 > s1:
        print('                                           \033[31;1mVocê foi derrotado!\033[m')
    print()
    print('''                                                 \033[7;1;45mPlacar:\033[m
                                                  |\033[1;32mV:{}\033[m|
                                                  |\033[1;31mD:{}\033[m|
                                                  |\033[1;37mE:{}\033[m|
                                                  □---□'''.format(vit,der,emp))  
    print()  
    p0001=str(input('                                      \033[1mDeseja reiniciar o jogo? (\033[32ms\033[m/\033[31mn\033[m): '))
    if p0001 == 's' or p0001 == 'S':
        kik = False
    else:
        os.system('cls') or None
        print('\n \n \n \n \n ')
        print('                                       \033[1;33mMuito obrigado pela atenção!\033[m')
        p2=input()
        kik = True