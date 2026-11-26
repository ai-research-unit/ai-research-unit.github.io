# __The Block Reading of the Operators of $M_n(\mathbb{C})$__

## Introduction

**The question.** Fix a splitting $\mathbb{C}^n=U\oplus W$ of dimensions $k$ and $n-k$. How do $L_A$, $R_B$ and $T_{A,B}$ act on the four blocks of $M_n$, and which blocks stay separate?

**The answer in one line.** With $E$ the projection onto $U$ and $F=\mathrm I-E$, the space splits into the four Peirce corners
$$
EM_nE,\quad EM_nF,\quad FM_nE,\quad FM_nF,
$$
of dimensions $k^2,k(n-k),(n-k)k,(n-k)^2$; a one-sided operator preserves the corners on its own side only, and a general two-sided operator mixes all four.

**Why the article is needed.** At $n=2$ with $k=1$ the four corners are one-dimensional, so every operator is a $2\times2$ block matrix and the mixing is invisible. At general $n$ the corners have different sizes and the mixing pattern is the content: it is what the Peirce decomposition of the algebra becomes in the operator picture, and it is where the half-integer labels of $n=4$ come from.

**Boundaries.** The Peirce decomposition of the algebra is *The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$*; the chirality split is *Operator Chirality on $M_n(\mathbb{C})$*; the four sectors of the biquaternion algebra are *The Operators on the Four Sectors of $M_n(\mathbb{C})$*.

**Conventions.** $E$ is a projection of rank $k$, $F=\mathrm I-E$, and a matrix $X$ is written as the block matrix $\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}$ with $X_{11}=EXE$, $X_{12}=EXF$, $X_{21}=FXE$, $X_{22}=FXF$.

## The Four Corners

**The dimensions.** $EM_nE\cong M_k$, $EM_nF\cong\mathbb{C}^{k\times(n-k)}$, $FM_nE\cong\mathbb{C}^{(n-k)\times k}$, $FM_nF\cong M_{n-k}$. The complex dimensions are $k^2,k(n-k),k(n-k),(n-k)^2$ and they add to $n^2$.

**The multiplication table.** For corners $C_{ij}=E_iM_nE_j$ with $E_1=E$, $E_2=F$,
$$
C_{ij}C_{lm}\subseteq\delta_{jl}C_{im}.
$$
So the corners are the Peirce spaces of the two-idempotent decomposition, and the two off-diagonal corners multiply to zero in both directions.

**The transpose.** The transpose exchanges the two off-diagonal corners, $C_{12}^{\mathsf T}=C_{21}$, and preserves the diagonal ones. This is the operator version of the chirality of *Operator Chirality on $M_n(\mathbb{C})$*.

**The trace.** The trace vanishes on both off-diagonal corners and restricts to the trace on each diagonal corner.

## The One-Sided Operators

**Proposition.** $L_A(C_{ij})\subseteq C_{1j}+C_{2j}$, and $L_A$ preserves $M_nE_j$ for each $j$.

*Proof.* $A(EXF)=AXF$, which ends on the right with $F$; a general $A$ sends $EXF$ into $M_nF=C_{12}+C_{22}$. $\square$

**In blocks.** With $A=\begin{pmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{pmatrix}$,
$$
L_A\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}
=\begin{pmatrix}A_{11}X_{11}+A_{12}X_{21}&A_{11}X_{12}+A_{12}X_{22}\\ A_{21}X_{11}+A_{22}X_{21}&A_{21}X_{12}+A_{22}X_{22}\end{pmatrix}.
$$
The right index of $X$ is untouched; the left index is mixed.

**The right copy.** $R_B$ mixes the right index and leaves the left one:
$$
R_B X=\begin{pmatrix}X_{11}B_{11}+X_{12}B_{21}&X_{11}B_{12}+X_{12}B_{22}\\ X_{21}B_{11}+X_{22}B_{21}&X_{21}B_{12}+X_{22}B_{22}\end{pmatrix}.
$$

**The preservation statement.** $L_A$ preserves the two column spaces $C_{11}+C_{21}$ and $C_{12}+C_{22}$, and $R_B$ preserves the two row spaces $C_{11}+C_{12}$ and $C_{21}+C_{22}$. Neither preserves an individual corner unless $A$ or $B$ is block diagonal.

## The Two-Sided Operators

**Proposition.** $(AXB)_{ij}=\sum_{p,q}A_{ip}X_{pq}B_{qj}$, so every corner of $X$ contributes to every corner of the result.

*Proof.* Block multiplication. $\square$

**The four contributions to one corner.** The $(1,1)$ corner of $AXB$ is
$$
A_{11}X_{11}B_{11}+A_{11}X_{12}B_{21}+A_{12}X_{21}B_{11}+A_{12}X_{22}B_{21},
$$
so the corner receives one term from each of the four corners of $X$, weighted by the appropriate blocks of $A$ and $B$.

**The invariant case.** If $A$ and $B$ are both block diagonal, then $A_{12}=A_{21}=B_{12}=B_{21}=0$ and $T_{A,B}$ preserves each corner:
$$
T_{A,B}(C_{ij})\subseteq C_{ij},\qquad T_{A,B}\rvert_{C_{ij}}=T_{A_{ii},B_{jj}}.
$$

**The mixture measure.** In general the off-diagonal blocks of $A$ and $B$ are exactly the terms that move $X$ between corners, so the mixing is controlled by the size of those blocks. The distance of $T_{A,B}$ from the corner-preserving operators is the norm of the off-diagonal part of the pair.

## The Operators as Block Matrices

**The block matrix of $T_{A,B}$.** Ordering the carrier by the four corners, $T_{A,B}$ is a $4\times4$ block matrix whose entries are themselves maps between corners, and each entry is a sum of at most four tensor products of blocks of $A$ and $B$.

**The corner block of $L_A$ and $R_B$.** $L_A$ is block upper triangular in the ordering $(C_{11},C_{21})\oplus(C_{12},C_{22})$ exactly when $A_{12}=0$, and $R_B$ is block triangular in the other ordering exactly when $B_{21}=0$.

**The dimensions of the operator blocks.** The corner $C_{ij}$ has dimension $d_{ij}$, and an operator mapping $C_{ij}$ to $C_{lm}$ is a $d_{lm}\times d_{ij}$ matrix. The four diagonal blocks of $L_A$ have sizes $k^2\times k^2$ and so on, and the off-diagonal blocks are rectangular.

## The Case $n=4$, $k=2$

**All four corners are four-dimensional.** $k=n-k=2$, so $d_{ij}=4$ for all four corners, and the operator space $M_4$ splits into four equal blocks of dimension $4$. This is the only $n$ at which the four corners are simultaneously equal and more than one-dimensional.

**The half-integers.** Under the principal copy at $n=4$, the two diagonal corners carry integer spins and the two off-diagonal corners carry the half-integer labels. The block reading is the operator-level sight of the Peirce corners that carry the half-integers; the spin statement is in *Integer Labels on the Algebra, a Half-Integer on the Module: The Carrier Condition*.

**What does not happen at $n=2$.** With $k=1$ the four corners are one-dimensional, the mixing is a $2\times2$ pattern, and every operator is already a block matrix of scalars. The biquaternion block reading is the shadow of this case.

## The Finite Check

Computed with numpy for $n=2,3,4,5$ and every $1\le k\le n-1$: the four corner dimensions $k^2,k(n-k),k(n-k),(n-k)^2$ sum to $n^2$ in every case, and the corner multiplication table $C_{ij}C_{lm}\subseteq\delta_{jl}C_{im}$ was checked on random corner elements to $10^{-15}$.

The preservation statements were checked by projecting: for random $X\in C_{12}$, the component of $L_AX$ in $C_{11}+C_{21}$ vanishes to $10^{-14}$, and the analogous statement holds for $R_B$ on the row spaces. For block-diagonal $A,B$ the residual $\lVert T_{A,B}X-P_{C}T_{A,B}P_{C}X\rVert$ vanishes for every corner projection $P_C$ to $10^{-14}$; for general $A,B$ it is bounded away from zero, and the size grows with the norm of the off-diagonal blocks.

## The Four Corners in Coordinates

**The corner sizes.** In the splitting $\mathbb{C}^n=\mathbb{C}^p\oplus\mathbb{C}^q$ with $p+q=n$ the four corners have dimensions $p^2$, $pq$, $qp$ and $q^2$, summing to $n^2$.

**The two-sided action.** $T_{A,B}$ preserves each corner: if $X$ has entries only in the corner $(i,j)$, then $AXB$ has entries only in the same corner.

*Proof.* $A$ acts on the row index and $B$ on the column index, and both preserve the decomposition of the index set into the first $p$ and the last $q$ indices. $\square$

**The one-sided action.** $L_A$ does not preserve the corners: the block $A_{12}$ sends the corner $(2,2)$ into the corner $(1,2)$, and the block $A_{21}$ sends $(1,1)$ into $(2,1)$.

**The mixture.** A general $T_{A,B}$ mixes the entries inside each corner, since $A$ and $B$ mix the indices within the two blocks, but it never moves an entry from one corner to another. The mixture of blocks comes from the one-sided families, not from the two-sided one.

## The Case $p=1$

**The dimensions.** For $p=1$ and $q=n-1$ the corners have dimensions $1$, $n-1$, $n-1$ and $(n-1)^2$.

**The reading.** The corner $(1,1)$ is one-dimensional and is the span of $E_{11}$; the corner $(2,2)$ is the algebra of the complement; the two off-diagonal corners are the two spaces of maps between the line and the complement, exchanged by the transpose.

**The consequence.** The block reading at $p=1$ is the reading in which the Peirce corners have the most unequal sizes, and it is the reading in which the two-sided action is the most visible: a two-sided operator acts on four blocks of very different sizes without moving between them.

## The Corner Alphabet

| corner | size | as maps |
|---|---|---|
| $(1,1)$ | $p^2$ | maps on the first block |
| $(1,2)$ | $pq$ | maps from the second block to the first |
| $(2,1)$ | $qp$ | maps from the first block to the second |
| $(2,2)$ | $q^2$ | maps on the second block |

**The transpose.** It exchanges $(1,2)$ and $(2,1)$ and preserves the two diagonal corners.

**The reading.** The alphabet is the alphabet of a $2\times2$ matrix of spaces, and the four Peirce corners of the algebra are its four letters.

## The Count

**The numbers.** The four corners sum to $p^{2}+2pq+q^{2}=n^{2}$, the complex dimension of the algebra, at every splitting and every $n$.

## Summary

A splitting into $U\oplus W$ splits $M_n$ into four corners of dimensions $k^2,k(n-k),k(n-k),(n-k)^2$ with a triangular multiplication table. The left copy mixes the left index and preserves the right, the right copy does the reverse, and a general two-sided operator mixes all four corners. The corners are preserved exactly when both parameters are block diagonal. At $n=2$ the corners are one-dimensional and the structure is invisible; at $n=4$ with $k=2$ they are equal and four-dimensional, and the half-integer carriers live off the diagonal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E,F$ | complementary projections of ranks $k$ and $n-k$ |
| $C_{ij}$ | the corner $E_iM_nE_j$ |
| $d_{ij}$ | the dimension of $C_{ij}$ |
| $X_{ij}$ | the block $E_iXE_j$ |
| $k(n-k)$ | the dimension of each off-diagonal corner |

## Further Reading
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-mnc.html), for the algebra-level decomposition.
- [Operator Chirality on $M_n(\mathbb{C})$](operator-chirality-on-mnc.html), for the symmetric and antisymmetric split.
- [The Operators on the Four Sectors of $M_n(\mathbb{C})$](the-operators-on-the-four-sectors-of-mnc.html), for the sector reading.
- [Integer Labels on the Algebra, a Half-Integer on the Module: The Carrier Condition](integer-labels-on-the-algebra-a-half-integer-on-the-module.html), for the half-integer labels.
- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the case $n=4$.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the case $n=2$.
