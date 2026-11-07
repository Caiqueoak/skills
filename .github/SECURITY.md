# Security policy

This is a public repository of reusable agent instructions and optional helper
scripts. Treat any installed skill or script as code: inspect changes before
running them, especially when granting tools or local file permissions.

## Reporting a vulnerability

**Report security issues privately.** If GitHub private vulnerability reporting
is enabled, use the repository's **Security → Advisories → Report a
vulnerability** flow. If that option is unavailable, contact the maintainer
through an established private channel; do not publish exploit details or
sensitive data in an issue or pull request.

Do not include real credentials, access tokens, confidential materials,
workplace information, or personal data in reports, test cases, or reproduction
artifacts. Revoke or rotate any credential that may already have been exposed.

## Supported versions and fixes

The default branch is the maintained source. Fixes are reviewed and released
through normal repository changes. No security response deadline or support for
older versions is guaranteed.

## Scope

Security reports may concern agent instruction handling, unsafe tool access,
optional scripts, installation behavior, or information exposure. Tool/agent
permissions and private extensions depend on the environment where skills are
installed; repository instructions alone do not form a security boundary.
