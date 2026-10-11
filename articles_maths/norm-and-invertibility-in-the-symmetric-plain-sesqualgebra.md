# __Norm and Invertibility in the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ on the biquaternion space, the Hermitian form $H$ read as a multiplication (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article studies the two notions that the general plain algebra attaches to its multiplication and that the block, having no unit, cannot inherit unchanged: the **norm** of an element and its **invertibility**.

A norm and an inverse name a product. The definitions are relative and are stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*; here they are read on the block. The block is **not unital**: it has no two-sided unit, and consequently no inverse, no group of units and no division structure, and the sections that would carry them state the **absence**. What the block does carry is a **norm**, the diagonal of the Hermitian form, and the norm is the substitute the block uses. In the general plain algebra the norm decides invertibility; here the analogous statement is a **definiteness**: the norm of the block vanishes only at the origin.

**Placement.** The article is the second entry of the *Common Theory* section of the block, after *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* and after *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and it precedes the articles on the zero divisors and on the roots of the central values. It uses the product and the class of the introduction, the definitions of the relative notions, and the positivity of the form.

**Boundaries.** The product, its class, its table and its placement among the twelve structures are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*. The form $H$, its Gram matrix, its positivity and its cone are *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the norm and the invertibility of the parent product are *Norm and Invertibility in the General Plain Algebra*. The definitions of the unit, the inverse, the group of units, the norm and the relative notions are *Definitions for the Study of the 12 Algebraic Structures*, and the four general products with their units are *Comparison Between the Four General Products*. The operators of the block, the group of linear maps that preserve $H$ and its algebra, are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2 = e_3$, and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu \varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu \overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is

$$
\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0, \qquad H(\tilde P,\tilde Q) = \sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$

and it is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$: $\mathbb{C}$-linear in the first argument and conjugate-linear in the second. The **norm** of the block is the diagonal of $H$, written $N(\tilde{Q}) = H(\tilde{Q},\tilde{Q})$.

## The Relative Notions

The word *unit*, the word *inverse* and the word *group of units* name a product, so the definitions are stated once for a general product and then read on the products of this space; they are in *Definitions for the Study of the 12 Algebraic Structures*.

**Definition (recalled).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star\tilde{Q} = \tilde{Q}$ for every $\tilde{Q}\in\mathbb{B}$, a **right unit** when $\tilde{Q}\star e = \tilde{Q}$ for every $\tilde{Q}\in\mathbb{B}$, and a **two-sided unit**, or an **identity**, when it is both. When a two-sided unit $e$ exists, an element $\tilde{Q}$ is **invertible of $\star$** when there is a $\tilde{R}$ with $\tilde{Q}\star\tilde{R} = \tilde{R}\star\tilde{Q} = e$, the element $\tilde{R}$ being the **inverse of $\tilde{Q}$ of $\star$**; the **group of units of $\star$** is the set of the invertible elements, a group under $\star$. When no two-sided unit exists, the three notions are empty and the group of units is not defined.

Throughout this article the product is the symmetric plain sesqualgebra $\star$, and another product is named where it is meant.

## The Absence of a Unit

**Theorem (the block has no unit).** The block has no left unit and no right unit: there is no element $e$ with $e\star\tilde{Q} = \tilde{Q}$ for every $\tilde{Q}\in\mathbb{B}$, and none with $\tilde{Q}\star e = \tilde{Q}$ for every $\tilde{Q}\in\mathbb{B}$. Hence there is no two-sided unit either.

*Proof.* Every value of the product is central, $e\star\tilde{Q} = H(e,\tilde{Q})e_0 \in \mathbb{C}e_0$. The element $e_1$ is not central, so $e\star e_1 \neq e_1$ for every $e$, and $e_1\star e \neq e_1$ for every $e$; there is therefore no left unit and no right unit, and so no two-sided unit. In particular the idempotent $e_0$ is not a unit: $e_0\star e_1 = H(e_0,e_1)e_0 = 0$, since the basis is orthonormal for $H$.

**Remark (the reason is the image).** The failure is structural and not an accident of one candidate: a product whose image is the central line cannot reproduce an element with a vector part, and the block has non-central elements. The same reason deprives the symmetric quaternionic product of a unit, while the symmetric plain product, whose image is the whole space, has the unit $e_0$.

## The Absence of an Inverse and of the Group of Units

**Theorem (no element is invertible, and there is no group of units).** No element of $\mathbb{B}$ is invertible of $\star$, and the group of units of $\star$ is not defined.

*Proof.* The notions of §*The Relative Notions* presuppose a two-sided unit, and §*The Absence of a Unit* shows that the block has none; the definition is therefore empty. There is no invertible element and no inverse formula.

**Remark (what the block does not have).** The block has no unit, no inverse, no group of units, no division structure and no three-way classification of the elements into the zero, the invertible and the zero divisors; its element classification is two-way and is read in §*The Substitute for the Invertibility Criterion*. The invertible elements of the plain product are read in *Norm and Invertibility in the General Plain Algebra*, and the block neither inherits them nor carries a substitute group.

## The Norm of the Block

**Definition.** The **norm of the block** of an element $\tilde{Q}$ is the diagonal of the Hermitian form,

$$
N(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2} \in \mathbb{R}_{\geq 0},
$$

a real non-negative number, and it is the coefficient of the square of the element,

$$
\tilde{Q}\star\tilde{Q} = N(\tilde{Q})e_0 .
$$

The equation names the product $\star$: the norm is relative to the product, and the norm of the general plain **algebra** is $\tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^{2}$, a different quadratic form (*Norm and Invertibility in the General Plain Algebra*). The diagonal of the general plain **sesquilinear** form is this same $N$, since the product of the block is that form read as a multiplication, so the norm separates the block from the plain algebra and not from the sesquilinear parent.

**Basic properties.** Each is a direct reading of the definition.

- $N(\tilde{Q})$ is a **real** number, $\overline{N(\tilde{Q})} = N(\tilde{Q})$, because each $\lvert Q_\mu\rvert^{2}$ is real.
- $N(\tilde{Q})$ is **non-negative**, and $N(\tilde{Q}) = 0$ exactly at $\tilde{Q} = 0$; the form $N$ is **positive definite**, of signature $(8,0)$ on the real space underlying $\mathbb{B}$.
- $N$ is **invariant under the three conjugations**, $N(\tilde{Q}^{\natural}) = N(\overline{\tilde{Q}}) = N(\tilde{Q}^{*}) = N(\tilde{Q})$, because each conjugation preserves the moduli $\lvert Q_\mu\rvert$ of the coordinates.
- $N$ is **homogeneous of degree two** over the reals but not over $\mathbb{C}$: $N(\lambda\tilde{Q}) = \lvert\lambda\rvert^{2}N(\tilde{Q})$ for $\lambda\in\mathbb{C}$.
- $N$ is the **polarisation source** of $H$: the form $H$ is recovered from $N$ in §*The Polarisation of the Norm*.

**Proposition (the Gram matrix and the square map).** On the basis $e_0,e_1,e_2,e_3$ the form $H$ has Gram matrix the identity, $H(e_\mu,e_\nu) = \delta_{\mu\nu}$, so $N(e_\mu) = 1$; the square map $\tilde{Q}\mapsto\tilde{Q}\star\tilde{Q}$ has image the real ray $\mathbb{R}_{\geq 0}e_0$ and is surjective onto it.

*Proof.* The Gram statement is $H(e_\mu,e_\nu) = \sum_\sigma (e_\mu)_\sigma\overline{(e_\nu)_\sigma} = \delta_{\mu\nu}$, and the square display gives the image. The ray is attained since $\tilde{Q} = \sqrt{\lambda}e_0$ gives $N(\tilde{Q}) = \lambda$ for $\lambda\geq 0$.

## The Failure of Multiplicativity

The norm of the general plain algebra is multiplicative, $N(\tilde P\tilde Q) = N(\tilde P)N(\tilde Q)$ (*Norm and Invertibility in the General Plain Algebra*). The norm of the block is **not** multiplicative, and the defect is exactly the failure of the form to be resolved by the norms of its two arguments.

**Theorem (the norm of a product).** For all $\tilde P,\tilde Q$,

$$
N(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2},
$$

the square of the modulus of the form on the two arguments; consequently $N(\tilde P\star\tilde Q) = N(\tilde P)N(\tilde Q)$ exactly when the two arguments are linearly dependent over $\mathbb{C}$.

*Proof.* The product is central, $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$, and $N(\lambda e_0) = \lvert\lambda\rvert^{2}$. So the norm of the product is $\lvert H(\tilde P,\tilde Q)\rvert^{2}$. For the equality case, the quadratic form $t\mapsto N(\tilde P - t\tilde Q)\geq 0$ in the complex variable $t$ has discriminant $N(\tilde P)N(\tilde Q) - \lvert H(\tilde P,\tilde Q)\rvert^{2}$, so this quantity is non-negative, and the vanishing of the discriminant is the vanishing of the form at its minimising argument, that is the proportionality of $\tilde P$ and $\tilde Q$.

**Corollary (the defect is the discriminant).** For all $\tilde P,\tilde Q$,

$$
N(\tilde P)N(\tilde Q) - N(\tilde P\star\tilde Q) = N(\tilde P)N(\tilde Q) - \lvert H(\tilde P,\tilde Q)\rvert^{2} \geq 0,
$$

with equality exactly when $\tilde P$ and $\tilde Q$ are linearly dependent. The norm is therefore **submultiplicative** and multiplicative exactly on linearly dependent pairs.

**Remark (the identity that replaces multiplicativity).** The block has one exact multiplicativity, read on the form rather than on the norm: for all $\tilde P,\tilde Q,\tilde R$,

$$
H(\tilde P\star\tilde Q,\tilde R) = H(\tilde P,\tilde Q)\,H(e_0,\tilde R),
$$

and dually $H(\tilde R,\tilde P\star\tilde Q) = H(\tilde R,e_0)\overline{H(\tilde P,\tilde Q)}$. The first factor $H(\tilde P,\tilde Q)$ is the coefficient of the product, the second is the evaluation of the form on the unit idempotent; the product is central, so the form evaluates it only through that one coefficient.

**Remark (the norm is multiplicative on the centre).** On the central line the block is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ and the norm is the squared modulus, $N(\lambda e_0) = \lvert\lambda\rvert^{2}$; on central elements the norm is multiplicative in the plain sense, $N\bigl((\lambda e_0)\star(\mu e_0)\bigr) = N(\lambda e_0)N(\mu e_0)$, because $\mathbb{C}e_0$ is a field. Multiplicativity holds on the centre and fails off it, and the failure is measured by the corollary.

## The Polarisation of the Norm

**Theorem (the polarisation).** The polar form of the quadratic map $N$ is twice the real part of $H$,

$$
N(\tilde P + \tilde Q) - N(\tilde P) - N(\tilde Q) = 2\Re H(\tilde P,\tilde Q),
$$

and the full Hermitian form is recovered from the norm by

$$
H(\tilde P,\tilde Q) = \tfrac{1}{4}\sum_{k=0}^{3}i^{k}\,N(\tilde P + i^{k}\tilde Q).
$$

*Proof.* The first display expands $N(\tilde P+\tilde Q) = N(\tilde P)+N(\tilde Q)+H(\tilde P,\tilde Q)+\overline{H(\tilde P,\tilde Q)}$. For the second, insert the four values $k = 0,1,2,3$ and use $N(\tilde P + i^k\tilde Q) = N(\tilde P)+N(\tilde Q)+2\Re\bigl(i^{-k}H(\tilde P,\tilde Q)\bigr)$; the four coefficients $1,i,-1,-i$ average to the real and imaginary parts of $H$, giving $H$.

**Remark (the polarisation is the Hermitian one).** The second display is the polarisation of a sesquilinear form and not of a bilinear one: the four coefficients are the fourth roots of unity, not the pair $\pm1$ of the symmetric polarisation, which is the form of the Hermitian symmetry $H(\tilde Q,\tilde P) = \overline{H(\tilde P,\tilde Q)}$. The first display extracts only the real part, because the diagonal $N$ of a Hermitian form is real; the imaginary part is carried by the four-term display. This is the sense in which the norm of the block polarises to $H$ and not to the symmetric bilinear form of the parent.

## The Substitute for the Invertibility Criterion

**Theorem (the criterion of the block).** For $\tilde{Q}\in\mathbb{B}$,

$$
N(\tilde{Q}) = 0 \quad\Longleftrightarrow\quad \tilde{Q} = 0 .
$$

*Proof.* $N(\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ is a sum of non-negative reals, vanishing exactly when every $Q_\mu$ vanishes.

**Remark (what replaces the criterion).** In the general plain algebra the criterion of invertibility reads $N(\tilde{Q})\neq0$ and separates the invertible elements from the zero divisors, the three-way classification (*Norm and Invertibility in the General Plain Algebra*). The block has no invertible element, and its criterion reads instead that the norm never vanishes off the origin: the block has **no nonzero element of zero norm**, or, in the vocabulary of forms, **no nonzero isotropic vector** for $H$ (the origin alone is isotropic). The block's element classification is therefore two-way, the zero element and the non-zero elements, and the non-zero elements are all of one kind, the zero divisors of *Zero Divisors of the Symmetric Plain Sesqualgebra*. The definiteness is the reason, and it is the exact opposite of the general plain algebra, whose norm $c(\tilde{Q}) = \sum_\mu Q_\mu^{2}$ vanishes on the nonzero isotropic cone.

**Corollary (the substitute for the group of units).** The block has no group of units; the set that replaces it is the group of the linear maps of $\mathbb{B}$ that preserve the form $H$, together with its algebra, and it is read as a group of linear maps in *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. The block carries no subgroup of its own elements to play that role, since it has no invertible element.

## The Comparison with the General Plain Algebra

The two products separate on every clause of the definition, and the table collects the separation.

| clause | general plain algebra | symmetric plain sesqualgebra |
|---|---|---|
| norm | $\tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^{2}$, complex | $H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$, real non-negative |
| multiplicativity | $N(\tilde P\tilde Q) = N(\tilde P)N(\tilde Q)$ | $N(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2}$, no multiplicativity |
| definiteness | indefinite, isotropic cone $\{c = 0\}$ | definite, no nonzero isotropic vector |
| unit | $e_0$, two-sided | none |
| invertible elements | norm non-zero, a group | none |
| zero divisors | the norm cone, non-zero | every non-zero element |

The parent is unital, its invertibility criterion is the non-vanishing of a multiplicative norm, and its zero divisors are a proper subset. The block is non-unital, its criterion is the non-vanishing of a definite norm, and its zero divisors are the whole complement of the origin; the two structures disagree at every clause above, and the disagreement is not a defect of the block but the shape of a rank-one product.

## Summary

The symmetric plain sesqualgebra $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ has **no unit**, because every value of the product is central and $\mathbb{B}$ has non-central elements; consequently it has **no inverse**, **no group of units** and no division structure, and the relative definitions are empty. Its **norm** is the diagonal of the Hermitian form, $N(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2} = $ the coefficient of $\tilde{Q}\star\tilde{Q}$, a real non-negative definite quadratic form of signature $(8,0)$, invariant under the three conjugations. The norm is **not multiplicative**: $N(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2}$, the defect is the discriminant $N(\tilde P)N(\tilde Q) - \lvert H(\tilde P,\tilde Q)\rvert^{2}\geq 0$, vanishing exactly on linearly dependent pairs, and the norm is multiplicative on the centre alone. What replaces multiplicativity is the exact identity $H(\tilde P\star\tilde Q,\tilde R) = H(\tilde P,\tilde Q)H(e_0,\tilde R)$. The norm polarises to the Hermitian form, $\Re H$ at the symmetric step and $H$ at the four-term display. What replaces the invertibility criterion is the **definiteness**, $N(\tilde{Q}) = 0\Leftrightarrow\tilde{Q} = 0$: the block has no nonzero isotropic vector and no invertible element, its element classification is two-way, and the complement of the origin is the zero-divisor set.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu}$ | the Hermitian form defining the block |
| $N(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ | the norm of the block, the coefficient of the square |
| $\tilde{Q}\star\tilde{Q} = N(\tilde{Q})e_0$ | the square map, image $\mathbb{R}_{\geq0}e_0$ |
| $N(\tilde P\star\tilde Q) = \lvert H(\tilde P,\tilde Q)\rvert^{2}$ | the norm of a product |
| $H(\tilde P\star\tilde Q,\tilde R) = H(\tilde P,\tilde Q)H(e_0,\tilde R)$ | the identity that replaces multiplicativity |
| $H(\tilde P,\tilde Q) = \tfrac14\sum_k i^{k}N(\tilde P + i^{k}\tilde Q)$ | the Hermitian polarisation of the norm |
| $N(\tilde{Q}) = 0\Leftrightarrow\tilde{Q} = 0$ | the definiteness, the substitute for the criterion |
| no unit, no inverse, no group of units | the absence carried by the block |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class, its table and its placement among the twelve structures.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative notions of the unit, the inverse, the group of units and the norm, and for their four-product dictionary.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the norm and the invertibility of the parent product, the multiplicativity and the isotropic cone.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form $H$ read as the product, its Gram matrix, its positivity and its restriction to the remarkable subspaces.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the positivity and the cone of $H$.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`), for the zero-divisor set that is the complement of the origin.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the group of linear maps that preserve $H$, the substitute for the group of units.
