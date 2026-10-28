# __The Peirce Decomposition__

## Introduction

**The four idempotents of a root cut the algebra into sixteen corner lines, and one idempotent alone cuts it into four corner blocks of dimensions $1+3+3+9$.** The first cut is the Peirce decomposition of the full spectral flag; the second is the coarse split by a rank-one idempotent. The article states both, proves the multiplication rule between the corners, identifies the corner isomorphisms, and reads the recursion that refines the coarse split into the fine one.

The idempotents come from *Roots of Unity and the Lagrange Idempotents*; the vectors inside the corner lines and the gauge that acts on them are *The Frame, the Simple Nilpotents and the Gauge*. The rank-two split, where the coarse idempotent has rank two and the corners are $4+4+4+4$, is *The Rank-Two Split*. The general construction for $M_n(\mathbb{C})$ is *The Peirce Decomposition and the Corner Recursion*.

The Peirce decomposition is a direct-sum decomposition of the algebra into spaces of linear maps. It is not a list of spinors, and an element of a corner is not a spinor: the corner $\mathcal{A}_{kl}$ is a line of rank-one maps $V_l\to V_k$. The carrier of the spin chain is the four-dimensional space $\mathbb{C}^4$, which is not a corner; it is *The Spin Chain and the Adjoint Decomposition*.

## The Spectral Flag

Let $H$ be a root of order four with simple spectrum, with projectors $P_k$ and spectral lines $V_k=\operatorname{im}P_k$, $k=1,2,3,4$. The lines are independent and sum to $\mathbb{C}^4$, and the partial sums

$$
F_k=V_1\oplus\cdots\oplus V_k,\qquad k=1,2,3,4,
$$

form the complete flag

$$
0\subset F_1\subset F_2\subset F_3\subset F_4=\mathbb{C}^4,\qquad \dim F_k=k.
$$

The flag is **spectral**: it is produced by $H$, not fixed in advance. The standard flag of *The Matrix Algebra $M_4(\mathbb{C})$* is the case $V_k=\mathbb{C}e_k$, that is, $H=H_0=\operatorname{diag}(1,i,-1,-i)$. A general root gives a flag in general position with respect to the standard one. The construction depends only on the flag and the lines, so it is invariant under a change of basis that preserves $H$.

## The Peirce Lines

**Definition.** Relative to the complete orthogonal family $P_1,\dots,P_4$, the **Peirce corners** are

$$
\mathcal{A}_{kl}=P_kM_4(\mathbb{C})P_l=\bigl\{P_kXP_l:X\in M_4(\mathbb{C})\bigr\},\qquad k,l=1,2,3,4.
$$

**Theorem.** Each corner is a complex line, the sixteen corners are independent and sum to the algebra,

$$
M_4(\mathbb{C})=\bigoplus_{k,l=1}^{4}\mathcal{A}_{kl},\qquad \dim_\mathbb{C}\mathcal{A}_{kl}=1,
$$

and the product obeys

$$
\mathcal{A}_{kl}\mathcal{A}_{mn}\subseteq\delta_{lm}\mathcal{A}_{kn}.
$$

**Proof.** In the standard frame $P_k=E_{kk}$, so

$$
\mathcal{A}_{kl}=E_{kk}M_4(\mathbb{C})E_{ll}=\mathbb{C}E_{kl}.
$$

The sixteen matrix units $E_{kl}$ are a basis of $M_4(\mathbb{C})$, so the sum is direct and each corner is a line. For a general root, conjugate by $S$ with $H=SH_0S^{-1}$: conjugation is an algebra automorphism and carries $P_k$ to $SE_{kk}S^{-1}$, hence carries the standard corners to the corners of the general frame and preserves dimensions and the direct sum.

For the product, let $X=P_kXP_l\in\mathcal{A}_{kl}$ and $Y=P_mYP_n\in\mathcal{A}_{mn}$. Then

$$
XY=P_kXP_lP_mYP_n=\delta_{lm}P_kXP_lYP_n\in\delta_{lm}\mathcal{A}_{kn},
$$

because $P_lP_m=\delta_{lm}P_l$.

**Corollary.** The diagonal corners $\mathcal{A}_{kk}$ are the lines $\mathbb{C}P_k$. The off-diagonal corners are square-zero:

$$
\mathcal{A}_{kl}^2=0\qquad(k\ne l).
$$

**Proof.** Let $X=P_kXP_l$ and $Y=P_kYP_l$ lie in $\mathcal{A}_{kl}$. Then

$$
XY=P_kXP_lP_kYP_l=P_kX(\delta_{lk}P_l)YP_l,
$$

which is $0$ when $k\ne l$. The diagonal corner $\mathcal{A}_{kk}=P_kM_4P_k$ is spanned by $P_k$ because $P_k$ has rank one and $P_kXP_k$ is a scalar multiple of $P_k$.

**The corners are maps.** Intrinsically, $P_k$ is the projector onto $V_k$ along the sum of the other lines, so $P_kXP_l$ is the map $V_l\to V_k$ followed by the inclusion and preceded by the projection; the space of such maps is $\operatorname{Hom}(V_l,V_k)$, of dimension $1$. The decomposition is the decomposition of $\operatorname{End}(\mathbb{C}^4)$ over the direct sum $\mathbb{C}^4=\bigoplus_kV_k$:

$$
\operatorname{End}\Bigl(\bigoplus_kV_k\Bigr)=\bigoplus_{k,l}\operatorname{Hom}(V_l,V_k).
$$

This is the intrinsic content of the matrix-unit formula, and it is the reason the corners are lines for every root.

### The Peirce Table

The multiplication of the sixteen lines is the matrix-unit table. The entry in row $\mathcal{A}_{kl}$ and column $\mathcal{A}_{mn}$ is the corner containing the products:

| $\cdot$ | $\mathcal{A}_{mn}$ | condition |
|---|---|---|
| $\mathcal{A}_{kl}$ | $\mathcal{A}_{kn}$ | if $l=m$ |
| $\mathcal{A}_{kl}$ | $0$ | if $l\ne m$ |

In the standard frame the surviving product is $E_{kl}E_{lm}=E_{km}$, and the vanishing is $E_{kl}E_{mn}=0$ for $l\ne m$. The table is the rule $E_{kl}E_{mn}=\delta_{lm}E_{kn}$ read on the corners. It is the table of a matrix algebra, not a table of a Clifford algebra or a spin representation.

### The Peirce Coordinates

Every $X\in M_4(\mathbb{C})$ has a unique decomposition

$$
X=\sum_{k,l=1}^{4}X_{kl},\qquad X_{kl}=P_kXP_l\in\mathcal{A}_{kl}.
$$

Choose a frame $E_{kl}=v_k\ell_l$ in each corner, with $(v_k)$ a basis and $(\ell_k)$ the dual basis. Then

$$
X=\sum_{k,l=1}^{4}a_{kl}E_{kl},\qquad a_{kl}=\ell_k(Xv_l),
$$

and the multiplication is

$$
(XY)_{kl}=\sum_{m=1}^{4}a_{km}b_{ml}.
$$

**Proof.** Apply $X=\sum a_{kl}v_k\ell_l$ to $v_m$: $Xv_m=\sum_k a_{km}v_k$, so the coefficient of $v_k$ is $a_{km}=\ell_k(Xv_m)$. The product formula is the matrix product of the coordinate arrays.

The four numbers $a_{k1}$ are the coordinates of the image of $v_1$, the four $a_{k2}$ the coordinates of the image of $v_2$, and so on: the coordinate array is the matrix of the linear map $X$ in the frame. The trace is $\sum_k a_{kk}$, the determinant is the determinant of the array, and the rank is its rank. In the standard frame the array is the matrix of $X$ in the standard basis; in the spectral frame it is the matrix of $X$ in a basis of eigenvectors of $H$.

**The coordinates are not eigenvalues.** The diagonal coordinate $a_{kk}$ is the compression of $X$ to the line $V_k$, not an eigenvalue of $X$. Only for $X=H$ is the coordinate array diagonal, with $a_{kk}=\zeta_k$. The eigenvalues of a general $X$ are the eigenvalues of the array, which need not be diagonal.

## The Coarse Split

**Definition.** Let $\Pi$ be an idempotent of rank one and $Q=I-\Pi$ its complement. The **coarse Peirce corners** are

$$
\mathcal{A}=\Pi M_4\Pi,\qquad
\mathcal{B}=\Pi M_4Q,\qquad
\mathcal{C}=QM_4\Pi,\qquad
\mathcal{D}=QM_4Q.
$$

**Theorem.** The algebra is the direct sum

$$
M_4(\mathbb{C})=\mathcal{A}\oplus\mathcal{B}\oplus\mathcal{C}\oplus\mathcal{D},
$$

with

$$
\dim_\mathbb{C}\mathcal{A}=1,\qquad
\dim_\mathbb{C}\mathcal{B}=3,\qquad
\dim_\mathbb{C}\mathcal{C}=3,\qquad
\dim_\mathbb{C}\mathcal{D}=9.
$$

The diagonal corners are algebras with units $\Pi$ and $Q$,

$$
\mathcal{A}\cong\mathbb{C},\qquad \mathcal{D}\cong M_3(\mathbb{C}),
$$

and the off-diagonal corners are the rectangular matrix spaces

$$
\mathcal{B}\cong\mathbb{C}^{1\times3},\qquad \mathcal{C}\cong\mathbb{C}^{3\times1}.
$$

**Proof.** Choose a basis whose first vector spans $\operatorname{im}\Pi$ and whose remaining three vectors span $\operatorname{im}Q$. In that basis

$$
\Pi=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q=\begin{pmatrix}0&0\\0&I_3\end{pmatrix},
$$

and the four corners are the four blocks of a block matrix:

$$
X=\begin{pmatrix}a&r\\c&B\end{pmatrix},
\qquad a\in\mathbb{C},\quad r\in\mathbb{C}^{1\times3},\quad c\in\mathbb{C}^{3\times1},\quad B\in M_3(\mathbb{C}).
$$

The dimensions are $1$, $3$, $3$ and $9$, and they sum to $16$. The diagonal blocks are closed under multiplication and contain the units $\Pi$ and $Q$; the off-diagonal blocks are the spaces of maps between the image of $\Pi$ and the image of $Q$. Deleting the zero rows and columns gives $\mathcal{A}\cong\mathbb{C}$ and $\mathcal{D}\cong M_3(\mathbb{C})$.

**Example.** In the standard frame with $\Pi=P_1=E_{11}$ and $Q=E_{22}+E_{33}+E_{44}$,

$$
\mathcal{A}=\mathbb{C}E_{11},\qquad
\mathcal{B}=\operatorname{span}\{E_{12},E_{13},E_{14}\},
$$

$$
\mathcal{C}=\operatorname{span}\{E_{21},E_{31},E_{41}\},\qquad
\mathcal{D}=\operatorname{span}\{E_{ij}:2\le i,j\le4\}.
$$

A general element is

$$
X=\begin{pmatrix}
a_{11}&a_{12}&a_{13}&a_{14}\\
a_{21}&a_{22}&a_{23}&a_{24}\\
a_{31}&a_{32}&a_{33}&a_{34}\\
a_{41}&a_{42}&a_{43}&a_{44}
\end{pmatrix}
=\begin{pmatrix}
a&r\\c&B
\end{pmatrix},
$$

with $a=a_{11}$, $r=(a_{12},a_{13},a_{14})$, $c=(a_{21},a_{31},a_{41})^{\mathsf T}$ and $B$ the lower-right $3\times3$ block. This is the coarse split of the coordinate matrix.

### The Coarse Multiplication

In block form the product is

$$
\begin{pmatrix}a&r\\c&B\end{pmatrix}
\begin{pmatrix}a'&r'\\c'&B'\end{pmatrix}
=
\begin{pmatrix}
aa'+rc'&ar'+rB'\\
ca'+Bc'&cr'+BB'
\end{pmatrix}.
$$

**Proof.** Multiply the blocks and use the dimensions: $rc'$ is a $1\times3$ row times a $3\times1$ column, a scalar; $ar'$ and $rB'$ are rows; $ca'$ and $Bc'$ are columns; $cr'$ is a $3\times1$ column times a $1\times3$ row, a $3\times3$ matrix.

The table of corners is

| $\cdot$ | $\mathcal{A}$ | $\mathcal{B}$ | $\mathcal{C}$ | $\mathcal{D}$ |
|---|---|---|---|---|
| $\mathcal{A}$ | $\mathcal{A}$ | $\mathcal{B}$ | $\mathcal{C}$ | $0$ |
| $\mathcal{B}$ | $0$ | $0$ | $\mathcal{A}$ | $\mathcal{B}$ |
| $\mathcal{C}$ | $\mathcal{C}$ | $\mathcal{D}$ | $0$ | $0$ |
| $\mathcal{D}$ | $0$ | $0$ | $\mathcal{C}$ | $\mathcal{D}$ |

The products $\mathcal{B}\mathcal{C}\subseteq\mathcal{A}$ and $\mathcal{C}\mathcal{B}\subseteq\mathcal{D}$ are the cross terms $rc'$ and $cr'$. They are the reason the coarse split is not a direct sum of algebras: the off-diagonal blocks multiply back into the diagonal. The diagonal part $\mathcal{A}\oplus\mathcal{D}$ is a subalgebra with unit $I$, isomorphic to $\mathbb{C}\oplus M_3(\mathbb{C})$, but it is not an ideal: multiplying a diagonal element by a general element produces an off-diagonal part. The algebra $M_4(\mathbb{C})$ is simple, so it has no proper two-sided ideal at all.

**The corner units.** The unit of $\mathcal{A}$ is $\Pi$, not $I$; the unit of $\mathcal{D}$ is $Q$. For an element $X$, the trace of its compression to $\mathcal{A}$ is $\operatorname{tr}(\Pi X\Pi)$, which differs from $\operatorname{tr}X$ in general; on $\mathcal{A}$ itself the two agree, because $\Pi$ has rank one. On $\mathcal{D}$ the compressed trace $\operatorname{tr}(QXQ)$ is the trace of the $3\times3$ block. Each of $\mathcal{A}$ and $\mathcal{D}$ is a non-unital subalgebra of $M_4$, with unit $\Pi$ or $Q$; their sum $\mathcal{A}\oplus\mathcal{D}$ is unital, with unit $\Pi+Q=I$.

## Refining the Coarse Split

**The coarse split by one rank-one idempotent leaves a $9$-dimensional corner $\mathcal{D}\cong M_3(\mathbb{C})$, and the same construction inside that corner refines it.** The complement of $\Pi=P_1$ in $M_4$ is $Q=P_2+P_3+P_4$, and $\mathcal{D}=QM_4Q$ is a copy of $M_3$. Inside it, the idempotent $P_2$ is rank one, and its complement in $\mathcal{D}$ is $Q-P_2=P_3+P_4$. The corners of $\mathcal{D}$ relative to $P_2$ have dimensions

$$
1+2+2+4,
$$

because the complement $P_3+P_4$ has rank two. The $4$-dimensional corner is a copy of $M_2$, and the same construction with $P_3$ refines it to

$$
1+1+1+1.
$$

The recursion is therefore

$$
n\longmapsto 1+(n-1)+(n-1)+(n-1)^2,
$$

and for $n=4$ it reads

$$
4\longmapsto 1+3+3+9,\qquad
3\longmapsto 1+2+2+4,\qquad
2\longmapsto 1+1+1+1.
$$

After the three refinements the dimensions sum to

$$
1+3+3+9=16,
$$

and the sixteen lines are the corners $\mathcal{A}_{kl}$ of §*The Peirce Lines*. The coarse split is the first step of the recursion, not the final decomposition.

**The refined table.** The four coarse corners split into the fine lines as follows:

| Coarse corner | Dimension | Fine lines | Dimension |
|---|---|---|---|
| $\mathcal{A}=\Pi M\Pi$ | $1$ | $\mathcal{A}_{11}$ | $1$ |
| $\mathcal{B}=\Pi MQ$ | $3$ | $\mathcal{A}_{12},\mathcal{A}_{13},\mathcal{A}_{14}$ | $1+1+1$ |
| $\mathcal{C}=QM\Pi$ | $3$ | $\mathcal{A}_{21},\mathcal{A}_{31},\mathcal{A}_{41}$ | $1+1+1$ |
| $\mathcal{D}=QMQ$ | $9$ | $\mathcal{A}_{kl}$, $k,l\in\{2,3,4\}$ | $9$ |

The table is the block structure of the coordinate matrix: the row $1$, the column $1$, and the lower-right $3\times3$ block.

## The Comparison with the Biquaternion Case

At $n=2$ the algebra is $M_2(\mathbb{C})$, the biquaternion algebra as a complex algebra. Its root of $+1$ gives two idempotents $P_+,P_-$, and the full Peirce decomposition has four corners,

$$
M_2(\mathbb{C})=\mathcal{A}_{++}\oplus\mathcal{A}_{+-}\oplus\mathcal{A}_{-+}\oplus\mathcal{A}_{--},
$$

each a line. A rank-one idempotent $\Pi=P_+$ has complement $Q=P_-$, of rank one, so the coarse split is

$$
1+1+1+1,
$$

the same four lines. **The coarse and the fine decompositions coincide at $n=2$**, and this is a feature of the dimension two, not a general fact: the complement of a line in $\mathbb{C}^2$ is a line, so there is nothing left to refine.

At $n=4$ the complement of a line is a three-dimensional space, and the coarse split is $1+3+3+9$. The fine split has sixteen lines. The four diagonal lines $\mathcal{A}_{kk}$ are the four idempotents; the other twelve lines are the off-diagonal corners. The biquaternion's "four lines" are all four Peirce lines of $M_2$; the four diagonal lines of $M_4$ are only a quarter of its sixteen Peirce lines.

**The gauge is not a second idempotent.** In $M_2$ the mixed corner is a line, and the choice of its generator is one complex parameter; that is the gauge $\lambda$ of the biquaternion frame. In $M_4$ the off-diagonal corners are also lines, but there are twelve of them, and the gauge that rescales the frame vectors has three parameters, one per simple nilpotent, not one per corner. The idempotents are fixed by the root; the gauge rescales the nilpotents and leaves the idempotents unchanged. The details are *The Frame, the Simple Nilpotents and the Gauge*.

## What the Decomposition Is Not

**The Peirce decomposition is a direct-sum decomposition of the algebra, not a list of spinors.** The summands are spaces of linear maps between the lines of a flag. An element of $\mathcal{A}_{kl}$ is a map $V_l\to V_k$ of rank at most one, not a spinor. Calling every matrix unit a spinor would make every element of the sixteen-dimensional algebra a spinor, which is false.

**The carrier is not a corner.** The carrier of the spin chain is $\mathbb{C}^4=\operatorname{Sym}^3(\mathbb{C}^2)$, of dimension four. The corner $\mathcal{A}_{kl}$ has dimension one for every $k,l$. The carrier is not isomorphic to a corner, and the spin-$\tfrac32$ representation is not a Peirce line. The relation between the carrier and the corners is the subject of *The Spin Chain and the Adjoint Decomposition* and *The Modules and the Minimal Left Ideals*.

**The decomposition is not a decomposition into ideals.** The algebra $M_4(\mathbb{C})$ is simple. The four coarse corners are subspaces; the diagonal pair is a subalgebra; none of them is a two-sided ideal. The Peirce decomposition is a decomposition of the vector space together with a graded multiplication, and the multiplication rule is the content.

## Summary

A root of order four with simple spectrum gives four idempotents $P_k$ and a complete spectral flag. The Peirce corners $\mathcal{A}_{kl}=P_kM_4P_l$ are sixteen lines summing to the algebra, with the multiplication rule $\mathcal{A}_{kl}\mathcal{A}_{mn}\subseteq\delta_{lm}\mathcal{A}_{kn}$; in a frame they are the matrix units, and the Peirce coordinates are the matrix entries. A rank-one idempotent $\Pi$ cuts the algebra into four coarse corners of dimensions $1+3+3+9$, with diagonal corners $\mathbb{C}$ and $M_3(\mathbb{C})$ and off-diagonal corners $\mathbb{C}^{1\times3}$ and $\mathbb{C}^{3\times1}$; the off-diagonal blocks multiply back into the diagonal, so the split is not a direct sum of algebras. Refining the $M_3$ corner by $P_2$ and then the $M_2$ corner by $P_3$ gives the recursion $1+(n-1)+(n-1)+(n-1)^2$ and the sixteen fine lines. At $n=2$ the coarse and fine splits coincide; at $n=4$ they do not. The decomposition is a direct sum of spaces of maps, not of ideals and not of spinors.

$$
\boxed{\ M_4(\mathbb{C})=\bigoplus_{k,l=1}^{4}\mathcal{A}_{kl},\qquad \mathcal{A}_{kl}\mathcal{A}_{mn}\subseteq\delta_{lm}\mathcal{A}_{kn},\qquad \dim_\mathbb{C}\mathcal{A}_{kl}=1.\ }
$$

| Split | Corners | Dimensions |
|---|---|---|
| Fine, by $P_1,P_2,P_3,P_4$ | $\mathcal{A}_{kl}=P_kM_4P_l$ | $16\times1$ |
| Coarse, by $P_1$ | $\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D}$ | $1+3+3+9$ |
| Coarse, rank two | $\Pi M\Pi,\Pi MQ,QM\Pi,QMQ$ | $4+4+4+4$ |
| Biquaternion, $n=2$ | four corners | $1+1+1+1$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_k$ | the Lagrange projector of $\zeta_k$, rank one |
| $V_k=\operatorname{im}P_k$ | the $k$-th spectral line |
| $F_k=V_1\oplus\cdots\oplus V_k$ | the spectral flag |
| $\mathcal{A}_{kl}=P_kM_4P_l$ | the fine Peirce corner, a line |
| $\Pi$, $Q=I-\Pi$ | a coarse rank-one idempotent and its complement |
| $\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D}$ | the coarse corners $\Pi M\Pi$, $\Pi MQ$, $QM\Pi$, $QMQ$ |
| $a_{kl}=\ell_k(Xv_l)$ | the Peirce coordinates of $X$ |
| $E_{kl}=v_k\ell_l$ | the matrix unit of the frame |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions, corner algebras and the multiplication table.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for block matrices, ranks and the spectral decomposition.
- [Roots of Unity and the Lagrange Idempotents](roots-of-unity-and-the-lagrange-idempotents-of-m4c.html), for the idempotents that produce the flag.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m4c.html), for the vectors inside the corner lines and the gauge.
- [The Rank-Two Split](the-rank-two-split-of-m4c.html), for the coarse split by an idempotent of rank two.
- [The Spin Chain and the Adjoint Decomposition](the-spin-chain-and-the-adjoint-decomposition-of-m4c.html), for the carrier, which is not a corner.
- [The Peirce Decomposition and the Corner Recursion](the-peirce-decomposition-and-the-corner-recursion-mnc.html), for the general construction at order $n$.
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the biquaternion case $n=2$, where the coarse and fine splits coincide.
