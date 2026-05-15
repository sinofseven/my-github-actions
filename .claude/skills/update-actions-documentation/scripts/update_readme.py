#!/usr/bin/env python3
"""
Script to update README.md and README_en.md for my-actions repository.
Reads submodule information and generates documentation with parameter comments.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

class ActionDocumentationGenerator:
    """Generate documentation for GitHub Actions repository."""

    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.gitmodules_path = self.repo_path / ".gitmodules"
        self.actions = {}

    def read_gitmodules(self) -> List[Tuple[str, str]]:
        """Read .gitmodules and extract submodule names and paths."""
        submodules = []
        if not self.gitmodules_path.exists():
            print(f"Warning: {self.gitmodules_path} not found")
            return submodules

        with open(self.gitmodules_path, 'r') as f:
            content = f.read()

        # Extract submodule names and paths
        pattern = r'\[submodule "([^"]+)"\]\s+path = ([^\n]+)'
        matches = re.findall(pattern, content)

        return matches

    def extract_action_info(self, readme_path: Path) -> Dict:
        """Extract action information from README."""
        if not readme_path.exists():
            return {}

        with open(readme_path, 'r') as f:
            content = f.read()

        info = {
            'description': '',
            'inputs': {},
            'outputs': {},
        }

        # Extract description (first line or heading)
        lines = content.split('\n')
        for line in lines:
            if line.strip() and not line.startswith('#'):
                info['description'] = line.strip()
                break

        # Extract inputs section
        inputs_match = re.search(r'## Inputs?.*?(?=##|\Z)', content, re.DOTALL)
        if inputs_match:
            inputs_section = inputs_match.group()
            # Look for input definitions
            input_pattern = r'[`*]*(\w+)[`*]*.*?(?:Required|Optional|required|optional)?.*?[:-]?\s*([^\n]*)'
            matches = re.findall(input_pattern, inputs_section)
            for name, desc in matches:
                if name and name not in ['Inputs']:
                    is_required = 'required' in desc.lower()
                    info['inputs'][name] = {
                        'description': desc.strip(),
                        'required': is_required
                    }

        # Extract outputs section
        outputs_match = re.search(r'## Outputs?.*?(?=##|\Z)', content, re.DOTALL)
        if outputs_match:
            outputs_section = outputs_match.group()
            output_pattern = r'[`*]*(\w+)[`*]*.*?[:-]?\s*([^\n]*)'
            matches = re.findall(output_pattern, outputs_section)
            for name, desc in matches:
                if name and name not in ['Outputs']:
                    info['outputs'][name] = desc.strip()

        return info

    def get_parameter_info(self, action_name: str) -> Dict:
        """Get parameter information for each action based on known data."""
        # Hardcoded parameter info for the three main actions
        parameter_map = {
            'action-request-id-token': {
                'audience': {
                    'description': 'OIDC audience claim - identifier for external service',
                    'description_en': 'OIDC audience claim - identifier for external service',
                    'required': False
                }
            },
            'action-verify-jwt': {
                'token': {
                    'description': '検証対象のJWTトークン',
                    'description_en': 'JWT token to verify',
                    'required': True
                },
                'jwks-url': {
                    'description': 'JWKS エンドポイントのURL',
                    'description_en': 'JWKS endpoint URL',
                    'required': True
                },
                'audience': {
                    'description': '検証対象の audience クレーム値',
                    'description_en': 'Expected audience claim value',
                    'required': False
                }
            },
            'action-repository-dispatch': {
                'target_repo': {
                    'description': 'イベント送信先リポジトリ（オーナー/リポジトリ形式）',
                    'description_en': 'Target repository (owner/repo format)',
                    'required': True
                },
                'event_type': {
                    'description': 'repository_dispatch イベントタイプ',
                    'description_en': 'repository_dispatch event type',
                    'required': True
                },
                'token': {
                    'description': '対象リポジトリへの権限を持つPAT',
                    'description_en': 'PAT with permissions for target repository',
                    'required': True
                },
                'payload': {
                    'description': 'イベント発火時に渡すペイロード（JSON形式）',
                    'description_en': 'Payload passed when triggering event (JSON format)',
                    'required': False
                }
            }
        }

        return parameter_map.get(action_name, {})

    def generate_readme_japanese(self) -> str:
        """Generate Japanese README.md."""
        content = """# my-actions

このリポジトリは、GitHub Actions ワークフロー内で使用するカスタムアクション（Composite Actions）の集合です。

## Available Actions

"""

        # Add each action
        actions_info = [
            {
                'name': 'action-request-id-token',
                'title': 'GitHub OIDC IDトークンを取得するアクション',
                'purpose': '外部サービスとのフェデレーション認証',
                'example_with': "audience: 'my-service'"
            },
            {
                'name': 'action-verify-jwt',
                'title': 'JWTトークンを検証するアクション',
                'purpose': 'JWKS エンドポイントを使用して JWT 署名を検証',
                'example_with': """token: ${{ env.JWT_TOKEN }}
    jwks-url: 'https://example.com/.well-known/jwks.json'
    audience: 'my-audience'"""
            },
            {
                'name': 'action-repository-dispatch',
                'title': '別リポジトリに `repository_dispatch` イベントを送信するアクション',
                'purpose': '別のリポジトリのワークフローを自動トリガー',
                'example_with': """target_repo: 'org/target-repo'
    event_type: 'deploy'
    token: ${{ secrets.GITHUB_TOKEN }}
    payload: '{"environment": "production"}'"""
            }
        ]

        for action in actions_info:
            content += f"""### {action['name']}

{action['title']}

**用途：** {action['purpose']}

**使用例：**
```yaml
- uses: sinofseven/{action['name']}@v1.0.0
  with:
    {action['example_with']}
```
"""

            # Add parameter comments
            if action['name'] == 'action-request-id-token':
                content = content.replace(
                    "audience: 'my-service'",
                    "audience: 'my-service'  # [Optional] OIDC audience クレーム - 外部サービスの識別子"
                )
            elif action['name'] == 'action-verify-jwt':
                content = content.replace(
                    "token: ${{ env.JWT_TOKEN }}",
                    "token: ${{ env.JWT_TOKEN }}  # [Required] 検証対象のJWTトークン"
                ).replace(
                    "jwks-url: 'https://example.com/.well-known/jwks.json'",
                    "jwks-url: 'https://example.com/.well-known/jwks.json'  # [Required] JWKS エンドポイントのURL"
                ).replace(
                    "audience: 'my-audience'",
                    "audience: 'my-audience'  # [Optional] 検証対象の audience クレーム値"
                )
            elif action['name'] == 'action-repository-dispatch':
                content = content.replace(
                    "target_repo: 'org/target-repo'",
                    "target_repo: 'org/target-repo'  # [Required] イベント送信先リポジトリ（オーナー/リポジトリ形式）"
                ).replace(
                    "event_type: 'deploy'",
                    "event_type: 'deploy'  # [Required] repository_dispatch イベントタイプ"
                ).replace(
                    "token: ${{ secrets.GITHUB_TOKEN }}",
                    "token: ${{ secrets.GITHUB_TOKEN }}  # [Required] 対象リポジトリへの権限を持つPAT"
                ).replace(
                    "payload: '{\"environment\": \"production\"}'",
                    "payload: '{\"environment\": \"production\"}'  # [Optional] イベント発火時に渡すペイロード（JSON形式）"
                )

        return content

    def generate_readme_english(self) -> str:
        """Generate English README_en.md."""
        content = """# my-actions

A collection of custom GitHub Actions (Composite Actions) for use in your workflows.

## Available Actions

"""

        # Add each action
        actions_info = [
            {
                'name': 'action-request-id-token',
                'title': 'Composite Action to retrieve GitHub OIDC ID tokens.',
                'purpose': 'Federated authentication with external services',
                'example_with': "audience: 'my-service'"
            },
            {
                'name': 'action-verify-jwt',
                'title': 'Action to verify JWT tokens.',
                'purpose': 'Verify JWT signature using JWKS endpoint',
                'example_with': """token: ${{ env.JWT_TOKEN }}
    jwks-url: 'https://example.com/.well-known/jwks.json'
    audience: 'my-audience'"""
            },
            {
                'name': 'action-repository-dispatch',
                'title': 'Action to send `repository_dispatch` event to another repository.',
                'purpose': 'Trigger workflows in other repositories automatically',
                'example_with': """target_repo: 'org/target-repo'
    event_type: 'deploy'
    token: ${{ secrets.GITHUB_TOKEN }}
    payload: '{"environment": "production"}'"""
            }
        ]

        for action in actions_info:
            content += f"""### {action['name']}

{action['title']}

**Purpose:** {action['purpose']}

**Usage Example:**
```yaml
- uses: sinofseven/{action['name']}@v1.0.0
  with:
    {action['example_with']}
```
"""

            # Add parameter comments
            if action['name'] == 'action-request-id-token':
                content = content.replace(
                    "audience: 'my-service'",
                    "audience: 'my-service'  # [Optional] OIDC audience claim - identifier for external service"
                )
            elif action['name'] == 'action-verify-jwt':
                content = content.replace(
                    "token: ${{ env.JWT_TOKEN }}",
                    "token: ${{ env.JWT_TOKEN }}  # [Required] JWT token to verify"
                ).replace(
                    "jwks-url: 'https://example.com/.well-known/jwks.json'",
                    "jwks-url: 'https://example.com/.well-known/jwks.json'  # [Required] JWKS endpoint URL"
                ).replace(
                    "audience: 'my-audience'",
                    "audience: 'my-audience'  # [Optional] Expected audience claim value"
                )
            elif action['name'] == 'action-repository-dispatch':
                content = content.replace(
                    "target_repo: 'org/target-repo'",
                    "target_repo: 'org/target-repo'  # [Required] Target repository (owner/repo format)"
                ).replace(
                    "event_type: 'deploy'",
                    "event_type: 'deploy'  # [Required] repository_dispatch event type"
                ).replace(
                    "token: ${{ secrets.GITHUB_TOKEN }}",
                    "token: ${{ secrets.GITHUB_TOKEN }}  # [Required] PAT with permissions for target repository"
                ).replace(
                    "payload: '{\"environment\": \"production\"}'",
                    "payload: '{\"environment\": \"production\"}'  # [Optional] Payload passed when triggering event (JSON format)"
                )

        return content

    def update_readmes(self):
        """Update both README files."""
        # Generate Japanese version
        readme_jp = self.generate_readme_japanese()
        readme_jp_path = self.repo_path / "README.md"
        with open(readme_jp_path, 'w') as f:
            f.write(readme_jp)
        print(f"✓ Updated {readme_jp_path}")

        # Generate English version
        readme_en = self.generate_readme_english()
        readme_en_path = self.repo_path / "README_en.md"
        with open(readme_en_path, 'w') as f:
            f.write(readme_en)
        print(f"✓ Updated {readme_en_path}")


if __name__ == "__main__":
    generator = ActionDocumentationGenerator()
    generator.update_readmes()
    print("\nDocumentation updated successfully!")
