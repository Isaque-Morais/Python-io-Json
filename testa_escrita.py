from pyexpat import model


arquivo_contato = open('C:/Users/ISAQU/OneDrive/Documentos/curso_alura/pythonio-projeto-inicial/dados/contatos-escrita.csv', encoding='latin_1', mode='a+')

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

for contatos in contatos:
    arquivo_contato.write(contatos)
    
arquivo_contato.flush()

arquivo_contato.seek(28)
arquivo_contato.write('12,Ana,ana@ana.com.br\n'.upper())
arquivo_contato.flush()
arquivo_contato.seek(0)


for linha in arquivo_contato:
    print(linha)