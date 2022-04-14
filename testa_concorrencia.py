contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

with open('C:/Users/ISAQU/OneDrive/Documentos/curso_alura/pythonio-projeto-inicial/dados/nao-existe.csv', encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open('C:/Users/ISAQU/OneDrive/Documentos/curso_alura/pythonio-projeto-inicial/dados/contatos-escrita.csv', encoding='latin_1', mode='a') as arquivo2: 
    arquivo2.write(contato_andreza)

arquivo2.write('Nova linha')