# Criacao de um Banco de Dados Relacional

Projeto pratico com a criacao de um banco de dados relacional desenvolvido como atividade avaliativa do BootCamp Engenheiro de Dados da XPEducacao.

Visando tornar o projeto compativel com o conceito de **Bancos de Dados Evolutivos**, utiliza-se as bibliotecas `alembic` e `sqlalchemy` para o deploy automatico do modelo fisico do banco de dados.

Utiliza-se como SGBD padrao o Banco de Dados Postgresql.

## **Levantamento de Requisitos**
### Empresa de Seguros de Automoveis
- Cada cliente possui CPF, nome, sexo, endereço e telefones de contato (celular e fixo), mas podem vir a ter outros telefones no futuro. 
- Os carros possuem uma placa, marca, modelo, ano, chassi e cor. Cada carro tem determinado número de sinistros de acidentes associados a ele, sabendo que pode ter ocorrido múltiplos acidentes ou nenhum. 
- Já os sinistros devem ser identificados por um código único, data de ocorrência, hora de ocorrência, local de ocorrência (Endereço completo) e condutor, que pode ou não ser o titular da apólice e precisa ser devidamente registrado no sistema. Além disso, o sinistro possui um tipo de ocorrência (Colisão, Roubo ou Furto, Incêndio, Enchente, Retrovisor, dentre outros). 
- Um cliente ou pessoa pode ter várias apólices (mínimo uma) vigentes ou nenhuma, e cada apólice de seguro tem um identificador único e só pertence a um cliente e a somente um carro, mas pode ter vários condutores vinculados, e tem data de início e fim da vigência, valor total assegurado e valor franquia associados a ela.
- É importante saber que o carro pode ter várias apólices vinculadas a ele, mas apenas uma vigente.
- E sempre que houver um sinistro é preciso saber qual o carro envolvido, além do número da apólice, uma vez que este precisa ser assegurado por uma apólice. Mesmo que o atendimento seja para terceiros vai ser registrado no sinistro do carro vinculado à apólice da empresa em questão. 

## **Modelo Conceitual**
![modelo_logico](media/modelo_logico.jpeg)

## **Modelo Logico**
![modelo_conceitual](media/modelo_conceitual.jpeg)

## **Modelo Fisico**  
![modelo_fisico](media/modelo_fisico.png)

## Ambiente de Desenvolvimento

Requisitos necessários para a instalação do sistema:
- [Python 3.10.2](https://www.python.org/downloads/)
- [Postgresql 9.6.1](https://www.postgresql.org/download/linux/ubuntu/)  

Instale as dependências:

```bash
    pip install -r requirements.txt
```

## Banco de dados
O gerenciamento do banco de dados no projeto foi feito utilizando a biblioteca Python `SQLAlchemy` junto com a biblioteca de versionamento `Alembic`, ambas instaladas no passo anterior.

Crie o database `seguros` no seu banco de dados e configure a URI do seu banco de dados no arquivo `alembic.ini` como no exemplo abaixo:

> sqlalchemy.url=postgresql://usuario:senha@host/seguros

Após isso, na raiz do projeto, execute o comando para execução das _migrations_ do `alembic` que irão criar as tabelas:
> alembic upgrade head

Pronto. O sistema está instalado.

## Criação do _Virtual Enviroment_ (opcional)
O _virtual enviroment_ Python é uma forma de encapsular as bibliotecas e recursos da sua aplicação, separando-os das demais aplicações Python no servidor e servindo na organização. A criação do ambiente virtual é opcional mas altamente recomendada.

O primeiro passo é instalar os pacotes abaixo:
> pip install virtualenv virtualenvwrapper

Para que o `virtualenvwrapper` possa ser utilizado é necessário adicioná-lo como _source_. Para isso, o comando abaixo deve ser adicionado ao fim do seu arquivo `~/.bashrc`. Salve o arquivo e reinicie o terminal.

Após instalados, podemos criar o ambiente virtual com o comando:
> mkvirtualenv <nome_ambiente> --python=python3

Para testar a criação do ambiente utilize o comando:
> workon <nome_ambiente>

Deve ser mostrado o nome do ambiente entre parênteses no início de cada nova linha no terminal, sinalizando que o ambiente está ativo.

