#!/usr/bin/env python3
"""
ALTERNATIVE: Streaming translation for faster feedback on small batches.
Use this if you want results in real-time instead of waiting for batch completion.
Best for: testing, small subsets, or when speed matters more than cost.

For full 395 files: use the batch approach (50% cheaper, slower, suitable for non-urgent work).
"""

import os
from pathlib import Path
import anthropic


def translate_file_streaming(client: anthropic.Anthropic, file_path: Path) -> str:
    """Translate a single file with streaming output."""

    with open(file_path, 'r', encoding='utf-8') as f:
        french_content = f.read()

    print(f"\nTranslating: {file_path.name}")

    translated_parts = []

    # Use streaming for real-time output
    with client.messages.stream(
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
    ) as stream:
        for text in stream.text_stream:
            translated_parts.append(text)
            print(text, end="", flush=True)

    print()  # newline after streaming
    return "".join(translated_parts)


def translate_files_streaming(max_files: int = None):
    """Translate files with streaming output."""

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    source_dir = Path("/home/user/Insurance_Startups/Fiches_Solutions")
    output_dir = Path("/home/user/Insurance_Startups/Insurtech_Solutions_EN")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Get files to translate
    solution_files = sorted(source_dir.glob("*.md"))
    if max_files:
        solution_files = solution_files[:max_files]

    print(f"Translating {len(solution_files)} files (streaming)...")
    print("=" * 70)

    successful = 0
    failed = 0

    for idx, file_path in enumerate(solution_files, 1):
        try:
            print(f"\n[{idx}/{len(solution_files)}]", end=" ")

            translated = translate_file_streaming(client, file_path)

            # Save translated file
            output_file = output_dir / file_path.name
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated)

            print(f"✓ Saved: {output_file.name}")
            successful += 1

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            failed += 1

    print("\n" + "=" * 70)
    print(f"Translation complete (streaming mode)")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Output directory: {output_dir}")


if __name__ == "__main__":
    import sys

    # Optional: limit to first N files for testing
    max_files = int(sys.argv[1]) if len(sys.argv) > 1 else None

    if max_files:
        print(f"Testing with first {max_files} files...")
    else:
        print("Warning: This will translate all 395 files and may take hours.")
        print("For faster/cheaper processing, use the batch approach instead.")
        response = input("Continue? (y/n): ")
        if response.lower() != 'y':
            print("Cancelled.")
            exit(0)

    translate_files_streaming(max_files)
