# __The Operators: One-Sided, Two-Sided, Sandwich__

## Introduction

An element of the biquaternion algebra acts on the algebra in three ways. The **left multiplication** $L_{\tilde Q}(X)=\tilde Q X$ and the **right multiplication** $R_{\tilde Q}(X)=X\tilde Q$ act on one side; the **sandwich** $\operatorname{H}_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}$ acts on both. The first two are linear in their parameter and carry an element; the third is quadratic and carries a frame. This article is the operator article of the *Algebra* block. It states what the three families are, how they compose, which form each is adjoint for, and what the differences mean physically.

The organising distinction is between **carriage** and **frame change**. A one-sided multiplication drags an object without compensating the other side: it changes the scale, and in general the sector, of what it acts on. A sandwich acts on both sides at once and preserves the two sectors; it is the algebraic shape of a change of frame. The physical Lorentz transformation is a sandwich, not a multiplication. The mass term, by contrast, is a right multiplication, and that is why it can move between the two chiralities while a left multiplication cannot.

The article reads the operator calculus of the general plain product and then crosses to the other structures. The mathematics is owned by *One-Sided Operators on the Biquaternion Algebra*, *Two-Sided Operators on the Biquaternion Algebra*, *Association and the Transpose on the Quaternion Algebra*, *The Operators of the Bilinear Product*, *The Monoid of Acting Maps*, *The Operators of the Twelve Structures* and *Ideals and the Peirce Decomposition*. The physics is the reading given below, with its boundaries stated at the end.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The left and right multiplications, their kernels and their images | [One-Sided Operators on the Biquaternion Algebra](../articles_maths/one-sided-operators-on-the-biquaternion-algebra.html) |
| The two-sided operators, their types and their composition | [Two-Sided Operators on the Biquaternion Algebra](../articles_maths/two-sided-operators-on-the-biquaternion-algebra.html) |
| The transpose, association and the swap of the sides | [Association and the Transpose on the Quaternion Algebra](../articles_maths/association-and-the-transpose-on-the-quaternion-algebra.html) |
| The operator calculus of the general plain product | [The Four General Products and Operators](../articles_maths/the-four-general-products-and-operators.html) |
| The monoid of acting maps and the enveloping algebra | [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html) |
| The sandwich as the map $X\mapsto MXM^{\dagger}$ | [The Four General Products and Operators](../articles_maths/the-four-general-products-and-operators.html) |
| The sandwich as a product of the two regular maps | [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), §*The Sandwich in the Regular Basis* |
| The action of the sandwich on the remarkable subspaces | [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |
| The Peirce decomposition and the four corners | [Ideals and Peirce Decompositions of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), [Hermitian Idempotents and the Peirce Decomposition](../articles_maths/hermitian-idempotents-and-the-peirce-decomposition.html) |

## The Three Families

The three families are defined by the side on which the parameter stands:

$$
L_{\tilde Q}(X)=\tilde Q X, \qquad R_{\tilde Q}(X)=X\tilde Q, \qquad \operatorname{H}_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}=L_{\tilde Q}R_{\tilde Q^{*}}(X).
$$

| Family | Parameter dependence | What it carries | Kernel | Image |
| --- | --- | --- | --- | --- |
| $L_{\tilde Q}$ | linear | an element acting on the left | $\{0\}$ if $\tilde Q$ is a unit; otherwise $\{X:\tilde QX=0\}$ | $\tilde Q\mathbb{B}$, a right ideal |
| $R_{\tilde Q}$ | linear | an element acting on the right | $\{0\}$ if $\tilde Q$ is a unit; otherwise $\{X:X\tilde Q=0\}$ | $\mathbb{B}\tilde Q$, a left ideal |
| $\operatorname{H}_{\tilde Q}$ | quadratic | a frame acting on both sides | $\{0\}$ if $\tilde Q$ is a unit; otherwise $\{X:\tilde QX\tilde Q^{*}=0\}$ | $\tilde Q\mathbb{B}\tilde Q^{*}$ |

All three maps are $\mathbb{C}$-linear in the argument $X$. The assignments are injective in the parameter: $L_{\tilde Q}=0$, $R_{\tilde Q}=0$ or $\operatorname{H}_{\tilde Q}=0$ forces $\tilde Q=0$. They are not all injective as assignments of operators: $L_{\tilde Q}=L_{\tilde U}$ iff $\tilde Q=\tilde U$, but $\operatorname{H}_{\tilde Q}=\operatorname{H}_{\tilde U}$ can hold for different parameters, because a central phase cancels.

The physical reading of the table is the first distinction of the article. A one-sided map has a nontrivial kernel in its argument exactly when the parameter is not a unit; it is the operator of **carriage**, the map that composes an operation with an object. The sandwich is the operator of **frame change**, and its parameter is defined only up to a central phase. The next three sections make the distinction precise.

## The Composition Laws

The one-sided maps compose by multiplying their parameters:

$$
L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}, \qquad R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}, \qquad L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}.
$$

The reversal in the right family is the anti-automorphism of the composition of maps: $(R_{\tilde A}R_{\tilde B})(X)=X\tilde B\tilde A=R_{\tilde B\tilde A}(X)$. The left and right families commute, because multiplication in the algebra is associative.

The two-sided maps compose by the rule

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)\bigl(L_{\tilde C}R_{\tilde D}\bigr)=L_{\tilde A\tilde C}R_{\tilde D\tilde B},
$$

and the sandwich is the special case in which the right parameter is the Hermitian conjugate of the left:

$$
\boxed{\;\operatorname{H}_{\tilde Q}\operatorname{H}_{\tilde U}=\operatorname{H}_{\tilde Q\tilde U}\;}.
$$

The sandwich is therefore multiplicative in its parameter. It is not linear: $\operatorname{H}_{\lambda\tilde Q}=|\lambda|^2\operatorname{H}_{\tilde Q}$, and $\operatorname{H}_{\tilde Q+\tilde U}\neq\operatorname{H}_{\tilde Q}+\operatorname{H}_{\tilde U}$ in general. It is a quadratic map that happens to preserve composition, a representation of the unit group modulo its central phase circle rather than a linear one.

The assignment $\tilde Q\mapsto\operatorname{H}_{\tilde Q}$ has kernel the central phase circle on the unit group. If $|\lambda|=1$ then $\operatorname{H}_{\lambda\tilde Q}=\operatorname{H}_{\tilde Q}$, so the phase is invisible to the operator. There is no further kernel: $\operatorname{H}_{\tilde Q}=0$ forces $\tilde Q=0$ by evaluating at $e_t$.

The one-sided families generate the full endomorphism algebra. Every $\mathbb{C}$-linear map of $\mathbb{B}$ is a sum of products $L_{\tilde A}R_{\tilde B}$, and the left regular and right regular matrices together span $M_4(\mathbb{C})$. The sandwich alone does not: it is an eight-real-parameter family of maps, not a sixteen-real-parameter algebra, and the linear span of the family is not the whole endomorphism algebra.

## The Adjoint and the Swap

The operator calculus has four adjoints in the corpus, one for each of the four forms. The one that belongs to this article is the adjoint for the general plain bilinear form

$$
\langle X,Y\rangle=\operatorname{Sc}(XY),
$$

which is symmetric and has Gram matrix $\operatorname{diag}(1,-1,-1,-1)$. Its adjoint is the **associate**, written $T^{\approx}$, and it is computed by one cyclic move of the scalar part:

$$
\langle L_{\tilde Q}X,Y\rangle=\operatorname{Sc}(\tilde QXY)=\operatorname{Sc}(XY\tilde Q)=\langle X,R_{\tilde Q}Y\rangle.
$$

Hence

$$
\bigl(L_{\tilde Q}\bigr)^{\approx}=R_{\tilde Q}, \qquad \bigl(R_{\tilde Q}\bigr)^{\approx}=L_{\tilde Q}, \qquad \bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}R_{\tilde A}.
$$

The adjoint **swaps the sides and does not conjugate the parameter**. This is the property that separates it from the three other adjoints of the corpus: the Hermitian dagger keeps the side and conjugates the parameter, $(L_{\tilde Q})^{*}=L_{\tilde Q^{*}}$; the quaternionic adjoint keeps the side and conjugates by ${}^{\natural}$; and the signed Hermitian adjoint reverses the side and conjugates by the coefficientwise conjugation.

The type criteria follow from the swap. A left multiplication is self-adjoint exactly when $R_{\tilde Q}=L_{\tilde Q}$, that is exactly when $\tilde Q$ is central. A nonzero one-sided operator is never skew-adjoint: $L_{\tilde Q}=-R_{\tilde Q}$ forces $\tilde Q=0$ by evaluating at $e_t$. A nonzero two-sided operator $L_{\tilde A}R_{\tilde B}$ is self-adjoint exactly when the two parameters are proportional over $\mathbb{C}$, and it is never skew-adjoint unless it is zero.

The physical reading is the absence of orientation in the measuring pairing. The plain form pairs two displacements and returns a number; it does not know which factor is on the left. The orientation of a process is in the antisymmetric part $XY-YX$, the commutator, and not in the form. The form therefore measures the symmetric data and leaves the orientation to the commutator.

This adjoint is **not** the physical adjoint of the observables. Self-adjointness for $\langle\cdot,\cdot\rangle$ is not hermiticity; the observables and the gauge generators are the self-adjoint and skew-adjoint operators for the Hermitian form of the sesquilinear block, and they are owned by the state articles. The distinction is one of the boundaries of the article.

## The Two-Sided Operator as a Pair

A two-sided operator is a pair of parameters, and only the relative data of the pair are physical. The identity is

$$
\boxed{\;L_{\tilde A}R_{\tilde B}=\mathrm{id}
\iff \tilde A\tilde B=e_t \ \text{and}\ \tilde A\ \text{central}
\iff (\tilde A,\tilde B)=(\lambda e_t,\lambda^{-1}e_t),\quad \lambda\in\mathbb{C}^{\times}\;}.
$$

For invertible parameters, more generally,

$$
L_{\tilde A}R_{\tilde B}=L_{\tilde C}R_{\tilde D}
\iff \tilde C=\lambda\tilde A,\quad \tilde D=\lambda^{-1}\tilde B,
$$

so the pair is defined up to a common central factor. The physical statement is that a frame change is specified by an operand and its adjoint operand, and a common central phase cancels between them. The pair, not either member of it, is the physical object.

The cancelling factor is the same fact that makes the sandwich phase-blind. In the sandwich the pair is $(\tilde Q,\tilde Q^{*})$, and the common factor is a central phase; in a general two-sided operator the pair is $(\tilde A,\tilde B)$ and the common factor is any central unit. The group of two-sided operators that are invertible is the image of $\mathbb{B}^{\times}\times\mathbb{B}^{\times}$ modulo the central pairs $(\lambda e_t,\lambda^{-1}e_t)$.

The two-sided operator is invertible exactly when both parameters are units. If either parameter is a zero divisor the operator has a nontrivial kernel: if $\tilde A$ is invertible the kernel is $\{X:X\tilde B=0\}$, and if $\tilde B$ is invertible it is $\{X:\tilde AX=0\}$. This is the operator-level form of the zero-divisor cone: the non-invertible two-sided maps are exactly those whose pair meets the cone.

## The Sandwich

The sandwich is the two-sided operator whose right parameter is the Hermitian conjugate of the left. It has three properties that the general two-sided operator does not.

**It preserves the two sectors.** For $X\in\mathbb{M}_\pm$,

$$
(\tilde Q X\tilde Q^{*})^{*}=\tilde Q X^{*}\tilde Q^{*}=\pm\,\tilde Q X\tilde Q^{*},
$$

so the image lies in the same sector. A general two-sided operator does not preserve the sectors. This is why the Lorentz transformation of a four-vector is a sandwich and not a general two-sided map.

**It is a congruence.** In the matrix picture it is $X\mapsto MXM^{\dagger}$, which preserves rank off the cone, scales the determinant by $\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$, and collapses to a rank-one line on the cone. The general two-sided operator is not a congruence and has no such rank theorem.

**It is self-adjoint for the Hermitian form exactly when its parameter is a phase multiple of a sector element.** For the Hermitian form $\langle X,Y\rangle_{*}=\operatorname{Sc}(X^{*}Y)$,

$$
\bigl(\operatorname{H}_{\tilde Q}\bigr)^{\dagger}=\operatorname{H}_{\tilde Q^{*}},
$$

so $\operatorname{H}_{\tilde Q}$ is self-adjoint iff $\tilde Q^{*}=\lambda\tilde Q$ for some $|\lambda|=1$, equivalently iff a central-phase multiple of $\tilde Q$ lies in $\mathbb{M}_+$ or $\mathbb{M}_-$. Since the sandwich does not see the phase, the criterion is a criterion on the class of $\tilde Q$. It is skew-adjoint only at $\tilde Q=0$. The criterion is algebraic; it does not by itself make the self-adjoint sandwiches observables. A Lorentz boost is a Hermitian parameter, hence lies in $\mathbb{M}_+$, and gives a self-adjoint sandwich, and it is a transformation, not an observable. The physical identification of the self-adjoint class is made in the state articles and not here.

On the null cone the sandwich survives as a rank-one map. Its image is the line spanned by $\tilde Q\tilde Q^{*}$, a Hermitian element whose normalisation is a minimal idempotent. If $Q_t=0$ the sandwich is nilpotent; if $Q_t\neq0$ it is a scaled projection. The two cases are the two faces of the cone: the absence of energy and the presence of a null momentum.

### The Sandwich, the Inner Automorphism and the Scale

The sandwich is an inner automorphism exactly on the **unitary slice**. When $\tilde Q\tilde Q^{*}=e_t$, the inverse is $\tilde Q^{*}$, and

$$
\operatorname{H}_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}=\tilde Q X\tilde Q^{-1}
$$

is the inner automorphism $\operatorname{Ad}_{\tilde Q}$: it preserves the product, not only the interval. The Lorentz parameters are not this slice in general. They satisfy $\tilde Q\tilde Q^{\natural}=e_t$, and for a boost $\tilde Q^{*}=\tilde Q$ while $\tilde Q^{-1}=\tilde Q^{\natural}$, so the sandwich is a **congruence**, not a similarity. The two maps agree on the rotations, where the parameter is a real unit quaternion and $\tilde Q^{*}=\tilde Q^{\natural}=\tilde Q^{-1}$; they differ on the boosts, where $\tilde Q$ is Hermitian, $\tilde Q^{*}=\tilde Q$ and $\tilde Q^{-1}=\tilde Q^{\natural}$. The sandwich is then the congruence that acts on the four-vectors: the parameter $\exp(u i\vec e_z)$ produces the boost of rapidity $2u$.

Off the unit-norm slice the sandwich is a congruence with a scale. The norm is multiplicative and the star conjugates it,

$$
\langle\operatorname{H}_{\tilde Q}(X)\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\,\langle X\rangle_{\natural}\,\langle\tilde Q^{*}\rangle_{\natural}=|\langle\tilde Q\rangle_{\natural}|^{2}\langle X\rangle_{\natural}.
$$

The scale is the squared modulus of the norm. In the polar word $\lvert\langle\tilde Q\rangle_{\natural}\rvert=r^{2}$, so the conformal factor of the sandwich is $r^{4}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$: the fourth power of the word's scale, and the square of the norm. On a four-momentum the norm is $-m^{2}c^{2}$, so the scale is $m^{4}c^{4}$; the mass is the modulus of the norm, not the scale. The phrase *the inner automorphism scaled by the norm* is exact on the unitary slice, where the scale is one and the map preserves the product. On the Lorentz slice the norm is one as well, but the map is a congruence: it preserves the interval and not the product.

**The boundary.** The identification fails where $\tilde Q^{*}\neq\tilde Q^{-1}$. A Lorentz parameter satisfies the norm-one condition; a boost is not unitary, and it is the counterexample. The sandwich is always a congruence; it is a similarity only on the unitary slice.

## The Central Phase and the State Space

A central phase acts as a scalar matrix on the element and as the identity on the sandwich:

$$
\operatorname{H}_{e^{i\alpha}\tilde Q}=\operatorname{H}_{\tilde Q}, \qquad \operatorname{H}_{e^{i\alpha}}=\mathrm{id}.
$$

The phase is therefore invisible to the operator and visible to the norm, the determinant and the module. The physical reading is that a global phase is not an operation on states; only the relative phase, carried by the vector part, is observable. The polar word keeps the phase because the word is a description of the element and not of the operator; the sandwich keeps the frame and the scale, and loses only the phase.

The scale is half-visible: a one-sided multiplication by a real scale $r$ dilates by $r$, while the sandwich dilates by $r^2$. The factor is the one-slot versus two-slot bookkeeping. It is the same factor of two that appears between the boost factor and the acting rotor in the polar decomposition.

## The Mass Coupling

The left multiplication preserves each minimal left ideal. In the adapted basis of the regular matrix it is block diagonal, so no left multiplication can carry an element of one chirality into the other. The right multiplication by a nilpotent can. With the standard pair

$$
\vec\Upsilon_1=\tfrac12(i\vec e_x-\vec e_y), \qquad \vec\Upsilon_2=\tfrac12(i\vec e_x+\vec e_y),
$$

one has $\vec\Upsilon_1^2=\vec\Upsilon_2^2=0$ and

$$
\tilde\Pi_+\vec\Upsilon_1=\vec\Upsilon_1, \qquad \tilde\Pi_-\vec\Upsilon_1=0,
$$

so the right multiplication by $\vec\Upsilon_1$ maps the first column onto the second and annihilates the second. It is the off-diagonal block that the left regular matrix does not have.

The physical reading is the mass coupling. The mass term of the biquaternionic Dirac equation is chirality-off-diagonal: it couples the left and right spinors. A left multiplication cannot do that; a right multiplication by the nilpotent can. The mass term is therefore a right action, and the algebraic reason is the block structure of the regular representation. The nilpotent is not a small parameter: it is exact, and its square is zero, so two mass couplings in the same direction vanish. The corpus reads the pair $\vec\Upsilon_1,\vec\Upsilon_2$ as the truncated ladder elements, with $\vec\Upsilon_1\vec\Upsilon_2=\tilde\Pi_+$ and $\vec\Upsilon_2\vec\Upsilon_1=\tilde\Pi_-$.

### The Missing Rows of the Dictionary

The worked examples cover the central dilation, the vector rotation by $\pi$ and the boost. Four further rows complete the dictionary; each is a reading of the same sandwich, not a new operator.

| acting element | the sandwich | the reading |
| --- | --- | --- |
| $i\tilde Q_2$ with $\tilde Q_2$ real | the same sandwich as $\tilde Q_2$, with the same scale | the rotor with its phase frozen |
| Hermitian of norm $-1$, e.g. $i\vec u$ with $\lvert\vec u\rvert=1$ | the rotation by $\pi$ about $\vec u$; the general case adds the polar boost | a boost composed with a $\pi$-rotation |
| material $\tilde R$ | the same family as $\mathbb{M}_+$, through $i\tilde R$ | the four-vector action |
| unit-norm slice | an isometry; it moves the ledger and leaves the phase alone | the frame change |

The first row is exact because $i$ is central: $(i\tilde Q_2)^{*}=-i\tilde Q_2^{*}$, so the two factors $i$ cancel in the sandwich. The second row is the negative-norm Hermitian case: $\tilde Q=i\vec u$ has $\langle\tilde Q\rangle_{\natural}=-1$ and $\tilde Q^{2}=e_t$, so the sandwich is $i\vec u\,X\,i\vec u=-\vec u X\vec u=\vec u X\vec u^{-1}$, the rotation by $\pi$ about $\vec u$. The corpus reads the general negative-norm element as a boost composed with that rotation. The third row is the identity $\operatorname{H}_{i\tilde R}=\operatorname{H}_{\tilde R}$ for material $\tilde R$, because $(i\tilde R)^{*}=i\tilde R$; the material four-vector and its Hermitian representative $i\tilde R$ produce the same sandwich. The fourth row is the unit-norm slice: it is the isometry group, and it preserves the sector and the interval.

The last two rows are why the temporal exchange and the material transformation theory are separate. Multiplication by the central $i$ exchanges the sectors and reverses the norm; a unit-norm sandwich preserves the sector and the norm. The central phase is invisible to the sandwich: the sandwich carries the modulus and not the argument. The two operations belong to different columns of the dictionary, and neither is a dynamics.

**The boundary.** The rows are readings of one sandwich, not four new operators. The negative-norm row uses the Hermitian representative; a general negative-norm element is read through the polar decomposition. The phase-frozen row is exact for an imaginary quaternion, where the central phase is a global factor.

## The Monoid of Acting Maps

The left multiplications form a monoid under composition, isomorphic to the multiplicative monoid of $\mathbb{B}$:

$$
L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}, \qquad L_{e_t}=\mathrm{id}.
$$

The monoid is associative, the order matters, the identity is the unit, and the reversible elements are the units of the algebra, that is the elements off the zero-divisor cone. The right multiplications form the opposite monoid, and the two-sided maps form a monoid whose units are the pairs of units.

The physical reading is the **process–state split**. A process is an acting map: it composes, it can be undone exactly when it is a unit, and the reversible processes form a group. A state is an idempotent: it is the fixed point of a projection and it is not a map of the same kind. The algebra supplies both in one object, and the cone is the boundary between the reversible and the irreversible.

The monoid is not a $C^{*}$-algebra. It has no involution that makes it one, it is not closed under sums, and the operator norm is not part of its structure. The idempotents are not given a trace rule by it, and the kernel of an acting map is not a measurement. A measurement needs a projection onto a state, which is the idempotent side, and the passage from an invertible map to a non-invertible one is the collapse, not the mere vanishing of the norm.

## The Peirce Decomposition

Relative to a Hermitian idempotent $\tilde\Pi$ ($\tilde\Pi^2=\tilde\Pi=\tilde\Pi^{*}$), the algebra splits into four corners:

$$
\boxed{\;X=\tilde\Pi X\tilde\Pi+\tilde\Pi X(1-\tilde\Pi)+(1-\tilde\Pi)X\tilde\Pi+(1-\tilde\Pi)X(1-\tilde\Pi)\;}.
$$

In the block matrix form,

$$
X=\begin{pmatrix}\tilde\Pi X\tilde\Pi & \tilde\Pi X(1-\tilde\Pi)\\ (1-\tilde\Pi)X\tilde\Pi & (1-\tilde\Pi)X(1-\tilde\Pi)\end{pmatrix}.
$$

The two diagonal corners are the **populations** and the two off-diagonal corners are the **coherences**. The Hermitian conjugation fixes the populations and exchanges the coherences. The Peirce decomposition is the operator-level form of the state/observable split: the idempotent is the two-outcome observable, with eigenvalues $0$ and $1$, and the four corners are the four ways an element can sit relative to it.

The left multiplication by $\tilde\Pi$ keeps the first row of the block matrix and kills the second; the right multiplication by $\tilde\Pi$ keeps the first column and kills the second. The minimal left ideals are the column supports, and left multiplication preserves them. The right multiplication by the nilpotent moves between them. The Peirce decomposition is therefore the structural reason the mass coupling is a right action: the left action preserves each column ideal, and the right action is the one that can carry an element from one to the other.

The frame is the axis of the observable up to sign. The Hermitian roots of $+1$ give the observable-driven frames and form the real projective plane $\mathbb{RP}^2$; the non-Hermitian roots give algebraically valid frames that no observable of square one carries; the trivial roots give the degenerate frame. The algebra supplies one block structure and selects no frame: all frames are conjugate by an inner automorphism.

## The Operators of the Twelve Structures

The twelve structures of the *Biquaternion Algebraic Structures* category are twelve products on one vector space. Each product attaches its own left and right multiplications, and each form attaches its own adjoint. The operator algebra with a unit exists only for the general plain bilinear product, the associative unital row.

| Structure | Product | The operator content |
| --- | --- | --- |
| General plain bilinear | $\tilde Q_1\tilde Q_2$ | the full monoid of left multiplications; the operator algebra with a unit |
| General quaternionic bilinear | $\tilde Q_1^{\natural}\tilde Q_2$ | left multiplications with a left unit only; the interval |
| General plain sesquilinear | $\tilde Q_1\tilde Q_2^{*}$ | the Hermitian adjoint; the observables and the positive form |
| General quaternionic sesquilinear | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the Krein adjoint; the gauge form and the sandwich |

The other eight structures are the symmetric and antisymmetric halves of these four. The symmetric halves compose; the antisymmetric halves give brackets and derivation algebras. The crossing reader *The Operators of the Twelve Structures* owns the comparison, and this article declares only the general plain column.

The physical reading of the table is the ladder of the corpus. Composition is the process; probability is the positive form on which the observables are read; causality is the interval and the oriented composition; gauge is the indefinite metric whose operators compose through the sandwich. The twelve rows are twelve ways one element of a frame can act on another, and only one of them supplies a unit for the composition.

## Worked Examples

**A central scalar.** For $\tilde Q=z e_t$ with $z\neq0$, the left and right multiplications coincide, $L_{ze_t}=R_{ze_t}=z\,\mathrm{id}$, and the sandwich is $\operatorname{H}_{ze_t}=|z|^2\mathrm{id}$. The operator is a dilation by $|z|^2$; it is invertible, of rank four, and self-adjoint for the plain form for every $z$, real or complex. Self-adjointness for the plain form therefore does not imply reality: the form is complex-bilinear, and every central scalar is self-adjoint.

**A vector.** For $\tilde Q=\vec e_x$, the left multiplication is a complex structure, $L_{\vec e_x}^2=-\mathrm{id}$, and the sandwich is $\operatorname{H}_{\vec e_x}(X)=-\vec e_x X\vec e_x$, a rotation by $\pi$ on the vector part. Both are invertible and of rank four. The left multiplication is neither self-adjoint nor skew-adjoint for the plain form, because $\vec e_x$ is not central and is not zero; the sandwich is self-adjoint, because $\vec e_x^{*}=-\vec e_x$.

**A null element.** For $\tilde Q=e_t+i\vec e_x$, of norm zero, the two-sided operator is not invertible. The left multiplication has rank two and a two-dimensional kernel, the right multiplication has rank two and a two-dimensional kernel, and the sandwich has rank one. Its image is the line of

$$
\tilde Q\tilde Q^{*}=\tilde Q^{2}=2(e_t+i\vec e_x),
$$

and the sandwich is the scaled projection $\operatorname{H}_{\tilde Q}^2=4\operatorname{H}_{\tilde Q}$. The element is a zero divisor, and the operator is the algebraic shape of the loss of rank.

**A boost.** For $\tilde Q=\tfrac53e_t+\tfrac43 i\vec e_z$, of norm one, the sandwich has eigenvalues $9,1,1,\tfrac19$, determinant one and trace $\tfrac{100}{9}$. The parameter is Hermitian, so the sandwich is self-adjoint for the Hermitian form, and it is a Lorentz boost and not an observable. The example is the shortest warning that the algebraic type criterion and the physical classification are not the same statement.

## Limits

The article states the operator calculus of the general plain product and declares the other rows. It does not re-prove the composition laws, which belong to *The Monoid of Acting Maps*, and it does not re-read the sandwich on the remarkable subspaces, which belongs to *The Operators: One-Sided, Two-Sided, Sandwich*.

The monoid of acting maps is not a $C^{*}$-algebra. The kernel of an acting map is not a measurement. The idempotents are states only when the physical reading of the state articles is supplied; the algebra alone gives them no probability rule.

The plain adjoint is a transpose, not the Hermitian adjoint. Self-adjointness for the plain form is not hermiticity, and the physical observables are not the self-adjoint elements of this article's family.

The sandwich is multiplicative in its parameter but quadratic and phase-blind. It loses the central phase and nothing else: the scale, the boost axis and the rotor are recoverable from it up to that phase. A physical statement that needs the phase cannot be read off the sandwich alone.

The twelve structures are not one calculus. Only the general plain bilinear row has an enveloping operator algebra with a unit; the other rows have multiplications, adjoints and brackets, and the crossing reader owns their comparison.

## Summary

- An element acts in three ways: left multiplication, right multiplication and the sandwich $\operatorname{H}_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}$.
- The one-sided maps are linear in the parameter and carry an element; the sandwich is quadratic and carries a frame.
- The one-sided composition laws are $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$ and $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$; the two families commute.
- The two-sided maps compose by $L_{\tilde A}R_{\tilde B}L_{\tilde C}R_{\tilde D}=L_{\tilde A\tilde C}R_{\tilde D\tilde B}$; the sandwich is multiplicative, $\operatorname{H}_{\tilde Q}\operatorname{H}_{\tilde U}=\operatorname{H}_{\tilde Q\tilde U}$.
- The sandwich is not linear; $\operatorname{H}_{\lambda\tilde Q}=|\lambda|^2\operatorname{H}_{\tilde Q}$, and as an assignment its kernel on the unit group is the central phase circle.
- The adjoint for the plain form swaps the sides and leaves the parameter alone; self-adjoint one-sided operators are exactly the central multiplications.
- The plain form measures the symmetric data; the orientation of a process is in the commutator.
- A two-sided operator is a pair defined up to a common central factor; the identity is the pair $(\lambda e_t,\lambda^{-1}e_t)$.
- The sandwich preserves the two sectors, is a congruence, and is self-adjoint for the Hermitian form exactly when a central-phase multiple of its parameter lies in $\mathbb{M}_+$ or $\mathbb{M}_-$ ($\tilde Q^{*}=\lambda\tilde Q$, $|\lambda|=1$).
- The sandwich is an inner automorphism on the unitary slice; on the Lorentz slice it is a congruence, and off the unit-norm slice it scales the interval by $\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$.
- The dictionary has four further rows: the imaginary quaternion (phase frozen), the negative-norm element (boost with a $\pi$-rotation), the material sector (through $i\tilde R$), and the unit-norm slice (frame change).
- On the null cone the sandwich collapses to a rank-one line; the nilpotent and the scaled projection are its two faces.
- The central phase is invisible to the sandwich and visible to the norm; the scale is seen squared, not once.
- Right multiplication by the nilpotent $\vec\Upsilon_x$ moves between the two chiralities; this is why the mass term is a right action.
- The acting maps form a monoid, not a $C^{*}$-algebra; the reversible maps are the units off the cone, the states are the idempotents, and a kernel is not yet a measurement.
- The Peirce decomposition gives the four corners: populations on the diagonal, coherences off it.
- The operator algebra with a unit exists only for the general plain bilinear row; the other eleven structures have operators but not that algebra.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $L_{\tilde Q}(X)=\tilde Q X$ | the left multiplication |
| $R_{\tilde Q}(X)=X\tilde Q$ | the right multiplication |
| $\operatorname{H}_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}$ | the sandwich, the Hermitian two-sided operator |
| $T^{\approx}$ | the associate, the adjoint for the plain form $\langle X,Y\rangle=\operatorname{Sc}(XY)$ |
| $T^{\dagger}$ | the Hermitian adjoint, the adjoint for $\langle X,Y\rangle_{*}=\operatorname{Sc}(X^{*}Y)$ |
| $\lambda$ | a central scalar, the cancelling factor of a two-sided pair |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$ | the nilpotent that implements the chirality flip |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the minimal idempotents, the two chiralities |
| $\mathbb{M}_\pm$ | the material and informational sectors |
| $\operatorname{Ad}_{\tilde Q}$ | the inner automorphism $X\mapsto \tilde Q X\tilde Q^{-1}$ |
| $\mathcal{P}_J$ | the $J$-positive cone of the Krein article |

## Further Reading

- [One-Sided Operators on the Biquaternion Algebra](../articles_maths/one-sided-operators-on-the-biquaternion-algebra.html), for the kernels, the images and the one-sided types.
- [Two-Sided Operators on the Biquaternion Algebra](../articles_maths/two-sided-operators-on-the-biquaternion-algebra.html), for the pair structure and the type criteria.
- [Association and the Transpose on the Quaternion Algebra](../articles_maths/association-and-the-transpose-on-the-quaternion-algebra.html), for the adjoint that swaps the sides.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the monoid, the enveloping algebra and the two-sided maps.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the four corners and the frames.
- [Hermitian Idempotents and the Peirce Decomposition](../articles_maths/hermitian-idempotents-and-the-peirce-decomposition.html), for the Hermitian corners and the state/observable split.
- [The Physical Interpretation of the 12 Products](the-physical-interpretation-of-the-12-products.html), for the crossing table of the twelve structures.
- [The Complementary Ideal and the Second State Space](the-complementary-ideal-and-the-second-state-space.html), for the corners in full.
- [The Element and Operator Representations](the-element-and-operator-representations.html), for the pictures in which these operators are matrices.
