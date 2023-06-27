# FUNÇÕES IMPORTADAS:
from operacoesbd import *
from time import sleep


# VARIAVÉIS DE MENSAGENS AUTOMÁTICAS:
loading = "↻ Carregando..."
acesso = "Acesso liberado! 🐍"
redirect = "Iremos te redirecionar para o menu principal."
error = "⚠︎ A opção inserida é inválida! ⚠︎"


# 0 - CATEGORIAS (SOMENTE POR QUESTÃO DE ORGANIZAÇÃO)
def categoriasOcorrencias():
    print("\n" + "◆ Categorias de Manifestações:" + "\n")
    print("[ 1 ] Reclamações")
    print("[ 2 ] Sugestões")
    print("[ 3 ] Elogios" + "\n")


# 1 - LISTAR TUDO NA TABELA (MENU)
def listarOcorrencias(conexao):
    consultaOcorrencias = "select * from ocorrencias"
    ocorrencias = listarBancoDados(conexao, consultaOcorrencias)

    if len(ocorrencias) == 0:
        print("\n" + "◆ Ainda não existem manifestações a serem exibidas!")

    else:
        print("\n" + "◆ Manifestações cadastradas até o momento:")
        for items in ocorrencias:
            sleep(2.5)
            print("\n" + "Protocolo:", items[0], "-", "Categoria:", items[1], "\n" + "➥ Título:", items[2],
                  "\n" + "➥ Descrição:", items[3], "\n" + "➥ Autor:", items[4])


        print("\n" + "◆ Fim da listagem.")

# 1.1 - LISTAR EM RESUMO
def listarResumido(conexao):
    consultaOcorrencias = "select protocolo, titulo, autor from ocorrencias"
    ocorrencias = listarBancoDados(conexao, consultaOcorrencias)

    if len(ocorrencias) == 0:
        print("\n" + "◆ Ainda não existem manifestações a serem exibidas!")

    else:
        print("\n" + "◆ Manifestações cadastradas até o momento:")
        for items in ocorrencias:
            sleep(1.75)
            print("\n" + "Protocolo:", items[0], "\n" + "➥ Título:", items[1], "\n" + "➥ Autor:", items[2])
            sleep(1.75)

        print("\n" + "◆ Fim da listagem.")


# 2 - LISTAR POR CATEGORIA (MENU)
def listarPorCategoria(conexao):
    categoriasOcorrencias()
    categoria = int(input("▶ Digite a categoria de manifestação que você deseja listar: "))

    if 0 < categoria < 4:
        ocorrenciasTipo = listarFromColumn(conexao, "tipo", str(categoria))

        if len(ocorrenciasTipo) == 0:
            print("\n" + "◆ Ainda não existem manifestações a serem exibidas nessa categoria!")

        else:
            print("\n" + "◆ Manifestações cadastradas na categoria até o momento:")
            for items in ocorrenciasTipo:
                sleep(1.75)
                print("\n" + "Protocolo:", items[0], "\n" + "➥ Título:", items[2], "\n" + "➥ Descrição:",
                      items[3], "\n" +
                      "➥ Autor:", items[4])
                sleep(1.75)

            print("\n" + "◆ Fim da listagem.")

    else:
        print("\n" + error.center(55, " "))

# 2.1 - LISTAR UMA COLUNA ESPECIFICA DA TABELA:
def listarFromColumn(conexao, coluna, condicao):
    consultaQuantidade = "select * from ocorrencias where  " + coluna + " = " + condicao
    resultado = listarBancoDados(conexao,consultaQuantidade)
    return resultado


# 3 - CADASTRAR NA TABELA "OCORRENCIAS" (MENU)
def cadastrarOcorrencias(conexao, nome):
    categoriasOcorrencias()
    type = int(input("▶ Digite pelo código em qual categoria você deseja cadastrar sua manifestação: "))

    if 0 < type < 4:
        print("\n" + "◆ Opções de cadastro:" + "\n")
        print("[ 1 ] Sob seu nome")
        print("[ 2 ] Em Anonimato" + "\n")

        userCadastro = int(input("▶ Digite pelo código a forma na qual você deseja cadastrar sua manifestação: "))

        if userCadastro == 2:
            nome = "Anônimo"

        title = input("\n" + "▶ Escreva um título que resuma sua manifestação: ")
        description = input("▶ Por favor, descreva sua manifestação: ")

        sqlInsercao = 'insert into ocorrencias (tipo, titulo , descricao , autor) values (%s,%s,%s,%s)'
        valores = [str(type), title, description, nome]

        protocolo = insertNoBancoDados(conexao, sqlInsercao, valores)
        print("\n" + "✔  Sua manifestação foi cadastrada com sucesso! O número do seu protocolo é:",protocolo)

    else:
        print("\n" + error.center(55, " "))

# 3.1 - CADASTRAR NA TABELA DA CATEGORIA
def cadastrarOcorrenciasEmCategoria(conexao, categoria, id, title, description, name):

    if categoria == 1:

        tabela = "reclamacoes"

    elif categoria == 2:

        tabela = "sugestoes"

    else:
        tabela = "elogios"

    sqlInsercao = "insert into " + tabela + " (protocolo, titulo, descricao, autor) values (%s,%s,%s,%s)"
    valores = [id, title, description, name]

    insertNoBancoDados(conexao, sqlInsercao, valores)

# 3.2 - CADASTRAR NA TABELA DE USUARIOS
def cadastroUsuarios(conexao, setor):
    print("\n" + loading.center(55, " ") + "\n")
    sleep(2.5)

    if 0 < setor < 4:

        nome = input("▶ Digite o seu nome completo: ")
        email = input("▶ Nos informe seu e-mail institucional: ")
        nomeSplit = nome.split()

        if setor == 1:
            print("\n" + "◆ Olá, " + nomeSplit[0] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")
            curso = input("▶ Digite o curso você faz na universidade: ")
            matricula = input("▶ Por fim, digite o seu número de matrícula: ")

            sqlInsertAssociados = "insert into estudantes (matricula,nome,curso,email_inst) values (%s,%s,%s,%s)"
            valores = [matricula, nome, curso, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

        elif setor == 2:
            print("\n" + "◆ Olá, Prof. " + nomeSplit[1] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")

            curso = input("▶ Digite para qual curso você leciona: ")
            disciplina = input("▶ Digite quais disciplinas você leciona em " + curso + ": ")
            id = input("▶ Por fim, digite seu número de identificação: ")

            sqlInsertAssociados = "insert into docentes (id,nome,curso,disciplinas,email_inst) values (%s,%s,%s,%s,%s)"
            valores = [id, nome, curso, disciplina, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

        elif setor == 3:
            print("\n" + "◆ Olá, " + nomeSplit[0] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")
            departamento = input("▶ Digite o departamento da universidade no qual você trabalha: ")
            id = input("▶ Por fim, digite o seu número de identificação: ")

            sqlInsertAssociados = "insert into colaboradores (id,nome,depart,email_inst) values (%s,%s,%s,%s)"
            valores = [id, nome, departamento, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

    else:
        print(error + "\n" +
              "De antemão, deve ser alertado que essa Ouvidoria é um sistema direcionado somente à "
              "associados do centro universitário." + "\n" + "Se esse não for o seu caso, o acesso não será permitido.")

    return nome


# 4 - CONTAGEM DE OCORRENCIAS (MENU)
def contarOcorrencias(conexao):
    quantidadeTotal = selectCount(conexao)
    quantidadeRec = selectCountColumn(conexao, "tipo", "1")
    quantidadeSug = selectCountColumn(conexao, "tipo", "2")
    quantidadeElo = selectCountColumn(conexao, "tipo", "3")

    print("\n" + "◆ No total, existem", quantidadeTotal, "manifestações cadastradas. Dentre essas:")
    print("➥", quantidadeRec, "são reclamações")
    print("➥", quantidadeSug, "são sugestões")
    print("➥", quantidadeElo, "são elogios")

# 4.1 - CÓDIGO DA CONSULTA DE CONTAGEM
def selectCount(conexao):
    consultaQuantidade = "select count(*) from ocorrencias"
    resultado = listarBancoDados(conexao, consultaQuantidade)
    quantidade = resultado[0][0]
    return quantidade

# 4.2 - CÓDIGO DA CONSULTA DE CONTAGEM DE UMA COLUNA ESPECIFICA
def selectCountColumn(conexao, coluna, condicao):
    consultaQuantidade = "select count(*) from ocorrencias where  " + coluna + " = " + condicao
    resultado = listarBancoDados(conexao,consultaQuantidade)
    quantidade = resultado[0][0]
    return quantidade


# 5 - PESQUISAR POR CÓDIGO (MENU)
def consultarPorCodigo(conexao):
    listarResumido(conexao)
    codigo = int(input("\n" + "▶ Digite o protocolo da manifestação que deseja encontrar: "))
    consultaOcorrrencia = selectCountColumn(conexao, "protocolo", str(codigo))

    if consultaOcorrrencia == 0:
        print("\n" + error.center(55, " "))

    else:
        pesquisarOcorrencia = listarFromColumn(conexao, "protocolo", str(codigo))
        print("\n" + "⌕ A manifestação pesquisada foi:")
        for items in pesquisarOcorrencia:
            print("\n" + "Categoria:", items[1], "\n" + "➥ Título:", items[2],
                  "\n" + "➥ Descrição:", items[3], "\n" + "➥ Autor:", items[4])


# 6 - ALTERAR (MENU)
def alterarManifestacao(conexao):
    listarResumido(conexao)
    codigo = input("\n" + "▶ Digite o protocolo da manifestação que deseja alterar: ")
    consultaOcorrencia = selectCountColumn(conexao, "protocolo", codigo)

    if consultaOcorrencia == 0:
        print("\n" + error.center(55, " "))

    else:
        pesquisarOcorrencia = listarFromColumn(conexao, "protocolo", codigo)
        print("\n" + "⌕ A manifestação selecionada foi:")

        for items in pesquisarOcorrencia:
            sleep(1.75)
            print("\n" + "Categoria:", items[1], "\n" + "➥ Título:", items[2],
                  "\n" + "➥ Descrição:", items[3], "\n" + "➥ Autor:", items[4])
            sleep(1.75)

        print("\n" + "◆ A seguir, você poderá modifica-la ⤵")
        newTitle = input("\n" + "▶ Reescreva o título da manifestação: ")
        newDescription = input("▶ Adicione a nova descrição dessa manifestação: ")

        sqlAtualizar = "update ocorrencias set titulo = %s, descricao = %s  where protocolo = " + codigo
        valores = [newTitle, newDescription]
        atualizarBancoDados(conexao, sqlAtualizar, valores)

        print("\n" + "✓  A manifestação foi atualizada com sucesso!")


# 7 - DELETAR (MENU)
def deletarManifestacoes(conexao):
    quantidade = selectCount(conexao)

    if quantidade == 0:
        print("\n" + "◆ Ainda não existem manifestações que possam ser deletadas!")

    else:
        print("\n" + "◆ Opções disponiveis:" + "\n")
        print("[ 1 ] Remover Todas as Manifestações")
        print("[ 2 ] Remover Todas as Manifestações de uma Categoria")
        print("[ 3 ] Remover Manifestações Específicas")

        remove = int(input("\n" + "▶ Digite a opção que deseja realizar: "))

        if remove == 1:
            removerTodasManifestacoes(conexao)

        elif remove == 2:
            removerPorCategoria(conexao)

        elif remove == 3:
            removerPorProtocolo(conexao)

        else:
            print("\n"  + error.center(55, " "))

# 7.1 - [ 1 ] REMOVER TODAS AS MANIFESTAÇÕES:
def removerTodasManifestacoes(conexao):
    print("\n" + "Essa ação é irreversivel! Tem certeza que deseja remover todas as manifestações da ouvidoria?")
    print("\n" + "[ 1 ] Sim" + "\n" + "[ 2 ] Não" + "\n")
    escolha = int(input("▶ Digite o código da sua escolha: "))

    if escolha == 1:
        sqlDelet = "delete from ocorrencias"
        delAllBancoDados(conexao, sqlDelet)
        print("\n" + "✔  Todas as manifestações foram removidas com sucesso!")

    elif escolha == 2:
        print("\n" + "◆ O processo de remoção foi cancelado.")

    else:
        print("\n" + error.center(55, " "))

# 7.2 - [ 2 ] REMOVER TODAS AS MANIFESTAÇÕES DE UMA CATEGORIA ESPECIFICA:
def removerPorCategoria(conexao):
    categoriasOcorrencias()
    codigo = int(input("▶ Digite o código da categoria que você deseja realizar a remoção: "))

    if 0 < codigo < 4:
        quantidadeCategoria = selectCountColumn(conexao, "tipo", str(codigo))

        if quantidadeCategoria == 0:
            print("\n" + "◆ Nessa categoria, ainda não existem manifestações que possam ser deletadas!")

        else:
            print("\n" + "Essa ação é irreversivel! Tem certeza que deseja remover todas as manifestações dessa categoria?")
            print("\n" + "[ 1 ] Sim" + "\n" + "[ 2 ] Não" + "\n")
            escolha = int(input("▶ Digite o código da sua escolha: "))

            if escolha == 1:
                deletFromColumn(conexao, "tipo", str(codigo))
                print("\n" + "✔  Todas as manifestações da categoria selecionada foram removidas com sucesso!")

            elif escolha == 2:
                print("\n" + "◆ O processo de remoção foi cancelado.")

            else:
                print("\n" + error.center(55, " "))

    else:
        print("\n" + error.center(55, " "))

# 7.3 - [ 3 ] REMOVER MANIFESTAÇÃO POR PROTOCOLO:
def removerPorProtocolo(conexao):
    listarResumido(conexao)
    codigo = input("\n" + "▶ Digite o protocolo da manifestação que você deseja deletar: ")
    quantidadeCategoria = selectCountColumn(conexao, "protocolo", codigo)

    if quantidadeCategoria == 0:
        print("\n" + error.center(55, " "))
    else:
        print("\n" + "Essa ação é irreversivel! Tem certeza que deseja remover essa manifestação?")
        print("\n" + "[ 1 ] Sim" + "\n" + "[ 2 ] Não" + "\n")
        escolha = int(input("▶ Digite o código da sua escolha: "))

        if escolha == 1:
            deletFromColumn(conexao, "protocolo", codigo)
            print("\n" + "✔  A manifestação de protocolo", codigo, "foi removida com sucesso!")

        elif escolha == 2:
            print("\n" + "◆ O processo de remoção foi cancelado.")

        else:
            print("\n" + error.center(55, " "))

# 7.4 - DELETAR SOB A CONDIÇÃO DE UMA COLUNA ESPECIFICA
def deletFromColumn(conexao, coluna, condicao):
    sqlDelet = "delete from ocorrencias where %s = %s"
    dados = (coluna, condicao)
    excluirBancoDados(conexao, sqlDelet, dados)
