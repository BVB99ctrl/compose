// On récupère l'URL du backend via les variables d'environnement 
// (Note : selon ton outil de build comme Vite ou Webpack, la syntaxe peut varier)
const backendUrl = process.env.BACKEND_URL || 'backend'; 
const backendPort = process.env.BACKEND_PORT || '3000';

async function checkBackend() {
    try {
        // On essaie de contacter le backend
        const response = await fetch(`http://${backendUrl}:${backendPort}/`);
        const data = await response.text();
        document.getElementById('status').innerText = "Réponse du backend : " + data;
    } catch (error) {
        document.getElementById('status').innerText = "Erreur : Impossible de joindre le backend";
        console.error(error);
    }
}

checkBackend();