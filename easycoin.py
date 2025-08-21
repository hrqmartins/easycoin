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
    
def mostrar_opcoes():
    print('\033[1;37m1.\033[0m Adicionar Moedas')
    print('\033[1;37m2.\033[0m Remover Moedas')
    print('\033[1;37m3.\033[0m Ver Cofrinho')
    print('\033[1;37m4.\033[0m Sair')
    
def voltar_menu():
    input('Pressione ENTER para voltar ao menu')
    limpar_tela()
    titulo_personalizado()
    mostrar_opcoes()