# Profile automation workflows

This directory contains GitHub Actions that refresh contribution statistics, activity feeds, and profile assets.

Do not add a `README.md` here. GitHub treats `.github/README.md` in a `username/username` profile repo as the profile landing page and will hide the root [`README.md`](../README.md).

---

## Workflows

- **`update_activity.yml`**: Runs on a 12-hour cron (`0 */12 * * *`) and on `workflow_dispatch`. It executes inside a `python:3.12-slim` container. `actions/checkout` is SHA-pinned.

### Branching model: `develop` → `master`

This repo runs an unattended develop→master pipeline, with no manual review step:

1. **Validate** — the job checks out `develop` and byte-compiles `update_github_activity.py`, `download_badges.py`, and `design_tokens.py` (`python -m py_compile`). If validation fails, the job stops here — nothing is committed or promoted.
2. **Generate + commit to `develop`** — `update_github_activity.py` regenerates `README.md` and the `assets/stat-overview.svg` / `assets/stat-languages.svg` / `assets/stat-heatmap.svg` badges, and the changes are committed and pushed to `develop` (not `master`) as `github-actions[bot]`.
3. **Promote to `master`** — once the `develop` commit lands, the same job fast-forwards `master` to that commit (`git merge --ff-only`) and pushes it. This is a straight fast-forward, never a force-push; if `develop` and `master` have diverged such that a fast-forward isn't possible, the job fails loudly instead of overwriting history.

**`master` is the branch that actually renders as the public [github.com/knownassurajit](https://github.com/knownassurajit) profile page.** `develop` is where the bot's generated commits land first and pass validation before being promoted.
