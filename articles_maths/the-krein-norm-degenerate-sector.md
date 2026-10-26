# __The K-Degenerate Sector__

## Introduction

This is the zero half of the Krein partition of the biquaternion algebra: the set on which the Krein norm vanishes, the **null set**

$$
\mathcal K=\{\tilde Q:\langle\tilde Q\rangle_{\natural*}=0\}
=\{\tilde Q:|Q_t|=\lVert\vec Q\rVert_E\}.
$$

It is a real cone of real codimension one, smooth off its apex, and its partner is *The K-Regular Sector*. The two articles carry the partition of *K-Regularity and Degeneracy in the Biquaternion Algebra*; the spectral condition is not used as a subdivision, and §*Why There Is No Spectral Split* of that article gives the four reasons.

The sector is **not homogeneous algebraically**. It splits by the algebraic norm into the **doubly null set** $\mathcal K_{\mathrm d}=\mathcal K\cap\mathcal N$, which is the Peirce lines together with the origin, and the **isotropic units** $\mathcal K_{\mathrm u}=\mathcal K\setminus\mathcal K_{\mathrm d}$. That split is the trace of the algebraic partition, zero divisors against units, and it is the only refinement of the sector that the corpus uses.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, of complex dimension four and real dimension eight, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$, the Hermitian conjugation is $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$, and $\varepsilon=(1,-1,-1,-1)$. The forms are

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}},\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}},
$$

so that $\langle\tilde Q\rangle_{\natural*}=|Q_t|^2-\lVert\vec Q\rVert_E^2$ is the **Krein norm**. The **algebraic norm** is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ with $B^2=Q_x^2+Q_y^2+Q_z^2$; it is multiplicative and it decides invertibility. Its zero set is the algebraic null cone $\mathcal N$, and $\mathcal Z=\mathcal N\setminus\{0\}$ is the zero-divisor set. The product is the plain product, with unit $e_t$.

## Definition and Characterisation

**Definition.** The **Krein-degenerate sector** is the null set

$$
\mathcal K=\{\tilde Q:\langle\tilde Q\rangle_{\natural*}=0\}
=\{\tilde Q:|Q_t|=\lVert\vec Q\rVert_E\}.
$$

Its elements are **isotropic**; the non-zero ones are the **Krein-null** elements.

**Theorem (five descriptions).** For $\tilde Q\neq0$ the following are equivalent:

(i) $\tilde Q\in\mathcal K$;

(ii) $|Q_t|=\lVert\vec Q\rVert_E$;

(iii) the complex line $\mathbb{C}\tilde Q$ is totally isotropic for the Krein form;

(iv) the real plane $\operatorname{span}_{\mathbb{R}}\{\tilde Q,i\tilde Q\}$ is totally isotropic for the realified form;

(v) the restriction of the Krein form to $\mathbb{C}\tilde Q$ vanishes identically.

*Proof.* (i) $\iff$ (ii) is the coordinate form of the norm. On the complex line the form is $\lambda\mapsto|\lambda|^2\langle\tilde Q\rangle_{\natural*}$, which vanishes identically exactly when $\langle\tilde Q\rangle_{\natural*}=0$, and then the line is its own radical: this is (ii) $\iff$ (iii) $\iff$ (v). The real plane is the real space of the complex line, and the real form is the real part of the Hermitian one, so its radical is the real space of the complex radical: (iii) $\iff$ (iv).

**Corollary (the Krein sign on a null line).** A null line is neither positive nor negative definite: it is degenerate, and its radical is the line itself. This is the line criterion of *K-Regularity and Degeneracy in the Biquaternion Algebra*, §*Krein Orthogonality and the Complement*, read at the value zero.

**Corollary (the scalar part never vanishes off the origin).** Every non-zero element of $\mathcal K$ has $Q_t\neq0$.

*Proof.* If $Q_t=0$ then $\lVert\vec Q\rVert_E=0$, hence $\vec Q=0$ and $\tilde Q=0$.

**Remark (the null set is not the algebraic null cone).** The two cones are different objects of the same ambient space: $\mathcal N$ has complex dimension three and real dimension six, and $\mathcal K$ is a real hypersurface of real dimension seven. They meet in $\mathcal K_{\mathrm d}$, of real dimension four. The element $e_t+\vec e_x$ is Krein-null and a unit; the element $\vec e_x+i\vec e_y$ is a zero divisor and not Krein-null.

## Geometry

**Theorem (a real cone with an apex).** $\mathcal K$ is a real cone of real dimension $7$, invariant under every complex scalar, and smooth off the origin. Its only singular point is the origin.

*Proof.* The norm is homogeneous of degree two under complex scalars, $\langle\lambda\tilde Q\rangle_{\natural*}=|\lambda|^2\langle\tilde Q\rangle_{\natural*}$, so the zero set is a cone. The gradient in the real coordinates $(\operatorname{Re}Q_t,\operatorname{Im}Q_t,\operatorname{Re}\vec Q,\operatorname{Im}\vec Q)$ is $2(\operatorname{Re}Q_t,\operatorname{Im}Q_t,-\operatorname{Re}\vec Q,-\operatorname{Im}\vec Q)$, which vanishes only at the origin; off it the zero set is a smooth hypersurface. At the origin the cone has its apex.

**Theorem (parametrisation).** The map

$$
\Psi:\mathbb{C}^{\times}\times S^5\longrightarrow\mathcal K\setminus\{0\},
\qquad
\Psi(Q_t,W)=Q_t(e_t+W),
$$

with $S^5=\{W\in\mathbb{C}^3:\lVert W\rVert_E=1\}$, is a bijection. Hence $\mathcal K\setminus\{0\}$ is connected, of real dimension $7$, and homotopy equivalent to $S^1\times S^5$.

*Proof.* For $\tilde Q\neq0$ null, $Q_t\neq0$ and $W=\vec Q/Q_t$ has $\lVert W\rVert_E=|\lVert\vec Q\rVert_E/|Q_t|=1$; conversely $\langle Q_t(e_t+W)\rangle_{\natural*}=|Q_t|^2(1-\lVert W\rVert_E^2)=0$. The inverse is $\tilde Q\mapsto(Q_t,\vec Q/Q_t)$. The factor $\mathbb{C}^{\times}$ is homotopy equivalent to $S^1$.

**Corollary (one orbit).** The isometry group $\mathrm{U}(1,3)$ acts transitively on $\mathcal K\setminus\{0\}$. Every $\mathrm{U}(1,3)$-invariant function on the punctured null set is constant, so the metric structure of the sector is exhausted by the value of the norm: there is no further metric invariant inside it.

*Proof.* The parametrisation identifies $\mathcal K\setminus\{0\}$ with $\mathbb{C}^{\times}\times S^5$, and $\mathrm{U}(1,3)$ acts transitively on it by §*Why There Is No Spectral Split* of the main article.

**Remark (the projective quadric).** The quotient of $\mathcal K\setminus\{0\}$ by the complex scalars is the null quadric of the form in $\mathbb{CP}^3$, a real manifold of dimension $5$; the parametrisation above exhibits the punctured null set as a $\mathbb{C}^{\times}$-bundle over it. The quadric is the boundary of the complex hyperbolic space of *The Krein Level Sets and the Hyperbolic Structure*.

**Remark (the cone is not pointed).** $\mathcal K$ is invariant under $\tilde Q\mapsto-\tilde Q$, so it contains opposite pairs of rays. It is not convex either: the null elements $e_t+\vec e_x$ and $-e_t+\vec e_x$ have the midpoint $\vec e_x$, of value $-1$.

## The Witt Index

**Definition.** A subspace $\mathbb{W}$ is **totally isotropic** when $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=0$ for all $\tilde Q_1,\tilde Q_2\in\mathbb{W}$, equivalently when $\mathbb{W}\subseteq\mathbb{W}^{\perp_K}$, where $\mathbb{W}^{\perp_K}=\{\tilde Q:\langle\tilde Q,\tilde W\rangle_{\natural*}=0\ \text{for every}\ \tilde W\in\mathbb{W}\}$ is the Krein-orthogonal complement; it is **maximal** when it is contained in no larger one. The **Witt index** is the common dimension of the maximal totally isotropic subspaces.

**Theorem (the Witt index).** The Witt index is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$. Every maximal totally isotropic complex subspace is a line, and $\mathbb{C}(e_t+\vec e_x)$ is one; a maximal totally isotropic real subspace is the plane
$$
\mathbb{W}_{\mathrm{iso}}=\operatorname{span}_{\mathbb{R}}\{e_t+\vec e_x,\ i(e_t+\vec e_x)\}.
$$
Every totally isotropic subspace is contained in a maximal one, and $\mathrm{U}(1,3)$ acts transitively on the maximal ones.

*Proof.* A totally isotropic subspace meets $\mathbb{V}_{\mathbb{B}}=\operatorname{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}$ only at the origin, since a non-zero element of $\mathbb{V}_{\mathbb{B}}$ has negative value; it therefore injects into $\mathbb{B}/\mathbb{V}_{\mathbb{B}}$, of real dimension $2$ and complex dimension $1$. Hence its real dimension is at most $2$ and its complex dimension at most $1$. The displayed line and plane are totally isotropic,
$$
\langle e_t+\vec e_x,e_t+\vec e_x\rangle_{\natural*}=0,\qquad
\langle e_t+\vec e_x,i(e_t+\vec e_x)\rangle_{\natural*}=0,\qquad
\langle i(e_t+\vec e_x),i(e_t+\vec e_x)\rangle_{\natural*}=0,
$$
and they attain the bounds. Witt's extension theorem gives the extension property and the transitivity.

**Remark (the real planes).** Every real totally isotropic plane is the realification of a complex isotropic line. A real plane that is not complex would complexify to a complex totally isotropic plane of dimension two, beyond the Witt index one. The maximal real plane $\mathbb{W}_{\mathrm{iso}}$ is not a Peirce line: it is a real plane and not a complex line, and it contains $e_t+\vec e_x$, of algebraic norm $2$.

## The Two Strata

**Definition.** The **doubly null set** and the **isotropic units** are

$$
\mathcal K_{\mathrm d}=\mathcal K\cap\mathcal N=\{\tilde Q\in\mathcal K:\langle\tilde Q\rangle_{\natural}=0\},\qquad
\mathcal K_{\mathrm u}=\mathcal K\setminus\mathcal K_{\mathrm d}.
$$

**Theorem (the two strata).** $\mathcal K=\mathcal K_{\mathrm d}\uplus\mathcal K_{\mathrm u}$. The doubly null set is closed in $\mathcal K$, of real dimension $4$; the isotropic units form its open dense complement, of real dimension $7$. The points of $\mathcal K_{\mathrm d}$ are the origin together with the zero divisors of $\mathcal K$; every point of $\mathcal K_{\mathrm u}$ is a unit.

*Proof.* $\mathcal K_{\mathrm d}$ is the trace on $\mathcal K$ of the closed algebraic null cone, hence closed. On $\mathcal K$ the algebraic norm takes the values determined by the two parameters: in the parametrisation $\Psi$ one has $\langle\Psi(Q_t,W)\rangle_{\natural}=Q_t^2(1+B^2(W))$, which vanishes exactly when $B^2(W)=-1$. With $\lVert W\rVert_E=1$, writing $W=a+ib$ with $a,b\in\mathbb{R}^3$, the conditions $\lVert W\rVert_E=1$ and $B^2(W)=-1$ give $a\cdot b=0$, $|a|^2+|b|^2=1$ and $|a|^2-|b|^2=-1$, hence $a=0$ and $|b|=1$: the set is $\mathbb{C}^{\times}\times(e_t+iS^2)$, of real dimension $4$. An element with $\langle\tilde Q\rangle_{\natural}\neq0$ is not a zero divisor, and being non-zero it is a unit; at the origin the element is neither.

**Corollary (the split is the algebraic partition).** The two strata are exactly the traces on $\mathcal K$ of the three algebraic classes:

$$
\mathcal K_{\mathrm u}=\mathcal K\cap\mathbb{B}^{\times},\qquad
\mathcal K_{\mathrm d}\setminus\{0\}=\mathcal K\cap\mathcal Z,\qquad
\{0\}=\mathcal K\cap\{0\}.
$$

**Remark (the correct refinement).** This is why the sector is refined by the algebraic norm and not by the discriminant. The algebraic norm decides invertibility, and invertibility is the property that the products, the sandwich and the polar decomposition follow; the discriminant decides only the separation of the eigenvalues and is not preserved by the isometry group. §*Why There Is No Spectral Split* of the main article gives the four reasons in full.

## The Doubly Null Stratum

**Theorem (the Peirce lines).** In the parametrisation above the doubly null set is

$$
\mathcal K_{\mathrm d}\setminus\{0\}
=\mathbb{C}^{\times}\cdot(e_t+iS^2)
=\{c(e_t+i\vec u)\ :\ c\in\mathbb{C}^{\times},\ \vec u\in S^2\},
$$

that is, the union of the complex lines $\mathbb{C}(e_t+i\vec u)$. These are exactly the doubly null Peirce lines, whose idempotents, minimal ideals and Peirce decompositions are *Ideals and Peirce Decompositions of the Biquaternion Algebra*. The parametrisation by $(c,\vec u)$ is a bijection, and $\mathcal K_{\mathrm d}\setminus\{0\}$ is homotopy equivalent to $S^1\times S^2$.

*Proof.* The computation of the preceding theorem gives the first equality; the identification with the Peirce lines is the classification of *Ideals and Peirce Decompositions of the Biquaternion Algebra*. Injectivity: $c(e_t+i\vec u)=c'(e_t+i\vec u')$ forces $c=c'$ from the scalar parts and then $\vec u=\vec u'$.

**Theorem (the idempotents).** For $\vec u\in S^2$ the element

$$
\tilde\Pi_{\vec u}=\tfrac12(e_t+i\vec u)
$$

is an idempotent, $\tilde\Pi_{\vec u}^2=\tilde\Pi_{\vec u}$, with complementary idempotent $\tilde\Pi_{-\vec u}=\tfrac12(e_t-i\vec u)$, and

$$
\tilde\Pi_{\vec u}+\tilde\Pi_{-\vec u}=e_t,\qquad
\tilde\Pi_{\vec u}\tilde\Pi_{-\vec u}=0 .
$$

The line $\mathbb{C}(e_t+i\vec u)$ is the line of the idempotent, and it is a minimal left ideal.

*Proof.* $(e_t+i\vec u)^2=e_t+2i\vec u+(i\vec u)^2=e_t+2i\vec u+\vec u^2=2e_t+2i\vec u$, since $\vec u^2=-e_t$; dividing by four gives the idempotent. The complement is computed in the same way, and $(e_t+i\vec u)(e_t-i\vec u)=e_t-\vec u^2=e_t-e_t=0$. The line is a minimal left ideal, by the classification of the doubly null Peirce lines in the cited section.

**Corollary (the algebraic status).** Every non-zero point of $\mathcal K_{\mathrm d}$ is a zero divisor, and the origin is neither a unit nor a zero divisor. The algebraic norm vanishes identically on $\mathcal K_{\mathrm d}$.

**Remark (not the nilpotent cone).** The doubly null set and the nilpotent cone $\{\tilde Q:\tilde Q^2=0\}$ both have real dimension $4$, and they are different cones: $e_t+i\vec e_x$ is doubly null and its square is $2e_t+2i\vec e_x\neq0$, while a non-zero nilpotent has $Q_t=0$ and therefore is not in $\mathcal K$. Their intersection is the origin. The nilpotent cone is the intersection $\mathcal N\cap\mathcal S$ of the algebraic null cone with the spectral-degenerate cone, and the doubly null set is the intersection $\mathcal N\cap\mathcal K$ of the algebraic null cone with the Krein null set; the two intersections are computed from different second conditions.

## The Isotropic Units

**Theorem (the open stratum).** In the parametrisation of §*Geometry*,

$$
\mathcal K_{\mathrm u}=\mathbb{C}^{\times}\cdot\bigl(e_t+(S^5\setminus iS^2)\bigr)
=\{Q_t(e_t+W)\ :\ Q_t\in\mathbb{C}^{\times},\ W\in S^5,\ B^2(W)\neq-1\}.
$$

It is open and dense in $\mathcal K$, connected, of real dimension $7$, and it is a cone with its apex deleted.

*Proof.* The complement of $\mathbb{C}^{\times}\cdot(e_t+iS^2)$ in $\mathbb{C}^{\times}\cdot(e_t+S^5)$ is $\mathbb{C}^{\times}\cdot\bigl(e_t+(S^5\setminus iS^2)\bigr)$. The set $iS^2$ is a $2$-sphere in $S^5$, of real codimension three, so its complement is connected and open; multiplying by $\mathbb{C}^{\times}$ and taking the closure adds the apex. The dimension is $2+5=7$.

**Theorem (the algebraic norm on the stratum).** On $\mathcal K_{\mathrm u}$ the algebraic norm takes every non-zero complex value, and the map

$$
\mathcal K_{\mathrm u}\longrightarrow\mathbb{C}^{\times},\qquad
\tilde Q\longmapsto\langle\tilde Q\rangle_{\natural},
$$

is surjective. On $\mathcal K_{\mathrm d}$ it is identically zero.

*Proof.* For $\tilde Q=c(e_t+\vec e_x)$ with $c\neq0$ one has $\langle\tilde Q\rangle_{\natural*}=|c|^2(1-1)=0$ and $\langle\tilde Q\rangle_{\natural}=2c^2$, which ranges over $\mathbb{C}^{\times}$ as $c$ does. On the doubly null set the norm vanishes by definition.

**Corollary (the two strata are not separated by the metric).** Both strata lie in the single orbit $\mathcal K\setminus\{0\}$ of $\mathrm{U}(1,3)$; the isometry group moves a point of $\mathcal K_{\mathrm d}$ to a point of $\mathcal K_{\mathrm u}$. The stratum is an invariant of the algebra, not of the form.

**Remark (the spectral locus).** The spectral-degenerate cone $\mathcal S=\{B^2=0\}$ meets $\mathcal K$ in the origin together with a real cone of dimension $5$, contained in $\mathcal K_{\mathrm u}$: in the parametrisation, $B^2(W)=0$ on $S^5$ is a set of real dimension $3$, and $\mathbb{C}^{\times}$ adds two. Every non-zero point of that intersection is a unit. Nothing in the Krein split depends on it, and it is recorded only because the inner derivation $\mathrm{ad}_{\tilde Q}$ is nilpotent exactly on $\mathcal S$.

## Multiplication and Inversion

**Theorem (the sector is not closed under multiplication).** The product of two null elements can be positive, negative or null.

*Proof.* Three witnesses.

- **Null times null, positive product.** $e_t+\vec e_x$ and $e_t-\vec e_x$ are null, and $(e_t+\vec e_x)(e_t-\vec e_x)=2e_t$, of value $4$.
- **Null times null, negative product.** $(e_t+\vec e_x)^2=2\vec e_x$, of value $-4$.
- **Null times null, null product.** $e_t+\vec e_x$ and $e_t+i\vec e_x$ are null, and
$$
(e_t+\vec e_x)(e_t+i\vec e_x)=(1-i)e_t+(1+i)\vec e_x,\qquad
\langle\cdot\rangle_{\natural*}=2-2=0.
$$

**Theorem (inversion preserves the null set).** If $\tilde Q$ is a unit then

$$
\langle\tilde Q^{-1}\rangle_{\natural*}=\frac{\langle\tilde Q\rangle_{\natural*}}{\lvert\langle\tilde Q\rangle_{\natural}\rvert^2}.
$$

*Proof.* $\tilde Q^{-1}=(Q_t-\vec Q)/\langle\tilde Q\rangle_{\natural}$, so the scalar part of the inverse is $Q_t/\langle\tilde Q\rangle_{\natural}$ and its vector part is $-\vec Q/\langle\tilde Q\rangle_{\natural}$; the value follows.

**Corollary (the strata under inversion).** The null set is stable under inversion on its units: $\mathcal K_{\mathrm u}$ is closed under inversion. It is not closed under multiplication. The doubly null set is not inversion-stable, its non-zero points being zero divisors. The isotropic units therefore form a **symmetric subset of the unit group**, not a subgroup.

**Remark (the products of the strata).** The doubly null set is a set of zero divisors, so its products with anything are constrained by the algebraic norm: the product of an element of $\mathcal K_{\mathrm d}$ with any element has algebraic norm zero, hence lies in $\mathcal N$. The isotropic units have non-zero algebraic norm, so their products are units. Neither statement uses the Krein norm, and this is the sense in which the algebraic partition is the finer one inside the sector.

## Relation to the Algebraic Partition

**Theorem (the three traces).** The null set meets the algebraic classes exactly as follows:

| | unit | zero divisor | neither |
|---|---|---|---|
| **$\mathcal K_{\mathrm d}$** | none | $\mathcal K_{\mathrm d}\setminus\{0\}$ | the origin |
| **$\mathcal K_{\mathrm u}$** | all | none | none |

The pair of witnesses is $e_t+\vec e_x$, of pair $(0,2)$, and $e_t+i\vec e_x$, of pair $(0,0)$, where the pair is $(\langle\tilde Q\rangle_{\natural*},\langle\tilde Q\rangle_{\natural})$.

**Corollary (the sector straddles the algebraic partition).** The null set is neither contained in the unit group nor in the zero-divisor set: it meets both, and its two strata are exactly the two intersections. The Krein norm alone cannot see the difference, since it vanishes on both; the algebraic norm is the invariant that separates them.

**Remark (the equality case).** The doubly null set is the equality case of the inequality of *K-Regularity and Degeneracy in the Biquaternion Algebra*, §*The degeneracy case: the null set*: an algebraic-null element has non-positive Krein norm, and it is Krein-null exactly on the Peirce lines, together with the origin. So the closed negative half-space $\{\langle\cdot\rangle_{\natural*}\le0\}$ contains the whole zero-divisor set, and the doubly null set is where the two cones touch.

## Comparison with the Regular Sector

| | degenerate sector | regular sector |
|---|---|---|
| condition | $\langle\tilde Q\rangle_{\natural*}=0$ | $\langle\tilde Q\rangle_{\natural*}\neq0$ |
| real dimension | $7$ | $8$ |
| components | one | two |
| smoothness | smooth off the origin, apex at the origin | open submanifold |
| homotopy type | $S^1\times S^5$ up to homotopy | $S^1\uplus S^5$ |
| line $\mathbb{C}\tilde Q$ | totally isotropic | non-degenerate, definite |
| algebraic classes | zero divisors and units | units and zero divisors |
| closed under products | no | no |
| closed under inversion | on the isotropic units | on the units |
| refinement inside | algebraic norm | sign and algebraic norm |

**The two sectors exhaust the algebra.** $\mathbb{B}=\mathcal K\uplus\mathbb{B}^{\natural*}$. The comparison of the algebraic classes is the point of the pair: the regular sector separates units from zero divisors by the sign, and the degenerate sector separates them by the algebraic norm alone.

## Consequences

**Left multiplication.** If $\tilde Q\in\mathcal K_{\mathrm u}$ it is a unit, and $L_{\tilde Q}$ is a bijection of complex rank $4$. If $\tilde Q\in\mathcal K_{\mathrm d}$ is non-zero it is a zero divisor, and $L_{\tilde Q}$ has rank $2$; at the origin it has rank $0$. The rank follows the algebraic norm and not the Krein norm: it is constant on $\mathcal K_{\mathrm u}$ and on each point of $\mathcal K_{\mathrm d}$ it is the algebraic rank, by *The Four General Products and Their Relations over the Biquaternion Algebra*, §*The Annihilators*.

**The sandwich.** The operator $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ is singular exactly on the algebraic null cone, by *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*, §*The Sandwich*. On the null set it is therefore singular exactly on $\mathcal K_{\mathrm d}$, and invertible on $\mathcal K_{\mathrm u}$. This is the sharpest operator reading of the two strata: the sandwich separates them, and it does so through the algebraic norm.

**The polar decomposition.** The modulus–unit decomposition $\tilde Q=\Rho\tilde U$ requires $\Rho^2=\langle\tilde Q\rangle_{\natural}$ with $\Rho\neq0$, so it exists exactly on the unit group. On the null set it therefore exists exactly on $\mathcal K_{\mathrm u}$ and fails on $\mathcal K_{\mathrm d}$; *The Polar Decomposition of a N-Regular Biquaternion*.

**The adjoint.** The Krein adjoint is defined at every point of the sector, the form being non-degenerate; the sector imposes no restriction on it. The operator theory is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*.

**The level set.** The sector is the level set of value zero. It bounds both sign regions of the regular sector, and its projective quotient is the null quadric, the boundary of the complex hyperbolic ball of *The Krein Level Sets and the Hyperbolic Structure*.

## Summary

| question | answer |
|---|---|
| definition | $\mathcal K=\{\langle\tilde Q\rangle_{\natural*}=0\}=\{|Q_t|=\lVert\vec Q\rVert_E\}$ |
| descriptions | totally isotropic line; totally isotropic real plane; every non-zero point has $Q_t\neq0$ |
| geometry | real cone of dimension $7$, smooth off the apex, $\mathcal K\setminus\{0\}\cong\mathbb{C}^{\times}\times S^5$, one orbit of $\mathrm{U}(1,3)$ |
| strata | $\mathcal K_{\mathrm d}$: Peirce lines and the origin, dimension $4$, zero divisors; $\mathcal K_{\mathrm u}$: isotropic units, dimension $7$, open dense |
| doubly null | $c(e_t+i\vec u)$, the idempotents $\tfrac12(e_t+i\vec u)$ and their complements |
| algebraic norm | $0$ on $\mathcal K_{\mathrm d}$; onto $\mathbb{C}^{\times}$ on $\mathcal K_{\mathrm u}$ |
| multiplication | not closed: null times null can be positive, negative or null |
| inversion | preserves the null set, and $\mathcal K_{\mathrm u}$ is inversion-stable |
| operators | rank of left multiplication and the sandwich follow the algebraic norm; the polar decomposition exists exactly on $\mathcal K_{\mathrm u}$ |

The sector is the light cone of the Krein form. It is a single orbit of the isometry group, so the metric structure sees no further subdivision; the only subdivision it admits is algebraic, and it is the split into the Peirce lines and the isotropic units. The doubly null stratum carries the zero divisors and the origin, closed and of dimension four; the isotropic units carry the rest, open and dense and of dimension seven. The Krein norm vanishes on both, and only the algebraic norm tells them apart.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal K$ | the null set, the Krein-degenerate sector |
| $\mathcal K_{\mathrm d}=\mathcal K\cap\mathcal N$ | the doubly null set, the Peirce lines and the origin |
| $\mathcal K_{\mathrm u}=\mathcal K\setminus\mathcal K_{\mathrm d}$ | the isotropic units |
| $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ | the algebraic null cone |
| $\mathcal Z=\mathcal N\setminus\{0\}$ | the zero-divisor set |
| $\langle\tilde Q\rangle_{\natural*}=|Q_t|^2-\lVert\vec Q\rVert_E^2$ | the Krein norm |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the algebraic norm, which decides invertibility |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part |
| $S^5$ | the unit sphere of $\mathbb{C}^3$ |
| $iS^2$ | the set of pure imaginary unit vectors, $B^2=-1$ |
| $\mathbb{C}(e_t+i\vec u)$, $\vec u\in S^2$ | the doubly null Peirce lines |
| $\tilde\Pi_{\vec u}=\tfrac12(e_t+i\vec u)$ | the Hermitian idempotent of the Peirce line |
| $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ | the sandwich |

## Further Reading

- [The K-Regular Sector](the-krein-norm-regular-sector.html), for the positive and negative regions and their geometry.
- [K-Regularity and Degeneracy in the Biquaternion Algebra](krein-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the partition, the line criterion, the Krein cone, the two partitions of the algebra, and the four reasons why no spectral split is available.
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets, the null quadric and the complex hyperbolic ball.
- [The Krein Isometry Group and Its Cartan Decomposition](the-krein-isometry-group-and-its-cartan-decomposition.html), for the group $\mathrm{U}(1,3)$ and its transitive action.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the algebraic norm, the unit group and the zero-divisor cone.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the Peirce idempotents and the minimal left ideals behind the doubly null lines.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the sandwich, the rank of left multiplication and the polar decomposition.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ and its failure at the algebraic null cone.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restriction of the form to the six remarkable subspaces.
