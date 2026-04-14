#!/usr/bin/env python3
"""
ONE-TIME SETUP: Create batch job for translating all solution files.
Run this once, save the batch_id, then use translate_batch_monitor.py to poll.
"""

import json
import os
from pathlib import Path
import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

def create_translation_batch():
    """Create a batch job to translate all solution files."""

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    source_dir = Path("/home/user/Insurance_Startups/Fiches_Solutions")
    output_dir = Path("/home/user/Insurance_Startups/Insurtech_Solutions_EN")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect all markdown files
    solution_files = sorted(source_dir.glob("*.md"))
    print(f"Found {len(solution_files)} solution files to translate")

    # Build batch requests (max 100,000 per batch)
    requests = []

    for file_path in solution_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            french_content = f.read()

        request = Request(
            custom_id=file_path.stem,  # Use filename without extension as ID
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-4-6",
                max_tokens=4096,
                messages=[{
                    "role": "user",
                    "content": f"""Translate the following French insurance solution description to English.

CRITICAL REQUIREMENTS:
1. Maintain EXACT markdown structure and formatting (headers, lists, tables, links)
2. Keep all URLs unchanged
3. Keep company names and technical terms unchanged
4. Keep hashtags (#) and special symbols as-is
5. Translate ONLY descriptive text content
6. Keep section header names in English (e.g., "## Identity" not "## Identité")
7. Preserve all formatting precisely

FRENCH CONTENT:
{french_content}

Return ONLY the translated markdown, with no preamble or explanation."""
                }]
            )
        )
        requests.append(request)

    print(f"Creating batch with {len(requests)} translation requests...")

    # Create the batch
    batch = client.messages.batches.create(requests=requests)

    print(f"\n✓ Batch created successfully!")
    print(f"  Batch ID: {batch.id}")
    print(f"  Status: {batch.processing_status}")
    print(f"  Total requests: {len(requests)}")

    # Save batch ID for reference
    batch_info = {
        "batch_id": batch.id,
        "created_at": batch.created_at.isoformat() if batch.created_at else None,
        "total_files": len(requests),
        "output_dir": str(output_dir),
        "source_dir": str(source_dir)
    }

    batch_file = Path("/home/user/Insurance_Startups/batch_info.json")
    with open(batch_file, 'w') as f:
        json.dump(batch_info, f, indent=2)

    print(f"  Batch info saved to: {batch_file}")
    print(f"\nNext steps:")
    print(f"1. Wait for batch to complete (usually within 1 hour)")
    print(f"2. Run: python translate_batch_monitor.py")
    print(f"3. Or manually check: python -c \"import anthropic; print(anthropic.Anthropic().messages.batches.retrieve('{batch.id}'))\"")

    return batch.id

if __name__ == "__main__":
    batch_id = create_translation_batch()
