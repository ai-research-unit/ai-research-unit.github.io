# __Norm and Invertibility in the Symmetric Plain Algebra__

## Introduction

This article studies the algebraic norm that the symmetric plain algebra, the biquaternion space under the Jordan product $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ of *Introduction to the Symmetric Plain Algebra*, carries, and the invertibility of its elements.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. The symmetrisation keeps the scalar part of a product, so the block carries the algebraic norm of the general plain bilinear product, the general plain bilinear algebraic norm

$$
\langle\tilde Q\rangle=\mathrm{Sc}\bigl(\tilde Q\bullet\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

complex-valued, indefinite and **not** multiplicative. The article defines it, records its Gram matrix, its signature and its vanishing set, and proves the failure of multiplicativity; the four general products carry four algebraic norms in all, and $\langle\cdot\rangle$ is the one of this row.

The invertibility is where the article records an **absence**. The block is commutative and unital, with the unit $e_t$, but it is not associative, and its invertibility is governed by a quadratic form that is **not** its algebraic norm. The element $e_t+\vec e_x$ is invertible and satisfies $\langle e_t+\vec e_x\rangle=0$, and the element $e_t+i\vec e_x$ is a zero divisor and satisfies $\langle e_t+i\vec e_x\rangle=2$: the non-vanishing of the algebraic norm is neither necessary nor sufficient for invertibility, and the article states that absence rather than a criterion. The invertibility the block does have is the invertibility of the Jordan theory, carried by a different quadratic form and studied in *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

**The results.** The block carries one algebraic norm, the diagonal of its scalar-part form, $\langle\tilde Q\rangle=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$, complex-valued and indefinite, of Gram matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, with the complex cone as its vanishing set. It is **not multiplicative**, the pair $(\vec e_x,\vec e_y)$ separating the two sides. It does **not** decide invertibility: the unit $e_t+\vec e_x$ has $\langle\cdot\rangle=0$ and the zero divisor $e_t+i\vec e_x$ has $\langle\cdot\rangle=2$, so the non-vanishing of the algebraic norm is neither necessary nor sufficient; the invertibility the block does have is that of the Jordan theory, carried by a different quadratic form. Each section below states its result first and then proves it.

**Boundaries.** The algebraic norm of the general plain bilinear product is *Norm and Invertibility in the Biquaternion Algebra*, and the three other algebraic norms are *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*; none of the four is read here beyond $\langle\cdot\rangle$. The product, its unit and its non-associativity are *Introduction to the Symmetric Plain Algebra*; the trace form the algebraic norm polarises is *The Trace Form and the Invariance of the Symmetric Plain Algebra*; the square and the quadratic identity are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*; the zero divisors are *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the definitions of the unit and the inverse are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x\vec e_y=\vec e_z$, $\vec e_k^{2}=-e_t$ and central scalar imaginary $i$. An element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=\sum_{k=1}^{3}Q_k\vec e_k$ and $Q_\mu\in\mathbb{C}$; the two elements of a product are $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ and $\tilde Q_2=Q_{2t}e_t+\vec Q_2$, with $(\vec Q_1,\vec Q_2)=\sum_kQ_{1k}Q_{2k}$ the complex bilinear dot product of the vector parts. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. Juxtaposition is the plain product and $\bullet$ is the product of the block, $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$.

## The Algebraic Norm of the Block

**The block carries exactly one algebraic norm**, the diagonal of its scalar-part form, $\langle\tilde Q\rangle=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$; it is complex-valued and indefinite, of Gram matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, and its vanishing set is the complex cone.

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
\langle\tilde Q\rangle=\mathrm{Sc}\bigl(\tilde Q\bullet\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

equivalently $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle$ for the form

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}\bigl(\tilde Q_1\bullet\tilde Q_2\bigr)=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2\bigr)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2),
$$

which is the general plain bilinear form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*. The symmetrisation does not change the scalar part, so the block carries the algebraic norm of the general plain bilinear product; the form and its diagonal are of the same letter.

**Basic properties.** Each is a direct reading of the definition.

- $\langle\tilde Q\rangle$ is **complex-valued** in general; it is real exactly on the union of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and its imaginary translate $i\mathbb{H}_{\mathbb{B}}$.
- $\langle\cdot\rangle$ is **homogeneous of degree two**, $\langle\lambda\tilde Q\rangle=\lambda^{2}\langle\tilde Q\rangle$ for $\lambda\in\mathbb{C}$, and its polarisation is the form of the same letter, $\langle\tilde Q_1+\tilde Q_2\rangle-\langle\tilde Q_1\rangle-\langle\tilde Q_2\rangle=2\langle\tilde Q_1,\tilde Q_2\rangle$.
- $\langle\cdot\rangle$ is **not positive definite** and **not definite**.
- Its Gram matrix on the basis is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and the realification of $\langle\cdot\rangle$ is non-degenerate of signature $(4,4)$ on $\mathbb{B}\cong\mathbb{R}^{8}$.
- Its **vanishing set** is the complex cone $\{\langle\tilde Q\rangle=0\}$, the complex quadric of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, and not the zero-divisor set of the block.

## The Algebraic Norm Is Not Multiplicative

**The algebraic norm of the block is not multiplicative:** $\langle\tilde Q_1\bullet\tilde Q_2\rangle\neq \langle\tilde Q_1\rangle\langle\tilde Q_2\rangle$ in general, the pair $(\vec e_x,\vec e_y)$ separating the two sides.

**Proposition.** The algebraic norm of the block is **not** multiplicative:

$$
\langle\tilde Q_1\bullet\tilde Q_2\rangle\neq \langle\tilde Q_1\rangle\,\langle\tilde Q_2\rangle\quad\text{in general.}
$$

*Proof.* The pair $\vec e_x,\vec e_y$ separates the two sides: $\vec e_x\bullet \vec e_y=\tfrac12(\vec e_x\vec e_y+\vec e_y\vec e_x)=\tfrac12(\vec e_z-\vec e_z)=0$, so $\langle \vec e_x\bullet \vec e_y\rangle=\langle 0\rangle=0$, while $\langle \vec e_x\rangle\langle \vec e_y\rangle=(-1)(-1)=1$. The two values differ, so no multiplicativity holds.

**Remark (the multiplicative algebraic norm is another form).** Of the four algebraic norms of the space the multiplicative one is $\langle\cdot\rangle_{\natural}$, the algebraic norm of the quaternionic product, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$; it is a different quadratic form on the same space, and the block, whose product is not associative and has zero divisors, fails multiplicativity for its own algebraic norm $\langle\cdot\rangle$. The multiplicativity that the block does retain is the one of the quadratic representation of the Jordan theory, a statement about a different quadratic form and not about $\langle\cdot,\cdot\rangle$.

## The Unit and the Degeneracy of the Naive Inverse

**The block is commutative and unital with unit $e_t$, but it is not associative, and its naive inverse equation $\tilde Q_1\bullet\tilde Q_2=e_t$ is degenerate: the element $\tilde\Upsilon=\vec e_x+i\vec e_y$ satisfies it for a two-dimensional affine family of $\tilde Q_2$.**

The unit of the block is $e_t$: the product is commutative, so its one-sided inverse equations coincide, and $e_t$ is the two-sided unit (*Introduction to the Symmetric Plain Algebra*). The block is **not associative**: $(\tilde Q_1\bullet\tilde Q_2)\bullet\tilde Q_3\neq\tilde Q_1\bullet(\tilde Q_2\bullet\tilde Q_3)$ in general, and the single equation $\tilde Q_1\bullet\tilde Q_2=e_t$ is **degenerate**: the element $\tilde\Upsilon=\vec e_x+i\vec e_y$ satisfies $\tilde\Upsilon\bullet\tilde Q_2=e_t$ for a two-dimensional affine family of $\tilde Q_2$, because its left multiplication has a two-dimensional kernel. The naive inverse equation therefore does not define an inverse, and the block is treated with the inverse of the Jordan theory in *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm does not decide invertibility:** $\langle\tilde Q\rangle=0$ does not force $\tilde Q$ non-invertible, and $\langle\tilde Q\rangle\neq0$ does not force $\tilde Q$ invertible.

The algebraic norm of a product would decide invertibility if the invertible elements were exactly the elements of non-vanishing algebraic norm. For the block that statement is **false in both directions**, and the article records the absence rather than a criterion.

**Theorem (the algebraic norm does not decide invertibility).** Neither implication holds:

$$
\langle\tilde Q\rangle=0\ \not\Longrightarrow\ \tilde Q\text{ non-invertible},
\qquad
\langle\tilde Q\rangle\neq0\ \not\Longrightarrow\ \tilde Q\text{ invertible}.
$$

*Proof.* For the first implication, the element $\tilde Q=e_t+\vec e_x$ has $\langle\tilde Q\rangle=1^{2}-1^{2}=0$, and it is invertible: $(e_t+\vec e_x)\bullet\tfrac12(e_t-\vec e_x)=\tfrac12(e_t+\vec e_x)(e_t-\vec e_x)=\tfrac12\cdot2e_t=e_t$ and $\tilde Q^{\bullet2}\bullet\tfrac12(e_t-\vec e_x)=\tilde Q$, so $\tfrac12(e_t-\vec e_x)$ is its inverse of the block. For the second implication, the element $\tilde Q=e_t+i\vec e_x$ has $\langle\tilde Q\rangle=1^{2}-(i)^{2}=1+1=2\neq0$, and it is a zero divisor, $(e_t+i\vec e_x)(e_t-i\vec e_x)=e_t^{2}-(i\vec e_x)^{2}=e_t-e_t=0$, hence non-invertible while its algebraic norm does not vanish.

**Remark (the two witnesses).** The element $e_t+\vec e_x$ is invertible with vanishing algebraic norm, so the algebraic norm is not necessary for invertibility; the element $e_t+i\vec e_x$ is non-invertible with non-vanishing algebraic norm, so it is not sufficient either. The vanishing set of $\langle\cdot\rangle$ is the complex cone and the zero-divisor set is the cone of a different quadratic form; the two cones meet but neither contains the other.

**Remark (what replaces the criterion).** The block is not left without an invertibility theory: it is commutative and unital, the Jordan inverse is defined by its two equations, and the zero divisors are characterised in *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. That theory is **not** read from the algebraic norm of the block, which is the one algebraic norm the block carries; the criterion it uses is carried by a different quadratic form and belongs to the article that owns that form.

## Summary

The symmetric plain product $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ carries one algebraic norm, the diagonal of its scalar-part form, the general plain bilinear algebraic norm

$$
\langle\tilde Q\rangle=\mathrm{Sc}\bigl(\tilde Q\bullet\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

complex-valued, of Gram matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, with the complex cone as its vanishing set, and it is **not multiplicative**, the pair $(\vec e_x,\vec e_y)$ separating the two sides, $\langle \vec e_x\bullet \vec e_y\rangle=\langle 0\rangle=0$ against $\langle \vec e_x\rangle\langle \vec e_y\rangle=1$.

The block is commutative and unital, with the unit $e_t$, and it is not associative, the naive inverse equation $\tilde Q_1\bullet\tilde Q_2=e_t$ being degenerate at $\tilde\Upsilon=\vec e_x+i\vec e_y$. Its algebraic norm does **not** decide invertibility: the invertible element $e_t+\vec e_x$ has $\langle\cdot\rangle=0$ and the zero divisor $e_t+i\vec e_x$ has $\langle\cdot\rangle=2$, so the non-vanishing of the algebraic norm is neither necessary nor sufficient. The article records that absence; the invertibility the block does have is the invertibility of the Jordan theory, carried by a different quadratic form, which is not the algebraic norm of the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ | the symmetric plain product, the multiplication of the block |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\bullet\tilde Q_2)=\sum_\mu\varepsilon_\mu Q_{1\mu} Q_{2\mu}$ | the general plain bilinear form, the scalar-part form of the product |
| $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$ | the algebraic norm of the block, one of the four algebraic norms of the space |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $\langle\cdot\rangle$; the signature of its realification is $(4,4)$ |
| $\{\langle\tilde Q\rangle=0\}$ | the complex cone, the vanishing set of the algebraic norm |
| $e_t$ | the two-sided unit of the block |
| $\tilde\Upsilon=\vec e_x+i\vec e_y$ | the witness of the degeneracy of the naive inverse equation |
| $e_t+\vec e_x$, $e_t+i\vec e_x$ | the witnesses: invertible with $\langle\cdot\rangle=0$, and zero divisor with $\langle\cdot\rangle=2$ |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the general plain bilinear form $\langle\cdot,\cdot\rangle$ and the table of the four forms.
- *Introduction to the Symmetric Plain Algebra* (`articles_maths/introduction-to-the-symmetric-plain-algebra.md`), for the product, its unit, its commutativity and its non-associativity.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra* (`articles_maths/the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra.md`), for the form the algebraic norm polarises.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.md`), for the invertibility the block does have, carried by a different quadratic form.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), §*The Unit and the Inverse*, for the relative definitions of the unit and the inverse.
- *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the zero divisors, which the algebraic norm of the block does not detect.
- *Remarkable Subspaces and the Four Algebraic Norms* (`articles_maths/remarkable-subspaces-and-the-four-algebraic-norms.md`), for the restriction of $\langle\cdot\rangle$ to the remarkable subspaces with its signature.
