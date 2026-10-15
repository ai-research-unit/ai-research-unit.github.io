# __Norm and Invertibility in the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ on the biquaternion space, the Hermitian form $H$ read as a multiplication (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article studies the algebraic norm that the block carries and the invertibility that it does not.

A norm and an inverse name a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. For the block the form is $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)$ and its diagonal is

$$
H(\tilde Q)=H(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2},
$$

the symmetric plain sesquilinear algebraic norm, **real and positive definite**, one of the four algebraic norms of the space and not one of the other three. The two arities of the letter are one object: with two arguments the form, with one argument its diagonal.

The invertibility is where the article records an **absence**. The block is **not unital**: every value of the product is central, so it has no two-sided unit, and consequently no inverse, no group of units and no division structure. Its algebraic norm does **not** repair the absence: $H$ is positive definite, so $H(\tilde Q)=0$ exactly at $\tilde Q=0$, the block has no nonzero isotropic vector and no invertible element, and its element classification is two-way, the origin and everything else. The article states the absence, then the algebraic norm, then the failure of multiplicativity and the polarisation.

**Boundaries.** The product, its class and its table are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the relative definitions of the unit, the inverse and the group of units are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*, and the four general products with their units are *Comparison Between the Four General Products*. The definition of the algebraic norm as the form at the two equal arguments and the three other algebraic norms are *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*; the algebraic norm of the plain product is $B$, a different form, and its theory is *Norm and Invertibility in the General Plain Algebra*. The form $H$, its Gram matrix, its positivity and its cone are *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the zero divisors are *Zero Divisors of the Symmetric Plain Sesqualgebra*; the operators of the block are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu \varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu \overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ with $H(\tilde P,\tilde Q) = \sum_{\mu=0}^{3}P_\mu\overline{Q_\mu}$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$; the **algebraic norm of the block** is its diagonal $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$.

**The results.** Every value of the product $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ is central, so the block has no unit, no inverse and no group of units, and no element is invertible. The block carries one algebraic norm, $H(\tilde{Q}) = \sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}$, real, non-negative and positive definite of signature $(8,0)$ on the real space underlying $\mathbb{B}$, vanishing only at $\tilde{Q} = 0$, with image of its square map the real ray $\mathbb{R}_{\geq0}e_0$. The algebraic norm is not multiplicative: $H(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2}$, with defect the discriminant $H(\tilde P)H(\tilde Q) - \lvert H(\tilde P,\tilde Q)\rvert^{2}\geq0$ vanishing exactly on linearly dependent pairs, and it polarises to the Hermitian form. The definiteness is why it cannot decide invertibility: $H(\tilde{Q}) = 0$ exactly at the origin, so the block has no nonzero isotropic vector and its element classification is two-way.

## The Relative Notions

The word *unit*, the word *inverse* and the word *group of units* name a product, so the definitions are stated once for a general product and then read on the products of this space; they are in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Definition (recalled).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde{Q} = \tilde{Q}$ for every $\tilde{Q}\in\mathbb{B}$, a **right unit** when $\tilde{Q}\star e = \tilde{Q}$ for every $\tilde{Q}\in\mathbb{B}$, and a **two-sided unit**, or an **identity**, when it is both. When a two-sided unit $e$ exists, an element $\tilde{Q}$ is **invertible of $\star$** when there is a $\tilde{R}$ with $\tilde{Q}\star\tilde{R} = \tilde{R}\star\tilde{Q} = e$, the element $\tilde{R}$ being the **inverse of $\tilde{Q}$ of $\star$**; the **group of units of $\star$** is the set of the invertible elements, a group under $\star$. When no two-sided unit exists, the three notions are empty and the group of units is not defined.

Throughout this article the product is the symmetric plain sesqualgebra $\star$, and another product is named where it is meant.

## The Absence of a Unit

**The block has no unit of any kind: there is no left, no right and no two-sided unit $e$, because every value of the product is central and the block has non-central elements.**

**Theorem (the block has no unit).** The block has no left unit and no right unit: there is no element $e$ with $e\star\tilde{Q} = \tilde{Q}$ for every $\tilde{Q}\in\mathbb{B}$, and none with $\tilde{Q}\star e = \tilde{Q}$ for every $\tilde{Q}\in\mathbb{B}$. Hence there is no two-sided unit either.

*Proof.* Every value of the product is central, $e\star\tilde{Q} = H(e,\tilde{Q})e_0 \in \mathbb{C}e_0$. The element $e_1$ is not central, so $e\star e_1 \neq e_1$ for every $e$, and $e_1\star e \neq e_1$ for every $e$; there is therefore no left unit, no right unit and no two-sided unit. In particular the idempotent $e_0$ is not a unit: $e_0\star e_1 = H(e_0,e_1)e_0 = 0$, since the basis is orthonormal for $H$.

**Remark (the reason is the image).** The failure is structural: a product whose image is the central line cannot reproduce an element with a vector part, and the block has non-central elements. The same reason deprives the symmetric quaternionic product of a unit, while the symmetric plain product, whose image is the whole space, has the unit $e_0$.

## The Absence of an Inverse and of the Group of Units

**No element of the block is invertible of $\star$, and the group of units of $\star$ is not defined, both notions being empty for want of a two-sided unit.**

**Theorem (no element is invertible, and there is no group of units).** No element of $\mathbb{B}$ is invertible of $\star$, and the group of units of $\star$ is not defined.

*Proof.* The notions of §*The Relative Notions* presuppose a two-sided unit, and §*The Absence of a Unit* shows that the block has none; the definition is therefore empty. There is no invertible element and no inverse formula.

**Remark (what the block does not have).** The block has no unit, no inverse, no group of units, no division structure and no three-way classification of the elements into the zero, the invertible and the zero divisors; its element classification is two-way and is read in §*The Absence of a Criterion from the Algebraic Norm*. The block neither inherits the invertible elements of another product nor carries a substitute group of its own elements.

## The Algebraic Norm of the Block

**The block carries one algebraic norm, $H(\tilde{Q}) = \mathrm{Sc}(\tilde Q\star\tilde Q) = \sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}$, real, non-negative and positive definite; its Gram matrix is the identity on the basis $e_0,e_1,e_2,e_3$ and its square map has image the real ray $\mathbb{R}_{\geq0}e_0$.**

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
H(\tilde{Q}) = \mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr) = H(\tilde{Q},\tilde{Q}) = \sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2} \in \mathbb{R}_{\geq 0},
$$

a real non-negative number, and it is the coefficient of the square of the element,

$$
\tilde{Q}\star\tilde{Q} = H(\tilde{Q})e_0 .
$$

The equation names the product $\star$: the algebraic norm is relative to the product, and the algebraic norms of the other three rows are different quadratic maps on the same space (*The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*).

**Basic properties.** Each is a direct reading of the definition.

- $H(\tilde{Q})$ is a **real** number, $\overline{H(\tilde{Q})} = H(\tilde{Q})$, because each $\lvert Q_\mu\rvert^{2}$ is real.
- $H(\tilde{Q})$ is **non-negative**, and $H(\tilde{Q}) = 0$ exactly at $\tilde{Q} = 0$; the quadratic form is **positive definite**, of signature $(8,0)$ on the real space underlying $\mathbb{B}$.
- $H$ is **invariant under the three conjugations**, $H(\tilde{Q}^{\natural}) = H(\overline{\tilde{Q}}) = H(\tilde{Q}^{*}) = H(\tilde{Q})$, because each conjugation preserves the moduli $\lvert Q_\mu\rvert$ of the coordinates.
- $H$ is **homogeneous of degree two** over the reals but not over $\mathbb{C}$: $H(\lambda\tilde{Q}) = \lvert\lambda\rvert^{2}H(\tilde{Q})$ for $\lambda\in\mathbb{C}$.
- $H$ is the **polarisation source** of the form $H(\tilde P,\tilde Q)$, recovered from the diagonal in §*The Polarisation of the Algebraic Norm*.

**Proposition (the Gram matrix and the square map).** On the basis $e_0,e_1,e_2,e_3$ the form has Gram matrix the identity, $H(e_\mu,e_\nu) = \delta_{\mu\nu}$, so $H(e_\mu) = 1$; the square map $\tilde{Q}\mapsto\tilde{Q}\star\tilde{Q}$ has image the real ray $\mathbb{R}_{\geq 0}e_0$ and is surjective onto it.

*Proof.* The Gram statement is $H(e_\mu,e_\nu) = \sum_\sigma (e_\mu)_\sigma\overline{(e_\nu)_\sigma} = \delta_{\mu\nu}$, and the square display gives the image. The ray is attained since $\tilde{Q} = \sqrt{\lambda}e_0$ gives $H(\tilde{Q}) = \lambda$ for $\lambda\geq 0$.

## The Failure of Multiplicativity

**The algebraic norm of the block is not multiplicative: $H(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2}$, the defect $H(\tilde P)H(\tilde Q) - \lvert H(\tilde P,\tilde Q)\rvert^{2}\geq0$ vanishes exactly on linearly dependent pairs, and multiplicativity holds on the centre alone.**

**Theorem (the algebraic norm of a product).** For all $\tilde P,\tilde Q$,

$$
H(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2},
$$

the square of the modulus of the form on the two arguments; consequently $H(\tilde P\star\tilde Q) = H(\tilde P)H(\tilde Q)$ exactly when the two arguments are linearly dependent over $\mathbb{C}$.

*Proof.* The product is central, $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$, and $H(\lambda e_0) = \lvert\lambda\rvert^{2}$. So the algebraic norm of the product is $\lvert H(\tilde P,\tilde Q)\rvert^{2}$. For the equality case, the quadratic form $t\mapsto H(\tilde P - t\tilde Q)\geq 0$ in the complex variable $t$ has discriminant $H(\tilde P)H(\tilde Q) - \lvert H(\tilde P,\tilde Q)\rvert^{2}$, so this quantity is non-negative, and the vanishing of the discriminant is the vanishing of the form at its minimising argument, that is the proportionality of $\tilde P$ and $\tilde Q$.

**Corollary (the defect is the discriminant).** For all $\tilde P,\tilde Q$,

$$
H(\tilde P)H(\tilde Q) - H(\tilde P\star\tilde Q) = H(\tilde P)H(\tilde Q) - \lvert H(\tilde P,\tilde Q)\rvert^{2} \geq 0,
$$

with equality exactly when $\tilde P$ and $\tilde Q$ are linearly dependent. The algebraic norm is therefore **submultiplicative** and multiplicative exactly on linearly dependent pairs.

**Remark (the identity that replaces multiplicativity).** The block has one exact multiplicativity, read on the form rather than on the algebraic norm: for all $\tilde P,\tilde Q,\tilde R$,

$$
H(\tilde P\star\tilde Q,\tilde R) = H(\tilde P,\tilde Q)\,H(e_0,\tilde R),
$$

and dually $H(\tilde R,\tilde P\star\tilde Q) = H(\tilde R,e_0)\overline{H(\tilde P,\tilde Q)}$. The first factor $H(\tilde P,\tilde Q)$ is the coefficient of the product, the second is the evaluation of the form on the idempotent $e_0$; the product is central, so the form evaluates it only through that one coefficient.

**Remark (the algebraic norm is multiplicative on the centre).** On the central line the block is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ and the algebraic norm is the squared modulus, $H(\lambda e_0) = \lvert\lambda\rvert^{2}$; on central elements it is multiplicative, $H\bigl((\lambda e_0)\star(\mu e_0)\bigr) = H(\lambda e_0)H(\mu e_0)$, because $\mathbb{C}e_0$ is a field. Multiplicativity holds on the centre and fails off it, and the failure is measured by the corollary.

## The Polarisation of the Algebraic Norm

**The polar form of $H$ is twice the real part of the sesquilinear form, $H(\tilde P + \tilde Q) - H(\tilde P) - H(\tilde Q) = 2\Re H(\tilde P,\tilde Q)$, and the full Hermitian form is recovered from the algebraic norm by the four-term polarisation $H(\tilde P,\tilde Q) = \tfrac{1}{4}\sum_{k=0}^{3}i^{k}H(\tilde P + i^{k}\tilde Q)$.**

**Theorem (the polarisation).** The polar form of the quadratic map $H$ is twice the real part of the sesquilinear form,

$$
H(\tilde P + \tilde Q) - H(\tilde P) - H(\tilde Q) = 2\Re H(\tilde P,\tilde Q),
$$

and the full Hermitian form is recovered from the algebraic norm by

$$
H(\tilde P,\tilde Q) = \tfrac{1}{4}\sum_{k=0}^{3}i^{k}\,H(\tilde P + i^{k}\tilde Q).
$$

*Proof.* The first display expands $H(\tilde P+\tilde Q) = H(\tilde P)+H(\tilde Q)+H(\tilde P,\tilde Q)+\overline{H(\tilde P,\tilde Q)}$. For the second, insert the four values $k = 0,1,2,3$ and use $H(\tilde P + i^k\tilde Q) = H(\tilde P)+H(\tilde Q)+2\Re\bigl(i^{-k}H(\tilde P,\tilde Q)\bigr)$; the four coefficients $1,i,-1,-i$ average to the real and imaginary parts of $H$, giving $H$.

**Remark (the polarisation is the Hermitian one).** The second display is the polarisation of a sesquilinear form and not of a bilinear one: the four coefficients are the fourth roots of unity, not the pair $\pm1$ of the symmetric polarisation, which is the form of the Hermitian symmetry $H(\tilde Q,\tilde P) = \overline{H(\tilde P,\tilde Q)}$. The first display extracts only the real part, because the diagonal $H$ of a Hermitian form is real; the imaginary part is carried by the four-term display.

## The Absence of a Criterion from the Algebraic Norm

**The block has no invertible element, so no criterion can name one, and its algebraic norm decides nothing: $H(\tilde{Q}) = 0$ holds exactly at $\tilde{Q} = 0$, so the block has no nonzero element of zero algebraic norm and no nonzero isotropic vector.**

**Theorem (the algebraic norm does not decide invertibility).** The block has no invertible element, so no criterion can name one; and its algebraic norm has no nonzero zero:

$$
H(\tilde{Q}) = 0 \quad\Longleftrightarrow\quad \tilde{Q} = 0 .
$$

*Proof.* The first clause is the theorem on the absence of the inverse. The equivalence is the positive definiteness: $H(\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ is a sum of non-negative reals, vanishing exactly when every $Q_\mu$ vanishes.

**Remark (what replaces the criterion).** A criterion would equate the invertible elements with the complement of a hypersurface of the algebraic norm. For the block the algebraic norm is definite, it vanishes only at the origin, and it therefore separates nothing: the block has **no nonzero element of zero algebraic norm**, or, in the vocabulary of forms, **no nonzero isotropic vector**. Its element classification is two-way, the zero element and the non-zero elements, and the non-zero elements are all of one kind, the zero divisors of *Zero Divisors of the Symmetric Plain Sesqualgebra*. The definiteness is the exact opposite of the general plain product, whose algebraic norm $B$ is indefinite and does not decide invertibility either (*Norm and Invertibility in the General Plain Algebra*).

**Corollary (the substitute for the group of units).** The block has no group of units; the set that replaces it is the group of the linear maps of $\mathbb{B}$ that preserve the form $H$, together with its algebra, and it is read in *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. The block carries no subgroup of its own elements to play that role, since it has no invertible element.

## The Comparison with the General Plain Algebra

**The parent is unital and the block is not; the two products carry different algebraic norms $B$ and $H$; neither algebraic norm decides invertibility, the block having no invertible element at all; and the block's zero divisors are every nonzero element while the parent's are a proper subset.**

| clause | general plain algebra | symmetric plain sesqualgebra |
|---|---|---|
| algebraic norm | $B(\tilde{Q}) = \mathrm{Sc}(\tilde Q\tilde Q) = Q_0^2-(\vec Q,\vec Q)$, complex, indefinite | $H(\tilde{Q}) = \mathrm{Sc}(\tilde Q\star\tilde Q) = \sum_\mu\lvert Q_\mu\rvert^{2}$, real, definite |
| multiplicativity of the algebraic norm | $B$ not multiplicative | $H$ submultiplicative, $H(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2}$ |
| isotropic vectors | the complex cone of $B$ | none but the origin |
| unit | $e_0$, two-sided | none |
| invertible elements | defined; not read from $B$ | none |
| zero divisors | a proper subset | every non-zero element |

The parent is unital and the block is not; the two products carry **different** algebraic norms, $B$ and $H$, and neither algebraic norm decides invertibility: the parent has invertible elements that its algebraic norm $B$ does not see, and the block has no invertible element at all. The last three rows are the absence and the shape of a rank-one product.

## Summary

The symmetric plain sesqualgebra $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ has **no unit**, because every value of the product is central and $\mathbb{B}$ has non-central elements; consequently it has **no inverse**, **no group of units** and no division structure, and the relative definitions are empty. It carries one algebraic norm, the diagonal of its scalar-part form,

$$
H(\tilde{Q}) = \mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr) = \sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2},
$$

a real non-negative definite quadratic map of signature $(8,0)$, invariant under the three conjugations. The algebraic norm is **not multiplicative**: $H(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2}$, the defect is the discriminant $H(\tilde P)H(\tilde Q) - \lvert H(\tilde P,\tilde Q)\rvert^{2}\geq 0$, vanishing exactly on linearly dependent pairs, and multiplicativity holds on the centre alone. What replaces it is the exact identity $H(\tilde P\star\tilde Q,\tilde R) = H(\tilde P,\tilde Q)H(e_0,\tilde R)$, and the algebraic norm polarises to the Hermitian form, $\Re H$ at the symmetric step and $H$ at the four-term display. The **absence of a criterion** is the definiteness, $H(\tilde{Q}) = 0\Leftrightarrow\tilde{Q} = 0$: the block has no nonzero isotropic vector and no invertible element, and its element classification is two-way.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form defining the block, the scalar-part form of the product |
| $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, one of the four algebraic norms of the space |
| $\tilde{Q}\star\tilde{Q} = H(\tilde{Q})e_0$ | the square map, image $\mathbb{R}_{\geq0}e_0$ |
| $H(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2}$ | the algebraic norm of a product |
| $H(\tilde P\star\tilde Q,\tilde R) = H(\tilde P,\tilde Q)H(e_0,\tilde R)$ | the identity that replaces multiplicativity |
| $H(\tilde P,\tilde Q) = \tfrac14\sum_k i^{k}H(\tilde P + i^{k}\tilde Q)$ | the Hermitian polarisation of the algebraic norm |
| $H(\tilde{Q}) = 0\Leftrightarrow\tilde{Q} = 0$ | the definiteness, the substitute for the criterion |
| no unit, no inverse, no group of units | the absence carried by the block |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the Hermitian form $H$ and the table of the four forms.
- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class, its table and its placement among the twelve structures.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), §*The Unit and the Inverse*, for the relative notions of the unit, the inverse and the group of units.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the algebraic norm $B$ of the plain product, which is not the form $H$ of this article.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form $H$ read as the product, its Gram matrix, its positivity and its restriction to the remarkable subspaces.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the positivity and the cone of $H$.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`), for the zero-divisor set that is the complement of the origin.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the group of linear maps that preserve $H$, the substitute for the group of units.
