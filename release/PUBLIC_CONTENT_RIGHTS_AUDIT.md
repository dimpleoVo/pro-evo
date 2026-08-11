# Public content rights audit

**Result: PASS** (repository-content audit; not legal advice).

## Scope and evidence

- Every non-license public file was introduced by the clean-room public staging history, whose first commit is `a3be2d673d1e39dbd723e6a32d76b9c3b9dd7449`; the staging history has no private-repository parent.
- The tracked-file hash comparison against the private repository's tracked files found no exact file-content overlap.
- All figures are repository-native SVG authored for this release; there are no downloaded images, binaries, or embedded external assets.
- The audit found no copyright notices, third-party attribution notices, company/internal identifiers, or claims of imported external code in the public content.
- The three canonical license texts were retrieved from their official publishers and retained unmodified as license texts.

## Origin classification

| Content class | Audit classification | Publication decision |
| --- | --- | --- |
| Open-core code, examples, tests, and tools | Original clean-room public release content | Included |
| Documentation and figures | Original clean-room public release content | Included |
| Gate20–Gate22 JSON evidence projections | User-authorized sanitized public research evidence | Included |
| Canonical license texts | Compatibly licensed standard legal texts | Included |
| Private runtime, benchmarks, raw artifacts, provider material, and hidden evaluation assets | Not part of the public allowlist | Excluded |

This audit does not infer ownership for material not present in this repository. Any future addition must be classified as owned or compatibly licensed before publication.

