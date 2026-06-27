# Design Spec: AIToBox WeeklyNews Zensical Migration

This specification details the plan to migrate the existing document collection of AIToBox weekly AI news files (in `docs/`) into a static site using the **Zensical** documentation system, automated with a navigation generator script and deployed via GitHub Actions.

## 1. Directory & Document Restructuring

We will rename the files in `docs/` to follow the standard pattern: `AIToBoxWeeklyNews_YYYYMMDD.md`.

### 1.1 File Renaming Mapping
Using first Git commit dates, the files will be renamed as follows:
* `docs/issue-001.md` (2024-01-07) -> `docs/AIToBoxWeeklyNews_20240107.md`
* `docs/issue-002.md` (2024-01-12) -> `docs/AIToBoxWeeklyNews_20240112.md`
* `docs/issue-003.md` (2024-01-19) -> `docs/AIToBoxWeeklyNews_20240119.md`
* `docs/issue-004.md` (2024-01-26) -> `docs/AIToBoxWeeklyNews_20240126.md`
* `docs/issue-005.md` (2024-02-04) -> `docs/AIToBoxWeeklyNews_20240204.md`
* `docs/issue-006.md` (2024-02-22) -> `docs/AIToBoxWeeklyNews_20240222.md`
* `docs/issue-007.md` (2024-03-09) -> `docs/AIToBoxWeeklyNews_20240309.md`
* `docs/issue-008.md` (2024-03-28) -> `docs/AIToBoxWeeklyNews_20240328.md`
* `docs/issue-009.md` (2024-04-19) -> `docs/AIToBoxWeeklyNews_20240419.md`
* `docs/issue-010.md` (2024-05-19) -> `docs/AIToBoxWeeklyNews_20240519.md`
* `docs/issue-011.md` (2024-06-14) -> `docs/AIToBoxWeeklyNews_20240614.md`
* `docs/issue-012.md` (2024-07-28) -> `docs/AIToBoxWeeklyNews_20240728.md`
* `docs/issue-013.md` (2024-08-25) -> `docs/AIToBoxWeeklyNews_20240825.md`
* `docs/issue-014.md` (2024-09-14) -> `docs/AIToBoxWeeklyNews_20240914.md`
* `docs/issue-015.md` (2024-10-27) -> `docs/AIToBoxWeeklyNews_20241027.md`
* `docs/issue-016.md` (2024-11-29) -> `docs/AIToBoxWeeklyNews_20241129.md`
* `docs/issue-017.md` (2024-12-29) -> `docs/AIToBoxWeeklyNews_20241229.md`
* `docs/issue-018.md` (2025-01-25) -> `docs/AIToBoxWeeklyNews_20250125.md`
* `docs/issue-019.md` (2025-03-25) -> `docs/AIToBoxWeeklyNews_20250325.md`
* `docs/issue-020.md` (2025-04-30) -> `docs/AIToBoxWeeklyNews_20250430.md`
* `docs/issue-021.md` (2025-05-23) -> `docs/AIToBoxWeeklyNews_20250523.md`
* `docs/issue-022.md` (2026-05-22) -> `docs/AIToBoxWeeklyNews_20260522.md`
* `docs/issue-023.md` (2026-06-02) -> `docs/AIToBoxWeeklyNews_20260602.md`
* `docs/issue-024.md` (2026-06-07) -> `docs/AIToBoxWeeklyNews_20260607.md`
* `docs/issue-025.md` (2026-06-14) -> `docs/AIToBoxWeeklyNews_20260614.md`
* `docs/AIToBox周刊_20260621.md` -> `docs/AIToBoxWeeklyNews_20260621.md`
* `docs/AIToBox周刊_20260627.md` -> `docs/AIToBoxWeeklyNews_20260627.md`

### 1.2 References Update
* The main `README.md` will be updated to point to the new paths.
* Any self-references (e.g. image paths in `AIToBoxWeeklyNews_20240107.md`) will remain resolved since the parent directory `images/issue-001/` remains intact.

## 2. Zensical Configuration & Navigation Script

### 2.1 Navigation Structure Requirements
* Group issues by Year (e.g. `2026`, `2025`, `2024`).
* Group issues within each Year by Month (Chinese names like `一月`, `二月`, etc.).
* Sort items chronologically by date descending (**newest first**).

### 2.2 Navigation Generation Script (`scripts/generate_nav.py`)
A Python script will:
1. Scan the `docs/` folder for `AIToBoxWeeklyNews_*.md`.
2. Extract the date from each filename (`YYYYMMDD`).
3. Read the first heading (`# AIToBox周刊：...` or `# AIToBox周刊：第 X 期`) from each markdown file to determine its display title.
4. Construct a nested navigation tree grouped by Year (descending) -> Month (descending) -> Issue (descending).
5. Load the base `zensical.toml` parameters and output the complete configured TOML to `zensical.toml`.

### 2.3 Base Config (`zensical.toml.template` or base config in Python)
The base configuration parameters:
```toml
[project]
site_name = "AIToBox WeeklyNews"
site_description = "记录每周值得分享的AI资讯、好用的工具和服务，周六发布。"
site_author = "AIToBox"
site_url = "https://aitobox.github.io/newsweekly/"

[project.theme]
variant = "modern"
features = ["navigation.sections", "navigation.top"]
```

## 3. GitHub Actions CI/CD Deployment

We will add `.github/workflows/deploy.yml`:
```yaml
name: Deploy Zensical Site to GitHub Pages

on:
  push:
    branches:
      - main
      - master

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Generate Navigation
        run: |
          python scripts/generate_nav.py

      - name: Install Zensical
        run: |
          pip install zensical

      - name: Build Zensical Site
        run: |
          zensical build

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload Artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'site'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```
