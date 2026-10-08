# __The Idempotents of the Four Products__

## Introduction

An **idempotent** of one of the four products of the biquaternion algebra is an element $\tilde\Pi$ with $\tilde\Pi\star\tilde\Pi = \tilde\Pi$, the equation read in that product. The equation is the algebraic form of a projection, and each of the four groups of the chapter solves it for its own multiplication: the complex bilinear product in *Biquaternion Idempotents and Projections*, the complex quaternionic bilinear product in *Idempotents of the Quaternionic Product*, the complex sesquilinear product in *Projections of the Biquaternion Sesqualgebra*, and the complex quaternionic sesquilinear product in *Idempotents of the Quaternionic Sesquilinear Product*. This article sets the four solution sets side by side and reads their invariants together, the four sets themselves having been tabulated in *Comparison Between the Four Biquaternion Products* §*The Squares, the Idempotents and the Roots*.

The four sets are of four different kinds, and the difference is not in the size of the sets alone but in the place they occupy in the algebra. The plain product's idempotents are the idempotents of the algebra: the trivial pair, the two-sphere of the Hermitian idempotents that the sesquilinear product singles out, and a four-parameter family of non-trivial idempotents lying in no distinguished subspace, every member of the family outside the trivial pair being a zero divisor. The natural product keeps only the trivial pair. The complex sesquilinear product keeps the Hermitian two-sphere, and the complex quaternionic sesquilinear product replaces it by the two-sphere $-\tfrac12e_0+\mu$, whose members are the only nontrivial idempotents of the four multiplications that are **units**. The article owns the comparison of the four sets, the effect of the central square on each, the reading of each in the six distinguished subspaces and the complementation that pairs the members of the plain family.

**Conventions.** The notation is that of *The Four Biquaternion Complex Products* and of the introduction to this group, with the natural conjugation $\tilde Q^{\natural} = Q_0-\mathbf Q$, the star $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$ and the **central square** $\tilde Q^{\natural}\tilde Q = \tilde Q\tilde Q^{\natural}$, a central element. The four products are written $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$, and the six distinguished subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$.

## The Four Sets

**Theorem (the four idempotent sets, quoted).** The idempotents of the four products are:

| product | idempotents | owner |
|---|---|---|
| $\tilde P\tilde Q$ | $0$, $e_0$, and $\tfrac12(e_0+\xi i)$ for a root $\xi$ of $-e_0$ | *Biquaternion Idempotents and Projections* |
| $\tilde P^{\natural}\tilde Q$ | $0$ and $e_0$ alone | *Idempotents of the Quaternionic Product* |
| $\tilde P\tilde Q^{*}$ | $0$, $e_0$, and $\tfrac12(e_0+i\hat\mu)$ for a real unit vector $\hat\mu$ | *Projections of the Biquaternion Sesqualgebra* |
| $\tilde P^{\natural}\tilde Q^{*}$ | $0$, $e_0$, and $-\tfrac12e_0+\mu$ for a real vector $\mu$ with $(\mu,\mu) = \tfrac34$ | *Idempotents of the Quaternionic Sesquilinear Product* |

Everything the four columns share is the trivial pair; everything else separates them. The comparison below reads the four sets through the central square, the unit structure and the distinguished subspaces, and it begins with the plain family, because the other three are described in its terms.

## The Plain Family and the Roots of Minus One

The plain product is the one associative multiplication with a unit, and its idempotents are the idempotents of the algebra.

**Theorem (the plain family, quoted).** The idempotents of $\mathbb{B}$ are $0$, $e_0$, and the elements $\tilde\Pi = \tfrac12(e_0+\xi i)$ over the roots $\xi$ of $-e_0$. The map $\xi\mapsto\tfrac12(e_0+\xi i)$ is a bijection from the roots of $-e_0$ onto the idempotents, and the complementary pair is $\{\tfrac12(e_0+\xi i),\ \tfrac12(e_0-\xi i)\}$.

**Proof.** The proof is in *Biquaternion Idempotents and Projections*; it reduces the equation $\tilde\Pi^2 = \tilde\Pi$ to the classification of the roots of $-e_0$, which is *Biquaternion Square Roots of Minus One, Zero and Plus One*. $\square$

The classification of the roots organises the family in three parts, and each part has its own geometry. The **trivial** roots $\xi = \pm i$ give the trivial idempotents, $0$ and $e_0$. The **real** roots $\xi = \hat\mu$, the unit real vectors, form the two-sphere of $\mathbb{R}^{3}$, and give the two-sphere $\tfrac12(e_0+i\hat\mu)$ of **Hermitian** idempotents, the family the complex sesquilinear product keeps. The **non-trivial** roots $\xi = \mathbf p+i\mathbf p'$, with $\mathbf p,\mathbf p'$ real vectors, $\mathbf p'\neq0$, satisfying $\sum_k p_k^{2}-\sum_k p'^{2}_k = 1$ and $\sum_k p_kp'_k = 0$, form a four-parameter family, and give the **non-trivial** idempotents, a four-parameter family that lies in none of the four four-dimensional subspaces of the algebra.

The second and the third parts are related by the same formula and are not the same: the Hermitian idempotents have a real scalar part and a purely imaginary vector part, while a non-trivial idempotent $\tilde\Pi = \tfrac12(e_0+\xi i)$ with $\xi = \mathbf p+i\mathbf p'$ is

$$
\tilde\Pi = \tfrac12\bigl(e_0-\mathbf p'\bigr) + \tfrac12\mathbf p\,i ,
$$

whose vector part $\tfrac12(-\mathbf p'+i\mathbf p)$ carries both a real and an imaginary term, so that the element is neither Hermitian nor anti-Hermitian and has no other distinguished subspace to lie in. The four-parameter family is the largest part of the plain idempotent set, and it is the one the other three products discard.

## The Two Spheres

Two of the other three sets are two-spheres, and only the second of them is a sphere of units of the algebra.

**Proposition (the two spheres).** The idempotents of the complex sesquilinear product beyond the trivial pair are the Hermitian idempotents $\tilde\Pi_+(\hat\mu) = \tfrac12(e_0+i\hat\mu)$ over the real vectors $\hat\mu$ with $\sum_k\hat\mu_k^{2} = 1$, a two-sphere lying in $\mathbb{M}_+$; the idempotents of the complex quaternionic sesquilinear product beyond the trivial pair are the elements $\tilde\Pi(\mu) = -\tfrac12e_0+\mu$ over the real vectors $\mu$ with $(\mu,\mu) = \tfrac34$, a two-sphere lying in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$.

**Proof.** The first is *Projections of the Biquaternion Sesqualgebra*: applying ${}^{*}$ to $\tilde Q\tilde Q^{*} = \tilde Q$ shows $\tilde Q$ Hermitian, so the equation is $\tilde Q^{2} = \tilde Q$, and the Hermitian roots of that equation are the displayed ones. The second is *Idempotents of the Quaternionic Sesquilinear Product*: inside the quaternion subspace, where a real element has $\tilde Q^{*} = \tilde Q^{\natural}$, the equation $\tilde Q^{\natural}\tilde Q^{*} = \tilde Q$ becomes $(\tilde Q^{\natural})^{2} = \tilde Q$, and its solutions are the displayed ones. $\square$

The two families are both two-spheres of the algebra, read off the real directions, and the two products place them differently. A real vector $\mu$ with $\sum_k\mu_k^{2} = \tfrac34$ is $\tfrac{\sqrt3}{2}\hat\mu$ for a real $\hat\mu$ with $\sum_k\hat\mu_k^{2} = 1$, so the fourth family is the sphere of radius $\tfrac{\sqrt3}{2}$ about the point $-\tfrac12e_0$, while the Hermitian family is the sphere $\tfrac12e_0+\tfrac i2\hat\mu$ of radius $\tfrac12$ about the point $\tfrac12e_0$: two spheres of different radius and different centre. On the Hermitian sphere the antipode $\hat\mu\mapsto-\hat\mu$ is the complementation $\tilde\Pi_+\mapsto e_0-\tilde\Pi_+$; on the fourth sphere it is the reflection $\mu\mapsto-\mu$, which sends $-\tfrac12e_0+\mu$ to $\tfrac12e_0-\mu$, an element that is **not** a member of the family. The passage from the one sphere to the other is the visible difference between the two sesquilinear products.

## The Central Square of an Idempotent

The central square of an idempotent is the invariant that separates the four sets, because it is the second-order invariant of the plain product and every idempotent satisfies a quadratic equation there.

**Theorem (the central square of an idempotent).** On the four idempotent sets the central square takes the values:

| idempotent | central square |
|---|---|
| $0$ | $0$ |
| $e_0$ | $e_0$ |
| $\tfrac12(e_0+\xi i)$, $\xi$ a real or a non-trivial root of $-e_0$ (the Hermitian $\tfrac12(e_0+i\hat\mu)$ for a real root $\xi = \hat\mu$) | $0$ |
| $-\tfrac12e_0+\mu$, $(\mu,\mu) = \tfrac34$ | $e_0$ |

**Proof.** For the plain family, $\bigl(\tfrac12(e_0+\xi i)\bigr)^{\natural}\bigl(\tfrac12(e_0+\xi i)\bigr) = \tfrac14\bigl(e_0-\xi i\bigr)\bigl(e_0+\xi i\bigr) = \tfrac14\bigl(e_0-(\xi i)^{2}\bigr)$, and $(\xi i)^{2} = \xi^{2}i^{2} = e_0$ for a root $\xi$ of $-e_0$, so the central square is $0$; the Hermitian idempotents are the members of that family with a real root, and the computation is the same. For the fourth family the idempotent is real, so $\tilde\Pi^{\natural} = -\tfrac12e_0-\mu$, and $\tilde\Pi^{\natural}\tilde\Pi = \bigl(-\tfrac12e_0-\mu\bigr)\bigl(-\tfrac12e_0+\mu\bigr) = \tfrac14e_0-\mu^{2} = \tfrac14e_0+(\mu,\mu)e_0 = \bigl(\tfrac14+\tfrac34\bigr)e_0 = e_0$, so the central square is $e_0$; the product $\overline{\tilde\Pi}\tilde\Pi$ computed in *Idempotents of the Quaternionic Sesquilinear Product* is $\tilde\Pi^{\natural}$, which is the same central value. $\square$

Zero for the two families of zero divisors, $e_0$ for the two units: the central square is the invariant that decides which idempotents are units of the algebra and which are not, and it decides it in opposite directions for the plain family and for the fourth family. The Hermitian idempotents are therefore **null** for the algebra's central square although they are the pure states of the sesqualgebra (*Projections of the Biquaternion Sesqualgebra*), a coincidence of language worth noticing: the algebraic positivity of the sesqualgebra and the central square of the algebra are different objects, and the idempotents lie in its zero set.

## Units, Zero Divisors and the Antipode

**Theorem (units and zero divisors among the idempotents).** Among the idempotents of the four products, the units of the algebra are $e_0$ and the two-sphere $-\tfrac12e_0+\mu$ of the fourth product; the zero divisors of the algebra are the members of the plain family $\tfrac12(e_0+\xi i)$ with $\xi$ non-trivial or real, and no other idempotent; and $0$ is neither.

**Proof.** The values of the central square are the previous theorem, and the criterion of invertibility is that the central square not vanish (*Biquaternion Norm and Invertibility*). $\square$

The theorem is the sharpest separation of the four sets. The natural product's idempotents are both units, so the smallest set is the one with no zero divisors at all. The plain product and the complex sesquilinear product have nontrivial idempotents and every one of them is a zero divisor; the plain product's non-trivial family is a part of the zero-divisor cone that no other product's idempotents reach. The fourth product is the only one whose nontrivial idempotents are units, and they are its own: neither $\tfrac12(e_0+i\hat\mu)$ nor $\tfrac12(e_0+\xi i)$ is an idempotent of the complex quaternionic sesquilinear product, and neither $-\tfrac12e_0+\mu$ nor $\tfrac12(e_0+\xi i)$ is an idempotent of the natural product, whose only idempotents are $0$ and $e_0$.

The complementation pairs the members of the two families of the algebra's own product.

**Proposition (the antipodal idempotent).** Let $\tilde\Pi$ be an idempotent of the plain product. Then $e_0-\tilde\Pi$ is an idempotent of the plain product, the two are orthogonal in the plain product, $\tilde\Pi(e_0-\tilde\Pi) = 0$, and they sum to $e_0$. The map is the antipode of the parameter set: $\xi\mapsto-\xi$ for the plain family, and $\hat\mu\mapsto-\hat\mu$ for the Hermitian subfamily.

**Proof.** $(e_0-\tilde\Pi)^{2} = e_0-2\tilde\Pi+\tilde\Pi^{2} = e_0-\tilde\Pi$ and $\tilde\Pi(e_0-\tilde\Pi) = \tilde\Pi-\tilde\Pi^{2} = 0$. The parametrisation gives $\tfrac12(e_0+\xi i)$ to $\tfrac12(e_0-\xi i)$. $\square$

The complementation exists for the plain product alone, because it uses the associativity and the unit of that product; the two-sphere of the fourth product carries no complementation inside itself, and the natural product, having only the trivial pair, has the complementation only on it.

## The Position in the Six Subspaces

Each family lives in a specific place, and the places are read off the coefficient conditions of the six subspaces.

**Theorem (the position of the families).** The trivial pair lies in the centre $\mathbb{C}_{\mathbb{B}}$. The Hermitian family lies in $\mathbb{M}_+$ and in no other four-dimensional subspace. The family $-\tfrac12e_0+\mu$ lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and in no other four-dimensional subspace. The non-trivial family of the plain product lies in none of the four four-dimensional subspaces.

**Proof.** $0$ and $e_0$ are complex multiples of $e_0$, hence central. For $\tfrac12(e_0+i\hat\mu)$ the scalar part is real and the vector part is purely imaginary, which is the definition of $\mathbb{M}_+$; the element is not pure, so it is not in $\mathrm{Vect}(\mathbb{B})$, its scalar part is not purely imaginary, so it is not in $\mathbb{M}_-$, and its vector part is not real, so it is not in $\mathbb{H}_{\mathbb{B}}$ or in $i\mathbb{H}_{\mathbb{B}}$. For $-\tfrac12e_0+\mu$ the coefficients are real, so the element is in $\mathbb{H}_{\mathbb{B}}$; its scalar part is real and nonzero, so it is not anti-Hermitian, and its vector part is real and nonzero, so it is not Hermitian. For the non-trivial $\tilde\Pi = \tfrac12(e_0-\mathbf p')+\tfrac12\mathbf p\,i$ the vector part carries both a real term $-\tfrac12\mathbf p'$ and an imaginary term $\tfrac12\mathbf p\,i$, and the scalar part is real; the element is neither Hermitian, nor anti-Hermitian, nor pure, nor real. $\square$

The four sets therefore occupy four different regions: the centre for the trivial pair, $\mathbb{M}_+$ for the Hermitian family, $\mathbb{H}_{\mathbb{B}}$ for the fourth family, and no distinguished region at all for the non-trivial family, which is the whole point of its name. The restrictions of the products themselves to these subspaces are *The Six Subspaces and the Four Complex Products*.

## The Peirce Data

Of the four products, only the plain one supports the Peirce theory, and the reason is associativity.

**Theorem (the Peirce decomposition is the plain product's own).** For an idempotent $\tilde\Pi$ of the plain product the algebra splits as $\mathbb{B} = \tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B}$, and the two summands are left ideals; for the idempotents of the other three products no such decomposition is available, because the products are not associative and the multiplication by an idempotent is not a projection.

**Proof.** The decomposition and the ideal structure are *Biquaternion Ideals and Peirce Decomposition*; the display $\tilde\Pi(e_0-\tilde\Pi) = 0$ of the previous section is the orthogonality the decomposition needs, and it uses associativity, which the three other products fail. $\square$

The comparison is the last separation of the article, and it is the reason the plain product's idempotents are the idempotents of the algebra. The Hermitian idempotents of the complex sesquilinear product act as projections on the positive cone and on the Hermitian module (*Projections of the Biquaternion Sesqualgebra*), the two-sphere of the fourth product is the family of idempotents of that product with central square $e_0$, and the natural product has neither, having only the trivial pair; the projector of the algebra's Hilbert structure is the Hermitian one, and it is a projector of the sesquilinear product while being an idempotent of the plain product.

## Summary

The four products of *The Four Biquaternion Complex Products* have four idempotent sets, all containing the trivial pair. The plain product, whose idempotents are the idempotents of the algebra, has the elements $\tfrac12(e_0+\xi i)$ over the roots $\xi$ of $-e_0$: the trivial pair, the two-sphere $\tfrac12(e_0+i\hat\mu)$ of the Hermitian idempotents, and a four-parameter family lying in none of the four four-dimensional subspaces; the natural product has the trivial pair alone; the complex sesquilinear product has the trivial pair and the Hermitian two-sphere; and the complex quaternionic sesquilinear product has the trivial pair and the two-sphere $-\tfrac12e_0+\mu$ with $(\mu,\mu) = \tfrac34$.

The central square separates the sets: it is $e_0$ on $e_0$, $0$ on every nontrivial idempotent of the plain product and of the complex sesquilinear product, and $e_0$ on the two-sphere of the fourth product. The idempotents of the four sets that are units of the algebra are therefore $e_0$ and the fourth product's sphere; the idempotents that are zero divisors are the nontrivial ones of the plain product and the Hermitian ones of the complex sesquilinear product; and the natural product's set consists of the two units alone.

The families occupy the centre, $\mathbb{M}_+$, $\mathbb{H}_{\mathbb{B}}$ and no distinguished subspace, and the complementation $\tilde\Pi\mapsto e_0-\tilde\Pi$ pairs the members of the plain family and is available for the plain product alone. The Peirce decomposition is the plain product's, because it needs associativity, and the comparison in one sentence is this: the plain product is the only one of the four whose idempotents build the algebra, the fourth product is the only one whose nontrivial idempotents are units, and the natural product is the only one with no nontrivial idempotent at all. The four sets themselves are tabulated in *Comparison Between the Four Biquaternion Products*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi$ | an idempotent, $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ in the product at hand |
| $\xi$ | a root of $-e_0$, $\xi^{2} = -e_0$; trivial $\pm i$, real $\hat\mu$, or non-trivial $\mathbf p+i\mathbf p'$ |
| $\hat\mu$ | a real unit vector, $\hat\mu^{2} = -e_0$ |
| $\tilde\Pi_+(\hat\mu) = \tfrac12(e_0+i\hat\mu)$ | the Hermitian idempotents of the complex sesquilinear product |
| $-\tfrac12e_0+\mu$ | the idempotents of the complex quaternionic sesquilinear product, $(\mu,\mu) = \tfrac34$ |

## Further Reading

- *Comparison Between the Four Biquaternion Products* (`articles_maths/comparison-between-the-four-biquaternion-products.md`), for the tabulation of the four idempotent sets and the four square-root problems.
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the idempotents of the algebra, their bijection with the roots of $-e_0$ and their role in the Peirce decomposition.
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the three families of roots of $-e_0$.
- *Idempotents of the Quaternionic Product* (`articles_maths/idempotents-of-the-quaternionic-product.md`), for the trivial pair of the natural product.
- *Projections of the Biquaternion Sesqualgebra* (`articles_maths/projections-of-the-biquaternion-sesqualgebra.md`), for the Hermitian two-sphere and its projections.
- *Idempotents of the Quaternionic Sesquilinear Product* (`articles_maths/idempotents-of-the-quaternionic-sesquilinear-product.md`), for the two-sphere of units.
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the decomposition the plain idempotents carry.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the positive cone on whose boundary the Hermitian idempotents lie.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the criterion that the central square not vanish, which the table applies.
- *The Six Subspaces and the Four Complex Products* (`articles_maths/the-six-subspaces-and-the-four-complex-products.md`), for the six subspaces and the products on them.
