# __The Exponential Polar Decomposition__

## Introduction

Every invertible $A\in M_6(\mathbb{C})$ factors as

$$
A=e^H e^{\mathrm iK},
\qquad
H,K\in\operatorname{Herm}_6,
$$

the **exponential polar decomposition**. It is the left polar decomposition

$$
A=P'U',
\qquad
P'=(AA^*)^{1/2}>0,\quad
U'=P'^{-1}A,
$$

written in exponential form: $P'=e^H$ with $H=\log P'$, and $U'=e^{\mathrm iK}$ with $K$ a Hermitian logarithm of the $*$-unitary factor. The Hermitian factor $H$ is unique; the $*$-unitary factor is unique, and $K$ is unique modulo $2\pi$ on each eigenspace.

The decomposition is different from the right polar decomposition $A=UP=e^{\mathrm iK'}e^{H'}$: the two share the $*$-unitary factor, and their positive factors are conjugate by it. They coincide exactly when $A$ is normal, equivalently when $[H,K]=0$.

The exponential polar decomposition exists exactly on $GL_6$: both factors are invertible, so a singular matrix has no such factorisation. The polar decomposition with a partial isometry survives on the singular set, and the Hermitian factor diverges logarithmically at the boundary.

The article assumes the polar decomposition of *The Polar Decomposition*, the exponential of *The Exponential and the Lie Group*, and the chiral split of *The Two Chiralities*. The comparison with the rank-two case is *The Exponential Polar Decomposition of $M_4(\mathbb{C})$*; the mass block is *The Mass Block and the Chiral Polar Decomposition*.

## The Left Polar Decomposition

### Definition

**Theorem (the left polar decomposition).** Every invertible $A\in M_6(\mathbb{C})$ has a unique factorization

$$
A=P'U',
$$

with $P'$ positive definite Hermitian and $U'$ $*$-unitary:

$$
P'=(AA^*)^{1/2},\qquad
U'=P'^{-1}A.
$$

**Proof.** $AA^*$ is positive definite, so $P'$ is positive definite and invertible. Set $U'=P'^{-1}A$. Then

$$
U'^*U'=A^*P'^{-2}A=A^*(AA^*)^{-1}A=I_6,
$$

so $U'$ is $*$-unitary. Uniqueness: $P'^2=AA^*$ forces $P'=(AA^*)^{1/2}$, and then $U'=P'^{-1}A$.

**Corollary (the two polars).** The same $A$ has the right polar decomposition

$$
A=UP,
\qquad
P=(A^*A)^{1/2},\qquad
U=AP^{-1}.
$$

The $*$-unitary factors agree, $U'=U$, and the positive factors are conjugate, $P'=UPU^*$.

**Proof.** From $A=UP$, $AA^*=UP^2U^*$, so $P'=UPU^*$ and $U'=P'^{-1}A=UP^{-1}U^*UP=U$.

### The Exponential Form

**Theorem.** Every positive definite $P'$ has a unique Hermitian logarithm

$$
P'=e^H,
\qquad
H=\log P'\in\operatorname{Herm}_6,
$$

and every $*$-unitary $U'$ has a Hermitian logarithm

$$
U'=e^{\mathrm iK},
\qquad
K\in\operatorname{Herm}_6,
$$

unique modulo $2\pi$ on each eigenspace.

**Proof.** The spectral theorem for $P'>0$ gives $P'=V\operatorname{diag}(p_i)V^*$ with $p_i>0$; then $H=V\operatorname{diag}(\log p_i)V^*$. For $U'$, diagonalize unitarily with eigenvalues $e^{\mathrm i\theta_j}$; then $K=V\operatorname{diag}(\theta_j)V^*$, and the angles are determined modulo $2\pi$.

**Corollary (the exponential polar decomposition).** Every invertible $A$ has

$$
A=e^He^{\mathrm iK},
\qquad
H=\log P',\quad
K=\log U' .
$$

**Proof.** Substitute $P'=e^H$ and $U'=e^{\mathrm iK}$ in $A=P'U'$.

**Corollary (the right exponential form).** Every invertible $A$ also has

$$
A=e^{\mathrm iK'}e^{H'},
\qquad
H'=\log P,\quad
K'=\log U,
$$

with $P=(A^*A)^{1/2}$ and $U=AP^{-1}$.

**Proof.** Apply the exponential form to the right polar decomposition.

### The Two Orders

**Theorem.** The left and right exponential forms are related by

$$
e^H e^{\mathrm iK}=e^{\mathrm iK}e^{H'},
\qquad
H'=e^{-\mathrm iK}He^{\mathrm iK},
\qquad
K'\equiv K\pmod{2\pi}.
$$

The $*$-unitary factors agree, $e^{\mathrm iK'}=e^{\mathrm iK}=U$, and the Hermitian factors are conjugate, $H'=U^*HU$.

**Proof.** The right polar is $A=UP$ with $P=U^*P'U$; hence $H'=U^*HU$ and $K'=K$ (modulo $2\pi$). The left form is $A=e^He^{\mathrm iK}$; the right form is $A=e^{\mathrm iK}e^{H'}$.

**Corollary (the normal case).** The two orderings coincide if and only if $A$ is normal, equivalently $[H,K]=0$.

**Proof.** If $A$ is normal, $P'=P$ and $H'=H$, so the two forms are $e^He^{\mathrm iK}=e^{\mathrm iK}e^H$; the factors commute. Conversely, if they commute, $A=e^{H+\mathrm iK}$ is normal.

**Corollary (the spectral form).** For a normal $A$, there is a $*$-unitary $V$ and real diagonal $h,\theta$ with

$$
A=Ve^{h}e^{\mathrm i\theta}V^*,
\qquad
H=VhV^*,\quad
K=V\theta V^* .
$$

**Proof.** Diagonalize the normal $A$ unitarily; the eigenvalues are $e^{h_j+\mathrm i\theta_j}$.

## The Uniqueness

### The Hermitian Factor

**Theorem.** The Hermitian factor $H=\log P'$ is unique.

**Proof.** $P'=(AA^*)^{1/2}$ is unique, and the positive definite logarithm is unique.

### The $*$-Unitary Factor

**Theorem.** The $*$-unitary factor $U'$ is unique. The Hermitian exponent $K$ is unique modulo $2\pi$: if $e^{\mathrm iK}=e^{\mathrm iK'}=U'$, then $K-K'$ has eigenvalues in $2\pi\mathbb{Z}$ on the eigenspaces of $U'$.

**Proof.** The $*$-unitary factor is $U'=P'^{-1}A$; the logarithm of a $*$-unitary is unique modulo $2\pi$ on each eigenspace.

**Corollary (the principal exponent).** There is a unique $K$ with spectrum in $(-\pi,\pi]$; it is the principal Hermitian logarithm of $U'$.

**Proof.** Choose the principal argument of each eigenvalue.

### The Count

**Theorem.** The exponential polar map

$$
\operatorname{Herm}_6\times\operatorname{Herm}_6\longrightarrow GL_6,
\qquad
(H,K)\longmapsto e^He^{\mathrm iK},
$$

is surjective, and its fibres are the sets of $(H,K+2\pi Z)$ with $Z$ Hermitian commuting with $K$ and with spectrum in $\mathbb{Z}$.

**Proof.** The polar decomposition and the two logarithms give the surjectivity; the fibre is the ambiguity of the Hermitian logarithm of $U'$.

**Corollary (the dimensions).**

$$
\dim_{\mathbb{R}}\operatorname{Herm}_6=36,
\qquad
\dim_{\mathbb{R}}GL_6=72=36+36 .
$$

**Proof.** A Hermitian matrix has $36$ real parameters; the two Hermitian factors give $72$, matching $GL_6$.

**Remark (the global structure).** The map $(H,K)\mapsto e^He^{\mathrm iK}$ is surjective but not injective: the periodicity $K\mapsto K+2\pi Z$ gives the same $*$-unitary factor whenever $Z$ commutes with $K$.

## The Reach on the Singular Elements

### The Invertible Locus

**Theorem.** The exponential polar decomposition exists exactly on $GL_6$.

**Proof.** $e^H$ is positive definite, hence invertible; $e^{\mathrm iK}$ is $*$-unitary, hence invertible; their product is invertible. Conversely, every invertible matrix has the decomposition.

**Corollary (the singular elements).** A singular $A$ has no factorization $A=e^He^{\mathrm iK}$ with $H,K$ Hermitian.

**Proof.** The product of two invertible matrices is invertible.

### The Limit

**Theorem.** Let $A(t)$ be a smooth family of invertible matrices with $A(0)$ singular of rank $k<6$. Then the positive factor $P'(t)$ tends to the singular $P'(0)$, the Hermitian factor $H(t)=\log P'(t)$ diverges: its eigenvalues tend to $-\infty$ in the kernel directions. The $*$-unitary factor may have a limit, and when it does, the limit depends on the direction of approach.

**Proof.** The positive factor is continuous; the logarithm of a positive eigenvalue tending to zero tends to $-\infty$. The $*$-unitary factor is the partial isometry of the singular polar decomposition, and its extension on the kernel is the free choice.

**Corollary (the singular values).** The singular values of $A$ are $e^{h_j}$, where $h_j$ are the eigenvalues of $H$; at a zero singular value the logarithm diverges.

**Proof.** The eigenvalues of $P'=e^H$ are $e^{h_j}$; the singular values are the eigenvalues of $P'$.

### The Polar Decomposition Survives

**Theorem.** Every singular $A$ has a polar decomposition $A=UP$ with $P\ge0$ and $U$ a partial isometry; the positive factor is unique, and the partial isometry is free on the kernel.

**Proof.** This is *The Polar Decomposition*; the exponential form requires $P>0$, which fails at the singular set, but the positive semidefinite form and the partial isometry survive.

**Corollary (the two reaches).** The exponential polar decomposition reaches $GL_6$; the polar decomposition with a partial isometry reaches all of $M_6$.

**Proof.** The first is the invertibility of the factors; the second is the existence theorem for the semidefinite polar decomposition.

**Remark (the boundary).** The exponential polar decomposition degenerates at the singular set: the Hermitian factor escapes to infinity, and the $*$-unitary factor loses its uniqueness. **The singular set is the boundary of the exponential polar chart.**

## The Comparison with the Split Case

### The Chiral Split

**Definition.** In the chiral split $\mathbb{C}^6=V_+\oplus V_-$, with $\dim V_\pm=3$, an element is

$$
A=\begin{pmatrix}A_{++}&A_{+-}\\A_{-+}&A_{--}\end{pmatrix},
\qquad
A_{\pm\pm}\in M_3(\mathbb{C}).
$$

The **mass block** is $M=A_{+-}\in M_3(\mathbb{C})$.

**Theorem (the chiral decomposition).** The mass block has the singular value decomposition

$$
M=U_L\Sigma U_R^*,
\qquad
U_L,U_R\in U(3),\quad
\Sigma=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)\ge0 .
$$

**Proof.** The SVD of a $3\times3$ matrix; the singular values are the square roots of the eigenvalues of $M^*M$.

**Corollary (the two decompositions).** The full exponential polar decomposition is the Cartan decomposition of $GL_6$,

$$
A=e^He^{\mathrm iK},
\qquad
H,K\in\operatorname{Herm}_6,
$$

while the chiral decomposition is the SVD of the mass block,

$$
M=U_L\Sigma U_R^*,
\qquad
U_L,U_R\in U(3).
$$

They answer different questions: the first separates the scale and the phase of the full $6\times6$ matrix; the second separates the two chiral gauges of the $3\times3$ block.

**Proof.** The first is the polar decomposition of $A$; the second is the SVD of $M$.

### The Dimensions

**Theorem.** The dimensions are

$$
\dim_{\mathbb{R}}GL_6=72,
\qquad
\dim_{\mathbb{R}}\operatorname{Herm}_6=36,
\qquad
\dim_{\mathbb{R}}M_3(\mathbb{C})=18,
\qquad
\dim_{\mathbb{R}}U(3)\times U(3)=18 .
$$

**Proof.** $6^2=36$ complex, $72$ real; Hermitian $36$ real; $M_3$ has $9$ complex, $18$ real; $U(3)$ has $9$ real, the product $18$.

**Corollary (the two gauge groups).** The full exponential polar has the unitary gauge $U(6)$ of dimension $36$; the chiral decomposition has the gauge $U(3)\times U(3)$ of dimension $18$, the stabilizer of the chiral split.

**Proof.** The polar $*$-unitary factor ranges over $U(6)$; the chiral SVD uses the two unitaries of the two chiral planes.

### The Biquaternion Comparison

**Theorem (the biquaternion case).** For $M_2(\mathbb{C})\cong\mathbb{B}$, the same theorem holds: every invertible $A$ has $A=e^He^{\mathrm iK}$ with $H,K\in\operatorname{Herm}_2$; the left polar is $A=P'U'$ with $P'=(AA^*)^{1/2}$; the reach is $GL_2$, and the singular elements are the zero divisors.

**Proof.** The dimension is $2$ instead of $6$; the proof is identical.

**Corollary (the family).** The exponential polar decomposition is the same theorem for every $n$; the $M_6$ case has the $3+3$ chiral split and the $3\times3$ mass block, the $M_4$ case the $2+2$ split and the $2\times2$ block, and the $M_2$ case the $1+1$ split of the biquaternion.

**Proof.** The polar decomposition and the matrix logarithm are dimension-independent.

**Remark (the split case).** The **split case** is the chiral split $3+3$: the two chiral halves are the eigenspaces of $\Gamma$, the mass block is the off-diagonal $3\times3$ block, and the chiral gauge is $U(3)\times U(3)$. The full exponential polar decomposition does not see the split; the chiral decomposition sees only the mass block. **The two decompositions are the global Cartan decomposition and the block SVD; they coexist and are not the same.**

## Summary

Every invertible $A\in M_6(\mathbb{C})$ has the exponential polar decomposition

$$
A=e^He^{\mathrm iK},
\qquad
H,K\in\operatorname{Herm}_6,
$$

with $H=\log P'$ unique and $K$ unique modulo $2\pi$. It is the left polar decomposition $A=P'U'$, $P'=(AA^*)^{1/2}$, $U'=P'^{-1}A$, in exponential form. The right polar decomposition $A=UP$ shares the $*$-unitary factor, and the positive factors are conjugate, $P'=UPU^*$. The two orderings coincide exactly when $A$ is normal.

$$
\boxed{\ A=e^He^{\mathrm iK},\quad H=\log P',\quad U'=e^{\mathrm iK},\quad A\in GL_6 .\ }
$$

The decomposition exists exactly on $GL_6$; at the singular set the Hermitian factor diverges, the $*$-unitary factor loses its uniqueness, and the polar decomposition with a partial isometry survives.

In the $3+3$ chiral split the mass block $M=A_{+-}\in M_3(\mathbb{C})$ has the SVD $M=U_L\Sigma U_R^*$ with $U_L,U_R\in U(3)$; this is the block decomposition, not the full exponential polar decomposition. The $n=2$ case is the biquaternion algebra $M_2(\mathbb{C})$.

| Object | Data |
|---|---|
| Exponential polar | $A=e^He^{\mathrm iK}$, $H,K$ Hermitian |
| Left polar | $A=P'U'$, $P'=(AA^*)^{1/2}$ |
| Right polar | $A=UP$, $P=(A^*A)^{1/2}$ |
| Uniqueness | $H$ unique, $K$ mod $2\pi$ |
| Reach | $GL_6$ |
| Singular set | no exponential polar; Hermitian factor diverges |
| Chiral split | $3+3$; mass block $3\times3$ |
| Chiral gauge | $U(3)\times U(3)$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P'=(AA^*)^{1/2}$ | the left positive factor |
| $U'=P'^{-1}A$ | the left $*$-unitary factor |
| $H=\log P'$ | the Hermitian exponent of the scale |
| $K=\log U'$ | the Hermitian exponent of the phase |
| $M=A_{+-}$ | the mass block in the $3+3$ split |
| $U_L,U_R$ | the chiral unitaries |

## Further Reading

- [The Polar Decomposition](the-polar-decomposition-of-m6c.html), for the right polar decomposition and the singular case.
- [The Exponential and the Lie Group](the-exponential-and-the-lie-group-of-m6c.html), for the matrix logarithm and the one-parameter subgroups.
- [The Mass Block and the Chiral Polar Decomposition](the-mass-block-and-the-chiral-polar-decomposition-of-m6c.html), for the chiral decomposition of the $3\times3$ block.
- [The Two Chiralities](the-two-chiralities-of-m6c.html), for the $3+3$ split and the chirality involution.
- [The Exponential Polar Decomposition of $M_4(\mathbb{C})$](the-exponential-polar-decomposition-of-m4c.html), for the $2+2$ split and the $2\times2$ mass block.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), for the regular case.
- [The Cartan Decomposition and the Cartan Involution](the-cartan-decomposition-and-the-cartan-involution.html), for the symmetric space and the exponential polar form.
