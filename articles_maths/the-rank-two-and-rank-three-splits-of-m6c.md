# __The Rank-Two and Rank-Three Splits__

## Introduction

A single idempotent of rank two cuts $M_6(\mathbb{C})$ into corners of dimensions

$$
4+8+8+16=36,
$$

and one of rank three cuts it into

$$
9+9+9+9=36 .
$$

The corner algebras are $P M_6P\cong M_2$, $Q M_6Q\cong M_4$ in the first case and $P M_6P\cong M_3$, $Q M_6Q\cong M_3$ in the second. The mixed corners are the mass blocks: of dimension $8=2\cdot4$ in the rank-two split, and of dimension $9=3\cdot3$ in the rank-three split.

This article states the two splits, proves the corner isomorphisms, and writes the two-sided Peirce tables. It is the detailed companion of *The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners*, which treats the gauge decomposition and the block embeddings; the gauge is not repeated here.

It assumes the coarse Peirce decomposition of *The Peirce Decomposition* and the algebra $M_6(\mathbb{C})$ of *The Matrix Algebra $M_6(\mathbb{C})$*. It uses no form and no topology. The mass block's polar decomposition is *The Mass Block and the Chiral Polar Decomposition*; the chiral split is *The Two Chiralities*.

## The Rank-Two Projection

### The Corners

**Theorem.** Let $E\in M_6(\mathbb{C})$ be an idempotent of rank two and $F=I_6-E$. Then

$$
M_6(\mathbb{C})=EME\oplus EMF\oplus FME\oplus FMF,
$$

with

$$
\dim EME=4,\qquad
\dim EMF=8,\qquad
\dim FME=8,\qquad
\dim FMF=16 .
$$

**Proof.** In coordinates with $E=\operatorname{diag}(I_2,0_4)$ and $F=\operatorname{diag}(0_2,I_4)$, the four corners are the blocks of sizes $2\times2$, $2\times4$, $4\times2$ and $4\times4$. Their dimensions are $4,8,8,16$.

### The Corner Isomorphisms

**Theorem.** With $E$ of rank two and $F=I_6-E$,

$$
EME\cong M_2(\mathbb{C}),\qquad
FMF\cong M_4(\mathbb{C}),
$$

and

$$
EMF\cong\operatorname{Hom}(\operatorname{im}F,\operatorname{im}E)\cong\mathbb{C}^{2\times4},
\qquad
FME\cong\operatorname{Hom}(\operatorname{im}E,\operatorname{im}F)\cong\mathbb{C}^{4\times2}.
$$

**Proof.** The corner $EME$ acts faithfully on the image of $E$, a two-dimensional space, and every endomorphism of that space is of the form $EAE$; so $EME\cong\operatorname{End}(\operatorname{im}E)\cong M_2$. The same argument with $F$ gives $M_4$. An element $EAF$ is a linear map from $\operatorname{im}F$ to $\operatorname{im}E$; the map $EAF\mapsto(EAF)|_{\operatorname{im}F}$ is an isomorphism onto $\operatorname{Hom}(\operatorname{im}F,\operatorname{im}E)$, of dimension $2\cdot4=8$. The corner $FME$ is the same with the roles exchanged.

**Corollary (the block form).** Every element is

$$
A=\begin{pmatrix}A_2&M\\N&B_4\end{pmatrix},
\qquad
A_2\in M_2,\quad M\in\mathbb{C}^{2\times4},\quad N\in\mathbb{C}^{4\times2},\quad B_4\in M_4,
$$

with $M$ the mass block of dimension $8$ and $N$ its partner.

**Remark (the split is unique up to conjugacy).** All rank-two idempotents of $M_6$ are conjugate under $GL_6$: two idempotents of the same rank have images of the same dimension, and a linear isomorphism carrying one image to the other conjugates the idempotents. So the rank-two split has one isomorphism type, and the block form above is a normal form. The same holds for rank three.

**Proof.** If $E,F$ have rank two, choose an isomorphism $g$ with $g(\operatorname{im}E)=\operatorname{im}F$. Then $gEg^{-1}$ has image $\operatorname{im}F$ and is the identity there, hence equals $F$; so $F=gEg^{-1}$.

### The Two-Sided Peirce Table

**Theorem.** The corners multiply according to

| $\cdot$ | $EME$ | $EMF$ | $FME$ | $FMF$ |
|---|---|---|---|---|
| $EME$ | $EME$ | $EMF$ | $0$ | $0$ |
| $EMF$ | $0$ | $0$ | $EME$ | $EMF$ |
| $FME$ | $FME$ | $FMF$ | $0$ | $0$ |
| $FMF$ | $0$ | $0$ | $FME$ | $FMF$ |

with dimensions

| $\cdot$ | $4$ | $8$ | $8$ | $16$ |
|---|---|---|---|---|
| $4$ | $4$ | $8$ | $0$ | $0$ |
| $8$ | $0$ | $0$ | $4$ | $8$ |
| $8$ | $8$ | $16$ | $0$ | $0$ |
| $16$ | $0$ | $0$ | $8$ | $16$ |

**Proof.** The general Peirce rule is $A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}$ with $i,j,k,l\in\{E,F\}$. The nonvanishing products are the eight composable triples $E\to E\to E$, $E\to E\to F$, $E\to F\to E$, $E\to F\to F$, $F\to E\to E$, $F\to E\to F$, $F\to F\to E$ and $F\to F\to F$, which give the eight nonzero entries of the table. The dimensions are those of the target corners, not of the products: the table records containment, and the product of two corners can be a proper subset.

**Remark (the products are not all surjective).** The corner product $FME\cdot EMF$ is contained in $FMF$ but is not all of $FMF$: it is the set of products $NM$ of a $4\times2$ matrix with a $2\times4$ matrix, which is exactly the set of $4\times4$ matrices of rank at most two, not the whole $4\times4$ space. The table is a table of containments; the equality of a product with its target holds only for some pairs. For instance $EMF\cdot FME=EME$, because every $2\times2$ matrix is $MN$ with $M=[A,0]$ and $N=[I_2;0]$.

**Corollary (the two-sided structure).** The corner $EME$ acts on $EMF$ on the left and on $FME$ on the right; $FMF$ acts on $EMF$ on the right and on $FME$ on the left. The table above is the two-sided multiplication table of the quartet.

## The Rank-Three Projection

### The Corners

**Theorem.** Let $E\in M_6(\mathbb{C})$ be an idempotent of rank three and $F=I_6-E$. Then

$$
M_6(\mathbb{C})=EME\oplus EMF\oplus FME\oplus FMF,
$$

with

$$
\dim EME=\dim EMF=\dim FME=\dim FMF=9,
$$

and

$$
9+9+9+9=36 .
$$

**Proof.** In coordinates with $E=\operatorname{diag}(I_3,0_3)$ and $F=\operatorname{diag}(0_3,I_3)$, the four corners are the four $3\times3$ blocks.

### The Corner Isomorphisms

**Theorem.** With $E$ of rank three and $F=I_6-E$,

$$
EME\cong M_3(\mathbb{C}),\qquad
FMF\cong M_3(\mathbb{C}),
\qquad
EMF\cong FME\cong M_3(\mathbb{C})
$$

as vector spaces, and

$$
EMF\cong\operatorname{Hom}(\operatorname{im}F,\operatorname{im}E),
\qquad
FME\cong\operatorname{Hom}(\operatorname{im}E,\operatorname{im}F).
$$

**Proof.** The same argument as for rank two, with $2$ replaced by $3$. The mixed corners are $3\times3$ matrix spaces, of dimension $9$.

**Corollary (the block form).** Every element is

$$
A=\begin{pmatrix}A_+&M\\N&A_-\end{pmatrix},
\qquad
A_+,A_-,M,N\in M_3(\mathbb{C}),
$$

with $M$ the mass block of dimension $9$ and $N$ its partner.

**Remark (the square mass block).** The rank-three split is the only one of the three coarse splits in which the mass block is square and has the same size as the diagonal blocks. This is why the algebra is a tensor product in this case, $M_6\cong M_3\otimes M_2$, and not in the rank-two case.

### The Two-Sided Peirce Table

**Theorem.** The corners multiply according to

| $\cdot$ | $EME$ | $EMF$ | $FME$ | $FMF$ |
|---|---|---|---|---|
| $EME$ | $EME$ | $EMF$ | $0$ | $0$ |
| $EMF$ | $0$ | $0$ | $EME$ | $EMF$ |
| $FME$ | $FME$ | $FMF$ | $0$ | $0$ |
| $FMF$ | $0$ | $0$ | $FME$ | $FMF$ |

with dimensions

| $\cdot$ | $9$ | $9$ | $9$ | $9$ |
|---|---|---|---|---|
| $9$ | $9$ | $9$ | $0$ | $0$ |
| $9$ | $0$ | $0$ | $9$ | $9$ |
| $9$ | $9$ | $9$ | $0$ | $0$ |
| $9$ | $0$ | $0$ | $9$ | $9$ |

**Proof.** The same eight composable pairs as in the rank-two table; every corner has dimension nine.

**Remark (the products are surjective here).** In the rank-three split the products $EMF\cdot FME=EME$ and $FME\cdot EMF=FMF$ are surjective, because every $3\times3$ matrix is a product of a $3\times3$ and a $3\times3$ (take the first factor to be the identity). This is the algebraic difference between the two splits: the rank-three mass block is a square matrix that may be invertible, while the rank-two mass block is rectangular and has no inverse.

## The Two Mass Blocks

### Dimensions and Ranks

**Theorem.** The mass block of the rank-$p$ split is the mixed corner $EMF$, of dimension

$$
p(6-p).
$$

For $p=1,2,3$ the dimensions are

$$
5,\qquad 8,\qquad 9 .
$$

The generic rank of the mass block is $\min(p,6-p)$, so the numbers of mass channels are

$$
1,\qquad 2,\qquad 3 .
$$

**Proof.** The mass block is a $p\times(6-p)$ matrix; its dimension is the product, and its rank is at most the smaller of the two sizes, attained on the open dense set of full-rank matrices.

**Corollary (the two mass blocks of the title).** The rank-two split has the mass block of dimension $8$, a $2\times4$ matrix with two mass channels. The rank-three split has the mass block of dimension $9$, a $3\times3$ matrix with three mass channels.

### The Mass Block as a Bimodule

**Theorem.** The mixed corner $EMF$ is a left module over $EME\cong M_p$ and a right module over $FMF\cong M_{6-p}$, and

$$
EMF\cong\mathbb{C}^p\otimes(\mathbb{C}^{6-p})^*
$$

as a bimodule. The corner $FME$ is the dual bimodule.

**Proof.** The left action is $A\cdot M=A_{11}M$ and the right action is $M\cdot B=MB_{22}$; the map $u\otimes\varphi\mapsto u\varphi$ intertwines them. The dimensions are $p(6-p)$ on both sides.

**Corollary (the mass-squared operator).** The product $MN\in EME$ is the **mass-squared operator** of the mass block, and $NM\in FMF$ is its partner. For the rank-two split it is a $2\times2$ matrix; for the rank-three split it is a $3\times3$ matrix.

**Proof.** $M\in\mathbb{C}^{p\times(6-p)}$ and $N\in\mathbb{C}^{(6-p)\times p}$, so $MN$ is $p\times p$ and $NM$ is $(6-p)\times(6-p)$.

**Proposition (the singular values).** The number of nonzero singular values of $M$ is its rank, at most $\min(p,6-p)$. When the partner is the Hermitian adjoint, $N=M^*$, the nonzero eigenvalues of $MN=MM^*$ are the squares of the nonzero singular values of $M$, and the same holds for $NM=M^*M$.

**Proof.** If $M=U\Sigma V^*$ is the singular value decomposition, then $MM^*=U\Sigma^2U^*$ and $M^*M=V\Sigma^2V^*$; the eigenvalues are the squares of the singular values. For a general independent partner $N$, the spectrum of $MN$ is not determined by the singular values of $M$.

### The Massless Locus

**Theorem.** The mass block vanishes exactly on the diagonal corner algebra

$$
\left\{\begin{pmatrix}A_p&0\\0&A_{6-p}\end{pmatrix}\right\}
\cong M_p\oplus M_{6-p},
$$

of dimension $p^2+(6-p)^2$. For $p=2$ this is $M_2\oplus M_4$, of dimension $20$; for $p=3$ it is $M_3\oplus M_3$, of dimension $18$.

**Proof.** The mass block is the $EMF$ corner; it vanishes if and only if the element has no $EMF$ component, that is if and only if it is block diagonal. The dimension is $p^2+(6-p)^2$.

**Corollary (the mass adds the mixed dimensions).** The full algebra has dimension

$$
p^2+(6-p)^2+2p(6-p)=36,
$$

so the two mixed corners add $2p(6-p)$ dimensions: $16$ at $p=2$ and $18$ at $p=3$.

**Proof.** $2\cdot2\cdot4=16$ and $2\cdot3\cdot3=18$.

## The Two-Sided Peirce Tables Compared

### The General Table

For any rank $p$, the two-sided Peirce table is

| $\cdot$ | $EME$ | $EMF$ | $FME$ | $FMF$ |
|---|---|---|---|---|
| $EME$ | $EME$ | $EMF$ | $0$ | $0$ |
| $EMF$ | $0$ | $0$ | $EME$ | $EMF$ |
| $FME$ | $FME$ | $FMF$ | $0$ | $0$ |
| $FMF$ | $0$ | $0$ | $FME$ | $FMF$ |

with the dimensions

$$
p^2,\quad p(6-p),\quad p(6-p),\quad (6-p)^2
$$

on the diagonal and the corresponding target dimensions in the nonzero entries.

**Proof.** The table depends only on the composability of the arrows $E\to E$, $E\to F$, $F\to E$, $F\to F$; the dimension of each entry is the dimension of the target corner.

### The Three Tables

| $p$ | $EME$ | $EMF$ | $FME$ | $FMF$ | Total |
|---|---|---|---|---|---|
| $1$ | $1$ | $5$ | $5$ | $25$ | $36$ |
| $2$ | $4$ | $8$ | $8$ | $16$ | $36$ |
| $3$ | $9$ | $9$ | $9$ | $9$ | $36$ |

**Proof.** Substitute $p=1,2,3$ in $p^2,p(6-p),p(6-p),(6-p)^2$.

### The Refinement by the Fine Peirce Lines

**Theorem.** For an idempotent $E=\sum_{k\in I}P_k$ that is a sum of $p$ Lagrange projectors (equivalently, after conjugating $E$ into the frame), the coarse corners of the rank-$p$ split are unions of the fine Peirce lines $A_{kl}=P_kM_6P_l$:

$$
EME=\bigoplus_{k,l\in I}A_{kl},
\qquad
EMF=\bigoplus_{k\in I,\,l\notin I}A_{kl},
\qquad
FME=\bigoplus_{k\notin I,\,l\in I}A_{kl},
\qquad
FMF=\bigoplus_{k,l\notin I}A_{kl},
$$

where $I$ is a set of $p$ indices (the lines in the image of $E$) and $E=\sum_{k\in I}P_k$.

**Proof.** $E$ is the sum of the $p$ Lagrange projectors indexed by $I$, and $F$ is the sum of the other $6-p$. The corner $EME$ is the sum of the lines $P_kM P_l$ with $k,l\in I$, and similarly for the other three.

**Corollary.** The coarse splits have

$$
p^2,\quad p(6-p),\quad p(6-p),\quad (6-p)^2
$$

fine lines respectively. At $p=2$ this is $4,8,8,16$; at $p=3$ it is $9,9,9,9$.

**Proof.** There are $p^2$ ordered pairs $(k,l)$ with both indices in $I$, $p(6-p)$ with the first in $I$ and the second outside, and so on.

**Remark (coarse and fine).** The rank-three split by the special idempotent $\Pi_+=P_1+P_3+P_5$ is the chiral split of *The Two Chiralities*: its corners are the $3\times3$ chiral blocks and the mass block of dimension $9$. A general rank-three idempotent gives a conjugate split, with the same corner dimensions; the chiral split is the representative adapted to the root. **The corner dimensions see only the rank; the root sees which lines are grouped.**

## Summary

The rank-two idempotent splits the algebra into corners of dimensions

$$
4+8+8+16=36,
\qquad
EME\cong M_2,\quad FMF\cong M_4,
$$

with the mass block $EMF\cong\mathbb{C}^{2\times4}$ of dimension $8$ and two mass channels. The rank-three idempotent splits it into

$$
9+9+9+9=36,
\qquad
EME\cong M_3,\quad FMF\cong M_3,
$$

with the square mass block $EMF\cong M_3$ of dimension $9$ and three mass channels.

$$
\boxed{\ \text{rank }2:\ 4+8+8+16,\quad \text{rank }3:\ 9+9+9+9 .\ }
$$

The two-sided Peirce table is the same in both cases,

| $\cdot$ | $EME$ | $EMF$ | $FME$ | $FMF$ |
|---|---|---|---|---|
| $EME$ | $EME$ | $EMF$ | $0$ | $0$ |
| $EMF$ | $0$ | $0$ | $EME$ | $EMF$ |
| $FME$ | $FME$ | $FMF$ | $0$ | $0$ |
| $FMF$ | $0$ | $0$ | $FME$ | $FMF$ |

and both corner products are surjective in the rank-three split, while in the rank-two split $EMF\cdot FME=EME$ is surjective and $FME\cdot EMF$ is only the rank-at-most-two locus of $FMF$.

| Split | $EME$ | $EMF$ | $FME$ | $FMF$ | Mass block | Channels |
|---|---|---|---|---|---|---|
| $p=1$ | $1$ | $5$ | $5$ | $25$ | $1\times5$ | $1$ |
| $p=2$ | $4$ | $8$ | $8$ | $16$ | $2\times4$ | $2$ |
| $p=3$ | $9$ | $9$ | $9$ | $9$ | $3\times3$ | $3$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E,F=I_6-E$ | idempotents of ranks $p$ and $6-p$ |
| $EME,EMF,FME,FMF$ | the four corners |
| $M$ | the mass block $EMF$, of dimension $p(6-p)$ |
| $N$ | the partner $FME$ |
| $MN$ | the mass-squared operator in $EME$ |
| $I$ | the set of $p$ indices in the image of $E$ |
| $A_{kl}$ | the fine Peirce lines refining the corners |

## Further Reading

- [The Peirce Decomposition](the-peirce-decomposition-of-m6c.html), for the general corner multiplication and the rank-one split.
- [The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners](the-m3-m3-and-m2-m4-corners-of-m6c.html), for the gauge decomposition and the block embeddings.
- [The Two Chiralities](the-two-chiralities-of-m6c.html), for the rank-three split by $\Pi_+$.
- [The Mass Block and the Chiral Polar Decomposition](the-mass-block-and-the-chiral-polar-decomposition-of-m6c.html), for the polar decomposition of the mass block.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m6c.html), for the corner modules.
- [Idempotents and Involutions of an Algebra](idempotents-and-involutions-of-an-algebra.html), for the conjugacy of idempotents of a fixed rank.
- [The Geometry of the Idempotents](the-geometry-of-the-idempotents-of-m6c.html), for the homogeneous space of the rank-$p$ idempotents.
