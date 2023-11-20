# Utilisez une image de base appropriée pour votre application Django
FROM python:3.8

# Ajoutez ces lignes pour installer les dépendances système nécessaires pour mysqlclient
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installez les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Ajoutez le reste de votre configuration Docker ici
# ...
