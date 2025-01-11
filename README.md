Si vous souhaitez utiliser un dossier spécifique pour vos fichiers statiques générés par Vue.js (comme le dossier `dist` qui contient le build de votre application Vue.js), voici les étapes pour configurer correctement les fichiers statiques dans Django, tout en ayant `STATIC_URL = 'static/'` :

### 1. **Configurer `STATIC_URL` et `STATICFILES_DIRS`**

Dans votre `settings.py`, vous avez déjà :

```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "dist",  # Le chemin vers votre dossier 'dist' généré par Vue.js
]
```

Cela signifie que les fichiers statiques générés par Vue.js dans le dossier `dist` seront accessibles par Django sous l'URL `/static/`. Cependant, vous devrez peut-être aussi ajuster la configuration des fichiers statiques pour vous assurer qu'ils sont bien collectés et servis en production.

### 2. **Vérifier la configuration des fichiers statiques en production**

En production, Django ne sert pas les fichiers statiques directement. Vous devez utiliser `collectstatic` pour rassembler tous les fichiers statiques dans un seul dossier (souvent appelé `STATIC_ROOT`), et vous pouvez utiliser un serveur comme **Nginx** ou **WhiteNoise** pour servir ces fichiers.

Ajoutez la configuration suivante à votre `settings.py` :

#### Définir `STATIC_ROOT`

```python
STATIC_ROOT = BASE_DIR / "staticfiles"  # Dossier où collectstatic rassemblera tous les fichiers statiques
```

Lorsque vous exécutez la commande `collectstatic`, Django copiera tous les fichiers statiques (y compris ceux dans `frontend/dist`) dans ce dossier `staticfiles`.

#### Exemple de commandes pour préparer les fichiers statiques pour la production

1. **Construire votre projet Vue.js** :

   Dans le dossier `frontend`, exécutez :

   ```bash
   npm run build
   ```

   Cela génère le dossier `dist` contenant tous les fichiers statiques (HTML, CSS, JS, etc.).

2. **Collecter les fichiers statiques** :

   Ensuite, exécutez la commande suivante dans votre projet Django pour collecter les fichiers statiques :

   ```bash
   python manage.py collectstatic
   ```

   Cette commande va déplacer tous les fichiers du dossier `frontend/dist` vers le dossier `staticfiles`.

### 3. **Servir les fichiers statiques avec WhiteNoise (optionnel)**

Si vous souhaitez que Django serve les fichiers statiques directement (sans serveur comme Nginx), vous pouvez utiliser **WhiteNoise**, qui permet de servir les fichiers statiques en production.

1. **Installez WhiteNoise** :

   ```bash
   pip install whitenoise
   ```

2. **Ajoutez-le dans `MIDDLEWARE`** :

   Modifiez votre `MIDDLEWARE` pour inclure `WhiteNoiseMiddleware` juste après `SecurityMiddleware` :

   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',  # Ajoutez cette ligne
       # autres middleware...
   ]
   ```

3. **Configurer le stockage des fichiers statiques** :

   Dans `settings.py`, ajoutez cette configuration pour compresser et gérer les fichiers statiques :

   ```python
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

### 4. **Gérer les fichiers statiques dans votre template**

Dans votre template `index.html` (qui est généré par Vue.js), assurez-vous d'utiliser les bonnes URL pour les fichiers statiques :

#### Exemple de `index.html` généré par Vue.js

Assurez-vous d'avoir une structure de base comme celle-ci dans le fichier `index.html` de Vue.js, que Django servira :

```html
<body>
  <div id="app"></div>
  
  <!-- Liens vers les fichiers JS et CSS générés par Vue.js -->
  <script src="{% static 'mangalib/js/main.js' %}"></script>
</body>
```

Si vous utilisez `WhiteNoise` ou un serveur comme **Nginx**, il est important que les fichiers statiques soient correctement référencés pour être servis sous l'URL `/static/`.

### 5. **Vérification en production**

Lorsque tout est configuré, vous pouvez vérifier que tout fonctionne correctement en exécutant les commandes suivantes dans un environnement de production :

1. **Collecter les fichiers statiques** :

   ```bash
   python manage.py collectstatic
   ```

2. **Démarrer le serveur Django** (en production, vous devriez utiliser un serveur comme `gunicorn` ou `uWSGI`, mais vous pouvez tester avec le serveur de développement de Django) :

   ```bash
   python manage.py runserver
   ```

3. **Vérifiez l'accès aux fichiers statiques** : Vous pouvez essayer d'accéder à un fichier statique généré par Vue.js via l'URL `/static/`.

---

### Conclusion

En résumé, vous avez correctement configuré `STATIC_URL` pour pointer vers `'static/'` et vous avez configuré `STATICFILES_DIRS` pour inclure les fichiers build de Vue.js dans `frontend/dist`. Vous devez ensuite utiliser `collectstatic` pour rassembler les fichiers dans `STATIC_ROOT` et vous assurer que les fichiers sont servis correctement, soit par Django (avec WhiteNoise), soit par un serveur comme Nginx en production.
