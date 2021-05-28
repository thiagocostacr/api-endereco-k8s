# Flask API - Endereco

# Objetivo
Olá, esse projeto tem o intuíto de criar microsserviço em Flask para ser
utilizado como laboratório de docker e k8s. Futuramente agregarei mais serviços
e utilizarei o padrão de modelagem DDD.

O código apresentado nessa microsserviço aplicação não tem como objetivo demonstrar práticas de
padrões de projeto, clean clode e/ou solid.

O microsserviço desse projeto está com o CRUD completo de um domínio cliente por meio
dos métodos POST, GET, PUT e DELETE. Resolvi utilizar o PUT ao invés do PATCH para simplificar
a implementação.

# Importante
- Esse microsserviço está associado a API de Cliente que você pode encontrar no meu repositório: https://github.com/thiagocostacr/api-cliente-k8s

# Pré Requisito
- Nessa API, assim como na api de Cliente, o banco de dados MySQL é pré requieito
- Caso queira fazer o laboratório de containers é necessário ter o Docker e o Kubernetes instalado previamente. Esse projeto foi desenvolvimento em um ambiente com **Minikube**

# Estrutura de Diretórios e Arquivos
- Dentro dos diretórios **k8s** e **docker** os respectivos **Dockefile**, **docker-compose** e **YAML's** estão os arquivos prontos para montar imagens e fazer deploy no **Kubernetes**.
- Atenção para ajustar as variáveis de ambiente que estão nos **YAML's** do **ConfigMap** e **Secrets** os os valores do seu ambiente local

# Container Registry
- A imagem desses projeto está disponível no meu DockerHub: https://hub.docker.com/repository/docker/thiagocostacr/endereco
