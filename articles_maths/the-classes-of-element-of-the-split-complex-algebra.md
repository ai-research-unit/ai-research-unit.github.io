# __The Classes of Element of the Split-Complex Algebra__

## Introduction

The corpus studies, for each algebraic structure of the twelve, the classes of element singled out by the multiplication: the units and the zero divisors, the idempotents, the nilpotents, the square roots of the three central values $-1$, $0$ and $+1$, and the square roots of a general element. This article is the **hub** of those classes for the split-complex algebra $\mathbb{D}$, the two-dimensional member of the family. It names each class with its pointer, records the inclusions and the disjointness among the classes, and owns the one object that none of the specialised articles carries: the **order cone of squares**.

**The classes and their articles.** The classes are now developed in the articles of the block, one subject per article:

- the units, the norm and the criterion of invertibility are *Norm and Invertibility in the General Split-Complex Algebra*;
- the zero divisors, their two families and the null cone are *Zero Divisors of the Split-Complex Algebra*;
- the annihilators and the multiplication operators are *Annihilators of the Split-Complex Algebra*;
- the roots of $+1$ and the idempotents are *Square Roots of One and the Idempotents of the Split-Complex Algebra*;
- the roots of $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents of the Split-Complex Algebra*;
- the roots of a general element are *Square Roots of a General Element in the Split-Complex Algebra*;
- the ideals, the Peirce decomposition and the radical are *Ideals and Peirce Decomposition of the Split-Complex Algebra*.

This article does not restate the proofs of those articles. It records the **relations among the classes**, which no single article owns, and the order cone of squares, which is the image of the square map and the order that the algebra carries.

**The results.** The elements of $\mathbb{D}$ fall into the three disjoint classes: the units, the zero element, and the zero divisors. The idempotents are the four elements $0,1,\Pi_{+},\Pi_{-}$; the nontrivial ones are the primitive zero divisors, and $0$ is an idempotent but not a zero divisor. There are no nonzero nilpotents, so the nilpotent class is empty; the square-zero elements are exactly $\{0\}$, which is the root of $0$ and is not a nilpotent under the corpus convention. The roots of $+1$ are the four elements $\pm1,\pm j$, all units; the roots of $-1$ are empty; the roots of a general element exist exactly on the forward cone $\mathcal{C}=\{q\ge|q'|\}$, with four, two, one or no roots according to the position in the cone. The forward cone is a pointed closed convex cone, the image of the square map, and the order it defines is compatible with addition and with multiplication by elements of the cone.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[j]$, $j^{2}=+1$, with basis $1,j$, general element $Q=q+jq'$, conjugate $\bar Q=q-jq'$, idempotents $\Pi_{\pm}=\tfrac12(1\pm j)$, and idempotent coordinates $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ with $Q_{\pm}=q\pm q'$. The algebraic norm of the plain product is $\langle Q\rangle=Q^{2}$; the algebraic norm of the sesquilinear product is $\langle Q\rangle_{*}=Q\bar Q=q^{2}-q'^{2}$. The **null cone** is $\mathcal{N}=\{\langle Q\rangle_{*}=0\}=\mathbb{R}\Pi_{+}\cup\mathbb{R}\Pi_{-}$, and the **zero-divisor set** is $\mathcal{Z}=\mathcal{N}\setminus\{0\}$.

## The Classes and Their Articles

**The classes are organised by the equation that defines them and by the article that owns them; the table is the index of the block.**

| class | defining equation or condition | set in $\mathbb{D}$ | article |
|---|---|---|---|
| units | $QB=1$ soluble | $\{Q_{+}Q_{-}\neq0\}$ | *Norm and Invertibility in the General Split-Complex Algebra* |
| zero divisors | $Q\neq0$, $QB=0$ with $B\neq0$ | $\mathbb{R}^{\times}\Pi_{+}\cup\mathbb{R}^{\times}\Pi_{-}$ | *Zero Divisors of the Split-Complex Algebra* |
| annihilators | $\{B:QB=0\}$ | $\{0\}$ off $\mathcal{N}$, the opposite line on $\mathcal{N}\setminus\{0\}$, and $\mathbb{D}$ at $0$ | *Annihilators of the Split-Complex Algebra* |
| idempotents | $\Pi^{2}=\Pi$ | $\{0,1,\Pi_{+},\Pi_{-}\}$ | *Square Roots of One and the Idempotents of the Split-Complex Algebra* |
| roots of $+1$ | $\Xi^{2}=1$ | $\{1,-1,j,-j\}$ | *Square Roots of One and the Idempotents of the Split-Complex Algebra* |
| roots of $0$ | $\Xi^{2}=0$ | $\{0\}$ | *Square Roots of Zero and the Nilpotents of the Split-Complex Algebra* |
| nilpotents | $\Upsilon\neq0$, $\Upsilon^{n}=0$ | $\varnothing$ | *Square Roots of Zero and the Nilpotents of the Split-Complex Algebra* |
| roots of $-1$ | $\Xi^{2}=-1$ | $\varnothing$ | *Square Roots of One and the Idempotents of the Split-Complex Algebra* |
| roots of a general $Q$ | $\Xi^{2}=Q$ | $\varepsilon_{+}\sqrt{Q_{+}}\Pi_{+}+\varepsilon_{-}\sqrt{Q_{-}}\Pi_{-}$ over the real signs; nonempty exactly when $Q_{+},Q_{-}\ge0$ | *Square Roots of a General Element in the Split-Complex Algebra* |
| ideals | additive subgroups closed under multiplication | $0$, $\mathbb{R}\Pi_{+}$, $\mathbb{R}\Pi_{-}$, $\mathbb{D}$ | *Ideals and Peirce Decomposition of the Split-Complex Algebra* |

## The Inclusions and the Disjointness

**The units, the zero element and the zero divisors are the three disjoint classes of the plain product; the idempotents meet the zero divisors in the two nontrivial idempotents and meet the units in $1$; the nilpotents are empty; the roots of $+1$ are units; the roots of $0$ are the origin.**

### The Partition by Invertibility

For $Q\in\mathbb{D}$ exactly one of the following holds:

1. $Q$ is a unit: $Q_{+}Q_{-}\neq0$;
2. $Q=0$;
3. $Q$ is a zero divisor: $Q_{+}Q_{-}=0$ and $Q\neq0$.

**Proof.** This is the three-way classification of *Norm and Invertibility in the General Split-Complex Algebra*, read in the idempotent coordinates.

So the units and the zero divisors do not meet, and the origin is neither. The non-units are the origin and the zero divisors; they do not form an ideal, because $\Pi_{+}+\Pi_{-}=1$.

### The Idempotents

The idempotents are $0,1,\Pi_{+},\Pi_{-}$. Their intersections with the three classes are:

- $1$ is a unit;
- $0$ is the zero element;
- $\Pi_{+}$ and $\Pi_{-}$ are zero divisors.

The two nontrivial idempotents are the **primitive** zero divisors: every zero divisor is a nonzero real multiple of one of them. The origin is an idempotent, because $0^{2}=0$, and it is not a zero divisor, because the definition excludes it.

### The Nilpotents and the Square-Zero Elements

There are **no nonzero nilpotents**. The square-zero elements are exactly $\{0\}$. Under the corpus convention the nilpotent is a nonzero element, so the nilpotent set is empty and $0$ is a square-zero element but not a nilpotent. The two notions are kept separate in *Square Roots of Zero and the Nilpotents of the Split-Complex Algebra*.

### The Roots of the Central Values

The roots of $+1$ are the four elements $\pm1,\pm j$, all units; the roots of $0$ are the origin; the roots of $-1$ are empty. The three sets are pairwise disjoint, and their cardinalities are $4,1,0$. The roots of $+1$ form the group $(\mathbb{Z}/2\mathbb{Z})^{2}$; the root of $0$ is fixed by the conjugation; the empty set is the whole answer for $-1$.

### The General Roots

The roots of $\Xi^{2}=Q$ exist exactly on the forward cone

$$
\mathcal{C}=\{Q:Q_{+}\ge0,\ Q_{-}\ge0\}=\{Q:q\ge|q'|\}.
$$

On the interior of the cone there are four roots; on the boundary minus the origin there are two; at the origin there is one; outside there are none. A root of a unit is a unit, a root of a nonzero zero divisor is a zero divisor, and the root of $0$ is $0$. The classification is *Square Roots of a General Element in the Split-Complex Algebra*.

### The Two Algebraic Norms and the Classes

The two algebraic norms see different classes, and the difference is the source of the three-way classification.

| norm | value | vanishing set | class it decides |
|---|---|---|---|
| $\langle Q\rangle=Q^{2}$ | $\mathbb{D}$-valued | $\{0\}$ | none; it does not decide invertibility |
| $\langle Q\rangle_{*}=Q\bar Q$ | real, signature $(1,1)$ | $\mathcal{N}=\mathbb{R}\Pi_{+}\cup\mathbb{R}\Pi_{-}$ | the units (value $\neq0$) and the null cone (value $0$); the zero divisors are the punctured cone |

The first norm is anisotropic and sees only the origin; the second is indefinite and sees the null cone. The zero divisors are $\mathcal{N}\setminus\{0\}$, the units are the complement of $\mathcal{N}$, and the origin is the only element that lies on neither side of the dichotomy.

## The Order Cone of Squares

**The image of the square map is the forward cone $\mathcal{C}=\{Q:Q_{+}\ge0,Q_{-}\ge0\}=\{Q:q\ge|q'|\}$, a pointed closed convex cone; it defines a partial order on $\mathbb{D}$ compatible with addition and with multiplication by elements of the cone, and a radicand has a square root exactly when it lies in $\mathcal{C}$.**

### The Image of the Square

For $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ one has

$$
Q^{2}=Q_{+}^{2}\Pi_{+}+Q_{-}^{2}\Pi_{-}.
$$

The two coordinates of a square are squares of real numbers, hence non-negative, and every non-negative pair is attained by choosing $Q_{\pm}=\pm\sqrt{\cdot}$. Therefore

$$
\operatorname{Im}(\square)=\{Q:Q_{+}\ge0,\ Q_{-}\ge0\}.
$$

In the basis $1,j$ the inequalities are $q+q'\ge0$ and $q-q'\ge0$, that is

$$
q\ge|q'| .
$$

The set is the closed cone of angle $90^{\circ}$ between the two null lines $\mathbb{R}\Pi_{+}$ and $\mathbb{R}\Pi_{-}$, containing the positive real axis. It is the **forward cone** of the split-complex plane.

### The Cone Is Pointed, Convex and Closed

**Proposition.** The set $\mathcal{C}$ is a closed convex cone with apex $0$, and it is **pointed**: $\mathcal{C}\cap(-\mathcal{C})=\{0\}$.

**Proof.** It is the image of the closed positive quadrant $\mathbb{R}_{\ge0}^{2}$ under the linear isomorphism $Q\mapsto(Q_{+},Q_{-})$, hence closed and convex; it is invariant under multiplication by non-negative scalars, hence a cone. A point in $\mathcal{C}\cap(-\mathcal{C})$ has both coordinates non-negative and non-positive, hence both zero.

The cone is **not** the whole plane and **not** a half-plane: it has nonempty interior, the set $q>|q'|$, and two boundary rays, the non-negative halves of the two null lines.

### The Order

The cone defines a partial order on $\mathbb{D}$ by

$$
Q\succeq B\iff Q-B\in\mathcal{C}\iff Q_{+}\ge B_{+}\text{ and }Q_{-}\ge B_{-}.
$$

**Proposition.** The relation $\preceq$ is a partial order, it is compatible with addition, and it is compatible with multiplication by non-negative real scalars. It is also compatible with multiplication by elements of $\mathcal{C}$: if $Q\succeq Q'$ and $B\succeq0$ then $QB\succeq Q'B$.

**Proof.** The order is the componentwise order of $\mathbb{R}^{2}$ transported by the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$, so the first two properties are the componentwise order of the plane. For the third, the idempotent coordinates of a product are the products of the coordinates, and the product of two non-negative reals is non-negative.

The order is not total: $\Pi_{+}$ and $\Pi_{-}$ are incomparable, since their difference $j$ has coordinates $(1,-1)$ and neither $j$ nor $-j$ lies in $\mathcal{C}$.

### The Square and the Order

**Proposition.** The square map is monotone on $\mathcal{C}$: if $0\preceq Q\preceq B$ then $Q^{2}\preceq B^{2}$.

**Proof.** In the idempotent coordinates, $0\le Q_{\pm}\le B_{\pm}$ gives $Q_{\pm}^{2}\le B_{\pm}^{2}$.

**Corollary.** A radicand $Q$ has a square root exactly when $Q\succeq0$; the square root is unique in $\mathcal{C}$, namely $\sqrt{Q_{+}}\,\Pi_{+}+\sqrt{Q_{-}}\,\Pi_{-}$, and the four roots of an interior radicand are the independent sign choices in the two idempotent coordinates.

The order cone is therefore the exact domain of the square-root problem: the forward cone is the image of the square, the set of radicands that have a root, and the order that the algebra carries. The boundary of the cone is the non-negative part of the null cone of the zero divisors, and the interior is the set of units that are squares.

### The Order and the Classes

| region of $\mathbb{D}$ | condition | class |
|---|---|---|
| interior of $\mathcal{C}$ | $q>|q'|$ | units that are squares; four roots |
| boundary minus $0$ | $q=|q'|\neq0$ | zero divisors; two roots |
| apex | $q=q'=0$ | the zero element; one root |
| complement of $\mathcal{C}$ | $q<|q'|$ | no root; the units off the negative null rays, and the zero divisors on them |

The complement contains the **backward cone** $- \mathcal{C}=\{q\le-|q'|\}$ away from the apex, whose interior points are units with no square root and whose boundary, the two negative null rays, are zero divisors; the two side sectors between the cones contain units and no zero divisors.

## The Three Central Values Compared

**The central values $-1,0,+1$ have $0,1,4$ roots; the pattern is the pattern of the sign of the scalar, and the value $-1$ is the one that the split sign removes.**

| $\lambda$ | equation | roots | number |
|---|---|---|---|
| $-1$ | $\Xi^{2}=-1$ | none | $0$ |
| $0$ | $\Xi^{2}=0$ | $0$ | $1$ |
| $+1$ | $\Xi^{2}=1$ | $1,-1,j,-j$ | $4$ |

The value $+1$ has the four roots because the non-central unit $j$ is a root of $+1$; the value $-1$ has none because a sum of two real squares is non-negative; the value $0$ has the single root $0$ because the algebra is reduced. The three sets are disjoint, and their cardinalities are the three values $4,1,0$.

## Summary

The classes of element of the split-complex algebra are indexed by the articles of the block: the units and the criterion of invertibility by the general norm article, the plain norm by the other, the annihilators by the annihilator article, the roots and the idempotents by the two central-value articles, the general roots by the square-root article, and the ideals by the Peirce article. The units, the zero element and the zero divisors are the three disjoint classes of the plain product; the idempotents are $0,1,\Pi_{+},\Pi_{-}$, with the two nontrivial ones the primitive zero divisors; there are no nonzero nilpotents and the square-zero elements are $\{0\}$; the roots of $+1$ are the four units $\pm1,\pm j$; the roots of $-1$ are empty.

The order cone of squares is the forward cone

$$
\mathcal{C}=\{Q:Q_{+}\ge0,Q_{-}\ge0\}=\{Q:q\ge|q'|\},
$$

the image of the square map, a pointed closed convex cone. It defines the componentwise partial order of the algebra, compatible with addition and with multiplication by elements of the cone, and it is the exact domain of the square-root problem: four roots in its interior, two on its boundary minus the apex, one at the apex, none outside. Its boundary is the non-negative part of the null cone of the zero divisors, and its interior is the set of units that are squares.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Q=q+jq'$ | General split complex number |
| $Q_{\pm}=q\pm q'$ | Idempotent coordinates |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | Idempotents |
| $\mathcal{N}=\mathbb{R}\Pi_{+}\cup\mathbb{R}\Pi_{-}$ | Null cone |
| $\mathcal{Z}=\mathcal{N}\setminus\{0\}$ | Zero-divisor set |
| $\mathcal{C}=\{Q:Q_{+}\ge0,Q_{-}\ge0\}=\{q\ge|q'|\}$ | Forward cone, the image of the square |
| $Q\succeq B\iff Q-B\in\mathcal{C}$ | The order of the forward cone |
| $\Xi_{\pm}=\pm\sqrt{Q_{\pm}}$ | The roots in the interior of $\mathcal{C}$ |

## Further Reading

- [Norm and Invertibility in the Split-Complex Algebra](norm-and-invertibility-in-the-split-complex-algebra.html), for the plain algebraic norm, which sees only the origin.
- [Norm and Invertibility in the General Split-Complex Algebra](norm-and-invertibility-in-the-general-split-complex-algebra.html), for the criterion of invertibility and the three-way classification.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the null cone and its two families.
- [Annihilators of the Split-Complex Algebra](annihilators-of-the-split-complex-algebra.html), for the annihilator of a class.
- [Square Roots of One and the Idempotents of the Split-Complex Algebra](square-roots-of-one-and-the-idempotents-of-the-split-complex-algebra.html), for the roots of $+1$ and the four idempotents.
- [Square Roots of Zero and the Nilpotents of the Split-Complex Algebra](square-roots-of-zero-and-the-nilpotents-of-the-split-complex-algebra.html), for the roots of $0$ and the absence of nilpotents.
- [Square Roots of a General Element in the Split-Complex Algebra](square-roots-of-a-general-element-in-the-split-complex-algebra.html), for the full classification of the roots.
- [Ideals and Peirce Decomposition of the Split-Complex Algebra](ideals-and-peirce-decomposition-of-the-split-complex-algebra.html), for the ideals and the radical.
