
# __Involutive Banach Spaces__

## Introduction

An involutive Banach space is a Banach space with a continuous involution, and completeness turns the generalities of the normed case into theorems: the fixed and negated subspaces are themselves Banach spaces, a continuous involution extends uniquely to the completion with the fixed subspace of the completion equal to the closure of the fixed subspace, an everywhere-defined linear involution with closed graph is continuous by the closed graph theorem, and the dual with the transposed involution is again an involutive Banach space with the same norm. Completeness also gives the automatic continuity of a linear involution with closed graph, so on a Banach space the only obstruction to continuity is the failure of the graph to be closed.

This article develops the Banach theory of an involution. The completion of an involutive topological space and the extension of the involution are *Involutive Topological Linear Spaces*; the norm of an involution and the equivalent invariant norm are *Involutive Normed Spaces*; the dual norm and the transposed involution are *The Involution and the Dual Pairing* and *Involutive Normed Spaces*; the open mapping and closed graph theorems and the completeness of the dual are *Banach Spaces*, *The Open Mapping Theorem* and *The Closed Graph Theorem*. The separable and reflexive refinements and the weak topologies are *Duality Theory* and the later articles of the category. No form and no Hilbert structure is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $\varsigma$ is the involution of $\mathbb{K}$, $X$ is a Banach space over $\mathbb{K}$ with norm $\lVert\cdot\rVert$, and $\theta$ is a continuous $\varsigma$-semilinear involution of $X$ with $\theta^{2} = \mathrm{id}$; the linear case is written $T$, the fixed and negated subspaces are $X^{\theta}$ and $X^{-}$, and $\widehat{X}$ is the completion of a normed space $X$ with $\iota : X \to \widehat{X}$ the inclusion.

## Completeness of the Summands and the Splitting

**Theorem (the summands are Banach spaces).** Let $X$ be a Banach space and $\theta$ a continuous involution. Then the fixed subspace $X^{\theta}$ and the negated subspace $X^{-}$ are closed, hence complete, subspaces of $X$, and each is a Banach space for the restriction of the norm; in the antilinear case $X^{\theta}$ is a real Banach space.

**Proof.** The subspaces are the kernels of the continuous maps $\mathrm{id} \mp \theta$, hence closed by *Involutive Normed Spaces*; a closed subspace of a complete normed space is complete, so each is a Banach space for the restricted norm of *Banach Spaces*. The antilinear statement is that the restriction of the scalars to $\mathbb{R}$ preserves completeness.

**Theorem (topological direct sum).** With $2$ invertible in $\mathbb{K}$ the averaging maps $\pi_{\pm} = \frac12(\mathrm{id}\pm\theta)$ are continuous projections and

$$
X = X^{\theta} \oplus X^{-}
$$

is a topological direct sum of Banach spaces; the projection onto $X^{\theta}$ along $X^{-}$ is bounded, and the direct sum norm is equivalent to the norm of $X$.

**Proof.** The projections are bounded as composites of $\mathrm{id}$ and $\theta$ with the scalar $\frac12$, and they exhibit the direct sum by *Involutive Normed Spaces*; the open mapping theorem applied to the bounded bijection $X^{\theta}\oplus X^{-} \to X$, $(x_{+}, x_{-}) \mapsto x_{+} + x_{-}$, from the complete space $X^{\theta}\oplus X^{-}$ onto the complete space $X$, gives that the inverse is bounded, hence the equivalence of the norms.

## The Extension to the Completion

**Theorem (extension of a bounded involution).** Let $X$ be a normed space with a continuous involution $\theta$ and let $\widehat{X}$ be its completion. Then $\theta$ extends uniquely to a continuous involution $\widehat{\theta}$ of $\widehat{X}$ with $\widehat{\theta}^{\,2} = \mathrm{id}$, of the same kind as $\theta$, and

$$
\lVert\widehat{\theta}\rVert = \lVert\theta\rVert ;
$$

if $\theta$ is isometric then so is $\widehat{\theta}$.

**Proof.** The extension of a continuous involution to the completion and its uniqueness are *Involutive Topological Linear Spaces*; the norm identity is the density of $X$ in $\widehat{X}$, the unit ball of $X$ being dense in that of $\widehat{X}$, so the suprema defining the two operator norms agree; the isometric statement follows.

**Theorem (the fixed subspace of the completion).** With $2$ invertible in $\mathbb{K}$, the fixed subspace of the extension is the closure of the fixed subspace,

$$
\widehat{X}^{\widehat{\theta}} = \overline{\iota(X^{\theta})} ,
$$

and the negated subspace of the completion is the closure of the negated subspace.

**Proof.** The direction $\overline{\iota(X^{\theta})} \subseteq \widehat{X}^{\widehat{\theta}}$ is the continuity of $\widehat{\theta}$ and the closedness of its fixed subspace; conversely, if $\hat x \in \widehat{X}^{\widehat{\theta}}$ and $x_{n} \to \hat x$ with $x_{n} \in X$, then $\pi_{+}x_{n} \to \pi_{+}\hat x = \hat x$ by the boundedness of $\pi_{+}$ and the continuity of $\widehat{\theta}$, and $\pi_{+}x_{n} \in X^{\theta}$, so $\hat x$ is a limit of fixed elements.

**Corollary (fixed points are limits of fixed points).** An element of the completion is fixed exactly when it is a limit of fixed elements of the original space; in particular a dense fixed subspace of a normed space forces the involution to be the identity, and the extension adds limits and no new fixed element.

**Proof.** The theorem together with the density criterion of *Involutive Topological Linear Spaces*.

## Automatic Continuity on a Banach Space

**Theorem (closed graph).** Let $X$ be a Banach space and let $T$ be an everywhere-defined linear involution of $X$ with closed graph. Then $T$ is continuous and is a topological isomorphism of $X$ onto itself; its norm satisfies $\lVert T\rVert \geq 1$, with equality exactly in the isometric case.

**Proof.** The closed graph theorem of *The Closed Graph Theorem* gives the continuity of an everywhere-defined linear map between Banach spaces with closed graph; the involution is then a continuous bijection with inverse itself, hence a topological isomorphism, and $\lVert T\rVert \geq 1$ by *Involutive Normed Spaces*.

**Corollary (the open mapping form).** A continuous linear surjection of Banach spaces is open, so a continuous linear involution of a Banach space is automatically a homeomorphism; the continuity cannot be improved to isometry without renorming, and $\lVert x\rVert_{T} = \sup(\lVert x\rVert, \lVert Tx\rVert)$ is the equivalent norm that makes it isometric.

**Proof.** The open mapping theorem is *The Open Mapping Theorem*; the renorming statement is *Involutive Normed Spaces*.

## The Dual

**Theorem (the dual is an involutive Banach space).** The dual $X^{*}$ with the dual norm is a Banach space, the transposed involution $\theta'(\varphi) = \varphi\circ\theta$ is a continuous involution of the same kind with

$$
\lVert\theta'\rVert = \lVert\theta\rVert ,
$$

and the fixed and negated subspaces of $\theta'$ are the annihilators of $X^{-}$ and $X^{\theta}$; hence $(X^{*}, \theta')$ is an involutive Banach space, isometric exactly when $\theta$ is isometric.

**Proof.** The completeness of the dual is *Banach Spaces*; the transposed involution and its norm are *Involutive Normed Spaces*, and the annihilator identification is *The Involution and the Dual Pairing*.

**Theorem (reflexivity and the second transpose).** If $X$ is reflexive then $(\theta')' = \theta$ under the canonical identification $X^{**} = X$, so the operation $\theta \mapsto \theta'$ is an involution of the class of involutive Banach spaces, and $(X^{*}, \theta')$ is reflexive exactly when $X$ is.

**Proof.** The identity $(\theta')' = \theta$ is the symmetry $(\theta^{t})^{t} = \theta$ of *The Involution and the Dual Pairing* under the canonical identification; reflexivity of the dual is *Duality Theory*.

## Examples

**Example (the sequence spaces).** On $\ell^{p}$, $1 \leq p \leq \infty$, and on $c_{0}$ the coordinatewise conjugation is an antilinear isometric involution, so each is an involutive Banach space with $\lVert\theta\rVert = 1$; the fixed subspace is the corresponding real sequence space, itself a Banach space over $\mathbb{R}$, and the dual of $\ell^{p}$ with the transposed involution is $\ell^{q}$ with the coordinatewise conjugation.

**Example (the function spaces).** On $C(K)$ for a compact Hausdorff $K$ the map $f \mapsto \overline{f}$ is an antilinear isometric involution with fixed subspace the real Banach space $C(K,\mathbb{R})$; on $L^{p}(\mu)$ the map $f \mapsto \overline{f}$ is an antilinear isometric involution with fixed subspace the real space $L^{p}(\mu,\mathbb{R})$, the completions of the corresponding finitely supported spaces.

**Example (the completion of an involutive space).** On $\mathbb{C}[x]$ with the $(x)$-adic topology the involution $\varphi_{0}(f)(x) = f(-x)$ is continuous with fixed subspace the even polynomials; its extension to the completion $\mathbb{C}[[x]]$ has fixed subspace the even power series, the closure of the even polynomials, and the extension adds limits and no new fixed element.

## Summary

On a Banach space a continuous involution has closed fixed and negated subspaces, which are therefore Banach spaces for the restricted norms; when $2$ is invertible the averaging projections exhibit the space as the topological direct sum $X^{\theta}\oplus X^{-}$, with the norms equivalent by the open mapping theorem. A continuous involution of a normed space extends uniquely to a continuous involution of the completion with the same norm and the same kind, and with $2$ invertible the fixed subspace of the completion is the closure of the fixed subspace, so the extension adds limits and no new fixed element. An everywhere-defined linear involution of a Banach space with closed graph is continuous by the closed graph theorem, and a continuous linear involution is automatically a homeomorphism. The dual with the transposed involution is again an involutive Banach space, $\lVert\theta'\rVert = \lVert\theta\rVert$, isometric exactly when $\theta$ is, with the fixed and negated parts the annihilators of the summands; when $X$ is reflexive the operation is an involution, $(\theta')' = \theta$. The sequence and function spaces with conjugation and the completion of the involutive $\mathbb{C}[x]$ are the standard examples. The metrisable locally convex case is *Involutive Fréchet Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $\lVert\cdot\rVert$ | Banach space and its norm |
| $\theta$, $T$ | Continuous involution; the linear case |
| $X^{\theta}$, $X^{-}$ | Closed summands, Banach spaces |
| $\pi_{\pm} = \frac12(\mathrm{id}\pm\theta)$ | Bounded averaging projections |
| $\widehat{X}$, $\iota$ | Completion and inclusion of a normed space |
| $\widehat{\theta}$, $\lVert\widehat{\theta}\rVert = \lVert\theta\rVert$ | Extended involution and its norm |
| $\widehat{X}^{\widehat{\theta}} = \overline{\iota(X^{\theta})}$ | Fixed subspace of the completion |
| $\theta'$, $\lVert\theta'\rVert = \lVert\theta\rVert$ | Transposed involution and its norm |
| $(\theta')' = \theta$ | Reflexive symmetry |

## Further Reading

- Stefan Banach, *Theory of Linear Operations* (North-Holland, 1987), for the completeness, the open mapping theorem and the closed graph theorem.
- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the involutive Banach spaces and the extension to the completion.
- Walter Rudin, *Functional Analysis* (McGraw-Hill, second edition, 1991), for the duality, the annihilators and the reflexivity.
- Robert E. Megginson, *An Introduction to Banach Space Theory* (Springer, 1998), for the normed and Banach background and the equivalences of norms.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the real structures and the transposed involutions.
