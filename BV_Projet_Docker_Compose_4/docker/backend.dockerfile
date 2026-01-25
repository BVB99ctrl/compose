# Image de base légère
FROM node:20-alpine

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# On copie d'abord les fichiers de dépendances (optimisation du cache)
# Note : On part de la racine du projet car le context est "."
COPY backend/package*.json ./

# Installation des dépendances
RUN npm install

# Copie du reste du code source
COPY backend/ .

# Exposition du port (sera remplacé dynamiquement par les variables d'env si l'app le gère)
# Mais on indique le port par défaut pour la doc interne
EXPOSE 3000

# Commande de lancement
CMD ["npm", "start"]