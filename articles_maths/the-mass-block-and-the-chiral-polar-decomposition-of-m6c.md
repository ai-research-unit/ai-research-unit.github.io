# __The Mass Block and the Chiral Polar Decomposition__

## Introduction

In the $3+3$ chiral split the only coupling between the two halves is the off-diagonal block

$$
M=A_{+-}\in\operatorname{Hom}(V_-,V_+)\cong M_3(\mathbb{C}),
$$

the **mass block**. The chiral unitaries act on it by

$$
M\longmapsto U_LMU_R^{-1},
\qquad
U_L,U_R\in U(3),
$$

and the orbits are classified by the three singular values

$$
\sigma_1\ge\sigma_2\ge\sigma_3\ge0 .
$$

The mass block has a polar decomposition $M=U_L\Sigma U_R^{-1}$ with $\Sigma=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)$. The full element $A\in GL_6(\mathbb{C})$ has its own polar decomposition $A=UP$ with $U\in U(6)$ and $P$ positive definite; the two polar decompositions are different, and the article keeps them apart.

The article assumes the chiral split of *The Two Chiralities* and the rank-three corners of *The Rank-Two and Rank-Three Splits*. It uses no topology beyond the $*$-unitary groups. The polar decomposition of the full algebra is *The Polar Decomposition*; the exponential is *The Exponential and the Lie Group*; the comparison with $M_4$ is *The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*.

## The Mass Block

### Definition

**Definition.** In the chiral split $\mathbb{C}^6=V_+\oplus V_-$, the **mass block** is

$$
M=A_{+-}=\Pi_+A\Pi_-:V_-\longrightarrow V_+,
$$

a $3\times3$ complex matrix. Its partner is $N=A_{-+}:V_+\to V_-$.

**Proposition.** The mass block has $18$ real dimensions, and the element has the block form

$$
A=\begin{pmatrix}A_+&M\\N&A_-\end{pmatrix},
\qquad
A_\pm\in M_3(\mathbb{C}),\quad M,N\in M_3(\mathbb{C}).
$$

**Proof.** A $3\times3$ complex matrix has nine complex entries, hence $18$ real dimensions. The block form is the chiral decomposition of *The Two Chiralities*.

### The Chiral Transformation

**Definition.** The **chiral gauge group** of the mass block is

$$
U(3)_L\times U(3)_R,
$$

acting by

$$
(U_L,U_R)\cdot M=U_LMU_R^{-1}.
$$

**Proposition.** The action is well defined, and the singular values of $M$ are invariant:

$$
\sigma_i(U_LMU_R^{-1})=\sigma_i(M),\qquad i=1,2,3 .
$$

**Proof.** $(U_LMU_R^{-1})^*=U_RM^*U_L^{-1}$, so

$$
(U_LMU_R^{-1})^*(U_LMU_R^{-1})=U_RM^*MU_R^{-1},
$$

which is unitarily conjugate to $M^*M$; the eigenvalues of $M^*M$ are the squares of the singular values.

**Theorem (the orbit classification).** Two mass blocks lie in the same $U(3)\times U(3)$ orbit if and only if they have the same singular values. For a full-rank $M$ with distinct singular values the orbit has dimension $15$, and the stabilizer is the diagonal torus $U(1)^3$.

**Proof.** The singular value decomposition $M=U\Sigma V^*$ exhibits every $M$ as the orbit of the diagonal $\Sigma$; the singular values are the orbit invariants. The stabilizer of $\Sigma$ consists of the pairs $(U_L,U_R)$ with $U_L\Sigma U_R^{-1}=\Sigma$; in the basis of $\Sigma$ this forces $U_L$ and $U_R$ to have the same diagonal phases, a torus of dimension three. The orbit dimension is $9+9-3=15$.

**Corollary (the rank stratification).**

| Rank | Orbit dimension | Locus dimension | Locus |
|---|---|---|---|
| $3$ | $15$ | $18$ | open dense |
| $2$ | $14$ | $16$ | $\det M=0$ |
| $1$ | $9$ | $10$ | all $2\times2$ minors zero |
| $0$ | $0$ | $0$ | $M=0$ |

**Proof.** The orbit dimensions are $18-\dim(\text{stabilizer})$. For rank $2$ the stabilizer is $U(1)^2$ on the nonzero part times $U(1)\times U(1)$ on the one-dimensional kernel, of dimension four, so the orbit is $14$; the determinantal locus $\det M=0$ has real codimension two, dimension $16$. For rank $1$ the stabilizer is $U(1)$ on the nonzero part times $U(2)\times U(2)$ on the kernel, of dimension $1+4+4=9$, so the orbit is $9$; the rank-one locus is the image of $\mathbb{C}^3\times\mathbb{C}^3\to M_3$, $(u,v)\mapsto uv^{\mathsf T}$, of dimension $3+3-1=5$ complex $=10$ real. Rank $0$ is the single point $M=0$.

### The Determinant and the Phase

**Theorem.** For $M=U\Sigma V^*$,

$$
\det M=\det U\,\det V^*\,\sigma_1\sigma_2\sigma_3,
\qquad
\lvert\det M\rvert=\sigma_1\sigma_2\sigma_3 .
$$

The phase of $\det M$ is the phase of the $*$-unitary polar factor $UV^*$; under the chiral gauge it transforms by $\det U_L/\det U_R$ and can be gauged to $1$.

**Proof.** The determinant is multiplicative, $\det\Sigma=\sigma_1\sigma_2\sigma_3$, and $\lvert\det U\rvert=\lvert\det V\rvert=1$. Under $M\mapsto U_LMU_R^{-1}$ the determinant is multiplied by $\det U_L/\det U_R$, a phase that can be any unit complex number.

**Corollary (the invariants of the orbit).** The orbit invariants are the three singular values; the phase of the determinant is not an invariant.

**Proof.** The singular values classify the orbit by the theorem above; the phase can be changed arbitrarily by $U_L$.

### The Rank and Masslessness

**Definition.** The **mass channels** are the singular values $\sigma_1,\sigma_2,\sigma_3$. The mass block is **massless** if $M=0$; it has **rank** $k$ if exactly $k$ singular values are nonzero.

**Proposition.** The mass block is massless if and only if $A$ is block diagonal, that is, if and only if $A\in M_3(V_+)\oplus M_3(V_-)$.

**Proof.** $M=A_{+-}=0$ means the element has no component in the mixed corner; the block form is diagonal.

**Corollary (the massless algebra).** The massless elements form the subalgebra $M_3\oplus M_3$, of complex dimension $18$ and real dimension $36$; the mass block and its partner add the remaining $36$ real dimensions.

**Proof.** $M_3\oplus M_3$ has complex dimension $9+9=18$ and real dimension $36$. The mass block and its partner each have complex dimension $9$ and real dimension $18$; together they add $36$ real dimensions, for a total of $72$.

## The Chiral Polar Decomposition

### The Mass Block

**Theorem (the chiral polar decomposition).** Every $M\in M_3(\mathbb{C})$ has a decomposition

$$
M=U_L\Sigma U_R^{-1},
\qquad
U_L,U_R\in U(3),\quad
\Sigma=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)\ge0 .
$$

If $M$ is invertible and the singular values are distinct, the decomposition is unique up to the diagonal torus $U(1)^3$ acting on both sides.

**Proof.** This is the singular value decomposition $M=U\Sigma V^*$ with $U_L=U$ and $U_R=V$. Uniqueness: if $U_L\Sigma U_R^{-1}=U_L'\Sigma U_R'^{-1}$, then $U_L'^{-1}U_L$ commutes with $\Sigma$; for distinct positive $\sigma_i$ it is diagonal with phases, and the same for $U_R'^{-1}U_R$, with the phases equal.

**Definition.** The **positive mass factor** is $\Sigma$, and the **chiral unitaries** are $U_L,U_R$. The **chiral phase** is the phase of $\det(U_LU_R^{-1})$.

**Remark (the singular case).** If $M$ has rank $k<3$, the positive factor $\Sigma$ is still unique, but the unitaries are not: on the kernel of $M$ they can be chosen arbitrarily. The polar decomposition exists but is not unique.

### The Full Element

**Theorem (the $U(6)$ polar decomposition).** Every $A\in GL_6(\mathbb{C})$ has a unique decomposition

$$
A=UP,
\qquad
U\in U(6),\quad
P=(A^*A)^{1/2}>0 .
$$

For a singular $A$, the positive factor $P$ is unique, and $U$ is unique on the image of $P=(\ker A)^\perp$ and arbitrary on $\ker A$.

**Proof.** $A^*A$ is positive semidefinite, so it has a unique positive semidefinite square root $P$. If $A$ is invertible, $P>0$ and $U=AP^{-1}$ is $*$-unitary: $U^*U=P^{-1}A^*AP^{-1}=I$. Uniqueness follows by applying the same computation to any decomposition. For singular $A$, $P$ is still unique; $U$ is determined on the image of $P=(\ker A)^\perp$ and arbitrary on $\ker A$.

**Definition.** The **$U(6)$ polar factor** of $A$ is $U=A(A^*A)^{-1/2}$; the **positive factor** is $P=(A^*A)^{1/2}$.

**Theorem (the chiral block form).** Write

$$
U=\begin{pmatrix}U_{++}&U_{+-}\\U_{-+}&U_{--}\end{pmatrix},
\qquad
P=\begin{pmatrix}P_{++}&P_{+-}\\P_{-+}&P_{--}\end{pmatrix}
$$

in the chiral split. Then

$$
M=A_{+-}=U_{++}P_{+-}+U_{+-}P_{--}.
$$

**Proof.** Multiply the block matrices $A=UP$ and read the upper-right block.

**Corollary (the two extreme cases).**

- If $A$ is $*$-unitary, $P=I_6$ and $M=U_{+-}$: the mass block is the off-diagonal block of the $U(6)$ polar factor.
- If $A$ is positive definite, $U=I_6$ and $M=P_{+-}$: the mass block is the off-diagonal block of the positive factor.

**Proof.** In the first case $A=U$, in the second $A=P$.

**Remark (the two polar decompositions are different).** The mass block's polar decomposition uses $U(3)\times U(3)$ and produces the three singular values of $M$. The $U(6)$ polar decomposition uses the whole $*$-unitary group and produces the six singular values of $A$. The off-diagonal block $U_{+-}$ of the $U(6)$ polar factor is not the $*$-unitary factor $U_L$ of $M$; the mass block of $A$ is the sum of two products of blocks of $U$ and $P$. **The chiral polar decomposition of $M$ and the $U(6)$ polar decomposition of $A$ are different decompositions of different objects.**

### The Positive Factor and the Mass

**Proposition.** The positive factor $P$ is block positive: the matrix $P$ is positive definite, but its off-diagonal block $P_{+-}$ need not be small or zero. The mass block of $A$ is not the positive factor of $M$.

**Proof.** A positive definite $6\times6$ matrix can have nonzero off-diagonal blocks; for example $P=I_6+t(E_{14}+E_{41})$ is positive for small $t$, and its off-diagonal block is nonzero.

**Corollary (the massless case).** If $A$ is block diagonal and invertible, then $U$ and $P$ are block diagonal, and the mass block vanishes.

**Proof.** The polar decomposition of a block-diagonal matrix is block diagonal, because $A^*A$ is block diagonal and its square root is block diagonal.

## The Invariants

### The Three Mass Scales

**Theorem.** The orbit of $M$ under $U(3)\times U(3)$ is determined by the three singular values, and the orbit space is the closed positive cone

$$
\sigma_1\ge\sigma_2\ge\sigma_3\ge0 .
$$

**Proof.** The singular value decomposition gives a representative $\Sigma$ for every orbit, and two diagonal matrices with the same ordered singular values are equal. The ordering removes the permutation.

**Corollary (the mass spectrum).** The mass spectrum has three channels; the number of nonzero channels is the rank of $M$; the product of the channels is $\lvert\det M\rvert$.

**Proof.** The rank is the number of nonzero singular values, and the determinant modulus is their product.

### The $U(6)$ Invariants

**Proposition.** The $U(6)$ orbit of $A$ is determined by the six singular values of $A$; the polar factor $U$ distinguishes the orbits inside a fixed singular-value type.

**Proof.** The singular value decomposition $A=U\Sigma V^*$ with $U,V\in U(6)$; the singular values classify the $U(6)\times U(6)$ orbit, and the polar factor is the $*$-unitary part.

**Remark (the two invariant lists).** The mass block contributes three numbers (the mass scales); the full element contributes six (the singular values of $A$) plus the $*$-unitary polar factor. The mass scales are not the singular values of $A$; they are the singular values of the off-diagonal block, which depends on the chiral split.

## The Comparison with $M_4$

### The $2\times2$ Mass Block

For $M_4(\mathbb{C})$ the chiral split is $2+2$, the mass block is a $2\times2$ matrix, and the chiral gauge is $U(2)\times U(2)$. The singular values are two,

$$
\sigma_1\ge\sigma_2\ge0,
$$

the orbit dimensions are

| Rank | Orbit dimension | Locus dimension |
|---|---|---|
| $2$ | $6$ | $8$ |
| $1$ | $5$ | $6$ |
| $0$ | $0$ | $0$ |

and the determinant is a phase times $\sigma_1\sigma_2$.

**Proof.** The mass block has real dimension $8$; the full-rank stabilizer is $U(1)^2$, of dimension two, so the orbit is $6$; the rank-one stabilizer is $U(1)\times U(1)^2$, of dimension three, so the orbit is $5$.

### The Pattern

**Theorem.** For the chiral split $m+m$ of $M_{2m}(\mathbb{C})$, the mass block is $m\times m$, the chiral gauge is $U(m)\times U(m)$, and the number of mass channels is $m$. The full-rank orbit has dimension

$$
2m^2-m,
$$

and the orbit space is the cone $\sigma_1\ge\cdots\ge\sigma_m\ge0$.

**Proof.** The mass block has $2m^2$ real dimensions; the stabilizer of a full-rank diagonal with distinct singular values is the diagonal torus $U(1)^m$, of dimension $m$; the orbit dimension is $2m^2-m$.

**Corollary.** The three cases are

| Algebra | $m$ | Mass block | Channels | Full-rank orbit | Rank-$(m-1)$ orbit |
|---|---|---|---|---|---|
| $M_2$ | $1$ | $1\times1$ | $1$ | $1$ | $0$ |
| $M_4$ | $2$ | $2\times2$ | $2$ | $6$ | $5$ |
| $M_6$ | $3$ | $3\times3$ | $3$ | $15$ | $14$ |

**Proof.** Substitute $m=1,2,3$ in $2m^2-m$ and $2m^2-m-1$.

**Remark (the growth).** The number of mass channels grows linearly in $m$; the number of real mass parameters grows quadratically. **The $3\times3$ mass block of $M_6$ has three channels and eighteen real parameters; the $2\times2$ block of $M_4$ has two channels and eight; the $1\times1$ block of $M_2$ has one channel and one.**

## Summary

The mass block of the $3+3$ chiral split is a $3\times3$ complex matrix $M=A_{+-}$, of $18$ real dimensions. The chiral gauge $U(3)\times U(3)$ acts by $M\mapsto U_LMU_R^{-1}$, and the orbits are classified by the three singular values $\sigma_1\ge\sigma_2\ge\sigma_3\ge0$.

$$
\boxed{\ M=U_L\Sigma U_R^{-1},\qquad \Sigma=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3),\qquad \lvert\det M\rvert=\sigma_1\sigma_2\sigma_3 .\ }
$$

The determinant phase is gauge-dependent; the modulus is the product of the channels; the rank is the number of nonzero channels. The massless block is $M=0$, and the massless algebra is $M_3\oplus M_3$.

The full element has the $U(6)$ polar decomposition $A=UP$, with $U\in U(6)$ and $P>0$; the mass block of $A$ is $U_{++}P_{+-}+U_{+-}P_{--}$, a sum of two products of chiral blocks. The $U(6)$ polar factor and the $U(3)\times U(3)$ polar factors of $M$ are different objects.

| Object | Data |
|---|---|
| Mass block | $M=A_{+-}$, $3\times3$, $18$ real |
| Chiral gauge | $U(3)\times U(3)$, dimension $18$ |
| Invariants | $\sigma_1,\sigma_2,\sigma_3$ |
| Determinant | phase $\times\sigma_1\sigma_2\sigma_3$ |
| Rank | number of nonzero channels |
| Massless algebra | $M_3\oplus M_3$, real dimension $36$ |
| $U(6)$ polar | $A=UP$, $U\in U(6)$, $P>0$ |
| $M_4$ comparison | $2\times2$, two channels, orbit $6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=A_{+-}$ | the mass block $V_-\to V_+$ |
| $N=A_{-+}$ | the partner $V_+\to V_-$ |
| $U_L,U_R$ | the chiral unitaries in $U(3)$ |
| $\Sigma$ | the positive diagonal factor of $M$ |
| $\sigma_1,\sigma_2,\sigma_3$ | the three singular values (mass channels) |
| $U$ | the $U(6)$ polar factor of $A$ |
| $P$ | the positive factor $(A^*A)^{1/2}$ |

## Further Reading

- [The Two Chiralities](the-two-chiralities-of-m6c.html), for the $3+3$ split and the mass block.
- [The Rank-Two and Rank-Three Splits](the-rank-two-and-rank-three-splits-of-m6c.html), for the mass block as the mixed corner.
- [The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners](the-m3-m3-and-m2-m4-corners-of-m6c.html), for the massless algebra and the relative scale.
- [The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$](the-mass-block-and-the-chiral-polar-decomposition-of-m4c.html), for the $2\times2$ comparison.
- [The Polar Decomposition](the-polar-decomposition-of-m6c.html), for the full $U(6)$ polar decomposition.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m6c.html), for the $*$-unitary group $U(6)$.
- [The Geometry of the Idempotents](the-geometry-of-the-idempotents-of-m6c.html), for the homogeneous spaces of the chiral unitaries.
