# __The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$__

## Introduction

**The idempotents of a root of unity cut the algebra into corner lines, and a coarser idempotent cuts it into four corner blocks whose dimensions are $p^{2}$, $p(n-p)$, $(n-p)p$ and $(n-p)^{2}$.** The first cut is the Peirce decomposition of the full flag; the second is the recursion that embeds one matrix algebra in another.

The article states both cuts and the multiplication rule between the corners, proves the corner isomorphisms, and reads the recursion that orders the categories $M_3$, $M_4$, $M_5$, $M_6$. It also states what the decomposition is not: a direct-sum decomposition of the algebra into subspaces, not a list of spinors.

The idempotents come from *Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$*; the vectors inside the corner lines and the gauge that acts on them are *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$*.

## The Spectral Flag

**A root with simple spectrum produces a complete flag, and the flag is what the Peirce decomposition depends on.** Let $H^{n}=I$ have simple spectrum, with projectors $P_k$ and eigenvalues $\zeta_k$, $k=1,\dots,n$. Put $V_k=\operatorname{im}P_k$, a line. The $V_k$ are independent and sum to $\mathbb{C}^{n}$, and the partial sums

$$
F_k=V_1\oplus V_2\oplus\cdots\oplus V_k,\qquad k=1,\dots,n,
$$

form the complete flag

$$
0\subset F_1\subset F_2\subset\cdots\subset F_n=\mathbb{C}^{n},\qquad \dim F_k=k.
$$

**The flag is spectral, not standard.** The standard flag of *The Matrix Algebra $M_n(\mathbb{C})$* is the case $V_k=\mathbb{C}e_k$, that is, $H=\operatorname{diag}(\zeta_1,\dots,\zeta_n)$. Every other root gives a flag in general position with respect to the standard one. The construction depends only on the flag, so it is invariant under a change of basis that keeps $H$.

**Different roots, different flags.** The map $H\mapsto F$ is the projection $PGL_n(\mathbb{C})/T\to PGL_n(\mathbb{C})/B$ from the root set to the flag variety. Its fibre is the gauge of *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$*: the root fixes the flag, and the gauge fixes the vectors inside the lines.

## The Peirce Lines

**The Peirce corner $A_{kl}$ is the space of maps from the $l$-th line to the $k$-th line.** Put

$$
A_{kl}=P_kM_n(\mathbb{C})P_l=\{P_kXP_l: X\in M_n(\mathbb{C})\}.
$$

**Proposition.** Each $A_{kl}$ is a complex line, the lines are independent and sum to the algebra,

$$
M_n(\mathbb{C})=\bigoplus_{k,l=1}^{n}A_{kl},\qquad \dim_{\mathbb{C}}A_{kl}=1,
$$

and the product obeys

$$
A_{kl}A_{mn}\subseteq\delta_{lm}A_{kn}.
$$

*Proof.* The rank-one projector $P_k$ has image the line $V_k$, so $P_kXP_l$ is a linear map $V_l\to V_k$ followed by the inclusions; the space of such maps is $\operatorname{Hom}(V_l,V_k)$, of dimension $1$. The direct sum is the decomposition of $\operatorname{End}(\mathbb{C}^{n})=\bigoplus_{k,l}\operatorname{Hom}(V_l,V_k)$ over the direct-sum decomposition $\mathbb{C}^{n}=\bigoplus_kV_k$. For the product, $P_kXP_l\,P_mYP_n=\delta_{lm}P_kXP_lYP_n\in A_{kn}$. $\square$

**The multiplication table is the table of matrix units.** Choosing a nonzero $E_{kl}\in A_{kl}$ gives $E_{kl}E_{mn}=\delta_{lm}c_{kmn}E_{kn}$ with a scalar $c_{kmn}$ depending on the choices; the frame article chooses the vectors so that $c=1$. The Peirce lines are therefore an intrinsic version of the matrix units, defined without a choice of basis inside the lines.

**The Peirce coordinates.** Every $X\in M_n(\mathbb{C})$ has a unique decomposition

$$
X=\sum_{k,l}X_{kl},\qquad X_{kl}=P_kXP_l\in A_{kl},
$$

and the product is read in the coordinates as

$$
(XY)_{kl}=\sum_{m}X_{km}Y_{ml}.
$$

This is the matrix product written in the spectral basis. The diagonal corners $A_{kk}$ are the lines of the identity on $V_k$; the off-diagonal corners are the maps between distinct lines.

## The Coarse Split

**A single idempotent of rank $p$ cuts the algebra into four blocks.** Let $\Pi\in M_n(\mathbb{C})$ be an idempotent of rank $p$, $1\le p\le n-1$, and put $Q=I-\Pi$. The Peirce decomposition relative to $\Pi$ is

$$
M_n(\mathbb{C})=\Pi M\Pi\oplus\Pi MQ\oplus QM\Pi\oplus QMQ.
$$

Write the four corners as $A=\Pi M\Pi$, $B=\Pi MQ$, $C=QM\Pi$, $D=QMQ$. Their complex dimensions are

$$
\dim A=p^{2},\qquad \dim B=p(n-p),\qquad \dim C=(n-p)p,\qquad \dim D=(n-p)^{2},
$$

and they sum to $p^{2}+2p(n-p)+(n-p)^{2}=n^{2}$.

**The multiplication table of the coarse split.** In block form, with an element written $\begin{pmatrix}A&B\\C&D\end{pmatrix}$,

$$
\begin{pmatrix}A&B\\C&D\end{pmatrix}
\begin{pmatrix}A'&B'\\C'&D'\end{pmatrix}
=
\begin{pmatrix}AA'+BC'&AB'+BD'\\CA'+DC'&CB'+DD'\end{pmatrix}.
$$

The diagonal blocks are subalgebras with units $\Pi$ and $Q$; the off-diagonal blocks are bimodules. The table shows that the cross terms can return to the diagonal: $BC'\subseteq A$ and $CB'\subseteq D$. This is why the split is not a direct sum of algebras.

**The split is not a decomposition into ideals.** The algebra $M_n(\mathbb{C})$ is simple, so its only two-sided ideals are $0$ and the algebra. The four corners are subspaces, and the block-diagonal part $A\oplus D$ is a subalgebra, not an ideal. The decomposition is a decomposition of the vector space together with a graded multiplication; it is not a decomposition of the algebra as a direct sum of ideals. When the categories say that $M_5$ "contains" $M_2\oplus M_3$, the word means the block-diagonal subalgebra, not an ideal.

## The Corner Isomorphisms

**Each diagonal corner is a full matrix algebra.** Choose a basis $u_1,\dots,u_p$ of $\operatorname{im}\Pi$ and a basis $w_1,\dots,w_{n-p}$ of $\operatorname{im}Q$. In the basis $(u,w)$ of $\mathbb{C}^{n}$,

$$
\Pi=\begin{pmatrix}I_p&0\\0&0\end{pmatrix},\qquad
Q=\begin{pmatrix}0&0\\0&I_{n-p}\end{pmatrix},
$$

and the four corners are the four blocks of the block matrix. The map that deletes the zero rows and columns gives isomorphisms of algebras

$$
\Pi M_n\Pi\cong M_p(\mathbb{C}),\qquad QM_nQ\cong M_{n-p}(\mathbb{C}),
$$

unital for the units $\Pi$ and $Q$ respectively. The off-diagonal corners are

$$
\Pi M_nQ\cong\operatorname{Hom}(\operatorname{im}Q,\operatorname{im}\Pi)\cong M_{p,n-p}(\mathbb{C}),
$$

and $QM_n\Pi\cong M_{n-p,p}(\mathbb{C})$. The isomorphisms depend on the choice of bases, but the dimensions do not.

**The diagonal corner is a matrix algebra with a compressed unit.** The unit of $A=\Pi M\Pi$ is $\Pi$, not $I$; the trace of $A$ as a matrix algebra is the compression $\operatorname{tr}(\Pi X\Pi)$, not $\operatorname{tr}X$. The complement $\mathbb{C}(I-\Pi)$ is not part of $A$. This is the precise sense in which $A$ is a matrix algebra and not a unital subalgebra of $M_n$ with the unit $I$.

**The corner is a $*$-algebra only for a projection.** If $\Pi^{*}=\Pi$ then the compression $X\mapsto\Pi X^{*}\Pi$ is an involution of $A$, and $A$ is a $*$-subalgebra of $M_n$. If $\Pi$ is merely idempotent and not Hermitian, the compression of the involution does not land in $A$ in general, and $A$ is only an algebra. The distinction matters in the biquaternion case, where the natural idempotents need not be Hermitian for the coefficient conjugation.

## The Corner Recursion

**A rank-$p$ idempotent exhibits $M_n$ as a block matrix algebra over $M_p$ and $M_{n-p}$.** With the basis above,

$$
M_n(\mathbb{C})\supset
\left\{\begin{pmatrix}A&0\\0&D\end{pmatrix}:A\in M_p,\ D\in M_{n-p}\right\}
\cong M_p(\mathbb{C})\oplus M_{n-p}(\mathbb{C}),
$$

a block-diagonal subalgebra, and the off-diagonal blocks $B$ and $C$ complete it to the whole algebra. The inclusion is the recursion: **$M_n$ contains $M_p\oplus M_{n-p}$ whenever $1\le p\le n-1$.**

**The cases that order the categories.** Taking the rank $p$ and its complement:

$$
M_3\supset M_2\oplus M_1,\qquad
M_4\supset M_2\oplus M_2\ \text{and}\ M_3\oplus M_1,
$$

$$
M_5\supset M_2\oplus M_3\ \text{and}\ M_4\oplus M_1,\qquad
M_6\supset M_3\oplus M_3,\ M_2\oplus M_4\ \text{and}\ M_5\oplus M_1.
$$

The two balanced cases are the ones the categories single out: $M_4\supset M_2\oplus M_2$, $M_6\supset M_3\oplus M_3$; the unbalanced ones are $M_5\supset M_2\oplus M_3$ and $M_6\supset M_2\oplus M_4$. This is why the categories are ordered $M_3,M_4,M_5,M_6$: each contains the previous ones as corners, and the articles of a later category can cite the earlier ones.

**The Peirce dimensions in a table.** For a rank-one idempotent and for the balanced split:

| $n$ | rank-one corners | rank-$p$ corners | balanced split |
|---|---|---|---|
| $3$ | $1+2+2+4$ | $p=2$: $4+2+2+1$ | — |
| $4$ | $1+3+3+9$ | $p=2$: $4+4+4+4$ | $M_2\oplus M_2$ |
| $5$ | $1+4+4+16$ | $p=2$: $4+6+6+9$ | — |
| $6$ | $1+5+5+25$ | $p=2$: $4+8+8+16$; $p=3$: $9+9+9+9$ | $M_3\oplus M_3$ |

The rank-one row is the full Peirce decomposition seen from one line: $1$ for the line, $n-1$ for the maps out of it, $n-1$ for the maps into it, and $(n-1)^{2}$ for the complement. The remaining $n-1$ lines of the full flag are the Peirce lines of the complement, refined further.

## The Biquaternion Case

**At $n=2$ the full Peirce decomposition has four lines, and the coarse split of a rank-one idempotent is the same four lines.** The rank-one corners are $1+1+1+1$, and for $p=1$ the coarse split and the full split coincide: there is only one line to separate. This is a feature of $n=2$ and does not persist.

**The diagonal lines carry canonical vectors and the mixed lines do not.** In the algebra $M_2(\mathbb{C})$, the corner $P_kM_2P_k$ is spanned by $P_k$ itself, which is canonical. The mixed corner $P_kM_2P_l$ is spanned by a matrix unit $E_{kl}$ defined only up to a scalar. The biquaternion frame article read that scalar freedom as a second root; the correct reading is the gauge parameter $\lambda$, one complex number for the two mixed lines, acting as $E_{kl}\mapsto\lambda E_{kl}$ and $E_{lk}\mapsto\lambda^{-1}E_{lk}$. The idempotents $P_k$ do not depend on $\lambda$.

## What the Decomposition Is Not

**The Peirce decomposition is a direct-sum decomposition of the algebra, not a list of spinors.** The summands $A_{kl}$ are spaces of linear maps between the lines of a flag. An element of $A_{kl}$ is a map $V_l\to V_k$, not a spinor. The decomposition is a statement about the algebra as a module over itself, not about a representation of a spin group.

**Not every Peirce element is a spinor.** The corner $A_{kl}$ is one-dimensional, and every nonzero element of it is a map of rank one between two lines. Calling such an element a spinor would make every matrix unit a spinor, which is false. A spinor, where the word applies, is a vector of the carrier module of the spin chain, introduced in *The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$*; it is not an element of a Peirce corner.

**The carrier is not a corner.** For $n=2$ the carrier is $\mathbb{C}^{2}$, isomorphic to a minimal left ideal; for $n\ge3$ the carrier is $\mathbb{C}^{n}=\operatorname{Sym}^{n-1}(\mathbb{C}^{2})$, of dimension $n$, and it is not isomorphic to any Peirce corner. The corner $A_{kl}$ has dimension $1$ for every $n$; the carrier has dimension $n$. They never coincide in dimension for $n\ge2$.

## Summary

A root with simple spectrum gives a complete flag, and the Peirce corners $A_{kl}=\operatorname{Hom}(V_l,V_k)$ are lines that sum to the algebra with the multiplication rule $A_{kl}A_{mn}\subseteq\delta_{lm}A_{kn}$. A rank-$p$ idempotent gives four corners of dimensions $p^{2}$, $p(n-p)$, $(n-p)p$ and $(n-p)^{2}$, with diagonal corners isomorphic to $M_p$ and $M_{n-p}$ and off-diagonal corners isomorphic to rectangular matrix spaces. The block-diagonal subalgebra is $M_p\oplus M_{n-p}$, which is the recursion $M_n\supset M_p\oplus M_{n-p}$ and the reason the categories are ordered $M_3,\dots,M_6$. The decomposition is a direct sum of subspaces, not of ideals, and its elements are maps, not spinors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_k$ | the Lagrange projector of $\zeta_k$, of rank $1$ |
| $V_k=\operatorname{im}P_k$ | the $k$-th spectral line |
| $F_k$ | the partial sum $V_1\oplus\cdots\oplus V_k$ |
| $A_{kl}=P_kM_nP_l$ | the Peirce corner, a line |
| $\Pi$, $Q=I-\Pi$ | a coarse idempotent of rank $p$ and its complement |
| $A,B,C,D$ | the four coarse corners $\Pi M\Pi$, $\Pi MQ$, $QM\Pi$, $QMQ$ |
| $M_{p,n-p}$ | the space of $p\times(n-p)$ matrices |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions, corner algebras and the multiplication table.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for block matrices, ranks and the spectral decomposition.
- [Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-mnc.html), for the idempotents that produce the flag.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-mnc.html), for the vectors inside the corner lines.
- [The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$](the-spin-chain-and-the-adjoint-decomposition-mnc.html), for the carrier, which is not a corner.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the biquaternion case $n=2$, where the coarse and the fine splits coincide.
- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), the case $n=3$.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), the case $n=4$.
- [The Peirce Decomposition of $M_5(\mathbb{C})$](the-peirce-decomposition-of-m5c.html), the case $n=5$.
- [The Peirce Decomposition of $M_6(\mathbb{C})$](the-peirce-decomposition-of-m6c.html), the case $n=6$.
