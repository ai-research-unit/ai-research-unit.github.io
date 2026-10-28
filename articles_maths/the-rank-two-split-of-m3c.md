# __The Rank-Two Split of $M_3(\mathbb{C})$__

## Introduction

Let $P$ be a rank-two idempotent of $M_{3}(\mathbb{C})$ and $Q=I-P$ its rank-one complement. Relative to the decomposition

$$
\mathbb{C}^{3}=\operatorname{im}P\oplus\ker P,
$$

every matrix has a block form with a $2\times2$ block $M$, a column $u$, a row $v$ and a scalar $c$:

$$
A=\begin{pmatrix}M&u\\v&c\end{pmatrix},
\qquad
M\in M_{2}(\mathbb{C}),\quad u\in\mathbb{C}^{2},\quad v\in(\mathbb{C}^{2})^{*},\quad c\in\mathbb{C}.
$$

The four blocks are the four coarse Peirce corners $PMP$, $PMQ$, $QMP$, $QMQ$, of dimensions $4+2+2+1$. The product is the block product; the determinant is

$$
\det A=c\det M-v\operatorname{adj}(M)u,
$$

which exhibits the **mass block** $uv\in PMP$: the coupling of the two mixed corners can make $A$ invertible when the compression $M$ is singular, and the compression can be singular while $A$ is invertible. The trace is $\operatorname{tr}M+c$.

This article states the block decomposition, the corner dimensions, the multiplication table, the determinant formula and its consequences, and the comparison with the rank-one split $1+2+2+4$. The corner $PMP\cong M_{2}(\mathbb{C})$ as a unital algebra and as a $*$-algebra is *The $M_{2}$ Corner of $M_{3}(\mathbb{C})$*; the coarse split by a rank-one idempotent is *The Peirce Decomposition of $M_{3}(\mathbb{C})$*; the determinant and the singular set are *The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$*.

## The Block Decomposition

**Definition.** Let $P$ be a rank-two idempotent, $Q=I-P$, and choose a basis of $\mathbb{C}^{3}$ adapted to $\mathbb{C}^{3}=\operatorname{im}P\oplus\ker P$, with the first two vectors in $\operatorname{im}P$ and the third in $\ker P$. In this basis

$$
P=\begin{pmatrix}I_{2}&0\\0&0\end{pmatrix},
\qquad
Q=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

Write a matrix $A$ as

$$
A=\begin{pmatrix}M&u\\v&c\end{pmatrix},
\qquad
M\in M_{2}(\mathbb{C}),\quad u\in\mathbb{C}^{2},\quad v\in(\mathbb{C}^{2})^{*},\quad c\in\mathbb{C},
$$

where $u$ is a column, $v$ is a row, and $c$ is a scalar. The four blocks are

$$
PAP=\begin{pmatrix}M&0\\0&0\end{pmatrix},\quad
PAQ=\begin{pmatrix}0&u\\0&0\end{pmatrix},\quad
QAP=\begin{pmatrix}0&0\\v&0\end{pmatrix},\quad
QAQ=\begin{pmatrix}0&0\\0&c\end{pmatrix}.
$$

**Proposition.** The four coarse corners have dimensions

$$
\dim PMP=4,\qquad \dim PMQ=2,\qquad \dim QMP=2,\qquad \dim QMQ=1,
$$

and

$$
M_{3}(\mathbb{C})=PMP\oplus PMQ\oplus QMP\oplus QMQ
$$

as vector spaces. The sum is direct and the dimensions add to $4+2+2+1=9$.

**Proof.** In the adapted basis the four corners are the four blocks of the block decomposition: $PMP$ is the set of matrices with only the upper-left $2\times2$ block, of dimension $4$; $PMQ$ is the set with only the upper-right column, of dimension $2$; $QMP$ is the set with only the lower-left row, of dimension $2$; $QMQ$ is the set with only the lower-right entry, of dimension $1$. Every matrix is the sum of its four blocks, and a sum of blocks is zero only if each block is zero. The corners are the images of the maps $A\mapsto PAP$, $A\mapsto PAQ$, $A\mapsto QAP$, $A\mapsto QAQ$, which are the four components of the block decomposition.

**The rank-two idempotent in its own block form.** The idempotent $P$ itself is

$$
P=\begin{pmatrix}I_{2}&0\\0&0\end{pmatrix},
\qquad
Q=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\qquad
I=\begin{pmatrix}I_{2}&0\\0&1\end{pmatrix}.
$$

The two units $P$ and $Q$ are the diagonal blocks; $I=P+Q$.

**The corner dimensions are the multiplicities of the two units.** The corner $PMP$ is the algebra of endomorphisms of the two-dimensional image, of dimension $2^{2}=4$; the corner $QMQ$ is the algebra of endomorphisms of the one-dimensional kernel, of dimension $1^{2}=1$; the mixed corners are the homomorphisms between the two spaces, of dimensions $2\cdot1=2$ and $1\cdot2=2$. The count $4+2+2+1$ is the count $2^{2}+2\cdot1+1\cdot2+1^{2}=(2+1)^{2}=9$.

## The Multiplication Table

**Theorem (the block product).** For

$$
A=\begin{pmatrix}M&u\\v&c\end{pmatrix},\qquad
B=\begin{pmatrix}M'&u'\\v'&c'\end{pmatrix},
$$

the product is

$$
AB=\begin{pmatrix}MM'+uv'&Mu'+uc'\\vM'+cv'&vu'+cc'\end{pmatrix}.
$$

**Proof.** This is the ordinary product of block matrices, valid because the block sizes are compatible: $M$ is $2\times2$, $u$ is $2\times1$, $v$ is $1\times2$, $c$ is $1\times1$. The entry in the upper-left block is $MM'+uv'$; the upper-right is $Mu'+uc'$; the lower-left is $vM'+cv'$; the lower-right is $vu'+cc'$.

**The Peirce table.** The products of the four corners are

| $\cdot$ | $PMP$ | $PMQ$ | $QMP$ | $QMQ$ |
|---|---|---|---|---|
| $PMP$ | $PMP$ | $PMQ$ | $0$ | $0$ |
| $PMQ$ | $0$ | $0$ | $PMP$ | $PMQ$ |
| $QMP$ | $QMP$ | $QMQ$ | $0$ | $0$ |
| $QMQ$ | $0$ | $0$ | $QMP$ | $QMQ$ |

with the dimensions

| $\cdot$ | $PMP$ $(4)$ | $PMQ$ $(2)$ | $QMP$ $(2)$ | $QMQ$ $(1)$ |
|---|---|---|---|---|
| $PMP$ $(4)$ | $4$ | $2$ | $0$ | $0$ |
| $PMQ$ $(2)$ | $0$ | $0$ | $4$ | $2$ |
| $QMP$ $(2)$ | $2$ | $1$ | $0$ | $0$ |
| $QMQ$ $(1)$ | $0$ | $0$ | $2$ | $1$ |

The tables are the Peirce rule $B_{ij}B_{kl}\subseteq\delta_{jk}B_{il}$ read on the two-block split, with the indices $1$ for $P$ and $2$ for $Q$; the numerical table records only the dimensions of the corners, not the dimensions of the products, which can be smaller.

**The mixed corners are not ideals.** $PMQ$ is a left module over $PMP$ and a right module over $QMQ$; $QMP$ is the other way round. Neither is a two-sided ideal: multiplying $PMQ$ on the left by $QMP$ lands in $PMP$, and multiplying it on the right by $QMP$ vanishes. The algebra is simple, so no nonzero corner is an ideal, and the block decomposition is not a direct sum of algebras.

**The unit and the idempotents.** The unit $I$ has $M=I_{2}$, $u=0$, $v=0$, $c=1$. The idempotent $P$ has $M=I_{2}$, $u=0$, $v=0$, $c=0$. The idempotent $Q$ has $M=0$, $u=0$, $v=0$, $c=1$. A general idempotent with the same image and kernel as $P$ has $M=I_{2}$, $u=0$, $v=0$, $c=0$ in this basis; a general rank-two idempotent with a different kernel has a different block form.

## The Determinant and the Mass Block

**Theorem (the determinant formula).** For $A=\begin{pmatrix}M&u\\v&c\end{pmatrix}$,

$$
\boxed{\;\det A=c\det M-v\operatorname{adj}(M)u,\;}
$$

where $\operatorname{adj}(M)$ is the adjugate of the $2\times2$ matrix $M$, $\operatorname{adj}(M)=\operatorname{tr}(M)I_{2}-M$.

**Proof.** If $M$ is invertible, factor

$$
\begin{pmatrix}M&u\\v&c\end{pmatrix}
=
\begin{pmatrix}I&0\\vM^{-1}&1\end{pmatrix}
\begin{pmatrix}M&0\\0&c-vM^{-1}u\end{pmatrix}
\begin{pmatrix}I&M^{-1}u\\0&1\end{pmatrix}.
$$

The first and third factors are block triangular with diagonal blocks $I$ and $1$, so each has determinant $1$; the middle factor is block diagonal with determinant $\det M\,(c-vM^{-1}u)$. Multiplying gives

$$
\det A=\det M\,(c-vM^{-1}u)=c\det M-v(\det M\,M^{-1})u=c\det M-v\operatorname{adj}(M)u,
$$

because $\operatorname{adj}(M)=\det M\,M^{-1}$ for an invertible $2\times2$ matrix. Both sides are polynomial in the entries of $M,u,v,c$, and the invertible matrices are dense, so the identity holds for every $M$.

**The Schur complement.** The scalar

$$
s=c-vM^{-1}u
$$

is the **Schur complement** of the block $M$. When $M$ is invertible, $\det A=\det M\,s$; the matrix $A$ is invertible exactly when $s\neq0$, and then

$$
A^{-1}=
\begin{pmatrix}
M^{-1}+M^{-1}u s^{-1}vM^{-1} & -M^{-1}u s^{-1}\\
-s^{-1}vM^{-1} & s^{-1}
\end{pmatrix}.
$$

The formula is the $2+1$ block version of the Schur complement; it is used in *The Polar Decomposition of $M_3(\mathbb{C})$* and in the analysis of the singular set.

**The mass block.** The product of the two mixed corners is

$$
PMQ\cdot QMP=\{uv:u\in PMQ,\ v\in QMP\}\subseteq PMP.
$$

The element $uv$ is a rank-one $2\times2$ matrix; the set of such products is the **mass block**. It is not a linear subspace: the sum of two rank-one matrices can have rank two. The determinant formula

$$
\det A=c\det M-v\operatorname{adj}(M)u
$$

shows that $A$ is singular exactly when the scalar $c\det M$ equals the **mass term** $v\operatorname{adj}(M)u$. The mass term is the pairing of the mixed parts of $A$ through the adjugate of the compression.

**The mass can rescue a singular compression.** Take

$$
A=\begin{pmatrix}1&0&0\\0&0&1\\0&1&1\end{pmatrix},
\qquad
M=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad u=\begin{pmatrix}0\\1\end{pmatrix},\quad v=(0,1),\quad c=1.
$$

The compression $M$ is singular, $\det M=0$, and the adjugate is $\operatorname{adj}(M)=\begin{pmatrix}0&0\\0&1\end{pmatrix}$. The mass term is

$$
v\operatorname{adj}(M)u=(0,1)\begin{pmatrix}0&0\\0&1\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix}=1,
$$

so $\det A=0-1=-1\neq0$. The matrix $A$ is invertible although its compression to $\operatorname{im}P$ is singular: the mixed entries carry the invertibility through the kernel direction.

**The mass can cancel an invertible compression.** Take

$$
A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix},
\qquad
M=\begin{pmatrix}1&2\\4&5\end{pmatrix},\quad u=\begin{pmatrix}3\\6\end{pmatrix},\quad v=(7,8),\quad c=9.
$$

Here $\det M=-3$ and $M^{-1}=\frac13\begin{pmatrix}-5&2\\4&-1\end{pmatrix}$. The Schur complement is

$$
s=9-(7,8)\frac13\begin{pmatrix}-5&2\\4&-1\end{pmatrix}\begin{pmatrix}3\\6\end{pmatrix}
=9-\frac13\bigl((-35+32)\cdot3+(14-8)\cdot6\bigr)=9-\frac13(-9+36)=9-9=0.
$$

So $\det A=\det M\cdot0=0$, and indeed the rows of $A$ are linearly dependent. The compression is invertible, but the mass term cancels the determinant exactly.

**The massless case.** If $u=0$ or $v=0$, the matrix is block triangular,

$$
A=\begin{pmatrix}M&u\\0&c\end{pmatrix}\quad\text{or}\quad
A=\begin{pmatrix}M&0\\v&c\end{pmatrix},
$$

and $\det A=c\det M$. In the massless case $A$ is invertible exactly when $M$ is invertible and $c\neq0$: the two diagonal corners are independently invertible, and the mixed corners do not couple them.

**The trace.** For every $A$,

$$
\operatorname{tr}A=\operatorname{tr}M+c,
$$

because the mixed blocks $u$ and $v$ have no diagonal entries. The trace of the compression is $\operatorname{tr}M$; the scalar $c$ is the trace on the kernel line.

## The Rank-One Split and the Exchange

**The rank-one split is the same table with the two units exchanged.**

If $P$ is a rank-one idempotent and $Q=I-P$ has rank two, the coarse corners are

$$
PMP\cong\mathbb{C},\qquad PMQ\cong\mathbb{C}^{2},\qquad QMP\cong(\mathbb{C}^{2})^{*},\qquad QMQ\cong M_{2}(\mathbb{C}),
$$

of dimensions $1+2+2+4$. The block form is the same, with the $1\times1$ block first and the $2\times2$ block last; the determinant formula is the same with the roles of the scalar and the $2\times2$ block exchanged. The rank-two split $4+2+2+1$ is the rank-one split $1+2+2+4$ read from the other end.

**The exchange of the units.** The map $P\mapsto Q$ exchanges the two diagonal corners and the two mixed corners:

$$
PMP\leftrightarrow QMQ,\qquad PMQ\leftrightarrow QMP.
$$

It preserves the product table, because it is the same block decomposition with the two blocks relabelled. The determinant formula is not symmetric in the two blocks in the same way, because the determinant of a $3\times3$ matrix is not the product of the determinants of the two diagonal blocks when the mixed blocks are nonzero.

**The two splits of the menu.** The rank-one split $1+2+2+4$ is the split by a line, with a two-dimensional complement; the rank-two split $4+2+2+1$ is the split by a plane, with a one-dimensional complement. Both are coarse Peirce decompositions; the fine decomposition $1+1+1+1+1+1+1+1+1$ is the split by the three Lagrange idempotents. The three splits are related by refinement: the rank-two split is the coarse split by $P=P_{1}+P_{2}$, and it refines to the fine split by separating $P_{1}$ and $P_{2}$ inside $PMP$ and $P_{3}=Q$ in the complement.

**The mass block in the rank-one split.** In the rank-one split the mass block is the product of the two-dimensional mixed corners, which lands in the $2\times2$ corner; the determinant formula is the same with the $2\times2$ block in the lower-right position. The mass term is the scalar $v\operatorname{adj}(M)u$ in the rank-two split and the corresponding scalar in the rank-one split; the two are the same formula after the exchange of the blocks.

## Summary

For a rank-two idempotent $P$ and $Q=I-P$, the algebra splits into four coarse corners

$$
\boxed{\;M_{3}(\mathbb{C})=PMP\oplus PMQ\oplus QMP\oplus QMQ,\qquad 4+2+2+1,\;}
$$

with $PMP\cong M_{2}(\mathbb{C})$, $QMQ\cong\mathbb{C}$, and mixed corners of dimensions $2$ and $2$. In the adapted block form

$$
A=\begin{pmatrix}M&u\\v&c\end{pmatrix},
\qquad
\operatorname{tr}A=\operatorname{tr}M+c,
\qquad
\det A=c\det M-v\operatorname{adj}(M)u.
$$

The **mass block** $uv$ is the product of the two mixed corners; it can make $A$ invertible when $M$ is singular (the example with $\det A=-1$), and it can cancel an invertible compression (the example with $\det A=0$). The split is a vector-space split, not an algebra direct sum; the mixed corners are nonzero bimodules.

| Quantity | Rank-two split |
|---|---|
| Corners | $PMP\oplus PMQ\oplus QMP\oplus QMQ$ |
| Dimensions | $4+2+2+1$ |
| Diagonal corners | $M_{2}(\mathbb{C})$, $\mathbb{C}$ |
| Trace | $\operatorname{tr}M+c$ |
| Determinant | $c\det M-v\operatorname{adj}(M)u$ |
| Mass block | $uv\subseteq PMP$ |
| Rank-one split | $1+2+2+4$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$ | a rank-two idempotent |
| $Q=I-P$ | the complementary rank-one idempotent |
| $M$ | the $2\times2$ compression $PAP$ in a basis of $\operatorname{im}P$ |
| $u$ | the column $PAQ$ |
| $v$ | the row $QAP$ |
| $c$ | the scalar $QAQ$ |
| $s=c-vM^{-1}u$ | the Schur complement |
| $\operatorname{adj}(M)$ | the adjugate, $\operatorname{tr}(M)I_{2}-M$ |
| $uv$ | the mass block element |

## Further Reading

- [The $M_2$ Corner of $M_3(\mathbb{C})$](the-m2-corner-of-m3c.html), for the corner as a unital algebra and as a $*$-algebra.
- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the coarse split and the fine nine lines.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the trace and the determinant.
- [The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m3c.html), for the singular set and its geometry.
- [The Polar Decomposition of $M_3(\mathbb{C})$](the-polar-decomposition-of-m3c.html), for the Schur complement in the polar decomposition.
- [The Two-Parameter Gauge of $M_3(\mathbb{C})$](the-two-parameter-gauge-of-m3c.html), for the gauge of the mixed entries.
