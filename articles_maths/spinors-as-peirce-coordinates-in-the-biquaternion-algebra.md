# __Spinors as Peirce Coordinates in the Biquaternion Algebra__

## Introduction

A **spinor** of the biquaternion algebra $\mathbb{B}$ is an element of one of the two Peirce spaces

$$
S_{+}=\mathbb{B}\tilde\Pi_{+}=\mathbb{B}_{++}\oplus\mathbb{B}_{-+},\qquad
S_{-}=\mathbb{B}\tilde\Pi_{-}=\mathbb{B}_{+-}\oplus\mathbb{B}_{--},
$$

where $\tilde\Pi_{+},\tilde\Pi_{-}$ is a nondegenerate complete family of idempotents and $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$ are the four Peirce lines. The family fixes the two spaces and their splitting into a diagonal line and a mixed line. The diagonal line is spanned by the idempotent; the mixed line has no canonical generator. A Peirce basis chooses one, and the choice is the gauge of *The Peirce Basis of the Biquaternion Algebra*. The spinor is the algebra element; its Peirce coordinates are its coefficients in the adapted basis. The coordinates depend on the basis, the element does not.

The article defines the two spaces and their canonical splitting, gives the adapted bases and the gauge action, computes the ladder by the mixed units, identifies the invariants of a single spinor, reads the Peirce index as a right index, treats right multiplication and the exchange, and says what the spinor is not. An example is given at the end.

## The Two Spinor Spaces

**Definition.** The two **spinor spaces** of the family are

$$
S_{+}=\mathbb{B}\tilde\Pi_{+},\qquad S_{-}=\mathbb{B}\tilde\Pi_{-}.
$$

They are the two Peirce columns of the family: $S_{+}=\mathbb{B}_{++}\oplus\mathbb{B}_{-+}$ and $S_{-}=\mathbb{B}_{+-}\oplus\mathbb{B}_{--}$.

**Proposition.** $\mathbb{B}=S_{+}\oplus S_{-}$.

**Proof.** Every $\tilde Q\in\mathbb{B}$ is

$$
\tilde Q=\tilde Q(\tilde\Pi_{+}+\tilde\Pi_{-})=\tilde Q\tilde\Pi_{+}+\tilde Q\tilde\Pi_{-}\in S_{+}+S_{-}.
$$

If $\xi\in S_{+}\cap S_{-}$, then $\xi=\eta_{+}\tilde\Pi_{+}=\eta_{-}\tilde\Pi_{-}$; multiplying on the right by $\tilde\Pi_{+}$ gives $\xi=\eta_{+}\tilde\Pi_{+}=\eta_{-}\tilde\Pi_{-}\tilde\Pi_{+}=0$. So the sum is direct.

**The left action.** Left multiplication by any $\tilde Q\in\mathbb{B}$ preserves each $S_{\pm}$, because $\tilde Q(\xi\tilde\Pi_{\pm})=(\tilde Q\xi)\tilde\Pi_{\pm}$. This is the action of the algebra on the spinor spaces. It is the algebra product.

## The Canonical Splitting

**Proposition.** The family splits each spinor space into a diagonal line and a mixed line:

$$
S_{+}=\mathbb{C}\tilde\Pi_{+}\oplus\mathbb{B}_{-+},\qquad
S_{-}=\mathbb{B}_{+-}\oplus\mathbb{C}\tilde\Pi_{-}.
$$

**Proof.** For $\psi_{+}\in S_{+}$, insert $\tilde\Pi_{+}+\tilde\Pi_{-}=e_{t}$ on the left:

$$
\psi_{+}=(\tilde\Pi_{+}+\tilde\Pi_{-})\psi_{+}=\tilde\Pi_{+}\psi_{+}+\tilde\Pi_{-}\psi_{+}.
$$

The first term lies in $\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_{+}$ and the second in $\mathbb{B}_{-+}$. The sum is direct because the two lines have different left indices. The proof for $S_{-}$ is the same with the signs exchanged.

**The intrinsic form of a spinor.** Every positive spinor has a unique form

$$
\psi_{+}=a\tilde\Pi_{+}+\nu_{+},\qquad a\in\mathbb{C},\quad \nu_{+}\in\mathbb{B}_{-+},
$$

and every negative spinor has a unique form

$$
\psi_{-}=\nu_{-}+d\tilde\Pi_{-},\qquad \nu_{-}\in\mathbb{B}_{+-},\quad d\in\mathbb{C}.
$$

The coefficient $a$ is the scalar such that $\tilde\Pi_{+}\psi_{+}=a\tilde\Pi_{+}$, and $\nu_{+}=\psi_{+}-a\tilde\Pi_{+}$ is the nilpotent part. The coefficient $d$ is the scalar such that $\tilde\Pi_{-}\psi_{-}=d\tilde\Pi_{-}$, and $\nu_{-}=\psi_{-}-d\tilde\Pi_{-}$ is the nilpotent part. The coefficients and the elements $\nu_{\pm}$ are intrinsic; the coordinates of $\nu_{\pm}$ in a chosen mixed line are not.

**The adapted bases.** A Peirce basis $\tilde\Pi_{+},\vec\Upsilon_{+-},\vec\Upsilon_{-+},\tilde\Pi_{-}$ gives the bases

$$
(\tilde\Pi_{+},\vec\Upsilon_{-+})\ \text{of}\ S_{+},\qquad
(\vec\Upsilon_{+-},\tilde\Pi_{-})\ \text{of}\ S_{-}.
$$

In these bases,

$$
\psi_{+}=a\tilde\Pi_{+}+c\vec\Upsilon_{-+},\qquad
\psi_{-}=b\vec\Upsilon_{+-}+d\tilde\Pi_{-}.
$$

The numbers $a,c$ and $b,d$ are the Peirce coordinates of the two spinors in the adapted basis. The basis is not canonical; the family is.

## The Ladder

**Proposition.** Let $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ be the mixed units of a Peirce basis. Left multiplication by $\vec\Upsilon_{+-}$ maps $S_{+}$ onto $\mathbb{C}\tilde\Pi_{+}$ and annihilates $\mathbb{C}\tilde\Pi_{+}$; left multiplication by $\vec\Upsilon_{-+}$ maps $S_{+}$ onto $\mathbb{B}_{-+}$ and annihilates $\mathbb{B}_{-+}$. On coordinates,

$$
\vec\Upsilon_{+-}\psi_{+}=\vec\Upsilon_{+-}(a\tilde\Pi_{+}+c\vec\Upsilon_{-+})=c\tilde\Pi_{+},
$$

$$
\vec\Upsilon_{-+}\psi_{+}=\vec\Upsilon_{-+}(a\tilde\Pi_{+}+c\vec\Upsilon_{-+})=a\vec\Upsilon_{-+}.
$$

**Proof.** The corner rule gives $\vec\Upsilon_{+-}\tilde\Pi_{+}=0$, $\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_{+}$, $\vec\Upsilon_{-+}\tilde\Pi_{+}=\vec\Upsilon_{-+}$ and $\vec\Upsilon_{-+}\vec\Upsilon_{-+}=0$. The two displayed formulas follow.

**The composites are the projections.** Using the products of the basis,

$$
\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_{-},\qquad
\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_{+}.
$$

Therefore left multiplication by $\vec\Upsilon_{-+}\vec\Upsilon_{+-}$ is the projection of $S_{+}$ onto $\mathbb{B}_{-+}$, and left multiplication by $\vec\Upsilon_{+-}\vec\Upsilon_{-+}$ is the projection of $S_{+}$ onto $\mathbb{C}\tilde\Pi_{+}$. Each composite is idempotent; neither is the identity on $S_{+}$. The two maps are the two steps of the ladder.

**The normalization is the gauge.** Without the product normalization, the two maps are defined only up to reciprocal scale: if $\vec\Upsilon_{+-}$ is replaced by $\lambda\vec\Upsilon_{+-}$, the first map is multiplied by $\lambda$ and the second by $\lambda^{-1}$. The ladder is therefore canonical on the family and gauge-dependent on the basis, as it must be.

## The Gauge

**The action on coordinates.** Under the basis change of *The Peirce Basis of the Biquaternion Algebra*,

$$
\vec\Upsilon'_{+-}=t^{-1}\vec\Upsilon_{+-},\qquad
\vec\Upsilon'_{-+}=t\vec\Upsilon_{-+},\qquad t\in\mathbb{C}^{\times},
$$

the coordinates transform by

$$
a'=a,\qquad c'=t^{-1}c,\qquad b'=tb,\qquad d'=d.
$$

The diagonal coefficients are gauge-invariant; the mixed coefficients carry the reciprocal factors. The spinor element is unchanged; only its coordinates change.

**The gauge is not a symmetry of the spinor.** The gauge is a change of basis of the same family. It does not move the spinor in the algebra; it moves the coordinate description. A statement about a spinor is gauge-covariant when it is independent of $t$.

**The Hermitian gauge.** If the family and the basis are Hermitian, $\tilde\Pi_{\pm}^{*}=\tilde\Pi_{\pm}$ and $\vec\Upsilon_{-+}=\vec\Upsilon_{+-}^{*}$, then the allowed gauge is $|t|=1$. The Hermitian norm of a positive spinor is

$$
\mathrm{Sc}(\psi_{+}\psi_{+}^{*})
=\frac12\bigl(|a|^{2}+|c|^{2}\bigr),
$$

and the norm of a negative spinor is

$$
\mathrm{Sc}(\psi_{-}\psi_{-}^{*})
=\frac12\bigl(|b|^{2}+|d|^{2}\bigr).
$$

The formulas are invariant under the circle $|t|=1$. They are positive definite and vanish only at the zero spinor.

## The Invariants of a Single Spinor

**The intrinsic data.** Fix the family. The canonical splitting of §*The Canonical Splitting* gives, for a positive spinor,

$$
\psi_{+}=a\tilde\Pi_{+}+\nu_{+},\qquad
a\in\mathbb{C},\quad \nu_{+}\in\mathbb{B}_{-+},
$$

with $a$ and $\nu_{+}$ intrinsic. The coordinate $c$ in a chosen basis is not intrinsic: $\nu_{+}=c\vec\Upsilon_{-+}$ and $c$ is multiplied by $t^{-1}$ under the gauge.

**The invariant conditions.** The following conditions are independent of the basis:

- $a=0$: the spinor is a nilpotent, $\psi_{+}=\nu_{+}$.
- $\nu_{+}=0$: the spinor is pure, $\psi_{+}=a\tilde\Pi_{+}$.
- $a=0$ and $\nu_{+}=0$: the spinor is zero.
- $a\ne0$: the spinor has a nonzero diagonal part; the ratio $c/a$ is a coordinate on the mixed line and is not invariant, since it is multiplied by $t^{-1}$.

**What is not invariant.** The pair $(a,c)$ is not invariant; only $a$ and the element $\nu_{+}$ are. The vanishing of $c$ is invariant, because $c=0$ exactly when $\nu_{+}=0$; the value of a nonzero $c$ is not. In the Hermitian gauge the norm $\frac12(|a|^{2}+|c|^{2})$ is invariant; it is not an invariant of the gauge $\mathbb{C}^{\times}$ without the Hermitian condition.

**The negative spinor.** The same statements hold for $\psi_{-}=\nu_{-}+d\tilde\Pi_{-}$, with $d$ and $\nu_{-}$ intrinsic and $b$ gauge-dependent: $b'=tb$.

## The Peirce Index

**Right multiplication by the idempotents.** For $\psi_{+}\in S_{+}$,

$$
\psi_{+}\tilde\Pi_{+}=\psi_{+},\qquad
\psi_{+}\tilde\Pi_{-}=0.
$$

For $\psi_{-}\in S_{-}$,

$$
\psi_{-}\tilde\Pi_{-}=\psi_{-},\qquad
\psi_{-}\tilde\Pi_{+}=0.
$$

So $S_{+}$ is the image of right multiplication by $\tilde\Pi_{+}$ and the kernel of right multiplication by $\tilde\Pi_{-}$, and $S_{-}$ is the reverse.

**The index is the right index.** The two spinor spaces are the two values of the right Peirce index. The index is a label of the space, not the value of an operator: it is the idempotent that acts as the identity on the right. The diagonal coefficient $a$ or $d$ and the mixed coordinate $c$ or $b$ are read in that space.

## Right Multiplication

**Preservation of a spinor space.** Right multiplication by $\tilde Q\in\mathbb{B}$ sends $S_{+}$ into $S_{+}$ exactly when

$$
\tilde\Pi_{+}\tilde Q\tilde\Pi_{-}=0,
$$

which in the basis is $Q_{+-}=0$. It sends $S_{-}$ into $S_{-}$ exactly when $\tilde\Pi_{-}\tilde Q\tilde\Pi_{+}=0$, which is $Q_{-+}=0$.

**Proof.** For $\xi=\eta\tilde\Pi_{+}\in S_{+}$, $\xi\tilde Q=\eta\tilde\Pi_{+}\tilde Q$. This lies in $S_{+}$ exactly when $\tilde\Pi_{+}\tilde Q=\tilde\Pi_{+}\tilde Q\tilde\Pi_{+}$, that is when $\tilde\Pi_{+}\tilde Q\tilde\Pi_{-}=0$. The basis expansion gives $\tilde\Pi_{+}\tilde Q\tilde\Pi_{-}=Q_{+-}\vec\Upsilon_{+-}$, so the condition is $Q_{+-}=0$. The proof for $S_{-}$ is the same with the signs exchanged.

**The exchange by the mixed units.** Right multiplication by $\vec\Upsilon_{+-}$ sends $S_{+}$ onto $S_{-}$ and kills $S_{-}$; right multiplication by $\vec\Upsilon_{-+}$ sends $S_{-}$ onto $S_{+}$ and kills $S_{+}$:

$$
\xi\in S_{+}\longmapsto\xi\vec\Upsilon_{+-}\in S_{-},\qquad
\eta\in S_{-}\longmapsto\eta\vec\Upsilon_{-+}\in S_{+}.
$$

On the coordinates,

$$
(a\tilde\Pi_{+}+c\vec\Upsilon_{-+})\vec\Upsilon_{+-}=a\vec\Upsilon_{+-}+c\tilde\Pi_{-},
$$

$$
(b\vec\Upsilon_{+-}+d\tilde\Pi_{-})\vec\Upsilon_{-+}=b\tilde\Pi_{+}+d\vec\Upsilon_{-+}.
$$

Each map is an isomorphism of the two complex planes, and the two maps are inverse:

$$
(\xi\vec\Upsilon_{+-})\vec\Upsilon_{-+}=\xi\tilde\Pi_{+}=\xi,\qquad
(\eta\vec\Upsilon_{-+})\vec\Upsilon_{+-}=\eta\tilde\Pi_{-}=\eta.
$$

Each map is square-zero, because the unit kills the space it maps onto:

$$
\xi\vec\Upsilon_{+-}\vec\Upsilon_{+-}=0,\qquad
\eta\vec\Upsilon_{-+}\vec\Upsilon_{-+}=0.
$$

The exchange depends on the basis: under the gauge the first map is multiplied by $t^{-1}$ and the second by $t$.

**The star does not exchange the spaces.** If the family is Hermitian, then

$$
S_{+}^{*}=(\mathbb{B}\tilde\Pi_{+})^{*}=\tilde\Pi_{+}\mathbb{B},
$$

the right Peirce row of $\tilde\Pi_{+}$, not $S_{-}=\mathbb{B}\tilde\Pi_{-}$. The two spaces are different subspaces: the row contains $\mathbb{B}_{++}\oplus\mathbb{B}_{+-}$ and $S_{-}$ contains $\mathbb{B}_{+-}\oplus\mathbb{B}_{--}$. They share the mixed line $\mathbb{B}_{+-}$ but are not equal. Chirality belongs to the left grouping, not to the involution.

## What the Spinor Is Not

**It is not a state vector in an external space.** The spinor is an element of the algebra, in one of the two Peirce spaces. Its coordinates are the Peirce coordinates in an adapted basis. There is no separate Hilbert space here; a Hermitian form, when it is used, is a form on the algebra.

**It is not a column of a matrix.** A column appears when $\mathbb{B}$ is written as $M_{2}(\mathbb{C})$ and the spinor space is read as a column of the matrix. That is one picture of the same element; the algebra element and its Peirce coordinates are the definition. The matrix picture belongs to *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*.

**It is not defined by an auxiliary element.** The family defines the two spaces and their splitting. The mixed line has no canonical element, and a basis is a choice. No element outside the family is part of the definition.

## Example: The Standard Family

For the standard family

$$
\tilde\Pi_{+}=\frac{e_{t}+i\vec e_{z}}{2},\qquad
\tilde\Pi_{-}=\frac{e_{t}-i\vec e_{z}}{2},
$$

with the standard mixed units

$$
\vec\Upsilon_{+-}=\frac{i\vec e_{x}-\vec e_{y}}{2},\qquad
\vec\Upsilon_{-+}=\frac{i\vec e_{x}+\vec e_{y}}{2},
$$

a positive spinor is

$$
\psi_{+}=a\tilde\Pi_{+}+c\vec\Upsilon_{-+},
$$

and a negative spinor is

$$
\psi_{-}=b\vec\Upsilon_{+-}+d\tilde\Pi_{-}.
$$

The gauge acts by

$$
a'=a,\qquad c'=t^{-1}c,\qquad b'=tb,\qquad d'=d.
$$

The ladder is

$$
\vec\Upsilon_{+-}\psi_{+}=c\tilde\Pi_{+},\qquad
\vec\Upsilon_{-+}\psi_{+}=a\vec\Upsilon_{-+}.
$$

The Peirce index is

$$
\psi_{+}\tilde\Pi_{+}=\psi_{+},\qquad
\psi_{+}\tilde\Pi_{-}=0,
$$

and the reverse for $\psi_{-}$. In the Hermitian standard basis the norms are

$$
\mathrm{Sc}(\psi_{+}\psi_{+}^{*})=\frac12\bigl(|a|^{2}+|c|^{2}\bigr),\qquad
\mathrm{Sc}(\psi_{-}\psi_{-}^{*})=\frac12\bigl(|b|^{2}+|d|^{2}\bigr).
$$

## Summary

A spinor is an element of one of the two Peirce spaces $S_{\pm}=\mathbb{B}\tilde\Pi_{\pm}$. The family splits each space canonically into a diagonal line and a mixed line, $S_{+}=\mathbb{C}\tilde\Pi_{+}\oplus\mathbb{B}_{-+}$ and $S_{-}=\mathbb{B}_{+-}\oplus\mathbb{C}\tilde\Pi_{-}$. A Peirce basis chooses a generator of the mixed line and gives the adapted coordinates; the gauge is the reciprocal scaling of the two mixed units. The ladder is left multiplication by the mixed units, and its composites are the two projections. The intrinsic data of a single spinor are the diagonal coefficient and the element of the mixed line; the mixed coordinate is gauge-dependent. The Peirce index is the right index. Right multiplication preserves a spinor space under a corner condition and exchanges the two spaces by the mixed units; the star does not exchange them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{\pm}=\mathbb{B}\tilde\Pi_{\pm}$ | The two spinor spaces |
| $\psi_{\pm}$ | A spinor of the corresponding space |
| $\tilde\Pi_{\pm}$ | The idempotents of the family |
| $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ | The mixed units of a basis |
| $a,c$ | The coordinates of a positive spinor |
| $b,d$ | The coordinates of a negative spinor |
| $t$ | The gauge parameter, with $|t|=1$ in the Hermitian case |

## Further Reading

- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the family, the four lines and the product rule.
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the basis, the gauge and the coordinates.
- [$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the matrix picture of the two spaces.
- [The Minimal Left Ideals](the-minimal-left-ideals.html), for the identification of the two spaces as minimal left ideals.
- [The Commutator Operator](the-commutator-operator.html), for the right multiplication and the exchange as operators.
- [Idempotents](idempotents.html), for the classification of the idempotents and the standard pair.
