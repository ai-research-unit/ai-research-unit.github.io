# __Norm and Invertibility in the General Quaternionic Algebra__

## Introduction

This article studies the **algebraic norm** of the biquaternion algebra read through the general quaternionic bilinear product, and it settles what invertibility means for that product.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*. For the general quaternionic product the square of every element is scalar, so the scalar-part form is read directly off the square and its diagonal is the scalar that the square produces. That scalar is the quadratic form $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, the algebraic norm of this product and not the algebraic norm of the plain product, which is a different form on the same space; and it is multiplicative for $\star$.

The inverse is where the two products separate. The definition of an inverse, stated once in *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The Unit and the Inverse*, presupposes a product with a **two-sided unit**, and the general quaternionic product has a **left unit** alone. The consequence is stated and not filled: no element of $\mathbb{B}$ is invertible of $\star$, the product has no group of units of its own, and the word has no reading for it. What survives is the pair of one-sided inverse equations relative to the left unit $e_0$, and the article computes them: the two have the same unique solution, $(\tilde P^{-1})^{\natural}$, exactly when the norm is non-zero, and neither has a solution when the norm vanishes. The criterion is therefore the algebraic norm of this product, and it is not the algebraic norm of the plain product; the two products do not share their algebraic norms.

**The results.** The general quaternionic product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ has a central square, $\tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural}e_0$ with $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=Q_0^2+(\vec Q,\vec Q)$, and $\langle\cdot\rangle_{\natural}$ is multiplicative, $\langle\tilde P\star\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$. The product has the left unit $e_0$ and no right unit, hence no two-sided unit, so **no element is invertible of $\star$** and the product has **no group of units**; what survives is the pair of one-sided equations $\tilde P\star\tilde X=e_0$ and $\tilde X\star\tilde P=e_0$, soluble exactly when $\langle\tilde P\rangle_{\natural}\neq0$ with the common unique solution $(\tilde P^{-1})^{\natural}=\tilde P/\langle\tilde P\rangle_{\natural}$, and insoluble when $\langle\tilde P\rangle_{\natural}=0$. The criterion is therefore the algebraic norm: a nonzero $\tilde P$ is a zero divisor exactly when $\langle\tilde P\rangle_{\natural}=0$, and the elements of non-vanishing norm form the plain group of units $\mathbb{B}^{\times}=\{N\neq0\}$, stable under $\star$ but not a group under it. Each section below states its result first and then proves it.

**Boundaries.** The algebraic norm of the plain product is $\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$, a different form, and its theory is *Norm and Invertibility in the Biquaternion Algebra*; the algebraic norm $\langle\cdot\rangle_{\natural}$ is the one of this product, and the criterion $N\neq0$ is proved here. The zero divisors are *Zero Divisors of the General Quaternionic Algebra*, where the set $\{N=0\}\setminus\{0\}$ is characterised as a set; the one-sided inverse equations of the four general products side by side, and the tabulation of their solutions, are *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The One-Sided Inverse Equations*, whose table is quoted and not restated. The product and its element theory are *Introduction to the General Quaternionic Algebra*; the left multiplications and the monoid they form are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*; and the signatures of the norm on the remarkable subspaces are *Remarkable Subspaces under the General Quaternionic Algebra*. The Hermitian form $\tilde Q\tilde Q^{*}$ is a different object, of the informational sector, whose positivity is *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint* and whose scalar part carries the Euclidean norm of *The Euclidean Topology of the Biquaternion Algebra*; the polar scale $r$ as a physical reading is *The Polar Element Representation of Biquaternions* and *The Four Readings of a Biquaternion: Norm, Rank, Charge and Scale*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$. Juxtaposition is the plain product $\tilde P\tilde Q$, and the product of this article is the general quaternionic bilinear product

$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q ,
$$

with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_0-\vec Q$ and $\vec Q=\sum_{k=1}^{3}Q_ke_k$ the vector part. An element is $\tilde Q=Q_0e_0+\vec Q$, and $(\vec P,\vec Q)=\sum_kP_kQ_k$ is the complex bilinear form of the vector parts.

## The Algebraic Norm of the Product

**The general quaternionic product carries exactly one algebraic norm, the scalar of its central square, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=Q_0^2+(\vec Q,\vec Q)$; its polar form is the scalar coefficient $\langle\tilde P,\tilde Q\rangle_{\natural}=P_0Q_0+(\vec P,\vec Q)$ of the symmetrised product, and it is multiplicative, $\langle\tilde P\star\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$.**

### Definition

The algebraic norm of a product is the diagonal of its scalar-part form (*The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*).

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\varphi(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)$ be its scalar-part form. The **algebraic norm of $\star$** is the diagonal

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr).
$$

Throughout this article the product is the general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, whose square is central, so that the algebraic norm is the scalar coefficient of the square; it means the algebraic norm of that product.

**Proposition.** For every $\tilde Q\in\mathbb{B}$,

$$
\tilde Q\star\tilde Q=\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}\,e_0 , \qquad \langle\tilde Q\rangle_{\natural}=\sum_{\mu=0}^{3}Q_\mu^2=Q_0^2+(\vec Q,\vec Q) .
$$

**Proof.** The first display is the definition of the product at equal arguments; the scalar–vector form of *Introduction to the General Quaternionic Algebra* gives $\tilde Q^{\natural}\tilde Q=(Q_0-\vec Q)(Q_0+\vec Q)=Q_0^2-\vec Q^2$, and $\vec Q^2=-(\vec Q,\vec Q)$ for a vector part. The same scalar is produced in the two orders, $\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}$, because the computation read the other way, $(Q_0+\vec Q)(Q_0-\vec Q)=Q_0^2-\vec Q^2$, gives the same value.

The algebraic norm is therefore an element of $\mathbb{C}$ and not a length: it is the value of a quadratic form on the complex space $\mathbb{B}$, and its vanishing set is a cone and not a sphere.

### The Polarisation

**Proposition.** The polar form of the algebraic norm is the scalar coefficient of the symmetrised product. Writing

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=P_0Q_0+(\vec P,\vec Q) ,
$$

one has

$$
\langle\tilde P+\tilde Q\rangle_{\natural}-\langle\tilde P\rangle_{\natural}-\langle\tilde Q\rangle_{\natural}=2\langle\tilde P,\tilde Q\rangle_{\natural} , \qquad
\tilde P\star\tilde Q+\tilde Q\star\tilde P=2\langle\tilde P,\tilde Q\rangle_{\natural}\,e_0 .
$$

**Proof.** The scalar–vector form of $\tilde P+\tilde Q$ gives $\langle\tilde P+\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}+\langle\tilde Q\rangle_{\natural}+2\langle\tilde P,\tilde Q\rangle_{\natural}$; and $\tilde P\star\tilde Q+\tilde Q\star\tilde P=(\tilde P^{\natural}\tilde Q)+(\tilde P^{\natural}\tilde Q)^{\natural}$ has scalar part twice $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}$ and vanishing vector part, by the symmetry computation of the introduction.

The symmetric half read as an operation, with its centrality, its coefficient on the remarkable subspaces and its Jordan reading, is *The Symmetrised Quaternionic Product and the Hermitian Subspace*, which owns the symmetrisation; the proposition above is the same statement read as the polarisation of the quadratic form of the algebraic norm.

### Multiplicativity

**Proposition.** The algebraic norm is multiplicative for the product,

$$
\langle\tilde P\star\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\,\langle\tilde Q\rangle_{\natural} ,
$$

and it is invariant under the natural conjugation, $\langle\tilde P^{\natural}\rangle_{\natural}=\langle\tilde P\rangle_{\natural}$.

**Proof.** Since $\natural$ is an anti-automorphism and an involution, $(\tilde P^{\natural}\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural\natural}=\tilde Q^{\natural}\tilde P$, so

$$
\langle\tilde P\star\tilde Q\rangle_{\natural}=(\tilde P^{\natural}\tilde Q)^{\natural}(\tilde P^{\natural}\tilde Q)=\tilde Q^{\natural}\tilde P\tilde P^{\natural}\tilde Q=\tilde Q^{\natural}\langle\tilde P\rangle_{\natural}\tilde Q=\langle\tilde P\rangle_{\natural}\,\tilde Q^{\natural}\tilde Q=\langle\tilde P\rangle_{\natural}\,\langle\tilde Q\rangle_{\natural} ,
$$

using that $\langle\tilde P\rangle_{\natural}$ is central. For the invariance, $\langle\tilde P^{\natural}\rangle_{\natural}=\tilde P^{\natural}(\tilde P^{\natural})^{\natural}=\tilde P^{\natural}\tilde P=\langle\tilde P\rangle_{\natural}$.

The multiplicativity is the law of the algebraic norm of this product, and it is the reason this product is the one that carries the multiplicative quadratic form of the space; the plain product carries a different algebraic norm, $\langle\cdot\rangle$, which is not multiplicative.

**Corollary.** The vanishing set of the algebraic norm is stable under the product: if $\langle\tilde Q\rangle_{\natural}=0$ then $\langle\tilde P\star\tilde Q\rangle_{\natural}=0$ for every $\tilde P$, and the same with the factors exchanged.

## The Norm as a Semi-Norm

**Read as a norm of the algebra, $\langle\cdot\rangle_{\natural}$ is only a semi-norm: of the usual axioms the sign axiom holds, the triangle inequality has no content on a complex value, and the scaling axiom fails for a complex scalar.**

The scalar $\langle\cdot\rangle_{\natural}$ is the norm of the biquaternion algebra as well as the algebraic norm of the product $\star$, and read as a norm of the algebra it is the **semi-norm** of the biquaternion literature (Ward; Sangwine, Ell and Le Bihan), the name recording two departures from a norm: the value is complex rather than real, and a nonzero element can have vanishing value. The audit of the usual axioms is as follows.

- The **sign axiom** holds, $\langle-\tilde Q\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$.
- The **triangle inequality** has no content, because $\mathbb{C}$ carries no order.
- The **scaling axiom** fails for a complex scalar. The homogeneity is quadratic, $\langle\lambda\tilde Q\rangle_{\natural}=\lambda^{2}\langle\tilde Q\rangle_{\natural}$, and for the square root one has $\sqrt{\langle\lambda\tilde Q\rangle_{\natural}}=\sqrt{\lambda^{2}}\sqrt{\langle\tilde Q\rangle_{\natural}}$, where the principal square root $\sqrt{\lambda^{2}}$ lies in the right half-plane and not at $\lvert\lambda\rvert$: with $\lambda=i$ and $\tilde Q=e_0$, $\sqrt{\langle ie_0\rangle_{\natural}}=\sqrt{-1}=i$ against $\lvert\lambda\rvert\sqrt{\langle e_0\rangle_{\natural}}=1$. For a real $\lambda$ the axiom holds, and it is the complex case that the algebra is about.

So $\langle\cdot\rangle_{\natural}$ is a complex-valued multiplicative semi-norm: multiplicative, homogeneous of degree two over the complex scalars, indefinite, and vanishing exactly on the zero divisors. The failure of the scaling axiom is the arithmetic reason the polar representation carries a scale beside its phase, the phase not being the missing absolute value.

## The Unique Real Norm

**The unique multiplicative real norm on the units normalised by $\rho(\lambda e_0)=\lvert\lambda\rvert$ for real $\lambda$ is $r(\tilde Q)=\sqrt{\lvert \langle\tilde Q\rangle_{\natural}\rvert}=\sqrt{\lvert\det\mathsf{M}_2(\tilde Q)\rvert}$.**

The positive statement about size is sharp: there is a **unique** real norm that is multiplicative and normalised on the real scalars. If $\rho$ is a continuous multiplicative function from the group of units of $\mathbb{B}$ to the non-negative reals with

$$
\rho(\lambda e_0)=\lvert\lambda\rvert\qquad\text{for }\lambda\in\mathbb{R},
$$

then $\rho$ is determined, and it is

$$
r(\tilde Q)=\sqrt{\lvert \langle\tilde Q\rangle_{\natural}\rvert}=\sqrt{\lvert\det\mathsf{M}_2(\tilde Q)\rvert},
$$

where $\mathsf{M}_2$ is the matrix realisation of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, whose determinant is the norm.

*Proof.* The group of units is $\mathrm{GL}_2(\mathbb{C})$ under $\mathsf{M}_2$. A continuous homomorphism from $\mathrm{GL}_2(\mathbb{C})$ to $\mathbb{R}_{>0}$ is constant on the commutator subgroup; that subgroup is $\mathrm{SL}_2(\mathbb{C})$, which is perfect, so the homomorphism factors through the determinant, $\mathrm{GL}_2(\mathbb{C})\to\mathbb{C}^{\times}$. A continuous homomorphism $\mathbb{C}^{\times}\to\mathbb{R}_{>0}$ is $z\mapsto\lvert z\rvert^{t}$: on the positive reals it is a power, and the unit circle is compact and connected, so its image is trivial. Hence $\rho(\tilde Q)=\lvert\det\mathsf{M}_2(\tilde Q)\rvert^{t}$, and the normalisation gives $\lvert\lambda\rvert^{2t}=\lvert\lambda\rvert$, so $t=\tfrac12$, which is $r$ because $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

The function $r$ vanishes exactly on the zero divisors and is a genuine norm on the units. The uniqueness says that the scale carried by the polar representation is not a convention: it is the only real size function compatible with multiplicativity and with $r(e_0)=1$. The $4\times4$ regular representation carries $\det=N^{2}$ instead, so its face of the scale is the fourth root (*Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*). The reading of $r$ as the scale of the four-position, the four-velocity and the four-momentum is *The Polar Element Representation of Biquaternions* and *The Four Readings of a Biquaternion: Norm, Rank, Charge and Scale*. The **argument** of the norm, by contrast, is not a reading of its own: $\langle\cdot\rangle_{\natural}=\det\mathsf{M}_2(\tilde Q)$ and the polar central phase is $\alpha=\tfrac12\arg\det\mathsf{M}_2(\tilde Q)$, so $\arg N=2\alpha$ is twice the central phase owned by *The Polar Element Representation of Biquaternions*, and the complex value of $\langle\cdot\rangle_{\natural}$ therefore carries the modulus as its scale, the real part as the interval and the imaginary part as the coupling of the halves, its argument belonging to the central-rotation band.

## The Norm from the Halves

**On the halves $\tilde Q=q_r+iq_i$ the norm splits as $\Re N=\langle q_r\rangle_{\natural}-\langle q_i\rangle_{\natural}$ and $\Im N=2\langle q_r,q_i\rangle$, so $\langle\tilde Q\rangle_{\natural}=0$ exactly when the halves have equal norms and vanishing scalar product.**

Writing $\tilde Q=q_r+iq_i$ with $q_r,q_i$ real quaternions, the norm splits into its real and imaginary parts,

$$
\Re \langle\tilde Q\rangle_{\natural}=\langle q_r\rangle_{\natural}-\langle q_i\rangle_{\natural},\qquad \Im \langle\tilde Q\rangle_{\natural}=2\langle q_r,q_i\rangle,
$$

with $\langle q_r,q_i\rangle=\sum_\mu(q_r)_\mu(q_i)_\mu$ the scalar product of the two real quaternions. The special cases read directly:

- $q_r\perp q_i$: the norm is real, and negative whenever $\langle q_i\rangle_{\natural}>\langle q_r\rangle_{\natural}$;
- $\langle q_r\rangle_{\natural}=\langle q_i\rangle_{\natural}$: the norm is purely imaginary;
- $q_r=0$: the norm is $-\langle q_i\rangle_{\natural}$, negative real;
- $q_r\perp q_i$ **and** $\langle q_r\rangle_{\natural}=\langle q_i\rangle_{\natural}$: the norm vanishes.

So the criterion $\langle\tilde Q\rangle_{\natural}=0$ reads, on the halves, that they have **equal norms and vanishing scalar product**, which is the algebraic shape of a null element; the two families of the zero-divisor cone of *Zero Divisors of the General Quaternionic Algebra* are that condition read on the pure and on the non-pure elements.

## The Norm and the Hermitian Form

**The norm $\langle\cdot\rangle_{\natural}$ and the Hermitian form $\tilde Q\tilde Q^{*}$ are different objects: they coincide exactly on the quaternion subspace, the Hermitian form is the negative of the norm on the imaginary sector, and its scalar part $\sum_\mu\lvert Q_\mu\rvert^{2}$ is definite and detects no zero divisor.**

The two objects are of different kinds, and the difference is worth stating because the two words suggest a coincidence:

- the norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ is a complex scalar, multiplicative, and vanishes on the zero divisors;
- the Hermitian form $\tilde Q\tilde Q^{*}$ is a Hermitian element whose scalar part $\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}$ is non-negative and vanishes only at the origin.

They coincide as biquaternions exactly when all four coefficients are real, that is on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and on the imaginary sector $i\mathbb{H}_{\mathbb{B}}$ the Hermitian form is the **negative** of the norm, $+\sum_\mu(q'_\mu)^{2}e_0$. Elsewhere they differ in kind, and the scalar part of the Hermitian form **detects no zero divisor**: the element $e_0+ie_1$ has $\langle\cdot,\cdot\rangle_{\natural}=0$ and $\mathrm{Sc}(\tilde Q\tilde Q^{*})=2$. The norm carries the multiplicative structure — the invertibility, the zero divisors and the multiplicative quadratic form — and the scalar part of the Hermitian form carries the topological one, being the square of the Euclidean norm $\lVert\tilde Q\rVert_E=(\sum_\mu\lvert Q_\mu\rvert^{2})^{1/2}$, the unique topological norm of the space (*Remarkable Subspaces and the Four Algebraic Norms*; *The Euclidean Topology of the Biquaternion Algebra*).

## The Unit and the Absence of the Inverse

**The product has the left unit $e_0$ and no right unit, hence no two-sided unit, so no element of $\mathbb{B}$ is invertible of $\star$ and the product has no group of units.**

**Definition.** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star x=x$ for every $x$, a **right unit** when $x\star e=x$ for every $x$, and a **two-sided unit**, or **identity**, when it is both; and if $\star$ has a two-sided unit $e$, an element $x$ is **invertible of $\star$** when there is a $y$ with $x\star y=y\star x=e$. The definitions are *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The Unit and the Inverse*, and they name the product at every step.

The unit of the general quaternionic product is settled in *Introduction to the General Quaternionic Algebra*, and it is recalled here because the inverse depends on it.

**Proposition (the unit).** The element $e_0$ is a left unit of $\star$ and the only one; there is no right unit; hence there is no two-sided unit.

**Proof.** $e_0\star\tilde Q=e_0^{\natural}\tilde Q=e_0\tilde Q=\tilde Q$, and a left unit $\tilde E$ reads $\tilde E^{\natural}=e_0$ at $\tilde Q=e_0$, whence $\tilde E=e_0$. The equation $\tilde P\star\tilde E=\tilde P$ at $\tilde P=e_0$ forces $\tilde E=e_0$, and at $\tilde P=e_1$ reads $e_1\star e_0=-e_1\neq e_1$; so there is no right unit.

**Absence (the inverse).** The quaternionic product has no two-sided unit, so the definition of the inverse has no reading for it: **no element of $\mathbb{B}$ is invertible of $\star$**, and the product has no group of units. What the article computes in the next section is the pair of one-sided equations relative to the left unit $e_0$; it is not an inverse theory of the product, and it is never called one.

## The One-Sided Inverse Equations

**The two one-sided equations $\tilde P\star\tilde X=e_0$ and $\tilde X\star\tilde P=e_0$ have a solution exactly when $\langle\tilde P\rangle_{\natural}\neq0$, and then each has the same unique solution $(\tilde P^{-1})^{\natural}=\tilde P/\langle\tilde P\rangle_{\natural}$; when $\langle\tilde P\rangle_{\natural}=0$ neither equation has a solution.**

Relative to a left unit $e_0$ the two halves of the inverse equation remain meaningful, and they are the definition of the one-sided invertibility of the product.

**Definition.** Let $\tilde P\in\mathbb{B}$. An element $\tilde R$ with $\tilde P\star\tilde R=e_0$ is a **right inverse** of $\tilde P$ relative to $e_0$, and an element $\tilde L$ with $\tilde L\star\tilde P=e_0$ is a **left inverse** of $\tilde P$ relative to $e_0$. The element $\tilde P$ is **right-invertible** when it has a right inverse and **left-invertible** when it has a left inverse.

**Theorem (the one-sided equations).** For every $\tilde P\in\mathbb{B}$ the two equations

$$
\tilde P\star\tilde X=e_0 , \qquad \tilde X\star\tilde P=e_0
$$

have a solution exactly when $\langle\tilde P\rangle_{\natural}\neq0$, and then each has the **same unique** solution,

$$
\tilde X=(\tilde P^{-1})^{\natural}=\frac{\tilde P^{\natural\natural}}{\langle\tilde P^{\natural}\rangle_{\natural}}=\frac{\tilde P}{\langle\tilde P\rangle_{\natural}} ,
$$

where $\tilde P^{-1}=\tilde P^{\natural}/\langle\tilde P\rangle_{\natural}$ is the inverse of the plain product. When $\langle\tilde P\rangle_{\natural}=0$ neither equation has a solution.

**Proof.** The first equation is $\tilde P^{\natural}\tilde X=e_0$, a plain-product equation with the fixed right-hand side $e_0$; composing on the left with the plain inverse of $\tilde P^{\natural}$, legitimate exactly when that element is invertible, gives $\tilde X=(\tilde P^{\natural})^{-1}$. The plain algebra is associative, so the solution is unique when it exists. Now $\tilde P^{\natural}$ is a unit of the plain product exactly when $\langle\tilde P^{\natural}\rangle_{\natural}\neq0$, that is exactly when $\langle\tilde P\rangle_{\natural}\neq0$, and its inverse is $(\tilde P^{\natural})^{-1}=(\tilde P^{\natural})^{\natural}/\langle\tilde P^{\natural}\rangle_{\natural}=\tilde P/\langle\tilde P\rangle_{\natural}=(\tilde P^{-1})^{\natural}$. This proves the statement for the first equation. For the second, $\tilde X\star\tilde P=\tilde X^{\natural}\tilde P=e_0$; composing on the right with the plain inverse of $\tilde P$ gives $\tilde X^{\natural}=\tilde P^{-1}$, hence $\tilde X=(\tilde P^{-1})^{\natural}$, the same element, and the same invertibility condition. If $\langle\tilde P\rangle_{\natural}=0$ and $\tilde P\neq0$ then $\tilde P^{\natural}$ is a zero divisor of the plain product, so the equation $\tilde P^{\natural}\tilde X=e_0$ has no solution; and if $\tilde P=0$ the equations read $0=e_0$, also with no solution.

**Remark.** The common solution is the natural conjugate of the plain inverse, and not the plain inverse itself. The coincidence of the two one-sided solutions, and the fact that they are given by the plain inverse of the conjugated element, are the whole content of the table of *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* §*The One-Sided Inverse Equations* read on this product; the table is quoted there and the computation is the one above.

**Corollary.** The element $\tilde P$ is left-invertible and right-invertible relative to $e_0$ exactly when $\langle\tilde P\rangle_{\natural}\neq0$, and then one and the same element, $(\tilde P^{-1})^{\natural}$, serves as both a left inverse and a right inverse:

$$
\tilde P\star(\tilde P^{-1})^{\natural}=e_0=(\tilde P^{-1})^{\natural}\star\tilde P .
$$

**Proof.** The theorem gives the two solutions and they are equal. The displayed identity is the theorem at that element, using $\tilde P\star\tilde R=\tilde P^{\natural}(\tilde P^{-1})^{\natural}=(\tilde P^{-1}\tilde P)^{\natural}=e_0$ and $(\tilde P^{-1})^{\natural}\star\tilde P=(\tilde P^{-1})^{\natural\natural}\tilde P=\tilde P^{-1}\tilde P=e_0$.

The corollary is a statement about the left unit $e_0$ and not an inverse of the product, because the product has no right unit: the equation it solves uses $e_0$ on the right, where $e_0$ is not a right unit, so the solution is a one-sided object of each equation and not an inverse in the sense of *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

## The Criterion

**For a nonzero $\tilde P$ the conditions $\langle\tilde P\rangle_{\natural}\neq0$, solubility of the plain equation $\tilde P\tilde X=e_0$, and solubility of the two one-sided equations of $\star$ are equivalent; equivalently, $\tilde P$ is a zero divisor of the algebra exactly when $\langle\tilde P\rangle_{\natural}=0$.**

**Theorem (the criterion for the general quaternionic product).** For a nonzero $\tilde P\in\mathbb{B}$ the following are equivalent:

1. $\langle\tilde P\rangle_{\natural}\neq0$;
2. the plain-product equation $\tilde P\tilde X=e_0$ has a solution, namely $\tilde X=\tilde P^{-1}=\tilde P^{\natural}/\langle\tilde P\rangle_{\natural}$;
3. the two one-sided equations of §*The One-Sided Inverse Equations* have a solution.

They are equivalent to the single negative statement that $\tilde P$ is a zero divisor of the algebra if and only if $\langle\tilde P\rangle_{\natural}=0$.

**Proof.** The equivalence of (1) and (2) is the statement that the scalar $\tilde P^{\natural}\tilde P=\langle\tilde P\rangle_{\natural}e_0$ is nonzero exactly when $\tilde P$ is not a zero divisor of the plain product, which is the zero-divisor criterion of *Zero Divisors of the General Quaternionic Algebra*. The equivalence of (1) and (3) is the theorem of the preceding section. For the last clause, $\tilde P\neq0$ with $\langle\tilde P\rangle_{\natural}=0$ is a zero divisor of the algebra, and conversely (*Zero Divisors of the General Quaternionic Algebra*).

The criterion is expressed by the algebraic norm $\langle\cdot\rangle_{\natural}$ of this product, because the vanishing set of $\langle\cdot\rangle_{\natural}$ is the zero-divisor set; it is not expressible by the algebraic norm of the plain product, which is $\langle\cdot\rangle$ and does not decide invertibility (*Norm and Invertibility in the Biquaternion Algebra*).

**Corollary.** If $\tilde P$ is a unit of the plain product, so is $\tilde P^{\natural}$, and $(\tilde P^{\natural})^{-1}=\overline{\tilde P^{-1}}$.

**The unit-norm case, and the dagger.** For an element of **unit norm**, $\langle\tilde P\rangle_{\natural}=1$, the inverse formula collapses to

$$
\tilde P^{-1}=\tilde P^{\natural},
$$

the quaternion conjugate; this is the case of every rotor. The dagger coincides with it exactly on the unitary elements, $\tilde P\tilde P^{*}=e_0$: a rotation rotor with real coefficients has $\tilde R^{-1}=\tilde R^{\natural}=\tilde R^{*}$, while a boost rotor is Hermitian, $\tilde B^{*}=\tilde B$, so its dagger is itself and not its inverse,

$$
\tilde B = \cosh\frac{\psi}{2}e_0 + i\sinh\frac{\psi}{2}\,e_3, \qquad
\tilde B^{-1} = \tilde B^{\natural} = \cosh\frac{\psi}{2}e_0 - i\sinh\frac{\psi}{2}\,e_3 \neq \tilde B^{*} = \tilde B .
$$

The two operations are therefore interchangeable in the rotation case and must be kept apart in the boost case; the distinction is the algebraic form of the statement that the action $\tilde Q\mapsto\tilde R\tilde Q\tilde R^{*}$ is an inner automorphism in the unitary sector and not elsewhere (*Biquaternion Rotations and Lorentz Transformations*; *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*; *The Operators of the Bilinear Product: One-Sided, Two-Sided and the Sandwich*).

## The Three-Way Classification

**The elements of $\mathbb{B}$ fall into exactly three classes by the value of $\langle\cdot\rangle_{\natural}$: $\langle\tilde P\rangle_{\natural}\neq0$ gives a unit of the plain product with both one-sided equations of $\star$ soluble, while $\langle\tilde P\rangle_{\natural}=0$ gives the zero element at $\tilde P=0$ and a zero divisor, with neither equation soluble, otherwise.**

The elements of $\mathbb{B}$ fall into three classes according to the value of the algebraic norm, and the classes are the ones of the plain algebra with the inverse column replaced by the one-sided column.

| condition on $\langle\tilde P\rangle_{\natural}$ | condition on $\tilde P$ | under the plain product | under the quaternionic product |
|---|---|---|---|
| $\langle\tilde P\rangle_{\natural}\neq0$ | none | a unit | the one-sided equations soluble, with the common solution $(\tilde P^{-1})^{\natural}$ |
| $\langle\tilde P\rangle_{\natural}=0$ | $\tilde P=0$ | the zero element | the zero element |
| $\langle\tilde P\rangle_{\natural}=0$ | $\tilde P\neq0$ | a zero divisor | a zero divisor, with neither one-sided equation soluble |

The classification is a classification of the elements by their behaviour in the two products, and the middle column is quoted from *Zero Divisors of the General Quaternionic Algebra*; the third column is this article.

## The Group of Units, and Why There Is None

**The set $\mathbb{B}^{\times}=\{\tilde P:\langle\tilde P\rangle_{\natural}\neq0\}$ is the group of units of the plain product and is stable under $\star$, but it is not a group under $\star$, because that product has no two-sided unit and is not associative.**

Let $\mathbb{B}^{\times}=\{\tilde P:\langle\tilde P\rangle_{\natural}\neq0\}$ be the set of the elements on which the algebraic norm does not vanish.

**Proposition.** The set $\mathbb{B}^{\times}$ is the group of units of the plain product, it contains $e_0$, and it is stable under the quaternionic product. It is **not** a group under $\star$: the product has no two-sided unit and it is not associative, so $\mathbb{B}^{\times}$ with $\star$ is a set with a left unit in which every left translation is a bijection, and nothing more.

**Proof.** The first clause is the plain invertibility criterion. Stability under $\star$ is the multiplicativity of the algebraic norm: $\langle\tilde P\star\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}\neq0$. The absence of a two-sided unit is §*The Unit and the Absence of the Inverse*, and the failure of associativity is *Introduction to the General Quaternionic Algebra*; a group requires both, so there is none. Finally, the left translation $\tilde X\mapsto\tilde P\star\tilde X=L^{\mathrm{plain}}_{\tilde P^{\natural}}(\tilde X)$ is a plain left multiplication by a unit and is therefore a bijection, and the same holds on the right by the multiplicativity read in the other order.

**Corollary (the group of the left multiplications).** The left multiplications $L_{\tilde P}$ with $\tilde P\in\mathbb{B}^{\times}$ are the invertible left multiplications of the product; they form a group under composition, and the map $\tilde P\mapsto L_{\tilde P}$ is an anti-isomorphism of $\mathbb{B}^{\times}$ onto it. The monoid law $L_{\tilde P}L_{\tilde R}=L_{\tilde R\tilde P}$ and the failure of the right family are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*.

**Proof.** $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$ is invertible exactly when $\tilde P^{\natural}$, hence $\tilde P$, is a plain unit; the composition law is the one cited, and it reverses the order, so the map is an anti-isomorphism onto its image, which is stable under composition and inversion.

This is the precise sense in which the product "has a group of units" only on the operator side. The set $\mathbb{B}^{\times}$ carries the inverse of the plain product, and it is the index set of the invertible operators; the product $\star$ does not make it a group.

## The Algebraic Norm on the Remarkable Subspaces

**The algebraic norm is definite on the quaternion and the anti-quaternion subspaces and indefinite on the centre and on the vector, Hermitian and anti-Hermitian subspaces; accordingly every nonzero element of the first two is a plain unit, while the other four subspaces carry the elements of norm zero.**

The algebraic norm is the quadratic form of the algebra, so its restriction to the remarkable subspaces is a form with a signature, and the sign decides which subspaces carry elements of algebraic norm zero. The signatures are computed in *Remarkable Subspaces under the General Quaternionic Algebra* and are quoted here.

| remarkable subspace | signature of $\langle\cdot\rangle_{\natural}$ | elements of algebraic norm zero |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $(1,1)$ | $0$ alone |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $(3,3)$ | the isotropic cone of the vector subspace |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $(4,0)$ | $0$ alone |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $(0,4)$ | $0$ alone |
| $\mathbb{M}_{+}$, the Hermitian subspace | $(1,3)$ | the isotropic cone of $\mathbb{M}_{+}$, all of it non-pure |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $(3,1)$ | the isotropic cone of $\mathbb{M}_{-}$, all of it non-pure |

**Corollary.** Every nonzero element of the quaternion subspace and of the anti-quaternion subspace is a unit of the plain product and satisfies both one-sided equations of $\star$. The other four subspaces contain nonzero elements of algebraic norm zero; on those the criterion fails and neither one-sided equation is soluble, and they are zero divisors of the algebra.

**Proof.** The algebraic norm is definite on the quaternion and the anti-quaternion subspaces and indefinite on the other four, by the table; the criterion of §*The Criterion* converts the values into the two statements. On a pure element the algebraic norm is $(\vec P,\vec P)$ and on a Hermitian element it is $|a_0|^2-|\vec b|^2$ in the coordinates of the subspace, so every zero of the algebraic norm in $\mathbb{M}_{+}$ or in $\mathbb{M}_{-}$ has non-zero scalar part, that is, is non-pure.

**Remark (a mixed real form of signature $(2,2)$).** Beyond the remarkable subspaces the geometry uses one mixed real subspace, the **split form**

$$
W=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,ie_2,ie_3\},\qquad N|_W=a^{2}+b^{2}-c^{2}-d^{2},
$$

of real dimension four, matrix $\operatorname{diag}(1,1,-1,-1)$, complexification $(\mathbb{B},N)$ and projective quadric the doubly ruled real surface $S^{1}\times S^{1}$ (*Biquaternion Lorentzian and Conformal Geometry*; *The Null Quadric and Its Projective Geometry*).

## Summary

The general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ has a central square, $\tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural}e_0$ with $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=Q_0^2+(\vec Q,\vec Q)$, and this scalar is the **algebraic norm** of the product, with polar form the scalar coefficient $\langle\tilde P,\tilde Q\rangle_{\natural}=P_0Q_0+(\vec P,\vec Q)$ of the symmetrised product and with the multiplicative law $\langle\tilde P\star\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$.

The product has the left unit $e_0$ and no right one, hence no two-sided unit, and the definition of the inverse, which requires one, applies to no element: **there is no invertible element and no group of units of the quaternionic product**. What survives is the pair of one-sided equations relative to $e_0$: both have the same unique solution, $(\tilde P^{-1})^{\natural}=\tilde P/\langle\tilde P\rangle_{\natural}$, exactly when $\langle\tilde P\rangle_{\natural}\neq0$, and neither has a solution when $\langle\tilde P\rangle_{\natural}=0$. The criterion is thus the algebraic norm, as for the plain product, and the elements of non-vanishing algebraic norm form the plain group of units $\mathbb{B}^{\times}$, stable under $\star$ and carrying the invertible left multiplications, without being a group of the product. For an element of unit norm the inverse is the quaternion conjugate, $\tilde P^{-1}=\tilde P^{\natural}$, which coincides with the dagger exactly on the unitary elements, the rotation rotors, and not on the boosts. On the quaternion and the anti-quaternion subspaces the norm is definite and every nonzero element is a unit of the plain product; on the centre, the vector, the Hermitian and the anti-Hermitian subspaces it is indefinite and they carry the zero divisors. Beyond the six remarkable subspaces the geometry uses one mixed real form, the split form $W=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,ie_2,ie_3\}$ of signature $(2,2)$.

Read as a norm of the algebra, $\langle\cdot\rangle_{\natural}$ is the **semi-norm** of the literature: of the usual axioms only the sign axiom survives, the triangle inequality having no content on a complex value and the scaling axiom failing for a complex scalar, since $\sqrt{\lambda^{2}}$ lies in the right half-plane and not at $\lvert\lambda\rvert$. The absolute square root $r(\tilde Q)=\sqrt{\lvert \langle\tilde Q\rangle_{\natural}\rvert}=\sqrt{\lvert\det\mathsf{M}_2(\tilde Q)\rvert}$ is the **unique** multiplicative real norm on the units normalised by $r(\lambda e_0)=\lvert\lambda\rvert$ for real $\lambda$, and it is the real scale of the polar representation. On the halves $\tilde Q=q_r+iq_i$ the norm splits as $\Re N=\langle q_r\rangle_{\natural}-\langle q_i\rangle_{\natural}$ and $\Im N=2\langle q_r,q_i\rangle$, so it vanishes exactly when the halves have equal norms and vanishing scalar product. The Hermitian form $\tilde Q\tilde Q^{*}$ is a different object: its scalar part $\sum_\mu\lvert Q_\mu\rvert^{2}$ is definite, defines the Euclidean norm and detects no zero divisor, and the two forms coincide exactly on the quaternion subspace.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k$ the quaternion units |
| $\tilde Q=Q_0e_0+\vec Q$ | an element and its scalar–vector split |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the algebraic norm of the product, the scalar of the square, $\tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural}e_0$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural}=P_0Q_0+(\vec P,\vec Q)$ | the polar form of the algebraic norm |
| the sign axiom, the triangle inequality, the scaling axiom | the audit of the norm axioms, of which only the first survives; $\langle\cdot\rangle_{\natural}$ is the semi-norm of the literature |
| $r(\tilde Q)=\sqrt{\lvert \langle\tilde Q\rangle_{\natural}\rvert}=\sqrt{\lvert\det\mathsf{M}_2(\tilde Q)\rvert}$ | the unique multiplicative real norm on the units, the polar scale |
| $\tilde Q=q_r+iq_i$ | the halves; $\Re N=\langle q_r\rangle_{\natural}-\langle q_i\rangle_{\natural}$, $\Im N=2\langle q_r,q_i\rangle$ |
| $\tilde Q\tilde Q^{*}$ | the Hermitian form; $\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $W=\operatorname{span}_{\mathbb{R}}\{e_0,e_1,ie_2,ie_3\}$ | the mixed real form of signature $(2,2)$ |
| $e_0$ | the left unit of $\star$; there is no right unit, hence no two-sided one |
| $\tilde P^{-1}=\tilde P^{\natural}/\langle\tilde P\rangle_{\natural}$ | the inverse of the plain product |
| $(\tilde P^{-1})^{\natural}$ | the common solution of the two one-sided equations of $\star$ |
| $\mathbb{B}^{\times}=\{N\neq0\}$ | the plain group of units, stable under $\star$ |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_{+},\mathbb{M}_{-}$ | the remarkable subspaces |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the algebraic norm and the one-sided inverses of a non-associative algebra.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for a quadratic form defined by a product and the polarisation of its multiplicative law.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm of the biquaternion algebra.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the semi-norm, its axioms and the Hermitian form.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the unique multiplicative real norm of the algebra.
- *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the definition of the algebraic norm as the form at the two equal arguments and the separation of the four algebraic norms.
- *Norm and Invertibility in the Biquaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.md`), for the algebraic norm $\langle\cdot\rangle$ of the plain product, which is not the form $\langle\cdot,\cdot\rangle_{\natural}$ of this article.
- *Remarkable Subspaces and the Four Algebraic Norms* (`articles_maths/remarkable-subspaces-and-the-four-algebraic-norms.md`), for the Euclidean norm as the square root of $\langle\cdot\rangle_{*}$ and the unique topological norm of the space, and *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the topology the Euclidean norm carries.
- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Unit and the Inverse*, for the definitions of the unit, the two-sided inverse and the one-sided inverse.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the set $\{N=0\}\setminus\{0\}$, its criterion and its annihilators.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the one-sided inverse equations of the four general products tabulated side by side.
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for the monoid law of the left multiplications and the group of its invertible elements.
- *Remarkable Subspaces under the General Quaternionic Algebra* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra.md`), for the signatures of the algebraic norm on the six subspaces.
