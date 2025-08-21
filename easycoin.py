def titulo_personalizado():
    print('\033[1;31m')  # Vermelho escuro (bordas)
    print('╔════════════════════════════════════════╗')
    print('║                                        ║')
    print('\033[1;37m', end='')  # Branco negrito (EasyCoin)
    frase = '🪙  𝐸𝒶𝓈𝓎𝒞𝑜𝒾𝓃  🪙'
    print(frase.center(40))
    print('\033[1;33m        O seu Cofrinho Digital          ')
    print('\033[1;31m', end='')  # Volta para vermelho escuro (bordas)
    print('║                                        ║')
    print('╚════════════════════════════════════════╝')
    print('\033[0m')  # Volta para a cor padrão do terminal