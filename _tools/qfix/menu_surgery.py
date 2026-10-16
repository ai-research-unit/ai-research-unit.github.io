import re, os, shutil, sys

REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'
APPLY = '--apply' in sys.argv
p = os.path.join(REPO, 'maths.md')
text = open(p, encoding='utf-8').read()
lines = text.split('\n')

# ---- slugs retired from the Quaternioid menu ----
RETIRE_QA = [
    # Generalities
    'remarkable-subspaces-under-the-six-operations',
    # SPA element theory
    'norm-and-invertibility-in-the-symmetric-plain-algebra-of-quaternioid',
    'zero-divisors-of-the-symmetric-plain-algebra-of-quaternioid',
    'annihilators-of-the-symmetric-plain-algebra-of-quaternioid',
    'square-roots-of-one-and-the-idempotents-of-the-symmetric-plain-algebra-of-quaternioid',
    'square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-algebra-of-quaternioid',
    'square-roots-of-a-general-element-in-the-symmetric-plain-algebra-of-quaternioid',
    # APA element theory
    'norm-and-invertibility-in-the-antisymmetric-plain-algebra-of-quaternioid',
    'zero-divisors-of-the-antisymmetric-plain-algebra-of-quaternioid',
    'annihilators-of-the-antisymmetric-plain-algebra-of-quaternioid',
    'square-roots-of-one-and-the-idempotents-of-the-antisymmetric-plain-algebra-of-quaternioid',
    'square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-plain-algebra-of-quaternioid',
    'square-roots-of-a-general-element-in-the-antisymmetric-plain-algebra-of-quaternioid',
    # GQA element theory
    'norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternioid',
    'zero-divisors-of-the-general-quaternionic-algebra-of-quaternioid',
    'annihilators-of-the-general-quaternionic-algebra-of-quaternioid',
    'square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra-of-quaternioid',
    'square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-quaternioid',
    'square-roots-of-a-general-element-in-the-general-quaternionic-algebra-of-quaternioid',
]
RETIRE_Q = [
    'topology-and-metric-for-each-of-the-six-operations',
]
RETIRE_BLOCKS = [
    '### The Quaternioid Symmetric Quaternionic Algebra (SQA) over $\\mathbb{R}$',
    '### The Quaternioid Antisymmetric Quaternionic Algebra (AQA) over $\\mathbb{R}$',
]
MOVE_TO_QA_FROM_Q = [
    'the-two-adjoints-of-the-two-algebras-in-examples',
]
EMPTY_HEADINGS_Q = ['#### Operators', '#### Operators Representations']
INSERT_AT_GENERALITIES_END = [
    '<a href="articles_maths/the-two-adjoints-of-the-two-algebras-in-examples.html">The Two Adjoints of the Two Algebras in Examples</a>',
    '<!-- the adjoints of the two general products, gathered and worked on examples: the transpose for the plain form, the conjugate transpose for the quaternion form; the identity relations; the worked elements. -->',
]

def find_line(pred, lo=0):
    for i in range(lo, len(lines)):
        if pred(lines[i]):
            return i
    raise SystemExit('not found')

def slug_of(line):
    m = re.search(r'href="articles_maths/([^"]+)\.html"', line)
    return m.group(1) if m else None

def block_span(i):
    """span of an entry starting at line i: the <a> line plus following comment line(s)."""
    j = i + 1
    while j < len(lines) and lines[j].lstrip().startswith('<!--'):
        j += 1
    return i, j

q_start = find_line(lambda l: l == '## Quaternions')
qa_start = find_line(lambda l: l == '## Quaternioid Algebraic Structures')
sq_start = find_line(lambda l: l == '## Split-Quaternions')

removed = []
# collect removals as (start,end) spans, then apply from the end
spans = []
for i in range(q_start, sq_start):
    s = slug_of(lines[i])
    if s in RETIRE_Q or s in MOVE_TO_QA_FROM_Q:
        a, b = block_span(i)
        spans.append((a, b, s))
    elif lines[i] in EMPTY_HEADINGS_Q and i < qa_start:
        spans.append((i, i + 1, lines[i]))
for i in range(qa_start, sq_start):
    s = slug_of(lines[i])
    if s in RETIRE_QA:
        a, b = block_span(i)
        spans.append((a, b, s))
# whole blocks
for h in RETIRE_BLOCKS:
    a = find_line(lambda l: l == h)
    b = find_line(lambda l: l.startswith('### ') and len(l) > 4, a + 1)
    spans.append((a, b, 'BLOCK:' + h))

# apply
spans.sort(key=lambda t: t[0], reverse=True)
for a, b, tag in spans:
    removed.append(tag)
    del lines[a:b]

# insert the moved entries at the end of Generalities
qa2 = find_line(lambda l: l == '## Quaternioid Algebraic Structures')
gqa_head = find_line(lambda l: l == '### The Quaternioid General Quaternionic Algebra (GQA) over $\\mathbb{R}$', qa2)
# back off over blank lines
k = gqa_head
while k > 0 and lines[k - 1].strip() == '':
    k -= 1
lines[k:k] = INSERT_AT_GENERALITIES_END + ['']

print('removed', len(removed), 'menu units')
for t in sorted(removed):
    print('   ', t)

if APPLY:
    shutil.copyfile(p, '/tmp/qcheck/maths.md.bak')
    open(p, 'w', encoding='utf-8').write('\n'.join(lines))
    print('WROTE maths.md')
else:
    print('DRY RUN')
