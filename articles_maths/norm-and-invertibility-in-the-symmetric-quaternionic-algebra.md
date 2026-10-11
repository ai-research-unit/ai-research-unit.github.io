# __Norm and Invertibility in the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ is central, commutative and without unit (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). This article is the second Common Theory entry of the block, and its subject is the pair of notions that the parent algebra carries and the block does not: a **norm** and an **inverse**. Both are stated as absences and not filled, and the article then records the **substitute** the block uses, which is exact and short.

The product has no unit and no one-sided unit, so the words *left-inverse*, *right-inverse* and *inverse* have no content in it, and the invertible elements do not form a group. What the block carries instead is a single quadratic form, the diagonal of the pairing, and it is the **norm of the parent plain product**; the criterion of invertibility of the parent runs on that diagonal, the inverse formula of the parent reads its denominator there, and the set of elements with non-vanishing diagonal is the exact analogue of the group of units. The article states the quadratic form, its non-multiplicativity for the block, the absence of a unit and of an inverse, and the transfer of the parent's invertibility theory onto the diagonal.

**Boundaries.** The general definitions of the unit and the inverse are *Definitions for the Study of the 12 Algebraic Structures* §*The Unit and the Inverse*; the norm, its multiplicativity, its polarisation, its real forms and the invertibility of the parent are *Norm and Invertibility in the General Plain Algebra*; the isotropic cone of the same form is *Zero Divisors of the General Plain Algebra* and, in the block, *Zero Divisors of the Symmetric Quaternionic Algebra*; the form read as the multiplication of the block is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*; the group of linear maps preserving the form and its Lie algebra are *The Multiplication Operators of the Symmetric Quaternionic Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, and central scalar imaginary $i$, $i^2=-1$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$, and $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$. The **symmetric quaternionic multiplication** is $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)=N(\tilde P,\tilde Q)e_0$, with $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$; it is written $\bullet$ in the Specific Theory and Operators entries of the block. Its diagonal is written $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$.

## The General Definitions

The two notions are relative to a product, and the general statements are those of the definitions article.

**Definition (unit of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star x=x$ for every $x$; a **right unit** when $x\star e=x$ for every $x$; and a **two-sided unit**, or an identity, when it is both. A product with a two-sided unit is **unital**, and the two-sided unit is then unique.

**Definition (inverse of a product).** Let $\star$ be a product with a two-sided unit $e$. An element $x$ is **left-invertible of $\star$** when there is $y$ with $y\star x=e$; **right-invertible** when there is $y$ with $x\star y=e$; and **invertible of $\star$** when there is $y$ with $x\star y=y\star x=e$. Such a $y$ is an **inverse of $x$**, written $x^{-1}$. In an associative unital product the inverse is unique, and the invertible elements form the **group of units**.

Throughout this article the product is the **symmetric quaternionic product** of the block, and the norm, the inverse and the group of units are the notions of that product. Where the corresponding notions of the parent general quaternionic product or of the general plain product are meant, they are named and cited.

## The Quadratic Form of the Block

**Definition.** The **form of the block** is the coefficient of the product, $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$, and its **diagonal** is

$$
N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2 .
$$

The two are related by the square of the product, which is the diagonal placed in the centre: $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). The form is symmetric, $\mathbb{C}$-bilinear and non-degenerate, of Gram matrix the identity on the basis $e_0,e_1,e_2,e_3$; its radical is $\{0\}$ (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*).

**Theorem (the diagonal is the norm of the parent product).** The diagonal of the block is the multiplicative norm of the general plain algebra,

$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural},
$$

and the block's product is its polarisation read on the central line, $\tilde P\star\tilde Q=\tfrac12\bigl(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\bigr)e_0$.

*Proof.* In the plain product $\tilde Q\tilde Q^{\natural}=\bigl(Q_0^2+(\mathbf Q,\mathbf Q)\bigr)e_0=N(\tilde Q)e_0$ (*Norm and Invertibility in the General Plain Algebra*), and $N(\tilde Q)=N(\tilde Q,\tilde Q)$ by definition; the polarisation is the expansion of the square of $\tilde P+\tilde Q$ by bilinearity.

**Remark (the two squares are different).** The diagonal $N(\tilde Q)$ and the conjugate square $\tilde Q\star\tilde Q^{\natural}$ are not the same element: $\tilde Q\star\tilde Q^{\natural}=N(\tilde Q,\tilde Q^{\natural})e_0=\bigl(Q_0^2-(\mathbf Q,\mathbf Q)\bigr)e_0$, the **other** quadratic form of the space. The block's norm is the diagonal $N(\tilde Q)=\tilde Q\star\tilde Q$'s coefficient, the one that equals the norm $\tilde Q\tilde Q^{\natural}$ of the parent plain algebra; the coefficient $Q_0^2-(\mathbf Q,\mathbf Q)$ is the form whose isotropic cone is the light cone of the two Hermitian subspaces (*Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*). The convention is stated here because the symbol $N$ is used throughout the block with the first meaning only.

**Proposition (the diagonal is not multiplicative for the block).** For the product of the block,

$$
N(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)^2,\qquad\text{which differs in general from } N(\tilde P)N(\tilde Q).
$$

At $\tilde P=e_1$, $\tilde Q=e_2$ the first is $0$ because $N(e_1,e_2)=0$, while the second is $1$.

*Proof.* $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$, and $N(\lambda e_0)=\lambda^2$; the witness is the computation of the table entry $e_1\star e_2=0$.

The block therefore carries **no multiplicative norm of its own**: the multiplicativity belongs to the parent plain product, and the diagonal of the block transmits it to that product and no further. A reader who expects $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)$ is reading the norm of the parent into the block.

**Proposition (the three conjugations preserve the product).** The natural conjugation, the star and the Hermitian conjugation satisfy

$$
(\tilde P\star\tilde Q)^{\natural}=\tilde P^{\natural}\star\tilde Q^{\natural},\qquad
(\tilde P\star\tilde Q)^{*}=\tilde P^{*}\star\tilde Q^{*},\qquad
\overline{\tilde P\star\tilde Q}=\overline{\tilde P}\star\overline{\tilde Q},
$$

and the natural conjugation preserves the diagonal while the star conjugates its value, $N(\tilde Q^{\natural})=N(\tilde Q)$ and $N(\tilde Q^{*})=\overline{N(\tilde Q)}$.

*Proof.* The value is central, so each conjugation acts on it coefficientwise: $(\tilde P\star\tilde Q)^{\natural}=N(\tilde P,\tilde Q)e_0$ and $\tilde P^{\natural}\star\tilde Q^{\natural}=N(\tilde P^{\natural},\tilde Q^{\natural})e_0$, and $N(\tilde P^{\natural},\tilde Q^{\natural})=P_0Q_0+(-\mathbf P,-\mathbf Q)=N(\tilde P,\tilde Q)$; the star and the bar are the same computation with the coefficients conjugated, using $N(\tilde P^{*},\tilde Q^{*})=\overline{N(\tilde P,\tilde Q)}$ and $N(\overline{\tilde P},\overline{\tilde Q})=\overline{N(\tilde P,\tilde Q)}$. On the diagonal the first is $N(\tilde Q^{\natural})=N(\tilde Q^{\natural},\tilde Q^{\natural})=N(\tilde Q)$ and the second $N(\tilde Q^{*})=\overline{N(\tilde Q)}$.

The natural conjugation, an anti-automorphism of the plain product, is an **automorphism** of the block, because it is $\mathbb{C}$-linear and the block is commutative with central values; the star and the Hermitian conjugation preserve the product as well, and they are **conjugate-linear**, hence conjugations of the block and not automorphisms of it. The contrast with the parent is the reason the diagonal is stable under the natural conjugation.

## The Absence of a Unit and of an Inverse

**Theorem (the block is not unital).** The symmetric quaternionic product has no left unit, no right unit and no two-sided unit. For every element $\tilde A$,

$$
\tilde A\star e_0=e_0\star\tilde A=A_0e_0 ,
$$

so the element $e_0$ acts as the identity of the central line alone, and its action on an argument with non-vanishing vector part differs from the identity.

*Proof.* The display is the square formula at the argument $e_0$, $N(\tilde A,e_0)=A_0=N(e_0,\tilde A)$. A left unit $u$ would satisfy $u\star e_1=e_1$, that is $u_1e_0=e_1$, impossible because $u_1e_0$ is central and $e_1$ is not; the same with the roles exchanged excludes a right unit (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, §*The Image and the Unit*).

**Corollary (no inverse, no group of units).** Since the product has no two-sided unit, no element is left-invertible, right-invertible or invertible of the block; the set of invertible elements is empty, and the block has no group of units. The particular element $e_0$ is an idempotent of the block — $e_0\star e_0=e_0$ — and it is not a unit: the two notions are different, and the idempotent is a unit of no product of the block.

*Proof.* The definition of the inverse presupposes a two-sided unit, which the theorem excludes; the statement about $e_0$ is the display at $\tilde A=e_0$, $e_0\star e_0=e_0$, together with the failure of the unit equations on $e_1$.

The absence is total and is not repaired by a change of element: it is the absence of the unit itself, and no element of the block plays the role. The definition is nevertheless not idle, because the same words applied to the parent product have content, and the content is read on the form of the block.

## The Substitute the Block Uses

**Definition.** An element $\tilde Q$ of $\mathbb{B}$ is **non-isotropic** for the block when $N(\tilde Q)\neq0$, and **isotropic** when $N(\tilde Q)=0$. The non-isotropic class is the complement of the isotropic cone, and it is the exact analogue of the group of units.

**Theorem (the non-isotropic class is the unit class of the parent).** The non-isotropic elements of the block are precisely the invertible elements of the general plain product: $\tilde Q$ is a unit of the plain product exactly when $N(\tilde Q)\neq0$, and its inverse of that product is

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)} .
$$

*Proof.* The plain product has the unit $e_0$ and the identity $\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_0$; for $N(\tilde Q)\neq0$ the displayed element is a two-sided inverse, and for $N(\tilde Q)=0$ there is no inverse because $\tilde Q\tilde R=0$ has the nonzero solution $\tilde R=\tilde Q^{\natural}$ (*Norm and Invertibility in the General Plain Algebra*).

**Corollary (the criterion of the parent, read on the diagonal of the block).** The criterion for invertibility of the parent, the inverse formula of the parent and the group of units of the parent are stated on the diagonal $N$ of the block, and the three statements are those of *Norm and Invertibility in the General Plain Algebra*; the block owns the form, not the group. The elements with $N(\tilde Q)=0$ are the zero divisors of the parent and the square-zero elements of the block (*Zero Divisors of the Symmetric Quaternionic Algebra*, *Nilpotents of the Symmetric Quaternionic Algebra*).

**Remark (the group of linear maps preserving the form).** The group-theoretic substitute inside the block is not a group of elements but a group of operators: the group of $\mathbb{C}$-linear maps of $\mathbb{B}$ preserving the form $N$, whose membership condition on a matrix $\mathsf M$ is $\mathsf M^{\mathsf T}\mathsf M=I_4$ because the Gram matrix is the identity. That group, its Lie algebra and the question of which elements of the block act by maps of it are *The Multiplication Operators of the Symmetric Quaternionic Algebra*; the block itself contributes no unit and hence no such group of elements.

**Remark (the norm-one slice).** The set $N(\tilde Q)=1$ is a quadric of complex dimension three, containing the four basis elements $e_0,e_1,e_2,e_3$; the three level sets $N=-1$, $N=0$, $N=1$ are the three root sets of the block (*Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*). The slice is the exact analogue of the norm-one group of an associative unital product, and it is not a group here, because the block has no unit to be the identity of it.

## Summary

The symmetric quaternionic product has no unit and no one-sided unit, hence no inverse and no group of units: the definitions of the unit and the inverse are those of *Definitions for the Study of the 12 Algebraic Structures*, and the block answers them with an absence, the element $e_0$ being a unit of the central line alone. The substitute the block uses is the single quadratic form $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$, the diagonal of the pairing, which is exactly the multiplicative norm $\tilde Q\tilde Q^{\natural}$ of the parent plain product; the block's product is its polarisation placed in the centre, the conjugate square $\tilde Q\star\tilde Q^{\natural}$ is the different form $Q_0^2-(\mathbf Q,\mathbf Q)$, and $N$ is not multiplicative for the block, $N(\tilde P\star\tilde Q)=N(\tilde P,\tilde Q)^2$. The non-isotropic class $N\neq0$ is precisely the group of units of the parent, with the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$, so the invertibility theory of the parent is read on the diagonal of the block; the isotropic class $N=0$ consists of $0$ together with the square-zero elements. The group-theoretic substitute inside the block is the group of linear maps preserving $N$, which is treated in the Operators entry and not here.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | the form of the block, the quaternion form |
| $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$ | the diagonal, the norm of the parent plain product |
| $N\neq0$, $N=0$ | the non-isotropic class, the isotropic cone |
| $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$ | the inverse in the parent plain product, read on the diagonal |
| ${}^{\natural}$, ${}^{*}$, $\overline{\cdot}$ | the three conjugations; the natural one is an automorphism of the block, the other two are conjugate-linear |
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definitions of the unit and the inverse.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the norm of the parent, its multiplicativity, its polarisation and the group of units of the parent.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the isotropic cone of the same norm.
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the square of the block and the absence of a unit.
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form of the block, its Gram matrix and its real forms.
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the group of linear maps preserving the form and its Lie algebra.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-symmetric-quaternionic-algebra.md`), for the three level sets of the diagonal.
