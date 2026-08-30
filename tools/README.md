# Build / import tools

## Import baseline GSM Laboratory

The supplied GSM Laboratory archive is the source baseline for this project. Run from the repository root:

```powershell
python tools/import_gsm_baseline.py "C:\path\MTK GSM LABORATORY.zip"
```

The importer places reusable Python/Qt source under `mtk/`, rewrites internal imports from `mtkclient` to `mtk`, and excludes payload/exploit modules used for security bypass. Authentication/security bypass is intentionally external to this project; MCT may be used separately before normal DA/flash operations.

## Runtime

```powershell
python -m pip install -r requirements.txt
```

After import, test the GUI and MTK transport from the repository root. Keep device firmware, private loaders, auth files, and personal data outside the public repository.
