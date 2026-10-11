# __Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

This article studies the algebraic norm and the invertibility of the antisymmetric quaternionic sesqualgebra

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)
=\mathbf{P}\times\overline{\mathbf{Q}},
$$

the conjugate cross product, the antisymmetric half of the general quaternionic sesquilinear product, the operation $\mathrm{AQS}$ of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*. The operation is $\mathbb{C}$-bilinear in the first slot, conjugate-linear in the second, vector valued, and it has no unit on either side.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. For the block the scalar part is identically zero, $\mathrm{Sc}(\tilde P\diamond\tilde Q)=0$, because every value is a pure vector; the algebraic norm of the operation is therefore **the zero function**, and by the convention of the same article a vanishing quadratic form is not an algebraic norm, so the block is counted with **no algebraic norm** rather than with a zero one.

Both notions of the title are therefore **absences**, and they fail for one reason: the unit of the parent algebra is a square-zero element of the block. The block has no unit on either side, so no element is invertible and the group of units is empty; the one-sided inverse equations to the centre have no solution. What replaces the invertibility is not a norm but an operator reading: the one-sided multiplication by an element has a kernel and an image, and the relative inverse below accounts for the loss on the quotient.

**Boundaries.** The operation, its class and the absence of a unit are *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*; the general definitions of the unit and the inverse are *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*, and the unit table of the four general products is *Comparison Between the Four General Products*; the element theory that uses the substitute is *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*. The algebraic norm of the general quaternionic sesquilinear product is $K$, a different form, and its theory is *Norm and Invertibility in the General Quaternionic Sesqualgebra*; the invariant forms of the block are *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$ with $e_1e_2=e_3$ and $e_k^2=-e_0$, central scalar imaginary $i$ and $Q_\mu\in\mathbb{C}$; an element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf{Q}$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The general quaternionic sesquilinear product is $\tilde P^{\natural}\tilde Q^{*}$, and the product of the block is $\diamond$. The complex bilinear dot product of two vector parts is $(\mathbf{A},\mathbf{B})=\sum_kA_kB_k$.

## The Relative Definitions

The word *unit* and the word *inverse* name a product, so the definitions are stated once for a general product and read on the block; they are *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*.

**Definition (unit).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde X=\tilde X$ for every $\tilde X$, a **right unit** when $\tilde X\star e=\tilde X$ for every $\tilde X$, and a **two-sided unit** when it is both. A product with a two-sided unit is **unital**.

**Definition (inverse and group of units).** Let $\star$ be a unital product with identity $e$. An element $\tilde Q$ is **left-invertible of $\star$** when there is $\tilde R$ with $\tilde R\star\tilde Q=e$, **right-invertible** when there is $\tilde R$ with $\tilde Q\star\tilde R=e$, and **invertible** when there is $\tilde R$ with $\tilde Q\star\tilde R=\tilde R\star\tilde Q=e$. Such an $\tilde R$ is the **inverse of $\tilde Q$**, and in an associative unital product the invertible elements form the **group of units**.

Throughout this article the product is the block $\diamond$, and, unqualified, *unit* and *inverse* are read in $\diamond$.

## The Absence of a Unit

**Theorem (no unit).** The block has no left unit, no right unit and no two-sided unit.

*Proof.* A left unit $e$ must satisfy $e\diamond e_0=e_0$; but $e\diamond e_0=\mathbf{e}\times\overline{\mathbf{0}}=0$, since the vector part of $e_0$ is zero, so the equation reads $0=e_0$ and is false. A right unit $e$ must satisfy $e_0\diamond e=e$; but $e_0\diamond e=\mathbf{0}\times\overline{\mathbf{e}}=0$, so the equation reads $0=e$ and is false for a nonzero $e$, while the origin satisfies it only at the element zero.

**Remark (the unit is a square-zero element).** The failure is not a subtle one: the unit of the parent algebra satisfies $e_0\diamond e_0=0$ in the block, so it is not merely a non-unit, it is a nilpotent of index two. The whole central line shares the reading, $\lambda e_0\diamond\lambda e_0=0$, and the centre is annihilated by the block in both slots; the line of the units of the algebras is the line of the square-zero elements of the block.

## The Absence of an Inverse

**Corollary (no inverse, no group of units).** No element of the block is left-invertible, right-invertible or invertible, and the group of units of the block is empty.

*Proof.* The three definitions of the inverse are equations with the unit of the product on the right side, and the block has no unit on either side by the theorem above, so the equations cannot be written down. The statement is not a statement about the elements: it is the statement that the class of the invertible elements of the block is empty.

**Proposition (the one-sided equations have no solution).** For every $\tilde Q$ the two equations

$$
\tilde Q\diamond\tilde R=e_0,\qquad \tilde R\diamond\tilde Q=e_0
$$

have no solution $\tilde R$.

*Proof.* Each left member is a value of the block, hence a pure vector of scalar part zero; the right member $e_0$ has scalar part one. A pure vector is never $e_0$, so neither equation holds.

## The Algebraic Norm of the Block

**Definition (the algebraic norm of the operation).** Let $f$ be an operation on $\mathbb{B}$ with scalar-part form $\varphi(\tilde P,\tilde Q)=\mathrm{Sc}\,f(\tilde P,\tilde Q)$. The **algebraic norm of $f$** is the diagonal of that form,

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)=\mathrm{Sc}\,f(\tilde Q,\tilde Q),
$$

and for an operation whose scalar part vanishes identically the algebraic norm is the zero function (*The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*).

**Theorem (the algebraic norm of the block is the zero function).** For the antisymmetric quaternionic sesqualgebra,

$$
\mathrm{Sc}\bigl(\tilde P\diamond\tilde Q\bigr)=0\quad\text{for all }\tilde P,\tilde Q,
\qquad\text{hence}\qquad
\varphi_{\diamond}(\tilde Q)=0\quad\text{for all }\tilde Q .
$$

The algebraic norm of the operation is identically zero, and by the convention of the definition the block carries **no algebraic norm**.

*Proof.* The value of the block is the conjugate cross product $\mathbf{P}\times\overline{\mathbf{Q}}$, a pure vector of scalar part zero for every pair; its diagonal is therefore the zero function. A vanishing quadratic form is not an algebraic norm, and its vanishing set is the whole space, so the block is counted with no algebraic norm rather than with a zero one.

**Remark (the diagonal is a pure vector).** The sesquilinear product is not alternating in the bilinear sense — its second slot is conjugate-linear — so the diagonal need not vanish as an element of the block:

$$
\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}},
$$

a pure vector, generally nonzero. It is central exactly when it vanishes, so there is no quadratic form $N_\diamond$ with $\tilde X\diamond\tilde X=N_\diamond(\tilde X)e_0$ for every $\tilde X$: the equation would hold only on the cone of vanishing diagonal and define nothing outside. No central-valued quadratic map is built from the product.

## The Relative Inverse

The block has no inverse, but the one-sided multiplication by an element is an operator with a kernel and an image, and its invertibility on a quotient is the substitute the article records.

**Proposition (the kernel of the multiplication).** For the block, the one-sided multiplication by a non-central element $\tilde A$,

$$
L_{\tilde A}\tilde R=\tilde A\diamond\tilde R=\mathbf{A}\times\overline{\mathbf{R}},
$$

has the complex plane $\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf{A}}$ of complex dimension two as its kernel, and it induces a conjugate-linear bijection of the quotient of $\mathbb{B}$ by that kernel onto the plane of the values orthogonal to $\mathbf{A}$ in the complex bilinear dot.

*Proof.* The kernel is the annihilator computed in *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*, of complex dimension two for a non-central element, and the block is conjugate-linear in its second slot, so the induced map on the quotient is conjugate-linear; the image is the plane $\{\tilde W:\mathbf{W}\in\operatorname{Vect}(\mathbb{B}),\ (\mathbf{W},\mathbf{A})=0\}$, and the dimension count gives the bijection.

So the equation $\tilde A\diamond\tilde R=\tilde W$ is solvable exactly for the values on that plane, and the set of its solutions is a coset of the kernel. The block has no inverse, and it has a **relative inverse** in which each non-central element acts invertibly between two spaces of complex dimension two, the loss and the gain being accounted by the kernel and the image.

## The Invertibility Criterion Is Not Transferred

**Remark (the criterion of the parent is not read here).** The parent general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$ has no unit on either side, and its element theory is read without a unit; its algebraic norm is $K$, the diagonal of $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, a different form of a different product (*Norm and Invertibility in the General Quaternionic Sesqualgebra*). That form is not the algebraic norm of the block and is not read here. The block loses the parent's structure at once: every nonzero element is a two-sided zero divisor, the multiplication by a fixed element has a nonzero kernel, and the place of the criterion is taken by the relative inverse above.

## Summary

The antisymmetric quaternionic sesqualgebra $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ has no unit on either side, so no element of it is invertible and the group of units is empty; the unit of the parent algebra is a square-zero element of the block, and the whole central line is annihilated by the block in both slots. The **algebraic norm** of the operation is the diagonal of its scalar-part form; the scalar part vanishes identically, the diagonal is the zero function, and by the convention of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* a vanishing quadratic form is not an algebraic norm, so the block carries **no algebraic norm**. The diagonal of the block is the pure vector $\mathbf{Q}\times\overline{\mathbf{Q}}$, a value and not a norm. What replaces the invertibility is not a norm but the operator reading: the multiplication by a non-central element has a two-dimensional kernel and induces a conjugate-linear bijection of the quotient onto the plane of the solvable values, the relative inverse. The algebraic norm $K$ of the parent quaternionic sesquilinear product is a different form of a different product and is not read here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})=\mathbf{P}\times\overline{\mathbf{Q}}$ | the antisymmetric quaternionic sesqualgebra, the operation $\mathrm{AQS}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | the parent general quaternionic sesquilinear product |
| $e_0$ | the unit of the parent algebra, a square-zero element of the block |
| $\mathrm{Sc}(\tilde P\diamond\tilde Q)=0$ | the scalar part of the block vanishes identically |
| $\varphi_{\diamond}(\tilde Q)=0$ | the algebraic norm of the block, the zero function; the block carries no algebraic norm |
| $\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}$ | the diagonal, a pure vector |
| $L_{\tilde A}\tilde R=\mathbf{A}\times\overline{\mathbf{R}}$ | the one-sided multiplication, kernel $\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf{A}}$ |
| no unit, no inverse, no group of units | the absence carried by the block |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the definition of the algebraic norm as the diagonal of a scalar-part form, for the zero diagonal of the four antisymmetric operations, and for the convention that counts them with no algebraic norm.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Unit and the Inverse*, for the unit, the inverse and the relativity of the definitions to the product.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the operation, its class, its image and the absence of a unit.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the unit table of the four general products.
- *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the annihilator and the relative inverse of the block.
- *Norm and Invertibility in the General Quaternionic Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-sesqualgebra.md`), for the algebraic norm $K$ of the parent sesquilinear product, which is not the form of this block.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the invariant forms of the block.
