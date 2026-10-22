# __Norm and Invertibility in the General Split-Complex Algebra__

## Introduction

This article studies the **algebraic norm** of the split-complex algebra read through the general plain sesquilinear product, and it settles what invertibility means for the plain product.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its form, the definition of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*. For the general plain sesquilinear product

$$
Q_1\star Q_2=Q_1\bar Q_2,
$$

the square of every element is scalar, $Q\star Q=Q\bar Q=\langle Q\rangle_{*}1$, so the form is real-valued and its diagonal is the real scalar $\langle Q\rangle_{*}=q^{2}-q'^{2}$. That scalar is the **second algebraic norm** of the space, the algebraic norm of this product and not the algebraic norm of the plain product, which is the $\mathbb{D}$-valued $\langle Q\rangle=Q^{2}$ of *Norm and Invertibility in the Split-Complex Algebra*. The norm $\langle\cdot\rangle_{*}$ is real, of signature $(1,1)$, indefinite, and multiplicative for the product.

The inverse is where the two products separate. The definition of an inverse presupposes a product with a **two-sided unit**, and the general plain sesquilinear product has a **right unit** alone. The consequence is stated and not filled: no element of $\mathbb{D}$ is invertible of $\star$, the product has no group of units of its own, and the word has no reading for it. What survives is the pair of one-sided inverse equations relative to the right unit $1$, and the article computes them: the two have the same unique solution, $Q_1/\langle Q_1\rangle_{*}$, exactly when the norm is non-zero, and neither has a solution when the norm vanishes. The criterion is therefore the algebraic norm of this product, and it is not the algebraic norm of the plain product; the two products do not share their algebraic norms.

**The results.** The general plain sesquilinear product $Q_1\star Q_2=Q_1\bar Q_2$ has a central square, $Q\star Q=\langle Q\rangle_{*}1$ with $\langle Q\rangle_{*}=q^{2}-q'^{2}$, and $\langle\cdot\rangle_{*}$ is multiplicative, $\langle Q_1\star Q_2\rangle_{*}=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$. The product has the right unit $1$ and no left unit, hence no two-sided unit, so **no element is invertible of $\star$** and the product has **no group of units**; what survives is the pair of one-sided equations $Q_1\star Q_2=1$ and $Q_2\star Q_1=1$, soluble exactly when $\langle Q_1\rangle_{*}\neq0$ with the common unique solution $Q_1/\langle Q_1\rangle_{*}$, and insoluble when $\langle Q_1\rangle_{*}=0$. The criterion is therefore the algebraic norm: a nonzero $Q$ is a zero divisor exactly when $\langle Q\rangle_{*}=0$, and the elements of non-vanishing norm form the plain group of units $\mathbb{D}^{\times}=\{\langle Q\rangle_{*}\neq0\}$, stable under $\star$ but not a group under it. Each section below states its result first and then proves it.

**Boundaries.** The algebraic norm of the plain product is $\langle Q\rangle=Q^{2}$, a $\mathbb{D}$-valued form, and its theory is *Norm and Invertibility in the Split-Complex Algebra*; the algebraic norm $\langle\cdot\rangle_{*}$ is the one of this product, and the criterion $\langle Q\rangle_{*}\neq0$ is proved here. The zero divisors are *Zero Divisors of the Split-Complex Algebra*, where the set $\{\langle Q\rangle_{*}=0\}\setminus\{0\}$ is characterised as a set; the annihilators are *Annihilators of the Split-Complex Algebra*; the one-sided inverse equations read on the two products side by side are *Relations and Comparison Between the Two Products of the Split-Complexoid Space*. The product and its element theory are *Split-Complex Algebra*; the two forms and the two algebraic norms are *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*; and the polar and exponential decompositions that the criterion must agree with are *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^{2}-1)=\mathbb{R}[j]$ with basis $1,j$, $j^{2}=+1$. A general element is $Q=q+jq'$ with $q=\operatorname{Re}Q$ and $q'=\operatorname{Im}Q$ real, the conjugate is $\bar Q=q-jq'$, and the idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$, with idempotent coordinates $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ and $Q_{\pm}=q\pm q'$. Juxtaposition is the plain product $Q_1Q_2$, and the product of this article is the general plain sesquilinear product

$$
Q_1\star Q_2=Q_1\bar Q_2 .
$$

## The Algebraic Norm of the Product

**The general plain sesquilinear product carries exactly one algebraic norm, the scalar of its central square, $\langle Q\rangle_{*}=q^{2}-q'^{2}$; its polar form is $\langle Q_1,Q_2\rangle_{*}=q_1q_2-q'_1q'_2$, and it is multiplicative, $\langle Q_1\star Q_2\rangle_{*}=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$.**

### Definition

The algebraic norm of a product is the diagonal of its form.

**Definition.** Let $\star$ be a product on $\mathbb{D}$ and let $\varphi(Q_1,Q_2)=\operatorname{Sc}(Q_1\star Q_2)$ be the scalar part of its form. The **algebraic norm of $\star$** is the diagonal

$$
\varphi(Q)=\varphi(Q,Q)=\operatorname{Sc}\bigl(Q\star Q\bigr).
$$

Throughout this article the product is the general plain sesquilinear product $Q_1\star Q_2=Q_1\bar Q_2$, whose square is scalar, so that the algebraic norm is the scalar coefficient of the square; it means the algebraic norm of that product, written $\langle\cdot\rangle_{*}$.

**Proposition.** For every $Q\in\mathbb{D}$,

$$
Q\star Q=Q\bar Q=\langle Q\rangle_{*}1,\qquad \langle Q\rangle_{*}=q^{2}-q'^{2}.
$$

**Proof.** The first display is the definition of the product at equal arguments; the product $Q\bar Q=(q+jq')(q-jq')=q^{2}-j^{2}q'^{2}=q^{2}-q'^{2}$ is real. The same scalar is produced in the two orders, $Q\bar Q=\bar Q Q$, because $\mathbb{D}$ is commutative.

The algebraic norm is therefore an element of $\mathbb{R}$ and not of $\mathbb{D}$: it is the value of a real quadratic form on the plane, and its vanishing set is a pair of lines and not a point.

### The Polarisation

**Proposition.** The polar form of the algebraic norm is

$$
\langle Q_1,Q_2\rangle_{*}=q_1q_2-q'_1q'_2,
$$

and one has

$$
\langle Q_1+Q_2\rangle_{*}-\langle Q_1\rangle_{*}-\langle Q_2\rangle_{*}=2\langle Q_1,Q_2\rangle_{*},\qquad
Q_1\star Q_2+Q_2\star Q_1=2\langle Q_1,Q_2\rangle_{*}1 .
$$

**Proof.** The first display is the expansion of $(q_1+q_2)^{2}-(q'_1+q'_2)^{2}$ minus the two diagonals. For the second, $Q_1\star Q_2+Q_2\star Q_1=Q_1\bar Q_2+Q_2\bar Q_1$, and the sum is real because the two terms are conjugate; its value is twice the real part of $Q_1\bar Q_2$, which is $q_1q_2-q'_1q'_2$.

The polar form is the **split bilinear form** $g$ of signature $(1,1)$; its Gram matrix in the basis $1,j$ is $\operatorname{diag}(1,-1)$.

### Multiplicativity

**Proposition.** The algebraic norm is multiplicative for the product,

$$
\langle Q_1\star Q_2\rangle_{*}=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*},
$$

and it is invariant under the conjugation, $\langle\bar Q\rangle_{*}=\langle Q\rangle_{*}$.

**Proof.** Since the bar is an automorphism and an involution,

$$
\langle Q_1\star Q_2\rangle_{*}=(Q_1\bar Q_2)(\overline{Q_1\bar Q_2})=Q_1\bar Q_2\bar Q_1 Q_2=Q_1\bar Q_1Q_2\bar Q_2=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*},
$$

using the commutativity of the algebra. For the invariance, $\langle\bar Q\rangle_{*}=\bar Q Q=Q\bar Q=\langle Q\rangle_{*}$.

**Corollary.** The vanishing set of the algebraic norm is stable under the product: if $\langle Q_2\rangle_{*}=0$ then $\langle Q_1\star Q_2\rangle_{*}=0$ for every $Q_1$, and the same with the factors exchanged.

## The Norm as a Semi-Norm

**Read as a norm of the algebra, $\langle\cdot\rangle_{*}$ is only a semi-norm: the sign axiom holds, the triangle inequality fails, and the value vanishes on nonzero elements.**

The scalar $\langle\cdot\rangle_{*}$ is the norm of the split-complex algebra as well as the algebraic norm of the product $\star$, and read as a norm of the algebra it is a **semi-norm**, the name recording two departures from a norm: the value is real but indefinite, and a nonzero element can have vanishing value. The audit of the usual axioms is as follows.

- The **sign axiom** holds, $\langle-Q\rangle_{*}=\langle Q\rangle_{*}$.
- The **triangle inequality** fails. For $Q=1+j$ and $B=1-j$ one has $\langle Q\rangle_{*}=\langle B\rangle_{*}=0$ while $\langle Q+B\rangle_{*}=\langle2\rangle_{*}=4$, so $\langle Q+B\rangle_{*}\le\langle Q\rangle_{*}+\langle B\rangle_{*}$ is false.
- The **scaling axiom** holds for real scalars in the quadratic form, $\langle\lambda Q\rangle_{*}=\lambda^{2}\langle Q\rangle_{*}$ for $\lambda\in\mathbb{R}$, and the square root $\sqrt{|\langle\cdot\rangle_{*}|}$ is absolutely homogeneous and multiplicative, but it is not subadditive.

So $\langle\cdot\rangle_{*}$ is a real-valued multiplicative semi-norm: multiplicative, homogeneous of degree two over the real scalars, indefinite, and vanishing exactly on the zero divisors and the origin. The absolute value $\rho=\sqrt{|\langle Q\rangle_{*}|}$ is the **modulus** of the polar decomposition; it is multiplicative and absolutely homogeneous, positive exactly on the units, and it is not a norm because it vanishes on the null cone.

## The Unique Real Norm

**The positive definite real norm of the algebra is the Euclidean norm $\|Q\|_{E}=\sqrt{q^{2}+q'^{2}}$, which comes from the real part of the plain square and not from the algebraic norm of either product.**

The **Euclidean form** is

$$
\langle Q,B\rangle_{E}=qb+q'b',
$$

the ordinary inner product of $\mathbb{R}^{2}$, positive definite and symmetric, of Gram matrix $\operatorname{diag}(1,1)$. Its diagonal is

$$
\|Q\|_{E}^{2}=q^{2}+q'^{2}=\operatorname{Re}(Q^{2}),
$$

the real part of the first algebraic norm. The Euclidean norm is a genuine norm: positive definite, subadditive, homogeneous of degree one. It is the norm that turns $\mathbb{D}$ into a topological algebra and that underlies the analysis of *Split-Complex Analysis*.

The Euclidean form is **not multiplicative**, and the Euclidean norm is not preserved by the split-complex product: for $Q=1+j$ one has $\|Q\|_{E}^{2}=2$ while $\|Q^{2}\|_{E}=\|2+2j\|_{E}=2\sqrt2\neq2$. It is the topological norm of the plane, not the algebraic norm of the ring.

## The Norm from the Halves

**In the idempotent coordinates the algebraic norm is the product of the two coordinates, $\langle Q\rangle_{*}=Q_{+}Q_{-}$, and this is the reason it vanishes exactly when one idempotent coordinate vanishes.**

Write $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ with $Q_{\pm}=q\pm q'$. Since multiplication is componentwise in the idempotent basis,

$$
Q\bar Q=(Q_{+}\Pi_{+}+Q_{-}\Pi_{-})(Q_{+}\Pi_{-}+Q_{-}\Pi_{+})=Q_{+}Q_{-}\Pi_{+}+Q_{+}Q_{-}\Pi_{-}=Q_{+}Q_{-},
$$

using $\bar\Pi_{\pm}=\Pi_{\mp}$. The two coordinates of the norm are equal, as they must be because the norm is real. In the same coordinates,

$$
\|Q\|_{E}^{2}=q^{2}+q'^{2}=\tfrac12(Q_{+}^{2}+Q_{-}^{2}),
$$

so the Euclidean norm is the root of the mean of the squares of the two idempotent coordinates, while the algebraic norm is their product. The two are related by

$$
Q_{+}^{2}+Q_{-}^{2}=2\|Q\|_{E}^{2},\qquad Q_{+}Q_{-}=\langle Q\rangle_{*} .
$$

## The Norm and the Hermitian Form

**The Hermitian form $H(Q_1,Q_2)=Q_1\bar Q_2$ is conjugate-symmetric, of real part the split bilinear form $g$ and imaginary part $q'_1q_2-q_1q'_2$; its diagonal is the algebraic norm $\langle Q\rangle_{*}$, and it is indefinite. There is no positive definite Hermitian form on $\mathbb{D}$.**

The **Hermitian form** is

$$
H(Q_1,Q_2)=Q_1\bar Q_2=(q_1q_2-q'_1q'_2)+j(q'_1q_2-q_1q'_2).
$$

It is $\mathbb{R}$-linear in the first slot and conjugate-linear in the second, and it is conjugate-symmetric,

$$
H(Q_2,Q_1)=\overline{H(Q_1,Q_2)} .
$$

Its real part is the polar form $g(Q_1,Q_2)=q_1q_2-q'_1q'_2$ of the algebraic norm, of signature $(1,1)$; its imaginary part is the alternating form $q'_1q_2-q_1q'_2$. Its diagonal is $H(Q,Q)=Q\bar Q=\langle Q\rangle_{*}$, real and indefinite. The form is therefore not positive definite, and neither is its negative.

There is **no positive definite Hermitian form** on $\mathbb{D}$ analogous to the one on $\mathbb{C}$, because the conjugation group is too small: the only non-trivial involution is the bar, and every sesquilinear form it defines has the indefinite real part $g$. The positive definite substitute is the Euclidean form $\langle\cdot,\cdot\rangle_{E}$ of the preceding section, which is symmetric and does not depend on the algebra structure. The Hermitian form $H$ and the Euclidean form are different objects: the diagonal of $H$ is the indefinite norm, and the diagonal of the Euclidean form is the positive definite square.

## The Unit and the Absence of the Inverse

**The product has the right unit $1$ and no left unit, hence no two-sided unit, so no element of $\mathbb{D}$ is invertible of $\star$ and the product has no group of units.**

**Definition.** Let $\star$ be a product on $\mathbb{D}$. An element $e$ is a **left unit of $\star$** when $e\star x=x$ for every $x$, a **right unit** when $x\star e=x$ for every $x$, and a **two-sided unit**, or **identity**, when it is both; and if $\star$ has a two-sided unit $e$, an element $x$ is **invertible of $\star$** when there is a $y$ with $x\star y=y\star x=e$. The definitions are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*, and they name the product at every step.

**Proposition (the unit).** The element $1$ is a right unit of $\star$ and the only one; there is no left unit; hence there is no two-sided unit.

**Proof.** $Q\star1=Q\bar1=Q$, so $1$ is a right unit. A right unit $E$ reads $1\star E=1$, that is $\bar E=1$, whence $E=1$. For the left unit, the equation $E\star Q=E\bar Q=Q$ at $Q=1$ gives $E=1$, and at $Q=j$ gives $E\bar j=-Ej=j$, that is $E=-1$, a contradiction. So there is no left unit.

**Absence (the inverse).** The product has no two-sided unit, so the definition of the inverse has no reading for it: **no element of $\mathbb{D}$ is invertible of $\star$**, and the product has no group of units. What the article computes in the next section is the pair of one-sided equations relative to the right unit $1$; it is not an inverse theory of the product, and it is never called one.

## The One-Sided Inverse Equations

**The two one-sided equations $Q_1\star Q_2=1$ and $Q_2\star Q_1=1$ have a solution exactly when $\langle Q_1\rangle_{*}\neq0$, and then each has the same unique solution $Q_1/\langle Q_1\rangle_{*}$; when $\langle Q_1\rangle_{*}=0$ neither equation has a solution.**

Relative to a right unit $1$ the two halves of the inverse equation remain meaningful, and they are the definition of the one-sided invertibility of the product.

**Definition.** Let $Q_1\in\mathbb{D}$. An element $Q_2$ with $Q_1\star Q_2=1$ is a **right inverse** of $Q_1$ relative to $1$, and an element $Q_3$ with $Q_3\star Q_1=1$ is a **left inverse** of $Q_1$ relative to $1$. The element $Q_1$ is **right-invertible** when it has a right inverse and **left-invertible** when it has a left inverse.

**Theorem (the one-sided equations).** For every $Q_1\in\mathbb{D}$ the two equations

$$
Q_1\star Q_2=1,\qquad Q_2\star Q_1=1
$$

have a solution exactly when $\langle Q_1\rangle_{*}\neq0$, and then each has the **same unique** solution,

$$
Q_2=\frac{Q_1}{\langle Q_1\rangle_{*}} .
$$

When $\langle Q_1\rangle_{*}=0$ neither equation has a solution.

**Proof.** The first equation is $Q_1\bar Q_2=1$, a plain-product equation; composing on the left with the plain inverse of $Q_1$, legitimate exactly when $Q_1$ is a unit, gives $\bar Q_2=Q_1^{-1}=\bar Q_1/\langle Q_1\rangle_{*}$, hence $Q_2=Q_1/\langle Q_1\rangle_{*}$. The plain algebra is associative, so the solution is unique when it exists. The element $Q_1$ is a unit of the plain product exactly when $\langle Q_1\rangle_{*}\neq0$. For the second equation, $Q_2\bar Q_1=1$; composing on the right with the plain inverse of $\bar Q_1$ gives $Q_2=(\bar Q_1)^{-1}=Q_1/\langle Q_1\rangle_{*}$, the same element. If $\langle Q_1\rangle_{*}=0$ and $Q_1\neq0$ then $Q_1$ is a zero divisor, so the equation $Q_1\bar Q_2=1$ has no solution; if $Q_1=0$ the equations read $0=1$, also with no solution.

**Remark.** The common solution is the quotient of the element by its norm, $Q_1/\langle Q_1\rangle_{*}$, and not the plain inverse $\bar Q_1/\langle Q_1\rangle_{*}$. The two differ by the conjugation; the coincidence of the two one-sided solutions is the content of the pair of equations read on this product.

**Corollary.** The element $Q_1$ is left-invertible and right-invertible relative to $1$ exactly when $\langle Q_1\rangle_{*}\neq0$, and then one and the same element, $Q_1/\langle Q_1\rangle_{*}$, serves as both a left inverse and a right inverse:

$$
Q_1\star\frac{Q_1}{\langle Q_1\rangle_{*}}=1=\frac{Q_1}{\langle Q_1\rangle_{*}}\star Q_1 .
$$

**Proof.** The theorem gives the two solutions and they are equal. The identity is the theorem at that element, using $Q_1\bar Q_1=\langle Q_1\rangle_{*}1$ and $\bar Q_1Q_1=\langle Q_1\rangle_{*}1$.

The corollary is a statement about the right unit $1$ and not an inverse of the product, because the product has no left unit: the equation it solves uses $1$ on the right, where $1$ is not a left unit, so the solution is a one-sided object of each equation and not an inverse in the sense of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Criterion

**For a nonzero $Q$ the conditions $\langle Q\rangle_{*}\neq0$, solubility of the plain equation $QB=1$, and solubility of the two one-sided equations of $\star$ are equivalent; equivalently, $Q$ is a zero divisor of the algebra exactly when $\langle Q\rangle_{*}=0$.**

**Theorem (the criterion for the general split-complex product).** For a nonzero $Q\in\mathbb{D}$ the following are equivalent:

1. $\langle Q\rangle_{*}\neq0$;
2. the plain-product equation $QB=1$ has a solution, namely $B=Q^{-1}=\bar Q/\langle Q\rangle_{*}$;
3. the two one-sided equations of §*The One-Sided Inverse Equations* have a solution.

They are equivalent to the single negative statement that $Q$ is a zero divisor of the algebra if and only if $\langle Q\rangle_{*}=0$.

**Proof.** The equivalence of (1) and (2) is the plain invertibility criterion: $Q\bar Q=\langle Q\rangle_{*}1$ is nonzero exactly when $Q$ is not a zero divisor of the plain product. The equivalence of (1) and (3) is the theorem of the preceding section. For the last clause, $Q\neq0$ with $\langle Q\rangle_{*}=0$ is a zero divisor of the algebra, and conversely (*Zero Divisors of the Split-Complex Algebra*).

The criterion is expressed by the algebraic norm $\langle\cdot\rangle_{*}$ of this product, because the vanishing set of $\langle\cdot\rangle_{*}$ is the zero-divisor set; it is not expressible by the algebraic norm of the plain product, which is $\langle\cdot\rangle=Q^{2}$ and does not decide invertibility (*Norm and Invertibility in the Split-Complex Algebra*).

**Corollary.** If $Q$ is a unit of the plain product, so is $\bar Q$, and $(\bar Q)^{-1}=\overline{Q^{-1}}$.

**The unit-norm case.** For an element of **unit norm**, $\langle Q\rangle_{*}=1$, the inverse formula collapses to

$$
Q^{-1}=\bar Q,
$$

the conjugate; these are the versors of *The Versors and the Orthogonal Group of the Split-Complex Numbers*. The inverse and the conjugate coincide exactly on the unit hyperbola $\langle Q\rangle_{*}=1$, and not elsewhere: for $Q=2$ one has $Q^{-1}=\tfrac12$ while $\bar Q=2$.

## The Three-Way Classification

**The elements of $\mathbb{D}$ fall into exactly three classes by the value of $\langle\cdot\rangle_{*}$: $\langle Q\rangle_{*}\neq0$ gives a unit of the plain product with both one-sided equations of $\star$ soluble, while $\langle Q\rangle_{*}=0$ gives the zero element at $Q=0$ and a zero divisor, with neither equation soluble, otherwise.**

The elements of $\mathbb{D}$ fall into three classes according to the value of the algebraic norm, and the classes are the ones of the plain algebra with the inverse column replaced by the one-sided column.

| condition on $\langle Q\rangle_{*}$ | condition on $Q$ | under the plain product | under the sesquilinear product |
|---|---|---|---|
| $\langle Q\rangle_{*}>0$ | none | a timelike unit | the one-sided equations soluble, with the common solution $Q/\langle Q\rangle_{*}$ |
| $\langle Q\rangle_{*}<0$ | none | a spacelike unit | the one-sided equations soluble, with the common solution $Q/\langle Q\rangle_{*}$ |
| $\langle Q\rangle_{*}=0$ | $Q=0$ | the zero element | the zero element |
| $\langle Q\rangle_{*}=0$ | $Q\neq0$ | a zero divisor | a zero divisor, with neither one-sided equation soluble |

The classification by the sign of the norm is multiplicative, since $\langle Q_1\star Q_2\rangle_{*}=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$: the product of two timelike elements is timelike, a timelike times a spacelike is spacelike, and a null factor makes the product null.

## The Group of Units

**The set $\mathbb{D}^{\times}=\{Q:\langle Q\rangle_{*}\neq0\}$ is the group of units of the plain product and is stable under $\star$, but it is not a group under $\star$, because that product has no two-sided unit and is not associative.**

Let $\mathbb{D}^{\times}=\{Q:\langle Q\rangle_{*}\neq0\}$ be the set of the elements on which the algebraic norm does not vanish.

**Proposition.** The set $\mathbb{D}^{\times}$ is the group of units of the plain product, it contains $1$, and it is stable under the sesquilinear product. It is **not** a group under $\star$: the product has no two-sided unit and it is not associative, so $\mathbb{D}^{\times}$ with $\star$ is a set with a right unit in which every right translation is a bijection, and nothing more.

**Proof.** The first clause is the plain invertibility criterion. Stability under $\star$ is the multiplicativity of the algebraic norm: $\langle Q_1\star Q_2\rangle_{*}=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}\neq0$. The absence of a two-sided unit is §*The Unit and the Absence of the Inverse*, and the failure of associativity is *The Two Products of the Split-Complexoid Space*; a group requires both, so there is none. Finally, the right translation $Q_2\mapsto Q_1\star Q_2=Q_1\bar Q_2$ is a plain right multiplication by the unit $Q_1$ composed with the conjugation, and it is a bijection.

**The four components.** Under the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ the group of units corresponds to

$$
\mathbb{D}^{\times}\cong\mathbb{R}^{\times}\times\mathbb{R}^{\times},
$$

the pairs with both coordinates nonzero. Each factor $\mathbb{R}^{\times}$ has two connected components, so the product has four, indexed by the signs of the two idempotent coordinates:

$$
\{Q_{+}>0,Q_{-}>0\},\quad \{Q_{+}>0,Q_{-}<0\},\quad \{Q_{+}<0,Q_{-}>0\},\quad \{Q_{+}<0,Q_{-}<0\}.
$$

The identity component is $\{Q_{+}>0,Q_{-}>0\}=\{\langle Q\rangle_{*}>0,\operatorname{Re}Q>0\}$, isomorphic as a Lie group to $\mathbb{R}^{2}$; it is the image of the exponential map of *Split-Complex Exponential and Lie Group Structure*.

**Non-compactness.** The group $\mathbb{D}^{\times}$ is **not compact**: the real units $Q=t$ with $t\ge1$ form an unbounded subset in the Euclidean norm. Equivalently, the unit hyperbola $\{\langle Q\rangle_{*}=1\}$ is unbounded, in contrast with the compact unit circle of $\mathbb{C}$.

## The Algebraic Norm on the Distinguished Subspaces

**The algebraic norm is definite on the real and the split imaginary lines and identically zero on the two idempotent lines; accordingly every nonzero element of the first two is a plain unit, while the two idempotent lines carry the zero divisors.**

The distinguished one-dimensional subspaces of $\mathbb{D}$ are the eigenspaces of the conjugation, $\mathbb{R}_{\mathbb{D}}$ and $j\mathbb{R}_{\mathbb{D}}$, and the two idempotent lines $\mathbb{R}\Pi_{+}$ and $\mathbb{R}\Pi_{-}$.

### The Real Subspace $\mathbb{R}_{\mathbb{D}}$

On $\mathbb{R}_{\mathbb{D}}$ the norm is $\langle q\rangle_{*}=q^{2}$, positive definite and vanishing only at $q=0$. Every nonzero real number is a timelike unit, with $\langle\cdot\rangle_{*}>0$; the units of $\mathbb{R}_{\mathbb{D}}$ are $\mathbb{R}^{\times}$, the two open rays. There are no zero divisors on $\mathbb{R}_{\mathbb{D}}$.

### The Split Imaginary Subspace $j\mathbb{R}_{\mathbb{D}}$

On $j\mathbb{R}_{\mathbb{D}}$ the norm is $\langle jq'\rangle_{*}=-q'^{2}$, negative definite and vanishing only at $q'=0$. Every nonzero element $jq'$ is a spacelike unit, and

$$
(jq')^{-1}=\frac{\overline{jq'}}{\langle jq'\rangle_{*}}=\frac{-jq'}{-q'^{2}}=\frac{j}{q'},
$$

so $(jq')(j/q')=1$. There are no zero divisors on $j\mathbb{R}_{\mathbb{D}}$.

### The Idempotent Lines

The zero divisors lie on neither eigenspace but on the two diagonal lines

$$
\mathbb{R}\Pi_{+}=\mathbb{R}(1+j),\qquad \mathbb{R}\Pi_{-}=\mathbb{R}(1-j),
$$

on each of which $\langle\cdot\rangle_{*}$ vanishes identically. These lines are not fixed by the conjugation; it swaps them, $\overline{\Pi_{+}}=\Pi_{-}$. They are the two isotropic lines of the form $g$, and their union is the null cone $\mathcal{N}$.

### Summary of the Distribution

| subspace | dimension | restricted $\langle\cdot\rangle_{*}$ | invertible elements | zero divisors |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $1$ | $q^{2}$, positive definite | all nonzero, timelike | none |
| $j\mathbb{R}_{\mathbb{D}}$ | $1$ | $-q'^{2}$, negative definite | all nonzero, spacelike | none |
| $\mathbb{R}\Pi_{+}$ | $1$ | $0$ | none but $0$ | all nonzero |
| $\mathbb{R}\Pi_{-}$ | $1$ | $0$ | none but $0$ | all nonzero |

So the two eigenspaces of the conjugation are totally invertible, while the two idempotent lines are totally singular; the null cone meets the two eigenspaces only at the origin.

## Summary

The general plain sesquilinear product $Q_1\star Q_2=Q_1\bar Q_2$ carries one algebraic norm, the scalar of its central square,

$$
\langle Q\rangle_{*}=Q\bar Q=q^{2}-q'^{2},
$$

real, of signature $(1,1)$, indefinite, and multiplicative, $\langle Q_1\star Q_2\rangle_{*}=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$. Its polar form is $g(Q_1,Q_2)=q_1q_2-q'_1q'_2$, the split bilinear form; its vanishing set is the two null lines $\mathbb{R}\Pi_{+}\cup\mathbb{R}\Pi_{-}$.

The product has the right unit $1$ and no left unit, hence no two-sided unit, so no element is invertible of $\star$ and the product has no group of units. The two one-sided equations relative to $1$ have the common unique solution $Q/\langle Q\rangle_{*}$ exactly when $\langle Q\rangle_{*}\neq0$, and no solution when the norm vanishes. The criterion is therefore the algebraic norm: a nonzero element is a zero divisor exactly when its norm vanishes, and the elements of non-vanishing norm form the plain group of units

$$
\mathbb{D}^{\times}=\{\langle Q\rangle_{*}\neq0\}\cong\mathbb{R}^{\times}\times\mathbb{R}^{\times},
$$

an abelian group with four connected components and non-compact, in contrast with the compact connected unit circle of $\mathbb{C}$. The elements are classified as timelike, null or spacelike by the sign of the norm, the classification being multiplicative; the null class consists of the zero divisors together with the origin. On the two eigenspaces of the conjugation the restricted norm is definite, while the two idempotent lines are totally singular.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Q=q+jq'$ | General split complex number |
| $\bar Q=q-jq'$ | Split complex conjugate |
| $Q_1\star Q_2=Q_1\bar Q_2$ | General plain sesquilinear product |
| $\langle Q\rangle_{*}=Q\bar Q=q^{2}-q'^{2}$ | Algebraic norm of $\star$, signature $(1,1)$ |
| $g(Q_1,Q_2)=q_1q_2-q'_1q'_2$ | Polarisation of $\langle\cdot\rangle_{*}$, the split bilinear form |
| $Q_{\pm}=q\pm q'$ | Idempotent coordinates, $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | Idempotents |
| $\mathcal{N}=\{\langle Q\rangle_{*}=0\}$ | Isotropic cone, the two null lines $\mathbb{R}\Pi_{\pm}$ |
| $\rho=\sqrt{|\langle Q\rangle_{*}|}=\sqrt{|Q_{+}Q_{-}|}$ | Modulus, multiplicative and absolutely homogeneous |
| $\|Q\|_{E}=\sqrt{q^{2}+q'^{2}}$ | Euclidean norm, the positive definite real norm |
| $\langle Q,B\rangle_{E}=qb+q'b'$ | Euclidean inner product |
| $H(Q_1,Q_2)=Q_1\bar Q_2=(q_1q_2-q'_1q'_2)+j(q'_1q_2-q_1q'_2)$ | Hermitian form; real part $g$, indefinite |
| $\mathbb{D}^{\times}=\{\langle Q\rangle_{*}\neq0\}$ | Group of units of the plain product |
| $\mathbb{D}^{\times}_{0}$ | Identity component, $\{Q_{+}>0,Q_{-}>0\}$ |

## Further Reading

- [Norm and Invertibility in the Split-Complex Algebra](norm-and-invertibility-in-the-split-complex-algebra.html), for the other algebraic norm, the $\mathbb{D}$-valued $Q^{2}$, and the absence of a criterion from it.
- [The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space](the-two-forms-and-the-two-algebraic-norms-of-the-split-complexoid-space.html), for the two forms and the two algebraic norms, their Gram matrices and their realified signatures.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the zero-divisor set and its two families.
- [Annihilators of the Split-Complex Algebra](annihilators-of-the-split-complex-algebra.html), for the annihilation of a line by a zero divisor.
- [The Two Products of the Split-Complexoid Space](the-two-products-of-the-split-complexoid-space.html), for the two products and the failure of associativity of the sesquilinear one.
- [Split-Complex Algebra](split-complex-algebra.html), for the product, its unit and its element theory.
- [The Versors and the Orthogonal Group of the Split-Complex Numbers](the-versors-and-the-orthogonal-group-of-the-split-complex-numbers.html), for the unit-norm group and its geometry.
