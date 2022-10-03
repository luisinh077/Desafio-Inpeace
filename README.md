# Instruções para usar o script

- Para funcionamento do script, necessário que tenha o python instalado e configurado em sua máquina
- Primeiro realize o git clone do código em uma pasta do seu desktop
- Abra o terminal dentro da pasta Desafio-Inpeace
- O comando para rodar o script é: python desafioInpeace.py "a.xml" "b.xml" colorPrimary A2A2A2
  - python -> Comando pra executar o arquivo python
  - desafioInpeace.py -> Nome do arquivo python a ser executado
  - "a.xml" -> Nome do arquivo xml de onde será copiado os valores, arquivo já se encontra na pasta
  - "b.xml" -> Nome do arquivo xml onde será colado as informações do arquivo a.xml e caso não exista, será criado o arquivo b.xml
  - colorPrimary -> Nome do atributo que será feita uma busca por todas tags color e verificar se existe um atributo name com o valor passado, caso não tenha não faz       nada
  -A2A2A2 -> Caso encontre o atributo, esse será o valor que será substituído
- Após rodar o script será substituído as informações do arquivo b.xml pelas informações do a.xml, caso não exista o b.xml será criado o arquivo b.xml. E também será feita a mudança do texto que contém o atributo informado na chamada do script
