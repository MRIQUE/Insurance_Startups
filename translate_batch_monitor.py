#!/usr/bin/env python3
"""
Monitor batch job and retrieve translated files once complete.
"""

import json
import os
import time
from pathlib import Path
import anthropic


def monitor_and_retrieve_batch(batch_id: str = None):
    """Monitor batch progress and retrieve results when complete."""

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Load batch info if not provided
    if not batch_id:
        batch_file = Path("/home/user/Insurance_Startups/batch_info.json")
        if batch_file.exists():
            with open(batch_file) as f:
                batch_info = json.load(f)
                batch_id = batch_info["batch_id"]
                output_dir = Path(batch_info["output_dir"])
        else:
            print("❌ No batch_info.json found. Run translate_batch_setup.py first.")
            return

    print(f"Monitoring batch: {batch_id}")
    print(f"Output directory: {output_dir}")

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Poll for completion
    max_wait_seconds = 24 * 3600  # 24 hours max
    start_time = time.time()

    while True:
        batch = client.messages.batches.retrieve(batch_id)

        elapsed = time.time() - start_time
        minutes = int(elapsed / 60)

        print(f"\n[{minutes:3d}m] Status: {batch.processing_status}")
        print(f"       Succeeded: {batch.request_counts.succeeded}")
        print(f"       Processing: {batch.request_counts.processing}")
        print(f"       Errored: {batch.request_counts.errored}")

        if batch.processing_status == "ended":
            print(f"\n✓ Batch processing complete!")
            break

        if elapsed > max_wait_seconds:
            print(f"\n⏱ Batch processing exceeded 24 hours. Proceeding to retrieve results.")
            break

        # Wait before next check (exponential backoff, max 5 minutes)
        wait_time = min(300, 10 + minutes)
        print(f"   Waiting {wait_time}s before next check...")
        time.sleep(wait_time)

    # Retrieve and save results
    print(f"\nRetrieving {batch.request_counts.succeeded} translated files...")

    successful = 0
    failed = 0
    failed_files = []

    for result in client.messages.batches.results(batch_id):
        custom_id = result.custom_id

        if result.result.type == "succeeded":
            msg = result.result.message
            # Extract translated content from response
            translated_text = next(
                (b.text for b in msg.content if b.type == "text"),
                None
            )

            if translated_text:
                # Save to output file
                output_file = output_dir / f"{custom_id}.md"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(translated_text)
                successful += 1
                if successful % 50 == 0:
                    print(f"  ✓ {successful} files saved...")
            else:
                print(f"  ✗ {custom_id}: No text in response")
                failed += 1
                failed_files.append(custom_id)

        elif result.result.type == "errored":
            print(f"  ✗ {custom_id}: {result.result.error.message}")
            failed += 1
            failed_files.append(custom_id)

    print(f"\n{'='*60}")
    print(f"Translation complete!")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Output directory: {output_dir}")

    if failed_files:
        print(f"\nFailed files ({len(failed_files)}):")
        for fname in failed_files[:10]:
            print(f"  - {fname}.md")
        if len(failed_files) > 10:
            print(f"  ... and {len(failed_files) - 10} more")

        # Save failed file list
        failed_file = Path("/home/user/Insurance_Startups/translation_failed.txt")
        with open(failed_file, 'w') as f:
            for fname in failed_files:
                f.write(f"{fname}.md\n")
        print(f"\nFailed files saved to: {failed_file}")

    return successful, failed


if __name__ == "__main__":
    import sys

    batch_id = sys.argv[1] if len(sys.argv) > 1 else None
    monitor_and_retrieve_batch(batch_id)
