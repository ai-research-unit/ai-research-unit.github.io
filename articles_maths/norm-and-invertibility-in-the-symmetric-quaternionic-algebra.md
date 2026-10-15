# __Norm and Invertibility in the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ is central, commutative and without unit (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). This article is the second Common Theory entry of the block, and its subject is the algebraic norm that the block carries and the inverse that it does not.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. For the block the form is $\mathrm{Sc}(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)$ and its diagonal is

$$
N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2},
$$

the symmetric quaternionic algebraic norm, complex-valued, indefinite and **not** multiplicative for the block; it is one of the four algebraic norms of the space and not one of the other three.

The invertibility is where the article records an **absence**. The block has **no left unit, no right unit and no two-sided unit**, so no element is invertible of the block and the block has no group of units. The one object it carries is the dichotomy of its algebraic norm, the non-isotropic class $N\neq0$ and the isotropic cone $N=0$, and the article records that this dichotomy is the analogue of a group of units without being one: the non-isotropic class coincides with the invertible set of the **plain** product, and it is not closed under the product of the block.

**Boundaries.** The general definitions of the unit and the inverse are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*; the definition of the algebraic norm as the form at the two equal arguments and the three other algebraic norms are *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*; the algebraic norm of the plain product is $B$, a different form, and its theory is *Norm and Invertibility in the General Plain Algebra*. The isotropic cone of the block is *Zero Divisors of the Symmetric Quaternionic Algebra*; the form read as the multiplication of the block is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*; the group of linear maps preserving the form and its Lie algebra are *The Multiplication Operators of the Symmetric Quaternionic Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$; a general element is $\tilde Q=Q_0e_0+\vec Q$ with $\vec Q=Q_1e_1+Q_2e_2+Q_3e_3$, and $(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\vec Q$. The **symmetric quaternionic multiplication** is $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)=\mathrm{Sc}(\tilde P\star\tilde Q)\,e_0$, with $\mathrm{Sc}(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q)$; it is written $\bullet$ in the Specific Theory and Operators entries of the block. Its diagonal is the algebraic norm of the block, $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2}$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$.

**The results.** The block carries exactly one algebraic norm, the diagonal of its scalar-part form, $N(\tilde Q)=\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2}$, complex-valued, indefinite, of Gram matrix the identity on $e_0,e_1,e_2,e_3$ and radical $\{0\}$. It is the multiplicative form of the plain product, $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ with $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, but it is **not** multiplicative for the block, where $N(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)^2$. The block has no left unit, no right unit and no two-sided unit, hence no inverse and no group of units. The non-isotropic class $N\neq0$ is exactly the group of units of the plain product, with the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$.

## The General Definitions

The two notions are relative to a product, and the general statements are those of the definitions article.

**Definition (unit of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star x=x$ for every $x$; a **right unit** when $x\star e=x$ for every $x$; and a **two-sided unit**, or an identity, when it is both. A product with a two-sided unit is **unital**, and the two-sided unit is then unique.

**Definition (inverse of a product).** Let $\star$ be a product with a two-sided unit $e$. An element $x$ is **left-invertible of $\star$** when there is $y$ with $y\star x=e$; **right-invertible** when there is $y$ with $x\star y=e$; and **invertible of $\star$** when there is $y$ with $x\star y=y\star x=e$. Such a $y$ is an **inverse of $x$**, written $x^{-1}$. In an associative unital product the inverse is unique, and the invertible elements form the **group of units**.

Throughout this article the product is the **symmetric quaternionic product** of the block, and the unit, the inverse and the group of units are the notions of that product.

## The Algebraic Norm of the Block

**The block carries one algebraic norm, the diagonal of its scalar-part form $N(\tilde Q)=\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2}$; it is complex-valued and indefinite, of Gram matrix the identity on $e_0,e_1,e_2,e_3$ and radical $\{0\}$, it is the multiplicative form of the plain product, $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ with $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, and it is **not** multiplicative for the block, where $N(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)^2$; the three conjugations preserve the product, and $N(\tilde Q^{\natural})=N(\tilde Q)$ while $N(\tilde Q^{*})=\overline{N(\tilde Q)}$.**

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
N(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu=0}^{3}Q_\mu^{2},
$$

equivalently $N(\tilde Q)=N(\tilde Q,\tilde Q)$ for the form

$$
N(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\star\tilde Q\bigr)=P_0Q_0+(\vec P,\vec Q),
$$

which is the general quaternionic bilinear form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*. The two are related by the square of the product, which is the diagonal placed in the centre, $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). The form is symmetric, $\mathbb{C}$-bilinear and non-degenerate, of Gram matrix the identity on the basis $e_0,e_1,e_2,e_3$; its radical is $\{0\}$ (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*).

**Theorem (the algebraic norm is the multiplicative form of the plain product).** The algebraic norm of the block satisfies

$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural},\qquad N(\tilde P\tilde Q)=N(\tilde P)\,N(\tilde Q),
$$

the second identity being the multiplicativity of the form for the **plain** product, not for the block; and the product of the block is the polarisation read on the central line,

$$
\tilde P\star\tilde Q=\tfrac12\bigl(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\bigr)e_0 .
$$

*Proof.* In the plain product $\tilde Q\tilde Q^{\natural}=\bigl(Q_0^2+(\vec Q,\vec Q)\bigr)e_0=N(\tilde Q)e_0$ by the multiplication table; the multiplicativity is the standard identity $(\tilde P\tilde Q)(\tilde P\tilde Q)^{\natural}=\tilde P\tilde Q\tilde Q^{\natural}\tilde P^{\natural}=N(\tilde P)N(\tilde Q)e_0$, using the centrality of the scalar; and the polarisation is the expansion of the square of $\tilde P+\tilde Q$ by bilinearity.

**Remark (the diagonal is the form, and only the form).** The symbol $N$ denotes the algebraic norm of the block and its polar form, and nothing else; the other three algebraic norms of the space are not read here. In particular the conjugate square $\tilde Q\star\tilde Q^{\natural}$ is a different element of the central line, with coefficient $N(\tilde Q,\tilde Q^{\natural})=Q_0^2-(\vec Q,\vec Q)$, and that coefficient is not the algebraic norm of the block.

**Proposition (the algebraic norm is not multiplicative for the block).** For the product of the block,

$$
N(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)^2,\qquad\text{which differs in general from } N(\tilde P)N(\tilde Q).
$$

At $\tilde P=e_1$, $\tilde Q=e_2$ the first is $0$ because $N(e_1,e_2)=0$, while the second is $1$.

*Proof.* $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ and $N(\lambda e_0)=\lambda^2$, so the first value is $N(\tilde P,\tilde Q)^2$; the witness is the computation of the table entry $e_1\star e_2=0$.

The block therefore carries **no multiplicative algebraic norm of its own**: the multiplicativity holds for the plain product, and the diagonal of the block transmits it to that product and no further. A reader who expects $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)$ is reading the multiplicity of the plain product into the block.

**Proposition (the three conjugations preserve the product).** The natural conjugation, the star and the Hermitian conjugation satisfy

$$
(\tilde P\star\tilde Q)^{\natural}=\tilde P^{\natural}\star\tilde Q^{\natural},\qquad
(\tilde P\star\tilde Q)^{*}=\tilde P^{*}\star\tilde Q^{*},\qquad
\overline{\tilde P\star\tilde Q}=\overline{\tilde P}\star\overline{\tilde Q},
$$

and the natural conjugation preserves the algebraic norm while the star conjugates its value, $N(\tilde Q^{\natural})=N(\tilde Q)$ and $N(\tilde Q^{*})=\overline{N(\tilde Q)}$.

*Proof.* The value is central, so each conjugation acts on it coefficientwise: $(\tilde P\star\tilde Q)^{\natural}=N(\tilde P,\tilde Q)e_0$ and $\tilde P^{\natural}\star\tilde Q^{\natural}=N(\tilde P^{\natural},\tilde Q^{\natural})e_0$, and $N(\tilde P^{\natural},\tilde Q^{\natural})=P_0Q_0+(-\vec P,-\vec Q)=N(\tilde P,\tilde Q)$; the star and the bar are the same computation with the coefficients conjugated. On the diagonal the first is $N(\tilde Q^{\natural})=N(\tilde Q)$ and the second $N(\tilde Q^{*})=\overline{N(\tilde Q)}$.

The natural conjugation, an anti-automorphism of the plain product, is an **automorphism** of the block, because it is $\mathbb{C}$-linear and the block is commutative with central values; the star and the Hermitian conjugation are **conjugate-linear**, hence conjugations of the block and not automorphisms of it.

## The Absence of a Unit and of an Inverse

**The symmetric quaternionic product has no left unit, no right unit and no two-sided unit, so no element is left-invertible, right-invertible or invertible of the block, the set of invertible elements is empty and the block has no group of units.**

**Theorem (the block is not unital).** The symmetric quaternionic product has no left unit, no right unit and no two-sided unit. For every element $\tilde A$,

$$
\tilde A\star e_0=e_0\star\tilde A=A_0e_0 ,
$$

so the element $e_0$ acts as the identity of the central line alone, and its action on an argument with non-vanishing vector part differs from the identity.

*Proof.* The display is the square formula at the argument $e_0$, $N(\tilde A,e_0)=A_0=N(e_0,\tilde A)$. A left unit $u$ would satisfy $u\star e_1=e_1$, that is $u_1e_0=e_1$, impossible because $u_1e_0$ is central and $e_1$ is not; the same with the roles exchanged excludes a right unit (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, §*The Image and the Unit*).

**Corollary (no inverse, no group of units).** Since the product has no two-sided unit, no element is left-invertible, right-invertible or invertible of the block; the set of invertible elements is empty, and the block has no group of units. The particular element $e_0$ is an idempotent of the block, $e_0\star e_0=e_0$, and it is not a unit: the two notions are different, and the idempotent is a unit of no product of the block.

*Proof.* The definition of the inverse presupposes a two-sided unit, which the theorem excludes; the statement about $e_0$ is the display at $\tilde A=e_0$, $e_0\star e_0=e_0$, together with the failure of the unit equations on $e_1$.

The absence is total and is not repaired by a change of element: it is the absence of the unit itself. The definition is nevertheless not idle, because the same words applied to the plain product have content, and that content is read on the algebraic norm of the block.

## The Non-Isotropic Class

**The non-isotropic class $N\neq0$ is exactly the group of units of the plain product, with the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$; it is stable under the plain product and not under the product of the block, its subset $N=1$ is a quadric of complex dimension three that is the analogue of a norm-one group without being one, and the group-theoretic substitute inside the block is the group of $\mathbb{C}$-linear maps preserving the form $N$, of matrices $\mathsf M$ with $\mathsf M^{\mathsf T}\mathsf M=I_4$.**

**Definition.** An element $\tilde Q$ of $\mathbb{B}$ is **non-isotropic** for the block when $N(\tilde Q)\neq0$, and **isotropic** when $N(\tilde Q)=0$. The non-isotropic class is the complement of the isotropic cone, and it is the analogue of a group of units without being one.

**Theorem (the non-isotropic class is the unit class of the plain product).** The non-isotropic elements of the block are precisely the invertible elements of the **plain** product: $\tilde Q$ is a unit of the plain product exactly when $N(\tilde Q)\neq0$, and its inverse of that product is

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)} .
$$

*Proof.* The plain product has the unit $e_0$ and the identity $\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_0$; for $N(\tilde Q)\neq0$ the displayed element is a two-sided inverse, and for $N(\tilde Q)=0$ with $\tilde Q\neq0$ the equation $\tilde Q\tilde R=e_0$ has no solution, the plain product being the multiplication of an algebra with zero divisors. The statement is a statement about the **plain** product read through the form $N$; it is not an invertibility of the block, which has none.

**Remark (the block owns the form, not the group).** The non-isotropic class is stable under the plain product by the multiplicativity $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, and it is **not** stable under the product of the block: $N(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)^2$ can vanish for non-isotropic factors, as at $e_1,e_2$. The invertibility of the plain product is therefore read on the algebraic norm of the block, and the product of the block has no invertibility to read.

**Remark (the algebraic norm-one slice).** The set $N(\tilde Q)=1$ is a quadric of complex dimension three, containing the four basis elements $e_0,e_1,e_2,e_3$; the three level sets $N=-1$, $N=0$, $N=1$ are the root sets of the block, read in *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* for $N=-1$ and $N=1$ and in *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* for $N=0$. The slice is the analogue of the norm-one group of an associative unital product, and it is not a group here, because the block has no unit to be the identity of it.

**Remark (the group of linear maps preserving the form).** The group-theoretic substitute inside the block is not a group of elements but a group of operators: the group of $\mathbb{C}$-linear maps of $\mathbb{B}$ preserving the form $N$, whose membership condition on a matrix $\mathsf M$ is $\mathsf M^{\mathsf T}\mathsf M=I_4$ because the Gram matrix is the identity. That group, its Lie algebra and the question of which elements of the block act by maps of it are *The Multiplication Operators of the Symmetric Quaternionic Algebra*; the block itself contributes no unit and hence no such group of elements.

## Summary

The symmetric quaternionic product $\tilde P\star\tilde Q=\mathrm{Sc}(\tilde P\star\tilde Q)e_0$ has no unit and no one-sided unit, hence no inverse and no group of units: the definitions of the unit and the inverse are those of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*, and the block answers them with an absence, the element $e_0$ being a unit of the central line alone.

The one object the block carries is its algebraic norm, the diagonal of its scalar-part form,

$$
N(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu=0}^{3}Q_\mu^{2},
$$

complex-valued, indefinite, the coefficient of the block-square and the multiplicative form of the plain product; it is **not multiplicative for the block**, $N(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)^2$. The non-isotropic class $N\neq0$ is precisely the group of units of the plain product, with the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$, so the invertibility of the plain product is read on the algebraic norm of the block; the isotropic class $N=0$ consists of $0$ together with the square-zero elements. The block owns the form and not the group, and it has no invertibility of its own.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)=P_0Q_0+(\vec P,\vec Q)$ | the general quaternionic bilinear form, the scalar-part form of the product |
| $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$ | the algebraic norm of the block, one of the four algebraic norms of the space |
| $N(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)^2$ | the failure of multiplicativity for the block |
| $N\neq0$, $N=0$ | the non-isotropic class, the isotropic cone |
| $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$ | the inverse in the plain product, read on the algebraic norm of the block |
| ${}^{\natural}$, ${}^{*}$, $\overline{\cdot}$ | the three conjugations; the natural one is an automorphism of the block, the other two are conjugate-linear |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the general quaternionic bilinear form and the table of the four forms.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), §*The Unit and the Inverse*, for the general definitions of the unit and the inverse.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the algebraic norm $B$ of the plain product, which is not the form $N$ of this article.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), for the isotropic cone of the block.
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the square of the block and the absence of a unit.
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form of the block, its Gram matrix and its real forms.
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the group of linear maps preserving the form and its Lie algebra.
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra.md`), for the level sets $N=-1$ and $N=1$ of the algebraic norm.
- *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra.md`), for the level set $N=0$.
