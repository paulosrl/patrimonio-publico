import re

with open('01-Introducao-IA-Patrimonio-Publico-Paulo-Lima.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract <style> block
style_match = re.search(r'<style>(.*?)</style>', text, re.DOTALL)
style_content = style_match.group(1) if style_match else ''

# Extract all classes used in HTML/JS
class_matches = re.findall(r'class=["\']([^"\']+)["\']', text)
classes_used = set()
for cm in class_matches:
    for c in cm.split():
        classes_used.add(c)

print('Total unique classes used:', len(classes_used))
missing_classes = []
for c in sorted(classes_used):
    if f'.{c}' not in style_content and f'{c}' not in style_content:
        missing_classes.append(c)

print('Missing in style:', missing_classes)
