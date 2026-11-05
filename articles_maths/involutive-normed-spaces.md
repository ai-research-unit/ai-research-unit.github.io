
# __Involutive Normed Spaces__

## Introduction

A normed space with a continuous involution carries a number, the **norm of the involution** $\lVert\mathrm{J}\rVert$, and the involution is an isometry exactly when that number is one; since $\mathrm{J}$ is its own inverse, a continuous involution always has norm at least one and is a homeomorphism, and replacing the norm by the equivalent norm $\sup(\lVert x\rVert, \lVert\mathrm{J} x\rVert)$ makes it isometric. The fixed and negated subspaces are closed and the splitting into them is topological; in the antilinear case the fixed subspace is a real normed space of the same dimension as the complex space. On the dual the transposed involution has the same norm, and it is isometric when the involution is.

This article develops the normed theory of an involution: the norm of the involution, the isometric case, the equivalent invariant norm, the fixed and negated subspaces with the norm they inherit, and the transposed involution on the dual with the dual norm. The topological involution and its closedness and splitting are *Involutive Topological Linear Spaces*; the locally convex version is *Locally Convex Spaces with an Involution*; the norms, the bounded operators and the operator norm are *Normed and Banach Spaces* and *Bounded Operators and the Operator Norm*; the transposed involution on the dual is *The Involution and the Dual Pairing*. The completion is *Involutive Banach Spaces*, the next article of this group. No form, no adjoint and no Hilbert structure is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $\varsigma$ is the involution of $\mathbb{K}$ (the identity or the complex conjugation), $X$ is a normed space over $\mathbb{K}$ with norm $\lVert\cdot\rVert$, and $\mathrm{J}$ is a continuous $\varsigma$-semilinear involution of $X$ with $\mathrm{J}^{2} = \mathrm{id}$; the linear case is written $T$, the antilinear case is $\varsigma \neq \mathrm{id}$, and the fixed and negated subspaces are $X^{\mathrm{J}} = \ker(\mathrm{J} - \mathrm{id})$ and $X^{-} = \ker(\mathrm{J} + \mathrm{id})$.

## The Norm of an Involution

**Proposition (continuity and the norm).** Let $\mathrm{J}$ be a $\varsigma$-semilinear involution of $X$. Then $\mathrm{J}$ is continuous if and only if it is bounded, and then

$$
\boxed{\;\lVert\mathrm{J}\rVert = \sup_{x \neq 0}\frac{\lVert\mathrm{J} x\rVert}{\lVert x\rVert} = \sup_{\lVert x\rVert \leq 1}\lVert\mathrm{J} x\rVert\;}
$$

is finite and satisfies $\lVert\mathrm{J}\rVert \geq 1$ and $\lVert\mathrm{J}^{-1}\rVert = \lVert\mathrm{J}\rVert$; a continuous involution is a topological isomorphism of $X$ onto itself.

**Proof.** Boundedness is the normed form of continuity, and the operator norm is *Bounded Operators and the Operator Norm*. Since $\mathrm{J}^{-1} = \mathrm{J}$ and $\mathrm{J}$ is a bijection, $\lVert\mathrm{J}\rVert\lVert\mathrm{J}^{-1}\rVert \geq \lVert\mathrm{J}\mathrm{J}^{-1}\rVert = 1$ gives $\lVert\mathrm{J}\rVert \geq 1$; the equality of the norms of $\mathrm{J}$ and $\mathrm{J}^{-1}$ is the identity $\lVert\mathrm{J}\rVert = \lVert\mathrm{J}^{-1}\rVert$ for an involution, read from $\mathrm{J}^{-1} = \mathrm{J}$.

**Proposition (isometric exactly at norm one).** A continuous involution $\mathrm{J}$ satisfies $\lVert\mathrm{J}\rVert = 1$ if and only if it is an isometry, $\lVert\mathrm{J} x\rVert = \lVert x\rVert$ for all $x$. For an involutive isometry, $\mathrm{J}^{-1} = \mathrm{J}$ gives the reverse inequality, so $\lVert\mathrm{J}\rVert = 1$.

**Proof.** If $\mathrm{J}$ is an isometry then $\lVert\mathrm{J}\rVert = \sup_{\lVert x\rVert\leq1}\lVert x\rVert = 1$. Conversely, $\lVert\mathrm{J}\rVert = 1$ gives $\lVert\mathrm{J} x\rVert \leq \lVert x\rVert$, and applying this to $\mathrm{J} x$ gives $\lVert x\rVert = \lVert\mathrm{J}^{2}x\rVert \leq \lVert\mathrm{J} x\rVert$, so equality.

**Proposition (equivalent invariant norm).** For a continuous involution $\mathrm{J}$ the formula

$$
\lVert x\rVert_{\mathrm{J}} = \sup(\lVert x\rVert, \lVert\mathrm{J} x\rVert)
$$

defines a norm on $X$, equivalent to $\lVert\cdot\rVert$, for which $\mathrm{J}$ is isometric, $\lVert\mathrm{J} x\rVert_{\mathrm{J}} = \lVert x\rVert_{\mathrm{J}}$; the norms coincide exactly when $\mathrm{J}$ is already isometric for $\lVert\cdot\rVert$.

**Proof.** The supremum is a norm because it is the supremum of two norms, and it is equivalent because $\lVert x\rVert \leq \lVert x\rVert_{\mathrm{J}} \leq \max(1, \lVert\mathrm{J}\rVert)\lVert x\rVert$. Invariance is the computation of *Locally Convex Spaces with an Involution*: $\lVert\mathrm{J} x\rVert_{\mathrm{J}} = \sup(\lVert\mathrm{J} x\rVert, \lVert\mathrm{J}^{2}x\rVert) = \sup(\lVert\mathrm{J} x\rVert, \lVert x\rVert) = \lVert x\rVert_{\mathrm{J}}$. The equality case is the preceding proposition.

## The Fixed and Negated Subspaces

**Proposition (closedness and the inherited norm).** The fixed subspace $X^{\mathrm{J}}$ and the negated subspace $X^{-}$ are closed subspaces of $X$, and each is a normed space for the restriction of the norm; in the antilinear case $X^{\mathrm{J}}$ is a real normed space. When $2$ is invertible the averaging maps $\pi_{1,2} = \frac12(\mathrm{id}\pm\mathrm{J})$ are continuous projections and the direct sum

$$
\boxed{\;X = X^{\mathrm{J}} \oplus X^{-}\;}
$$

is topological, the sum being equivalent to the direct sum of the two restricted norms.

**Proof.** The subspaces are the kernels of the continuous maps $\mathrm{id} \mp \mathrm{J}$, hence closed; a subspace of a normed space is normed for the restricted norm. The projections and the splitting are the topological splitting of *Involutive Topological Linear Spaces*, and the equivalence of the norm with the direct sum of the restricted norms is the standard open mapping statement for a topological direct sum of normed spaces.

**Proposition (the invariant norm on the sum).** With the invariant norm and $2$ invertible, every $x = x_{+} + x_{-}$ with $x_{\pm} \in X^{\pm}$ satisfies

$$
\max\bigl(\lVert x_{+}\rVert_{\mathrm{J}}, \lVert x_{-}\rVert_{\mathrm{J}}\bigr) \leq \lVert x\rVert_{\mathrm{J}} \leq \lVert x_{+}\rVert_{\mathrm{J}} + \lVert x_{-}\rVert_{\mathrm{J}} ,
$$

and the two inequalities are equalities on the summands; the direct sum norm $\lVert x_{+}\rVert_{\mathrm{J}} + \lVert x_{-}\rVert_{\mathrm{J}}$ and $\lVert x\rVert_{\mathrm{J}}$ are equivalent, with the fixed and negated subspaces isometric to the summands.

**Proof.** $\pi_{1,2}$ are contractions for the invariant norm, since $\lVert\pi_{1,2}x\rVert_{\mathrm{J}} = \sup(\lVert\pi_{1,2}x\rVert, \lVert\mathrm{J}\pi_{1,2}x\rVert) = \sup(\lVert\pi_{1,2}x\rVert, \lVert\pi_{1,2}x\rVert) = \lVert\pi_{1,2}x\rVert \leq \lVert x\rVert_{\mathrm{J}}$, giving the lower bound; the upper bound is the triangle inequality. On a summand $\mathrm{J}$ acts by $\pm\mathrm{id}$, so $\lVert\cdot\rVert_{\mathrm{J}}$ and $\lVert\cdot\rVert$ agree there.

## The Transposed Involution and the Dual Norm

**Definition.** The **transposed involution** of $\mathrm{J}$ on the dual $X^{*}$ is $\mathrm{J}'(\varphi) = \varphi \circ \mathrm{J}$; it is an involution of the same kind, and it is continuous for the dual norm.

**Theorem (the transpose has the same norm).** For a continuous involution $\mathrm{J}$,

$$
\boxed{\;\lVert\mathrm{J}'\rVert = \lVert\mathrm{J}\rVert\;} ,
$$

and $\mathrm{J}'$ is isometric exactly when $\mathrm{J}$ is isometric.

**Proof.** This is the isometry of the transpose, $\lVert\mathrm{J}'\rVert = \lVert\mathrm{J}\rVert$, from *The Dual Operator*; the isometric statement follows because the equality of norms characterises the isometric case in both spaces, by the proposition above.

**Proposition (the dual summands).** The fixed and negated subspaces of $\mathrm{J}'$ are the annihilators,

$$
(X^{*})^{\mathrm{J}'} = (X^{-})^{\circ}, \qquad (X^{*})^{-} = (X^{\mathrm{J}})^{\circ} ,
$$

and each is a normed space for the dual norm; the dual of the involutive space with the transposed involution is the involutive normed space $(X^{*}, \mathrm{J}')$.

**Proof.** The annihilator identification is *The Involution and the Dual Pairing*; the dual norm restricts to a norm on each closed subspace, and the involution is continuous by the theorem.

## Examples

**Example (the conjugation of $\mathbb{C}^{n}$).** On $\mathbb{C}^{n}$ with the Euclidean norm the componentwise conjugation is an antilinear isometry, $\lVert\mathrm{J} z\rVert_{2} = \lVert z\rVert_{2}$, so $\lVert\mathrm{J}\rVert = 1$; its fixed subspace is $\mathbb{R}^{n}$ with the Euclidean norm, and the real splitting $\mathbb{C}^{n} = \mathbb{R}^{n} \oplus i\mathbb{R}^{n}$ is isometric for the direct sum of the restricted norms in the sense that $\lVert z\rVert_{2}^{2} = \lVert x\rVert_{2}^{2} + \lVert y\rVert_{2}^{2}$ for $z = x + iy$.

**Example (the coordinate involution of $\ell^{n}$).** On $\ell^{n}$, $1 \leq p \leq \infty$, the coordinatewise conjugation is an antilinear isometry with fixed subspace the real sequence space $\ell^{n}_{\mathbb{R}}$, and the norm of the involution is one; the same holds for the coordinatewise negation on the real space, a linear isometry whose fixed subspace is the sequences vanishing in the chosen coordinates.

**Example (a discontinuous involution).** Let $X$ be an infinite-dimensional normed space and let $T_{0}$ be an unbounded linear automorphism of it, which exists by a Hamel-basis construction. On the normed space $X \oplus X$ the map $T(u, v) = (T_{0}u, T_{0}^{-1}v)$ is a linear involution, and it is unbounded, hence discontinuous; its operator norm is infinite. This shows that the continuity hypothesis is not automatic and that the equivalent invariant norm exists only for bounded involutions.

## Summary

On a normed space a continuous involution $\mathrm{J}$ has a finite norm $\lVert\mathrm{J}\rVert \geq 1$, it is a topological isomorphism equal to its own inverse, and it is an isometry exactly when $\lVert\mathrm{J}\rVert = 1$; the formula $\lVert x\rVert_{\mathrm{J}} = \sup(\lVert x\rVert, \lVert\mathrm{J} x\rVert)$ is an equivalent norm for which every continuous involution is isometric, and the original norm is already invariant exactly in the isometric case. The fixed and negated subspaces are closed and normed for the restricted norms, and when $2$ is invertible the averaging projections exhibit $X$ as the topological direct sum $X^{\mathrm{J}}\oplus X^{-}$, the invariant norm being equivalent to the direct sum of the restrictions, which are isometric to the summands; in the antilinear case the fixed subspace is a real normed space. On the dual the transposed involution $\mathrm{J}'(\varphi) = \varphi\circ\mathrm{J}$ has the same norm, $\lVert\mathrm{J}'\rVert = \lVert\mathrm{J}\rVert$, is isometric exactly when $\mathrm{J}$ is, and its fixed and negated parts are the annihilators of $X^{-}$ and $X^{\mathrm{J}}$. The conjugation of $\mathbb{C}^{n}$, the coordinate involution of $\ell^{n}$ and the discontinuous involutions of an infinite-dimensional normed space are the standard examples. The Banach case, where completeness is used, is *Involutive Banach Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$, $\varsigma$ | Field and its involution |
| $X$, $\lVert\cdot\rVert$ | Normed space and its norm |
| $\mathrm{J}$, $T$ | Continuous involution; the linear case |
| $\lVert\mathrm{J}\rVert$ | Norm of the involution, $\geq 1$ |
| $\lVert\mathrm{J}\rVert = 1$ | The isometric case |
| $\lVert x\rVert_{\mathrm{J}} = \sup(\lVert x\rVert, \lVert\mathrm{J} x\rVert)$ | Equivalent invariant norm |
| $X^{\mathrm{J}}$, $X^{-}$ | Fixed and negated subspaces, normed |
| $\pi_{1,2} = \frac12(\mathrm{id}\pm\mathrm{J})$ | Averaging projections |
| $\mathrm{J}'(\varphi) = \varphi\circ\mathrm{J}$ | Transposed involution on the dual |
| $\lVert\mathrm{J}'\rVert = \lVert\mathrm{J}\rVert$ | Norm of the transpose |
| $(X^{-})^{\circ}$, $(X^{\mathrm{J}})^{\circ}$ | Annihilators, the dual summands |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the normed spaces with an involution and the equivalent invariant norms.
- Gottfried Köthe, *Topological Vector Spaces I* and *II* (Springer, 1969 and 1979), for the involutions of a normed space and their duals.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the norm of an involution, the isometric case and the transposed involution.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the real structures and the invariant norms.
- Robert E. Megginson, *An Introduction to Banach Space Theory* (Springer, 1998), for the normed-space background and the equivalences of norms.
