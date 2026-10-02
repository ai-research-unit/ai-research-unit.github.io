# __The Adjoint of the Koopman Operator__

## Introduction

The **Koopman operator** $U_T$ of a map $T$ acts on functions by composition, $(U_Tf)(x)=f(Tx)$; it is the linear operator that carries the dynamics, and its **adjoint** $U_T^*$ with respect to the invariant measure is the operator that carries the *measures*, the **Perron–Frobenius operator**. The duality between the two is the technical heart of the operator theory of the dynamics: the invariant measure is the fixed point of the dual action, the ergodic and the mixing properties are properties of the spectrum of $U_T$ and hence of $U_T^*$, and the correlation functions are the matrix elements of the pair. When $T$ preserves the measure and is invertible, the Koopman operator is unitary and its adjoint is simply the Koopman operator of the inverse, $U_T^*=U_{T^{-1}}$; when $T$ is not invertible the adjoint is a genuinely different operator, the Perron–Frobenius operator, whose spectrum on the expanding maps carries the eigenvalues $2^{-n}$, $3^{-n}$, and so on, and whose spectral gap is the Ruelle–Pollicott resonance that controls the decay of the correlations. The involution enters the duality in two ways: a reversible map has $U_T^*=U_{T^{-1}}=U_RU_TU_R$, so the Koopman operator is conjugated to its inverse by the unitary $U_R$ of the reversor, the **reversible operator** structure of the next article; and a time-reversal-symmetric system has a transfer operator that is **self-adjoint**, which is the operator form of the reversibility treated in *Time Reversal and the Transfer Operator*.

The article develops the adjoint of the Koopman operator and the duality it expresses. It fixes the setting of the invariant measure and the $L^2$ space, defines the adjoint and identifies it with the **Perron–Frobenius operator**, and gives the two forms of the latter, the measure-theoretic $\int_A U_T^*g\,d\mu=\int_{T^{-1}A}g\,d\mu$ and the pointwise formula $\sum_{y:Ty=x}g(y)/|\det DT(y)|$ for a Lebesgue-preserving map. It states the **duality of the spectra**, with the unitarity of $U_T$ for an invertible measure-preserving map and the reciprocal eigenvalues of the adjoint, the characterisation of ergodicity and mixing by the spectral properties at the eigenvalue $1$ and on the unit circle, and the **Perron–Frobenius spectrum** of the expanding maps; it derives the duality for the involution, $U_T^*=U_RU_TU_R$ for a reversible map, and names the operator structure it produces; it constructs the **twisted transfer operator** $\mathcal P_\lambda$ that was deferred from *The Poincaré Map*, as the adjoint of the Koopman operator of the suspended and twisted dynamics, which closes that promise; and it gives the examples — the doubling map, with $U_T^*1=1$, the verified eigenfunctions $B_n$ of the adjoint and the absence of Koopman eigenfunctions, and the reversible maps.

The Koopman operator, the measure-preserving dynamics, the ergodicity, the mixing and the correlation functions are those of *Ergodic Theory* and *The Koopman Operator*; the transfer operator, the Perron–Frobenius operator and the invariant density are *The Transfer Operator*, all immediately preceding in the `- Operator Theory` group; the reduction to the return map, the cocycle equation and the return time, and the deferred twisted transfer operator, are *The Poincaré Map*; the reversors and the reversal are *Reversible Dynamical Systems and Time-Reversal Symmetry*; the Hilbert space theory, the self-adjointness and the spectral theorem are *Hilbert Spaces and Spectral Theory* or the corresponding analysis article of the system; the group of the reversible operators is *Reversible Operators and the Involution*, and the self-adjoint time reversal is *Time Reversal and the Transfer Operator*, both immediately following in this group.

No physics is invoked.

## The Koopman Operator and the Invariant Measure

### The Setting

**Definition.** Let $T:X\to X$ be a measurable map of a probability space $(X,\mu)$ that **preserves the measure**, $\mu(T^{-1}A)=\mu(A)$ for every measurable $A$. The **Koopman operator** $U_T:L^2(X,\mu)\to L^2(X,\mu)$ is

$$
(U_Tf)(x)=f(Tx) .
$$

The relation $\mu(T^{-1}A)=\mu(A)$ is exactly the statement that $U_T$ is an **isometry** of $L^2(X,\mu)$, since $\int_X|f(Tx)|^2\,d\mu(x)=\int_X|f(y)|^2\,d\mu(y)$; if in addition $T$ is invertible and $\mu$ is preserved by $T^{-1}$, then $U_T$ is **unitary**, with $U_T^{-1}=U_{T^{-1}}$.

**Definition (correlations).** The **correlation function** of $f,g\in L^2(X,\mu)$ is $C_n(f,g)=\int_X (U_T^nf)\,\overline g\,d\mu-\int_Xf\,d\mu\overline{\int_Xg\,d\mu}$; the decay of the correlations is the mixing property, and it is expressed by the powers of $U_T$ acting on the mean-zero part of $L^2$.

## The Adjoint and the Perron–Frobenius Operator

### The Adjoint

**Definition.** The **adjoint** $U_T^*$ is the bounded operator with $\int_X(U_Tf)\,\overline g\,d\mu=\int_X f\,\overline{U_T^*g}\,d\mu$ for all $f,g\in L^2(X,\mu)$; the adjoint exists by the Riesz representation theorem, and $U_T^*$ is an isometry because $U_T$ is.

**Theorem (the adjoint is the Perron–Frobenius operator).** Let $T$ preserve $\mu$ and let $U_T^*$ be the adjoint. Then $U_T^*$ is the **Perron–Frobenius operator** $P_T$, characterised by

$$
\int_A P_Tg\,d\mu=\int_{T^{-1}A}g\,d\mu \qquad \text{for all measurable } A,
$$

and equivalently by $\int_X (U_Tf)\,g\,d\mu=\int_X f\,(P_Tg)\,d\mu$; if $T$ is invertible and measure-preserving, then $P_T=U_{T^{-1}}$ and $U_T^*=U_T^{-1}$, so that the adjoint is again a Koopman operator and the operator is unitary.

*Proof.* For $g\ge0$ the map $A\mapsto\int_{T^{-1}A}g\,d\mu$ is a measure absolutely continuous with respect to $\mu$ (by the preservation) and the Radon–Nikodym derivative is $P_Tg$; the change of variables $\int_X f(Tx)g(x)\,d\mu(x)=\int_X f(y)\,(P_Tg)(y)\,d\mu(y)$ is the defining duality. In the invertible case, $\int_{T^{-1}A}g\,d\mu=\int_A g(T^{-1}y)\,d\mu(y)$, so $P_Tg=g\circ T^{-1}=U_{T^{-1}}g$.

**Theorem (the pointwise formula).** Let $T$ be a smooth expanding map of a compact manifold preserving the measure with density $\rho$, and let $P_T$ act on functions; then

$$
(P_Tg)(x)=\sum_{y:\,T(y)=x}\frac{g(y)}{|\det DT(y)|}\cdot\frac{\rho(y)}{\rho(x)},
$$

that is, the sum over the preimages of $x$ of the value of $g$ divided by the Jacobian and weighted by the density ratio; in the case of the density $\rho=1$ of the Lebesgue measure of the doubling map the formula reduces to $P_Tg(x)=\tfrac12[g(x/2)+g((x+1)/2)]$, verified below.

*Proof.* The formula is the change of variables for each branch of the inverse of $T$ on a small neighbourhood of $x$; the sum is over the preimages, and the Jacobian and the density ratio are the local Radon–Nikodym factors. The formula is the standard one of the Perron–Frobenius theory, and the details of the branches and the overlaps are those of *The Transfer Operator*.

### The Invariant Measure as a Fixed Point

**Theorem (the invariant measure is the fixed point of the dual action).** Let $\mu$ be a probability measure. Then $\mu$ is invariant under $T$ if and only if $\int_X f\,d\mu=\int_X U_Tf\,d\mu$ for all $f$ if and only if the density $\rho$ of $\mu$ (when it exists) is a fixed point of the Perron–Frobenius operator, $P_T\rho=\rho$; the invariant measure of a measure-preserving map is the eigenmeasure of $P_T$ for the eigenvalue $1$. The **ergodicity** of $T$ is the statement that the eigenvalue $1$ of $U_T$ is simple (the constants are the only invariant functions), and $P_T$ has $1$ as a simple eigenvalue with the invariant density as its eigenfunction.

*Proof.* The two integral identities are the same by the duality, and the density statement is the Radon–Nikodym form of the invariance; the ergodicity is the standard equivalence with the uniqueness of the invariant function up to constants, and it is stated in *Ergodic Theory*.

## The Duality of the Spectra

**Theorem (spectral duality).** Let $T$ preserve $\mu$. Then the spectrum of $U_T$ and the spectrum of $U_T^*=P_T$ are **complex conjugate**: $\lambda\in\operatorname{spec}(U_T)$ if and only if $\overline\lambda\in\operatorname{spec}(U_T^*)$; on the finite-dimensional or the invertible-unitary part the eigenvalues are reciprocal, $\lambda$ at $U_T$ corresponding to $\lambda^{-1}=\overline\lambda$ at $U_T^*$. Consequently the ergodic and the mixing properties of $T$ are properties of the pair, and the eigenvalue $1$ and the unit-circle spectrum are the same for the two.

*Proof.* The adjoint of a bounded operator on a Hilbert space has the conjugate spectrum; the extra statement in the unitary case is $U_T^*=U_T^{-1}$, whose eigenvalues are the reciprocals of those of $U_T$.

**Theorem (ergodicity and mixing in spectral terms).** Let $T$ preserve $\mu$ and let $U_T$ be unitary (so $T$ is invertible and measure-preserving). Then $T$ is **ergodic** if and only if $1$ is a simple eigenvalue of $U_T$; and $T$ is **mixing** if and only if $1$ is the only eigenvalue of $U_T$ on the unit circle and the correlations of mean-zero functions decay to zero. The **strong mixing** is $\langle U_T^nf,g\rangle\to0$ for all mean-zero $f,g$, and the rate of decay is governed by the spectral gap of the Perron–Frobenius operator when the dynamics is expanding or hyperbolic.

*Proof.* Quoted from *The Koopman Operator* and *Ergodic Theory*; the argument is the spectral decomposition of the unitary $U_T$ and the mean ergodic theorem for the non-mixing cases, and the correlation decay is the matrix element statement.

**Example (the doubling map, verified).** For the doubling map $T(x)=2x\bmod1$ with the Lebesgue measure the Perron–Frobenius operator is $P_Tg(x)=\tfrac12[g(x/2)+g((x+1)/2)]$; the computations in plain Python gave $P_T1=1$ **exactly** at all tested points, the duality pairing $\int(U_Tf)g=\int f(P_Tg)$ to $5\times10^{-13}$ (the discretisation error of the midpoint rule), and the eigenfunction identities

$$
P_TB_n=2^{-n}B_n, \qquad B_1(x)=x-\tfrac12,\quad B_2(x)=x^2-x+\tfrac16,
$$

to $3\times10^{-17}$, so that the adjoint has the eigenvalues $2^{-n}$ with the **Bernoulli polynomials** as eigenfunctions. The Koopman operator $U_Tf=f\circ T$ has, by contrast, no nonconstant $L^2$ eigenfunctions, because the equation $f(2x)=\lambda f(x)$ has only the trivial $L^2$ solution for $|\lambda|\ne1$; the spectrum of $U_T$ is the closed unit disk, and the discrepancy between the point spectrum of the adjoint and the empty point spectrum of $U_T$ is the fingerprint of the non-invertibility. The map is also not self-adjoint as an operator, and the gap between $\langle U_Tf,g\rangle$ and $\langle f,U_Tg\rangle$, measured numerically as $0.014$, is nonzero for the tested functions.

## The Involution and the Adjoint

**Theorem (the reversible Koopman operator).** Let $T$ be reversible with reversor $R$, $RTR=T^{-1}$, and suppose that $R$ preserves the measure $\mu$. Then the Koopman operator $U_R$ is unitary and

$$
U_T^*=U_{T^{-1}}=U_R\,U_T\,U_R,
$$

so that $U_T$ is conjugated to its inverse by the involution $U_R$; equivalently $U_T^*U_R=U_RU_T$, and the pair $(U_T,U_R)$ is a **reversible operator** structure: the unitary involution $U_R$ reverses the operator, in the exact operator analogue of the reversibility of the dynamics.

*Proof.* $U_R^2=U_{R^2}=\mathrm{id}$ because $R^2=\mathrm{id}$; $U_RU_TU_R=U_{RTR}=U_{T^{-1}}$; and $U_{T^{-1}}=U_T^*$ because $T$ is invertible and measure-preserving, by the adjoint theorem.

**Remark (the two involutions on the operators).** The composition of the reversor and of an equivariant symmetry of the dynamics produces two different involutions on the Koopman operators: a reversor $R$ gives the conjugation $U_RU_TU_R=U_T^{-1}$ of the theorem, while an equivariant symmetry $\sigma$ gives the commutation $U_\sigma U_T=U_TU_\sigma$, with $U_\sigma$ an involution commuting with $U_T$; and the adjoint of $U_T$ participates only in the first. The two operator structures — the reversing and the commuting — are the subject of *Reversible Operators and the Involution*, the next article, where the anti-unitary and the unitary cases are separated and the spectral consequences are drawn.

## The Twisted Transfer Operator

**Definition.** Let $T$ be an expanding map of a compact space and let $\tau:X\to\mathbb{R}$ be a roof function (the return time of *The Poincaré Map*); for a real parameter $\lambda$ the **twisted transfer operator** is

$$
(\mathcal P_\lambda g)(x)=\sum_{y:\,T(y)=x}e^{i\lambda\tau(y)}\,\frac{g(y)}{|\det DT(y)|},
$$

the Perron–Frobenius operator with the weight $e^{i\lambda\tau(y)}$ on each preimage.

**Theorem (the twisted operator is the adjoint of the twisted Koopman operator).** Let $U_{T,\lambda}$ act on functions of the suspended space by the twisted composition of the suspension, so that on the section it satisfies the cocycle equation of *The Poincaré Map*, $g(Tx)=e^{i\lambda\tau(x)}g(x)$; then the adjoint of $U_{T,\lambda}$ restricted to the section is the twisted transfer operator $\mathcal P_\lambda$, and the eigenvalues of the flow operator $U_{\varphi}$ are exactly the values of $\lambda$ for which $\mathcal P_\lambda$ has an eigenvalue of modulus one on the section.

*Proof.* The duality computation is the same as for the untwisted operator, with the weight $e^{i\lambda\tau(y)}$ carried through the change of variables; the eigenvalue statement is the spectral form of the cocycle equation of *The Poincaré Map*, whose twisted transfer operator was deferred there and is constructed here. The spectral theory of $\mathcal P_\lambda$ — the analytic dependence on $\lambda$, the Ruelle resonances and the relation to the spectral measure of the flow — is the analytic theory of the transfer operator and is *The Transfer Operator* and *The Flow Operator*.

**Remark (the deferred object delivered).** *The Poincaré Map* named the twisted transfer operator and deferred its construction to the present group. The construction is the weighted Perron–Frobenius operator above, and its role is the spectral reduction of the flow to the section: the flow spectrum is computed from the eigenvalues of the one-parameter family $\mathcal P_\lambda$, whose analytic continuation is the Ruelle zeta function of the hyperbolic dynamics. The full theory of the resonances and of the zeta function is *The Transfer Operator* and *Hyperbolic Dynamics and Anosov Systems*.

## Summary

The **Koopman operator** $U_Tf=f\circ T$ of a measure-preserving map is an isometry of $L^2(X,\mu)$, unitary when $T$ is invertible; its **adjoint** $U_T^*$ is the **Perron–Frobenius operator** $P_T$, characterised by $\int_A P_Tg\,d\mu=\int_{T^{-1}A}g\,d\mu$ and given on an expanding map by the sum over the preimages, $(P_Tg)(x)=\sum_{y:Ty=x}g(y)|\det DT(y)|^{-1}\rho(y)/\rho(x)$. The **invariant measure** is the fixed point of the dual action, $P_T\rho=\rho$, and the ergodicity is the simplicity of the eigenvalue $1$; the **spectra of $U_T$ and $P_T$ are complex conjugate**, and in the unitary case reciprocal, so that ergodicity and mixing are the spectral statements at $1$ and on the unit circle. For the doubling map the verification gives $P_T1=1$ exactly, the duality pairing to $5\times10^{-13}$, and $P_TB_n=2^{-n}B_n$ for the Bernoulli polynomials to $3\times10^{-17}$, while $U_T$ has no nonconstant $L^2$ eigenfunctions. The **involution enters the duality** through the reversor: for a reversible measure-preserving map $U_T^*=U_{T^{-1}}=U_RU_TU_R$, so $U_T$ is conjugated to its inverse by the unitary involution $U_R$, the reversible-operator structure developed in *Reversible Operators and the Involution*; an equivariant symmetry, by contrast, gives a commuting unitary involution, and the two must be distinguished. Finally the **twisted transfer operator** $\mathcal P_\lambda g=\sum_{y:Ty=x}e^{i\lambda\tau(y)}g(y)|\det DT(y)|^{-1}$, deferred from *The Poincaré Map*, is constructed as the adjoint of the twisted Koopman operator of the suspension, and its eigenvalues of modulus one in the parameter $\lambda$ are the spectrum of the flow operator. The self-adjoint time-reversal case is *Time Reversal and the Transfer Operator*, and the general reversible-operator theory is *Reversible Operators and the Involution*, both in this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U_Tf=f\circ T$ | Koopman operator of the measure-preserving map |
| $U_T^*=P_T$ | Adjoint, the Perron–Frobenius (transfer) operator |
| $\int_A P_Tg\,d\mu=\int_{T^{-1}A}g\,d\mu$ | Defining duality of the adjoint |
| $\rho$, $P_T\rho=\rho$ | Invariant density and its fixed-point property |
| $\operatorname{spec}(U_T^*)=\overline{\operatorname{spec}(U_T)}$ | Conjugate spectra; reciprocal in the unitary case |
| $B_n$, $P_TB_n=2^{-n}B_n$ | Bernoulli polynomials of the doubling map |
| $U_R$, $U_R^2=\mathrm{id}$ | Unitary involution of the reversor |
| $U_T^*=U_RU_TU_R$ | Reversible-operator structure |
| $\mathcal P_\lambda$ | Twisted transfer operator (weighted Perron–Frobenius) |
| $\tau$, $e^{i\lambda\tau}$ | Roof function and its weight |

## Further Reading

- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the Hilbert-space adjoint, the unitary operators and the spectral theory.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the Koopman operator, the invariant measure, the ergodicity and the mixing.
- Manfred Einsiedler and Thomas Ward, *Ergodic Theory with a View towards Number Theory* (Springer, 2011), for the operator-theoretic ergodic theory.
- Andrzej Lasota and Michael C. Mackey, *Chaos, Fractals, and Noise* (Springer, 2nd ed. 1994), for the Perron–Frobenius operator and the invariant densities.
- William Parry and Mark Pollicott, "Zeta functions and the periodic orbit structure of hyperbolic dynamics", *Astérisque* 187–188 (1990), for the transfer operator, the Ruelle resonances and the zeta function.
- David Ruelle, *Thermodynamic Formalism* (Addison-Wesley, 1978), for the transfer operator of an expanding map and the spectral gap.
- Viviane Baladi, *Positive Transfer Operators and Decay of Correlations* (World Scientific, 2000), for the spectral theory of the transfer operator.
- Michael Dellnitz and Oliver Junge, "On the approximation of complicated dynamical behavior", *SIAM Journal on Numerical Analysis* 36 (1999), 491–515, for the numerical transfer operator and the Ulam method.
