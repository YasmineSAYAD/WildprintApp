# Comparatif d'outils

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
