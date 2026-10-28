# __The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners of $M_6(\mathbb{C})$__

## Introduction

A rank-$p$ idempotent $E$ cuts $M_6(\mathbb{C})$ into four corners. The diagonal corners are the matrix algebras $M_p$ and $M_{6-p}$, and their direct sum $M_p\oplus M_{6-p}$ is a subalgebra of $M_6$. Three values of $p$ give the three coarse splits of the algebra:

$$
\begin{array}{c|c|c}
p & \text{corners} & \text{diagonal algebra}\\ \hline
1 & 1+5+5+25 & \mathbb{C}\oplus M_5\\
2 & 4+8+8+16 & M_2\oplus M_4\\
3 & 9+9+9+9 & M_3\oplus M_3
\end{array}
$$

The case $p=3$ is the tensor-product recursion $M_6\cong M_3\otimes M_2$, with diagonal corner $M_3\oplus M_3=M_3\otimes\mathbb{C}^2$. The case $p=2$ is the Levi recursion $M_2\oplus M_4$, the diagonal part of the parabolic preserving a $2$-plane. Both live in the same algebra, and both carry a mass block: a square $3\times3$ block in the first case, a rectangular $2\times4$ block in the second.

The gauge of either corner is five-dimensional, split as

$$
\underbrace{2+2+1}_{p=3}=\underbrace{3+1+1}_{p=2}=5:
$$

the traceless torus of the first block, the traceless torus of the second block, and one relative scale.

The article assumes the coarse Peirce decomposition of *The Peirce Decomposition of $M_6(\mathbb{C})$* and the gauge of *The Frame, the Simple Nilpotents and the Gauge of $M_6(\mathbb{C})$*. It uses no form and no topology. The mass block is developed in *The Mass Block and the Chiral Polar Decomposition of $M_6(\mathbb{C})$*; the full flag and the parabolic are *The Adjoint Action, the Orbits and the Flag Variety of $M_6(\mathbb{C})$*.

## The Three Coarse Splits

### The Corner Dimensions

**Theorem.** Let $E\in M_6(\mathbb{C})$ be an idempotent of rank $p$, and $F=I_6-E$ its complement. Then

$$
M_6(\mathbb{C})=EME\oplus EMF\oplus FME\oplus FMF,
$$

with

$$
\dim EME=p^2,\quad
\dim EMF=p(6-p),\quad
\dim FME=(6-p)p,\quad
\dim FMF=(6-p)^2 .
$$

**Proof.** Choose coordinates in which $E=\operatorname{diag}(I_p,0)$ and $F=\operatorname{diag}(0,I_{6-p})$. The four corners are the four blocks of the block matrix, of sizes $p\times p$, $p\times(6-p)$, $(6-p)\times p$ and $(6-p)\times(6-p)$.

**Corollary.** The three ranks give

$$
p=1:\ 1+5+5+25=36,\qquad
p=2:\ 4+8+8+16=36,\qquad
p=3:\ 9+9+9+9=36 .
$$

**Proof.** Substitute $p=1,2,3$ in the formula.

### The Diagonal Corner Algebra

**Theorem.** The diagonal part

$$
D_E=EME\oplus FMF
$$

is a subalgebra of $M_6(\mathbb{C})$, isomorphic to $M_p(\mathbb{C})\oplus M_{6-p}(\mathbb{C})$, of dimension

$$
p^2+(6-p)^2 .
$$

**Proof.** A product of two block-diagonal matrices is block diagonal, and the blocks multiply separately. The corner $EME$ is the full endomorphism algebra of the image of $E$, a $p$-dimensional space, hence is $M_p$; the corner $FMF$ is the endomorphism algebra of the image of $F$, of dimension $6-p$, hence is $M_{6-p}$.

**Remark (the whole algebra is not the direct sum).** The four corners are a direct sum of vector spaces, but only the diagonal part is a subalgebra: the mixed corners $EMF$ and $FME$ are not closed under multiplication. The algebra $M_6$ is an extension of the diagonal algebra by the mixed blocks, not a direct product.

### The Block Matrices

In the coordinates of the theorem, an element is

$$
A=\begin{pmatrix}A_{11}&M\\N&A_{22}\end{pmatrix},
\qquad
A_{11}\in M_p,\quad M\in\mathbb{C}^{p\times(6-p)},\quad N\in\mathbb{C}^{(6-p)\times p},\quad A_{22}\in M_{6-p},
$$

and the product is

$$
\begin{pmatrix}A_{11}&M\\N&A_{22}\end{pmatrix}
\begin{pmatrix}A_{11}'&M'\\N'&A_{22}'\end{pmatrix}
=
\begin{pmatrix}
A_{11}A_{11}'+MN' & A_{11}M'+MA_{22}'\\
NA_{11}'+A_{22}N' & NM'+A_{22}A_{22}'
\end{pmatrix}.
$$

**Definition.** The off-diagonal block $M$ is the **mass block** of the split, and $N$ is its partner. The block $M$ maps the complement into the corner, and $N$ maps the corner into the complement.

**Proposition (the trace and the determinant).** For the block matrix above,

$$
\operatorname{tr}A=\operatorname{tr}A_{11}+\operatorname{tr}A_{22},
\qquad
\det A=\det A_{11}\det A_{22}
$$

when $M=N=0$, and in general

$$
\det A=\det A_{22}\det\left(A_{11}-MA_{22}^{-1}N\right)
$$

when $A_{22}$ is invertible.

**Proof.** The trace is the sum of the diagonal entries of the two diagonal blocks. For the determinant, factor

$$
\begin{pmatrix}A_{11}&M\\N&A_{22}\end{pmatrix}
=
\begin{pmatrix}I_p&M\\0&A_{22}\end{pmatrix}
\begin{pmatrix}A_{11}-MA_{22}^{-1}N&0\\A_{22}^{-1}N&I_{6-p}\end{pmatrix},
$$

and take determinants; the two triangular factors have determinant $\det A_{22}$ and $1$.

The Schur complement $A_{11}-MA_{22}^{-1}N$ is the effective block seen after eliminating the second corner; the mass block enters quadratically.

## The Rank-Two Split: $M_2\oplus M_4$

### The Corners

Take $p=2$, $E=\operatorname{diag}(I_2,0_4)$, $F=\operatorname{diag}(0_2,I_4)$. The corners are

$$
EME\cong M_2,\qquad
FMF\cong M_4,\qquad
EMF\cong\mathbb{C}^{2\times4},\qquad
FME\cong\mathbb{C}^{4\times2},
$$

of dimensions $4,16,8,8$. The block matrix is

$$
A=\begin{pmatrix}A_2&M\\N&B_4\end{pmatrix},
\qquad
A_2\in M_2,\quad M\in\mathbb{C}^{2\times4},\quad N\in\mathbb{C}^{4\times2},\quad B_4\in M_4,
$$

and the mass block $M$ is **rectangular**, of size $2\times4$.

**Proposition.** The diagonal corner algebra is $M_2\oplus M_4$, of dimension $20$. The block upper triangular subalgebra

$$
\mathfrak{p}=\left\{\begin{pmatrix}A_2&M\\0&B_4\end{pmatrix}\right\}
$$

has dimension $4+8+16=28$ and is the parabolic subalgebra of $\mathfrak{gl}_6$ preserving the flag $0\subset\mathbb{C}^2\subset\mathbb{C}^6$. Its Levi factor is $M_2\oplus M_4$, and its nilpotent radical is the mass block $\mathbb{C}^{2\times4}$.

**Proof.** The dimensions are $4+8+16=28$ and $4+16=20$. The parabolic is the stabiliser of the $2$-plane $\mathbb{C}^2\oplus0$; the Levi factor is the block-diagonal part, and the radical is the strictly upper-right block.

### The Mass Block

**Proposition.** A $2\times4$ mass block has rank at most two. Its singular values are two nonnegative numbers $\sigma_1\ge\sigma_2\ge0$, and its polar decomposition is

$$
M=U\Sigma V^*,
\qquad
U\in U(2),\quad V\in U(4),\quad
\Sigma=\begin{pmatrix}\sigma_1&0&0&0\\0&\sigma_2&0&0\end{pmatrix}.
$$

**Proof.** The rank of a $2\times4$ matrix is at most $2$, so its singular value decomposition has at most two nonzero singular values; the $*$-unitary groups act on the two sides.

**Corollary (the mass has two channels).** The rank-two split has two mass channels, the two singular values of $M$. The rank-three split has three, and the rank-one split has one.

**Proof.** The number of singular values is $\min(p,6-p)$, which is $1,2,3$ for $p=1,2,3$.

### The Gauge of the Rank-Two Corner

**Proposition.** The gauge of the corner is

$$
T_{2,4}=\left(\mathbb{C}^\times\right)^2\times\left(\mathbb{C}^\times\right)^4/\mathbb{C}^\times
\cong\left(\mathbb{C}^\times\right)^5,
$$

and it splits as the traceless torus of $M_2$ (dimension $1$), the traceless torus of $M_4$ (dimension $3$), and the relative scale (dimension $1$):

$$
1+3+1=5 .
$$

**Proof.** Write a diagonal gauge as $\operatorname{diag}(t_1,t_2,s_1,s_2,s_3,s_4)$. The overall scalar $(t,t,t,t,t,t)$ is quotiented out. The traceless part of the first block is the single ratio $t_1/t_2$; the traceless part of the second is the three ratios $s_1/s_2,s_2/s_3,s_3/s_4$; the remaining parameter is the relative scale $t/s$, where $t$ is the common scale of the first block and $s$ of the second. The dimensions add to $1+3+1=5$.

**Corollary (the action on the mass block).** Under the scalar part of the gauge, the mass block is multiplied by the relative scale:

$$
M\longmapsto\frac{t}{s}M .
$$

**Proof.** The gauge matrix is $\operatorname{diag}(tI_2,sI_4)$; conjugation sends the block $M$ to $tMs^{-1}=(t/s)M$.

## The Rank-Three Split: $M_3\oplus M_3$

### The Corners

Take $p=3$, $E=\operatorname{diag}(I_3,0_3)$, $F=\operatorname{diag}(0_3,I_3)$. The four corners are

$$
EME\cong M_3,\qquad
FMF\cong M_3,\qquad
EMF\cong M_3,\qquad
FME\cong M_3,
$$

all of dimension $9$. The block matrix is

$$
A=\begin{pmatrix}A_+&M\\N&A_-\end{pmatrix},
\qquad
A_+,A_-,M,N\in M_3,
$$

and the mass block $M$ is **square**, of size $3\times3$.

**Theorem (the tensor-product recursion).**

$$
M_6(\mathbb{C})\cong M_3(\mathbb{C})\otimes M_2(\mathbb{C})
\cong M_2(M_3(\mathbb{C})),
$$

and under this isomorphism the block form is the $2\times2$ matrix of $3\times3$ blocks. The diagonal corner is

$$
M_3\oplus M_3\cong M_3\otimes\mathbb{C}^2,
$$

where $\mathbb{C}^2$ is the algebra of diagonal $2\times2$ matrices.

**Proof.** The algebra $M_2(M_3)$ of $2\times2$ matrices with entries in $M_3$ is $M_2\otimes M_3$ by $E_{ab}\otimes A\mapsto$ the matrix with $A$ in block $(a,b)$. The identification $M_2(M_3)\cong M_6$ is the block form: a $2\times2$ matrix of $3\times3$ blocks has $36$ entries. The block-diagonal matrices are the elements with the off-diagonal blocks zero, and they form $M_3\oplus M_3$.

**Corollary (the two commuting factors).** The subalgebras

$$
M_3\otimes I_2=\left\{\begin{pmatrix}A&0\\0&A\end{pmatrix}:A\in M_3\right\},
\qquad
I_3\otimes M_2=\left\{\begin{pmatrix}\lambda I_3&\mu I_3\\\nu I_3&\rho I_3\end{pmatrix}\right\}
$$

commute, and together they generate $M_6$.

**Proof.** $(A\otimes I_2)(I_3\otimes B)=A\otimes B=(I_3\otimes B)(A\otimes I_2)$. The tensor product is generated by the two factors.

**Remark (the recursion is a tensor product only for equal blocks).** The rank-two split is not a tensor product: $M_2(M_4)$ would be $M_8$, not $M_6$. The rank-three split is special because $p=6-p=3$, so the mixed blocks are square and of the same size as the diagonal ones. **The $M_3\oplus M_3$ recursion is the tensor product $M_3\otimes M_2$; the $M_2\oplus M_4$ recursion is a Levi factor, not a tensor product.**

### The Mass Block

**Proposition.** A $3\times3$ mass block has three singular values $\sigma_1\ge\sigma_2\ge\sigma_3\ge0$, and its polar decomposition is

$$
M=U\Sigma V^*,
\qquad
U,V\in U(3),\quad
\Sigma=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3).
$$

**Proof.** The singular value decomposition of a square matrix.

**Corollary (the mass has three channels).** The rank-three split has three mass channels, and the relative scale of the gauge multiplies all three singular values by the same factor.

**Proof.** The singular values of $(t/s)M$ are $\lvert t/s\rvert\sigma_i$.

### The Gauge of the Rank-Three Corner

**Proposition.** The gauge of the corner splits as

$$
2+2+1=5:
$$

the traceless torus of the first $M_3$ (dimension $2$), the traceless torus of the second $M_3$ (dimension $2$), and the relative scale (dimension $1$).

**Proof.** A diagonal gauge is $\operatorname{diag}(t_1,t_2,t_3,s_1,s_2,s_3)$; the overall scalar is quotiented out; the traceless ratios are $t_1/t_2,t_2/t_3$ and $s_1/s_2,s_2/s_3$; the relative scale is $t/s$.

## The Gauge of the Two Corners

### The Three Terms

**Theorem.** For every rank $p$, the gauge of the corner algebra $M_p\oplus M_{6-p}$ decomposes as

$$
\underbrace{(p-1)}_{\text{first corner}}
+\underbrace{(5-p)}_{\text{second corner}}
+\underbrace{1}_{\text{relative scale}}
=5 .
$$

**Proof.** The diagonal torus of $M_p$ has dimension $p$, and its traceless part has dimension $p-1$; the torus of $M_{6-p}$ has dimension $6-p$, and its traceless part has dimension $5-p$. The two common scales are one overall scale, quotiented out, and one relative scale. The sum is $(p-1)+(5-p)+1=5$.

**Corollary.** The three splits give

$$
p=1:\ 0+4+1=5,\qquad
p=2:\ 1+3+1=5,\qquad
p=3:\ 2+2+1=5 .
$$

### The Corner Tori and the Relative Scale

**Definition.** The **corner tori** of the split are the traceless diagonal tori

$$
T_p=\left\{\operatorname{diag}(t_1,\dots,t_p):\prod t_i=1\right\},
\qquad
T_{6-p}=\left\{\operatorname{diag}(s_1,\dots,s_{6-p}):\prod s_j=1\right\},
$$

of dimensions $p-1$ and $5-p$. The **relative scale** is the class of

$$
\operatorname{diag}(tI_p,sI_{6-p}),\qquad t,s\in\mathbb{C}^\times,
$$

modulo the overall scalar; it is parameterised by $t/s\in\mathbb{C}^\times$ and is one-dimensional.

**Proposition.** The gauge torus is the direct product

$$
T\cong T_p\times T_{6-p}\times\mathbb{C}^\times_{\text{rel}},
$$

of dimension $(p-1)+(5-p)+1=5$.

**Proof.** A diagonal gauge has $p+(6-p)=6$ parameters. Divide by the overall scalar, which is the diagonal $(t,\dots,t)$, and split the remaining five into the traceless parts of the two blocks and the ratio of their common scales.

**Remark (why the relative scale is not in either corner).** The traceless tori act inside one block and fix the other. The relative scale acts on both blocks at once, with opposite signs in the logarithms, and it is the only gauge direction that multiplies the mass block. **The relative scale is the gauge direction of the mass block.**

## The Block Embeddings

### The Smaller Algebras Inside $M_6$

**Definition.** For $k=1,\dots,5$ let $E_k=\operatorname{diag}(I_k,0_{6-k})$. The **corner embedding** of $M_k$ is

$$
\iota_k:M_k(\mathbb{C})\longrightarrow M_6(\mathbb{C}),
\qquad
\iota_k(A)=\begin{pmatrix}A&0\\0&0\end{pmatrix}=E_kAE_k .
$$

The **unital embedding** is

$$
\widehat\iota_k(A)=\begin{pmatrix}A&0\\0&I_{6-k}\end{pmatrix}.
$$

**Proposition.** $\iota_k$ is an injective algebra homomorphism with unit $E_k$; $\widehat\iota_k$ is an injective unital algebra homomorphism with unit $I_6$. On the images,

$$
\operatorname{tr}_{M_6}\iota_k(A)=\operatorname{tr}_{M_k}A,
\qquad
\det\widehat\iota_k(A)=\det_{M_k}A,
\qquad
\det\iota_k(A)=0\ \text{for }k<6 .
$$

**Proof.** The block products are the products of the blocks. The trace of $\iota_k(A)$ is the trace of $A$ plus $6-k$ zeros. The determinant of the unital embedding is the product of $\det A$ and $\det I_{6-k}=1$; the corner embedding has a zero block, so its determinant vanishes.

**Corollary (the chain of categories).** The unital embeddings give a chain

$$
M_1\subset M_2\subset M_3\subset M_4\subset M_5\subset M_6,
$$

and the corner embeddings give, for each $k$, the algebra $M_k$ as the corner $E_kM_6E_k$.

**Remark (the previous categories).** The algebra $M_2$ is the biquaternion algebra of the previous category; $M_3,M_4,M_5$ are the algebras of their categories. Each is read inside $M_6$ in two ways: as a corner $E_kM_6E_k$ (nonunital, trace-preserving on its own trace) and as a unital block (determinant-preserving). **The corner reading keeps the trace; the unital reading keeps the determinant.**

### The Mixed Blocks as Bimodules

**Proposition.** The mixed corner $EMF$ is a left module over $EME\cong M_p$ and a right module over $FMF\cong M_{6-p}$, and it is isomorphic to the bimodule $\mathbb{C}^{p}\otimes(\mathbb{C}^{6-p})^*$ of $p\times(6-p)$ matrices. The corner $FME$ is the dual bimodule.

**Proof.** $A_{11}MN'$ and $M B_{22}$ are the left and right actions; the dimensions match, and the isomorphism is $u\otimes\varphi\mapsto u\varphi$.

**Corollary (the mass block is a bimodule element).** The mass block $M$ is not an element of either corner algebra; it is an element of the mixed bimodule. The gauge acts on it by the relative scale, and the corner unitaries act on it by left and right multiplication.

### The Two Recursions

**Theorem (the two recursions in one algebra).** The same algebra $M_6(\mathbb{C})$ contains the two diagonal corner algebras

$$
M_3\oplus M_3\cong M_3\otimes\mathbb{C}^2,
\qquad
M_2\oplus M_4,
$$

of dimensions $18$ and $20$. The first is a tensor-product factor of $M_6\cong M_3\otimes M_2$; the second is the Levi factor of the parabolic preserving a $2$-plane.

**Proof.** The first is the block-diagonal part of the $3+3$ split, and $M_6\cong M_2(M_3)\cong M_2\otimes M_3$. The second is the block-diagonal part of the $2+4$ split, and the block upper triangular matrices form the parabolic of the flag $0\subset\mathbb{C}^2\subset\mathbb{C}^6$.

**Corollary (the two mass blocks).** The $3+3$ split has the square mass block $M\in M_3$ with three singular values; the $2+4$ split has the rectangular mass block $M\in\mathbb{C}^{2\times4}$ with two singular values.

**Proof.** The number of singular values is $\min(p,6-p)$, which is $3$ at $p=3$ and $2$ at $p=2$.

**Remark (the massless limits).** If the mass block vanishes in the $3+3$ split, the algebra element is block diagonal and lies in $M_3\oplus M_3$. If it vanishes in the $2+4$ split, the element lies in $M_2\oplus M_4$. In both cases the massless elements form the diagonal corner algebra, of dimension $18$ or $20$; the mass block adds the remaining $18$ or $16$ dimensions.

## Summary

The three coarse splits of $M_6(\mathbb{C})$ by an idempotent of rank $p=1,2,3$ have corners

$$
1+5+5+25,\qquad
4+8+8+16,\qquad
9+9+9+9 .
$$

The diagonal corners are the algebras

$$
\mathbb{C}\oplus M_5,\qquad
M_2\oplus M_4,\qquad
M_3\oplus M_3,
$$

of dimensions $26,20,18$. The mixed corner $EMF$ is the mass block: a $1\times5$, a rectangular $2\times4$, or a square $3\times3$ matrix, with one, two or three singular values.

$$
\boxed{\ M_6\cong M_3\otimes M_2\ \text{contains}\ M_3\oplus M_3;\quad
M_6\ \text{contains the Levi factor}\ M_2\oplus M_4 .\ }
$$

The gauge of every corner splits as

$$
(p-1)+(5-p)+1=5,
$$

the two traceless corner tori and the relative scale. The relative scale is the gauge direction of the mass block.

| Split | Corners | Diagonal algebra | Dimension | Mass block | Singular values |
|---|---|---|---|---|---|
| $p=1$ | $1+5+5+25$ | $\mathbb{C}\oplus M_5$ | $26$ | $1\times5$ | $1$ |
| $p=2$ | $4+8+8+16$ | $M_2\oplus M_4$ | $20$ | $2\times4$ | $2$ |
| $p=3$ | $9+9+9+9$ | $M_3\oplus M_3$ | $18$ | $3\times3$ | $3$ |

| Gauge split | $p=1$ | $p=2$ | $p=3$ |
|---|---|---|---|
| first corner | $0$ | $1$ | $2$ |
| second corner | $4$ | $3$ | $2$ |
| relative scale | $1$ | $1$ | $1$ |
| total | $5$ | $5$ | $5$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E,F=I_6-E$ | an idempotent of rank $p$ and its complement |
| $EME,EMF,FME,FMF$ | the four corners |
| $D_E=EME\oplus FMF$ | the diagonal corner algebra |
| $M$ | the mass block $EMF$ |
| $N$ | the transpose mass block $FME$ |
| $T_p,T_{6-p}$ | the traceless corner tori, of dimensions $p-1$ and $5-p$ |
| $t/s$ | the relative scale |
| $\iota_k,\widehat\iota_k$ | the corner and unital embeddings of $M_k$ |

## Further Reading

- [The Peirce Decomposition of $M_6(\mathbb{C})$](the-peirce-decomposition-of-m6c.html), for the four corners and the corner multiplication.
- [The Frame, the Simple Nilpotents and the Gauge of $M_6(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m6c.html), for the five-dimensional gauge.
- [The Mass Block and the Chiral Polar Decomposition of $M_6(\mathbb{C})$](the-mass-block-and-the-chiral-polar-decomposition-of-m6c.html), for the polar decomposition of the mass block.
- [The Two Chiralities of $M_6(\mathbb{C})$](the-two-chiralities-of-m6c.html), for the $3+3$ split of the carrier.
- [The Rank-Two and Rank-Three Splits of $M_6(\mathbb{C})$](the-rank-two-and-rank-three-splits-of-m6c.html), for the idempotent geometry of the two ranks.
- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the trace, the determinant and the block multiplication.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the $3\times3$ block.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the $4\times4$ block.
- [Flag Manifolds](flag-manifolds.html), for the Levi factors and the radicals.
