#!/usr/bin/env python3
"""Check the fifty-four Lagrangian articles against the heading contract.

Reads the articles, not the maps. The maps are derived; this script is the
source of truth. Run from the repository root:

    python3 check_lagrangian_headings.py

Exit status 0 means every article obeys the contract.
"""

import glob
import os
import re
import sys

# Slots that may carry more than one section: 3 when the action is stated in
# blocks, 9 when the currents split into a positive statement and a denial,
# 12 when the ledger separates what the method adds from what the chart adds.
# 4 when an article varies two independent fields, 7 carries more than one
# section in three fluid articles. Every other slot
# appears at most once.
REPEATABLE = ('3', '4', '6', '7', '9', '12', 'M2', 'KEEP')

MANDATORY = [
    ('1', 'Introduction'),
    ('2', 'Conventions'),
    ('3', 'The Action in '),
    ('4', 'The Variation'),
    ('7', 'The Structural Consequence'),
    ('9', 'The Noether Currents'),
    ('12', 'What the Principle Adds and What It Relabels'),
    ('15', 'Summary'),
    ('16', 'Summary of Notation'),
    ('17', 'Further Reading'),
]

CONDITIONAL = []

CANONICAL = [
    ('1', 'Introduction'),
    ('2', 'Conventions'),
    ('3', 'The Action in '),
    ('4', 'The Variation'),
    ('5', 'The Reality of the Action'),
    ('6', 'The Constraints the Action Imposes'),
    ('7', 'The Structural Consequence'),
    ('8', 'The Second Variation'),
    ('9', 'The Noether Currents'),
    ('10', 'The Two Settings'),
    ('11', 'The Limits and the Truncation\u2019s Error'),
    ('11a', 'The Limit: The Deletion'),
    ('11b', 'The Limit: The Truncation and Its Error'),
    ('11c', 'The Limit: What Survives'),
    ('12', 'What the Principle Adds and What It Relabels'),
    ('13', 'Comparisons with Other Formulations'),
    ('14', 'Open Questions'),
    ('15', 'Summary'),
    ('16', 'Summary of Notation'),
    ('17', 'Further Reading'),
    ('P1', 'The Parameter Basis and the Four Brackets'),
    ('P2', 'The Reconstruction and Its Limits'),
    ('M1', 'The Symbol and the Quadratic Form'),
    ('M2', 'Zero, Pole and the On-Shell Action'),
    ('M3', 'The Legendre Transform'),
    ('KEEP', 'Aside:'),
    ('KEEP', 'Verification'),
]


CANONICAL_BY_LENGTH = sorted(CANONICAL, key=lambda x: -len(x[1]))

# Slot 5 is one section over four distinct questions. The questions are fixed
# subsections, in this order; a subsection that does not arise carries a
# declaration and is never dropped.
SUBSECTIONS = {
    '5': [
        'The Pairing',
        'The Type of the Coefficient',
        'The Selection Rule',
        'What Reality Does Not Buy',
    ],
}


def slot_of(heading):
    for slot, prefix in CANONICAL_BY_LENGTH:
        if heading == prefix or heading.startswith(prefix):
            return slot
    return None


def h2(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            out.append(line[3:].strip())
    return out


def h2_with_h3(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('## '):
            out.append([line[3:].strip(), []])
        elif line.startswith('### ') and out:
            out[-1][1].append(line[4:].strip())
    return out


def title(path):
    first = open(path, encoding='utf-8').readline()
    return re.sub(r'^#+\s*', '', first).strip().strip('_').strip()


def main():
    arts = sorted(p for p in glob.glob('articles_physics/*.md')
                  if title(p).startswith('The Lagrangian and '))
    sector = sorted(p for p in glob.glob('articles_physics/*.md')
                    if 'lagrangian' in title(p).lower()
                    and not title(p).startswith('The Lagrangian and '))
    fail = 0
    carried = []
    for p in arts:
        slug = os.path.basename(p)[:-3]
        heads = h2(p)
        errs = []
        for h in heads:
            if slot_of(h) is None:
                errs.append('unmapped heading: %r' % h)
        for slot, name in MANDATORY:
            n = sum(1 for h in heads if slot_of(h) == slot)
            if n == 0:
                errs.append('mandatory slot %s (%s) absent' % (slot, name))
            elif n > 1 and slot not in REPEATABLE:
                errs.append('slot %s appears %d times' % (slot, n))
        for slot in sorted(set(s for s in (slot_of(h) for h in heads) if s)):
            n = sum(1 for h in heads if slot_of(h) == slot)
            if n > 1 and slot not in REPEATABLE and slot not in [m[0] for m in MANDATORY]:
                errs.append('conditional slot %s appears %d times' % (slot, n))
        order = [slot_of(h) for h in heads]
        pos = {}
        for i, s in enumerate(order):
            if s in [m[0] for m in MANDATORY] and s not in pos:
                pos[s] = i
        want = [m[0] for m in MANDATORY]
        got = sorted(pos, key=pos.get)
        if got != want:
            errs.append('mandatory slots out of order: %s (want %s)' % (got, want))
        for slot, want_subs in SUBSECTIONS.items():
            blocks = [b for b in h2_with_h3(p) if slot_of(b[0]) == slot]
            if len(blocks) != 1:
                continue
            got = blocks[0][1]
            missing = [s for s in want_subs if s not in got]
            if missing:
                errs.append('slot %s missing subsections: %s' % (slot, missing))
            elif [s for s in got if s in want_subs] != want_subs:
                errs.append('slot %s subsections out of order: %s' % (slot, got))
        for slot, name in CONDITIONAL:
            if sum(1 for h in heads if slot_of(h) == slot) == 0:
                carried.append(slug)
        if errs:
            fail += 1
            print('%s' % slug)
            for e in errs:
                print('    %s' % e)
    print()
    print('articles checked: %d' % len(arts))
    print('articles failing: %d' % fail)
    print('sector and level-0 articles not checked here: %d' % len(sector))
    for p in sector:
        print('    %s' % os.path.basename(p)[:-3])
    return 1 if fail else 0


if __name__ == '__main__':
    sys.exit(main())
