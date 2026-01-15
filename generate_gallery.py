import os

gallery_dir = 'source/gallery'
output_file = 'source/_data/gallery.yml'

extensions = {'.jpg', '.jpeg', '.png', '.gif'}
entries = []

for filename in sorted(os.listdir(gallery_dir)):
    if any(filename.lower().endswith(ext) for ext in extensions):
        # Format: /gallery/filename
        full_link = f'/gallery/{filename}'
        # Use filename as description for now, removing extension
        descr = os.path.splitext(filename)[0]
        entry = f"""- full_link: {full_link}
  descr: "{descr}"
"""
        entries.append(entry)

with open(output_file, 'w') as f:
    f.writelines(entries)

print(f"Generated {len(entries)} entries in {output_file}")
