# Graph Report - tallerDDD  (2026-11-11)

## Corpus Check
- 2 files · ~26,546 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 9 nodes · 8 edges · 2 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]

## God Nodes (most connected - your core abstractions)
1. `lista()` - 2 edges
2. `afinidad()` - 2 edges
3. `toggle` - 1 edges
4. `nav` - 1 edges
5. `open` - 1 edges
6. `year` - 1 edges

## Toxic Hotspots (high risk + high activity)
1. `csv_de()` - Risk Score: 85% (FUNCTION)

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "Community 0"
_Handles opening, toggling, and navigating through years in a calendar component._
Cohesion: 0.4
Nodes (4): nav, open, toggle, year

### Community 1 - "Community 1"

Cohesion: 0.67
Nodes (2): afinidad(), lista()

## Knowledge Gaps
- **4 isolated node(s):** `toggle`, `nav`, `open`, `year`
  These have ≤1 connection - possible missing edges or undocumented components.