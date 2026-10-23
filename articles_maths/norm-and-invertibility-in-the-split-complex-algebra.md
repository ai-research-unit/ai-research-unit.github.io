# __Norm and Invertibility in the Split-Complex Algebra__

## Introduction

This article studies the algebraic norm that the general plain bilinear product, the multiplication $Q_2Q_1$ of the split-complex algebra, carries, and the invertibility of the elements of that product.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its general plain bilinear form, the definition of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*: for the plain product the form is $\langle Q_2,Q_1\rangle=Q_2Q_1$ and its diagonal is

$$
\langle Q\rangle=Q^{2}=(q^{2}+q'^{2})+2qq'j,
$$

the first of the two algebraic norms of the space and not the second, $\langle Q\rangle_{*}=Q\bar Q=q^{2}-q'^{2}$. The article defines it, records its value, its Gram matrix, its anisotropy and its vanishing set, and proves that it is **multiplicative** as an element of the ring and **not a real norm**. That is the whole of the algebraic norm of the plain product.

The invertibility is where the article records an **absence**. The plain product is associative and unital, so its invertible elements and its group of units are defined; but the algebraic norm of the product does **not** decide them. The element $1+j$ is a zero divisor and satisfies $\langle 1+j\rangle=2(1+j)\neq0$: the non-vanishing of the algebraic norm is not sufficient for invertibility. The converse failure cannot occur, because $\langle Q\rangle=0$ forces $Q=0$ over the reals; the norm is anisotropic and sees only the origin. The article states that absence rather than a criterion. The criterion of the plain product is furnished by the other algebraic norm, $\langle Q\rangle_{*}=Q\bar Q$, which is not the algebraic norm of the plain product and is studied in *Norm and Invertibility in the General Split-Complex Algebra*; the zero divisors are *Zero Divisors of the Split-Complex Algebra*.

**The results.** The plain product carries one algebraic norm, the diagonal of its general plain bilinear form, $\langle Q\rangle=Q^{2}=(q^{2}+q'^{2})+2qq'j$, $\mathbb{D}$-valued, anisotropic, of realified Gram matrix $\operatorname{diag}(1,1)$ in the basis $1,j$. It is **multiplicative**, $\langle QB\rangle=\langle Q\rangle\langle B\rangle$, by associativity of the ring. It is **not a real norm**: its value is not real in general, it defines no order and no modulus, and its vanishing set is the single point $\{0\}$. It does **not** decide invertibility: $\langle Q\rangle\neq0$ does not force $Q$ to be a unit, the witness being the zero divisor $1+j$. Each section below states its result first and then proves it.

## The Algebraic Norm of the Plain Product

**The general plain bilinear product carries exactly one algebraic norm, the diagonal of its general plain bilinear form, $\langle Q\rangle=Q^{2}=(q^{2}+q'^{2})+2qq'j$; it is $\mathbb{D}$-valued and anisotropic, of realified Gram matrix $\operatorname{diag}(1,1)$, and its vanishing set is the origin.**

### Definition

The **algebraic norm of the plain product** is the diagonal of the general plain bilinear form of the product,

$$
\langle Q\rangle=\langle Q,Q\rangle=Q^{2},
$$

for the form

$$
\langle Q_2,Q_1\rangle=Q_2Q_1,
$$

the general plain bilinear form of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*. The form is symmetric, because the algebra is commutative. In coordinates,

$$
\langle Q\rangle=(q+jq')^{2}=q^{2}+q'^{2}+2qq'j,
$$

so the algebraic norm takes its value in the whole algebra $\mathbb{D}$ and not in the base field.

**Basic properties.** Each is a direct reading of the definition.

- $\langle Q\rangle$ is **$\mathbb{D}$-valued**; it is real exactly when $qq'=0$, that is on the real line $\mathbb{R}_{\mathbb{D}}$ or on the split imaginary line $j\mathbb{R}_{\mathbb{D}}$.
- $\langle\cdot\rangle$ is **homogeneous of degree two**, $\langle\lambda Q\rangle=\lambda^{2}\langle Q\rangle$ for $\lambda\in\mathbb{R}$, and its polarisation is the form of the same letter, $\langle Q+B\rangle-\langle Q\rangle-\langle B\rangle=2\langle Q,B\rangle=2QB$.
- $\langle\cdot\rangle$ is **anisotropic**: it vanishes only at $Q=0$. It is therefore not indefinite, but it is not a real norm either, because its value is not real.
- Its **realified Gram matrix** on the basis $1,j$ is the identity $\operatorname{diag}(1,1)$, since the real part of $Q_2Q_1$ is $q_2q_1+q'_2q'_1$. The full $\mathbb{D}$-valued form has the symmetric Gram matrix $\begin{pmatrix}1&j\\j&1\end{pmatrix}$.
- Its **vanishing set** is $\{Q:\langle Q\rangle=0\}=\{0\}$.

### The Polarisation

**Proposition.** The polar form of the algebraic norm is the symmetrised product,

$$
\boxed{\; \langle Q_2,Q_1\rangle=\tfrac12\bigl(\langle Q_2+Q_1\rangle-\langle Q_2\rangle-\langle Q_1\rangle\bigr)=Q_2Q_1 \;},
$$

and it is $\mathbb{D}$-valued and symmetric.

**Proof.** Expand $(Q_2+Q_1)^{2}=Q_2^{2}+Q_2Q_1+Q_1Q_2+Q_1^{2}$; the algebra is commutative, so the two middle terms are equal and the half-difference is $Q_2Q_1$.

### Multiplicativity

**Theorem.** The algebraic norm of the plain product is multiplicative:

$$
\boxed{\;\langle QB\rangle=\langle Q\rangle\langle B\rangle,\qquad Q,B\in\mathbb{D}\;}.
$$

**Proof.** By associativity and commutativity of the ring,

$$
\langle QB\rangle=(QB)^{2}=QBQB=Q^{2}B^{2}=\langle Q\rangle\langle B\rangle.
$$

The multiplicativity is the multiplicativity of the square in any commutative associative algebra; it does not make $\langle\cdot\rangle$ a scalar norm, because the product on the right is the product of the ring and not the product of real numbers.

**Corollary.** The algebraic norm is invariant under the conjugation, $\langle\bar Q\rangle=\overline{\langle Q\rangle}$.

**Proof.** $\bar Q^{\,2}=\overline{Q^{2}}$, the bar being an automorphism of the algebra.

## The Algebraic Norm Is Not a Real Norm

**The algebraic norm is $\mathbb{D}$-valued, not real; its real part is the Euclidean form $q^{2}+q'^{2}$, positive definite, and its imaginary part is $2qq'$. It is therefore not a norm of the real vector space, although it is multiplicative.**

### The Real and the Imaginary Parts

Write $Q^{2}=B_{0}+jB_{1}$ with

$$
B_{0}=q^{2}+q'^{2},\qquad B_{1}=2qq'.
$$

The real part $B_{0}$ is the **Euclidean quadratic form** of the plane, positive definite, of Gram matrix $\operatorname{diag}(1,1)$; the imaginary part $B_{1}$ is the hyperbolic cross term. The real part is not multiplicative: for $Q=B=1+j$ one has $B_{0}(Q)=B_{0}(B)=2$, while $QB=2+2j$ and $B_{0}(QB)=8$, not $4$. The full algebraic norm is multiplicative because it keeps both parts and multiplies in the ring; the real part alone does not.

### The Vanishing Set and Anisotropy

**Proposition.** The algebraic norm vanishes only at the origin:

$$
\boxed{\;Q^{2}=0\iff Q=0\;}.
$$

**Proof.** $Q^{2}=0$ gives $q^{2}+q'^{2}=0$ and $2qq'=0$. The first equation forces $q=q'=0$ over $\mathbb{R}$, since both squares are non-negative and their sum is zero.

So the algebraic norm is **anisotropic**. This is the sharp difference from the second algebraic norm $\langle Q\rangle_{*}=q^{2}-q'^{2}$, which vanishes on the two null lines and therefore on every zero divisor. The plain algebraic norm sees the zero-divisor set as a set of nonzero values and cannot separate it from the units.

### The Shell of the Algebraic Norm

The **shell** of the algebraic norm at a central value $\lambda\in\mathbb{R}$ is the set

$$
\{Q:\langle Q\rangle=\lambda\}.
$$

For $\lambda=0$ it is $\{0\}$. For $\lambda=1$ it is the four-element set $\{\pm1,\pm j\}$, the roots of $+1$ of *Square Roots of One and the Idempotents of the Split-Complex Algebra*. For $\lambda=-1$ it is empty, because the real part $q^{2}+q'^{2}$ is non-negative. The shell is not a level set of a real norm: for a real central value it is a finite set, of four points when $\lambda>0$, one point when $\lambda=0$, and empty when $\lambda<0$.

## The Algebraic Norm Does Not Decide Invertibility

**The algebraic norm does not decide invertibility: $\langle Q\rangle=0$ forces $Q=0$, which is not a unit, but $\langle Q\rangle\neq0$ does not force $Q$ to be a unit.**

The algebraic norm of a product would decide invertibility if the invertible elements were exactly the elements of non-vanishing algebraic norm. For the plain product that statement is **false in the direction that matters**, and the article records the absence rather than a criterion.

**Theorem (the algebraic norm does not decide invertibility).** The implication

$$
\langle Q\rangle=0\Longrightarrow Q\text{ non-invertible}
$$

holds, but the converse implication

$$
\langle Q\rangle\neq0\Longrightarrow Q\text{ invertible}
$$

fails.

**Proof.** The first statement is the anisotropy of the norm: $\langle Q\rangle=0$ gives $Q=0$, and $0$ has no inverse. For the second, take $Q=1+j$. Its algebraic norm is

$$
\langle 1+j\rangle=(1+j)^{2}=1+2j+j^{2}=2+2j\neq0,
$$

while $Q$ is a zero divisor, $(1+j)(1-j)=1-j^{2}=0$, hence not invertible.

**Remark (the witness).** The element $1+j$ is the whole of the failure. It is a nonzero zero divisor, so it lies on the null cone of the *other* algebraic norm, $\langle 1+j\rangle_{*}=1^{2}-1^{2}=0$; its plain algebraic norm is $2+2j$, a nonzero element of the ring. The vanishing set of $\langle\cdot\rangle$ is the origin and the vanishing set of $\langle\cdot\rangle_{*}$ is the two null lines; the zero-divisor set is the second vanishing set with the origin removed, and the first norm cannot see it.

**Remark (what replaces the criterion).** The plain product is not left without an invertibility theory: it is associative and unital, every element of its group of units has an inverse, and the zero divisors are characterised in *Zero Divisors of the Split-Complex Algebra*. What the article records is that this theory is **not** read from the algebraic norm of the plain product, which is the one algebraic norm the product carries; the criterion that does exist is carried by the other algebraic norm, $\langle Q\rangle_{*}=Q\bar Q$, and belongs to *Norm and Invertibility in the General Split-Complex Algebra*.

## The Unit and the Group of Units

**The plain product is associative and unital, with the two-sided unit $1$, and its invertible elements form the group of units $\mathbb{D}^{\times}$, a proper subset of $\mathbb{D}\setminus\{0\}$ because the product has zero divisors.**

The unit of the plain product is $1$: it is a two-sided unit, $Q1=1Q=Q$, and it is the only one. The product is associative and commutative, so the inverse of an element is unique when it exists and the invertible elements form the **group of units** of the plain product, an abelian group.

The plain product has zero divisors: the identity $(1+j)(1-j)=0$ exhibits a product of two nonzero elements that is zero. The plain algebra is therefore not a division algebra, and the group of units is a proper subset of $\mathbb{D}\setminus\{0\}$. The zero divisors, their two families and their geometry are *Zero Divisors of the Split-Complex Algebra*, and they are cited here, not read.

The group is described by the other algebraic norm: an element is a unit exactly when $\langle Q\rangle_{*}=Q\bar Q\neq0$, and then $Q^{-1}=\bar Q/\langle Q\rangle_{*}$. That criterion, the four components of the group and the distribution of the units among the distinguished subspaces are the subject of *Norm and Invertibility in the General Split-Complex Algebra*; the present article only records that the group exists and that its boundary is not the vanishing set of $\langle\cdot\rangle$.

## Summary

The general plain bilinear product $Q_2Q_1$ carries one algebraic norm, the diagonal of its general plain bilinear form,

$$
\langle Q\rangle=Q^{2}=(q^{2}+q'^{2})+2qq'j,
$$

$\mathbb{D}$-valued, anisotropic, of realified Gram matrix $\operatorname{diag}(1,1)$ and vanishing set the origin. It is multiplicative, $\langle QB\rangle=\langle Q\rangle\langle B\rangle$, by associativity of the ring, and invariant under the conjugation, $\langle\bar Q\rangle=\overline{\langle Q\rangle}$.

It is **not a real norm**: its value is not real in general, its real part is the Euclidean form $q^{2}+q'^{2}$ and its imaginary part is $2qq'$, and it defines no order and no modulus. It does **not** decide invertibility: the zero divisor $1+j$ has $\langle 1+j\rangle=2+2j\neq0$, so non-vanishing is not sufficient; the implication $\langle Q\rangle=0\Rightarrow Q=0$ holds, but it only says that the origin is not a unit. The plain product is associative and unital, with unit $1$ and a genuine abelian group of units; the criterion is carried by the other algebraic norm $\langle Q\rangle_{*}=Q\bar Q$, which is not the algebraic norm of the plain product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_2,Q_1$ | the two elements of a product, first and second slot |
| $Q_2Q_1$ | the general plain bilinear product, the multiplication of the split-complex algebra |
| $\langle Q_2,Q_1\rangle=Q_2Q_1$ | the general plain bilinear form, the form of the product |
| $\langle Q\rangle=\langle Q,Q\rangle=Q^{2}=(q^{2}+q'^{2})+2qq'j$ | the algebraic norm of the plain product, the first of the two algebraic norms |
| $\operatorname{diag}(1,1)$ | the realified Gram matrix of $\langle\cdot\rangle$ in the basis $1,j$ |
| $\{Q:\langle Q\rangle=0\}=\{0\}$ | the vanishing set of the algebraic norm; not the zero-divisor set |
| $1$ | the two-sided unit of the plain product |
| $\mathbb{D}^{\times}$ | the group of units of the plain product, not read from $\langle\cdot\rangle$ |
| $1+j$ | the witness: a zero divisor with $\langle 1+j\rangle=2+2j\neq0$ |

## Further Reading

- [The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space](the-two-forms-and-the-two-algebraic-norms-of-the-split-complexoid-space.html), for the definition of the algebraic norm as the form at the two equal arguments, the two algebraic norms and their separation.
- [Norm and Invertibility in the General Split-Complex Algebra](norm-and-invertibility-in-the-general-split-complex-algebra.html), for the other algebraic norm, the criterion of invertibility and the group of units.
- [Split-Complex Algebra](split-complex-algebra.html), for the product, its associativity, its unit and its element theory.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the zero divisors, which the algebraic norm of the plain product does not detect.
- [Square Roots of One and the Idempotents of the Split-Complex Algebra](square-roots-of-one-and-the-idempotents-of-the-split-complex-algebra.html), for the shell at $1$ and the four roots of $+1$.
