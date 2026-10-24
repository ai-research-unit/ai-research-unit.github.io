# __Norm and Invertibility in the Antisymmetric Plain Sesqualgebra__

## Introduction

This article studies the algebraic norm and the invertibility of the antisymmetric plain sesqualgebra

$$
\tilde Q_1\diamond\tilde Q_2=\operatorname{Vect}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)
=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}}\bigr)
=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2},
$$

the antisymmetric half of the general plain sesquilinear product, the operation $\mathrm{APS}$ of *Introduction to the Antisymmetric Plain Sesqualgebra*. The operation is $\mathbb{C}$-bilinear in the first slot, conjugate-linear in the second, vector valued, and it has no unit on either side.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The Four Forms and the Four Algebraic Norms*. For the block the scalar part is identically zero, $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$, because every value is a pure vector; the algebraic norm of the operation is therefore **the zero function**, and by the convention of the same article a vanishing quadratic form is not an algebraic norm, so the block is counted with **no algebraic norm** rather than with a zero one.

Both notions of the title are therefore **absences**. The block has no two-sided unit, so no element is invertible and the group of units is empty; the one-sided inverse equations to the centre have no solution. What replaces the invertibility is not a norm but an operator reading: the one-sided multiplication by an element has a kernel and an image, and the relative inverse below accounts for the loss on the quotient.

**The results.** The block has **no algebraic norm**: its scalar part vanishes identically, $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$, so the diagonal is the zero function and, by the convention that a vanishing quadratic form is not an algebraic norm, the block is counted with no algebraic norm rather than a zero one. It has **no unit** on either side, hence **no invertible element** and an **empty group of units**, and the one-sided inverse equations $\tilde Q\diamond\tilde Q_2=e_t$ and $\tilde Q_2\diamond\tilde Q=e_t$ have **no solution**, because every value of the block is a pure vector. The invertibility criterion of the parent is **not transferred**: the form $\langle\cdot,\cdot\rangle_{*}$ is not the algebraic norm of the block and is not read here. What replaces the inverse is the operator reading, in which the multiplication by a non-central $\tilde Q_3$ has the complex plane $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$ as its kernel and induces a conjugate-linear bijection of the quotient onto the plane of the values orthogonal to $\vec Q_3$.

## The Relative Definitions

The word *unit* and the word *inverse* name a product, so the definitions are stated once for a general product and read on the block; they are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*.

**Definition (unit).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, a **right unit** when $\tilde Q_1\star e=\tilde Q_1$ for every $\tilde Q_1$, and a **two-sided unit** when it is both. A product with a two-sided unit is **unital**.

**Definition (inverse and group of units).** Let $\star$ be a unital product with identity $e$. An element $\tilde Q$ is **left-invertible of $\star$** when there is $\tilde Q_2$ with $\tilde Q_2\star\tilde Q=e$, **right-invertible** when there is $\tilde Q_2$ with $\tilde Q\star\tilde Q_2=e$, and **invertible** when there is $\tilde Q_2$ with $\tilde Q\star\tilde Q_2=\tilde Q_2\star\tilde Q=e$. Such an $\tilde Q_2$ is the **inverse of $\tilde Q$**, and in an associative unital product the invertible elements form the **group of units**.

Throughout this article the product is the block $\diamond$, and, unqualified, *unit* and *inverse* are read in $\diamond$.

## The Absence of a Unit

**The block has neither a left unit nor a right unit:** there is no element $\tilde u$ with $\tilde u\diamond\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, and none with $\tilde Q_1\diamond\tilde u=\tilde Q_1$ for every $\tilde Q_1$, because every value of the block is a pure vector of scalar part zero while $e_t$ has scalar part one.

**Theorem (no unit).** The block has neither a left unit nor a right unit. There is no element $\tilde u$ with $\tilde u\diamond\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, and none with $\tilde Q_1\diamond\tilde u=\tilde Q_1$ for every $\tilde Q_1$.

*Proof.* The two one-sided actions of $e_t$ are

$$
\tilde Q_1\diamond e_t=\vec Q_1,\qquad e_t\diamond\tilde Q=-\overline{\vec Q},
$$

the first being $\operatorname{Vect}(\tilde Q_1)$ and the second $\operatorname{Vect}(\tilde Q^{*})$. A left unit $\tilde u$ would satisfy, at $\tilde Q_1=e_t$, the equation $\tilde u\diamond e_t=e_t$, that is $\vec q=e_t$; the left member is a vector part, of scalar part zero, while the right member has scalar part one, so the equation is impossible. A right unit $\tilde u$ would satisfy, at $\tilde Q_1=e_t$, the equation $e_t\diamond\tilde u=e_t$, that is $-\overline{\vec q}=e_t$; the same parity of the scalar part forbids it.

The obstruction is the projection: every value of the block is a pure vector, so its scalar part vanishes, while the unit $e_t$ has scalar part one. The block cannot see the unit of the space on either side, and the two displays above are the two one-sided actions that replace it. The parent product $\tilde Q_1\tilde Q_2^{*}$ has the right unit $e_t$, and the block destroys it: the right-unit equation survives on the vector subspace alone and fails at every element with a non-zero scalar part.

## The Absence of an Inverse

**No element of the block is invertible and the group of units is empty**, and the one-sided inverse equations $\tilde Q\diamond\tilde Q_2=e_t$ and $\tilde Q_2\diamond\tilde Q=e_t$ have no solution, because each left member is a pure vector and $e_t$ is not.

**Corollary (no inverse, no group of units).** No element of $\mathbb{B}$ is invertible of the block, and the group of units of $\diamond$ is empty.

*Proof.* The inverse is defined relative to a two-sided unit, and the two-sided unit does not exist; the definition has no instance in the block, and the symbol $\tilde Q^{-1}$ read with the product of the block names nothing. The group of units is the empty set.

**Proposition (the one-sided equations have no solution).** For every $\tilde Q$ the two equations

$$
\tilde Q\diamond\tilde Q_2=e_t,\qquad \tilde Q_2\diamond\tilde Q=e_t
$$

have no solution $\tilde Q_2$.

*Proof.* Each left member is a value of the block, hence a pure vector of scalar part zero; the right member $e_t$ has scalar part one. A pure vector is never $e_t$, so neither equation holds.

## The Algebraic Norm of the Block

**The algebraic norm of the block is the zero function**, $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$ for all $\tilde Q_1,\tilde Q_2$ and $\varphi_{\diamond}(\tilde Q)=0$ for all $\tilde Q$, and by the convention that a vanishing quadratic form is not an algebraic norm the block carries **no algebraic norm**.

**Definition (the algebraic norm of the operation).** Let $f$ be an operation on $\mathbb{B}$ with scalar-part form $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The **algebraic norm of $f$** is the diagonal of that form,

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)=\mathrm{Sc}\,f(\tilde Q,\tilde Q),
$$

and for an operation whose scalar part vanishes identically the algebraic norm is the zero function (*The Four Forms and the Four Algebraic Norms*).

**Theorem (the algebraic norm of the block is the zero function).** For the antisymmetric plain sesqualgebra,

$$
\boxed{\;
\mathrm{Sc}\bigl(\tilde Q_1\diamond\tilde Q_2\bigr)=0\quad\text{for all }\tilde Q_1,\tilde Q_2,
\qquad\text{hence}\qquad
\varphi_{\diamond}(\tilde Q)=0\quad\text{for all }\tilde Q
\;}.
$$

The algebraic norm of the operation is identically zero, and by the convention of the definition the block carries **no algebraic norm**.

*Proof.* Every value of the block is a pure vector, $\tilde Q_1\diamond\tilde Q_2=\operatorname{Vect}(\tilde Q_1\tilde Q_2^{*})\in\operatorname{Vect}(\mathbb{B})$, of scalar part zero for every pair; the diagonal is therefore the zero function. A vanishing quadratic form is not an algebraic norm, and its vanishing set is the whole space, so the block is counted with no algebraic norm rather than with a zero one.

**Remark (the diagonal of the block).** The sesquilinear product is not alternating in the bilinear sense — its second slot is conjugate-linear — so the diagonal need not vanish as an element of the block:

$$ \boxed{\; \tilde Q\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde Q\tilde Q^{*}\bigr)\in\operatorname{Vect}(\mathbb{B}) \;}, $$

the vector part of the Hermitian square $\tilde Q\tilde Q^{*}$; it is central exactly when it is zero, that is exactly when $\tilde Q\tilde Q^{*}$ is central. The witness $\tilde Q=\vec e_x+i\vec e_y$ gives $\tilde Q\diamond\tilde Q=2i\vec e_z\neq0$. The diagonal is a value and not a norm, and it is not central in general, so no central-valued quadratic map is built from the product.

## The Relative Inverse

**The multiplication by a non-central element $\tilde Q_3$ has the complex plane $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$ as its kernel, and it induces a conjugate-linear bijection of the quotient of $\mathbb{B}$ by that kernel onto the plane of the values orthogonal to $\vec Q_3$ in the complex bilinear dot**, the relative inverse that replaces the missing inverse.

The block has no inverse, but the one-sided multiplication by an element is an operator with a kernel and an image, and its invertibility on a quotient is the substitute the article records.

**Proposition (the kernel of the multiplication).** For the block, the one-sided multiplication by a non-central element $\tilde Q_3$,

$$
L_{\tilde Q_3}\tilde Q_2=\tilde Q_3\diamond\tilde Q_2,
$$

has the complex plane $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$ of complex dimension two as its kernel, and it induces a conjugate-linear bijection of the quotient of $\mathbb{B}$ by that kernel onto the plane of the values orthogonal to $\vec Q_3$ in the complex bilinear dot.

*Proof.* The kernel is the annihilator computed in *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, of complex dimension two for a non-central element, and the block is conjugate-linear in its second slot, so the induced map on the quotient is conjugate-linear; the image is the plane $\{\tilde W:\vec W\in\operatorname{Vect}(\mathbb{B}),\ (\vec W,\vec Q_3)=0\}$, and the dimension count gives the bijection.

So the equation $\tilde Q_3\diamond\tilde Q_2=\tilde W$ is solvable exactly for the values on that plane, and the set of its solutions is a coset of the kernel. The block has no inverse, and it has a **relative inverse** in which each non-central element acts invertibly between two spaces of complex dimension two, the loss and the gain being accounted by the kernel and the image.

## The Invertibility Criterion Is Not Transferred

**The invertibility criterion of the parent is not transferred to the block:** the form $\langle\cdot,\cdot\rangle_{*}$ of the parent general plain sesquilinear product is not the algebraic norm of the block and is not read here, and the block loses the parent's one-sided equations at once, their place taken by the relative inverse.

**Remark (the criterion of the parent is not read here).** The parent general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$ has the right unit $e_t$, and its one-sided inverse equations are decided by a quadratic form that is the algebraic norm $\langle\cdot\rangle_{*}$ of a different product, the diagonal of $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ (*Norm and Invertibility in the General Plain Sesqualgebra*). That form is not the algebraic norm of the block and is not read here. The block loses the parent's one-sided equations at once, because the value has been moved into a subspace that meets the centre only at the origin, and the place of the criterion is taken by the relative inverse above.

## Summary

The antisymmetric plain sesqualgebra $\tilde Q_1\diamond\tilde Q_2=\operatorname{Vect}(\tilde Q_1\tilde Q_2^{*})$ has no unit on either side, hence no invertible element and an empty group of units, and the one-sided inverse equations $\tilde Q\diamond\tilde Q_2=e_t$ and $\tilde Q_2\diamond\tilde Q=e_t$ have no solution because every value of the block is a pure vector. The **algebraic norm** of the operation is the diagonal of its scalar-part form; the scalar part vanishes identically, the diagonal is the zero function, and by the convention of *The Four Forms and the Four Algebraic Norms* a vanishing quadratic form is not an algebraic norm, so the block carries **no algebraic norm**. The diagonal of the block is the vector part of the Hermitian square, a value and not a norm, central only where it vanishes. What replaces the invertibility is not a norm but the operator reading: the multiplication by a non-central element has a two-dimensional kernel and induces a conjugate-linear bijection of the quotient onto the plane of the solvable values, the relative inverse. The algebraic norm $\langle\cdot\rangle_{*}$ of the parent sesquilinear product is a different form of a different product and is not read here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\diamond\tilde Q_2=\operatorname{Vect}(\tilde Q_1\tilde Q_2^{*})=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | the antisymmetric plain sesqualgebra, the operation $\mathrm{APS}$ |
| $\tilde Q_1\tilde Q_2^{*}$ | the parent general plain sesquilinear product |
| $\tilde Q_1\diamond e_t=\vec Q_1$, $e_t\diamond\tilde Q=-\overline{\vec Q}$ | the two one-sided actions of $e_t$ |
| $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$ | the scalar part of the block vanishes identically |
| $\varphi_{\diamond}(\tilde Q)=0$ | the algebraic norm of the block, the zero function; the block carries no algebraic norm |
| $\tilde Q\diamond\tilde Q=\operatorname{Vect}(\tilde Q\tilde Q^{*})$ | the diagonal, the vector part of the Hermitian square |
| $L_{\tilde Q_3}\tilde Q_2=\tilde Q_3\diamond\tilde Q_2$ | the one-sided multiplication, kernel $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, $\operatorname{Vect}(\mathbb{B})$ | the centre, the vector subspace |
| no unit, no inverse, no group of units | the absence carried by the block |

## Further Reading

- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the definition of the algebraic norm as the diagonal of a scalar-part form, for the zero diagonal of the four antisymmetric operations, and for the convention that counts them with no algebraic norm.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the unit, the inverse and the relativity of the definitions to the product.
- [Introduction to the Antisymmetric Plain Sesqualgebra](introduction-to-the-antisymmetric-plain-sesqualgebra.html), for the operation, its class, its image and the absence of a unit.
- [The Four General Products and Their Relations](the-four-general-products-and-their-relations.html), for the unit table of the four general products.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the annihilator and the relative inverse of the block.
- [The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra](the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.html), for the structural reading of the diagonal.
- [Norm and Invertibility in the General Plain Sesqualgebra](norm-and-invertibility-in-the-general-plain-sesqualgebra.html), for the algebraic norm $\langle\cdot\rangle_{*}$ of the parent sesquilinear product, which is not the form of this block.
