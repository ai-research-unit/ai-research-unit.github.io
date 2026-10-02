
# __Reversible Markov Chains and Time Reversal__

## Introduction

A Markov chain is **reversible** when the statistics of the chain read backwards in the index are the statistics read forwards, and the precise form of that statement is the **detailed balance** identity
$$
\pi(x)\,p(x,y)=\pi(y)\,p(y,x)\qquad (x,y\in E),
$$
for a stationary measure $\pi$. The operation of reading the chain backwards is the **time reversal**, the involution $r$ of the path space that sends a path $\{x_n\}$ to the path $\{x_{-n}\}$, and reversibility is the invariance of the law of the stationary chain under that involution. The article develops the two faces of the reversibility: the **element-level** statement, that the involution $r$ preserves the law of the chain, and the **operator-level** statement, that the Markov operator is self-adjoint on $L^2(\pi)$. It defines the reversed chain, proves that detailed balance and self-adjointness are equivalent, records the consequences — real spectrum, orthogonal eigenfunctions, the Dirichlet form and the variational formula for the spectral gap — and illustrates them on the reversible random walks, the birth–death chains and the two-state chain, with a non-reversible cycle as the contrasting example.

The chain theory is fixed elsewhere. The Markov chain, its transition kernel, its paths and its stationarity are *Markov Chains and Processes*, written; the Markov operator, its invariant measures and its ergodicity are *The Markov Operator*, earlier in this category; the computation of the adjoint operator is *The Adjoint of the Markov Operator*, later in this category, and the reversal of a stationary process at the level of its law is *The Reversibility of a Stationary Process*, next in this category; the spectral theorem for self-adjoint operators and the orthogonal decompositions are *Banach and Hilbert Spaces*, written; the ergodicity and the mixing of the chain are *Ergodic Theory*, written. The involution on the elements of the algebra of random variables is *The Involution on the Algebra of Random Variables*, later in this category. No physics is invoked; the word time names the index of the chain and nothing else.

Throughout, $E$ is a countable set or a standard Borel space, $p(x,dy)$ is the transition kernel, $\pi$ is a stationary probability measure, and the chain is $\{X_n\}$. The invariance is $\pi P=\pi$ in the notation of *The Markov Operator*. The Hilbert space is $L^2(\pi)$ with the inner product $\langle f,g\rangle_\pi=\int f\bar g\,d\pi$, and the path space is $E^{\mathbb Z}$ with the shift $\sigma$ and the reversal $r$, $(r\omega)_n=\omega_{-n}$.

## Detailed Balance and the Reversed Chain

### Detailed balance

**Definition.** The chain is **reversible** with respect to the stationary measure $\pi$ if the **detailed balance** identity holds,
$$
\pi(x)\,p(x,y)=\pi(y)\,p(y,x)
$$
for all $x,y$; equivalently, the measure $\pi(x)p(x,dy)$ on $E\times E$ is symmetric under the interchange of the two coordinates.

**Theorem (detailed balance implies stationarity).** If $\pi$ satisfies detailed balance then it is stationary, $\pi P=\pi$.

*Proof.* Summing the balance identity over $x$ gives $\sum_x\pi(x)p(x,y)=\sum_x\pi(y)p(y,x)=\pi(y)$, which is $\pi P=\pi$.

**Proposition (the reversed chain).** Let $\pi$ be stationary and define
$$
\hat p(x,y)=\frac{\pi(y)\,p(y,x)}{\pi(x)},
$$
with $\hat p(x,y)=0$ or arbitrary on the $\pi$-null set where $\pi(x)=0$. Then $\hat p$ is a Markov kernel and $\pi$ is stationary for it; it is called the **reversed chain** of $p$ with respect to $\pi$. The chain is reversible if and only if $\hat p=p$ as kernels on the support of $\pi$.

*Proof.* The positivity is clear, and $\sum_y\hat p(x,y)=\sum_y\pi(y)p(y,x)/\pi(x)=(\pi P)(x)/\pi(x)=1$ by the stationarity; the reversed chain's stationarity is the symmetry of the definition, and its equality with $p$ is the detailed balance identity rearranged.

### The reversal of the path space

**Definition.** The **time reversal** is the involution of the path space
$$
r:E^{\mathbb Z}\to E^{\mathbb Z},\qquad (r\omega)_n=\omega_{-n},
$$
with $r^2=\mathrm{id}$ and $r\circ\sigma=\sigma^{-1}\circ r$.

**Theorem (reversibility as the invariance of the law).** Let $\mathbb P_\pi$ be the law of the stationary chain on $E^{\mathbb Z}$. Then the chain is reversible if and only if
$$
\mathbb P_\pi\circ r^{-1}=\mathbb P_\pi ,
$$
that is, if and only if the law of the chain is invariant under the time reversal. For the reversed chain $\hat p$, the law of the chain running backwards under $p$ is the law of the chain running forwards under $\hat p$.

*Proof.* The finite-dimensional distributions of $r$-transformed path are the reversed-time distributions of the original chain; the reversed chain $\hat p$ is exactly the chain whose forward distributions are those, as the definition of $\hat p$ shows by induction on the length of the window. The equality of the two laws is therefore the equality of the forward distributions of $p$ and $\hat p$, which is $p=\hat p$.

## Self-Adjointness and the Spectrum

### The operator criterion

**Theorem (reversibility is self-adjointness).** The chain is reversible with respect to $\pi$ if and only if its Markov operator is self-adjoint on $L^2(\pi)$:
$$
\langle Pf,g\rangle_\pi=\langle f,Pg\rangle_\pi\qquad\text{for all }f,g\in L^2(\pi).
$$

*Proof.* The two pairings are $\langle Pf,g\rangle_\pi=\sum_{x,y}\pi(x)p(x,y)f(y)\bar g(x)$ and $\langle f,Pg\rangle_\pi=\sum_{x,y}\pi(x)p(x,y)f(x)\bar g(y)$. They are equal for all $f,g$ exactly when $\pi(y)p(y,x)=\pi(x)p(x,y)$ for all $x,y$, which is detailed balance; the passage between the two displays is a relabelling of the summation.

**Corollary (the adjoint is the reversed chain).** For a general stationary chain, the adjoint $P^*$ on $L^2(\pi)$ is the Markov operator of the reversed chain $\hat p$; the chain is reversible exactly when $P^*=P$. The computation of the adjoint is *The Adjoint of the Markov Operator*, later in this category.

*Proof.* The adjoint is characterised by $\langle f,P^*g\rangle_\pi=\langle Pf,g\rangle_\pi$ for all $f,g$, and the kernel $\hat p$ satisfies the resulting identity by the same relabelling as in the theorem.

### The real spectrum

**Theorem (spectral consequences).** Let the chain be reversible with stationary measure $\pi$. Then the Markov operator on $L^2(\pi)$ is self-adjoint and a contraction, its eigenvalues are real and lie in $[-1,1]$, its eigenfunctions belonging to distinct eigenvalues are orthogonal in $L^2(\pi)$, and the operator has an orthonormal basis of eigenfunctions when $E$ is finite. For an ergodic chain the eigenvalue $1$ is simple with eigenvector the constant function, and in the ergodic aperiodic case it is the only eigenvalue of modulus one.

*Proof.* Self-adjointness is the theorem, and the spectral theorem for a self-adjoint operator of norm at most one gives the rest; the Perron–Frobenius statement for the eigenvalue one is *The Markov Operator*, earlier in this category, and the uniqueness of the eigenvalue of modulus one is its aperiodic conclusion.

**Corollary (the second eigenvalue).** For a finite connected reversible chain the spectrum ordered decreasingly is $\{1=\lambda_1>\lambda_2\ge\cdots\ge\lambda_{|E|}\ge-1\}$, the second eigenvalue $\lambda_2$ is real, and the relaxation to the stationary measure is governed by $\lambda_2$ together with the smallest eigenvalue when it is negative.

*Proof.* The ordering and the realness are the theorem; the convergence rate is the spectral expansion of the transition matrix.

## The Dirichlet Form and the Gap

### The Dirichlet form

**Definition.** For a reversible chain with stationary measure $\pi$ the **Dirichlet form** is
$$
\mathcal{E}(f,g)=\langle(I-P)f,g\rangle_\pi .
$$

**Theorem (the sum form).** For a reversible chain,
$$
\mathcal{E}(f,g)=\frac12\sum_{x,y}\pi(x)\,p(x,y)\,\bigl(f(x)-f(y)\bigr)\bigl(\overline{g(x)-g(y)}\bigr),
$$
and $\mathcal{E}(f,f)\ge0$ with equality exactly when $f$ is constant.

*Proof.* Expanding the right side gives $\langle f,g\rangle_\pi-\langle Pf,g\rangle_\pi$ when $P$ is self-adjoint, by the relabelling used in the self-adjointness theorem; the positivity is the square $\frac12\sum\pi(x)p(x,y)|f(x)-f(y)|^2\ge0$, and its vanishing is the constancy of $f$ on the classes of positive transition probability, that is on the connected components.

### The variational formula for the gap

**Theorem (the Poincaré inequality).** For a finite connected reversible chain with stationary measure $\pi$, the **spectral gap** $\gamma=1-\lambda_2$ is
$$
\gamma=\inf\Bigl\{\frac{\mathcal{E}(f,f)}{\operatorname{Var}_\pi(f)}:f\text{ non-constant}\Bigr\},
$$
where $\operatorname{Var}_\pi(f)=\|f-\int f\,d\pi\|_{L^2(\pi)}^2$, and the infimum is attained at the eigenfunction of $\lambda_2$.

*Proof.* In the orthonormal basis of the eigenfunctions the quotient is a weighted average of the eigenvalues $1-\lambda_k$, so its infimum over the non-constant functions is the smallest of these, $1-\lambda_2$; the Dirichlet form is the quadratic form of $I-P$ and the variance is the squared norm on the orthogonal complement of the constants.

## Worked Examples

**Example (the reversible random walk on a graph).** Let $G$ be a connected graph with conductances $w_{xy}=w_{yx}>0$ and $w_x=\sum_yw_{xy}$. The random walk with $p(x,y)=w_{xy}/w_x$ is reversible with respect to $\pi(x)=w_x/W$, since $\pi(x)p(x,y)=w_{xy}/W=\pi(y)p(y,x)$. The Dirichlet form is $\mathcal{E}(f,g)=\frac{1}{2W}\sum_{x,y}w_{xy}(f(x)-f(y))(\overline{g(x)-g(y)})$ and the spectral gap is the Poincaré constant of the weighted graph.

**Example (the birth–death chain).** On $E=\{0,1,2,\dots\}$ with $p(n,n+1)=b_n$, $p(n,n-1)=a_n$ and $p(n,n)=1-a_n-b_n$, the measure $\pi(n)=\pi(0)\prod_{k<n}b_k/a_{k+1}$ satisfies detailed balance, so every birth–death chain with a stationary measure is reversible. The two-state chain is the case $E=\{0,1\}$ and is reversible for every choice of $a,b$.

**Example (the two-state chain).** With $p(0,1)=a$ and $p(1,0)=b$ one has $\pi=(b/(a+b),a/(a+b))$ and $\pi(0)a=\pi(1)b=ab/(a+b)$; the chain is reversible for all $a,b$, its Markov operator on $L^2(\pi)$ is the symmetric matrix with eigenvalues $1$ and $1-a-b$, and the spectral gap is $a+b$.

**Example (a non-reversible cycle).** On $E=\{1,2,3\}$ let $p(i,i+1)=1$ cyclically. The uniform measure is stationary, but $\pi(1)p(1,2)=\frac13$ while $\pi(2)p(2,1)=0$, so the chain is not reversible; the reversed chain runs around the cycle backwards, the Markov operator is the cyclic permutation matrix with the complex eigenvalues $1,e^{\pm2\pi i/3}$, and the spectrum is not real.

**Example (the Ornstein–Uhlenbeck chain).** The diffusion with generator $\frac{\sigma^2}{2}\partial_x^2-\theta x\partial_x$ and invariant law $N(0,\sigma^2/(2\theta))$ is reversible, its generator is self-adjoint on $L^2$ of the normal law, and its spectrum is the arithmetic set $\{-n\theta\}$ of the Hermite operator; the reversibility is the symmetry of the Gaussian kernel.

## Failure of the Degenerate Cases

Reversibility degenerates in four configurations. First, a stationary measure need not satisfy detailed balance: on a finite irreducible chain the stationarity is the unique positive harmonic vector of the transpose, while the detailed balance is the symmetry of the kernel, a strictly stronger condition, and it fails as soon as the chain has a net circulation, the cycle above being the minimal example. Second, the stationary measure need not be unique, and the reversal is defined with respect to one chosen measure; on a reducible chain each ergodic measure gives its own reversed chain. Third, the reversed chain can coincide with the original even when the chain is not reversible in the strong sense on a larger state space, when the support of $\pi$ omits the states that break the balance. Fourth, self-adjointness fails for the general stationary chain, the spectrum is then a general subset of the disc, and the Dirichlet form loses its positivity; the sum form of the Dirichlet form and the variational formula for the gap are available exactly in the reversible case, and the non-reversible theory needs the singular values in place of the eigenvalues.

## Summary

A Markov chain with a stationary measure $\pi$ is reversible when the detailed balance identity $\pi(x)p(x,y)=\pi(y)p(y,x)$ holds, equivalently when the measure $\pi(x)p(x,dy)$ on the product is symmetric, equivalently when the law of the stationary chain is invariant under the time reversal $r$ of the path space, equivalently when the Markov operator is self-adjoint on $L^2(\pi)$. The reversed chain is the kernel $\hat p(x,y)=\pi(y)p(y,x)/\pi(x)$, its forward law is the backward law of the original, and reversibility is $\hat p=p$. On a finite connected reversible chain the spectrum is real, lies in $[-1,1]$, the eigenfunctions are orthogonal, the eigenvalue one is simple, and the spectral gap is given by the variational formula $\gamma=\inf\mathcal{E}(f,f)/\operatorname{Var}_\pi(f)$ of the Dirichlet form $\mathcal{E}(f,g)=\langle(I-P)f,g\rangle_\pi=\frac12\sum\pi(x)p(x,y)(f(x)-f(y))(\overline{g(x)-g(y)})$. The reversible random walks, the birth–death chains and the Gaussian diffusions are the standard examples, and the directed cycle is the standard nonreversible one. The adjoint operator is *The Adjoint of the Markov Operator*, later in this category, and the reversal at the level of the law of a process is the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi(x)p(x,y)=\pi(y)p(y,x)$ | detailed balance |
| $\hat p(x,y)=\pi(y)p(y,x)/\pi(x)$ | the reversed chain |
| $r$, $(r\omega)_n=\omega_{-n}$ | the time reversal of the path space |
| $r\sigma=\sigma^{-1}r$ | the reversal intertwines the shift with its inverse |
| $\langle Pf,g\rangle_\pi=\langle f,Pg\rangle_\pi$ | self-adjointness on $L^2(\pi)$ |
| $\lambda_2$, $\gamma=1-\lambda_2$ | second eigenvalue, spectral gap |
| $\mathcal{E}(f,g)=\langle(I-P)f,g\rangle_\pi$ | the Dirichlet form |
| $\operatorname{Var}_\pi(f)$ | variance with respect to $\pi$ |

## Further Reading

- J. R. Norris, *Markov Chains* (Cambridge University Press, 1997), for the reversible chains, the detailed balance and the reversed chain.
- David A. Levin, Yuval Peres and Elizabeth L. Wilmer, *Markov Chains and Mixing Times* (American Mathematical Society, 2nd edition, 2017), for the Dirichlet forms, the spectral gap and the Poincaré inequality.
- Persi Diaconis and Daniel Stroock, "Geometric bounds for eigenvalues of Markov chains", *The Annals of Applied Probability* 1 (1991), 36–61, for the variational characterisation of the gap.
- Martin L. Silverstein, *Symmetric Markov Processes* (Springer, 1974), for the Dirichlet forms of the symmetric semigroups.
- David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs* (monograph, 2002), for the reversal, the conductances and the spectral theory.
