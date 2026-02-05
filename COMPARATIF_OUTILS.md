# Comparatif d'outils

## 📋 Tableau comparatif

| Outil           | Catégorie        | Avantages                                                               | Inconvénients                                       | Note /10 | Choix ? |
| --------------- | ---------------- | ----------------------------------------------------------------------- | --------------------------------------------------- | -------- | ------- |
| **Ruff**        | Linter           | Ultra rapide, règles modernes, remplace Flake8 + isort, facile à config | Moins exhaustif que Pylint sur l’analyse profonde   | 9/10     | ✅      |
| **Flake8**      | Linter           | Classique, stable, énorme écosystème de plugins                         | Plus lent, moins strict, dépend de plugins          | 7/10     | ❌      |
| **Pylint**      | Linter           | Analyse très complète, détecte code smells avancés                      | Lent, très verbeux, faux positifs fréquents         | 6/10     | ❌      |
| **Ruff format** | Formatter        | Ultra rapide, compatible Black, cohérent avec Ruff linter               | Peu personnalisable                                 | 9/10     | ✅      |
| **Black**       | Formatter        | Opinionated, standard de facto, stable                                  | Très peu configurable                               | 8/10     | ❌      |
| **autopep8**    | Formatter        | Simple, permissif, configurable                                         | Résultats moins cohérents, pas un vrai standard     | 6/10     | ❌      |
| **Mypy**        | Type Checker     | Référence du typage Python, très précis                                 | Plus lent, nécessite parfois beaucoup d’annotations | 8/10     | ❌      |
| **Pyright**     | Type Checker     | Très rapide, excellent support VS Code, peu de faux positifs            | Moins configurable que Mypy                         | 9/10     | ✅      |
| **Pyre**        | Type Checker     | Très rapide, conçu pour gros projets Meta                               | Installation lourde, moins adopté                   | 6/10     | ❌      |
| **pytest**      | Tests            | Ultra flexible, assertions simples, énorme écosystème de plugins        | Peut encourager trop de magie si mal utilisé        | 10/10    | ✅      |
| **unittest**    | Tests            | Standard library, robuste, sans dépendances                             | Verbeux, moins ergonomique que pytest               | 7/10     | ❌      |
| **Bandit**      | Security Scanner | Analyse statique Python, simple à intégrer                              | Ne couvre pas les dépendances                       | 7/10     | ❌      |
| **Safety**      | Security Scanner | Détecte vulnérabilités des dépendances                                  | Base gratuite limitée                               | 8/10     | ❌      |
| **Snyk**        | Security Scanner | Très complet, CI/CD friendly, analyse code + deps + containers          | Payant pour les features avancées                   | 9/10     | ❌      |
| **Trivy**       | Security Scanner | Excellent pour containers, rapide, open‑source                          | Moins ciblé Python                                  | 8/10     | ❌      |

## Choix d'outils

### 🎨 Linters Python

Ruff :

- Ultra rapide (écrit en Rust, 10–100× plus rapide que Flake8/Pylint).

- Tout‑en‑un : remplace Flake8 + isort + pyupgrade + une partie de Pylint.

- Facile à configurer (un seul outil, un seul fichier de config).

- Communauté massive et adoption explosive.

- Entièrement gratuit et open‑source.

👉 **Pourquoi pas Flake8 ?** Trop dépendant de plugins.

👉 **Pourquoi pas Pylint ?** Trop lent, trop verbeux, faux positifs.

### 🎨 Formatters Python

Ruff format :

- Très rapide (Rust encore).

- Compatible Black, mais plus rapide.

- Intégré au même outil que Ruff linter → cohérence totale.

- Gratuit, simple, sans configuration inutile.

👉 **Pourquoi pas Black ?** Très bon, mais plus lent et moins intégré.

👉 **Pourquoi pas autopep8 ?** Résultats moins cohérents, moins adopté.

### 🔒 Type Checkers

Pyright :

- Extrêmement rapide (analyse incrémentale).

- Intégré nativement dans VS Code → expérience fluide.

- Très peu de faux positifs.

- Gratuit et maintenu activement par Microsoft.

- Supporte très bien les projets modernes (Pydantic, dataclasses…).

👉 **Pourquoi pas Mypy ?** Plus lent, nécessite souvent plus d’annotations.

👉 **Pourquoi pas Pyre ?** Peu adopté, installation lourde.

### 🧪 Frameworks de Tests

pytest :

- Syntaxe simple et lisible (assertions naturelles).

- Énorme écosystème de plugins (coverage, fixtures, mocks…).

- Très flexible (tests unitaires, intégration, paramétrés…).

- Communauté gigantesque.

- Gratuit et stable.

👉 **Pourquoi pas unittest ?** Trop verbeux, moins ergonomique.

### 🔐 Security Scanners

Pour rester 100% gratuit, le meilleur combo est :

**✔ Bandit**

- Analyse statique du code Python.

- Détecte injections, mauvaises pratiques, secrets, etc.

- Léger, facile à intégrer en CI.

**✔ Safety**

- Analyse des dépendances vulnérables.

- Base gratuite suffisante pour un projet pédagogique.

👉 **Pourquoi pas Snyk ?** Très bon mais payant pour les features avancées.

👉 **Pourquoi pas Trivy ?** Excellent pour containers, moins ciblé Python.
