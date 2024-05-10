# todo
Estiam api todo

# todo-api-estiam

## Description
Ce projet est un serveur API basé sur FastAPI, conçu pour gérer les tâches (todos) et l'authentification des utilisateurs. Il utilise Firebase pour la gestion de l'authentification des utilisateurs et de la base de données.

## Configuration requise
- Python 3.x
- Node.js (si vous utilisez des dépendances npm)

## Installation
1. Clonez ce dépôt sur votre machine locale :

2. Installez les dépendances Python en exécutant la commande suivante dans votre terminal :


3. Si vous utilisez des dépendances npm, installez-les en exécutant la commande suivante :


## Configuration Firebase
1. Créez un projet Firebase sur [Firebase Console](https://console.firebase.google.com/).
2. Téléchargez le fichier de configuration `firebase-adminsdk.json` et placez-le dans le répertoire `config` de votre projet.
3. Définissez les variables d'environnement `FIREBASE_SERVICE_ACCOUNT_KEY` et `FIREBASE_CONFIG` avec le contenu du fichier de configuration et les informations d'authentification Firebase respectivement.

## Utilisation
1. Pour démarrer le serveur API, exécutez la commande suivante dans votre terminal :


Assurez-vous d'être dans le répertoire racine de votre projet où se trouve le fichier `main.py`.

2. Accédez à l'URL spécifiée dans votre navigateur ou via un outil comme Postman pour tester les différentes routes de l'API. Par exemple, si vous exécutez localement, l'URL par défaut pourrait être `http://127.0.0.1:8000/`.

## Documentation
La documentation de l'API est disponible à l'URL racine du serveur.

## Routes
- `/auth` : Routes pour l'authentification des utilisateurs.
- `/todos` : Routes pour la gestion des tâches (todos).

## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :
1. Fork du dépôt
2. Créez une nouvelle branche (`git checkout -b feature/feature-name`)
3. Faites vos modifications et ajoutez-les (`git add .`)
4. Committez vos modifications (`git commit -m "Add feature"`)
5. Push vers la branche (`git push origin feature/feature-name`)
6. Créez une demande d'extraction

## Auteurs
[Liste des auteurs/contributeurs]

## Licence
Ce projet est sous licence [MIT Licence](LICENSE).
