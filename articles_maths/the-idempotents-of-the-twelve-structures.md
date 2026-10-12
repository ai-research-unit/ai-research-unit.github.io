# __The Idempotents of the Twelve Structures__

## Introduction

An **idempotent** of one of the four general products of the biquaternion algebra is an element $\tilde\Pi$ with $\tilde\Pi\star\tilde\Pi = \tilde\Pi$, the equation read in that product. The equation is the algebraic form of a projection, and each of the four groups of the chapter solves it for its own multiplication: the general plain bilinear product in *Idempotents of the General Plain Algebra*, the general quaternionic bilinear product in *Idempotents of the General Quaternionic Algebra*, the general plain sesquilinear product in *Idempotents of the General Plain Sesqualgebra*, and the general quaternionic sesquilinear product in *Idempotents of the General Quaternionic Sesqualgebra*. This article sets the four solution sets side by side and reads their invariants together, the four sets themselves having been tabulated in *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*.

The four sets are of four different kinds, and the difference is not in the size of the sets alone but in the place they occupy in the algebra. The plain product's idempotents are the idempotents of the algebra: the trivial pair, the family of the Hermitian idempotents that the sesquilinear product singles out, and a four-parameter family of non-trivial idempotents lying in no remarkable subspace, every member of the family outside the trivial pair being a zero divisor. The natural product keeps only the trivial pair. The general plain sesquilinear product keeps the Hermitian family, and the general quaternionic sesquilinear product replaces it by the family $-\tfrac12e_0+\mu$, whose members are the only nontrivial idempotents of the four multiplications that are **units**. The article owns the comparison of the four sets, the effect of the central square on each, the reading of each in the remarkable subspaces and the complementation that pairs the members of the plain family.

**Conventions.** The notation is that of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and of the introduction to this group, with the natural conjugation $\tilde Q^{\natural} = Q_0-\mathbf Q$, the star $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$ and the **central square** $\tilde Q^{\natural}\tilde Q = \tilde Q\tilde Q^{\natural}$, a central element. The four general products are written $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$, and the remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$.

## The Four Sets

**Theorem (the four idempotent sets, quoted).** The idempotents of the four general products are:

| product | idempotents | owner |
|---|---|---|
| $\tilde P\tilde Q$ | $0$, $e_0$, and $\tfrac12(e_0+\tilde\Xi i)$ for a root $\tilde\Xi$ of $-e_0$ | *Idempotents of the General Plain Algebra* |
| $\tilde P^{\natural}\tilde Q$ | $0$ and $e_0$ alone | *Idempotents of the General Quaternionic Algebra* |
| $\tilde P\tilde Q^{*}$ | $0$, $e_0$, and $\tfrac12(e_0+i\hat\mu)$ for a real unit vector $\hat\mu$ | *Idempotents of the General Plain Sesqualgebra* |
| $\tilde P^{\natural}\tilde Q^{*}$ | $0$, $e_0$, and $-\tfrac12e_0+\mu$ for a real vector $\mu$ with $(\mu,\mu) = \tfrac34$ | *Idempotents of the General Quaternionic Sesqualgebra* |

Everything the four columns share is the trivial pair; everything else separates them. The comparison below reads the four sets through the central square, the unit structure and the remarkable subspaces, and it begins with the plain family, because the other three are described in its terms.

## The Twelve Idempotent Sets

The four products are four of the twelve structures of the space, the other eight being the symmetric and the antisymmetric parts of the four (*The 12 Products of the Biquaternion Complex Space*, *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The idempotent equation $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ is written in the operation of the structure, so each of the twelve carries an idempotent set of its own, and it is the square operator that decides them all.

| structure | the square $\tilde\Pi\star\tilde\Pi$ | the idempotents |
|---|---|---|
| $\mathrm{GPA}$ | $\tilde\Pi^{2}$ | $0$, $e_0$, $\tfrac12(e_0+\tilde\Xi i)$ |
| $\mathrm{SPA}$ | $\tilde\Pi^{2}$, the plain square | the same set as $\mathrm{GPA}$ |
| $\mathrm{APA}$ | $0$ | $0$ alone |
| $\mathrm{GQA}$ | $C(\tilde\Pi)e_0$ | $0$, $e_0$ |
| $\mathrm{SQA}$ | $C(\tilde\Pi)e_0$ | $0$, $e_0$ |
| $\mathrm{AQA}$ | $0$ | $0$ alone |
| $\mathrm{GPS}$ | $\tilde\Pi\tilde\Pi^{*}$ | $0$, $e_0$, $\tfrac12(e_0+i\hat\mu)$ |
| $\mathrm{SPS}$ | $\mathrm{Sc}(\tilde\Pi\tilde\Pi^{*})e_0$, real and $\geq 0$ | $0$, $e_0$ |
| $\mathrm{APS}$ | $\tfrac12(\tilde\Pi\tilde\Pi^{*}-\overline{\tilde\Pi\tilde\Pi^{*}})$ | $0$ alone |
| $\mathrm{GQS}$ | $\tilde\Pi^{\natural}\tilde\Pi^{*}$ | $0$, $e_0$, $-\tfrac12e_0+\mu$ |
| $\mathrm{SQS}$ | $\tfrac12(\tilde\Pi^{\natural}\tilde\Pi^{*}+\overline{\tilde\Pi^{\natural}\tilde\Pi^{*}})$ | $0$, $e_0$, $-\tfrac12e_0+\mu$ |
| $\mathrm{AQS}$ | $\tfrac12(\tilde\Pi^{\natural}\tilde\Pi^{*}-\overline{\tilde\Pi^{\natural}\tilde\Pi^{*}})$ | $0$ alone |

**Theorem (only five structures carry a nontrivial idempotent).** Among the twelve structures of the biquaternion complex space, an idempotent other than $0$ and $e_0$ exists exactly for $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ and $\mathrm{SQS}$. The four antisymmetric structures have $0$ alone, and $\mathrm{GQA}$, $\mathrm{SQA}$ and $\mathrm{SPS}$ have the trivial pair. The idempotent sets of $\mathrm{GQS}$ and $\mathrm{SQS}$ coincide.

*Proof.* On the two bilinear antisymmetric structures the square vanishes identically, $\tilde\Pi\star\tilde\Pi = 0$, so the equation $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ forces $\tilde\Pi = 0$; this closes the rows $\mathrm{APA}$ and $\mathrm{AQA}$. On the two antisymmetric sesquilinear structures the square is a pure vector, so an idempotent has vanishing scalar part; writing it $\tilde\Pi = \mathbf p$, its square is the conjugate cross product $-\mathbf p\times\overline{\mathbf p}$ for $\mathrm{APS}$ and $\mathbf p\times\overline{\mathbf p}$ for $\mathrm{AQS}$, a purely imaginary vector, and a purely imaginary $\mathbf p$ makes the cross product vanish, so the equation again reads $\mathbf p = 0$; this closes the rows $\mathrm{APS}$ and $\mathrm{AQS}$. On $\mathrm{GQA}$, $\mathrm{SQA}$ and $\mathrm{SPS}$ the square is the central element $C(\tilde\Pi)e_0$ or $\mathrm{Sc}(\tilde\Pi\tilde\Pi^{*})e_0$, so an idempotent is central, hence $\tilde\Pi = qe_0$ with $q\in\mathbb{C}$, and the equation on the centre, $q = q^{2}$ for the two bilinear structures and $q = \lvert q\rvert^{2}$ for the sesquilinear one, leaves $q\in\{0,1\}$. The five remaining rows are the theorem of §*The Four Sets*, together with the identity $\tilde\Pi\bullet\tilde\Pi = \tilde\Pi^{2}$ for the symmetric plain structure, whose square is therefore the plain square and whose idempotents are the algebra's own. For the symmetric quaternionic sesquilinear structure the square is the coefficientwise real part of $\tilde\Pi^{\natural}\tilde\Pi^{*}$, which is a real element, so the idempotent equation forces $\tilde\Pi$ real and reduces to $(\tilde\Pi^{\natural})^{2} = \tilde\Pi$; the resulting set is the family $-\tfrac12e_0+\mu$ with $(\mu,\mu) = \tfrac34$, the same set as the general quaternionic sesquilinear structure (*Idempotents of the Symmetric Quaternionic Sesqualgebra*).

The classification is sharp, and it reads the ways a square operator can fail to be the plain square. The **antisymmetric** square destroys the equation, being identically zero on the two bilinear structures and a purely imaginary pure vector on the two sesquilinear ones. The **scalar-valued** square, the one of $\mathrm{GQA}$, $\mathrm{SQA}$ and $\mathrm{SPS}$, returns a central element, so an idempotent must be central and only the trivial pair survives. The **symmetric plain** square is the plain square itself, so $\mathrm{SPA}$ carries exactly the plain family, four parameters and all, although it is not associative (it does carry the unit $e_0$). The three structures that keep a two-parameter family of nontrivial idempotents — $\mathrm{GPS}$ with the Hermitian family, and $\mathrm{GQS}$ and $\mathrm{SQS}$ with the family $-\tfrac12e_0+\mu$ — are the structures whose square operator is neither identically zero nor central-valued; the family of $\mathrm{SQS}$ is the family of $\mathrm{GQS}$ because the coefficientwise real part of $\tilde\Pi^{\natural}\tilde\Pi^{*}$ equals $\tilde\Pi^{\natural}\tilde\Pi^{*}$ itself whenever $\tilde\Pi$ is real.

## The Plain Family and the Roots of Minus One

The plain product is the one associative multiplication with a unit, and its idempotents are the idempotents of the algebra.

**Theorem (the plain family, quoted).** The idempotents of $\mathbb{B}$ are $0$, $e_0$, and the elements $\tilde\Pi = \tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$. The map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi i)$ is a bijection from the roots of $-e_0$ onto the idempotents, and the complementary pair is $\{\tfrac12(e_0+\tilde\Xi i),\ \tfrac12(e_0-\tilde\Xi i)\}$.

**Proof.** The proof is in *Idempotents of the General Plain Algebra*; it reduces the equation $\tilde\Pi^2 = \tilde\Pi$ to the classification of the roots of $-e_0$, which is *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

The classification of the roots organises the family in three parts, and each part has its own type. The **trivial** roots $\tilde\Xi = \pm i$ give the trivial idempotents, $0$ and $e_0$. The **real** roots $\tilde\Xi = \hat\mu$, the unit real vectors, form the unit sphere of $\mathbb{R}^{3}$, and give the family $\tfrac12(e_0+i\hat\mu)$ of **Hermitian** idempotents, the family the general plain sesquilinear product keeps. The **non-trivial** roots $\tilde\Xi = \mathbf p+i\mathbf p'$, with $\mathbf p,\mathbf p'$ real vectors, $\mathbf p'\neq0$, satisfying $\sum_k p_k^{2}-\sum_k p'^{2}_k = 1$ and $\sum_k p_kp'_k = 0$, form a four-parameter family, and give the **non-trivial** idempotents, a four-parameter family that lies in none of the four four-dimensional subspaces of the algebra.

The second and the third parts are related by the same formula and are not the same: the Hermitian idempotents have a real scalar part and a purely imaginary vector part, while a non-trivial idempotent $\tilde\Pi = \tfrac12(e_0+\tilde\Xi i)$ with $\tilde\Xi = \mathbf p+i\mathbf p'$ is

$$
\tilde\Pi = \tfrac12\bigl(e_0-\mathbf p'\bigr) + \tfrac12\mathbf p\,i ,
$$

whose vector part $\tfrac12(-\mathbf p'+i\mathbf p)$ carries both a real and an imaginary term, so that the element is neither Hermitian nor anti-Hermitian and has no other remarkable subspace to lie in. The four-parameter family is the largest part of the plain idempotent set, and it is the one the other three products discard.

## The Two Families

Two of the other three sets are two-parameter families, and only the second of them is a family of units of the algebra.

**Proposition (the two families).** The idempotents of the general plain sesquilinear product beyond the trivial pair are the Hermitian idempotents $\tilde\Pi_1(\hat\mu) = \tfrac12(e_0+i\hat\mu)$ over the real vectors $\hat\mu$ with $\sum_k\hat\mu_k^{2} = 1$, a family lying in $\mathbb{M}_+$; the idempotents of the general quaternionic sesquilinear product beyond the trivial pair are the elements $\tilde\Pi(\mu) = -\tfrac12e_0+\mu$ over the real vectors $\mu$ with $(\mu,\mu) = \tfrac34$, a family lying in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$.

**Proof.** The first is *Idempotents of the General Plain Sesqualgebra*: applying ${}^{*}$ to $\tilde Q\tilde Q^{*} = \tilde Q$ shows $\tilde Q$ Hermitian, so the equation is $\tilde Q^{2} = \tilde Q$, and the Hermitian roots of that equation are the displayed ones. The second is *Idempotents of the General Quaternionic Sesqualgebra*: inside the quaternion subspace, where a real element has $\tilde Q^{*} = \tilde Q^{\natural}$, the equation $\tilde Q^{\natural}\tilde Q^{*} = \tilde Q$ becomes $(\tilde Q^{\natural})^{2} = \tilde Q$, and its solutions are the displayed ones.

The two families are both two-parameter families of the algebra, read off the real directions, and the two products place them differently. A real vector $\mu$ with $\sum_k\mu_k^{2} = \tfrac34$ is $\tfrac{\sqrt3}{2}\hat\mu$ for a real $\hat\mu$ with $\sum_k\hat\mu_k^{2} = 1$, so the fourth family is the set $-\tfrac12e_0+\mu$ with $(\mu,\mu)=\tfrac34$, while the Hermitian family is the set $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$: two families of different radius and different centre. On the Hermitian family the antipode $\hat\mu\mapsto-\hat\mu$ is the complementation $\tilde\Pi_1\mapsto e_0-\tilde\Pi_1$; on the fourth family it is the map $\mu\mapsto-\mu$, which sends $-\tfrac12e_0+\mu$ to $\tfrac12e_0-\mu$, an element that is **not** a member of the family. The passage from the one family to the other is the visible difference between the two sesquilinear products.

## The Central Square of an Idempotent

The central square of an idempotent is the invariant that separates the four sets, because it is the second-order invariant of the plain product and every idempotent satisfies a quadratic equation there.

**Theorem (the central square of an idempotent).** On the four idempotent sets the central square takes the values:

| idempotent | central square |
|---|---|
| $0$ | $0$ |
| $e_0$ | $e_0$ |
| $\tfrac12(e_0+\tilde\Xi i)$, $\tilde\Xi$ a real or a non-trivial root of $-e_0$ (the Hermitian $\tfrac12(e_0+i\hat\mu)$ for a real root $\tilde\Xi = \hat\mu$) | $0$ |
| $-\tfrac12e_0+\mu$, $(\mu,\mu) = \tfrac34$ | $e_0$ |

**Proof.** For the plain family, $\bigl(\tfrac12(e_0+\tilde\Xi i)\bigr)^{\natural}\bigl(\tfrac12(e_0+\tilde\Xi i)\bigr) = \tfrac14\bigl(e_0-\tilde\Xi i\bigr)\bigl(e_0+\tilde\Xi i\bigr) = \tfrac14\bigl(e_0-(\tilde\Xi i)^{2}\bigr)$, and $(\tilde\Xi i)^{2} = \tilde\Xi^{2}i^{2} = e_0$ for a root $\tilde\Xi$ of $-e_0$, so the central square is $0$; the Hermitian idempotents are the members of that family with a real root, and the computation is the same. For the fourth family the idempotent is real, so $\tilde\Pi^{\natural} = -\tfrac12e_0-\mu$, and $\tilde\Pi^{\natural}\tilde\Pi = \bigl(-\tfrac12e_0-\mu\bigr)\bigl(-\tfrac12e_0+\mu\bigr) = \tfrac14e_0-\mu^{2} = \tfrac14e_0+(\mu,\mu)e_0 = \bigl(\tfrac14+\tfrac34\bigr)e_0 = e_0$, so the central square is $e_0$; the owner's idempotence criterion is the product in the other order, $\overline{\tilde\Pi}\tilde\Pi = \tilde\Pi^{2} = \tilde\Pi^{\natural}$ for this real idempotent, which is the plain square and not the central square.

Zero for the two families of zero divisors, $e_0$ for the two units: the central square is the invariant that decides which idempotents are units of the algebra and which are not, and it decides it in opposite directions for the plain family and for the fourth family. The Hermitian idempotents are therefore **null** for the algebra's central square although they are the pure states of the sesqualgebra (*Idempotents of the General Plain Sesqualgebra*), a coincidence of language worth noticing: the algebraic positivity of the sesqualgebra and the central square of the algebra are different objects, and the idempotents lie in its zero set.

## Units, Zero Divisors and the Antipode

**Theorem (units and zero divisors among the idempotents).** Among the idempotents of the four general products, the units of the algebra are $e_0$ and the family $-\tfrac12e_0+\mu$ of the fourth product; the zero divisors of the algebra are the members of the plain family $\tfrac12(e_0+\tilde\Xi i)$ with $\tilde\Xi$ non-trivial or real, and no other idempotent; and $0$ is neither.

**Proof.** The values of the central square are the previous theorem, and the criterion of invertibility is that the central square not vanish (*Norm and Invertibility in the General Plain Algebra*).

The theorem is the sharpest separation of the four sets. The natural product's nontrivial idempotent, $e_0$, is a unit, so the smallest set is the one with no zero divisors at all. The plain product and the general plain sesquilinear product have nontrivial idempotents and every one of them is a zero divisor; the plain product's non-trivial family is a part of the zero-divisor cone that no other product's idempotents reach. The fourth product is the only one whose nontrivial idempotents are units, and the nontrivial idempotents of the other three are not idempotents of it: neither $\tfrac12(e_0+i\hat\mu)$ nor a nontrivial $\tfrac12(e_0+\tilde\Xi i)$ is an idempotent of the general quaternionic sesquilinear product, and neither $-\tfrac12e_0+\mu$ nor a nontrivial $\tfrac12(e_0+\tilde\Xi i)$ is an idempotent of the natural product, whose only idempotents are $0$ and $e_0$.

The complementation pairs the members of the two families of the algebra's own product.

**Proposition (the antipodal idempotent).** Let $\tilde\Pi$ be an idempotent of the plain product. Then $e_0-\tilde\Pi$ is an idempotent of the plain product, the two are orthogonal in the plain product, $\tilde\Pi(e_0-\tilde\Pi) = 0$, and they sum to $e_0$. The map is the antipode of the parameter set: $\tilde\Xi\mapsto-\tilde\Xi$ for the plain family, and $\hat\mu\mapsto-\hat\mu$ for the Hermitian subfamily.

**Proof.** $(e_0-\tilde\Pi)^{2} = e_0-2\tilde\Pi+\tilde\Pi^{2} = e_0-\tilde\Pi$ and $\tilde\Pi(e_0-\tilde\Pi) = \tilde\Pi-\tilde\Pi^{2} = 0$. The parametrisation gives $\tfrac12(e_0+\tilde\Xi i)$ to $\tfrac12(e_0-\tilde\Xi i)$.

The complementation is available wherever the family is closed under $\tilde\Pi\mapsto e_0-\tilde\Pi$: for the plain product it pairs the whole family, the four-parameter part included, and for the general plain sesquilinear product it pairs the Hermitian family. It fails for the general quaternionic sesquilinear product, whose family is not closed — the map $\mu\mapsto-\mu$ sends $-\tfrac12e_0+\mu$ outside it — and for the natural product, which has no family beyond the trivial pair, on which the complementation is the exchange of the two.

## The Position in the Remarkable Subspaces

Each family lives in a specific place, and the places are read off the coefficient conditions of the remarkable subspaces.

**Theorem (the position of the families).** The trivial pair lies in the centre $\mathbb{C}_{\mathbb{B}}$. The Hermitian family lies in $\mathbb{M}_+$ and in no other four-dimensional subspace. The family $-\tfrac12e_0+\mu$ lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and in no other four-dimensional subspace. The non-trivial family of the plain product lies in none of the four four-dimensional subspaces.

**Proof.** $0$ and $e_0$ are complex multiples of $e_0$, hence central. For $\tfrac12(e_0+i\hat\mu)$ the scalar part is real and the vector part is purely imaginary, which is the definition of $\mathbb{M}_+$; the element is not pure, so it is not in $\mathrm{Vect}(\mathbb{B})$, its scalar part is not purely imaginary, so it is not in $\mathbb{M}_-$ or in $i\mathbb{H}_{\mathbb{B}}$, and its vector part is not real, so it is not in $\mathbb{H}_{\mathbb{B}}$. For $-\tfrac12e_0+\mu$ the coefficients are real, so the element is in $\mathbb{H}_{\mathbb{B}}$; its scalar part is real and nonzero, so it is not anti-Hermitian, and its vector part is real and nonzero, so it is not Hermitian. For the non-trivial $\tilde\Pi = \tfrac12(e_0-\mathbf p')+\tfrac12\mathbf p\,i$ the vector part carries both a real term $-\tfrac12\mathbf p'$ and an imaginary term $\tfrac12\mathbf p\,i$, and the scalar part is real; the element is neither Hermitian, nor anti-Hermitian, nor pure, nor real.

The four sets therefore occupy four different regions: the centre for the trivial pair, $\mathbb{M}_+$ for the Hermitian family, $\mathbb{H}_{\mathbb{B}}$ for the fourth family, and no distinguished region at all for the non-trivial family, which is the whole point of its name. The restrictions of the products themselves to these subspaces are *Remarkable Subspaces and the Four General Products*.

## The Peirce Data

Of the four general products, only the plain one supports the Peirce theory, and the reason is associativity.

**Theorem (the Peirce decomposition is the plain product's own).** For an idempotent $\tilde\Pi$ of the plain product the algebra splits as $\mathbb{B} = \mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_0-\tilde\Pi)$, and the two summands are left ideals; for the idempotents of the other three products no such decomposition is available, because the products are not associative, and it is the associativity that turns the Peirce corners into ideals.

**Proof.** The decomposition and the ideal structure are *Ideals and Peirce Decomposition of the General Plain Algebra*; the display $\tilde\Pi(e_0-\tilde\Pi) = 0$ of the previous section is the orthogonality the decomposition needs, and the associativity of the plain product is what makes the summands $\mathbb{B}\tilde\Pi$ and $\mathbb{B}(e_0-\tilde\Pi)$ left ideals, which the three other products fail.

The comparison is the last separation of the article, and it is the reason the plain product's idempotents are the idempotents of the algebra. The Hermitian idempotents of the general plain sesquilinear product act as projections on the positive cone and on the Hermitian module (*Idempotents of the General Plain Sesqualgebra*), the family of the fourth product is the family of idempotents of that product with central square $e_0$, and the natural product has neither, having only the trivial pair; the Hermitian idempotent of the algebra's Hilbert structure is the one fixed by the star, and it is an idempotent of the sesquilinear product while being an idempotent of the plain product.

## Summary

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* have four idempotent sets, all containing the trivial pair. The plain product, whose idempotents are the idempotents of the algebra, has the elements $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$: the trivial pair, the family $\tfrac12(e_0+i\hat\mu)$ of the Hermitian idempotents, and a four-parameter family lying in none of the four four-dimensional subspaces; the natural product has the trivial pair alone; the general plain sesquilinear product has the trivial pair and the Hermitian family; and the general quaternionic sesquilinear product has the trivial pair and the family $-\tfrac12e_0+\mu$ with $(\mu,\mu) = \tfrac34$.

The central square separates the sets: it is $e_0$ on $e_0$, $0$ on every nontrivial idempotent of the plain product and of the general plain sesquilinear product, and $e_0$ on the family of the fourth product. The idempotents of the four sets that are units of the algebra are therefore $e_0$ and the fourth product's family; the idempotents that are zero divisors are the nontrivial ones of the plain product and the Hermitian ones of the general plain sesquilinear product; and the natural product's set consists of the two units alone.

The families occupy the centre, $\mathbb{M}_+$, $\mathbb{H}_{\mathbb{B}}$ and no remarkable subspace, and the complementation $\tilde\Pi\mapsto e_0-\tilde\Pi$ pairs the members of the plain family, being available for the two products whose idempotent family it preserves — the plain product and the general plain sesquilinear product. The Peirce decomposition is the plain product's, because it needs associativity, and the comparison in one sentence is this: the plain product is the only one of the four whose idempotents build the algebra, the fourth product is the only one whose nontrivial idempotents are units, and the natural product is the only one with no nontrivial idempotent at all. The four sets themselves are tabulated in *Comparison Between the Four General Products*.

Read among the twelve structures the idempotent equation loses most of its solutions. The four antisymmetric structures have $0$ alone: the two bilinear ones have an identically vanishing square, and on the two sesquilinear ones the square is a purely imaginary pure vector that leaves only the origin; the three structures with a scalar-valued square, $\mathrm{GQA}$, $\mathrm{SQA}$ and $\mathrm{SPS}$, have the trivial pair; and five of the twelve, $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ and $\mathrm{SQS}$, carry a nontrivial idempotent, the last two sharing the family $-\tfrac12e_0+\mu$. The symmetric plain structure is the surprise of the list: its square is the plain square, so it carries the whole plain family although it is not associative.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi$ | an idempotent, $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ in the product at hand |
| $\tilde\Xi$ | a root of $-e_0$, $\tilde\Xi^{2} = -e_0$; trivial $\pm i$, real $\hat\mu$, or non-trivial $\mathbf p+i\mathbf p'$ |
| $\hat\mu$ | a real unit vector, $\hat\mu^{2} = -e_0$ |
| $\tilde\Pi_1(\hat\mu) = \tfrac12(e_0+i\hat\mu)$ | the Hermitian idempotents of the general plain sesquilinear product |
| $-\tfrac12e_0+\mu$ | the idempotents of the general quaternionic sesquilinear product, $(\mu,\mu) = \tfrac34$ |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space, the four general ones and their eight symmetric and antisymmetric parts |

## Further Reading

- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the tabulation of the four idempotent sets and the four square-root problems.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the idempotents of the algebra, their bijection with the roots of $-e_0$ and their role in the Peirce decomposition.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the three families of roots of $-e_0$.
- *Idempotents of the General Quaternionic Algebra* (`articles_maths/idempotents-of-the-general-quaternionic-algebra.md`), for the trivial pair of the natural product.
- *Idempotents of the General Plain Sesqualgebra* (`articles_maths/idempotents-of-the-general-plain-sesqualgebra.md`), for the Hermitian family and its projections.
- *Idempotents of the General Quaternionic Sesqualgebra* (`articles_maths/idempotents-of-the-general-quaternionic-sesqualgebra.md`), for the family of units.
- *Ideals and Peirce Decomposition of the General Plain Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra.md`), for the decomposition the plain idempotents carry.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the positive cone on whose boundary the Hermitian idempotents lie.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the criterion that the central square not vanish, which the table applies.
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the remarkable subspaces and the products on them.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the four general products and their symmetric and antisymmetric parts.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve names and the class of each.
- *Idempotents of the Symmetric Plain Algebra* (`articles_maths/idempotents-of-the-symmetric-plain-algebra.md`), for the block whose idempotents are the idempotents of the algebra, the whole plain family and the Jordan Peirce decomposition.
- *Idempotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/idempotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the family $-\tfrac12e_0+\mu$ as a two-sphere in the real quaternion subspace.
- *Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the trivial pair of the scalar-valued square.
