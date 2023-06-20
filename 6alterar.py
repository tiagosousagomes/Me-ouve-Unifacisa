elif escolha == 6:

if len(ocorrencias) == 0:
    print("\n" + "◆ Ainda não existem manifestações que possam ser alteradas!")

else:
    codigo = input("\n" + "▶ Digite o protocolo da manifestação que deseja alterar: ")
    consultaAlt = "select * from ocorrencias where protocolo = " + codigo
    ocorrencia = listarBancoDados(conexao, consultaAlt)

    if len(ocorrencia) == 1:
        print("\n" + "⌕ A manifestação selecionada foi:")
        for items in ocorrencia:
            print("\n" + "Categoria:", items[1], "\n" + "➥ Título:", items[2],
                  "\n" + "➥ Descrição:", items[3], "\n" + "➥ Autor:", items[4])

        print("\n" + "◆ A seguir, você poderá modifica-la:")
        newTitle = input("\n" + "▶ Reescreva o título da manifestação: ")
        newDescription = input("▶ Adicione a nova descrição dessa manifestação: ")

        sqlAtualizar = "update ocorrencias set titulo = %s, descricao = %s  where protocolo = " + codigo
        valores = (newTitle, newDescription)
        atualizarBancoDados(conexao, sqlAtualizar, valores)

        print("\n" + "✓  A manifestação foi atualizada com sucesso!")

    else:
        print("\n" + error.center(55, " "))

    print("\n" + redirect.center(55, " ")