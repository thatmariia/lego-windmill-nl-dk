# LEGO Windmill NL–DK

Building instructions and BrickLink Studio model. Add or replace files in `files/` and push to `main` to update the GitHub Pages index.

After initializing or cloning the repository, enable automatic PDF compression with `git config --local core.hooksPath .githooks`. The hooks require Python 3 and Ghostscript (`brew install ghostscript` on macOS).

On commit, staged PDFs over 100 MiB are compressed while the local copies stay at full resolution.
