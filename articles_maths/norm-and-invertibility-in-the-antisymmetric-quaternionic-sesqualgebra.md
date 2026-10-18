# __Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

This article studies the algebraic norm and the invertibility of the antisymmetric quaternionic sesqualgebra

$$
\tilde Q_1\diamond\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)
=\vec Q_1\times\overline{\vec Q_2},
$$

the conjugate cross product, the antisymmetric half of the general quaternionic sesquilinear product, the operation $\mathrm{AQS}$ of *Introduction to the Antisymmetric Quaternionic Sesqualgebra*. The operation is $\mathbb{C}$-bilinear in the first slot, conjugate-linear in the second, vector valued, and it has no unit on either side.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*. For the block the scalar part is identically zero, $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$, because every value is a pure vector; the algebraic norm of the operation is therefore **the zero function**, and by the convention of the same article a vanishing quadratic form is not an algebraic norm, so the block is counted with **no algebraic norm** rather than with a zero one.

Both notions of the title are therefore **absences**, and they fail for one reason: the unit of the parent algebra is a square-zero element of the block. The block has no unit on either side, so no element is invertible and the group of units is empty; the one-sided inverse equations to the centre have no solution. What replaces the invertibility is not a norm but an operator reading: the one-sided multiplication by an element has a kernel and an image, and the relative inverse below accounts for the loss on the quotient.

**Boundaries.** The operation, its class and the absence of a unit are *Introduction to the Antisymmetric Quaternionic Sesqualgebra*; the general definitions of the unit and the inverse are *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The Unit and the Inverse*, and the unit table of the four general products is *Comparison Between the Four General Products*; the element theory that uses the substitute is *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*. The algebraic norm of the general quaternionic sesquilinear product is $\langle\cdot\rangle_{\natural*}$, a different form, and its theory is *Norm and Invertibility in the General Quaternionic Sesqualgebra*; the invariant forms of the block are *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_\mu^2=-e_t$, central scalar imaginary $i$ and $Q_{1\mu}\in\mathbb{C}$; an element is $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ with $\vec Q_1=\sum_{\mu\in\{x,y,z\}}Q_{1\mu}\vec e_\mu$, and a second is $\tilde Q_2=Q_{2t}e_t+\vec Q_2$. The natural conjugation is $\tilde Q_1^{\natural}=Q_{1t}-\vec Q_1$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The general quaternionic sesquilinear product is $\tilde Q_1^{\natural}\tilde Q_2^{*}$, and the product of the block is $\diamond$. The complex bilinear dot product of two vector parts is $(\vec A,\vec B)=\sum_\mu A_\mu B_\mu$.

**The results.** The antisymmetric quaternionic sesqualgebra $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$, the conjugate cross product, has no unit on either side, so no element is invertible and the group of units is empty; the unit $e_t$ of the parent algebra is a square-zero element of the block, and the whole central line is annihilated by the block in both slots. The scalar part vanishes identically, so the algebraic norm of the operation is the zero function and the block carries **no algebraic norm** by the convention that counts a vanishing quadratic form as no norm; the diagonal $\tilde Q_1\diamond\tilde Q_1=\vec Q_1\times\overline{\vec Q_1}$ is a pure vector, a value and not a norm. The substitute for the inverse is the relative inverse: the multiplication by a non-central element $\tilde Q_3$ has the complex plane $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$, of real dimension four, as its kernel and induces a conjugate-linear bijection of the quotient onto the plane of the values orthogonal to $\vec Q_3$ in the complex bilinear dot, so that $\tilde Q_3\diamond\tilde{Q}_2=\tilde W$ is solvable exactly on that plane and its solutions form a coset of the kernel. Each section below states its result before it is proved.

## The Relative Definitions

The word *unit* and the word *inverse* name a product, so the definitions are stated once for a general product and read on the block; they are *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The Unit and the Inverse*.

**Definition (unit).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, a **right unit** when $\tilde Q_1\star e=\tilde Q_1$ for every $\tilde Q_1$, and a **two-sided unit** when it is both. A product with a two-sided unit is **unital**.

**Definition (inverse and group of units).** Let $\star$ be a unital product with identity $e$. An element $\tilde Q_1$ is **left-invertible of $\star$** when there is $\tilde{Q}_2$ with $\tilde{Q}_2\star\tilde Q_1=e$, **right-invertible** when there is $\tilde{Q}_2$ with $\tilde Q_1\star\tilde{Q}_2=e$, and **invertible** when there is $\tilde{Q}_2$ with $\tilde Q_1\star\tilde{Q}_2=\tilde{Q}_2\star\tilde Q_1=e$. Such an $\tilde{Q}_2$ is the **inverse of $\tilde Q_1$**, and in an associative unital product the invertible elements form the **group of units**.

Throughout this article the product is the block $\diamond$, and, unqualified, *unit* and *inverse* are read in $\diamond$.

## The Absence of a Unit

**The block has no unit on either side, and the unit $e_t$ of the parent algebra is a square-zero element of the block.**

**Theorem (no unit).** The block has no left unit, no right unit and no two-sided unit.

*Proof.* A left unit $e$ must satisfy $e\diamond e_t=e_t$; but $e\diamond e_t=\vec e\times\overline{\mathbf{0}}=0$, since the vector part of $e_t$ is zero, so the equation reads $0=e_t$ and is false. A right unit $e$ must satisfy $e_t\diamond e=e$; but $e_t\diamond e=\mathbf{0}\times\overline{\vec e}=0$, so the equation reads $0=e$ and is false for a nonzero $e$, while the origin satisfies it only at the element zero.

**Remark (the unit is a square-zero element).** The failure is not a subtle one: the unit of the parent algebra satisfies $e_t\diamond e_t=0$ in the block, so it is not merely a non-unit, it is a nilpotent of index two. The whole central line shares the reading, $\lambda e_t\diamond\lambda e_t=0$, and the centre is annihilated by the block in both slots; the line of the units of the algebras is the line of the square-zero elements of the block.

## The Absence of an Inverse

**No element of the block is left-invertible, right-invertible or invertible, and the group of units is empty; the one-sided equations $\tilde Q_1\diamond\tilde{Q}_2=e_t$ and $\tilde{Q}_2\diamond\tilde Q_1=e_t$ have no solution.**

**Corollary (no inverse, no group of units).** No element of the block is left-invertible, right-invertible or invertible, and the group of units of the block is empty.

*Proof.* The three definitions of the inverse are equations with the unit of the product on the right side, and the block has no unit on either side by the theorem above, so the equations cannot be written down. The statement is not a statement about the elements: it is the statement that the class of the invertible elements of the block is empty.

**Proposition (the one-sided equations have no solution).** For every $\tilde Q_1$ the two equations

$$
\tilde Q_1\diamond\tilde{Q}_2=e_t,\qquad \tilde{Q}_2\diamond\tilde Q_1=e_t
$$

have no solution $\tilde{Q}_2$.

*Proof.* Each left member is a value of the block, hence a pure vector of scalar part zero; the right member $e_t$ has scalar part one. A pure vector is never $e_t$, so neither equation holds.

## The Algebraic Norm of the Block

**The scalar part of the block vanishes identically, so the algebraic norm of the operation is the zero function and the block carries no algebraic norm by the convention that counts a vanishing quadratic form as no norm; the diagonal $\tilde Q_1\diamond\tilde Q_1=\vec Q_1\times\overline{\vec Q_1}$ is a pure vector, a value and not a norm.**

**Definition (the algebraic norm of the operation).** Let $f$ be an operation on $\mathbb{B}$ with scalar-part form $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The **algebraic norm of $f$** is the diagonal of that form,

$$
\varphi(\tilde Q_1)=\varphi(\tilde Q_1,\tilde Q_1)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_1),
$$

and for an operation whose scalar part vanishes identically the algebraic norm is the zero function (*The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*).

**Theorem (the algebraic norm of the block is the zero function).** For the antisymmetric quaternionic sesqualgebra,

$$
\mathrm{Sc}\bigl(\tilde Q_1\diamond\tilde Q_2\bigr)=0\quad\text{for all }\tilde Q_1,\tilde Q_2,
\qquad\text{hence}\qquad
\varphi_{\diamond}(\tilde Q_1)=0\quad\text{for all }\tilde Q_1 .
$$

The algebraic norm of the operation is identically zero, and by the convention of the definition the block carries **no algebraic norm**.

*Proof.* The value of the block is the conjugate cross product $\vec Q_1\times\overline{\vec Q_2}$, a pure vector of scalar part zero for every pair; its diagonal is therefore the zero function. A vanishing quadratic form is not an algebraic norm, and its vanishing set is the whole space, so the block is counted with no algebraic norm rather than with a zero one.

**Remark (the diagonal is a pure vector).** The sesquilinear product is not alternating in the bilinear sense — its second slot is conjugate-linear — so the diagonal need not vanish as an element of the block:

$$
\tilde Q_1\diamond\tilde Q_1=\vec Q_1\times\overline{\vec Q_1},
$$

a pure vector, generally nonzero. It is central exactly when it vanishes, so there is no quadratic form $N_\diamond$ with $\tilde Q_1\diamond\tilde Q_1=N_\diamond(\tilde Q_1)e_t$ for every $\tilde Q_1$: the equation would hold only on the cone of vanishing diagonal and define nothing outside. No central-valued quadratic map is built from the product.

## The Relative Inverse

**For a non-central element $\tilde Q_3$, the multiplication $L_{\tilde Q_3}\tilde{Q}_2=\vec Q_3\times\overline{\vec Q_2}$ has the complex plane $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$, of real dimension four, as its kernel and induces a conjugate-linear bijection of the quotient onto the plane of the values orthogonal to $\vec Q_3$ in the complex bilinear dot, so that $\tilde Q_3\diamond\tilde{Q}_2=\tilde W$ is solvable exactly on that plane and its solutions form a coset of the kernel.**

The block has no inverse, but the one-sided multiplication by an element is an operator with a kernel and an image, and its invertibility on a quotient is the substitute the article records.

**Proposition (the kernel of the multiplication).** For the block, the one-sided multiplication by a non-central element $\tilde Q_3$,

$$
L_{\tilde Q_3}\tilde{Q}_2=\tilde Q_3\diamond\tilde{Q}_2=\vec Q_3\times\overline{\vec Q_2},
$$

has the complex plane $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$ of complex dimension two as its kernel, and it induces a conjugate-linear bijection of the quotient of $\mathbb{B}$ by that kernel onto the plane of the values orthogonal to $\vec Q_3$ in the complex bilinear dot.

*Proof.* The kernel is the annihilator computed in *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, of complex dimension two for a non-central element, and the block is conjugate-linear in its second slot, so the induced map on the quotient is conjugate-linear; the image is the plane $\{\tilde W:\vec W\in\operatorname{Vect}(\mathbb{B}),\ (\vec W,\vec Q_3)=0\}$, and the dimension count gives the bijection.

So the equation $\tilde Q_3\diamond\tilde{Q}_2=\tilde W$ is solvable exactly for the values on that plane, and the set of its solutions is a coset of the kernel. The block has no inverse, and it has a **relative inverse** in which each non-central element acts invertibly between two spaces of complex dimension two, the loss and the gain being accounted by the kernel and the image.

## The Invertibility Criterion Is Not Transferred

**The algebraic norm $\langle\cdot\rangle_{\natural*}$ of the parent quaternionic sesquilinear product is a form of a different product and is not transferred to the block; the block has no invertibility criterion of its own, and the place of the criterion is taken by the relative inverse above.**

**Remark (the criterion of the parent is not read here).** The parent general quaternionic sesquilinear product $\tilde Q_1^{\natural}\tilde Q_2^{*}$ has no unit on either side, and its element theory is read without a unit; its algebraic norm is $\langle\cdot\rangle_{\natural*}$, the diagonal of $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, a different form of a different product (*Norm and Invertibility in the General Quaternionic Sesqualgebra*). That form is not the algebraic norm of the block and is not read here. The block loses the parent's structure at once: every nonzero element is a two-sided zero divisor, the multiplication by a fixed element has a nonzero kernel, and the place of the criterion is taken by the relative inverse above.

## Summary

The antisymmetric quaternionic sesqualgebra $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$ has no unit on either side, so no element of it is invertible and the group of units is empty; the unit of the parent algebra is a square-zero element of the block, and the whole central line is annihilated by the block in both slots. The **algebraic norm** of the operation is the diagonal of its scalar-part form; the scalar part vanishes identically, the diagonal is the zero function, and by the convention of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* a vanishing quadratic form is not an algebraic norm, so the block carries **no algebraic norm**. The diagonal of the block is the pure vector $\vec Q_1\times\overline{\vec Q_1}$, a value and not a norm. What replaces the invertibility is not a norm but the operator reading: the multiplication by a non-central element has a two-dimensional kernel and induces a conjugate-linear bijection of the quotient onto the plane of the solvable values, the relative inverse. The algebraic norm $\langle\cdot\rangle_{\natural*}$ of the parent quaternionic sesquilinear product is a different form of a different product and is not read here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\diamond\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural})=\vec Q_1\times\overline{\vec Q_2}$ | the antisymmetric quaternionic sesqualgebra, the operation $\mathrm{AQS}$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the parent general quaternionic sesquilinear product |
| $e_t$ | the unit of the parent algebra, a square-zero element of the block |
| $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$ | the scalar part of the block vanishes identically |
| $\varphi_{\diamond}(\tilde Q_1)=0$ | the algebraic norm of the block, the zero function; the block carries no algebraic norm |
| $\tilde Q_1\diamond\tilde Q_1=\vec Q_1\times\overline{\vec Q_1}$ | the diagonal, a pure vector |
| $L_{\tilde Q_3}\tilde{Q}_2=\vec Q_3\times\overline{\vec Q_2}$ | the one-sided multiplication, kernel $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$ |
| no unit, no inverse, no group of units | the absence carried by the block |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the definition of the algebraic norm as the diagonal of a scalar-part form, for the zero diagonal of the four antisymmetric operations, and for the convention that counts them with no algebraic norm.
- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Unit and the Inverse*, for the unit, the inverse and the relativity of the definitions to the product.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-sesqualgebra.md`), for the operation, its class, its image and the absence of a unit.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the unit table of the four general products.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the annihilator and the relative inverse of the block.
- *Norm and Invertibility in the General Quaternionic Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-sesqualgebra.md`), for the algebraic norm $\langle\cdot\rangle_{\natural*}$ of the parent sesquilinear product, which is not the form of this block.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the invariant forms of the block.
