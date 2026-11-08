from html import escape
from pathlib import Path
from shutil import copyfile, rmtree
from urllib.parse import quote


PREVIEW_EXTENSIONS = {".avif", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".pdf", ".png", ".svg", ".webp"}


root = Path(__file__).resolve().parent
files = root / "files"
output = root / "_site"
if output.exists():
    rmtree(output)
output.mkdir()

entries = []
for source in sorted(files.rglob("*")):
    relative = source.relative_to(files)
    if not source.is_file() or any(part.startswith(".") for part in relative.parts):
        continue

    published = Path("files") / relative
    destination = output / published
    destination.parent.mkdir(parents=True, exist_ok=True)
    copyfile(source, destination)

    name = escape(relative.as_posix())
    download_url = quote(published.as_posix())
    open_link = ""
    if source.suffix.lower() in PREVIEW_EXTENSIONS:
        open_link = f'<a href="{download_url}" aria-label="Open {name}">Open</a>'

    entries.append(
        f'<li><h2>{name}</h2><p>'
        f'{open_link}'
        f'<a href="{download_url}" download aria-label="Download {name}">Download</a>'
        f'</p></li>'
    )

template = (root / "index.html").read_text(encoding="utf-8")
(output / "index.html").write_text(
    template.replace("<!-- file-list -->", "\n      ".join(entries)), encoding="utf-8"
)
