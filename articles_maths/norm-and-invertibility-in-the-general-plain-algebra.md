# __Norm and Invertibility in the General Plain Algebra__

## Introduction

This article studies the algebraic norm that the general plain bilinear product, the multiplication $\tilde P\tilde Q$ of the general plain algebra, carries, and the invertibility of the elements of that product.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*: for the plain product the form is $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$ and its diagonal is

$$
B(\tilde Q)=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},
$$

one of the four algebraic norms of the space and not one of the other three. The article defines it, records its field of values, its Gram matrix, its signature and its vanishing set, and proves that it is **not** multiplicative; that is the whole of the algebraic norm of the plain product.

The invertibility is where the article records an **absence**. The plain product is associative and unital, so its invertible elements and its group of units are defined; but the algebraic norm of the product does **not** decide them. The element $e_0+e_1$ is invertible and satisfies $B(e_0+e_1)=0$, and the element $e_0+ie_1$ is a zero divisor and satisfies $B(e_0+ie_1)=2$: the non-vanishing of the algebraic norm is neither necessary nor sufficient for invertibility, and the article states that absence rather than a criterion. The criterion of the plain product is furnished by a different quadratic form, which is not the algebraic norm of the plain product and is not studied here; the zero divisors are *Zero Divisors of the General Plain Algebra*.

**The results.** The plain product carries one algebraic norm, the diagonal of its scalar-part form, $B(\tilde Q)=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2}$, complex-valued and indefinite, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, with the complex cone as its vanishing set. It is **not multiplicative**. It does **not** decide invertibility: $B(\tilde Q)=0$ does not force $\tilde Q$ non-invertible, and $B(\tilde Q)\neq0$ does not force $\tilde Q$ invertible. Each section below states its result first and then proves it.

**Boundaries.** The three other algebraic norms of the space are *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*, and they are not read here: the general quaternionic algebraic norm $N$ is that of the quaternionic algebra, the general plain sesquilinear algebraic norm $H$ is that of the general plain sesqualgebra, and the general quaternionic sesquilinear algebraic norm $K$ is that of the general quaternionic sesqualgebra. The product and its element theory are *Introduction to the General Plain Algebra of Biquaternions*; the conjugations and the remarkable subspaces are the basic algebra article; the unit tables of the four products are *Comparison Between the Four General Products*; the definitions of the unit, the inverse and the group of units are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$, with $e_1e_2=e_3$, $e_k^{2}=-e_0$ and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written in the centre–vector split $\tilde Q=Q_0e_0+\vec Q$ with $\vec Q=\sum_{k=1}^{3}Q_ke_k$. The scalar part is $\mathrm{Sc}$, the natural conjugation is $\tilde Q^{\natural}=Q_0-\vec Q$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$, and $(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k$ is the complex bilinear dot product of the vector parts. Throughout this article the product is the general plain bilinear product, written by juxtaposition, $\tilde P\tilde Q$.

## The Algebraic Norm of the Plain Product

**The general plain bilinear product carries exactly one algebraic norm**, the diagonal of its scalar-part form, $B(\tilde Q)=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2}$; it is complex-valued and indefinite, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, and its vanishing set is the complex cone.

**Definition.** The **algebraic norm of the plain product** is the diagonal of the scalar-part form of the product,

$$
B(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},
$$

equivalently $B(\tilde Q)=B(\tilde Q,\tilde Q)$ for the form

$$
B(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu Q_\mu=P_0Q_0-(\vec P,\vec Q),
$$

which is the general plain bilinear form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, the $\mathbb{C}$-bilinear form of the pair $(\mathrm{id},\mathrm{id})$. The two arities of the letter are one object: with two arguments the form, with one argument its diagonal.

The form is symmetric, $B(\tilde P,\tilde Q)=B(\tilde Q,\tilde P)$, and non-degenerate, and on the diagonal the splitting of the coefficients into real and imaginary parts gives

$$
\operatorname{Re}B=\sum_{\mu=0}^{3}\bigl(q_\mu^{2}-(q'_\mu)^{2}\bigr),\qquad \operatorname{Im}B=2\sum_{\mu=0}^{3}q_\mu q'_\mu,\qquad Q_\mu=q_\mu+iq'_\mu .
$$

**Basic properties.** Each is a direct reading of the definition.

- $B(\tilde Q)$ is **complex-valued** in general, a complex multiple of $e_0$; it is real exactly on the union of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and its imaginary translate $i\mathbb{H}_{\mathbb{B}}$.
- $B$ is **homogeneous of degree two**, $B(\lambda\tilde Q)=\lambda^{2}B(\tilde Q)$ for $\lambda\in\mathbb{C}$, and its polarisation is the form of the same letter, $B(\tilde P+\tilde Q)-B(\tilde P)-B(\tilde Q)=2B(\tilde P,\tilde Q)$.
- $B$ is **not positive definite** and **not definite**: it takes complex values and it vanishes on nonzero elements.
- Its Gram matrix on the basis $e_0,e_1,e_2,e_3$ is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and the realification of $B$ on $\mathbb{B}\cong\mathbb{R}^{8}$ is non-degenerate of signature $(4,4)$, a split signature.
- Its **vanishing set** is the complex cone $\{B(\tilde Q)=0\}$, the complex quadric of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; it is the vanishing set of the algebraic norm of the plain product and not the zero-divisor cone of the algebra.

## The Algebraic Norm Is Not Multiplicative

**The algebraic norm of the plain product is not multiplicative:** $B(\tilde P\tilde Q)\neq B(\tilde P)B(\tilde Q)$ in general, the pair $(e_1,e_2)$ separating the two sides.

**Proposition.** The algebraic norm of the plain product is **not** multiplicative:

$$
B(\tilde P\tilde Q)\neq B(\tilde P)\,B(\tilde Q)\quad\text{in general.}
$$

*Proof.* The pair $\tilde P=e_1$, $\tilde Q=e_2$ separates the two sides: $e_1e_2=e_3$, so $B(\tilde P\tilde Q)=B(e_3)=-1$, while $B(e_1)B(e_2)=(-1)(-1)=1$. The two values differ, so no multiplicativity holds.

**Remark (the multiplicative algebraic norm is another form).** Of the four algebraic norms of the space the multiplicative one is $N$, the algebraic norm of the quaternionic product, $N(\tilde Q)=\sum_\mu Q_\mu^{2}$; it is a different quadratic form on the same space, and it is not the algebraic norm of the plain product. The plain product is the ordinary multiplication of an algebra that has zero divisors, and its algebraic norm $B$, complex-valued and indefinite, fails multiplicativity outright.

## The Unit and the Group of Units

**The plain product is associative and unital, with the two-sided unit $e_0$, and its invertible elements form the group of units $\mathbb{B}^{\times}$, a proper subset of $\mathbb{B}\setminus\{0\}$ because the product has zero divisors.**

The unit of the plain product is $e_0$: it is a two-sided unit, $\tilde Q e_0=e_0\tilde Q=\tilde Q$, and it is the only one (*Introduction to the General Plain Algebra of Biquaternions*; *Comparison Between the Four General Products*). The product is associative, so the inverse of an element is unique when it exists and the invertible elements form the **group of units** of the plain product, a genuine group (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*).

The plain product has zero divisors: the identity $(e_0+ie_1)(e_0-ie_1)=e_0^{2}-(ie_1)^{2}=e_0-e_0=0$ exhibits a product of two nonzero elements that is zero. The plain algebra is therefore not a division algebra, and the group of units is a proper subset of $\mathbb{B}\setminus\{0\}$. The zero divisors, their families and their geometry are *Zero Divisors of the General Plain Algebra*, and they are cited here, not read.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm does not decide invertibility:** $B(\tilde Q)=0$ does not force $\tilde Q$ non-invertible, and $B(\tilde Q)\neq0$ does not force $\tilde Q$ invertible.

The algebraic norm of a product would decide invertibility if the invertible elements were exactly the elements of non-vanishing algebraic norm. For the plain product that statement is **false in both directions**, and the article records the absence rather than a criterion.

**Theorem (the algebraic norm does not decide invertibility).** Neither implication holds:

$$
B(\tilde Q)=0\ \not\Longrightarrow\ \tilde Q\text{ non-invertible},
\qquad
B(\tilde Q)\neq0\ \not\Longrightarrow\ \tilde Q\text{ invertible}.
$$

*Proof.* For the first implication, the element $\tilde Q=e_0+e_1$ has $B(\tilde Q)=1^{2}-1^{2}=0$, and it is a unit of the plain product: $(e_0+e_1)(e_0-e_1)=e_0^{2}-e_0e_1+e_1e_0-e_1^{2}=e_0-e_1+e_1+e_0=2e_0$, so $\tilde Q^{-1}=\tfrac12(e_0-e_1)$ and $\tilde Q$ is invertible while its algebraic norm vanishes. For the second implication, the element $\tilde Q=e_0+ie_1$ has $B(\tilde Q)=1^{2}-(i)^{2}=1+1=2\neq0$, and it is a zero divisor, $(e_0+ie_1)(e_0-ie_1)=e_0^{2}-(ie_1)^{2}=e_0-e_0=0$, hence non-invertible while its algebraic norm does not vanish.

**Remark (the two witnesses).** The two witnesses are the two halves of the failure. The element $e_0+e_1$ is invertible with vanishing algebraic norm, so the algebraic norm is not necessary for invertibility; the element $e_0+ie_1$ is non-invertible with non-vanishing algebraic norm, so it is not sufficient either. The vanishing set of $B$ is the complex cone, and the zero-divisor set is the cone of a different quadratic form; the two cones meet but neither contains the other, and that is the geometric form of the absence.

**Remark (what replaces the criterion).** The plain product is not left without an invertibility theory: it is associative and unital, every element of its group of units has an inverse, and the zero divisors are characterised in *Zero Divisors of the General Plain Algebra*. What the article records is that this theory is **not** read from the algebraic norm of the plain product, which is the one algebraic norm the product carries; the criterion that does exist is carried by a different quadratic form and belongs to the articles that own that form.

## Summary

The general plain bilinear product $\tilde P\tilde Q$ carries one algebraic norm, the diagonal of its scalar-part form, the general plain bilinear algebraic norm

$$
B(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},
$$

complex-valued, of Gram matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, with the complex cone as its vanishing set, and it is **not multiplicative**, the pair $(e_1,e_2)$ separating the two sides, $B(e_1e_2)=B(e_3)=-1$ against $B(e_1)B(e_2)=1$.

The plain product is associative and unital, with the two-sided unit $e_0$ and a genuine group of units, and it has zero divisors, $(e_0+ie_1)(e_0-ie_1)=0$. Its algebraic norm does **not** decide invertibility: the invertible element $e_0+e_1$ has $B=0$ and the zero divisor $e_0+ie_1$ has $B=2$, so the non-vanishing of the algebraic norm is neither necessary nor sufficient. The article records that absence; the criterion the plain product does have is carried by a different quadratic form, which is not the algebraic norm of the plain product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\tilde Q$ | the general plain bilinear product, the multiplication of the general plain algebra |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the general plain bilinear form, the scalar-part form of the product |
| $B(\tilde Q)=B(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2}$ | the algebraic norm of the plain product, one of the four algebraic norms of the space |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $B$; the signature of its realification is $(4,4)$ |
| $\{B(\tilde Q)=0\}$ | the complex cone, the vanishing set of the algebraic norm; not the zero-divisor set |
| $e_0$ | the two-sided unit of the plain product |
| $\mathbb{B}^{\times}$ | the group of units of the plain product, not read from $B$ |
| $e_0+e_1$, $e_0+ie_1$ | the witnesses: invertible with $B=0$, and zero divisor with $B=2$ |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the definition of the algebraic norm as the form at the two equal arguments, the four algebraic norms and their separation.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the general plain bilinear form $B$, the table of the four forms and the complex quadric that is the vanishing set of $B$.
- *Introduction to the General Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-biquaternions.md`), for the product, its associativity, its unit and its element theory.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), §*The Unit and the Inverse*, for the relative definitions of the unit, the inverse and the group of units.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the unit table of the four products and the fact that they do not share their units.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the zero divisors, which the algebraic norm of the plain product does not detect.
- *Remarkable Subspaces and the Four Algebraic Norms* (`articles_maths/remarkable-subspaces-and-the-four-algebraic-norms.md`), for the restriction of $B$ to the remarkable subspaces with its signature.
