# 🧩 CI/CD — Concepts, enjeux, outils

## 🚀 Qu'est-ce que la CI (Continuous Integration) ?

La CI (Intégration Continue) est une pratique DevOps qui consiste à intégrer automatiquement et fréquemment les modifications de code dans une branche commune.
Chaque intégration déclenche :

- une compilation automatique

- des tests automatisés (unitaires, intégration…)

- une vérification de la qualité du code

**Objectif** : détecter les conflits et erreurs le plus tôt possible.

## 🛠️ Quels problèmes la CI résout-elle ?

- Conflits de fusion entre développeurs travaillant en parallèle

- “Merge day” douloureux (gros lots de code difficiles à intégrer)

- Bugs détectés trop tard

- Environnements différents entre développeurs

- Manque de visibilité sur la qualité du code

## 🔑 Principes clés de la CI

- Intégrations fréquentes (plusieurs fois par jour)

- Automatisation complète : build + tests

- Pipeline reproductible

- Feedback rapide pour les développeurs

- Un tronc commun stable

## 🧰 Exemples d’outils de CI

| Outil     | Description                             |
| --------- | --------------------------------------- |
| Jenkins   | Serveur CI/CD open source très flexible |
| GitLab CI | CI/CD intégré à GitLab                  |
| CircleCI  | Plateforme CI/CD cloud très utilisée    |

## 📦 Qu'est-ce que le CD (Continuous Delivery / Continuous Deployment) ?

Le CD correspond à l’automatisation des étapes après la CI : tests avancés, packaging, déploiement.

Il existe deux variantes :

- Continuous Delivery (Distribution Continue)
  Le code est automatiquement testé et préparé pour la production.

- Le déploiement final nécessite une validation humaine.

- Continuous Deployment (Déploiement Continu)
  Le code est déployé automatiquement en production, sans intervention humaine.

- Chaque commit validé part en production.

## ⚖️ Différence entre Continuous Delivery et Continuous Deployment

| Critère                   | Continuous Delivery | Continuous Deployment            |
| ------------------------- | ------------------- | -------------------------------- |
| Déploiement en production | Manuel              | Automatique                      |
| Niveau d’automatisation   | Élevé               | Total                            |
| Risque                    | Plus faible         | Plus élevé si tests insuffisants |
| Vitesse                   | Rapide              | Très rapide                      |

## 📉 Risques & 📈 Bénéfices du CD

**Bénéfices**

- Déploiements plus rapides

- Moins d’erreurs humaines

- Feedback utilisateur accéléré

- Pipeline reproductible et fiable

- Amélioration continue du produit

**Risques**

- Dépendance forte aux tests automatisés

- Risque de déployer un bug en production (surtout en Continuous Deployment)

- Investissement initial important (tests, pipelines, monitoring)

## 🔗 Pourquoi CI/CD est important ?

**🧪 Impact sur la qualité du code**

- Détection précoce des bugs

- Tests automatisés systématiques

- Code base toujours stable

- Réduction des régressions

**⚡ Impact sur la vitesse de développement**

- Automatisation des tâches répétitives

- Déploiements plus rapides

- Feedback immédiat

- Moins de temps perdu sur les merges complexes

**🤝 Impact sur la collaboration en équipe**

- Un tronc commun partagé et stable

- Moins de conflits entre développeurs

- Transparence sur l’état du code

- Alignement Dev + Ops (culture DevOps)

## 🧭 Conclusion

La CI/CD est aujourd’hui indispensable pour les équipes modernes : elle améliore la qualité, accélère le développement et renforce la collaboration. Elle permet de livrer plus vite, plus souvent, et avec plus de confiance.

# 🧩 Maitriser uv

## 🚀 Qu’est-ce que uv ?

uv est un outil ultra‑rapide pour gérer les environnements Python, installer des dépendances et exécuter des projets.
Il remplace plusieurs outils traditionnels (pip, venv, poetry, pipenv) en offrant :

- un gestionnaire de dépendances

- un résolveur très rapide

- un runner Python

- un build backend compatible pyproject.toml

uv est écrit en Rust et vise la performance, la simplicité et la compatibilité avec l’écosystème Python.

## 🔍 En quoi uv est différent de pip / poetry / pipenv ?

| Fonction                   | pip              | pipenv  | poetry         | uv              |
| -------------------------- | ---------------- | ------- | -------------- | --------------- |
| Installation de paquets    | ✔️               | ✔️      | ✔️             | ✔️ Ultra‑rapide |
| Résolution des dépendances | ❌               | Moyenne | Bonne          | ⚡ Très rapide  |
| Gestion d’environnements   | ❌               | ✔️      | ✔️             | ✔️ intégrée     |
| Fichier de config          | requirements.txt | Pipfile | pyproject.toml | pyproject.toml  |
| Build backend              | ❌               | ❌      | ✔️             | ✔️              |
| Performance                | lente            | moyenne | correcte       | ⚡⚡ extrême    |

**En résumé**

- pip : installe mais ne résout pas les dépendances

- pipenv : lent, plus maintenu activement

- poetry : complet mais plus lourd

- uv : rapide, moderne, compatible pyproject.toml, unifie tout

## 🌟 Avantages de uv

**⚡ Performance**

- Résolution des dépendances extrêmement rapide (Rust + algorithmes optimisés)

- Installation quasi instantanée

**🧩 Unification**

- Un seul outil pour : installer, gérer les environnements, exécuter Python, builder

**📦 Compatibilité**

- Fonctionne avec pyproject.toml

- Compatible avec les standards PEP

**🔒 Reproductibilité**

- Lockfile clair et stable

- Résolution déterministe

**🛠️ Simplicité**

- Commandes cohérentes

- Pas besoin de virtualenv ou pip séparément

## 📁 uv et pyproject.toml

uv utilise pyproject.toml comme source unique de configuration, comme Poetry.

**🧱 Structure du fichier**

Exemple minimal :

```toml
[project]
name = "mon-projet"
version = "0.1.0"
dependencies = [
    "numpy",
    "pandas",
]

[build-system]
requires = ["uv"]
build-backend = "uv.build"
```

**📌 Gestion des dépendances (sections)**

uv lit les dépendances dans :

```toml
[project]
dependencies = [...]
```

Pour les dépendances de développement :

```toml
[project.optional-dependencies]
dev = ["pytest", "ruff"]
```

uv permet ensuite :

```bash
uv add numpy
uv add --dev pytest
uv remove numpy
```

**🏗️ Build backend avec uv**

- uv peut agir comme backend de build

- Il expose un module uv.build compatible PEP 517

- Il permet de construire des wheels et sdists très rapidement

Exemple dans pyproject.toml :

```toml
[build-system]
requires = ["uv"]
build-backend = "uv.build"
```

uv gère :

- la construction du package

- la résolution des dépendances de build

- la génération des artefacts

## 🤖 Utiliser uv dans GitHub Actions

**📥 Installation dans un workflow**

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v1
```

**⚡ Cache des dépendances**

uv gère automatiquement un cache basé sur :

- le lockfile

- la version Python

- la plateforme

Dans GitHub Actions :

```yaml
- name: Cache uv
  uses: actions/cache@v3
  with:
    path: ~/.cache/uv
    key: ${{ runner.os }}-uv-${{ hashFiles('uv.lock') }}
```

**▶️ Exécution de commandes**

Installer les dépendances :

```yaml
- name: Install dependencies
  run: uv sync
```

Exécuter les tests :

```yaml
- name: Run tests
  run: uv run pytest
```

uv remplace donc :

- pip install -r requirements.txt

- poetry install

- python -m venv

- pipenv install

## 🧭 Conclusion

uv est un outil moderne qui :

- unifie l’écosystème Python

- remplace pip + venv + poetry

- accélère drastiquement la résolution et l’installation

- s’intègre parfaitement avec pyproject.toml

- propose un backend de build rapide

- simplifie les workflows CI/CD (GitHub Actions)

C’est aujourd’hui l’un des outils les plus prometteurs pour la gestion de projets Python.

# 🧩 Comprendre Semantic Release

## 🎯 Qu’est‑ce que le versionnage sémantique (SemVer) ?

Le versionnage sémantique est une convention standardisée pour numéroter les versions d’un logiciel selon le format : MAJOR.MINOR.PATCH

**🔹 MAJOR**

Incrémenté lorsque :

- des changements incompatibles sont introduits,

- l’API publique casse la rétro‑compatibilité.

**🔹 MINOR**

Incrémenté lorsque :

- de nouvelles fonctionnalités compatibles sont ajoutées,

- l’API publique s’enrichit sans casser l’existant.

**🔹 PATCH**

Incrémenté lorsque :

- des corrections de bugs sont apportées,

- aucune nouvelle fonctionnalité n’est ajoutée,

- aucune rupture n’est introduite.

**📌 Résumé rapide**

| Niveau    | Quand bumper ?           |
| --------- | ------------------------ |
| **MAJOR** | Rupture de compatibilité |
| **MINOR** | Nouvelle fonctionnalité  |
| **PATCH** | Correction de bug        |

## 📝 Qu’est‑ce que les Conventional Commits ?

Les Conventional Commits définissent un format standardisé pour les messages Git afin d’automatiser le versionnage et la génération de changelog.

**🔹 Format général**

```code
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**🔹 Types de commits les plus courants**

| Type         | Signification                           | Impact SemVer |
| ------------ | --------------------------------------- | ------------- |
| **feat**     | Nouvelle fonctionnalité                 | MINOR         |
| **fix**      | Correction de bug                       | PATCH         |
| **docs**     | Documentation                           | Aucun         |
| **style**    | Formatage, lint                         | Aucun         |
| **refactor** | Refactoring sans changement fonctionnel | Aucun         |
| **perf**     | Amélioration de performance             | PATCH         |
| **test**     | Ajout/modification de tests             | Aucun         |
| **chore**    | Maintenance, CI/CD                      | Aucun         |

**🔥 Cas particulier : BREAKING CHANGE**

Deux façons de déclarer une rupture :

1. Dans le footer :

```code
BREAKING CHANGE: la fonction X a été supprimée
```

2. Dans le type :

```code
feat!: suppression de l’ancienne API
```

## 🤖 Comment fonctionne python‑semantic‑release ?

python‑semantic‑release automatise :

- le bump de version selon les commits,

- la génération du changelog,

- la création des tags Git,

- la publication des releases GitHub,

- la publication sur PyPI (optionnel).

**🔧 Configuration dans pyproject.toml**

Exemple minimal :

```toml
[tool.semantic_release]
version_variable = "package/__init__.py:__version__"
branch = "main"
upload_to_pypi = false
upload_to_release = true
changelog_file = "CHANGELOG.md"
```

**🔹 Détection automatique du bump**

| Commit                       | Bump  |
| ---------------------------- | ----- |
| **fix:**                     | PATCH |
| **feat:**                    | MINOR |
| **BREAKING CHANGE** ou **!** | MAJOR |

**📄 Génération du CHANGELOG**

python‑semantic‑release lit l’historique Git et génère automatiquement un changelog structuré :

- regroupé par version,

-classé par type (feat, fix…),

- avec liens vers les commits.

Exemple :

```code
## v1.4.0
### Feat
- ajout du module d’export (#42)

### Fix
- correction du bug d’auth (#39)
```

**🚀 Création des releases GitHub**

Si activé :

- un tag Git est créé (v1.4.0),

- une release GitHub est générée,

- le changelog est automatiquement injecté dans la release.

## 📌 Synthèse finale

| Concept                     | Rôle                                    | Lien avec les autres                                             |
| --------------------------- | --------------------------------------- | ---------------------------------------------------------------- |
| **SemVer**                  | Définit comment numéroter les versions  | python‑semantic‑release applique SemVer automatiquement          |
| **Conventional Commits**    | Définit comment écrire les messages Git | python‑semantic‑release lit ces messages pour déterminer le bump |
| **python‑semantic‑release** | Automatise version, changelog, release  | S’appuie sur Conventional Commits + SemVer                       |
