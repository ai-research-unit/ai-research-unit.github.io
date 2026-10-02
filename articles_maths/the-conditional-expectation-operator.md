
# __The Conditional Expectation Operator__

## Introduction

Conditional expectation is the averaging of a random variable over the information carried by a sub-$\sigma$-algebra, and on the square-integrable variables it is exactly the orthogonal projection onto the closed subspace of the measurable functions of that information. Writing $\mathbb E[\cdot\mid\mathcal G]$ for the operator belonging to a sub-$\sigma$-algebra $\mathcal G$, the identity
$$
\langle \mathbb E[X\mid\mathcal G],Y\rangle=\langle X,Y\rangle\qquad (Y\in L^2(\mathcal G))
$$
is the defining property, and it says that the conditional expectation is the self-adjoint idempotent whose range is $L^2(\mathcal G)$. This article treats the conditional expectation as an operator: the projection property and the module property over the bounded $\mathcal G$-measurable functions, the composition law of the tower as the law of a monotone family of projections, and the convergence of the projections along an increasing or a decreasing filtration, which is the martingale convergence theorem in operator form. The two facts that the conditional expectation and the adjoint agree, and that the conditional expectation is the ergodic projection for the invariant $\sigma$-algebra, are the reasons the operator is the meeting point of the probability theory and the ergodic theory.

The probabilistic content is fixed elsewhere. The conditional expectation, its existence by the Radon–Nikodym theorem, its elementary properties, the independence and the filtrations are *Independence and Conditional Expectation*, written; the martingale theory, the convergence theorem and the optional stopping theorem are *Martingales*, written; the invariant $\sigma$-algebra and the ergodic projection are *Ergodic Theory*, written; and the operator form of the mean ergodic theorem is *The Ergodic Operator*, the preceding article of this category. The orthogonal projections and the spectral theorem are *Banach and Hilbert Spaces*, the Radon–Nikodym theorem is *Measure Theory and Integration*. The present article is the operator layer and proves the projection statements and the convergence of the projections. No physics is invoked.

Throughout, $(\Omega,\mathcal F,\mathbb P)$ is a probability space, $\mathcal G\subseteq\mathcal F$ a sub-$\sigma$-algebra, and $L^2(\mathcal G)=L^2(\Omega,\mathcal G,\mathbb P)$ is the closed subspace of the $\mathcal G$-measurable square-integrable functions, identified with a subspace of $L^2(\mathcal F)=L^2(\Omega,\mathcal F,\mathbb P)$. The inner product is $\langle X,Y\rangle=\mathbb E[X\bar Y]$, the norm is $\|X\|_2=\langle X,X\rangle^{1/2}$, and the conditional expectation is written $\mathbb E[\cdot\mid\mathcal G]$ or $E_{\mathcal G}$.

## The Conditional Expectation as an Orthogonal Projection

### Definition

**Definition.** For $X\in L^2(\mathcal F)$ the **conditional expectation** $E_{\mathcal G}X=\mathbb E[X\mid\mathcal G]$ is the unique element of $L^2(\mathcal G)$ with
$$
\mathbb E[E_{\mathcal G}X\,\mathbf 1_A]=\mathbb E[X\,\mathbf 1_A]\qquad \text{for every } A\in\mathcal G,
$$
equivalently the unique element of $L^2(\mathcal G)$ orthogonal to $X-E_{\mathcal G}X$.

The two descriptions agree because the indicators of the sets of $\mathcal G$ span a dense subspace of $L^2(\mathcal G)$, so the orthogonality to $X-E_{\mathcal G}X$ is the same as the equality of the integrals.

### The projection properties

**Theorem.** The map $E_{\mathcal G}:L^2(\mathcal F)\to L^2(\mathcal F)$ is the orthogonal projection onto $L^2(\mathcal G)$; in particular
$$
E_{\mathcal G}^2=E_{\mathcal G},\qquad E_{\mathcal G}^*=E_{\mathcal G},\qquad \|E_{\mathcal G}\|=1,\qquad \|E_{\mathcal G}X\|_2\le\|X\|_2 ,
$$
and $E_{\mathcal G}X=X$ exactly when $X\in L^2(\mathcal G)$.

*Proof.* The range is contained in $L^2(\mathcal G)$ and $E_{\mathcal G}$ fixes $L^2(\mathcal G)$, so $E_{\mathcal G}^2=E_{\mathcal G}$; the self-adjointness is the defining identity $\langle E_{\mathcal G}X,Y\rangle=\langle X,E_{\mathcal G}Y\rangle$ for $X,Y\in L^2(\mathcal F)$, which follows from the same identity restricted to $Y\in L^2(\mathcal G)$ after decomposing; the norm is one because a nonzero projection has norm one, and the contraction is the general property of a projection. The fixed space is the range.

**Theorem (positivity and Jensen).** If $X\ge0$ then $E_{\mathcal G}X\ge0$, and for every convex $\varphi:\mathbb R\to\mathbb R$ with $\varphi(X)$ integrable,
$$
\varphi(E_{\mathcal G}X)\le E_{\mathcal G}[\varphi(X)] .
$$

*Proof.* The positivity is the definition of the conditional expectation as an average; the inequality is the conditional Jensen inequality of *Independence and Conditional Expectation*, which is the statement that the projection is an order-preserving contraction and not merely a linear one.

### The module property

**Theorem (the module property).** If $Y$ is bounded and $\mathcal G$-measurable and $X\in L^2(\mathcal F)$, then
$$
E_{\mathcal G}(YX)=Y\,E_{\mathcal G}(X).
$$
Equivalently, $E_{\mathcal G}$ is a module map over $L^\infty(\mathcal G)$: it commutes with the multiplication by the bounded $\mathcal G$-measurable functions.

*Proof.* Both sides are $\mathcal G$-measurable, and for $A\in\mathcal G$ the integral of the right side over $A$ is $\mathbb E[Y\mathbf 1_A X]=\mathbb E[Y\mathbf 1_A E_{\mathcal G}X]$, which is the integral of the left side, because $Y\mathbf 1_A$ is $\mathcal G$-measurable and bounded; the uniqueness in the definition gives the identity.

The module property is the operator statement that the conditional expectation is not an arbitrary projection but the projection onto an $L^\infty(\mathcal G)$-submodule; it is what makes the conditional expectation compatible with the algebra of random variables, and it is used in *The Involution on the Operator Algebra of a Process*, later in this category.

## The Tower and the Lattice of Sub-$\sigma$-algebras

### Composition and the tower

**Theorem (the tower property).** If $\mathcal H\subseteq\mathcal G$ are sub-$\sigma$-algebras, then
$$
E_{\mathcal H}E_{\mathcal G}=E_{\mathcal G}E_{\mathcal H}=E_{\mathcal H}.
$$
Consequently the projections $\{E_{\mathcal G}\}$ over the sub-$\sigma$-algebras of $\mathcal F$ form a commuting family, and the map $\mathcal G\mapsto E_{\mathcal G}$ reverses inclusions.

*Proof.* The range of $E_{\mathcal G}$ is $L^2(\mathcal G)$ and $E_{\mathcal H}$ is the identity on $L^2(\mathcal H)\subseteq L^2(\mathcal G)$, so $E_{\mathcal H}E_{\mathcal G}=E_{\mathcal H}$; the second product is the adjoint of the first.

### Conditional independence

**Theorem (the conditional expectation and independence).** If $\mathcal G$ and $\sigma(X)$ are independent, then $E_{\mathcal G}X=\mathbb E[X]$; more generally, if $\mathcal G$ is independent of $\sigma(X)$ given $\mathcal H\subseteq\mathcal G$, then $E_{\mathcal G}X=E_{\mathcal H}X$.

*Proof.* The first statement is the constancy of the conditional expectation on an independent $\sigma$-algebra, from the definition applied to the generating sets; the second is the tower applied to the conditional law, and it is the statement that a conditional expectation only uses the information in $\mathcal G$ that is not already independent of $X$. The independence is *Independence and Conditional Expectation*.

## Martingale Convergence

### The increasing projections

**Theorem (convergence of the projections).** Let $\{\mathcal F_n\}_{n\ge0}$ be an increasing filtration with $\mathcal F_\infty=\sigma(\bigcup_n\mathcal F_n)$. Then for every $X\in L^2(\mathcal F)$,
$$
E_{\mathcal F_n}X\longrightarrow E_{\mathcal F_\infty}X\qquad \text{in } L^2\text{ and a.s.},
$$
and the sequence $\{E_{\mathcal F_n}X\}$ is the uniformly integrable martingale of *Martingales*, written $X_n=\mathbb E[X\mid\mathcal F_n]$.

*Proof.* The projections $E_{\mathcal F_n}$ increase with $n$, and $\bigcup_nL^2(\mathcal F_n)$ is dense in $L^2(\mathcal F_\infty)$; the strong convergence of an increasing family of projections to the projection onto the closed union is the standard fact for projections, and the a.s. convergence is Lévy's theorem for the uniformly integrable martingale $X_n=E_{\mathcal F_n}X$. The martingale convergence theorem is *Martingales*.

### The decreasing case and Lévy's downward theorem

**Theorem (reverse martingale).** Let $\{\mathcal G_n\}_{n\ge0}$ be a decreasing filtration with $\mathcal G_\infty=\bigcap_n\mathcal G_n$. Then for every $X\in L^1(\mathcal F)$,
$$
E_{\mathcal G_n}X\longrightarrow E_{\mathcal G_\infty}X\qquad \text{a.s. and in } L^1 ,
$$
and on $L^2$ the convergence is also in norm.

*Proof.* The sequence $\{E_{\mathcal G_n}X\}$ is a reverse martingale, and the decreasing family of projections has as strong limit the projection onto the intersection $\bigcap_nL^2(\mathcal G_n)=L^2(\mathcal G_\infty)$; the $L^2$ statement is the projection statement, and the a.s. and $L^1$ statements are the downward convergence theorem of *Martingales*, which is applied here.

### The maximal inequality

**Theorem (Doob's maximal inequality, operator form).** For $X\in L^2$ and the martingale $X_n=E_{\mathcal F_n}X$,
$$
\Bigl\|\sup_{n\ge0}|X_n|\Bigr\|_2\le2\|X\|_2 .
$$

*Proof.* The inequality is Doob's $L^2$ maximal inequality for the martingale of the projections; it is *Martingales*, and it is recorded here because it is the quantitative form of the convergence of the projections.

## The Conditional Expectation and the Ergodic Projection

**Theorem.** Let $T$ be measure-preserving on $(X,\mathcal B,\mu)$ with invariant $\sigma$-algebra $\mathcal I$. Then the ergodic projection of *The Ergodic Operator*, the preceding article, is the conditional expectation $E_{\mathcal I}$, and the mean ergodic theorem is the statement that the Cesàro averages of the Koopman powers converge strongly to $E_{\mathcal I}$.

*Proof.* The ergodic projection is the orthogonal projection onto $\ker(U-I)=L^2(X,\mathcal I,\mu)$, which is the range of $E_{\mathcal I}$; the two projections therefore coincide. In the Markov case the projection is $E_{\mathcal J}$ for the invariant $\sigma$-algebra $\mathcal J$ of the chain, and the operator is the rank-one projection onto the constants when the chain is ergodic.

The identification places the two operators in one family: the conditional expectations are the projections of the probability theory, the ergodic projections are the limits of the Cesàro averages, and the invariant $\sigma$-algebra is the common object.

## Worked Examples

**Example (a finite $\sigma$-algebra).** Let $\mathcal G$ be generated by a finite partition $\{A_1,\dots,A_k\}$ of positive probability. Then $E_{\mathcal G}X$ is constant on each atom,
$$
E_{\mathcal G}X=\sum_{i=1}^k\frac{\mathbb E[X\mathbf 1_{A_i}]}{\mathbb P(A_i)}\mathbf 1_{A_i},
$$
and the projection has rank $k$; it is the averaging of $X$ over the atoms, the discrete Radon–Nikodym derivative of the restriction of $X\,d\mathbb P$ to $\mathcal G$.

**Example (the tail $\sigma$-algebra).** Let $\{Y_n\}$ be independent and $\mathcal G_n=\sigma(Y_n,Y_{n+1},\dots)$, so that $\mathcal G_n$ decreases to the tail $\sigma$-algebra $\mathcal T$. Then $E_{\mathcal G_n}X\to E_{\mathcal T}X$ a.s.; Kolmogorov's zero–one law states that $\mathcal T$ is trivial for an independent sequence, so the limit is the constant $\mathbb E[X]$. This is the reverse case of the convergence theorem and the probabilistic form of the zero–one law.

**Example (the Markov conditional expectation).** For a Markov chain with initial state $x$ the identity $Pf(x)=\mathbb E[f(X_1)\mid X_0=x]$ exhibits the Markov operator as the conditional expectation on the next state; the module property $E_{\mathcal G}(Yf)=YE_{\mathcal G}(f)$ for $Y$ a function of $X_0$ is the operator content of the Markov property.

**Example (the ergodic case).** For an ergodic measure-preserving $T$ the invariant $\sigma$-algebra is trivial, $E_{\mathcal I}$ has rank one and its range is the constants; the ergodic projection is $Pf=\int f\,d\mu$. This is the boundary case in which the conditional expectation carries the least information.

## Failure of the Degenerate Cases

The conditional expectation as an operator degenerates in four configurations. First, on $L^1$ it is a contraction but not an orthogonal projection: there is no inner product on $L^1$, the map $E_{\mathcal G}$ is a positive contractive idempotent whose range is $L^1(\mathcal G)$, and the identity $\|E_{\mathcal G}X\|_1=\|X\|_1$ holds exactly when $X$ is $\mathcal G$-measurable; the Hilbert-space statements are available only after the passage to $L^2$. Second, an increasing family of projections can converge strongly without converging in norm; the limiting projection $E_{\mathcal F_\infty}$ need not be at finite distance from any $E_{\mathcal F_n}$, and the convergence of the operators is strong and not uniform. Third, the convergence of the projections need not hold in $L^1$ for a general $X\in L^1$ without the uniform integrability of the martingale, which is the hypothesis of Lévy's theorem and not a formality. Fourth, for a conditional expectation onto a $\sigma$-algebra that is not countably generated the density argument must be replaced by a net rather than a sequence, and the convergence of the projections is along the net; the countably generated case, which is the hypothesis of the sequential theorems, is the boundary on which the statements are as stated.

## Summary

The conditional expectation $\mathbb E[\cdot\mid\mathcal G]$ is the orthogonal projection of $L^2(\mathcal F)$ onto the closed subspace $L^2(\mathcal G)$, characterised by $\mathbb E[E_{\mathcal G}X\,\mathbf 1_A]=\mathbb E[X\mathbf 1_A]$ for $A\in\mathcal G$; it is self-adjoint, idempotent, of norm one, positive, dominated by the conditional Jensen inequality, and a module map over the bounded $\mathcal G$-measurable functions. The projections form a commuting family under the tower property $E_{\mathcal H}E_{\mathcal G}=E_{\mathcal H}$ for $\mathcal H\subseteq\mathcal G$, and the conditional expectation is the identity on $L^2(\mathcal G)$ and the mean on an independent $\sigma$-algebra. Along an increasing filtration the projections converge strongly and a.s. to $E_{\mathcal F_\infty}$, which is the martingale convergence theorem for the uniformly integrable martingale $X_n=\mathbb E[X\mid\mathcal F_n]$, with Doob's maximal inequality as the quantitative form; along a decreasing filtration they converge to $E_{\mathcal G_\infty}$ by the downward theorem, with Kolmogorov's zero–one law as the independent case. The ergodic projection of the preceding article is $E_{\mathcal I}$ for the invariant $\sigma$-algebra, so the conditional expectations and the ergodic projections are one family. The probabilistic statements are *Independence and Conditional Expectation* and *Martingales*, and the operator layer is proved here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\Omega,\mathcal F,\mathbb P)$, $\mathcal G$ | probability space and sub-$\sigma$-algebra |
| $E_{\mathcal G}X=\mathbb E[X\mid\mathcal G]$ | conditional expectation |
| $L^2(\mathcal G)$ | $\mathcal G$-measurable square-integrable functions |
| $E_{\mathcal G}^2=E_{\mathcal G}$, $E_{\mathcal G}^*=E_{\mathcal G}$ | idempotence and self-adjointness |
| $E_{\mathcal G}(YX)=YE_{\mathcal G}(X)$ | module property over $L^\infty(\mathcal G)$ |
| $E_{\mathcal H}E_{\mathcal G}=E_{\mathcal H}$ | tower property for $\mathcal H\subseteq\mathcal G$ |
| $\mathcal F_n$, $\mathcal F_\infty$ | increasing filtration and its limit |
| $E_{\mathcal F_n}X\to E_{\mathcal F_\infty}X$ | martingale convergence of the projections |
| $\mathcal G_n$, $\mathcal G_\infty$ | decreasing filtration and its intersection |
| $\mathcal I$, $E_{\mathcal I}$ | invariant $\sigma$-algebra and ergodic projection |

## Further Reading

- Joseph L. Doob, *Stochastic Processes* (Wiley, 1953), for the conditional expectation as an operator and the martingale convergence theorems.
- David Williams, *Probability with Martingales* (Cambridge University Press, 1991), for the projections, the tower property and the convergence theorems.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the orthogonal projections and the strong convergence of monotone families.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd edition, 1990), for the projection operators and the conditional expectation on a von Neumann algebra.
- Patrick Billingsley, *Probability and Measure* (Wiley, 3rd edition, 1995), for the construction of the conditional expectation by the Radon–Nikodym theorem.
