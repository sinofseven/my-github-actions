# my-actions

このリポジトリは、GitHub Actions ワークフロー内で使用するカスタムアクション（Composite Actions）の集合です。

## Available Actions

### action-request-id-token

GitHub OIDC IDトークンを取得するアクション

**用途：** 外部サービスとのフェデレーション認証

**使用例：**
```yaml
- uses: sinofseven/action-request-id-token@v1.0.0
  with:
    audience: 'my-service'  # [Optional] OIDC audience クレーム - 外部サービスの識別子
```

### action-verify-jwt

JWTトークンを検証するアクション

**用途：** JWKS エンドポイントを使用して JWT 署名を検証

**使用例：**
```yaml
- uses: sinofseven/action-verify-jwt@v1.0.0
  with:
    token: ${{ env.JWT_TOKEN }}  # [Required] 検証対象のJWTトークン
    jwks-url: 'https://example.com/.well-known/jwks.json'  # [Required] JWKS エンドポイントのURL
    audience: 'my-audience'  # [Optional] 検証対象の audience クレーム値
```

### action-repository-dispatch

別リポジトリに `repository_dispatch` イベントを送信するアクション

**用途：** 別のリポジトリのワークフローを自動トリガー

**使用例：**
```yaml
- uses: sinofseven/action-repository-dispatch@v1.0.0
  with:
    target_repo: 'org/target-repo'  # [Required] イベント送信先リポジトリ（オーナー/リポジトリ形式）
    event_type: 'deploy'  # [Required] repository_dispatch イベントタイプ
    token: ${{ secrets.GITHUB_TOKEN }}  # [Required] 対象リポジトリへの権限を持つPAT
    payload: '{"environment": "production"}'  # [Optional] イベント発火時に渡すペイロード（JSON形式）
```