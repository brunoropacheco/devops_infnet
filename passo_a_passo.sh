cd "C:\Users\bruno\Transmissão no Google Drive\Meu Drive\Academico_Pesquisa\repos\devops_infnet\docker_bd"
docker build . -t brunoropacheco/bd_mysql_java:0.1
docker network create appvenda_nw
docker run --name bd_mysql_appvenda --network appvenda_nw -d -P brunoropacheco/bd_mysql_java:0.1

