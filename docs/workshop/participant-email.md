# Workshop Preparation — Please Complete Before the Session

Hi team,

Please complete the following setup steps before the workshop. This should take about 15-20 minutes.

---

## 1. Verify Access

You've been granted access to the following. Please verify you can reach each one:

- [ ] **GitLab:** https://gitlab.dataart.com/da/dalf — you should see the DALF repositories
- [ ] **GitHub:** https://github.com/okomissarov/full-stack-fastapi-template — public workshop repo
- [ ] **JIRA:** https://support.dataart.com/browse/AWSP-114 — Time Tracking epic in AWSP project

If any access is missing, let me know before the workshop.

---

## 2. Install Prerequisites

### Python 3.10+

macOS:
```bash
brew install python
```
Windows:
```bash
winget install Python.Python.3
```
Linux:
```bash
sudo apt update && sudo apt install python3 python3-pip
```
Verify: `python3 --version`

### Node.js 18+

macOS:
```bash
brew install node
```
Windows:
```bash
winget install OpenJS.NodeJS
```
Linux:
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs
```
Verify: `node --version`

### Git

Verify: `git --version`

---

## 3. Install Kiro CLI

Follow the official installation guide: https://kiro.dev/docs/cli/installation/

Quick install:
```bash
# macOS / Linux
curl -fsSL https://kiro.dev/install.sh | bash

# Windows — see https://kiro.dev/docs/cli/installation/
```

### Login to Kiro

```bash
kiro-cli login
```

when prompted, provide:
- region: us-east-1 
- start-url https://dataart.awsapps.com/start/#

This opens a browser for authentication. Log in with your DataArt credentials and authorize the access.

### Verify Kiro Works

Open your IDE (VS Code, or any terminal) and run:
```bash
kiro-cli --version
```

Or start an interactive session:
```bash
kiro-cli chat
```

Type `/quit` to exit.

---

## 4. Clone Repositories

### Workshop repo (GitHub):
```bash
git clone https://github.com/okomissarov/full-stack-fastapi-template.git
```

### AILA SDK (GitLab):
```bash
git clone git@gitlab.dataart.com:da/dalf/aila-kiro-home.git
```

If SSH doesn't work, try HTTPS:
```bash
git clone https://gitlab.dataart.com/da/dalf/aila-kiro-home.git
```

---

## 5. Jira MCP Server (for reading JIRA stories)

The workshop uses a Jira MCP server so agents can read JIRA epics and stories directly.

### Install uv (package runner)

macOS / Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify: `uvx --version`

### Generate JIRA Personal Access Token

1. Go to https://support.dataart.com/secure/ViewProfile.jspa
2. Click "Personal Access Tokens" in the left menu
3. Click "Create token"
4. Name it "kiro-workshop" and click "Create"
5. Copy the token (you won't see it again)

### Configure MCP

Create or update `~/.kiro/settings/mcp.json`:
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": ["mcp-atlassian"],
      "env": {
        "JIRA_URL": "https://support.dataart.com",
        "JIRA_PERSONAL_TOKEN": "YOUR_TOKEN_HERE",
        "JIRA_SSL_VERIFY": "false"
      }
    }
  }
}
```

Replace `YOUR_TOKEN_HERE` with your personal access token.

### Verify

Start Kiro and ask: "Read JIRA issue AWSP-114"

---

## 6. Quick Verification Checklist

Run through this checklist to confirm everything is ready:

- [ ] `python3 --version` → 3.10+
- [ ] `node --version` → 18+
- [ ] `git --version` → any
- [ ] `uvx --version` → installed
- [ ] `kiro-cli --version` → installed
- [ ] `kiro-cli login` → authenticated
- [ ] `~/.kiro/settings/mcp.json` → exists with JIRA token
- [ ] `cd full-stack-fastapi-template && ls workspace.py` → file exists
- [ ] `cd aila-kiro-home && ls AILA-SKILLS-BOOTSTRAP.md` → file exists
- [ ] Can access JIRA AWSP-114 in browser

---

If you run into any issues, reach out and we'll sort it out before the workshop.

**Workshop agenda:** https://github.com/okomissarov/full-stack-fastapi-template/blob/master/docs/workshop/agenda.md

See you there!
