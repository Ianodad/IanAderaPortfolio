#!/usr/bin/env bash
# Curl every external href in index.html and print "status  url".
# Usage: scripts/check-links.sh [path/to/index.html]

set -u

FILE="${1:-index.html}"

if [[ ! -f "$FILE" ]]; then
  echo "File not found: $FILE" >&2
  exit 1
fi

urls=$(grep -oE 'href="https?://[^"]+"' "$FILE" | sed -E 's/^href="//; s/"$//' | sort -u)

if [[ -z "$urls" ]]; then
  echo "No external links found in $FILE"
  exit 0
fi

while IFS= read -r url; do
  status=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 15 -A "Mozilla/5.0 (compatible; link-check/1.0)" "$url")
  printf "%-5s %s\n" "$status" "$url"
done <<< "$urls"
