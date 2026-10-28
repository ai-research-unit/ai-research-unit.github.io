# __The Rank-Two Split__

## Introduction

A rank-two idempotent $P$ cuts $M_5(\mathbb{C})$ into four corners of dimensions

$$
4+6+6+9=25:
$$

the algebra $PM_5P\cong M_2(\mathbb{C})$ of the two-dimensional image, the algebra $QM_5Q\cong M_3(\mathbb{C})$ of the three-dimensional kernel, and the two rectangular blocks $PM_5Q\cong\mathbb{C}^{2\times3}$ and $QM_5P\cong\mathbb{C}^{3\times2}$, of dimension $6$ each. The block $PM_5Q$ is the **mass block**; its dual $QM_5P$ is the conjugate mass block. The two together are the off-diagonal bimodule that couples the two corners.

This article develops the **split**: the corner dimensions, the corner isomorphisms, the mass block and its pairings, and the two-sided Peirce table. The group side of the same decomposition — the block stabiliser $P(GL_2\times GL_3)$, the two corner tori and the relative scale $1+2+1=4$ — is *The $M_2\oplus M_3$ Corner*. The two articles describe the same projection from the two sides, the algebra and the group; the present one is the algebra.

The article assumes the matrix algebra, the Peirce decomposition and the gauge. The corners are the $p=2$ case of the general rank-$p$ split; the $p=1$ case is the coarse split $1+4+4+16$ of *The Peirce Decomposition*, and the rank-two split is the next case of the recursion $M_{p+q}\supset M_p\oplus M_q$. The two diagonal corners are the previous categories: $M_2(\mathbb{C})$ is the biquaternion matrix model, and $M_3(\mathbb{C})$ is the three-dimensional matrix algebra.

## The Projection and the Block Form

### The Projection

**Definition.** A **rank-two projection** is an idempotent $P\in M_5(\mathbb{C})$ with $\operatorname{rank}P=2$. Its complement is $Q=I-P$, of rank $3$.

**Proposition.** There is a basis of $V=\mathbb{C}^5$ in which

$$
P=\operatorname{diag}(1,1,0,0,0),\qquad Q=\operatorname{diag}(0,0,1,1,1),
$$

and in this basis every $A$ has the block form

$$
A=\begin{pmatrix}A_{11}&A_{12}\\ A_{21}&A_{22}\end{pmatrix},
\qquad
A_{11}\in M_2,\quad A_{12}\in\mathbb{C}^{2\times3},\quad A_{21}\in\mathbb{C}^{3\times2},\quad A_{22}\in M_3 .
$$

**Proof.** Choose a basis $v_1,v_2$ of $\operatorname{im}P$ and $v_3,v_4,v_5$ of $\ker P=\operatorname{im}Q$; the matrix of $P$ is the displayed diagonal, and the matrix of an arbitrary element is cut into the four blocks by the two bases.

**Corollary.** The four blocks are the four coarse Peirce corners:

$$
PMP=\left\{\begin{pmatrix}A_{11}&0\\0&0\end{pmatrix}\right\},\quad
PMQ=\left\{\begin{pmatrix}0&A_{12}\\0&0\end{pmatrix}\right\},\quad
QMP=\left\{\begin{pmatrix}0&0\\A_{21}&0\end{pmatrix}\right\},\quad
QMQ=\left\{\begin{pmatrix}0&0\\0&A_{22}\end{pmatrix}\right\}.
$$

**Proof.** Multiply the block matrix by $P$ and $Q$ on the left and on the right; the projectors select the block rows and columns.

### The Block Product

**Proposition.** The product of two block matrices is

$$
\begin{pmatrix}A_{11}&A_{12}\\ A_{21}&A_{22}\end{pmatrix}
\begin{pmatrix}B_{11}&B_{12}\\ B_{21}&B_{22}\end{pmatrix}
=
\begin{pmatrix}
A_{11}B_{11}+A_{12}B_{21}&A_{11}B_{12}+A_{12}B_{22}\\
A_{21}B_{11}+A_{22}B_{21}&A_{21}B_{12}+A_{22}B_{22}
\end{pmatrix}.
$$

**Proof.** The ordinary matrix product, with the block sizes $2$ and $3$; every product of a $2\times3$ block with a $3\times2$ block is a $2\times2$ block, and every product of a $3\times2$ block with a $2\times3$ block is a $3\times3$ block.

**Corollary.** The diagonal blocks form the subalgebra $M_2\oplus M_3$ with unit $I$, and the off-diagonal blocks are a bimodule over it. The product of two off-diagonal blocks is diagonal:

$$
PMQ\cdot QMP\subseteq PMP,\qquad QMP\cdot PMQ\subseteq QMQ .
$$

**Proof.** The block formula: the $(1,1)$ block of the product of two off-diagonal matrices is $A_{12}B_{21}\in PMP$; the $(2,2)$ block is $A_{21}B_{12}\in QMQ$; the off-diagonal blocks of the product vanish.

## The Four Corners

### The Dimensions

**Theorem.** The four corners have complex dimensions

$$
\dim PMP=4,\qquad \dim PMQ=6,\qquad \dim QMP=6,\qquad \dim QMQ=9,
$$

and the sum is $4+6+6+9=25$.

**Proof.** In the block basis, $PMP$ is the set of $2\times2$ blocks, of dimension $4$; $PMQ$ is the set of $2\times3$ blocks, of dimension $6$; $QMP$ is the set of $3\times2$ blocks, of dimension $6$; $QMQ$ is the set of $3\times3$ blocks, of dimension $9$. The four blocks are in direct sum and exhaust the $5\times5$ matrices.

**Corollary.** The dimensions are $p^2$, $p(5-p)$, $(5-p)p$ and $(5-p)^2$ for $p=2$; for general $p$ they are

$$
p^2+p(5-p)+p(5-p)+(5-p)^2=25 .
$$

**Proof.** The block sizes are $p$ and $5-p$, and the number of entries in a block is the product of its two sizes.

### The Corner Isomorphisms

**Theorem.** The compressions give algebra isomorphisms

$$
PMP\cong M_2(\mathbb{C}),\qquad QMQ\cong M_3(\mathbb{C}),
$$

and vector-space isomorphisms

$$
PMQ\cong M_{2,3}(\mathbb{C})\cong\mathbb{C}^{2\times3},\qquad
QMP\cong M_{3,2}(\mathbb{C})\cong\mathbb{C}^{3\times2}.
$$

**Proof.** In the block basis, $PMP$ is the set of matrices $\operatorname{diag}(A_{11},0)$ with $A_{11}\in M_2$; the map $A_{11}\mapsto\operatorname{diag}(A_{11},0)$ is an algebra isomorphism onto the corner. The second corner is the same with $A_{22}\in M_3$. The off-diagonal corners are the rectangular matrices $A_{12}$ and $A_{21}$.

**Corollary.** The corner $PMP$ has unit $P$, and the corner $QMQ$ has unit $Q$; neither unit is the unit of $M_5$ unless the complementary rank is zero. The isomorphism $PMP\cong M_2$ is not canonical: it depends on the choice of a basis of $\operatorname{im}P$.

**Proof.** $P$ acts as the identity on $\operatorname{im}P$ and as zero on $\ker P$, so it is the unit of the compression; the basis dependence is the conjugation by the change of basis inside $\operatorname{im}P$.

### The Mass Block

**Definition.** The **mass block** is the off-diagonal corner

$$
\mathcal{M}=PM_5Q\cong\mathbb{C}^{2\times3},
$$

of dimension $6$. Its **conjugate** is $\mathcal{M}^*=QM_5P\cong\mathbb{C}^{3\times2}$, also of dimension $6$.

**Proposition.** The mass block is a bimodule over $M_2\oplus M_3$:

$$
M_2\times\mathcal{M}\to\mathcal{M},\quad (A,X)\mapsto AX;\qquad
\mathcal{M}\times M_3\to\mathcal{M},\quad (X,B)\mapsto XB;
$$

and the conjugate block is the dual bimodule. The pairings

$$
\mathcal{M}\times\mathcal{M}^*\to M_2,\quad (X,Y)\mapsto XY;\qquad
\mathcal{M}^*\times\mathcal{M}\to M_3,\quad (Y,X)\mapsto YX
$$

span the diagonal corners: the linear span of the products $XY$ is $M_2$, and the linear span of the products $YX$ is $M_3$.

**Proof.** The block product gives the actions; $XY$ is a $2\times2$ matrix and $YX$ a $3\times3$ matrix. The product map $M_{2,3}\times M_{3,2}\to M_2$ is surjective because for every $A\in M_2$ one may take $X=(A,0)$ and $Y=\binom{I_2}{0}$. The products $YX$ span $M_3$: every matrix is a sum of rank-one matrices $uv^{\mathsf T}$, and each is $YX$ with $Y=(u,0)$ and $X=\binom{v^{\mathsf T}}{0}$.

**Remark.** **The mass block is the part of the algebra that couples the two corners.** It is not an ideal: the product of two mass-block elements is diagonal, and the product of a mass-block element with a diagonal element stays in the mass block. It is a bimodule, and its dimension $6$ is the product of the two block sizes. The word *mass* is the name of the off-diagonal block in the block decomposition; the conjugate block is the dual, and the two pairings are the two ways of contracting the indices.

**Corollary.** The algebra is **$\mathbb{Z}/2$-graded** with even part $M_2\oplus M_3$ and odd part $\mathcal{M}\oplus\mathcal{M}^*$. The odd part is a bimodule, not an ideal with square zero: the product of two odd elements is a nonzero even element. The algebra is not the direct product $M_2\times M_3$.

**Proof.** The block multiplication gives the graded product; the square of the odd part lies in the even part, and it is nonzero because $XY$ and $YX$ are nonzero for suitable $X,Y$. The mixed blocks are nonzero, so the algebra is larger than the direct product.

## The Two-Sided Peirce Table

### The Table

**Theorem.** The products of the four corners are given by the following table, the row being the left factor and the column the right factor.

| left $\backslash$ right | $PMP$ | $PMQ$ | $QMP$ | $QMQ$ |
|---|---|---|---|---|
| $PMP$ | $PMP$ | $PMQ$ | $0$ | $0$ |
| $PMQ$ | $0$ | $0$ | $PMP$ | $PMQ$ |
| $QMP$ | $QMP$ | $QMQ$ | $0$ | $QMP$ |
| $QMQ$ | $0$ | $0$ | $QMP$ | $QMQ$ |

**Proof.** The block formula of §*The Projection and the Block Form*: the nonvanishing products are those with no factor $PQ$ or $QP$ in the middle. The four diagonal products are the subalgebra products; the four products $PMP\cdot PMQ$, $PMQ\cdot QMQ$, $QMQ\cdot QMP$, $QMP\cdot PMP$ are the bimodule actions; the two products $PMQ\cdot QMP$ and $QMP\cdot PMQ$ are the pairings into the diagonal corners. All other products vanish.

**Corollary.** The table has the same pattern as the rank-one table of *The Peirce Decomposition*, with the scalar corner replaced by $M_2$ and the $M_4$ corner replaced by $M_3$. The pattern depends only on the **two block indices**, not on the sizes; the sizes enter only in the dimensions.

**Proof.** The pattern is the block-index multiplication: $(i,j)(j,k)\subseteq(i,k)$ and zero otherwise, for $i,j,k\in\{1,2\}$. The sizes are the dimensions of the blocks.

### The Dimensions of the Products

**Proposition.** The pairings span the diagonal corners of the stated dimensions:

$$
\operatorname{span}(PMQ\cdot QMP)=PMP,\qquad
\operatorname{span}(QMP\cdot PMQ)=QMQ .
$$

The bimodule actions are surjective:

$$
PMP\cdot PMQ=PMQ,\quad PMQ\cdot QMQ=PMQ,\quad QMQ\cdot QMP=QMP,\quad QMP\cdot PMP=QMP .
$$

**Proof.** The product of $M_{2,3}$ with $M_{3,2}$ spans $M_2$; the product of $M_{3,2}$ with $M_{2,3}$ spans $M_3$; the actions are the ordinary matrix products and are surjective because the identity matrices act as identities.

**Corollary.** The mass block $PMQ$ is a **simple bimodule** over $M_2\oplus M_3$: it is the tensor product of the standard $M_2$-module and the dual standard $M_3$-module, and it has no nontrivial sub-bimodule. As a left $M_2$-module it is three copies of the standard module $\mathbb{C}^2$; as a right $M_3$-module it is two copies of the dual standard module $(\mathbb{C}^3)^*$. The dual bimodule is $QMP$.

**Proof.** The mass block is $M_{2,3}\cong\mathbb{C}^2\otimes(\mathbb{C}^3)^*$. The left action of $M_2$ is on the factor $\mathbb{C}^2$, which is simple; the right action of $M_3$ is on the factor $(\mathbb{C}^3)^*$, which is simple. The tensor product of a simple left module and a simple right module is a simple bimodule. The identification of the three columns with $\mathbb{C}^2$ and the two rows with $(\mathbb{C}^3)^*$ gives the stated multiplicities.

### The Graded Structure

**Definition.** The **block parity** of a corner is even for $PMP$ and $QMQ$, odd for $PMQ$ and $QMP$.

**Proposition.** The parity gives a $\mathbb{Z}/2$-grading

$$
M_5=M_{\mathrm{even}}\oplus M_{\mathrm{odd}},\qquad
M_{\mathrm{even}}=M_2\oplus M_3,\quad M_{\mathrm{odd}}=\mathcal{M}\oplus\mathcal{M}^*,
$$

with $M_{\mathrm{even}}M_{\mathrm{even}}\subseteq M_{\mathrm{even}}$, $M_{\mathrm{even}}M_{\mathrm{odd}}\subseteq M_{\mathrm{odd}}$, and $M_{\mathrm{odd}}M_{\mathrm{odd}}\subseteq M_{\mathrm{even}}$.

**Proof.** The block parity is the parity of the number of off-diagonal blocks; the block product adds the parities.

**Remark.** **The $\mathbb{Z}/2$-grading is the coarsest grading of the split; the $\mathbb{Z}/5$-grading of the root is a different structure.** The root grading has five components of dimension $5$; the block grading has two components of dimensions $13$ and $12$. They are not the same, and neither refines the other in general. The Peirce decomposition refines both when the projection is spectral.

## The Corners as Previous Categories

### The $M_2$ Corner

The corner $PMP\cong M_2(\mathbb{C})$ is the algebra of the biquaternion model. The biquaternion algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, and the whole biquaternion theory — the idempotents, the Peirce lines, the spinor, the matrix model — is read inside this corner, with the unit $P$ and the trace compressed by $P$.

**Proposition.** The compression $A\mapsto PAP$ is a unital algebra homomorphism from the corner $M_2$ into $M_5$, with image $PMP$; it is not unital as a map into $M_5$, because $P\ne I$.

**Proof.** $P(AB)P=(PAP)(PBP)$ and $PIP=P$; the unit of the image is $P$.

**Remark.** **The corner is a previous category, not a quotient of the present one.** The biquaternion structures live in $M_2$; the $M_5$ root, the $M_5$ Peirce decomposition and the $M_5$ carrier are different structures on the larger algebra. The corner embedding is the way the smaller category sits inside the larger one.

### The $M_3$ Corner

The corner $QMQ\cong M_3(\mathbb{C})$ is the three-dimensional matrix algebra. Its own root of order $3$, its idempotents and its Peirce decomposition are the $n=3$ analogues; the corner carries them with the unit $Q$. The block embedding $B\mapsto\operatorname{diag}(0,B)$ is unital into the corner and not into $M_5$.

**Proposition.** The two corners commute and intersect in zero; their sum $M_2\oplus M_3$ has dimension $13$, and the complement is the off-diagonal bimodule of dimension $12$.

**Proof.** The block matrices $\operatorname{diag}(A,0)$ and $\operatorname{diag}(0,B)$ commute and their product is zero; the dimensions are $4+9=13$ and $25-13=12$.

### The Bimodule

The off-diagonal bimodule is the **mass** sector of the split. Its two blocks are dual, and the pairings with the diagonal corners are the two contractions. The bimodule is simple as a bimodule; the algebra is $\mathbb{Z}/2$-graded with this odd part. This is the algebraic skeleton that the mass terminology names: the two diagonal corners are the two sectors, and the mass block is the coupling.

**Remark.** The split $4+6+6+9$ is the $p=2$ case of the general $p^2+p(5-p)+p(5-p)+(5-p)^2$. The $p=1$ case is $1+4+4+16$; the $p=3$ case is $9+6+6+4$, the same split with the corners exchanged; the $p=4$ case is $16+4+4+1$. The symmetric cases $p=1$ and $p=4$, and $p=2$ and $p=3$, are exchanged by $P\leftrightarrow Q$.

## The Split from the Root

### The Spectral Partition

Let $H$ be a root with spectral projectors $P_0,\dots,P_4$, and let

$$
P=P_0+P_1,\qquad Q=P_2+P_3+P_4 .
$$

Then $P$ is a rank-two projection, $Q$ its complement, and the block split is the partition of the five spectral lines into the first two and the last three.

**Proposition.** The corners are the sums of the Peirce lines with indices in the two blocks:

$$
PMP=\bigoplus_{k,l\in\{0,1\}}A_{kl},\qquad
PMQ=\bigoplus_{k\in\{0,1\},\,l\in\{2,3,4\}}A_{kl},
$$

$$
QMP=\bigoplus_{k\in\{2,3,4\},\,l\in\{0,1\}}A_{kl},\qquad
QMQ=\bigoplus_{k,l\in\{2,3,4\}}A_{kl}.
$$

The dimensions are $4$, $6$, $6$ and $9$, the numbers of pairs in the four index sets.

**Proof.** The Peirce line $A_{kl}$ lies in the corner selected by the block membership of $k$ and $l$; the direct sum over the lines is the corner. The counts are $2\cdot2=4$, $2\cdot3=6$, $3\cdot2=6$, $3\cdot3=9$.

**Corollary.** The rank-two split refines the $\mathbb{Z}/5$-grading only partially: a line $A_{kl}$ lies in the grade $k-l$ and in the block corner selected by the two indices. The grade does not determine the corner, and the corner does not determine the grade.

**Proof.** The grade is the difference of the indices; two pairs with the same difference can lie in different corners.

### The Refinement of the Split

The rank-one split of *The Peirce Decomposition* is the partition $\{0\},\{1,2,3,4\}$; the rank-two split is the partition $\{0,1\},\{2,3,4\}$; the rank-three split is $\{0,1,2\},\{3,4\}$; the rank-four split is $\{0,1,2,3\},\{4\}$. Each is a coarsening of the fine Peirce decomposition by a partition of the index set. The dimensions of the corners are the products of the sizes of the two parts.

**Proposition.** For a partition $S\sqcup T=\{0,\dots,4\}$ with $|S|=p$, the corner dimensions are

$$
p^2,\quad p(5-p),\quad (5-p)p,\quad (5-p)^2 .
$$

**Proof.** The corner $PMP$ is the sum of the lines with both indices in $S$, of which there are $p^2$; the mixed corners have $p(5-p)$ each; the corner $QMQ$ has $(5-p)^2$.

**Remark.** **The rank-two split is the case $p=2$ of the partition, and the mass block is the mixed corner of size $2\cdot3=6$.** The split is not a new algebra; it is the same algebra read through a partition of the spectral indices. The group side, with the relative scale, is *The $M_2\oplus M_3$ Corner*.

## Summary

A rank-two projection $P$ and its complement $Q=I-P$ split the algebra into four corners of dimensions

$$
4+6+6+9=25,
$$

with

$$
PMP\cong M_2(\mathbb{C}),\qquad QMQ\cong M_3(\mathbb{C}),\qquad PMQ\cong\mathbb{C}^{2\times3},\qquad QMP\cong\mathbb{C}^{3\times2}.
$$

The mass block $PMQ$ has dimension $6$; its dual $QMP$ has dimension $6$; the pairings $PMQ\times QMP\to PMP$ and $QMP\times PMQ\to QMQ$ span the diagonal corners. The algebra is $\mathbb{Z}/2$-graded with even part $M_2\oplus M_3$ and odd part the off-diagonal bimodule.

$$
\boxed{\ M_5\supset M_2\oplus M_3,\qquad 4+6+6+9=25,\qquad \text{mass block }6,\text{ dual }6.\ }
$$

The two-sided Peirce table has the block pattern $(i,j)(j,k)\subseteq(i,k)$, with the sizes $2$ and $3$. The two diagonal corners are the previous categories: $M_2$ is the biquaternion matrix model and $M_3$ is the three-dimensional matrix algebra. The split from the root is the partition $\{0,1\},\{2,3,4\}$ of the spectral lines; the corner dimensions are the products of the block sizes.

| Corner | Isomorphism | Dimension |
|---|---|---|
| $PMP$ | $M_2(\mathbb{C})$ | $4$ |
| $PMQ$ (mass) | $\mathbb{C}^{2\times3}$ | $6$ |
| $QMP$ (dual) | $\mathbb{C}^{3\times2}$ | $6$ |
| $QMQ$ | $M_3(\mathbb{C})$ | $9$ |
| Total | | $25$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$ | A rank-two projection |
| $Q=I-P$ | The complementary rank-three projection |
| $PMP$, $PMQ$, $QMP$, $QMQ$ | The four corners |
| $\mathcal{M}=PMQ$ | The mass block, dimension $6$ |
| $\mathcal{M}^*=QMP$ | The conjugate mass block, dimension $6$ |
| $M_{2,3}$, $M_{3,2}$ | The rectangular matrix spaces |
| $M_{\mathrm{even}}=M_2\oplus M_3$ | The even part of the $\mathbb{Z}/2$-grading |
| $M_{\mathrm{odd}}=\mathcal{M}\oplus\mathcal{M}^*$ | The odd part |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce corners, the corner isomorphisms and the graded algebra of a block decomposition.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the block multiplication, the rectangular blocks and the rank of a product.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the corner decomposition in an algebra with involution and the behaviour of the mass block.
- [The Matrix Algebra $M_5(\mathbb{C})$](the-matrix-algebra-m5c.html), for the algebra and its dimensions.
- [The Peirce Decomposition](the-peirce-decomposition-of-m5c.html), for the coarse split $1+4+4+16$ and the fine Peirce lines.
- [The $M_2\oplus M_3$ Corner](the-m2-m3-corner-of-m5c.html), for the block stabiliser, the two corner tori and the relative scale $1+2+1=4$.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m5c.html), for the gauge parameters regrouped by the block structure.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m5c.html), for the modules of the corners and the bimodule.
- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the biquaternion algebra in the $M_2$ corner.
