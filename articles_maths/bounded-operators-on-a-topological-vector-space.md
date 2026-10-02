
# __Bounded Operators on a Topological Vector Space__

## Introduction

The operators of a topological vector space are its continuous linear maps, and they form a vector space in their own right. This article fixes that space, its vector-space structure and its composition, and then studies the notion of **boundedness** attached to a linear map. On a normed space continuity and boundedness coincide, and the two are measured by a single number, the **operator norm**; on a general topological vector space continuity always implies boundedness, but the converse requires a bornological hypothesis on the domain, and a finite operator norm exists only when the target is normable.

The article assumes the topological vector spaces, the neighbourhoods of zero, the bounded sets and the locally convex spaces of *Topological Modules and Vector Spaces* and *Locally Convex Spaces*, the norms, the normed spaces, the bounded linear maps, the operator norm and the completeness theorems of *Normed and Banach Spaces*, and the duality of a locally convex space with its dual from *Duality Theory*. The topology of bounded convergence on the operator space, its completeness and the strong dual, are *Operators on a Locally Convex Space*; the transpose on the dual is *The Dual Operator*; the operator algebra as a normed algebra is *Bounded Operators and the Operator Norm*; the two-sided and signed operators built on this layer are the later articles of this group. Nothing analytic and nothing geometric is used: the spectrum, the spectral radius and the functional calculus are *Analysis on Linear Spaces* in Part III.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ and $E, F, G$ are topological vector spaces over $\mathbb{K}$, Hausdorff unless a norm or a completion is discussed. The space of continuous linear maps is $\mathcal{L}(E, F)$, its endomorphism form is $\mathcal{L}(E) = \mathcal{L}(E, E)$, the topological dual of $E$ is $E' = \mathcal{L}(E, \mathbb{K})$, and for normed spaces $X, Y$ the space of bounded linear maps is $B(X, Y) = \mathcal{L}(X, Y)$ with the **operator norm** $\lVert T\rVert$. A subset of a topological vector space is **bounded** when it is absorbed by every neighbourhood of $0$.

## The Space of Continuous Operators

**Definition.** The **continuous operators** from $E$ to $F$ are the linear maps $T : E \to F$ that are continuous; they form the subset $\mathcal{L}(E, F)$ of the vector space $F^{E}$ of all maps, and $\mathcal{L}(E, F)$ is a vector space under the pointwise operations, $(S + T)(x) = Sx + Tx$ and $(\lambda T)(x) = \lambda\,Tx$.

**Proposition (elementary properties).** Let $T : E \to F$ be linear. Then $T$ is continuous if and only if it is continuous at $0$, and then it is uniformly continuous for the additive uniformities; its kernel $\ker T$ is a closed subspace of $E$; for $S \in \mathcal{L}(F, G)$ the composite $ST$ lies in $\mathcal{L}(E, G)$; and for fixed $S$ the maps $T \mapsto ST$ and $T \mapsto TS$ are linear. The dual $E' = \mathcal{L}(E, \mathbb{K})$ is a subspace of the algebraic dual $E^{*}$, and it separates the points of $E$ when $E$ is locally convex.

**Proof.** Continuity of a linear map is translation-invariant, so continuity at one point is continuity everywhere; a continuous homomorphism of topological groups is uniformly continuous for the left uniformity, and an additive map preserves it, so the same holds for the right uniformity. The kernel is the preimage of the closed set $\{0\}$. Bilinearity of composition is the associativity and the linearity of the operators. The separation statement is the Hahn–Banach theorem in *Locally Convex Spaces*.

**Proposition (continuity is boundedness on a normed space).** Let $X, Y$ be normed spaces and let $T : X \to Y$ be linear. The following are equivalent: $T$ is continuous; $T$ is continuous at $0$; there is $C \geq 0$ with $\lVert Tx\rVert \leq C\lVert x\rVert$ for all $x$; $T$ maps bounded sets to bounded sets; $T$ is uniformly continuous. In this case the least constant is

$$
\lVert T\rVert = \sup_{x \neq 0}\frac{\lVert Tx\rVert}{\lVert x\rVert} = \sup_{\lVert x\rVert \leq 1}\lVert Tx\rVert = \sup_{\lVert x\rVert = 1}\lVert Tx\rVert ,
$$

the **operator norm** of $T$.

**Proof.** This is the theorem on bounded linear maps of *Normed and Banach Spaces*; the three expressions for the norm agree by homogeneity and the continuity of the norm, and the least constant is attained by the supremum over the unit sphere.

**Proposition (the operator norm makes $B(X, Y)$ a normed space).** With the operator norm, $B(X, Y)$ is a normed space, complete when $Y$ is complete; the norm is **submultiplicative**,

$$
\lVert ST\rVert \leq \lVert S\rVert\,\lVert T\rVert ,
$$

for composable bounded maps, so $B(X) = B(X, X)$ is a normed algebra with unit of norm one; and $\lVert T^{n}\rVert \leq \lVert T\rVert^{n}$ for every $n \geq 1$.

**Proof.** The norm axioms and submultiplicativity are *Normed and Banach Spaces*; the inequality for powers follows by induction from submultiplicativity, and the unit has norm one because $\lVert \mathrm{id}\rVert = \sup_{\lVert x\rVert \leq 1}\lVert x\rVert = 1$.

## Boundedness on a General Topological Vector Space

**Proposition (continuity implies boundedness).** Every $T \in \mathcal{L}(E, F)$ maps bounded subsets of $E$ to bounded subsets of $F$.

**Proof.** Let $B \subseteq E$ be bounded and let $V$ be a neighbourhood of $0$ in $F$. By continuity $T^{-1}(V)$ is a neighbourhood of $0$ in $E$, so it absorbs $B$: there is $\lambda > 0$ with $B \subseteq \lambda T^{-1}(V)$, hence $T(B) \subseteq \lambda V$. Therefore $V$ absorbs $T(B)$, and $T(B)$ is bounded.

**Definition.** A linear map $T : E \to F$ is **bounded** when it maps bounded sets to bounded sets. Thus every continuous operator is bounded; the converse is the content of the next proposition.

**Theorem (the bornological converse).** A locally convex space $E$ is **bornological** exactly when every bounded linear map $E \to F$ into a locally convex space $F$ is continuous; on a bornological space continuity and boundedness of linear maps coincide. Normed spaces are bornological.

**Proof.** The characterisation of bornological spaces by this property is the definition of the class in *Locally Convex Spaces*, where the bornological spaces are also shown to be the locally convex spaces that are inductive limits of normed spaces; a normed space is bornological because its bounded sets are the subsets of the multiples of its unit ball, so a map bounded on bounded sets is bounded on the unit ball and hence bounded. The statements are quoted from that article.

**Remark (the converse fails in general).** On a topological vector space that is not bornological there is a linear map, bounded on bounded sets, that is not continuous; equivalently, such a space carries a locally convex topology strictly finer than the bornological topology associated with it, and the identity is bounded but not continuous. The distinction disappears on normed spaces and on all Fréchet spaces, which are bornological.

## Examples of Operators and Norms

**Example (finite dimension).** For $X = \mathbb{K}^{m}$, $Y = \mathbb{K}^{n}$ every linear map is continuous, $B(\mathbb{K}^{m}, \mathbb{K}^{n})$ is the space $M_{n, m}(\mathbb{K})$ of matrices, and the operator norm is

$$
\lVert A\rVert_{\mathrm{op}} = \sup_{\lVert x\rVert_{2} \leq 1}\lVert Ax\rVert_{2} = \sigma_{1}(A) ,
$$

the largest singular value, the identification of the injective norm of *Topological Tensor Products*. For the identity matrix this is $1$, and for a diagonal matrix it is the largest modulus of a diagonal entry.

**Example (the shift on $\ell^p$).** On $X = \ell^p$, $1 \leq p \leq \infty$, the right shift $R(x_{1}, x_{2}, \dots) = (0, x_{1}, x_{2}, \dots)$ is a linear isometry, so $R \in B(\ell^p)$ with $\lVert R\rVert = 1$; the left shift $L(x_{1}, x_{2}, \dots) = (x_{2}, x_{3}, \dots)$ is surjective with $\lVert L\rVert = 1$, and $LR = \mathrm{id}$ while $RL \neq \mathrm{id}$, so $B(X)$ is not commutative.

**Example (diagonal and multiplication operators).** On $\ell^p$ the diagonal operator $D_{\varphi}(x_{k}) = (\varphi_{k}x_{k})$ is bounded exactly when $\varphi \in \ell^{\infty}$, and then $\lVert D_{\varphi}\rVert = \lVert \varphi\rVert_{\infty}$. On $C(K)$ for a compact Hausdorff space $K$ the multiplication operator $M_{f}(g) = fg$ is bounded for every $f \in C(K)$, with $\lVert M_{f}\rVert = \lVert f\rVert_{\infty}$.

**Example (functionals).** The continuous linear functionals are the elements of $E' = \mathcal{L}(E, \mathbb{K})$; for a normed space $X$ one has $\mathcal{L}(X, \mathbb{K}) = B(X, \mathbb{K}) = X^{*}$ with the norm $\lVert \varphi\rVert = \sup_{\lVert x\rVert \leq 1}\lvert \varphi(x)\rvert$, and the dual norm is computed by the polar calculus of *Duality Theory*.

## Products, Quotients and the Induced Map

**Proposition (products and quotients).** Let $T : E \to F \times G$ be linear with components $T_{1}, T_{2}$. Then $T$ is continuous if and only if both components are. Let $M \subseteq E$ be a subspace and let $q : E \to E/M$ be the quotient map; a linear map $S : E/M \to F$ is continuous if and only if $Sq$ is, and the **induced map**

$$
\overline{T} : E/{\ker T} \longrightarrow F, \qquad \overline{T}(q x) = Tx ,
$$

is a well-defined continuous linear injection when $T$ is continuous.

**Proof.** For the product, continuity of $T$ is continuity of each composite $\pi_{i}T = T_{i}$, and conversely the components assemble because the product topology is initial. For the quotient, $Sq$ continuous gives $S$ continuous by the universal property of the quotient topology, which is final; $S$ continuous gives $Sq$ continuous as a composite. The induced map is well defined because $T$ vanishes on $\ker T$, it is injective by construction, and it is continuous because $\overline{T}q = T$ and $q$ is a quotient map.

**Theorem (open mapping).** Let $E$ and $F$ be $F$-spaces and let $T \in \mathcal{L}(E, F)$ be surjective. Then $T$ is open, and the induced map $\overline{T} : E/{\ker T} \to F$ is a topological isomorphism. In particular a continuous linear bijection between Banach or Fréchet spaces is a topological isomorphism.

**Proof.** The open mapping theorem is proved in *Normed and Banach Spaces* for Banach spaces and in *Fréchet Spaces* for the metrisable complete case; openness of $T$ makes the quotient topology on $E/\ker T$, which is the finest making $q$ continuous, coincide with the initial topology carried by the bijection $\overline{T}$.

## Summary

The continuous operators $\mathcal{L}(E, F)$ between topological vector spaces form a vector space under the pointwise operations, closed under composition, with $E' = \mathcal{L}(E, \mathbb{K})$, and every continuous operator is bounded, carrying bounded sets to bounded sets. On normed spaces $X, Y$ continuity and boundedness coincide, and the operator norm

$$
\lVert T\rVert = \sup_{\lVert x\rVert \leq 1}\lVert Tx\rVert
$$

is the least constant in the bound $\lVert Tx\rVert \leq \lVert T\rVert\lVert x\rVert$; it makes $B(X, Y)$ a normed space, complete when $Y$ is complete, submultiplicative under composition, so $B(X)$ is a normed algebra with $\lVert T^{n}\rVert \leq \lVert T\rVert^{n}$. On a locally convex space the converse direction, that a bounded linear map is continuous, holds exactly when the space is bornological, which normed spaces and Fréchet spaces are; on a general topological vector space the converse can fail. The finite-dimensional, diagonal, shift and multiplication examples fix the norm in the standard cases, and the induced map $E/\ker T \to F$ of a continuous operator is a continuous injection, a topological isomorphism when $E$ and $F$ are $F$-spaces and $T$ is surjective.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$ |
| $E, F, G$ | Topological vector spaces over $\mathbb{K}$ |
| $\mathcal{L}(E, F)$ | Continuous linear maps $E \to F$ |
| $\mathcal{L}(E)$, $B(E)$ | Continuous, respectively bounded, endomorphisms of $E$ |
| $E' = \mathcal{L}(E, \mathbb{K})$ | Topological dual |
| $E^{*}$ | Algebraic dual |
| $\lVert T\rVert$ | Operator norm, $\sup_{\lVert x\rVert \leq 1}\lVert Tx\rVert$ |
| $B(X, Y)$ | Bounded linear maps of normed spaces |
| $\lVert ST\rVert \leq \lVert S\rVert\lVert T\rVert$ | Submultiplicativity |
| $T^{n}$ | Iterated composition of an endomorphism |
| $\overline{T} : E/{\ker T} \to F$ | The map induced by $T$ |
| bounded | Absorbed by every neighbourhood of $0$; for a map, carrying bounded sets to bounded sets |
| bornological | Locally convex space on which bounded linear maps are continuous |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the space of continuous linear maps, the bounded sets and the bornological spaces.
- Gottfried Köthe, *Topological Vector Spaces I* (Springer, 1969), for the operator spaces of a topological vector space and the topology of bounded convergence.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the bounded operators, the bornological spaces and the uniform boundedness principle.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, second edition, 1991), for the bounded linear maps, the operator norm and the open mapping theorem.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the normed operators and the standard examples of norms.
