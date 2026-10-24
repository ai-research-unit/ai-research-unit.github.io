# __Norm and Invertibility in the Biquaternion Algebra__

## Introduction

This article studies the algebraic norm that the general plain bilinear product, the multiplication $\tilde Q_2\tilde Q_1$ of the biquaternion algebra, carries, and the invertibility of the elements of that product.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The Four Forms and the Four Algebraic Norms*: for the plain product the form is $\langle\tilde Q_2,\tilde Q_1\rangle=\mathrm{Sc}(\tilde Q_2\tilde Q_1)$ and its diagonal is

$$
\langle\tilde Q\rangle=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

one of the four algebraic norms of the space and not one of the other three. The article defines it, records its field of values, its Gram matrix, its signature and its vanishing set, and proves that it is **not** multiplicative; that is the whole of the algebraic norm of the plain product.

The invertibility is where the article records an **absence**. The plain product is associative and unital, so its invertible elements and its group of units are defined; but the algebraic norm of the product does **not** decide them. The element $e_t+\vec e_x$ is invertible and satisfies $\langle e_t+\vec e_x\rangle=0$, and the element $e_t+i\vec e_x$ is a zero divisor and satisfies $\langle e_t+i\vec e_x\rangle=2$: the non-vanishing of the algebraic norm is neither necessary nor sufficient for invertibility, and the article states that absence rather than a criterion. The criterion of the plain product is furnished by a different quadratic form, which is not the algebraic norm of the plain product and is not studied here; the zero divisors are *Zero Divisors of the Biquaternion Algebra*.

**The results.** The plain product carries one algebraic norm, the diagonal of its scalar-part form, $\langle\tilde Q\rangle=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$, complex-valued and indefinite, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, with the complex cone as its vanishing set. It is **not multiplicative**. It does **not** decide invertibility: $\langle\tilde Q\rangle=0$ does not force $\tilde Q$ non-invertible, and $\langle\tilde Q\rangle\neq0$ does not force $\tilde Q$ invertible. Each section below states its result first and then proves it.

## The Algebraic Norm of the Plain Product

**The general plain bilinear product carries exactly one algebraic norm**, the diagonal of its scalar-part form, $\langle\tilde Q\rangle=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$; it is complex-valued and indefinite, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, and its vanishing set is the complex cone.

**Definition.** The **algebraic norm of the plain product** is the diagonal of the scalar-part form of the product,

$$
\langle\tilde Q\rangle=\mathrm{Sc}\bigl(\tilde Q\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

equivalently $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle$ for the form

$$
\langle\tilde Q_2,\tilde Q_1\rangle=\mathrm{Sc}\bigl(\tilde Q_2\tilde Q_1\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{2\mu} Q_{1\mu}=Q_{2,0}Q_{1t}-(\vec Q_2,\vec Q_1),
$$

which is the general plain bilinear form of *The Four Forms and the Four Algebraic Norms*, the $\mathbb{C}$-bilinear form of the pair $(\mathrm{id},\mathrm{id})$. The two arities of the letter are one object: with two arguments the form, with one argument its diagonal.

The form is symmetric, $\langle\tilde Q_2,\tilde Q_1\rangle=\langle\tilde Q_1,\tilde Q_2\rangle$, and non-degenerate, and on the diagonal the splitting of the coefficients into real and imaginary parts gives

$$
\boxed{\;
\operatorname{Re}B=\sum_{\mu\in\{t,x,y,z\}}\bigl(q_\mu^{2}-(q'_\mu)^{2}\bigr),\qquad \operatorname{Im}B=2\sum_{\mu\in\{t,x,y,z\}}q_\mu q'_\mu,\qquad Q_\mu=q_\mu+iq'_\mu
\;}.
$$

**Basic properties.** Each is a direct reading of the definition.

- $\langle\tilde Q\rangle$ is **complex-valued** in general, a complex multiple of $e_t$; it is real exactly on the union of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and its imaginary translate $i\mathbb{H}_{\mathbb{B}}$.
- $\langle\cdot\rangle$ is **homogeneous of degree two**, $\langle\lambda\tilde Q\rangle=\lambda^{2}\langle\tilde Q\rangle$ for $\lambda\in\mathbb{C}$, and its polarisation is the form of the same letter, $\langle\tilde Q_2+\tilde Q_1\rangle-\langle\tilde Q_2\rangle-\langle\tilde Q_1\rangle=2\langle\tilde Q_2,\tilde Q_1\rangle$.
- $\langle\cdot\rangle$ is **not positive definite** and **not definite**: it takes complex values and it vanishes on nonzero elements.
- Its Gram matrix on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and the realification of $\langle\cdot\rangle$ on $\mathbb{B}\cong\mathbb{R}^{8}$ is non-degenerate of signature $(4,4)$, a split signature.
- Its **vanishing set** is the complex cone $\{\langle\tilde Q\rangle=0\}$, the complex quadric of *The Four Forms and the Four Algebraic Norms*; it is the vanishing set of the algebraic norm of the plain product and not the zero-divisor cone of the algebra.

## The Algebraic Norm Is Not Multiplicative

**The algebraic norm of the plain product is not multiplicative:** $\langle\tilde Q_2\tilde Q_1\rangle\neq \langle\tilde Q_2\rangle\langle\tilde Q_1\rangle$ in general, the pair $(\vec e_x,\vec e_y)$ separating the two sides.

**Proposition.** The algebraic norm of the plain product is **not** multiplicative:

$$
\boxed{\;
\langle\tilde Q_2\tilde Q_1\rangle\neq \langle\tilde Q_2\rangle\,\langle\tilde Q_1\rangle\quad\text{in general.}
\;}
$$

*Proof.* The pair $\tilde Q_2=\vec e_x$, $\tilde Q_1=\vec e_y$ separates the two sides: $\vec e_x\vec e_y=\vec e_z$, so $\langle\tilde Q_2\tilde Q_1\rangle=\langle \vec e_z\rangle=-1$, while $\langle \vec e_x\rangle\langle \vec e_y\rangle=(-1)(-1)=1$. The two values differ, so no multiplicativity holds.

**Remark (the multiplicative algebraic norm is another form).** Of the four algebraic norms of the space the multiplicative one is $\langle\cdot\rangle_{\natural}$, the algebraic norm of the quaternionic product, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$; it is a different quadratic form on the same space, and it is not the algebraic norm of the plain product. The plain product is the ordinary multiplication of an algebra that has zero divisors, and its algebraic norm $\langle\cdot\rangle$, complex-valued and indefinite, fails multiplicativity outright.

## The Unit and the Group of Units

**The plain product is associative and unital, with the two-sided unit $e_t$, and its invertible elements form the group of units $\mathbb{B}^{\times}$, a proper subset of $\mathbb{B}\setminus\{0\}$ because the product has zero divisors.**

The unit of the plain product is $e_t$: it is a two-sided unit, $\tilde Q e_t=e_t\tilde Q=\tilde Q$, and it is the only one (*The Biquaternion Algebra and Its Vector Spaces*; *The Four General Products and Their Relations*). The product is associative, so the inverse of an element is unique when it exists and the invertible elements form the **group of units** of the plain product, a genuine group (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*).

The plain product has zero divisors: the identity $(e_t+i\vec e_x)(e_t-i\vec e_x)=e_t^{2}-(i\vec e_x)^{2}=e_t-e_t=0$ exhibits a product of two nonzero elements that is zero. The plain algebra is therefore not a division algebra, and the group of units is a proper subset of $\mathbb{B}\setminus\{0\}$. The zero divisors, their families and their geometry are *Zero Divisors of the Biquaternion Algebra*, and they are cited here, not read.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm does not decide invertibility:** $\langle\tilde Q\rangle=0$ does not force $\tilde Q$ non-invertible, and $\langle\tilde Q\rangle\neq0$ does not force $\tilde Q$ invertible.

The algebraic norm of a product would decide invertibility if the invertible elements were exactly the elements of non-vanishing algebraic norm. For the plain product that statement is **false in both directions**, and the article records the absence rather than a criterion.

**Theorem (the algebraic norm does not decide invertibility).** Neither implication holds:

$$
\boxed{\;
\langle\tilde Q\rangle=0\ \not\Longrightarrow\ \tilde Q\text{ non-invertible},
\qquad
\langle\tilde Q\rangle\neq0\ \not\Longrightarrow\ \tilde Q\text{ invertible}
\;}.
$$

*Proof.* For the first implication, the element $\tilde Q=e_t+\vec e_x$ has $\langle\tilde Q\rangle=1^{2}-1^{2}=0$, and it is a unit of the plain product: $(e_t+\vec e_x)(e_t-\vec e_x)=e_t^{2}-e_t\vec e_x+\vec e_xe_t-\vec e_x^{2}=e_t-\vec e_x+\vec e_x+e_t=2e_t$, so $\tilde Q^{-1}=\tfrac12(e_t-\vec e_x)$ and $\tilde Q$ is invertible while its algebraic norm vanishes. For the second implication, the element $\tilde Q=e_t+i\vec e_x$ has $\langle\tilde Q\rangle=1^{2}-(i)^{2}=1+1=2\neq0$, and it is a zero divisor, $(e_t+i\vec e_x)(e_t-i\vec e_x)=e_t^{2}-(i\vec e_x)^{2}=e_t-e_t=0$, hence non-invertible while its algebraic norm does not vanish.

**Remark (the two witnesses).** The two witnesses are the two halves of the failure. The element $e_t+\vec e_x$ is invertible with vanishing algebraic norm, so the algebraic norm is not necessary for invertibility; the element $e_t+i\vec e_x$ is non-invertible with non-vanishing algebraic norm, so it is not sufficient either. The vanishing set of $\langle\cdot\rangle$ is the complex cone, and the zero-divisor set is the cone of a different quadratic form; the two cones meet but neither contains the other, and that is the geometric form of the absence.

**Remark (what replaces the criterion).** The plain product is not left without an invertibility theory: it is associative and unital, every element of its group of units has an inverse, and the zero divisors are characterised in *Zero Divisors of the Biquaternion Algebra*. What the article records is that this theory is **not** read from the algebraic norm of the plain product, which is the one algebraic norm the product carries; the criterion that does exist is carried by a different quadratic form and belongs to the articles that own that form.

## Summary

The general plain bilinear product $\tilde Q_2\tilde Q_1$ carries one algebraic norm, the diagonal of its scalar-part form, the general plain bilinear algebraic norm

$$
\langle\tilde Q\rangle=\mathrm{Sc}\bigl(\tilde Q\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

complex-valued, of Gram matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ and realification of signature $(4,4)$, with the complex cone as its vanishing set, and it is **not multiplicative**, the pair $(\vec e_x,\vec e_y)$ separating the two sides, $\langle \vec e_x\vec e_y\rangle=\langle \vec e_z\rangle=-1$ against $\langle \vec e_x\rangle\langle \vec e_y\rangle=1$.

The plain product is associative and unital, with the two-sided unit $e_t$ and a genuine group of units, and it has zero divisors, $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$. Its algebraic norm does **not** decide invertibility: the invertible element $e_t+\vec e_x$ has $\langle\cdot\rangle=0$ and the zero divisor $e_t+i\vec e_x$ has $\langle\cdot\rangle=2$, so the non-vanishing of the algebraic norm is neither necessary nor sufficient. The article records that absence; the criterion the plain product does have is carried by a different quadratic form, which is not the algebraic norm of the plain product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_2, \tilde Q_1$ | the two elements of a product, first and second slot |
| $\tilde Q_2\tilde Q_1$ | the general plain bilinear product, the multiplication of the biquaternion algebra |
| $\langle\tilde Q_2,\tilde Q_1\rangle=\mathrm{Sc}(\tilde Q_2\tilde Q_1)=\sum_\mu\varepsilon_\mu Q_{2\mu} Q_{1\mu}$ | the general plain bilinear form, the scalar-part form of the product |
| $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$ | the algebraic norm of the plain product, one of the four algebraic norms of the space |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $\langle\cdot\rangle$; the signature of its realification is $(4,4)$ |
| $\{\langle\tilde Q\rangle=0\}$ | the complex cone, the vanishing set of the algebraic norm; not the zero-divisor set |
| $e_t$ | the two-sided unit of the plain product |
| $\mathbb{B}^{\times}$ | the group of units of the plain product, not read from $\langle\cdot\rangle$ |
| $e_t+\vec e_x$, $e_t+i\vec e_x$ | the witnesses: invertible with $\langle\cdot\rangle=0$, and zero divisor with $\langle\cdot\rangle=2$ |

## Further Reading

- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the definition of the algebraic norm as the form at the two equal arguments, the four algebraic norms and their separation.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the general plain bilinear form $\langle\cdot,\cdot\rangle$, the table of the four forms and the complex quadric that is the vanishing set of $\langle\cdot,\cdot\rangle$.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the product, its associativity, its unit and its element theory.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the relative definitions of the unit, the inverse and the group of units.
- [The Four General Products and Their Relations](the-four-general-products-and-their-relations.html), for the unit table of the four products and the fact that they do not share their units.
- [Zero Divisors of the Biquaternion Algebra](zero-divisors-of-the-biquaternion-algebra.html), for the zero divisors, which the algebraic norm of the plain product does not detect.
- [Remarkable Subspaces and the Four Algebraic Norms](remarkable-subspaces-and-the-four-algebraic-norms.html), for the restriction of $\langle\cdot\rangle$ to the remarkable subspaces with its signature.
