
# __The Markov Operator__

## Introduction

A Markov chain carries two operators, one acting on the functions of its state and one acting on the measures on its state, and they are the transposes of each other. The operator on functions, $Pf(x)=\mathbb E_x[f(X_1)]$, averages the next state, and the operator on measures, $\mu P(B)=\mathbb P_\mu(X_1\in B)$, pushes a measure forward by one step; the invariance of the transition law is the statement that the two actions agree with the pairing $\langle f,\mu\rangle=\int f\,d\mu$. This article treats the pair as a single operator with two actions: it records the positivity, the preservation of the constants and the two contraction properties, identifies the invariant measures as the fixed vectors of the action on measures, reads the ergodicity of the chain as the one-dimensionality of the fixed space of the action on functions, proves the mean ergodic theorem for the Cesàro averages of the powers, and states the spectral radius, the Perron–Frobenius theorem and the spectral gap that control the rate of convergence.

The probabilistic content is fixed elsewhere and is cited rather than re-derived. The Markov chain, the transition kernel and the Chapman–Kolmogorov equations, the classification of the states, the recurrence and the transience, the existence and the uniqueness of the stationary distribution, the ergodic theorem for the chain and the convergence to stationarity are *Markov Chains and Processes*, written; the operator identities proved here are the operator form of those statements. The link to the martingale theory is $Ph=h$: a bounded harmonic function of the chain is a martingale along the chain, and the fixed space of the operator is the space of the harmonic functions, so the martingale convergence theorem of *Martingales* controls them. The condition that the operator be self-adjoint on $L^2(\pi)$, which is the reversibility of the chain, is *Reversible Markov Chains and Time Reversal* and the computation of the adjoint itself is *The Adjoint of the Markov Operator*, both later in this category; the continuous-time semigroup and its generator are *The Transition Operator*, next in this category; the general Cesàro averaging of a unitary operator is *The Ergodic Operator*, later in this category; and the shift whose orbit is the chain is *The Shift Operator of a Process*, later in this category. The general operator theory of the Hilbert space is *Banach and Hilbert Spaces*, and the measure theory is *Measure Theory and Integration*. No physics is invoked.

Throughout, $E$ is a state space, countable with the discrete $\sigma$-algebra or a Polish space with its Borel $\sigma$-algebra, and $p(x,dy)$ is a Markov kernel on $E$; the chain is $\{X_n\}_{n\ge0}$ on a probability space $(\Omega,\mathcal F,\mathbb P)$ with $\mathbb P_x$ and $\mathbb E_x$ marking the law started at $x$. The pairing of a bounded measurable function and a finite measure is $\langle f,\mu\rangle=\int_E f\,d\mu$, the sup norm is $\|f\|_\infty=\operatorname{ess\,sup}_E|f|$, the norm of a finite signed measure is the total variation $\|\mu\|_{\mathrm{TV}}=\sup\{|\langle f,\mu\rangle|:\|f\|_\infty\le1\}$, and the norm of $L^p(\pi)$ is $\|f\|_{L^p(\pi)}=(\int_E|f|^p\,d\pi)^{1/p}$ for $1\le p<\infty$.

## The Operator and Its Two Actions

### The two actions

**Definition.** The **Markov operator** of the kernel $p$ acts on bounded measurable functions by
$$
Pf(x)=\int_E f(y)\,p(x,dy)=\mathbb E_x[f(X_1)],
$$
and on finite signed measures by
$$
\mu P(B)=\int_E \mu(dx)\,p(x,B)=\mathbb P_\mu(X_1\in B).
$$

**Theorem (positivity, unitality, contractions).** The operator $P$ is positive, $f\ge0\Rightarrow Pf\ge0$; it preserves the constants, $P\mathbf 1=\mathbf 1$; it is a contraction of the sup norm, $\|Pf\|_\infty\le\|f\|_\infty$; the measure action preserves positivity, $\mu\ge0\Rightarrow\mu P\ge0$, and is a contraction of the total variation, $\|\mu P\|_{\mathrm{TV}}\le\|\mu\|_{\mathrm{TV}}$ with equality for $\mu\ge0$. In particular $P$ maps the probability measures into themselves.

*Proof.* The positivity on functions is the positivity of the kernel, and $P\mathbf 1(x)=p(x,E)=1$; the sup-norm bound is $|Pf(x)|\le\int|f|\,dp(x,\cdot)\le\|f\|_\infty$. On measures, $\mu P(B)\ge0$ is the same positivity, and $\|\mu P\|_{\mathrm{TV}}\le\|\mu\|_{\mathrm{TV}}$ follows from $\langle f,\mu P\rangle=\langle Pf,\mu\rangle$ with $\|Pf\|_\infty\le\|f\|_\infty$; for $\mu\ge0$ the mass is preserved by $P\mathbf 1=\mathbf 1$ and the norm is the mass.

### The transpose pairing and the powers

**Theorem (transpose).** The two actions are paired:
$$
\langle f,\mu P\rangle=\langle Pf,\mu\rangle,
$$
so the measure action is the transpose of the function action. It is not the Hilbert adjoint: the adjoint of $P$ with respect to an invariant measure $\pi$ is computed in *The Adjoint of the Markov Operator*, later in this category, and it is a different operator whenever the chain is not reversible.

**Theorem (Chapman–Kolmogorov).** For all $m,n\ge0$,
$$
P^{m+n}=P^mP^n,\qquad P^nf(x)=\mathbb E_x[f(X_n)],\qquad \mu P^n(B)=\mathbb P_\mu(X_n\in B).
$$
The powers $\{P^n\}$ are the discrete semigroup of the chain, and the identity is the semigroup law of the transition operator in discrete time.

*Proof.* The measure-preserving form of the Chapman–Kolmogorov equations of *Markov Chains and Processes* is $p^{(m+n)}(x,B)=\int_E p^{(m)}(y,B)\,p^{(n)}(x,dy)$; reading it as the composition of the two actions gives $P^{m+n}=P^mP^n$, and the probabilistic display is the iteration.

### The action on $L^p(\pi)$

**Theorem (contractivity on $L^p$).** Let $\pi$ be an invariant probability measure. Then $P$ acts on $L^p(\pi)$ for every $1\le p\le\infty$ and
$$
\|Pf\|_{L^p(\pi)}\le\|f\|_{L^p(\pi)},\qquad P\mathbf 1=\mathbf 1 ,
$$
so $P$ is a contraction of every $L^p(\pi)$ that fixes the constants.

*Proof.* For finite $p$ the bound is Jensen's inequality applied to the conditional expectation $Pf(x)=\mathbb E[f(X_1)\mid X_0=x]$ and the invariance of $\pi$, which makes $P$ the conditional expectation of $f(X_1)$ on the initial state; for $p=\infty$ it is the sup-norm bound. The preservation of the constants is the unitality.

The $L^2(\pi)$ case is the one used below: with respect to $\langle f,g\rangle_\pi=\int f\bar g\,d\pi$ the operator $P$ is a contraction, and it is self-adjoint exactly when the chain is reversible.

## Invariant Measures

### Invariance

**Definition.** A probability measure $\pi$ is **invariant** (or stationary) for the chain if $\pi P=\pi$, that is $\langle Pf,\pi\rangle=\langle f,\pi\rangle$ for every bounded $f$. Equivalently $\pi$ is a fixed vector of the action on measures, and $\pi$ is the law of a strictly stationary sequence under the chain.

**Theorem (the fixed points on measures).** The invariant probability measures of $P$ form a convex set, closed in the weak topology, and it is nonempty when $E$ is compact; the ergodic invariant measures are exactly its extreme points. If the chain is irreducible and positive recurrent there is exactly one, and $\pi(x)=1/\mathbb E_x[\tau_x^+]$ in the countable case.

*Proof.* The set is convex because the action is affine, and closed by the continuity of $\mu\mapsto\mu P$ in the weak topology; the existence for compact $E$ is the Krylov–Bogoliubov argument. The uniqueness and the formula for $\pi(x)$ are the existence theorem of *Markov Chains and Processes*; the identification of the extreme points with the ergodic measures is the ergodic decomposition of *Ergodic Theory*.

### The fixed space and the harmonic functions

**Definition.** A bounded measurable $h$ is **harmonic** for $P$ if $Ph=h$. The fixed space of the action on functions is the space of the bounded harmonic functions, and a bounded harmonic function produces a martingale $h(X_n)$ along the chain, by $Ph=h$ and the Markov property.

**Theorem (Liouville).** If the chain is irreducible positive recurrent with invariant measure $\pi$, then every bounded harmonic function is constant $\pi$-almost surely; the fixed space of $P$ in $L^\infty(\pi)$ is spanned by $\mathbf 1$.

*Proof.* The martingale $h(X_n)$ of *Martingales* is bounded, hence almost surely convergent, and its limit is measurable with respect to the tail $\sigma$-algebra; on an irreducible chain the limit is invariant under the transition, so $h$ is constant on the communicating class and equal to its $\pi$-average. The $L^\infty$ identification follows.

## Ergodicity and the Mean Ergodic Theorem

### The ergodicity criterion

**Definition.** The invariant measure $\pi$ is **ergodic** if every measurable set $A$ with $P\mathbf 1_A=\mathbf 1_A$ $\pi$-a.e. satisfies $\pi(A)\in\{0,1\}$.

**Theorem (equivalent forms).** Let $\pi$ be invariant. The following are equivalent:

1. $\pi$ is ergodic;
2. the fixed space $\ker(P-I)$ in $L^2(\pi)$ is one-dimensional, spanned by $\mathbf 1$;
3. every bounded harmonic function is constant $\pi$-a.e.;
4. the invariant $\sigma$-algebra of the chain is $\pi$-trivial.

*Proof.* The equivalences are the standard chain statements of *Markov Chains and Processes*, read through the operator: an invariant set is a $\{0,1\}$-valued harmonic function and conversely the indicator of an invariant set spans a fixed direction; a fixed $f$ in $L^2$ has $\{f>c\}$ invariant; the fixed space is spanned by the invariant bounded functions, and the invariant $\sigma$-algebra is generated by them.

### The mean ergodic theorem

**Theorem (mean ergodic theorem for the Markov operator).** Let $\pi$ be invariant and ergodic and let $\Pi$ be the orthogonal projection of $L^2(\pi)$ onto the constants, $\Pi f=\int_E f\,d\pi\,\mathbf 1$. Then for every $f\in L^2(\pi)$,
$$
\frac1n\sum_{k=0}^{n-1}P^kf\longrightarrow \Pi f\qquad \text{in } L^2(\pi),
$$
and the convergence is dominated by $\|f\|_{L^2(\pi)}$.

*Proof.* The operator $P$ is a contraction of $L^2(\pi)$ with fixed space the constants, and the Cesàro averages of the powers of a contraction converge in the strong operator topology to the orthogonal projection onto the fixed space; this is the von Neumann ergodic theorem applied to $P$, proved in *The Ergodic Operator*, later in this category, where the general operator statement is given. The identification of the limit with the constant of the mean is the ergodicity criterion, and the domination is the contractivity.

**Corollary (the occupation measure).** Under the same hypothesis, for every bounded $f$ and every initial distribution,
$$
\frac1n\sum_{k=0}^{n-1}f(X_k)\longrightarrow \int_E f\,d\pi\qquad \mathbb P\text{-a.s.},
$$
which is the ergodic theorem of the chain; the almost-sure form is the Birkhoff theorem of *Ergodic Theory* applied to the shift, and the present theorem is its $L^2$ mean form.

## The Spectrum and the Rate of Convergence

### The spectral radius

**Theorem (spectrum).** Let the chain have an invariant probability $\pi$ and let $P$ act on $L^2(\pi)$. Then the spectrum is contained in the closed unit disc,
$$
\sigma(P)\subseteq\{z\in\mathbb C:|z|\le1\},\qquad 1\in\sigma(P),
$$
and $1$ is an eigenvalue with eigenvector $\mathbf 1$. If the chain is aperiodic and ergodic, $1$ is the only eigenvalue of modulus one.

*Proof.* The inclusion is $\|P\|_{L^2(\pi)}\le1$ for the contraction; $P\mathbf 1=\mathbf 1$ gives the eigenvalue and $1\in\sigma(P)$. The eigenvalue of modulus one that is not $1$ would give a periodic invariant function, excluded by aperiodicity and ergodicity; the statement is the classical one for the transition matrix and the kernel.

**Theorem (Perron–Frobenius).** For a finite irreducible chain the eigenvalue $1$ is simple, and the corresponding left and right eigenvectors are strictly positive; the spectral radius is $1$. For irreducible and aperiodic, all other eigenvalues have modulus strictly less than $1$.

*Proof.* This is the Perron–Frobenius theorem applied to the nonnegative irreducible matrix $P$, whose spectral radius is $1$ because $P$ is stochastic; the strict inequality is the primitivity of $P$ in the aperiodic case.

### The spectral gap

**Definition.** For a finite irreducible aperiodic chain with invariant measure $\pi$, the **spectral gap** is
$$
\gamma=1-\sup\{|z|:z\in\sigma(P),\ z\ne1\},
$$
a positive number by the theorem above.

**Theorem (mixing rate).** The total variation distance to stationarity is bounded by
$$
\|\mathbb P_\mu(X_n\in\cdot)-\pi(\cdot)\|_{\mathrm{TV}}\le\frac12\Bigl(\max_x\frac{\mu(x)}{\pi(x)}\Bigr)^{1/2}(1-\gamma)^n,
$$
so the chain mixes at the geometric rate of the spectral gap.

*Proof.* The inequality is the standard spectral bound for a finite chain, obtained by expanding the initial distribution in the eigenbasis of $P$ on $L^2(\pi)$; the sharp theory is *Markov Chains and Processes*, and the reversibility case, where the spectrum is real, is *Reversible Markov Chains and Time Reversal*, later in this category.

## Worked Examples

**Example (a two-state chain).** Let $E=\{0,1\}$ and $P=\begin{pmatrix}1-a&a\\b&1-b\end{pmatrix}$ with $a,b\in(0,1)$. The invariant measure is $\pi=(b/(a+b),\,a/(a+b))$, the eigenvalues are $1$ and $1-a-b$, and the spectral gap is $a+b$. For $a=b=1$ the chain is the deterministic flip, with eigenvalues $1$ and $-1$; it is periodic and its gap is $0$, which is the degenerate case excluded by aperiodicity.

**Example (the random walk on a finite cycle).** Let $E=\mathbb Z_n$ and $p(x,x\pm1)=\frac12$. The operator is $Pf(x)=\frac12(f(x+1)+f(x-1))$, with the characters $e^{2\pi ikx/n}$ as eigenfunctions and eigenvalues $\cos(2\pi k/n)$; the invariant measure is uniform and the spectral gap is $1-\cos(2\pi/n)$. This is the finite model of the Laplacian on the circle, whose spectral theory is that of the heat semigroup in *The Transition Operator*, next in this category.

**Example (the independent chain).** Let $p(x,\cdot)=\pi$ for a fixed probability $\pi$, independently of $x$. Then $Pf(x)=\int f\,d\pi$, the operator is the rank-one projection $\Pi$ onto the constants, $P^2=P$, and the chain is ergodic and mixes in one step; every bounded harmonic function is constant because the kernel has one-dimensional range.

**Example (a reducible chain).** Let $E=\{0,1\}$ with $p(0,0)=p(1,1)=1$. Then $P=\mathrm{id}$, every invariant probability is a fixed vector and the fixed space of the function action is all of $L^2$; the invariant measures form the whole interval of probabilities, the extreme points are the two point masses, and the chain is not ergodic. This is the degenerate case of the ergodicity criterion: the fixed space is as large as possible.

## Failure of the Degenerate Cases

The operator structure degenerates in four configurations, and they are collected because they are the boundary of the statements above. First, the invariant measure need not be unique: on a reducible chain the set of invariant probabilities has as many extreme points as there are recurrent classes, and the mean ergodic limit is the average along the class that carries the initial law rather than a single constant. Second, the invariant probability need not exist: a null recurrent or a transient chain has none, and the operator then has no invariant state on which the $L^2(\pi)$ theory rests, although it still contracts $L^\infty$. Third, the operator need not be self-adjoint on any $L^2(\pi)$: the spectrum is a general subset of the disc, the eigenvalues may be complex, and the spectral gap must be replaced by the second singular value; self-adjointness is exactly reversibility and is treated later in this category. Fourth, on a noncompact state space the weak compactness of the set of invariant probabilities fails, and the Krylov–Bogoliubov argument requires a tightness or a Lyapunov condition; the statement of the existence theorem is accordingly conditional.

## Summary

The Markov operator of a kernel $p$ acts on bounded functions by $Pf(x)=\int f\,dp(x,\cdot)$ and on finite measures by $\mu P(B)=\int\mu(dx)p(x,B)$, the two actions being paired by $\langle f,\mu P\rangle=\langle Pf,\mu\rangle$ and composed by the Chapman–Kolmogorov law $P^{m+n}=P^mP^n$. It is positive, unital and a contraction of the sup norm on the functions and of the total variation on the measures; if $\pi$ is invariant it is a contraction of every $L^p(\pi)$ fixing the constants. The invariant probabilities are the fixed vectors of the measure action and form a convex weakly compact set whose extreme points are the ergodic measures, unique when the chain is irreducible positive recurrent; the fixed vectors of the function action are the bounded harmonic functions, which are constant for an ergodic chain, and they produce the martingales $h(X_n)$. Ergodicity of $\pi$ is the one-dimensionality of the fixed space in $L^2(\pi)$, and the mean ergodic theorem states that the Cesàro averages of the powers converge in $L^2(\pi)$ to the projection onto the constants, with the occupation measure as the almost-sure corollary. The spectrum lies in the closed unit disc with $1$ an eigenvalue, simple for a finite irreducible chain by Perron–Frobenius and the only eigenvalue of modulus one in the aperiodic ergodic case, and the spectral gap bounds the geometric rate of convergence to stationarity. The adjoint is *The Adjoint of the Markov Operator*, the semigroup and the generator are *The Transition Operator*, the general mean ergodic theorem is *The Ergodic Operator*, and the shift is *The Shift Operator of a Process*, all later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$, $p(x,dy)$, $p_{xy}$ | state space, Markov kernel, transition matrix |
| $X_n$, $\mathbb P_x$, $\mathbb E_x$ | the chain, and its law and expectation started at $x$ |
| $Pf(x)=\int f\,dp(x,\cdot)$ | Markov operator on functions |
| $\mu P(B)=\int\mu(dx)p(x,B)$ | the action on measures |
| $\langle f,\mu\rangle=\int f\,d\mu$ | pairing of a function and a measure |
| $\|f\|_\infty$, $\|\mu\|_{\mathrm{TV}}$, $\|f\|_{L^p(\pi)}$ | sup norm, total variation, $L^p(\pi)$ norm |
| $P^{m+n}=P^mP^n$ | Chapman–Kolmogorov for the operator |
| $\pi P=\pi$ | invariant measure |
| $Ph=h$, $h(X_n)$ | harmonic function and its martingale |
| $\Pi f=\int f\,d\pi$ | projection onto the constants in $L^2(\pi)$ |
| $\frac1n\sum_{k<n}P^k\to\Pi$ | mean ergodic theorem |
| $\sigma(P)$, $\gamma$ | spectrum and spectral gap |
| $\tau_x^+$ | first return time, $\pi(x)=1/\mathbb E_x[\tau_x^+]$ |

## Further Reading

- J. R. Norris, *Markov Chains* (Cambridge University Press, 1997), for the transition operator, the invariant measure and the ergodic theorem for chains.
- David A. Levin, Yuval Peres and Elizabeth L. Wilmer, *Markov Chains and Mixing Times* (American Mathematical Society, 2nd edition, 2017), for the $L^2(\pi)$ contraction, the spectral gap and the mixing rate.
- Kai Lai Chung, *Markov Chains with Stationary Transition Probabilities* (Springer, 2nd edition, 1967), for the classical operator treatment of recurrence and stationarity.
- Daniel W. Stroock, *An Introduction to Markov Processes* (Springer, 2nd edition, 2014), for the positive operators and the invariant measures on a general state space.
- Einar Hille and Ralph Phillips, *Functional Analysis and Semi-Groups* (American Mathematical Society, 1957), for the semigroup of the powers and the contractions of $L^p$.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the contractions, the fixed spaces and the mean ergodic theorem.
