FROM node:20-alpine

WORKDIR /app

# Copie des fichiers de configuration
COPY frontend/package*.json ./

RUN npm install

# Copie de l'intégralité du dossier frontend
COPY frontend/ .

# Exposition du port frontend
EXPOSE 5173

# Lancement en mode dev
CMD ["npm", "run", "dev", "--", "--host"]