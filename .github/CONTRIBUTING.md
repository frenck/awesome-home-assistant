# Contribution Guidelines

Your contributions are always welcome! Thank you for your suggestions! :smiley:

Please note that this project is released with a
[Contributor Code of Conduct](https://github.com/frenck/awesome-home-assistant/blob/main/.github/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.

Contributing is pretty easy, all you need is a GitHub account.

[Just click this link to edit the list, right from your browser](https://github.com/frenck/awesome-home-assistant/edit/main/README.md).

## Acceptance criteria

Every entry on this list **must** meet the criteria below. Pull requests that
add or update entries are checked automatically; CI will block PRs that fail
any hard requirement and post warnings for soft ones.

### Universal — every entry

- The URL **must** be reachable. Lychee runs on every PR; broken links are
  rejected.
- The URL **must** use HTTPS. No plain `http://`.
- The URL **must not** be a shortener (e.g. `bit.ly`, `t.co`, `goo.gl`,
  `tinyurl.com`, `ow.ly`, `is.gd`). Shortener services routinely shut down
  and take their URLs with them — link to the canonical URL instead.
- The URL **must not** already be listed elsewhere in this README.
- Common tracking parameters (`utm_*`, `fbclid`, `gclid`, `mc_eid`) **should**
  be stripped from the URL before submitting. CI will warn if they're present.

### Software entries (GitHub repositories)

Applies to: **Apps** (Official + Third Party), **Custom Integrations**,
**Dashboards** (Custom Cards, Themes, Alternative Dashboards), **DIY** entries
that link to a code repository, and **Alternative Home Automation Software**.

The repository **must**:

- Not be archived.
- Have been pushed to within the last **18 months**.
- Be at least **6 months old** (created at least 6 months before submission).
- Have a `README.md` at the repository root.
- Be released under an [OSI-approved](https://opensource.org/licenses)
  open-source license. Proprietary, "Other", and source-available licenses
  (Elastic-2.0, BSL, SSPL, Commons Clause) are not accepted.

The repository **should** mention "Home Assistant" in its `README.md`.
This is a CI warning, not a blocker — for general-purpose libraries that
happen to be used by HA integrations the warning can be acknowledged in the
PR description.

A soft warning is also shown for repositories with **fewer than 10 stars**
at the time of submission. Submit anyway, but explain in the PR description
why this niche or new tool meets the "widely recommended" bar.

### HACS-installable entries

Applies to: **Custom Integrations** and **Dashboards › Custom Cards**.

The repository **must** ship a valid `hacs.json` so users can install through
[HACS](https://hacs.xyz). For Custom Cards / Lovelace plugins this typically
means:

```json
{
  "name": "My Card",
  "filename": "my-card.js",
  "render_readme": true
}
```

For Custom Integrations, `hacs.json` plus a valid `manifest.json` under
`custom_components/<domain>/`.

If the project genuinely cannot be HACS-installed (e.g. it's a CLI tool that
sits alongside HA), it probably belongs in the Uncategorized section, not
under Custom Integrations.

### Content entries (blogs, podcasts, YouTube channels)

Applies to: **Blogs**, **Podcasts**, **YouTube Channels**.

The publication **must** have a new post / episode / video within the last
**12 months**. Stale = abandoned for content; if the author resumes, the
entry can be re-added at that point.

### Section-specific exemptions

- **Public Configurations** — license check waived. Most are personal HA
  configs without an explicit license; that's expected.
- **DIY Projects** that link to a forum thread or blog post (not a code
  repository) — only the universal URL checks apply. The HA-mention check is
  also waived since the link target isn't a repo.
- **Other Awesome Lists** — accepts Creative Commons licenses (CC-BY, CC0,
  CC-BY-SA) in addition to OSI-approved licenses, since these are content
  curation works rather than software.

### Subjective — manual review

These can't be checked automatically. Reviewers will look for:

- Widely recommended regardless of personal opinion.
- Well known or discussed within the community.
- Written in English.
- Not self-promotion. CI flags PRs where the author's GitHub account matches
  the linked repository's owner; if that's you, please explain in the PR
  description why this entry is awesome.

## Adding a new link

- **Make an individual pull request for each link suggestion.**
- Search previous suggestions before making a new one — yours may be a duplicate.
- Use the following format:

  ```text
  - [project-name](https://example.com/) - A short description ends with a period.
  ```

  - Keep the description short and simple, but descriptive.
  - A description ends with a full stop / period `.`.
  - The description **must not** start with the item name (e.g. "Foo" → "A useful tool…", not "Foo is a useful tool…").
  - Don't mention "Home Assistant" in the description — it's implied.
- Check your spelling and grammar.
- Position your suggestion as the **last item** in the relevant category.

## Adding a new section / category

New categories or improvements to the existing categorization are welcome.

- Ensure the section has a nice description.
- A description ends with a full stop / period `.`.
- Add the section to the table of contents.
- Check your spelling and grammar.
- Remove any trailing whitespace.

## Deleting a link

Typical reasons for deleting links:

- The item no longer applies to or works with current Home Assistant.
- No updates / abandoned upstream (fails the activity-window checks).
- Deprecated.
- License missing or no longer open source.
- Dead link.
- Project taken over and now distributing malware or content unrelated to its
  original purpose. See [SECURITY.md](./SECURITY.md).
