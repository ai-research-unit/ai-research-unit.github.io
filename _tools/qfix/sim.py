import os, glob, difflib

D = 'articles_maths'
fam = {
    'annihilators': 'annihilators-of-the-*-of-quaternioid.md',
    'zero-divisors': 'zero-divisors-of-the-*-of-quaternioid.md',
    'sq-one-idem': 'square-roots-of-one-and-the-idempotents-of-the-*-of-quaternioid.md',
    'sq-zero-nilp': 'square-roots-of-zero-and-the-nilpotents-of-the-*-of-quaternioid.md',
    'specificities': 'the-specificities-of-the-*-of-quaternioid.md',
    'norm-inv': 'norm-and-invertibility-in-the-*-of-quaternioid.md',
    'intro': 'introduction-to-the-*-of-quaternioid.md',
    '2x2': '*-in-the-2x2-matrix-element-representation-of-quaternioid.md',
    '4x4': '*-in-the-4x4-matrix-element-representation-of-quaternioid.md',
}

def body(p):
    t = open(os.path.join(D, p), encoding='utf-8').read()
    # drop Further Reading and Summary of Notation to compare substance
    return t

for name, pat in fam.items():
    files = sorted(glob.glob(os.path.join(D, pat)))
    files = [f for f in files if 'general-plain' not in f]
    if len(files) < 2:
        print(name, '->', len(files), 'files (skipped)'); continue
    print(f'\n=== {name}  ({len(files)} files) ===')
    for f in files: print('   ', os.path.basename(f))
    txts = [body(os.path.basename(f)) for f in files]
    ratios = []
    for i in range(len(txts)):
        for j in range(i + 1, len(txts)):
            r = difflib.SequenceMatcher(None, txts[i], txts[j]).ratio()
            ratios.append(r)
    print(f'    pairwise similarity: min {min(ratios):.2f}  max {max(ratios):.2f}  mean {sum(ratios)/len(ratios):.2f}')
