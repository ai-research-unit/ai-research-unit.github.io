
# __The Covariance Function and Hermitian Positivity__

## Introduction

The **covariance function** of a family of random variables records the pairing of the family with itself in the form of the category,
$$
R(s,t)=\varphi\bigl(X_sX_t^*\bigr)=\langle X_s,X_t\rangle ,
$$
the expectation form of *The Involution on the Algebra of Random Variables*, the preceding article. Its two structural properties are the **Hermitian symmetry** $R(s,t)=\overline{R(t,s)}$ and the **positive definiteness**
$$
\sum_{i,j=1}^k c_i\,\overline{c_j}\,R(t_i,t_j)\ge0 ,
$$
which together say that $R$ is the Gram matrix of the family in the Hilbert space of the theory. The article develops the covariance function from that point of view: it defines the covariance and its operator, proves the Hermitian symmetry, the Cauchy–Schwarz inequality and the positive definiteness, proves the realization theorem that every Hermitian positive-definite kernel is the covariance of a family (the Gelfand–Naimark–Segal construction followed by the Kolmogorov extension), specialises to the stationary case, where the covariance depends on the differences of the indices and the **Herglotz–Bochner theorem** identifies the stationary covariance functions with the Fourier transforms of the positive measures, and compares the covariance with the general form of the category.

The conventions are those of *The Involution on the Algebra of Random Variables*, the preceding article: the algebra of random variables $L^\infty(\Omega,\mathcal F,\mathbb P)$, the conjugation $x^*=\bar x$, the state $\varphi(x)=\mathbb E[x]$ and the form $\langle x,y\rangle=\varphi(xy^*)$ on $\mathcal{H}=L^2(\Omega,\mathbb P)$, all faithful and positive definite. The realization of a process from its finite-dimensional laws is the Kolmogorov extension, *Measure-Theoretic Probability*, written; the Gaussian laws determined by their covariances are *Independence and Conditional Expectation*, written; the Gram matrices, the positive operators and the Hilbert space geometry are *Banach and Hilbert Spaces*, written; the spectral theory of the stationary processes and the Herglotz representation are *Ergodic Theory*, written, and the reversibility consequences of the covariance symmetry are *The Reversibility of a Stationary Process*, earlier in this category. The Fourier transform of the law, its conjugate symmetry and its positive-definiteness are *The Characteristic Function and Conjugate Symmetry*, the next article. No physics is invoked.

Throughout, $T$ is an index set, $\{X_t\}_{t\in T}$ is a family of complex random variables in $L^2(\Omega,\mathbb P)$ with means $m_t=\varphi(X_t)$, and the covariance is taken centred, $R(s,t)=\varphi\bigl((X_s-m_s)(X_t-m_t)^*\bigr)$, or without centring where the context makes the means zero. The Hilbert space is $\mathcal{H}=L^2(\Omega,\mathbb P)$ with the form of the category, the covariance operator is $C$ on the closed span of the family, and for $T=\mathbb Z$ or $T=\mathbb R$ the stationary covariance is written $R(t-s)$.

## The Covariance Function

### Definition and the covariance operator

**Definition.** The **covariance function** of the family is
$$
R(s,t)=\varphi\bigl((X_s-m_s)(X_t-m_t)^*\bigr)=\bigl\langle X_s-m_s,\ X_t-m_t\bigr\rangle ,
$$
and the **covariance operator** is the linear operator on the closed span of the centred family with
$$
\langle C f,g\rangle=\sum_{i,j}\overline{c_i}\,d_j\,R(t_i,t_j)\qquad\text{for } f=\sum_ic_i(X_{t_i}-m_{t_i}),\ g=\sum_jd_j(X_{t_j}-m_{t_j}).
$$

### Hermitian symmetry and Cauchy–Schwarz

**Theorem.** The covariance is Hermitian,
$$
R(s,t)=\overline{R(t,s)},
$$
it satisfies the Cauchy–Schwarz inequality
$$
|R(s,t)|^2\le R(s,s)\,R(t,t),
$$
and $R(t,t)=\varphi(|X_t-m_t|^2)=\operatorname{Var}(X_t)\ge0$, so the diagonal is real and nonnegative.

*Proof.* The Hermitian symmetry is the anti-linearity of the form in the second argument, $R(t,s)=\langle X_t,X_s\rangle=\overline{\langle X_s,X_t\rangle}$; the Cauchy–Schwarz inequality is the general inequality for a positive-definite form on the two vectors; the diagonal is the variance.

### Positive definiteness

**Theorem (positive definiteness).** For every finite set of indices $t_1,\dots,t_k$ and complex scalars $c_1,\dots,c_k$,
$$
\sum_{i,j=1}^k c_i\,\overline{c_j}\,R(t_i,t_j)=\varphi\Bigl(\Bigl|\sum_ic_i(X_{t_i}-m_{t_i})\Bigr|^2\Bigr)\ge0 ,
$$
so $R$ is a **positive-definite** kernel, and the matrix $(R(t_i,t_j))$ is positive semi-definite Hermitian. The kernel is positive definite in the strict sense: the double sum vanishes exactly when $\sum_ic_i(X_{t_i}-m_{t_i})=0$ in $\mathcal{H}$, because the form of the category is positive definite, which is the faithfulness of the state established in the preceding article.

*Proof.* The double sum is the squared norm of the linear combination in $\mathcal{H}$, hence nonnegative; the identification of the vanishing locus is the positive definiteness of the form of the category, which is the faithfulness of the state, established in the preceding article.

## The Realization Theorem

### The GNS construction and the Gram matrix

**Theorem (realization).** Let $R:T\times T\to\mathbb{C}$ be Hermitian and positive definite and let $m:T\to\mathbb{C}$. Then there are a probability space $(\Omega,\mathcal F,\mathbb P)$ and a family $\{X_t\}_{t\in T}$ of random variables with means $m_t$ and covariance $R$; the family is realised as the vectors $x_t$ of the Gelfand–Naimark–Segal space of the kernel, $X_t=m_t+\pi(x_t)$ on the GNS space, and $R$ is the Gram matrix, $R(s,t)=\langle x_s,x_t\rangle$.

*Proof.* Form the free vector space on $T$ with the sesquilinear form $\langle x_s,x_t\rangle=R(s,t)$; the positive definiteness makes the form an inner product after the quotient by the null vectors, and the completion is a Hilbert space $\mathcal{K}$ with the coordinate vectors $x_t$ satisfying the Gram conditions. The von Neumann algebra generated by the coordinate multiplication on $\mathcal{K}$ with the vector state $\varphi(z)=\langle z\mathbf 1,\mathbf 1\rangle$ provides the algebra of random variables and the state; the passage to a genuine probability space, when $T$ is countable and $R$ is measurable, is the Kolmogorov extension applied to the finite-dimensional laws. The construction is the commutative case of the GNS construction of *Non-Commutative Probability and the Involutive Algebra of Random Variables*, earlier in this category.

**Corollary (the covariance is the form).** The covariance function of a family is exactly the restriction to the family of the form of the category; two families have the same covariance exactly when their centred spans are isometric in $L^2(\Omega,\mathbb P)$, and the covariance operator is the restriction of the multiplication in the sense of the Gram operator of the family.

*Proof.* The identification $R(s,t)=\langle X_s,X_t\rangle$ is the definition, and the isometry of the spans is the standard statement that the Gram matrix determines the inner-product geometry of a spanning set.

### The extension of the laws

**Theorem (Kolmogorov).** Let $T=\mathbb Z$ or $T=\mathbb R$ and let $\{R(s,t)\}$ be a Hermitian positive-definite kernel with a compatible family of finite-dimensional marginal laws $\mu_{t_1,\dots,t_k}$; then there is a probability space with a process whose finite-dimensional laws are the $\mu_{t_1,\dots,t_k}$, unique up to equality of the laws. For the Gaussian family the laws are determined by the kernel and the means, and the realization of the kernel alone yields a Gaussian process with that covariance.

*Proof.* The consistency of the marginals and the Kolmogorov extension theorem give the process on the product space with the cylinder $\sigma$-algebra; the Gaussian case is the statement that the finite-dimensional Gaussian laws are determined by the mean vector and the covariance matrix, which is *Independence and Conditional Expectation*.

## The Stationary Case and Bochner

### The stationary covariance

**Definition.** For $T=\mathbb Z$ or $T=\mathbb R$ the covariance is **stationary** if it depends only on the difference, $R(s,t)=R(t-s)$; equivalently the family is stationary in the second order.

**Theorem.** A stationary covariance function $R$ is Hermitian, $R(-t)=\overline{R(t)}$, positive definite, and bounded,
$$
|R(t)|\le R(0),\qquad R(0)=\operatorname{Var}(X_0)\ge0 .
$$

*Proof.* The Hermitian symmetry of the general covariance becomes $R(-t)=\overline{R(t)}$, and the positive definiteness is the positive definiteness of the function on the group $\mathbb Z$ or $\mathbb R$; the bound is the Cauchy–Schwarz inequality with the stationarity, $|R(t)|\le R(0)$.

### Herglotz and Bochner

**Theorem (Herglotz).** A function $R:\mathbb Z\to\mathbb{C}$ is the stationary covariance of some process if and only if it is positive definite, and then there is a unique finite positive measure $\mu$ on the circle with
$$
R(n)=\int_{\mathbb T}e^{in\lambda}\,d\mu(\lambda),\qquad R(0)=\mu(\mathbb T).
$$

**Theorem (Bochner).** A continuous function $R:\mathbb R\to\mathbb{C}$ is positive definite if and only if it is the Fourier transform of a unique finite positive measure,
$$
R(t)=\int_{\mathbb R}e^{it\lambda}\,d\mu(\lambda),
$$
and the measure is the **spectral measure** of the stationary process.

*Proof.* The two theorems are the spectral theory of the unitary representation of $\mathbb Z$ and of $\mathbb R$ by the shift, or by the translation; the positive definiteness is precisely the positivity of the spectral measure in the Gelfand–Raikov–Godement construction, and the uniqueness is the uniqueness of the Fourier transform. The proofs are *Ergodic Theory*, written, for the Herglotz case, and the classical Bochner theorem for the continuous case. The symmetry of the spectral measure under $\lambda\mapsto-\lambda$ and its relation to the reversibility are *The Reversibility of a Stationary Process*, earlier in this category.

**Corollary (the spectral form of the variance).** For a stationary covariance, $R(0)=\mu(\mathbb R)$ and
$$
\operatorname{Var}\Bigl(\sum_ic_iX_{t_i}\Bigr)=\int_{\mathbb R}\Bigl|\sum_ic_ie^{it_i\lambda}\Bigr|^2d\mu(\lambda)\ge0 ,
$$
a nonnegative trigonometric polynomial integrated against the positive spectral measure.

*Proof.* The variance of the trigonometric polynomial of the shifts is the squared norm in $L^2(\mu)$ of the symbol $\sum_ic_ie^{it_i\lambda}$ by the Bochner representation.

## Worked Examples

**Example (the white noise).** The covariance $R(s,t)=\delta_{s,t}$ is Hermitian and positive definite, with the spectral measure the Lebesgue measure of total mass one on the circle; the realization is the family of the orthonormal vectors of a Hilbert space, and the process is the white noise of unit variance. The covariance operator is the identity.

**Example (the Gaussian kernel).** The function $R(t)=e^{-t^2/2}$ on $\mathbb R$ is continuous and positive definite, and its Fourier transform is the standard normal density; the realization is the stationary Gaussian process with that covariance, whose spectral measure is the normal law. This is the Bochner theorem in its smoothest instance.

**Example (the Fejér kernel).** The function $R(n)=\bigl(1-|n|/N\bigr)_+$ on $\mathbb Z$, the triangular window of width $N$, is positive definite, its spectral density being the Fejér kernel $\frac{1}{2\pi N}\bigl(\frac{\sin(N\lambda/2)}{\sin(\lambda/2)}\bigr)^2$, the squared modulus of the Dirichlet kernel divided by $N$; the example shows that the positive definiteness is not a decay condition.

**Example (a non-positive-definite function).** The function $R(n)=\mathbf 1_{|n|\le1}$ is Hermitian and bounded but not positive definite: for the indices $-1,0,1$ the matrix $(R(t_i-t_j))$ is $\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}$, whose eigenvalues are $1$, $1+\sqrt2$ and $1-\sqrt2<0$. Hence it is not a covariance function, and no stationary process has it as its covariance. The example exhibits the content of the positive definiteness.

**Example (the Ornstein–Uhlenbeck kernel).** The function $R(t)=e^{-\alpha|t|}$ on $\mathbb R$ is continuous and positive definite, with the spectral measure the Cauchy density $\frac{\alpha}{\pi(\alpha^2+\lambda^2)}d\lambda$; the realization is the stationary Ornstein–Uhlenbeck process, whose reversibility and self-adjoint generator are *Reversible Markov Chains and Time Reversal*, earlier in this category.

## Failure of the Degenerate Cases

The covariance degenerates in four configurations. First, the Hermitian symmetry alone is not enough: a Hermitian kernel can fail the positive definiteness, as the interval indicator above shows, and the failure is exactly the failure of the Gram matrix to come from vectors. Second, the covariance determines only the second-order structure, and two processes with the same covariance can have different laws; the Gaussian family is where the determination is complete, and outside it the covariance is only a shadow. Third, the realization of an arbitrary positive-definite kernel gives a family on a Hilbert space and not automatically on a standard probability space; the passage to a stochastic process requires measurability and the Kolmogorov extension, which is where the countability or the regularity of the index enters. Fourth, the stationary covariance functions are the positive-definite functions of the group and not all of them are continuous, for a general index group; Bochner's theorem gives the continuous ones and their spectral measures, and the non-continuous ones are handled by the spectral theory of the unitary groups, *Ergodic Theory*, written, together with *Banach and Hilbert Spaces*, written.

## Summary

The covariance function of a family of random variables is the pairing $R(s,t)=\varphi\bigl((X_s-m_s)(X_t-m_t)^*\bigr)$ in the form of the category; it is Hermitian, $R(s,t)=\overline{R(t,s)}$, it satisfies the Cauchy–Schwarz inequality $|R(s,t)|^2\le R(s,s)R(t,t)$, and it is positive definite, the double sum $\sum c_i\bar c_jR(t_i,t_j)$ being the squared norm of the combination $\sum c_i(X_{t_i}-m_{t_i})$. Conversely every Hermitian positive-definite kernel is the covariance of some family, realised as the coordinate vectors of its GNS space, with the passage to a stochastic process by the Kolmogorov extension and the Gaussian determination of the law by the covariance. In the stationary case the covariance depends on the difference, it is bounded, $|R(t)|\le R(0)$, and the Herglotz and Bochner theorems identify the stationary covariance functions of $\mathbb Z$ and of $\mathbb R$ with the Fourier transforms of the finite positive spectral measures. The function and its positivity also carry the reversibility of the process and the conjugate symmetry of the law, which are *The Reversibility of a Stationary Process*, earlier in this category, and *The Characteristic Function and Conjugate Symmetry*, the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R(s,t)=\varphi\bigl((X_s-m_s)(X_t-m_t)^*\bigr)$ | the covariance function |
| $R(s,t)=\overline{R(t,s)}$ | Hermitian symmetry |
| $|R(s,t)|^2\le R(s,s)R(t,t)$ | Cauchy–Schwarz |
| $\sum c_i\bar c_jR(t_i,t_j)\ge0$ | positive definiteness |
| $C$ | the covariance operator, the Gram operator of the family |
| $R(-t)=\overline{R(t)}$, $|R(t)|\le R(0)$ | the stationary covariance |
| $R(n)=\int_{\mathbb T}e^{in\lambda}d\mu$ | Herglotz representation |
| $R(t)=\int_{\mathbb R}e^{it\lambda}d\mu$ | Bochner representation |
| $\mu$ | the spectral measure of the stationary process |

## Further Reading

- Harald Cramér and Herman Wold, *Stationary and Related Stochastic Processes* (Wiley, 1967), for the covariance, the spectral representation and the stationary theory.
- Norbert Wiener, *Extrapolation, Interpolation, and Smoothing of Stationary Time Series* (MIT Press, 1949), for the spectral measure and the covariance.
- I. A. Ibragimov and Yuri A. Rozanov, *Gaussian Random Processes* (Springer, 1978), for the Gaussian determination by covariance.
- Salomon Bochner, *Lectures on Fourier Integrals* (Princeton University Press, 1959), for the Bochner theorem and the positive-definite functions.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd edition, 1990), for the Gram matrices, the positive operators and the spectrum.
