# __N-Regularity and N-Degeneracy in the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries one multiplicative norm, the quaternionic norm, the diagonal of the general quaternionic bilinear form. It alone decides invertibility. This article defines it, proves its multiplicative law, and separates the elements of $\mathbb{B}$ into the two cases of its value: the **$\natural$-regular** case of non-zero norm, whose elements are the units of the algebra and form a group, and the **$\natural$-degenerate** case of zero norm, the null cone. This article is the study of this one norm and of its two cases.

**Notation.** An element is $\tilde Q=Q_t e_t+\vec Q$, its natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$, and the product of the article is the plain product $\tilde P\tilde Q$ of the algebra, which is associative and has the two-sided unit $e_t$. The norm is $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$. A biquaternion is **$\natural$-regular** when $\langle\tilde Q\rangle_{\natural}\neq0$ and **$\natural$-degenerate** when $\langle\tilde Q\rangle_{\natural}=0$, the two terms fixed in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*. The product $\tilde P^{\natural}\tilde Q$ has a left unit and no right unit; it is recorded in one remark in §*The $\natural$-Regular Case*, because only the plain product has a group of units.

## The Quaternionic Norm

**Definition.** The **quaternionic norm**, also the **general quaternionic bilinear algebraic norm**, of $\tilde Q=Q_t e_t+\vec Q$ is the complex scalar

$$
\langle\tilde Q\rangle_{\natural}=\sum_{\mu}Q_{\mu}^{2}=Q_t^{2}+(\vec Q,\vec Q).
$$

**The identity of the norm.** Because $(Q_t-\vec Q)(Q_t+\vec Q)=Q_t^2-\vec Q^2$ and $\vec Q^2=-(\vec Q,\vec Q)$ for a vector part,

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t.
$$

The value is a complex scalar, not a length. Its vanishing set is the null cone in $\mathbb{B}$, not a sphere. The name records the algebra: $\mathbb{B}$ is the complexification of the quaternions, and $\langle\cdot\rangle_{\natural}$ is the quaternionic norm of that algebra.

**Theorem (multiplicativity).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}.
$$

*Proof.* The natural conjugation is an anti-automorphism, so $(\tilde P\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural}$. Then

$$
(\tilde P\tilde Q)(\tilde P\tilde Q)^{\natural}
=\tilde P\tilde Q\tilde Q^{\natural}\tilde P^{\natural}
=\tilde P\,\langle\tilde Q\rangle_{\natural}e_t\,\tilde P^{\natural}
=\langle\tilde Q\rangle_{\natural}\tilde P\tilde P^{\natural}
=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}e_t,
$$

and the left side is $\langle\tilde P\tilde Q\rangle_{\natural}e_t$ by the identity of the norm.

**Consequence.** The unit set $\{\langle\cdot\rangle_{\natural}\neq0\}$ and the null cone $\{\langle\cdot\rangle_{\natural}=0\}$ are both stable under the product.

## The Two Cases

The value of the norm separates the algebra into two parts.

| condition on $\langle\tilde Q\rangle_{\natural}$ | set | name |
|---|---|---|
| $\neq0$ | $\mathbb{B}^{\times}=\{\langle\cdot\rangle_{\natural}\neq0\}$ | the **$\natural$-regular case**: the group of units |
| $=0$ | the **null cone** $\mathcal{N}=\{\langle\cdot\rangle_{\natural}=0\}$ | the **$\natural$-degenerate case**: the origin together with the zero divisors |

The split is by the value of the norm, not by zero-divisorhood. The origin lies in the null cone, and it is not a zero divisor; every non-zero point of the cone is one. So the $\natural$-regular case is exactly the unit group, and the $\natural$-degenerate case is the cone, of which the zero-divisor set is the punctured part.

**Remark (the word regular).** In ring theory a regular element is a non-zero-divisor, and the origin qualifies, so the ring-regular elements are $\mathbb{B}^{\times}\cup\{0\}$. The title uses **$\natural$-regular** instead: the regular side is the unit group, and the origin is $\natural$-degenerate. The two readings differ at one point, the apex, and the article follows the norm.

**Criterion.** For $\tilde Q\neq0$ the following are equivalent:

1. $\tilde Q$ is $\natural$-regular, $\langle\tilde Q\rangle_{\natural}\neq0$;
2. $\tilde Q$ is a unit of the plain product;
3. $\tilde Q$ is not a zero divisor;
4. the left translation $\tilde X\mapsto\tilde Q\tilde X$ is injective;
5. the right translation $\tilde X\mapsto\tilde X\tilde Q$ is injective.

*Proof.* (1)$\Rightarrow$(2): the inverse is $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$, by the identity of the norm. (2)$\Rightarrow$(3): a unit cannot annihilate a non-zero element. (3)$\Rightarrow$(4): if the left translation is not injective, some $\tilde X\neq0$ has $\tilde Q\tilde X=0$, and $\tilde Q$ is a left zero divisor. (4)$\Rightarrow$(1): if $\langle\tilde Q\rangle_{\natural}=0$ then $\tilde Q\tilde Q^{\natural}=0$ with $\tilde Q^{\natural}\neq0$, so the left translation kills $\tilde Q^{\natural}$. The right-hand conditions are treated the same way.

Equivalently, for $\tilde Q\neq0$, the element is $\natural$-degenerate exactly when it is a zero divisor; the origin is $\natural$-degenerate and is neither. The norm therefore decides invertibility in the precise sense that its non-vanishing set is the unit group; and its vanishing set, minus the origin, is the zero-divisor set.

## The $\natural$-regular case: The Group of Units

**Definition.** The **$\natural$-regular set** is the set of $\natural$-regular biquaternions,

$$
\mathbb{B}^{\times}=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}\neq0\},
$$

and it is the **unit group** of the plain product.

By the criterion above it is the complement of the null cone: the algebra minus the origin and the zero divisors.

**Theorem.** $\mathbb{B}^{\times}$ is a group under the plain product.

*Proof.* Closure: $\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}\neq0$. Associativity: the plain product is associative. Identity: $e_t$, with $\langle e_t\rangle_{\natural}=1$. Inverse: for $\tilde Q\in\mathbb{B}^{\times}$,

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}},
$$

since $\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$.

**Remark (the inverse is the conjugate over the norm).** In the plain product the two-sided inverse is $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$. In the product $\tilde P^{\natural}\tilde Q$ the one-sided solution is $\tilde Q/\langle\tilde Q\rangle_{\natural}$. The criterion $\langle\cdot\rangle_{\natural}\neq0$ is the same; the inverse is not. The unit group is a plain-product object.

**Theorem (the partition).** The algebra is the disjoint union of the $\natural$-regular and the $\natural$-degenerate biquaternions,

$$
\mathbb{B}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\}\uplus\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\}=\mathbb{B}^{\times}\uplus\mathcal{N},
$$

and the second set, the null cone $\mathcal{N}$, is the origin together with the zero divisors, $\mathcal{N}=\{0\}\uplus\mathcal Z$. The first is the unit group.

*Proof.* The two sets are complementary by the law of excluded middle on a complex number, and the cone splits into the origin and its punctured part, which is the zero-divisor set by §*The Zero Divisors*.

**Corollary (topology).** $\mathbb{B}^{\times}$ is open and dense in $\mathbb{B}$; $\mathcal{N}$ is closed, has empty interior, and is of real codimension $2$; and

$$
\partial\mathbb{B}^{\times}=\mathcal{N}.
$$

The origin is the only point of the cone that is not a zero divisor.

*Proof.* The cone is the zero set of a polynomial, hence closed, and it is a proper algebraic subset, hence of empty interior; its complement is open and dense. The boundary of the group is the intersection of the closures of the group and of its complement, that is the cone.

**Remark (the $\natural$-bilinear product).** For the product $\tilde P^{\natural}\tilde Q$ the element $e_t$ is a left unit and there is no right unit, so no element has a two-sided inverse and there is no group of units. The two one-sided equations with $e_t$ have the common unique solution $\tilde Q/\langle\tilde Q\rangle_{\natural}$ exactly when $\langle\tilde Q\rangle_{\natural}\neq0$. The criterion is unchanged; what is lost is the group, and with it the two-sided inverse $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$. That is why this article uses the plain product.

## The $\natural$-degenerate case: the origin together with the zero divisors

**Definition.** Let $\cdot$ be a product on $\mathbb{B}$. A non-zero $\tilde Q$ is a **left zero divisor** of $\cdot$ if $\tilde Q\cdot\tilde X=0$ for some $\tilde X\neq0$, a **right zero divisor** if $\tilde X\cdot\tilde Q=0$ for some $\tilde X\neq0$, and a **zero divisor** if it is one or the other. The element $0$ is not a zero divisor of any product.

Throughout this section the product is the plain product $\tilde Q_1\tilde Q_2$ of the algebra, which is associative and has the two-sided unit $e_t$; it is the product in which the zero-divisor set is visible as a stratification.

**Theorem (the criterion).** A non-zero $\tilde Q$ is a zero divisor of the plain product exactly when $\langle\tilde Q\rangle_{\natural}=0$.

*Proof.* If $\langle\tilde Q\rangle_{\natural}=0$ and $\tilde Q\neq0$, then $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t=0$ with $\tilde Q^{\natural}\neq0$, so $\tilde Q$ is a left zero divisor. Conversely, if $\tilde Q\tilde X=0$ with $\tilde X\neq0$ and $\langle\tilde Q\rangle_{\natural}\neq0$, then $\tilde Q$ is a unit of the plain product, of inverse $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$, and $\tilde X=\tilde Q^{-1}\tilde Q\tilde X=0$, a contradiction.

**Remark (one set for the four products).** The same set is selected by the $\natural$-bilinear product: there the relevant square is $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$, so a vanishing norm gives $\tilde Q^{\natural}\tilde Q=0$. The four general products have four different zero-divisor equations and, in this algebra, one and the same zero-divisor set.

**Definition (the two strata).** The **pure stratum** and the **non-pure stratum** of the null cone are

$$
\mathcal{N}_{\mathrm p}=\{\langle\cdot\rangle_{\natural}=0,\ Q_t=0,\ \tilde Q\neq0\},\qquad
\mathcal{N}_{\mathrm{np}}=\{\langle\cdot\rangle_{\natural}=0,\ Q_t\neq0\}.
$$

**Observation.** On $\mathcal{N}$, $Q_t^2+\vec Q^2=0$, so

$$
Q_t=0\iff\vec Q^2=0\iff\tilde Q^2=0.
$$

The pure stratum is therefore the set of non-zero elements with vanishing square; on the non-pure stratum, where $Q_t\neq0$, the square is instead $\tilde Q^2=2Q_t\tilde Q$. No object outside the norm enters the characterisation.

**Theorem (the pure stratum).** Every element of $\mathcal{N}_{\mathrm p}$ is a nilpotent of index two: $\tilde Q=\vec Q$ and $\tilde Q^2=-\vec Q^2e_t=0$. The stratum is a complex cone of complex dimension $2$ and real dimension $4$ in the three vector coefficients, cut out by the single quadratic equation

$$
Q_x^2+Q_y^2+Q_z^2=0.
$$

*Proof.* On $\mathcal{N}_{\mathrm p}$ the scalar part vanishes and $Q_t^2+\vec Q^2=0$ gives $\vec Q^2=0$, so $\tilde Q=\vec Q$ and $\tilde Q^2=-\vec Q^2e_t=0$. The equation is one complex equation in the three complex vector coefficients, homogeneous of degree two, with gradient $2(Q_x,Q_y,Q_z)$ non-vanishing off the origin; its real dimension is $2\cdot3-2=4$ and its complex dimension is $3-1=2$.

**Real-coordinate form.** Write $\vec Q=\vec\rho+i\vec\rho'$ with $\vec\rho,\vec\rho'\in\mathbb{R}^3$. Then

$$
\vec Q^2=(|\vec\rho'|^2-|\vec\rho|^2)e_t-2i(\vec\rho\cdot\vec\rho')e_t,
$$

so the pure stratum is the set of bivectors with

$$
\vec\rho\cdot\vec\rho'=0,\qquad |\vec\rho|=|\vec\rho'|.
$$

Equivalently it is the set of elements $r(\vec u+i\vec u_\perp)$ with $r>0$, $\vec u$ a real unit vector and $\vec u_\perp$ a real unit vector perpendicular to $\vec u$: one radius, one direction and one perpendicular direction, that is $1+2+1=4$ real dimensions.

**Theorem (the non-pure stratum).** Every element of $\mathcal{N}_{\mathrm{np}}$ satisfies $\tilde Q^2=2Q_t\tilde Q$, and is therefore a non-zero complex multiple of a non-trivial idempotent:

$$
\tilde Q=2Q_t\tilde\Pi,\qquad \tilde\Pi=\frac{\tilde Q}{2Q_t},\qquad \tilde\Pi^2=\tilde\Pi.
$$

The stratum is open in $\mathcal{N}$, of real dimension $6$, and its complement in $\mathcal{N}$ is the pure stratum.

*Proof.* $\tilde Q^2=(Q_t^2-\vec Q^2)e_t+2Q_t\vec Q$; on $\mathcal{N}$ we have $\vec Q^2=-Q_t^2$, so $\tilde Q^2=2Q_t^2e_t+2Q_t\vec Q=2Q_t\tilde Q$. Dividing by $2Q_t\neq0$ gives $\tilde\Pi^2=\tilde\Pi$, and $\tilde\Pi\neq0,e_t$ because $\tilde Q\neq0$ and $\tilde Q$ is not a scalar multiple of $e_t$. The stratum is the complement in $\mathcal{N}$ of the closed subset $\{Q_t=0\}$, hence open in $\mathcal{N}$, and it has the dimension of $\mathcal{N}$.

**Peirce factorisation.** Let $\tilde\Pi=\tilde Q/(2Q_t)$ be the idempotent of a non-pure zero divisor. The mixed Peirce corners contain elements

$$
u\in\tilde\Pi\mathbb{B}(e_t-\tilde\Pi),\qquad w\in(e_t-\tilde\Pi)\mathbb{B}\tilde\Pi,
$$

normalised so that $uw=\tilde\Pi$, and both are square-zero: $u^2=w^2=0$. Hence every non-pure zero divisor is a scalar multiple of a product of two nilpotents,

$$
\tilde Q=2Q_t\,uw,\qquad u^2=w^2=0.
$$

The idempotents, their classification and their Peirce systems are *The Peirce Decomposition of the Biquaternion Algebra*; the factorisation is recorded here because it places the non-pure zero divisors in the same Peirce framework as the pure ones.

**Theorem (the zero-divisor set).** The set

$$
\mathcal Z=\{\tilde Q\neq0:\langle\tilde Q\rangle_{\natural}=0\}=\mathcal{N}\setminus\{0\}
$$

is a complex cone of complex dimension $3$ and real dimension $6$ in $\mathbb{B}\cong\mathbb{C}^4$. It is the complement of the units in the complement of the origin,

$$
\mathcal Z=\mathbb{B}\setminus\bigl(\{0\}\cup\mathbb{B}^{\times}\bigr),
$$

and it is stable under multiplication by non-zero complex scalars.

*Proof.* $\langle\cdot\rangle_{\natural}=0$ is one complex equation in the four complex coefficients, homogeneous of degree two, with non-vanishing gradient off the origin. The real dimension is $2\cdot4-2=6$ and the complex dimension is $4-1=3$; removing the origin changes neither.

**Correspondence (the remarkable subspaces).** By the signatures tabulated in §*The Two Cases on the Remarkable Subspaces*, the norm is anisotropic on the centre, the quaternion subspace and the anti-quaternion subspace: it vanishes only at the origin there, so none of the three contains a zero divisor; the zero-divisor set in the vector subspace is the pure stratum; and the Hermitian and anti-Hermitian subspaces each carry a null cone. A generic zero divisor has all four coefficients non-zero and lies in none of them.

**Remark (the spectral reading).** Inside $\mathcal{N}$ the pure stratum is cut out by $\vec Q^2=0$, which is the quadratic equation that also marks the spectral-degenerate elements. The strata here are defined by $Q_t$ alone; the comparison of the two cones belongs to *The Spectrum*.

The matrix reading of the split is in *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*, §*The Factorisation*: a non-zero null element is a rank-one matrix $uv^{\mathsf T}$, its scalar part is the contraction $\tfrac12 v^{\mathsf T}u$, the pure stratum is the locus $v^{\mathsf T}u=0$, and the square identity $\tilde Q^2=2Q_t\tilde Q$ is the rank-one identity.

## The Two Cases on the Remarkable Subspaces

The restriction of the norm to a remarkable subspace has a realified signature, and the complex equation $\langle\cdot\rangle_{\natural}=0$ decides whether the subspace carries non-zero elements of norm zero. The values are computed in *Remarkable Subspaces under the General Quaternionic Algebra*.

| remarkable subspace | realified signature of $\langle\cdot\rangle_{\natural}$ | elements of norm zero |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $(1,1)$ | $0$ alone |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $(3,3)$ | the isotropic cone of the vector subspace |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $(4,0)$ | $0$ alone |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $(0,4)$ | $0$ alone |
| $\mathbb{M}_{+}$, the Hermitian subspace | $(1,3)$ | the isotropic cone of $\mathbb{M}_{+}$, all of it non-pure |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $(3,1)$ | the isotropic cone of $\mathbb{M}_{-}$, all of it non-pure |

**Corollary.** Every non-zero element of the centre, the quaternion subspace and the anti-quaternion subspace is a unit. The vector, Hermitian and anti-Hermitian subspaces contain zero divisors, and the origin is the only element of norm zero in those subspaces that is not one.

*Proof.* The signatures give the values, and the criterion above converts the values into the two statements. On the centre the norm is $Q_t^2$, which vanishes only at the origin. On a pure element the norm is $(\vec Q,\vec Q)$ and on a Hermitian element it is $|a_0|^2-|\vec b|^2$, so a zero in $\mathbb{M}_{+}$ or $\mathbb{M}_{-}$ has non-zero scalar part and is non-pure.

**Remark.** The geometry also uses one mixed real subspace, the split form $W=\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,i\vec e_y,i\vec e_z\}$ of real dimension four, on which $\langle\cdot\rangle_{\natural}|_W=a^2+b^2-c^2-d^2$, of signature $(2,2)$.

## Summary

The biquaternion algebra carries one multiplicative norm, the quaternionic norm, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$, and only it decides invertibility.

The plain product is associative and has the two-sided unit $e_t$. The $\natural$-regular biquaternions are the units: they form the group $\mathbb{B}^{\times}$, with inverse $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$, and the algebra is the disjoint union $\mathbb{B}=\mathbb{B}^{\times}\uplus\mathcal{N}$ of the $\natural$-regular and the $\natural$-degenerate biquaternions. The group is open and dense, the cone is closed of real codimension $2$ and is its boundary. The $\natural$-bilinear product, which has a left unit and no right unit, is recorded in one remark: there the one-sided solution is $\tilde Q/\langle\tilde Q\rangle_{\natural}$, and the criterion is the same.

The $\natural$-degenerate case is the null cone, with the origin at its apex and the zero divisors at its punctured points. The zero-divisor set splits into the pure stratum, the nilpotents of index two, of real dimension $4$, and the non-pure stratum, the non-zero complex multiples of idempotents, of real dimension $6$, the split being by the scalar part $Q_t$. In the matrix model a non-zero null element is the rank-one matrix $uv^{\mathsf T}$; its scalar part is the contraction $\tfrac12 v^{\mathsf T}u$, the pure stratum is the locus $v^{\mathsf T}u=0$, and the identity $\tilde Q^2=2Q_t\tilde Q$ is the rank-one identity $\mathsf M_2(\tilde Q)^2=(v^{\mathsf T}u)\mathsf M_2(\tilde Q)$. The cone is not a subspace and is stable under the product. The norm vanishes only at the origin on the centre, the quaternion and the anti-quaternion subspaces, and the other three carry a null cone.


## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity |
| $\tilde Q=Q_t e_t+\vec Q$ | an element and its scalar–vector split |
| $\tilde Q^{\natural}=Q_t-\vec Q$ | the natural conjugation |
| $\tilde P\tilde Q$ | the plain product, associative, with the two-sided unit $e_t$ |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the quaternionic norm, written $\langle\tilde Q\rangle_{\natural}$, the only multiplicative one |
| $\natural$-regular | $\langle\tilde Q\rangle_{\natural}\neq0$; the unit group |
| $\natural$-degenerate | $\langle\tilde Q\rangle_{\natural}=0$; the null cone |
| $\mathbb{B}^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\}$ | the unit group, the $\natural$-regular set, with inverse $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ |
| $\mathcal{N}=\{\tilde Q:\langle\cdot\rangle_{\natural}=0\}$ | the null cone, the $\natural$-degenerate set |
| $\mathcal Z=\mathcal{N}\setminus\{0\}$ | the zero-divisor set |
| $\mathcal{N}_{\mathrm p}=\{Q_t=0,\ \tilde Q\neq0\}$ | the pure stratum, the nilpotents of index two |
| $\mathcal{N}_{\mathrm{np}}=\{Q_t\neq0\}$ | the non-pure stratum, complex multiples of non-trivial idempotents |
| $\mathsf M_2(\tilde Q)=uv^{\mathsf T}$ | the rank-one factorisation of a non-zero null element |
| $\tilde P^{\natural}\tilde Q$ | the $\natural$-bilinear product, with a left unit and no right unit |
| $S(\tilde Q)=\tilde Q/\langle\tilde Q\rangle_{\natural}$ | the one-sided solution of that product |

## Further Reading

- [The Spectrum](the-spectrum.html), for the quadratic condition $B^2$, the spectral-degenerate cone and the behaviour on it.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the comparison of the norm with the spectral condition, the four sectors and the information each invariant carries.
- [The N-Regular Sector](the-n-regular-sector.html), for the unit group as a sector, its matrix model, its topology and its two spectral cells.
- [The N-Degenerate Sector](the-n-degenerate-sector.html), for the null cone, its three strata, its link and its degenerate polar decomposition.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the norm and the one-sided inverses of a non-associative algebra.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for a quadratic form defined by a product and its multiplicative law.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the complex-valued norm of the biquaternion algebra.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the norm and its axioms.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the definition of an algebraic norm and the separation of the four.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the Peirce factorisation of the strata.
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the isomorphism $\mathsf M_2$, the determinant, the trace, the rank-one elements and the contraction of their factors.
- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the topology of $\mathbb{B}^{\times}$, its maximal compact subgroup and its homotopy.
- [Zero Divisors of the General Quaternionic Algebra](zero-divisors-of-the-general-quaternionic-algebra.html), for the zero-divisor set and its criterion for the general quaternionic product.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the comparison of the zero-divisor sets of the twelve products.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the definitions of the unit and of the one-sided inverse.
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), for the signatures of the norm on the six subspaces.
