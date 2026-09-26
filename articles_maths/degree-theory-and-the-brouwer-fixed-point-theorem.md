
# __Degree Theory and the Brouwer Fixed Point Theorem__

## Introduction

Let $f : S^n \to S^n$ be a continuous map of the sphere to itself. Since $H_n(S^n;\mathbb{Z}) \cong \mathbb{Z}$, the induced map on the top homology is multiplication by an integer, and that integer is the **degree** $\deg f$: it counts, with signs, how many times $f$ wraps the sphere around itself. The degree is the simplest homological invariant of a self-map, and it is a complete invariant of the homotopy class (Hopf's theorem); it governs the existence of fixed points, of retractions and of nonvanishing vector fields, and it is the source of the classical topological fixed point theorems: the **Brouwer fixed point theorem**, that every continuous self-map of a closed disc has a fixed point, and the **Lefschetz fixed point theorem**, that a continuous self-map of a finite CW complex whose **Lefschetz number** is nonzero has a fixed point. The two are related: Brouwer's theorem follows from Lefschetz's by the vanishing of the reduced homology of the disc except in degree zero, and the Lefschetz number of a self-map of the sphere is computed by the degree.

The distinction from the analytic fixed-point theory must be made at once. **The topological degree is the subject of this article**: the degree of a map of spheres and of closed oriented manifolds, defined by the top homology class and computed by the local degrees at the points of a fibre, together with the fixed point theorems that follow from it. The **analytic fixed point theory is not**: the Banach contraction principle, the Schauder and Leray–Schauder fixed point theorems, the degree of a map between Banach spaces and the fixed point theorems for continuous maps of infinite-dimensional convex sets are the subject of of Part III, planned, where the completeness and the limit are available; they are not used and not developed here. Nor is the integration theory of Part III used: the formula expressing the degree as the ratio of two integrals of a top form is quoted from the *Differential Forms and Stokes' Theorem*, where the integral of a top form over an oriented manifold is constructed, and the degree is here defined homologically and computed by the local degrees, in the manner of *Simplicial and Singular Homology* and *Poincaré Duality*.

The article defines the degree and establishes its properties — homotopy invariance, multiplicativity, the behaviour under suspension and under reflections, the local degree formula at a regular value, and the identification with the winding number in dimension one; it then proves the Brouwer fixed point theorem by way of the nonexistence of a retraction of the disc onto its boundary; it states and applies the Lefschetz fixed point theorem, computing the Lefschetz number of the sphere and of the torus; and it closes with the classical applications: the hairy ball theorem on nonvanishing vector fields, the Borsuk–Ulam theorem on antipodal pairs, the Jordan–Brouwer separation theorem and the invariance of domain.

Throughout, $S^n$ is the unit sphere in $\mathbb{R}^{n+1}$, $D^{n+1}$ the closed unit disc, $\deg f$ the degree of a self-map of $S^n$, $L(f)$ the Lefschetz number of a self-map of a finite CW complex, and $\chi(X)$ the Euler characteristic. Homology is singular with $\mathbb{Z}$ coefficients unless another coefficient ring is named; $f_*$ denotes the induced map on homology and $f^*$ the induced map on cohomology.

## The Degree of a Map of Spheres

### Definition and Well-Definedness

**Definition.** Let $n \geq 1$ and let $f : S^n \to S^n$ be continuous. The **degree** of $f$ is the unique integer $\deg f$ such that

$$
f_* : H_n(S^n;\mathbb{Z}) \to H_n(S^n;\mathbb{Z}), \qquad f_*[S^n] = (\deg f)\,[S^n],
$$

where $[S^n]$ is the fundamental class of $S^n$ with either orientation, fixed once and for all.

**Proposition (well-definedness).** The degree is well defined, and for $n \geq 1$ it is an integer; the assignment $f \mapsto \deg f$ is constant on homotopy classes and complete, in the sense that two self-maps of $S^n$ are homotopic if and only if they have the same degree (Hopf).

*Proof.* $H_n(S^n;\mathbb{Z}) \cong \mathbb{Z}$ by *Simplicial and Singular Homology*, so a homomorphism of $\mathbb{Z}$ to itself is multiplication by an integer, determined by its effect on a generator; the fundamental class generates, and the choice of orientation changes both $[S^n]$ and $\deg f$ by a common sign, so the integer is independent of the choice. Homotopy invariance is the homotopy invariance of the induced map on homology. The converse, Hopf's theorem, is standard and is quoted. $\square$

**Theorem (elementary properties).** For continuous self-maps of $S^n$:

1. $\deg(\mathrm{id}) = 1$, and $\deg f = \pm 1$ whenever $f$ is a homotopy equivalence.
2. $\deg(g \circ f) = \deg g \cdot \deg f$.
3. If $f \simeq g$ then $\deg f = \deg g$: the degree is a homotopy invariant.
4. $\deg f = 0$ if and only if $f$ is null-homotopic.
5. The **suspension** satisfies $\deg(\Sigma f) = \deg f$, where $\Sigma f$ is the suspension of $f$, and more generally the degree is stable under the suspension isomorphism of *Homotopy Groups and Fibrations*.

*Proof.* (1) and (2) are functoriality. (3) is the homotopy invariance of $f_*$. (4) A null-homotopic $f$ factors through a point and hence induces the zero map on $H_n$ for $n \geq 1$; conversely if $\deg f = 0$ then $f_* = 0$ on $H_n(S^n)$, and since $S^n$ is a Moore space in the top degree, the homotopy class of $f$ is detected by its effect on $H_n$; the vanishing therefore implies null-homotopy by Hopf's theorem. (5) The suspension isomorphism $H_n(S^n)\cong H_{n+1}(S^{n+1})$ is natural, so $\Sigma f$ has the same degree. $\square$

**Example (reflections and the antipodal map).** The reflection $r_i$ changing the sign of one coordinate of $\mathbb{R}^{n+1}$ restricts to a self-map of $S^n$ of degree $-1$, since it reverses the orientation of the sphere; the **antipodal map** $A(x) = -x$ is the composition of the $n+1$ reflections $r_0,\ldots,r_n$, so

$$
\deg A = (-1)^{n+1}.
$$

For $n = 1$ the antipodal map of the circle has degree $(-1)^2 = 1$, the rotation by $\pi$, and indeed it is homotopic to the identity; for $n = 2$ it has degree $-1$.

**Example (the circle and the winding number).** For $n = 1$ the degree of $f : S^1 \to S^1$ is the **winding number**: under the identification $\pi_1(S^1) \cong \mathbb{Z}$ of *The Fundamental Group and Covering Spaces*, the class of $f$ in $\pi_1(S^1)$ is $\deg f$, and the two agree by the Hurewicz theorem of *Homotopy Groups and Fibrations*, $H_1(S^1) \cong \pi_1(S^1)^{\mathrm{ab}} \cong \mathbb{Z}$. The map $z \mapsto z^k$ has degree $k$; a homeomorphism of the circle of geometric rotation angle $\theta$ has degree $1$; and a map that reverses orientation has degree $-1$.

**Example (linear maps).** If $T \in O(n+1)$ is an orthogonal transformation, then the induced $f_T : S^n \to S^n$ has $\deg f_T = \det T$, the sign of the determinant being exactly the orientation behaviour. In particular the identity component $SO(n+1)$ acts by maps of degree $1$, and an orientation-reversing orthogonal map has degree $-1$.

### Local Degree and the Regular Value Formula

**Definition.** Let $f : S^n \to S^n$ be continuous and let $y \in S^n$ with $f^{-1}(y)$ finite, say $f^{-1}(y) = \{x_1,\ldots,x_m\}$. The **local degree** $\deg_{x_i}f$ is defined by choosing a small disc $D_i$ around $x_i$ with $f(\partial D_i) \subseteq S^n \setminus \{y\}$ and setting $\deg_{x_i}f$ to be the degree of the induced map of pairs

$$
f_* : H_n(D_i,\partial D_i) \to H_n(S^n, S^n\setminus\{y\}) \cong \mathbb{Z},
$$

the identifications being by excision and by the local homology of $S^n$.

**Theorem (the sum formula).** With $f$ and $y$ as above, and only finitely many $x_i$ with $\deg_{x_i}f \neq 0$, there is the **sum formula**

$$
\deg f = \sum_{i=1}^{m} \deg_{x_i}f .
$$

*Proof.* Consider the commutative diagram in which the top row is the Mayer–Vietoris sequence of the decomposition $S^n = \bigsqcup_i D_i \cup (S^n \setminus \bigcup_i \operatorname{int}D_i)$, using that $H_n(\partial D_i) = 0$ for $n \geq 2$ and the pair sequence for $n = 1$; the induced map sends the fundamental class to the sum of the local fundamental classes, and evaluating against $[S^n]$ gives the formula. $\square$

**Theorem (the regular value formula).** Let $f : S^n \to S^n$ be smooth and let $y \in S^n$ be a **regular value** of $f$, that is, a point such that the differential $df_x$ is invertible for every $x \in f^{-1}(y)$. Then $f^{-1}(y)$ is finite, and

$$
\deg f = \sum_{x \in f^{-1}(y)} \operatorname{sign}\det\bigl(df_x : T_xS^n \to T_yS^n\bigr),
$$

the signs being computed with respect to orientations of the tangent spaces induced by those of the spheres.

*Proof sketch.* By the inverse function theorem each $x \in f^{-1}(y)$ has a neighbourhood mapped diffeomorphically to a neighbourhood of $y$; the local degree is $\pm 1$ according to whether that local diffeomorphism preserves or reverses the orientation, i.e. according to the sign of the Jacobian determinant; the sum formula gives the result, and the sum formula itself shows that only finitely many terms are nonzero. $\square$

**Example (the regular value formula on the circle).** For $f(z) = z^k$ on $S^1$ and $y = 1$, the preimage is the set of $k$-th roots of unity, each of local degree $+1$, and the sum formula gives $\deg f = k$, in agreement with the winding number computation.

**Remark (the integral formula).** The degree has an analytic expression: for a smooth $f : S^n \to S^n$ and an $n$-form $\omega$ on $S^n$ with $\int_{S^n}\omega \neq 0$,

$$
\deg f = \frac{\int_{S^n} f^*\omega}{\int_{S^n}\omega},
$$

an immediate consequence of the change of variables formula for the integral of a top form, as constructed in the written *Differential Forms and Stokes' Theorem*. This article does not use the formula as a definition: the degree is homological, and the integral formula is quoted for orientation. The measure theory behind the change of variables formula, and the $L^p$ theory of the resulting densities, belong to Part III.

## The Degree of a Map of Manifolds

### Closed Oriented Manifolds

**Definition.** Let $M$, $N$ be closed connected oriented $n$-manifolds. For a continuous $f : M \to N$ the **degree** is the integer $\deg f$ with

$$
f_*[M] = (\deg f)\,[N] \in H_n(N;\mathbb{Z}) \cong \mathbb{Z},
$$

where the fundamental classes are the orientation classes of *Poincaré Duality*.

**Theorem (properties of the degree of a manifold map).** The degree of a map of closed connected oriented $n$-manifolds is well defined, homotopy invariant, multiplicative under composition, satisfies $\deg(\mathrm{id}) = 1$, and is computed by the sum of the local degrees over the fibre of any point of the target; only finitely many local degrees are nonzero, so the sum is finite:

$$
\deg f = \sum_{x \in f^{-1}(y)} \deg_x f,
$$

the sum being finite for every $y$, since the local degrees vanish at all but finitely many points.

*Proof.* The proofs are those of the sphere case, with $H_n(S^n)$ replaced by $H_n(N)$ and the local homology $H_n(N, N\setminus\{y\}) \cong \mathbb{Z}$ of *Poincaré Duality* replacing the corresponding group for the sphere. $\square$

**Theorem (nonorientable manifolds; degree modulo 2).** Let $M$, $N$ be closed connected $n$-manifolds with $n \geq 1$. With $\mathbb{F}_2$ coefficients, $H_n(M;\mathbb{F}_2) \cong \mathbb{F}_2$ and $H_n(N;\mathbb{F}_2) \cong \mathbb{F}_2$, by the local homology computation with $\mathbb{F}_2$ coefficients of *Poincaré Duality* applied to the mod $2$ fundamental classes; hence there is a well-defined **degree modulo 2** $\deg_2 f \in \mathbb{F}_2$ with $f_*[M]_2 = (\deg_2 f)[N]_2$, and $\deg_2 f \equiv \deg f \bmod 2$ whenever the integral degree is defined.

*Proof.* The class $[M]_2$ generates $H_n(M;\mathbb{F}_2)$ over $\mathbb{F}_2$, so the homomorphism $f_*$ is multiplication by an element of $\mathbb{F}_2$, determined by the image of the generator. The congruence with the integral degree follows by reducing $f_*[M] = (\deg f)[N]$ modulo $2$. $\square$

**Remark.** The degree of a map of spheres is thus the special case $M = N = S^n$; for maps $S^n\to S^n$ the local degree at a point is $\pm 1$ or $0$, while for general manifolds it can be any integer, and it is the obstruction to $f$ being a covering map: a map of degree $d$ between closed connected oriented $n$-manifolds with $|d| = \#$fibre and the local degrees all $+1$ is a covering.

### Boundaries and Applications of the Degree

**Definition.** Let $M$ be a compact oriented $n$-manifold with boundary and $N$ a closed connected oriented $n$-manifold. For a continuous $f : M \to N$ the **degree** is defined by $f_*[M,\partial M] = (\deg f)[N]$ using the relative fundamental class of *Poincaré Duality*.

**Theorem (boundary dependence).** If $f, g : M \to N$ are continuous and agree on $\partial M$, then $\deg f = \deg g$; in particular the degree of $f$ is determined by the restriction $f|_{\partial M}$ up to addition of the degrees of maps of $M$ that vanish on the boundary.

*Proof.* The difference $f_* - g_*$ on $H_n(M,\partial M)$ factors through the quotient $M/\partial M$ by the hypothesis that $f$ and $g$ agree on the boundary; the resulting map $H_n(M/\partial M) \to H_n(N)$ is independent of the choice of the extension, and the two degrees agree. $\square$

**Corollary (maps of nonzero degree are surjective).** Let $f : M \to N$ be a map between closed connected oriented $n$-manifolds with $\deg f \neq 0$. Then $f$ is surjective.

*Proof.* If $y \notin f(M)$, then $f^{-1}(y) = \emptyset$, and the sum formula applied at the point $y$ gives $\deg f = \sum_{x \in f^{-1}(y)}\deg_x f = 0$, an empty sum; hence $\deg f = 0$, a contradiction. $\square$

**Corollary (no retraction of the disc onto the sphere).** For $n \geq 1$ there is no continuous map $r : D^{n+1} \to S^n$ with $r|_{S^n} = \mathrm{id}$.

*Proof.* If such an $r$ existed, the composite $r_* \circ i_*$ on $H_n(S^n)$ would be the identity of $\mathbb{Z}$, where $i : S^n \to D^{n+1}$ is the inclusion; but $i_*$ factors through $H_n(D^{n+1}) = 0$ since $D^{n+1}$ is contractible, so $r_* i_* = 0$, a contradiction. $\square$

## The Brouwer Fixed Point Theorem

### Statement and Proof

**Theorem (Brouwer).** Every continuous map $f : D^{n+1} \to D^{n+1}$ has a fixed point, for every $n \geq 0$.

*Proof.* Suppose $f(x) \neq x$ for every $x \in D^{n+1}$. For each $x$, let $u(x) = x - f(x) \neq 0$ and define

$$
r(x) = x + t(x)u(x), \qquad t(x) = \frac{-x\cdot u(x) + \sqrt{\bigl(x\cdot u(x)\bigr)^2 + \bigl(1 - |x|^2\bigr)|u(x)|^2}}{|u(x)|^2},
$$

the point where the ray from $f(x)$ through $x$ meets $S^n$. The radicand is nonnegative because $|x| \leq 1$ on the disc, the denominator is nonzero by hypothesis, and $t$ is continuous in $x$; hence $r$ is continuous, $|r(x)| = 1$ by construction, and for $|x| = 1$ one has $t(x) = 0$ and $r(x) = x$. Thus $r$ would be a retraction of $D^{n+1}$ onto $S^n$, contradicting the preceding corollary. $\square$

**Remark.** The proof shows the logical equivalence of three statements: Brouwer's fixed point theorem; the nonexistence of a retraction of $D^{n+1}$ onto $S^n$; and the nontriviality of $H_n(S^n;\mathbb{Z})$. The form of the argument — a fixed point free map would produce a retraction, and a retraction is excluded by a homology computation — is the prototype of the degree-theoretic proofs in the rest of the article, and it is precisely the argument that fails in infinite dimensions, where the unit ball of a Banach space is not compact and the corresponding convex-set fixed point theorems require compactness or completeness assumptions and are theorems of Part III.

### Equivalent and Generalised Forms

**Theorem (general forms of Brouwer).** The following hold:

1. Every continuous self-map of a space homeomorphic to $D^{n+1}$, and more generally of a compact convex subset of a finite-dimensional normed space, has a fixed point.
2. Every continuous map $f : D^n \to \mathbb{R}^n$ with $f(S^{n-1}) \subseteq D^n$ has a fixed point.
3. If $C \subseteq \mathbb{R}^n$ is compact and convex and nonempty, then every continuous $f : C \to C$ has a fixed point.

*Proof.* (1) A compact convex subset of a finite-dimensional normed space is a retract of a closed disc containing it, and the retraction can be chosen to be the radial projection from an interior point; composing $f$ with the retraction reduces to the disc case. (2) is (1) after observing that the hypothesis on the boundary guarantees that $f(D^n) \subseteq D^n$ up to the reduction of composing with the radial projection, so the disc case applies. (3) is (1) with the norm of the ambient finite-dimensional space. $\square$

**Corollary (the sphere theorem).** A continuous map $f : S^n \to S^n$ of degree $\neq 0$ is surjective, and the identity map of $S^n$ is not null-homotopic; the sphere $S^n$ is not contractible.

*Proof.* The first is the corollary of the previous section; the second is the case $f = \mathrm{id}$ of degree $1$; the third is the definition of contractible applied to the identity. $\square$

**Example (the fundamental theorem of algebra, as a degree statement).** Let $p(z) = a_dz^d + \cdots + a_0$ with $d \geq 1$ and $a_d \neq 0$. The rational map $z \mapsto p(z)$ extends continuously to the one-point compactification $S^2 = \mathbb{C}\cup\{\infty\}$ by sending $\infty$ to $\infty$, and the extension has degree $d$: near infinity, $p(z)/z^d$ tends to $a_d$, so the local degree at the pole is the same as that of $z\mapsto a_dz^d$, namely $d$. A map of degree $d \neq 0$ of $S^2$ is surjective, by the corollary above, so the value $0$ is attained on $S^2$; since $p(\infty) = \infty \neq 0$, it is attained at a point of $\mathbb{C}$, which is the root. No analysis beyond the degree and the compactification is used.

## The Lefschetz Fixed Point Theorem

### The Lefschetz Number

**Definition.** Let $X$ be a finite CW complex and $f : X \to X$ continuous. The **Lefschetz number** is

$$
L(f) = \sum_{i \geq 0} (-1)^i \operatorname{tr}\bigl(f_* : H_i(X;\mathbb{Q}) \to H_i(X;\mathbb{Q})\bigr),
$$

the sum being finite because $X$ is a finite complex. The Lefschetz number is a homotopy invariant of $f$ and satisfies $L(g \circ f) = L(f \circ g)$ when the composites are defined.

**Theorem (Lefschetz fixed point theorem).** If $L(f) \neq 0$ then $f$ has a fixed point.

*Proof sketch.* Suppose first that $X = M$ is a closed smooth manifold. The fixed points of $f$ are the points of the intersection of the **graph** $\Gamma_f = \{(x,f(x))\} \subseteq M \times M$ with the **diagonal** $\Delta \subseteq M\times M$. By Poincaré duality the algebraic intersection number $\Gamma_f \cdot \Delta$ of the two $n$-dimensional cycles in the $2n$-manifold $M\times M$ is well defined, and it is computed by the **Lefschetz trace formula**: the cup product structure of $H^*(M\times M)$ given by the Künneth theorem of *Cup and Cap Products* identifies $\Gamma_f\cdot\Delta$ with $\sum_i(-1)^i\operatorname{tr}(f_*|H_i(M;\mathbb{Q})) = L(f)$. If $f$ has no fixed point the cycles are disjoint, so the intersection number is zero, and $L(f) = 0$. The general finite CW complex case is reduced to the manifold case by embedding $X$ in a Euclidean space and thickening to a regular neighbourhood, using the homotopy invariance of $L$. $\square$

**Corollary (Brouwer, via Lefschetz).** Every continuous self-map of a contractible finite CW complex, and in particular of $D^{n+1}$, has a fixed point.

*Proof.* For a contractible space $H_i = 0$ for $i > 0$ and $H_0 \cong \mathbb{Q}$, so $L(f) = \operatorname{tr}(f_*|H_0) = 1 \neq 0$, and the theorem applies. $\square$

**Corollary (the Euler characteristic).** For a finite CW complex $X$, $L(\mathrm{id}) = \chi(X)$; in particular a finite CW complex with $\chi(X) \neq 0$ has the property that every map homotopic to the identity has a fixed point.

*Proof.* $L(\mathrm{id}) = \sum_i(-1)^i\operatorname{tr}(\mathrm{id}|H_i) = \sum_i(-1)^i\dim_{\mathbb{Q}}H_i(X;\mathbb{Q}) = \chi(X)$, by the identification of the Euler characteristic with the alternating sum of the Betti numbers of *Simplicial and Singular Homology*. $\square$

### Computation on Spheres and Tori

**Theorem (the Lefschetz number of a sphere).** For a continuous $f : S^n \to S^n$, $n \geq 1$, the homology is $\mathbb{Q}$ in degrees $0$ and $n$ and zero elsewhere, with $f_* = \mathrm{id}$ in degree $0$ and $f_* = \deg f$ in degree $n$; hence

$$
L(f) = 1 + (-1)^n \deg f .
$$

Consequently:

1. For $n$ even, every self-map of $S^n$ with $\deg f \neq -1$ has a fixed point, and the degree $(-1)^{n+1} = -1$ is the only degree compatible with a fixed-point-free map.
2. For $n$ odd, every self-map of $S^n$ with $\deg f \neq 1$ has a fixed point, and the antipodal map, of degree $(-1)^{n+1} = 1$, is fixed-point-free.

*Proof.* $L(f) = 1 + (-1)^n\deg f$ by the computation of the homology of the sphere and of $f_*$; the theorem gives a fixed point whenever the number is nonzero, and the antipodal map shows the remaining case is realised. $\square$

**Example.** On $S^1$ a rotation by angle $\theta \neq 0$ has degree $1$ and no fixed points, and $L = 1 - 1 = 0$. The identity, the rotation by $0$, also has $L = 1 - 1 = 0$ although every point is fixed: the Lefschetz number vanishes for every self-map of the circle of degree $1$, so the converse of the theorem fails. On $S^2$ the antipodal map has degree $-1$ and no fixed points, and $L = 1 + (-1) = 0$; every other degree gives a fixed point, including degree $0$: a constant map has its image point fixed.

**Theorem (the Lefschetz number of a torus).** Let $f : T^n \to T^n$ be a continuous self-map of the $n$-torus, with $T^n = \mathbb{R}^n/\mathbb{Z}^n$, and let $A$ be the matrix of $f_* : H_1(T^n;\mathbb{Z}) \to H_1(T^n;\mathbb{Z}) \cong \mathbb{Z}^n$. Then $f_*$ on $H_i(T^n;\mathbb{Z}) \cong \Lambda^i\mathbb{Z}^n$ is the $i$-th exterior power of $A$, and

$$
L(f) = \sum_{i=0}^n (-1)^i \operatorname{tr}\bigl(\Lambda^iA\bigr) = \det(I - A).
$$

In particular, if $\det(I - A) \neq 0$ then every continuous self-map of $T^n$ inducing $A$ on $H_1$ has a fixed point.

*Proof.* The Künneth theorem identifies $H_*(T^n)$ with the exterior algebra on $H_1$, and the induced map is the exterior power; the alternating sum of the traces of the exterior powers is the determinant $\det(I-A)$ by the standard identity for the characteristic polynomial, $\sum_i(-1)^i\operatorname{tr}(\Lambda^iA) = \det(I-A)$. The last statement is the Lefschetz theorem. $\square$

**Example.** For $n = 1$ the map $z \mapsto z^k$ has $A = (k)$ and $L = 1 - k$; for $k \neq 1$ there is a fixed point. For $k = 1$ the map is the identity, with $L = 0$ and every point fixed, while a nontrivial rotation $z \mapsto az$ with $a \neq 1$, which also has degree $1$, has no fixed point; the vanishing of $L$ therefore does not by itself decide the question. For $n = 2$ and $A = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$, $\det(I - A) = 2 \neq 0$, so the induced map — the "rotation" of the torus — has a fixed point, as it must, the fixed point being the origin.

**Remark (the converse).** The Lefschetz number is a lower bound and not the whole answer. The **Nielsen number** $N(f)$ of a self-map of a closed manifold satisfies $N(f) \geq \lvert L(f) \rvert$, and by Wecken's theorem $N(f)$ is the minimal number of fixed points in the homotopy class of $f$ when the dimension is at least $3$; a vanishing Lefschetz number therefore guarantees a fixed-point-free map in the homotopy class only when the Nielsen number vanishes too. For the sphere and the torus the criterion is exact in every dimension, the fixed-point-free examples being realised by the antipodal map and by the translations.

## Applications

### Nonvanishing Vector Fields and the Hairy Ball Theorem

**Definition.** A **vector field** on a smooth manifold $M$ is a section of the tangent bundle; it is **nonvanishing** if $X(x) \neq 0$ for every $x$.

**Theorem (Poincaré–Hopf).** Let $M$ be a closed connected smooth manifold and $X$ a vector field on $M$ with isolated zeros. Then the sum of the **indices** of the zeros of $X$ — the local degrees of the vector field around each zero — equals the Euler characteristic $\chi(M)$; consequently, if $\chi(M) \neq 0$ then every continuous vector field on $M$ has a zero.

*Proof sketch.* Choose a metric and replace $X$ by a small perturbation with only nondegenerate zeros, which does not change the index sum. At a nondegenerate zero $x$ the index is $\pm 1$, computed as the local degree at $x$ of the map $x' \mapsto X(x')/|X(x')|$ from a small sphere around $x$ to the unit sphere; the sum of the indices is therefore the degree of that map on the boundary of a disc bundle neighbourhood, which is the evaluation $\langle e(TM),[M]\rangle$ of the Euler class of the tangent bundle on the fundamental class. The Poincaré–Hopf theorem is the identification of this Euler number with $\chi(M)$, which is the statement $L(\mathrm{id}) = \chi(M)$ of the Lefschetz fixed point theorem read through the tangent bundle. $\square$

**Corollary (the hairy ball theorem).** Since $\chi(S^n) = 1 + (-1)^n$ by *Poincaré Duality*, the sphere $S^n$ admits a nonvanishing continuous tangent vector field if and only if $n$ is odd.

*Proof.* For $n$ even, $\chi(S^n) = 2 \neq 0$, so every continuous field has a zero by Poincaré–Hopf. For $n$ odd, $\chi(S^n) = 0$ and the field

$$
X(x_0,x_1,\ldots,x_{n-1},x_n) = (-x_1, x_0, -x_3, x_2, \ldots, -x_n, x_{n-1})
$$

is tangent, $x\cdot X(x) = 0$, and nonvanishing, $|X(x)| = |x| = 1$; the pairing of consecutive coordinates is possible because $n+1$ is even. $\square$

### Antipodal Points and Borsuk–Ulam

**Theorem (Borsuk's theorem on odd maps).** A continuous map $g : S^n \to S^n$ with $g(-x) = -g(x)$ for every $x$ — an **odd** map — has odd degree.

*Proof sketch.* An odd map commutes with the antipodal map $A$, of degree $(-1)^{n+1}$, and descends to a self-map of the quotient $\mathbb{RP}^n$; the transfer relating the cohomology of $S^n$ to that of $\mathbb{RP}^n$ shows that the degree of an odd map is congruent to $1$ modulo $2$. $\square$

**Theorem (Borsuk–Ulam).** For every continuous $f : S^n \to \mathbb{R}^n$ there is a point $x \in S^n$ with $f(x) = f(-x)$.

*Proof.* Suppose $f(x) \neq f(-x)$ for every $x$, and put

$$
g(x) = \frac{f(x) - f(-x)}{|f(x) - f(-x)|} \in S^{n-1} \subseteq \mathbb{R}^n .
$$

Then $g$ is continuous and odd, $g(-x) = -g(x)$, so the restriction of $g$ to the equator $S^{n-1} = \{x \in S^n : x_{n+1} = 0\}$ is an odd map $S^{n-1}\to S^{n-1}$, of odd degree by Borsuk's theorem, hence of degree $\neq 0$. But $g$ is defined on the whole of $S^n$ and hence on the upper hemisphere $D^n_+$, whose boundary is the equator; therefore $g|_{S^{n-1}}$ extends to a map of the disc and is null-homotopic, of degree $0$, a contradiction. $\square$

**Corollary (the ham sandwich theorem, in dimension two).** For any two bounded measurable regions $A, B$ of the plane there is a line bisecting both areas. The notion of area required by the statement is supplied by the measure theory of Part III; what is proved here is the topological input, the Borsuk–Ulam theorem, and the reduction of the bisection problem to it is a standard argument of Part III.

**Corollary (odd maps into spheres do not exist).** There is no continuous odd map $g : S^n \to S^{n-1}$ for $n \geq 1$.

*Proof.* Such a $g$ would make the composite $h = i \circ g : S^n \to S^n$ odd, where $i : S^{n-1}\hookrightarrow S^n$ is the equatorial inclusion; by Borsuk's theorem $\deg h$ would be odd, hence nonzero. But $h$ factors through $S^{n-1}$, and $H_n(S^{n-1};\mathbb{Z}) = 0$ for $n \geq 2$, so $h_* = 0$ on $H_n(S^n)$ and $\deg h = 0$; for $n = 1$ the same conclusion follows because $S^0$ is disconnected and $H_1(S^0) = 0$. The contradiction proves the claim. $\square$

### Separation and Invariance of Domain

**Theorem (the Jordan–Brouwer separation theorem).** Let $\Sigma \subseteq S^n$ be a subset homeomorphic to $S^{n-1}$, with $n \geq 2$. Then $S^n \setminus \Sigma$ has exactly two connected components, and $\Sigma$ is the boundary of each.

*Proof sketch.* By **Alexander duality**, which for a compact subset $K \subseteq S^n$ states $\tilde H_i(S^n\setminus K;\mathbb{Z}) \cong \tilde H^{n-i-1}(K;\mathbb{Z})$, and is a consequence of the Lefschetz duality of *Poincaré Duality* applied to a regular neighbourhood; applying it to $K = \Sigma \cong S^{n-1}$ gives

$$
\tilde H_0(S^n\setminus\Sigma) \cong \tilde H^{n-1}(S^{n-1}) \cong \mathbb{Z}, \qquad \tilde H_i(S^n\setminus\Sigma) \cong \tilde H^{n-i-1}(S^{n-1}) = 0 \quad (i \neq 0),
$$

where the last vanishing uses $n-i-1 \neq n-1$, i.e. $i \neq 0$. A space with $\tilde H_0$ free of rank one and all reduced homology in positive degrees zero has exactly two path components, and the complement of each component is exactly $\Sigma$, so each component has $\Sigma$ as boundary. $\square$

**Theorem (invariance of domain; Brouwer).** If $U \subseteq \mathbb{R}^n$ is open and $f : U \to \mathbb{R}^n$ is injective and continuous, then $f(U)$ is open and $f$ is a homeomorphism onto its image.

*Proof sketch.* It suffices to show that $f(U)$ contains a neighbourhood of $f(x)$ for every $x \in U$; choose a closed disc $D \subseteq U$ around $x$ and apply the Jordan–Brouwer theorem to the image of $\partial D$, which is a sphere in $\mathbb{R}^n$ contained in $f(U)$; the complement of that sphere has two components, and $f(x)$ lies in the bounded one, which is contained in $f(D) \subseteq f(U)$. The argument uses only the separation theorem, hence no analysis beyond the topology of $\mathbb{R}^n$ as a normed space. $\square$

**Corollary (dimension is a topological invariant).** If $\mathbb{R}^n$ and $\mathbb{R}^m$ are homeomorphic, then $n = m$.

*Proof.* Suppose $n < m$ and let $h : \mathbb{R}^n \to \mathbb{R}^m$ be a homeomorphism. Identify $\mathbb{R}^n$ with the coordinate subspace $\mathbb{R}^n\times\{0\} \subseteq \mathbb{R}^m$ and let $g = \iota \circ h^{-1} : \mathbb{R}^m \to \mathbb{R}^m$, where $\iota$ is that inclusion; then $g$ is continuous and injective, with image exactly $\mathbb{R}^n \times \{0\}$. By the invariance of domain, the image of an injective continuous map $\mathbb{R}^m \to \mathbb{R}^m$ is open; but $\mathbb{R}^n\times\{0\}$ has empty interior in $\mathbb{R}^m$ when $n < m$, since every open ball in $\mathbb{R}^m$ contains a point with a nonzero last coordinate. The contradiction gives $n = m$. $\square$

## Summary

The degree of a self-map of $S^n$ is the integer by which it multiplies the fundamental class in $H_n(S^n;\mathbb{Z}) \cong \mathbb{Z}$; it is well defined, homotopy invariant, multiplicative, unchanged by suspension, equal to $\det T$ for the map induced by an orthogonal transformation, and equal to $(-1)^{n+1}$ for the antipodal map; in dimension one it is the winding number, and it classifies self-maps up to homotopy. It can be computed as a sum of local degrees over the fibre of a point, and for a smooth map at a regular value as a sum of signs of Jacobian determinants; the integral formula expressing it as a ratio of top-form integrals is quoted from *Differential Forms and Stokes' Theorem*, the underlying measure theory being Part III's. The definition extends to maps of closed connected oriented manifolds and, modulo $2$, to nonorientable ones, and a map of nonzero degree is surjective.

Brouwer's fixed point theorem, that every continuous self-map of $D^{n+1}$ has a fixed point, is equivalent to the nonexistence of a retraction of the disc onto its boundary, and hence to the nonvanishing of $H_n(S^n)$; the general form for compact convex sets follows. The Lefschetz number of a self-map of a finite CW complex, defined as the alternating sum of the traces on rational homology, is the algebraic intersection number of the graph with the diagonal, and its nonvanishing is a sufficient condition for a fixed point; for the disc it equals one, recovering Brouwer, for $S^n$ it equals $1 + (-1)^n\deg f$, and for the torus it equals $\det(I - A)$. The applications are the hairy ball theorem, from the Poincaré–Hopf index theorem and the Euler characteristic of the sphere; the Borsuk–Ulam theorem, from the oddness of an induced map and the degree of odd self-maps of the sphere; and the Jordan–Brouwer separation theorem and invariance of domain, from Alexander duality.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^n$, $D^{n+1}$ | Unit sphere in $\mathbb{R}^{n+1}$; closed unit disc |
| $\deg f$ | Degree: $f_*[S^n] = (\deg f)[S^n]$ on $H_n(S^n;\mathbb{Z})$ |
| $[S^n]$, $[M]$ | Fundamental class; orientation class of *Poincaré Duality* |
| $\deg_x f$ | Local degree at an isolated preimage point |
| $\deg_2 f$ | Degree modulo $2$, for nonorientable manifolds |
| $A(x) = -x$ | Antipodal map; $\deg A = (-1)^{n+1}$ |
| $\Sigma f$ | Suspension of $f$; $\deg(\Sigma f) = \deg f$ |
| $r : D^{n+1}\to S^n$ | Retraction; nonexistence is equivalent to Brouwer's theorem |
| $L(f) = \sum(-1)^i\operatorname{tr}(f_*|H_i(X;\mathbb{Q}))$ | Lefschetz number of a self-map of a finite CW complex |
| $\chi(X) = L(\mathrm{id})$ | Euler characteristic; $= \sum(-1)^i\dim_{\mathbb{Q}}H_i(X;\mathbb{Q})$ |
| $\Gamma_f$, $\Delta$ | Graph of $f$, diagonal in $M\times M$; $L(f) = \Gamma_f\cdot\Delta$ |
| $L(f) = 1 + (-1)^n\deg f$ | Lefschetz number of a self-map of $S^n$ |
| $L(f) = \det(I - A)$ | Lefschetz number of a self-map of $T^n$, $A = f_*|H_1$ |
| $X$, $\mathrm{ind}_x X$ | Vector field and index of a zero; $\sum\mathrm{ind}_x X = \chi(M)$ |
| $g$ odd, $g(-x) = -g(x)$ | Odd map; odd degree (Borsuk) |
| $\tilde H_i(S^n\setminus K)$ | Alexander duality: $\cong \tilde H^{n-i-1}(K)$ |



## Further Reading

- L. E. J. Brouwer, *Über Abbildung von Mannigfaltigkeiten* (Mathematische Annalen 71, 1911), for the original fixed point theorem and the degree.
- Heinz Hopf, *Abbildungsklassen $n$-dimensionaler Mannigfaltigkeiten* (Mathematische Annalen 96, 1927), for the classification of self-maps of spheres by degree.
- Solomon Lefschetz, *Intersections and Transformations of Complexes and Manifolds* (Transactions of the American Mathematical Society 28, 1926), for the fixed point theorem and the trace formula.
- Karol Borsuk, *Drei Sätze über die $n$-dimensionale euklidische Sphäre* (Fundamenta Mathematicae 20, 1933), for the theorem on odd maps and the antipodal theorem.
- Eberhard Zeidler, *Nonlinear Functional Analysis and Its Applications I: Fixed-Point Theorems* (Springer, 1986), for the analytic fixed point theory and the Leray–Schauder degree of Part III.
- Victor Guillemin and Alan Pollack, *Differential Topology* (Prentice-Hall, 1974), for the degree, the regular value formula and the Jordan–Brouwer theorem.
- John W. Milnor, *Topology from the Differentiable Viewpoint* (University Press of Virginia, 1965), for the smooth proof of Brouwer's theorem and the hairy ball theorem.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the Lefschetz fixed point theorem, Alexander duality and the degree.
