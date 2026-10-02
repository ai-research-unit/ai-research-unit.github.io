
# __The Transition Operator__

## Introduction

A Markov process is described by its transition operator, the family $\{P_t\}_{t\ge0}$ whose element $P_t$ sends the state at one moment to the law of the state $t$ units later: on functions $P_tf(x)=\mathbb E_x[f(X_t)]$ and on measures $\mu P_t(B)=\mathbb P_\mu(X_t\in B)$. The family carries the structure of a semigroup, $P_0=I$ and $P_{s+t}=P_sP_t$, and the semigroup is the whole process; the local description of the process is its **generator**, the operator $L=\lim_{t\to0}(P_t-I)/t$, and the passage between the two is the content of this article. The generator is the derivative of the semigroup at the origin, the semigroup is recovered from the generator by $P_t=e^{tL}$ where the exponential is defined, and the resolvent $(\lambda-L)^{-1}$ is the Laplace transform of the semigroup. The article states the semigroup law, the Feller regularity that makes the theory work, the definition and the maximal domain of the generator, the resolvent identity, the Hille–Yosida characterisation, the Kolmogorov forward and backward equations, and the examples that fix the meaning: the Poisson process, whose generator is a difference operator, and the Brownian motion, whose generator is one half of the Laplacian.

The chain theory is fixed elsewhere. The discrete semigroup $\{P^n\}$ and the Markov operator $P=P_1$ of a chain are *The Markov Operator*, the preceding article of this category, and the semigroup statements there are the case of integer times; the transition semigroup, its generator, the Kolmogorov equations, the Hille–Yosida theorem and the martingale problem are *Markov Chains and Processes*, written, and are quoted here rather than proved; the heat semigroup, the Brownian motion and its generator $\frac12\Delta$ are *Brownian Motion and Stochastic Calculus*, written; the semigroups of operators on a Banach space and the $C_0$ theory are *Operator Algebras*; the spectral theory used in the examples is *Banach and Hilbert Spaces*; the invariant measures and the ergodicity of the semigroup are *Ergodic Theory*; and the adjoint semigroup and the time reversal are *The Adjoint of the Transition Operator*, later in this category. No physics is invoked.

Throughout, $E$ is a Polish space with its Borel $\sigma$-algebra, $\{X_t\}_{t\ge0}$ is a Markov process on $(\Omega,\mathcal F,\mathbb P)$ with $\mathbb P_x$ and $\mathbb E_x$ marking the law started at $x$, and $p_t(x,B)=\mathbb P_x(X_t\in B)$ is the transition kernel. The pairing is $\langle f,\mu\rangle=\int_E f\,d\mu$, the sup norm is $\|f\|_\infty$, the total variation is $\|\mu\|_{\mathrm{TV}}$, and $C_0(E)$ is the Banach space of continuous functions vanishing at infinity with the sup norm. The generator is written $L$ and its domain $\mathcal D(L)$; the resolvent is $R_\lambda=(\lambda-L)^{-1}$.

## The Transition Semigroup

### Definition and the semigroup law

**Definition.** A **transition operator** (or transition semigroup) on $E$ is a family $\{P_t\}_{t\ge0}$ of Markov kernels, acting on bounded measurable functions by
$$
P_tf(x)=\int_E f(y)\,p_t(x,dy)=\mathbb E_x[f(X_t)],
$$
and on finite measures by $\mu P_t(B)=\int_E\mu(dx)\,p_t(x,B)$, such that
$$
P_0=I,\qquad P_{s+t}=P_sP_t\quad(s,t\ge0).
$$

**Theorem (basic properties).** Each $P_t$ is positive, unital and a contraction of the sup norm, and its measure action preserves the probability measures; the map $t\mapsto P_tf$ is measurable for every bounded measurable $f$; and the discrete semigroup is the case $P_n=P^n$ of *The Markov Operator*, the preceding article.

*Proof.* The positivity, the unitality and the sup-norm bound are the properties of a Markov kernel; the semigroup law is the Chapman–Kolmogorov identity for the transition kernels; the measurability is the measurability of $(t,x)\mapsto p_t(x,B)$.

### The Feller property and the action on $C_0(E)$

**Definition.** The semigroup is a **Feller semigroup** if each $P_t$ maps $C_0(E)$ into itself and $P_tf\to f$ uniformly as $t\to0$ for every $f\in C_0(E)$.

The Feller property is the regularity hypothesis under which the generator has the Hille–Yosida characterisation below; it is automatic for the transition semigroup of a random walk on a locally compact group, whose kernels are translates of one another, and it holds for the diffusions whose coefficients are continuous. On the Banach space $C_0(E)$ the Feller semigroup is a strongly continuous contraction semigroup, and the general theory of such semigroups is the subject of *Operator Algebras*.

## The Generator

### Definition and the domain

**Definition.** The **generator** of the transition semigroup is
$$
Lf=\lim_{t\to0}\frac{P_tf-f}{t},
$$
with domain $\mathcal D(L)$ the set of $f\in C_0(E)$ for which the limit exists uniformly.

**Theorem (the generator is closed and densely defined).** For a Feller semigroup, $\mathcal D(L)$ is dense in $C_0(E)$, the generator is closed, and it determines the semigroup: two Feller semigroups with the same generator coincide on $C_0(E)$.

*Proof.* The density and the closedness are the standard properties of the generator of a strongly continuous contraction semigroup; the uniqueness is the Hille–Yosida theorem below. The statements are *Markov Chains and Processes*.

### The resolvent

**Definition.** For $\lambda>0$ the **resolvent** of the semigroup is the bounded operator
$$
R_\lambda f=\int_0^\infty e^{-\lambda t}P_tf\,dt .
$$

**Theorem (resolvent identity).** For $\lambda,\mu>0$,
$$
R_\lambda-R_\mu=(\mu-\lambda)R_\lambda R_\mu,\qquad (\lambda-L)R_\lambda=\mathrm{id},\qquad R_\lambda(\lambda-L)=\mathrm{id}\ \text{on }\mathcal D(L),
$$
and $R_\lambda f$ is the unique solution of $\lambda u-Lu=f$.

*Proof.* The resolvent identity is the algebra of $\int_0^\infty e^{-\lambda t}P_t\,dt$ with the semigroup law, and the two identities are the integration by parts of $\partial_t(P_tf)=-e^{-\lambda t}\cdot$; the uniqueness is the maximum principle for $\lambda-L$, obtained by taking the Laplace transform of the semigroup and using the contraction property. This is the classical resolvent calculus of a semigroup.

### The Hille–Yosida characterisation

**Theorem (Hille–Yosida).** A linear operator $L$ on $C_0(E)$ is the generator of a Feller semigroup if and only if its domain is dense, $L$ is dissipative, and the range of $\lambda-L$ is dense for some, equivalently every, $\lambda>0$. Equivalently, $\lambda-L$ is invertible with $\|\lambda R_\lambda\|\le1$ for every $\lambda>0$.

*Proof.* The necessity is the contraction property of the semigroup written through the resolvent; the sufficiency is the construction of the semigroup as the strong limit of the Yosida approximations $P_t=\lim_n e^{tLnR_n}$, by the exponential formula. The theorem is *Markov Chains and Processes*, and it is the functional-analytic characterisation that makes the generator an equivalent description of the process.

## The Kolmogorov Equations and the Discrete Case

### The forward and backward equations

**Theorem (Kolmogorov equations).** Let the transition semigroup be Feller with generator $L$ and let the process be non-explosive. Then for $f\in\mathcal D(L)$ the function $u(t,x)=P_tf(x)$ solves the **backward equation**
$$
\partial_tu=Lu,\qquad u(0,x)=f(x),
$$
and the transition kernels solve the **forward equation** $\partial_t p_t=p_tL$ in the weak sense. For a finite state space both reduce to $P_t=e^{tL}$, and for a general state space $P_tf=\lim_n(I-\tfrac tnL)^{-n}f$ on $\mathcal D(L)$.

*Proof.* The backward equation is the semigroup law differentiated at $t=0$ in the space variable; the forward equation is the same statement read on the measures, where the generator acts as the transpose $L^*$ on the predual. The exponential formula is the Hille–Yosida approximation.

### The $Q$-matrix of a countable chain

**Definition.** For a continuous-time chain on a countable $E$ the **generator matrix** (or $Q$-matrix) has entries
$$
q_{xy}=\lim_{t\to0}\frac{p_t(x,y)-\delta_{xy}}{t},\qquad q_{xy}\ge0\ (x\ne y),\qquad \sum_y q_{xy}=0 .
$$

**Theorem.** The $Q$-matrix acts on finitely supported functions by $Lf(x)=\sum_y q_{xy}f(y)$, and on a finite state space the semigroup is the matrix exponential $P_t=e^{tQ}$.

*Proof.* The action is the definition of $Q$ as the derivative at the origin; the matrix exponential solves $\partial_tP_t=P_tQ=QP_t$ in finite dimension, which is the two Kolmogorov equations.

## The Invariant Measures of the Semigroup

**Definition.** A probability measure $\pi$ is **invariant** for the semigroup if $\pi P_t=\pi$ for all $t\ge0$; it is **ergodic** if the only invariant sets of the semigroup have measure $0$ or $1$.

**Theorem (invariance and the generator).** Let the semigroup be Feller with generator $L$ and let $\pi$ be a probability measure with $\pi(Lf)=0$ for every $f$ in a core of $L$. Then $\pi$ is invariant. Conversely, if $\pi$ is invariant then $\pi(Lf)=0$ for $f\in\mathcal D(L)$, and $\pi$ is ergodic exactly when the fixed space of the semigroup in $L^2(\pi)$ is one-dimensional.

*Proof.* Invariance of $\pi$ means that $t\mapsto\pi(P_tf)$ is constant for every $f$, and differentiating at $t=0$ gives $\pi(Lf)=0$; conversely $\pi(Lf)=0$ on a core makes the derivative of $t\mapsto\pi(P_tf)$ vanish, and the semigroup law makes the function constant. The ergodicity statement is the semigroup form of the ergodicity criterion of *The Markov Operator*, the preceding article.

**Theorem (the reversible case).** If $\pi$ is invariant and the semigroup is **reversible**, $\langle P_tf,g\rangle_\pi=\langle f,P_tg\rangle_\pi$ for all $t$, then the generator is self-adjoint on $L^2(\pi)$ and the semigroup consists of self-adjoint contractions; the spectral gap of $L$ is the exponential rate of convergence of the semigroup to the constants.

*Proof.* Self-adjointness of the generator is the derivative of the symmetry of $P_t$ at $t=0$, and the converse is the exponential formula; the rate is the spectral theorem applied to the self-adjoint generator. The reversibility itself is *Reversible Markov Chains and Time Reversal*, later in this category.

## Worked Examples

**Example (the Poisson process).** Let $X_t$ count the arrivals of rate $\lambda>0$: the increments are independent and $X_{t+s}-X_s\sim\mathrm{Pois}(\lambda t)$. The semigroup is $P_tf(n)=\sum_{k\ge0}e^{-\lambda t}(\lambda t)^kf(n+k)/k!$, and the generator is the difference operator
$$
Lf(n)=\lambda\bigl(f(n+1)-f(n)\bigr),
$$
with domain the bounded functions; for $\mu>0$ the resolvent is
$$
R_\mu f(n)=\frac{1}{\mu+\lambda}\sum_{k\ge0}\Bigl(\frac{\lambda}{\mu+\lambda}\Bigr)^k f(n+k),
$$
and the semigroup has no invariant probability, the process drifting to infinity.

**Example (Brownian motion and the heat semigroup).** For the standard Brownian motion on $\mathbb R^d$ the semigroup is the **heat semigroup** $P_tf(x)=\int_{\mathbb R^d}(2\pi t)^{-d/2}e^{-|x-y|^2/2t}f(y)\,dy$, with the Fourier multiplier $\widehat{P_tf}(\xi)=e^{-t|\xi|^2/2}\hat f(\xi)$ and the generator
$$
L=\tfrac12\Delta,
$$
the Laplacian being *Brownian Motion and Stochastic Calculus*, written; the semigroup is self-adjoint on $L^2(\mathbb R^d)$ and has no invariant probability, since Lebesgue measure is only invariant up to the normalisation.

**Example (the Ornstein–Uhlenbeck semigroup).** For $dX_t=-\theta X_t\,dt+\sigma\,dW_t$ with $\theta,\sigma>0$ the semigroup is $P_tf(x)=\mathbb E[f(e^{-\theta t}x+\sigma\int_0^te^{-\theta(t-s)}dW_s)]$, the generator is
$$
L=\tfrac{\sigma^2}{2}\frac{d^2}{dx^2}-\theta x\frac{d}{dx},
$$
and the invariant law is the normal distribution $N(0,\sigma^2/(2\theta))$, for which the semigroup is reversible and self-adjoint with purely discrete spectrum, the Hermite eigenvalues $-n\theta$.

**Example (the birth–death chain).** For $q_{n,n+1}=b_n$, $q_{n,n-1}=a_n$ the generator is $Lf(n)=b_n(f(n+1)-f(n))+a_n(f(n-1)-f(n))$, and the invariant law $\pi(n)=\pi(0)\prod_{k<n}b_k/a_{k+1}$ exists exactly when the product converges; the simple random walk on $\mathbb Z$ is the case $a_n=b_n=\frac12$ and is null recurrent, so it has no invariant probability.

## Failure of the Degenerate Cases

The transition operator degenerates in four configurations. First, the generator may not determine the semigroup on the whole space: on a non-Feller semigroup, or on a state space where the process is explosive, the semigroup must be specified on a boundary, and the generator only controls the interior. Second, on an infinite state space the semigroup may fail to be continuous at $t=0$ in the strong operator topology unless the Feller condition is imposed, and then the generator is not densely defined. Third, $\lambda-L$ may fail to be invertible for some $\lambda>0$ when $L$ is not dissipative, which is the failure of the Hille–Yosida hypotheses; the process then has no semigroup of contractions. Fourth, the invariant probability need not exist even for a recurrent process, as the simple random walk shows, so the $L^2(\pi)$ spectral theory has no invariant state on which to rest; the reversible case, where the self-adjointness is available, is the boundary on which the spectral statements are sharpest.

## Summary

A transition semigroup is a family $\{P_t\}_{t\ge0}$ of Markov kernels with $P_0=I$ and $P_{s+t}=P_sP_t$, acting by $P_tf(x)=\mathbb E_x[f(X_t)]$ and $\mu P_t(B)=\mathbb P_\mu(X_t\in B)$; it is Feller when it preserves $C_0(E)$ and is strongly continuous at the origin, and then its generator $L=\lim_{t\to0}(P_t-I)/t$ is closed and densely defined and determines the semigroup. The resolvent $R_\lambda=\int_0^\infty e^{-\lambda t}P_t\,dt$ satisfies the resolvent identity and inverts $\lambda-L$, and the Hille–Yosida theorem characterises the generators of Feller semigroups by density, dissipativity and the range condition. The Kolmogorov backward and forward equations are the differentiated forms of the semigroup law, reducing on a finite state space to $P_t=e^{tL}$ and on a countable state space to the $Q$-matrix exponential. The invariant measures are characterised by $\pi(Lf)=0$ on a core, they are the fixed vectors of $\pi P_t=\pi$, and the reversible case is the self-adjoint one in which the spectral gap of the generator gives the exponential rate. The Poisson process, the Brownian motion with the heat semigroup and the generator $\frac12\Delta$, the Ornstein–Uhlenbeck semigroup and the birth–death chain are the standard examples; the adjoint semigroup is *The Adjoint of the Transition Operator*, later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$, $\{X_t\}$, $p_t(x,B)$ | state space, process, transition kernel |
| $P_tf(x)=\int f\,dp_t(x,\cdot)$ | transition operator on functions |
| $\mu P_t(B)=\int\mu(dx)p_t(x,B)$ | the action on measures |
| $P_0=I$, $P_{s+t}=P_sP_t$ | the semigroup law |
| $C_0(E)$, Feller | continuous functions vanishing at infinity; preservation and continuity |
| $Lf=\lim_{t\to0}(P_tf-f)/t$ | generator, domain $\mathcal D(L)$ |
| $R_\lambda=(\lambda-L)^{-1}=\int_0^\infty e^{-\lambda t}P_t\,dt$ | resolvent |
| $P_t=e^{tL}$, $\partial_tu=Lu$ | exponential formula and Kolmogorov backward equation |
| $q_{xy}$, $Q$ | generator matrix and its action on finitely supported functions |
| $\pi P_t=\pi$, $\pi(Lf)=0$ | invariant measure, its generator characterisation |
| $\widehat{P_tf}(\xi)=e^{-t|\xi|^2/2}\hat f$ | heat semigroup on $\mathbb R^d$ |
| $L=\frac12\Delta$, $L=\frac{\sigma^2}{2}\partial_x^2-\theta x\partial_x$ | Brownian and Ornstein–Uhlenbeck generators |

## Further Reading

- Daniel W. Stroock, *An Introduction to Markov Processes* (Springer, 2nd edition, 2014), for the Feller semigroups, the generator and the martingale problem.
- Stewart N. Ethier and Thomas G. Kurtz, *Markov Processes: Characterization and Convergence* (Wiley, 1986), for the Hille–Yosida theorem and the convergence of semigroups.
- Einar Hille and Ralph Phillips, *Functional Analysis and Semi-Groups* (American Mathematical Society, 1957), for the $C_0$ semigroups, the resolvent identities and the exponential formula.
- Kiyosi Itô and Henry P. McKean, *Diffusion Processes and their Sample Paths* (Springer, 1965), for the heat semigroup and the diffusions.
- Andrey N. Kolmogorov, "Über die analytischen Methoden in der Wahrscheinlichkeitsrechnung", *Mathematische Annalen* 104 (1931), 415–458, for the forward and backward equations.
- William Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II (Wiley, 1971), for the semigroups, the generators and the boundary theory.
