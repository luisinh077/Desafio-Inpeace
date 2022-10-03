import sys
import xml.etree.ElementTree as ET

# Carregando o arquivo de a.xml com o método parse()
file_A = ET.parse(sys.argv[1])
# Gravar o contéudo de a.xml no arquivo b.xml com o método write, caso não exista o arquivo b.xml, será criado o arquivo
file_A.write("b.xml")
# Carregando o arquivo de b.xml
file_B = ET.parse(sys.argv[2])
# Laço de repetição passando por todas as tags de nome color
for color in file_B.findall('color'):
    # Verifica se a tag color tem um atributo name com valor colorPrimary, encontrando modifica o valor
    if(color.attrib == {'name': sys.argv[3]}):
        color.text = '#' + sys.argv[4]
# Gravar a alteração no arquivo b.xml
file_B.write(sys.argv[2])