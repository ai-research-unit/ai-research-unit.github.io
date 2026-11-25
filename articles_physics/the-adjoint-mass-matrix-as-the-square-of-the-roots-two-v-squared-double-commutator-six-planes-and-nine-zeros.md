# __The Adjoint Mass Matrix as the Square of the Roots: $M^2=2v^2[D,[D,\cdot]]$, Six Planes at $32v^2$ and Nine Zeros__

## Introduction

**The adjoint mass matrix of the fifteen is one operator, and the operator is a double commutator with the vacuum.** With $\Phi_0=vD$ the vacuum of the scalar that breaks $\mathrm{SU}(4)$,

$$
M^{2}_{XY}=\operatorname{tr}\bigl([X,\Phi_0]^{\dagger}[Y,\Phi_0]\bigr)=v^{2}\operatorname{tr}\bigl(X^{\dagger}\,[D,[D,Y]]\bigr).
$$

In the physics basis, whose twelve plane arrays satisfy $\operatorname{tr}(X_a^{\dagger}X_b)=2\delta_{ab}$ — the three diagonal arrays lie in the kernel, so their normalisation does not matter — that reads

$$
M^{2}=2v^{2}\,\mathcal E,\qquad \mathcal E(X)=[D,[D,X]] .
$$

**The spectrum is the square of the root system of the vacuum.** The eigenvalues of $\mathcal E$ on the fifteen are the squares $(\lambda_j-\lambda_k)^{2}$ of the differences of the vacuum's diagonal entries, on the twelve planes, and zero on the three Cartan directions. **A squared mass is $2v^{2}$ times the square of a root of the vacuum, and a massless generator is a generator the vacuum does not see.** That is the whole content of the nine-and-six display, and it is one sentence rather than fifteen computations.

**What the identity buys.** Three things that the entry-by-entry computation states and does not explain. First, the six and the nine are not two computations: they are the non-zero and the zero of one operator. Second, the nine are a subalgebra because they are the kernel of a commutator, and a kernel of $\operatorname{ad}_D$ is by construction a centraliser, hence closed under the bracket. Third, the number $32$ is not special to the minimal vacuum: at a regular vacuum every mass is $2v^{2}(d_j-d_k)^{2}$, and the minimal vacuum is the degenerate case in which six of the twelve roots collapse to zero and the twelve masses collapse to six.

**What the identity does not buy.** It computes nothing about couplings, nothing about the loop corrections, and nothing about the six weak generators, which are not in the fifteen and take their masses from the doublet vacuum. Those are stated in the closing section.

**The division of labour with the entry-by-entry article.** [The Adjoint Mass Matrix of the Fifteen](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html) computes all $225$ entries, states the commutator lemma that produces them, and separates the artefact that a recomputation of a weak mass produces. This article states the operator behind that computation, derives the spectrum from it, and reads the kernel as a Lie-algebra statement. The numbers must agree, and the checks confirm that they do.

**The root language, and one caution.** A root of a compact Cartan element $H=i\operatorname{diag}(\ldots)$ is imaginary — the values $\pm i,\pm2i,\pm3i$ of [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html). A root of a Hermitian vacuum $\Phi_0=vD$ is real, because $D$ is Hermitian and not anti-Hermitian. The mass is the square of the real root, and there is no contradiction: the vacuum is in the Hermitian half of $\mathfrak{sl}_4$, which is where a symmetry-breaking direction lives.

## The Identity

**The definition, and the first form.** For $X,Y$ in the fifteen,

$$
M^{2}_{XY}=\operatorname{tr}\bigl([X,\Phi_0]^{\dagger}[Y,\Phi_0]\bigr),\qquad \Phi_0=vD,\qquad D=\operatorname{diag}(-3,1,1,1).
$$

This is the mass matrix of [The Adjoint Mass Matrix of the Fifteen](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html), and the definition is the one the corpus uses throughout.

**Proposition (the identity).** For every $X,Y$ in the fifteen,

$$
M^{2}_{XY}=v^{2}\operatorname{tr}\bigl(X^{\dagger}\,[D,[D,Y]]\bigr).
$$

**Proof.** $[X,\Phi_0]=v[X,D]$, and $[X,D]$ is self-adjoint because $X$ is anti-Hermitian and $D$ is Hermitian, so $[X,D]^{\dagger}=[X,D]$ and the dagger in the definition acts trivially. Then

$$
M^{2}_{XY}=v^{2}\operatorname{tr}\bigl([X,D][Y,D]\bigr).
$$

Both factors are self-adjoint, so the trace of their product is real. The cyclic identity $\operatorname{tr}([X,D]\,[Y,D])=\operatorname{tr}\bigl(X\,[D,[Y,D]]\bigr)$ follows by writing the first commutator out, moving one factor around the trace and cancelling,

$$
\operatorname{tr}\bigl(XD[Y,D]\bigr)-\operatorname{tr}\bigl(DX[Y,D]\bigr)
=\operatorname{tr}\bigl(XD[Y,D]\bigr)-\operatorname{tr}\bigl(X[Y,D]D\bigr)
=\operatorname{tr}\bigl(X[D,[Y,D]]\bigr),
$$

and $[D,[Y,D]]=-[D,[D,Y]]$, so $M^{2}_{XY}=-v^{2}\operatorname{tr}\bigl(X\mathcal E(Y)\bigr)$ with $\mathcal E(Y)=[D,[D,Y]]$. Since $X^{\dagger}=-X$ for every element of the fifteen, $\operatorname{tr}(X^{\dagger}\mathcal E(Y))=-\operatorname{tr}(X\mathcal E(Y))$, and the two forms agree. 

**The operator, and the factor two.** Write $\mathcal E(X)=[D,[D,X]]$. Then

$$
M^{2}_{XY}=v^{2}\operatorname{tr}\bigl(X^{\dagger}\,\mathcal E(Y)\bigr),
$$

and if the basis is chosen with $\operatorname{tr}(X_a^{\dagger}X_b)=2\delta_{ab}$ — which the plane arrays satisfy, $\operatorname{tr}(A_{jk}^{\dagger}A_{jk})=\operatorname{tr}(S_{jk}^{2})=2$ — the matrix of $M^{2}$ is $2v^{2}$ times the matrix of $\mathcal E$. **The factor two is the trace normalisation and nothing else.** On arrays normalised to unit trace the matrix is $v^{2}\mathcal E$, and no mass changes.

**Why $\mathcal E$ preserves the fifteen.** $[D,X]$ alone does not: for a real plane array $[A_{jk},D]=(\lambda_k-\lambda_j)S_{jk}$ is real symmetric, outside $\mathfrak{su}(4)$. The second commutator brings it back, $[D,[D,A_{jk}]]=(\lambda_j-\lambda_k)^{2}A_{jk}$, and the same for $iS_{jk}$. So the mass operator is defined on the fifteen, its square root is not, and that is why the identity is stated with two commutators and not with a square.

## The Spectrum

**Proposition (the eigenvalues).** On each plane $\{j,k\}$, $\mathcal E$ acts as the scalar $(\lambda_j-\lambda_k)^{2}$, and on the three diagonal directions it acts as zero.

**Proof.** A diagonal $D$ commutes with a diagonal matrix, so $\mathcal E(iD)=\mathcal E(d_2)=\mathcal E(d_3)=0$. For the planes, $[A_{jk},D]=(\lambda_k-\lambda_j)S_{jk}$ and $[S_{jk},D]=(\lambda_k-\lambda_j)A_{jk}$, so applying the commutator twice returns the array it started from, multiplied by the square of the difference. 

**The minimal vacuum, evaluated.** $D=\operatorname{diag}(-3,1,1,1)$ has one lepton line of entry $-3$ and three colour lines of entry $1$. The differences across a plane are

| plane | $\lambda_k-\lambda_j$ | $(\lambda_j-\lambda_k)^{2}$ | $M^{2}$ |
|---|---|---|---|
| $\{t,a\}$, leptoquark | $4$ | $16$ | $32v^{2}$ |
| $\{a,b\}$, colour | $0$ | $0$ | $0$ |
| diagonal directions | — | $0$ | $0$ |

Six planes through the lepton line, three colour planes, three diagonals: $6+3+3=15$. The display is

$$
M^{2}=\operatorname{diag}\bigl(\underbrace{32v^{2},\dots,32v^{2}}_{6},\underbrace{0,\dots,0}_{9}\bigr),
$$

which is the display of the entry-by-entry article, reached without touching an entry.

**The general vacuum.** Let $\Phi_0=\operatorname{diag}(d_1,d_2,d_3,d_4)$ with $\sum d_j=0$. Then the same three-line proof gives

$$
M^{2}=2(d_j-d_k)^{2}\ \text{ on the plane }\{j,k\},
$$

and the minimal vacuum is the case $d=(-3,1,1,1)v$ in which the three colour entries coincide. **The formula is the same at every vacuum; only the differences move.** That is the sense in which the mass matrix is the squared root system of the vacuum and not a feature of one vacuum.

**A regular vacuum, as the check.** At $d=(3,1,-1,-3)v$ the differences are $2,4,6$ and their negatives, so the spectrum is

$$
2v^{2}\cdot\{4,4,4,4,4,4,\ 16,16,16,16,\ 36,36\},\qquad 0,0,0,
$$

that is eight entries at $8v^{2}$, four at $32v^{2}$, two at $72v^{2}$, and three zeros. $6+6+3=15$: twelve roots and three Cartan directions. The minimal vacuum keeps six of the twelve non-zero — the ones that cross the lepton line — and sends the six inside the colour triple to zero.

**Why six of the twelve roots collapse.** At $D=\operatorname{diag}(-3,1,1,1)$ the three colour entries are equal, so the six roots that live inside the colour triple take the value zero. The twelve become $\pm4$ three times each and $0$ six times; the square sends the two signs to one mass, so the six non-zero roots give the six masses $32v^{2}$, and the three Cartan directions join the six collapsed roots in the nine zeros of $\mathcal E$. **The nine-and-six display is a statement about how degenerate the vacuum is**, which is the same statement as "colour is unbroken".

## The Kernel Is a Subalgebra

**The kernel.** $\ker M^{2}=\{X:[D,X]=0\}$: the massless directions are exactly the generators that commute with the vacuum.

**Proposition (the kernel is closed under the bracket).** If $[D,X]=[D,Y]=0$ then $[D,[X,Y]]=0$, by the Jacobi identity. So the kernel is a centraliser, hence a subalgebra, and the nine massless generators are an algebra and not a set of nine numbers that happen to be zero.

**Which algebra.** The centraliser of $\operatorname{diag}(-3,1,1,1)$ in $\mathfrak{su}(4)$ is $\mathfrak{su}(3)\oplus\mathfrak u(1)$: the eight colour directions on the triple of equal entries, and the one direction that is a multiple of the identity on that triple and the compensating multiple on the lepton line. Its dimension is $8+1=9$, and it is the residual algebra $\mathfrak{su}(3)\oplus\mathfrak u(1)_{B-L}$ of [The Unbroken Subgroup](the-unbroken-subgroup-of-the-four-colours-left-right-model-nine-massless-generators-twelve-that-acquire-mass.html).

**Why this is the strongest form of the statement.** A mass matrix whose kernel is a subalgebra is the matrix statement that the breaking leaves a group standing, and the double-commutator form makes that automatic rather than checked: **the kernel of a commutator is a centraliser, and a centraliser is an algebra.** The entry-by-entry article verifies all $81$ brackets of the nine land back in the nine; the identity says they must.

## What the Identity Does Not Cover

**It does not compute the weak bosons.** The six weak generators are not in the fifteen; on the carrier they are sums of colour and leptoquark planes, and their masses come from the doublet vacuum at the second and third breakings. A recomputation that applies this matrix to $T^{L}_{a}$ as printed produces $8v^{2}$ for $W_L$ and not a mass — the factor $\tfrac14$ is the half in $T^{L}_{a}$ appearing twice, and [The Adjoint Mass Matrix of the Fifteen](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html) states the artefact in full.

**It does not fix a coupling.** All three gauge couplings of the model are symbolic, so $32v^{2}$ is a coefficient of $v^{2}$ and not a number in kilograms.

**It does not survive to one loop.** At one loop the coefficients shift and the pattern of six and nine is corrected; the shift is the effective-potential article's business, not this identity's.

**It does not say the nine stay massless.** Two of the nine are eaten at the second and third breakings, and the photon is a null direction of the neutral block rather than a stabiliser. The identity is a statement at one scale, the first breaking, and [The Breaking Chain](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html) continues the story.

## The Checks

Twelve recomputations, on the quartet ordered $(t,x,y,z)$, with $D=\operatorname{diag}(-3,1,1,1)$ and the physics basis of fifteen arrays.

| check | computation | result |
|---|---|---|
| the identity, entrywise | $\max\lvert M^{2}_{XY}-v^{2}\operatorname{tr}(X^{\dagger}\mathcal E(Y))\rvert$ over the $225$ pairs | $0$ |
| the operator form | $\max\lvert M^{2}-2v^{2}\mathcal E\rvert$ | $0$ |
| the diagonal | off-diagonal entries of $M^{2}$ | $210$ zero |
| the spectrum | eigenvalues of $M^{2}$ | $32v^{2}$ six times, $0$ nine times |
| the eigenvalues of $\mathcal E$ | eigenvalues on the fifteen | $16$ six times, $0$ nine times |
| the trace | $\operatorname{tr}M^{2}$ against $2v^{2}\sum(\lambda_j-\lambda_k)^{2}$ | $192v^{2}$, $192v^{2}$ |
| the rank, and the kernel dimension | $\operatorname{rank}M^{2}$ | $6$, kernel $9$ |
| the kernel is a centraliser | $\lvert[D,X]\rvert$ for $X$ in the nine | $0$ for all nine |
| the kernel is closed | the $81$ brackets of the nine | $81/81$ inside |
| the general formula | eigenvalues at $d=(3,1,-1,-3)v$ | $8v^{2}$ six, $32v^{2}$ four, $72v^{2}$ two, $0$ three |
| the roots of the vacuum | $\lambda_k-\lambda_j$ on the six leptoquark planes | $+4$ three times, $-4$ three times |
| the two bases | $32$ against $64$ with Gram $2$ against $4$ | $16$ either way |

## Summary

**One identity.** $M^{2}_{XY}=v^{2}\operatorname{tr}(X^{\dagger}[D,[D,Y]])$, which in the trace-normalised basis reads $M^{2}=2v^{2}\mathcal E$ with $\mathcal E(X)=[D,[D,X]]$.

**One spectrum.** The eigenvalues of $\mathcal E$ are the squares of the roots of the vacuum: $(\lambda_j-\lambda_k)^{2}$ on the twelve planes and zero on the three Cartan directions. At the minimal vacuum that is $32v^{2}$ six times and zero nine times.

**One structural consequence.** The kernel of a commutator is a centraliser, so the nine massless generators form a subalgebra without any further check: $\mathfrak{su}(3)\oplus\mathfrak u(1)_{B-L}$.

**One caution.** The factor two is the trace normalisation; the roots of a compact Cartan element are imaginary and the roots of a Hermitian vacuum are real, and it is the second kind that the mass squares.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Phi_0=vD$ | the vacuum of the scalar that breaks $\mathrm{SU}(4)$ |
| $D=\operatorname{diag}(-3,1,1,1)$ | the vacuum direction, traceless |
| $M^{2}_{XY}$ | $\operatorname{tr}([X,\Phi_0]^{\dagger}[Y,\Phi_0])$, the adjoint mass matrix |
| $\mathcal E(X)=[D,[D,X]]$ | the double commutator, the mass operator up to $2v^{2}$ |
| $\lambda_j=d_j$ | the diagonal entries of $D$ |
| $\lambda_k-\lambda_j$ | the root of the vacuum across the plane $\{j,k\}$ |
| $\ker M^{2}$ | the centraliser of $D$, the unbroken algebra |

## Further Reading

- [The Adjoint Mass Matrix of the Fifteen: One Number per Plane, $32v^2$ on Six and Zero on Nine](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html). The same matrix computed entry by entry, all $225$ entries, the commutator lemma, and the artefact of a weak-mass recomputation.
- [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html). The roots of a compact Cartan element, imaginary, and why a root vector is outside the algebra.
- [The Unbroken Subgroup of the Four Colours Left–Right Model: Nine Massless Generators, Twelve That Acquire Mass](the-unbroken-subgroup-of-the-four-colours-left-right-model-nine-massless-generators-twelve-that-acquire-mass.html). The same nine read as a group rather than as a matrix.
- [The Breaking Chain of the Four Colours Left–Right Model: One Flag, Three Stabilisers, Three Scales](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html). What happens to the nine after the first breaking.
- [The Cartan Subalgebra, the Roots and the Three Real Forms](the-cartan-subalgebra-the-roots-and-the-three-real-forms.html). The root language, for the Lorentz algebra, where the same complexification question is settled.
