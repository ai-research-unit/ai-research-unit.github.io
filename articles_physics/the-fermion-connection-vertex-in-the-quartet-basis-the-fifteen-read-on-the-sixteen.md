# __The Fermion–Connection Vertex in the Quartet Basis: The Fifteen Read on the Sixteen__

## Introduction

**This article prints the fermion side of the connection interaction: the fifteen arrays of $\mathfrak{su}(4)$ acting on the sixteen fields, entry by entry, with the quantum numbers of every entry.** It is the companion of [The Feynman Rules](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html), which states the rule $\Gamma^{a}_{\imath}=-ig_{4}\gamma_{\imath}(t_{a}\otimes\mathbb{1}_{2})$ and hands the matrices to this article.

**Three questions it answers, and one it does not.**

- **Where does each entry go?** Every one of the $120$ nonzero fermion–connection entries is a coefficient joining one quartet line to one quartet line. **There are $60$ on the quartet half and $60$ on the conjugate half**, and the article names the four families, prints their matrices, and lists the pairs.
- **What does each entry carry?** $B-L$ is read off the entry and computed for every family. **The fifteen carry $B-L$ and do not carry $T_{3}$**, and the article says exactly where that split sits and why the missing half is a wall and not an oversight.
- **What does the algebra forbid?** No generator moves a fermion along the lepton line into another lepton line, no generator changes the copy index, and the six mixed planes are the only entries that change a line at all. **Each of the three is a statement with a proof, not a remark.**
- **It does not derive the fermion Lagrangian.** The matrices are the corpus's; the dynamics is the transcription. **The dynamics is [the spin note](../articles_internal/internal-note-on-the-spin-of-the-lagrangian-articles.html)'s ledger**, and this article inherits it without softening it.

## Conventions, and the Order of the Sixteen

**The sixteen fields, and the two indices they carry.**

$$
\xi_{i}^{\alpha},\qquad \bar\xi^{i}_{\alpha},\qquad i\in\{t,r,g,b\},\quad \alpha\in\{1,2\}.
$$

**The quartet index $i$ is slow and the copy index $\alpha$ is fast**, and every matrix below is printed in that order. **The sixteen are two quartets and two antiquartets**: eight fields in $\mathbf 4$ and eight in $\bar{\mathbf4}$.

**The copy index is the weak-doublet slot, and the model does not representative it.** $\alpha$ distinguishes the two members of a cell — for the lepton line the neutrino from the electron, for a spatial line the up from the down — and **no generator of the fifteen carries an $\alpha$**: every array is $\mathbb 1$ on it. The consequence is the whole of §*What the Algebra Forbids*.

**The convention of the whole article.**

$$
X\ \text{on the sixteen} = X\otimes\mathbb{1}_{2},
\qquad
\bigl[X\otimes\mathbb{1}_{2},\ \mathbb{1}_{4}\otimes M\bigr]=0\ \ \text{for every }M .
$$

**Each $4\times4$ array is printed twice on the diagonal and never off it.** A reader who wants the quartet content can read the top-left $8\times8$ block and stop.

**The charges, and which of them the group owns.**

$$
B-L=\tfrac13 D=\operatorname{diag}\bigl(-1,\tfrac13,\tfrac13,\tfrac13\bigr),
\qquad
Q=\tau_{3}+\tfrac12(B-L),
$$

with $\tau_{3}=\pm\tfrac12$ on the copy index. **$B-L$ is a generator and $Q$ is not**: $B-L=\tfrac13D$ is one of the fifteen up to normalisation, while $Q$ mixes a diagonal of the fifteen with $\tau_{3}$, **and $\tau_{3}$ is not in the algebra.** A quantum number built from a generator and a non-generator is not a symmetry charge, and that is the sentence the electroweak wall is made of.

**The four cells and their two charges each.**

| cell | $B-L$ | $Q$ on copy $1$ | $Q$ on copy $2$ | the particles |
| --- | --- | --- | --- | --- |
| $(t,t)$ | $-1$ | $0$ | $-1$ | $\nu$, $e$ |
| $(x,x)$ | $+\tfrac13$ | $+\tfrac23$ | $-\tfrac13$ | $u^{r}$, $d^{r}$ |
| $(y,y)$ | $+\tfrac13$ | $+\tfrac23$ | $-\tfrac13$ | $u^{g}$, $d^{g}$ |
| $(z,z)$ | $+\tfrac13$ | $+\tfrac23$ | $-\tfrac13$ | $u^{b}$, $d^{b}$ |

**Two sums, and both are zero.** $B-L$ over one generation: $2(-1)+6(\tfrac13)=0$. Electric charge over one generation: $0-1+3(\tfrac23)-3(\tfrac13)=0$. **The second sum is what makes the generation neutral, and it holds because $D$ is traceless** — the trace of the diagonal is $-3+1+1+1=0$, and one generation is one full pass over the quartet.

## The Fifteen, in Four Families

**The fifteen are four families and the classification is the whole of the matrix content.**

| family | count | matrix | what an entry does | boson's $B-L$ |
| --- | --- | --- | --- | --- |
| spatial planes | $6$ | $A_{ab}$, $iS_{ab}$, $a,b\in\{x,y,z\}$ | $a\to b$ inside the triple | $0$ |
| $\mathfrak{su}(3)$ Cartan | $2$ | $d_{2}$, $d_{3}$ | phases inside the triple | $0$ |
| corner | $1$ | $iD$ | phases, $-3i$ on $t$ and $+i$ on each $a$; no entry moves a line | $0$ |
| mixed planes | $6$ | $A_{ta}$, $iS_{ta}$ | $t\leftrightarrow a$ | $\pm\tfrac43$ |

**The last column is the charge the *boson* carries and not the charge of a field.** An entry that joins $t$ to $a$ moves a state from $B-L=-1$ to $B-L=+\tfrac13$, so the boson that carries the entry must take $-\tfrac43$ with it: **$-1=\tfrac13-\tfrac43$, and the vertex conserves $B-L$ exactly.**

**The families as $4\times4$ blocks.** The spatial planes and the $\mathfrak{su}(3)$ Cartan are block-diagonal, with the $3\times3$ spatial block acting and the $t$ entry untouched:

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

**The eight-by-eight form of one of them, printed once.** With $A_{tx}\otimes\mathbb{1}_{2}$ in the order $(t_{1},t_{2},x_{1},x_{2})$, the acting block is

$$
A_{tx}\otimes\mathbb{1}_{2}=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
-1&0&0&0\\
0&-1&0&0
\end{pmatrix},
$$

**and the shape is the whole two-index rule.** The array moves $t_{1}\leftrightarrow x_{1}$ and $t_{2}\leftrightarrow x_{2}$ and annihilates every other pair. **No entry mixes $\alpha=1$ with $\alpha=2$**, because the copy index is acted on by the identity.

## The Selection Rule, and the Count $48+12$

**Dividing the fifteen by what each does to $e_{t}$ is the one classification that matters for physics.**

| class | count | action on $e_{t}$ | consequence |
| --- | --- | --- | --- |
| spatial planes, and the two differences of frame directions that cancel the lepton entry | $8$ | $0$ | no coupling of a adjoint direction to a lepton |
| the corner direction $iD$, the sum of the three frame arrays | $1$ | $-3i\,e_{t}$ | the lepton's $B-L$, and no change of line |
| mixed planes $A_{ta}$, $iS_{ta}$ | $6$ | into the three lines | the leptoquarks, and the only change of line |

**The count is exhaustive and each row is a computation.** A spatial plane $A_{ab}$ has its two nonzero entries in rows and columns $a,b$, both inside the triple, so its $t$ column is zero. **The corner is diagonal, so it cannot move a line, and its $t$ entry is $-3i$.** The six mixed planes have their entries in the $t$ row and the $a$ column, so each sends $e_{t}$ to a multiple of $e_{a}$ and nothing else.

**The count of entries, family by family.**

$$
\underbrace{48}_{\text{twelve planes}\times2\times2}
+\underbrace{12}_{\text{three frame directions}\times2\times2}
=\underbrace{60}_{\text{one half}},
\qquad
60+60=\mathbf{120}.
$$

**A printed list that takes $iD$ as a member gives $48+8+8=64$ instead, and its extra $8$ belongs to a sum**: $iD$'s four entries sit on the same four diagonal cells that the three frame directions already occupy, two each. **The count of vertex positions is therefore a basis statement; the selection rule below is not.**

**The second $60$ is the conjugate half**, where the vertex is $-t_{a}^{T}\otimes\mathbb{1}_{2}$ and every entry is reversed with a minus. **The two halves have the same count and the opposite sign**, which is the statement §*The Conjugate Half* makes precise.

**What the first row forbids is lepton flavour.** No generator has an entry joining the lepton line to itself except the diagonal weight on it, so no connection vertex can turn one lepton into another. **That is [the lepton-flavour article](lepton-flavour-in-the-su4-model-nothing-turns-the-lepton.html)'s structural result**, and here it is one row of a table.

**What the second row forbids is a representative origin for $Q$.** The corner gives the same phase $-3i$ to both copies in the lepton cell and the same phase $+i$ to both copies in a spatial cell. **A matrix that is $\mathbb 1$ on the copy index cannot separate $\nu$ from $e$**, and the statement is exact: the two copy entries of every array are equal.

**What the third row allows is the whole of the model's new physics.** Six entries join the lepton line to a spatial line, each carries $B-L=\mp\tfrac43$, and each conserves $B-L$ at the vertex because the boson carries it away. **Six generators, three lines and the two plane types, and that is the leptoquark sector.**

## The Charges of Every Entry

**The charge an entry transfers is the difference of the diagonals it joins.** An entry at row $\imath$, column $\jmath$ sends a fermion on line $\jmath$ to line $\imath$, so the fermion's $B-L$ changes by $\tfrac13(D_{\imath}-D_{\jmath})$ and the boson carries the opposite. **Three families, five rows, and two of them are nonzero.**

| family | entry | $\Delta(B-L)$ of the fermion | boson's $B-L$ | boson's $Q$ |
| --- | --- | --- | --- | --- |
| spatial plane | $(\imath,\jmath)$ both spatial | $0$ | $0$ | $0$ |
| $\mathfrak{su}(3)$ Cartan | diagonal | $0$ | $0$ | $0$ |
| corner | diagonal | $0$ | $0$ | $0$ |
| mixed plane | $(t,a)$: spatial $\to$ lepton | $\tfrac13(-3-1)=-\tfrac43$ | $+\tfrac43$ | $+\tfrac23$ |
| mixed plane | $(a,t)$: lepton $\to$ spatial | $\tfrac13(1+3)=+\tfrac43$ | $-\tfrac43$ | $-\tfrac23$ |

**The $Q$ column is half the $B-L$ column, and that is not a coincidence.** Every connection vertex is diagonal in the copy index, so $\tau_{3}$ is the same before and after: **$\Delta Q=\Delta(B-L)/2$ for the fermion, which is why the boson's $Q$ is $\mp\tfrac23$ where its $B-L$ is $\mp\tfrac43$.** The two charges agree on the sector because the sector cannot see $\tau_{3}$.

**The six mixed planes in the naming of particles.**

| entry | line changed | the vertex | boson's $Q$ |
| --- | --- | --- | --- |
| $A_{tr}$, $iS_{tr}$ | $t\leftrightarrow r$ | $\nu\to u^{r}$, $e\to d^{r}$ | $\mp\tfrac23$ |
| $A_{tg}$, $iS_{tg}$ | $t\leftrightarrow g$ | $\nu\to u^{g}$, $e\to d^{g}$ | $\mp\tfrac23$ |
| $A_{tb}$, $iS_{tb}$ | $t\leftrightarrow b$ | $\nu\to u^{b}$, $e\to d^{b}$ | $\mp\tfrac23$ |

**Each of the six is one entry in the quartet and two in the sixteen**, because the copy index doubles it. **So the leptoquark couples to both members of the doublet with the same strength**, and that equality is again the absence of $\tau_{3}$ from the algebra. **The pairing is fixed and not chosen**: $\nu$ goes to $u$ and $e$ to $d$, never $e$ to $u$, because the vertex cannot change $\alpha$.

## The Conjugate Half, and Where the Minus Actually Sits

**The conjugate fields carry the transposed matrix with a minus, and the minus is not a convention.**

$$
\Gamma^{a}_{\imath}\bigl(\bar\xi\bigr)=-ig_{4}\gamma_{\imath}\bigl(t_{a}^{T}\otimes\mathbb{1}_{2}\bigr),
$$

**because $C^{-1}t_{a}C=-t_{a}^{T}$ for the generators of a real form.** A vertex read off the quartet half and copied to the conjugate half with the same sign is wrong on every entry, and the error is invisible in a square.

**What the minus does to the charges.** The transfer is computed the same way with the row and column exchanged, so **every entry of the conjugate half carries the opposite $B-L$**: $+\tfrac43$ where the quartet half had $-\tfrac43$. That is the statement that the sextet's six fields come in conjugate pairs, three at $+\tfrac43$ and three at $-\tfrac43$.

**The equality of the two halves' counts is a check on the transpose.** Transposing a matrix moves nonzero entries and does not create or destroy them, so $64=64$ is automatic — **and the per-family count is a check that no family is diagonal-heavy**: the corner has four entries and transposes to four.

## What the Algebra Forbids

**Three prohibitions, and each is one line of matrix arithmetic.**

1. **No generator changes the copy index.** Every array is $\mathbb 1_{2}$ on $\alpha$, so $(X\otimes\mathbb 1_{2})$ has no entry between $\alpha=1$ and $\alpha=2$. **The consequence is that no connection vertex converts a $\nu$ into an $e$ or a $u$ into a $d$**, and there is no $W$ in the model for the same reason. The copy index carries a global $\mathrm{U}(2)$ that the sector cannot see; **whether the Yukawa sector breaks it is [the Yukawa article](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html)'s question.**
2. **No generator has two entries on the lepton line.** The corner has one, the six mixed planes have one each in the $t$ row, and the spatial block has none. **So a lepton can be turned into a quark or given a phase, and not into another lepton.**
3. **No generator carries $T_{3}$.** The fifteen are $\mathbb 1$ on the copy index, so no combination of them can produce $\tau_{3}$: **$[\mathbb 1_{4}\otimes\tau_{3},X\otimes\mathbb 1_{2}]=0$ for every $X$ in the fifteen, so $\tau_{3}$ commutes with the whole algebra and is not in it.** That is the wall, and it is a commutation statement.

## What the Article Does Not Do

**No weak matrices, because there are none.** Three matrices $\mathbb 1_{4}\otimes\tau_{i}$ would sit beside the fifteen and make $88$ vertices per chirality. **They are not generators of this model**, and a table that lists them as connection vertices is a table of a different Lagrangian. **The weak sector is treated downstream**, where the second factor exists.

**No derivation of the fermion action and no loop.** The matrices are exact; the statement that a fermion propagates with them is imported. **No anomalous magnetic moment, no running coupling, no vertex correction**: all three need the loop expansion the corpus does not attempt here.

## The Checks

| check | statement | result |
| --- | --- | --- |
| entries per half | $48+12$ | $60$ |
| entries in all | $60+60$ | $120$ |
| quartet entries of the fifteen | $12\cdot2+3\cdot2$ | $30$ |
| nonzero brackets | of the $105$ pairs | $80$ |
| mixed planes | three lines, two plane types | $6$ |
| corner entries | four diagonal cells, a sum of three arrays | $4$ |
| $B-L$ transfer, mixed plane | $-1=\tfrac13-\tfrac43$ | $-1$ |
| $B-L$ per generation | $2(-1)+6(\tfrac13)$ | $0$ |
| $Q$ per generation | $0-1+3(\tfrac23)-3(\tfrac13)$ | $0$ |
| copy-index mixing | $[X\otimes\mathbb 1_{2},\mathbb 1_{4}\otimes\tau_{3}]=0$ | exact |
| trace of $D$ | $-3+1+1+1$ | $0$ |
| transposed count | nonzero entries of $t_{a}^{T}$ | $60$ |

## Summary

**The fifteen act on the sixteen as $X\otimes\mathbb 1_{2}$, and the shadow they cast has $120$ nonzero entries.** Three families and a sum, one selection rule: the spatial block does not see the lepton, the corner gives it a phase, and the six mixed planes move it to a spatial line and carry $\mp\tfrac43$ away with them.

**The copy index is where the model stops.** Every array is the identity on it, so no connection vertex can change it, and $Q$ therefore has a global half and a connection half that never meet. **That is the chiral wall, stated as a matrix fact.**

**The conjugate half is the same table with the sign flipped on every entry**, and the sextet's three-plus-three is that sign, read at the level of charges.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\xi^{\alpha}_{i}$, $\bar\xi^{i}_{\alpha}$ | the sixteen Weyl fields, quartet index slow, copy index fast |
| $\alpha$ | the copy index, the weak-doublet slot, not made local |
| $X\otimes\mathbb 1_{2}$ | an array on the quartet, uniform in the copy index |
| $D=\operatorname{diag}(-3,1,1,1)$ | the condensate direction, and $B-L=\tfrac13D$ |
| $\tau_{3}$ | the global isospin on the copy index, not a generator |
| $Q=\tau_{3}+\tfrac12(B-L)$ | the electric charge, half global and half representative |
| $t_{a}$ | the normalised generator, $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |
| $\mp\tfrac43$ | the $B-L$ a mixed plane's boson carries |

## Further Reading

- [The Feynman Rules of the $\mathrm{SU}(4)$ Model](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html). The rule this article expands, and the normalisation that precedes it.
- [The Classification of the Fermions](classification-of-the-fermions-in-the-su4-model-sixteen-weyl-fields-closed-under-c-and-cp.html). The sixteen, the $B-L$ column, and the two copies.
- [Charge Quantisation from the Fourth Line](charge-quantisation-from-the-fourth-line-one-trace-one-third.html). Why the corner is $-3$ and the three are $+1$.
- [Lepton Flavour in the $\mathrm{SU}(4)$ Model](lepton-flavour-in-the-su4-model-nothing-turns-the-lepton.html). The same prohibition, from the flavour side.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). The $80$ nonzero brackets this article quotes.
