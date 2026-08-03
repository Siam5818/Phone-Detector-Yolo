# Phone Detector

Système de détection de téléphone portable en temps réel basé sur YOLO, avec envoi automatique d'une alerte email lors d'une détection.

## Installation (développement local)

Prérequis : Python 3.13, Git

\`\`\`powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
\`\`\`

## Structure du projet

- \`app/camera\` — capture du flux vidéo
- \`app/detection\` — détection du téléphone via YOLO
- \`app/email\` — module de notification SMTP
- \`app/storage\` — historique local des détections
- \`app/config\` — configuration et paramètres
- \`app/utils\` — utilitaires partagés
- \`tests/\` — tests unitaires
- \`docs/\` — documentation du projet