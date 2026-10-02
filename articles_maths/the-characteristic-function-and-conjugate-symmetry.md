
# __The Characteristic Function and Conjugate Symmetry__

## Introduction

The **characteristic function** of a random variable is the Fourier transform of its law,
$$
\phi_X(t)=\mathbb E\bigl[e^{itX}\bigr]=\int_{\mathbb R}e^{itx}\,d\mu_X(x),
$$
the functional that converts the convolution of the laws into the product pointwise and the moments into the derivatives at the origin. Its defining structural property is the **conjugate symmetry**
$$
\phi_X(-t)=\overline{\phi_X(t)},
$$
which holds for every real random variable $X$ and is the counterpart, on the side of the law, of the Hermitian symmetry $R(s,t)=\overline{R(t,s)}$ of the covariance of *The Covariance Function and Hermitian Positivity*, the preceding article: on the side of the variable the involution is the complex conjugation $x^*=\bar x$ of *The Involution on the Algebra of Random Variables*, earlier in this category, and it produces the conjugate symmetry of the transform. The article defines the characteristic function, proves the conjugate symmetry and the positive definiteness, states the Bochner theorem that these two properties with the normalisation characterise the characteristic functions, identifies the reality of the characteristic function with the symmetry of the law, computes the moments and the cumulants as the derivatives of the function and of its logarithm, and derives the Hermitian symmetry of the covariance from the conjugate symmetry of the joint characteristic function.

The conventions are those of the category: the algebra of random variables $L^\infty(\Omega,\mathcal F,\mathbb P)$ with the conjugation $x^*=\bar x$, the state $\varphi(x)=\mathbb E[x]$ and the form $\langle x,y\rangle=\varphi(xy^*)$ of *The Involution on the Algebra of Random Variables*, earlier in this category. The law, its tightness and the weak convergence are *Measure-Theoretic Probability*, written; the independence and the Gaussian laws are *Independence and Conditional Expectation*, written; the Fourier transform, the inversion and the positive-definite functions are *Fourier Analysis and Distributions*, written, and *Banach and Hilbert Spaces*, written; the spectral measure of a stationary process, its Herglotz representation and its reality under reversibility are *Ergodic Theory*, written, and *The Reversibility of a Stationary Process*, earlier in this category. The covariance function and its Hermitian positivity are the preceding article. No physics is invoked.

Throughout, $X$ is a random variable with law $\mu_X$ on the real line, and $\phi_X(t)=\mathbb E[e^{itX}]$ is its characteristic function; for a pair $(X,Y)$ the joint characteristic function is $\phi_{X,Y}(s,t)=\mathbb E[e^{i(sX+tY)}]$. The moments are $m_n=\mathbb E[X^n]$ when they exist, the cumulants are the coefficients of the logarithm of the characteristic function, and the covariance is $R_{XY}=\varphi(XY)-\varphi(X)\varphi(Y)$.

## The Characteristic Function

### Definition and first properties

**Definition.** The **characteristic function** of $X$ is
$$
\phi_X(t)=\mathbb E\bigl[e^{itX}\bigr]=\varphi\bigl(e^{itX}\bigr)=\int_{\mathbb R}e^{itx}\,d\mu_X(x).
$$

**Theorem.** The characteristic function satisfies
$$
\phi_X(0)=1,\qquad |\phi_X(t)|\le1,\qquad \phi_X:\mathbb R\to\mathbb C\text{ is uniformly continuous},
$$
and it is the Fourier transform of the law. If $X$ and $Y$ are independent then
$$
\phi_{X+Y}=\phi_X\,\phi_Y ,
$$
and if $X$ has $n$ finite moments then $\phi_X$ is $n$ times differentiable and $\phi_X^{(k)}(0)=i^km_k$.

*Proof.* The normalisation and the bound follow from $e^{i0}=1$ and $|e^{itX}|=1$ with $|\varphi|\le\|\cdot\|_\infty$; the uniform continuity is the dominated convergence with the continuity of $t\mapsto e^{itX}$; the product formula is the multiplicativity of the expectation across independent factors; the differentiation under the expectation is the theorem on the derivatives of a Fourier transform with finite moments, giving $\phi_X^{(k)}(0)=i^k\mathbb E[X^k]$.

### Conjugate symmetry

**Theorem (conjugate symmetry).** For every real random variable $X$,
$$
\phi_X(-t)=\overline{\phi_X(t)}\qquad (t\in\mathbb R),
$$
that is, the characteristic function is **Hermitian** as a function on the line with the conjugation, and consequently its real part is even and its imaginary part is odd:
$$
\Re\phi_X(-t)=\Re\phi_X(t),\qquad \Im\phi_X(-t)=-\Im\phi_X(t).
$$

*Proof.* $e^{-itX}=\overline{e^{itX}}$, hence $\phi_X(-t)=\mathbb E[\overline{e^{itX}}]=\overline{\mathbb E[e^{itX}]}=\overline{\phi_X(t)}$, using the reality of $X$ in the step $\overline{X}=X$; the parity of the real and imaginary parts is the reading of the identity.

**Theorem (the joint symmetry).** For a pair of real random variables,
$$
\phi_{X,Y}(-s,-t)=\overline{\phi_{X,Y}(s,t)},
$$
so the joint characteristic function is Hermitian under the simultaneous reflection of the two variables, the reflection being the conjugation of the parameter in the same sense as above.

*Proof.* The same computation with $e^{-i(sX+tY)}=\overline{e^{i(sX+tY)}}$.

### Positive definiteness and Bochner

**Theorem (positive definiteness).** The characteristic function is positive definite:
$$
\sum_{i,j=1}^k c_i\,\overline{c_j}\,\phi_X(t_i-t_j)\ge0
$$
for all real $t_1,\dots,t_k$ and complex $c_1,\dots,c_k$.

*Proof.* The double sum is $\mathbb E\bigl[|\sum_ic_ie^{it_iX}|^2\bigr]\ge0$, since the exponential is a complex-valued random variable with modulus one and the expectation of a squared modulus is nonnegative.

**Theorem (Bochner).** A continuous function $\phi:\mathbb R\to\mathbb C$ with $\phi(0)=1$ is the characteristic function of a probability measure on $\mathbb R$ if and only if it is positive definite; the measure is then unique. The Hermitian symmetry is automatic for the transform of every finite real measure; the measure is **symmetric** under $x\mapsto-x$ exactly when $\phi$ is real.

*Proof.* The positive definiteness is necessary by the computation above and sufficient by the Bochner theorem, which constructs the measure as the spectral measure of the translation representation; the uniqueness is the Fourier inversion, which recovers the measure from the function. Every finite real measure has the Hermitian transform, $\hat\mu(-t)=\int e^{-itx}d\mu=\overline{\hat\mu(t)}$; the measure is invariant under $x\mapsto-x$ exactly when $\hat\mu$ is real, which is the computation of the next section.

## The Law and its Symmetries

### The reality of the characteristic function

**Theorem (reality and symmetry).** For a real random variable $X$, the characteristic function is real, $\phi_X(t)\in\mathbb R$ for all $t$, if and only if the law is symmetric, $X\overset{d}{=}-X$, that is if and only if $\mu_X(A)=\mu_X(-A)$ for every Borel $A$.

*Proof.* If $\phi_X$ is real then $\phi_X(t)=\overline{\phi_X(t)}=\phi_X(-t)=\phi_{-X}(t)$ for all $t$, so by the uniqueness of the characteristic function the laws of $X$ and $-X$ coincide, which is the symmetry. Conversely if $X\overset d=-X$ then $\phi_X(t)=\phi_{-X}(t)=\phi_X(-t)=\overline{\phi_X(t)}$, so $\phi_X$ is real. The symmetry of the law and the reality of the transform are the same statement seen from the two sides.

**Corollary (the law as a Fourier transform).** The law is recovered from the characteristic function by the inversion formula,
$$
\mu_X([a,b])=\lim_{T\to\infty}\frac{1}{2\pi}\int_{-T}^{T}\frac{e^{-ita}-e^{-itb}}{it}\,\phi_X(t)\,dt
$$
at the continuity points $a<b$ of the distribution function, and the characteristic function determines the law.

*Proof.* This is the Fourier inversion for the finite measure $\mu_X$; the convergence and the form of the kernel are the standard theorem, *Fourier Analysis and Distributions*, written.

### The moments and the cumulants

**Theorem (the moments).** If $\mathbb E|X|^n<\infty$ then
$$
\phi_X(t)=\sum_{k=0}^{n}\frac{(it)^k}{k!}m_k+o(t^n),\qquad m_k=i^{-k}\phi_X^{(k)}(0)=\frac{\phi_X^{(k)}(0)}{i^k},
$$
and $m_k$ is real for the real $X$.

*Proof.* The Taylor expansion of the exponential with the dominated convergence for the remainder gives the expansion; the reality of the moments is the reality of $X$ together with the reality of the state.

**Definition and Theorem (the cumulants).** The **cumulants** $\kappa_n$ are the coefficients of the expansion
$$
\log\phi_X(t)=\sum_{n\ge1}\kappa_n\frac{(it)^n}{n!},
$$
defined where the logarithm is analytic; for the sum of two independent variables the cumulants add, $\kappa_n(X+Y)=\kappa_n(X)+\kappa_n(Y)$, and the first cumulants are $\kappa_1=\mathbb E[X]$, $\kappa_2=\operatorname{Var}(X)$, $\kappa_3=\mathbb E[(X-\mathbb E X)^3]$.

*Proof.* The product formula $\phi_{X+Y}=\phi_X\phi_Y$ for the independent sum becomes the additivity under the logarithm, and the coefficients are the derivatives at the origin; the identifications of the first three cumulants are the expansions of the logarithm to the third order.

### The covariance and its Hermitian symmetry

**Theorem (the covariance from the joint characteristic function).** For a pair of real random variables with a finite second moment,
$$
R_{XY}=\operatorname{Cov}(X,Y)=-\frac{\partial^2}{\partial s\,\partial t}\log\phi_{X,Y}(s,t)\Big|_{s=t=0},
$$
and the covariance is Hermitian, $R_{XY}=\overline{R_{YX}}=R_{YX}$ in the real case, that is the Hermitian symmetry of *The Covariance Function and Hermitian Positivity*, the preceding article, is the shadow of the Hermitian symmetry of the joint characteristic function.

*Proof.* The mixed second derivative of the logarithm of the joint characteristic function at the origin is the mixed cumulant $\kappa_{1,1}=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]$, which is the covariance; the Hermitian symmetry of the covariance is the reality of the variables together with the commutation of the mixed partial derivatives, matching the Hermitian symmetry $\phi_{X,Y}(-s,-t)=\overline{\phi_{X,Y}(s,t)}$ of the joint function.

## Worked Examples

**Example (the Gaussian).** For $X$ normal with mean $m$ and variance $\sigma^2$ one has $\phi_X(t)=\exp\bigl(imt-\frac12\sigma^2t^2\bigr)$, which is Hermitian, real exactly when $m=0$, and whose logarithm has the two cumulants $\kappa_1=m$, $\kappa_2=\sigma^2$ and no others; the reality of $\phi_X$ for the centred Gaussian is the symmetry of the normal law.

**Example (the Bernoulli variable).** For $X$ taking the values $\pm1$ with equal probability, $\phi_X(t)=\cos t$ is real and even, and the law is symmetric; for $X$ taking the values $0$ and $1$ with probabilities $q$ and $p$, $\phi_X(t)=q+pe^{it}$, whose conjugate symmetry $\phi_X(-t)=\overline{\phi_X(t)}$ is visible and whose reality fails because the law is not symmetric.

**Example (the Cauchy variable).** For $X$ standard Cauchy, $\phi_X(t)=e^{-|t|}$, real and even, the law symmetric and without finite moments; the example shows that the reality of the characteristic function does not require the finiteness of any moment beyond the existence of the law.

**Example (the Poisson variable).** For $X$ Poisson of parameter $\lambda$, $\phi_X(t)=\exp(\lambda(e^{it}-1))$, Hermitian with the conjugate symmetry, not real; its logarithm has all the cumulants equal to $\lambda$, the additive structure of the Poisson law under the independent sum.

**Example (the stationary process).** For a stationary process the covariance is the inverse Fourier transform of the spectral measure, and the reality of the covariance under reversibility is the symmetry of the spectral measure; the conjugate symmetry of the characteristic functions of the finite windows is the same reality read on the laws, and the two are *The Reversibility of a Stationary Process*, earlier in this category.

## Failure of the Degenerate Cases

The characteristic function degenerates in four configurations. First, the conjugate symmetry is automatic for a real variable and therefore carries no information; the information is in the **reality** of the function, which is the symmetry of the law, and confusing the two is the standard error. Second, the positive definiteness is a genuine condition and not a consequence of the conjugate symmetry: the Hermitian function $t\mapsto\cosh t$ is not positive definite and is not a characteristic function, while $t\mapsto e^{-|t|}$ is both. Third, the Bochner theorem needs the continuity: a positive-definite function on $\mathbb R$ that is not continuous need not be the transform of any measure at all, and it is the continuity together with the normalisation $\phi(0)=1$ that produces the probability measure. Fourth, the logarithm of the characteristic function is analytic only where the function does not vanish, and the cumulants need not exist beyond the order at which the moments fail; the Cauchy variable has no cumulants at all, and the moment and cumulant expansions are local statements about the origin.

## Summary

The characteristic function of a random variable is the Fourier transform of its law, $\phi_X(t)=\mathbb E[e^{itX}]$, normalised by $\phi_X(0)=1$, bounded by one, uniformly continuous, multiplicative over independent sums and differentiable to the order of the finite moments, with $\phi_X^{(k)}(0)=i^km_k$. For every real variable it is **Hermitian**, $\phi_X(-t)=\overline{\phi_X(t)}$, and **positive definite**, $\sum c_i\bar c_j\phi_X(t_i-t_j)\ge0$; the Bochner theorem states that every continuous positive-definite function with the value one at the origin is the characteristic function of a unique probability measure, whose transform is Hermitian automatically and is real exactly when the measure is symmetric. The characteristic function is real exactly when the law is symmetric, $X\overset d=-X$; the law is recovered from it by the inversion formula; the cumulants are the coefficients of its logarithm and add under independent sums. The covariance is the mixed second cumulant of the joint characteristic function, and its Hermitian symmetry mirrors the Hermitian symmetry $\phi_{X,Y}(-s,-t)=\overline{\phi_{X,Y}(s,t)}$ of the joint function, which is the same conjugate symmetry as the one of the single variable. The covariance and its positivity are the preceding article, and the reality of the spectral measure under reversibility is *The Reversibility of a Stationary Process*, earlier in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\phi_X(t)=\mathbb E[e^{itX}]$ | the characteristic function |
| $\phi_X(0)=1$, $|\phi_X|\le1$ | normalisation and bound |
| $\phi_X(-t)=\overline{\phi_X(t)}$ | conjugate (Hermitian) symmetry |
| $\sum c_i\bar c_j\phi_X(t_i-t_j)\ge0$ | positive definiteness |
| $\phi_X$ real $\iff X\overset d=-X$ | reality and symmetry of the law |
| $\phi_{X+Y}=\phi_X\phi_Y$ | multiplicativity for independent sums |
| $m_k=i^{-k}\phi_X^{(k)}(0)$ | the moments |
| $\log\phi_X(t)=\sum\kappa_n(it)^n/n!$ | the cumulants |
| $R_{XY}=-\partial_s\partial_t\log\phi_{X,Y}|_0$ | the covariance as a mixed cumulant |

## Further Reading

- Eugene Lukacs, *Characteristic Functions* (Griffin, 2nd edition, 1970), for the characteristic functions, the positive definiteness and the inversion.
- Kai Lai Chung, *A Course in Probability Theory* (Academic Press, 3rd edition, 2001), for the characteristic functions, the moments and the weak convergence.
- William Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II (Wiley, 2nd edition, 1971), for the characteristic functions, the cumulants and the classical examples.
- Salomon Bochner, *Lectures on Fourier Integrals* (Princeton University Press, 1959), for the Bochner theorem and the positive-definite functions.
- David Williams, *Probability with Martingales* (Cambridge University Press, 1991), for the characteristic functions and the Fourier methods in probability.
