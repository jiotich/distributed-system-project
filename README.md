# distributed-system-project

# Criando o venv

    Na pasta principal onde estão as pastas do cliente e servidor, 
    execute o seguinte comando para criar o ambiente virtual: make venv
    
    Em seguida, execute o seguinte comando para instalar 
    as dependências no ambiente virtual: make install

# Server

    Dentro da pasta Server, abra um terminal nesta pasta, e execute o 
    seguinte comando para ativar o ambiente virtual de python: 
    
    source ../imago_env/bin/activate
    
    Em seguinda execute o comando: make server
    Agora o server estará rodando, para fecha-lo basta pressionar ctrl+c

# Server API

    Dentro da pasta log_server, abra um terminal nesta pasta, e execute o 
    seguinte comando para ativar o ambiente virtual de python: 
    
    source ../imago_env/bin/activate
    
    Em seguinda execute o comando: make api
    Agora o server de logs estará rodando, para fecha-lo basta pressionar ctrl+c

# Client

    Dentro da pasta Client, abra um terminal nesta pasta, e execute o 
    seguinte comando para ativar o ambiente virtual de python: 
    
    source ../imago_env/bin/activate
    
    Em seguinda execute o comando: make client
