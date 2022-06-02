arquivo = open('dados/contatos-escrita.csv', mode="a+")

print(type(arquivo.buffer))


texto_em_bytes = bytes('Esse é um texto em bytes', 'UTF-8')
#print(texto_em_bytes)


contato = bytes('15,Verônia,veronica@veronica.com.br\n', 'UTF-8')
arquivo.buffer.write(contato)

arquivo.close()