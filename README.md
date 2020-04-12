# Unidade Client
Assistente virtual por voz. Esse projeto é uma prova de conceito e será usado como um cliente que executa tarefas diversas e se comunica com um servidor a fim de ser integrado com IoT e smarthomes.

## Instalação

**Importante:** O projeto foi feito inicialmente no Windows 10, mas há planos de migração para um container.

Abra um terminal e clone o projeto:

`git clone https://github.com/FioriBazarello/Unidade.git`

Ative o ambiente virtual:

`source .\unidade\Scripts\activate.bat` ou `. .\unidade\Scripts\activate.bat`

Instale as dependências:

`python -m pip install -r requirements.txt`

Caso aconteça algum problema com a instalação do PyAudio, provavelmente você precisa instalar os binários da biblioteca para Windows. Não se preocupe, é fácil:

* Descubra a sua versão do Python e se é 32 ou 64 bits rodando `python` no terminal. Toda a informação necessária vai aparecer com esse comando;
* Baixe o arquivo `whl` correspondente a sua versão do Python [nesta página](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio). Se for, por exemplo, `3.7.3` e `64 bit (AMD64)` segundo o passo acima, você vai baixar o `PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl`;
* Vá para o diretório onde você baixou os binários pelo terminal e instale usando o comando `pip install <nome do arquivo baixado>`. O do exemplo acima, por exemplo, seria `pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl`;
* Tente instalar as dependências novamente.

Inicie o arquivo de configuração para gerar mensagens padrão:

`python config.py`

Agora é só rodar o programa:

`python main.py`

## Uso
O sistema ainda é uma pequena prova de conceito, as funções iniciais são de pesquisa na Wikipedia e busca de previsão do tempo.
Caso tenha ideias que ache interessante, mande uma mensagem. Pull Requests com correções serão muito apreciados! :)
