# Corretor de Simulados Einstein Floripa (SimuENEM, SimUFSC e Simulinho)

### Sumário

1. [Introdução](#introdução)
2. [Requerimentos](#requerimentos)
3. [Setup do programa](#setup-do-programa)  
  2.1. [Como baixar](#como-baixar)  
  2.2. [Como instalar](#como-instalar) 
4. [Uso](#uso)  
  3.1. [Como rodar o programa](#como-rodar-o-programa)   
  3.2. [Formatação arquivos de entrada](#Formatação-arquivos-de-entrada)

## Introdução

O algortimo aqui desenvolvido serve para facilitar e automatizar o processo de correção de simulados do EF (Enstein Floripa), ele recebe como input o **gabarito**, as **provas (com uma estrutura de nomes)** e uma lista com os **dados dos alunos**, tudo isso sendo arquivos ***.csv*** ou ***.xlsx***

## Requrimentos
Antes de começar a instalação, é necessário que os seguintes itens estejam instalados na sua máquina:  
**Lembrando que a instalaçao dos itens a seguir deve ser feita em ordem!**
1. `python 3.10`  
O download para Mac, Windows e Linux pode ser feito no site oficial do Python:
> https://www.python.org/downloads/
2. `python poetry`  
O link com as instruçoes para instalar o `poetry` estao abaixo:  
> https://python-poetry.org/docs/  

## Setup do programa

### Como baixar
O codido fonte é aberto para qualquer pessoa utilizar e pode ser encontrado no repositório:
> https://github.com/einsteinfloripa/corretor-simulados/

Depois de baixado, a pasta contendo o programa deve conter os seguintes arquivos:

![image](https://user-images.githubusercontent.com/92338508/215291665-292fb8dd-2323-45c0-a8a6-1ff35094961c.png)

### Como instalar

1. O usuário deve abrir um terminal de comandos, esse passo depende do sistema operacional utilizado, seguem as instruções de como fazer isso em Windows, Mac e linux.

Windows:

> https://tecnoblog.net/responde/7-maneiras-de-abrir-o-prompt-de-comando-no-windows-10-e-11/

Mac:  

> https://support.apple.com/pt-br/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac

Linux (Ubuntu):

> https://askubuntu.com/questions/183775/how-do-i-open-a-terminal

2. Utilizando o terminal, navege até o [diretório contendo os aquivos baixados](#como-baixar).
3. Digite o seguinte comando:

```shell
poetry install
```
Depois de algus segundos, a instalação deve estar concluída.

## Uso

### Como rodar o programa

1. Abra um terminal da mesma forma citada em [Como Instalar](#como-instalar), ou utilize um ja aberto anteriormente.
2. Utilizando o terminal, navege até o [diretório contendo os aquivos baixados](#como-baixar).
3. Digite o seguinte comando:

```shell
poetry run python src/__init__.py
```

Após a execução do comando, a interface gráfica do programa deve aparecer na tela, indicando que está tudo pronto para o uso.

<img src="https://user-images.githubusercontent.com/92338508/215187159-bd145598-e1a4-497f-8cd5-ddf6baf4d19c.png" width="600" height="450">

### Formatação arquivos de entrada

É essencial que o usuário selecione arquivos de entrada formatados corretamente, abaixo estão alguns exemplos de boa formatação.

** IMAGENS COM OS EXEMPLOS **
