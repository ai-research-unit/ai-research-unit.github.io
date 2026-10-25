# __Norm and Invertibility in the Antisymmetric Quaternionic Algebra__

## Introduction

This article studies the algebraic norm and the invertibility of the antisymmetric quaternionic multiplication

$$
\tilde Q_1\diamond\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr)
=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2,
$$

the antisymmetric part of the general quaternionic product $\tilde Q_1^{\natural}\tilde Q_2$ (*Introduction to the Antisymmetric Quaternionic Algebra*). The operation is $\mathbb{C}$-bilinear, alternating and vector valued, and it has no unit on either side.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. For the block the scalar part is identically zero, $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$, because every value is a pure vector; the algebraic norm of the operation is therefore **the zero function**, and by the convention of the same article a vanishing quadratic form is not an algebraic norm, so the block is counted with **no algebraic norm** rather than with a zero one.

The invertibility is a second and independent absence. The block has **no left unit, no right unit and no two-sided unit**, hence no inverse and an empty group of units; the inverse equation to the centre has no solution, because the block cannot produce a central value at all.

**The results.** The antisymmetric quaternionic multiplication has no left unit, no right unit and no two-sided unit, hence no inverse and an empty group of units, and the inverse equation $\tilde Q_1\diamond\tilde Q_2=e_t$ has no solution because every value of the block is a pure vector. Its scalar part vanishes identically, so its algebraic norm is the zero function and the block carries no algebraic norm rather than a zero one. Its square vanishes identically, $\tilde Q_1\diamond\tilde Q_1=0$, and its conjugated square is the pure vector $\tilde Q_1\diamond\tilde Q_1^{\natural}=-2Q_{1t}\vec Q_1$, so neither canonical quadratic is central-valued. The invertibility criterion $N\neq0$ of the parent quaternionic product is not transferred.

## The Relative Definitions

The word *unit* and the word *inverse* name a product, so the definitions are stated once for a general product and read on the block; they are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*.

**Definition (unit).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, a **right unit** when $\tilde Q_1\star e=\tilde Q_1$ for every $\tilde Q_1$, and a **two-sided unit** when it is both. A product with a two-sided unit is **unital**.

**Definition (inverse and group of units).** Let $\star$ be a unital product with identity $e$. An element $\tilde Q$ is **left-invertible of $\star$** when there is $\tilde{Q}_3$ with $\tilde{Q}_3\star\tilde Q=e$, **right-invertible** when there is $\tilde{Q}_3$ with $\tilde Q\star\tilde{Q}_3=e$, and **invertible** when there is $\tilde{Q}_3$ with $\tilde Q\star\tilde{Q}_3=\tilde{Q}_3\star\tilde Q=e$. Such an $\tilde{Q}_3$ is the **inverse of $\tilde Q$**, and in an associative unital product the invertible elements form the **group of units**.

Throughout this article the product is the antisymmetric quaternionic multiplication $\diamond$ of the block, and the unit, the inverse and the group of units are read in $\diamond$.

## The Absence of a Unit

**The operation $\diamond$ has no unit on either side: there is no left unit, no right unit and no two-sided unit.**

**Theorem (no unit).** The operation $\diamond$ has no left unit and no right unit; there is no $\tilde E$ with $\tilde E\diamond\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, and none with $\tilde Q_1\diamond\tilde E=\tilde Q_1$ for every $\tilde Q_1$. Hence there is no two-sided unit.

*Proof.* A left unit $\tilde E$ gives at $\tilde Q_1=e_t$ the value $\tilde E\diamond e_t=-\vec E$, which would have to equal $e_t$; a right unit gives at $\tilde Q_1=e_t$ the value $e_t\diamond\tilde E=\vec E$, which would have to equal $e_t$; and neither $-\vec E$ nor $\vec E$ is central for a nonzero value of $\vec E$, while $\vec E=0$ gives the value $0$.

The absence is structural: the value of the block is a pure vector for every pair of arguments, and the equations that would name a unit require the central element $e_t$ on one side. The block has, however, a one-sided identity on its own image: the element $e_t$ satisfies $e_t\diamond\tilde Q_1=\vec Q_1$ and $\tilde Q_1\diamond e_t=-\vec Q_1$, the two one-sided actions on the vector part; the operation itself remains without a two-sided unit.

## The Absence of an Inverse

**No element of $\mathbb{B}$ is invertible of the block and the group of units is empty; the inverse equation $\tilde Q_1\diamond\tilde Q_2=e_t$ has no solution.**

**Corollary (no inverse, no group of units).** No element of $\mathbb{B}$ is invertible of the block, and the group of units of $\diamond$ is empty.

*Proof.* The inverse is defined by the two equations $\tilde Q_1\diamond\tilde Q_2=\tilde Q_2\diamond\tilde Q_1=e$ with $e$ a two-sided unit; the block has no two-sided unit by the theorem above, so the equations have no solution. There is no one-sided notion either, the one-sided inverse being defined against a one-sided unit and no one-sided unit existing.

**Remark (the equation to the centre).** A direct computation reaches the same conclusion without naming a unit. The equation

$$
\tilde Q_1\diamond\tilde Q_2=e_t
$$

has no solution in $\mathbb{B}$, because the left side has zero scalar part for every pair $\tilde Q_1,\tilde Q_2$ and the right side has scalar part one. The block cannot produce a central value at all, so the equation that defines an inverse is unsolvable even before the two-sided character of the unit is required.

## The Algebraic Norm of the Block

**The scalar part of the block vanishes identically, so the algebraic norm of the operation is the zero function and the block carries no algebraic norm rather than a zero one; its square vanishes identically and its conjugated square is the pure vector $\tilde Q_1\diamond\tilde Q_1^{\natural}=-2Q_{1t}\vec Q_1$.**

**Definition (the algebraic norm of the operation).** Let $f$ be an operation on $\mathbb{B}$ with scalar-part form $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The **algebraic norm of $f$** is the diagonal of that form,

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)=\mathrm{Sc}\,f(\tilde Q,\tilde Q),
$$

and for an operation whose scalar part vanishes identically the algebraic norm is the zero function (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*).

**Theorem (the algebraic norm of the block is the zero function).** For the antisymmetric quaternionic multiplication,

$$
\boxed{\;
\mathrm{Sc}\bigl(\tilde Q_1\diamond\tilde Q_2\bigr)=0\quad\text{for all }\tilde Q_1,\tilde Q_2,
\qquad\text{hence}\qquad
\varphi_{\diamond}(\tilde Q)=0\quad\text{for all }\tilde Q
\;}.
$$

The algebraic norm of the operation is identically zero, and by the convention of the definition the block carries **no algebraic norm**.

*Proof.* The value $\tilde Q_1\diamond\tilde Q_2=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ is a pure vector: the scalar parts of $Q_{1t}\vec Q_2$ and $Q_{2t}\vec Q_1$ cancel, and the cross product has zero scalar part. Its diagonal is therefore the zero function. A vanishing quadratic form is not an algebraic norm, and its vanishing set is the whole space, so the block is counted with no algebraic norm rather than with a zero one.

**Remark (the two canonical quadratics of the block).** The product being alternating, the square vanishes identically, and the conjugated square is a pure vector:

$$ \boxed{\; \tilde Q_1\diamond\tilde Q_1=0,\qquad \tilde Q_1\diamond\tilde Q_1^{\natural}=-2Q_{1t}\vec Q_1 \;}. $$

The square is the zero map, and the conjugated square is central exactly on the vector subspace and on the centre, not everywhere; neither takes its values in the centre at every element, so no central-valued quadratic map is built from the product. The parent product $\tilde Q_1^{\natural}\tilde Q_2$ removes its scalar part in the block, and with the scalar part removed from a square the central quadratic form is gone.

## The Invertibility Criterion Is Not Transferred

**The algebraic norm $\langle\cdot\rangle_{\natural}$ of the parent quaternionic product is a different form and does not decide anything for the block: no element is invertible and the group of units is empty, so no invertibility criterion is transferred.**

**Remark (the criterion of the parent is not read here).** The general quaternionic bilinear product $\tilde Q_1^{\natural}\tilde Q_2$ is left-unital with left unit $e_t$, and its invertibility is decided by the non-vanishing of its algebraic norm $\langle\cdot\rangle_{\natural}$, the diagonal of $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ (*N-Regularity and Degeneracy in the Biquaternion Algebra*). That form is a different algebraic norm, it is not the algebraic norm of the block, and it is not read here. The block has no unit against which to invert and no algebraic norm to decide anything: no element is invertible, and the empty group of units is the sharp form of the statement.

## Summary

The antisymmetric quaternionic multiplication $\tilde Q_1\diamond\tilde Q_2=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ has no unit on either side, hence no invertible element and an empty group of units, and the inverse equation $\tilde Q_1\diamond\tilde Q_2=e_t$ has no solution because every value of the block is a pure vector. The **algebraic norm** of the operation is the diagonal of its scalar-part form; the scalar part vanishes identically, the diagonal is the zero function, and by the convention of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* a vanishing quadratic form is not an algebraic norm, so the block carries **no algebraic norm**. The square vanishes identically and the conjugated square is the pure vector $-2Q_{1t}\vec Q_1$, so neither canonical quadratic is central-valued. The algebraic norm $\langle\cdot\rangle_{\natural}$ of the parent quaternionic product is a different form of a different product and is not read here; no invertibility criterion is transferred, and the place of both notions is taken by the absence of a unit and of an inverse.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\diamond\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | the parent general quaternionic product |
| $\mathrm{Sc}(\tilde Q_1\diamond\tilde Q_2)=0$ | the scalar part of the block vanishes identically |
| $\varphi_{\diamond}(\tilde Q)=0$ | the algebraic norm of the block, the zero function; the block carries no algebraic norm |
| $\tilde Q_1\diamond\tilde Q_1=0$, $\tilde Q_1\diamond\tilde Q_1^{\natural}=-2Q_{1t}\vec Q_1$ | the square vanishes; the conjugated square is a pure vector |
| no unit, no inverse, no group of units | the absence carried by the block |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the definition of the algebraic norm as the diagonal of a scalar-part form, for the zero diagonal of the four antisymmetric operations, and for the convention that counts them with no algebraic norm.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the unit, the inverse and the relativity of the definitions to the product.
- [Introduction to the Antisymmetric Quaternionic Algebra](introduction-to-the-antisymmetric-quaternionic-algebra.html), for the operation, its class, its image and the absence of a unit.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the unit table of the four general products.
- [N-Regularity and Degeneracy in the Biquaternion Algebra](n-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the algebraic norm $\langle\cdot\rangle_{\natural}$ of the quaternionic product, which is not the form of this block.
- [The Symmetric and Antisymmetric Parts of an Algebra Product](the-symmetric-and-antisymmetric-parts-of-an-algebra-product.html), for the antisymmetrisation from which the block is written.
- [The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra](the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.html), for the invariant forms of the block.
