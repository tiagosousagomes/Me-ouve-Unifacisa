# Integrantes do Grupo:

# Jessica Vitória Luiz Batista
# Renata Cardoso Mantovani
# Fábio José Dantas Filho
# Thayse Fernanda Silva de Barros
# Evelyn Julia da Silva
# Tiago Sousa Gomes

# comandos importados:
from classes import *
from time import sleep

# Banco de Dados:
conexao = abrirBancoDados('localhost', 'root', '331046', 'ouvidoria1')

print("\n" + "📣 Olá, seja bem-vindo à ouvidoria Me Ouve, Unifacisa! 📣" + "\n")
print("◆ Você faz parte de qual esfera do nosso sistema?" + "\n")
print("[ 1 ] Estudante")
print("[ 2 ] Docente")
print("[ 3 ] Colaborador")

setor = int(input("\n" + "▶ Insira aqui sua opção: "))
nome = cadastroUsuarios(conexao,setor)

if 0 < setor < 4:
    print("\n" + acesso.center(55, " "))

    # MENU:
    escolha = 333
    while escolha != 8:

        print("\n" + loading.center(55, " ") + "\n")
        sleep(2.5)

        print("           ┏━━━━━━━━━━━━━┓")
        print("                 MENU     ")
        print("           ┗━━━━━━━━━━━━━┛" + "\n")
        print("[ 1 ] Listar Manifestações")
        print("[ 2 ] Listar Manifestações por Categoria")
        print("[ 3 ] Cadastrar Manifestações")
        print("[ 4 ] Exibir Quantidade de Manifestações")
        print("[ 5 ] Consultar Manifestações por Código")
        print("[ 6 ] Alterar Manifestações")
        print("[ 7 ] Deletar Manifestações")
        print("[ 8 ] Sair da Ouvidoria" + "\n")

        escolha = int(input("▶ Escolha a opção que deseja acessar: "))

        # LISTAR MANIFESTAÇÕES:
        if escolha == 1:
            listarOcorrencias(conexao)
            print("\n" + redirect.center(55, " "))

        # LISTAR MANIFESTAÇÕES POR CATEGORIA:
        elif escolha == 2:
            listarPorCategoria(conexao)
            print("\n" + redirect.center(55, " "))

        # CADASTRAR MANIFESTAÇÕES:
        elif escolha == 3:
            cadastrarOcorrencias(conexao, nome)
            print("\n" + redirect.center(55, " "))

        # EXIBIR QUANTIDADE DE MANIFESTAÇÕES:
        elif escolha == 4:
            contarOcorrencias(conexao)
            print("\n" + redirect.center(55, " "))

        # CONSULTAR MANIFESTAÇÕES POR CÓDIGO:
        elif escolha == 5:
            consultarPorCodigo(conexao)
            print("\n" + redirect.center(55, " "))

        # ALTERAR MANIFESTAÇÕES
        elif escolha == 6:
            alterarManifestacao(conexao)
            print("\n" + redirect.center(55, " "))

        # DELETAR MANIFESTAÇÕES
        elif escolha == 7:
            deletarManifestacoes(conexao)
            print("\n" + redirect.center(55, " "))

        # CONDIÇÃO DO WHILE PARA SAIR DO SISTEMA:
        elif escolha == 8:
            print("\n" + "Agradecemos por ter utilizado o nosso sistema da Ouvidoria, "
                         "a opinião dos nossos associados é muito importante para nós!")
            print("\n" + loading.center(55, " ") + "\n")

        # CASO O NÚMERO INSERIDO NÃO FOR UMA OPÇÃO DISPONIBILIZADA NO MENU:
        else:
            print("\n" + error.center(55, " "))
            print("\n" + redirect.center(55, " "))

encerrarBancoDados(conexao)
