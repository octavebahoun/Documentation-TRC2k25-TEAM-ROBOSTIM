import os
import re

components = {
    'InfoCard': '@site/src/components/InfoCard',
    'FeatureGrid': '@site/src/components/FeatureGrid',
    'Table': '@site/src/components/Table',
    'StepCard': '@site/src/components/StepCard',
    'CodeBlock': '@site/src/components/CodeBlock'
}

def add_imports(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    if not lines:
        return

    # Detect frontmatter
    frontmatter_end_idx = -1
    if lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                frontmatter_end_idx = i
                break
    
    # Determine insertion point
    insert_idx = 0
    if frontmatter_end_idx != -1:
        insert_idx = frontmatter_end_idx + 1
    
    # Find active imports
    existing_imports = set()
    for line in lines:
        match = re.search(r'import\s+(\w+)\s+from', line)
        if match:
            existing_imports.add(match.group(1))

    # Identify needed imports
    imports_to_add = []
    for comp, path in components.items():
        # Check usage (naive check, assumes <Comp)
        if f'<{comp}' in content:
            if comp not in existing_imports:
                imports_to_add.append(f"import {comp} from '{path}';")

    if not imports_to_add:
        return

    # Insert imports
    # Add a newline before imports if inserting after frontmatter
    insert_lines = []
    if frontmatter_end_idx != -1:
         insert_lines.append('')
    
    insert_lines.extend(imports_to_add)
    
    # Add newline after imports if not present
    if insert_idx < len(lines) and lines[insert_idx].strip() != '':
        insert_lines.append('')

    new_lines = lines[:insert_idx] + insert_lines + lines[insert_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines) + '\n')
    
    print(f"Updated {filepath} with imports: {imports_to_add}")

for root, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.mdx') or file.endswith('.md'):
            add_imports(os.path.join(root, file))
