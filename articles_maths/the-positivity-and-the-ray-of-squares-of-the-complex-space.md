# __The Positivity and the Ray of Squares of the Complex Space__

## Introduction

Positivity is the choice of a cone. On the complex space the cone of Hermitian squares is the ray of the non-negative reals, and it is the smallest cone any non-trivial positivity can give. A ray is a cone of dimension one: it is closed under addition, closed under the multiplication of the algebra, closed under inversion, and it is its own boundary.

The article defines the cone, proves that it is the ray, explains why the rank of the algebra forces the collapse, reads the order it induces, states what positivity adds beyond the definiteness of the Hermitian form, and compares the count with the split-complex algebra, where the set of Hermitian squares is the real line and the set of elements with non-negative Hermitian square is a double cone.

The definiteness of the forms is *The Two Forms and the Two Algebraic Norms of the Complex Space*; the Hermitian square of an element is *The Classes of Element of the Complex Algebra*; the field property that makes the order of the algebra incompatible with its multiplication is *The Specificities of the Complex Algebra*; the triple whose quadratic representation is the norm is *The Ternary Product and the Associator of the Complex Space*.

**Interpretation.** The element is $Q=q+iq'$ with real coordinates, the conjugation is the bar, and the Hermitian form is $H(Q_1,Q_2)=Q_1\bar Q_2$ with norm $H(Q)=Q\bar Q$. The **self-adjoint part** of the algebra is the set of fixed elements of the conjugation, which is the real line; the **Hermitian square** of $Q$ is $Q\bar Q$. A cone here is a subset closed under addition and under multiplication by non-negative real scalars.

## The Cone of Squares

**Definition.** The **cone of squares** of the algebra is

$$
\mathcal{C}=\Bigl\{\sum_{k=1}^{n}Q_k\bar Q_k : n\ge1,\; Q_k\in\mathbb{C}\Bigr\},
$$

the set of finite sums of Hermitian squares.

**Theorem.** $\mathcal{C}=[0,\infty)$, the ray of the non-negative reals.

*Proof.* Each term $Q_k\bar Q_k=q_k^{2}+(q'_k)^{2}$ is a non-negative real, so a finite sum of them is a non-negative real, and the ray contains $\mathcal{C}$. Conversely a real $r\ge0$ is the Hermitian square of $\sqrt r$, so the ray is contained in $\mathcal{C}$.

### The Cone Is a Ray

**Proposition.** The cone is closed under addition, closed under multiplication by non-negative real scalars, closed under the multiplication of the algebra, and closed under inversion.

*Proof.* The sum and the positive multiple of two non-negative reals are non-negative; the product of two non-negative reals is non-negative; the inverse of a positive real is positive.

**Corollary.** The cone is a ray: it is a convex cone of real dimension one, spanned by $1$.

### The Cone Is Its Own Boundary

**Proposition.** The cone has empty interior in $\mathbb{C}$ and coincides with its own boundary there.

*Proof.* An open ball of $\mathbb{C}$ around a point of the ray contains points of positive and of negative imaginary part, and no such point is a non-negative real; so no point of the ray is interior. A point of the ray is a limit of points outside it, namely of itself plus $\varepsilon i$ for $\varepsilon\to0$, so every point of the ray is a boundary point.

**Remark (the contrast with a symmetric cone).** A symmetric cone in the Jordan sense is a closed convex cone with non-empty interior, self-dual for a positive definite form. The cone here is closed and convex, self-dual as a subset of the real line, and of empty interior in the algebra: the symmetric cone of the smallest possible kind, whose ambient algebra is the line it spans.

## Why the Cone Is a Ray

**Remark (the three notions of positive).** Three notions compete. A **square** is an element of the form $Q^{2}$; a **sum of Hermitian squares** is an element of $\mathcal{C}$; a **limit of squares** adds the closure. In $\mathbb{C}$ the first notion is empty of content: every complex number is a square, by the fundamental theorem of algebra, so the set of squares is the whole plane and defines no cone. The second notion is the ray. The third is the ray, the ray being closed. Hence the notion that survives is the Hermitian one, and its cone is the ray because the algebra has one complex dimension.

**Remark (the rank).** The cone of an algebra of rank $r$ has dimension $r$, and here $r=1$. The two Peirce spaces of the only non-trivial idempotent $1$ are the algebra and zero, the spectrum of a self-adjoint element is a single real number, and the space of states read on the self-adjoint functionals is a single point. Every measure of the size of a cone returns the same answer, one, and the answer is forced by the dimension.

## The Order

**Definition.** The **quadratic order** of the self-adjoint part is $r\ge s$ when $r-s\in\mathcal{C}$.

**Proposition.** The order is total on the self-adjoint part, compatible with the addition, and compatible with the multiplication by non-negative elements of the cone.

*Proof.* The self-adjoint part is the real line, and the order of the reals is total; the two compatibilities are the compatibilities of the order of $\mathbb{R}$.

**Proposition.** The order is not compatible with the multiplication of the algebra: there are $r,s\ge0$ and $Q$ with $r\ge s$ and $rQ\not\ge sQ$.

*Proof.* Take $r=1$, $s=0$ and $Q=i$. Then $r-s=1\in\mathcal{C}$, while $rQ-sQ=i$ is not in $\mathcal{C}$.

**Remark (why no order of the field).** A field that is ordered as a ring has its squares positive, so $-1$ is not a square. In $\mathbb{C}$ the element $-1$ is the square of $i$, so no order of the field is compatible with the multiplication. This is the classical obstruction, and the proposition above is its infinitesimal form: the order survives on the self-adjoint part and dies as soon as an imaginary factor enters.

**Remark (positivity is not a total order of the algebra).** The order compares self-adjoint elements and nothing else, and no extension of the cone compares two elements with non-zero imaginary parts. Asking positivity to order the algebra is asking for an order of the field, and the field has none.

## What Positivity Adds Beyond Definiteness

**Proposition.** The Hermitian form is positive definite, and its cone is the cone of squares.

*Proof.* Definiteness is $H(Q)>0$ for $Q\ne0$, which says that $H$ takes its values in the ray and vanishes only at the origin; the cone is the closure in $\mathbb{R}$ of that set of values, and that closure is the ray.

**Remark (the difference of the two statements).** Definiteness is a statement about the values of one form; positivity is a statement about a set closed under addition, under the multiplication of the algebra and under inversion. The complex and the split-complex algebras carry the same kind of form and different cones, so the form does not determine the cone; the algebra does.

**Remark (admitting square roots).** In $\mathbb{C}$ every element is a square, so the passage from an element to its square root loses nothing and the notion of a square is useless for positivity; the useful notion is the Hermitian square, whose value at $Q$ is real and whose two roots $\pm Q$ include an element of the cone whenever the value is positive. In $\mathbb{C}^{\mathrm{spl}}$ not every element is a square, the set of squares is already a cone, and the two notions part company. The capacity to take square roots therefore does not make positivity easier; it makes the naive definition of positivity vacuous, and the Hermitian definition is what remains.

## The Cone Read in the Four Forms

The four forms of the general theory fall two-and-two on $\mathbb{C}$, and the table records the positivity each one defines.

| the form | its value at $Q$ | the positivity it defines |
|---|---|---|
| $\langle Q,Q\rangle$ | $Q^{2}$, complex | none: no cone, no order |
| $\langle Q,Q\rangle_{\natural}$ | $Q^{2}$, complex | none |
| $\langle Q,Q\rangle_{*}$ | $Q\bar Q$, real non-negative | the ray $[0,\infty)$ |
| $\langle Q,Q\rangle_{\natural*}$ | $Q\bar Q$, real non-negative | the ray $[0,\infty)$ |

**Remark (two rows, one cone).** Positivity is carried by the two sesquilinear rows and only by them, and the two carry the same cone. The plain rows define no positivity because a complex-valued form has no non-negative values to single out. In a higher-rank algebra the four rows need not collapse; here the intrinsic conjugation is the identity, so the four forms are two and the two sesquilinear rows carry one cone. The complex case has one cone because it has one dimension.

## The Hilbert Algebra of Rank One

**Proposition.** The algebra with the form $H$ and the involution ${}^{*}=\bar{\cdot}$ satisfies the adjoint axiom $H(Q_1Q_2,Q_3)=H(Q_2,Q_1^{*}Q_3)$.

*Proof.* The left side is $Q_1Q_2\bar Q_3$ and the right side is $Q_2\overline{\bar Q_1Q_3}=Q_2Q_1\bar Q_3$, and the two agree by commutativity.

**Corollary.** $\mathbb{C}$ with the bar and $H$ is a Hilbert algebra, of rank one.

*Proof.* The form is positive definite, the involution is conjugate-linear and anti-multiplicative, being the conjugation of a commutative field, and the adjoint axiom holds. The rank is the complex dimension, which is one.

**Theorem (Cauchy–Schwarz, in the degenerate form).** $|H(Q_1,Q_2)|^{2}=H(Q_1)H(Q_2)$ for every pair, so the inequality of Cauchy–Schwarz is an equality and never strict.

*Proof.* $H(Q_1,Q_2)=Q_1\bar Q_2$, hence $|H(Q_1,Q_2)|^{2}=|Q_1|^{2}|Q_2|^{2}=H(Q_1)H(Q_2)$, the modulus being multiplicative.

**Remark (why the inequality carries no information).** On a space of complex dimension one every two elements are proportional, so the case of equality of Cauchy–Schwarz is the only case. The inequality is empty here, and the statement with content is the next one, which asks when the value is real and non-negative. In a higher-dimensional module the inequality is strict for some pairs.

**Theorem (the real non-negative values).** $H(Q_1,Q_2)$ is real and non-negative exactly when $Q_1=0$ or $Q_2=\lambda Q_1$ with $\lambda\ge0$ real.

*Proof.* For $Q_1\ne0$ write $Q_2=\lambda Q_1$ with $\lambda=Q_2/Q_1$, which is always possible. Then $H(Q_1,Q_2)=\bar\lambda H(Q_1)$, which is real exactly when $\lambda$ is real, and non-negative exactly when that real number is non-negative; for $Q_1=0$ both sides vanish.

**Remark (the condition that carries content).** The proportionality over $\mathbb{C}$ is automatic, so the only condition left is the reality and the sign of the factor, and that is what the cone records: $H(Q_1,Q_2)$ lies on the ray exactly when the second element lies on the ray of the first.

### The Unit Circle

**Proposition (the unitary group).** The set $\mathrm{U}(1)=\{u:H(u)=1\}$ is the unit circle; it is a group under the multiplication, abelian and compact, and it acts on the algebra by $Q\mapsto uQ$ preserving $H$ and preserving the cone.

*Proof.* The product of two elements of norm one has norm one, the inverse of an element of norm one is its conjugate, also of norm one, and $H(uQ)=H(u)H(Q)=H(Q)$. The circle is closed and bounded in $\mathbb{R}^{2}$.

**Remark (the orbits).** The orbits of $\mathrm{U}(1)$ are the circles $H=r$ with $r>0$, so the orbit space is the ray: the cone is one-dimensional because the unitaries move every element along its circle.

### The Witt Group

**Remark (the Witt group).** The Hermitian forms over the algebra are classified by their inertia, and the definite ones, those of the positive cone, by their rank alone. The classes modulo the hyperbolic forms form the Witt group $\mathbb{Z}$, generated by the norm form. The classification is *The Hermitian Modules and the Unitary Witt Group over the Complex Algebra*; positivity enters it only through the definiteness, which makes the forms of the cone isomorphic to sums of copies of the norm.

## The Comparison with the Split-Complex Algebra

**Proposition.** In $\mathbb{C}^{\mathrm{spl}}$ the Hermitian square is $Q\bar Q=a^{2}-b^{2}$, a real number, and it runs over all of $\mathbb{R}$: the set of Hermitian squares is the real line, not a ray.

*Proof.* With $Q=a+jb$ and $j^{2}=1$, the conjugate is $a-jb$ and the product is $Q\bar Q=a^{2}-b^{2}$. The value $t\ge0$ is attained at $Q=\sqrt{t}$, and the value $t<0$ at $Q=\sqrt{-t}\,j$; every value is real.

**Proposition.** The set of elements of $\mathbb{C}^{\mathrm{spl}}$ whose Hermitian square is non-negative is the double cone
$$
\{Q=a+jb : a^{2}\ge b^{2}\}=\{a\ge|b|\}\cup\{a\le-|b|\}.
$$

*Proof.* $Q\bar Q=a^{2}-b^{2}$, which is non-negative exactly when $a^{2}\ge b^{2}$.

**Remark (the two split sets and the two complex sets).** The two notions must be kept apart. The set of Hermitian *values* is a ray in $\mathbb{C}$ and the whole real line in $\mathbb{C}^{\mathrm{spl}}$; the set of *elements* whose Hermitian square is non-negative is the whole plane in $\mathbb{C}$ and the double cone in $\mathbb{C}^{\mathrm{spl}}$. The double cone is not the set of Hermitian squares, and it is not convex: the two components are opposite and meet only at the origin.

**Remark (the contrast).** In $\mathbb{C}$ the Hermitian square of $Q$ carries no trace of the direction of $Q$: it is $|Q|^{2}$, one real number, and every non-negative real is attained on a whole circle of elements. In $\mathbb{C}^{\mathrm{spl}}$ the Hermitian square is $a^{2}-b^{2}$, positive on the interior of the forward cone, negative on the interior of the backward one, and zero on the two null lines; its level sets are the hyperbolas of *The Level Sets of the Split Norm and the Hyperbolic Structure*. The complex square loses the direction because the multiplication by $i$ is a rotation; the split square keeps a sign because the multiplication by $j$ is a reflection.

**Remark (the order of the split algebra).** $\mathbb{C}^{\mathrm{spl}}$ is the product $\mathbb{R}\oplus\mathbb{R}$, and the order that makes it an ordered ring is the product order, whose cone is $\{(a,b):a\ge0,\;b\ge0\}$. That cone is neither the set of Hermitian squares, which is the real line, nor the set of elements with non-negative Hermitian square, which is the double cone; the product order comes from the splitting into idempotents, and the double cone comes from the indefinite form $H$.

## Summary

The cone of Hermitian squares of the complex space is the ray $[0,\infty)$, closed under addition, under the multiplication of the algebra and under inversion, of empty interior in the algebra and coinciding with its own boundary. It is a ray because the algebra has rank one: the spectrum of a self-adjoint element is a single real number and the state space is a point. It induces a total order on the self-adjoint part and no compatible order on the algebra, $-1$ being a square. Positivity adds to the definiteness of the Hermitian form the closure properties of a set, and only the two sesquilinear rows of the four forms carry it. The form makes the algebra a Hilbert algebra of rank one: Cauchy–Schwarz holds as an identity, the value is real and non-negative exactly on the real rays, the unitary group is the circle $\mathrm{U}(1)$, and the Witt group of the Hermitian forms is $\mathbb{Z}$. Against the split-complex algebra, whose Hermitian squares form the real line and whose set of elements with non-negative Hermitian square is a double cone of non-empty interior, the complex cone is the smallest possible: one ray, one dimension, one point of spectrum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q=q+iq'$ | the element, with real coordinates |
| $Q\bar Q=q^{2}+(q')^{2}$ | the Hermitian square, the square of the modulus |
| $\mathcal{C}=[0,\infty)$ | the cone of Hermitian squares, a ray |
| $r\ge s$ | the quadratic order on the self-adjoint part, $r-s\in\mathcal{C}$ |
| $\mathbb{C}^{\mathrm{spl}}$ | the split-complex algebra, whose Hermitian squares are $\mathbb{R}$ and whose $H$-positive set is $\{(a,b):a^{2}\ge b^{2}\}$ |

## Further Reading

- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis*, Cambridge Tracts in Mathematics 190 (Cambridge University Press, 2012), for cones of squares, symmetric cones and the order of a Jordan structure.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the cone of squares, its closure properties and its relation to the quadratic representation.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for ordered fields, the positivity of squares and the obstruction $-1=x^{2}$.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the norm form of an algebra, its isotropy and the cones attached to a real algebra.
