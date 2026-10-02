
# __The Adjoint of the Markov Operator__

## Introduction

The Markov operator of a chain is a contraction of $L^2(\pi)$ when the stationary measure $\pi$ is fixed, and this article computes its **adjoint**. The result is the cleanest statement of the time reversal at the level of operators: the adjoint is the Markov operator of the **reversed chain**,
$$
P^*f(y)=\frac{1}{\pi(y)}\sum_x\pi(x)\,p(x,y)\,f(x)=\sum_x\hat p(y,x)f(x),\qquad \hat p(y,x)=\frac{\pi(x)p(x,y)}{\pi(y)},
$$
so the adjoint operation reverses the direction of the transitions and keeps the stationary measure. It follows that the chain is reversible exactly when $P$ is self-adjoint, $P^*=P$, which is the detailed balance of *Reversible Markov Chains and Time Reversal*, earlier in this category, and that the adjoint operation is the operator counterpart of the reversal $r$ of the path space. The article derives the formula, identifies the adjoint with the reversed chain, records the properties of the adjoint — the constants and the stationary measure, the powers and the spectrum, the self-adjointness and the unitarity — and states the comparison between the involution on the elements and the adjoint on the operators, the two structures that the group of this entry builds.

The conventions are those of the category. The chain, its transition kernel, its paths and its stationarity are *Markov Chains and Processes*, written; the Markov operator, its invariant measures and its ergodicity are *The Markov Operator*, earlier in this category; the transition operator and its semigroup are *The Transition Operator*, earlier in this category; the reversed chain, the detailed balance and the self-adjointness are *Reversible Markov Chains and Time Reversal*, earlier in this category; the adjoint of an operator on a Hilbert space, the self-adjointness and the spectral theorem are *Banach and Hilbert Spaces*, written, and the operator-algebraic adjoint is *Operator Algebras*, written. The involution on the operator algebra of a process, which is the element-level structure underlying this adjoint, is *The Involution on the Operator Algebra of a Process*, the next article of this category, and the adjoint of the transition operator is *The Adjoint of the Transition Operator*, later in this category. No physics is invoked; the word time names the index of the chain and nothing else.

Throughout, $E$ is a countable set or a standard Borel space, $p(x,dy)$ is the transition kernel, $\pi$ is a stationary probability measure, and the chain is $\{X_n\}$. The Markov operator is $Pf(x)=\int p(x,dy)f(y)$, acting on $L^2(\pi)$ with the inner product
$$
\langle f,g\rangle_\pi=\int_E f\bar g\,d\pi ,
$$
and it satisfies $\|P\|_{L^2(\pi)}\le1$ and $P1=1$ when $\pi$ is stationary. The reversed chain is $\hat p$ with $\hat p(x,dy)=\pi(dy)p(y,dx)/\pi(dx)$, and $\hat P$ is its Markov operator.

## The Adjoint on $L^2(\pi)$

### Definition and the formula

**Definition.** The **adjoint** $P^*$ is the bounded operator on $L^2(\pi)$ characterised by
$$
\langle Pf,g\rangle_\pi=\langle f,P^*g\rangle_\pi\qquad\text{for all }f,g\in L^2(\pi).
$$

**Theorem (the adjoint formula).** Let $\pi$ be stationary for $p$. Then
$$
P^*g(y)=\frac{1}{\pi(y)}\int_E \pi(dx)\,p(x,dy)\,g(x)=\int_E\hat p(y,dx)\,g(x)
$$
$\pi$-almost everywhere, where $\hat p(y,dx)=\pi(dx)p(x,dy)/\pi(y)$ is the reversed kernel. Equivalently $P^*=\hat P$, the Markov operator of the reversed chain.

*Proof.* Compute
$$
\langle Pf,g\rangle_\pi=\int_E\pi(dx)\Bigl(\int_Ep(x,dy)f(y)\Bigr)\overline{g(x)}=\int_E f(y)\Bigl(\int_E\pi(dx)p(x,dy)\overline{g(x)}\Bigr),
$$
the interchange being guaranteed by the finiteness of the mass and the boundedness of the two factors. The inner integral is absolutely continuous with respect to $\pi$ with density $\int_E\pi(dx)p(x,dy)/\pi(y)$, by the definition of the reversed kernel, so the right side is $\int_E f(y)\,\pi(dy)\,\overline{\int_E\hat p(y,dx)g(x)}$; comparing with $\langle f,P^*g\rangle_\pi$ gives the formula.

**Theorem (the adjoint is a Markov operator).** The reversed kernel $\hat p$ is a transition kernel with $\pi$ stationary, $P^*1=1$, $P^*\ge0$ and $\|P^*\|_{L^2(\pi)}\le1$; the adjoint is again a Markov operator, and the construction is involutive, $(P^*)^*=P$.

*Proof.* The reversed kernel is a kernel because $\int\hat p(x,dy)=\int\pi(dy)p(y,dx)/\pi(x)=(\pi P)(dx)/\pi(x)=1$ by the stationarity of $\pi$; the constant function is preserved, $P^*1=1$, and the positivity and the contraction bound are those of a Markov operator. The involution is the symmetry of the definition of $\hat p$ in the pair $(p,\pi)$, which is the same as the relation between the two chains.

## Properties of the Adjoint

### Stationary measures and the constants

**Theorem (the stationary measure and the constants).** The adjoint $P^*$ has $\pi$ as a stationary measure, $\pi P^*=\pi$, and it fixes the constants, $P^*1=1$; the adjoint of a Markov operator is therefore a Markov operator with the same stationary measure. The harmonic functions of $P^*$, the solutions of $P^*f=f$, are those of the reversed chain; they coincide with the harmonic functions of $P$ exactly when the chain is reversible.

*Proof.* Integrating the adjoint formula against $\pi$ gives $\int\pi(dy)P^*g(y)=\int\pi(dx)(Pg)(x)$, so $\pi P^*=\pi P=\pi$; the constant is fixed because $\int\hat p(y,dx)=1$. A function is harmonic for $P^*$ exactly when it is harmonic for the reversed chain $\hat p$, and the two chains have the same harmonic functions exactly when they coincide, that is when the chain is reversible.

### Products, powers and the spectrum

**Theorem.** The adjoint satisfies
$$
(PQ)^*=Q^*P^*,\qquad (P^n)^*=(P^*)^n,\qquad (\lambda P+\mu Q)^*=\bar\lambda P^*+\bar\mu Q^*,
$$
and its spectrum is the complex conjugate of that of $P$,
$$
\operatorname{spec}(P^*)=\overline{\operatorname{spec}(P)}=\{\bar\lambda:\lambda\in\operatorname{spec}(P)\}.
$$

*Proof.* The first three identities are the general properties of the adjoint on a Hilbert space; the spectrum identity is the standard fact that the adjoint has the conjugated spectrum, since $P^*-\bar\lambda I=(P-\lambda I)^*$ is invertible if and only if $P-\lambda I$ is.

**Corollary (the real spectrum in the reversible case).** If the chain is reversible, $P^*=P$, the Markov operator is self-adjoint, its spectrum is real and contained in $[-1,1]$, and the eigenfunctions of distinct eigenvalues are orthogonal; these are the spectral consequences of *Reversible Markov Chains and Time Reversal*, earlier in this category, now read as a statement about the adjoint.

*Proof.* Self-adjointness is $P^*=P$, and the spectral theorem for a self-adjoint contraction gives the reality and the bound; the orthogonality is the general theorem for a self-adjoint operator.

### Self-adjointness and the detailed balance

**Theorem (reversibility as self-adjointness).** The chain is reversible with respect to $\pi$ exactly when $P^*=P$; equivalently, the adjoint is the identity of the reversal, and the reversed chain is the original.

*Proof.* By the formula, $P^*=P$ is the identity $\pi(x)p(x,y)=\pi(y)p(y,x)$ for the discrete case, which is the detailed balance; the general case is the same identity between the kernels. The statement is the operator form of the reversibility of *Reversible Markov Chains and Time Reversal*, earlier in this category.

## Unitarity and Measure Preservation

**Theorem (unitarity).** The Markov operator is unitary on $L^2(\pi)$, $P^*P=PP^*=I$, if and only if it is invertible with $\pi$ also stationary for the inverse; then $\hat p$ is the inverse kernel $p^{-1}$ in the sense that $\sum_z\hat p(x,z)p(z,y)=\delta_{xy}$, the chain is a bijection of the classes of positive $\pi$-measure, and the reversed chain is the inverse of the original.

*Proof.* A contraction with $P1=1$ is unitary exactly when it is invertible; the inverse of a Markov operator with $\pi$ stationary is again a Markov operator exactly when the transition is a bijection of the state space, and the reversed kernel is then the inverse, $\hat p=p^{-1}$, which is the statement $P^*=P^{-1}$.

**Theorem (measure preservation and the adjoint of the Koopman case).** If the chain is deterministic and $\pi$ is preserved by the map $T$, so that $p(x,\cdot)=\delta_{T(x)}$, then the Markov operator is the Koopman operator $U_Tf=f\circ T$ and its adjoint is $U_T^*=U_{T^{-1}}$ when $T$ is invertible, the operator of the reversed dynamics; for a non-invertible $T$ the adjoint is the transfer operator of $T$ with respect to $\pi$, which averages over the preimages.

*Proof.* The Koopman operator of $T$ is the composition; its adjoint for the $\pi$-invariant form is the composition with $T^{-1}$ when $T$ is invertible, and the general adjoint computes $\int f\circ T\,\bar g\,d\pi=\int f\,\overline{(U_T^*g)}\,d\pi$, which for the non-invertible $T$ is the conditional expectation over the preimage $\sigma$-algebra, the transfer operator. The Koopman operator is *The Koopman Operator*, written, and the transfer operator is *The Transfer Operator*, written.

## Comparison with the Involution

### The two structures

**Theorem (the involution on the elements and the adjoint on the operators).** The involution on the **elements** — the complex conjugation of the functions of *The Involution on the Algebra of Random Variables*, earlier in this category — and the adjoint on the **operators** are two structures on two levels; the adjoint $P\mapsto P^*$ is the involution of the operator algebra, whose systematic treatment is *The Involution on the Operator Algebra of a Process*, the next article of this category. They are linked by the defining relation $\langle Pf,g\rangle_\pi=\langle f,P^*g\rangle_\pi$ and are not the same operation: $P^*$ is neither $P$ nor the multiplication by the conjugate in general, and $P$ is self-adjoint exactly when the chain is reversible, a coincidence that is **proved** from the detailed balance and never assumed.

*Proof.* The conjugation is an anti-linear map on the functions, while the adjoint is an anti-linear anti-automorphism $P\mapsto P^*$ of the operator algebra for the form $\langle\cdot,\cdot\rangle_\pi$; the self-adjointness $P^*=P$ is the reversibility by the theorem above, and the reverse chain $\hat p$ exhibits the difference in the non-reversible case.

## Worked Examples

**Example (the two-state chain).** With $p(0,1)=a$, $p(1,0)=b$ and $\pi=(b,a)/(a+b)$, the adjoint has the reversed kernel $\hat p(0,1)=\pi(1)p(1,0)/\pi(0)=a$ and $\hat p(1,0)=b$, so $\hat p=p$ and the chain is self-adjoint for all $a,b$; the adjoint is the original.

**Example (the directed cycle).** On $\{1,2,3\}$ with $p(i,i+1)=1$ cyclically and uniform stationary measure, the reversed kernel is $p(i,i-1)=1$, the adjoint is the backwards cycle, and $P^*\ne P$; the adjoint is the complex conjugate in the eigenbasis of the cyclic shift, where the eigenvalues $1,e^{\pm2\pi i/3}$ become their conjugates.

**Example (the birth–death chain).** The birth–death chain is reversible by *Reversible Markov Chains and Time Reversal*, earlier in this category, so $P^*=P$; the self-adjointness is the detailed balance $\pi(n)b_n=\pi(n+1)a_{n+1}$ of the stationary measure.

**Example (the Koopman adjoint).** For the doubling map $T(x)=2x\bmod1$ on the circle with the Lebesgue measure, the Koopman operator $U_Tf=f\circ T$ has the adjoint $U_T^*g(x)=\frac12(g(x/2)+g((x+1)/2))$, the transfer operator, which averages over the two preimages; the adjoint is not the Koopman operator of any map, since $T$ is not invertible.

## Failure of the Degenerate Cases

The adjoint degenerates in four configurations. First, the adjoint is taken with respect to a **chosen** stationary measure, and the formula is meaningless without the choice; on a chain with several stationary measures each gives its own adjoint and its own reversal. Second, on the $\pi$-null parts of the state space the density $\pi(x)p(x,y)/\pi(y)$ is not defined, and the adjoint is determined only up to the null sets; the ambiguity is the same as in the definition of the reversed chain. Third, the reversible case is where the two structures coincide, and the temptation to assume the coincidence in general is the error the group contract forbids: the adjoint is not the involution, and the difference is the reversed chain. Fourth, the unitarity is a genuine restriction: the Markov operators that are not invertible, among them the transfer operators of the non-invertible maps, have a nontrivial adjoint and no inverse, and the spectrum is the conjugate rather than the reciprocal.

## Summary

The adjoint of the Markov operator with respect to the stationary measure $\pi$ and the form $\langle f,g\rangle_\pi$ is the Markov operator of the reversed chain,
$$
P^*g(y)=\frac{1}{\pi(y)}\int\pi(dx)p(x,dy)g(x)=\int\hat p(y,dx)g(x),\qquad \hat p(y,dx)=\frac{\pi(dx)p(x,dy)}{\pi(y)},
$$
so the adjoint reverses the transition, keeps the stationary measure and the constants, is again a Markov operator, and is involutive. It satisfies $(PQ)^*=Q^*P^*$, $(P^n)^*=(P^*)^n$ and $\operatorname{spec}(P^*)=\overline{\operatorname{spec}(P)}$; it is self-adjoint exactly when the chain satisfies the detailed balance and is reversible, in which case the spectrum is real and lies in $[-1,1]$; and it is unitary exactly when the chain is invertible, in which case the reversed chain is the inverse. The adjoint is the operator form of the reversal $r$ of the path space, and it is distinct from the involution on the operator algebra of a process, *The Involution on the Operator Algebra of a Process*, the next article of this category, with which it coincides precisely on the reversible operators. The adjoint of the transition operator is *The Adjoint of the Transition Operator*, later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$, $Pf(x)=\int p(x,dy)f(y)$ | the Markov operator |
| $\langle f,g\rangle_\pi=\int f\bar g\,d\pi$ | the stationary form |
| $P^*$, $\langle Pf,g\rangle_\pi=\langle f,P^*g\rangle_\pi$ | the adjoint |
| $\hat p(x,dy)=\pi(dy)p(y,dx)/\pi(dx)$ | the reversed kernel |
| $P^*=\hat P$ | the adjoint is the reversed chain |
| $P^*=P\iff$ detailed balance | reversibility as self-adjointness |
| $(P^n)^*=(P^*)^n$, $\operatorname{spec}(P^*)=\overline{\operatorname{spec}(P)}$ | powers and spectrum |
| $P^*=P^{-1}$ | unitarity and invertibility |

## Further Reading

- David A. Levin, Yuval Peres and Elizabeth L. Wilmer, *Markov Chains and Mixing Times* (American Mathematical Society, 2nd edition, 2017), for the reversibility, the adjoint and the reversed chain.
- J. R. Norris, *Markov Chains* (Cambridge University Press, 1997), for the transitions, the stationarity and the reversal.
- Martin L. Silverstein, *Symmetric Markov Processes* (Springer, 1974), for the symmetric semigroups and their adjoints.
- Andrzej Lasota and Michael C. Mackey, *Chaos, Fractals, and Noise* (Springer, 2nd edition, 1994), for the transfer operators and the adjoints of the non-invertible maps.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the adjoints, the self-adjointness and the spectrum.
