# Insurance Solutions Translation Guide

This guide explains how to translate ~395 French solution files to English using the Anthropic SDK.

## Overview

Three approaches are provided:

| Approach | Cost | Speed | When to use |
|----------|------|-------|------------|
| **Batch API** (recommended) | 50% off | ~1 hour for 395 files | Full production run |
| **Streaming** | Full price | Real-time | Testing, small subsets |
| **Manual streaming** | Full price | Real-time | Debugging individual files |

## Quick Start: Batch API (Recommended)

### Step 1: Create the batch job (one-time)

```bash
python translate_batch_setup.py
```

Output:
```
✓ Batch created successfully!
  Batch ID: msgbatch_0198...
  Status: processing
  Total requests: 395
  Batch info saved to: batch_info.json

Next steps:
1. Wait for batch to complete (usually within 1 hour)
2. Run: python translate_batch_monitor.py
```

**Save the batch ID** — you'll need it to retrieve results.

### Step 2: Monitor progress and retrieve results

Check status periodically (or leave running):

```bash
python translate_batch_monitor.py
```

The script will:
- Poll every 10-300 seconds
- Display progress (succeeded, processing, errored)
- Retrieve all translated files once complete
- Save to `Insurtech_Solutions_EN/`

Example output:
```
[  0m] Status: processing
       Succeeded: 0
       Processing: 395
       Errored: 0
   Waiting 10s before next check...

[  5m] Status: processing
       Succeeded: 156
       Processing: 239
       Errored: 0

... (continues until complete)

✓ Batch processing complete!
  Successful: 392
  Failed: 3
  Output directory: /home/user/Insurance_Startups/Insurtech_Solutions_EN
```

## Alternative: Streaming Mode (Real-Time Feedback)

Use this if you want to see translations in real-time (useful for testing or small batches):

```bash
# Test with first 5 files
python translate_streaming.py 5

# Or translate all (slower, full price)
python translate_streaming.py
```

## Testing Individual Files

For debugging a single file:

```python
python -c "
import anthropic
from pathlib import Path

client = anthropic.Anthropic()
file_path = Path('Fiches_Solutions/360Globalnet_-_360SiteView.md')

with open(file_path) as f:
    content = f.read()

response = client.messages.create(
    model='claude-opus-4-6',
    max_tokens=4096,
    messages=[{'role': 'user', 'content': f'''Translate to English, preserve markdown:
{content}'''}]
)

print(response.content[0].text)
"
```

## Retrying Failed Files

If some files fail (saved to `translation_failed.txt`), you can retry them:

```bash
python translate_batch_setup.py --retry translation_failed.txt
```

(This script can be created if needed — ask if any files fail)

## Understanding the Output

### Success Case

```
Insurtech_Solutions_EN/
├── 360Globalnet_-_360SiteView.md
├── 7Analytics_-_7Analytics.md
├── A1_Tracker_-_A1_Tracker.md
└── ... (395 files total)
```

Each file contains the translated markdown with:
- ✓ Exact same structure (headers, lists, links)
- ✓ URLs unchanged
- ✓ Company names unchanged
- ✓ All markdown formatting preserved

### Partial Failure

```
Translation complete!
  Successful: 392
  Failed: 3
  
Failed files (3):
  - file1.md
  - file2.md
  - file3.md

Failed files saved to: translation_failed.txt
```

Retry these 3 files separately using streaming mode.

## Cost Comparison

For 395 files (~1.4M French characters):

| Method | Input cost | Output cost | Total | Notes |
|--------|-----------|-----------|-------|-------|
| Batch (50% off) | ~$3.50 | ~$17.50 | ~$21 | Slower, recommended |
| Streaming (full price) | ~$7.00 | ~$35.00 | ~$42 | Real-time feedback |

## Requirements

- Python 3.8+
- `anthropic` SDK: `pip install anthropic`
- `ANTHROPIC_API_KEY` environment variable set
- ~2GB disk space for output files

## Troubleshooting

### "No API key found"

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
python translate_batch_setup.py
```

### Batch stuck in "processing"

- Batches can take up to 24 hours
- Check status manually:
  ```bash
  python -c "import anthropic; b=anthropic.Anthropic().messages.batches.retrieve('msgbatch_...'); print(b.processing_status)"
  ```

### Some files failed to translate

1. Check `translation_failed.txt` for file list
2. Retry with streaming:
   ```bash
   python translate_streaming.py 5  # test mode
   ```
3. Or manually debug one file with test command above

### Output directory already exists

The scripts will preserve existing files. To force re-run:
```bash
rm -rf Insurtech_Solutions_EN
python translate_batch_setup.py
```

## Implementation Details

### Batch API Benefits

- **Cost**: 50% off all token pricing
- **Reliability**: Automatic retries, guaranteed delivery
- **Latency**: ~1 hour typical (up to 24 hours acceptable)
- **Scale**: Handles 100K+ requests per batch

### Markdown Preservation

Each translation request includes:
- Explicit instruction to preserve all markdown structure
- Keep URLs, company names, hashtags unchanged
- Only translate descriptive text
- Translate section headers to English (Identité → Identity)

### Error Handling

- Failed requests are reported with the original file name
- Network errors trigger automatic retries (SDK handles this)
- Invalid API responses are caught and logged
- Partial batches can be re-run with failed file subset

## Next Steps

1. **Run setup:** `python translate_batch_setup.py`
2. **Monitor:** `python translate_batch_monitor.py`
3. **Verify:** Check 5-10 translated files for quality
4. **Commit:** Git commit the `Insurtech_Solutions_EN/` directory
5. **Optional retry:** If any files failed, retry with streaming mode

---

**Questions?** Check the script comments or modify the prompt in `translate_batch_setup.py` if you need different translation behavior.
