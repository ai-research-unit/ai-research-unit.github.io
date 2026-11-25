# __The Colours in $\mathrm{SU}(3)$: A Coordinate Label on the Eight, Not a Charge__

## Introduction

**The question.** Below $M_C$ the corpus writes $r\bar g$ on eight gluons and calls them colours. **What are they, and why eight?**

**The answer.** The labels are still coordinates, and for the first time they are coordinates of a group that is gauged. **Eight is $3^{2}-1$, the rank is two, and the ninth colour–anticolour slot is not a missing gluon.** It is the $B-L$ vector, and this model already contains it.

**What this article establishes.** Why the residual group is $\mathrm{SU}(3)$ and not $\mathrm{SO}(3)$. The nine slots and the eight. The two diagonal gluons and the basis among them. That the excluded singlet is occupied, by the corner. And the four facts that are measurable against the labels that are not.

**What it does not establish.** That colour exists above $M_C$ — **it does not, and the companion article *The Colours in $\mathrm{SU}(4)$* is the half that says so**. Nor that the group is derived: the residual is $\mathrm{SU}(3)$ given the quartet, with $N_c=4-1=3$, and the measurement that confirms three is not this article's business.

**The relation between the two articles in one line.** Above $M_C$ there are fifteen coordinates and no group to be charged under. **Below it there are eight coordinates and a group.** The coordinates did not change their nature; what changed is that there is now something for them to be coordinates of.

## The Group Is $\mathrm{SU}(3)$, and the Rank Says So

**The residual is the stabiliser of the lepton line.**

$$
\mathrm{SU}(3)_c=\mathrm{Stab}_{\mathrm{SU}(4)}(e_t),
\qquad
\dim_{\mathbb R}\mathfrak{su}(3)=8,
\qquad
\operatorname{rank}\mathfrak{su}(3)=2 .
$$

**Colour is never broken.** The vacuum is $D=\operatorname{diag}(-3,1,1,1)$ in the $(\ell,r,g,b)$ order, and **on the colour block it is a multiple of the identity**, so it commutes with every matrix acting on that block:

$$
[D,X]=0\quad\text{for every colour }X .
$$

**That one line is why the eight are exactly massless below $M_C$ and not merely light.** The mass form $M^{2}_{XY}=\operatorname{tr}([X,D]^{\dagger}[Y,D])$ vanishes on all eight, and the vanishing is a symmetry statement rather than a numerical accident.

**And it is why the residual is $\mathrm{SU}(3)$ and not $\mathrm{SO}(3)$.** The rank of a group is the number of independent diagonal generators, and the two numbers differ:

| candidate residual | dimension | rank | diagonal bosons | shape |
| --- | --- | --- | --- | --- |
| $\mathrm{SU}(3)_c$ | $8$ | $2$ | $2$ | colour |
| $\mathrm{SO}(3)\cong\mathrm{SU}(2)/\mathbb Z_2$ | $3$ | $1$ | $1$ | the electroweak shape |

**A rank-one residual gives one diagonal boson, and colour has two.** The two are the standard combinations, and they are in the corpus's grid as the two diagonal cells of the $3\times3$ block. **A group that gave one would be an $\mathrm{SU}(2)$ in disguise**, which is the shape the weak sector takes and not this one.

**The check is arithmetic and does not need the groups named.** The colour block is $3\times3$, so it has three diagonal cells; one combination is removed; **two remain.** A rank-one group would have one diagonal, and no arrangement of a $3\times3$ grid produces that.

## The Nine Slots and the Eight

**Colour–anticolour is the tensor product of the triplet with its conjugate, and it is reducible.**

$$
\mathbf 3\otimes\bar{\mathbf3}=\mathbf 8\oplus\mathbf 1,
\qquad
8+1=9 .
$$

**Nine slots, eight gluons, and the ninth is the singlet.** The count is the whole content of the phrase *one fewer on the diagonal*, and it is worth printing the nine before subtracting anything.

| slot | where it sits | in the octet |
| --- | --- | --- |
| $r\bar g$, $r\bar b$, $g\bar r$, $g\bar b$, $b\bar r$, $b\bar g$ | the six off-diagonal cells | yes |
| $r\bar r$, $g\bar g$, $b\bar b$ | the three diagonal cells | two combinations yes, the third no |
| the trace $r\bar r+g\bar g+b\bar b$ | the sum of the three | **no, this is the singlet** |

**The six off-diagonal slots are four independent generators plus their reverses** — six directions, three planes, two amplitudes per plane. **The three diagonal slots are three directions, of which the trace is not a generator of $\mathrm{SU}(3)$**, because $\mathfrak{su}(3)$ is traceless.

**So the diagonal carries two gluons and not three**, and the reason is not a choice of basis: **the removed direction is the one the $S$ in $\mathrm{SU}$ removes.** A reader who rotates the three colour lines freely will move the two gluons among the diagonal cells, and will not produce a third.

**The count, twice.**

$$
\underbrace{6}_{\text{off-diagonal}}+\underbrace{2}_{\text{diagonal}}=8=\underbrace{3^{2}-1}_{\dim\mathfrak{su}(3)} .
$$

## The Two Diagonal Gluons, and Why the Pair Is Not Canonical

**The invariant statement comes first, because it is the one that can be checked without choosing a pair.** A general element of the Cartan is $a\,iD+b\,d_{2}+c\,d_{3}$, and its entry on the lepton line is

$$
\bigl(a\,iD+b\,d_{2}+c\,d_{3}\bigr)_{\ell\ell}=-3ia+0+0 .
$$

**That entry vanishes if and only if $a=0$.** So the Cartan directions that lie inside the colour block are exactly the span of $d_{2}$ and $d_{3}$, and that span is two-dimensional. **That, and not any choice of pair, is what "two of the three diagonals stay inside the octet" means.** The third direction is the only one that touches the lepton line, and it is the one that leaves.

**The printed arrays, and the words they come from.** The diagonal words are $\ell_{j}r_{j}$, and each is a signed permutation with an eigenvalue $-1$ on the $\{t,j\}$ block:

$$
W_{xx}=\operatorname{diag}(-1,-1,1,1),\quad
W_{yy}=\operatorname{diag}(-1,1,-1,1),\quad
W_{zz}=\operatorname{diag}(-1,1,1,-1).
$$

**Their sum is the vacuum direction**, $W_{xx}+W_{yy}+W_{zz}=\operatorname{diag}(-3,1,1,1)=D$, which is why $iD=i\sum_{j}W_{jj}$ is traceless and why the sum is taken rather than the differences. **The two differences give**

$$
d_{2}=\tfrac{i}{2}\bigl(W_{yy}-W_{xx}\bigr)=\operatorname{diag}(0,i,-i,0),
\qquad
d_{3}=\tfrac{i}{2}\bigl(W_{zz}-W_{yy}\bigr)=\operatorname{diag}(0,0,i,-i).
$$

**Compare them with Gell-Mann, and the comparison is exact and worth doing in two steps.**

$$
d_{2}=i\,\lambda_{3}^{\mathrm{emb}},
\qquad
d_{3}=i\Bigl(-\tfrac12\lambda_{3}^{\mathrm{emb}}+\tfrac{\sqrt3}{2}\lambda_{8}^{\mathrm{emb}}\Bigr),
$$

**with $\lambda_{3}^{\mathrm{emb}}=\operatorname{diag}(0,1,-1,0)$ and $\lambda_{8}^{\mathrm{emb}}=\tfrac{1}{\sqrt3}\operatorname{diag}(0,1,1,-2)$.** Three things follow, and each corrects a natural guess.

- **The factor $i$ is a convention, not a rescaling.** The corpus's generators are anti-Hermitian and Gell-Mann's are Hermitian; $d_{a}=i\,(\text{real symmetric})$ throughout, exactly as the planes are $iS_{jk}$.
- **The individual norms agree.** $\operatorname{tr}(d_{a}^{\dagger}d_{a})=2$ and $\operatorname{tr}(\lambda_{a}\lambda_{b})=2\delta_{ab}$, so $d_{2}$ is *literally* $i\lambda_{3}^{\mathrm{emb}}$ and no normalisation differs between the two conventions.
- **The change of basis is not orthogonal.** $d_{3}$ is a unit-coefficient combination of the two, and $\operatorname{tr}(d_{2}^{\dagger}d_{3})=-1$, so the corpus's pair is a **sheared** basis of the same plane, not a rotated one.

**The Gram, stated as a matrix.** In the pairing $-\operatorname{tr}(XY)$ on anti-Hermitian arrays,

$$
G=\begin{pmatrix}\operatorname{tr}(d_{2}^{\dagger}d_{2}) & \operatorname{tr}(d_{2}^{\dagger}d_{3})\\[2pt] \operatorname{tr}(d_{3}^{\dagger}d_{2}) & \operatorname{tr}(d_{3}^{\dagger}d_{3})\end{pmatrix}
=\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix},
$$

**with $\det G=3$ and eigenvalues $1$ and $3$.** Positive definite, so the pair is a genuine basis; not diagonal, so it is not an orthogonal one. **Both statements matter**: the first is why the two are linearly independent and the space is truly two-dimensional, the second is why "the two diagonal gluons" is a phrase with an asterisk.

**The corpus says exactly this, in one sentence worth quoting.** $\operatorname{tr}(d_{2}d_{3})=+1$ is, in its own words, *the array form of the statement that a colour basis is a choice and the algebra is not.* **That is this article's thesis one scale down**, and it is the reason the pair needs no defence.

**An orthogonal pair is one rotation away, and the rotation is free.** $G$ is positive definite and $2\times2$, so a single rotation diagonalises it; the result is $(\lambda_{3},\lambda_{8})$ up to signs and order. **Nothing computed from the octet depends on which of the two pairs a calculation starts from**, because both span the same two-dimensional space and the Casimirs are traces over the whole algebra.

### What Is Less Certain Below $M_C$, Said Plainly

**The construction above $M_C$ is uniform, and that is why the labels there are unambiguous.** One rule, $W_{\mu\nu}=\ell_{\mu}r_{\nu}$, produces one word per generator; the planes are sums and differences of words; **every one of the fifteen is exactly one word or one combination of two, and the rule never consults a basis of the Cartan.** That is what makes "cell $(i,j)$" a well-defined address above $M_C$.

**Below $M_C$ the octet inherits a basis that was chosen for a different purpose.** The pair $(d_{2},d_{3})$ exists because the colour block is chained $x\to y\to z$ and the two successive differences were taken. **Chain it $z\to y\to x$ and you get another non-orthogonal pair spanning the same plane.** So:

| object | status below $M_C$ |
| --- | --- |
| the two-dimensional colour-block Cartan | invariant |
| the split $2+1$ | invariant |
| the direction that leaves, $iD$ | invariant up to scale |
| the pair $(d_{2},d_{3})$ | a by-product of the chain order |
| the pair $(\lambda_{3},\lambda_{8})$ | an orthogonal basis of the same plane |
| the names "the two diagonal gluons" | a name for whichever pair is in use |

**So the phrase "the two diagonal gluons" is not canonical, and the honest statement says so.** What is canonical is *the two-dimensional space of diagonal generators that act only on colour*. **A reader who wants a canonical pair should fix an orthogonal one; a reader who wants to reproduce the corpus's arrays should use $d_{2}$ and $d_{3}$ and carry the $-1$ in the Gram.** Neither choice is more physical.

**One asymmetry is worth naming, because it is why the corpus's choice looks half-familiar.** $d_{2}$ is exactly $i\lambda_{3}^{\mathrm{emb}}$: the chain starts at the $x$–$y$ difference, and that difference *is* Gell-Mann's third generator. **$d_{3}$ is where the shear enters**, because it takes the difference of the next pair rather than the trace-orthogonal complement. **A reader who checks only $d_{2}$ against $\lambda_{3}$ will conclude the two conventions agree, and will be right about that entry and wrong about the pair.**

**And this is the sense in which the two phases differ in kind.** Above $M_C$ the labels are addresses in a grid whose construction never needed a Cartan basis, so the question "which pair?" does not arise. **Below $M_C$ the group is unbroken and its adjoint is split into an octet and a singlet, and that split forces a choice of Cartan basis on us.** The choice is free; the split is not.

## The Ninth Slot Is the $B-L$ Vector, and That Is Why the Grid Closes

**This model does not leave the singlet empty. It puts the corner in it.**

**Take the colour-block identity and complete it tracelessly in four dimensions.** The colour-block identity is $\operatorname{diag}(0,1,1,1)$ in the $(\ell,r,g,b)$ order — zero on the lepton line, one on each colour line — and its trace is three, so it is not a generator of $\mathfrak{su}(4)$. **Subtract a quarter of the $4\times4$ identity:**

$$
\operatorname{diag}(0,1,1,1)-\tfrac34\,\mathbb 1
=\bigl(-\tfrac34,\tfrac14,\tfrac14,\tfrac14\bigr)
=\tfrac14\operatorname{diag}(-3,1,1,1)
=\tfrac14 D .
$$

**The ninth slot, made traceless, is the corner.** The colour-block trace and the $B-L$ direction are one direction once the four-dimensional trace is removed, and **that identification is the reason the grid holds fifteen generators and not sixteen.**

**So the singlet is not an absent gluon. It is a different particle.** Three properties separate it from the octet, and each is checkable:

| property | the eight | the singlet |
| --- | --- | --- |
| the algebra | non-abelian, self-coupling | abelian, no self-coupling |
| the coupling | the strong coupling | its own, and it mixes downstream |
| the fate below $M_C$ | massless, and it stays massless | massless until a second vacuum mixes it |

**And the words matter here.** The singlet is a gauge boson of the unbroken colour group in the same sense that the eight are — **but it is not a gluon**, because a gluon is a boson of the non-abelian factor. **Calling it a ninth gluon would be the same error as calling the photon a fourth weak boson**: the count of the factor's adjoint is eight, and the ninth slot belongs to a different factor.

**The objection, named before it is answered.** *If the singlet is the $B-L$ boson, is the exclusion of the singlet not a bookkeeping artefact?* **No, and the arithmetic shows why.** The exclusion is the statement $\dim\mathfrak{su}(3)=8$ rather than $9$; the model happens to possess a ninth vector, and that vector is not in the adjoint of $\mathrm{SU}(3)$. **A theory with a $\mathrm{U}(3)$ gauge group would have nine, and would be a different theory with a different spectrum.**

## The Labels Are Coordinates Here Too

**Nothing about the previous article's argument changes at $M_C$.** The gauge field is still $A_\mu=\sum_{a}A^{a}_\mu t_{a}$, the index is still a coordinate, and a gauge transformation still rotates the components:

$$
A_\mu\ \longmapsto\ U A_\mu U^{\dagger}+\tfrac{i}{g_3}U\partial_\mu U^{\dagger},
\qquad
A^{a}_\mu\ \longmapsto\ R^{ab}A^{b}_\mu+\text{inhomogeneous}.
$$

**A field carrying $r\bar g$ in one gauge carries a combination of all eight in another.** The label is a coordinate on the adjoint, and **a coordinate that a symmetry rotates away is not a property of a particle.**

**What changed at $M_C$ is not the status of the label. It is the status of the group.** Above the transition the coordinates were coordinates of a basis with no factor attached; below it they are coordinates of a factor that is gauged and unbroken. **The map became a map of something.**

**And that is why QCD may talk about colour at all.** The coordinate is conventional; the structure it coordinatises is measured. **The invariants are the measurable part**, and each is computed from the dimension and the rank with no reference to a letter:

$$
C_{F}=\frac{N^{2}-1}{2N}=\frac43,
\qquad
C_{A}=N=3,
\qquad
T_{R}=\tfrac12 .
$$

**These three are structural**: they follow from $N=3$ alone, which is why they may be printed here, and the measurement that fixes $N=3$ is not this article's subject. **What no experiment can decide is whether the third colour is called blue**, because a relabelling of the three lines is an automorphism of the description and not a change in the world.

## What Is Real and What Is Chosen

**Four facts, and each is checkable without naming a colour.**

$$
\boxed{\;
G=\mathrm{SU}(3)_c,\qquad
\dim_{\mathbb R}\mathfrak g=8,\qquad
\operatorname{rank}\mathfrak g=2,\qquad
\text{the singlet excluded}
\;}
$$

**What is chosen is everything a relabelling of the three lines can move.**

| object | status |
| --- | --- |
| the letters $r,g,b$ | notation |
| the label $r\bar g$ of a given slot | a coordinate |
| which two combinations are $\lambda_{3}$ and $\lambda_{8}$ | one basis of a two-dimensional space |
| which diagonal slot is called the missing one | a basis statement |
| the pair $(d_{2},d_{3})$, non-orthogonal, against $(\lambda_{3},\lambda_{8})$ | a sheared basis of one plane |

**The test is the one the companion article states, applied one size down.** Take a sentence with a colour word, relabel the three lines, ask what survives. **The dimension, the rank, the exclusion of the singlet and the three Casimirs survive. The letters do not.**

## The Rank Ledger: $3=2+1$

**"The rank drops from three to two" is true of the simple factor and false of the algebra**, and the difference is worth one paragraph because it is the commonest slip.

$$
\operatorname{rank}\mathfrak{su}(4)=3,
\qquad
\operatorname{rank}\bigl(\mathfrak{su}(3)\oplus\mathfrak u(1)\bigr)=2+1=3 .
$$

**The total rank is preserved at this breaking.** One diagonal direction leaves the simple factor and becomes an abelian factor of its own, so the count of diagonal directions is the same before and after. **Rank is monotone downwards inside an algebra and additive across factors**, and this transition does both at once: $\mathfrak{su}(4)\to\mathfrak{su}(3)$ loses one, and $\mathfrak{su}(3)\to\mathfrak{su}(3)\oplus\mathfrak u(1)$ gains one back.

**The ledger closes at three, and it must.** A breaking that removed a diagonal direction and added nothing would leave a rank-two algebra with a rank-three's worth of Cartan directions, which is impossible. **The corner is where the third direction goes**, which is the same statement as the previous section's identification, read on the ranks instead of the cells.

## The Checks

| check | arithmetic | result |
| --- | --- | --- |
| slots of the tensor product | $3\times3$ | $9$ |
| the adjoint | $3^{2}-1$ | $8$ |
| the singlet | $9-8$ | $1$ |
| the octet's composition | six off-diagonal $+$ two diagonal | $8$ |
| the diagonal cells | three cells, one trace removed | $2$ |
| the dimension | $3^{2}-1$ | $8=\dim\mathfrak{su}(3)$ |
| the rank | independent diagonal directions | $2$ |
| the rank ledger | $2+1$ | $3=\operatorname{rank}\mathfrak{su}(4)$ |
| the kernel at $M_C$ | six off-diagonal $+$ two diagonal $+$ the corner | $6+2+1=9=\dim\mathfrak u(3)$ |
| the singlet's identity | $\operatorname{diag}(0,1,1,1)-\tfrac34\mathbb 1$ | $\tfrac14 D$ |
| the eight's mass | $[D,X]=0$ on the colour block | $0$, exact |
| the sextet's mass | $D$ differs across the lepton line | $32v^{2}$ |
| the fundamental Casimir | $(9-1)/(2\cdot3)$ | $4/3$ |
| the adjoint Casimir | $N$ at $N=3$ | $3$ |
| the lepton-line entry of the Cartan | $a\,iD+b\,d_{2}+c\,d_{3}\mapsto-3ia$ | zero iff $a=0$ |
| the colour-block Cartan | span of the two with zero lepton entry | $2$ |
| the Gram of the pair | $\det\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ | $3>0$, so a basis |
| the Gram's eigenvalues | $\lambda^{2}-4\lambda+3$ | $1$ and $3$, not degenerate |
| $d_{2}$ against Gell-Mann | $d_{2}=i\lambda_{3}^{\mathrm{emb}}$ | exact |
| the individual norms | $\operatorname{tr}(d_{a}^{\dagger}d_{a})$ and $\operatorname{tr}(\lambda_{a}\lambda_{b})=2\delta_{ab}$ | $2=2$, no rescaling |
| a rank-one residual would give | one diagonal boson | not colour |

## Summary

**Eight, rank two, singlet excluded.** The phrase *one fewer on the diagonal* is the arithmetic $9\to8$, and it is the same arithmetic as the companion article's $16\to15$ applied one size down. **The dimension, the rank and the exclusion are invariant; the letters and the choice of basis are not.**

**The residual is $\mathrm{SU}(3)$ and not $\mathrm{SO}(3)$, and the rank is the test.** Two diagonal bosons require rank two, and a rank-one group has one. **Colour is never broken at $M_C$**, which is why the eight are exact zeros of the mass matrix rather than small ones.

**The ninth slot is occupied.** The colour-block identity, completed tracelessly in four dimensions, is the corner $D/4$; the singlet is therefore the $B-L$ vector and not a missing gluon. **That identification is why fifteen generators and not sixteen**, and it is the sharpest link between the two articles.

**The two diagonal gluons are a space, not a pair.** The Cartan directions inside the colour block are exactly those with zero lepton-line entry, so the space is two-dimensional and that is invariant; the pair $(d_{2},d_{3})$ is a non-orthogonal basis of it, with $\operatorname{tr}(d_{2}^{\dagger}d_{3})=-1$ and Gram eigenvalues $1$ and $3$. **$d_{2}$ is exactly $i\lambda_{3}^{\mathrm{emb}}$ and the norms agree term by term**, so the conventions differ by a shear and not by a rescaling — a fact that misleads anyone who checks only the first entry.

**The labels are coordinates below $M_C$ as they were above it.** What changed is that the group is now gauged, so the invariants computed from the coordinates are measurable. **The map became a map of something, and the territory is the group.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $(\ell,r,g,b)$ | the four lines, in the order the vacuum uses |
| $\mathrm{SU}(3)_c$ | $\mathrm{Stab}_{\mathrm{SU}(4)}(e_t)$, the unbroken colour factor, dimension $8$, rank $2$ |
| $\mathfrak u(3)$ | $\mathfrak{su}(3)_c\oplus\mathfrak u(1)_{B-L}$, the kernel of $\operatorname{ad}(iD)$, dimension $9$ |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the vacuum's direction |
| $B-L$ | $\tfrac13 D$, the abelian factor's generator |
| $d_{2}$, $d_{3}$ | the corpus's two colour diagonals, $\operatorname{diag}(0,i,-i,0)$ and $\operatorname{diag}(0,0,i,-i)$ |
| $\lambda_{3}^{\mathrm{emb}}$, $\lambda_{8}^{\mathrm{emb}}$ | Gell-Mann's two, embedded on the colour block: $d_{2}=i\lambda_{3}^{\mathrm{emb}}$, $d_{3}$ a unit combination of both |
| $G$ | the Gram matrix $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ of the corpus's pair, $\det=3$ |
| $C_{F}$, $C_{A}$, $T_{R}$ | the three Casimirs, fixed by $N=3$ |
| $\mathbf 8$, $\mathbf 1$ | the adjoint and the singlet of the tensor product |

## Further Reading

- [The Colours in $\mathrm{SU}(4)$: A Coordinate Label on the Fifteen, Not a Charge](the-colours-in-su4-a-coordinate-label-on-the-fifteen-not-a-charge.html), the first half: the fifteen flat labels and why none is a charge.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html), for $\operatorname{ad}(iD)$, its spectrum $0^{9}\oplus(\pm4i)^{3}$ and the kernel $\mathfrak u(3)$.
- [Classification of the Bosons in the $\mathrm{SU}(4)$ Model](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html), for the grid and the octet's $6+2$ read as cells.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$](quantum-chromodynamics-as-the-residual-of-su4.html), for what the corpus does and does not reach of QCD, and for the status of $N_c=3$ as imported.
- [The Centraliser, the Complement, and the Index](the-centraliser-the-complement-and-the-index-dimension-and-rank.html), for rank monotone downwards inside an algebra and additive across factors.
