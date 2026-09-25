
# __List of Norms and Seminorms__

## Introduction

This article lists the norms, seminorms and families of seminorms that the corpus uses, together with the completeness each one confers on the space it defines. A norm is a real-valued function on a vector space that is positive definite, homogeneous and satisfies the triangle inequality; a seminorm drops positive definiteness; a family of seminorms defines a locally convex topology without necessarily defining a norm. Each row names one such object, records the space or the class of spaces it acts on and the completeness it produces there, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The objects are grouped by the layer that introduces them, and the functions that look like norms and are not — seminorms that vanish on nonzero vectors, quasi-norms that fail the triangle inequality, norms that are not submultiplicative — are recorded beside them as non-examples.

## Norms on Linear Spaces

| Object | The space it defines, and the completeness it gives | Introduced in |
|---|---|---|
| a norm $\lVert\cdot\rVert$ | a normed space; complete exactly when the space is Banach | *Normed and Banach Spaces* |
| the operator norm $\lVert T\rVert = \sup_{\lVert x\rVert\leq1}\lVert Tx\rVert$ | $B(X,Y)$; complete when $Y$ is complete | *Normed and Banach Spaces* |
| the inner-product norm $\lVert x\rVert = \langle x,x\rangle^{1/2}$ | an inner product space; complete exactly when it is a Hilbert space | *Banach and Hilbert Spaces* |
| the dual norm on $X^*$ | the dual space $X^* = B(X,\mathbb K)$; always complete | *Normed and Banach Spaces* |
| the quotient norm | $X/M$ for a closed subspace $M$; complete when $X$ is | *Normed and Banach Spaces* |
| equivalence of norms | finitely many norms on a finite-dimensional space are equivalent, so all give the same completeness | *Normed and Banach Spaces* |

## Norms on Sequence and Function Spaces

| Object | The space it defines, and the completeness it gives | Introduced in |
|---|---|---|
| the $\ell^p$ norm $\lVert(x_n)\rVert_p$ | $\ell^p$; complete for $1 \leq p \leq \infty$ | *Normed and Banach Spaces* |
| the supremum norm $\lVert f\rVert_\infty = \sup_x \lvert f(x)\rvert$ | $C(K)$, $C_b(X)$, $B(X,Y)$; complete when the target is complete | *Normed and Banach Spaces*; *Metric, Uniform and Complete Spaces* |
| the essential supremum norm | $L^\infty(\mu)$; complete | *Measure Theory and Integration* |
| the $L^p$ norm $\lVert f\rVert_p$ | $L^p(\mu)$; complete for $1 \leq p \leq \infty$ | *Measure Theory and Integration* |
| the Sobolev norm $\lVert f\rVert_{W^{k,p}}$ | $W^{k,p}(\Omega)$; complete | *Sobolev Spaces and Weak Solutions* |
| the homogeneous Sobolev norm, and $p^* = np/(n-p)$ | the Sobolev conjugate exponent, with the embedding $W^{1,p}\hookrightarrow L^{p^*}$ | *Sobolev Spaces and Weak Solutions* |
| the Bessel-potential norm $\lVert(1-\Delta)^{s/2}f\rVert_p$ | $H^s_p$; complete | *Interpolation Theory* |
| the Hölder norm | $C^{k,\alpha}$; complete | *Besov and Triebel–Lizorkin Spaces* |
| the Besov norm (an $\ell^q(L^p)$ norm of the Littlewood–Paley blocks) | $B^s_{p,q}$; a quasi-norm for $p<1$ or $q<1$, complete | *Besov and Triebel–Lizorkin Spaces* |
| the Triebel–Lizorkin norm (an $L^p(\ell^q)$ norm of the blocks) | $F^s_{p,q}$; complete | *Besov and Triebel–Lizorkin Spaces* |
| the Lorentz norm | $L^{p,q}$; complete, and the interpolation norm between two $L^p$ norms | *Interpolation Theory* |
| the Hardy-space norm $\lVert f\rVert_{H^p}$ | $H^p(\mathbb D)$ for $1 \leq p \leq \infty$; complete for $1 \leq p < \infty$, and $H^\infty$ is the bounded holomorphic functions | *Complex Harmonic Analysis* |
| the Paley–Wiener norm inherited from $L^2$ | $PW_B$; a closed subspace of $L^2$, hence complete | *Complex Harmonic Analysis* |
| the total-variation norm $\lvert\nu\rvert(X)$ | the space of signed and complex measures; complete | *Measure Theory and Integration* |

## Norms on Algebras and in Duality

| Object | The space it defines, and the completeness it gives | Introduced in |
|---|---|---|
| the submultiplicative norm, $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$ | a normed algebra; complete exactly when it is a Banach algebra | *Topological Algebras and Banach Algebras* |
| the Neumann-series bound $(1-x)^{-1} = \sum_n x^n$ for $\lVert x\rVert<1$ | the openness of the unit group in a normed algebra | *Topological Algebras and Banach Algebras* |
| the spectral radius $r(a) = \lim_n \lVert a^n\rVert^{1/n}$ | a quantity bounded above by the norm, $r(a) \leq \lVert a\rVert$, but not a norm itself | *Topological Algebras and Banach Algebras* |
| the Hilbert–Schmidt norm | $L^2(H)$; complete, an inner-product norm | *Operator Algebras* |
| the trace-class norm $\lVert T\rVert_1 = \operatorname{Tr}\lvert T\rvert$ | $L^1(H)$; complete | *Operator Algebras* |
| the strong and weak operator seminorms | the initial topologies of the operator families; not norms | *Operator Algebras* |
| the polar and the Minkowski gauge $p_A$ | a seminorm when $A$ is convex, balanced and absorbing; gives local convexity | *Locally Convex Spaces* |
| the seminorm of a topological vector space | a locally convex topology, complete exactly when the space is Fréchet or otherwise as stated | *Locally Convex Spaces* |

## Seminorms and Families of Seminorms

| Object | The topology or property it defines | Introduced in |
|---|---|---|
| a seminorm $p$ | a convex, balanced, absorbing unit ball $B_p = \{x : p(x)\leq1\}$; the topology of a locally convex space | *Locally Convex Spaces* |
| a generating family $\mathcal P$ of seminorms | the locally convex topology it generates; complete exactly when the resulting space is complete | *Locally Convex Spaces* |
| a basic convex neighbourhood $U_{p_1,\dots,p_n;\varepsilon}$ | the neighbourhood filter of $0$ | *Locally Convex Spaces* |
| an increasing sequence $(p_n)$ of seminorms | the Fréchet topology it generates | *Fréchet Spaces* |
| the $F$-norm $\lvert x\rvert = \sum_n 2^{-n}\min(1,p_n(x))$ | the invariant metric $d(x,y) = \lvert x-y\rvert$; an $F$-space when complete | *Fréchet Spaces* |
| the Schwartz seminorms $p_{\alpha,\beta}(f) = \sup_x \lvert x^\alpha\partial^\beta f\rvert$ | the Fréchet topology of $\mathcal S(\mathbb R^n)$; complete | *Fréchet Spaces*; *Fourier Analysis on Euclidean Spaces* |
| the seminorms of the derivatives on compacta | the Fréchet topology of $C^\infty(U)$ and of $\mathcal O(\Omega)$; complete | *Fréchet Spaces* |
| the seminorms $\sup_K \lvert\partial^\alpha f\rvert$ on $\mathcal D_K$ | the inductive-limit topology of $\mathcal D(\Omega)$; complete and not normable | *Distributions and Fundamental Solutions* |
| the $p$-adic absolute value $\lvert\cdot\rvert_p$ | an absolute value satisfying the strong triangle inequality; gives a non-Archimedean norm | *Topological Modules and Vector Spaces*; *p-adic Integration* |
| a valuation $v = v_p$ | a non-Archimedean valuation, $\lvert x\rvert_p = p^{-v(x)}$ | *Topological Modules and Vector Spaces* |

## Functions That Are Not Norms

| Object | The property that fails | Introduced in |
|---|---|---|
| $\lvert f(0)\rvert$ on the continuous functions | vanishes on the nonzero functions that are $0$ at $0$: a seminorm and not a norm | *Locally Convex Spaces* |
| $L^p(\mu)$ with $0 < p < 1$ | the triangle inequality fails; the function is a quasi-norm and not a norm, and the topology is not locally convex | *Locally Convex Spaces* |
| the constant function $0$ | vanishes on every vector: the degenerate seminorm | *Locally Convex Spaces* |
| the sup norm on $C^k(U)$ | does not control the derivatives, so it does not make $C^k$ complete: a norm, but not the one the class carries | *Differential Calculus on Normed Spaces* |
| the spectral radius $r(a)$ | subadditive and submultiplicative, but not positive definite: a quasinilpotent element satisfies $r(a) = 0$ with $a \neq 0$ | *Topological Algebras and Banach Algebras* |

## Summary

This list gathers the norms of the corpus — the operator, inner-product, supremum, $L^p$, Sobolev, Hölder, Besov, Triebel–Lizorkin and Lorentz norms, with the completeness each confers — and the seminorms, either single or in generating families, that define the locally convex, Fréchet and inductive-limit topologies. The final table records the functions that are named or used as norms and fail to be one.

## Summary of Notation

The objects are named rather than denoted; the symbols used in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $\lVert\cdot\rVert$ | a norm; $\lVert T\rVert$ the operator norm |
| $p$ | a seminorm, and $B_p$ its unit ball |
| $\mathcal P$ | a generating family of seminorms |
| $\lvert\cdot\rvert_p$, $v_p$ | the $p$-adic absolute value and valuation |
| $F$-norm, Fréchet | the invariant metric norm and the complete metrisable locally convex case |
| quasi-norm | a function failing the triangle inequality, as in $L^p$ with $p<1$ |

## Further Reading

- Albrecht Pietsch, *History of Banach Spaces and Linear Operators* (Birkhäuser, 2007), for the classical norms and their completeness properties.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for norms, seminorms and the locally convex topologies they generate.
- Hans Triebel, *Theory of Function Spaces* (Birkhäuser, 1983), for the norms and quasi-norms of the Sobolev, Besov and Triebel–Lizorkin scales.
