
# __Fixed Point Theory and Degree Theory__

## Introduction

A fixed point of a map $T$ of a set into itself is a solution of the equation $x=Tx$, and the fixed-point theorems are the existence statements for that equation. In finite dimensions the existence is governed by the topology of the domain through the **Brouwer degree**, and the Brouwer fixed point theorem is its corollary; in infinite dimensions the same construction is not available directly, because a closed bounded set is no longer compact and the degree of a map of the unit ball into itself has no finite-dimensional definition. What replaces compactness of the space is compactness of the map: a continuous map whose image of a bounded set is relatively compact behaves in every essential respect like a map of a finite-dimensional set, and the degree of the finite-dimensional theory can be transported to the operators $I-T$, first by finite-dimensional approximation and then by the homotopy properties of the resulting integer. The resulting **Leray–Schauder degree** exists for the maps $I-T$ with $T$ compact, and from it follow the analytic fixed point theorems: the **Schauder theorem**, that a continuous compact self-map of a closed bounded convex set has a fixed point; the **Leray–Schauder continuation theorem**, that a compact homotopy connecting $T$ to $0$ whose fixed points stay away from the boundary has a fixed point; **Schaefer's theorem**, that a compact map whose fixed-point set is bounded along the homotopy has a fixed point; and **Krasnoselskii's theorem**, that a compact perturbation of a contraction has a fixed point.

The topological degree in its finite-dimensional form — the degree of a map of spheres and of closed oriented manifolds, the Brouwer fixed point theorem, the Lefschetz fixed point theorem, the Jordan–Brouwer separation theorem — is the subject of the companion article *Degree Theory and the Brouwer Fixed Point Theorem*, which is written; the present article is the **analytic** fixed-point theory, in which compactness of the map replaces compactness of the domain, and it takes the finite-dimensional degree as an input, citing it rather than re-deriving it. The classification in the two articles is deliberate and is recorded on both sides: the topological and homological degree there, the analytic fixed point theorems and the degree of a compact perturbation of the identity here.

The article begins with the contraction principle, the metric fixed-point theorem that needs completeness and not compactness, and with its extensions. It then develops the compact-mapping theory: the Schauder projection, the Schauder fixed point theorem and its finite-dimensional input from *Degree Theory and the Brouwer Fixed Point Theorem*, and the Leray–Schauder degree with its properties. It proves the continuation and Schaefer theorems, states the theorems of Krasnoselskii, Rothe and Altman, introduces the measures of noncompactness and the fixed-point theorems for condensing maps, and closes with the fixed point index and its applications.

The calculus on normed spaces, the Fréchet derivative and the inverse function theorem are those of *Differential Calculus on Normed Spaces* and *Nonlinear Functional Analysis*; convexity, the subdifferential and the monotone operators are those of *Nonlinear Functional Analysis*. The finite-dimensional degree, the Brouwer fixed point theorem and the Lefschetz fixed point theorem are those of *Degree Theory and the Brouwer Fixed Point Theorem*, and the topological degrees of the classical one-dimensional case are the winding numbers of that article. The compact operators and the Fredholm theory are those of *Fredholm Theory*; the Ascoli–Arzelà theorem and the compactness in the function spaces are those of *Metric, Uniform and Complete Spaces*, *Topological Spaces* and *Topology on Linear Spaces*; the locally convex version of the fixed point theory (Tychonoff's theorem for locally convex spaces) uses *Topological Modules and Vector Spaces*. The applications to ordinary equations, to elliptic boundary problems and to the Cauchy problem belong to *Differential Equations*.

No physics is invoked.

## The Contraction Principle

### Statement and Sharpness

**Theorem (Banach contraction principle).** Let $(M,d)$ be a complete metric space and $T:M\to M$ a contraction with constant $\kappa<1$, that is, $d(Tx,Ty)\le\kappa\,d(x,y)$ for all $x,y$. Then $T$ has exactly one fixed point $x^*$, and for every $x \in M$,

$$
d(T^nx,x^*)\le\frac{\kappa^n}{1-\kappa}\,d(x,Tx),
$$

so the iterates converge to $x^*$ at the rate of a geometric series.

*Proof.* Let $x_0=x$ and $x_n=T^nx$. Then $d(x_{n+1},x_n)\le\kappa^nd(x_1,x_0)$, so for $m>n$,

$$
d(x_m,x_n)\le\sum_{j=n}^{m-1}\kappa^jd(x_1,x_0)\le\frac{\kappa^n}{1-\kappa}d(x_1,x_0),
$$

and $(x_n)$ is Cauchy; its limit $x^*$ satisfies $Tx^*=x^*$ by continuity of $T$. Uniqueness: if $Tx^*=x^*$ and $Ty^*=y^*$ then $d(x^*,y^*)=d(Tx^*,Ty^*)\le\kappa d(x^*,y^*)$, so $d(x^*,y^*)=0$. $\square$

**Example (completeness is needed).** On $M=(0,1]$ with the usual metric, $Tx=x/2$ is a contraction with no fixed point in $M$; the fixed point $0$ lies outside. On $M=\mathbb{R}$, the translation $Tx=x+1$ has no fixed point and is an isometry, not a contraction. On the closed unit ball of a Banach space, the map $Tx=(1-\|x\|)x$ is continuous and has fixed points, but it is not a contraction.

### Local and Weaker Forms

**Theorem (local contraction).** Let $T$ map the closed ball $\overline B(x_0,r)$ into itself and satisfy $d(Tx,Ty)\le\kappa d(x,y)$ there with $\kappa<1$ and $d(Tx_0,x_0)\le(1-\kappa)r$. Then $T$ has a unique fixed point in $\overline B(x_0,r)$.

**Theorem (Edelstein).** Let $(M,d)$ be compact and $T:M\to M$ satisfy $d(Tx,Ty)<d(x,y)$ for all $x \neq y$. Then $T$ has a unique fixed point.

*Proof.* The function $x\mapsto d(x,Tx)$ is continuous on the compact set $M$ and attains its minimum at some $x^*$; if $Tx^*\neq x^*$ then $d(T^2x^*,Tx^*)<d(Tx^*,x^*)$ contradicts minimality, so $d(x^*,Tx^*)=0$; uniqueness is immediate from the strict inequality. $\square$

**Theorem (Rakotch).** Let $(M,d)$ be complete and let $T:M\to M$ satisfy $d(Tx,Ty)\le\alpha(d(x,y))\,d(x,y)$ where $\alpha:[0,\infty)\to[0,1)$ is nonincreasing. Then $T$ has a unique fixed point.

These forms are the standard weakening of the contraction hypothesis; the strict contraction is what makes the iteration converge uniformly, and the compactness in Edelstein's theorem replaces the uniformity.

**Example (applications).** The contraction principle gives the existence and uniqueness for the initial-value problem $y'=f(x,y)$, $y(x_0)=y_0$ with $f$ Lipschitz in $y$, by solving the integral equation $y(x)=y_0+\int_{x_0}^xf(t,y(t))dt$ on a small interval; it gives the inverse function theorem of *Nonlinear Functional Analysis* and the convergence of Newton's method; and it gives the convergence of the Neumann series for the resolvent of an operator with small norm and, more generally, of the successive approximations for a Fredholm integral equation of the second kind, as in *Fredholm Theory*. The ordinary differential equation and the Picard–Lindelöf theorem belong to *Differential Equations*.

## Compact Maps and Schauder's Theorem

### The Schauder Projection

**Definition.** Let $C$ be a subset of a Banach space $X$. A continuous map $T:C\to X$ is **compact** if the image of every bounded subset of $C$ is relatively compact; equivalently, if $T$ is continuous and maps bounded sets into sets whose closure is compact. The map is **finite-dimensional** if its image lies in a finite-dimensional subspace.

**Lemma (Schauder projection).** Let $K \subseteq X$ be compact and $\epsilon>0$. Then there is a finite-dimensional subspace $X_\epsilon \subseteq X$ and a continuous map $P_\epsilon:K\to X_\epsilon$ with $\|P_\epsilon x-x\|\le\epsilon$ for all $x \in K$; the map can be taken to have its image in the convex hull of a finite $\epsilon$-net for $K$.

*Proof.* Choose $x_1,\dots,x_m \in K$ with the balls $B(x_i,\epsilon)$ covering $K$, let $X_\epsilon=\operatorname{span}\{x_1,\dots,x_m\}$, and set

$$
P_\epsilon x=\frac{\sum_{i=1}^m\max\{0,\ \epsilon-\|x-x_i\|\}\,x_i}{\sum_{i=1}^m\max\{0,\ \epsilon-\|x-x_i\|\}} ,
$$

the denominator being positive on $K$; the map is continuous, its image lies in the convex hull of the $x_i$, and for $x$ in $K$ the estimate $\|P_\epsilon x-x\|\le\epsilon$ follows because $P_\epsilon x$ is a convex combination of the centres of the balls containing $x$. $\square$

### The Schauder Fixed Point Theorem

**Theorem (Schauder).** Let $C$ be a nonempty closed bounded convex subset of a Banach space $X$ and let $T:C\to C$ be continuous and compact. Then $T$ has a fixed point.

*Proof.* For $n \in \mathbb{N}$ let $P_n:T(C)\to X_n$ be the Schauder projection of the compact set $\overline{T(C)}$ with constant $1/n$, and put $T_n=P_n\circ T$. Then $T_n$ maps $C$ into the finite-dimensional convex set $C_n=X_n\cap C$, and the Brouwer fixed point theorem of *Degree Theory and the Brouwer Fixed Point Theorem* gives $x_n \in C_n$ with $T_nx_n=x_n$. Since $T(C)$ is relatively compact and the projection moves points by at most $1/n$,

$$
\|x_n-Tx_n\|=\|T_nx_n-Tx_n\|\le1/n ,
$$

so $(Tx_n)$ has a convergent subsequence, say $Tx_{n_k}\to x^* \in\overline{T(C)}\subseteq C$; then $x_{n_k}=T_{n_k}x_{n_k}\to x^*$ as well, and continuity of $T$ gives $Tx^*=\lim Tx_{n_k}=x^*$. $\square$

The proof is the model of the passage from the finite-dimensional to the infinite-dimensional theory: the finite-dimensional theorem is applied to the projections, and the compactness of $T$ upgrades the approximate fixed points to an exact one.

**Corollary (unbounded convex sets).** If $C$ is a closed convex set and $T:C\to C$ is continuous and compact with $T(C)$ bounded, then $T$ has a fixed point: choose $r$ with $T(C)\subseteq B(0,r)$ and apply Schauder's theorem to the closed bounded convex set $C\cap\overline{B(0,r)}$, which is invariant under $T$. If the fixed point is sought in a specified bounded open set rather than anywhere in $C$, the degree theory of the next section is used instead.

**Corollary (compact convex sets).** Let $C$ be a compact convex subset of $X$ and $T:C\to C$ continuous. Then $T$ has a fixed point, since $T$ is compact and $C$ is closed, bounded and convex; in particular every nonexpansive self-map of a compact convex set has a fixed point. The generalisation to a weakly compact convex set and a nonexpansive map, in the form of the Ryll-Nardzewski theorem, needs the weak topology and the existence of an invariant mean, and its statement and proof belong to the topological fixed point theory .

## The Leray–Schauder Degree

### Construction and Properties

**Definition.** Let $X$ be a Banach space, $\Omega \subseteq X$ a bounded open set, and $T:\overline\Omega\to X$ continuous and compact with $p \notin(I-T)(\partial\Omega)$. The **Leray–Schauder degree** $\deg(I-T,\Omega,p)$ is the integer defined by finite-dimensional approximation: choose a finite-dimensional subspace $X_\epsilon$ containing $p$ and a Schauder projection $P_\epsilon$ of the compact set $\overline{T(\overline\Omega)}$ with constant $\epsilon$; on a finite-dimensional subspace containing $X_\epsilon$ and invariant for the projected map, the Brouwer degree of $I-P_\epsilon T$ at $p$ relative to $\Omega\cap X_\epsilon$ is defined, and the value is independent of the approximation once $\epsilon$ is small enough.

**Theorem (properties of the degree).** The integer $\deg(I-T,\Omega,p)$ is well defined and has the following properties:

(i) **Normalisation.** $\deg(I,\Omega,p)=1$ if $p \in\Omega$, and $\deg(I,\Omega,p)=0$ if $p \notin\overline\Omega$; in finite dimensions the integer reduces to the Brouwer degree of *Degree Theory and the Brouwer Fixed Point Theorem*.

(ii) **Solvability.** If $\deg(I-T,\Omega,p)\neq0$ then $p \in(I-T)(\Omega)$, so the equation $x-Tx=p$ has a solution in $\Omega$.

(iii) **Additivity.** If $\Omega_1,\Omega_2$ are disjoint open subsets of $\Omega$ with $p \notin(I-T)(\overline\Omega\setminus(\Omega_1\cup\Omega_2))$, then $\deg(I-T,\Omega,p)=\deg(I-T,\Omega_1,p)+\deg(I-T,\Omega_2,p)$.

(iv) **Homotopy invariance.** If $H:[0,1]\times\overline\Omega\to X$ is continuous, $H(t,\cdot)$ compact for every $t$, and $p \notin(I-H(t,\cdot))(\partial\Omega)$ for every $t$, then $\deg(I-H(t,\cdot),\Omega,p)$ is independent of $t$.

(v) **Excision.** If $\Omega_0 \subseteq\Omega$ is open and $p \notin(I-T)(\overline\Omega\setminus\Omega_0)$, then $\deg(I-T,\Omega,p)=\deg(I-T,\Omega_0,p)$.

*Proof (sketch).* For the finite-dimensional case the statements are those of the Brouwer degree, cited from *Degree Theory and the Brouwer Fixed Point Theorem*; for the general case one observes that the approximation used in the definition has a uniform bound on the finite-dimensional degrees when the homotopy stays away from $p$ on the boundary, by the homotopy property in finite dimensions, and the integer obtained is therefore independent of the choice. The properties follow by passing to the limit in the corresponding finite-dimensional identities. $\square$

**Corollary.** $\deg(I-T,\Omega,p)$ depends only on the restriction of $T$ to $\partial\Omega$ and on the connected component of $X\setminus(I-T)(\partial\Omega)$ containing $p$; in particular, if $T$ is not defined on all of $\overline\Omega$ but only on a neighbourhood of $\overline\Omega$, the degree is unchanged.

### The Continuation Theorem and Schauder's Consequence

**Theorem (Leray–Schauder continuation).** Let $H:[0,1]\times\overline\Omega\to X$ be a compact homotopy with $H(0,\cdot)=0$ and with $x \neq H(t,x)$ for all $x \in\partial\Omega$ and $t \in[0,1]$. Then $H(1,\cdot)$ has a fixed point in $\Omega$.

*Proof.* By homotopy invariance and normalisation, $\deg(I-H(1,\cdot),\Omega,0)=\deg(I,\Omega,0)=1$, and the solvability property gives a fixed point. $\square$

The theorem is the standard tool for existence in nonlinear problems: one embeds the given equation in a one-parameter family joining it to the trivial equation, proves the a priori bound that keeps the fixed points away from the boundary, and concludes.

**Theorem (Schaefer).** Let $T:X\to X$ be continuous and compact, and suppose the set

$$
S=\{x \in X:x=\lambda\,Tx \text{ for some } \lambda \in[0,1]\}
$$

is bounded. Then $T$ has a fixed point.

*Proof.* Choose $r>\sup_{x \in S}\|x\|$ and $\Omega=B(0,r)$; the homotopy $H(t,x)=t\,Tx$ has no fixed point on $\partial\Omega$ for $t \in[0,1]$, because a fixed point with $\|x\|=r$ would lie in $S$; the continuation theorem applies. $\square$

**Corollary (Schauder for unbounded sets).** If $C$ is a closed convex set and $T:C\to C$ is continuous and compact with $T(C)$ bounded, then $T$ has a fixed point: take $r$ with $T(C)\subseteq B(0,r)$ and apply Schauder's theorem to the closed bounded convex set $C\cap\overline{B(0,r)}$, which is invariant under $T$.

## Further Fixed Point Theorems

### Krasnoselskii, Rothe and Altman

**Theorem (Krasnoselskii).** Let $C$ be a nonempty closed bounded convex subset of a Banach space $X$, let $S:C\to X$ be a contraction with constant $\kappa<1$, and let $K:C\to X$ be continuous and compact. If $Sx+Ky \in C$ for all $x,y \in C$, then $S+K$ has a fixed point in $C$.

*Proof.* Extend $S$ to a map of $X$ with the same constant $\kappa$, which is possible because $C$ is a convex subset of a Banach space; then the series $\sum_{j\ge0}S^j$ converges in the operator norm, so $I-S$ is invertible with $(I-S)^{-1}=\sum_{j\ge0}S^j$ and $\|(I-S)^{-1}\|\le\frac1{1-\kappa}$. Put $T=(I-S)^{-1}K$; then $T$ is continuous and compact, as the composition of a continuous map with a compact one. To see that $T(C)\subseteq C$, fix $y \in C$ and let $z$ be the fixed point of the contraction $x\mapsto Sx+Ky$, which exists by the contraction principle; starting the iteration from any $x_0 \in C$, each iterate lies in $C$ by the hypothesis $Sx+Ky \in C$, so the limit $z$ lies in $C$ (which is closed). Hence $T(C)\subseteq C$, Schauder's theorem gives $z=Tz$, and $z=Tz$ means $(I-S)z=Kz$, that is, $z=Sz+Kz$. $\square$

**Theorem (Rothe).** Let $C$ be a nonempty closed bounded convex subset of $X$ with $0 \in C$, and let $T:C\to X$ be continuous and compact with $T(\partial C)\subseteq C$. Then $T$ has a fixed point in $C$.

**Theorem (Altman).** Let $C$ be a nonempty closed bounded convex subset of $X$ with $0 \in C$ and let $T:C\to X$ be continuous and compact. If $\|Tx-x\|^2\ge\|Tx\|^2-\|x\|^2$ for every $x \in\partial C$, then $T$ has a fixed point in $C$.

The three theorems are different boundary conditions under which the compact map cannot escape the convex set; they are proved from the Leray–Schauder degree by verifying that $\deg(I-T,C,0)\neq0$ on the boundary, and their proofs are the standard ones cited below.

### Measures of Noncompactness and Condensing Maps

**Definition.** The **Kuratowski measure of noncompactness** of a bounded set $A \subseteq X$ is

$$
\alpha(A)=\inf\{d>0:A \text{ is covered by finitely many sets of diameter at most } d\},
$$

and the **Hausdorff measure of noncompactness** is $\beta(A)=\inf\{r>0:A \text{ has a finite cover by balls of radius } r\}$. A continuous map $T:D\to X$ is **condensing** (or $\alpha$-condensing) if $\alpha(T(A))<\alpha(A)$ for every bounded $A \subseteq D$ with $\alpha(A)>0$.

**Theorem (Darbo–Sadovskii).** Let $C$ be nonempty, closed, bounded and convex and let $T:C\to C$ be continuous and condensing. Then $T$ has a fixed point.

*Proof (sketch).* One constructs a transfinite sequence of closed convex sets $C_\alpha$ by $C_{\alpha+1}=\overline{\mathrm{conv}}\,T(C_\alpha)$, starting from $C_0=C$, and shows that the ordinal sequence must stabilise at a set with $\alpha=0$, that is, at a compact convex set, on which Schauder's theorem applies. The construction is the standard transfinite one of the theory of condensing maps, cited below. $\square$

A compact map is condensing, so the theorem contains Schauder's; the value of the extension is that many integral operators and many perturbations of the identity are condensing without being compact, and the theory applies to them.

## The Fixed Point Index

**Definition.** For a bounded open set $\Omega \subseteq X$ and a continuous compact map $T:\overline\Omega\to X$ with no fixed point on $\partial\Omega$, the **fixed point index** is

$$
i(T,\Omega)=\deg(I-T,\Omega,0).
$$

**Theorem (properties of the index).** The index satisfies:

(i) **Normalisation.** $i(T,\Omega)=1$ for the constant map with value in $\Omega$, and $i(T,\Omega)$ is the Brouwer index when an isolated nondegenerate fixed point $x_0$ is concerned, in the sense of the computation below.

(ii) **Solvability.** $i(T,\Omega)\neq0$ implies that $T$ has a fixed point in $\Omega$.

(iii) **Additivity.** If $\Omega_1,\Omega_2$ are disjoint open subsets of $\Omega$ and $T$ has no fixed point in $\overline\Omega\setminus(\Omega_1\cup\Omega_2)$, then $i(T,\Omega)=i(T,\Omega_1)+i(T,\Omega_2)$.

(iv) **Homotopy invariance.** If $H:[0,1]\times\overline\Omega\to X$ is a compact homotopy with no fixed point of $H(t,\cdot)$ on $\partial\Omega$ for any $t$, then $i(H(t,\cdot),\Omega)$ is independent of $t$.

(v) **Excision.** The index depends only on the values of $T$ on a neighbourhood of the set of its fixed points in $\Omega$.

*Proof.* The statements are the degree properties of the previous section translated by the definition, since $i(T,\Omega)=\deg(I-T,\Omega,0)$ and a fixed point of $T$ is a zero of $I-T$. $\square$

**Example (the index of a nondegenerate fixed point).** If $T$ is $C^1$ near a fixed point $x_0$, if $I-T'(x_0)$ is invertible, and if $x_0$ is the only fixed point in a small ball $\Omega$, then

$$
i(T,\Omega)=\operatorname{sign}\det\bigl(I-T'(x_0)\bigr)
$$

in the finite-dimensional case, and $i(T,\Omega)=\pm1$ according to the parity of the number of negative real eigenvalues of $I-T'(x_0)$ in the general case; the index is thus a local invariant computed from the derivative, and the global index is the sum of the local indices by additivity. This is the analytic counterpart of the local-degree formula of *Degree Theory and the Brouwer Fixed Point Theorem*, and it is the beginning of the Lefschetz theory for compact maps, whose topological form belongs to that article.

**Corollary (index and multiplicity).** If the fixed points of $T$ in $\Omega$ are isolated and their indices are $i_1,\dots,i_m$, then $i(T,\Omega)=\sum_ji_j$; consequently an index different from zero gives at least one fixed point, and an index with absolute value exceeding one gives several, counted with multiplicity.

## Applications

**Example (an integral equation).** Let $k:[0,1]\times[0,1]\to\mathbb{R}$ be continuous and let $g:\mathbb{R}\to\mathbb{R}$ be continuous and bounded; the operator

$$
(Tu)(x)=\int_0^1k(x,y)\,g(u(y))\,dy
$$

is continuous and compact on $C[0,1]$ by the Ascoli–Arzelà theorem, and if $\|g\|_\infty\int|k|\,dy\le1$ then $T$ maps a ball into itself and Schauder's theorem gives a solution of $u=Tu$. The example is the standard existence theorem for a nonlinear integral equation, and the detailed regularity theory belongs andboth.

**Example (the Cauchy problem).** The local existence theorem of Peano for $y'=f(x,y)$ follows by applying Schauder's theorem to the compact operator $u\mapsto y_0+\int_{x_0}^x f(t,u(t))dt$ on a ball in $C[x_0-\delta,x_0+\delta]$; the a priori bound that makes the ball invariant is the boundedness of $f$ on the relevant strip. The theorem, its sharpness and the uniqueness theory belong to *Differential Equations*.

**Example (a semilinear elliptic problem).** For the boundary problem $-\Delta u=g(u)$ on a bounded domain with $u=0$ on the boundary, the inverse of $-\Delta$ with Dirichlet conditions is compact on the appropriate space, and the problem is equivalent to the fixed point equation $u=(-\Delta)^{-1}g(u)$; the growth and sign conditions on $g$ that make the Schauder or Schaefer hypotheses hold are the hypotheses of the existence theory, which belongs .

**Example (a monotone perturbation).** If $A$ is maximal monotone and $K$ is compact, the equation $Au+Ku\ni0$ is solved by combining the surjectivity theorem for monotone operators of *Nonlinear Functional Analysis* with the Leray–Schauder degree; the abstract scheme is the content of the present article, and the concrete applications are to variational inequalities and to evolution equations, treated and *Differential Equations*.

## Summary

The analytic fixed point theory solves $x=Tx$ by two devices: completeness together with contractivity, and compactness of the map. The **contraction principle** states that a contraction of a complete metric space has a unique fixed point, with the iterates converging geometrically at the rate $d(T^nx,x^*)\le\frac{\kappa^n}{1-\kappa}d(x,Tx)$; completeness is essential, and the local, Edelstein and Rakotch forms weaken the hypotheses without abandoning the iteration. The **Schauder projection** replaces a compact set by a finite-dimensional approximant at distance $\epsilon$, and the **Schauder theorem** applies the Brouwer fixed point theorem to the projected maps and passes to the limit, giving a fixed point for every continuous compact self-map of a nonempty closed bounded convex set. From it follow the fixed point theorem for continuous maps of compact convex sets and, with an a priori bound, for maps of unbounded convex sets with bounded image.

The **Leray–Schauder degree** $\deg(I-T,\Omega,p)$ is the integer defined for a bounded open $\Omega$ and a compact $T$ with $p$ outside $(I-T)(\partial\Omega)$ by finite-dimensional approximation, and it satisfies normalisation, solvability, additivity, homotopy invariance and excision; the solution of $x-Tx=p$ in $\Omega$ is guaranteed by a nonzero degree. The **continuation theorem** deduces a fixed point of $H(1,\cdot)$ from the absence of fixed points of the homotopy on the boundary and from $H(0,\cdot)=0$, and **Schaefer's theorem** gives a fixed point of a compact map whose homotopy fixed-point set is bounded. **Krasnoselskii's theorem** solves $x=Sx+Kx$ for a contraction $S$ and a compact $K$ on a closed bounded convex set by applying Schauder to $(I-S)^{-1}K$, and the boundary conditions of **Rothe** and **Altman** are further criteria for the same conclusion. The **measures of noncompactness** and the **Darbo–Sadovskii theorem** extend the theory to condensing maps, which need not be compact. The **fixed point index** $i(T,\Omega)=\deg(I-T,\Omega,0)$ satisfies the same properties, and the index of an isolated nondegenerate fixed point is computed from $I-T'(x_0)$; sums of local indices give the global index and hence multiplicity statements. The topological degree in finite dimensions, the Brouwer fixed point theorem and the Lefschetz fixed point theorem are the subject of *Degree Theory and the Brouwer Fixed Point Theorem*; the present article is the analytic theory that uses them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$ | Banach space |
| $C$ | closed convex subset |
| $\Omega$ | bounded open subset |
| $T$, $S$, $K$, $H$ | maps and homotopies |
| $\kappa$ | contraction constant |
| $\overline B(x_0,r)$ | closed ball |
| $P_\epsilon$ | Schauder projection |
| $\deg(I-T,\Omega,p)$ | Leray–Schauder degree |
| $i(T,\Omega)$ | fixed point index |
| $\alpha(A)$, $\beta(A)$ | Kuratowski and Hausdorff measures of noncompactness |
| $\overline{\mathrm{conv}}$ | closed convex hull |
| $(-\Delta)^{-1}$ | inverse of the Dirichlet Laplacian |
| $C[0,1]$ | space of continuous functions |





## Further Reading

- Stefan Banach, "Sur les opérations dans les ensembles abstraits et leur application aux équations intégrales", *Fundamenta Mathematicae* 3 (1922), 133–181, for the contraction principle and its applications.
- Juliusz Schauder, "Der Fixpunktsatz in Funktionalräumen", *Studia Mathematica* 2 (1930), 171–180, for the fixed point theorem for compact maps.
- Jean Leray and Juliusz Schauder, "Topologie et équations fonctionnelles", *Annales Scientifiques de l'École Normale Supérieure* 51 (1934), 45–78, for the degree of a compact perturbation of the identity and the continuation theorem.
- Mark A. Krasnoselskii, *Topological Methods in the Theory of Nonlinear Integral Equations* (Pergamon, 1964), for the fixed point theorems of Krasnoselskii, Rothe and Altman and their applications.
- Felix E. Browder, "On a generalization of the Schauder fixed point theorem", *Duke Mathematical Journal* 26 (1959), 291–303, for the theory of condensing maps and the fixed point index.
- Klaus Deimling, *Nonlinear Functional Analysis* (Springer, 1985), for the Leray–Schauder degree, the fixed point index and the boundary conditions.
- Roger D. Nussbaum, "The fixed point index and fixed point theorems", in *Topological Methods in Nonlinear Functional Analysis* (American Mathematical Society, 1983), for the fixed point index and its computation.
- Andrzej Granas and James Dugundji, *Fixed Point Theory* (Springer, 2003), for the systematic treatment of the finite-dimensional degree, the infinite-dimensional extension and the applications to differential equations.
