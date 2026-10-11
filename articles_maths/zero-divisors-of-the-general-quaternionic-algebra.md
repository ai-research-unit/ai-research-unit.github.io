# __Zero Divisors of the General Quaternionic Algebra__

## Introduction

This article studies the **zero divisors** of the biquaternion algebra $\mathbb{B}$ read through the general quaternionic bilinear product, and it complements the norm of the product by describing the set on which the norm vanishes.

A divisor is relative to a product, and the definition is stated once in *Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor and the Annihilator*; the unqualified "zero divisor" means the zero divisor of the general quaternionic product throughout, and every other product is named. The article establishes four things. First, the **criterion**: a nonzero $\tilde Q$ is a zero divisor of $\star$ exactly when its norm vanishes, so the zero divisors of the quaternionic product are the nonzero solutions of $N(\tilde Q)=0$. Second, the set is the **zero-divisor cone**, a real cone of dimension six in the eight-dimensional real space that is not a subspace, and it is the union of the **pure** and the **non-pure** families of the element theory of the algebra. Third, the two **annihilators** of an element, taken with respect to $\star$, are each of complex dimension two for a zero divisor and vanish for a unit, and the element lies in its own annihilators. Fourth, and the sharpest fact of the article, the two annihilators **coincide for every element**, unit or zero divisor alike, because the natural conjugation is a $\mathbb{C}$-linear anti-automorphism of order two; the quaternionic product is the one product of the block whose annihilators are not exchanged by the conjugation.

**Boundaries.** The zero divisors of the algebra, the two families, the criterion in the plain product and the structure of the cone are *Zero Divisors of the General Plain Algebra*; the plain nilpotents are *Nilpotents of the General Plain Algebra*, and the plain idempotents *Idempotents of the General Plain Algebra*. The fact that the four general products select one and the same zero-divisor set, with its proof, and the one-sided inverse equations, are *The Zero Divisors and the Four General Products*; the article quotes that coincidence and does not reprove it. The norm and the one-sided equations of this product are *Norm and Invertibility in the General Quaternionic Algebra*; the nilpotents of the product are *Nilpotents of the General Quaternionic Algebra*; and the form on the remarkable subspaces is *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$. Juxtaposition is the plain product and $\star$ the general quaternionic bilinear product,

$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q ,
$$

with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_0-\mathbf Q$. An element is $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$, the **norm** is $N(\tilde Q)=\tilde Q^{\natural}\tilde Q=\sum_\mu Q_\mu^2$, and $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ is the complex bilinear form of the vector parts. An element is **pure** when $Q_0=0$ and **non-pure** when $Q_0\neq0$.

## Definition

The word names a product, so the definition is stated for a general product and then read on $\star$.

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$; a **right zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde R\star\tilde Q=0$; and a **zero divisor of $\star$** when it is one or the other. It is a **two-sided zero divisor of $\star$** when it is both. The definition is *Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor and the Annihilator*, and the origin is not a zero divisor, both factors being required to be nonzero.

Throughout this article the product is the general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$. On it the two defining equations are

$$
\tilde Q^{\natural}\tilde R=0 \quad\text{(left)},\qquad \tilde R^{\natural}\tilde Q=0 \quad\text{(right)} ,
$$

which are plain-product equations in the conjugated first factor.

## The Criterion

**Theorem (the criterion for the general quaternionic product).** For a nonzero $\tilde Q\in\mathbb{B}$, $\tilde Q$ is a zero divisor of $\star$ if and only if

$$
N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2=0 .
$$

**Proof.** Suppose $N(\tilde Q)=0$ and $\tilde Q\neq0$. Then

$$
\tilde Q\star\tilde Q=\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0=0 ,
$$

so $\tilde R=\tilde Q$ is a nonzero element with $\tilde Q\star\tilde R=0$ and $\tilde Q$ is a left zero divisor; the mirror computation with the factors exchanged gives the right statement. Conversely, suppose $\tilde Q$ is a zero divisor of $\star$: there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$, that is $\tilde Q^{\natural}\tilde R=0$. If $N(\tilde Q)\neq0$ then $\tilde Q^{\natural}$ is a unit of the plain product by §*The Criterion* of *Norm and Invertibility in the General Quaternionic Algebra*, and multiplying the equation by its inverse gives $\tilde R=0$, a contradiction. Hence $N(\tilde Q)=0$.

The criterion is the criterion of the plain product read on this product; the two are the same equation because the norm is the same quadratic form, and the two products are distinguished by the object that turns the equation into a statement — the plain inverse there, the conjugated one-sided solution here.

## The Three-Way Classification

Combining the criterion with the invertibility theory of the norm, the elements of $\mathbb{B}$ are partitioned into three classes, and the classification is the one of *Zero Divisors of the General Plain Algebra* with the inverse column read for this product.

| condition on $N(\tilde Q)$ | condition on $\tilde Q$ | conclusion |
|---|---|---|
| $N(\tilde Q)\neq0$ | none | a unit of the plain product, not a zero divisor of $\star$ |
| $N(\tilde Q)=0$ | $\tilde Q=0$ | the zero element, not a zero divisor |
| $N(\tilde Q)=0$ | $\tilde Q\neq0$ | a zero divisor of $\star$ |

The zero divisors are exactly the nonzero elements on which the norm vanishes. The classification is a classification of the elements by their behaviour under $\star$, and it does not describe them under the other products.

## The Algebra Is Not a Division Algebra

A **division algebra** is an algebra in which every nonzero element is invertible; for a finite-dimensional algebra this is equivalent to the absence of zero divisors. The biquaternion algebra contains zero divisors, so it is **not** a division algebra. The statement is the one of *Zero Divisors of the General Plain Algebra*, and it is independent of the product: the same elements are the zero divisors of both products, by the criterion above and the coincidence quoted below.

## The Two Families of Zero Divisors

The zero divisors split into two families according to the value of the scalar part, and the split does not depend on the product, because $N(\tilde Q)=Q_0^2+(\mathbf Q,\mathbf Q)$ separates the two cases on the element. A biquaternion is **pure** when $Q_0=0$ and **non-pure** when $Q_0\neq0$; on a pure element the criterion is $(\mathbf Q,\mathbf Q)=0$, and on a non-pure one it is $(\mathbf Q,\mathbf Q)=-Q_0^2$, which can be met by the vector part cancelling the scalar contribution. The two families are developed in *Zero Divisors of the General Plain Algebra*; in this product they are separated not by the square, which vanishes on both, but by the plain square, as the two sections below compute.

## Pure Zero Divisors

**Proposition (the square of a pure element).** Let $\tilde Q=\mathbf Q$ be a pure element. Then

$$
\tilde Q\star\tilde Q=(\mathbf Q,\mathbf Q)\,e_0 , \qquad \tilde Q\tilde Q=-(\mathbf Q,\mathbf Q)\,e_0 , \qquad \tilde Q^{\natural}=-\tilde Q .
$$

**Proof.** The scalar–vector form of the product at a pure pair is $(\mathbf Q,\mathbf Q)e_0$ for the quaternionic product and $-(\mathbf Q,\mathbf Q)e_0$ for the plain one, and the natural conjugation negates a pure element.

**Theorem (the criterion in the pure case).** For a nonzero pure $\tilde Q$ the following are equivalent:

1. $\tilde Q$ is a zero divisor of $\star$;
2. $(\mathbf Q,\mathbf Q)=0$;
3. $\tilde Q\star\tilde Q=0$;
4. $\tilde Q$ is a nilpotent of the plain product, $\tilde Q\tilde Q=0$.

**Proof.** The equivalence of (1) and (2) is the criterion specialised to $Q_0=0$. The equivalence of (2) with (3) and with (4) is the proposition above, both squares being the same scalar up to sign.

The pure zero divisors are therefore the **nilpotents of the plain product**: on them the two products have the same square, up to the sign, and in particular a pure zero divisor vanishes when squared in either product. In the older vocabulary they are the isotropic **bivectors** $\boldsymbol\rho+i\boldsymbol\rho'$ with $\boldsymbol\rho\perp\boldsymbol\rho'$ and $|\boldsymbol\rho|=|\boldsymbol\rho'|$, the parameterisation of *Zero Divisors of the General Plain Algebra*, §*The Bivector Form*.

## Non-Pure Zero Divisors

**Proposition (the square of a non-pure element).** Let $\tilde Q=Q_0e_0+\mathbf Q$ with $Q_0\neq0$ and $N(\tilde Q)=0$. Then

$$
\tilde Q\star\tilde Q=0 , \qquad \tilde Q\tilde Q=2Q_0\tilde Q\neq0 .
$$

**Proof.** The quaternionic square is $N(\tilde Q)e_0$ and the norm vanishes by the criterion. The plain square is $(Q_0^2-(\mathbf Q,\mathbf Q))e_0+2Q_0\mathbf Q$, and the criterion $(\mathbf Q,\mathbf Q)=-Q_0^2$ turns it into $2Q_0^2e_0+2Q_0\mathbf Q=2Q_0\tilde Q$, which is nonzero because $Q_0\neq0$ and $\tilde Q\neq0$.

**Theorem (the non-pure family is the idempotent family).** A non-pure zero divisor is a complex multiple of a nontrivial idempotent of the plain product,

$$
\tilde Q=2Q_0\tilde\Pi , \qquad \tilde\Pi=\frac{\tilde Q}{2Q_0} ,
$$

and conversely every complex multiple of a nontrivial plain idempotent is a non-pure zero divisor of $\star$.

**Proof.** The relation $\tilde Q\tilde Q=2Q_0\tilde Q$ of the proposition makes $\tilde\Pi=\tilde Q/(2Q_0)$ an idempotent of the plain product, nontrivial because $\tilde Q\neq0$ and $Q_0\neq0$; the converse is the statement of *Idempotents of the General Plain Algebra*, §*Idempotents and the Non-Pure Zero Divisors*, read with the norm.

**Remark (the displacement).** The non-pure zero divisor has vanishing quaternionic square, so it is a **nilpotent of the quaternionic product**, while it is the opposite of a nilpotent in the plain product: its plain square is the nonzero element $2Q_0\tilde Q$. In particular the Hermitian idempotents $\tilde\Pi(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$ satisfy

$$
\tilde\Pi(\hat\mu)\star\tilde\Pi(\hat\mu)=N(\tilde\Pi(\hat\mu))e_0=\tfrac14\bigl(1-(\hat\mu,\hat\mu)\bigr)e_0=0 , \qquad \tilde\Pi(\hat\mu)\tilde\Pi(\hat\mu)=\tilde\Pi(\hat\mu) ,
$$

so the two products see the same element as an idempotent and as a square-zero element. This displacement is the subject of *Idempotents of the General Quaternionic Algebra*.

## The Zero Divisor Set

**Definition.** The **zero-divisor cone** of the quaternionic product is the vanishing set of the norm,

$$
C=\{\tilde Q\in\mathbb{B}:N(\tilde Q)=0\}=\{\tilde Q:\tilde Q\star\tilde Q=0\} .
$$

**Proposition (shape).** The set $C$ is a real cone of real dimension $6$ in the real eight-dimensional space $\mathbb{B}$, and it is not a real subspace.

**Proof.** With $Q_\mu=q_\mu+iq'_\mu$ the real and the imaginary parts, the equation $N=\sum_\mu(q_\mu^2-q'_\mu{}^2)+2i\sum_\mu q_\mu q'_\mu=0$ is one complex equation, hence two real equations, and the set is a cone because $N$ is homogeneous of degree two; the two equations are independent off the origin, so the real dimension is $8-2=6$. For the failure of linearity, the elements $e_1+ie_2$ and $e_1-ie_2$ have norm $1-1=0$, while their sum $2e_1$ has norm $4$.

**Corollary.** The cone is a multiplicative set: for every $\tilde P$ and every $\tilde Q$ with $N(\tilde Q)=0$,

$$
N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)=0 ,
$$

so the product of a cone point with any element is again in the cone, on either side.

**Proof.** The multiplicativity of the norm of *Norm and Invertibility in the General Quaternionic Algebra*, §*Multiplicativity*, evaluated at $N(\tilde Q)=0$.

**The two families and the cone.** The cone is the union of the two families and of the origin: the pure family is the isotropic cone of the vector subspace, of real dimension four, and the non-pure family is the rest, of real dimension six. On a pure element the quaternionic and the plain squares vanish together; on a non-pure one only the quaternionic square vanishes, and the plain square is the nonzero multiple $2Q_0\tilde Q$. The distinction is invisible at the level of the quaternionic square, which is blind to it, and it is read from the scalar part of the element.

## The Annihilators

**Definition.** For $\tilde Q\in\mathbb{B}$ the **left annihilator** and the **right annihilator** with respect to $\star$ are

$$
\mathrm{Ann}_\ell(\tilde Q)=\{\tilde X\in\mathbb{B}:\tilde X\star\tilde Q=0\}=\{\tilde X:\tilde X^{\natural}\tilde Q=0\} , \qquad
\mathrm{Ann}_r(\tilde Q)=\{\tilde X\in\mathbb{B}:\tilde Q\star\tilde X=0\}=\{\tilde X:\tilde Q^{\natural}\tilde X=0\} .
$$

Both are $\mathbb{C}$-subspaces of $\mathbb{B}$, because the product is $\mathbb{C}$-linear in each slot and the conjugation ${}^{\natural}$ is $\mathbb{C}$-linear. They are nonzero exactly when $\tilde Q$ is a zero divisor of the corresponding side, and they are the kernels of the two one-sided multiplications.

### The Dimension of the Annihilators

**Theorem (the dimension of the annihilators).** Let $\tilde Q\in\mathbb{B}$.

- If $\tilde Q$ is a unit of the plain product, $N(\tilde Q)\neq0$, then $\mathrm{Ann}_\ell(\tilde Q)=\mathrm{Ann}_r(\tilde Q)=0$.
- If $\tilde Q\neq0$ is a zero divisor, $N(\tilde Q)=0$, then $\mathrm{Ann}_\ell(\tilde Q)$ and $\mathrm{Ann}_r(\tilde Q)$ are each of complex dimension two, and each contains $\tilde Q$.

**Proof.** The left annihilator is $\{\tilde X:\tilde X^{\natural}\tilde Q=0\}=\{\tilde Y^{\natural}:\tilde Y\tilde Q=0\}$, the substitution $\tilde Y=\tilde X^{\natural}$ being a bijection of $\mathbb{B}$; so its dimension is the dimension of the kernel of right multiplication by $\tilde Q$ in the plain product, which is $4-\operatorname{rank}(R_{\tilde Q})$. The plain algebra is isomorphic to the matrix algebra $M_2(\mathbb{C})$, so $\operatorname{rank}(R_{\tilde Q})$ is $4$ for a unit and $2$ for a nonzero zero divisor; hence the dimensions $0$ and $2$. The right annihilator is the same argument with left multiplication, whose rank is the same. Finally, if $N(\tilde Q)=0$ then $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0=0$, so $\tilde Q\in\mathrm{Ann}_\ell(\tilde Q)$, and $\tilde Q\tilde Q^{\natural}=0$, so $\tilde Q\in\mathrm{Ann}_r(\tilde Q)$.

A zero divisor annihilates itself on both sides. It is the reason the annihilator is the natural two-dimensional object attached to a point of the cone, and it is the reason the two annihilators of the next section are not empty.

### The Two Annihilators Coincide

For an arbitrary non-associative product the two annihilators of an element have no reason to be equal. For the quaternionic product they always are.

**Theorem (the coincidence).** For **every** $\tilde Q\in\mathbb{B}$, unit or zero divisor alike,

$$
\mathrm{Ann}_\ell(\tilde Q)=\mathrm{Ann}_r(\tilde Q) .
$$

**Proof.** Let $\tilde X\in\mathbb{B}$. Applying the involution ${}^{\natural}$ to the equation $\tilde X^{\natural}\tilde Q=0$ gives $(\tilde X^{\natural}\tilde Q)^{\natural}=0$, which is $\tilde Q^{\natural}\tilde X=0$ because ${}^{\natural}$ is an anti-automorphism of order two; the argument reverses because ${}^{\natural}$ is a bijection of $\mathbb{B}$ onto itself. Hence

$$
\tilde X\star\tilde Q=0 \iff \tilde X^{\natural}\tilde Q=0 \iff \tilde Q^{\natural}\tilde X=0 \iff \tilde Q\star\tilde X=0 ,
$$

and the two annihilators contain exactly the same elements.

**Corollary.** The two-sided annihilator $\mathrm{Ann}(\tilde Q)=\mathrm{Ann}_\ell(\tilde Q)=\mathrm{Ann}_r(\tilde Q)$ is a $\mathbb{C}$-subspace of complex dimension two when $\tilde Q$ is a zero divisor and is $0$ when it is a unit.

The coincidence is a property of this product: it holds because ${}^{\natural}$ is a **$\mathbb{C}$-linear** anti-automorphism of order two, so that the first factor can be conjugated away without changing the annihilation. The two sesquilinear products of the four carry the conjugate-linear star in the slot, and the corresponding statement there is theirs to make; it is not a property of an algebra with an involution alone.

**Example.** For the pure zero divisor $\tilde Q=e_1+ie_2$, whose vector part has $(\mathbf Q,\mathbf Q)=1-1=0$, the common annihilator is

$$
\mathrm{Ann}(e_1+ie_2)=\mathbb{C}\{e_1+ie_2,\ e_3-ie_0\} ,
$$

and for the non-pure zero divisor $\tilde Q=e_0+ie_1$, of norm $1-1=0$,

$$
\mathrm{Ann}(e_0+ie_1)=\mathbb{C}\{e_0+ie_1,\ e_2+ie_3\} .
$$

In both cases the element lies in its own annihilator and the annihilator is a two-dimensional $\mathbb{C}$-subspace; the two bases annihilate the element on both sides and are read off the multiplication table.

## The Zero Divisors and the Four General Products

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* give four definitions of a zero divisor, hence four zero-divisor sets. For the biquaternion algebra the four sets are one and the same set,

$$
\{\tilde Q\neq0:N(\tilde Q)=0\} ,
$$

and this is a theorem of *The Zero Divisors and the Four General Products*, §*The Four Zero-Divisor Sets Coincide*, which this article quotes and does not reprove. What the product changes is the **equation** and the **annihilator**: the four left zero-divisor equations are $\tilde Q\tilde R=0$, $\tilde Q^{\natural}\tilde R=0$, $\tilde Q\tilde R^{*}=0$ and $\tilde Q^{\natural}\tilde R^{*}=0$, four different equations with the same solution set, and the annihilators of one element depend on the product, as the coincidence theorem above shows for this one. The one-sided inverse equations and their solutions for the four products are the same article's §*The One-Sided Inverse Equations*, and the plain reading of the criterion is *Zero Divisors of the General Plain Algebra*.

## The Zero Divisors and the Remarkable Subspaces

Since the zero divisors are the nonzero elements of norm zero, their distribution among the remarkable subspaces is the distribution of the zeros of the quadratic form $N$, and the signatures are *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*.

| remarkable subspace | zero divisors |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | none |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | none |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | none |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | the pure family, an isotropic cone of real dimension four |
| $\mathbb{M}_{+}$, the Hermitian subspace | the non-pure Hermitian elements with $Q_0^2=-(\mathbf Q,\mathbf Q)$ |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | the non-pure anti-Hermitian elements with the same condition |

The centre, the quaternion subspace and the anti-quaternion subspace carry no zero divisor: the norm is definite on the last two and vanishes on the first only at the origin. The vector subspace carries the whole pure family. The two Hermitian subspaces carry the non-pure family in the form in which its elements are fixed by the star; a general non-pure zero divisor lies in neither, and the elements $e_1+ie_2$, of the vector subspace, and $e_0+ie_1$, of the Hermitian subspace, are the two standard witnesses.

## Summary

For the general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, a nonzero element is a zero divisor exactly when its norm vanishes, $N(\tilde Q)=\sum_\mu Q_\mu^2=0$, and the zero divisors are the nonzero points of the zero-divisor cone, a real cone of dimension six that is not a subspace and is stable under the product. The cone is the union of the **pure** family, the plain nilpotents $\boldsymbol\rho+i\boldsymbol\rho'$ with $\boldsymbol\rho\perp\boldsymbol\rho'$ and equal lengths, on which the quaternionic and the plain squares vanish together, and the **non-pure** family, the complex multiples of the nontrivial plain idempotents, on which the quaternionic square vanishes while the plain square is the nonzero multiple $2Q_0\tilde Q$. The left and the right annihilator of a zero divisor are each a complex plane containing the element, and both are $0$ for a unit; the two annihilators **coincide for every element**, because the natural conjugation is a $\mathbb{C}$-linear anti-automorphism of order two that turns the one equation into the other. The zero-divisor set is the same set as for the plain product, a coincidence of the algebra proved in *The Zero Divisors and the Four General Products*; what this product changes is the equation, the cone-shaped square, and the annihilator, which is symmetric here where the sesquilinear products make it conjugate-symmetric.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2=-e_0$ |
| $\tilde Q=Q_0e_0+\mathbf Q$ | an element and its scalar–vector split |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the norm, vanishing exactly on the zero-divisor cone |
| $C=\{N=0\}$ | the zero-divisor cone, the square-zero set of the product |
| pure, non-pure | $Q_0=0$; $Q_0\neq0$ |
| $\tilde\Pi(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ | the Hermitian idempotent over a real unit vector $\hat\mu$ |
| $\mathrm{Ann}_\ell(\tilde Q),\mathrm{Ann}_r(\tilde Q)$ | the left and the right annihilator of $\tilde Q$ for $\star$ |
| $\mathrm{Ann}(\tilde Q)$ | their common value, of complex dimension two for a zero divisor |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for zero divisors and annihilators in a non-associative algebra.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the product-relative definition of the zero divisor and of the annihilator.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for isotopes and the way a change of product moves the zero divisors.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for annihilators in a ring with an involution and the symmetry that an anti-automorphism imposes on them.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the isotropic vectors of the complex quaternion algebra and the quadratic form $\sum_\mu Q_\mu^2$.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the two families, the criterion in the plain product and the structure of the cone.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the norm, its multiplicativity and the one-sided equations.
- *The Zero Divisors and the Four General Products* (`articles_maths/the-zero-divisors-and-the-four-general-products.md`), for the coincidence of the four zero-divisor sets and the dependence of the annihilators on the product.
- *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra.md`), for the square-zero elements of the product and the index of nilpotency.
- *Idempotents of the General Quaternionic Algebra* (`articles_maths/idempotents-of-the-general-quaternionic-algebra.md`), for the displacement of the plain idempotents into the nilpotents of the product.
- *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the signatures of the norm on the six subspaces.
