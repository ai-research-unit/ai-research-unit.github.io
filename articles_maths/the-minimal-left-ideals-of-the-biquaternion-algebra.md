# __The Minimal Left Ideals of the Biquaternion Algebra__

## Introduction

An idempotent $\tilde\Pi$ cuts the algebra into $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_t-\tilde\Pi)$, and the two summands are left ideals. For the biquaternion algebra the idempotents come in a sphere of pairs, one pair for each unit real axis $\vec u$, and each of the two summands is as small as a left ideal can be: it contains no nonzero proper left subideal.

This article defines the idempotents at an axis, computes the two ideals they generate, proves minimality, gives the decomposition $\mathbb{B}=S_{+}\oplus S_{-}$, describes the lattice of left ideals, and draws the consequence that matters for the carriers: because the algebra is simple, a carrier of the multiplication is necessarily one-sided, and the two-sided ideals are the two trivial ones.

The idempotents themselves, their classes and their Peirce decompositions are *The Square Roots of One and the Idempotents of the Biquaternion Algebra*, *Peirce Decompositions of the Biquaternion Algebra* and *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*; the nilpotent that accompanies each ideal is *The Companion Nilpotents of the Biquaternion Algebra*; the module category is *The Category of Modules in the Biquaternion Algebra*; and the carrier these ideals define is *The Carriers of the Biquaternion Algebra*.

Nothing below is a statement of physics. The elements are written $\tilde Q$ with coefficients $Q_t,Q_x,Q_y,Q_z$, the axis $\vec u$ is a unit real vector, and $\vec e_x,\vec e_y,\vec e_z$ are the pure quaternion units.

## The Idempotents at an Axis

**Definition.** For a unit real vector $\vec u$ put

$$
\tilde\Pi_{\pm}(\vec u)=\tfrac12\bigl(e_t\pm i\vec u\bigr).
$$

**Proposition (the four relations).** The two elements are idempotents, they are orthogonal and complementary:

$$
\tilde\Pi_{\pm}^{2}=\tilde\Pi_{\pm},\qquad \tilde\Pi_{+}\tilde\Pi_{-}=\tilde\Pi_{-}\tilde\Pi_{+}=0,\qquad \tilde\Pi_{+}+\tilde\Pi_{-}=e_t .
$$

*Proof.* $(\vec u)^{2}=-e_t$ for a unit real vector, so $(i\vec u)^{2}=e_t$ and $\tilde\Pi_{\pm}^{2}=\tfrac14(e_t\pm2i\vec u+e_t)=\tfrac12(e_t\pm i\vec u)=\tilde\Pi_{\pm}$. The products are $\tfrac14(e_t-(i\vec u)^{2})=\tfrac14(e_t-e_t)=0$, and the sum is $e_t$.

**Proposition (the conjugate idempotent).** $\tilde\Pi_{\pm}(\vec u)^{*}=\tilde\Pi_{\mp}(\vec u)$; the two idempotents of a pair are exchanged by the Hermitian conjugation, and neither is Hermitian at a real axis.

*Proof.* ${}^{*}$ fixes $e_t$ and reverses $i\vec u$, so $\tilde\Pi_{+}^{*}=\tfrac12(e_t-i\vec u)=\tilde\Pi_{-}$; an idempotent is Hermitian only if it equals its conjugate, which would force $\vec u=0$, and no idempotent of the algebra is Hermitian at a real axis.

**Remark (the axis is a parameter).** The pair is indexed by the sphere of unit real axes, a two-sphere, and no point of it is preferred by the algebra. Under $Q\mapsto uQu^{*}$ with $u$ a unit real quaternion the axis rotates, so the unitary group acts on the family of pairs transitively; the pair at $\vec e_z$ is the model, and every other pair is its conjugate.

**Example (the model pair).** At $\vec u=\vec e_z$,

$$
\tilde\Pi_{+}(\vec e_z)=\tfrac12(e_t+i\vec e_z)=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
\tilde\Pi_{-}(\vec e_z)=\tfrac12(e_t-i\vec e_z)=\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$

in the $M_2(\mathbb{C})$ Pauli representation, with $e_t$ the identity and $\vec e_k=-i\sigma_k$.

## The Two Ideals

**Definition.** The **left ideal at the axis** is

$$
S_{\pm}(\vec u)=\mathbb{B}\,\tilde\Pi_{\pm}(\vec u)=\{\tilde Q\tilde\Pi_{\pm}(\vec u) : \tilde Q\in\mathbb{B}\}.
$$

**Proposition (ideal, dimension, basis).** $S_{\pm}$ is a left ideal of $\mathbb{B}$, of real dimension $4$ and complex dimension $2$, with $\mathbb{C}$-basis

$$
S_{+}=\operatorname{span}_{\mathbb{C}}\bigl\{\tilde\Pi_{+},\ \vec\Upsilon_{-+}\bigr\},\qquad
S_{-}=\operatorname{span}_{\mathbb{C}}\bigl\{\tilde\Pi_{-},\ \vec\Upsilon_{+-}\bigr\},
$$

where

$$
\vec\Upsilon_{-+}(\vec u)=\tfrac12\bigl(i\vec a+\vec b\bigr),\qquad
\vec\Upsilon_{+-}(\vec u)=\tfrac12\bigl(i\vec a-\vec b\bigr)
$$

for unit real vectors $\vec a,\vec b$ that complete $\vec u$ to a right-handed orthonormal triple.

*Proof.* The set is a left ideal because $X(Y\tilde\Pi_{\pm})=(XY)\tilde\Pi_{\pm}$. At the axis $\vec u=\vec e_z$, with $\vec a=\vec e_x$ and $\vec b=\vec e_y$, the four products of the basis elements with $\tilde\Pi_{+}$ are

$$
e_t\tilde\Pi_{+}=\tilde\Pi_{+},\qquad
\vec e_x\tilde\Pi_{+}=-i\vec\Upsilon_{-+},\qquad
\vec e_y\tilde\Pi_{+}=\vec\Upsilon_{-+},\qquad
\vec e_z\tilde\Pi_{+}=-i\tilde\Pi_{+},
$$

so the four real spanning vectors lie in the complex span of $\tilde\Pi_{+}$ and $\vec\Upsilon_{-+}$, which is therefore the whole ideal and has complex dimension $2$. The general axis follows by the transitivity of the conjugation by the unit real quaternions, and the same computation with $\tilde\Pi_{-}$ gives $S_{-}$.

**Example (the model ideals).** At $\vec u=\vec e_z$,

$$
S_{+}=\left\{\begin{pmatrix}a&0\\c&0\end{pmatrix}\right\},\qquad
S_{-}=\left\{\begin{pmatrix}0&b\\0&d\end{pmatrix}\right\},
$$

the first-column and the second-column matrices. Each is a two-dimensional complex space, four real dimensions, and each is closed under left multiplication by every biquaternion.

## Minimality

**Theorem (the two ideals are minimal).** $S_{\pm}$ has no left subideal other than $0$ and $S_{\pm}$.

*Proof.* In the matrix model, $S_{+}$ is the space of matrices whose image is the first coordinate axis; a left ideal of $M_2(\mathbb{C})$ is a set of matrices whose images lie in a fixed subspace $W\subseteq\mathbb{C}^2$, and the left ideals contained in $S_{+}$ correspond to the subspaces $W$ of the line $\mathbb{C}e_1$, of which there are two: $0$ and the line itself. The same argument on the second axis gives $S_{-}$. Intrinsically: if $0\neq s\in S_{\pm}$ then $\mathbb{B}s$ is a nonzero left ideal contained in $S_{\pm}$, and in the model $\mathbb{B}s$ is the whole column space because $M_2(\mathbb{C})s=\mathbb{C}^2$ for $s\neq 0$.

**Corollary (every nonzero element is a generator).** For $0\neq s\in S_{\pm}$ one has $\mathbb{B}s=S_{\pm}$; the ideal is generated by any one of its nonzero elements.

**Remark (what minimality excludes).** A left ideal strictly between $0$ and $S_{\pm}$ would be a left submodule, and a carrier of the multiplication is by definition irreducible; minimality is exactly the statement that $S_{\pm}$ qualifies. Nothing smaller than two complex dimensions can be a left ideal, since a line $\mathbb{C}s$ is a left ideal only if $\mathbb{B}s\subseteq\mathbb{C}s$, which fails for every nonzero $s$.

**Remark (the dimension is not an accident).** The complex dimension $2$ is the dimension of the simple module, and it is forced: an algebra of the form $M_n(\mathbb{C})$ has simple modules of dimension $n$, and $n=2$ here because the biquaternion algebra is a full $2\times2$ matrix algebra.

## The Decomposition of the Algebra

**Theorem.** $\mathbb{B}=S_{+}\oplus S_{-}$ as left $\mathbb{B}$-modules.

*Proof.* The two idempotents are orthogonal and sum to the unit, so every $\tilde Q$ decomposes as $\tilde Q=\tilde Q\tilde\Pi_{+}+\tilde Q\tilde\Pi_{-}$; the sum is direct because an element of both ideals is annihilated by both idempotents and hence is zero, $\tilde Q=\tilde Q e_t=\tilde Q(\tilde\Pi_{+}+\tilde\Pi_{-})=0$.

**Corollary (dimensions).** $4+4=8$ over $\mathbb{R}$ and $2+2=4$ over $\mathbb{C}$; the two summands have equal dimension, and the decomposition is a splitting of the regular module into two copies of one simple module.

**Remark (the two copies are isomorphic, not equal).** $S_{+}$ and $S_{-}$ are isomorphic as left modules: right multiplication by the companion nilpotent $\vec\Upsilon_{+-}$ carries $S_{+}$ into $S_{-}$, it does not vanish, and a nonzero map of simple modules is an isomorphism. The two remain distinct subspaces of the same algebra. *The Companion Nilpotents of the Biquaternion Algebra* gives the maps explicitly.

## The Lattice of Left Ideals

**Theorem (the left ideals).** The left ideals of $\mathbb{B}$ are exactly the sets

$$
I_W=\{\tilde Q : \tilde Q(\mathbb{C}^2)\subseteq W\}
$$

for the subspaces $W\subseteq\mathbb{C}^2$ in the defining module, and the lattice of left ideals is the lattice of subspaces of a two-dimensional complex space: $0$, two families of lines, and $\mathbb{B}$.

*Proof.* In the matrix model a left ideal $I$ is a subspace of $M_2(\mathbb{C})$ closed under left multiplication; the condition $MI\subseteq I$ for all $M$ forces $I=\{M : M(\mathbb{C}^2)\subseteq W\}$ with $W=\bigcup_{M\in I}M(\mathbb{C}^2)$, which is a subspace; conversely such a set is a left ideal. The subspaces of $\mathbb{C}^2$ are $0$, the lines and the plane, and the lines form a projective line.

**Corollary (three kinds).** The left ideals are $0$; the minimal ones, the two columns at a chosen axis together with all their conjugates; and $\mathbb{B}$. The minimal ones are the carriers.

**Remark (the lattice is not a chain).** There are two minimal ideals and they are incomparable, so the lattice is not a chain: the sum $S_{+}+S_{-}$ is already $\mathbb{B}$, and the intersection is $0$. A left ideal is never strictly between a minimal one and the algebra.

## Simplicity and the One-Sidedness

**Theorem.** $\mathbb{B}$ is simple: its only two-sided ideals are $0$ and $\mathbb{B}$.

*Proof.* *The Biquaternion Algebra*, §*Simplicity*: a nonzero two-sided ideal contains a nonzero element, and multiplying by the units and taking linear combinations produces the whole algebra; equivalently $\mathbb{B}\cong M_2(\mathbb{C})$ is a full matrix algebra over a field, which is simple.

**Corollary (a carrier of the multiplication is one-sided).** No two-sided ideal other than $0$ and $\mathbb{B}$ exists, so an irreducible left ideal is a carrier and the algebra itself is not one. The two-sided structure is exhausted by the trivial pair, and every carrier of the multiplication is a minimal left ideal.

**Corollary (the algebra is the sum of its carriers).** $\mathbb{B}=S_{+}\oplus S_{-}$ is a direct sum of two carriers, and it is not itself a carrier because it is reducible. The carrier is a summand, never the whole.

**Remark (why a two-sided carrier cannot exist).** A two-sided ideal is at the same time a left and a right ideal; the two-sided ideals are $0$ and $\mathbb{B}$, and both are excluded — $0$ is not a carrier by definition, and $\mathbb{B}$ is reducible. The reason the count of carriers is finite and small is the simplicity of the algebra together with the shortness of the lattice of left ideals.

## The Sphere of Axes and the Type

**Proposition (transitivity).** The group of unit real quaternions acts transitively on the pairs $\bigl(\tilde\Pi_{+}(\vec u),\tilde\Pi_{-}(\vec u)\bigr)$, and it carries $S_{+}(\vec u)$ to $S_{+}(\vec u')$ for a suitable rotation of the axis.

*Proof.* A unit real quaternion $\tilde q$ acts by $Q\mapsto\tilde qQ\tilde q^{*}$, which rotates $\vec u$ to $\vec u'$; the idempotent $\tilde\Pi_{+}(\vec u)=\tfrac12(e_t+i\vec u)$ is carried to $\tfrac12(e_t+i\vec u')$, and the ideal generated by it to the ideal generated by its image. The action of the unit quaternions on the axes is the standard transitive action on the two-sphere, with stabiliser the circle about the axis.

**Corollary (one type, many subspaces).** All the minimal left ideals have the same type, of complex dimension $2$; the axis is a parameter of the family and not a datum of the algebra. The type is what a carrier contributes to the count, and it does not depend on the axis.

**Remark (the axis and the weight).** The axis does affect the weight string of a generator: the generator $\tilde S(\vec u)$ is the one that is diagonal on the ideal at the axis $\vec u$, and a generator at another axis has a different matrix in the same basis. *The Weights of a Carrier* reads the string at the axis of the ideal, where it is $\{+\tfrac12,-\tfrac12\}$.

## Summary

For each unit real axis $\vec u$ the element $\tilde\Pi_{\pm}(\vec u)=\tfrac12(e_t\pm i\vec u)$ is an idempotent, the two are orthogonal and sum to the unit, and they generate the two left ideals $S_{\pm}=\mathbb{B}\tilde\Pi_{\pm}$.

Each ideal is four real-dimensional and two complex-dimensional, with basis $\{\tilde\Pi_{\pm},\vec\Upsilon_{\mp\pm}\}$, and it is minimal: any nonzero element of it generates it, and no left ideal lies strictly between $0$ and it. In the matrix model the two ideals are the two columns.

The algebra splits as $\mathbb{B}=S_{+}\oplus S_{-}$ into two copies of one simple module, the left ideals form the lattice of subspaces of a two-dimensional complex space, and the algebra is simple, so its only two-sided ideals are the two trivial ones. Hence a carrier of the multiplication is one-sided, the algebra itself is never a carrier, and the family of carriers is one type over a sphere of axes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi_{\pm}(\vec u)=\tfrac12(e_t\pm i\vec u)$ | the complementary idempotents at the axis $\vec u$ |
| $S_{\pm}(\vec u)=\mathbb{B}\tilde\Pi_{\pm}(\vec u)$ | the minimal left ideals |
| $\vec\Upsilon_{-+},\vec\Upsilon_{+-}$ | the companion nilpotents, the second basis vector of each ideal |
| $I_W$ | the left ideal of the matrices whose image lies in $W$ |
| $\mathbb{C}^2$ | the defining module, the type of the two ideals |
| simple algebra | an algebra whose only two-sided ideals are $0$ and the algebra |
| minimal left ideal | a left ideal with no left subideal other than $0$ and itself |

## Further Reading

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the ideals as carriers and for the count of types
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for $\vec\Upsilon_{\mp\pm}$, the corners and the Peirce functional
- [The Square Roots of One and the Idempotents of the Biquaternion Algebra](idempotents.html), for the classification of the idempotents of the whole algebra
- [Peirce Decompositions of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the Peirce decomposition at an idempotent
- [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the basis adapted to a pair of idempotents
- [The Category of Modules in the Biquaternion Algebra](the-category-of-modules.html), for the simple module and the Morita equivalence
- [The Regular Module in the Biquaternion Algebra](the-regular-module.html), for the algebra as a module over itself
- [The $M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the matrix model used in the examples
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, minimal left ideals and the Peirce decomposition.
- Israel Nathan Herstein, *Noncommutative Rings* (Carus Monographs, 1968), for the simplicity of a full matrix algebra and its left ideals.
