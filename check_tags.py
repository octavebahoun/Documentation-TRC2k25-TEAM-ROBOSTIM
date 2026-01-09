import os
import re

tags = ['InfoCard', 'FeatureGrid', 'Table', 'StepCard']

def is_inside_code_block(content, pos):
    # Compter le nombre de triple backticks avant pos
    before = content[:pos]
    matches = re.findall(r'```', before)
    return len(matches) % 2 != 0

for root, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.mdx') or file.endswith('.md'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for tag in tags:
                for match in re.finditer(f'<{tag}', content):
                    if not is_inside_code_block(content, match.start()):
                        # Tag is outside code block. check if imported.
                        if not re.search(f'import {tag}', content):
                            print(f"ERROR: {path} uses <{tag} outside code block without import at pos {match.start()}")
