# __The Adjoint Mass Matrix of the Fifteen: One Number per Plane, $32v^2$ on Six and Zero on Nine__

## Introduction

**One scalar direction, one matrix, fifteen numbers of which six are not zero.** The fifteen generators of $\mathfrak{su}(4)$ acquire masses from the vacuum of the scalar that breaks $\mathrm{SU}(4)$, and the object that carries them is the adjoint mass matrix
$$
M^{2}_{XY}=\operatorname{tr}\bigl([X,\Phi_0]^{\dagger}[Y,\Phi_0]\bigr),\qquad \Phi_0=vD,\qquad D=\operatorname{diag}(-3,1,1,1).
$$
**In the physics basis it is diagonal, with one value per plane**, and the value is $2v^{2}$ times the square of the difference of two eigenvalues of $D$:
$$
M^{2}=2v^{2}\bigl(\lambda_j-\lambda_k\bigr)^{2}\ \text{ on the plane }\{j,k\},\qquad \lambda=\operatorname{eig}(D).
$$
**Evaluated, that is one display.**
$$
M^{2}=\operatorname{diag}\bigl(\underbrace{32v^{2},\dots,32v^{2}}_{6},\underbrace{0,\dots,0}_{9}\bigr).
$$

**The six are the leptoquark planes and the nine are colour plus the corner.** A plane here is one array: the three geometric pairs $\{t,a\}$ each carry a real array $A_{ta}$ and an imaginary one $iS_{ta}$, so three pairs make the six. The nine are not "small": they are exactly zero, they are closed under the bracket, and they are the algebra that the first breaking leaves standing. **The article computes the matrix entry by entry, says why six and not nine, checks that the corpus's two bases give the same masses, and separates one artefact that a recomputation is likely to produce.** It does not compute the second breaking's mixing and it does not fix a coupling.

**The whole content is one lemma.** The commutator of a plane array with a diagonal is the other plane array of the same pair, times the difference of two eigenvalues. **Everything below is that sentence applied six times.**

## The Definition, and Two Conventions That Turn Out to Be One

**Where the matrix comes from.** The scalar kinetic term contains $[A_\mu,\Phi]$, and a generator that commutes with the vacuum does not appear in it. **Write the gauge field as $A_\mu=A^{X}_{\mu}X$ over a basis of the adjoint, put $\Phi=\Phi_0+\eta$, and the piece quadratic in the gauge field and quadratic in $v$ is**
$$
\mathcal{L}\supset\tfrac12\,g^{2}\,A^{X}_{\mu}\,M^{2}_{XY}\,A^{Y\mu},\qquad M^{2}_{XY}=\operatorname{tr}\bigl([X,\Phi_0]^{\dagger}[Y,\Phi_0]\bigr).
$$
**The commutator is the whole mechanism**: a generator that does not move the vacuum has no mass, and one that moves it has a mass proportional to how far it moves it.

**Two conventions, and they are the same matrix.** The corpus writes the vacuum as $vD$ with $D$ Hermitian, and the structures note writes it as $v\,iD$ with $iD$ anti-Hermitian and takes the real part of the trace. **The two agree identically.** When $\Phi_0$ is Hermitian and $X$ anti-Hermitian, $[X,\Phi_0]$ is anti-Hermitian, so $[X,\Phi_0]^{\dagger}=-[X,\Phi_0]$ and
$$
\operatorname{tr}\bigl([X,\Phi_0]^{\dagger}[Y,\Phi_0]\bigr)=-\operatorname{tr}\bigl([X,\Phi_0][Y,\Phi_0]\bigr)=\operatorname{Re}\operatorname{tr}\bigl([X,\Phi_0]^{\dagger}[Y,\Phi_0]\bigr),
$$
**so the $D$ form is already real and no $\operatorname{Re}$ is needed.** Computed on all $225$ pairs of the fifteen the two forms agree entry by entry, and the $D$ form has no imaginary part at all. **A reader who compares the two formulas has found a change of letter, not a discrepancy.**

**What is factored out, and what is not.** Three things sit outside $M^{2}$ and none of them is computed here: the coupling $g^{2}$, the $\tfrac12$ of the mass-term normalisation, and the field normalisation, which enters through $\operatorname{tr}(X^{\dagger}X)$. **The entries below are the trace form of the arrays exactly as the AXF article prints them**, and every ratio of masses is independent of those three factors.

## The Commutator Lemma: One Plane Array Against the Corner

**The corner is diagonal, so the commutator of a matrix unit is one entry.** With $E_{jk}$ the matrix unit, $\lambda=\operatorname{eig}(D)$ and $D$ diagonal,
$$
[E_{jk},D]=\bigl(\lambda_k-\lambda_j\bigr)E_{jk}.
$$
**Antisymmetrising and symmetrising that line gives the two plane arrays of the pair**, because the coefficient is the same on both entries only if the array is taken symmetric:
$$
[A_{jk},D]=\bigl(\lambda_k-\lambda_j\bigr)S_{jk},\qquad [S_{jk},D]=\bigl(\lambda_k-\lambda_j\bigr)A_{jk},\qquad [iS_{jk},D]=i\bigl(\lambda_k-\lambda_j\bigr)A_{jk}.
$$
**So the commutator of a plane array never leaves its pair**: it exchanges the real plane and the imaginary one and multiplies by $\Delta\lambda_{jk}:=\lambda_k-\lambda_j$. Six planes, six coefficients, computed:

| plane $\{j,k\}$ | $\Delta\lambda_{jk}$ | $[A_{jk},D]$ | $[iS_{jk},D]$ |
| --- | --- | --- | --- |
| $\{t,x\},\{t,y\},\{t,z\}$ | $+4$ | $\pm4S_{ta}$ | $\pm4iA_{ta}$ |
| $\{x,y\},\{x,z\},\{y,z\}$ | $0$ | $0$ | $0$ |

**The zero row is colour.** $D$ is $1$ on all three colour lines, so a colour plane's two eigenvalues are equal and its commutator vanishes — **not because colour is special in the algebra, but because that one array is a multiple of the identity there.** The $+4$ row is the lepton line: $-3$ against $+1$.

**Two traces finish the computation.** $\operatorname{tr}(A_{jk}^{2})=-2$, $\operatorname{tr}(S_{jk}^{2})=+2$ and $\operatorname{tr}(A_{jk}S_{jk})=0$ for all six planes, so the $2\times2$ block of one pair is already diagonal and its two entries are equal:
$$
M^{2}\Big|_{\{j,k\}}=2v^{2}\bigl(\Delta\lambda_{jk}\bigr)^{2}\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$
**The vanishing of $\operatorname{tr}(A_{jk}S_{jk})$ is why no pair mixes**, and it is a one-line computation rather than a theorem: an antisymmetric matrix against a symmetric one, in the same two-plane, gives zero.

## The Fifteen-by-Fifteen, in the Physics Basis

**The ordering is the one of the AXF article**: $A_{tx},A_{ty},A_{tz},A_{xy},A_{xz},A_{yz},iS_{tx},iS_{ty},iS_{tz},iS_{xy},iS_{xz},iS_{yz},iD,d_2,d_3$. **Fifteen rows, one number each, and everything off the diagonal is zero.**

| array | plane | $\Delta\lambda$ | $M^{2}$ |
| --- | --- | --- | --- |
| $A_{tx},A_{ty},A_{tz}$ | $\{t,a\}$, leptoquark | $+4$ | $32v^{2}$ |
| $A_{xy},A_{xz},A_{yz}$ | $\{b,c\}$, colour | $0$ | $0$ |
| $iS_{tx},iS_{ty},iS_{tz}$ | $\{t,a\}$, leptoquark | $+4$ | $32v^{2}$ |
| $iS_{xy},iS_{xz},iS_{yz}$ | $\{b,c\}$, colour | $0$ | $0$ |
| $iD$ | the corner | $-$ | $0$ |
| $d_2,d_3$ | colour diagonals | $-$ | $0$ |

**Three statements about that table, each checked separately.** The matrix is diagonal: $0$ in all $225-15=210$ off-diagonal entries. It is real and Hermitian: the largest imaginary part is $0$, so the $D$ and $iD$ conventions do not even differ by a phase here. And its rank is $6$: six equal entries, nine zeros.

**The kernel is the unbroken algebra, and this is the sentence that makes the nine a result.** The arrays annihilated by $[\,\cdot\,,D]$ are the nine with zero mass: the six colour planes, the two colour diagonals, and the corner. **They span a nine-dimensional subspace, they are exactly $\mathfrak{su}(3)\oplus\mathfrak{u}(1)_{B-L}$, and they are closed under the bracket** — all $81$ brackets of the nine land back in the nine, with a residual of $1.2\times10^{-15}$. **A mass matrix whose kernel is a subalgebra is the matrix statement that the breaking leaves a group standing.**

**The two zero rows have two different reasons, and the table does not distinguish them.** The colour planes are zero because $\Delta\lambda=0$, a degeneracy of the vacuum along the colour triple. The corner and the colour diagonals are zero because those arrays are themselves diagonal, so they commute with $D$ identically: $[iD,D]=0$. **One is a degeneracy; the other is a commutation.** Both are exact, and both are visible only because the basis separates them.

## Why Six and Not Nine: The Lepton Line Is the Only Departure

**Read $32$ off the eigenvalues.** $32=2\times4^{2}$, and $4=1-(-3)$ is a colour eigenvalue minus the lepton eigenvalue. **The lepton line is the one place where $D$ departs from a multiple of the identity, and a plane's mass is the square of that departure across it**: a plane touching the lepton line sees it, a plane inside the colour triple does not, and a direction along a line cannot see a departure at all.

**This is why the six massive gauge bosons are the only coloured ones.** Every massive plane contains the lepton index $t$, so every massive generator moves the lepton line into colour; those are the six leptoquarks, three real planes and three imaginary planes, two amplitudes each. **The eight colour generators and the corner stay massless at this scale, and no statement about the group is needed to see it** — one eigenvalue of one array is enough.

**The homogeneity is also the reason the number is $32$ and not something else.** A vacuum proportional to the identity would commute with everything and break nothing; the trace-zero condition forces the corner to be $\operatorname{diag}(-3,1,1,1)$ up to scale and sign, so $4$ is not a parameter but the only difference available. **Change the normalisation of $D$ and every entry scales by its square; change the direction and the pattern of six and nine changes with it.**

## The Same Operator in the Maths Base: Six Rank-One Blocks

**The maths base is the fifteen words taken as they are**, $\ell_a$, $r_a$, $iN_{bc}$. **The same matrix there is not diagonal**, and that is the whole content of the pair-resolution argument: it is block diagonal in six $2\times2$ blocks, each of rank one.

| block | the matrix, in units of $v^{2}$ | eigenvalues |
| --- | --- | --- |
| $(\ell_a,r_a)$, three blocks | $32\begin{pmatrix}1&1\\1&1\end{pmatrix}$ | $0$, $64$ |
| $(iN_{bc},iN_{cb})$, three blocks | $32\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ | $0$, $64$ |
| $iN_{xx},iN_{yy},iN_{zz}$ | $0$ | $0$ |

**Twenty-four non-zero entries out of $225$, twelve of them on the diagonal — two in each block — and six eigenvalues equal to $64v^{2}$.** The reason for the factor two against the physics base is the block, not the physics: $32[[1,1],[1,1]]$ has eigenvalue $64$ on its eigenline, while the physics base puts the two normalised arrays on the two eigenlines and reads $32$ twice. **The physics base is the basis in which the matrix is already diagonal, which is why the pair resolution was worth spending a choice on.**

**Raise the index and the two bases give one number.** The Gram entries are $\operatorname{tr}(X^{\dagger}X)=2$ for each physics array ($12$ for $iD$, whose mass is zero) and $4$ for each word. **Dividing the entry by the Gram entry gives $32/2=16$ and $64/4=16$.** The remaining factors, $g^{2}$, the $\tfrac12$ and the field normalisation, are common to every entry and cancel in every ratio. **No basis change can move a mass, and the two displays are one matrix written twice.**

**The three diagonal words carry nothing, and that is a statement about $D$ too.** $iN_{xx}+iN_{yy}+iN_{zz}=iD$ is the vacuum itself, so the three commute with it: a direction along a diagonal cannot see a diagonal.

## The Caveat: $8v^{2}$ on the Carrier Is an Artefact

**The scalar that breaks $\mathrm{SU}(4)$ is a singlet of $\mathrm{SU}(2)_L$.** Its vacuum is a direction in the quartet, and the left triple acts on the doublet factor, not on the quartet. **So $T^{L}_{a}$ does not move $\Phi_0$ in the model, and the first breaking does not touch $W_L$.**

**A recomputation on the carrier will say otherwise, and the number it produces is $8v^{2}$.** Take $T^{L}_{x}=\tfrac12\ell_x$ as a four-row array acting on the quartet, and compute the same trace:
$$
\operatorname{tr}\bigl([T^{L}_{x},\Phi_0]^{\dagger}[T^{L}_{x},\Phi_0]\bigr)=8v^{2}.
$$
**Read the arithmetic and the artefact is visible.** $[\ell_x,D]=4S_{tx}$, so $[T^{L}_{x},D]=2S_{tx}$, and $4\operatorname{tr}(S_{tx}^{2})=4\times2=8$. **The factor $\tfrac14$ between $8$ and $32$ is the half in $T^{L}_{x}$ appearing twice**, and it is a warning about which carrier the array is being read on, not a mass. **The six weak generators are not in the fifteen**; on the carrier they are sums of colour and leptoquark planes, and their masses come from the second breaking through the doublet vacuum, not from this one.

## What the Matrix Does Not Say

**It says nothing about a coupling.** All three gauge couplings of the model are symbolic, so $32v^{2}$ is a coefficient of $v^{2}$ and not a number in kilograms. **The coupling sector is a separate ledger.**

**It says nothing about the corner's eventual mass.** $[iD,D]=0$ is exact at this scale. The $B-L$ boson acquires a mass only through the mixing that produces $\gamma$, $Z$ and $Z_R$, and that mixing is computed in [The Breaking Chain](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html), not here.

**It says nothing about the second breaking's spectrum.** The right triple, the doublet vacuum and the neutral mixing are the next step, and their masses are coefficients of a different scale.

## The Checks

Sixteen recomputations, at $\operatorname{tr}$ in the fundamental, quartet ordered $(t,x,y,z)$, product fixed by $\vec e_x\vec e_y=\vec e_z$, vacuum $\Phi_0=vD$ with $D=\operatorname{diag}(-3,1,1,1)$ and $v=1$.

| check | result |
| --- | --- |
| the fifteen distinct, anti-Hermitian, traceless | $15/15$ |
| $[A_{jk},D]=\Delta\lambda_{jk}S_{jk}$ | $6/6$ exact |
| $[S_{jk},D]=\Delta\lambda_{jk}A_{jk}$ / $[iS_{jk},D]=i\Delta\lambda_{jk}A_{jk}$ | $6/6$ / $6/6$ exact |
| $\Delta\lambda=+4$ on the three $t$-planes, $0$ on the three colour planes | $6/6$ |
| $\operatorname{tr}(A^{2})=-2$, $\operatorname{tr}(S^{2})=+2$, $\operatorname{tr}(AS)=0$ | $6/6$ each |
| the six $2\times2$ blocks | $32\operatorname{I}_2$ on the $t$-planes, $0$ on the colour planes |
| $M^{2}$ off-diagonal entries | $0$ in all $210$ |
| $M^{2}$ real and Hermitian | no imaginary part, $M^{2}=M^{2\dagger}$ |
| rank of $M^{2}$ | $6$ |
| kernel dimension, and the kernel named | $9$: six colour planes, $d_2$, $d_3$, $iD$ |
| kernel closed under the bracket | $81/81$, residual $1.2\times10^{-15}$ |
| the $D$ form against the $iD$ form with $\operatorname{Re}$ | $225/225$ agree |
| maths-base blocks $32[[1,1],[1,1]]$ / $32[[1,-1],[-1,1]]$ | $3/3$ / $3/3$ |
| maths-base spectrum, and Gram entries | $64v^{2}$ six times; $4$ per word |
| raised index, both bases | $64/4=32/2=16$ |
| $\operatorname{tr}([T^{L}_{x},\Phi_0]^{\dagger}[T^{L}_{x},\Phi_0])$ on the carrier | $8v^{2}$, the artefact |

## Summary

**The adjoint mass matrix of the fifteen is one number per plane, and the number is $2v^{2}$ times the square of the eigenvalue difference across the plane.** On the vacuum $\operatorname{diag}(-3,1,1,1)$ that is $32v^{2}$ on the six planes through the lepton line and exactly zero on the nine that avoid it.

**Six and nine are one difference.** The lepton line is the only departure of $D$ from a multiple of the identity, so a plane that touches it is heavy and a plane that does not is massless; the corner and the colour diagonals are massless for the second, exact reason that they commute with $D$. **The nine-dimensional kernel is the unbroken $\mathfrak{su}(3)\oplus\mathfrak{u}(1)_{B-L}$, and it is closed under the bracket.**

**The physics base is the basis in which the matrix is diagonal**, the maths base is the basis in which it is six rank-one blocks, and the two are one matrix: $32$ against $64$ with Gram $2$ against $4$ gives $16$ either way. **The one number that a recomputation produces wrongly is $8v^{2}$ for $W_L$ on the carrier, and it is the half in $T^{L}_{x}$ appearing twice.**

## Summary of Notation

| symbol | what it is |
| --- | --- |
| $X,Y$ | two of the fifteen, in the physics basis unless said otherwise |
| $\Phi_0=vD$ | the vacuum of the scalar that breaks $\mathrm{SU}(4)$, along the lepton line |
| $D=\operatorname{diag}(-3,1,1,1)$ | the corner, with $B-L=\tfrac13D$ |
| $\lambda_j$ | the eigenvalue of $D$ on the base vector $e_j$ |
| $\Delta\lambda_{jk}=\lambda_k-\lambda_j$ | the departure across the plane $\{j,k\}$; $+4$ through $t$, $0$ in colour |
| $M^{2}_{XY}$ | the adjoint mass matrix $\operatorname{tr}([X,\Phi_0]^{\dagger}[Y,\Phi_0])$ |
| $s$ | the sign with which the two words of a pair agree, $+1$ for $\{t,a\}$ and $-1$ for $\{b,c\}$ |
| $\operatorname{tr}(X^{\dagger}X)$ | the Gram entry, $2$ for each physics array, $4$ for each word |

## Further Reading

- [Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html). The twenty-one arrays, the three-step construction, and the property table this article's basis is taken from.
- [Building the Two Bases of $\mathfrak{su}(4)$ from the Axis-Free Left and Right Matrices](../articles_internal/structures/structure-SU4-basis-construction.html). The pair lemma, the rank-one blocks, the maths-base display, and the theorem that one plane, eigenline and diagonal are one condition.
- [The Breaking Chain of the Four Colours Left–Right Model: One Flag, Three Stabilisers, Three Scales](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html). What happens after this matrix: the second and third breaking, the mixing, and the scales.
- [Classification of the Bosons: Twenty-Four Cells, Twenty-One Generators](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html). Which boson sits on each array, and the full spectrum with colour and charge.
- [The Leptoquarks of the Four Colours Left–Right Model: Six States, One Bound, and Why Proton Decay Does Not Bite](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html). The six massive states of this matrix, their charges and the bound on their mass.
- [The Scalar Sector of the Four Colours Left–Right Model: Twenty-Four Real Components, Twelve Eaten, Twelve Surviving](the-scalar-sector-of-the-four-colours-left-right-model-twenty-four-real-components-twelve-eaten-twelve-surviving.html). Where the vacuum comes from and what is eaten to feed these six masses.
- [The Four Colours Left–Right Model](the-four-colours-left-right-model.html). The declaration, the carrier and the stabiliser that make $D$ the only trace-zero direction available.
