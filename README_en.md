# my-actions

[日本語](README.md)

A collection of custom GitHub Actions (Composite Actions) for use in your workflows.

## Available Actions

### action-request-id-token

Composite Action to retrieve GitHub OIDC ID tokens.

**Purpose:** Federated authentication with external services

**Usage Example:**
```yaml
- uses: sinofseven/action-request-id-token@v1.0.0
  with:
    audience: 'my-service'  # [Optional] OIDC audience claim - identifier for external service
```

### action-verify-jwt

Action to verify JWT tokens.

**Purpose:** Verify JWT signature using JWKS endpoint

**Usage Example:**
```yaml
- uses: sinofseven/action-verify-jwt@v1.0.0
  with:
    token: ${{ env.JWT_TOKEN }}  # [Required] JWT token to verify
    jwks-url: 'https://example.com/.well-known/jwks.json'  # [Required] JWKS endpoint URL
    audience: 'my-audience'  # [Optional] Expected audience claim value
```

### action-repository-dispatch

Action to send `repository_dispatch` event to another repository.

**Purpose:** Trigger workflows in other repositories automatically

**Usage Example:**
```yaml
- uses: sinofseven/action-repository-dispatch@v1.0.0
  with:
    target_repo: 'org/target-repo'  # [Required] Target repository (owner/repo format)
    event_type: 'deploy'  # [Required] repository_dispatch event type
    token: ${{ secrets.GITHUB_TOKEN }}  # [Required] PAT with permissions for target repository
    payload: '{"environment": "production"}'  # [Optional] Payload passed when triggering event (JSON format)
```
