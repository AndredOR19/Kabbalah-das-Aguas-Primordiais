# Repo Inventory

This file summarizes repository structure for Zencoder assistance.

- Root: /home/andre/Kabbalah-das-Aguas-Primordiais
- Notes: Large content, some duplicated trees (SCII_*, zorar-operativo), mixed assets (PDF/MD/JS/PY), and some accidental files.

## Conventions
- Keep canonical sources in their primary folders (SCII_Corpo_Do_Verbo, SCII-NEURAL, templates, zorar-operativo subfolders).
- Remove mirrors from scii_database.js/data and backup/.trashed copies.
- Exclude "Biblioteca Mística" except curated subsets noted in .gitignore.

## Cleanup Plan (applied)
- Remove clearly invalid filenames created by mistake: archiver.archive_post('URL_DO_POST'), archiver.update_index(), "<!DOCTYPE html>", UI marker files (box-drawing and emoji-titled).
- Deduplicate: prefer canonical paths listed above.
- Purge .trashed-* copies under Livro_do_Templo_Interno_1/.
- Normalize: keep templates in /templates.
