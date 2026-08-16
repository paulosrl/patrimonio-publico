import re

with open('01-Inteligencia-Artificial-e-Engenharia-de-Contexto-na-Tutela-do-Patrimonio-Publico-Paulo-Lima.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('File read successfully. Length:', len(text))
matches = [m.start() for m in re.finditer('Como a IA manipula', text, re.IGNORECASE)]
for idx in matches:
    print('--- MATCH ---')
    print(text[max(0, idx-100):min(len(text), idx+1000)])
