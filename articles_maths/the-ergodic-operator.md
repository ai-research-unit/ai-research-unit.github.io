
# __The Ergodic Operator__

## Introduction

To a measure-preserving transformation $T$ of a probability space the ergodic theory attaches the Koopman operator $U_Tf=f\circ T$, a unitary operator on $L^2$, and the question of the ergodic theorems is the question of the behaviour of the Cesàro averages of its powers. The average
$$
A_n=\frac1n\sum_{k=0}^{n-1}U_T^k
$$
is the **ergodic operator** of $T$, and the mean ergodic theorem of von Neumann states that $A_n$ converges in the strong operator topology to the orthogonal projection $P$ onto the fixed space of $U_T$; when $T$ is ergodic that projection is the rank-one operator of the mean, $Pf=\int f\,d\mu$. The theorem is a statement about one operator and not about the transformation: it holds for every contraction of a Hilbert space, and it identifies the limit as the spectral projection of the operator at the eigenvalue one. This article defines the ergodic operator, proves the mean ergodic theorem in the sharp operator form, identifies the ergodic projection with the conditional expectation onto the invariant $\sigma$-algebra, records the general contraction version, and states the maximal inequality of Hopf and its use in the pointwise theorem.

The ergodic theory is fixed elsewhere. The measure-preserving system, the invariant $\sigma$-algebra, the ergodicity and the mixing, the Koopman operator, the von Neumann and Birkhoff ergodic theorems, the ergodic decomposition and the entropy are *Ergodic Theory*, written, and are quoted here; the present article is the operator layer of those statements, and it proves the mean convergence as a theorem about the averages of the powers of a contraction. The conditional expectation as an operator and its projection property are *The Conditional Expectation Operator*, next in this category; the projection $P$ of the theorem is that operator for the invariant $\sigma$-algebra. The Markov operator and its mean ergodic theorem are *The Markov Operator*, earlier in this category; the spectral theorem for normal operators and the orthogonal projections are *Banach and Hilbert Spaces*; the group-action generalisation of the whole subject is *Ergodic Theory of Group Actions*, later in this Part. No physics is invoked.

Throughout, $(X,\mathcal B,\mu)$ is a probability space, $T:X\to X$ is measurable and measure-preserving, $\mathcal I=\{A\in\mathcal B:\mu(T^{-1}A\triangle A)=0\}$ is the invariant $\sigma$-algebra, and statements hold almost everywhere (a.e.). The Koopman operator is $Uf=f\circ T$, the fixed space is $\ker(U-I)$, a **coboundary** is a function $g\circ T-g$, and the inner product is $\langle f,g\rangle=\int_Xf\bar g\,d\mu$ with $\|f\|_2=\langle f,f\rangle^{1/2}$.

## The Koopman Operator

### Definition and unitarity

**Definition.** The **Koopman operator** of the measure-preserving $T$ is
$$
U=U_T:L^2(X,\mu)\to L^2(X,\mu),\qquad Uf=f\circ T .
$$

**Theorem.** $U$ is a linear isometry, and it is unitary exactly when $T$ is invertible, in which case $U^{-1}=U_{T^{-1}}$. The fixed space $\ker(U-I)$ is the space of the $T$-invariant $L^2$ functions, and it is the image of the orthogonal projection onto $L^2(X,\mathcal I,\mu)$.

*Proof.* The isometry is the change of variables, $\langle Uf,Ug\rangle=\int f(Tx)\bar g(Tx)\,d\mu(x)=\int f\bar g\,d\mu$, because $T$ preserves $\mu$; $U$ is onto exactly when $T$ is invertible. A function is fixed by $U$ exactly when it is measurable with respect to $\mathcal I$, and the $L^2$ functions of $\mathcal I$ form the closed subspace $L^2(X,\mathcal I,\mu)$.

### The coboundary decomposition

**Theorem (orthogonal decomposition).** For a unitary $U$,
$$
L^2=\ker(U-I)\oplus\overline{\operatorname{Im}(U-I)},
$$
the second summand being the closed span of the coboundaries $g\circ T-g$, and the two summands are orthogonal.

*Proof.* For a normal operator the orthogonal complement of the kernel is the closure of the range; for $U$ unitary the range of $U-I$ is the span of the coboundaries, and the orthogonal complement of the range is the kernel. The decomposition is the form in which the mean ergodic theorem is proved.

## The Ergodic Operator and the Mean Ergodic Theorem

### Definition

**Definition.** The **ergodic operator** of $T$ is the sequence of Cesàro averages
$$
A_n=\frac1n\sum_{k=0}^{n-1}U^k,\qquad n\ge1,
$$
each $A_n$ a contraction of $L^2$ with $\|A_n\|\le1$.

### The mean ergodic theorem

**Theorem (von Neumann).** Let $P$ be the orthogonal projection of $L^2$ onto $\ker(U-I)$. Then for every $f\in L^2$,
$$
A_nf=\frac1n\sum_{k=0}^{n-1}f\circ T^k\longrightarrow Pf\qquad \text{in } L^2,
$$
and $\|A_nf\|\le\|f\|_2$ for every $n$.

*Proof.* Decompose $f=Pf+(f-Pf)$ by the orthogonal decomposition. The first summand is fixed, so $A_nPf=Pf$. The second lies in the closure of the range: on an exact coboundary $f=g\circ T-g$ the averages telescope,
$$
A_nf=\frac1n\bigl(U^ng-g\bigr),
$$
whose norm is at most $2\|g\|_2/n\to0$, and the general element of the closure is handled by approximation, the operators $A_n$ being uniformly bounded. The theorem is *Ergodic Theory*, written; the proof reproduced here is the operator form.

### The limit as the ergodic projection

**Theorem (identification of the limit).** The limit $P$ of the ergodic operator is the conditional expectation onto the invariant $\sigma$-algebra,
$$
Pf=\mathbb E[f\mid\mathcal I]\qquad \text{a.e.},
$$
and $T$ is ergodic exactly when $P$ is the rank-one projection $Pf=\int f\,d\mu$.

*Proof.* The range of $P$ is $\ker(U-I)=L^2(X,\mathcal I,\mu)$ and $P$ fixes $L^2(X,\mathcal I,\mu)$ and is self-adjoint, which is the characterisation of the conditional expectation as the orthogonal projection onto $L^2(X,\mathcal I,\mu)$; the conditional expectation as a projection is *The Conditional Expectation Operator*, next in this category. The ergodicity criterion is the triviality of $\mathcal I$, which makes $L^2(X,\mathcal I,\mu)$ one-dimensional.

### The pointwise companion

**Theorem (Birkhoff).** For $f\in L^1(X,\mu)$ the averages converge a.e. and in $L^1$ to $Pf=\mathbb E[f\mid\mathcal I]$. The mean theorem is the $L^2$ statement and the pointwise theorem is the a.e. statement; the second is *Ergodic Theory*, and the maximal inequality of Hopf below is its engine.

## The General Contraction Theorem

**Theorem (von Neumann for a contraction).** Let $V$ be a contraction of a Hilbert space $\mathcal H$ and let $P$ be the orthogonal projection onto $\ker(V-I)$. Then
$$
\frac1n\sum_{k=0}^{n-1}V^k\longrightarrow P\qquad \text{strongly}.
$$

*Proof.* The same decomposition, with the coboundary telescoping $A_n(Vg-g)=(V^ng-g)/n$; the estimate $\|V^n\|\le1$ bounds it by $2\|g\|/n$. The only difference from the unitary case is that the range of $V-I$ need not be closed, which is why the closure is taken.

**Corollary (the Markov and transition cases).** The mean ergodic theorem for a Markov operator on $L^2(\pi)$ and for the elements of a transition semigroup is the corollary of the general theorem; these are *The Markov Operator* and *The Transition Operator*, earlier in this category.

**Theorem (spectral form).** If $V$ is normal with spectral measure $E$, then the ergodic projection is the spectral projection at the eigenvalue one, $P=E(\{1\})$, and the ergodic operator is the Cesàro mean of the spectral integrals $\int z^k\,dE(z)$.

*Proof.* The functional calculus puts $V^k=\int z^k\,dE(z)$, and the Cesàro mean of $z^k$ converges to the indicator of $\{z=1\}$ pointwise on the unit disc, so the strong limit is $E(\{1\})$; the details are the spectral theorem of *Banach and Hilbert Spaces*.

## The Maximal Inequality

**Theorem (Hopf's maximal inequality).** Let $T$ be measure-preserving and let $f\in L^1$, with $M_Nf=\max_{n\le N}\sum_{k=0}^{n-1}f\circ T^k$. Then
$$
\int_{\{M_Nf>0\}}f\,d\mu\ge0 .
$$

*Proof.* On the set where the first positive partial sum occurs at the index $k$, the sum $S_kf$ dominates the later increments up to $N$, and summing over $k$ gives the displayed inequality; this is the maximal ergodic inequality of *Ergodic Theory*.

The maximal inequality is the estimate behind the pointwise ergodic theorem: applied to $\pm(f-g)$ for a bounded invariant $g$ it controls the set on which the averages differ from $g$ by more than $\varepsilon$, and the density of the bounded functions in $L^1$ gives the a.e. convergence. The mean theorem of this article needs no maximal inequality, since the convergence is in norm, and the contrast between the two proofs is the reason the operator form is the one that generalises to the contraction.

## Worked Examples

**Example (an irrational rotation).** Let $X=\mathbb R/\mathbb Z$, $\mu$ the Lebesgue measure and $Tx=x+\alpha$ with $\alpha$ irrational. The characters $e_m(x)=e^{2\pi imx}$ satisfy $Ue_m=e^{2\pi im\alpha}e_m$, so $A_ne_m=\frac1n\sum_{k<n}e^{2\pi imk\alpha}e_m\to0$ for $m\ne0$ and $A_ne_0=e_0$; the ergodic projection is the mean $Pf=\int f\,d\mu$, and the system is ergodic. The convergence is not absolute and the rate is not geometric, which is the generic behaviour of the ergodic operator.

**Example (the Bernoulli shift).** Let $X=\{0,1\}^{\mathbb Z}$ with the product measure $\frac12,\frac12$ and $T$ the shift. The system is mixing, hence ergodic, the invariant $\sigma$-algebra is trivial, and the ergodic projection is the mean; the correlation $\langle U^nf,g\rangle\to\langle f,1\rangle\langle1,g\rangle$ decays exponentially for a finitely determined $f,g$, which is faster than the mean convergence of the ergodic operator and is a mixing statement, not a mean ergodic one.

**Example (the identity).** For $T=\mathrm{id}$ one has $U=I$, $\mathcal I=\mathcal B$ and $A_n=I$; the ergodic projection is the identity, and the system is ergodic only when the measure space is a single atom up to null sets. This is the degenerate case in which the fixed space is as large as possible.

**Example (the Markov operator).** For an irreducible positive recurrent chain the average $\frac1n\sum_{k<n}P^k$ converges in $L^2(\pi)$ to the rank-one projection onto the constants; this is the Markov case of the theorem, stated in *The Markov Operator*, earlier in this category.

## Failure of the Degenerate Cases

The ergodic operator degenerates in four configurations. First, the projection $P$ need not be of rank one: for a non-ergodic system it is the conditional expectation onto a nontrivial invariant $\sigma$-algebra, and the limit of the averages is a random variable rather than a constant. Second, there is no rate: the convergence of the Cesàro averages is not exponential in general, and for the rotation the averages decay at the rate of a Dirichlet kernel; the geometric rate is a property of the mixing systems and not of the theorem. Third, the mean theorem fails in $L^1$ for the projection: $A_n$ is a contraction of $L^1$ but the limit of $A_nf$ need not be $\mathbb E[f\mid\mathcal I]$ in the $L^1$ norm, and the a.e. theorem is the substitute; the failure is the reason the pointwise theory needs the maximal inequality. Fourth, for a contraction that is not normal there need be no spectral projection at the eigenvalue one, and the limit of the averages is not read from a spectral measure; the normal case, and in particular the unitary Koopman operator, is the boundary on which the spectral description is available.

## Summary

To a measure-preserving transformation $T$ the ergodic theory attaches the Koopman operator $Uf=f\circ T$, an isometry on $L^2$ that is unitary when $T$ is invertible, with fixed space $\ker(U-I)$ the invariant $L^2$ functions. The ergodic operator is the Cesàro average $A_n=\frac1n\sum_{k<n}U^k$, a contraction, and the mean ergodic theorem of von Neumann states that $A_n$ converges strongly to the orthogonal projection $P$ onto the fixed space; the proof is the orthogonal decomposition of $L^2$ into the fixed space and the closure of the coboundaries, on which the averages telescope. The limit is the conditional expectation $\mathbb E[\cdot\mid\mathcal I]$ onto the invariant $\sigma$-algebra, the rank-one mean when the system is ergodic. The theorem holds for every contraction of a Hilbert space, and for a normal contraction the limit is the spectral projection at the eigenvalue one. The pointwise theorem of Birkhoff is the a.e. companion, and its engine is Hopf's maximal inequality $\int_{\{M_Nf>0\}}f\,d\mu\ge0$. The conditional expectation operator is next in this category, the Markov and transition cases are the preceding articles, and the group-action generalisation is later in this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X,\mathcal B,\mu,T)$ | measure-preserving system |
| a.e. | almost everywhere; the probabilistic synonym is not used here |
| $U=U_T$, $Uf=f\circ T$ | Koopman operator; isometry, unitary for invertible $T$ |
| $\mathcal I$ | invariant $\sigma$-algebra |
| $\ker(U-I)$, coboundary | fixed functions; $g\circ T-g$ |
| $A_n=\frac1n\sum_{k<n}U^k$ | ergodic operator |
| $P$, $A_n\to P$ | ergodic projection; the mean ergodic theorem |
| $Pf=\mathbb E[f\mid\mathcal I]$ | the limit as a conditional expectation |
| $M_Nf$, $Mf$ | truncated maximum, maximal function |
| $\int_{\{M_Nf>0\}}f\,d\mu\ge0$ | Hopf's maximal inequality |

## Further Reading

- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the Koopman operator, the mean ergodic theorem and the ergodic projection.
- Karl Petersen, *Ergodic Theory* (Cambridge University Press, 1983), for the spectral theory of the Koopman operator and the mixing hierarchy.
- John von Neumann, "Proof of the quasi-ergodic hypothesis", *Proceedings of the National Academy of Sciences* 18 (1932), 70–82, for the mean ergodic theorem.
- George D. Birkhoff, "Proof of the ergodic theorem", *Proceedings of the National Academy of Sciences* 17 (1931), 656–660, for the pointwise theorem.
- Eberhard Hopf, *Ergodentheorie* (Springer, 1937), for the maximal inequality.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the contractions, the fixed spaces and the Cesàro means.
