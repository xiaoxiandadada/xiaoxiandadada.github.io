import os
import time

def add_front_matter(filepath, category):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if content.startswith('---'):
        # Already has front matter, check if it has categories
        # For simplicity, we assume if it has FM we might just append/check.
        # But user files seemed to have NO FM based on GRM.md check.
        # If it has FM, we might need to inject category.
        lines = content.split('\n')
        # Check if categories exists
        has_cat = False
        for line in lines[:20]: # Check first 20 lines
            if line.strip().startswith('categories:'):
                has_cat = True
                break
        if not has_cat:
            # Insert categories after date or at end of FM
            # Finding second ---
            try:
                second_dash_idx = content.find('\n---', 3)
                if second_dash_idx != -1:
                    new_content = content[:second_dash_idx] + f'\ncategories: [{category}]' + content[second_dash_idx:]
                    with open(filepath, 'w') as f:
                        f.write(new_content)
                    print(f"Updated {filepath} with category {category}")
            except:
                pass
        return

    # No Front matter, add it
    filename = os.path.basename(filepath)
    title = os.path.splitext(filename)[0].replace('-', ' ').title()
    
    # Try to find a # Header for title
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
            
    date_str = time.strftime("%Y-%m-%d %H:%M:%S")
    
    front_matter = f"""---
title: {title}
date: {date_str}
categories: [{category}]
---
"""
    new_content = front_matter + content
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Added front matter to {filepath}")

def process_dir(directory, category):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                add_front_matter(filepath, category)

process_dir('source/_posts/GWAS', 'GWAS')
process_dir('source/_posts/DL', 'DL-notes')
