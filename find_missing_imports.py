import os
import re

components = ['InfoCard', 'FeatureGrid', 'Table', 'Alert', 'StepCard', 'CodeBlock']

for root, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.mdx') or file.endswith('.md'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for comp in components:
                # Check if component is used: <CompName
                if re.search(f'<{comp}', content):
                    # Check if component is imported: import CompName
                    if not re.search(f'import {comp}', content):
                        print(f"File {path} is missing import for {comp}")
