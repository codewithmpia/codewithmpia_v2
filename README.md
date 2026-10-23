# codewithmpia v2

Réécriture complète de [codewithmpia.com](https://codewithmpia.com) avec [Asok](https://github.com/asok-framework/asok) — un framework Python sans dépendance runtime.

Le développement est public. Si quelque chose te semble cassé, mal fait, ou améliorable, ouvre une issue ou une PR.

---

## Ce que fait le site

**Authentification complète**
- Inscription, connexion, déconnexion
- Mot de passe oublié / réinitialisation
- Dashboard et profil utilisateur
- Certificats de complétion de cours

**Contenu**
- Cours avec chapitres et leçons (progression, accès premium)
- Blog bilingue FR/EN avec catégories
- Snippets et cheat sheets
- Annuaire d'outils dev
- Recherche fulltext (cours, articles, snippets, outils)

**Autres**
- Système de commentaires
- Newsletter avec confirmation
- Page contact
- Pages légales (CGU, confidentialité)
- Espace admin intégré (logs, sessions, corbeille, 2FA)

## Stack

- **Framework** : [Asok](https://github.com/asok-framework/asok) v0.8.0
- **Base de données** : Postgresql, SQLite
- **Langage** : Python 3.11+
- **Templates** : moteur de templates Asok (fichiers `.html` côté `src/pages` et `src/partials`)
- **Icons** : asok-lucide
- **CSS** : tailwindcss

## Structure

```
src/
  models/       # modèles de données (ORM Asok)
  pages/        # pages/routes
    auth/       
    articles/   
    courses/    
    snippets/
    cheat-sheets/
    tools/
    search/     
    newsletter/
    contact/
    about/, privacy/, terms/, support/
    404/, 429/, 500/
  partials/     # composants et layouts HTML
  components/   # composants réutilisables
  middlewares/  # middlewares custom
  locales/      # traductions FR/EN
  migrations/   # migrations SQL
wsgi.py         # point d'entrée WSGI
```

## Installation

```bash
git clone https://github.com/codewithmpia/codewithmpia_v2
cd codewithmpia_v2
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Crée un fichier `.env` à la racine (voir `.env.example` si dispo), puis :

```bash
asok make migration
asok migrate
asok createsuperuser
asok dev
```

## Contribuer

Le développement est ouvert. Pas de processus compliqué :

1. Fork le repo
2. Crée une branche (`git checkout -b fix/nom-du-truc`)
3. Commit et push
4. Ouvre une PR en décrivant ce que tu changes et pourquoi

Pour les bugs, ouvre une issue d'abord si c'est quelque chose de non trivial — ça évite de travailler dans le vide.

Les contributions bienvenues : corrections de bugs, amélioration des templates, accessibilité, performances, traductions.

## Licence

[MIT](LICENSE)
