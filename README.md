# PE Plugins marketplace

A Claude plugin marketplace containing **pe-lp-accounting**: end-to-end investor-side private equity accounting, reporting and IFRS compliance.

## Repository layout

```
.claude-plugin/marketplace.json        Marketplace catalogue
plugins/pe-lp-accounting/
  .claude-plugin/plugin.json           Plugin manifest
  skills/<12 skills>/SKILL.md
  commands/<43 commands>.md
  references/                          Policies, journals, taxonomy, controls
  scripts/pe_calcs.py                  Calculations
  templates/                           CSV schemas
  tests/                               Unit tests
```

## Publish on GitHub

```bash
git init
git add .
git commit -m "PE LP accounting plugin v1.0.0"
git branch -M main
git remote add origin https://github.com/<your-org>/<repo-name>.git
git push -u origin main
```

A private repository works for your organisation as long as users have access to it.

## Install in Claude Code

```
/plugin marketplace add <your-org>/<repo-name>
/plugin install pe-lp-accounting@pe-plugins
```

## Install in the Claude app (organisation)

An organisation owner can add the GitHub repository as a plugin marketplace in the organisation's plugin settings and enable `pe-lp-accounting` for members. Alternatively, upload the plugin folder as a zip where your plan supports custom plugin uploads.

## Update

Bump `version` in both `marketplace.json` and `plugin.json`, push, then run `/plugin marketplace update pe-plugins`.

## Test

```bash
python3 -m unittest discover -s plugins/pe-lp-accounting/tests -v
```
