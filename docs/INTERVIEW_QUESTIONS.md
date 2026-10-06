# DevOps Internship Task 4: Interview Questions & Answers

### 1. What is Git?
**Git** is a distributed version control system (DVCS) designed to track changes in source code over time. Unlike centralized VCS (like SVN), every developer has a full copy of the entire repository history locally. This enables offline work, fast branching and merging, high data integrity via SHA-1/SHA-256 cryptographic hashing, and collaborative development across teams.

---

### 2. What is the difference between merge and rebase?
| Feature | `git merge` | `git rebase` |
| :--- | :--- | :--- |
| **Commit History** | Preserves complete history with a dedicated merge commit. | Rewrites commit history linearly by replaying commits on top of another branch. |
| **History Shape** | Branched, non-linear history graph. | Completely straight, linear commit history. |
| **Traceability** | Easy to see when branches were integrated. | Cleaner `git log`, but original commit hashes and dates change. |
| **Rule of Thumb** | Best for shared/public branches (`main`, `dev`). | Best for cleaning up local personal feature branches before merging. |

---

### 3. What is a pull request?
A **Pull Request (PR)** (or Merge Request in GitLab) is an event in a Git hosting platform (such as GitHub) where a developer notifies team members that they have completed a feature or bug fix and requests that their changes be reviewed and merged from a head branch (e.g., `feature/xyz`) into a target base branch (e.g., `dev` or `main`). PRs provide:
- Peer code review and threaded comments.
- Automated CI/CD test and linting validation.
- Audit trail for approvals and discussions.

---

### 4. How do you resolve merge conflicts?
A merge conflict occurs when Git cannot automatically reconcile differences between two commits (usually when the same line of code is edited differently in two branches).

**Resolution steps:**
1. **Identify conflicted files:** Run `git status` to see files marked `both modified`.
2. **Open the file:** Inspect conflict markers:
   ```text
   <<<<<<< HEAD (Current branch)
   Disk Threshold: 85%
   =======
   Disk Threshold: 90%
   >>>>>>> feature/new-thresholds (Incoming branch)
   ```
3. **Decide and edit:** Keep desired changes and remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
4. **Stage the resolved files:** Run `git add <filename>`.
5. **Complete the merge:** Run `git commit -m "chore: resolve merge conflict between dev and feature"` or `git rebase --continue`.

---

### 5. What are Git tags?
**Git tags** are reference pointers to specific commits in Git history, most commonly used to mark release milestones (e.g., `v1.0.0`, `v2.1.0` following Semantic Versioning).
- **Lightweight tags:** Simple pointer directly to a commit (`git tag v1.0.0`).
- **Annotated tags:** Stored as full objects in the Git database with tagger name, email, date, GPG signature, and a release message (`git tag -a v1.0.0 -m "Release version 1.0.0"`).

---

### 6. What is a Git workflow?
A **Git workflow** is a set of team conventions and branching strategies outlining how team members use Git to develop, review, test, and release software. Common workflows include:
- **Git Flow:** Strict branching model featuring `main` (production), `develop` (integration), `feature/*`, `release/*`, and `hotfix/*`.
- **GitHub Flow:** Lightweight, trunk-based workflow with `main` always deployable, short-lived feature branches, and Pull Requests.
- **Trunk-Based Development:** Developers merge small, frequent updates into a single shared branch.

---

### 7. Explain `git stash`.
`git stash` temporarily shelves (or stashes) uncommitted changes (both staged and unstaged tracked files) in a dirty working directory, returning the working directory to the clean `HEAD` state without committing unfinished work.
- `git stash push -m "work in progress"`: Stashes current changes with a description.
- `git stash list`: Lists all stashed snapshots.
- `git stash pop`: Re-applies the most recent stashed changes and drops it from the stash stack.
- `git stash apply`: Re-applies the stash without removing it from the stash list.

---

### 8. What is the use of `.gitignore`?
A `.gitignore` file specifies intentionally untracked files and patterns that Git should ignore and not stage. It prevents:
- Committing temporary build artifacts and compiler binaries.
- Storing local configuration and secrets (`.env`, private keys).
- Bloating repository size with dependencies (`node_modules/`, `venv/`).
- Committing operating system clutter (`.DS_Store`, `Thumbs.db`).
