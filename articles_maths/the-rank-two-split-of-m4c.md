# __The Rank-Two Split of $M_4(\mathbb{C})$__

## Introduction

**The rank-two idempotent $\Pi=P_+$ cuts $M_4(\mathbb{C})$ into four corners of dimension four each, and the diagonal corners are two copies of $M_2(\mathbb{C})$.** The split is the balanced split $M_4\supset M_2\oplus M_2$; the off-diagonal corners are the two mass blocks, and the block-diagonal subalgebra is not an ideal. The split is the chiral block decomposition of *The Two Chiralities of $M_4(\mathbb{C})$*, read as a Peirce decomposition.

The article states the rank-two idempotent, proves the corner dimensions $4+4+4+4$, identifies the two diagonal corners with $M_2(\mathbb{C})$, describes the two carrier modules and the mass block, gives the two-sided Peirce table and the multiplication table, and explains why the split is a vector-space decomposition and a subalgebra inclusion, not a direct sum of algebras.

The rank-one split is *The Peirce Decomposition of $M_4(\mathbb{C})$*; the chirality is *The Two Chiralities of $M_4(\mathbb{C})$*; the mass block and its polar decomposition are *The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*; the two $\mathfrak{su}_2$'s are *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*. The general recursion is *The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$*.

## The Rank-Two Idempotent

**Definition.** The **rank-two idempotent** of the root is

$$
\Pi=P_+=\frac12(I+\Gamma)=P_1+P_3,
$$

and its complement is

$$
Q=P_-=\frac12(I-\Gamma)=P_2+P_4 .
$$

**Proposition.** The elements $\Pi,Q$ are idempotent, orthogonal and complete:

$$
\Pi^2=\Pi,\qquad Q^2=Q,\qquad \Pi Q=Q\Pi=0,\qquad \Pi+Q=I.
$$

Each has rank $2$ and trace $2$. Their images are the two chiralities:

$$
\operatorname{im}\Pi=\mathbb{C}^2_+,\qquad \operatorname{im}Q=\mathbb{C}^2_- .
$$

**Proof.** $\Pi$ and $Q$ are the spectral projectors of the involution $\Gamma$ for the eigenvalues $+1$ and $-1$. The algebraic identities follow from $\Gamma^2=I$; the ranks are the dimensions of the eigenspaces; the traces are the ranks.

**The standard model.** For $\Gamma_0=\operatorname{diag}(1,-1,1,-1)$,

$$
\Pi_0=\operatorname{diag}(1,0,1,0)=E_{11}+E_{33},
\qquad
Q_0=\operatorname{diag}(0,1,0,1)=E_{22}+E_{44}.
$$

In this frame the two chiralities are the coordinate planes $\operatorname{span}\{e_1,e_3\}$ and $\operatorname{span}\{e_2,e_4\}$.

## The Four Corners

**Definition.** The **rank-two Peirce corners** are

$$
\mathcal{A}=\Pi M_4\Pi,\qquad
\mathcal{B}=\Pi M_4Q,\qquad
\mathcal{C}=QM_4\Pi,\qquad
\mathcal{D}=QM_4Q .
$$

**Theorem.** The algebra is the direct sum

$$
M_4(\mathbb{C})=\mathcal{A}\oplus\mathcal{B}\oplus\mathcal{C}\oplus\mathcal{D},
$$

with

$$
\dim_\mathbb{C}\mathcal{A}=4,\qquad
\dim_\mathbb{C}\mathcal{B}=4,\qquad
\dim_\mathbb{C}\mathcal{C}=4,\qquad
\dim_\mathbb{C}\mathcal{D}=4.
$$

The diagonal corners are full matrix algebras,

$$
\mathcal{A}\cong M_2(\mathbb{C}),\qquad
\mathcal{D}\cong M_2(\mathbb{C}),
$$

and the off-diagonal corners are the spaces of maps between the two chiralities,

$$
\mathcal{B}\cong\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)\cong M_2(\mathbb{C}),
\qquad
\mathcal{C}\cong\operatorname{Hom}(\mathbb{C}^2_+,\mathbb{C}^2_-)\cong M_2(\mathbb{C}).
$$

**Proof.** Choose a basis adapted to $\mathbb{C}^4=\mathbb{C}^2_+\oplus\mathbb{C}^2_-$, with the first two vectors in $\mathbb{C}^2_+$ and the last two in $\mathbb{C}^2_-$. In that basis

$$
\Pi=\begin{pmatrix}I_2&0\\0&0\end{pmatrix},
\qquad
Q=\begin{pmatrix}0&0\\0&I_2\end{pmatrix},
$$

and the four corners are the four $2\times2$ blocks of a block matrix. Each block has four entries, so each corner has dimension four. The diagonal blocks are closed under multiplication and are full matrix algebras with units $\Pi$ and $Q$; the off-diagonal blocks are the spaces of linear maps between the two planes.

**The compressed units.** The unit of $\mathcal{A}$ is $\Pi$, not $I$; the unit of $\mathcal{D}$ is $Q$. For an element $X$, the trace of its compression to $\mathcal{A}$ is $\operatorname{tr}(\Pi X\Pi)$, the trace of the $2\times2$ block, which differs from $\operatorname{tr}X$ in general; on $\mathcal{A}$ itself the two agree. The two diagonal corners are matrix algebras with their own units, and the embedding $\mathcal{A}\oplus\mathcal{D}\subset M_4$ is unital with unit $\Pi+Q=I$, while neither summand contains $I$.

**The block form.** A general element is

$$
A=\begin{pmatrix}A_{++}&A_{+-}\\A_{-+}&A_{--}\end{pmatrix},
\qquad
A_{++}\in\mathcal{A},\quad A_{+-}\in\mathcal{B},\quad A_{-+}\in\mathcal{C},\quad A_{--}\in\mathcal{D}.
$$

The product is

$$
\begin{pmatrix}A&B\\C&D\end{pmatrix}
\begin{pmatrix}A'&B'\\C'&D'\end{pmatrix}
=
\begin{pmatrix}
AA'+BC'&AB'+BD'\\
CA'+DC'&CB'+DD'
\end{pmatrix}.
$$

The products $BC'\subseteq\mathcal{A}$ and $CB'\subseteq\mathcal{D}$ are the cross terms; they are the reason the split is not an algebra direct sum.

## The Two Carrier Modules

**The two carrier spaces.** The idempotent $\Pi$ defines the left module

$$
L_+=M_4\Pi=\{X\Pi:X\in M_4\},
$$

of complex dimension $8$, and $Q$ defines

$$
L_-=M_4Q=\{XQ:X\in M_4\},
$$

also of dimension $8$. These are the **two algebraic carrier modules** of the split. The first is the set of matrices that kill the second chirality, equivalently the space of maps $\mathbb{C}^2_+\to\mathbb{C}^4$; the second is the set that kills the first chirality, equivalently the space of maps $\mathbb{C}^2_-\to\mathbb{C}^4$.

**Proposition.** As a left module over the block-diagonal algebra $\mathcal{A}\oplus\mathcal{D}$,

$$
L_+\cong\mathcal{A}\oplus\mathcal{C},\qquad
L_-\cong\mathcal{B}\oplus\mathcal{D}.
$$

**Proof.** A matrix in $L_+$ has zero second block-column; its first block-column has a top part in $\mathcal{A}=\Pi M\Pi$ and a bottom part in $\mathcal{C}=QM\Pi$. The left action of $\mathcal{A}\oplus\mathcal{D}$ preserves the row decomposition and acts on the two parts by $\mathcal{A}$ and $\mathcal{D}$ respectively. The same argument with the second block-column gives $L_-\cong\mathcal{B}\oplus\mathcal{D}$.

**The two carrier spaces of the spin chain.** The spin chain of *The Spin Chain and the Adjoint Decomposition of $M_4(\mathbb{C})$* has one carrier, $\mathbb{C}^4=\operatorname{Sym}^3(\mathbb{C}^2)$. The rank-two split has two carrier spaces, $\mathbb{C}^2_+$ and $\mathbb{C}^2_-$, one per chirality. They are the modules of the two $M_2$ factors:

$$
\mathcal{A}\ \text{acts on}\ \mathbb{C}^2_+,
\qquad
\mathcal{D}\ \text{acts on}\ \mathbb{C}^2_- .
$$

The maps in $\mathcal{B}$ go from $\mathbb{C}^2_-$ to $\mathbb{C}^2_+$; the maps in $\mathcal{C}$ go from $\mathbb{C}^2_+$ to $\mathbb{C}^2_-$. The two carrier spaces are two-dimensional; the spin chain carrier is four-dimensional. They are different objects with similar names.

**The mass block.** The corner

$$
\mathcal{B}=\Pi M_4Q=\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)
$$

is the **mass block**. It is four-dimensional, and it is a bimodule: $\mathcal{A}$ acts on the left and $\mathcal{D}$ acts on the right. An element $M\in\mathcal{B}$ is a linear map

$$
M:\mathbb{C}^2_-\longrightarrow\mathbb{C}^2_+,
$$

the mass operator of the split. The opposite corner $\mathcal{C}$ is the conjugate mass block, and the two together form the odd part of the algebra under $\operatorname{Ad}_\Gamma$. The polar decomposition of $M$ is *The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*.

## The Two-Sided Peirce Table

The four corners form a $2\times2$ table:

| | $\Pi$ | $Q$ |
|---|---|---|
| $\Pi$ | $\mathcal{A}\cong M_2(\mathbb{C})$ | $\mathcal{B}\cong M_2(\mathbb{C})$ |
| $Q$ | $\mathcal{C}\cong M_2(\mathbb{C})$ | $\mathcal{D}\cong M_2(\mathbb{C})$ |

The entry in row $\Pi$ and column $\Pi$ is the corner $\Pi M\Pi$; the entry in row $\Pi$ and column $Q$ is $\Pi MQ$; and so on. The table is the **two-sided Peirce table** of the pair $(\Pi,Q)$.

**The multiplication table.** The product of the corner in row $i$ and column $j$ with the corner in row $k$ and column $l$ is contained in the corner in row $i$ and column $l$ when $j=k$, and is zero otherwise:

$$
(\Pi_iM\Pi_j)(\Pi_kM\Pi_l)\subseteq\delta_{jk}\Pi_iM\Pi_l,
$$

where $\Pi_1=\Pi$ and $\Pi_2=Q$. Written as a table:

| $\cdot$ | $\mathcal{A}$ | $\mathcal{B}$ | $\mathcal{C}$ | $\mathcal{D}$ |
|---|---|---|---|---|
| $\mathcal{A}$ | $\mathcal{A}$ | $\mathcal{B}$ | $\mathcal{C}$ | $0$ |
| $\mathcal{B}$ | $0$ | $0$ | $\mathcal{A}$ | $\mathcal{B}$ |
| $\mathcal{C}$ | $\mathcal{C}$ | $\mathcal{D}$ | $0$ | $0$ |
| $\mathcal{D}$ | $0$ | $0$ | $\mathcal{C}$ | $\mathcal{D}$ |

**The refinement into lines.** Each four-dimensional corner is the sum of four fine Peirce lines:

$$
\mathcal{A}=\mathcal{A}_{11}\oplus\mathcal{A}_{13}\oplus\mathcal{A}_{31}\oplus\mathcal{A}_{33},
$$

$$
\mathcal{B}=\mathcal{A}_{12}\oplus\mathcal{A}_{14}\oplus\mathcal{A}_{32}\oplus\mathcal{A}_{34},
$$

$$
\mathcal{C}=\mathcal{A}_{21}\oplus\mathcal{A}_{23}\oplus\mathcal{A}_{41}\oplus\mathcal{A}_{43},
$$

$$
\mathcal{D}=\mathcal{A}_{22}\oplus\mathcal{A}_{24}\oplus\mathcal{A}_{42}\oplus\mathcal{A}_{44}.
$$

Each line is one-dimensional, and the sixteen lines are the full Peirce decomposition of *The Peirce Decomposition of $M_4(\mathbb{C})$*. The rank-two split groups the sixteen lines into four groups of four. It is a different grouping from the rank-one split, whose corners have dimensions $1,3,3,9$; neither grouping refines the other.

## The Failure of the Algebra Direct Sum

**The vector-space direct sum is not an algebra direct sum.** The algebra is the direct sum of the four corners as vector spaces, but it is not the direct sum of $\mathcal{A}$ and $\mathcal{D}$ as algebras. The off-diagonal blocks $\mathcal{B}$ and $\mathcal{C}$ are nonzero, and the cross terms

$$
\mathcal{B}\mathcal{C}\subseteq\mathcal{A},\qquad
\mathcal{C}\mathcal{B}\subseteq\mathcal{D}
$$

return to the diagonal. If the off-diagonal blocks were zero, the algebra would be $\mathcal{A}\oplus\mathcal{D}$; they are not, and the algebra is larger.

**The block-diagonal part is a subalgebra, not an ideal.** The subspace

$$
\mathcal{A}\oplus\mathcal{D}=\left\{\begin{pmatrix}A&0\\0&D\end{pmatrix}\right\}
$$

is closed under multiplication and contains the unit $I$. It is isomorphic to $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, the balanced subalgebra $M_2\oplus M_2$ of the recursion. It is not a two-sided ideal: multiplying a block-diagonal element by a general element produces an off-diagonal part. Indeed, $M_4(\mathbb{C})$ is simple, so it has no proper two-sided ideal at all.

**The meaning of "contains".** When the category says that $M_4$ contains $M_2\oplus M_2$, the word means the block-diagonal subalgebra, not an ideal and not a quotient. The inclusion is

$$
M_2(\mathbb{C})\oplus M_2(\mathbb{C})\longrightarrow M_4(\mathbb{C}),\qquad
(A,D)\longmapsto\begin{pmatrix}A&0\\0&D\end{pmatrix},
$$

and the off-diagonal blocks complete the image to the whole algebra. The same convention applies to the other categories: $M_6$ contains $M_3\oplus M_3$ and $M_5$ contains $M_2\oplus M_3$ as block-diagonal subalgebras.

**The trace and the determinant.** The trace splits as

$$
\operatorname{tr}A=\operatorname{tr}A_{++}+\operatorname{tr}A_{--},
$$

a sum of the traces of the two diagonal blocks. The determinant is the determinant of the full block matrix; when $A_{--}$ is invertible,

$$
\det A=\det(A_{++}-A_{+-}A_{--}^{-1}A_{-+})\det A_{--},
$$

and the formula extends by continuity when $A_{--}$ is singular.

The mass block enters through the Schur complement $A_{+-}A_{--}^{-1}A_{-+}$, which is a map on $\mathbb{C}^2_+$. The determinant is not the product $\det A_{++}\det A_{--}$ unless the mass block is zero.

## Comparison with the Rank-One Split and with $M_2$

**The rank-one split.** For the rank-one idempotent $\Pi=P_1$, the corners are

$$
1+3+3+9,
$$

with $\mathcal{A}\cong\mathbb{C}$, $\mathcal{D}\cong M_3$, $\mathcal{B}\cong\mathbb{C}^{1\times3}$ and $\mathcal{C}\cong\mathbb{C}^{3\times1}$. The rank-two split replaces the line and the three-space by two planes:

$$
1+3+3+9\ \longrightarrow\ 4+4+4+4.
$$

The rank-two split is the balanced split $M_2\oplus M_2$; the rank-one split is the unbalanced split $\mathbb{C}\oplus M_3$. The balanced split is the one adapted to the two chiralities, because both chiralities have the same dimension.

**The biquaternion case.** For $M_2(\mathbb{C})$, a rank-one idempotent $\Pi$ has complement $Q$ of rank one, and the split is

$$
1+1+1+1.
$$

There is no rank-two idempotent other than $I$, whose complement is $0$, so the balanced split $M_1\oplus M_1=\mathbb{C}\oplus\mathbb{C}$ is the only balanced split, and it is degenerate. The rank-two split $M_2\oplus M_2$ is a feature of $M_4$: it is the first case in which both chiralities are planes and both diagonal corners are non-scalar matrix algebras.

**The recursion.** The rank-two split is the case $p=2$ of the corner recursion

$$
M_n\supset M_p\oplus M_{n-p},
$$

and for $n=4$, $p=2$ gives $M_4\supset M_2\oplus M_2$. The rank-one split is the case $p=1$, $M_4\supset M_1\oplus M_3$. The two are the two nontrivial balanced-or-not splits of $M_4$; the third, $p=3$, is the complement of $p=1$ and gives the same dimensions in the opposite order.

## Summary

The rank-two idempotent $\Pi=P_+$ and its complement $Q=P_-$ cut the algebra into four corners of dimension four each:

$$
M_4(\mathbb{C})=\mathcal{A}\oplus\mathcal{B}\oplus\mathcal{C}\oplus\mathcal{D},
\qquad 4+4+4+4=16,
$$

with $\mathcal{A}\cong M_2(\mathbb{C})$, $\mathcal{D}\cong M_2(\mathbb{C})$, and $\mathcal{B},\mathcal{C}$ the mass blocks, each isomorphic to $M_2(\mathbb{C})$ as a vector space and to $\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)$ or its opposite as a bimodule. The diagonal part $\mathcal{A}\oplus\mathcal{D}$ is the block-diagonal subalgebra $M_2\oplus M_2$; it is not an ideal, and the cross terms $\mathcal{B}\mathcal{C}\subseteq\mathcal{A}$ and $\mathcal{C}\mathcal{B}\subseteq\mathcal{D}$ show that the split is not an algebra direct sum. The two algebraic carrier modules are $L_+=M_4\Pi\cong\mathcal{A}\oplus\mathcal{C}$ and $L_-=M_4Q\cong\mathcal{B}\oplus\mathcal{D}$, each of dimension eight; the mass block is the four-dimensional corner $\mathcal{B}$. The rank-two split is the balanced refinement of the rank-one split $1+3+3+9$ and the four-dimensional analogue of the biquaternion split $1+1+1+1$.

$$
\boxed{\ M_4=\mathcal{A}\oplus\mathcal{B}\oplus\mathcal{C}\oplus\mathcal{D},\qquad 4+4+4+4=16,\qquad \mathcal{A}\cong\mathcal{D}\cong M_2(\mathbb{C}),\qquad \mathcal{B}\cong\mathcal{C}\cong M_2(\mathbb{C}).\ }
$$

| Object | Dimension | Algebra or module |
|---|---|---|
| $\Pi=P_+$ | rank $2$ | idempotent |
| $Q=P_-$ | rank $2$ | complement |
| $\mathcal{A}=\Pi M\Pi$ | $4$ | $M_2(\mathbb{C})$ |
| $\mathcal{D}=QMQ$ | $4$ | $M_2(\mathbb{C})$ |
| $\mathcal{B}=\Pi MQ$ | $4$ | mass block, $\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)$ |
| $\mathcal{C}=Q M\Pi$ | $4$ | conjugate mass block |
| $\mathcal{A}\oplus\mathcal{D}$ | $8$ | block-diagonal $M_2\oplus M_2$ |
| $\mathcal{B}\oplus\mathcal{C}$ | $8$ | odd part |
| $L_+=M_4\Pi$ | $8$ | $\mathcal{A}\oplus\mathcal{C}$ |
| $L_-=M_4Q$ | $8$ | $\mathcal{B}\oplus\mathcal{D}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi=P_+$ | the rank-two idempotent, $\frac12(I+\Gamma)$ |
| $Q=P_-$ | the complement, $\frac12(I-\Gamma)$ |
| $\mathcal{A}=\Pi M_4\Pi$ | the left chiral corner, $\cong M_2(\mathbb{C})$ |
| $\mathcal{D}=QM_4Q$ | the right chiral corner, $\cong M_2(\mathbb{C})$ |
| $\mathcal{B}=\Pi M_4Q$ | the mass block |
| $\mathcal{C}=QM_4\Pi$ | the conjugate mass block |
| $L_+=M_4\Pi$, $L_-=M_4Q$ | the two algebraic carrier modules |
| $\mathbb{C}^2_\pm$ | the two carrier spaces |
| $\mathcal{A}_{kl}$ | the fine Peirce lines inside the corners |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions relative to a pair of orthogonal idempotents and for corner algebras.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for block matrices, Schur complements and the determinant.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the rank-one split and the sixteen fine lines.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the involution $\Gamma$ and the chiral blocks.
- [The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$](the-mass-block-and-the-chiral-polar-decomposition-of-m4c.html), for the mass operator and its polar decomposition.
- [The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$](the-peirce-su2-and-the-chiral-su2-su2-of-m4c.html), for the two $M_2$ factors and their Lie algebras.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-mnc.html), for the general recursion $M_n\supset M_p\oplus M_{n-p}$.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the biquaternion split $1+1+1+1$.
