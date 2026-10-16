import runpy, traceback, os, re
SCRIPTS = [
    'write_anchor.py', 'write_struct.py', 'e_spec.py', 'fix_q2.py',
    'e_qfix.py', 'drop_qa_bullets.py', 'e_6p.py', 'e_def.py', 'e_def2.py',
    'big1.py', 'big2.py', 'big3.py', 'fix_review.py', 'cites2.py', 'rename.py', 'q_hygiene.py', 'retire.py', 'normalize_cites.py',
]
D = '/tmp/qcheck'
REPO = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit'

# inline: fix titles split across a line break
import re as _re
for _d in ('articles_maths', 'articles_physics'):
    for _f in os.listdir(os.path.join(REPO, _d)):
        if not _f.endswith('.md'):
            continue
        _p = os.path.join(REPO, _d, _f)
        _t = open(_p, encoding='utf-8').read()
        _n = _re.sub(r'Quaternion\s+(\$\\mathbb\{R\}\$)\s+Space', r'Quaternioid \1 Space', _t)
        if _n != _t:
            open(_p, 'w', encoding='utf-8').write(_n)


# inline: drop the stray symmetric-quaternionic bullet in the topology intro
p = os.path.join(REPO, 'articles_maths', 'introduction-to-topology-on-the-quaternions.md')
if os.path.exists(p):
    lines = open(p, encoding='utf-8').read().split('\n')
    keep = [l for l in lines if not (l.startswith('- ') and 'introduction-to-the-symmetric-quaternionic-algebra-of-quaternioid.md' in l)]
    if len(keep) != len(lines):
        open(p, 'w', encoding='utf-8').write('\n'.join(keep))
        print('dropped topology bullet')

for s in SCRIPTS:
    print('=== ' + s)
    try:
        if s == 'retire.py':
            import sys
            sys.argv = ['retire.py', '--apply']
        if s == 'cites2.py':
            import sys
            sys.argv = ['cites2.py', '--apply']
        runpy.run_path(os.path.join(D, s), run_name='__main__')
    except SystemExit:
        pass
    except Exception:
        traceback.print_exc()
print('MASTER DONE')
