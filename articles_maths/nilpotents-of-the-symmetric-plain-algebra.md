# __Nilpotents of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*. This article determines the **nilpotents** of the block, the non-zero elements of square zero, describes their cone, and reads the operator each one produces.

The nilpotents of the block are the nilpotents of the algebra: the two squares agree, so the equation $\tilde\Upsilon\bullet\tilde\Upsilon=0$ is the equation $\tilde\Upsilon^2=0$, and the classification is the one of *Nilpotents of the General Plain Algebra*. The nilpotents are the pure isotropic elements, the non-zero roots of $0$; they form the nilpotent cone of the vector subspace, and their set coincides with the algebra's.

The block's own reading is the operator. In the algebra a square-zero element gives a **square-zero operator**, $L_{\tilde\Upsilon}^{2}=L_{\tilde\Upsilon^{\bullet2}}=0$, and the operator produces the flag $\{0\}\subseteq\mathrm{im}\,L_{\tilde\Upsilon}\subseteq\ker L_{\tilde\Upsilon}\subseteq\mathbb{B}$. In the block that fails at the first step: the operator of a nilpotent has **index three**, $L_{\tilde\Upsilon}^{2}\neq0$ and $L_{\tilde\Upsilon}^{3}=0$, its image is not contained in its kernel, and no flag is produced. The failure is the same failure of left alternativity that runs through the block, and its consequences are *The Specificities of the Symmetric Plain Algebra*.

A nilpotent is defined relative to a product, and the definition is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*; throughout this article the product is $\bullet$ and, unqualified, **nilpotent** means nilpotent of $\bullet$. The nilpotents of the algebra are *Nilpotents of the General Plain Algebra*; the associated zero divisors are *Zero Divisors of the Symmetric Plain Algebra*; and the operator theory is *The Multiplication Operators of the Symmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and $Q_\mu\in\mathbb{C}$. An element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$, and $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$. The product with the mark is $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$; the central square is $c(\tilde Q)=\sum_\mu Q_\mu^2$. The left multiplication is $L^{\bullet}_{\tilde X}:\tilde Y\mapsto\tilde X\bullet\tilde Y$.

## The Definition and the Criterion

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$; then $\tilde\Upsilon$ is a **nilpotent of $\star$**, or an element of **square zero**, when

$$
\tilde\Upsilon\neq0\qquad\text{and}\qquad\tilde\Upsilon\star\tilde\Upsilon=0 .
$$

The origin is a square-zero element of every product, and it is not a nilpotent.

Throughout this article the product is the symmetric plain product $\bullet$, and the equation is $\tilde\Upsilon\bullet\tilde\Upsilon=0$. It is the equation of the algebra, because the square of the block is the plain square; the criterion is therefore the criterion of the algebra.

**Theorem (the criterion).** An element of the block is nilpotent if and only if it is a non-zero pure isotropic element:

$$
\tilde\Upsilon\ \text{nilpotent of }\bullet\iff Q_0=0,\quad (\mathbf{Q},\mathbf{Q})=0,\quad \tilde\Upsilon\neq0 .
$$

*Proof.* Write $\tilde Q=Q_0e_0+\mathbf{Q}$; the plain square is $\tilde Q^2=\bigl[Q_0^2-(\mathbf{Q},\mathbf{Q})\bigr]e_0+2Q_0\mathbf{Q}$, and it vanishes exactly when $2Q_0\mathbf{Q}=0$ and $Q_0^2-(\mathbf{Q},\mathbf{Q})=0$. If $Q_0\neq0$ the first gives $\mathbf{Q}=0$ and the second $Q_0^2=0$, a contradiction, so $Q_0=0$; then the first is automatic and the second is $(\mathbf{Q},\mathbf{Q})=0$. So the square-zero elements are the pure isotropic ones and the origin.

The nilpotents are exactly the non-zero roots of $0$ of the block, and the criterion is the one of *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, §*The Roots of Zero*.

**Corollary.** The nilpotents of the block and the nilpotents of the algebra coincide, the two squares being the same.

## The Nilpotent Cone

**Definition.** The **nilpotent cone** of the block is the set of its nilpotents,

$$
\mathcal{N}=\{\tilde\Upsilon\in\mathrm{Vect}(\mathbb{B}):\ \tilde\Upsilon\neq0,\ (\tilde\Upsilon,\tilde\Upsilon)=0\}.
$$

It is the pure isotropic cone of the complex form $(\cdot,\cdot)$ restricted to the three-dimensional complex vector subspace. In real coordinates $\tilde\Upsilon=\mathbf{p}+i\mathbf{p}'$, the condition is the pair of real equations

$$
p_1^2+p_2^2+p_3^2-p'^2_1-p'^2_2-p'^2_3=0,\qquad p_1p_1'+p_2p_2'+p_3p_3'=0,
$$

so the cone is a **four-real-parameter** family and a complex quadric of complex dimension two. An example is $\tilde\Upsilon=e_1+ie_2$, for which

$$
(e_1+ie_2)^2=e_1^2+i^2e_2^2+i(e_1e_2+e_2e_1)=-e_0+e_0+0=0 .
$$


**Theorem.** The nilpotent cone of the block is exactly the nilpotent cone of the algebra, and it is a proper subset of the zero-divisor set of the block.

*Proof.* The coincidence is the corollary above; the strict inclusion is *Zero Divisors of the Symmetric Plain Algebra*, the vector subspace minus the origin being contained in the zero-divisor set and containing the cone properly, the element $e_1$ being pure, non-isotropic and a zero divisor.

So the block shares its nilpotents with the algebra and does not share its zero divisors; the two facts together say that the pure family of the block's zero divisors is strictly larger than the block's nilpotents.

## The Operator of a Nilpotent

### The Square-Zero Element Does Not Give a Square-Zero Operator

**Proposition.** For a nilpotent $\tilde\Upsilon$ the left multiplication is not square-zero: $L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0$, and its index is three,

$$
L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0,\qquad L^{\bullet}_{\tilde\Upsilon}{}^{3}=0 .
$$

*Proof.* On the witness $\tilde\Upsilon=e_1+ie_2$ the products are $\tilde\Upsilon\bullet e_0=\tilde\Upsilon$, $\tilde\Upsilon\bullet e_1=-e_0$, $\tilde\Upsilon\bullet e_2=-ie_0$, $\tilde\Upsilon\bullet e_3=0$; so $\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}=\mathrm{span}\{e_0,\tilde\Upsilon\}$, the image of the second power is $\mathrm{span}\{L^{\bullet}_{\tilde\Upsilon}e_0,L^{\bullet}_{\tilde\Upsilon}\tilde\Upsilon\}=\mathrm{span}\{\tilde\Upsilon,0\}=\mathbb{C}\tilde\Upsilon$, a line, and the third power is zero.

In the algebra the same witness has $L_{\tilde\Upsilon}^{2}=L_{\tilde\Upsilon^{\bullet2}}=L_{0}=0$, because the operator of a square is the square of the operator, which is left alternativity. The block is not left-alternative and the identity fails; the operator of a square-zero element has the index three of a regular nilpotent and not the index two of a square-zero one.

### The Absence of the Flag

**Corollary (no flag).** The image of $L^{\bullet}_{\tilde\Upsilon}$ is not contained in its kernel:

$$
\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}=\mathrm{span}\{e_0,\tilde\Upsilon\}\not\subseteq\ker L^{\bullet}_{\tilde\Upsilon},\qquad e_0\notin\ker L^{\bullet}_{\tilde\Upsilon}.
$$

*Proof.* The image is $\mathrm{span}\{e_0,\tilde\Upsilon\}$ and $L^{\bullet}_{\tilde\Upsilon}e_0=\tilde\Upsilon\neq0$, so the unit is not in the kernel; the containment that would place the image inside the kernel therefore fails.

So the block produces **no flag** $\{0\}\subseteq\mathrm{im}\,L\subseteq\ker L\subseteq\mathbb{B}$ from a nilpotent. The image and the kernel are two distinct subspaces of dimension two, and they are complementary,

$$
\mathbb{B}=\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}\oplus\ker L^{\bullet}_{\tilde\Upsilon},
$$

which is the shape the block produces instead: a direct sum and not a flag. On the witness the kernel is $\mathrm{span}\{e_3,-ie_1+e_2\}$, the image is $\mathrm{span}\{e_0,e_1+ie_2\}$, and the two are complementary.

### The Failure of the Ideal–Annihilator Coincidence

In the algebra the left ideal generated by a nilpotent coincides with its annihilator, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$. In the block the analogue fails.

**Proposition.** The image of $L^{\bullet}_{\tilde\Upsilon}$, the set $\mathbb{B}\bullet\tilde\Upsilon$, is $\mathrm{span}\{e_0,\tilde\Upsilon\}$, a two-dimensional subspace, and it is not the annihilator $\ker L^{\bullet}_{\tilde\Upsilon}$, which is the different two-dimensional subspace $\mathrm{span}\{e_3,-ie_1+e_2\}$; the two intersect only at the origin.

*Proof.* The image is computed above; the annihilator is computed in *Zero Divisors of the Symmetric Plain Algebra*, where the pure family has a kernel equal to the pure orthogonal complement of the vector part, for $\tilde\Upsilon=e_1+ie_2$ the subspace $\mathrm{span}\{e_3,-ie_1+e_2\}$. The unit is in the image and not in the kernel, so the intersection is trivial.

The coincidence $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ of the algebra is a theorem of its associativity, and the block, being non-associative, does not carry it.

## The Relation to the Other Notions

**Nilpotents and the zero divisors.** A nilpotent is a zero divisor with $\tilde\Upsilon\bullet\tilde\Upsilon=0$, and it belongs to the pure family of *Zero Divisors of the Symmetric Plain Algebra*, whose annihilator is the two-dimensional orthogonal complement of its vector part, a plane that contains the conjugate line, since $\tilde\Upsilon\bullet\tilde\Upsilon=0$, but is not it. Unlike the scalar family, its annihilator is not the line spanned by the conjugate.

**Nilpotents and the idempotents.** A nilpotent is a non-zero pure element, so it cannot be a non-trivial idempotent, which has scalar part $\tfrac12$; the only element that is both a square-zero element and an idempotent is the origin. The two families meet at the origin and nowhere else.

**Nilpotents and the roots.** The nilpotents are exactly the non-zero roots of $0$ of the block, and the roots of $0$ are the origin and them; this is the degeneracy of the general square-root problem at the central value $0$.

## Summary

The nilpotents of the block are the non-zero elements of square zero, and they are exactly the non-zero pure isotropic elements, the elements $\mathbf{p}+i\mathbf{p}'$ with $p_1^2+p_2^2+p_3^2-p'^2_1-p'^2_2-p'^2_3=0$ and $\mathbf{p}\cdot\mathbf{p}'=0$. They form the nilpotent cone, a four-real-parameter complex quadric, and they coincide with the nilpotents of the algebra, the two squares being equal; they are a proper subset of the block's zero-divisor set, which also contains every non-isotropic pure element. The block's own reading is the operator: a nilpotent gives **no** square-zero operator and **no** flag, its left multiplication having index three, $L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0$ and $L^{\bullet}_{\tilde\Upsilon}{}^{3}=0$, an image $\mathrm{span}\{e_0,\tilde\Upsilon\}$ not contained in its kernel, and the complementary decomposition $\mathbb{B}=\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}\oplus\ker L^{\bullet}_{\tilde\Upsilon}$ in place of a flag. The ideal–annihilator coincidence $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ of the algebra fails, the image and the annihilator being two different two-dimensional subspaces that meet only at the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\tilde\Upsilon$ | a nilpotent, $\tilde\Upsilon\neq0$ and $\tilde\Upsilon^{\bullet2}=0$ |
| $\mathcal N=\{\tilde\Upsilon\neq0:(\tilde\Upsilon,\tilde\Upsilon)=0\}$ | the nilpotent cone of the block |
| $\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}=\mathrm{span}\{e_0,\tilde\Upsilon\}$ | the image, of dimension two |
| $\ker L^{\bullet}_{\tilde\Upsilon}$ | the annihilator, of dimension two, orthogonal to the vector part |
| $L^{\bullet}_{\tilde\Upsilon}{}^{3}=0$, $L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0$ | the index-three operator of the nilpotent |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*, for the product-relative definition.
- *Nilpotents of the General Plain Algebra*, for the nilpotent cone of the algebra and its flag calculus, which the block does not have.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, for the roots of $0$ the nilpotents realise.
- *Zero Divisors of the Symmetric Plain Algebra*, for the pure family the nilpotents belong to and the annihilator computed there.
- *The Specificities of the Symmetric Plain Algebra*, for the left alternativity whose failure makes the operator of a nilpotent of index three.
