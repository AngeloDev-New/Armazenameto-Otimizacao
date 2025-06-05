FROM mysql:8.0

# Variáveis de ambiente para inicializar o banco
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=pass
ENV MYSQL_DATABASE=mecanica

# Expõe a porta interna padrão do MySQL
EXPOSE 3306

# Copia o script de inicialização (opcional, se existir)
COPY myconfig.cnf /etc/mysql/conf.d/myconfig.cnf
COPY db/*.sql /docker-entrypoint-initdb.d/
