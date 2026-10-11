# __Norm and Invertibility in the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ on the biquaternion space, the general plain sesquilinear product read as a multiplication, the operation of *Introduction to the General Plain Sesqualgebra of Biquaternions*. This article studies the two notions that the general plain algebra attaches to its multiplication and that the block, having no two-sided unit, cannot inherit unchanged: the **norm** of an element and its **invertibility**.

A norm and an inverse name a product; the definitions are stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures* and are read here on the block. The block is **not unital in the strict sense**: it has a **right unit** $e_0$ and no left unit, so the group of units of the ordinary definition is not available. What the block carries instead is the **one-sided inverse**, and its equations are not empty — they have a solution for exactly the elements of non-vanishing norm, the right-inverse equation and the left-inverse equation pick out the same element, and that element is $(\tilde Q^{-1})^{*}=\overline{\tilde Q}/\overline{N(\tilde Q)}$. The norm that decides them is the **biquaternion norm** $\tilde Q\tilde Q^{\natural}$, and the same norm is the one of the parent algebra; the block does not change the norm, it changes the inverse.

**Placement.** The article is the second entry of the *Common Theory* section of the block, after *Introduction to the General Plain Sesqualgebra of Biquaternions*, and it precedes the articles on the zero divisors, on the roots of the central values, on the idempotents and on the nilpotents. It uses the product and the class of the introduction, the relative definitions, and the norm of the parent algebra.

**Boundaries.** The product, its class and its placement among the twelve structures are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the relative definitions of the unit, the inverse, the group of units and the norm are *Definitions for the Study of the 12 Algebraic Structures*, and the four general products with their one-sided units are *Comparison Between the Four General Products*. The norm, the polarisation, the Clifford form and the group of units of the parent are *Norm and Invertibility in the General Plain Algebra*; the common zero-divisor set of the four products is *The Zero Divisors and the Four General Products*; the matrix model that carries the square is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*. Nothing topological and nothing metric appears; the Euclidean norm of the block is the scalar part of the form, an element of the algebra and not a length.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde Q^{\natural}=\sum_\mu\varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon=(1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde Q}=\sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\sum_\mu\varepsilon_\mu\overline{Q_\mu}e_\mu$. Juxtaposition is the **plain** product $\tilde P\tilde Q$ and $\star$ the block, $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The **biquaternion norm** is

$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_{\mu=0}^{3}Q_\mu^{2},
$$

a complex number, the norm of the parent algebra. The **Euclidean norm** is $\lVert\tilde Q\rVert_E^{2}=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}$.

## The Right Unit and the Absence of the Left One

**Theorem (the block has a right unit and no left unit).** For every $\tilde Q$,

$$
\tilde Q\star e_0=\tilde Q,\qquad e_0\star\tilde Q=\tilde Q^{*}.
$$

Consequently $e_0$ is a **right unit** of $\star$, $e_0$ is **not** a left unit, and the block has **no two-sided unit**.

*Proof.* The first display is $\tilde Q\star e_0=\tilde Q e_0^{*}=\tilde Q e_0=\tilde Q$, and the second is $e_0\star\tilde Q=e_0\tilde Q^{*}=\tilde Q^{*}$. The left action of $e_0$ is the involution ${}^{*}$, which is not the identity because $\tilde Q^{*}\neq\tilde Q$ for an element with a nonzero vector part, for instance $\tilde Q=e_1$, whose image is $e_1^{*}=-e_1$. A left unit $e$ would satisfy $e\star\tilde Q=\tilde Q$ for all $\tilde Q$, hence $e\tilde Q^{*}=\tilde Q$; at $\tilde Q=e_0$ this gives $e=e_0$, and then at $\tilde Q=e_1$ it gives $e_0\star e_1=e_1^{*}=-e_1\neq e_1$, a contradiction. So there is no left unit and no two-sided unit.

**Remark (the reason is the derived-operation shape).** The second display is the identity that fixes the whole block: the row of $e_0$ is the involution, because the product is the derived operation $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ and the involution sits in the second slot. The right unit is the plain unit, unaffected, and the left action is twisted by the involution; the block is therefore **right-unital and not left-unital**, the mirror of the general quaternionic algebra, which is left-unital and not right-unital (*Comparison Between the Four General Products*).

## The One-Sided Inverses and Their Coincidence

The definitions of the one-sided inverse are those of *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*, and they are the equations

$$
\tilde Q\star\tilde R=e_0\qquad\text{(the right-inverse equation)},\qquad \tilde R\star\tilde Q=e_0\qquad\text{(the left-inverse equation)} .
$$

The element $e_0$ on the right-hand side is the right unit of the block, and the equations are the general ones of *The Zero Divisors and the Four General Products*, §*The One-Sided Inverse Equations*.

**Theorem (the one-sided inverses coincide, and the criterion is the norm).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

1. the right-inverse equation has a solution $\tilde R$;
2. the left-inverse equation has a solution $\tilde R$;
3. $N(\tilde Q)\neq0$.

When they hold, the solution is unique, it is the same for the two equations, and it is

$$
\tilde Q^{-1\star}=(\tilde Q^{-1})^{*}=\frac{\overline{\tilde Q}}{\overline{N(\tilde Q)}}=\bigl(\tilde Q^{\natural}\bigr)^{*}\big/\overline{N(\tilde Q)} .
$$

*Proof.* The right-inverse equation reads $\tilde Q\tilde R^{*}=e_0$. The map $\tilde R\mapsto\tilde R^{*}$ is a bijection, so it is solvable exactly when $\tilde Q$ has a plain right inverse, that is exactly when $N(\tilde Q)\neq0$, and then $\tilde R^{*}=\tilde Q^{-1}$ with $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$, so $\tilde R=(\tilde Q^{-1})^{*}$. The displayed formula is $(\tilde Q^{-1})^{*}=\bigl(\tilde Q^{\natural}/N(\tilde Q)\bigr)^{*}=\overline{\tilde Q}/\overline{N(\tilde Q)}$, the second step using $\bigl(\tilde Q^{\natural}\bigr)^{\natural}=\tilde Q$ and the centrality of $N(\tilde Q)$. This $\tilde R$ solves the left-inverse equation as well, because $\tilde R\star\tilde Q=\tilde R\tilde Q^{*}=(\tilde Q^{-1})^{*}\tilde Q^{*}=\bigl(\tilde Q\tilde Q^{-1}\bigr)^{*}=e_0^{*}=e_0$, using $(AB)^{*}=B^{*}A^{*}$. The solution is unique on each side because $\tilde R^{*}$ is unique, and the two are therefore one element.

**Remark (what the block inherits and what it does not).** The block inherits the plain unit group $\mathbb{B}^{\times}=\{\tilde Q: N(\tilde Q)\neq0\}$ as a set, and it is the set on which the one-sided inverse is defined, because the criterion is the same $N\neq0$. It does **not** inherit the group: the product $\star$ is not associative and $e_0$ is only a right unit, so the group axioms of *Definitions for the Study of the 12 Algebraic Structures* are not met and the block has no group of units in the strict sense. The inverse is real nevertheless, an operation $\tilde Q\mapsto\tilde Q^{-1\star}$ on $\mathbb{B}^{\times}$, and it is the substitution the block makes for the group of units.

**Remark (the inverse is the star-conjugate of the plain inverse).** The formula says $\tilde Q^{-1\star}=(\tilde Q^{-1})^{*}$: the inverse of the block is the image of the inverse of the parent under the Hermitian conjugation, and it is **not** the coefficientwise conjugate $\overline{\tilde Q^{-1}}=(\overline{\tilde Q})^{\natural}/\overline{N(\tilde Q)}$, which solves neither inverse equation. The two inverses agree exactly when $\tilde Q^{-1}$ is Hermitian, that is exactly when $\tilde Q$ is, so they agree on the Hermitian elements and differ off them; on the real quaternion subspace, where the coefficientwise conjugation is the identity, the block inverse is the quaternion conjugate $(\tilde Q^{-1})^{\natural}$ of the parent inverse, and the two agree only on the nonzero real scalars.

## The Norm and the Invertibility Criterion

**Theorem (the norm is multiplicative).** For all $\tilde P,\tilde Q$,

$$
N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q),\qquad\text{and}\qquad N(\tilde Q^{*})=\overline{N(\tilde Q)} .
$$

*Proof.* The first is the multiplicativity of the biquaternion norm, reproduced in *Norm and Invertibility in the General Plain Algebra*: $(\tilde P\tilde Q)(\tilde P\tilde Q)^{\natural}=\tilde P\tilde Q\tilde Q^{\natural}\tilde P^{\natural}=N(\tilde P)N(\tilde Q)$ by the centrality of the scalar $N$. For the second, $N(\tilde Q^{*})=\sum_\mu(\varepsilon_\mu\overline{Q_\mu})^{2}=\sum_\mu\overline{Q_\mu}^{2}=\overline{N(\tilde Q)}$, the $\varepsilon_\mu$ being real and squaring to one.

**Corollary (the norm of a block product).** For all $\tilde P,\tilde Q$,

$$
N(\tilde P\star\tilde Q)=N(\tilde P)\,\overline{N(\tilde Q)},\qquad N(\tilde Q\star\tilde Q)=N(\tilde Q)\,\overline{N(\tilde Q)}=\lvert N(\tilde Q)\rvert^{2} .
$$

*Proof.* $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, and the two multiplicativity rules give $N(\tilde P\tilde Q^{*})=N(\tilde P)N(\tilde Q^{*})=N(\tilde P)\overline{N(\tilde Q)}$; the second display is the case $\tilde P=\tilde Q$.

**Remark (the block is not norm-multiplicative, it is norm-conjugate-multiplicative).** The parent is norm-multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$; the block multiplies the norm of the first factor by the **conjugate** of the norm of the second. On the real quaternion subspace the two rules agree, and off it they are the two faces of the involution in the second slot. The square of an element is the special case $\lvert N(\tilde Q)\rvert^{2}$, a non-negative real number: the norm of the **block-square** is not the square of the norm but its squared modulus.

**Corollary (the criterion of the block).** An element $\tilde Q$ is one-sidedly invertible of the block, and hence invertible in the substituted sense of §*The One-Sided Inverses and Their Coincidence*, exactly when $N(\tilde Q)\neq0$.

*Proof.* This is the equivalence of the previous section, and it is the same equation as the invertibility criterion of the parent algebra; the block changes the inverse and not the criterion.

**Remark (the two quadratic forms).** Two quadratic forms are attached to an element and they must not be interchanged. The **biquaternion norm** $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ is complex, indefinite, multiplicative and vanishing on the zero divisors; it decides the invertibility. The **Euclidean norm** $\lVert\tilde Q\rVert_E^{2}=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}$ is real, positive definite and vanishing only at the origin; it is the scalar part of the block-square and it is the coefficient that the block's own product uses. The parent's criterion is the non-vanishing of the first; the definiteness is a property of the second; and the two are related by $\mathrm{Sc}(\tilde Q\tilde Q^{\natural})=\mathrm{Re}\,N(\tilde Q)$, not by an identity of the forms.

## The Block-Square and the Positive Cone

**Proposition (the block-square is Hermitian, and its scalar part is the Euclidean norm).** For every $\tilde Q$ the element $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ is Hermitian, $(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*}$, and its scalar part is

$$
\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}=\lVert\tilde Q\rVert_E^{2}\geq0 ,
$$

which vanishes only at $\tilde Q=0$. The block-square is **not** the plain square, and its vector part need not vanish.

*Proof.* The Hermitianness is $(\tilde Q\tilde Q^{*})^{*}=\tilde Q^{**}\tilde Q^{*}=\tilde Q\tilde Q^{*}$. The scalar part is $\sum_\mu Q_\mu\overline{Q_\mu}=\sum_\mu\lvert Q_\mu\rvert^{2}$. The block-square is not the plain square and not scalar in general, and its vector part need not vanish: at the zero divisor $\tilde Q=e_1+ie_2$ the plain square is $\tilde Q^{2}=0$ while the block-square is $\tilde Q\star\tilde Q=2e_0+2ie_3\neq0$, computed from the table of *Introduction to the General Plain Sesqualgebra of Biquaternions*.

**Remark (the positive cone, and what it is not).** The block-square takes its values in the **Hermitian subspace** $\mathbb{M}_{+}$, and the set of its values is the set of the Hermitian elements whose scalar part dominates the modulus of the vector part, computed in *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*. The block-square is therefore the algebraic positive cone of the derived operation, and it is **not** the biquaternion norm: $N$ is complex-valued and indefinite, and it vanishes at the nontrivial Hermitian idempotents $\tfrac12(e_0+i\hat\mu)$, which are themselves zero divisors.

## The Comparison with the General Plain Algebra

| clause | general plain algebra | general plain sesqualgebra |
|---|---|---|
| unit | $e_0$, two-sided | $e_0$ right unit only, no left unit |
| inverse equation | $\tilde Q\tilde R=\tilde R\tilde Q=e_0$ | $\tilde Q\tilde R^{*}=e_0$ and $\tilde R\tilde Q^{*}=e_0$, both |
| inverse | $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$, two-sided | $\tilde Q^{-1\star}=(\tilde Q^{-1})^{*}=\overline{\tilde Q}/\overline{N(\tilde Q)}$, the same element for the two equations |
| group of units | $\mathbb{B}^{\times}$, a group | none in the strict sense; the substitution is $\mathbb{B}^{\times}$ with the inverse $\tilde Q\mapsto\tilde Q^{-1\star}$ |
| criterion | $N(\tilde Q)\neq0$ | $N(\tilde Q)\neq0$ |
| norm of a product | $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$ | $N(\tilde P\star\tilde Q)=N(\tilde P)\overline{N(\tilde Q)}$ |
| the square | central, $\tilde Q^{2}$, scalar part $N(\tilde Q)$ | Hermitian, scalar part $\lVert\tilde Q\rVert_E^{2}\geq0$ |
| the scalar form | $\mathrm{Sc}(\tilde Q\tilde Q^{\natural})=\mathrm{Re}\,N(\tilde Q)$ | $\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}$ |

The two structures agree on the **criterion** and differ on everything else: the block keeps the norm of the parent, loses the two-sided unit and the group, replaces the two-sided inverse by the one-sided inverse with the conjugated formula, and replaces the central square by the Hermitian block-square whose scalar part is definite. The first four clauses are the absence and the substitution of this article; the last two are the quadratic-form reading used by the articles on the zero divisors and on the square roots.

## Summary

The general plain sesqualgebra $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ has a **right unit** $e_0$, because $\tilde Q\star e_0=\tilde Q e_0^{*}=\tilde Q$, and **no left unit**, because the left action of $e_0$ is the involution, $e_0\star\tilde Q=\tilde Q^{*}$; consequently it has **no two-sided unit** and **no group of units** in the ordinary sense. What replaces the inverse is the **one-sided inverse**, and its two equations, $\tilde Q\star\tilde R=e_0$ and $\tilde R\star\tilde Q=e_0$, have a solution for exactly the elements of non-vanishing **biquaternion norm** $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$, the solution is unique, it is the same for the two equations, and it is $\tilde Q^{-1\star}=(\tilde Q^{-1})^{*}=\overline{\tilde Q}/\overline{N(\tilde Q)}$, the star-conjugate of the parent inverse. The **criterion** is therefore the criterion of the parent, $N(\tilde Q)\neq0$, but the inverse is the star-conjugated one and the invertible set is a group only as a set, the product being non-associative and the unit only right. The norm is **conjugate-multiplicative** on the block, $N(\tilde P\star\tilde Q)=N(\tilde P)\overline{N(\tilde Q)}$, so that $N(\tilde Q\star\tilde Q)=\lvert N(\tilde Q)\rvert^{2}$. The block-square $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ is Hermitian, its scalar part is the definite Euclidean norm $\sum_\mu\lvert Q_\mu\rvert^{2}$, and it is not the plain square, its vector part being generally non-zero; the two quadratic forms, the complex indefinite $N$ that decides the invertibility and the real definite scalar form that the product uses, must be kept apart.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the product of the block |
| $e_0$ | the right unit; $e_0\star\tilde Q=\tilde Q^{*}$ is the involution |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ | the biquaternion norm, complex, multiplicative, indefinite |
| $N(\tilde Q^{*})=\overline{N(\tilde Q)}$ | the norm of the conjugate |
| $N(\tilde P\star\tilde Q)=N(\tilde P)\overline{N(\tilde Q)}$ | the conjugate-multiplicativity of the block |
| $\tilde Q^{-1\star}=(\tilde Q^{-1})^{*}=\overline{\tilde Q}/\overline{N(\tilde Q)}$ | the one-sided inverse, common to the two equations |
| $N(\tilde Q)\neq0$ | the invertibility criterion of the block |
| $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}\in\mathbb{M}_{+}$ | the block-square, Hermitian, scalar part $\lVert\tilde Q\rVert_E^{2}$ |
| $\lVert\tilde Q\rVert_E^{2}=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the Euclidean norm, definite |
| $\mathbb{B}^{\times}=\{N\neq0\}$ | the invertible set, a group only as a set |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product, the right unit and the involution in the second slot.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definitions of the unit, the inverse, the group of units and the norm.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the one-sided unit table of the four products.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the biquaternion norm, the multiplicativity, the criterion and the group of units of the parent.
- *The Zero Divisors and the Four General Products* (`articles_maths/the-zero-divisors-and-the-four-general-products.md`), for the one-sided inverse equations and the common zero-divisor set.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the matrix model $\mathsf{M}_2(\tilde P\star\tilde Q)=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$ in which the block-square is positive semidefinite.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the image of the block-square and the cone it generates in the Hermitian subspace.
- *The Specificities of the General Plain Sesqualgebra* (`articles_maths/the-specificities-of-the-general-plain-sesqualgebra.md`), for the operator reading of the same product.
