# __The Fermion–Gauge Vertex in the Quartet Basis: The Fifteen Read on the Sixteen__

## Introduction

**This article prints the fermion side of the model's gauge interaction: the fifteen arrays of $\mathfrak{su}(4)$ acting on the sixteen fields, entry by entry, with the quantum numbers of every entry.** It is the companion of [The Feynman Rules of the Four Colours Left–Right Model](the-feynman-rules-of-the-four-colours-left-right-model-the-vertices-of-the-twenty-one-and-the-sixteen.html), which states the rule $\Gamma^{a}_{\imath}=-ig_{4}\gamma_{\imath}(t_{a}\otimes\mathbb{1}_{2})$ and hands the matrices to this article.

**Three questions it answers, and one it does not.**

- **Where does each entry go?** Every one of the $88$ nonzero fermion–gauge entries per chirality is a coefficient joining one quartet line to one quartet line, or one doublet slot to one doublet slot. The article names the four families, prints their matrices, and lists the pairs.
- **What charges does each entry carry?** $B-L$ and $Q$ are read off the entry, and the two are computed for both chiral blocks. **The fifteen carry $B-L$ and do not carry $Q$**, and the article says exactly where the failure sits.
- **What does the algebra forbid?** No generator turns a lepton into a lepton, no generator turns an up slot into a down slot, and the six mixed planes are the only entries that change $B-L$ per line. **Each of the three is a statement with a proof, not a remark.**
- **It does not derive the fermion Lagrangian.** The matrices are the corpus's; the dynamics is the transcription. That is [the spin note](../articles_internal/internal-note-on-the-spin-of-the-lagrangian-articles.html)'s ledger and this article inherits it without softening it.

## Conventions, and the Order of the Eight

**The eight left-handed states, in the order used by every matrix below.**

$$
\bigl(\,\nu_{L},\ e_{L},\ u^{r},\ d^{r},\ u^{g},\ d^{g},\ u^{b},\ d^{b}\,\bigr),
\qquad
\bigl(\,t/u,\ t/d,\ x/u,\ x/d,\ y/u,\ y/d,\ z/u,\ z/d\,\bigr).
$$

**The left column is the physics name and the right column is the index pair**, and the two lines name the same eight objects. **The order is the quartet index slow and the doublet index fast**, which is the order that makes every array act as a block structure rather than a scrambled pattern.

**The convention of the whole article.**
$$
X\ \text{on the eight} = X\otimes\mathbb{1}_{2},
\qquad
\tau_{i}\ \text{on the eight} = \mathbb{1}_{4}\otimes\tau_{i},
\qquad
\bigl[X\otimes\mathbb{1}_{2},\ \mathbb{1}_{4}\otimes\tau_{i}\bigr]=0 .
$$
**Every matrix printed below is $8\times8$ and block-diagonal in the doublet**: two identical $4\times4$ blocks on the diagonal, one for the up slot and one for the down slot. **A reader who wants the four-colour content can read the top-left block and stop.**

**The charges.** With $D=\operatorname{diag}(-3,1,1,1)$ and $T_{3}$ on the slot,
$$
B-L=\tfrac13 D=\operatorname{diag}\bigl(-1,\tfrac13,\tfrac13,\tfrac13\bigr),
\qquad
Q=T_{3}+\tfrac12(B-L).
$$
**$B-L$ is $\tfrac13D$ and not $\tfrac16D$**, and the factor is the reason the electric charge is $T_{3}+\tfrac16D$ and the corner's eigenvalues are $(-3,1,1,1)$ rather than $(-\tfrac12,\tfrac16,\tfrac16,\tfrac16)$.

## The Fifteen, in Four Families

**The fifteen are four families and the classification is the whole of the matrix content.**

| family | count | matrix | what an entry does | $B-L$ |
| --- | --- | --- | --- | --- |
| colour planes | $6$ | $A_{ab}$, $iS_{ab}$, $a,b\in\{x,y,z\}$ | $a\to b$ inside the triple | $0$ |
| colour Cartan | $2$ | $d_{2}$, $d_{3}$ | phases inside the triple | $0$ |
| corner | $1$ | $iD$ | phases, $-3i$ on $t$ and $+i$ on each $a$; no entry moves a line | $0$ per entry; the $-3i$ against $+i$ is where the $\pm\tfrac43$ sits |
| mixed planes | $6$ | $A_{ta}$, $iS_{ta}$ | $t\leftrightarrow a$ | $\pm\tfrac43$ |

**The $B-L$ column is the charge the *entry* transfers and not the charge of the field**, and the distinction is the reason the leptoquarks carry $\pm\tfrac43$: an entry that joins $t$ to $a$ moves a state from $B-L=-1$ to $B-L=+\tfrac13$, so the boson that carries the entry must take $\mp\tfrac43$ with it.

**The four families, as $4\times4$ blocks.** The colour planes and the colour Cartan are block-diagonal, with the $3\times3$ colour block acting and the $t$ entry untouched:
$$
A_{xy}=\begin{pmatrix}0&0&0&0\\0&0&1&0\\0&-1&0&0\\0&0&0&0\end{pmatrix},
\qquad
iS_{xy}=\begin{pmatrix}0&0&0&0\\0&0&i&0\\0&i&0&0\\0&0&0&0\end{pmatrix},
\qquad
d_{2}=\begin{pmatrix}0&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&0\end{pmatrix}.
$$
**The corner and the mixed planes are the ones that touch the lepton line.**
$$
iD=\begin{pmatrix}-3i&0&0&0\\0&i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix},
\qquad
A_{tx}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
iS_{tx}=\begin{pmatrix}0&i&0&0\\i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}.
$$

**The eight-by-eight form of one of them, printed once.** With $A_{tx}\otimes\mathbb{1}_{2}$ in the order above,

$$
A_{tx}\otimes\mathbb{1}_{2}=
\begin{pmatrix}
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
-1&0&0&0&0&0&0&0\\
0&-1&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0
\end{pmatrix},
$$

**and the shape is the whole two-index rule.** Four rows act and four are zero: the array moves $\nu_{L}\leftrightarrow u^{r}$ and $e_{L}\leftrightarrow d^{r}$, and it annihilates every colour state that is not red. **No entry mixes a $u$ row with a $d$ row**, because the two $4\times4$ blocks are identical and diagonal in the slot.

## The Selection Rule, and the Count $8+1+6$

**Dividing the fifteen by what each does to $e_{t}$ is the one classification that matters for physics.**

| class | count | action on $e_{t}$ | consequence |
| --- | --- | --- | --- |
| colour planes and colour Cartan | $8$ | $0$ | no coupling of a colour boson to a lepton |
| corner $iD$ | $1$ | $-3i\,e_{t}$ | the lepton's $B-L$, and no change of line |
| mixed planes $A_{ta}$, $iS_{ta}$ | $6$ | into the colour triple | the leptoquarks, and the only change of line |

**The count is exhaustive and each row is a computation.** A colour plane $A_{ab}$ has its two nonzero entries in rows and columns $a,b$, both inside the triple, so its $t$ column is zero. **The corner is diagonal, so it cannot move a line, and its $t$ entry is $-3i$.** The six mixed planes have their entries in the $t$ row and the $a$ column, so each sends $e_{t}$ to a multiple of $e_{a}$ and nothing else.

**What the first row forbids is lepton flavour.** If no generator has an entry joining $e_{t}$ to $e_{t}$ other than a multiple of the identity on that line, then no gauge vertex can turn one lepton into another, and a flavour label on the lepton has no gauge channel to act on. **That is [the lepton-flavour article](lepton-flavour-in-the-four-colours-model-nothing-turns-the-lepton.html)'s structural result, and here it is a count of matrix entries: eight zero, one diagonal, six into the triple.**

**What the second row forbids is an electric charge.** The corner gives the same phase $-3i$ to $\nu_{L}$ and to $e_{L}$, and the same phase $+i$ to $u^{r}$ and to $d^{r}$. **A quantum number that separates the members of a doublet cannot be a matrix on the quartet alone**, and the statement is exact: the two rows of the display are identical, so no property of the array distinguishes them.

**What the third row allows is the whole of the model's new physics.** Six entries join the lepton line to a colour line, each carries $B-L=\pm\tfrac43$, and each conserves $B-L$ at the vertex because the boson carries it away. **Six generators, three colours and the two plane types, and that is the leptoquark sector.**

## The Charges of Every Entry

**The eight left-handed fields, with the two charges and the two label values.** This is the table every vertex is read from.

| field | line | slot | $T_{3}$ | $B-L$ | $Q$ |
| --- | --- | --- | --- | --- | --- |
| $\nu_{L}$ | $t$ | $u$ | $+\tfrac12$ | $-1$ | $0$ |
| $e_{L}$ | $t$ | $d$ | $-\tfrac12$ | $-1$ | $-1$ |
| $u^{r}$ | $x$ | $u$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ |
| $d^{r}$ | $x$ | $d$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ |
| $u^{g}$ | $y$ | $u$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ |
| $d^{g}$ | $y$ | $d$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ |
| $u^{b}$ | $z$ | $u$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ |
| $d^{b}$ | $z$ | $d$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ |

**And the eight right-handed fields, whose charges are the left octet's own.**

| field | line | slot | $T^{R}_{3}$ | $B-L$ | $Q$ |
| --- | --- | --- | --- | --- | --- |
| $\nu_{eR}$ | $t$ | $u$ | $+\tfrac12$ | $-1$ | $0$ |
| $e_{R}$ | $t$ | $d$ | $-\tfrac12$ | $-1$ | $-1$ |
| $u^{r}_{R}$ | $x$ | $u$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ |
| $d^{r}_{R}$ | $x$ | $d$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ |
| $u^{g}_{R}$ | $y$ | $u$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ |
| $d^{g}_{R}$ | $y$ | $d$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ |
| $u^{b}_{R}$ | $z$ | $u$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ |
| $d^{b}_{R}$ | $z$ | $d$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ |

**The right-handed table is the left-handed table with an $R$ on the name, and that is the naming rule and not an accident.** A name denotes a particle, so $e_{R}$ carries the electron's $Q=-1$ and the electron's $B-L=-1$; only the *representation* carries the conjugate. [The classification article](classification-of-the-fermions-in-the-four-colours-left-right-model-one-generation-sixteen-fields-thirty-two-states-closed-under-cp-and-not-under-c.html) states the rule in one sentence and uses it to compute the anomaly on $(\mathbf4,\mathbf2,\mathbf1)$ and $(\bar{\mathbf4},\mathbf1,\mathbf2)$, where the second block's entries are the conjugates of the named right-handed fields.

**The formula holds in the same form on both octets.** $Q=T^{R}_{3}+\tfrac12(B-L)$ gives $-1$ for $e_{R}$ from $-\tfrac12-\tfrac12$, and $+\tfrac23$ for $u^{r}_{R}$ from $\tfrac12+\tfrac16$. **No sign is flipped between the two tables, and the reason is that the slot keeps its meaning**: the up slot is $+\tfrac12$ on both sides.

## The Right-Handed Block, and Where the Minus Actually Sits

**The generator on the $\bar{\mathbf{4}}$ is $-t^{\mathsf{T}}$, and the minus belongs to the representation and not to the table.**
$$
\bigl(t_{a}\bigr)_{ij}\ \text{on}\ (\mathbf{4},\mathbf{2},\mathbf{1}),
\qquad
-\bigl(t_{a}\bigr)_{ji}\ \text{on}\ (\bar{\mathbf{4}},\mathbf{1},\mathbf{2}).
$$
**The two displays are one vertex written two ways**, because a field in the $\bar{\mathbf{4}}$ and its conjugate in the $\mathbf{4}$ carry the same physical state read twice: the vertex reads $\bar\xi\,t\,\xi$ on the field in the $\mathbf{4}$ and reads with $t^{\mathsf{T}}$ and a minus when the same leg is written as the conjugate. **A diagonal generator therefore differs by a sign and a plane by a transposition, and neither changes a charge**, since a charge is read from the commuting generator and a transposition does not touch a diagonal.

**Worked on the leptoquark plane, both readings of the same vertex.**
$$
\text{on the fields: } u^{r}\to\nu_{L}\ \text{with } +1,
\qquad
\text{on the conjugates: } \bar u^{r}\to\bar\nu_{L}\ \text{with } -1,
$$
**and the charge transfer is $-\tfrac23$ in both lines.** The sign is opposite between a line and its conjugate, which is the statement that the boson carries $B-L=\pm\tfrac43$: the vertex and its conjugate use opposite signs of the boson's charge, and the two are the same physical process.

**What is not a sign flip, and the one table that is wrong.** The $B-L$ of a state and the $B-L$ carried by an entry are different objects; the conjugate reading reverses the first and not the second. **A table that gives a particle name the conjugate's charges — $e_{R}$ with $Q=+1$, $u^{r}_{R}$ with $Q=-\tfrac23$ — is wrong, and it is wrong in the direction that reverses seven of the eight electric charges and all eight $B-L$ values while leaving the shape of the table looking plausible.**

## The Weak Side, in the Same Basis

**The weak generators are not among the fifteen and this article prints them because a reader will otherwise look for them.**
$$
\tau_{3}\otimes\mathbb{1}_{4}\ \text{on the eight}:
\qquad
u^{a}\to+\tfrac12 u^{a},
\qquad
d^{a}\to-\tfrac12 d^{a},
\qquad
\text{for every }a\in\{t,x,y,z\}.
$$
**Eight entries, four up and four down, and none of them knows a colour.** The matrix is $\mathrm{diag}(+\tfrac12,-\tfrac12,+\tfrac12,-\tfrac12,\dots)$ on the order above, which is the statement that **the weak charge is uniform on each colour line and the colour charge is uniform on each slot** — the two facts that between them make the electric charge a sum of one entry from each display.

**The ladder is the one object that changes a slot.**
$$
\tau_{1}+i\tau_{2}=\begin{pmatrix}0&2\\0&0\end{pmatrix},
\qquad
d^{a}\to u^{a},
$$
**in the convention where the upper component is the up slot.** It is $2\times2$, it is not one of the twenty-one, and it is the only matrix in the model that turns a down quark into an up quark. **Everything else in this article preserves the slot**, which is why the fifteen are described as the colour and $B-L$ algebra and not as the whole gauge algebra.

**The count, one last time, and it is the article's only arithmetic.**
$$
\underbrace{48}_{\text{twelve planes}\times2\times2}+\underbrace{16}_{\text{corner }8,\ \text{two diagonals }4+4}+\underbrace{24}_{\text{three weak arrays}\times8}=88 .
$$
**Eighty-eight entries in one chirality and $176$ in both, and each is a number in a printed array.** The article has named all of them by family, by pair of lines and by the charge they transfer, and no entry has been computed that the corpus did not already print.

**The sparsity is worth one remark, because a reader expects more.** A plane such as $A_{tx}$ has two nonzero entries on the quartet and four on the eight: it moves one line into one other line and does nothing else. **Only the corner touches all four lines, and it does so diagonally.** So the gauge sector of this model is sparse in the fermion basis, and a vertex table written out is short.

## What the Article Does Not Do

**It does not choose a normalisation.** The entries printed are the arrays' own, and [the rules article](the-feynman-rules-of-the-four-colours-left-right-model-the-vertices-of-the-twenty-one-and-the-sixteen.html)'s rescaling sits between these matrices and a rule. **A reader who compares an entry here with an amplitude has one $i$, one rescaling and possibly one mixing to apply.**

**It does not derive the fermion kinetic term.** The matrices are exact as algebra and the coupling is transcribed, and the reason is the chiral wall: no chiral non-abelian matter representation is built, so no covariant derivative on the fermion's own carrier exists in $\mathbb{B}$.

**It does not fix the family index.** Every entry above carries an implicit $\delta^{ij}$ in the family, and the Yukawa matrices are what break that. **A leptoquark that changed a generation would need an entry in the family factor, and the minimal sector makes that matrix the identity** — which is why the $K_L\to\mu e$ channel closes in the minimal model and opens in the next one.

## The Checks

| check | computation | result |
| --- | --- | --- |
| the four families sum to fifteen | $6+2+1+6$ | $15$ |
| the selection rule | $8$ annihilate $e_{t}$, $1$ multiplies, $6$ move | $15$ |
| the corner on $e_{t}$ | $iD$ entry | $-3i$ |
| the corner on $e_{x}$ | $iD$ entry | $+i$ |
| the $B-L$ of the corner | $\tfrac13\operatorname{eig}D$ | $(-1,\tfrac13,\tfrac13,\tfrac13)$ |
| the two-index bracket | $[A_{tx}\otimes\mathbb{1}_{2},\mathbb{1}_{4}\otimes\tau_{3}]$ | $0$ |
| the charge formula on $e_{R}$ | $-\tfrac12+\tfrac12(-1)$ | $-1$ |
| the charge formula on $u^{r}_{R}$ | $+\tfrac12+\tfrac16$ | $+\tfrac23$ |
| the leptoquark transfer, up row | $0-(+\tfrac23)$ | $-\tfrac23$ |
| the leptoquark transfer, down row | $-1-(-\tfrac13)$ | $-\tfrac23$ |
| the gluon transfer | $+\tfrac23-(+\tfrac23)$ | $0$ |
| the entries, one chirality | $48+16+24$ | $88$ |
| the eight-by-eight block structure | the two $4\times4$ blocks | identical |

## Summary

**The fermion side of the gauge interaction is a set of fifteen printed matrices and a multiplication by $\mathbb{1}_{2}$, and nothing else.** The article prints them in four families, in both a $4\times4$ and an $8\times8$ form, and names every entry by the pair of lines it joins and the charge it transfers.

**The three structural statements are counts.** Eight of the fifteen annihilate the lepton line, one multiplies it, six move it into the colour triple; the sum is fifteen and no case is missing. **The first eight are why lepton flavour has no gauge channel, the middle one is why the corner is $B-L$ and not $Q$, and the last six are the leptoquark sector.**

**Two mistakes are forbidden by the tables and both are easy to make.** The first is to give a particle name the conjugate's charges, which reverses seven of the eight electric charges and every $B-L$. The second is to look for the weak charge among the fifteen, which is where it is not: $\tau_{3}$ is uniform on colour and the colour arrays are uniform on the slot, and the electric charge is the sum of one entry from each.

**What remains outside the article is the dynamics**: one $i$ and one rescaling per gauge leg, the coupling symbolic, and the fermion action transcribed rather than derived. **The matrices are the corpus's and they were already complete; the article's work is to read them in the order that makes the physics visible.**

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $X\otimes\mathbb{1}_{2}$ | An array on the eight, identical in both doublet slots |
| $\mathbb{1}_{4}\otimes\tau_{i}$ | A weak generator, uniform on the quartet |
| $T_{3}$ | $\tau_{3}$, the diagonal weak charge |
| $B-L$ | $\tfrac13D$, with eigenvalues $(-1,\tfrac13,\tfrac13,\tfrac13)$ |
| $Q$ | $T_{3}+\tfrac12(B-L)$ |
| $t/u,\ t/d,\dots$ | The eight left-handed states, line over slot |
| $u,d$ | The two doublet slots, $\uparrow$ and $\downarrow$ |
| $r,g,b$ | The colour lines $x,y,z$ |
| $\mathbf{4}$, $\bar{\mathbf{4}}$ | The two chiral blocks |
| $-t^{\mathsf{T}}$ | The generator on the conjugate block |
| $A_{ta}$, $iS_{ta}$ | The six mixed planes, the leptoquark entries |
| $88$ | The number of nonzero fermion–gauge entries in one chirality |

## Further Reading

- [The Feynman Rules of the Four Colours Left–Right Model](the-feynman-rules-of-the-four-colours-left-right-model-the-vertices-of-the-twenty-one-and-the-sixteen.html). The rule these matrices instantiate, and the normalisation that sits between matrix and amplitude.
- [Classification of the Fermions in the Four Colours Left–Right Model](classification-of-the-fermions-in-the-four-colours-left-right-model-one-generation-sixteen-fields-thirty-two-states-closed-under-cp-and-not-under-c.html). The sixteen fields, the two readings of the sixteen rows, and the conjugation.
- [The Commutation Table of the Twenty-One Generators](the-commutation-table-of-the-twenty-one-generators-441-entries-164-nonzero-and-six-rules.html). Which of these entries close into which under the bracket.
- [Lepton Flavour in the Four-Colours Model](lepton-flavour-in-the-four-colours-model-nothing-turns-the-lepton.html). The $8+1+6$ count in its physics setting, and the reason no gauge vertex turns a lepton.
- [The Leptoquarks of the Four Colours Left–Right Model](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html). The six states the six mixed planes become, and the $B-L=\pm\tfrac43$.
- [The Twenty-One AXF Matrices of the Bosons in Detail](the-21-axf-matrices-of-the-bosons-in-detail.html). Every array printed with its entries and spectrum.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html). The one-sided pair $\xi_{L},\xi_{R}$ and the chiral wall the transcribed action lives behind.
- [The Excitation Ladder Theory of Flavour](the-excitation-ladder-theory-of-flavour.html). What the family factor would have to be for the Yukawa matrix to be more than the identity.
