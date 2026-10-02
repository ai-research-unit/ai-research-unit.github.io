
# __Bounded Operators and the Operator Norm__

## Introduction

On a normed space the bounded operators form not only a normed space but a **normed algebra**, because composition is a multiplication compatible with the operator norm: it is submultiplicative, $\lVert ST\rVert \leq \lVert S\rVert\lVert T\rVert$. When the underlying space is complete the operator algebra is complete, and the single inequality then turns the algebra of operators into a place where convergent series can be manipulated: a series of operators that is absolutely convergent converges, and an operator close enough to the identity in the operator norm is invertible, with an inverse given by the geometric series. This makes the group of invertible operators open and inversion continuous.

This article treats the operator norm as an algebra norm and the completeness it inherits. The space of bounded operators and the equivalence of continuity with boundedness are *Bounded Operators on a Topological Vector Space*; the topology of bounded convergence, which for normed spaces is the operator-norm topology, is *Operators on a Locally Convex Space*; the transpose, which is an isometry, is *The Dual Operator*; the general theory of Banach algebras, the spectrum and the spectral radius belong to *Topological Algebras and Banach Algebras* in the next category of this Part, and the spectral theory of a single operator is *Analysis on Linear Spaces* in Part III. Nothing analytic and nothing geometric is used here beyond the convergence of series in a complete normed space, which is algebraic in nature.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $X$ and $Y$ are normed spaces over $\mathbb{K}$, $B(X, Y)$ is the space of bounded linear maps with the **operator norm** $\lVert T\rVert = \sup_{\lVert x\rVert \leq 1}\lVert Tx\rVert$, and $B(X) = B(X, X)$ is the algebra of bounded endomorphisms with composition as product and the identity $\mathrm{id}$.

## The Operator Algebra

**Proposition (the operator norm is an algebra norm).** On $B(X, Y)$ the operator norm is a norm, and composition is submultiplicative,

$$
\lVert ST\rVert \leq \lVert S\rVert\,\lVert T\rVert
$$

for $T \in B(X, Y)$ and $S \in B(Y, Z)$. Consequently $B(X)$ is a normed algebra over $\mathbb{K}$ with unit $\mathrm{id}$ of norm one, and $\lVert T^{n}\rVert \leq \lVert T\rVert^{n}$ for all $n \geq 1$.

**Proof.** The norm axioms are *Bounded Operators on a Topological Vector Space*; submultiplicativity is $\lVert STx\rVert \leq \lVert S\rVert\lVert Tx\rVert \leq \lVert S\rVert\lVert T\rVert\lVert x\rVert$ for $\lVert x\rVert \leq 1$. The unit has $\lVert \mathrm{id}\rVert = \sup_{\lVert x\rVert\leq1}\lVert x\rVert = 1$, and the power bound is induction.

**Proposition (the norm is not multiplicative in general).** A bounded operator $T$ satisfies $\lVert Tx\rVert = \lVert x\rVert$ for all $x$ exactly when $\lVert T\rVert = 1$ and $T$ is an isometry; the norm of a product can be strictly smaller than the product of the norms, $\lVert ST\rVert < \lVert S\rVert\lVert T\rVert$, and it can be zero for nonzero factors. The algebra $B(X)$ is commutative exactly when $X$ has dimension at most one.

**Proof.** If $T$ is an isometry then $\lVert T\rVert = 1$ and the two quantities agree; the strict inequality is exhibited by two non-overlapping rank-one operators on $\ell^{2}$, whose product is $0$, and the commutativity statement by the shifts $L, R$ of $\ell^{p}$ with $LR = \mathrm{id}$, $RL \neq \mathrm{id}$.

## Completeness and the Neumann Series

**Theorem (completeness).** If $Y$ is a Banach space then $B(X, Y)$ is a Banach space; in particular $B(X)$ is a Banach algebra when $X$ is a Banach space.

**Proof.** This is the completeness of the bounded operators of *Normed and Banach Spaces*: a Cauchy sequence $(T_{n})$ has $(T_{n}x)$ Cauchy for each $x$, defines $Tx = \lim T_{n}x$, and the limit is linear and bounded with $\lVert T - T_{n}\rVert \to 0$. The algebra structure is the proposition above, and a complete normed algebra is a Banach algebra by definition.

**Theorem (the Neumann series and the invertibles).** Let $X$ be a Banach space and let $T \in B(X)$ with $\lVert T\rVert < 1$. Then $\mathrm{id} - T$ is invertible, with

$$
(\mathrm{id} - T)^{-1} = \sum_{n \geq 0} T^{n}, \qquad \lVert(\mathrm{id} - T)^{-1}\rVert \leq \frac{1}{1 - \lVert T\rVert} .
$$

Consequently the group $B(X)^{\times}$ of invertible operators is open in $B(X)$, and inversion is continuous.

**Proof.** The series converges absolutely, $\sum_{n}\lVert T^{n}\rVert \leq \sum_{n}\lVert T\rVert^{n} < \infty$, and $B(X)$ is complete, so its sum exists; the identity $(\mathrm{id} - T)\sum_{n \leq N}T^{n} = \mathrm{id} - T^{N+1}$ passes to the limit, giving invertibility and the estimate. If $S$ is invertible and $\lVert T - S\rVert < \lVert S^{-1}\rVert^{-1}$ then $T = S(\mathrm{id} - S^{-1}(S - T))$ with $\lVert S^{-1}(S - T)\rVert < 1$, so $T$ is invertible; hence the invertibles are open. Continuity of inversion follows from the same expansion, applied to $T^{-1} = \sum_{n}(S^{-1}(S-T))^{n}S^{-1}$ near $S$.

**Corollary (the closed unit ball of the invertibles).** The set of operators of norm at most one is closed and convex; the invertibles of the form $\mathrm{id} - T$ with $\lVert T\rVert \leq r < 1$ form the closed ball of radius $r$ in the algebra of perturbations, and the image of that ball under inversion is bounded by $1/(1-r)$.

**Proof.** Immediate from the theorem and the triangle inequality for the norm.

## The Operator Norm and the Topologies

**Proposition (the operator norm defines the topology of bounded convergence).** On $B(X, Y)$ the operator norm generates the topology of uniform convergence on the bounded subsets of $X$, so $B(X, Y) = \mathcal{L}_{b}(X, Y)$ as topological spaces.

**Proof.** Bounded subsets of a normed space are contained in multiples of the unit ball, and the topology of bounded convergence is generated by the seminorm with $B$ the unit ball, which is the operator norm. This is the normed case of *Operators on a Locally Convex Space*.

**Proposition (the operator norm and the dual norm).** For $T \in B(X, Y)$ the transpose satisfies $\lVert T'\rVert = \lVert T\rVert$; the operator norm on $B(X, \mathbb{K}) = X^{*}$ is therefore the dual norm, and the operator norm on $B(X, Y)$ is recovered from the dual as

$$
\lVert T\rVert = \sup\{\lvert y^{*}(Tx)\rvert : \lVert x\rVert \leq 1, \ \lVert y^{*}\rVert \leq 1\} .
$$

**Proof.** The equality $\lVert T'\rVert = \lVert T\rVert$ is *The Dual Operator*; the displayed characterisation is the two-sided supremum over the unit balls of $X$ and $Y^{*}$, which equals $\sup_{\lVert x\rVert\leq1}\lVert Tx\rVert$ by the Hahn–Banach norm-attaining functional.

**Proposition (quotient norm).** Let $M \subseteq X$ be a closed subspace and let $q : X \to X/M$ be the quotient map. The **quotient norm** $\lVert qx\rVert = \inf\{\lVert x - m\rVert : m \in M\}$ makes $X/M$ a normed space, and for $T \in B(X, Y)$ vanishing on $M$ the induced operator $\overline{T}$ on $X/M$ has the same norm, $\lVert \overline{T}\rVert = \lVert T\rVert$. The algebra $B(X)/\mathcal{C}(X)$ of the bounded operators modulo the operators of finite rank has the quotient norm.

**Proof.** The quotient norm is the gauge of the image of the unit ball; the equality $\lVert \overline{T}\rVert = \lVert T\rVert$ holds because $\overline{T}q = T$ and $q$ maps the closed unit ball of $X$ onto a set dense in the closed unit ball of $X/M$. The statement about the finite-rank operators is the same computation with the two-sided ideal $\mathcal{C}(X)$ of finite-rank operators in place of $M$.

## Examples

**Example (the matrix algebra).** For $X = \mathbb{K}^{n}$ the algebra $B(X)$ is the matrix algebra $M_{n}(\mathbb{K})$, the operator norm is the spectral norm $\lVert A\rVert = \sigma_{1}(A)$ of *Topological Tensor Products*, and the Neumann series is the classical expansion $(\mathrm{id} - A)^{-1} = \sum_{n}A^{n}$ for a matrix with spectral norm below one; the group of invertibles is open and dense.

**Example (the diagonal algebra).** On $\ell^{p}$ the diagonal operators $D_{\varphi}$ with $\varphi \in \ell^{\infty}$ form a closed commutative subalgebra of $B(\ell^{p})$ isometric to $\ell^{\infty}$, with $\lVert D_{\varphi}\rVert = \lVert \varphi\rVert_{\infty}$ and $D_{\varphi}D_{\psi} = D_{\varphi\psi}$; the subalgebra is isomorphic to the $C(K)$ multiplication operators of the compact case.

**Example (the multiplication operators).** On $C(K)$ for a compact Hausdorff space $K$ the operators $M_{f}(g) = fg$ form a commutative subalgebra of $B(C(K))$ isometric to $C(K)$, and $\lVert M_{f}\rVert = \lVert f\rVert_{\infty}$; the subalgebra is closed because convergence in the operator norm is uniform convergence of the multipliers.

**Example (the operators that attain their norm).** The identity attains its norm $1$ at every unit vector, and the right shift on $\ell^{p}$ attains its norm $1$ at every unit vector; the diagonal operator $D_{\varphi}$ with $\varphi_{k} = 1 - 1/k$ has norm $1$, the supremum of $\lvert \varphi_{k}\rvert$ over $k$, and does not attain it at any unit vector, only in the limit. The operator norm is a supremum in general, not a maximum.

## Summary

On the bounded operators between normed spaces the operator norm makes $B(X, Y)$ a normed space and composition an algebra product with $\lVert ST\rVert \leq \lVert S\rVert\lVert T\rVert$, so $B(X)$ is a normed algebra with unit of norm one and $\lVert T^{n}\rVert \leq \lVert T\rVert^{n}$; the norm is not multiplicative in general and the algebra is noncommutative as soon as the dimension exceeds one. When $Y$ is complete $B(X, Y)$ is complete, and on a Banach space $X$ the algebra $B(X)$ is a Banach algebra; then the Neumann series gives $(\mathrm{id} - T)^{-1} = \sum_{n}T^{n}$ with $\lVert(\mathrm{id} - T)^{-1}\rVert \leq (1 - \lVert T\rVert)^{-1}$ whenever $\lVert T\rVert < 1$, the group of invertible operators is open and inversion is continuous. The operator norm generates the topology of bounded convergence, it equals the norm of the transpose, it is recovered from the dual as the two-sided supremum over the unit balls of the space and its dual, and it passes to the induced operator on a quotient by a closed subspace. The matrix algebra with the spectral norm, the diagonal algebra and the multiplication operators of $C(K)$ are the standard examples, and the operator norm is a supremum that need not be attained.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(X, Y)$ | Bounded linear maps with the operator norm |
| $B(X)$ | Bounded endomorphisms, a normed algebra |
| $\lVert T\rVert$ | Operator norm, $\sup_{\lVert x\rVert \leq 1}\lVert Tx\rVert$ |
| $\lVert ST\rVert \leq \lVert S\rVert\lVert T\rVert$ | Submultiplicativity |
| $\mathrm{id} - T$, $\sum_n T^{n}$ | Neumann series and invertibility for $\lVert T\rVert < 1$ |
| $B(X)^{\times}$ | Group of invertible bounded operators, open |
| $\lVert T'\rVert = \lVert T\rVert$ | Isometry of the transpose |
| $q : X \to X/M$, $\lVert \overline{T}\rVert = \lVert T\rVert$ | Quotient norm and induced operator |
| $M_{n}(\mathbb{K})$ | Matrix algebra of $\mathbb{K}^{n}$ |
| $D_{\varphi}$, $M_{f}$ | Diagonal and multiplication operators |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the operator norms and the topology of bounded convergence.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, second edition, 1991), for the bounded operators, the Neumann series and the group of invertibles.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the operator norm, its completeness and the classical examples.
- Ronald G. Douglas, *Banach Algebra Techniques in Operator Theory* (Springer, second edition, 1998), for the algebra $B(X)$, its invertibles and the Neumann series.
- M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the operator norm and the standard examples of bounded operators.
