---
name: update-actions-documentation
description: |
  Automatically update GitHub Actions repository documentation.
  
  Use this skill when you need to:
  - Update README files with action descriptions and usage examples
  - Add parameter documentation with [Required/Optional] labels to code examples
  - Maintain consistent documentation across Japanese and English versions
  - Extract and document inputs/outputs from submodule README files
  
  This skill is designed for my-actions repository (a GitHub Actions collection) and handles the complete documentation workflow from reading submodule metadata to generating fully-commented examples.
---

# update-actions-documentation Skill

## Overview

This skill automatically generates and updates README documentation for GitHub Actions repositories. It reads submodule information, extracts action details from their README files, and produces well-documented examples with parameter descriptions and Required/Optional indicators.

**What it does:**
1. Reads `.gitmodules` to identify all action submodules
2. Extracts action metadata from each submodule's README (description, inputs, outputs)
3. Generates root README files (Japanese and English versions)
4. Automatically adds inline comments to examples with parameter descriptions and Required/Optional labels

**Typical use:** After adding or updating action submodules, run this skill to keep documentation in sync.

## How to use

When you want to update README documentation:
1. Make sure any submodule README changes are committed
2. Invoke this skill
3. It will analyze `.gitmodules` and all submodule READMEs
4. It will output updated `README.md` (Japanese) and `README_en.md` (English)

The skill requires no manual parameters — it works by reading the repository structure.

## What gets generated

### README.md (Japanese version)
- Repository overview in Japanese
- List of all actions with descriptions
- Usage examples for each action
- Inline comments on examples with [Required/Optional] parameter labels and descriptions

### README_en.md (English version)
- Same structure as Japanese version but in English
- Consistent with Japanese version's organization and examples

## Example output format

```yaml
- uses: sinofseven/action-verify-jwt@v1.0.0
  with:
    token: ${{ env.JWT_TOKEN }}  # [Required] JWT token to verify
    jwks-url: 'https://example.com/.well-known/jwks.json'  # [Required] JWKS endpoint URL
    audience: 'my-audience'  # [Optional] Expected audience claim value
```

## How it determines Required vs Optional

The skill reads each action's submodule README and identifies which inputs are required. If an input doesn't have explicit documentation, it checks for:
- Keywords like "required" or "optional" in the description
- Whether a default value is provided
- Common patterns for required fields (e.g., token, url, id fields are usually required)

## Limitations

- Works with the current my-actions repository structure
- Requires readable README files in each submodule
- Assumes YAML format for action examples
- Currently handles the three main actions (action-request-id-token, action-verify-jwt, action-repository-dispatch)

## Future improvements

- Support for additional action submodules
- Configurable parameter documentation style
- Integration with action.yml metadata directly
- Automatic changelog generation
