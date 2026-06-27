import os
import re

# Map month numbers to Chinese
MONTH_MAP = {
    "01": "一月", "02": "二月", "03": "三月", "04": "四月",
    "05": "五月", "06": "六月", "07": "七月", "08": "八月",
    "09": "九月", "10": "十月", "11": "十一月", "12": "十二月"
}

def extract_title(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    title = line.strip("# \n")
                    return title
    except Exception:
        pass
    return os.path.basename(filepath)

def to_toml_val(val):
    if isinstance(val, str):
        # Escape backslashes and double quotes
        escaped = val.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    elif isinstance(val, list):
        items = [to_toml_val(x) for x in val]
        return "[" + ", ".join(items) + "]"
    elif isinstance(val, dict):
        parts = []
        for k, v in val.items():
            parts.append(f'"{k}" = {to_toml_val(v)}')
        return "{ " + ", ".join(parts) + " }"
    return str(val)

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
            if month_name not in data[year]:
                data[year][month_name] = []
                
            data[year][month_name].append((filename, title))

    # Sort logic: newest first
    nav = []
    
    # Sort years descending
    for year in sorted(data.keys(), reverse=True):
        year_nav = []
        months_in_year = data[year]
        
        # Sort months descending
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

    # Generate TOML manually
    toml_lines = [
        "[project]",
        f'site_name = "AIToBox WeeklyNews"',
        f'site_description = "记录每周值得分享的AI资讯、好用的工具和服务，周六发布。"',
        f'site_author = "AIToBox"',
        f'site_url = "https://newsweekly.aitobox.com/"',
        f'nav = {to_toml_val(nav)}',
        "",
        "[project.theme]",
        f'variant = "modern"',
        f'features = ["navigation.sections", "navigation.top"]'
    ]

    with open("zensical.toml", "w", encoding="utf-8") as f:
        f.write("\n".join(toml_lines) + "\n")
    print("zensical.toml generated successfully without external dependencies.")

    # Copy root README.md to docs/index.md, adjusting internal links
    readme_path = "README.md"
    index_path = os.path.join(docs_dir, "index.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
        # Change links pointing to docs/AIToBoxWeeklyNews_*.md to AIToBoxWeeklyNews_*.md since index.md is in docs/
        adjusted_content = readme_content.replace("docs/AIToBoxWeeklyNews_", "AIToBoxWeeklyNews_")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(adjusted_content)
        print("Generated docs/index.md from README.md with adjusted paths.")

if __name__ == "__main__":
    main()
