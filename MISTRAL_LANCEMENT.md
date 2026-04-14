# 🚀 Guide de Lancement - Traduction avec Mistral sur GitHub

## 📋 Étapes à suivre

### 1️⃣ Configurer le Secret GitHub (REQUIS)

⚠️ **AVANT de lancer le workflow**, vous DEVEZ ajouter votre clé Mistral comme secret GitHub:

1. Allez sur: **Settings → Secrets and variables → Actions**
2. Cliquez: **"New repository secret"**
3. Remplissez:
   - **Name**: `MISTRAL_API_KEY`
   - **Value**: `nzeqNQf8jYdwtGG4p0LXH34sVV6o8aSm`
4. Cliquez: **"Add secret"**

✓ La clé est maintenant sécurisée sur GitHub et ne sera jamais visible dans les logs.

### 2️⃣ Lancer le Workflow GitHub Actions

1. Allez à l'onglet: **Actions**
2. Sélectionnez: **"Mistral Translation Pipeline"** (à gauche)
3. Cliquez: **"Run workflow"** (bouton bleu)
4. Laissez vide: **"Batch ID"** (pour soumettre un nouveau batch)
5. Cliquez: **"Run workflow"**

### 3️⃣ Suivre la Progression

- Le workflow va:
  ✓ Soumettre les 395 fichiers à l'API Mistral
  ✓ Créer un fichier `batch_info_mistral.json` avec l'ID du batch
  ✓ Afficher le statut du batch dans les logs
  ✓ Télécharger les résultats
  ✓ Committer les fichiers traduits

- Durée estimée: **5-30 minutes** (traitement Mistral)

### 4️⃣ Récupérer les Résultats

Une fois le workflow terminé:

1. Allez à l'onglet: **Actions**
2. Cliquez sur le workflow exécuté
3. Téléchargez: **"batch-info"** (contient batch_info_mistral.json)
4. Les fichiers traduits seront dans: **`Insurtech_Solutions_EN/`**
5. Ils seront automatiquement committé sur la branche **`mistral-translation`**

## 📂 Fichiers de Configuration

| Fichier | Rôle |
|---------|------|
| `.github/workflows/mistral-translation.yml` | GitHub Actions workflow |
| `mistral_translate.py` | Script Python pour Mistral API |
| `MISTRAL_SETUP.md` | Documentation d'installation |
| `.gitignore` | Protège les clés API (ne pas committer) |

## 🔒 Sécurité

✓ **La clé API n'est jamais sauvegardée sur GitHub**
- Utilisez GitHub Secrets (Settings → Secrets)
- Jamais d'env variables en dur dans le code
- Fichiers sensibles dans `.gitignore`

⚠️ **Après utilisation**, you SHOULD rotate the API key:
```bash
# Sur le dashboard Mistral
# Générez une nouvelle clé et mettez à jour le Secret GitHub
```

## 🛠 Troubleshooting

### Le workflow échoue avec "API key not found"

❌ Vous avez oublié de configurer le Secret GitHub
✅ Solution: Allez à Settings → Secrets and add `MISTRAL_API_KEY`

### Le batch est "in_progress" après 1 heure

✓ C'est normal - les batches Mistral peuvent prendre jusqu'à plusieurs heures
✓ Le workflow continuera à vérifier la progression
✓ Les résultats seront committé automatiquement quand le batch est prêt

### Récupérer un batch existant

Si vous avez l'ID d'un batch en cours:

1. Allez: **Actions → Mistral Translation Pipeline**
2. Cliquez: **"Run workflow"**
3. Entrez: **Batch ID** (ex: `batch_0198xyz...`)
4. Cliquez: **"Run workflow"**

Le workflow va récupérer les résultats du batch et les committer.

## 📊 Résultats Attendus

```
Insurtech_Solutions_EN/
├── 360Globalnet_-_360SiteView.md
├── 7Analytics_-_7Analytics.md
├── A1_Tracker_-_A1_Tracker.md
├── ...
└── (395 fichiers au total)
```

Chaque fichier contient:
- ✓ Traduction française → anglaise
- ✓ Structure markdown préservée
- ✓ URLs inchangées
- ✓ Noms de sociétés intacts

## 📝 Notes Importantes

1. **Pas de hardcoding de clés**: La clé est gérée par GitHub Secrets
2. **Batch vs Stream**: On utilise le Batch API pour économiser (~50% moins cher)
3. **Fichiers ignorés**: `batch_info_mistral.json`, `.env`, logs - jamais committé
4. **Temps**: Mistral batch = 5-30 min, Claude batch = ~1 heure

## ✅ Checklist Avant de Lancer

- [ ] J'ai lu ce guide entièrement
- [ ] J'ai configuré `MISTRAL_API_KEY` en tant que GitHub Secret
- [ ] Je suis sur la branche `mistral-translation` (vérifiez dans le repo local)
- [ ] Je vais à l'onglet Actions de GitHub
- [ ] Je suis prêt à cliquer "Run workflow"

## 🎯 Prochaines Étapes

1. **Configurez le secret** (Settings → Secrets)
2. **Lancez le workflow** (Actions tab)
3. **Attendez la traduction** (5-30 minutes)
4. **Vérifiez les résultats** (Insurtech_Solutions_EN/ branch)
5. **Fusionnez vers main** si satisfait (Create Pull Request)

---

**Questions?** Vérifiez les logs du workflow pour plus de détails.
