# __Norm and Invertibility in the Antisymmetric Plain Sesqualgebra__

## Introduction

This article treats the two notions that a product carries at its centre, the **unit** and the **inverse**, and the functional that decides the second, the **algebraic norm**, in the antisymmetric plain sesqualgebra $\mathrm{APS}$ of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*. The block is the operation

$$
\tilde P\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)=\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}\bigr)
=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}},
$$

the antisymmetric half of the general plain sesquilinear product, and its standing defect is that it has no unit on either side.

Both notions are therefore **absences**, and the article states them as such. It does not fill them. The inverse is defined relative to a two-sided unit, and the block has none, so no element of the block is invertible, there is no group of units, and the one-sided inverse equations have no solution. The algebraic norm is a multiplicative quadratic form whose values are central, and the block kills the centre, so the self-product of the block is a value and not a norm. What survives is the Hermitian form $H$, which belongs to the space and not to the block, and whose reading on the block is the pairing of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*; the diagonal and its degeneracy are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

The definitions are stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*: §*The Unit and the Inverse* for the unit and the inverse, and §*Powers, the Square and the Roots* for the roots. Throughout this article the product is $\diamond$, and, unqualified, **unit** means a unit of $\diamond$, **invertible** means invertible of $\diamond$, and **norm** means the algebraic norm. The element classes that the absent inverse would have separated are elsewhere: the zero divisors of the block are *Zero Divisors of the Antisymmetric Plain Sesqualgebra*, its idempotents are *Idempotents of the Antisymmetric Plain Sesqualgebra*, its nilpotents are *Nilpotents of the Antisymmetric Plain Sesqualgebra*, and the general shape of the block is *The Specificities of the Antisymmetric Plain Sesqualgebra*. The units of the other three general products, and the fact that the four products of the space do not share them, are *Comparison Between the Four General Products*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and $Q_\mu\in\mathbb{C}$; an element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf{Q}$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$. The general plain bilinear product is written $\tilde P\tilde Q$ and the general plain sesquilinear product $\tilde P\tilde Q^{*}$; the block is $\diamond$. The Hermitian form is $H(\tilde P,\tilde Q)=\operatorname{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$, and the algebraic norm of the plain product is $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ (*Norm and Invertibility in the General Plain Algebra*). The centre is $\mathbb{C}_{\mathbb{B}}$ and the vector subspace is $\operatorname{Vect}(\mathbb{B})$; the projection $\operatorname{Vect}$ is the map that removes the scalar part, and it is $\mathbb{C}$-linear and surjective with kernel $\mathbb{C}_{\mathbb{B}}$.

## The Inverse of a Product

### The General Definition

A unit and an inverse belong to a product, and the definitions are stated once and for all in *Definitions for the Study of the 12 Algebraic Structures*. Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde X=\tilde X$ for every $\tilde X$, a **right unit of $\star$** when $\tilde X\star e=\tilde X$ for every $\tilde X$, and a **two-sided unit**, or **identity**, when it is both; a product with a two-sided unit is **unital**. When $\star$ is unital with unit $e$, an element $\tilde Q$ is **left-invertible of $\star$** when there is $\tilde R$ with $\tilde R\star\tilde Q=e$, **right-invertible** when there is $\tilde R$ with $\tilde Q\star\tilde R=e$, and **invertible** when there is $\tilde R$ with $\tilde Q\star\tilde R=\tilde R\star\tilde Q=e$; such an $\tilde R$ is the **inverse**, written $\tilde Q^{-1}$, and in an associative unital product the invertible elements form the **group of units** (*Unital Algebras*).

Both definitions are equations in the symbol $\star$, and both name it. The first names it by the two displays $e\star\tilde X=\tilde X$ and $\tilde X\star e=\tilde X$, the second by the display $\tilde Q\star\tilde R=\tilde R\star\tilde Q=e$. Substituting the product of the block gives its two equations, and they are the equations that decide the whole article.

### The Equations of the Block

Written on the block, the unit equations are

$$
\tilde u\diamond\tilde X=\tilde X\quad\text{for every }\tilde X,\qquad
\tilde X\diamond\tilde u=\tilde X\quad\text{for every }\tilde X,
$$

and the inverse equations, were a unit available, would be

$$
\tilde Q\diamond\tilde R=\tilde R\diamond\tilde Q=e_0 .
$$

The two unit equations are settled by the two one-sided actions of the element $e_0$ of the basis,

$$
\tilde P\diamond e_0=\mathbf{P},\qquad e_0\diamond\tilde Q=-\overline{\mathbf{Q}},
$$

the first being $\operatorname{Vect}(\tilde P)$ and the second $\operatorname{Vect}(\tilde Q^{*})$; the two displays are the proposition *The Image and the Absence of a Unit* of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*, where they are computed as $\tilde P\diamond e_0=\operatorname{Vect}(\tilde P e_0^{*})=\operatorname{Vect}(\tilde P)=\mathbf{P}$ and $e_0\diamond\tilde Q=\operatorname{Vect}(e_0\tilde Q^{*})=\operatorname{Vect}(\tilde Q^{*})=-\overline{\mathbf{Q}}$. Neither action is the identity map: the first forgets the scalar part of the element on its left, and the second both conjugates and takes the vector part. That is the whole content of the absence of the unit, and it is recorded once in the introduction of the block and quoted here.

## The Absence of a Unit

**Theorem (no unit).** The block has neither a left unit nor a right unit. There is no element $\tilde u$ with $\tilde u\diamond\tilde X=\tilde X$ for every $\tilde X$, and none with $\tilde X\diamond\tilde u=\tilde X$ for every $\tilde X$.

*Proof.* A left unit $\tilde u$ would satisfy, at $\tilde X=e_0$, the equation $\tilde u\diamond e_0=e_0$, that is $\mathbf{u}=e_0$; the left member is a vector part, whose scalar part is zero, while the right member has scalar part one, so the equation is impossible. A right unit $\tilde u$ would satisfy, at $\tilde X=e_0$, the equation $e_0\diamond\tilde u=e_0$, that is $-\overline{\mathbf{u}}=e_0$; the same parity of the scalar part forbids it. The two witnesses are $\tilde X=e_0$ for both sides, and they are the two displays of the preceding section read with the value on the left and the unit on the right.

The obstruction is the same in both cases and it is a **parity**: every value of the block is a pure vector, so its scalar part vanishes, while the element $e_0$ has scalar part one. The block therefore cannot see the unit of the space, on either side, and the two displays $\tilde u\diamond e_0=\mathbf{u}$ and $e_0\diamond\tilde u=-\overline{\mathbf{u}}$ are the two one-sided actions that replace it. The unit table of the four general products is *Comparison Between the Four General Products*, and the block's row of it is the entry *none* on both sides.

**Remark (the reason is the projection).** The parent product $\tilde P\tilde Q^{*}$ is not unital, but it has a right unit, the element $e_0$: at $\tilde Q=e_0$ its value is $\tilde P e_0^{*}=\tilde P$. **The block destroys that right unit and only that one** — the parent has no left unit to destroy. The relation $\tilde P\diamond e_0=\mathbf{P}$ shows that $\tilde P\diamond e_0=\tilde P$ for a given $\tilde P$ exactly when $\mathbf{P}=\tilde P$, that is exactly when $\tilde P$ is a **pure vector**: the right-unit equation survives on the vector subspace alone and fails at every element with a non-zero scalar part, the centre included, where $\mathbf{P}=0$. The defect is the projection $\operatorname{Vect}$, and it is not repairable: the block takes its values in the vector subspace and the unit lies in the centre.

## The Absence of the Inverse

### The Notion Is Vacuous

The inverse is defined relative to a two-sided unit, and the two-sided unit does not exist. The definition therefore has no instance in the block: the phrase *$\tilde Q$ is invertible of $\diamond$* has no truth value, and the symbol $\tilde Q^{-1}$, read with the product of the block, names nothing. The group of units of the block is the empty set, and it is not a group.

This is stronger than the non-invertibility of the plain product, where the group of units is the complement of the zero-divisor cone and is a genuine group (*Norm and Invertibility in the General Plain Algebra*). It is the **absence of the notion**, not the emptiness of a computed set. The block is one of the products for which the definition of *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*, is stated precisely because a two-sided unit may fail to exist.

### The One-Sided Equations Have No Solution

What can nevertheless be tested are the two one-sided equations, which do not need the name *inverse* but only the element $e_0$ of the space.

**Proposition.** For every $\tilde Q$ the two equations

$$
\tilde Q\diamond\tilde R=e_0,\qquad \tilde R\diamond\tilde Q=e_0
$$

have no solution $\tilde R$.

*Proof.* Each left member is a value of the block, hence a pure vector, whose scalar part is zero; the right member $e_0$ has scalar part one. A pure vector is never $e_0$, so neither equation holds.

**Remark (the reading against the parent).** For the parent product the equation $\tilde P\tilde Q^{*}=e_0$ has the solution $\tilde Q=\tilde P^{-1}{}^{*}$ for the invertible $\tilde P$, and $\tilde P^{\natural}\tilde Q^{*}=e_0$ likewise; the one-sided inverse equations of the four general products are collected in *The Zero Divisors and the Four General Products*, §*The One-Sided Inverse Equations*. **The block loses all of them at once**, and the reason is again the projection: the equation is solvable in the parent and unsolvable in the block, because the value has been moved into a subspace that does not meet the centre except at the origin.

## The Absence of an Algebraic Norm

### The General Definition

An **algebraic norm** is a multiplicative quadratic form whose values are central elements of the algebra and not real numbers; for $\mathbb{B}$ it is the **central square**

$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=\Bigl(\sum_{\mu=0}^{3}Q_\mu^{2}\Bigr)e_0,
$$

it is multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, and it is the functional that decides invertibility of the plain product, an element being invertible exactly when $N(\tilde Q)\neq0$ (*Norm and Invertibility in the General Plain Algebra*). The definition needs a self-product whose value is central, and it is exactly that which the block does not have.

### The Block Kills It

**Proposition (no central self-product).** The block carries no non-zero central value: $\tilde P\diamond\tilde Q\in\mathbb{C}_{\mathbb{B}}$ forces $\tilde P\diamond\tilde Q=0$. In particular the diagonal is never a central element:

$$
\tilde Q\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde Q\tilde Q^{*}\bigr)\in\operatorname{Vect}(\mathbb{B}),
\qquad
\tilde Q\diamond\tilde Q=0\ \text{only for }\ \tilde Q\tilde Q^{*}\ \text{central}.
$$

*Proof.* Every value is a pure vector, and the centre meets the vector subspace at the origin. The diagonal is a value, so it lies in the vector subspace; it is central exactly when it is $0$, that is exactly when $\tilde Q\tilde Q^{*}$ is central. The witness $\tilde Q=e_1+ie_2$ gives $\tilde Q\diamond\tilde Q=2ie_3\neq0$.

The diagonal is thus **degenerate** in the exact sense that matters here: it is not the value of a norm, it is not central, and it is not multiplicative. The structural reading of the diagonal, its criterion and the quadric it traces are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; this article records only that no norm descends to the block.

**Remark (the parent's norm does not descend either).** One might try to read the parent norm $N$ on the values of the block, since a value is an element of $\mathbb{B}$ and $N$ is defined on every element. That reading is not a norm of the block: it is not multiplicative over $\diamond$, and the block is not associative. The witnesses are the diagonal pairs, on which the block kills the value: $\tilde P=\tilde Q=e_0$ gives $e_0\diamond e_0=0$, with $N(0)=0$ against $N(e_0)N(e_0)=1$, and $\tilde P=\tilde Q=e_1$ gives $e_1\diamond e_1=0$, with $N(0)=0$ against $N(e_1)N(e_1)=1$, the norm of the basis elements being $N(e_0)=N(e_1)=e_0$. A pair off the diagonal, such as $\tilde P=e_0$, $\tilde Q=e_1$, may agree — the block gives $e_0\diamond e_1=-e_1$ and $N(-e_1)=N(e_1)=1=N(e_0)N(e_1)$, the quadratic form absorbing the sign — and it is the diagonal that breaks the multiplicativity. The two readings differ, so $N$ is not a norm of the block.

## The Functional That Survives

What the block does carry is not a norm of its own but the **Hermitian form** of the space,

$$
H(\tilde P,\tilde Q)=\operatorname{Sc}(\tilde P\tilde Q^{*})=\sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$

the positive definite form of *Norm and Invertibility in the General Plain Algebra*. It is a form on the space and not a norm of the block, and it is nondegenerate; its restriction to the image $\operatorname{Vect}(\mathbb{B})$ has signature $(3,0)$, and it is the form with respect to which the adjoints of the block are taken in *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*.

**Remark (why the form is the right residue).** The two functions of the norm of the algebra are to decide invertibility and to be multiplicative, and both are gone: the first because there is no invertibility to decide, the second because there is no norm to be multiplicative. What the form supplies in their place is a **pairing**, and the pairing of the block is developed where it belongs: the values $H(\tilde P\diamond\tilde Q,\tilde R)$, the Gram matrix, the invariance forms and the relation of the pairing to the norm of the value are *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*. This article stops at the statement that the form survives and the norm does not.

## Summary

The block has no unit on either side, by the parity of the scalar part: every value is a pure vector and the element $e_0$ is central, so the left-unit equation already fails at $\tilde u\diamond e_0=\mathbf{u}$ and the right-unit equation at $e_0\diamond\tilde u=-\overline{\mathbf{u}}$. The parent product $\tilde P\tilde Q^{*}$ has the right unit $e_0$, and the block loses it, the defect being the projection onto the vector subspace, which leaves the right-unit equation holding on the pure vectors alone: $\tilde P\diamond e_0=\tilde P$ exactly when $\tilde P$ is a pure vector, and never at an element with a non-zero scalar part.

The inverse is defined relative to a two-sided unit, so it is **vacuous** in the block: no element is invertible, the group of units is empty, and the two one-sided equations $\tilde Q\diamond\tilde R=e_0$ and $\tilde R\diamond\tilde Q=e_0$ have no solution, their left member being a pure vector and their right member central. This is the absence of the notion and not the emptiness of a set, and it is sharper than the plain product, where the invertible elements form the group of units.

The algebraic norm is a multiplicative quadratic form with central values, and the block carries no non-zero central value, so no norm descends to it: the diagonal $\tilde Q\diamond\tilde Q=\operatorname{Vect}(\tilde Q\tilde Q^{*})$ is degenerate, noncentral in general, and not multiplicative, its criterion and its quadric being *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*. The functional that survives is the Hermitian form $H$, a form of the space and not a norm of the block, and its pairing with the block is *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\diamond$ | the product of the block, $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ |
| $\operatorname{Vect}$ | the projection onto the vector subspace, $\tilde Q\mapsto\tilde Q-\operatorname{Sc}(\tilde Q)e_0$ |
| $\mathbb{C}_{\mathbb{B}}$, $\operatorname{Vect}(\mathbb{B})$ | the centre and the vector subspace, meeting at the origin |
| $e_0$ | the unit of the plain product and the right unit of the parent sesquilinear product, not a unit of the block |
| $\tilde P\diamond e_0=\mathbf{P}$, $e_0\diamond\tilde Q=-\overline{\mathbf{Q}}$ | the two one-sided actions that replace the unit |
| $H(\tilde P,\tilde Q)=\operatorname{Sc}(\tilde P\tilde Q^{*})$ | the Hermitian form, the functional that survives |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ | the algebraic norm of the plain product, which does not descend |
| $\tilde Q\diamond\tilde Q=\operatorname{Vect}(\tilde Q\tilde Q^{*})$ | the degenerate diagonal, not a norm |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Unit and the Inverse*, for the product-relative unit and inverse, and the unit table of the four general products.
- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), §*The Image and the Absence of a Unit*, for the image and the two one-sided actions.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the algebraic norm, its multiplicativity and its invertibility criterion.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the diagonal, its criterion and its quadric.
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the pairing of the block with the Hermitian form.
