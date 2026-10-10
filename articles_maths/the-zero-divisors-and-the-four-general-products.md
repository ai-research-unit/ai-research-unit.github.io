# __The Zero Divisors and the Four General Products__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*), $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$. A zero divisor is defined by an equation that names one of them: an element is a zero divisor of a product when that product lets a nonzero element be annihilated by it. Nothing in the definition is shared between the four products, and four different sets are what one expects. In the biquaternion algebra they coincide, and the whole of the difference between the four zero-divisor theories lies in the annihilators. The coincidence is a computed fact about this algebra, proved below; it is not a definition and not a property of a product with a conjugation in general.

This article establishes that fact and separates three things that are easily conflated. The **set** of zero divisors is the one point on which the four products agree: the four sets coincide, and each is the nonzero part of the vanishing set of the central square, $\{c = 0\}$. The **annihilator** of a fixed zero divisor is not common, and the four products attach eight planes to one element. The **inverse** of an element is not common either, because a unit in the two-sided sense exists in one product alone. The classical equivalence of ring theory, zero divisor if and only if not a unit, therefore holds for the plain product alone; for the other three it is replaced by the criterion that the two one-sided inverse equations have no solution, a criterion that reads the same in all four products.

The general form of the definitions used here — the zero divisor, the annihilator, the idempotent, the nilpotent and the rest, stated once for a general product and read on the products of the space — is *Definitions for the Study of the 12 Algebraic Structures*; this article is the four-product computation and the coincidence, and it keeps the definition read on the four.

The central square, its four multiplicative laws and the annihilators of a fixed element are *The Annihilating Elements of the Four General Products*. The two families of zero divisors, the pure and the non-pure, and the cone they form are *Zero Divisors of the General Plain Algebra*. The property table of the four products, the four idempotent sets and the four unit structures are *Comparison Between the Four General Products*. The isomorphism used here is *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, the norm and the invertibility criterion are *Biquaternion Norm and Invertibility*, and the position of the zero divisors in the remarkable subspaces is *Introduction to the Remarkable Subspaces*.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$, $i^2 = -1$; a general element is $\tilde Q = \sum_{\mu=0}^{3}Q_\mu e_\mu = Q_0 e_0 + \mathbf Q$ with $Q_0\in\mathbb{C}$ and $\mathbf Q = \sum_{k=1}^{3}Q_k e_k$. The natural conjugation is $\tilde Q^{\natural} = Q_0 - \mathbf Q$, the star is $\tilde Q^{*} = \overline{Q_0} - \overline{\mathbf Q}$, so that ${}^{*} = \bar{\cdot}\circ{}^{\natural}$. The unit of the algebra is written both $1$ and $e_0$; it is fixed by ${}^{\natural}$ and by ${}^{*}$. The **central square** is

$$
\tilde Q\tilde Q^{\natural} = \tilde Q^{\natural}\tilde Q = c(\tilde Q)e_0 , \qquad c(\tilde Q) = \sum_{\mu=0}^{3}Q_\mu^{2} ,
$$

and $(\mathbf P,\mathbf Q) = \sum_k P_kQ_k$ is the general plain bilinear form of the two vector parts. The four general products are written $f$ when the argument is common to all four.

## The Definition Names a Product

### Left, Right and Two-Sided

**Definition.** Let $f$ be one of the four general products and let $\tilde P\in\mathbb{B}$. The element $\tilde P$ is a **left zero divisor of $f$** when $\tilde P\neq0$ and there is a nonzero $\tilde X$ with $f(\tilde P,\tilde X) = 0$; it is a **right zero divisor of $f$** when $\tilde P\neq0$ and there is a nonzero $\tilde X$ with $f(\tilde X,\tilde P) = 0$; and it is a **zero divisor of $f$** when it is one or the other.

The word is the ring one: a left zero divisor sits on the left of the element it annihilates, and a right zero divisor on the right. The origin is excluded on both sides, and it is excluded from every set below.

### The Four Equations

Written out, the definition of a left zero divisor is one of

$$
\tilde P\tilde X = 0 , \qquad \tilde P^{\natural}\tilde X = 0 , \qquad \tilde P\tilde X^{*} = 0 , \qquad \tilde P^{\natural}\tilde X^{*} = 0 ,
$$

and the definition of a right zero divisor is one of

$$
\tilde X\tilde P = 0 , \qquad \tilde X^{\natural}\tilde P = 0 , \qquad \tilde X\tilde P^{*} = 0 , \qquad \tilde X^{\natural}\tilde P^{*} = 0 .
$$

The eight equations differ only in the product, and each of them names it. The eight conditions they define are therefore four pairs of candidate sets, one pair to a product, and nothing yet says that the four pairs coincide.

### The Two One-Sided Multiplications

The two conditions of a product are the kernels of its two one-sided multiplications. For a product $f$ and an element $\tilde P$ put

$$
L_f(\tilde P) : \tilde X\mapsto f(\tilde P,\tilde X) , \qquad R_f(\tilde P) : \tilde X\mapsto f(\tilde X,\tilde P) .
$$

**Proposition.** For each of the four products $f$ and each $\tilde P$, the element $\tilde P$ is a left zero divisor of $f$ exactly when $\ker L_f(\tilde P)\neq0$, and a right zero divisor of $f$ exactly when $\ker R_f(\tilde P)\neq0$.

**Proof.** The two statements are the definitions read through the two maps, with the nonzero solutions of the two equations as the nonzero vectors of the two kernels. Both kernels are complex subspaces: the maps are real-linear, and a map whose variable slot carries the star is conjugate-linear there, a conjugation that preserves vanishing. $\square$

The maps $L_f(\tilde P)$ and $R_f(\tilde P)$ are real-linear maps of the eight-dimensional real space $\mathbb{B}$ to itself, and a real-linear map of a finite-dimensional real space is injective exactly when it is surjective. The two kernels are therefore zero together with the failure of bijectivity, and the two-sided condition of a zero divisor is the failure of either one of the two maps to be bijective.

## The Zero Divisors of One Product

**Theorem (the criterion for a fixed product).** Let $f$ be one of the four general products and let $\tilde P\neq0$. Then the following three conditions are equivalent:

1. $\tilde P$ is a left zero divisor of $f$;
2. $\tilde P$ is a right zero divisor of $f$;
3. $c(\tilde P) = 0$.

Moreover $\ker L_f(\tilde P)$ is a complex plane, of complex dimension two, exactly when $c(\tilde P) = 0$, and it is zero exactly when $c(\tilde P)\neq0$; the same holds for $\ker R_f(\tilde P)$.

**Proof.** Read the four products in the model $\mathbb{B}\cong M_2(\mathbb{C})$. Let $\Phi$ be the isomorphism, with $\Phi(\tilde P) = P_0\mathrm{I}_2 - iP_1\sigma_1 - iP_2\sigma_2 - iP_3\sigma_3$ on the basis, $\Phi(\tilde P\tilde Q) = \Phi(\tilde P)\Phi(\tilde Q)$ and $\det\Phi(\tilde P) = c(\tilde P)$ (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*). The four left maps become, on the matrices,

$$
\Phi(\tilde P)\Phi(\tilde X) , \quad \Phi(\tilde P^{\natural})\Phi(\tilde X) , \quad \Phi(\tilde P)\Phi(\tilde X)^{*} , \quad \Phi(\tilde P^{\natural})\Phi(\tilde X)^{*} ,
$$

and the two right maps carry the same two factors in the other order. The maps $\tilde X\mapsto\Phi(\tilde X)$, $\tilde X\mapsto\Phi(\tilde X)^{*}$ and the two conjugations ${}^{\natural}$ and ${}^{*}$ of $\mathbb{B}$ are bijections, so the kernel of each of the eight maps is nonzero exactly when the matrix $\Phi(\tilde P)$ or the matrix $\Phi(\tilde P^{\natural})$ is singular. The two determinants are equal, $\det\Phi(\tilde P^{\natural}) = c(\tilde P^{\natural}) = c(\tilde P) = \det\Phi(\tilde P)$, and $\Phi(\tilde P)$ is singular exactly when $c(\tilde P) = 0$; this is the first equivalence and the second. A singular two-by-two matrix has rank one, its left and its right multiplication each carry a kernel of dimension two; a nonsingular matrix carries the zero kernel. $\square$

**Corollary (one set to a product).** For each of the four products the left zero divisors, the right zero divisors and the two-sided zero divisors are the same set, namely the nonzero elements of $\{c = 0\}$.

So no product distinguishes the left from the right. What a product may still do is distinguish its own set from the set of another product, and the next section shows that in the biquaternion algebra it does not.

## The Four Zero-Divisor Sets Coincide

**Theorem (the four sets coincide).** For the biquaternion algebra the four zero-divisor sets coincide. A nonzero element $\tilde P$ is a left, a right or a two-sided zero divisor of one of the four products exactly when $c(\tilde P) = 0$, and then it is a zero divisor of all four, on both sides.

**Proof.** Apply the criterion of the preceding section to the four products in turn. In each case the condition is $c(\tilde P) = 0$, read from the singularity of $\Phi(\tilde P)$ or of $\Phi(\tilde P^{\natural})$, whose determinants are the same. $\square$

The reason is structural and short, and it is a reason about the biquaternion algebra alone. Each of the four products is the plain product with a conjugation in one or both slots; each conjugation of $\mathbb{B}$ is a bijection that either fixes or conjugates the central square, $c(\tilde P^{\natural}) = c(\tilde P)$ and $c(\tilde P^{*}) = \overline{c(\tilde P)}$ (*The Annihilating Elements of the Four General Products*); and the central square is the single second-order invariant that decides the invertibility of the element. Composing a one-sided multiplication with a bijection leaves the kernel zero exactly when it was zero, so the four kernels vanish on the same elements and the four vanishing sets are one. The multiplicativity of the central square, $c(\tilde P\tilde Q) = c(\tilde P)c(\tilde Q)$ for the two bilinear products and $c(\tilde P\tilde Q) = c(\tilde P)\overline{c(\tilde Q)}$ for the two sesquilinear ones, is the same fact in the language of the products.

| product | condition for a left zero divisor | condition for a right zero divisor | the set |
|---|---|---|---|
| $\tilde P\tilde Q$ | $c(\tilde P) = 0$ | $c(\tilde P) = 0$ | $\{c = 0\}\setminus\{0\}$ |
| $\tilde P^{\natural}\tilde Q$ | $c(\tilde P) = 0$ | $c(\tilde P) = 0$ | $\{c = 0\}\setminus\{0\}$ |
| $\tilde P\tilde Q^{*}$ | $c(\tilde P) = 0$ | $c(\tilde P) = 0$ | $\{c = 0\}\setminus\{0\}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $c(\tilde P) = 0$ | $c(\tilde P) = 0$ | $\{c = 0\}\setminus\{0\}$ |

The four rows are identical, and that is the theorem. **The word is *coincide*, not *independent*.** The zero divisor is defined by an equation that names a product, so the notion belongs to the product, and the four products are four definitions, not one. What the theorem says is that for the biquaternion algebra the four definitions happen to select one and the same subset of $\mathbb{B}$; it does not say that the algebra carries a zero-divisor set of its own, apart from a product, and it does not carry to a general product with a conjugation. The two ingredients of the proof — that both conjugations are bijections of $\mathbb{B}$ and that one invariant, the central square, decides the singularity in all four — are facts about this algebra.

The table is also the reason the question is worth asking: the four rows of the comparison table of *Comparison Between the Four General Products* separate the four products on almost every other property, and they do not separate them here.

## What Does Depend on the Product

### The Annihilators of One Zero Divisor

Fix a zero divisor and ask which elements annihilate it. For a product $f$ write, for $\tilde P$ with $c(\tilde P) = 0$,

$$
A_f(\tilde P) = \{\tilde X : f(\tilde P,\tilde X) = 0\} , \qquad B_f(\tilde P) = \{\tilde X : f(\tilde X,\tilde P) = 0\} .
$$

These are the two kernels of the preceding sections, and each is a complex plane. The planes are not the same for the four products. On the element $\tilde P = e_0 + ie_1$, whose central square is $c(\tilde P) = 1 + i^2 = 0$, they are

| product | $A_f(\tilde P)$, the left annihilator | $B_f(\tilde P)$, the right annihilator |
|---|---|---|
| $\tilde P\tilde Q$ | $\mathbb{C}\{e_0 - ie_1,\ e_3 + ie_2\}$ | $\mathbb{C}\{e_0 - ie_1,\ e_3 - ie_2\}$ |
| $\tilde P^{\natural}\tilde Q$ | $\mathbb{C}\{e_0 + ie_1,\ e_3 - ie_2\}$ | $\mathbb{C}\{e_0 + ie_1,\ e_3 - ie_2\}$ |
| $\tilde P\tilde Q^{*}$ | $\mathbb{C}\{e_0 - ie_1,\ e_3 - ie_2\}$ | $\mathbb{C}\{e_0 - ie_1,\ e_3 - ie_2\}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $\mathbb{C}\{e_0 + ie_1,\ e_3 + ie_2\}$ | $\mathbb{C}\{e_0 + ie_1,\ e_3 - ie_2\}$ |

Four of the eight planes are distinct, the other four coinciding in pairs. The first generator is $\tilde P$ itself when the first slot carries the conjugation and $\tilde P^{\natural}$ when it does not; the second lies in the plane of $e_2$ and $e_3$, where it is $e_3 \pm ie_2$, the sign being fixed by the product and by the side. The two one-sided planes coincide for the natural product and for the general plain sesquilinear product, and they differ for the plain product and for the general quaternionic sesquilinear product, which is the reading of the theorem of *The Annihilating Elements of the Four General Products*. One set of elements, eight annihilators: the set is common to the four products, the annihilator is the product's own.

### The Square, the Idempotents and the Units

The annihilator is the first of four product-dependent readings that the common set does not determine, and the other three are recorded in *The Annihilating Elements of the Four General Products*. They are summarised here for completeness.

| reading | $\tilde P\tilde Q$ | $\tilde P^{\natural}\tilde Q$ | $\tilde P\tilde Q^{*}$ | $\tilde P^{\natural}\tilde Q^{*}$ |
|---|---|---|---|---|
| square-zero set | the pure cone $\{P_0 = 0,\ (\mathbf P,\mathbf P) = 0\}$ | the whole cone $\{c = 0\}$ | $\{0\}$ alone | the solutions of $\overline{\tilde P}\tilde P = 0$ |
| idempotent set | the plain family $\tfrac12(e_0 + \xi i)$ | $0$ and $e_0$ alone | the Hermitian idempotents | the family $-\tfrac12e_0 + \mu$ |
| unit | $e_0$, two-sided | $e_0$ on the left | $e_0$ on the right | none on either side |

Each of the three rows is a set of elements on which the four products disagree, and each of them is a set of elements of the zero-divisor cone or beside it. The zero-divisor set itself is the one row of the element theory on which they agree.

## Invertibility and the Zero Divisors

### The Units of the Four Products

A unit of a product is an element invertible in the two-sided sense, and the notion is available only when the product has a two-sided unit. Of the four general products one has a two-sided unit, two have one on a single side, and one has none; the entries are the unit rows of *Comparison Between the Four General Products*.

| product | $e_0$ is a left identity | $e_0$ is a right identity | two-sided unit |
|---|---|---|---|
| $\tilde P\tilde Q$ | yes | yes | yes |
| $\tilde P^{\natural}\tilde Q$ | yes | no | no |
| $\tilde P\tilde Q^{*}$ | no | yes | no |
| $\tilde P^{\natural}\tilde Q^{*}$ | no | no | no |

The three failures are one phenomenon: each of the three products inserts a conjugation into a slot, and a conjugation moves the candidate unit. The natural product reads the right factor through ${}^{\natural}$, so it keeps $e_0$ on the left and loses it on the right; the general plain sesquilinear product conjugates the right factor, so it keeps $e_0$ on the right and loses it on the left; and the fourth product carries a conjugation in each slot and keeps $e_0$ on neither side.

### The Equivalence for the Plain Product

For the plain product the classical equivalence is available and true.

**Theorem.** For the general plain bilinear product, and for a nonzero $\tilde P$, the following are equivalent: $\tilde P$ is a zero divisor; $c(\tilde P) = 0$; $\tilde P$ is not invertible.

**Proof.** The first equivalence is the criterion of the fixed product. For the second, the invertibility criterion of *Biquaternion Norm and Invertibility* states that $\tilde P$ is invertible exactly when $c(\tilde P)\neq0$. $\square$

In the model the statement is the standard one for $M_2(\mathbb{C})$: a matrix is a zero divisor exactly when it is nonzero and singular, and the two-sided invertible elements are the nonsingular matrices.

For the other three products the equivalence cannot be stated, since there is no two-sided unit and hence no group of units, and the elements are neither units nor non-units. What survives is the one-sided inverse, and it is decided by the central square in the same way for the four products.

### The One-Sided Inverse Equations

**Theorem (the inverse equations).** Let $f$ be one of the four general products and let $\tilde P\neq0$. Then $\tilde P$ is a zero divisor of $f$ exactly when neither of the two equations

$$
f(\tilde P,\tilde X) = e_0 , \qquad f(\tilde X,\tilde P) = e_0
$$

has a solution; equivalently, both equations have a solution exactly when $c(\tilde P)\neq0$.

**Proof.** If the equation $f(\tilde P,\tilde X) = e_0$ holds, then in the model the corresponding matrix equation is $\Phi(\tilde P)M = \mathrm{I}_2$ or $\Phi(\tilde P^{\natural})M = \mathrm{I}_2$ for an invertible $M$, so $\Phi(\tilde P)$ is invertible and $c(\tilde P)\neq0$. Conversely, if $c(\tilde P)\neq0$ then $\tilde P$ is invertible, and the four solutions are the ones of the table below. The two directions give the statement for the left equation, and the right equation is the same computation with the two factors in the other order. $\square$

The solutions are written with the inverse $\tilde P^{-1} = \tilde P^{\natural}/c(\tilde P)$ of the algebra, which exists for $c(\tilde P)\neq0$. The two conjugations commute, ${}^{\natural}\circ{}^{*} = {}^{*}\circ{}^{\natural} = \overline{\cdot}$, so the order of the two superscripts in the last row is immaterial.

| product | $\tilde X$ with $f(\tilde P,\tilde X) = e_0$ | $\tilde X$ with $f(\tilde X,\tilde P) = e_0$ |
|---|---|---|
| $\tilde P\tilde Q$ | $\tilde P^{-1}$ | $\tilde P^{-1}$ |
| $\tilde P^{\natural}\tilde Q$ | $(\tilde P^{-1})^{\natural}$ | $(\tilde P^{-1})^{\natural}$ |
| $\tilde P\tilde Q^{*}$ | $(\tilde P^{-1})^{*}$ | $(\tilde P^{-1})^{*}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $(\tilde P^{-1})^{*\natural}$ | $(\tilde P^{-1})^{*\natural}$ |

The criterion is the substitute for the missing equivalence: it uses the fixed element $e_0$, which is invariant under both conjugations, and it makes no appeal to a unit of the product. It reads the same in the four products, and it is the statement that the zero divisors are exactly the elements that cannot be inverted on either side.

## The Two Families

The zero divisors of $\mathbb{B}$ split into two families, and the split is read on the element and not on the product. An element is **pure** when its scalar part vanishes and **non-pure** when the scalar part is nonzero; the criterion $c(\tilde P) = 0$ then takes the two forms of *Zero Divisors of the General Plain Algebra*.

| | pure, $P_0 = 0$ | non-pure, $P_0\neq0$ |
|---|---|---|
| criterion | $(\mathbf P,\mathbf P) = 0$ | $c(\tilde P) = 0$ |
| square in the plain product | $\tilde P^{2} = 0$ | $\tilde P^{2} = 2P_0\tilde P$ |
| structure | the nilpotents | the complex multiples of the nontrivial idempotents |
| real dimension | $4$ | $6$ |

The two families are disjoint and their union is the zero-divisor set $\{c = 0\}\setminus\{0\}$, a complex cone of complex dimension three and real dimension six. Since the distinction is the vanishing of the scalar part, it is a distinction of the element, and it holds for the four products alike; what the product changes is the reading of the **square**, which is the first row of the table of the preceding section and is the reason the nilpotents of the plain product are not the square-zero elements of the other three. The pure zero divisor $e_1 + ie_2$ and the non-pure zero divisor $e_0 + ie_1$ are the two standard witnesses.

## The Matrix Model

In the model $\mathbb{B}\cong M_2(\mathbb{C})$ the whole picture is the linear algebra of a two-by-two complex matrix. The central square is the determinant,

$$
\det\Phi(\tilde P) = c(\tilde P) ,
$$

and the zero divisors are the nonzero singular matrices, that is the matrices of rank one (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*). Each of the eight one-sided multiplication maps is $\Phi(\tilde P)$ or its adjoint, multiplied on one side or the other by an invertible matrix, so each of the four products reads the same singularity. The rank-one matrix of a zero divisor is the outer product $\Phi(\tilde P) = uv^{T}$ determined up to $(\lambda u,\lambda^{-1}v)$, its two one-sided annihilators are the planes of the vectors orthogonal to $v$ and to $u$, and the collision of the two planes for the natural product and for the general plain sesquilinear product is the reading of the coincidences of the table of annihilators. The algebra's zero divisors are the rank-one matrices, the idempotents of the plain product are the rank-one projectors together with $0$ and $\mathrm{I}_2$, and the determinant is the invariant that decides all four products at once.

## The Zero Divisors and the Remarkable Subspaces

Whether a remarkable subspace contains zero divisors is the question of where the polynomial $c(\tilde P)$ vanishes on it, and the answer coincides for the four products because their sets coincide (*Introduction to the Remarkable Subspaces*).

| subspace | zero divisors |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | none |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | none |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | none |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | the nilpotent cone, of real dimension four |
| $\mathbb{M}_{+}$, the Hermitian subspace | a double cone |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | a double cone |

On the centre $c(\tilde P) = P_0^{2}$ vanishes only at the origin; on the two quaternion subspaces it is a sum of squares of real coefficients with a definite sign, and it vanishes only at the origin; on the vector subspace it is $(\mathbf P,\mathbf P)$, whose vanishing set is the pure cone of the nilpotents; and on the two Hermitian subspaces it is indefinite and cuts a double cone. A generic zero divisor lies in none of the remarkable subspaces. A zero divisor that lies in one of them is a zero divisor of all four products, like every other.

## Boundary: The Other Cone

The set $\{c = 0\}$ is a cone, and the chapter carries a second cone on the same space, the isotropic cone of the general plain bilinear form $\langle\tilde P,\tilde Q\rangle = \mathrm{Sc}(\tilde P\tilde Q)$. The two are different and must not be conflated: the diagonal of the central square is $P_0^{2} + (\mathbf P,\mathbf P)$ and the diagonal of the form is $P_0^{2} - (\mathbf P,\mathbf P)$, the two exchanges of the sign of the vector part. The element theory is built on the first and the geometry of the form on the second; the form and its isotropic cone are *The Four Pairings of the Biquaternion Algebra* and *Biquaternion Norm and Invertibility*, and the boundary is recorded here only to keep the two apart.

## Summary

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* define four notions of zero divisor, one to a product, and for the biquaternion algebra the four sets coincide — a coincidence of this algebra, proved here, not a definition. For each product a nonzero element is a left zero divisor if and only if it is a right zero divisor if and only if its central square vanishes, $c(\tilde P) = 0$; the criterion is the singularity of the matrix $\Phi(\tilde P)$ in the model $\mathbb{B}\cong M_2(\mathbb{C})$, and the conjugations that separate the four products are bijections that leave the central square alone or conjugate it. The zero divisors are therefore the nonzero elements of $\{c = 0\}$, a complex cone of complex dimension three and real dimension six, for the four products at once.

What differs from one product to the next is the annihilator of a fixed zero divisor: each product has two one-sided annihilators, each a complex plane, the eight planes collapsing to a smaller number of distinct ones and related by the two conjugations. What also differs is the square of an element, the idempotent equation and the unit; the four unit structures are one two-sided unit, one left unit, one right unit and none, so that the classical equivalence of ring theory, zero divisor if and only if not a unit, holds for the plain product alone. For the other three it is replaced by the criterion that the zero divisors are exactly the elements for which neither one-sided inverse equation $f(\tilde P,\tilde X) = e_0$ and $f(\tilde X,\tilde P) = e_0$ has a solution, a criterion that reads the same in the four products and invokes no unit.

The zero divisors split into the pure family, the nilpotents of real dimension four, and the non-pure family, the complex multiples of the nontrivial idempotents, of real dimension six. The split is a distinction of the element and is common to the four products; the reading of the square of a member of either family is not. Of the remarkable subspaces, the centre and the two quaternion subspaces contain no zero divisor, the vector subspace contains the nilpotent cone and the two Hermitian subspaces contain a double cone. The set $\{c = 0\}$ is not the isotropic cone of the general plain bilinear form, which is the other cone of the chapter. The annihilators themselves, with the central square and its four multiplicative laws, are the subject of *The Annihilating Elements of the Four General Products*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $f$ | a general one of the four general products |
| $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$ | the four general products |
| $L_f(\tilde P)$, $R_f(\tilde P)$ | the left and the right multiplication by $\tilde P$ for the product $f$ |
| $A_f(\tilde P)$, $B_f(\tilde P)$ | the two one-sided annihilators of $\tilde P$ for $f$ |
| $c(\tilde P) = \sum_\mu Q_\mu^{2}$ | the central square, $\tilde P\tilde P^{\natural} = c(\tilde P)e_0$ |
| $\{c = 0\}$ | the vanishing set of the central square, a complex cone of real dimension six |
| $\Phi$ | the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, with $\det\Phi(\tilde P) = c(\tilde P)$ |
| $\tilde P^{-1} = \tilde P^{\natural}/c(\tilde P)$ | the inverse of an element with $c(\tilde P)\neq0$ |
| pure, non-pure | scalar part zero, scalar part nonzero |

## Further Reading

- *The Annihilating Elements of the Four General Products* (`articles_maths/the-annihilating-elements-of-the-four-general-products.md`), for the central square, its four multiplicative laws and the eight annihilators of a fixed zero divisor.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the two families, the cone and the classification.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table, the four idempotent sets, the four square-root problems and the four unit entries.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four definitions and their scalar–vector forms.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm form and the invertibility criterion.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism, the determinant and the rank-one elements.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the general plain bilinear form and its isotropic cone.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the subspaces and the zero divisors they contain.
