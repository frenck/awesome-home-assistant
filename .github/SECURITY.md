# Security policy

Thanks for taking the time to help keep Awesome Home Assistant safe for
its readers. We take security seriously -- not just for the repository
itself, but also for the third-party links we curate.

## Reporting a vulnerability

**Please do not file public issues for security reports.**

Use GitHub's private vulnerability reporting instead:

> [Report a vulnerability](https://github.com/frenck/awesome-home-assistant/security/advisories/new)

If you cannot use GitHub for any reason, email
[security@frenck.dev](mailto:security@frenck.dev) instead. Please use the same
inbox for follow-up correspondence on a report.

When reporting, please include:

- A clear description of the issue and its impact.
- The URL or section of the repository involved (e.g. a specific link, a
  workflow file, or `awesome-ha.com`).
- Reproduction steps where applicable.
- Any proof-of-concept material -- screenshots, logs, recordings.

If you would like updates encrypted, attach a PGP key with your first message
and we will reply in kind.

## What's in scope

Reports are welcome on any of the following:

- **Malicious link contributions** -- a previously-merged link that now
  resolves to phishing, malware, drive-by downloads, cryptominers, or
  similarly hostile content.
- **Compromised upstream targets** -- a project we link to that has been
  taken over (typo-squat, account compromise, malicious release, hostile
  fork promoted as the original) and is actively distributing malware to
  Home Assistant users.
- **Repository or workflow vulnerabilities** -- supply-chain weaknesses in
  this repo's own GitHub Actions workflows, build pipeline, or generated
  site (`awesome-ha.com`).
- **Account or credential exposure** in the repo (leaked tokens in
  history, accidental secret exposure, etc.).

## What's out of scope

The following are not handled through this process:

- **Vulnerabilities in linked third-party projects themselves.** Report
  those upstream to the project's own maintainers; we are not in a
  position to fix software we do not own. We will, however, remove or
  flag links once an upstream issue is publicly known.
- **Vulnerabilities in Home Assistant Core.** Report those to the
  Home Assistant project at
  <https://www.home-assistant.io/security/> or
  [security@home-assistant.io](mailto:security@home-assistant.io).
- **Dependency advisories** in `requirements.txt` -- those are handled by
  Renovate / Dependabot and the dependency-review workflow on every PR.
- **Stale links or 404s** -- those are link rot, not security issues. The
  weekly link-check workflow files an issue when it spots them.
- **Style, formatting, or editorial complaints** about linked
  third-party projects.

## Supported versions

This is a curated list, not a versioned product. Only the `main` branch
and the rendered site at <https://awesome-ha.com> are supported. If a
report relates to historical content from a specific commit or release
tag, please mention the commit SHA explicitly.

| Branch | Supported |
| ------ | --------- |
| `main` | Yes |
| Other  | No  |

## Response timeline

We aim to:

- **Acknowledge** every valid report within **48 hours**.
- **Provide an initial assessment** within **7 days** of acknowledgement.
- **Resolve or publish guidance** within **90 days** of the initial
  report. Some upstream-driven issues may take longer -- if so, we will
  keep you updated.

If 90 days pass with no resolution, you are welcome to publicly disclose
the issue at your discretion. We will not pursue legal action against
researchers who follow this policy in good faith.

## Coordinated disclosure

Once a report is validated:

1. We work to remove or remediate the offending content as quickly as
   possible. For malicious link contributions this is usually within
   hours; for upstream-compromise reports it depends on how the upstream
   project responds.
2. We may publish a GitHub Security Advisory describing the issue, with
   credit to the reporter (unless you prefer to remain anonymous).
3. We may notify directly affected users where reasonably possible -- for
   example, by pinging the issue tracker of a previously-listed project
   that was taken over.

Thank you for helping keep this list safe.
