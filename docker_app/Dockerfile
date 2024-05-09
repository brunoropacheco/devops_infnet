# Use uma imagem base que tenha a JVM (Java Virtual Machine) instalada
FROM eclipse-temurin:latest

# Copie o arquivo JAR para o contêiner
COPY app.jar /app/app.jar

#COPY app_lib /app/app_lib

COPY files /app/files

COPY src /app/src

# Defina o diretório de trabalho
WORKDIR /app

# Comando para executar o aplicativo quando o contêiner for iniciado
CMD ["java", "-jar", "app.jar"]

# Defina a variável de ambiente MYSQL_ROOT_PASSWORD
ENV MYSQL_ROOT_PASSWORD=Noki@500

# Defina a variável de ambiente MYSQL_ROOT_USR
ENV MYSQL_ROOT_USR=root

EXPOSE 8080