import os

def patch_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Aggiornamento sintassi PyTorch obsoleta
    content = content.replace('.item()', '.item()')
    
    # 2. Aggiornamento sintassi Numpy deprecata in Numpy 1.24+
    content = content.replace('float', 'float')
    content = content.replace('int', 'int')
    content = content.replace('bool', 'bool')
    
    with open(filepath, 'w') as f:
        f.write(content)

# Scansiona tutte le sottocartelle e applica la patch
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            patch_file(os.path.join(root, file))

print("✅ PTNet3D è stata aggiornata con successo per il moderno ambiente di Kaggle!")
