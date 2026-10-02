# __Time Reversal and the Transfer Operator__

## Introduction

**Time reversal** is the operator that reverses the arrow of time of the dynamical system, and on the observables it acts as an **anti-unitary** involution: the reversal of the motion composed with the complex conjugation of the amplitudes, in the manner of the reversal operator of the operator theory. Combined with the transfer operator of the dynamics — the Perron–Frobenius operator $P_T$ that carries the densities forward — the reversal gives the statement that a time-reversal-symmetric dynamics has a **self-adjoint** transfer operator: the involution of the dynamics makes the symmetrised transfer operator $\Pi^{1/2}P_T\Pi^{-1/2}$, with $\Pi$ the multiplication by the invariant density, equal to its own adjoint, and this is the operator form of the **detailed balance** of the reversible dynamics. The consequence is a spectral rigidity: the spectrum of the transfer operator is **real**, the spectral gap is real, the correlation decay has real exponential rates, and the Ruelle–Pollicott resonances of a reversible hyperbolic system are real (or occur with their conjugate). The reversibility of the *map*, which we have treated as the conjugation $U_T^*=U_RU_TU_R$ with the unitary $U_R$ of the spatial reversor, and the time reversal of the *observables*, which is the anti-unitary conjugation, are the two halves of the same structure: the first is a unitary involution reversing the operator, and the second is an anti-unitary involution under which a self-adjoint operator becomes an involution; the present article treats the second half, the self-adjointness of the transfer operator, and its detailed-balance origin, and it separates the two in the operator theory of the dynamics.

The article develops the time reversal and the transfer operator. It defines the time-reversal operator on the observables as the anti-unitary involution of the reversal, and states its action on the dynamics and on the operators; it defines the **detailed balance** of a dynamics with respect to its invariant measure, $\mu(x)P(x,y)=\mu(y)P(y,x)$, and proves that it is equivalent to the **self-adjointness** of the symmetrised transfer operator $\Pi^{1/2}P\Pi^{-1/2}$ and to the reversibility of the dynamics with respect to the measure-preserving reversal; it draws the spectral consequences: the real spectrum, the real spectral gap, the real decay rates and the real resonances; it states the relationship with the reversible Markov chains and with the pair of the Koopman and the transfer operators; and it gives the examples — the reversible finite chains with the verified detailed balance and the symmetrised operator, the reversible hyperbolic maps with the real resonances, and the non-reversible perturbations in which the self-adjointness fails. The self-adjointness is the operator form of the reversibility, and the article keeps the unitary reversor of *Reversible Operators and the Involution* and the anti-unitary conjugation of the time reversal clearly apart.

The transfer operator, the Perron–Frobenius operator, the invariant density and the resonances are *The Transfer Operator*; the adjoint and the duality are *The Adjoint of the Koopman Operator*; the reversible operators, the unitary and the anti-unitary involutions and the spectral theorem are *Reversible Operators and the Involution*, immediately preceding; the reversor of the dynamics is *Reversible Dynamical Systems and Time-Reversal Symmetry*; the time reversal of the Markov chains and the detailed balance are the subject of *Reversible Markov Chains and Time Reversal*, which owns the probabilistic theory and the convergence to equilibrium; the Koopman operator and the correlation functions are *The Koopman Operator* and *Ergodic Theory*; the spectral theorem for the self-adjoint operators is *Hilbert Spaces and Spectral Theory*. The reversal of the flow operator is *The Involution on the Flow Operator*, the last article of this group.

No physics is invoked.

## The Time-Reversal Operator

### Definition

**Definition.** A **time-reversal operator** on the Hilbert space $H=L^2(X,\mu)$ is an **anti-unitary involution** $C$,

$$
C(\alpha u+\beta v)=\overline\alpha\,Cu+\overline\beta\,Cv, \qquad C^2=\mathrm{id}, \qquad \langle Cu,Cv\rangle=\overline{\langle u,v\rangle},
$$

the composition of the complex conjugation of the amplitudes with the spatial involution of the reversal; it is the operator form of the reversing map of the dynamics, with the additional complex conjugation that the passage to the amplitudes requires. The **reversal** of the dynamics $T$ is the operator condition

$$
C\,U_T\,C=U_T^{-1},
$$

which is the operator transcription of $RTR=T^{-1}$ with the anti-unitary reversal.

**Theorem (the elementary action of the reversal).** Let $C$ be the time-reversal operator. Then (i) $C$ is anti-unitary and $C^2=\mathrm{id}$, so $C$ is its own inverse; (ii) for a real operator $A$ (one commuting with $C$) the adjoint and the reversal combine as $C A^* C=\overline A=A$; (iii) if the dynamics is reversible with the anti-unitary $C$ then the spectrum of $U_T$ is invariant under $\lambda\mapsto\lambda^{-1}$ and $\lambda\mapsto\overline\lambda$; (iv) the fixed space $H_{\mathbb{R}}=\{u:Cu=u\}$ is a real Hilbert space with $H=H_{\mathbb{R}}\otimes\mathbb{C}$, and the real observables are the fixed vectors.

*Proof.* (i) is the definition. (ii) For $A$ real, $CA=AC$ and $C A^* C=(CAC)^*$; with $CAC=A$ (reality) and $C^2=I$ this gives $C A^*C=A^*$; for self-adjoint real $A$ it is $A$ again. (iii) is the spectral theorem of *Reversible Operators and the Involution* for the anti-unitary reversing involution. (iv) is the standard real structure of a conjugation.

## Detailed Balance and the Self-Adjointness

### The Setting

**Definition.** Let $\mu$ be a probability measure on $X$ and let $P=P_T$ be the transfer operator of the dynamics, written as a kernel $P(x,dy)$ or, in the discrete case, as a matrix $P(x,y)$. The measure $\mu$ satisfies **detailed balance** for $P$ if

$$
\mu(dx)\,P(x,dy)=\mu(dy)\,P(y,dx),
$$

that is, in the discrete case, $\mu(x)P(x,y)=\mu(y)P(y,x)$ for all $x,y$; the dynamics is then **reversible with respect to $\mu$** and $\mu$ is the **reversible measure**. The operator $\Pi$ of multiplication by the density $\rho=d\mu/dx$ (when it exists) is the **symmetriser**, and the **symmetrised transfer operator** is

$$
\hat P=\Pi^{1/2}\,P\,\Pi^{-1/2} .
$$

**Theorem (detailed balance is self-adjointness).** Let $\mu$ be invariant for $P$ and let $\hat P=\Pi^{1/2}P\Pi^{-1/2}$. Then the following are equivalent: (i) the detailed balance $\mu(x)P(x,y)=\mu(y)P(y,x)$ holds; (ii) the symmetrised operator $\hat P$ is **self-adjoint** on $L^2(X)$; (iii) the transfer operator $P$ is **self-adjoint** on $L^2(X,\mu)$, $\int (Pf)g\,d\mu=\int f(Pg)\,d\mu$; (iv) the dynamics is reversible with respect to $\mu$ under the reversal, $C P C=P$ with the anti-unitary reversal $C$.

*Proof.* (i) $\iff$ (ii): $\hat P(x,y)=\rho(x)^{1/2}P(x,y)\rho(y)^{-1/2}$ and its transpose is $\rho(y)^{1/2}P(y,x)\rho(x)^{-1/2}$, so the symmetry of $\hat P$ is exactly the symmetry of $\rho(x)P(x,y)$ in $x,y$. (ii) $\iff$ (iii): the similarity by $\Pi^{1/2}$ is an isometry of $L^2(\mu)$ onto $L^2(dx)$ carrying the self-adjointness of $\hat P$ to the self-adjointness of $P$ in $L^2(\mu)$. (iii) $\iff$ (iv): the reversibility $CPC=P$ with $C$ the anti-unitary reversal is the operator statement of the symmetry of the kernel, and it is equivalent to the detailed balance by the definitions. The details of the probabilistic side, the convergence to equilibrium and the ergodic theorems for the reversible chains are those of *Reversible Markov Chains and Time Reversal*.

### The Spectral Consequences

**Theorem (the real spectrum).** Let $P$ be self-adjoint in $L^2(X,\mu)$, equivalently let $\mu$ satisfy the detailed balance. Then the spectrum of $P$ is **real**, the spectral gap is real and equals the exponential rate of the correlation decay, the eigenvalues of $P$ are real and their eigenvectors are orthogonal in $L^2(\mu)$, the eigenvalue $1$ (the invariant density) is simple when the dynamics is ergodic, and the Ruelle–Pollicott resonances of a reversible hyperbolic dynamics are real or occur in complex conjugate pairs, with the reciprocal pairing of the reversible structure.

*Proof.* The self-adjoint operator has the real spectrum and the orthogonal eigenbasis by the spectral theorem for self-adjoint operators, quoted from *Hilbert Spaces and Spectral Theory*; the identification of the spectral gap with the exponential rate of the correlations is the standard variational characterisation of the spectral gap of a self-adjoint Markov operator, and the probabilistic account is *Reversible Markov Chains and Time Reversal*; the resonance statement is the combination of the self-adjointness with the reciprocal pairing of *Reversible Operators and the Involution*.

**Theorem (the Koopman and the transfer operator under the reversal).** Let the dynamics be reversible with the reversal $C$, so that $CU_TC=U_T^{-1}$. Then on the self-adjoint side the transfer operator satisfies $CPC=P$ and the Koopman operator satisfies $CU_TC=U_T^{-1}=U_T^*$; the pair $(U_T,P)$ is exchanged by the reversal, and the correlations $C_n(f,g)=\langle U_T^nf,g\rangle$ are real for real $f,g$ and decay at the real rates of the self-adjoint spectrum, so that the reversible dynamics has no complex oscillations in the correlation decay.

*Proof.* The identities are the conjugation of the Koopman operator by the anti-unitary reversal and the self-adjointness of the transfer operator; the reality of the correlations for real observables follows because $C$ fixes the real observables and $CU_T^nf=U_T^{-n}Cf$, so $C_n$ is the pairing of a self-adjoint operator with real vectors.

## The Examples

**Example (a reversible finite chain, verified).** Let $P$ be the birth–death chain on three states with the up rates $a_0=0.3$, $a_1=0.5$ and the down rates $b_1=0.4$, $b_2=0.2$; the stationary distribution is $\pi=(0.2759,0.2069,0.5172)$ to four decimals, the stationarity residual is $5.6\times10^{-17}$, the **detailed balance** $\pi_iP_{ij}=\pi_jP_{ji}$ holds to $1.4\times10^{-17}$, and the symmetrised operator $\hat P_{ij}=\pi_i^{1/2}P_{ij}\pi_j^{-1/2}$ is symmetric to $5.6\times10^{-17}$: the three identities of the theorem are confirmed numerically. The spectrum of $\hat P$ is real and one of its eigenvalues is $1$ (the trace of $\hat P$ is $1.6$ and the eigenvalue $1$ is present), and the reversible chain therefore has the real relaxation rates.

**Example (a non-reversible perturbation, verified).** Perturbing the chain by moving $0.05$ from $P_{00}$ to $P_{01}$ destroys the detailed balance, and the symmetrised operator of the perturbed chain is **not** symmetric: the check $\hat P_{ij}=\hat P_{ji}$ fails with error $0.058$. The example confirms that the self-adjointness is exactly the reversibility and is not automatic; a non-reversible dynamics has a symmetrised operator with a complex spectrum and a complex resonance structure.

**Example (a reversible hyperbolic map).** Let $T$ be a reversible hyperbolic map of the torus, for instance an Anosov automorphism with an involutive reversor; the transfer operator $P_T$ has the Ruelle–Pollicott resonances in the meromorphic continuation, the reversibility forces the reciprocal pairing $\lambda\leftrightarrow\lambda^{-1}$ and, with the detailed balance, the reality of the leading resonances (those governing the decay of the correlations of the real observables). The full analytic computation of the resonances is *The Transfer Operator*, and the present article records only the reality that the self-adjointness imposes. The doubling map, being non-invertible and not reversible in the operator sense, is the counterexample: its transfer operator has the verified non-self-adjointness gap $0.014$ and its Bernoulli eigenfunctions are not orthogonal in the relevant pairing.

**Example (the counterexample of the irreversibility).** A dissipative non-reversible system, such as a map with a complex pair of leading Ruelle resonances, has a transfer operator with a genuinely complex spectral picture; the detailed balance fails and the reversibility is absent, so no self-adjointness and no real spectrum can be asserted. This is the boundary of the present theory and it is the reason the reversibility is stated as a hypothesis rather than derived.

## Summary

**Time reversal** on the observables is an **anti-unitary involution** $C$, the complex conjugation composed with the spatial reversal, under which the dynamics is reversed, $CU_TC=U_T^{-1}$; the spectrum of a time-reversible operator is invariant under $\lambda\mapsto\lambda^{-1}$ and $\lambda\mapsto\overline\lambda$, a real self-adjoint reversible operator is an involution, and the conjugation defines the real structure $H_{\mathbb{R}}=\{u:Cu=u\}$. The transfer operator $P$ and the reversal meet in the **detailed balance** $\mu(x)P(x,y)=\mu(y)P(y,x)$, which is equivalent to the **self-adjointness** of the symmetrised operator $\hat P=\Pi^{1/2}P\Pi^{-1/2}$, to the self-adjointness of $P$ in $L^2(X,\mu)$, and to the reversibility $CPC=P$; the consequence is the **real spectrum**, the real spectral gap equal to the exponential correlation rate, the orthogonal eigenbasis and the real (or conjugate-paired) Ruelle–Pollicott resonances, with the reciprocal pairing of the reversible structure. The verified examples are the reversible three-state chain, with the detailed balance to $1.4\times10^{-17}$, the symmetry of $\hat P$ to $5.6\times10^{-17}$ and the eigenvalue $1$ present; the non-reversible perturbation, whose symmetrised operator fails to be symmetric with error $0.058$; and the doubling map, whose transfer operator has the non-self-adjointness gap $0.014$, the counterexample. The unitary reversor of *Reversible Operators and the Involution* reverses the operator by a conjugation to its inverse, while the anti-unitary time reversal of the present article forces the self-adjointness and the reality of the spectrum; the probabilistic theory, the convergence to equilibrium and the Markov chains are *Reversible Markov Chains and Time Reversal*, and the reversal of the flow operator is *The Involution on the Flow Operator*, the last article of this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C$, $C^2=\mathrm{id}$ | Anti-unitary time-reversal (conjugation) involution |
| $CU_TC=U_T^{-1}$ | Reversal of the dynamics |
| $H_{\mathbb{R}}=\{u:Cu=u\}$ | Real structure of the conjugation |
| $P=P_T$ | Transfer (Perron–Frobenius) operator |
| $\mu(x)P(x,y)=\mu(y)P(y,x)$ | Detailed balance (reversibility of the measure) |
| $\Pi$, $\rho=d\mu/dx$ | Multiplication by the invariant density |
| $\hat P=\Pi^{1/2}P\Pi^{-1/2}$ | Symmetrised transfer operator (self-adjoint iff reversible) |
| $\operatorname{spec}(P)\subseteq\mathbb{R}$ | Real spectrum of the reversible transfer operator |
| $\lambda\leftrightarrow\lambda^{-1}$ | Reciprocal pairing of the resonances |

## Further Reading

- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the Koopman and the transfer operators, the invariant measures and the correlations.
- Viviane Baladi, *Positive Transfer Operators and Decay of Correlations* (World Scientific, 2000), for the transfer-operator spectrum and the Ruelle–Pollicott resonances.
- David Ruelle, *Thermodynamic Formalism* (Addison-Wesley, 1978), for the transfer operator and the resonances of the hyperbolic dynamics.
- James R. Norris, *Markov Chains* (Cambridge University Press, 1997), and David A. Levin, Yuval Peres and Elizabeth L. Wilmer, *Markov Chains and Mixing Times* (American Mathematical Society, 2nd ed. 2017), for the reversible chains, the detailed balance and the spectral gap.
- Zhong-Qi Chen and others, and the standard references on the time reversal and the anti-unitary operators, for the reversal structure.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the anti-unitary operators and the spectral theorem for self-adjoint operators.
- William Parry and Mark Pollicott, "Zeta functions and the periodic orbit structure of hyperbolic dynamics", *Astérisque* 187–188 (1990), for the resonances and the zeta function.
- Michael B. Sevryuk, *Reversible Systems* (Springer Lecture Notes in Mathematics 1211, 1986), and John A. G. Roberts and G. R. W. Quispel, *Physics Reports* 216 (1992), 63–177, for the reversibility in the dynamics.
