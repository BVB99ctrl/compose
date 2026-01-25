const express = require('express');
const app = express();

// On récupère les variables injectées par Docker via docker/backend.env
const port = process.env.BACKEND_PORT || 3000;
const dbHost = process.env.DB_HOST; // Sera "database"

app.get('/', (req, res) => {
  res.send(`Backend connecté à la DB sur l'hôte : ${dbHost}`);
});

app.listen(port, () => {
  console.log(`Serveur lancé sur le port ${port}`);
});