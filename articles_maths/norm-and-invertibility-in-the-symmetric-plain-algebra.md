# __Norm and Invertibility in the Symmetric Plain Algebra__

## Introduction

This article studies the algebraic norm that the symmetric plain algebra, the biquaternion space under the Jordan product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*, carries, and the invertibility of its elements.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. The symmetrisation keeps the scalar part of a product, so the block carries the algebraic norm of the general plain bilinear product, the general plain bilinear algebraic norm

$$
B(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\bullet\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},
$$

complex-valued, indefinite and **not** multiplicative. The article defines it, records its Gram matrix, its signature and its vanishing set, and proves the failure of multiplicativity; the four general products carry four algebraic norms in all, and $B$ is the one of this row.

The invertibility is where the article records an **absence**. The block is commutative and unital, with the unit $e_0$, but it is not associative, and its invertibility is governed by a quadratic form that is **not** its algebraic norm. The element $e_0+e_1$ is invertible and satisfies $B(e_0+e_1)=0$, and the element $e_0+ie_1$ is a zero divisor and satisfies $B(e_0+ie_1)=2$: the non-vanishing of the algebraic norm is neither necessary nor sufficient for invertibility, and the article states that absence rather than a criterion. The invertibility the block does have is the invertibility of the Jordan theory, carried by a different quadratic form and studied in *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

**The results.** The block carries one algebraic norm, the diagonal of its scalar-part form, $B(\tilde Q)=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2}$, complex-valued and indefinite, of Gram matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, with the complex cone as its vanishing set. It is **not multiplicative**, the pair $(e_1,e_2)$ separating the two sides. It does **not** decide invertibility: the unit $e_0+e_1$ has $B=0$ and the zero divisor $e_0+ie_1$ has $B=2$, so the non-vanishing of the algebraic norm is neither necessary nor sufficient; the invertibility the block does have is that of the Jordan theory, carried by a different quadratic form. Each section below states its result first and then proves it.

**Boundaries.** The algebraic norm of the general plain bilinear product is *Norm and Invertibility in the General Plain Algebra*, and the three other algebraic norms are *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*; none of the four is read here beyond $B$. The product, its unit and its non-associativity are *Introduction to the Symmetric Plain Algebra of Biquaternions*; the trace form the algebraic norm polarises is *The Trace Form and the Invariance of the Symmetric Plain Algebra*; the square and the quadratic identity are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*; the zero divisors are *Zero Divisors of the Symmetric Plain Algebra*; the definitions of the unit and the inverse are *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, $e_k^{2}=-e_0$ and central scalar imaginary $i$. An element is $\tilde Q=Q_0e_0+\vec Q$ with $\vec Q=\sum_{k=1}^{3}Q_ke_k$ and $Q_\mu\in\mathbb{C}$; $(\vec P,\vec Q)=\sum_kP_kQ_k$ is the complex bilinear dot product of the vector parts. The natural conjugation is $\tilde Q^{\natural}=Q_0-\vec Q$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. Juxtaposition is the plain product and $\bullet$ is the product of the block, $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$.

## The Algebraic Norm of the Block

**The block carries exactly one algebraic norm**, the diagonal of its scalar-part form, $B(\tilde Q)=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2}$; it is complex-valued and indefinite, of Gram matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, and its vanishing set is the complex cone.

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
B(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\bullet\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},
$$

equivalently $B(\tilde Q)=B(\tilde Q,\tilde Q)$ for the form

$$
B(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\bullet\tilde Q\bigr)=\mathrm{Sc}\bigl(\tilde P\tilde Q\bigr)=P_0Q_0-(\vec P,\vec Q),
$$

which is the general plain bilinear form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*. The symmetrisation does not change the scalar part, so the block carries the algebraic norm of the general plain bilinear product; the form and its diagonal are of the same letter.

**Basic properties.** Each is a direct reading of the definition.

- $B(\tilde Q)$ is **complex-valued** in general; it is real exactly on the union of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and its imaginary translate $i\mathbb{H}_{\mathbb{B}}$.
- $B$ is **homogeneous of degree two**, $B(\lambda\tilde Q)=\lambda^{2}B(\tilde Q)$ for $\lambda\in\mathbb{C}$, and its polarisation is the form of the same letter, $B(\tilde P+\tilde Q)-B(\tilde P)-B(\tilde Q)=2B(\tilde P,\tilde Q)$.
- $B$ is **not positive definite** and **not definite**.
- Its Gram matrix on the basis is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and the realification of $B$ is non-degenerate of signature $(4,4)$ on $\mathbb{B}\cong\mathbb{R}^{8}$.
- Its **vanishing set** is the complex cone $\{B(\tilde Q)=0\}$, the complex quadric of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, and not the zero-divisor set of the block.

## The Algebraic Norm Is Not Multiplicative

**The algebraic norm of the block is not multiplicative:** $B(\tilde P\bullet\tilde Q)\neq B(\tilde P)B(\tilde Q)$ in general, the pair $(e_1,e_2)$ separating the two sides.

**Proposition.** The algebraic norm of the block is **not** multiplicative:

$$
B(\tilde P\bullet\tilde Q)\neq B(\tilde P)\,B(\tilde Q)\quad\text{in general.}
$$

*Proof.* The pair $e_1,e_2$ separates the two sides: $e_1\bullet e_2=\tfrac12(e_1e_2+e_2e_1)=\tfrac12(e_3-e_3)=0$, so $B(e_1\bullet e_2)=B(0)=0$, while $B(e_1)B(e_2)=(-1)(-1)=1$. The two values differ, so no multiplicativity holds.

**Remark (the multiplicative algebraic norm is another form).** Of the four algebraic norms of the space the multiplicative one is $N$, the algebraic norm of the quaternionic product, $N(\tilde Q)=\sum_\mu Q_\mu^{2}$; it is a different quadratic form on the same space, and the block, whose product is not associative and has zero divisors, fails multiplicativity for its own algebraic norm $B$. The multiplicativity that the block does retain is the one of the quadratic representation of the Jordan theory, a statement about a different quadratic form and not about $B$.

## The Unit and the Degeneracy of the Naive Inverse

**The block is commutative and unital with unit $e_0$, but it is not associative, and its naive inverse equation $\tilde Q\bullet\tilde R=e_0$ is degenerate: the element $\tilde\Upsilon=e_1+ie_2$ satisfies it for a two-dimensional affine family of $\tilde R$.**

The unit of the block is $e_0$: the product is commutative, so its one-sided inverse equations coincide, and $e_0$ is the two-sided unit (*Introduction to the Symmetric Plain Algebra of Biquaternions*). The block is **not associative**: $(\tilde P\bullet\tilde Q)\bullet\tilde R\neq\tilde P\bullet(\tilde Q\bullet\tilde R)$ in general, and the single equation $\tilde Q\bullet\tilde R=e_0$ is **degenerate**: the element $\tilde\Upsilon=e_1+ie_2$ satisfies $\tilde\Upsilon\bullet\tilde R=e_0$ for a two-dimensional affine family of $\tilde R$, because its left multiplication has a two-dimensional kernel. The naive inverse equation therefore does not define an inverse, and the block is treated with the inverse of the Jordan theory in *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm does not decide invertibility:** $B(\tilde Q)=0$ does not force $\tilde Q$ non-invertible, and $B(\tilde Q)\neq0$ does not force $\tilde Q$ invertible.

The algebraic norm of a product would decide invertibility if the invertible elements were exactly the elements of non-vanishing algebraic norm. For the block that statement is **false in both directions**, and the article records the absence rather than a criterion.

**Theorem (the algebraic norm does not decide invertibility).** Neither implication holds:

$$
B(\tilde Q)=0\ \not\Longrightarrow\ \tilde Q\text{ non-invertible},
\qquad
B(\tilde Q)\neq0\ \not\Longrightarrow\ \tilde Q\text{ invertible}.
$$

*Proof.* For the first implication, the element $\tilde Q=e_0+e_1$ has $B(\tilde Q)=1^{2}-1^{2}=0$, and it is invertible: $(e_0+e_1)\bullet\tfrac12(e_0-e_1)=\tfrac12(e_0+e_1)(e_0-e_1)=\tfrac12\cdot2e_0=e_0$ and $\tilde Q^{\bullet2}\bullet\tfrac12(e_0-e_1)=\tilde Q$, so $\tfrac12(e_0-e_1)$ is its inverse of the block. For the second implication, the element $\tilde Q=e_0+ie_1$ has $B(\tilde Q)=1^{2}-(i)^{2}=1+1=2\neq0$, and it is a zero divisor, $(e_0+ie_1)(e_0-ie_1)=e_0^{2}-(ie_1)^{2}=e_0-e_0=0$, hence non-invertible while its algebraic norm does not vanish.

**Remark (the two witnesses).** The element $e_0+e_1$ is invertible with vanishing algebraic norm, so the algebraic norm is not necessary for invertibility; the element $e_0+ie_1$ is non-invertible with non-vanishing algebraic norm, so it is not sufficient either. The vanishing set of $B$ is the complex cone and the zero-divisor set is the cone of a different quadratic form; the two cones meet but neither contains the other.

**Remark (what replaces the criterion).** The block is not left without an invertibility theory: it is commutative and unital, the Jordan inverse is defined by its two equations, and the zero divisors are characterised in *Zero Divisors of the Symmetric Plain Algebra*. That theory is **not** read from the algebraic norm of the block, which is the one algebraic norm the block carries; the criterion it uses is carried by a different quadratic form and belongs to the article that owns that form.

## Summary

The symmetric plain product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ carries one algebraic norm, the diagonal of its scalar-part form, the general plain bilinear algebraic norm

$$
B(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\bullet\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},
$$

complex-valued, of Gram matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, with the complex cone as its vanishing set, and it is **not multiplicative**, the pair $(e_1,e_2)$ separating the two sides, $B(e_1\bullet e_2)=B(0)=0$ against $B(e_1)B(e_2)=1$.

The block is commutative and unital, with the unit $e_0$, and it is not associative, the naive inverse equation $\tilde Q\bullet\tilde R=e_0$ being degenerate at $\tilde\Upsilon=e_1+ie_2$. Its algebraic norm does **not** decide invertibility: the invertible element $e_0+e_1$ has $B=0$ and the zero divisor $e_0+ie_1$ has $B=2$, so the non-vanishing of the algebraic norm is neither necessary nor sufficient. The article records that absence; the invertibility the block does have is the invertibility of the Jordan theory, carried by a different quadratic form, which is not the algebraic norm of the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | the symmetric plain product, the multiplication of the block |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the general plain bilinear form, the scalar-part form of the product |
| $B(\tilde Q)=B(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2}$ | the algebraic norm of the block, one of the four algebraic norms of the space |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $B$; the signature of its realification is $(4,4)$ |
| $\{B(\tilde Q)=0\}$ | the complex cone, the vanishing set of the algebraic norm |
| $e_0$ | the two-sided unit of the block |
| $\tilde\Upsilon=e_1+ie_2$ | the witness of the degeneracy of the naive inverse equation |
| $e_0+e_1$, $e_0+ie_1$ | the witnesses: invertible with $B=0$, and zero divisor with $B=2$ |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the general plain bilinear form $B$ and the table of the four forms.
- *Introduction to the Symmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-biquaternions.md`), for the product, its unit, its commutativity and its non-associativity.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra* (`articles_maths/the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra.md`), for the form the algebraic norm polarises.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.md`), for the invertibility the block does have, carried by a different quadratic form.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Unit and the Inverse*, for the relative definitions of the unit and the inverse.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra.md`), for the zero divisors, which the algebraic norm of the block does not detect.
- *Remarkable Subspaces and the Four Algebraic Norms* (`articles_maths/remarkable-subspaces-and-the-four-algebraic-norms.md`), for the restriction of $B$ to the remarkable subspaces with its signature.
