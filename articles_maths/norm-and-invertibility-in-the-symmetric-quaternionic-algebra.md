# __Norm and Invertibility in the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ is central, commutative and without unit (*Introduction to the Symmetric Quaternionic Algebra*). This article is the second Common Theory entry of the block, and its subject is the algebraic norm that the block carries and the inverse that it does not.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The Four Forms and the Four Algebraic Norms*. For the block the form is $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ and its diagonal is

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},
$$

the symmetric quaternionic algebraic norm, complex-valued, indefinite and **not** multiplicative for the block; it is one of the four algebraic norms of the space and not one of the other three.

The invertibility is where the article records an **absence**. The block has **no left unit, no right unit and no two-sided unit**, so no element is invertible of the block and the block has no group of units. The one object it carries is the dichotomy of its algebraic norm, the non-isotropic class $N\neq0$ and the isotropic cone $\langle\cdot\rangle_{\natural}=0$, and the article records that this dichotomy is the analogue of a group of units without being one: the non-isotropic class coincides with the invertible set of the **plain** product, and it is not closed under the product of the block.

**The results.** The block carries exactly one algebraic norm, the diagonal of its scalar-part form, $\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2}$, complex-valued, indefinite, of Gram matrix the identity on $e_t,\vec e_x,\vec e_y,\vec e_z$ and radical $\{0\}$. It is the multiplicative form of the plain product, $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ with $\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, but it is **not** multiplicative for the block, where $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}^2$. The block has no left unit, no right unit and no two-sided unit, hence no inverse and no group of units. The non-isotropic class $\langle\cdot\rangle_{\natural}\neq0$ is exactly the group of units of the plain product, with the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$.

## The General Definitions

The two notions are relative to a product, and the general statements are those of the definitions article.

**Definition (unit of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star x=x$ for every $x$; a **right unit** when $x\star e=x$ for every $x$; and a **two-sided unit**, or an identity, when it is both. A product with a two-sided unit is **unital**, and the two-sided unit is then unique.

**Definition (inverse of a product).** Let $\star$ be a product with a two-sided unit $e$. An element $x$ is **left-invertible of $\star$** when there is $y$ with $y\star x=e$; **right-invertible** when there is $y$ with $x\star y=e$; and **invertible of $\star$** when there is $y$ with $x\star y=y\star x=e$. Such a $y$ is an **inverse of $x$**, written $x^{-1}$. In an associative unital product the inverse is unique, and the invertible elements form the **group of units**.

Throughout this article the product is the **symmetric quaternionic product** of the block, and the unit, the inverse and the group of units are the notions of that product.

## The Algebraic Norm of the Block

**The block carries one algebraic norm, the diagonal of its scalar-part form $\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2}$; it is complex-valued and indefinite, of Gram matrix the identity on $e_t,\vec e_x,\vec e_y,\vec e_z$ and radical $\{0\}$, it is the multiplicative form of the plain product, $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ with $\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, and it is **not** multiplicative for the block, where $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}^2$; the three conjugations preserve the product, and $\langle\tilde Q^{\natural}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$ while $\langle\tilde Q^{*}\rangle_{\natural}=\overline{\langle\tilde Q\rangle_{\natural}}$.**

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},
$$

equivalently $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}$ for the form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde Q_1\star\tilde Q_2\bigr)=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2),
$$

which is the general quaternionic bilinear form of *The Four Forms and the Four Algebraic Norms*. The two are related by the square of the product, which is the diagonal placed in the centre, $\tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$ (*Introduction to the Symmetric Quaternionic Algebra*). The form is symmetric, $\mathbb{C}$-bilinear and non-degenerate, of Gram matrix the identity on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$; its radical is $\{0\}$ (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*).

**Theorem (the algebraic norm is the multiplicative form of the plain product).** The algebraic norm of the block satisfies

$$ \boxed{\; \langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural},\qquad \langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\,\langle\tilde Q_2\rangle_{\natural} \;}, $$

the second identity being the multiplicativity of the form for the **plain** product, not for the block; and the product of the block is the polarisation read on the central line,

$$
\tilde Q_1\star\tilde Q_2=\tfrac12\bigl(\langle\tilde Q_1+\tilde Q_2\rangle_{\natural}-\langle\tilde Q_1\rangle_{\natural}-\langle\tilde Q_2\rangle_{\natural}\bigr)e_t .
$$

*Proof.* In the plain product $\tilde Q\tilde Q^{\natural}=\bigl(Q_t^2+(\vec Q,\vec Q)\bigr)e_t=\langle\tilde Q\rangle_{\natural}e_t$ by the multiplication table; the multiplicativity is the standard identity $(\tilde Q_1\tilde Q_2)(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_1\tilde Q_2\tilde Q_2^{\natural}\tilde Q_1^{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}e_t$, using the centrality of the scalar; and the polarisation is the expansion of the square of $\tilde Q_1+\tilde Q_2$ by bilinearity.

**Remark (the diagonal is the form, and only the form).** The symbol $\langle\cdot,\cdot\rangle_{\natural}$ denotes the algebraic norm of the block and its polar form, and nothing else; the other three algebraic norms of the space are not read here. In particular the conjugate square $\tilde Q\star\tilde Q^{\natural}$ is a different element of the central line, with coefficient $\langle\tilde Q,\tilde Q^{\natural}\rangle_{\natural}=Q_t^2-(\vec Q,\vec Q)$, and that coefficient is not the algebraic norm of the block.

**Proposition (the algebraic norm is not multiplicative for the block).** For the product of the block,

$$ \boxed{\; \langle\tilde Q_1\star\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}^2,\qquad\text{which differs in general from } \langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural} \;}. $$

At $\tilde Q_1=\vec e_x$, $\tilde Q_2=\vec e_y$ the first is $0$ because $\langle \vec e_x,\vec e_y\rangle_{\natural}=0$, while the second is $1$.

*Proof.* $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ and $\langle \lambda e_t\rangle_{\natural}=\lambda^2$, so the first value is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}^2$; the witness is the computation of the table entry $\vec e_x\star \vec e_y=0$.

The block therefore carries **no multiplicative algebraic norm of its own**: the multiplicativity holds for the plain product, and the diagonal of the block transmits it to that product and no further. A reader who expects $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$ is reading the multiplicity of the plain product into the block.

**Proposition (the three conjugations preserve the product).** The natural conjugation, the star and the Hermitian conjugation satisfy

$$
(\tilde Q_1\star\tilde Q_2)^{\natural}=\tilde Q_1^{\natural}\star\tilde Q_2^{\natural},\qquad
(\tilde Q_1\star\tilde Q_2)^{*}=\tilde Q_1^{*}\star\tilde Q_2^{*},\qquad
\overline{\tilde Q_1\star\tilde Q_2}=\overline{\tilde Q}_1\star\overline{\tilde Q}_2,
$$

and the natural conjugation preserves the algebraic norm while the star conjugates its value, $\langle\tilde Q^{\natural}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$ and $\langle\tilde Q^{*}\rangle_{\natural}=\overline{\langle\tilde Q\rangle_{\natural}}$.

*Proof.* The value is central, so each conjugation acts on it coefficientwise: $(\tilde Q_1\star\tilde Q_2)^{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ and $\tilde Q_1^{\natural}\star\tilde Q_2^{\natural}=\langle\tilde Q_1^{\natural},\tilde Q_2^{\natural}\rangle_{\natural}e_t$, and $\langle\tilde Q_1^{\natural},\tilde Q_2^{\natural}\rangle_{\natural}=Q_{1t}Q_{2t}+(-\vec Q_1,-\vec Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$; the star and the bar are the same computation with the coefficients conjugated. On the diagonal the first is $\langle\tilde Q^{\natural}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$ and the second $\langle\tilde Q^{*}\rangle_{\natural}=\overline{\langle\tilde Q\rangle_{\natural}}$.

The natural conjugation, an anti-automorphism of the plain product, is an **automorphism** of the block, because it is $\mathbb{C}$-linear and the block is commutative with central values; the star and the Hermitian conjugation are **conjugate-linear**, hence conjugations of the block and not automorphisms of it.

## The Absence of a Unit and of an Inverse

**The symmetric quaternionic product has no left unit, no right unit and no two-sided unit, so no element is left-invertible, right-invertible or invertible of the block, the set of invertible elements is empty and the block has no group of units.**

**Theorem (the block is not unital).** The symmetric quaternionic product has no left unit, no right unit and no two-sided unit. For every element $\tilde Q_3$,

$$
\tilde Q_3\star e_t=e_t\star\tilde Q_3=Q_{3t}e_t ,
$$

so the element $e_t$ acts as the identity of the central line alone, and its action on an argument with non-vanishing vector part differs from the identity.

*Proof.* The display is the square formula at the argument $e_t$, $\langle\tilde Q_3,e_t\rangle_{\natural}=Q_{3t}=\langle e_t,\tilde Q_3\rangle_{\natural}$. A left unit $\tilde u$ would satisfy $\tilde u\star \vec e_x=\vec e_x$, that is $u_xe_t=\vec e_x$, impossible because $u_xe_t$ is central and $\vec e_x$ is not; the same with the roles exchanged excludes a right unit (*Introduction to the Symmetric Quaternionic Algebra*, §*The Image and the Unit*).

**Corollary (no inverse, no group of units).** Since the product has no two-sided unit, no element is left-invertible, right-invertible or invertible of the block; the set of invertible elements is empty, and the block has no group of units. The particular element $e_t$ is an idempotent of the block, $e_t\star e_t=e_t$, and it is not a unit: the two notions are different, and the idempotent is a unit of no product of the block.

*Proof.* The definition of the inverse presupposes a two-sided unit, which the theorem excludes; the statement about $e_t$ is the display at $\tilde Q_3=e_t$, $e_t\star e_t=e_t$, together with the failure of the unit equations on $\vec e_x$.

The absence is total and is not repaired by a change of element: it is the absence of the unit itself. The definition is nevertheless not idle, because the same words applied to the plain product have content, and that content is read on the algebraic norm of the block.

## The Non-Isotropic Class

**The non-isotropic class $\langle\cdot\rangle_{\natural}\neq0$ is exactly the group of units of the plain product, with the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$; it is stable under the plain product and not under the product of the block, its subset $\langle\cdot\rangle_{\natural}=1$ is a quadric of complex dimension three that is the analogue of a norm-one group without being one, and the group-theoretic substitute inside the block is the group of $\mathbb{C}$-linear maps preserving the form $\langle\cdot,\cdot\rangle_{\natural}$, of matrices $\mathsf M$ with $\mathsf M^{\mathsf T}\mathsf M=I_4$.**

**Definition.** An element $\tilde Q$ of $\mathbb{B}$ is **non-isotropic** for the block when $\langle\tilde Q\rangle_{\natural}\neq0$, and **isotropic** when $\langle\tilde Q\rangle_{\natural}=0$. The non-isotropic class is the complement of the isotropic cone, and it is the analogue of a group of units without being one.

**Theorem (the non-isotropic class is the unit class of the plain product).** The non-isotropic elements of the block are precisely the invertible elements of the **plain** product: $\tilde Q$ is a unit of the plain product exactly when $\langle\tilde Q\rangle_{\natural}\neq0$, and its inverse of that product is

$$ \boxed{\; \tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}} \;}. $$

*Proof.* The plain product has the unit $e_t$ and the identity $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$; for $\langle\tilde Q\rangle_{\natural}\neq0$ the displayed element is a two-sided inverse, and for $\langle\tilde Q\rangle_{\natural}=0$ with $\tilde Q\neq0$ the equation $\tilde Q\tilde Q_1=e_t$ has no solution, the plain product being the multiplication of an algebra with zero divisors. The statement is a statement about the **plain** product read through the form $\langle\cdot,\cdot\rangle_{\natural}$; it is not an invertibility of the block, which has none.

**Remark (the block owns the form, not the group).** The non-isotropic class is stable under the plain product by the multiplicativity $\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, and it is **not** stable under the product of the block: $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}^2$ can vanish for non-isotropic factors, as at $\vec e_x,\vec e_y$. The invertibility of the plain product is therefore read on the algebraic norm of the block, and the product of the block has no invertibility to read.

**Remark (the algebraic norm-one slice).** The set $\langle\tilde Q\rangle_{\natural}=1$ is a quadric of complex dimension three, containing the four basis elements $e_t,\vec e_x,\vec e_y,\vec e_z$; the three level sets $\langle\cdot\rangle_{\natural}=-1$, $\langle\cdot\rangle_{\natural}=0$, $\langle\cdot\rangle_{\natural}=1$ are the root sets of the block, read in *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* for $\langle\cdot\rangle_{\natural}=-1$ and $\langle\cdot\rangle_{\natural}=1$ and in *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* for $\langle\cdot\rangle_{\natural}=0$. The slice is the analogue of the norm-one group of an associative unital product, and it is not a group here, because the block has no unit to be the identity of it.

**Remark (the group of linear maps preserving the form).** The group-theoretic substitute inside the block is not a group of elements but a group of operators: the group of $\mathbb{C}$-linear maps of $\mathbb{B}$ preserving the form $\langle\cdot,\cdot\rangle_{\natural}$, whose membership condition on a matrix $\mathsf M$ is $\mathsf M^{\mathsf T}\mathsf M=I_4$ because the Gram matrix is the identity. That group, its Lie algebra and the question of which elements of the block act by maps of it are *The Multiplication Operators of the Symmetric Quaternionic Algebra*; the block itself contributes no unit and hence no such group of elements.

## Summary

The symmetric quaternionic product $\tilde Q_1\star\tilde Q_2=\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)e_t$ has no unit and no one-sided unit, hence no inverse and no group of units: the definitions of the unit and the inverse are those of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*, and the block answers them with an absence, the element $e_t$ being a unit of the central line alone.

The one object the block carries is its algebraic norm, the diagonal of its scalar-part form,

$$
\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},
$$

complex-valued, indefinite, the coefficient of the block-square and the multiplicative form of the plain product; it is **not multiplicative for the block**, $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}^2$. The non-isotropic class $\langle\cdot\rangle_{\natural}\neq0$ is precisely the group of units of the plain product, with the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$, so the invertibility of the plain product is read on the algebraic norm of the block; the isotropic class $\langle\cdot\rangle_{\natural}=0$ consists of $0$ together with the square-zero elements. The block owns the form and not the group, and it has no invertibility of its own.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$ | the symmetric quaternionic multiplication |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | the general quaternionic bilinear form, the scalar-part form of the product |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the algebraic norm of the block, one of the four algebraic norms of the space |
| $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}^2$ | the failure of multiplicativity for the block |
| $N\neq0$, $\langle\cdot,\cdot\rangle_{\natural}=0$ | the non-isotropic class, the isotropic cone |
| $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ | the inverse in the plain product, read on the algebraic norm of the block |
| ${}^{\natural}$, ${}^{*}$, $\overline{\cdot}$ | the three conjugations; the natural one is an automorphism of the block, the other two are conjugate-linear |

## Further Reading

- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the general quaternionic bilinear form and the table of the four forms.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the general definitions of the unit and the inverse.
- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the algebraic norm $\langle\cdot\rangle$ of the plain product, which is not the form $\langle\cdot,\cdot\rangle_{\natural}$ of this article.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the isotropic cone of the block.
- [Introduction to the Symmetric Quaternionic Algebra](introduction-to-the-symmetric-quaternionic-algebra.html), for the square of the block and the absence of a unit.
- [The Quaternion Form as a Product on the Symmetric Quaternionic Algebra](the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.html), for the form of the block, its Gram matrix and its real forms.
- [The Multiplication Operators of the Symmetric Quaternionic Algebra](the-multiplication-operators-of-the-symmetric-quaternionic-algebra.html), for the group of linear maps preserving the form and its Lie algebra.
- [Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the level sets $\langle\cdot\rangle_{\natural}=-1$ and $\langle\cdot\rangle_{\natural}=1$ of the algebraic norm.
- [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the level set $\langle\cdot,\cdot\rangle_{\natural}=0$.
