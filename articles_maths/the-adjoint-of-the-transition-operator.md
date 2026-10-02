
# __The Adjoint of the Transition Operator__

## Introduction

The transition operator $P_t$ of a stationary process is the operator of the conditional expectation of the state time $t$ ahead,
$$
P_tf(x)=\mathbb E\bigl[f(X_t)\,\big|\,X_0=x\bigr]=\int_E p_t(x,dy)f(y),
$$
and the family $\{P_t\}_{t\ge0}$ is a semigroup, $P_{s+t}=P_sP_t$, with $P_0=I$. This article computes its **adjoint** with respect to the form of the category and the stationary measure $\pi$,
$$
\langle f,g\rangle_\pi=\int f\bar g\,d\pi,\qquad P_t^*g(y)=\frac{1}{\pi(y)}\int\pi(dx)\,p_t(x,dy)\,g(x)=\int\hat p_t(y,dx)g(x),
$$
and shows that the adjoint semigroup $\hat P_t=P_t^*$ is the transition semigroup of the **reversed process**, with the kernels $\hat p_t(x,dy)=\pi(dy)p_t(y,dx)/\pi(dx)$. The process is reversible exactly when $P_t^*=P_t$ for all $t$, which is the detailed balance of the two-sided version; the infinitesimal generator of the adjoint semigroup is the adjoint of the generator, $L^*=\hat L$, so the generator is self-adjoint precisely in the reversible case. The article derives the formula, identifies the adjoint semigroup with the reversed process, records the semigroup and spectral properties, relates the self-adjointness to the symmetry of the Dirichlet form, and illustrates the theory on the reversible and the non-reversible examples.

The conventions are those of the category. The transition operator, its semigroup and its generator are *The Transition Operator*, earlier in this category; the Markov operator is its time-one member and is *The Markov Operator*, earlier in this category; the reversed chain, the detailed balance and the self-adjointness are *Reversible Markov Chains and Time Reversal*, earlier in this category; the adjoint of the time-one operator is *The Adjoint of the Markov Operator*, the preceding article of this category, and the refinement of the spectrum by the reversing symmetry is *Reversible Operators and Self-Adjointness*, later in this category. The processes, their paths and their finite-dimensional laws are *Markov Chains and Processes*, written; the operator algebra and its involution are *Operator Algebras*, written, and *The Involution on the Operator Algebra of a Process*, the preceding article of this category; the adjoints and the spectral theory on a Hilbert space are *Banach and Hilbert Spaces*, written. No physics is invoked; the word time names the index of the process and nothing else.

Throughout, $\{X_t\}_{t\ge0}$ is a Markov process with transition kernels $p_t(x,dy)$ and stationary measure $\pi$, the transition operator is $P_tf(x)=\int p_t(x,dy)f(y)$ acting on $L^2(\pi)$ with $\langle f,g\rangle_\pi=\int f\bar g\,d\pi$, and the reversed kernels are $\hat p_t(x,dy)=\pi(dy)p_t(y,dx)/\pi(dx)$ with $\hat P_t$ the reversed transition operator. The generator is $L=\lim_{t\downarrow0}(P_t-I)/t$ on its domain, with the adjoint generator $L^*$, and the Dirichlet form is $\mathcal{E}(f,g)=-\langle Lf,g\rangle_\pi$ where the generator exists.

## The Adjoint of the Transition Operator

### The formula

**Definition.** The **adjoint** $P_t^*$ is the bounded operator on $L^2(\pi)$ with
$$
\langle P_tf,g\rangle_\pi=\langle f,P_t^*g\rangle_\pi\qquad\text{for all }f,g\in L^2(\pi).
$$

**Theorem (the adjoint formula).** With $\pi$ stationary,
$$
P_t^*g(y)=\frac{1}{\pi(y)}\int_E\pi(dx)\,p_t(x,dy)\,g(x)=\int_E\hat p_t(y,dx)\,g(x)\qquad\pi\text{-a.e.},
$$
where $\hat p_t(y,dx)=\pi(dx)p_t(x,dy)/\pi(y)$. Equivalently $P_t^*=\hat P_t$, the transition operator of the reversed process.

*Proof.* The computation is the one of *The Adjoint of the Markov Operator*, the preceding article, applied to the kernel $p_t$:
$$
\langle P_tf,g\rangle_\pi=\int_E f(y)\Bigl(\int_E\pi(dx)p_t(x,dy)\overline{g(x)}\Bigr),
$$
and the inner bracket is absolutely continuous with respect to $\pi$ with density $\int_E\pi(dx)p_t(x,dy)/\pi(y)$, which is the value $\int\hat p_t(y,dx)g(x)$ of the reversed kernel; comparing with $\langle f,P_t^*g\rangle_\pi$ gives the formula.

### The reversed semigroup

**Theorem (the reversed process).** The family $\{\hat P_t\}_{t\ge0}$ is a transition semigroup,
$$
\hat P_{s+t}=\hat P_s\hat P_t,\qquad \hat P_0=I,\qquad \hat P_t\ge0,\qquad \hat P_t1=1 ,
$$
with $\pi$ as a stationary measure, and it is the semigroup of the reversed process $\{X_{-t}\}$ of a two-sided stationary version. Its members commute, $\hat P_s\hat P_t=\hat P_t\hat P_s$.

*Proof.* Taking adjoints in $P_{s+t}=P_sP_t$ gives $\hat P_{s+t}=P_{s+t}^*=P_t^*P_s^*=\hat P_t\hat P_s$, and the reverse order gives $\hat P_{s+t}=\hat P_s\hat P_t$ by the commutativity of the addition; hence the two orders agree and the family is a commutative semigroup. The reversed kernels satisfy $\int\hat p_t(x,dy)=\pi P_t(dx)/\pi(x)=1$, so each $\hat P_t$ preserves the constants, and the stationarity is the construction; the interpretation as the reversed process is the finite-dimensional statement that the reversed kernels describe the law of $\{X_{-t}\}$.

**Corollary (the reversal of the semigroup).** The adjoint operation inverts the order of the semigroup and produces the reversed semigroup, so that the backwards run of the process is the forward run of the adjoint; the reversal one-sided in time is implemented on the operators by the adjoint, and the reversal two-sided by the unitary $U_r$ of *The Involution on the Operator Algebra of a Process*, the preceding article.

*Proof.* The order inversion is $(P_sP_t)^*=P_t^*P_s^*$, and the identification of the reversed semigroup as the semigroup of the backwards process is the theorem; the two-sided statement is the conjugation by $U_r$.

## Reversibility and the Detailed Balance

### The criterion

**Theorem (reversibility as self-adjointness).** The process is reversible, that is its two-sided stationary version is invariant under the time reversal, if and only if
$$
P_t^*=P_t\qquad\text{for all }t\ge0,
$$
equivalently if and only if the kernels satisfy the detailed balance $\pi(dx)p_t(x,dy)=\pi(dy)p_t(y,dx)$ for all $t$. A reversible process has a self-adjoint transition semigroup.

*Proof.* The adjoint is the reversed semigroup, so $P_t^*=P_t$ for all $t$ is the equality of the kernels of the process and of its reverse, which is the detailed balance; the equivalence with the invariance of the law under the time reversal is the finite-dimensional statement of *The Reversibility of a Stationary Process*, earlier in this category. The time-one case is *The Adjoint of the Markov Operator*, the preceding article.

### The generator of the reversed semigroup

**Theorem (the generator).** Let $L$ be the generator of $P_t$ on its domain. Then the generator of the adjoint semigroup $\hat P_t=P_t^*$ is
$$
\hat L=L^* ,
$$
the adjoint of $L$ with respect to the form $\langle\cdot,\cdot\rangle_\pi$, with domain the adjoint domain. The process is reversible exactly when $L^*=L$, that is when $L$ is self-adjoint on $L^2(\pi)$.

*Proof.* Differentiating $\hat P_t=P_t^*$ at $t=0$ gives $\hat L=(\lim(P_t-I)/t)^*=L^*$, the adjoint of the limit being the limit of the adjoints on the common domain; the reversibility criterion $P_t^*=P_t$ for all $t$ is the equality of the generators $L^*=L$ and conversely, since a semigroup is determined by its generator.

### The Dirichlet form

**Theorem (the Dirichlet form).** For a reversible process the Dirichlet form
$$
\mathcal{E}(f,g)=-\langle Lf,g\rangle_\pi=-\langle f,Lg\rangle_\pi
$$
is symmetric and nonnegative on the domain of $L$; for the time-one chain it is $\mathcal{E}(f,g)=\langle(I-P_1)f,g\rangle_\pi$, the Dirichlet form of *Reversible Markov Chains and Time Reversal*, earlier in this category.

*Proof.* The symmetry is the self-adjointness of $L$, and the nonnegativity is the limit $-\langle Lf,f\rangle_\pi=\lim_{t\downarrow0}\frac1t\langle(I-P_t)f,f\rangle_\pi$, each term of which is nonnegative because $P_t$ is a contraction fixing the constants; the identification with the sum form in the discrete case is the computation of *Reversible Markov Chains and Time Reversal*.

## Properties of the Adjoint Semigroup

**Theorem (powers and spectrum).** The adjoint satisfies $(P_t^n)^*=(P_t^*)^n$ and
$$
\operatorname{spec}(P_t^*)=\overline{\operatorname{spec}(P_t)},\qquad \operatorname{spec}(L^*)=\overline{\operatorname{spec}(L)},
$$
so the spectrum of the adjoint is the conjugate of the spectrum of the original, for the semigroup and for the generator.

*Proof.* The powers identity is the general adjoint identity; the spectral identities are the standard statements that the adjoint has the conjugated spectrum, applied to $P_t$ and to $L$, *Banach and Hilbert Spaces*, written.

**Theorem (the contraction and the constants).** Each $P_t$ and each $P_t^*$ is a contraction of $L^2(\pi)$, $\|P_t\|_{L^2(\pi)}\le1$, fixes the constants, and its self-adjointness holds at one time $t_0>0$ if and only if it holds at all times.

*Proof.* The contraction property is the Jensen inequality for the conditional expectation; the constants are fixed because the kernels are Markov; the equivalence of the self-adjointness at one time and at all times is the semigroup property, since $P_t=P_{t/n}^n$ and the adjoint of a power is the power of the adjoint.

## Worked Examples

**Example (the two-state chain).** With $p_t$ the two-state semigroup, the adjoint is the reversed semigroup with $\hat p_t=p_t$ for all $t$ by the detailed balance $\pi(0)p_t(0,1)=\pi(1)p_t(1,0)$; the semigroup is self-adjoint, its generator is the self-adjoint $2\times2$ matrix with the eigenvalues $0$ and $-(a+b)$, and the Dirichlet form is symmetric.

**Example (the directed cycle).** On $\{1,2,3\}$ with the deterministic cyclic motion the transition operator is the cyclic shift, its adjoint is the backwards shift, and $\hat P_t\ne P_t$; the generator is the anti-Hermitian cyclic derivative, $L^*=-L$, with the purely imaginary spectrum, and the Dirichlet form is not symmetric.

**Example (the Ornstein–Uhlenbeck semigroup).** The generator $L=\frac{\sigma^2}{2}\partial_x^2-\theta x\partial_x$ on $L^2$ of the normal law is self-adjoint, so the semigroup $P_t$ is self-adjoint and the process reversible; the adjoint semigroup is the original, the spectrum of $L$ is $\{-n\theta\}$, and the Dirichlet form is the quadratic form of the Hermite operator.

**Example (the Brownian semigroup).** The heat semigroup $P_t=e^{\frac12\Delta t}$ on $L^2(\mathbb R)$ with the Lebesgue measure is self-adjoint, being the function of a self-adjoint operator; the adjoint is the original and the process reversible. The example shows that the reversibility is the symmetry of the Dirichlet form, $-\langle Lf,g\rangle=\frac12\langle\nabla f,\nabla g\rangle$.

## Failure of the Degenerate Cases

The adjoint of the transition operator degenerates in four configurations. First, the adjoint is taken with respect to the stationary measure, and a process with several invariant measures has several adjoints; on a non-ergodic process each ergodic component gives a reversed semigroup. Second, the formula is defined only $\pi$-almost everywhere, and on the null sets of $\pi$ the reversed kernel is arbitrary; the reversed process is determined up to the null sets alone. Third, the generator $L$ is in general an unbounded operator defined on a dense domain, and the identity $L^*=\hat L$ is a statement about the domains, not only about the formulas; the adjoint domain must be computed and can be strictly larger or smaller, as in the case of a boundary-value problem. Fourth, the reversible case is where the semigroup is self-adjoint, and outside it the reversed semigroup is a different semigroup with the conjugate spectrum; the temptation to assume $P_t^*=P_t$ is the error the group contract forbids, and the directed cycle exhibits it when the generator's spectrum is purely imaginary.

## Summary

The adjoint of the transition operator with respect to the stationary measure $\pi$ and the form $\langle f,g\rangle_\pi$ is the transition operator of the reversed process,
$$
P_t^*g(y)=\frac{1}{\pi(y)}\int\pi(dx)p_t(x,dy)g(x)=\int\hat p_t(y,dx)g(x),\qquad \hat p_t(y,dx)=\frac{\pi(dx)p_t(x,dy)}{\pi(y)},
$$
and the family $\{\hat P_t\}=\{P_t^*\}$ is again a commutative transition semigroup, with $\pi$ stationary and the constants fixed, namely the semigroup of the process run backwards. The process is reversible exactly when $P_t^*=P_t$ for all $t$, equivalently when the kernels satisfy the detailed balance, and then the generator is self-adjoint and the Dirichlet form symmetric; in general the generator of the adjoint semigroup is the adjoint of the generator, $L^*=\hat L$, with the conjugated spectrum, $\operatorname{spec}(P_t^*)=\overline{\operatorname{spec}(P_t)}$. The time-one case is *The Adjoint of the Markov Operator*, the preceding article, the abstract operator-algebra involution is *The Involution on the Operator Algebra of a Process*, the preceding article, and the refinement of the spectrum by the reversing symmetry is *Reversible Operators and Self-Adjointness*, later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_tf(x)=\int p_t(x,dy)f(y)$ | the transition operator |
| $P_{s+t}=P_sP_t$, $P_0=I$ | the semigroup |
| $\langle f,g\rangle_\pi=\int f\bar g\,d\pi$ | the stationary form |
| $P_t^*=\hat P_t$ | the adjoint, the reversed semigroup |
| $\hat p_t(x,dy)=\pi(dy)p_t(y,dx)/\pi(dx)$ | the reversed kernel |
| $P_t^*=P_t\iff$ detailed balance | reversibility |
| $L$, $\hat L=L^*$ | the generator and its adjoint |
| $\mathcal{E}(f,g)=-\langle Lf,g\rangle_\pi$ | the Dirichlet form |
| $\operatorname{spec}(P_t^*)=\overline{\operatorname{spec}(P_t)}$ | the conjugated spectrum |

## Further Reading

- Daniel W. Stroock and S. R. Srinivasa Varadhan, *Multidimensional Diffusion Processes* (Springer, 1979), for the transition semigroups, the generators and the adjoints.
- Andrzej Lasota and Michael C. Mackey, *Chaos, Fractals, and Noise* (Springer, 2nd edition, 1994), for the semigroups, the generators and the reversibility.
- Martin L. Silverstein, *Symmetric Markov Processes* (Springer, 1974), for the symmetric semigroups and the Dirichlet forms.
- Joseph L. Doob, *Classical Potential Theory and Its Probabilistic Counterpart* (Springer, 1984), for the semigroups, the dual processes and the potential theory.
- Kiyosi Itô and Henry P. McKean, *Diffusion Processes and their Sample Paths* (Springer, 1965), for the generators and the reverse semigroups.
