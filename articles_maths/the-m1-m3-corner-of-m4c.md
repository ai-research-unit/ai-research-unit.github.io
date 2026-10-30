# __The $M_1\oplus M_3$ Corner of $M_4(\mathbb{C})$__

## Introduction

Let $P$ be a rank-one idempotent of $M_4(\mathbb{C})$ and $Q=I-P$ its complement. The **compression** of the algebra to $P$ is $PM_4P=\{PAP:A\in M_4\}$, and the compression to $Q$ is $QM_4Q$. The first is one-dimensional, the second is a copy of $M_3(\mathbb{C})$, and the two off-diagonal blocks $PM_4Q$ and $QM_4P$ carry the maps between the line $\operatorname{im}P$ and the hyperplane $\operatorname{im}Q$. The dimensions are

$$
1+3+3+9=16,
$$

the extreme case of the corner recursion of the category.

This article states the split, the multiplication table, the two corner isomorphisms, the inherited trace and the determinant of the compression, the parabolic that stabilises $P$, and the Hermitian case. The rank-two split $M_2\oplus M_2$, with corners $4+4+4+4$, is *The Rank-Two Split of $M_4(\mathbb{C})$*; the recursion for general $n$ is *The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$*; the general theory of the compression is *The $M_2$ Corner of $M_3(\mathbb{C})$*, whose proofs apply here without change.

## The Rank-One Idempotent and the Split

**Definition.** An idempotent $P\in M_4(\mathbb{C})$ is a matrix with $P^{2}=P$. It is of **rank one** when $\operatorname{rank}P=1$. Its complement is $Q=I-P$.

**Proposition.** Let $P$ be a rank-one idempotent. Then $Q$ is an idempotent of rank three, $PQ=QP=0$, and

$$
\mathbb{C}^{4}=\operatorname{im}P\oplus\operatorname{im}Q=\operatorname{im}P\oplus\ker P.
$$

**Proof.** $Q^{2}=I-2P+P^{2}=I-P=Q$. The rank of $Q$ is $4-1=3$ because $QP=0$ and $PQ=0$ give $\operatorname{im}Q\subseteq\ker P$ and $\ker P\subseteq\operatorname{im}Q$, and $\dim\ker P=3$. The sum is direct because $P+Q=I$ and $PQ=0$.

**The standard form.** In a basis whose first vector spans $\operatorname{im}P$ and whose remaining three vectors span $\ker P$, the idempotent is

$$
P=\operatorname{diag}(1,0,0,0)=E_{11},\qquad Q=\operatorname{diag}(0,1,1,1).
$$

Every rank-one idempotent is conjugate to this one: a rank-one idempotent is the projection onto a line along a complementary hyperplane, and $GL_4$ acts transitively on the pairs (line, complementary hyperplane).

**The two readings.** The pair $(\operatorname{im}P,\ker P)$ is a **flag** $0\subset L\subset\mathbb{C}^{4}$ with $\dim L=1$. The idempotent determines the flag and is determined by it: $P$ is the projection with image $L$ and kernel the hyperplane $H$. The set of rank-one idempotents is therefore the total space of the bundle over $\operatorname{Gr}(1,4)=\mathbb{P}^{3}$ whose fibre at $L$ is the open set of complements of $L$ in $\mathbb{C}^{4}$, an affine space of dimension three.

## The Four Blocks

**Definition.** The **Peirce blocks** of $P$ are

$$
A_{11}=PM_4P,\qquad A_{12}=PM_4Q,\qquad A_{21}=QM_4P,\qquad A_{22}=QM_4Q.
$$

**Proposition (the dimensions).** In the standard form,

$$
A_{11}=\mathbb{C}E_{11},\qquad
A_{12}=\{a_{1j}E_{1j}:j=2,3,4\},\qquad
A_{21}=\{a_{i1}E_{i1}:i=2,3,4\},\qquad
A_{22}=M_3(\mathbb{C}),
$$

and

$$
\dim A_{11}=1,\qquad \dim A_{12}=3,\qquad \dim A_{21}=3,\qquad \dim A_{22}=9.
$$

**Proof.** A matrix $PAP$ has only the entry $(1,1)$ nonzero, because $P$ keeps the first row and the first column. A matrix $PAQ$ has only the first row and the columns $2,3,4$, so it is an arbitrary row of length three; a matrix $QAP$ is an arbitrary column of length three in the first column; and $QAQ$ is an arbitrary $3\times3$ matrix in the entries $(i,j)$ with $i,j\ge2$. The blocks are direct and their dimensions sum to $16$.

**The multiplication table.** For $X_{ij}\in A_{ij}$,

| Product | Lies in |
|---|---|
| $A_{11}A_{11}$ | $A_{11}$ |
| $A_{11}A_{12}$ | $A_{12}$ |
| $A_{12}A_{21}$ | $A_{11}$ |
| $A_{12}A_{22}$ | $A_{12}$ |
| $A_{21}A_{11}$ | $A_{21}$ |
| $A_{21}A_{12}$ | $A_{22}$ |
| $A_{22}A_{21}$ | $A_{21}$ |
| $A_{22}A_{22}$ | $A_{22}$ |

**Proof.** Each product is read from $P^{2}=P$, $Q^{2}=Q$ and $PQ=QP=0$: for instance $A_{12}A_{21}=(PMQ)(QMP)\subseteq PMP=A_{11}$, and $A_{21}A_{12}=(QMP)(PMQ)\subseteq QMQ=A_{22}$. The products $A_{11}A_{21}$ and $A_{22}A_{12}$ vanish, and they are absent from the table.

**The block form.** In the standard basis an element of $M_4$ is

$$
\begin{pmatrix}
a&\beta\\ \gamma&D
\end{pmatrix},\qquad a\in\mathbb{C},\ \beta\in\mathbb{C}^{1\times3},\ \gamma\in\mathbb{C}^{3\times1},\ D\in M_3(\mathbb{C}),
$$

and the product is the ordinary block product. The blocks $A_{ij}$ are the four positions of the array.

## The Two Corner Isomorphisms

**Theorem.** The compression $A_{11}=PM_4P$ is isomorphic to $\mathbb{C}$ with unit $P$, by $PAP\mapsto a$ in the standard form. The compression $A_{22}=QM_4Q$ is isomorphic to $M_3(\mathbb{C})$ with unit $Q$, by $QAQ\mapsto D$.

**Proof.** The map $PAP\mapsto a$ is a homomorphism because $(PAP)(PBP)=P(APA)PB P$ reduces in the standard form to the product of the scalars; it is bijective onto $\mathbb{C}$ because $a$ is arbitrary. The second map is the restriction of $QAQ$ to $\operatorname{im}Q$, which is an isomorphism onto $\operatorname{End}(\operatorname{im}Q)\cong M_3(\mathbb{C})$ by the argument of *The $M_2$ Corner of $M_3(\mathbb{C})$*. In both cases the unit of the corner is the idempotent, $P$ or $Q$, and not the ambient unit $I$.

**The corner is not an ideal.** $A_{11}\oplus A_{22}$ is a subalgebra of dimension $10$ with unit $P+Q=I$, but it is not a two-sided ideal: $A_{12}$ and $A_{21}$ carry elements out of it. The algebra $M_4$ is simple and has no nontrivial two-sided ideals; the split is a decomposition of the carrier and of the multiplication table, not a direct sum of ideals.

**The off-diagonal blocks are bimodules.** $A_{12}$ is a left module over $A_{11}=\mathbb{C}$ and a right module over $A_{22}=M_3$, that is, an $M_3$-module of dimension three; it is the standard module of $M_3$, and $A_{21}$ is its dual. The two blocks are exchanged by the involution when $P$ is Hermitian.

**The inherited trace.** For $X\in A_{11}\oplus A_{22}$ the ambient trace and the corner trace agree: $\operatorname{tr}_{M_4}X=\operatorname{tr}_{A_{11}}X+\operatorname{tr}_{A_{22}}X$. In the standard form this is the identity $\operatorname{tr}A=a+\operatorname{tr}D$. The determinant does not agree: $\det_{M_4}A=a\det D$ is the product of the two corner determinants, and the determinant of the compression $A_{22}$ is $\det D$, the determinant of the $3\times3$ block.

## The Parabolic and the Flag

**Proposition.** The stabiliser of $P$ in $GL_4(\mathbb{C})$ is the block-diagonal subgroup

$$
GL_1(\mathbb{C})\times GL_3(\mathbb{C})
=\left\{\begin{pmatrix}a&0\\0&D\end{pmatrix}:a\ne0,\ \det D\ne0\right\},
$$

of dimension $1+9=10$.

**Proof.** For $g\in GL_4$, the conjugate $gPg^{-1}$ is the projection onto $g(\operatorname{im}P)$ along $g(\ker P)$. It equals $P$ exactly when $g$ preserves both the line and the hyperplane. In the block form

$$
g=\begin{pmatrix}a&\beta\\ \gamma&D\end{pmatrix},
$$

the condition $g(\operatorname{im}P)=\operatorname{im}P$ gives $\gamma=0$, and the condition $g(\ker P)=\ker P$ gives $\beta=0$. The remaining block is arbitrary invertible block diagonal, of dimension $1+9$.

**The orbit.** The orbit of $P$ under conjugation is the set of rank-one idempotents, which is the total space of the bundle over $\operatorname{Gr}(1,4)=\mathbb{P}^{3}$ with affine fibre $\mathbb{C}^{3}$, of dimension $6$. The orbit–stabiliser count is

$$
16=6+10,
$$

the dimension of $GL_4$ being the dimension of the orbit plus the dimension of the stabiliser.

**The parabolic.** The subgroup that preserves the line $L=\operatorname{im}P$ alone, and not the hyperplane, is the parabolic

$$
P(1,3)=\left\{\begin{pmatrix}a&\beta\\0&D\end{pmatrix}:a\ne0,\ \det D\ne0\right\},
$$

of dimension $1+3+9=13$. It contains the stabiliser of $P$, and the quotient $P(1,3)/(GL_1\times GL_3)$ is the affine space of complements of $L$ in $\mathbb{C}^{4}$, of dimension $3$. The parabolic is the stabiliser of the flag $0\subset L\subset\mathbb{C}^{4}$, and the flag variety of lines is $\operatorname{Gr}(1,4)=\mathbb{P}^{3}$, of dimension $3$; the count $16=3+13$ is the orbit–stabiliser count for the action on lines.

**The extreme case.** The choice $p=1$ in the corner recursion gives $M_4\supset M_1\oplus M_3$; the choice $p=3$ gives $M_4\supset M_3\oplus M_1$; the choice $p=2$ gives the rank-two split $M_2\oplus M_2$ of *The Rank-Two Split of $M_4(\mathbb{C})$*. The three splits are the block-diagonal subalgebras attached to the three maximal parabolics; at $p=2$ the two blocks have equal size, and the split is the one that the chiral reading of the algebra uses.

## The Hermitian Case

**Proposition.** Let $P$ be a rank-one idempotent with $P=P^{*}$. Then $Q=Q^{*}$, the corner $A_{22}$ is a $*$-subalgebra with unit $Q$, and the two off-diagonal blocks are conjugate to each other, $A_{12}^{*}=A_{21}$.

**Proof.** $Q^{*}=I-P^{*}=Q$. For $X=QAQ\in A_{22}$, $X^{*}=Q A^{*}Q\in A_{22}$, and the unit is $Q$. For $Y=PAQ\in A_{12}$, $Y^{*}=Q A^{*}P\in A_{21}$.

**The unitary group.** In the standard form the Hermitian idempotents are the orthogonal projections, and the subgroup of $U(4)$ preserving the split is $U(1)\times U(3)$, embedded block diagonally. The inclusion is the compact form of the parabolic: the parabolic $P(1,3)$ retracts onto its maximal compact subgroup $U(1)\times U(3)$.

**The failure for a non-Hermitian idempotent.** For a general $P$ the corner $A_{22}$ is not stable under the involution: $X\in QMQ$ has $X^{*}\in Q^{*}MQ^{*}$, the corner of the other idempotent $Q^{*}$. The two corners $QMQ$ and $Q^{*}MQ^{*}$ are isomorphic as algebras but are different subalgebras of $M_4$; the involution exchanges them. The corner is a $*$-algebra exactly when $P$ is Hermitian.

## Summary

A rank-one idempotent splits $M_4(\mathbb{C})$ into the four Peirce blocks of dimensions $1$, $3$, $3$ and $9$. The diagonal corners are $\mathbb{C}$ with unit $P$ and $M_3(\mathbb{C})$ with unit $Q$; the off-diagonal blocks are the standard module of $M_3$ and its dual. The ambient trace is the sum of the corner traces, while the ambient determinant is the product $a\det D$ of the two corner determinants. The stabiliser of $P$ in $GL_4$ is the block-diagonal $GL_1\times GL_3$ of dimension $10$; the parabolic $P(1,3)$ that stabilises the line $L$ has dimension $13$. The orbit is the affine bundle of rank-one idempotents over $\mathbb{P}^{3}$, of dimension $6$. For a Hermitian $P$ the corner is a $*$-subalgebra and the compact stabiliser is $U(1)\times U(3)$.

| Quantity | Value |
|---|---|
| $\dim A_{11}$ | $1$ |
| $\dim A_{12}$ | $3$ |
| $\dim A_{21}$ | $3$ |
| $\dim A_{22}$ | $9$ |
| $\dim(A_{11}\oplus A_{22})$ | $10$ |
| Stabiliser of $P$ in $GL_4$ | $10$ |
| Parabolic $P(1,3)$ | $13$ |
| Rank-one idempotents | $6$ |
| $\operatorname{Gr}(1,4)=\mathbb{P}^{3}$ | $3$ |
| Full flag variety | $6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$ | a rank-one idempotent, $P^{2}=P$, $\operatorname{rank}P=1$ |
| $Q=I-P$ | the complementary idempotent |
| $A_{ij}$ | the Peirce blocks $PM_4P$, $PM_4Q$, $QM_4P$, $QM_4Q$ |
| $L=\operatorname{im}P$ | the line of the flag |
| $H=\ker P$ | the hyperplane of the flag |
| $P(1,3)$ | the parabolic of block upper triangular matrices with blocks $1$ and $3$ |
| $\operatorname{Gr}(1,4)$ | the Grassmannian of lines in $\mathbb{C}^{4}$, isomorphic to $\mathbb{P}^{3}$ |
| $D$ | the $3\times3$ block of $A_{22}$ |

## Further Reading

- [The Rank-Two Split of $M_4(\mathbb{C})$](the-rank-two-split-of-m4c.html), for the split $M_2\oplus M_2$ and the corners $4+4+4+4$.
- [The $M_2$ Corner of $M_3(\mathbb{C})$](the-m2-corner-of-m3c.html), for the general compression and its proofs.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the fine Peirce decomposition by four idempotents.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-mnc.html), for the recursion $M_n\supset M_p\oplus M_{n-p}$.
- [The Geometry of the Idempotents of $M_4(\mathbb{C})$](the-geometry-of-the-idempotents-of-m4c.html), for the homogeneous space of idempotents of each rank.
- [The Modules and the Minimal Left Ideals of $M_4(\mathbb{C})$](the-modules-and-the-minimal-left-ideals-of-m4c.html), for $M_4P$ as a minimal left ideal.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), for the parabolic and the flag variety.
