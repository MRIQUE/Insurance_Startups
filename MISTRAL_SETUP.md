# Mistral Translation Setup

## ⚠️ Security Notice

The Mistral API key should **NOT** be committed to GitHub. Instead:

1. **Store as GitHub Secret**:
   - Go to repo Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `MISTRAL_API_KEY`
   - Value: Your Mistral API key

2. **Use in GitHub Actions** (already configured in `.github/workflows/mistral-translation.yml`)

3. **Local testing** (use environment variable):
   ```bash
   export MISTRAL_API_KEY="your_key_here"
   python mistral_translate.py
   ```

## Usage

### Option 1: GitHub Actions (Recommended)

1. **Add the secret** to GitHub repository secrets (Settings → Secrets)

2. **Trigger the workflow**:
   - Go to Actions tab
   - Select "Mistral Translation Pipeline"
   - Click "Run workflow"
   - Leave batch_id empty to submit new batch

3. **Monitor in Actions tab** - workflow will:
   - Submit batch job to Mistral API
   - Save batch info
   - Commit results to `mistral-translation` branch

### Option 2: Local Execution

```bash
# Submit batch
python mistral_translate.py --api-key "your_key_here"

# Later, retrieve results
python mistral_translate.py --api-key "your_key_here" --batch-id "batch_xyz"
```

### Option 3: Retrieve batch submitted via GitHub Actions

1. Find batch ID in workflow logs
2. Trigger workflow again with batch_id parameter
3. Workflow will retrieve results and commit

## Files

- `mistral_translate.py` - Main translation script
- `.github/workflows/mistral-translation.yml` - GitHub Actions workflow
- `batch_info_mistral.json` - Batch metadata (auto-generated)
- `Insurtech_Solutions_EN/` - Output directory with translations

## Features

✓ **Batch processing** - Handles 395+ files efficiently  
✓ **Markdown preservation** - Keeps formatting, URLs, company names intact  
✓ **Error handling** - Tracks failed files for retry  
✓ **GitHub integration** - Auto-commits results, tracks batch status  
✓ **Secure API key** - Uses GitHub Secrets, never exposed in code  

## Notes

- Mistral batch API typically processes jobs in 5-30 minutes
- Temperature set to 0.3 for consistent translations
- Max 4096 tokens per response (sufficient for solution files)
- Failed files are logged and can be retried independently
