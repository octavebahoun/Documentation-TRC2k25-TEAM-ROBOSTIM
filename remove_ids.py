import os

def remove_id(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if not lines:
        return

    new_lines = []
    in_frontmatter = False
    
    if lines[0].strip() == '---':
        in_frontmatter = True
        new_lines.append(lines[0])
        
        for i in range(1, len(lines)):
            line = lines[i]
            if line.strip() == '---':
                in_frontmatter = False
                new_lines.append(line)
                # Append rest of file
                new_lines.extend(lines[i+1:])
                break
            
            if in_frontmatter and line.strip().startswith('id:'):
                continue # Skip id line
            
            new_lines.append(line)
            
    else:
        new_lines = lines

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Processed {filepath}")

for root, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.mdx') or file.endswith('.md'):
            remove_id(os.path.join(root, file))
