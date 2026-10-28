# __The $M_2\oplus M_3$ Corner__

## Introduction

A rank-two idempotent $P$ and its complement $Q=I-P$ cut $M_5(\mathbb{C})$ into four corners, and the two diagonal corners are full matrix algebras:

$$
M_5(\mathbb{C})\supset PM_5P\oplus QM_5Q\cong M_2(\mathbb{C})\oplus M_3(\mathbb{C}).
$$

The inclusion is the **recursion** $5=2+3$: the algebra of the five-dimensional space contains the algebra of a two-dimensional space and the algebra of a three-dimensional space, acting on the two summands of a direct-sum decomposition. The off-diagonal corners $PM_5Q$ and $QM_5P$ are the bimodules that couple the two summands; together with the diagonal corners they rebuild the whole algebra.

The subgroup of $PGL_5$ that preserves the decomposition is $P(GL_2\times GL_3)$, and its maximal torus has dimension

$$
1+2+1=4:
$$

one parameter for the $M_2$ corner, two for the $M_3$ corner, and one for the **relative scale** between the two corners. The relative scale is the direction that acts on the two summands with opposite weights, $\operatorname{diag}(\mu I_2,I_3)$ modulo scalars; it is the part of the gauge that is invisible to each corner separately. The four parameters are the same torus as the gauge of the frame, read through the block structure $2+3$.

The article assumes the matrix algebra of *The Matrix Algebra $M_5(\mathbb{C})$*, the Peirce decomposition of *The Peirce Decomposition*, and the gauge of *The Frame, the Simple Nilpotents and the Gauge*. The corner dimensions and the two-sided Peirce table are developed in *The Rank-Two Split*; the present article is the **recursion and the group**: the block embedding, the subalgebra $M_2\oplus M_3$, the two corner tori and the relative scale.

## The Rank-Two Projection

### The Idempotent

**Definition.** A **rank-two projection** is an idempotent $P\in M_5(\mathbb{C})$ with $\operatorname{rank}P=2$. Its **complement** is $Q=I-P$, of rank $3$.

**Proposition.** The ranks add: $\operatorname{rank}P+\operatorname{rank}Q=5$. The images and kernels are in direct sum,

$$
V=\operatorname{im}P\oplus\ker P=\operatorname{im}P\oplus\operatorname{im}Q,
\qquad
\ker P=\operatorname{im}Q,\quad \ker Q=\operatorname{im}P,
$$

and $P$ is the projection onto $\operatorname{im}P$ along $\operatorname{im}Q$.

**Proof.** An idempotent satisfies $V=\operatorname{im}P\oplus\ker P$: every $v$ is $Pv+(v-Pv)$, the first term in the image and the second in the kernel, and the intersection is zero because $Pv=0$ and $v=Pw$ imply $v=P^2w=Pw=0$. Since $Q=I-P$, $\operatorname{im}Q=\ker P$ and $\ker Q=\operatorname{im}P$. The rank is the dimension of the image.

**Corollary.** There is a basis of $V$ in which

$$
P=\operatorname{diag}(1,1,0,0,0),\qquad Q=\operatorname{diag}(0,0,1,1,1).
$$

**Proof.** Choose a basis of $\operatorname{im}P$ followed by a basis of $\operatorname{im}Q$; in this basis $P$ acts as the identity on the first two vectors and as zero on the last three.

### The Block Form

In the basis of the corollary, every $A$ has the block form

$$
A=\begin{pmatrix}A_{11}&A_{12}\\ A_{21}&A_{22}\end{pmatrix},
\qquad
A_{11}\in M_2(\mathbb{C}),\quad A_{12}\in\mathbb{C}^{2\times3},\quad A_{21}\in\mathbb{C}^{3\times2},\quad A_{22}\in M_3(\mathbb{C}).
$$

The four blocks are exactly the four coarse Peirce corners:

$$
PAP=\begin{pmatrix}A_{11}&0\\0&0\end{pmatrix},\quad
PAQ=\begin{pmatrix}0&A_{12}\\0&0\end{pmatrix},\quad
QAP=\begin{pmatrix}0&0\\A_{21}&0\end{pmatrix},\quad
QAQ=\begin{pmatrix}0&0\\0&A_{22}\end{pmatrix}.
$$

**Proposition.** The block multiplication is

$$
\begin{pmatrix}A_{11}&A_{12}\\ A_{21}&A_{22}\end{pmatrix}
\begin{pmatrix}B_{11}&B_{12}\\ B_{21}&B_{22}\end{pmatrix}
=
\begin{pmatrix}
A_{11}B_{11}+A_{12}B_{21}&A_{11}B_{12}+A_{12}B_{22}\\
A_{21}B_{11}+A_{22}B_{21}&A_{21}B_{12}+A_{22}B_{22}
\end{pmatrix}.
$$

**Proof.** The ordinary matrix product, written block by block; the sizes are $2+3$, so every product is defined.

**Corollary.** The diagonal blocks form the subalgebra

$$
PM_5P\oplus QM_5Q\cong M_2(\mathbb{C})\oplus M_3(\mathbb{C}),
$$

with unit $P+Q=I$. The off-diagonal blocks are not a subalgebra: their products land in the diagonal blocks.

**Proof.** The product of two block-diagonal matrices is block diagonal with the blocks multiplied; the unit is $\operatorname{diag}(I_2,I_3)=I$. The product of two off-diagonal matrices is block diagonal, as the block formula shows.

## The Subalgebra $M_2\oplus M_3$

### The Embedding

**Definition.** The **block embedding** of $M_2(\mathbb{C})\oplus M_3(\mathbb{C})$ into $M_5(\mathbb{C})$ is

$$
\iota(A,B)=\begin{pmatrix}A&0\\0&B\end{pmatrix}.
$$

**Proposition.** The map $\iota$ is an injective unital algebra homomorphism, and its image is $PM_5P\oplus QM_5Q$. The projections onto the two factors are the compressions

$$
\iota^{-1}\bigl(\iota(A,B)\bigr)=(PAP,QBQ).
$$

**Proof.** The block product of two diagonal block matrices is the diagonal block matrix of the products, and the unit is $I$. The image is exactly the set of block-diagonal matrices, which is $PM_5P\oplus QM_5Q$. The compression of $\iota(A,B)$ to the first block is $A$ and to the second is $B$.

**Remark.** The embedding is unital in $M_5$, but the **corner** $PM_5P$ is not unital in $M_5$: its unit is $P$, not $I$. The map $A\mapsto\iota(A,0)$ is an algebra homomorphism onto the corner with unit $P$, and it is unital as a map into the corner. The distinction matters when the corner is used as an algebra in its own right, as in the biquaternion model.

### The Two Corners

**Proposition.** The first corner $PM_5P$ is isomorphic to $M_2(\mathbb{C})$ and the second $QM_5Q$ to $M_3(\mathbb{C})$. The isomorphisms are the compressions $A\mapsto PAP$ and $A\mapsto QAQ$, read in the block basis; they are not canonical, because they depend on the choice of bases inside $\operatorname{im}P$ and $\operatorname{im}Q$.

**Proof.** In the block basis, $PAP=\operatorname{diag}(A_{11},0)$ and $QAQ=\operatorname{diag}(0,A_{22})$; the maps $A_{11}\mapsto\operatorname{diag}(A_{11},0)$ and $A_{22}\mapsto\operatorname{diag}(0,A_{22})$ are algebra isomorphisms onto the corners. A change of basis inside the image changes $A_{11}$ by conjugation.

**Corollary.** The algebra $M_5(\mathbb{C})$ contains a copy of $M_2(\mathbb{C})$ and a copy of $M_3(\mathbb{C})$, with commuting images, and the two copies together generate $M_2\oplus M_3$ but not $M_5$. The off-diagonal blocks are needed to generate the whole algebra.

**Proof.** The images commute because the blocks are diagonal; their sum is $M_2\oplus M_3$. A matrix with a nonzero off-diagonal block is not in the sum, so the sum is proper; the off-diagonal blocks together with the diagonal generate $M_5$ because every block matrix is a sum of its four blocks.

### The Off-Diagonal Bimodule

**Definition.** The **off-diagonal block** is

$$
\mathcal{M}=PM_5Q\oplus QM_5P,
$$

the sum of the row block $PM_5Q\cong\mathbb{C}^{2\times3}$ and the column block $QM_5P\cong\mathbb{C}^{3\times2}$.

**Proposition.** The off-diagonal block is a bimodule over $M_2\oplus M_3$: the left and right actions

$$
(A,B)\cdot(X,Y)=(AX,YB),\qquad (X,Y)\cdot(A,B)=(XA,BY)
$$

are defined for $X\in\mathbb{C}^{2\times3}$, $Y\in\mathbb{C}^{3\times2}$, and they commute. The algebra $M_5$ is the **$\mathbb{Z}/2$-graded algebra** with even part $M_2\oplus M_3$ and odd part $\mathcal{M}$:

$$
M_5=(M_2\oplus M_3)\oplus\mathcal{M},
\qquad
(A,B)(A',B')=(AA',BB'),\qquad
(A,B)(X,Y)=(AX,YB),
$$

with $\mathcal{M}^2\subseteq M_2\oplus M_3$. The odd part is a bimodule, not an ideal with square zero: the product of two odd elements is a nonzero even element.

**Proof.** The block multiplication gives the actions; the product of two off-diagonal blocks is diagonal, $XY\in M_2$ and $YX\in M_3$. The associativity is the associativity of the block product.

**Corollary.** The algebra is **graded by $\mathbb{Z}/2$** with even part $M_2\oplus M_3$ and odd part $\mathcal{M}$. The even part is a subalgebra; the odd part is a bimodule; the product of two odd elements lands in the even part. The algebra is not the direct product $M_2\times M_3$: the mixed blocks are nonzero.

**Proof.** The block parity is the parity of the number of off-diagonal blocks; the product rule preserves it. The mixed blocks $PMQ$ and $QMP$ are nonzero, so the algebra is larger than the direct product.

## The Gauge $1+2+1=4$

### The Stabiliser of the Decomposition

**Definition.** The **block-diagonal subgroup** of $GL_5(\mathbb{C})$ preserving the decomposition $V=\operatorname{im}P\oplus\operatorname{im}Q$ is

$$
GL_2(\mathbb{C})\times GL_3(\mathbb{C})=\left\{\begin{pmatrix}g_2&0\\0&g_3\end{pmatrix}:g_2\in GL_2,\ g_3\in GL_3\right\}.
$$

Its image in $PGL_5$ is $P(GL_2\times GL_3)$.

**Proposition.** The stabiliser of $P$ in $PGL_5$ is $P(GL_2\times GL_3)$, of complex dimension $4+9-1=12$. Its maximal torus has dimension $2+3-1=4$.

**Proof.** $gPg^{-1}=P$ if and only if $g$ preserves $\operatorname{im}P$ and $\ker P$, which is the block-diagonal condition. The dimensions are $\dim GL_2=4$, $\dim GL_3=9$, minus the scalars $1$; the maximal torus is the diagonal torus of $GL_2\times GL_3$, of dimension $2+3=5$, minus the scalars, $4$.

### The Three Directions

**Theorem.** The maximal torus of $P(GL_2\times GL_3)$ decomposes as

$$
T(PGL_2)\oplus T(PGL_3)\oplus\mathbb{C}^\times_{\mathrm{rel}},
\qquad
1+2+1=4 .
$$

The first factor is the diagonal torus of the $M_2$ corner, of dimension $1$; the second is the diagonal torus of the $M_3$ corner, of dimension $2$; the third is the **relative scale**

$$
\mu\longmapsto \operatorname{diag}(\mu I_2,I_3)\ \bmod\ \mathbb{C}^\times I,
\qquad \mu\in\mathbb{C}^\times,
$$

of dimension $1$.

**Proof.** A diagonal element of $GL_2\times GL_3$ is $\operatorname{diag}(t_1,t_2,s_1,s_2,s_3)$; modulo the common scalar, the independent ratios are $t_1/t_2$ (one), $s_1/s_3$ and $s_2/s_3$ (two), and the relative ratio $t_1/s_1$ (one). The first three are the corner tori, and the last is the relative scale. The four ratios are independent, and their product is not constrained (they are four coordinates on a four-dimensional torus).

**Corollary.** The relative scale acts on the blocks by

$$
\operatorname{diag}(\mu I_2,I_3)\begin{pmatrix}A_{11}&A_{12}\\ A_{21}&A_{22}\end{pmatrix}\operatorname{diag}(\mu^{-1}I_2,I_3)
=
\begin{pmatrix}A_{11}&\mu A_{12}\\ \mu^{-1}A_{21}&A_{22}\end{pmatrix}.
$$

It fixes both diagonal corners and rescales the two off-diagonal blocks reciprocally.

**Proof.** Conjugate the block matrix by the block-diagonal matrix; the diagonal blocks commute with the scalars, and the off-diagonal blocks acquire $\mu$ or $\mu^{-1}$.

**Remark.** **The relative scale is the part of the gauge that the two corners do not see.** The corner tori act inside $PM_5P$ and $QM_5Q$; the relative scale acts only on the off-diagonal blocks. In the frame of *The Frame, the Simple Nilpotents and the Gauge*, with the spectral indices $1,\dots,5$ split as $\{1,2\}|\{3,4,5\}$, the four parameters $\lambda_k=t_k/t_{k+1}$ are regrouped as

$$
\underbrace{\lambda_1}_{T(PGL_2)}\qquad
\underbrace{\lambda_2}_{\text{relative scale}}\qquad
\underbrace{\lambda_3,\lambda_4}_{T(PGL_3)} .
$$

The parameters $\lambda_1$ and $\lambda_3,\lambda_4$ act inside the two corners; $\lambda_2=t_2/t_3$ is the relative scale between them. The count $1+2+1=4$ is the invariant statement; the assignment of the four $\lambda_k$ depends on where the cut between the blocks is placed.

### The Gauge and the Root

**Proposition.** If $P=P_0+P_1$ is the sum of two spectral projectors of a root $H$, then the four-dimensional gauge torus of the root is the maximal torus of $P(GL_2\times GL_3)$. The gauge $1+2+1=4$ is the root gauge read through the block structure $2+3$.

**Proof.** The spectral frame diagonalises $H$; the diagonal torus $T$ of the frame consists of the matrices $\operatorname{diag}(t_0,t_1,t_2,t_3,t_4)$ modulo scalars. It preserves the decomposition $\operatorname{span}(e_0,e_1)\oplus\operatorname{span}(e_2,e_3,e_4)$ because it preserves each line; hence $T\subseteq P(GL_2\times GL_3)$. Both tori have dimension $4$, so they are equal.

**Corollary.** The rank-two projection $P=P_0+P_1$ has a larger stabiliser than the root: $P(GL_2\times GL_3)$ has dimension $12$, while the root's stabiliser $T$ has dimension $4$. The quotient has dimension $8$; it consists of the non-toral directions of the two corner groups, which move the vectors inside the two blocks without moving the root.

**Proof.** The stabiliser of $P$ is the block-diagonal group of dimension $12$; the stabiliser of $H$ is its maximal torus of dimension $4$. The quotient has dimension $8$, and the torus directions are exactly the four coordinates of $T$; the remaining directions are the unipotent and traceless-diagonal directions of the two corner groups.

## The Recursion and the Previous Categories

### The Recursion $5=2+3$

The decomposition is the first step of the recursion

$$
M_{p+q}(\mathbb{C})\supset M_p(\mathbb{C})\oplus M_q(\mathbb{C}),
\qquad p+q=5,
$$

for every rank-$p$ projection $P$. For $p=2$, $q=3$, the corner is $M_2\oplus M_3$; for $p=1$, $q=4$, it is $\mathbb{C}\oplus M_4$, the case of *The Peirce Decomposition*; for $p=3$, $q=2$, it is $M_3\oplus M_2$, the same decomposition with the factors exchanged. The recursion can be iterated, $5=2+3=2+(1+2)=\cdots$, and it terminates in the scalar corners.

**Proposition.** For every $p$, the diagonal corners of a rank-$p$ projection are $PMP\cong M_p$ and $QMQ\cong M_{5-p}$; the off-diagonal blocks are $\mathbb{C}^{p\times(5-p)}$ and $\mathbb{C}^{(5-p)\times p}$; the dimensions are

$$
p^2+p(5-p)+p(5-p)+(5-p)^2=25 .
$$

**Proof.** Choose bases of the image and the kernel; the compressions are the full matrix algebras of the two summands, and the off-diagonal blocks are the rectangular matrices.

### The $M_2$ Corner

The corner $PM_5P\cong M_2(\mathbb{C})$ is the algebra of the biquaternion model: $\mathbb{B}\cong M_2(\mathbb{C})$. The idempotents, the Peirce decomposition and the spinor of $\mathbb{B}$ are read inside this corner, with the unit $P$ and the trace rescaled by $P$. The embedding $A\mapsto\operatorname{diag}(A,0)$ carries the biquaternion matrices into $M_5$; the corner is not unital in $M_5$, and the unit of the corner is $P$.

**Proposition.** The compression $A\mapsto PAP$ is a unital algebra homomorphism from $M_2(\mathbb{C})$ onto the corner, and the trace of the corner is $\operatorname{tr}_{PM_5P}(PAP)=\operatorname{tr}(PAP)=\operatorname{tr}(A)$ for $A\in M_2$ embedded in the first block.

**Proof.** The compression is multiplicative on the block, and the trace of $\operatorname{diag}(A,0)$ is the trace of $A$.

**Remark.** **The corner is the biquaternion algebra, but the word spinor is not transferred to $M_5$.** The $M_2$ corner has a two-dimensional module, the spinor of the biquaternion model; the whole algebra $M_5$ has the five-dimensional carrier, of spin $2$. The corner is a subalgebra, and its module is not a module of $M_5$ unless it is induced. The distinction is the subject of *The Modules and the Minimal Left Ideals*.

### The $M_3$ Corner

The corner $QM_5Q\cong M_3(\mathbb{C})$ is the algebra of the three-dimensional space; its own root, idempotents and Peirce decomposition are the $n=3$ analogues of the present category. The block embedding carries the $M_3$ structures into the last three spectral lines when $P=P_0+P_1$. The relative scale couples the $M_2$ and $M_3$ corners through the off-diagonal blocks.

**Proposition.** The two corners commute, and their tensor product is not the whole algebra: $M_2\oplus M_3$ has dimension $13$, while $M_5$ has dimension $25$; the missing $12$ dimensions are the two off-diagonal blocks of dimension $6$ each.

**Proof.** $\dim M_2=4$, $\dim M_3=9$, sum $13$; $\dim M_5=25$; the difference is $12=6+6$, the dimensions of $\mathbb{C}^{2\times3}$ and $\mathbb{C}^{3\times2}$.

## Summary

A rank-two projection $P$ and its complement $Q=I-P$ give the recursion

$$
M_5(\mathbb{C})\supset PM_5P\oplus QM_5Q\cong M_2(\mathbb{C})\oplus M_3(\mathbb{C}),
$$

with the off-diagonal bimodule $\mathcal{M}=PM_5Q\oplus QM_5P$ of dimension $12$. The algebra is $\mathbb{Z}/2$-graded with even part $M_2\oplus M_3$ and odd part $\mathcal{M}$.

The stabiliser of the decomposition in $PGL_5$ is $P(GL_2\times GL_3)$, of dimension $12$; its maximal torus has dimension

$$
1+2+1=4,
$$

the $M_2$ corner torus, the $M_3$ corner torus and the relative scale $\operatorname{diag}(\mu I_2,I_3)$. The relative scale fixes both diagonal corners and rescales the off-diagonal blocks reciprocally. The four parameters are the gauge torus of the frame, read through the block structure $2+3$.

$$
\boxed{\ M_5\supset M_2\oplus M_3,\qquad \text{gauge }1+2+1=4,\qquad \text{off-diagonal }6+6=12.\ }
$$

| Object | Dimension |
|---|---|
| $PM_5P\cong M_2$ | $4$ |
| $QM_5Q\cong M_3$ | $9$ |
| $PM_5Q\cong\mathbb{C}^{2\times3}$ | $6$ |
| $QM_5P\cong\mathbb{C}^{3\times2}$ | $6$ |
| Total | $25$ |
| $P(GL_2\times GL_3)$ | $12$ |
| Maximal torus $1+2+1$ | $4$ |
| Relative scale | $1$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$ | A rank-two projection, $P^2=P$, $\operatorname{rank}P=2$ |
| $Q=I-P$ | The complementary projection, of rank $3$ |
| $A_{11},A_{12},A_{21},A_{22}$ | The four blocks of $A$ in the $2+3$ decomposition |
| $\mathcal{M}=PM_5Q\oplus QM_5P$ | The off-diagonal bimodule, dimension $12$ |
| $P(GL_2\times GL_3)$ | The block-diagonal stabiliser in $PGL_5$ |
| $T(PGL_2),T(PGL_3)$ | The corner tori, dimensions $1$ and $2$ |
| $\mu$ | The relative scale, $\operatorname{diag}(\mu I_2,I_3)$ modulo scalars |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition by an idempotent, the corner isomorphisms and the graded algebra of a block decomposition.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the corner decomposition of an algebra with involution and the behaviour of the summands.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the block multiplication and the rank of a projection.
- [The Matrix Algebra $M_5(\mathbb{C})$](the-matrix-algebra-m5c.html), for the algebra and its unit group.
- [The Peirce Decomposition](the-peirce-decomposition-of-m5c.html), for the coarse split $1+4+4+16$ and the corner isomorphisms.
- [The Rank-Two Split](the-rank-two-split-of-m5c.html), for the corners $4+6+6+9$ and the two-sided Peirce table.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m5c.html), for the four-parameter gauge and the simple nilpotents.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m5c.html), for the modules of the corner and of the whole algebra.
- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the biquaternion model $M_2(\mathbb{C})$ inside the corner.
