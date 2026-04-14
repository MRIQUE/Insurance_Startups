#!/usr/bin/env python3
"""
Mistral API translation script for solution files.
Uses Mistral's batch API for cost-effective translation of 395+ files.
"""

import json
import os
from pathlib import Path
import requests
import time


class MistralTranslator:
    """Translate files using Mistral API."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("MISTRAL_API_KEY")
        if not self.api_key:
            raise ValueError("MISTRAL_API_KEY not found in environment or arguments")

        self.base_url = "https://api.mistral.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def translate_single(self, content: str) -> str:
        """Translate content using Mistral API."""

        prompt = f"""Translate the following French insurance solution description to English.

CRITICAL REQUIREMENTS:
1. Maintain EXACT markdown structure and formatting (headers, lists, tables, links)
2. Keep all URLs unchanged
3. Keep company names and technical terms unchanged
4. Keep hashtags (#) and special symbols as-is
5. Translate ONLY descriptive text content
6. Keep section header names in English (e.g., "## Identity" not "## Identité")
7. Preserve all formatting precisely

FRENCH CONTENT:
{content}

Return ONLY the translated markdown, with no preamble or explanation."""

        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=self.headers,
            json={
                "model": "mistral-large-latest",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3,  # Lower temperature for consistent translations
                "max_tokens": 4096
            },
            timeout=30
        )

        response.raise_for_status()
        result = response.json()

        return result["choices"][0]["message"]["content"]

    def create_batch_requests(self) -> list:
        """Create batch requests for all solution files."""

        source_dir = Path("/home/user/Insurance_Startups/Fiches_Solutions")
        solution_files = sorted(source_dir.glob("*.md"))

        requests_list = []

        for file_path in solution_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                french_content = f.read()

            prompt = f"""Translate the following French insurance solution description to English.

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

            requests_list.append({
                "custom_id": file_path.stem,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "model": "mistral-large-latest",
                "temperature": 0.3,
                "max_tokens": 4096
            })

        return requests_list

    def submit_batch(self) -> str:
        """Submit batch job to Mistral API."""

        requests_list = self.create_batch_requests()
        print(f"Submitting batch with {len(requests_list)} requests...")

        # Mistral batch API
        response = requests.post(
            f"{self.base_url}/batch",
            headers=self.headers,
            json={
                "requests": requests_list,
                "timeout_seconds": 3600
            },
            timeout=60
        )

        response.raise_for_status()
        result = response.json()

        batch_id = result.get("id")
        print(f"✓ Batch submitted: {batch_id}")
        print(f"  Status: {result.get('status')}")

        return batch_id

    def get_batch_status(self, batch_id: str) -> dict:
        """Get batch status from Mistral API."""

        response = requests.get(
            f"{self.base_url}/batch/{batch_id}",
            headers=self.headers,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    def retrieve_batch_results(self, batch_id: str, output_dir: Path = None) -> tuple:
        """Retrieve and save batch results."""

        if output_dir is None:
            output_dir = Path("/home/user/Insurance_Startups/Insurtech_Solutions_EN")

        output_dir.mkdir(parents=True, exist_ok=True)

        response = requests.get(
            f"{self.base_url}/batch/{batch_id}/results",
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        successful = 0
        failed = 0
        failed_files = []

        for line in response.iter_lines():
            if not line:
                continue

            result = json.loads(line)
            custom_id = result.get("custom_id")

            if result.get("error"):
                print(f"✗ {custom_id}: {result['error']}")
                failed += 1
                failed_files.append(custom_id)
            else:
                try:
                    translated = result["result"]["choices"][0]["message"]["content"]
                    output_file = output_dir / f"{custom_id}.md"

                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(translated)

                    successful += 1
                    if successful % 50 == 0:
                        print(f"  ✓ {successful} files saved...")

                except (KeyError, IndexError) as e:
                    print(f"✗ {custom_id}: Failed to parse response - {e}")
                    failed += 1
                    failed_files.append(custom_id)

        return successful, failed, failed_files


def main():
    """Main translation workflow."""

    import sys

    api_key = None
    batch_id = None

    # Parse arguments
    if "--api-key" in sys.argv:
        idx = sys.argv.index("--api-key")
        api_key = sys.argv[idx + 1]

    if "--batch-id" in sys.argv:
        idx = sys.argv.index("--batch-id")
        batch_id = sys.argv[idx + 1]

    # Initialize translator
    translator = MistralTranslator(api_key=api_key)

    # Submit batch if no ID provided
    if not batch_id:
        print("=" * 70)
        print("MISTRAL TRANSLATION: Submitting batch job")
        print("=" * 70)

        batch_id = translator.submit_batch()

        # Save batch info
        batch_info = {
            "batch_id": batch_id,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "platform": "mistral"
        }

        batch_file = Path("/home/user/Insurance_Startups/batch_info_mistral.json")
        with open(batch_file, 'w') as f:
            json.dump(batch_info, f, indent=2)

        print(f"\nBatch info saved to: {batch_file}")
        print(f"To retrieve results later, run:")
        print(f"  python mistral_translate.py --batch-id {batch_id}")

        return

    # Monitor batch
    print("=" * 70)
    print(f"MISTRAL TRANSLATION: Monitoring batch {batch_id}")
    print("=" * 70)

    max_wait = 3600  # 1 hour for Mistral batch
    start_time = time.time()

    while True:
        try:
            status_info = translator.get_batch_status(batch_id)
            status = status_info.get("status")
            elapsed = int((time.time() - start_time) / 60)

            print(f"\n[{elapsed:3d}m] Status: {status}")

            if status in ["completed", "failed", "cancelled"]:
                break

            if time.time() - start_time > max_wait:
                print("⏱ Timeout reached. Attempting to retrieve results anyway...")
                break

            time.sleep(30)

        except Exception as e:
            print(f"Error checking status: {e}")
            time.sleep(30)

    # Retrieve results
    print("\n" + "=" * 70)
    print("Retrieving translated files...")
    print("=" * 70)

    try:
        successful, failed, failed_files = translator.retrieve_batch_results(batch_id)

        print(f"\n✓ Translation complete!")
        print(f"  Successful: {successful}")
        print(f"  Failed: {failed}")
        print(f"  Output: /home/user/Insurance_Startups/Insurtech_Solutions_EN/")

        if failed_files:
            print(f"\nFailed files:")
            for f in failed_files[:10]:
                print(f"  - {f}.md")
            if len(failed_files) > 10:
                print(f"  ... and {len(failed_files) - 10} more")

    except Exception as e:
        print(f"✗ Error retrieving results: {e}")


if __name__ == "__main__":
    main()
