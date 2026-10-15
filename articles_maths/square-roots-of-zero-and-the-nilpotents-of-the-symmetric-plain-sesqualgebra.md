# __Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ on the biquaternion space (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article determines the **roots of zero**, the nonzero elements $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = 0$, and then the **nilpotents**, the elements some power of which vanishes. The order is fixed: the roots of zero come first and the nilpotents after. The two differ, and the difference is the index; the root of zero asks the **square** to vanish and is empty, while the nilpotent asks **some power** to vanish and forms the vector subspace of index three.

The reduction is the one of *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, stated there for a general central value and quoted here for the value zero. The square of an element is central, $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$ a real non-negative number (*Norm and Invertibility in the Symmetric Plain Sesqualgebra*), so the equation $\tilde\Xi\star\tilde\Xi = 0$ reads $H(\tilde\Xi) = 0$, whose only solution is the origin. The **square-zero elements** are therefore the origin alone, and the block has **no nilpotent of index two**. The class is nonempty at **index three**: the cube is $(P\star P)\star P = H(P)\overline{P_0}e_0$, and it vanishes exactly when the scalar coordinate vanishes. The nilpotents are the elements of the **vector subspace** $\mathrm{Vect}(\mathbb{B}) = \{P_0 = 0\}$, of complex dimension three, each nonzero one of index three, and no other element is nilpotent of any index.

**Placement.** The article is the sixth entry of the *Common Theory* section of the block, after the roots of one and the idempotents, and before the general element. It uses the product and the class of the introduction, the algebraic norm and the square map of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, the reduction and the emptiness of the root set of zero of *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, and the punctured-space zero-divisor set of *Zero Divisors of the Symmetric Plain Sesqualgebra*.

**Boundaries.** The product, its class and its placement are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the relative definition of the nilpotent, of the index and of the square-zero element, and the bracketing of the powers, are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the root is defined there too. The nilpotents of the parent and their identification with the pure family of the zero divisors are *Nilpotents of the General Plain Algebra* and *Zero Divisors of the General Plain Algebra*; the square-zero sets of the four general products are *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Comparison Between the Four General Products*. The idempotents of the block are *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*. The model used here is *The Symmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu = Q_0e_0 + \vec Q$ with $Q_0\in\mathbb{C}$ and $\vec Q = \sum_{k=1}^{3}Q_ke_k$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu\varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is

$$
\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0, \qquad H(\tilde P,\tilde Q) = \sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$

and the algebraic norm is $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$. A root is written $\tilde\Xi$, a nilpotent $\tilde\Upsilon$, the vector subspace is $\mathrm{Vect}(\mathbb{B}) = \{Q_0 = 0\}$, and the central line is $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$.

**The results.** The root equation $\tilde\Xi\star\tilde\Xi = 0$ has the single solution $\tilde\Xi = 0$, so the root set of $0$ is empty and the block has no nonzero square-zero element. An element is nilpotent of the block if and only if its scalar coordinate vanishes, so the nilpotent set is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three and real dimension six. Every nonzero nilpotent has index three, its square being the nonzero central element $H(\tilde\Upsilon)e_0$ and its cube vanishing, while the square-zero elements are the origin alone, so the block has no nilpotent of index two, four or more. The nilpotent set is a linear subspace and not a cone, it is stable under the three conjugations, and every nonzero nilpotent is a two-sided zero divisor whose annihilator is the hyperplane $\tilde\Upsilon^{\perp}$.

## The Root of Zero

**There is no root of $0$: the equation reads $H(\tilde\Xi) = 0$, whose only solution is the origin, which the definition of a root excludes; the root set of $0$ is empty and the block has no nonzero square-zero element.**

**The reduction.** The square of an element is central, $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$ real and non-negative, and the root equation $\tilde\Xi\star\tilde\Xi = \lambda e_0$ reduces to the scalar equation $H(\tilde\Xi) = \lambda$; the reduction and its proof are *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, and it is quoted here for $\lambda = 0$.

**Definition (recalled).** A **root of $0$** in the block is a nonzero element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = 0$; a root of $0$ is a nonzero **square-zero element**, and the root set of $0$ is the set of the nonzero square-zero elements. The definition is that of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, read on the product $\star$.

**Theorem (no root of $0$).** The equation $\tilde\Xi\star\tilde\Xi = 0$ has the single solution $\tilde\Xi = 0$, so the block has no nonzero square-zero element and the root set of $0$ is empty.

*Proof.* The reduction reads $H(\tilde\Xi) = 0$, and the algebraic norm vanishes only at the origin; a root is required to be nonzero, so the set is empty.

**Remark (square-zero elements and nilpotents).** The block has no square-zero element, hence no nilpotent of index two; the index three exists nevertheless, and the nilpotents of the block are the subject of the rest of this article. The two statements are not in conflict: a nilpotent of index three carries a nonzero square and a vanishing cube, and its square is the central element $H(\tilde\Upsilon)e_0\neq0$.

## The Definition Relative to the Product

**Definition (recalled).** An element $\tilde\Upsilon$ is **nilpotent of the block** when some power of it vanishes, $\tilde\Upsilon^{\star k} = 0$ for some $k\geq1$, the least such $k$ being the **index of nilpotency**; an element of index two, $\tilde\Upsilon\star\tilde\Upsilon = 0$, is a **square-zero element**. The definition is that of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, read on the product $\star$; the origin is the trivial nilpotent, of index one, and the article is concerned with the others.

**The bracketing of the powers.** The block is not associative, $(X\star Y)\star Z = \overline{Z_0}H(X,Y)e_0$ against $X\star(Y\star Z) = X_0H(Z,Y)e_0$, so the power needs a bracketing; the definition uses the **left-nested reading**

$$
\tilde P^{\star k} = \bigl(\cdots\bigl((\tilde P\star\tilde P)\star\tilde P\bigr)\cdots\star\tilde P\bigr),
$$

and the right-nested reading is a different expression. For the block the two readings agree on **vanishing**, as §*The Cube* shows, so the nilpotent set does not depend on the convention.

## The Cube

**The left-nested and the right-nested cubes are $(P\star P)\star P = H(P)\overline{P_0}e_0$ and $P\star(P\star P) = H(P)P_0e_0$, central and conjugate, and both vanish exactly when the scalar coordinate $P_0$ vanishes or $P = 0$.**

**Theorem (the cube).** For every $\tilde P = P_0e_0 + \vec P$,

$$
(\tilde P\star\tilde P)\star\tilde P = H(\tilde P)\,\overline{P_0}\,e_0, \qquad \tilde P\star(\tilde P\star\tilde P) = H(\tilde P)\,P_0\,e_0,
$$

so the left-nested and the right-nested cubes vanish together, exactly when $P_0 = 0$ or $\tilde P = 0$.

*Proof.* The square is $\tilde P\star\tilde P = H(\tilde P)e_0$. Multiplying on the right by $\tilde P$, $H(\tilde P)e_0\star\tilde P = H(\tilde P)H(e_0,\tilde P)e_0 = H(\tilde P)\overline{P_0}e_0$; multiplying on the left, $\tilde P\star H(\tilde P)e_0 = H(\tilde P)H(\tilde P,e_0)e_0 = H(\tilde P)P_0e_0$. The scalar $H(\tilde P)$ is positive unless $\tilde P = 0$, so each cube vanishes exactly when the remaining factor vanishes.

**Corollary (the cube is central and of the first degree).** Both cubes are central, and each is the coefficientwise conjugate of the other; the two displays are the two readings of the same vanishing condition and neither is a square.

## The Nilpotent Set

**An element is nilpotent of the block if and only if its scalar coordinate vanishes, so the nilpotent set is the vector subspace $\mathrm{Vect}(\mathbb{B}) = \{P_0 = 0\}$, of complex dimension three, and every nonzero nilpotent has index three and no nilpotent has index four or more.**

**Theorem (the classification).** An element $\tilde\Upsilon$ is nilpotent of the block if and only if its scalar coordinate vanishes,

$$
\tilde\Upsilon\in\mathrm{Vect}(\mathbb{B}) = \{\tilde P = P_0e_0 + \vec P : P_0 = 0\},
$$

the vector subspace of complex dimension three. Every nonzero nilpotent has index three, and the block has no nilpotent of index four or more.

*Proof.* Let $\tilde P = P_0e_0 + \vec P$. If $P_0 = 0$ then $(\tilde P\star\tilde P)\star\tilde P = H(\tilde P)\overline{P_0}e_0 = 0$ by the cube, while $\tilde P\star\tilde P = H(\tilde P)e_0$ is nonzero as soon as $\tilde P\neq0$, so the index is exactly three. If $P_0\neq0$, then the powers are

$$
\tilde P^{\star k} = H(\tilde P)\,\overline{P_0}^{\,k-2}\,e_0 \qquad (k\geq2),
$$

the case $k = 2$ reading $H(\tilde P)e_0$ and the case $k = 3$ the cube above; the factor $H(\tilde P)\neq0$ and the power $\overline{P_0}^{\,k-2}\neq0$ never vanish, so no power vanishes, and the block has no nilpotent off the vector subspace. The index is three, so no index four or more occurs.

**Corollary (the nilpotent set is a subspace, not a cone).** The nilpotents of the block form the complex vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three and real dimension six; it is stable under addition and under complex scaling, it contains the origin, and it is not the isotropic cone of any form. The nilpotents of the parent form the pure part of the isotropic cone $C(\tilde P) = 0$, a cone of complex dimension two (*Nilpotents of the General Plain Algebra*); the block's set is a different algebraic set, a linear one, and the two are not related by the transfer of a classification.

**Remark (the block's genuine index three).** The square-zero set of the parent's sesquilinear product is $\{0\}$ (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*), so the block inherits no square-zero element from it; the index-three nilpotents are the block's own, and they are the reason the definition of the nilpotent needs the index and not only the square. The comparison of indices is the point of the present article and of the table of *Comparison Between the Four General Products*.

## The Index of Nilpotency

**The index theory of the block has only two indices: one, the trivial nilpotent $0$, and three, every nonzero element of $\mathrm{Vect}(\mathbb{B})$; the middle index two is empty.**

| element | powers | index |
|---|---|---|
| $0$ | $0$ | one, the trivial nilpotent |
| a nonzero element of $\mathrm{Vect}(\mathbb{B})$, $P_0 = 0$ | $\tilde P$, $H(\tilde P)e_0\neq0$, $0$, $0,\dots$ | three |
| an element with $P_0\neq0$ | $\tilde P$, $H(\tilde P)e_0$, $H(\tilde P)\overline{P_0}e_0$, $H(\tilde P)\overline{P_0}^{2}e_0,\dots$, never $0$ | none |

The table is the whole index theory of the block: two indices occur, one and three, and the middle index two is empty. The gap is the consequence of the definiteness: the square is a positive central element, and the third power is that element multiplied by the scalar coordinate, which is the only coordinate that can carry the vanishing.

**Corollary (the power string).** A nilpotent of the block has the finite string $\tilde\Upsilon,\tilde\Upsilon^{\star2} = H(\tilde\Upsilon)e_0,\tilde\Upsilon^{\star3} = 0$ of three terms, with the middle term nonzero; a non-nilpotent has the infinite string $\tilde P^{\star k} = H(\tilde P)\overline{P_0}^{\,k-2}e_0$ for $k\geq2$, the central element at each step being the previous one multiplied by the fixed scalar $\overline{P_0}$.

## The Nilpotents and the Zero Divisors

**Every nonzero nilpotent is a two-sided zero divisor, annihilating itself only in the cube, $\tilde\Upsilon^{\star3} = 0$, and its two annihilators are the same hyperplane $\tilde\Upsilon^{\perp}$ of complex dimension three.**

**Proposition (every nonzero nilpotent is a zero divisor).** Every nonzero nilpotent of the block is a two-sided zero divisor, and every nilpotent annihilates itself on both sides in the cube, $\tilde\Upsilon^{\star3} = 0$.

*Proof.* Every nonzero element of the block is a zero divisor (*Zero Divisors of the Symmetric Plain Sesqualgebra*), and a nilpotent is either the origin, which is not a zero divisor, or nonzero. The cube statement is the theorem on the cube.

**Remark (the implication and the two parents).** The implication "nilpotent implies zero divisor" holds in the block, and it holds immediately: the zero-divisor set is the whole punctured space, so every nonzero element already qualifies. It holds for the plain product too, where the nilpotents are the square-zero elements, that is the pure family of the zero-divisor cone (*Nilpotents of the General Plain Algebra*); and it holds vacuously for the plain sesquilinear product, whose only square-zero element is the origin (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*) and which therefore has no nonzero nilpotent at all. What the block and the two parents do not share is the shape and the size of the two sets: the block has the nilpotent subspace of complex dimension three inside the punctured space of complex dimension four, the plain product has the pure cone of complex dimension two inside its zero-divisor cone of complex dimension three, and the sesquilinear parent has the origin alone inside that same cone.

**Remark (the annihilator of a nilpotent).** The right and the left annihilators of a nonzero nilpotent $\tilde\Upsilon$ are the same hyperplane $\tilde\Upsilon^{\perp} = \{\tilde X : H(\tilde\Upsilon,\tilde X) = 0\}$, of complex dimension three; the nilpotent does not lie in its own annihilator unless it is isotropic, which for a definite form means it is zero, so a nonzero nilpotent is not in its annihilator and the self-annihilation is only at the cube and not at the square (*Zero Divisors of the Symmetric Plain Sesqualgebra*).

## The Nilpotents and the Idempotents

**The two classes meet only at the origin: away from it the nilpotents lie in the vector subspace and the idempotents are $e_0$, and $e_0$ is not nilpotent of any index.**

**Proposition (the two classes are disjoint and complementary).** No element of the block is both nilpotent and idempotent except the origin, which is the trivial nilpotent and an idempotent; away from the origin the nilpotents lie in the vector subspace and the idempotents are $e_0$.

*Proof.* The idempotents are $0$ and $e_0$ (*Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*); the nilpotents are the vector subspace. The intersection of $\{0,e_0\}$ with $\mathrm{Vect}(\mathbb{B})$ is $\{0\}$, since $e_0$ is not in the vector subspace.

**Remark (the idempotent $e_0$ is not nilpotent).** The element $e_0$ has $e_0^{\star k} = e_0$ for every $k$, so it is not nilpotent of any index; the two classes are the two ends of the power behaviour, the idempotent with a constant string of period one and the nilpotent with a finite string of three terms.

## The Conjugations

**The three conjugations carry the nilpotent set to itself and carry a nilpotent of index three to a nilpotent of index three.**

**Proposition (the nilpotents are conjugation-stable).** The three conjugations carry the nilpotent set to itself, and each carries a nilpotent of index three to a nilpotent of index three.

*Proof.* The natural conjugation, the coefficientwise conjugation and the Hermitian conjugation all preserve the scalar coordinate up to the coefficient, carrying the vector subspace $\{P_0 = 0\}$ to itself; the index is carried because the conjugation is compatible with the product up to the coefficientwise conjugation, $(\tilde P\star\tilde Q)^{*} = \overline{\tilde P\star\tilde Q} = \tilde Q\star\tilde P$, and a vanishing power is carried to a vanishing power.

**Corollary (the two real structures and the automorphism).** The natural conjugation is $\mathbb{C}$-linear and acts on a nilpotent by negating its vector part, $\tilde\Upsilon^{\natural} = -\tilde\Upsilon$; the coefficientwise conjugation conjugates its coordinates and fixes the vanishing scalar coordinate $0$; and the Hermitian conjugation, their composite, is antilinear. The nilpotent set is therefore a complex subspace carrying the two antilinear involutions $\overline{\cdot}$ and ${}^{*}$ as real structures, and the class is stable under all three conjugations.

## The Matrix Model

**In the $2\times2$ model the product is the trace-halving pairing and the nilpotents of the block are the matrices of trace-coordinate zero, the cube vanishing exactly with the scalar coordinate and not with the matrix.**

**The $2\times2$ representation.** In the realization $M_2(\mathbb{C})$ of *The Symmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, the product is the trace-halving $\tilde P\star\tilde Q = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr)I_2$, and the cube of the model is

$$
\mathsf{M}_2(\tilde\Upsilon^{\star3}) = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde\Upsilon)\mathsf{M}_2(\tilde\Upsilon)^{\dagger}\bigr)\overline{\Upsilon_0}\,I_2,
$$

the matrix form of the cube $H(\tilde\Upsilon)\overline{\Upsilon_0}e_0$; the nilpotents of the block are the matrices of trace-coordinate zero, that is the traceless part of the model with respect to the basis of *The Symmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*. The model records the index-three vanishing as the vanishing of the scalar coordinate and not of the matrix.

## The Nilpotents and the Remarkable Subspaces

**The nilpotent set is a subspace, so it meets each remarkable subspace in the elements of that subspace with vanishing scalar coordinate: the centre meets it only at the origin, the vector subspace is the whole nilpotent set, and the quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces each meet it in a real three-dimensional subspace.**

The nilpotent set is a subspace, so its intersection with a remarkable subspace is read at once: the nilpotents that a subspace contains are its elements with vanishing scalar coordinate, and the intersection is again a subspace.

**Proposition (the nilpotents inside each remarkable subspace).** On the six remarkable subspaces, the nilpotents that each contains are

| remarkable subspace $S$ | real dimension | nilpotents in $S$ | real dimension |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ | $2$ | $\{0\}$ | $0$ |
| $\mathrm{Vect}(\mathbb{B}) = \{P_0 = 0\}$ | $6$ | $S$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $\{q_1e_1+q_2e_2+q_3e_3 : q_k\in\mathbb{R}\}$ | $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $\{q_1ie_1+q_2ie_2+q_3ie_3 : q_k\in\mathbb{R}\}$ | $3$ |
| $\mathbb{M}_+$ | $4$ | $\{q_1ie_1+q_2ie_2+q_3ie_3 : q_k\in\mathbb{R}\}$ | $3$ |
| $\mathbb{M}_-$ | $4$ | $\{q_1e_1+q_2e_2+q_3e_3 : q_k\in\mathbb{R}\}$ | $3$ |

*Proof.* The nilpotents are the vector subspace $\{P_0 = 0\}$, so the intersection is the hyperplane condition read inside $S$. On the centre the scalar coordinate is free and the only element with $P_0 = 0$ is the origin. On the vector subspace the condition is the defining one and the intersection is the whole subspace. On the quaternion and the Hermitian subspaces the scalar coordinate is real, and on the anti-quaternion and the anti-Hermitian subspaces it is purely imaginary; in each of the four the vanishing of the scalar coordinate is one real linear condition on a real four-dimensional space, leaving real dimension three. The surviving part is the real span of the three vector generators, $e_1,e_2,e_3$ in the quaternion and anti-Hermitian rows and $ie_1,ie_2,ie_3$ in the anti-quaternion and Hermitian rows.

**Remark (a subspace meets a subspace; the contrast with the zero divisors).** The nilpotent set meets every remarkable subspace in a subspace and never in a punctured set, because it is itself linear; the zero-divisor set, being the complement of the origin, meets every subspace in its punctured self (*Zero Divisors of the Symmetric Plain Sesqualgebra*). The two questions are answered by two different objects, a hyperplane condition and a non-vanishing condition, and only the first has a preferred subspace, in the sense that the centre contains no nonzero nilpotent while the other five all do.

## Summary

The square of an element of the symmetric plain sesqualgebra is $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$ a real non-negative definite number, so the equation of the root $\tilde\Xi\star\tilde\Xi = \lambda e_0$ reduces to the scalar equation $H(\tilde\Xi) = \lambda$ (*Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*). At $\lambda = 0$ the reduction reads $H(\tilde\Xi) = 0$, whose only solution is the excluded origin: **there is no root of $0$**, the **square-zero elements** are the origin alone, and the block has no nilpotent of index two. The nilpotents are the elements of the **vector subspace** $\mathrm{Vect}(\mathbb{B}) = \{P_0 = 0\}$, of complex dimension three, and each nonzero one has **index three**: the square is the central element $H(\tilde\Upsilon)e_0$, nonzero, and the cube $(P\star P)\star P = H(P)\overline{P_0}e_0$ vanishes exactly with the scalar coordinate. The middle index is empty and the block carries the two indices one and three. The root of $0$ and the nilpotent class therefore differ, the root asking the square to vanish and the nilpotent asking a power to vanish, and the difference is the index. Every nonzero nilpotent is a two-sided zero divisor, and here the implication is immediate, the zero-divisor set being the whole punctured space; the sesquilinear parent, whose only square-zero element is the origin, carries no nonzero nilpotent at all. The nilpotents are conjugation-stable, the idempotent $e_0$ is never nilpotent, and the nilpotent set is a linear subspace and not a cone, in contrast with the pure cone that is the nilpotent set of the parent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, real and non-negative |
| $\mathcal{R}(0) = \varnothing$ | no nonzero root of $0$ |
| $\{0\}$ | the square-zero elements, the origin alone |
| $\tilde\Upsilon^{\star2} = H(\tilde\Upsilon)e_0$ | the square, always central, never zero off the origin |
| $(P\star P)\star P = H(P)\overline{P_0}e_0$ | the cube, vanishing exactly with $P_0$ |
| $\mathrm{Vect}(\mathbb{B}) = \{P_0 = 0\}$ | the nilpotent set, a complex subspace of dimension three |
| $\tilde P^{\star k} = H(\tilde P)\overline{P_0}^{\,k-2}e_0$, $k\geq2$ | the power string of the left-nested reading |
| index three | the index of every nonzero nilpotent |
| $\tilde\Upsilon^{\perp}$ | the annihilator of a nonzero nilpotent, a hyperplane |
| $S\cap\mathrm{Vect}(\mathbb{B})$ | the nilpotents inside a remarkable subspace $S$, a subspace |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and its placement.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the relative definition of the root, of the nilpotent, of the index, of the square-zero element and of the bracketing of the powers.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the algebraic norm, the square map and the definiteness.
- *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the reduction of the root equation and the emptiness of the root set of $0$.
- *Square Roots of a General Element in the Symmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-plain-sesqualgebra.md`), for the general reduction the present one specialises.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`), for the punctured-space zero-divisor set and the annihilators.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`), for the pure-cone nilpotents of the parent and the index-two theorem there.
- *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the square-zero set $\{0\}$ of the parent sesquilinear product.
- *The Symmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the model in which the cube is read.
- *Remarkable Subspaces under the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the subspaces whose intersection with the nilpotent set is read here.
