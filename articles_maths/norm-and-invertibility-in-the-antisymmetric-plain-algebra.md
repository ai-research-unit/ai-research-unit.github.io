# __Norm and Invertibility in the Antisymmetric Plain Algebra__

## Introduction

This article studies the algebraic norm and the invertibility of the antisymmetric plain multiplication

$$
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr)=\vec Q_1\times\vec Q_2,
$$

the cross product of the two vector parts, the antisymmetric half of the general plain bilinear product (*Introduction to the Antisymmetric Plain Algebra*). The operation is $\mathbb{C}$-bilinear, alternating and vector valued, and it has no unit on either side.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. For the block the scalar part is identically zero, $\mathrm{Sc}(\tilde Q_1\wedge\tilde Q_2)=0$, because every value is a pure vector; the algebraic norm of the operation is therefore **the zero function**, and by the convention of the same article a vanishing quadratic form is not an algebraic norm, so the block is counted with **no algebraic norm** rather than with a zero one.

The invertibility is a second and independent absence. The block has **no left unit, no right unit and no two-sided unit**, hence no inverse and an empty group of units; the inverse equation to the centre has no solution, because the block cannot produce a central value at all.

**The results.** The antisymmetric plain multiplication $\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2$ has no left unit, no right unit and no two-sided unit, hence no invertible element and an empty group of units; the inverse equation $\tilde Q_1\wedge\tilde Q_2=e_t$ has no solution, because every value of the block is a pure vector. Its scalar part vanishes identically, $\mathrm{Sc}(\tilde Q_1\wedge\tilde Q_2)=0$, so the algebraic norm of the block is the zero function and the block carries **no algebraic norm**. Both canonical quadratics built from the product, the square $\tilde Q_1\wedge\tilde Q_1$ and the conjugated square $\tilde Q_1\wedge\tilde Q_1^{\natural}$, vanish identically as well.

## The Relative Definitions

The word *unit* and the word *inverse* name a product, so the definitions are stated once for a general product and read on the block; they are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*.

**Definition (unit).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, a **right unit** when $\tilde Q_1\star e=\tilde Q_1$ for every $\tilde Q_1$, and a **two-sided unit** when it is both. A product with a two-sided unit is **unital**.

**Definition (inverse and group of units).** Let $\star$ be a unital product with identity $e$. An element $\tilde Q$ is **left-invertible of $\star$** when there is $\tilde Q_3$ with $\tilde Q_3\star\tilde Q=e$, **right-invertible** when there is $\tilde Q_3$ with $\tilde Q\star\tilde Q_3=e$, and **invertible** when there is $\tilde Q_3$ with $\tilde Q\star\tilde Q_3=\tilde Q_3\star\tilde Q=e$. Such an $\tilde Q_3$ is the **inverse of $\tilde Q$**, and in an associative unital product the invertible elements form the **group of units**.

Throughout this article the product is the antisymmetric plain multiplication $\wedge$ of the block, and the unit, the inverse and the group of units are read in $\wedge$.

## The Absence of a Unit

**The block has no left unit, no right unit and no two-sided unit.**

**Theorem (no unit).** The operation $\wedge$ has no left unit and no right unit; there is no $\tilde E$ with $\tilde E\wedge\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, and none with $\tilde Q_1\wedge\tilde E=\tilde Q_1$ for every $\tilde Q_1$. Hence there is no two-sided unit.

*Proof.* Let $\tilde E$ be a left unit. At $\tilde Q_1=e_t$, whose vector part is zero, the value is $\tilde E\wedge e_t=\vec E\times\mathbf{0}=0$, which would have to equal $e_t$; the two differ, since $e_t$ is nonzero. Let $\tilde E$ be a right unit. At $\tilde Q_1=e_t$ the value is $e_t\wedge\tilde E=\mathbf{0}\times\vec E=0$, which would again have to equal $e_t$. Hence neither one-sided unit exists.

The absence is structural: the value of the block is a pure vector for every pair of arguments, and the equations that would name a unit require the central element $e_t$ on the right. The scalar direction is invisible to the operation, and a unit is exactly an element the operation cannot see.

## The Absence of an Inverse

**No element of $\mathbb{B}$ is invertible of the block, the group of units of $\wedge$ is empty, and the inverse equation $\tilde Q_1\wedge\tilde Q_2=e_t$ has no solution.**

**Corollary (no inverse, no group of units).** No element of $\mathbb{B}$ is invertible of the block, and the group of units of $\wedge$ is empty.

*Proof.* The inverse is defined by the pair of equations $\tilde Q_1\wedge\tilde Q_2=e$ and $\tilde Q_2\wedge\tilde Q_1=e$ with $e$ a two-sided unit; the block has no two-sided unit by the theorem above, so the equations have no solution. There is no one-sided notion either, the one-sided inverse being defined against a one-sided unit and no one-sided unit existing.

**Remark (the equation to the centre).** A direct computation reaches the same conclusion without naming a unit. The equation

$$
\tilde Q_1\wedge\tilde Q_2=e_t
$$

has no solution in $\mathbb{B}$, because the left side is a pure vector, of scalar part zero, for every pair $\tilde Q_1,\tilde Q_2$, and the right side has scalar part one. The block cannot produce a central value at all, so the equation that defines an inverse is unsolvable even before the two-sided character of the unit is required.

## The Algebraic Norm of the Block

**The scalar part of the block vanishes identically, $\mathrm{Sc}(\tilde Q_1\wedge\tilde Q_2)=0$, so its algebraic norm is the zero function and the block carries no algebraic norm.**

**Definition (the algebraic norm of the operation).** Let $f$ be an operation on $\mathbb{B}$ with scalar-part form $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The **algebraic norm of $f$** is the diagonal of that form,

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)=\mathrm{Sc}\,f(\tilde Q,\tilde Q),
$$

and for an operation whose scalar part vanishes identically the algebraic norm is the zero function (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*).

**Theorem (the algebraic norm of the block is the zero function).** For the antisymmetric plain multiplication,

$$
\boxed{\;
\mathrm{Sc}\bigl(\tilde Q_1\wedge\tilde Q_2\bigr)=0\quad\text{for all }\tilde Q_1,\tilde Q_2,
\qquad\text{hence}\qquad
\varphi_{\wedge}(\tilde Q)=0\quad\text{for all }\tilde Q
\;}.
$$

The algebraic norm of the operation is identically zero, and by the convention of the definition the block carries **no algebraic norm**.

*Proof.* The value of the block is the cross product $\vec Q_1\times\vec Q_2$ of the two vector parts, a pure vector of scalar part zero for every pair; its diagonal is therefore the zero function. A vanishing quadratic form is not an algebraic norm, and its vanishing set is the whole space, so the block is counted with no algebraic norm rather than with a zero one.

**Remark (the two canonical quadratics of the block).** The product being alternating, the square and the conjugated square both vanish identically:

$$ \boxed{\; \tilde Q_1\wedge\tilde Q_1=0,\qquad \tilde Q_1\wedge\tilde Q_1^{\natural}=\vec X\times(-\vec X)=0 \;}. $$

There is therefore no central-valued quadratic map built from the product, neither $\tilde Q_1\wedge\tilde Q_1$ nor the conjugated square $\tilde Q_1\wedge\tilde Q_1^{\natural}$; the two coincide at the zero map and neither descends to an algebraic norm. The parent product $\tilde Q_1\tilde Q_2$ removes its scalar part in the block, and with the scalar part removed from a square the central quadratic form is gone.

## The Invertibility Criterion Is Not Transferred

**The invertibility criterion of the parent product is not read in the block: the block has no unit against which to invert and no algebraic norm to decide anything.**

**Remark (the criterion of the parent is not read here).** The general plain bilinear product $\tilde Q_1\tilde Q_2$ is associative and unital with unit $e_t$, and its invertibility is decided by the non-vanishing of its algebraic norm $\langle\cdot\rangle$, the diagonal of $\mathrm{Sc}(\tilde Q_1\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ (*Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*). That form is a different algebraic norm, it is not the algebraic norm of the block, and it is not read here. The block has no unit against which to invert and no algebraic norm to decide anything: no element is invertible, and the empty group of units is the sharp form of the statement.

## Summary

The antisymmetric plain multiplication $\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2$ has no unit on either side, hence no invertible element and an empty group of units, and the inverse equation $\tilde Q_1\wedge\tilde Q_2=e_t$ has no solution because every value of the block is a pure vector. The **algebraic norm** of the operation is the diagonal of its scalar-part form; the scalar part vanishes identically, the diagonal is the zero function, and by the convention of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* a vanishing quadratic form is not an algebraic norm, so the block carries **no algebraic norm**. Both canonical quadratics built from the product, the square and the conjugated square, vanish identically as well. The algebraic norm $\langle\cdot\rangle$ of the parent plain product is a different form of a different product and is not read here; no invertibility criterion is transferred, and the place of both notions is taken by the absence of a unit and of an inverse.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\wedge\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)=\vec Q_1\times\vec Q_2$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\tilde Q_1\tilde Q_2$ | the parent general plain bilinear product, associative and unital |
| $\mathrm{Sc}(\tilde Q_1\wedge\tilde Q_2)=0$ | the scalar part of the block vanishes identically |
| $\varphi_{\wedge}(\tilde Q)=0$ | the algebraic norm of the block, the zero function; the block carries no algebraic norm |
| $\tilde Q_1\wedge\tilde Q_1=0$, $\tilde Q_1\wedge\tilde Q_1^{\natural}=0$ | the square and the conjugated square, both identically zero |
| no unit, no inverse, no group of units | the absence carried by the block |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the definition of the algebraic norm as the diagonal of a scalar-part form, for the zero diagonal of the four antisymmetric operations, and for the convention that counts them with no algebraic norm.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the unit, the inverse and the relativity of the definitions to the product.
- [Introduction to the Antisymmetric Plain Algebra](introduction-to-the-antisymmetric-plain-algebra.html), for the operation, its class, its image and the absence of a unit.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the unit table of the four general products.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the algebraic norm $\langle\cdot\rangle$ of the plain product, which is not the form of this block.
- [The Symmetric and Antisymmetric Parts of an Algebra Product](the-symmetric-and-antisymmetric-parts-of-an-algebra-product.html), for the antisymmetrisation from which the block is written.
- [The Killing Form of the Antisymmetric Plain Algebra](the-killing-form-of-the-antisymmetric-plain-algebra.html), for the invariant forms of the block.
