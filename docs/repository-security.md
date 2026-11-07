# Public repository security baseline

These controls protect a public repository that publishes agent instructions.
Repository files **cannot enforce GitHub account- or repository-level settings**.
The repository administrator must review and enable the settings below.

## Repository-local safeguards

- The validation workflow uses read-only `GITHUB_TOKEN` permissions, an explicit
  job timeout, full-length pinned GitHub Actions commit SHAs, and checkout without
  persisted credentials.
- Dependabot checks GitHub Actions versions weekly. Review and test each update;
  pin the exact new commit SHA rather than switching to a mutable tag.
- CI rejects tracked private-key and machine-local file paths. This guard checks
  filenames, **not** secret content or Git history. `.gitignore` provides another
  local barrier, not a defense against `git add -f`.
- Pull requests include a public-information and security review checklist.
- Security reports should be private; consult `.github/SECURITY.md`.

## Administrator settings to enable

1. **Protect the default branch.** In **Settings → Rules → Rulesets**, create
   an **active branch ruleset** targeting `main` with **Require a pull request
   before merging**, **Require status checks to pass** (select the existing
   `test` GitHub Actions check), **Block force pushes**, and **Restrict
   deletions**. Ensure the ruleset applies to administrators; avoid permanent
   broad bypasses. Verify with a non-destructive test that direct pushes and
   failing CI cannot merge.
2. **Keep solo maintenance possible.** An approving-review requirement is
   useful when independent reviewers exist, but a sole maintainer cannot
   approve their own PR. Choose a feasible review policy rather than
   configuring an unmergeable repository. Conversation resolution is a useful
   additional check if discussions are used.
3. **Enable secret protections.** Under **Settings → Advanced Security /
   Code security**, enable available **secret scanning**, **push protection**,
   **Dependabot alerts**, and **Dependabot security updates**. Review whether
   private vulnerability reporting is enabled, and enable it if available.
   Availability and naming may vary by plan and repository settings.
4. **Limit workflow privileges.** Under **Settings → Actions → General**,
   prefer read-only default workflow permissions and disable workflows creating
   or approving PRs unless needed. Review allowed Actions, fork approval
   settings, and active GitHub Apps/collaborators. Do not grant untrusted PR
   code write tokens or secrets.
5. **Review code scanning and security advisories.** Enable available code
   scanning for relevant languages, triage alerts, and document valid
   remediation or accepted risk. Scanning and passing CI do not guarantee
   security.
6. **Review repository history and release contents.** Run a trusted local
   secret scanner against the full Git history, not only the current tree.
   If exposed secrets are discovered, rotate/revoke them immediately; deleting
   a file or rewriting history does not revoke a credential.

## Verification after applying settings

- Verify `main` is protected and that the ruleset is **active**, not merely
  evaluated or disabled.
- Open a PR that changes only safe, non-sensitive content. Confirm its `test`
  check is required and must pass; check required review settings do not
  deadlock maintenance.
- Check a Dependabot Actions update PR is opened on its next scheduled cycle.
- Confirm secret scanning/push protection and private vulnerability reporting
  in the repository Security/Settings UI; do not assume a config file enabled them.
- Record any unavailable features or accepted exceptions. Revisit settings
  when new maintainers, GitHub Apps, workflows, or credentials are introduced.
