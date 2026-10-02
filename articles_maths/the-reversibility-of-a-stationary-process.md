
# __The Reversibility of a Stationary Process__

## Introduction

A stationary process is **reversible** when the operation of reading it backwards in the index leaves its law unchanged, that is when the law on the path space is invariant under the involution
$$
r:E^{\mathbb Z}\to E^{\mathbb Z},\qquad (r\omega)_n=\omega_{-n},
$$
which sends the process $\{X_n\}$ to the process $\{X_{-n}\}$. The reversal is the involution on the elements at the level of the process, and the article studies what it forces and what it does not: the covariance function of a reversible process is symmetric, $R(-n)=R(n)$, hence real, and its spectral measure is invariant under the reflection $\lambda\mapsto-\lambda$; conversely the symmetry of the covariance need not imply the reversibility, the gap being filled exactly by the Gaussian processes, for which a real stationary process is always reversible because its law is determined by the covariance. The article states the definition, proves the necessary conditions on the covariance and the spectral measure, establishes the Gaussian criterion, and places the Markov case, where the reversibility is the detailed balance of the preceding article and is a genuine restriction.

The process theory is fixed elsewhere. The stationary processes, their spectral theory, the shift and the ergodicity are *Ergodic Theory*, written; the covariance function, its Hermitian symmetry and its positive-definiteness are *The Covariance Function and Hermitian Positivity*, later in this category, and the characteristic function is *The Characteristic Function and Conjugate Symmetry*, later in this category; the shift operator is *The Shift Operator of a Process*, earlier in this category; the reversibility of a Markov chain, with the detailed balance and the self-adjointness of the Markov operator, is *Reversible Markov Chains and Time Reversal*, the preceding article, and the adjoint operator is *The Adjoint of the Markov Operator*, later in this category. The Gaussian variables and their densities are *Independence and Conditional Expectation* and *Measure-Theoretic Probability*, written. No physics is invoked; the index is called time in the sense fixed by the theory of processes and carries no physical content.

Throughout, $\{X_n\}_{n\in\mathbb Z}$ is a stationary process with values in a measurable space $E$, with law $\mu$ on the path space $E^{\mathbb Z}$, and $\mathbb E$ is the expectation. The process is complex-valued unless it is called real; the covariance function is
$$
R(n)=\mathbb E\bigl[X_nX_0^*\bigr],
$$
the pairing of two random variables is $\langle X,Y\rangle=\mathbb E[XY^*]$, and the reversal is $r$. The spectral measure is the positive measure $\mu_R$ on the circle $\mathbb T=\mathbb R/2\pi\mathbb Z$ of the Herglotz theorem.

## Time Reversal of a Stationary Process

### Definition

**Definition.** The stationary process $\{X_n\}$ is **reversible** if its law is invariant under the reversal,
$$
\mu\circ r^{-1}=\mu ,
$$
equivalently, if the finite-dimensional distributions satisfy
$$
(X_{n_1},\dots,X_{n_k})\overset{d}{=}(X_{-n_1},\dots,X_{-n_k})
$$
for every choice of the indices. The **reversed process** is $\{X_{-n}\}$.

**Theorem (reversal preserves stationarity).** The reversed process is stationary, and the reversal commutes with the shift in the sense $r\sigma=\sigma^{-1}r$. The process is reversible exactly when the law of the reversed process equals the law of the original.

*Proof.* The stationarity of $\{X_{-n}\}$ is the stationarity of the original read on the reversed index; the commutation is $r(\sigma\omega)_n=(r\sigma\omega)_n=\omega_{-n-1}$ and $(\sigma^{-1}r\omega)_n=(r\omega)_{n+1}=\omega_{-n-1}$, the same. The last statement is the definition.

### The reversal of a Gaussian process

**Theorem (the Gaussian process).** Let $\{X_n\}$ be a real stationary Gaussian process with mean $m$ and covariance $R$. Then $R$ is even, $R(-n)=R(n)$, and the process is reversible; more generally a Gaussian stationary process, real or complex, is reversible if and only if the reversal of its mean and covariance coincides with the original.

*Proof.* A Gaussian process is determined by its mean and its covariance; the reversed process has the mean $m'$ with $m'_n=m_{-n}=m$ by stationarity and the covariance $R'(n)=R(-n)$. For a real process $R(-n)=\mathbb E[X_{-n}X_0]=\mathbb E[X_0X_n]=R(n)$, so the reversed process has the same mean and covariance, hence the same law, hence the process is reversible. In the complex case the same argument applies to the full Hermitian covariance and the relation, and the criterion is the coincidence of the two.

## The Covariance Function

### Hermitian symmetry

**Theorem (Hermitian symmetry).** For every stationary process the covariance is Hermitian,
$$
R(-n)=\overline{R(n)},
$$
and the covariance is positive definite:
$$
\sum_{i,j=1}^k c_i\overline{c_j}\,R(n_i-n_j)\ge0
$$
for all indices $n_i$ and complex scalars $c_i$.

*Proof.* Hermitian symmetry is $R(-n)=\mathbb E[X_{-n}X_0^*]=\mathbb E[X_0X_n^*]=\overline{\mathbb E[X_nX_0^*]}=\overline{R(n)}$, the middle step being the stationarity; the positive-definiteness is the variance of the linear combination, $\mathbb E\bigl[|\sum_ic_iX_{n_i}|^2\bigr]\ge0$. The covariance function and its positivity are *The Covariance Function and Hermitian Positivity*, later in this category.

### Symmetry under reversal

**Theorem (reversibility forces a symmetric covariance).** If the process is reversible then
$$
R(-n)=R(n)\qquad\text{for all } n,
$$
so the covariance is a real and even function of the index. Equivalently, the covariance matrix of every finite window is symmetric under the reflection of the index.

*Proof.* Reversibility gives $(X_0,X_n)\overset{d}{=}(X_n,X_0)$, hence $R(n)=\mathbb E[X_nX_0^*]=\mathbb E[X_0X_n^*]=R(-n)$; combined with the Hermitian symmetry, $R(n)=\overline{R(n)}$, so $R(n)$ is real. The finite-window statement is the same computation applied to the matrix entries.

**Corollary (the converse fails).** A stationary process with a real and even covariance need not be reversible; the symmetry of the covariance is necessary and not sufficient.

*Proof.* The stationary three-state cycle of *Reversible Markov Chains and Time Reversal*, the preceding article, is a stationary process whose covariance is real and even, being that of a real-valued chain, and which is not reversible, because its finite-dimensional distributions are not invariant under the reversal of the index; the circulation of the chain is the obstruction, and it is invisible in the covariance.

## The Spectral Measure

### The Herglotz representation

**Theorem (Herglotz).** A function $R:\mathbb Z\to\mathbb C$ is the covariance function of a stationary process if and only if it is positive definite, and then there is a unique finite positive measure $\mu_R$ on the circle with
$$
R(n)=\int_{\mathbb T}e^{in\lambda}\,d\mu_R(\lambda).
$$

*Proof.* The necessity is the positive-definiteness of the covariance; the sufficiency and the representation are the Herglotz theorem, the spectral theorem for the shift on the cyclic subspace generated by $X_0$. The measure $\mu_R$ is the spectral measure of the process, and the whole spectral theory is *Ergodic Theory*.

### The reality of the spectral measure

**Theorem (reversal and the spectral measure).** The covariance is real and even if and only if the spectral measure is invariant under the reflection $\lambda\mapsto-\lambda$,
$$
\mu_R(A)=\mu_R(-A)\qquad\text{for every } A .
$$
Consequently a reversible process has a symmetric spectral measure, and the spectral measure of a reversible process is determined by its values on the half-circle.

*Proof.* If $\mu_R$ is invariant under $\lambda\mapsto-\lambda$ then $R(-n)=\int e^{-in\lambda}d\mu_R=\int e^{in\lambda}d\mu_R(-(\lambda))=\int e^{in\lambda}d\mu_R=R(n)$, so $R$ is even and, with the Hermitian symmetry, real. Conversely an even real $R$ gives $\int e^{in\lambda}d[\mu_R-\tilde\mu_R]=0$ for the reflected measure $\tilde\mu_R(A)=\mu_R(-A)$ and all $n$, whence $\mu_R=\tilde\mu_R$ by the uniqueness in the Herglotz theorem.

**Corollary (the spectral meaning of reversibility).** A reversible process has a covariance that is the cosine transform of a symmetric measure, $R(n)=\int_{\mathbb T}\cos(n\lambda)\,d\mu_R(\lambda)$; its spectral measure carries no information about the sign of the frequency, and the one-sided spectral measure of the analytic-signal theory is not available.

*Proof.* Substituting the invariance into the Herglotz representation and using that $R$ is even, the integral of the sine vanishes and the cosine remains; the second statement is the reading of the symmetry.

## The Gaussian and the Markov Cases

**Theorem (the Gaussian criterion).** A Gaussian stationary process is reversible if and only if the covariance is symmetric under the reversal, that is if and only if $R(-n)=R(n)$ for all $n$. For a real Gaussian process this is automatic, so every real stationary Gaussian process is reversible.

*Proof.* The law of a Gaussian process is determined by the mean and the covariance, the stationary mean is constant and invariant under the reversal, and the reversed covariance is $R(-n)$; the two laws coincide exactly when the covariances do. The automatic symmetry in the real case is the theorem of the Gaussian section above.

**Theorem (the Markov criterion).** A stationary Markov chain is reversible, in the sense of the invariance of its law under the reversal, if and only if its transition kernel satisfies the detailed balance identity $\pi(x)p(x,y)=\pi(y)p(y,x)$; equivalently, if and only if the Markov operator is self-adjoint on $L^2(\pi)$.

*Proof.* This is the equivalence of *Reversible Markov Chains and Time Reversal*, the preceding article: the reversed chain is the kernel $\hat p(x,y)=\pi(y)p(y,x)/\pi(x)$, the law of the backwards chain is that of the forwards chain under $\hat p$, and the invariance of the law under $r$ is $\hat p=p$.

## Worked Examples

**Example (the real Gaussian process).** Let $\{X_n\}$ be real stationary Gaussian with covariance $R(n)=\rho^{|n|}$ for $\rho\in(-1,1)$. The covariance is even, the spectral measure is the symmetric density $\frac{1}{2\pi}\frac{1-\rho^2}{|1-\rho e^{i\lambda}|^2}$ on the circle, and the process is reversible by the Gaussian criterion; no computation of the finite-dimensional laws beyond the covariance is required.

**Example (the complex Gaussian process).** Let $X_n=Z\,e^{in\theta}$ with $Z$ a standard complex Gaussian and $\theta$ fixed. The process is stationary with $R(n)=e^{in\theta}$, which is Hermitian but not real unless $\theta\in\{0,\pi\}$; the reversal sends $X_n$ to $Z e^{-in\theta}$, a different process unless $\theta\in\{0,\pi\}$, so the reversibility fails and the covariance detects it. This is the boundary at which the covariance symmetry becomes a genuine condition.

**Example (the three-state cycle).** The stationary Markov chain on $\{1,2,3\}$ that moves cyclically is stationary with uniform measure and real covariance, and it is not reversible, the reversed chain running around the circle in the opposite direction; the covariance is even and real, and the non-reversibility is invisible in it. The example is the sharp statement that the covariance symmetry does not characterise the reversibility outside the Gaussian case.

**Example (the two-state chain).** The two-state chain is reversible for every transition probability by the preceding article, its covariance is a geometric sequence in $1-a-b$, real and even, and its spectral measure is symmetric; the reversibility is total in this family.

## Failure of the Degenerate Cases

The reversibility degenerates in four configurations. First, the symmetry of the covariance is only necessary for a general process, and the whole non-Gaussian information of the reversal sits in the higher moments; the covariance cannot see it. Second, a stationary process need not be determined by its covariance even when the covariance is real and even, so the Gaussian criterion does not extend, and the example of the cycle makes the failure explicit. Third, the spectral measure can be symmetric while the process is not reversible, for the same reason; the spectral symmetry is a statement about the second-order structure alone. Fourth, the reversal of a process indexed by $\mathbb R$ or by a group is a larger structure than the reversal of the index of a sequence, and the invariance of the law under the whole reversing group is a strictly stronger condition than the symmetry of the covariance; the group case is *Ergodic Theory of Group Actions*, later in this Part, and only the symmetry of the covariance survives from the present article to it.

## Summary

A stationary process is reversible when the law on its path space is invariant under the reversal $r$ of the index, equivalently when all its finite-dimensional distributions are invariant under the reversal of the indices, equivalently when the reversed process has the same law; the reversal commutes with the shift, $r\sigma=\sigma^{-1}r$. Reversibility forces the covariance to be symmetric, $R(-n)=R(n)$, hence real by the Hermitian symmetry $R(-n)=\overline{R(n)}$, and it forces the spectral measure of the Herglotz representation to be invariant under $\lambda\mapsto-\lambda$, so that $R(n)=\int\cos(n\lambda)d\mu_R$. The converse fails in general and holds in the Gaussian case, where the law is determined by the covariance: a real stationary Gaussian process is always reversible, and a complex one is reversible exactly when its covariance is real. For a stationary Markov chain the reversibility is the detailed balance of the preceding article and the self-adjointness of the Markov operator. The covariance function and its positivity are *The Covariance Function and Hermitian Positivity*, later in this category, and the spectral theory is *Ergodic Theory*, written.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $r$, $(r\omega)_n=\omega_{-n}$ | the reversal of the path space |
| $r\sigma=\sigma^{-1}r$ | the reversal intertwines the shift with its inverse |
| $R(n)=\mathbb E[X_nX_0^*]$ | the covariance function |
| $R(-n)=\overline{R(n)}$ | Hermitian symmetry |
| $R(-n)=R(n)$ | the covariance symmetry forced by reversibility |
| $\mu_R$, $R(n)=\int e^{in\lambda}d\mu_R$ | the spectral measure, Herglotz |
| $\mu_R(A)=\mu_R(-A)$ | the symmetry of the spectral measure |
| $R(n)=\int\cos(n\lambda)d\mu_R$ | the cosine form for a reversible process |

## Further Reading

- Ulf Grenander and Murray Rosenblatt, *Statistical Analysis of Stationary Time Series* (Wiley, 1957), for the covariance, the spectral measure and the Gaussian case.
- Norbert Wiener, *Extrapolation, Interpolation, and Smoothing of Stationary Time Series* (MIT Press, 1949), for the spectral theory of stationary processes.
- I. A. Ibragimov and Yuri A. Rozanov, *Gaussian Random Processes* (Springer, 1978), for the Gaussian laws determined by their covariances.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the shift and the spectral theory of the Koopman operator.
- Frank Spitzer, *Principles of Random Walk* (Springer, 2nd edition, 1976), for the reversible and the cyclic Markov examples.
