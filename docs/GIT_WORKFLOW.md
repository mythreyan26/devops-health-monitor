# Git Workflow & Branching Strategy

This document details the exact version control procedure used for this DevOps project.

## 1. Branching Model

```
(main)    ---[v0.1.0]---------------------------------------[v1.0.0 Merge PR] (Tag: v1.0.0)
                \                                                /
(dev)            \---[Initial Setup]-----------------[Merge PR]-/
                                  \                 /
(feature/metrics)                  \---[Add Tests]-/
```

- **`main`**: Production branch. Always stable, deployable, and tagged with version numbers (`v1.0.0`).
- **`dev`**: Integration branch where tested feature branches converge.
- **`feature/*`**: Short-lived branches created for specific enhancements or bug fixes.

---

## 2. Complete Step-by-Step Command Walkthrough

### Phase 1: Initialize Repository & Base Commit on `main`
```bash
# 1. Initialize local repository
git init

# 2. Ensure default branch is main
git branch -M main

# 3. Stage .gitignore and base files
git add .gitignore README.md config/ app/ tests/ docs/

# 4. Create initial commit
git commit -m "feat: initial commit with DevOps Health Monitor core architecture"

# 5. Tag baseline release
git tag -a v0.1.0 -m "Initial baseline version 0.1.0"
```

### Phase 2: Create and Switch to `dev` Branch
```bash
# Create and check out dev branch
git checkout -b dev

# Add enhancements or documentation updates
git add docs/
git commit -m "docs: add Git workflow documentation and interview question answers"
```

### Phase 3: Create Feature Branch
```bash
# Create and switch to feature branch
git checkout -b feature/enhanced-diagnostics

# Make changes to app/monitor.py or tests/
git add .
git commit -m "feat(monitor): add automated test suite and report export functionality"
```

### Phase 4: Push to GitHub & Pull Request Lifecycle
```bash
# Link remote GitHub repo (create a new empty repo on github.com first)
git remote add origin https://github.com/<YOUR_USERNAME>/devops-health-monitor.git

# Push main branch and tags
git push -u origin main --tags

# Push dev and feature branches
git push -u origin dev
git push -u origin feature/enhanced-diagnostics
```

### Phase 5: GitHub Pull Requests (Simulating Team Collaboration)
1. On GitHub, create a **Pull Request**: `feature/enhanced-diagnostics` into `dev`.
2. Review the diff, approve, and click **Merge Pull Request**.
3. Create a second **Pull Request**: `dev` into `main`.
4. Review, approve, and merge into `main`.

### Phase 6: Tagging Production Release
```bash
# Switch back to local main and pull the merged changes
git checkout main
git pull origin main

# Create production release tag
git tag -a v1.0.0 -m "Release v1.0.0: Fully tested DevOps Health Monitor CLI"

# Push tag to GitHub
git push origin v1.0.0
```
