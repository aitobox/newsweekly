# Zensical Site Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate AIToBox weekly newsletter files to Zensical document system with automated navigation sorting (newest first) by Year and Month.

**Architecture:** Use a Python-based utility script to dynamically parse file dates from `docs/AIToBoxWeeklyNews_*.md` and update `zensical.toml` before building. Execute CI/CD builds with GitHub Actions.

**Tech Stack:** Python 3, Zensical (pip), YAML, Git.

## Global Constraints

- Rename all `docs/issue-*.md` files to `docs/AIToBoxWeeklyNews_YYYYMMDD.md` using the first Git commit date.
- Rename `docs/AIToBox周刊_*.md` to `docs/AIToBoxWeeklyNews_*.md`.
- Navigation must group by Year (descending) -> Month (descending) -> Issue (descending).
- Site URL: `https://aitobox.github.io/newsweekly/`.

---

### Task 1: Rename Files and Update References

**Files:**
- Create: `scripts/rename_issues.py`
- Modify: `README.md`

**Interfaces:**
- Consumes: Existing files in `docs/` and git repository history.
- Produces: Renamed markdown files and updated references in `README.md`.

- [ ] **Step 1: Write the renaming script**
  Create `scripts/rename_issues.py` with the following content:
  ```python
  import os
  import subprocess
  import re

  def get_first_commit_date(filepath):
      try:
          output = subprocess.check_output(
              ["git", "log", "--diff-filter=A", "--format=%ad", "--date=short", "--", filepath],
              text=True
          )
          date_str = output.strip().split('\n')[0]
          return date_str.replace("-", "")
      except Exception as e:
          print(f"Error getting date for {filepath}: {e}")
          return None

  def main():
      docs_dir = "docs"
      readme_path = "README.md"
      
      # Read README
      with open(readme_path, "r", encoding="utf-8") as f:
          readme_content = f.read()

      # Track renaming map for updating README
      rename_map = {}

      # List files
      files = os.listdir(docs_dir)
      
      # 1. Handle issue-*.md
      issue_files = sorted([f for f in files if re.match(r"^issue-\d+\.md$", f)])
      for f in issue_files:
          filepath = os.path.join(docs_dir, f)
          date_suffix = get_first_commit_date(filepath)
          if date_suffix:
              new_name = f"AIToBoxWeeklyNews_{date_suffix}.md"
              rename_map[f] = new_name

      # 2. Handle AIToBox周刊_*.md
      cn_files = [f for f in files if f.startswith("AIToBox周刊_") and f.endswith(".md")]
      for f in cn_files:
          # Extract YYYYMMDD from AIToBox周刊_YYYYMMDD.md
          m = re.match(r"^AIToBox周刊_(\d{8})\.md$", f)
          if m:
              new_name = f"AIToBoxWeeklyNews_{m.group(1)}.md"
              rename_map[f] = new_name

      # Execute renaming
      for old_name, new_name in rename_map.items():
          old_path = os.path.join(docs_dir, old_name)
          new_path = os.path.join(docs_dir, new_name)
          print(f"Renaming {old_path} -> {new_path}")
          os.rename(old_path, new_path)

          # Update README references
          readme_content = readme_content.replace(f"docs/{old_name}", f"docs/{new_name}")

      with open(readme_path, "w", encoding="utf-8") as f:
          f.write(readme_content)

  if __name__ == "__main__":
      main()
  ```

- [ ] **Step 2: Run the renaming script**
  Run: `python scripts/rename_issues.py`
  Expected output: Renamed files in `docs/` and modified `README.md`.

- [ ] **Step 3: Verify output files exist**
  Run: `ls docs/AIToBoxWeeklyNews_*.md | wc -l`
  Expected: `27` files.

- [ ] **Step 4: Commit changes**
  Run:
  ```bash
  git add docs/AIToBoxWeeklyNews_*.md README.md
  git status # ensure no untracked old files left untracked
  git commit -m "refactor: rename issue files to AIToBoxWeeklyNews pattern and update README"
  ```

---

### Task 2: Implement Zensical Base Configuration and Navigation Generator

**Files:**
- Create: `scripts/generate_nav.py`
- Create: `zensical.toml`

**Interfaces:**
- Consumes: Renamed `docs/AIToBoxWeeklyNews_*.md` files.
- Produces: `zensical.toml` containing correct navigation data.

- [ ] **Step 1: Write the navigation generator script**
  Create `scripts/generate_nav.py` with the following content:
  ```python
  import os
  import re
  import toml

  # Map month numbers to Chinese
  MONTH_MAP = {
      "01": "一月", "02": "二月", "03": "三月", "04": "四月",
      "05": "五月", "06": "六月", "07": "七月", "08": "八月",
      "09": "九月", "10": "十月", "11": "十一月", "12": "十二月"
  }

  def extract_title(filepath):
      # Try to read the main header from the file content
      try:
          with open(filepath, "r", encoding="utf-8") as f:
              for line in f:
                  if line.startswith("# "):
                      title = line.strip("# \n")
                      # Clean up common title patterns if needed
                      return title
      except Exception:
          pass
      return os.path.basename(filepath)

  def main():
      docs_dir = "docs"
      pattern = re.compile(r"^AIToBoxWeeklyNews_(\d{4})(\d{2})\d{2}\.md$")
      
      # Grouping structure: { year: { month: [ (filename, display_title) ] } }
      data = {}
      
      for filename in os.listdir(docs_dir):
          m = pattern.match(filename)
          if m:
              year = m.group(1)
              month_num = m.group(2)
              month_name = MONTH_MAP.get(month_num, f"{month_num}月")
              
              filepath = os.path.join(docs_dir, filename)
              title = extract_title(filepath)
              
              if year not in data:
                  data[year] = {}
              if month_name not in data:
                  data[year][month_name] = []
                  
              data[year][month_name].append((filename, title))

      # Sort logic: newest first
      nav = []
      
      # Sort years descending
      for year in sorted(data.keys(), reverse=True):
          year_nav = []
          
          # Sort months descending (need mapping to numerical month to sort correctly)
          # We reverse-map month name to number to sort
          months_in_year = data[year]
          sorted_months = sorted(
              months_in_year.keys(),
              key=lambda m: [k for k, v in MONTH_MAP.items() if v == m][0] if m in MONTH_MAP.values() else m,
              reverse=True
          )
          
          for month in sorted_months:
              month_nav = []
              # Sort issues inside month by filename descending
              issues = sorted(months_in_year[month], key=lambda x: x[0], reverse=True)
              for filename, title in issues:
                  month_nav.append({title: filename})
              year_nav.append({month: month_nav})
              
          nav.append({year: year_nav})

      # Base config
      config = {
          "project": {
              "site_name": "AIToBox WeeklyNews",
              "site_description": "记录每周值得分享的AI资讯、好用的工具和服务，周六发布。",
              "site_author": "AIToBox",
              "site_url": "https://aitobox.github.io/newsweekly/",
              "nav": nav,
              "theme": {
                  "variant": "modern",
                  "features": ["navigation.sections", "navigation.top"]
              }
          }
      }

      with open("zensical.toml", "w", encoding="utf-8") as f:
          toml.dump(config, f)
      print("zensical.toml generated successfully.")

  if __name__ == "__main__":
      main()
  ```

- [ ] **Step 2: Run the script to generate `zensical.toml`**
  Run: `python scripts/generate_nav.py`
  Expected output: `zensical.toml generated successfully.`

- [ ] **Step 3: Verify generated `zensical.toml`**
  Run: `cat zensical.toml`
  Expected: Valid TOML with `[project]` settings and nested navigation tree sorted descending.

- [ ] **Step 4: Commit scripts and config**
  Run:
  ```bash
  git add scripts/generate_nav.py zensical.toml
  git commit -m "feat: implement dynamic navigation generator and basic zensical config"
  ```

---

### Task 3: CI/CD GitHub Actions Deployment Workflow

**Files:**
- Create: `.github/workflows/deploy.yml`

- [ ] **Step 1: Create the workflow file**
  Create `.github/workflows/deploy.yml` with the following content:
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

        - name: Install dependencies
          run: |
            pip install toml zensical

        - name: Generate Navigation
          run: |
            python scripts/generate_nav.py

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

- [ ] **Step 2: Commit workflow**
  Run:
  ```bash
  git add .github/workflows/deploy.yml
  git commit -m "ci: add GitHub Actions workflow to auto-deploy site"
  ```
