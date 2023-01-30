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

No diretório contendos os itens, abra o prompt de comando digitando "cmd" na barra de navegação:
![image](https://user-images.githubusercontent.com/92338508/215296194-38fa5e4f-a1c2-48e3-86ca-be3c568b6401.png)

Digite o seguinte comando:

```shell
poetry install
```
Depois de algus segundos, a instalação deve estar concluída.

## Uso

### Como rodar o programa

Abra um prompt de comando da mesma forma citada em [Como Instalar](#como-instalar) e digite o seguinte comando:

```shell
poetry run python src/__init__.py
```

Após a execução do comando, a interface gráfica do programa deve aparecer na tela, indicando que está tudo pronto para o uso.

<img src="https://user-images.githubusercontent.com/92338508/215187159-bd145598-e1a4-497f-8cd5-ddf6baf4d19c.png" width="600" height="450">

### Formatação arquivos de entrada

É essencial que o usuário selecione arquivos de entrada formatados corretamente, abaixo estão alguns exemplos de boa formatação.

** IMAGENS COM OS EXEMPLOS **
