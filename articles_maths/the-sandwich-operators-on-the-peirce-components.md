# __The Sandwich Operators on the Peirce Components__

## Introduction

The sandwich operator of an algebra is the two-sided multiplication $T_{a,b}(x)=axb$. An idempotent $e$ cuts the algebra into four Peirce corners,

$$
A=eAe\oplus eAf\oplus fAe\oplus fAf, \qquad f=1-e,
$$

and the sandwich is the operator that sees the four corners at once. The present article computes the block matrix of $T_{a,b}$ relative to the Peirce decomposition, identifies the elementary sandwiches $T_{e_i,e_j}$ as the Peirce projections, and reads the composition of two sandwiches as the multiplication in the enveloping algebra $A\otimes A^{\mathrm{op}}$.

The result is a matrix picture. If $a=\sum_{i,j}a_{ij}$ and $b=\sum_{k,l}b_{kl}$ are the Peirce components, then the block of $T_{a,b}$ from the source corner $A_{rs}$ to the target corner $A_{il}$ is

$$
x\longmapsto a_{ir}\,x\,b_{sl},
$$

a sandwich of the two corner elements $a_{ir}$ and $b_{sl}$. A homogeneous $a\in A_{ij}$ and $b\in A_{kl}$ therefore give a sandwich with a single nonzero block, from $A_{jk}$ to $A_{il}$; the pattern of the blocks is the Kronecker product of the two $2\times2$ block matrices of $a$ and $b^{\mathsf T}$. In the scalar case, when all four corners are one-dimensional, the $4\times4$ matrix of $T_{a,b}$ is literally $a\otimes b^{\mathsf T}$.

The article is the Peirce companion of *The Sandwich Operator on an Algebra* and *Left and Right Multiplication*. The Peirce decomposition is that of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the off-diagonal part and the noncentral case are *Off-Diagonal Peirce Components and Noncentral Idempotents*; the diagonal part is *The Centraliser and the Diagonal Peirce Part*; and the operator space is *The Operators on an Algebra*. The enveloping algebra is \(A\otimes A^{\mathrm{op}}\), with the action \(x\mapsto axb\). The article uses no form and no involution.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra with $1\neq0$, not assumed commutative and not assumed finite-dimensional unless a statement says so. The idempotent is $e$, its complement is $f=1-e$, and the two are written $e_0=e$, $e_1=f$. The corners are

$$
A_{ij}=e_iAe_j, \qquad i,j\in\{0,1\},
$$

and the Peirce decomposition is $A=\bigoplus_{i,j}A_{ij}$, with the multiplication table

$$
A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}.
$$

The sandwich is $T_{a,b}(x)=axb$, and $\mathcal{S}(A)$ is the sandwich space, the image of $A\otimes A^{\mathrm{op}}\to\operatorname{End}_k(A)$, $a\otimes b\mapsto T_{a,b}$.

## The Peirce Decomposition and the Sandwich

### The corners and the multiplication table

The Peirce decomposition is the direct sum of the four corners, and the product of two corners is zero unless the right index of the first equals the left index of the second:

$$
A=A_{00}\oplus A_{01}\oplus A_{10}\oplus A_{11}, \qquad
A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}.
$$

The corners $A_{00}=eAe$ and $A_{11}=fAf$ are algebras with identities $e$ and $f$; the mixed corners $A_{01}=eAf$ and $A_{10}=fAe$ are bimodules over them. The decomposition and the table are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the off-diagonal part $N=A_{01}\oplus A_{10}$ and its properties are *Off-Diagonal Peirce Components and Noncentral Idempotents*.

### The sandwich on a corner

**Proposition.** Let $a_{ij}\in A_{ij}$, $b_{kl}\in A_{kl}$ and $x\in A_{rs}$. Then

$$
a_{ij}\,x\,b_{kl}=0 \quad\text{unless } j=r \text{ and } k=s,
$$

and when $j=r$ and $k=s$ the product lies in $A_{il}$.

*Proof.* The product $a_{ij}x$ lies in $A_{ij}A_{rs}$, which is zero unless $j=r$, and then lies in $A_{is}$. Multiplying by $b_{kl}$, the product lies in $A_{is}A_{kl}$, which is zero unless $s=k$, and then lies in $A_{il}$.

**Corollary (the elementary sandwich).** For homogeneous $a\in A_{ij}$ and $b\in A_{kl}$, the sandwich $T_{a,b}$ has a single nonzero block, from the source corner $A_{jk}$ to the target corner $A_{il}$:

$$
\boxed{\;T_{a,b}(A_{rs})=0 \quad\text{for }(r,s)\neq(j,k), \qquad
T_{a,b}(A_{jk})\subseteq A_{il}\;}.
$$

On the source corner the block is $x\mapsto axb$. Every sandwich is a sum of such elementary sandwiches, one for each pair of Peirce components of $a$ and $b$.

### The block matrix of a general sandwich

Let

$$
a=\sum_{i,j}a_{ij}, \qquad b=\sum_{k,l}b_{kl}, \qquad a_{ij}\in A_{ij},\ b_{kl}\in A_{kl}.
$$

For $x\in A_{rs}$, the proposition applied to each pair of components gives

$$
T_{a,b}(x)=a x b=\sum_{i,j,k,l}a_{ij}\,x\,b_{kl}
=\sum_{i,l}a_{ir}\,x\,b_{sl},
$$

the last sum using $j=r$ and $k=s$. The block from $A_{rs}$ to $A_{il}$ is therefore

$$
T_{(i,l),(r,s)}:A_{rs}\longrightarrow A_{il}, \qquad x\longmapsto a_{ir}\,x\,b_{sl}.
$$

**Definition.** The **block matrix** of $T_{a,b}$ relative to the Peirce decomposition is the $4\times4$ matrix whose rows are indexed by the target corners $A_{il}$ and whose columns are indexed by the source corners $A_{rs}$, with entry $T_{(i,l),(r,s)}$ as above.

**Theorem.** The operator $T_{a,b}$ is the direct sum of the sixteen blocks $T_{(i,l),(r,s)}$. The block $T_{(i,l),(r,s)}$ is identically zero whenever $a_{ir}=0$ or $b_{sl}=0$; conversely, for a matrix algebra and nonzero $a_{ir},b_{sl}$, the block is nonzero. In the scalar case, when all four corners are one-dimensional, the $4\times4$ matrix of $T_{a,b}$ is the Kronecker product

$$
a\otimes b^{\mathsf T},
$$

with the row index $(i,l)$ and the column index $(r,s)$.

*Proof.* The direct sum statement is the computation above, summed over $i,l$. The vanishing criterion is immediate from $x\mapsto a_{ir}xb_{sl}$. For the scalar case, the entry is $a_{ir}b_{sl}$, which is the $(i,l),(r,s)$ entry of $a\otimes b^{\mathsf T}$ because $(b^{\mathsf T})_{ls}=b_{sl}$.

**Remark (the pattern, not the entries).** In a general algebra the block entries are operators between corner spaces, not scalars, and the block matrix is not a Kronecker product of two matrices of elements. What is always the Kronecker product is the **support pattern**: the block $(i,l),(r,s)$ can be nonzero only when $a_{ir}$ and $b_{sl}$ are both nonzero. The entries themselves are the sandwiches $T_{a_{ir},b_{sl}}$, and they carry the corner structure. In a matrix algebra with all corners one-dimensional, the pattern and the entries coincide with $a\otimes b^{\mathsf T}$.

### The diagonal and the off-diagonal cases

The block formula specializes to the two cases that matter most.

**Corollary (diagonal parameters).** If $a,b\in D=A_{00}\oplus A_{11}$, then $a_{ir}=0$ unless $i=r$ and $b_{sl}=0$ unless $s=l$. The block from $A_{rs}$ to $A_{il}$ is therefore nonzero only for $(i,l)=(r,s)$, and on the corner $A_{rs}$ it is

$$
T_{a_{rr},b_{ss}}:x\longmapsto a_{rr}\,x\,b_{ss}.
$$

So a sandwich with diagonal parameters preserves each Peirce corner and acts on $A_{rs}$ by the sandwich of the corner elements $a_{rr}$ and $b_{ss}$.

**Corollary (homogeneous parameters).** If $a\in A_{ij}$ and $b\in A_{kl}$, the sandwich has one block, from $A_{jk}$ to $A_{il}$. The general rule is the single block

$$
A_{jk}\longrightarrow A_{il},\qquad x\longmapsto a x b.
$$

For example:

**(a)** $a,b\in A_{00}$: the block is $A_{00}\to A_{00}$; for $a,b\in A_{11}$ it is $A_{11}\to A_{11}$.

**(b)** $a\in A_{01}$ and $b\in A_{10}$: the block is $A_{11}\to A_{00}$.

**(c)** $a\in A_{10}$ and $b\in A_{01}$: the block is $A_{00}\to A_{11}$.

**(d)** $a,b\in A_{01}$: the block is $A_{10}\to A_{01}$.

**(e)** $a,b\in A_{10}$: the block is $A_{01}\to A_{10}$.

The other pairs $(i,j)$ and $(k,l)$ give the other blocks of the $4\times4$ matrix by the same rule; the rule covers all sixteen pairs.

**Example (the degenerate case).** In the upper triangular algebra $T_2(k)$ with $e=E_{11}$, the corner $A_{10}=fAe$ is zero, because the lower-left entry is always zero. The block matrix has a zero row and a zero column, and the sandwich acts on the three remaining corners $A_{00}=kE_{11}$, $A_{01}=kE_{12}$, $A_{11}=kE_{22}$. The block formula remains correct; it simply has fewer nonzero blocks. The Peirce decomposition is not a full $2\times2$ matrix decomposition when a mixed corner vanishes.

## The Elementary Sandwiches

### The Peirce projections

**Theorem.** For $i,j\in\{0,1\}$, the elementary sandwich

$$
E_{ij}:=T_{e_i,e_j}:A\longrightarrow A, \qquad E_{ij}(x)=e_i\,x\,e_j,
$$

is the projection of $A$ onto the corner $A_{ij}$ along the other three corners. The four projections are orthogonal and complete:

$$
\boxed{\;E_{ij}E_{kl}=\delta_{ik}\delta_{jl}E_{ij}, \qquad \sum_{i,j}E_{ij}=\mathrm{id}_A\;} .
$$

*Proof.* On $x\in A_{rs}$, the product $e_ix e_j$ is nonzero only when $r=i$ and $s=j$, and then equals $x$; hence $E_{ij}$ is the identity on $A_{ij}$ and zero on the other corners. The composition is

$$
E_{ij}E_{kl}(x)=e_i(e_kxe_l)e_j=\delta_{ik}\delta_{lj}e_ixe_j=\delta_{ik}\delta_{jl}E_{ij}(x),
$$

using $e_ie_k=\delta_{ik}e_i$ and $e_le_j=\delta_{lj}e_j$; the sum is $\sum_{i,j}e_ixe_j=(\sum_i e_i)x(\sum_j e_j)=x$.

**Corollary.** The four Peirce projections are the elementary sandwiches of the complete orthogonal family $e,f$, and they form a complete family of pairwise orthogonal projections in $\operatorname{End}_k(A)$:

$$
E_{00}+E_{01}+E_{10}+E_{11}=\mathrm{id}, \qquad E_{ij}E_{kl}=\delta_{ik}\delta_{jl}E_{ij}.
$$

Each $E_{ij}$ is the projection onto its corner $A_{ij}$ along the other three corners. When a mixed corner vanishes, the corresponding projection is zero, and the family degenerates; the relations remain true.

**Remark.** The diagonal corner projection $P_e=T_{e,e}=E_{00}$ is the sandwich of $e$ with itself; it is not the projection onto the diagonal part $D=A_{00}\oplus A_{11}$, which is $E_{00}+E_{11}$. The four $E_{ij}$ are the finest Peirce projections; the sums $E_{00}+E_{01}=L_e$, $E_{00}+E_{10}=R_e$, $E_{00}+E_{11}$ and $E_{01}+E_{10}$ are the coarser operators of *Left and Right Multiplication on the Diagonal Peirce Part*.

### Composition

**Proposition.** For all $a,b,c,d\in A$,

$$
\boxed{\;T_{a,b}\,T_{c,d}=T_{ac,\,db}\;}.
$$

*Proof.* $T_{a,b}(T_{c,d}(x))=a(cxd)b=(ac)x(db)$.

**Corollary.** The assignment $(a,b)\mapsto T_{a,b}$ is a $k$-bilinear map $A\times A\to\operatorname{End}_k(A)$ that factors through the enveloping algebra,

$$
A\otimes A^{\mathrm{op}}\longrightarrow\operatorname{End}_k(A), \qquad a\otimes b\longmapsto T_{a,b},
$$

and the multiplication in the image is $(a\otimes b)(c\otimes d)=ac\otimes db$. In particular the elementary sandwiches satisfy

$$
E_{ij}E_{kl}=\delta_{ik}\delta_{jl}E_{ij},
$$

the orthogonality relations of the Peirce projections.

**Remark.** The composition law is the reason the sandwich is the natural action of the enveloping algebra on $A$: the first parameter multiplies on the left in the order of the product, and the second multiplies on the right in the reverse order. The Peirce decomposition of $A$ writes the enveloping algebra as

$$
A\otimes A^{\mathrm{op}}=\bigoplus_{i,j,k,l}A_{ij}\otimes A_{kl}^{\mathrm{op}},
$$

and the summand $A_{ij}\otimes A_{kl}^{\mathrm{op}}$ maps to the single block from $A_{jk}$ to $A_{il}$. The block matrix of §*The block matrix of a general sandwich* is the matrix form of this decomposition.

### Kernel and image

The block matrix gives the kernel and the image without further computation.

**Proposition.** Let $T=T_{a,b}$.

**(a)** The image of $T$ is contained in the sum of the target corners $A_{il}$ for which the block row $(i,l)$ is nonzero, that is, for which there exist $r,s$ with $a_{ir}\neq0$, $b_{sl}\neq0$ and $A_{rs}\neq0$.

**(b)** The kernel of $T$ contains the sum of the source corners $A_{rs}$ for which every block $T_{(i,l),(r,s)}$ vanishes; in the scalar case this is exactly the sum of the corners whose block column is zero.

**(c)** $T_{a,b}=0$ exactly when $aAb=0$. In a prime algebra, in particular in $M_n(k)$, this is equivalent to $a=0$ or $b=0$.

*Proof.* (a) and (b) are the direct-sum form of the block matrix. (c) $T_{a,b}=0$ says $axb=0$ for every $x$, that is, $aAb=0$. If $A$ is prime and $a,b\neq0$, then $aAb\neq0$ by the definition of primeness, so $T\neq0$. The converse is immediate.

**Remark.** The evaluation $T_{a,b}(1)=ab$ shows that $ab=0$ is necessary for $T_{a,b}=0$, but it is not sufficient. In $M_2(k)$, the elements $a=b=E_{12}$ satisfy $ab=0$, while $T_{a,b}(E_{21})=E_{12}E_{21}E_{12}=E_{12}\neq0$. The kernel is a statement about the whole corner structure, not about the single product $ab$.

## Examples

### The matrix algebra $M_2(k)$

Let $e=E_{11}$, $f=E_{22}$. The four corners are the four lines

$$
A_{00}=kE_{11}, \qquad A_{01}=kE_{12}, \qquad A_{10}=kE_{21}, \qquad A_{11}=kE_{22},
$$

and the basis $(E_{11},E_{12},E_{21},E_{22})$ is corner-adapted. For

$$
a=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}, \qquad
b=\begin{pmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{pmatrix},
$$

the block matrix of $T_{a,b}$ is $a\otimes b^{\mathsf T}$:

$$
\begin{pmatrix}
a_{11}b_{11} & a_{11}b_{21} & a_{12}b_{11} & a_{12}b_{21}\\
a_{11}b_{12} & a_{11}b_{22} & a_{12}b_{12} & a_{12}b_{22}\\
a_{21}b_{11} & a_{21}b_{21} & a_{22}b_{11} & a_{22}b_{21}\\
a_{21}b_{12} & a_{21}b_{22} & a_{22}b_{12} & a_{22}b_{22}
\end{pmatrix}.
$$

The rows are the target corners in the order $00,01,10,11$ and the columns are the source corners in the same order. The block at row $01$, column $01$ is $a_{11}b_{22}$: it is the sandwich of the diagonal entries, not of the off-diagonal entries. The formula shows exactly which entry of $a$ and which entry of $b$ enters each block: the target row $(i,l)$ and the source column $(r,s)$ select $a_{ir}$ and $b_{sl}$.

**Example (a single block).** For $a=E_{12}\in A_{01}$ and $b=E_{12}\in A_{01}$, the sandwich has a single block from $A_{10}$ to $A_{01}$:

$$
T_{E_{12},E_{12}}(E_{21})=E_{12}E_{21}E_{12}=E_{12},
$$

and it kills the other three corners. The $4\times4$ matrix has a single $1$ at row $01$, column $10$. The product $ab=E_{12}E_{12}=0$, but the sandwich is nonzero; the example is the smallest witness of the difference between $ab$ and $T_{a,b}$.

**Example (the Peirce projections).** The four elementary sandwiches are

$$
E_{00}=\operatorname{diag}(1,0,0,0), \quad
E_{01}=\operatorname{diag}(0,1,0,0), \quad
E_{10}=\operatorname{diag}(0,0,1,0), \quad
E_{11}=\operatorname{diag}(0,0,0,1)
$$

in the corner-adapted basis, and their orthogonality is visible. The sandwich $T_{E_{11},E_{22}}=E_{01}$ projects onto the line $kE_{12}$; the sandwich $T_{E_{11},E_{11}}=E_{00}$ projects onto $kE_{11}$.

### The split algebra $k\times k$

Let $A=k\times k$ and $e=(1,0)$, $f=(0,1)$. The corners are

$$
A_{00}=ke, \qquad A_{11}=kf, \qquad A_{01}=A_{10}=0,
$$

so the Peirce decomposition has only two nonzero corners. For $a=(a_0,a_1)$ and $b=(b_0,b_1)$, the sandwich is the diagonal operator

$$
T_{a,b}(x_0,x_1)=(a_0b_0x_0,\ a_1b_1x_1),
$$

and its block matrix is diagonal with entries $a_0b_0$ and $a_1b_1$ on the two corners. The example is the scalar case in which the mixed corners vanish; the Kronecker formula degenerates to the two diagonal entries.

### The upper triangular algebra

Let $A=T_2(k)$ and $e=E_{11}$. The corners are

$$
A_{00}=kE_{11}, \qquad A_{01}=kE_{12}, \qquad A_{10}=0, \qquad A_{11}=kE_{22}.
$$

The block matrix has the zero row and column indexed by $A_{10}$; on the three remaining corners the nonzero blocks are those determined by the formula of §*The block matrix of a general sandwich*. For $a=\begin{pmatrix}a_{11}&a_{12}\\0&a_{22}\end{pmatrix}$ and $b=\begin{pmatrix}b_{11}&b_{12}\\0&b_{22}\end{pmatrix}$, the corner $A_{00}$ receives $a_{11}b_{11}$ and the corner $A_{01}$ receives the three contributions $a_{11}b_{12}$, $a_{11}b_{22}$ and $a_{12}b_{22}$, while the corner $A_{11}$ receives $a_{22}b_{22}$. The example shows that the block formula is stable under the degeneration of a corner: the zero corner simply contributes no block.

### The biquaternion algebra

Let $\mathbb{B}=M_2(\mathbb{C})$ and let $e=E_{11}$, $f=E_{22}$. Under the matrix model, the four corners are the four complex lines of the Peirce decomposition, and the block matrix of $T_{a,b}$ is $a\otimes b^{\mathsf T}$ as in the matrix case. The biquaternion labels of the four lines, and the Peirce table in the biquaternion basis, are those of *The Peirce Decomposition of the Biquaternion Algebra*; the sandwich operators are the same operators in the two coordinates, and the Peirce projections are the elementary sandwiches of the two idempotents. The example is the matrix case of *The Sandwich Operator on an Algebra*, §*The Quaternion Algebra*, read on the Peirce basis.

## Summary

The Peirce decomposition $A=\bigoplus_{i,j}A_{ij}$ cuts the sandwich $T_{a,b}(x)=axb$ into sixteen blocks. The block from the source corner $A_{rs}$ to the target corner $A_{il}$ is $x\mapsto a_{ir}xb_{sl}$, a sandwich of the corner elements $a_{ir}$ and $b_{sl}$. A homogeneous $a\in A_{ij}$ and $b\in A_{kl}$ give a sandwich with a single block, from $A_{jk}$ to $A_{il}$; a diagonal $a,b$ give a block-diagonal sandwich that preserves each corner; a general sandwich is the sum of the elementary ones. The four elementary sandwiches $E_{ij}=T_{e_i,e_j}$ are the Peirce projections, and they form a complete family of pairwise orthogonal projections in $\operatorname{End}_k(A)$: $E_{ij}E_{kl}=\delta_{ik}\delta_{jl}E_{ij}$ and $\sum_{ij}E_{ij}=\mathrm{id}$. The composition law is $T_{a,b}T_{c,d}=T_{ac,db}$, the action of the enveloping algebra $A\otimes A^{\mathrm{op}}$; the sandwich space is its image, and the Peirce decomposition of $A$ writes it block by block. In the scalar case the block matrix is the Kronecker product $a\otimes b^{\mathsf T}$; in general it is the same pattern of blocks with operator entries. The matrix algebra $M_2(k)$, the split algebra $k\times k$, the upper triangular algebra and the biquaternion algebra are the worked examples. No form, involution or topology is used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e,f$ | idempotent and complement $f=1-e$ |
| $e_0,e_1$ | $e_0=e$, $e_1=f$ |
| $A_{ij}$ | the corner $e_iAe_j$ |
| $T_{a,b}$ | the sandwich $x\mapsto axb$ |
| $T_{(i,l),(r,s)}$ | the block $A_{rs}\to A_{il}$, $x\mapsto a_{ir}xb_{sl}$ |
| $E_{ij}$ | the Peirce projection $T_{e_i,e_j}$ |
| $\mathcal{S}(A)$ | the sandwich space, the image of $A\otimes A^{\mathrm{op}}\to\operatorname{End}_k(A)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the sandwich operators.
- Nathan Jacobson, *Basic Algebra II* (Freeman, 1989), for the enveloping algebra and the regular representations.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 1992), for the module-theoretic reading of the Peirce projections.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the matrix and biquaternion examples.
