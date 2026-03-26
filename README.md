# Base de Connaissance Insurtech & ClaimsTech

Espace de veille technologique et d'intelligence concurrentielle sur les solutions logicielles pour l'assurance — gestion des sinistres, automatisation documentaire, BPM, IA et spécialistes de niche.

---

## Structure du projet

```
Insurance_Startups/
├── Fiches_Solutions/         # Base de connaissance — fiches structurées par solution
├── session_veille/           # Zone tampon — fichiers de veille bruts en cours de traitement
│   └── archive/              # Fichiers de veille traités et archivés
├── Inputs/                   # Fichiers d'entrée bruts à traiter
├── index_solutions.md        # Index central de toutes les solutions documentées
├── tracking_actions.md       # Journal des actions de l'agent
└── agent.md                  # Instructions système de l'agent IA
```

---

## Périmètre couvert

La base couvre les solutions insurtech classées en plusieurs catégories :

| Catégorie | Exemples |
|-----------|---------|
| Gestion des sinistres (ClaimsTech) | Shift Technology, Bdeo, Verisk, CCC ONE... |
| Fraude & Vérification | Clearspeed, Photocert, Spotr.ai, Emotion Logic... |
| Data, Analytics & IA transverse | CLARA Analytics, Akur8, Sixfold, Cytora... |
| IDP / Hyperautomation | Rossum, Hyperscience, Nanonets, Indico Data... |
| Automatisation documentaire & BPM | Newgen Software, Paperbox, Dylogy, Solveva... |
| Niche / Spécialistes divers | Peak3, Continuity, Otonomi, Pace, Miss Moneypenny... |
| Plateformes core insurance | Guidewire, Duck Creek, Socotra, Majesco... |

**Total : 192 solutions documentées** (mars 2026)

---

## Format des fiches

Chaque fiche dans `Fiches_Solutions/` suit un format standardisé :

- **Identité** : éditeur, fondateurs, année, siège, effectifs, levées de fonds
- **Description** : proposition de valeur, problème adressé
- **Produits & Fonctionnalités** : tableau des modules avec usage et résultats clés
- **Technologie** : stack, architecture, certifications
- **Chiffres clés** : métriques business et techniques
- **Clients** : références clients publiques
- **Histoire & Dates clés** : jalons importants
- **Dirigeants** : tableau des profils clés
- **Perspectives** : axes de croissance
- **Concurrents** : tableau comparatif
- **Réputation** : note /10 et analyse
- **Tags** : catégorisation multi-axes (#domaine, #acteurs, #technologies, #géographie)

**Convention de nommage des fichiers** : `Nom_Editeur_-_Nom_Solution.md`

---

## Utilisation

### Trouver une solution

Consultez [`index_solutions.md`](index_solutions.md) — tableau complet de toutes les solutions classées par éditeur avec lien direct vers la fiche.

### Ajouter une nouvelle veille

1. Créer un fichier dans `session_veille/` avec le nommage `YYYY-MM-DD_HHmm_Sujet.md`
2. L'agent de consolidation transformera la veille brute en fiche structurée
3. La fiche est créée dans `Fiches_Solutions/`, l'index mis à jour, le fichier archivé

### Recherche par tag

Les fiches sont taguées selon une taxonomie structurée. Exemples de recherche :

```bash
# Toutes les solutions IA générative
grep -rl "#ia-générative" Fiches_Solutions/

# Toutes les solutions pour la fraude
grep -rl "#fraude" Fiches_Solutions/

# Solutions basées en France
grep -rl "#france" Fiches_Solutions/
```

---

## Workflow de l'agent

L'agent IA opère en deux rôles complémentaires (voir [`agent.md`](agent.md)) :

```
[Veille brute] → session_veille/ → [Agent Consolidation] → Fiches_Solutions/
                                          ↓                        ↓
                                  session_veille/archive/   index_solutions.md
```

1. **Scout** : collecte l'information brute depuis le web, URLs fournies ou demandes utilisateur
2. **Gardener** : transforme la veille brute en fiches structurées et maintient l'index

Toutes les actions sont tracées dans [`tracking_actions.md`](tracking_actions.md).

---

## Dernière mise à jour

**2026-03-25** — 192 solutions documentées
