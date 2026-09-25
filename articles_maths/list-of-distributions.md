
# __List of Distributions__

## Introduction

This article lists the distributions and the generalised functions the corpus introduces. A distribution is a continuous linear functional on a space of test functions, so that the objects of the calculus — differentiation, multiplication, convolution, Fourier transformation — are defined by duality, and a row below names one distribution, records the operations it supports and the sense in which it is a generalised function, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The objects are grouped by the layer that introduces them: the distribution spaces and their duality, the distinguished distributions — the delta, the Heaviside function, the principal value and the finite part — the operations and their limits, the fundamental solutions and kernels, and the distributions of the $p$-adic, complex and hypercomplex grounds. The rows that record an operation which is not defined — the product of two distributions, the restriction without a transversality hypothesis, the Fourier transform of an untempered distribution — stand beside the distributions as non-examples.

## The Distribution Spaces

| Object | What it is dual to, and what that buys | Introduced in |
|---|---|---|
| a distribution $u \in \mathcal D'(\Omega)$ | the test functions $\mathcal D(\Omega) = C_c^\infty(\Omega)$ under the LF topology; all derivatives and all multiplications by smooth functions are defined | *Distributions and Fundamental Solutions* |
| a distribution of finite order | the dual of $C^k_c$ for some $k$; the smallest $k$ is the order | *Distributions and Fundamental Solutions* |
| a compactly supported distribution $u \in \mathcal E'(\Omega)$ | the dual of $C^\infty(\Omega)$; convolution with every distribution is defined | *Distributions and Fundamental Solutions* |
| a tempered distribution $u \in \mathcal S'(\mathbb R^n)$ | the Schwartz class $\mathcal S(\mathbb R^n)$; the Fourier transform is defined | *Distributions and Fundamental Solutions*; *Fourier Analysis on Euclidean Spaces* |
| a distribution of function type | a locally integrable function $f$, acting by $\varphi \mapsto \int f\varphi$; the embedding of $L^1_{loc}$ into $\mathcal D'$ | *Distributions and Fundamental Solutions* |
| a measure as a distribution | a Radon measure, acting by $\varphi \mapsto \int\varphi\,d\mu$; the continuous dual of $C_0$ is a subspace of $\mathcal D'$ | *Distributions and Fundamental Solutions*; *Locally Compact Groups and Haar Measure* |
| a positive distribution | the distribution associated to the measure it defines by the Riesz representation theorem | *Distributions and Fundamental Solutions* |
| the Schwartz kernel $K \in \mathcal D'(Y \times X)$ | the distribution representing a continuous operator $T : \mathcal D(X) \to \mathcal D'(Y)$; unique | *The Schwartz Kernel Theorem* |

## The Distinguished Distributions

| Object | Its definition, and the operations it supports | Introduced in |
|---|---|---|
| the delta distribution $\delta$ | $\langle\delta,\varphi\rangle = \varphi(0)$; differentiable, the convolution identity, Fourier transform $1$ | *Distributions and Fundamental Solutions* |
| the translated delta $\delta_a$ | $\langle\delta_a,\varphi\rangle = \varphi(a)$; the derivative of the Heaviside step at $a$ | *Distributions and Fundamental Solutions* |
| the derivatives $\partial^\alpha\delta$ | $\langle\partial^\alpha\delta,\varphi\rangle = (-1)^{|\alpha|}\partial^\alpha\varphi(0)$; the only distributions supported at a point are their finite combinations | *Distributions and Fundamental Solutions* |
| the Heaviside function $H$ | $H(x) = \mathbf 1_{x>0}$ as a distribution; its derivative is $\delta$ | *Distributions and Fundamental Solutions* |
| the principal value $\mathrm{pv}\,\frac1x$ | $\langle \mathrm{pv}\,\frac1x,\varphi\rangle = \lim_{\epsilon\to0}\int_{\lvert x\rvert>\epsilon}\frac{\varphi(x)}{x}dx$; the distributional derivative of $\log\lvert x\rvert$, with Fourier transform $-\pi i\,\mathrm{sgn}$ | *Distributions and Fundamental Solutions*; *Fourier Analysis on Euclidean Spaces* |
| the finite part $\mathrm{pf}\,\frac1{x^2}$ | the Hadamard regularisation of the divergent integral; it supports a derivative and a convolution with the Hilbert kernel | *Distributions and Fundamental Solutions* |
| the delta distribution of a hypercomplex system | the identity of the convolution algebra of the split-complex, dual-number, quaternion or biquaternion plane | *Split-Complex Harmonic Analysis*; *Dual-Numbers Harmonic Analysis*; *Quaternion Harmonic Analysis*; *Biquaternion Integration* |
| the delta distribution on a locally compact group | the identity $\delta_e$ of the convolution algebra of measures, together with the Haar measure | *Harmonic Analysis on Groups* |

## Operations and Their Limits

| Object | The operation it supports, and the limit of that operation | Introduced in |
|---|---|---|
| differentiation of a distribution | $\langle u',\varphi\rangle = -\langle u,\varphi'\rangle$; defined for every distribution and of no higher order than the distribution | *Distributions and Fundamental Solutions* |
| multiplication by a smooth function | $\langle au,\varphi\rangle = \langle u,a\varphi\rangle$; defined for $a \in C^\infty$ | *Distributions and Fundamental Solutions* |
| the product of two distributions | defined only when their wave front sets do not meet in a forbidden way; $\delta\cdot\delta$ and $\delta\cdot\mathrm{pv}\frac1x$ are not defined | *Distributions and Fundamental Solutions*; *Microlocal Analysis* |
| convolution with a test function | $u * \varphi$ is a smooth function, a mollification and approximation of $u$ | *Distributions and Fundamental Solutions* |
| convolution of two distributions | defined when one has compact support; it is commutative only under that hypothesis | *Distributions and Fundamental Solutions* |
| the Fourier transform of a tempered distribution | $\langle\hat u,\varphi\rangle = \langle u,\hat\varphi\rangle$; exchanges differentiation and multiplication | *Distributions and Fundamental Solutions*; *Fourier Analysis on Euclidean Spaces* |
| restriction and pullback | defined under a transversality condition on the wave front set; the trace on a boundary needs it | *Distributions and Fundamental Solutions*; *Microlocal Analysis* |
| the wave front set $\operatorname{WF}(u)$ | the refined singular support: the directions in which $u$ fails to be smooth; the product and the pullback are governed by it | *Microlocal Analysis* |
| the order and the singular support | the structure theorem: a distribution of finite order is a sum of derivatives of measures | *Distributions and Fundamental Solutions* |

## Fundamental Solutions, Parametrices and Kernels

| Object | What it is, and the operations it supports | Introduced in |
|---|---|---|
| a fundamental solution $E$ of $P$ | $P E = \delta$; it solves $Pu = f$ by $u = E * f$ when the convolution is defined | *Distributions and Fundamental Solutions* |
| the fundamental solution of the Laplacian | the Newtonian potential, $E = \lvert x\rvert^{2-n}/((2-n)\omega_n)$, for $n \geq 3$ | *Distributions and Fundamental Solutions*; *Potential Theory* |
| the fundamental solution of the heat operator | the Gaussian kernel, giving the heat semigroup and the solution of the initial-value problem | *Distributions and Fundamental Solutions*; *Semigroups and Evolution Equations* |
| the fundamental solution of the Cauchy–Riemann and Dirac operators | the Cauchy kernel $1/(\pi z)$ and the Clifford kernel $\bar x/\lvert x\rvert^{n+1}$ | *Regularity and the Cauchy–Riemann Operator*; *Dirac Operators* |
| a parametrix of an elliptic operator | a distribution $E$ with $PE = \delta + R$ for a smoothing remainder $R$; it gives elliptic regularity | *Distributions and Fundamental Solutions*; *Pseudodifferential Operators* |
| the Green function | the fundamental solution of a boundary-value problem, carrying the boundary conditions | *Partial Differential Equations*; *Potential Theory* |
| the smooth kernel | a kernel $K \in C^\infty(Y\times X)$; it defines a smoothing operator, and this is the converse direction of elliptic regularity | *The Schwartz Kernel Theorem* |
| the kernel of a pseudodifferential operator | a distribution on the diagonal whose singularities are encoded by the symbol | *The Schwartz Kernel Theorem*; *Pseudodifferential Operators* |

## Distributions on Other Grounds

| Object | Its definition, and the operations it supports | Introduced in |
|---|---|---|
| a $p$-adic distribution | a continuous linear functional on $C(\mathbb Z_p,\mathbb Q_p)$; the Amice transform identifies it with a power series of bounded coefficients | *p-adic Integration* |
| a $p$-adic measure | a $p$-adic distribution of norm at most $1$; identified with $\mathbb Z_p[[T]]$, the Iwasawa algebra | *p-adic Integration* |
| the Bernoulli distribution | a $p$-adic distribution that is not a measure; its integral against a power of $x$ gives the Kubota–Leopoldt $p$-adic $L$-function | *p-adic Integration* |
| the distributional boundary value of a holomorphic function | the limit of $f(x+iy)$ as $y \to 0$; the Sokhotski–Plemelj formula for the jump | *Complex Harmonic Analysis* |
| the delta distribution on the dual numbers and the split complex plane | the identity for the convolution of the hypercomplex system | *Dual-Numbers Harmonic Analysis*; *Split-Complex Harmonic Analysis* |

## Operations That Are Not Defined

| Object | The failure | Introduced in |
|---|---|---|
| the product $\delta\cdot\delta$ and $\delta\cdot\mathrm{pv}\frac1x$ | no associative multiplication of distributions extends the product of functions; the wave front sets meet in a forbidden way | *Distributions and Fundamental Solutions* |
| "the delta function" as a function | there is no function $\delta$ with the defining property; the object exists only as a functional | *Distributions and Fundamental Solutions* |
| the derivative of a distribution times itself | not defined without a Hörmander product condition | *Microlocal Analysis* |
| the restriction of a distribution to a hypersurface | not defined without the transversality of the wave front set with the conormal | *Microlocal Analysis* |
| the Fourier transform of an arbitrary distribution | not defined: only the tempered distributions carry it, and the general distribution has no decay | *Distributions and Fundamental Solutions* |
| the convolution of two distributions without compact support | not defined in general; the supports must be compatible | *Distributions and Fundamental Solutions* |
| the integral of a distribution over an unbounded set | not defined: only the pairing with a test function is | *Distributions and Fundamental Solutions* |

## Summary

This list gathers the distributions of the corpus: the spaces $\mathcal D'$, $\mathcal E'$ and $\mathcal S'$ and the function-type, measure and positive distributions; the delta and its derivatives, the Heaviside function, the principal value and the finite part; the operations of differentiation, multiplication, convolution, Fourier transformation and restriction, with the limits each meets; the fundamental solutions, parametrices, Green functions and Schwartz kernels; and the $p$-adic, holomorphic and hypercomplex distributions. The closing table records the operations that the theory does not define.

## Summary of Notation

The objects are named by their standard symbols; the tables use the following.

| Symbol | Meaning |
|---|---|
| $\mathcal D$, $\mathcal E$, $\mathcal S$ | test functions, smooth functions, Schwartz class |
| $\mathcal D'$, $\mathcal E'$, $\mathcal S'$ | distributions, compactly supported and tempered distributions |
| $\langle u,\varphi\rangle$ | the duality pairing |
| $\delta$, $\delta_a$, $\partial^\alpha\delta$ | the delta distribution, its translate, its derivatives |
| $H$, $\mathrm{pv}\frac1x$, $\mathrm{pf}\frac1{x^2}$ | Heaviside function, principal value, finite part |
| $\hat u$ | the Fourier transform of a tempered distribution |
| $E$, $R$ | a fundamental solution or parametrix, and the smoothing remainder |
| $\operatorname{WF}(u)$ | the wave front set |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators*, vol. I (Springer, 1983), for the theory of distributions, the product and pullback conditions and the fundamental solutions.
- Laurent Schwartz, *Théorie des distributions* (Hermann, 2nd ed. 1966), for the original treatment of the distribution spaces and their operations.
- Israel M. Gelfand and Georgi E. Shilov, *Generalized Functions*, vols. I and II (Academic Press, 1964–1968), for the generalised functions of analysis and the distributions on other grounds.
