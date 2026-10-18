# __The Classes of Element of the Split-Complex Algebra__

## Introduction

The corpus studies, for each algebraic structure of the twelve, the classes of element singled out by the multiplication: the zero divisors, the idempotents, the nilpotents, the square roots of the three central values $-1$, $0$ and $+1$, and the square roots of a general element. This article is the **hub** of those classes for the split-complex algebra $\mathbb{D}$, the two-dimensional member of the family. It names the classes owned by other articles with their pointers, and it owns the three that no other article of the category carries: the **nilpotents**, the **square roots of the three central values**, and the **square roots of a general element**, together with the **square-zero elements** and the **order cone of squares**.

The results are the two-dimensional end of the family, and the reductions are short because $\mathbb{D}$ is commutative and reduced. The nilpotent class is the smallest possible, the single element $0$: the algebra is reduced, although it is not a field. The three central values split sharply: $+1$ has four square roots, the two scalars $\pm 1$ and the two non-scalars $\pm j$, the value $0$ has the single root $0$, and the value $-1$ has **none**, since a sum of two real squares cannot be negative. The square roots of a general element exist exactly on the forward cone $a \ge \lvert a'\rvert$, the image of the squaring map, whose boundary is the null cone of the zero divisors. Each of these is against the complex field, where $+1$ has two roots, $-1$ has two, and every nonzero element has two roots.

**Placement.** The article is the second entry of the split-complex general-plain-algebra block, after *Split-Complex Norm and Invertibility* and before *Split-Complex Zero Divisors*; it opens the classes of element, as the corresponding articles do in the other blocks. The definitions of a nilpotent, of the index of nilpotency and of a square-zero element are the standard ones; the norm, its sign, the criterion of invertibility and the group of units are *Split-Complex Norm and Invertibility*.

**The classes owned elsewhere.** Three of the six classes are the subject of articles of this category, and this article names them without restating them. The **zero divisors** are *Split-Complex Zero Divisors*, below this article in this category; their criterion is $A_+A_- = 0$, and their set is the null cone $\mathcal{N} = \{a^2 = a'^2\}$ with the origin removed. The **idempotents** are *Split-Complex Idempotents and Projections*, below this article in this category; there are exactly four, the two trivial ones $0$ and $1$ and the two nontrivial ones $\Pi_{1,2} = \tfrac12(1\pm j)$. The **ideals and the Peirce decomposition** are *Split-Complex Ideals and Peirce Decomposition*, below this article in this category. The ring property behind all of the classes is *The Specificities of the Split-Complex Algebra*, below this article in this category.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, with basis $1$, $j$, $j^2 = +1$, general element $A = a+ja'$ with $a = \operatorname{Re}A$ and $a' = \operatorname{Im}A$, conjugate $\bar A = a-ja'$, idempotents $\Pi_{1,2} = \tfrac12(1\pm j)$ and idempotent coordinates $A = A_+\Pi_1 + A_-\Pi_2$ with $A_\pm = a\pm a'$. The **involution** is the bar $\overline{\cdot}$: the idempotent swap coincides with it; where an article of the category says "the involution" it means $\overline{\cdot}$, and no article of this block uses the word for another map.

## The Nilpotents

**Definition.** An element $A \in \mathbb{D}$ is **nilpotent** if $A^n = 0$ for some integer $n \ge 1$; the **index of nilpotency** is the least such $n$. An element is **square-zero** if $A^2 = 0$. By the corpus convention the definition includes $0$, whose index is $1$; the article speaks of the nonzero nilpotents when it excludes it.

**Theorem.** The only nilpotent of $\mathbb{D}$ is $0$. The algebra is **reduced**.

**Proof.** Write $A = A_+\Pi_1 + A_-\Pi_2$. Since multiplication is componentwise in the idempotent basis, $A^n = A_+^n\Pi_1 + A_-^n\Pi_2$ for every $n \ge 1$. Thus $A^n = 0$ holds if and only if $A_+^n = 0$ and $A_-^n = 0$, and the field $\mathbb{R}$ has no nonzero nilpotent, so $A_+ = A_- = 0$ and $A = 0$.

So no nonzero nilpotent exists at any index, and in particular the only square-zero element is $0$, as the section below records. The mechanism is visible in the idempotent coordinates: a power raises each coordinate to the same power, and a real number raised to a positive power vanishes only when it is itself zero.

This is the first place where the split-complex algebra is *simpler* than the higher-dimensional members of the family: it has no nilpotent cone at all, because $\mathbb{D}$ has only the two central idempotents and no off-diagonal unit, so there is nothing to square to zero. The zero divisors of $\mathbb{D}$, which are $\mathbb{R}^\times\Pi_1\cup\mathbb{R}^\times\Pi_2$, are idempotent and not nilpotent: the primitive zero divisors satisfy $\Pi_{1,2}^2 = \Pi_{1,2}$. No element of $\mathbb{D}$ is both idempotent and a nonzero nilpotent, since a nilpotent power that stabilises must vanish.

The nilpotent class being $\{0\}$ is the statement that $\mathbb{D}$ is reduced, proved in *Split-Complex Ideals and Peirce Decomposition* as the vanishing of the nilradical, and it is the reason the algebra behaves as a product of two fields rather than as a local ring. The dual-number algebra $\mathbb{R}[\varepsilon]/(\varepsilon^2)$, by contrast, has the nonzero nilpotent $\varepsilon$, and its idempotents are only the trivial ones; the split-complex algebra has the opposite defect, an abundance of idempotents and no nilpotent.

## The Square Roots of Minus One, Zero and Plus One

The three central values are the three elements $-1$, $0$ and $+1$ of the real line inside $\mathbb{D}$. The problem is the system $X^2 = \lambda$ for $\lambda$ one of them, and it reduces to the plane because the squaring of a split-complex number acts coordinate by coordinate.

**Reduction.** Write $X = X_+\Pi_1 + X_-\Pi_2$. Then

$$
X^2 = X_+^2\Pi_1 + X_-^2\Pi_2 ,
$$

so for a real $\lambda$ the equation $X^2 = \lambda$ is equivalent to the two real equations

$$
X_+^2 = \lambda, \qquad X_-^2 = \lambda .
$$

The three cases differ only in which of these two equations is solvable, because a real number has a real square root exactly when it is non-negative, and then two unless it is zero.

### The Roots of Plus One

**Theorem.** The equation $X^2 = 1$ has exactly four solutions in $\mathbb{D}$:

$$
X \in \{1, -1, j, -j\} = \{\pm 1, \pm j\}.
$$

**Proof.** By the reduction, $X_+^2 = 1$ and $X_-^2 = 1$, so $X_+ = \pm 1$ and $X_- = \pm 1$, four combinations. In the basis $\{1, j\}$ the combinations are $\Pi_1+\Pi_2 = 1$, $-\Pi_1-\Pi_2 = -1$, $\Pi_1-\Pi_2 = j$ and $-\Pi_1+\Pi_2 = -j$.

Two of the four roots, $\pm 1$, are scalar; the other two, $\pm j$, are **non-scalar**, and $j$ is the **hyperbolic unit**: the generator itself, with $j^2 = +1$. This is the sharpest difference from the complex field, where the equation $X^2 = 1$ has only the two scalar roots $\pm 1$ and the non-scalar unit $i$ of the field is instead a root of $-1$. On $\mathbb{D}$ the non-scalar unit solves the equation that on $\mathbb{C}$ is solved by the scalars alone.

Note that $\mathbb{D}$ is commutative, so every element of $\mathbb{D}$ is central, and the words "scalar" and "non-scalar" distinguish $\mathbb{R}$ inside $\mathbb{D}$ and not the centre, which is all of $\mathbb{D}$. Here the only distinction available is scalar against non-scalar.

### The Roots of Zero

**Theorem.** The equation $X^2 = 0$ has exactly one solution, $X = 0$.

**Proof.** By the reduction, $X_+^2 = 0$ and $X_-^2 = 0$, so $X_+ = X_- = 0$ and $X = 0$.

So the square-zero elements of the plain product form the single point $\{0\}$, in agreement with the nilpotent theorem, and the root of $0$ is not a whole cone. The square-zero elements of the plain product are one thing; the square-zero elements of the *other* product carried by the space are another, and the difference is recorded in the section below.

### The Roots of Minus One

**Theorem.** The equation $X^2 = -1$ has **no** solution in $\mathbb{D}$.

**Proof.** By the reduction, $X_+^2 = -1$ and $X_-^2 = -1$; a square of a real number is non-negative, so neither equation can hold.

The absence is not accidental and it is total: there is no split-complex number whose square is $-1$, scalar or not. Since $\mathbb{D}$ is commutative the notion of a non-central root does not even arise, and the contrast with $\mathbb{C}$ is at the level of the value, not of the position of the root: $\mathbb{C}$ has the two roots $\pm i$ of $-1$, and $\mathbb{D}$ has none. In idempotent coordinates the reason is a single line: a square $X_+^2\Pi_1 + X_-^2\Pi_2$ has both coordinates non-negative, so its real part is non-negative, and $-1$ has real part $-1$.

The three sets are therefore entirely different in size, and they are collected in the next table.

### The Three Sets Compared

| value $\lambda$ | roots in $\mathbb{R}$ | roots in $\mathbb{C}$ | roots in $\mathbb{D}$ |
|---|---|---|---|
| $+1$ | $\pm 1$ | $\pm 1$ | $\pm 1$, $\pm j$ (four) |
| $0$ | $0$ | $0$ | $0$ (one) |
| $-1$ | none | $\pm i$ | none |

The linear algebra of the three rows reads off the sign of the square function on the base field: over $\mathbb{R}$ the values $+1$ and $0$ are reached and $-1$ is not; over $\mathbb{C}$ all three are reached; over $\mathbb{D}$ the reachable set is the same as over $\mathbb{R}$ for these three values, but the *number* of roots changes, because the two idempotent coordinates double the count whenever both are nonzero. The value $+1$ is the only one of the three with a non-scalar root, and it is the reason the ring has four square roots of its unity. The roots of $+1$ are invertible, of norm $\langle \pm 1\rangle_{\natural} = 1$ and $\langle \pm j\rangle_{\natural} = -1$; the root of $0$ is not a unit, and the empty set of roots of $-1$ needs no comment.

## The Square Roots of a General Element

### The Criterion

**Theorem.** An element $A \in \mathbb{D}$ has a square root in $\mathbb{D}$ if and only if both idempotent coordinates are non-negative, $A_+ \ge 0$ and $A_- \ge 0$. When it exists, the root is unique if $A = 0$, two-to-one if exactly one coordinate is zero, and four-to-one if both coordinates are positive.

**Proof.** The equation $X^2 = A$ is, by the reduction of the section above, the pair $X_+^2 = A_+$ and $X_-^2 = A_-$. Each real equation $X_\pm^2 = A_\pm$ has a real solution exactly when $A_\pm \ge 0$, and then it has one solution if $A_\pm = 0$ and two if $A_\pm > 0$. Multiplying the counts over the two independent coordinates gives the four cases.

So the elements with a square root are exactly those of the **forward cone**

$$
\mathcal{C} = \{A : A_+ \ge 0,\; A_- \ge 0\} = \{A = a+ja' : a \ge \lvert a'\rvert\},
$$

the set of elements whose two idempotent coordinates are non-negative, equivalently the set on which the real part dominates the split-imaginary part in absolute value. Off that cone the square root does not exist, and the failure is total: no root, not a real root only. The four roots of a general element of the interior are $\pm X_+^{1/2}\Pi_1 \pm X_-^{1/2}\Pi_2$, with the two signs independent.

The count is again the opposite of the complex case. In $\mathbb{C}$ every nonzero element has exactly two square roots and $0$ has one, a dichotomy with no exceptional elements; in $\mathbb{D}$ an element has none, one, two or four roots, and the failure set is a cone of positive area. The difference is the idempotent decomposition: the two coordinates of a square are squares of the two coordinates, so solvability is imposed coordinate by coordinate, and the constraint is the conjunction of two inequalities rather than a single non-vanishing.

### The Order Cone of Squares

The set of squares of the elements of $\mathbb{D}$, the image of the map $A \mapsto A^2$, is the set of elements of the form $X_+^2\Pi_1 + X_-^2\Pi_2$, which is exactly the forward cone $\mathcal{C}$ of the criterion: the criterion says that an element has a square root precisely when it lies in $\mathcal{C}$, and the constructive half of its proof exhibits the root, so the image and $\mathcal{C}$ coincide. The **cone of squares** is therefore $\mathcal{C}$, the same set as the solvability cone.

**Proposition.** The cone $\mathcal{C}$ is a pointed convex cone: it is closed under addition and under multiplication by non-negative reals, it contains $0$, and $\mathcal{C}\cap(-\mathcal{C}) = \{0\}$. It therefore defines a partial order on $\mathbb{D}$ by $A \preceq C \iff C - A \in \mathcal{C}$.

**Proof.** The idempotent coordinates of $\lambda A + \mu C$ are $\lambda A_\pm + \mu C_\pm$; a non-negative combination of non-negative numbers is non-negative, which gives closure under addition and under non-negative scaling, and $0$ has both coordinates $0$. If $A$ and $-A$ both lie in $\mathcal{C}$, then $A_\pm \ge 0$ and $-A_\pm \ge 0$, so $A_\pm = 0$ and $A = 0$, and the cone is pointed. The order axioms follow from the three closure properties.

The relation of the cone of squares to the null cone is a boundary relation. The null cone of *Split-Complex Zero Divisors*, below this article in this category, is the union of the two lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$; its non-negative half is the boundary of the cone of squares,

$$
\partial\mathcal{C} = \mathbb{R}_{\ge 0}\Pi_1 \cup \mathbb{R}_{\ge 0}\Pi_2 \subset \mathcal{N},
$$

the two rays of the null cone on which the idempotent coordinates are non-negative, and the zero divisors are that boundary with the origin removed. So the cone of squares and the null cone meet along two rays, and the interior of the cone of squares is the set of elements whose square roots number four.

This is the algebraic core of the order on $\mathbb{D}$; its reading as a positivity cone, its two components when the sign of the norm is allowed to vary, and the reversed inequality that holds on it are *The Hermitian Form and the Cone of the Split-Complexoid Algebra*, below this article in this category. The forward cone is the single component of the double cone $a^2 \ge a'^2$ that contains $1$; the other component is $-\mathcal{C}$, and the two are exchanged by negation.

## The Square-Zero Elements

**Definition.** An element is **square-zero** with respect to a named product if its square in that product is $0$. For the plain product $AC$ the square of $A$ is $A^2$, and the square-zero set is the set of roots of $0$.

**Proposition.** The square-zero elements of the plain product are exactly $\{0\}$.

**Proof.** This is the theorem on the roots of $0$ above, and it agrees with the nilpotent theorem: a square-zero element is a nilpotent of index two, and the only nilpotent of $\mathbb{D}$ is $0$.

The statement is worth separating from its complex analogue precisely because it is *not* the end of the matter. In $\mathbb{C}$ the square-zero elements are also only $0$, and it is easy to think that this is all a field can say; but in $\mathbb{D}$ the second product $A \star C = A\bar C$ carried by the same space has a different square, $A \star A = A\bar A = \langle A\rangle_{\natural}$, so its square-zero elements are the elements of vanishing norm, that is the whole null cone of zero divisors. The square-zero set of the plain product is a point; the square-zero set of the sesquilinear product is the pair of null lines. The comparison is drawn in *Relations and Comparison Between the Two Products of the Split-Complexoid Space*, above this article in this category.

## Summary

The classes of element of $\mathbb{D}$ fall into six families. Three are owned by articles of this category: the zero divisors (*Split-Complex Zero Divisors*), of criterion $A_+A_- = 0$, the idempotents (*Split-Complex Idempotents and Projections*), of which there are four, and the ideals with the Peirce decomposition (*Split-Complex Ideals and Peirce Decomposition*). Three are owned here.

The nilpotents, and with them the square-zero elements of the plain product: the algebra is reduced, $0$ is the only nilpotent of any index, and $\{0\}$ is the only square-zero element of the plain product. The square roots of the three central values: $X^2 = 1$ has the four roots $\pm 1$ and $\pm j$, with $j$ the non-scalar root; $X^2 = 0$ has the single root $0$; and $X^2 = -1$ has no root at all, since a split square has non-negative real part. The square roots of a general element: they exist exactly on the forward cone $\mathcal{C} = \{A_+ \ge 0, A_- \ge 0\} = \{a \ge \lvert a'\rvert\}$, the cone of squares, where they number one, two or four according to how many coordinates vanish; the cone is pointed and convex and defines the order on $\mathbb{D}$, and its boundary is the two non-negative rays of the null cone.

Each class is read against the two neighbours. Against $\mathbb{C}$, the multiplicatively simple case, the algebra keeps the trivial nilpotents and square-zero set but gains two nontrivial idempotents, a null cone of zero divisors, four roots of $+1$ and none of $-1$. The split-complex algebra is the minimal one in which the phenomenon of the family appears without non-commutativity: the zero divisors and the idempotents are present, while the nilpotents and the square-zero elements of the plain product are not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$ | Split-complex algebra |
| $A = a + ja'$ | General split-complex number |
| $\bar A = a - ja'$ | Conjugation, the only involution here |
| $\Pi_{1,2} = \tfrac12(1\pm j)$ | Idempotents |
| $A_\pm = a\pm a'$ | Idempotent coordinates, $A = A_+\Pi_1 + A_-\Pi_2$ |
| $\mathcal{N} = \{a^2 = a'^2\}$ | Null cone, the zero divisors with the origin removed |
| $\mathcal{C} = \{A_+ \ge 0, A_- \ge 0\} = \{a \ge \lvert a'\rvert\}$ | Forward cone, the cone of squares, the solvability cone of square roots |
| $X^2 = \lambda$ | Roots of a central value; $\lambda = 1$ gives $\{\pm 1,\pm j\}$, $\lambda = 0$ gives $\{0\}$, $\lambda = -1$ gives $\varnothing$ |
| index of nilpotency | Least $n$ with $A^n = 0$; the only nilpotent here is $0$ |
| square-zero | $A^2 = 0$ for the plain product; $\{0\}$ here, the null cone for the sesquilinear product |

## Further Reading

- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for nilpotents, reduced rings and the multiplicative vocabulary of a ring.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex numbers as a Clifford algebra and the roots of $\pm 1$.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for quadratic forms, squares and the order cones they define.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex plane, its idempotents and its null directions.
