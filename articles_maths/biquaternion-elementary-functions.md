# __Biquaternion Elementary Functions__

## Introduction

This article introduces the elementary functions of a biquaternion variable. It follows the basic algebra article, which defined the biquaternion algebra $\mathbb{B}$, its conjugations, and its remarkable subspaces. The goal is to define the exponential, the logarithm, the power functions, the trigonometric and hyperbolic functions, and the inverse functions, and to compute them in closed form. The article mirrors *Quaternion Special Functions* in its treatment of the elementary functions, adapted to the complexified algebra. The exponential is treated in full: its closed form, its exponential coordinates at the identity, its group law, its kernel, and the exponentials in the two real directions of the trace-free part. Its Lie-group consequences — the group of units and the norm-one group — are in *Biquaternion Lie Group and Exponential Structure*.

The logarithm is treated in the same detail as the exponential: the exponential equation, its two components $Q_{\log,t}$ and $\vec Q_{\log}$, the scalar part and the norm, the eigenvalue formula with the eigenvalues $Q_t\pm iB$ and the eigenprojections $\tilde\Pi_\pm$, the three cases, the parity-matched branch lattice, the principal branch and its cut walls, the principal domain on which the exponential is bijective, the two compositions, the derivative, and the value of the power function on all branches. The eigenvalue decomposition used throughout — the eigenvalues $\lambda_\pm=Q_t\pm iB$, the eigenprojections $\tilde\Pi_\pm$, the pure root $\vec\Xi$ and the parity-matched lattice — is that of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*, for the eigenvalues, the eigenprojections and the pure root, and of §*The Eigenvalue Formula* below for the parity-matched lattice; this article cites them and does not derive them. The worked examples are the kernel and logarithm computations and the counterexamples that establish the failure of the addition formulas.

The treatment is purely mathematical. No physics is invoked. The biquaternion algebra $\mathbb{B}$ is assumed from the basic algebra article, together with its scalar-vector decomposition, its biquaternion norm, written $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}$, and its four conjugations. An element is **$N$-regular** when $N(\tilde Q)\neq0$ and **$N$-degenerate** when $N(\tilde Q)=0$.

The key structural fact is that the elementary functions of a biquaternion are determined by the **powers** of the biquaternion, and the powers simplify dramatically in two regimes: when the vector part has a nonzero **complex norm**, and when the complex norm vanishes. These two regimes cover all possibilities. The first is the **oscillatory regime**; the second contains the **nilpotent case**, where the vector part is nonzero and squares to zero, and the **scalar case**, where the vector part vanishes. The purpose of this article is to develop the elementary functions in all three cases, with the scalar case distinguished where its logarithm or its powers are larger.

The higher special functions — Bessel, hypergeometric, gamma, zeta, and the functions arising from the analysis — are treated in the companion article on biquaternion higher special functions.

**Plan.** The spectral setting is recalled first, with the complex norm, the eigenvalue data, the regimes and the spectral calculus (§*The Spectral Setting*). The exponential and the logarithm follow, with their closed forms, kernels, images and fibres (§*The Exponential*, §*The Logarithm*); the powers and roots follow from the logarithm (§*Powers and Roots*); the trigonometric and hyperbolic functions and their inverses follow (§*The Trigonometric and Hyperbolic Functions*); the relations to the quaternion and complex cases close the theory (§*Relations to the Neighbouring Cases*). The results are collected in tables in §*Summary*, including the comparison with the split-complex and reduced biquaternion cases.

Every numerical value displayed below was recomputed in double precision.

**Notation.** Throughout, a biquaternion is written

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = Q_t e_t + \vec Q, \qquad \vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z.
$$

The scalar part is $Q_t \in \mathbb{C}$; the vector part is $\vec Q$. The quaternion conjugate is $\tilde{Q}^{\natural} = Q_t e_t - \vec Q$, and the biquaternion norm is

$$
\langle\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2.
$$

The scalar imaginary is $i$, which commutes with the quaternion units.

## The Spectral Setting

### The Eigenvalue Data

The vector part carries the **complex norm**
$$
B=\sqrt{Q_x^2+Q_y^2+Q_z^2},
$$
a fixed square root of the value of the complex quadratic form on $\vec Q$ (*N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Quaternionic Norm*), and, when $B\neq0$, the **axis**
$$
\vec Q=B\vec U,\qquad \vec U=\frac{\vec Q}{B},\qquad \vec U^2=-e_t.
$$
The square root, the axis and the pure root $\vec\Xi=-i\vec U$ are those of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spectral Criterion*, and are not derived again; replacing $B$ by $-B$ replaces $\vec U$ by $-\vec U$ and leaves $\tilde Q$ unchanged.

The spectral data are those of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spectral Criterion*, and *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*; the coordinate change and the lattice are derived in §*The Logarithm* below. The definitions, the decompositions and their proofs are there; this article uses them and does not repeat them. The table collects the results in the form used below.

| Quantity | Value |
|---|---|
| Spectrum | $\sigma(\tilde Q)=\{\lambda_+,\lambda_-\}$ |
| Eigenvalues | $\lambda_\pm=Q_t\pm iB=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ |
| Eigenprojections | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, $\vec\Xi=-i\vec U$, for $B\neq0$ |
| Eigenvalue decomposition | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, for $B\neq0$ |
| Characteristic polynomial | $p_{\tilde Q}(X)=X^2-2Q_tX+\langle\tilde Q\rangle_{\natural}=(X-\lambda_+)(X-\lambda_-)$ |
| Distinctness | $\lambda_+\neq\lambda_-$ exactly when $B\neq0$ |
| Norm | $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ |
| Unit criterion | $\tilde Q$ is a unit exactly when $Q_t^2+B^2\neq0$ |
| Polynomial calculus | $f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-$ for every polynomial $f$, when $B\neq0$ |
| Lattice | $\ker\exp\cap\mathbb C[\tilde Q]=\{\pi i m\,e_t+\pi n\,\vec U:\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\}$ |

The eigenvalues are distinct in the oscillatory regime and coincide in the nilpotent and scalar regimes; the eigenprojections exist only in the oscillatory regime. The lattice is the parity-matched lattice derived in §*The Logarithm* below; it is not the rectangular lattice $2\pi i\mathbb{Z}e_t\oplus2\pi\mathbb{Z}\vec U$.

### The Regimes

The vector part $\vec Q$ is a zero divisor exactly when $(\vec Q, \vec Q) = 0$ and $\vec Q\neq0$, i.e. when $B = 0$ and $\vec Q\neq0$; the criterion is in *N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*. The square root splits the discussion into two cases:

- **Oscillatory regime:** $B \neq 0$. The vector part is not a zero divisor, and it can be normalized to a root of $-1$. The powers of $\vec Q$ alternate, as in the quaternion case.
- **Nilpotent regime:** $B = 0$. The vector part is nilpotent, and $\vec Q^2 = 0$; when $\vec Q\neq0$ it is a pure zero divisor. The powers of $\vec Q$ truncate after the first.

These two cases cover all possibilities for the vector part; the case $\vec Q=0$ is the degenerate end of the second and is treated separately below. The elementary functions are computed separately in each case, and the formulas are different in the two regimes. The table below refines the two cases by the spectral type of the element; the spectral data of each regime are those of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Two Cases*.

| Regime | Condition | Consequence for the functions |
|---|---|---|
| Distinct, $N$-regular | $B\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ | $\exp$ reaches it; $\log$ is defined; the powers and roots read two nonzero eigenvalues |
| Oscillatory, $N$-degenerate | $B\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ | $\exp$ does not reach it, so $\log$ and general powers are undefined; a trigonometric or hyperbolic value may be $N$-degenerate |
| Jordan | $B=0$, $\vec Q\neq0$, $Q_t\neq0$ | $N$-regular; $\exp$ truncates and $\log$ exists; the powers are linear in $\vec Q$ |
| Nilpotent | $B=0$, $\vec Q\neq0$, $Q_t=0$ | $N$-degenerate and a nonzero zero divisor; $\exp$ truncates, $\log$ does not exist, and there is no square root |
| Scalar | $\vec Q=0$ | one complex scalar; the algebra of functions is the complex one; for $\tilde Q\neq0$ the logarithm gains the vector families |

The distinct and $N$-degenerate rows are the two subcases of $B\neq0$: the eigenvalues are distinct, and in the $N$-degenerate subcase one of them is zero. The distinct $N$-regular element is the domain of the logarithm and of general powers; the $N$-degenerate element has an eigenvalue decomposition but no logarithm. The $B=0$ case is the nilpotent regime, named for the vector part; the element is $N$-regular in the Jordan subcase $Q_t\neq0$ and $N$-degenerate and a pure nilpotent in the subcase $Q_t=0$. If $\vec Q=0$, the biquaternion is a complex scalar $\tilde Q=Q_te_t$, and the elementary functions reduce to the ordinary complex elementary functions. This is a degenerate subcase of the nilpotent regime, since $B=0$ and $\vec Q=0$; it is not in the oscillatory regime. It is treated separately in each section because its centraliser is the whole algebra.

In the nilpotent regime with a nonzero vector part, the element $\vec Q$ is a pure zero divisor, and its square vanishes. The elementary functions truncate, and the formulas are linear in $\vec Q$.

The split-complex and reduced biquaternion cases have no nilpotent regime, because those algebras are reduced; the scalar row is their only spectral degeneration. The nilpotent row is what the biquaternion adds.

### The Idempotent Principle

The elementary functions of a single biquaternion are tractable because the powers of one element span a commutative subalgebra. The $\mathbb{C}$-linear span of $\{e_t,\tilde{Q},\tilde{Q}^2,\dots\}$ is the **commutative subalgebra generated by $\tilde{Q}$**, written $\mathbb{C}[\tilde{Q}]$. Its structure — the minimal polynomial, the two isomorphism types and the convergence of power series — is that of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenvalues* and §*The Degenerate Regimes*, and its characteristic polynomial is that of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spectral Criterion*. By the Cayley–Hamilton identity of those articles,
$$
\tilde{Q}^2-2Q_t\tilde{Q}+\langle\tilde{Q}\rangle_{\natural}e_t=0,
$$
so $\mathbb{C}[\tilde{Q}]=\operatorname{span}_{\mathbb{C}}\{e_t,\tilde{Q}\}$, of dimension two when $B\neq0$ or $\vec Q\neq0$, and one, equal to $\mathbb{C}e_t$, when $\vec Q=0$.

**Theorem (Idempotent Principle, oscillatory regime).** Let $f$ be defined by a power series with radius of convergence $\rho$, and let $B\neq0$ with $\lvert\lambda_\pm\rvert<\rho$. Then

$$
\boxed{\; f(\tilde{Q})=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-,\qquad B\neq0 \;}
$$

**Proof.** The eigenvalue decomposition gives $\tilde Q^n=\lambda_+^n\tilde\Pi_++\lambda_-^n\tilde\Pi_-$ for every $n\geq0$ (*The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*). Summing the series termwise, using $\tilde\Pi_+^2=\tilde\Pi_+$, $\tilde\Pi_-^2=\tilde\Pi_-$, $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$, gives the display; the rearrangement is legitimate because the series converges absolutely in each eigenvalue.

The same display is the definition of the biquaternion extension of a function given by an integral, an inverse or another complex formula. In the nilpotent regime the idempotents are absent and the series truncates after the linear term, as computed in §*The Exponential* and §*The Logarithm*. The two regimes are the two isomorphism types of $\mathbb{C}[\tilde{Q}]$.

This is the Idempotent Principle of *Split-Complex Elementary Functions* and *Reduced Biquaternion Elementary Functions* in the oscillatory regime, extended by the truncated calculus of the nilpotent regime. Because $\mathbb{C}[\tilde{Q}]$ is commutative, the standard identities of complex analysis — the Pythagorean identity, the hyperbolic identity, the double-angle formulas, the relation between the exponential and the trigonometric functions — hold within it, and every elementary function $F(\tilde{Q})$ defined by a power series with coefficients in $\mathbb{C}$ lies in $\mathbb{C}[\tilde{Q}]$. This is the precise sense in which the non-commutativity of $\mathbb{B}$ does not obstruct the standard identities for a single biquaternion variable.

**Several variables.** For functions of two or more biquaternion variables the reduction fails. The powers of a sum $\tilde Q_1+\tilde Q_2$ involve both products $\tilde Q_1\tilde Q_2$ and $\tilde Q_2\tilde Q_1$, the binomial expansion does not hold, and $\exp(\tilde Q_1+\tilde Q_2)\neq\exp\tilde Q_1\exp\tilde Q_2$ in general. The theory of several variables is largely open (§*Open Questions*).

## The Exponential

### Definition

The **exponential** of a biquaternion $\tilde{Q}$ is defined by the power series

$$
\exp(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^n}{n!}.
$$

The series converges for every $\tilde{Q} \in \mathbb{B}$, because $\mathbb{B}$ is finite-dimensional and the Euclidean norm grows at most exponentially with $n$. So the exponential is an entire function on $\mathbb{B}$.

### The Closed Form

**Reduction to the vector part.** Write $\tilde{Q} = Q_t e_t + \vec Q$. The scalar part $Q_t e_t$ commutes with everything, so by the identity $\exp(A + B) = \exp(A)\exp(B)$ for commuting $A$ and $B$,

$$
\exp(\tilde{Q}) = \exp(Q_t e_t) \exp(\vec Q) = \exp(Q_t) \exp(\vec Q),
$$

where $\exp(Q_t)$ is the ordinary complex exponential. In the oscillatory case the Idempotent Principle computes $\exp(\tilde Q)$ directly; in the degenerate cases the reduction leaves the exponential of the vector part.

**The oscillatory case.** If $B\neq0$, the Idempotent Principle applies to the exponential series. With the eigenvalues and eigenprojections of §*The Eigenvalue Data*,

$$
\exp(\tilde Q)=\exp(\lambda_+)\tilde\Pi_++\exp(\lambda_-)\tilde\Pi_-
=\exp(Q_t)\bigl(\cos B\,e_t+\sin B\,\vec U\bigr),
$$

because $\lambda_\pm=Q_t\pm iB$ and $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ with $\vec\Xi=-i\vec U$. Hence

$$
\boxed{\; \exp(\tilde{Q}) = \exp(Q_t) \bigl(\cos B \, e_t + \sin B \, \vec U\bigr), \qquad B \neq 0 \;}
$$

**The case $B = 0$.** If $B = 0$, then $\vec Q^2 = 0$, so $\vec Q^n = 0$ for all $n \geq 2$. The power series truncates to

$$
\exp(\vec Q) = e_t + \vec Q,
\qquad
\exp(\tilde{Q}) = \exp(Q_t) (e_t + \vec Q), \qquad B = 0.
$$

This is the analogue of the exponential of a nilpotent matrix, $\exp(N) = I + N$.

**The scalar case.** If $\vec Q = 0$, the biquaternion is a complex scalar, and both formulas reduce to $\exp(\tilde{Q}) = \exp(Q_t) e_t$, the ordinary complex exponential.

The two closed forms are collected in one table.

| Regime | Condition | $\exp(\tilde Q)$ |
|---|---|---|
| Oscillatory | $B\neq0$ | $\exp(Q_t)\bigl(\cos B\,e_t+\sin B\,\vec U\bigr)$ |
| Nilpotent or scalar | $B=0$ | $\exp(Q_t)(e_t+\vec Q)$ |

In the table, $B = \sqrt{Q_x^2 + Q_y^2 + Q_z^2}$ and $\vec U = \vec Q/B$.

### The Kernel and the Image

Because $\exp$ is surjective onto the group of units but not injective (§*The Logarithm*), the fibre over the identity measures the ambiguity of the logarithm.

| Quantity | Value |
|---|---|
| Kernel | the elements diagonalisable over $\mathbb{C}$ with every eigenvalue in $2\pi i\mathbb{Z}$ |
| Image | the unit group $\mathbb{B}^\times=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| Periods | the central periods $2\pi i k\,e_t$; the kernel is larger, and it is not a subgroup |
| Injective | no |
| Surjective onto the image | yes |

**Theorem.** For a biquaternion $\tilde{Q}$ one has $\exp(\tilde{Q}) = e_t$ if and only if $\tilde{Q}$ is diagonalizable over $\mathbb{C}$ and every eigenvalue of $\tilde{Q}$ lies in $2\pi i\mathbb{Z}$.

**Proof.** If $\tilde{Q}$ is diagonalizable with eigenvalues $\lambda_1, \lambda_2$, then $\exp(\tilde{Q})$ is diagonalizable with eigenvalues $\exp(\lambda_1), \exp(\lambda_2)$, and equals $I$ exactly when $\exp(\lambda_1) = \exp(\lambda_2) = 1$. Conversely, write $\tilde{Q} = S + N$ with $S$ semisimple and $N$ nilpotent commuting. Then $\exp(\tilde{Q}) = \exp(S)\exp(N)$ is the product of a semisimple and a unipotent factor; if it equals $I$, the unipotent factor is semisimple, hence trivial, so $N = 0$.

**Concrete description.** A biquaternion lies in the kernel exactly when its representing matrix is conjugate to $\mathrm{diag}(2\pi i m, 2\pi i n)$ with $m, n \in \mathbb{Z}$. The kernel is thus an infinite subset of $\mathbb{B}$, not an additive subgroup, since $\exp$ is not a homomorphism. It contains the scalars $2\pi i k\, e_t$ but much more: $\mathrm{diag}(0, 2\pi i)$ also exponentiates to the identity.

**In biquaternion terms.** By *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Spectral Criterion*, the eigenvalues of the matrix representing $\tilde{Q}$ are $\lambda_\pm = Q_t \pm iB$, in the notation of §*The Eigenvalue Data*. So $\exp(\tilde{Q}) = e_t$ exactly when either $\vec Q = 0$ and $\tilde{Q} = Q_t e_t$ is a scalar with $Q_t \in 2\pi i\mathbb{Z}$, or $B \neq 0$ and both $Q_t \pm iB$ lie in $2\pi i\mathbb{Z}$. The second condition is equivalent to

$$
Q_t = \pi i m, \qquad B = \pi n, \qquad m, n \in \mathbb{Z}, \quad m \equiv n \pmod 2,
$$

the eigenvalues then being $\pi i(m\pm n)$. If $B = 0$ but $\vec Q \neq 0$, the matrix is a nonzero nilpotent, hence not diagonalizable and not in the kernel: $\exp(\vec Q) = e_t + \vec Q \neq e_t$.

**Example.** The biquaternion $\tilde{Q} = \pi i\, e_t + \pi\, \vec e_z$ has $Q_t = \pi i$, $B = \pi$, so $m = n = 1$ and $\exp(\tilde{Q}) = \exp(\pi i)(\cos\pi\, e_t + \sin\pi\, \vec e_z) = e_t$. Since $\langle\tilde{Q}\rangle_{\natural} = 0$, this kernel element is a zero divisor: the kernel is not contained in the group of units.

**On the phrase "eigenvalues differ by a multiple of $2\pi i$".** The condition implies such a difference, but the difference alone is weaker: $\tilde{Q} = e_t$ has equal eigenvalues yet $\exp(e_t) \neq e_t$. Each eigenvalue must be a multiple of $2\pi i$.

### Properties

| Property | Statement |
|---|---|
| Multiplicativity | $\exp(\tilde Q_1+\tilde Q_2)=\exp\tilde Q_1\exp\tilde Q_2$ when $[\tilde Q_1,\tilde Q_2]=0$; fails in general |
| Non-vanishing | $\exp\tilde Q$ is a unit for every $\tilde Q$ |
| Norm | $\langle\exp\tilde Q\rangle_{\natural}=\exp(2Q_t)=\exp(\operatorname{Tr}\tilde Q)$ |
| Hermitian norm | $\langle e^{\theta\tilde Q}\rangle_*=\lvert e^{\theta Q_t}\rvert^2\bigl(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\,\lVert\vec U\rVert_E^2\bigr)$ |
| Unitary flow | $e^{\theta\tilde Q}$ unitary for every real $\theta$ iff $\tilde Q^*=-\tilde Q$ |
| Self-adjoint flow | $e^{\theta\tilde Q}$ self-adjoint for every real $\theta$ iff $\tilde Q^*=\tilde Q$ |
| Derivative | $d\exp_{\tilde Q}(H)=\int_0^1\exp(s\tilde Q)H\exp((1-s)\tilde Q)\,ds$; it equals $\exp(\tilde Q)H$ when $[H,\tilde Q]=0$ |
| Injective | no; the kernel is computed in §*The Kernel and the Image* |
| Periods | the central periods $2\pi i k\,e_t$; further periods depend on $\tilde Q$ |

**Non-vanishing.** In the oscillatory case, $\exp(Q_t) \neq 0$ and the factor $\cos B \, e_t + \sin B \, \vec U$ is invertible: its inverse is $\cos B \, e_t - \sin B \, \vec U$, as follows from

$$
(\cos B \, e_t + \sin B \, \vec U)(\cos B \, e_t - \sin B \, \vec U) = (\cos^2 B + \sin^2 B) e_t = e_t.
$$

In the nilpotent case, $\exp(Q_t) \neq 0$ and $(e_t + \vec Q)(e_t - \vec Q) = e_t - \vec Q^2 = e_t$.

**Derivative in the scalar direction.** This is the reason the exponential is the fundamental solution of the scalar differential operator $\partial/\partial Q_t$.

**Derivative in the vector directions.** The derivatives $\partial/\partial Q_k \exp(\tilde{Q})$ for $k\in\{x,y,z\}$ are **not** equal to $\exp(\tilde{Q}) \vec e_k$ or $\vec e_k \exp(\tilde{Q})$ in general. The reason is that $\partial/\partial Q_k \tilde{Q} = \vec e_k$ does not commute with $\tilde{Q}$ unless $\tilde{Q}$ lies in the subalgebra generated by $e_t$ and $\vec e_k$. The correct expression is the biquaternion analogue of the matrix identity $\partial \exp(M) = \int_0^1 \exp(sM)(\partial M)\exp((1-s)M)\,ds$, namely

$$
\partial/\partial Q_k \exp(\tilde{Q}) = \int_0^1 \exp(s \tilde{Q}) \vec e_k \exp((1-s)\tilde{Q}) \, ds.
$$

This reduces to $\exp(\tilde{Q}) \vec e_k$ only when $\vec e_k$ commutes with $\tilde{Q}$.

**Biquaternion norm.** The verification is direct: in the oscillatory regime, $\langle\exp(\tilde{Q})\rangle_{\natural} = \exp(2 Q_t)(\cos^2 B + \sin^2 B) = \exp(2 Q_t)$; in the nilpotent regime, $\langle\exp(\tilde{Q})\rangle_{\natural} = \exp(2 Q_t)(1 + 0) = \exp(2 Q_t)$. Here $\operatorname{Tr}(\tilde{Q}) = 2\operatorname{Sc}\tilde{Q} = 2Q_t$.

### The Hermitian Norm and the Unitary Flow

The quaternionic norm is fixed by the scalar part alone. The Hermitian norm $\langle X\rangle_*=\operatorname{Sc}(XX^*)$ of *Conventions in Mathematics*, §*The Form Convention, the Norm Convention and the Unitary Convention*, is not: it reads the vector part as well, and it separates the three data of the element.

**Proposition (the Hermitian norm of the flow).** Let $B\neq0$, let $\vec U=\vec Q/B$, and let $\theta\in\mathbb{R}$. Then

$$
\langle e^{\theta\tilde Q}\rangle_*
=\lvert e^{\theta Q_t}\rvert^2
\left(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\,\lVert\vec U\rVert_E^2\right),
\qquad
\lVert\vec U\rVert_E^2=\sum_{k\in\{x,y,z\}}\lvert U_k\rvert^2.
$$

*Proof.* Write $e^{\theta\tilde Q}=e^{\theta Q_t}(a e_t+b\vec U)$ with $a=\cos(B\theta)$ and $b=\sin(B\theta)$. Since $\vec U$ is pure, the scalar part of $\vec U\vec U^*$ is $\lVert\vec U\rVert_E^2e_t$, and the cross terms $a\bar b\vec U^*+b\bar a\vec U$ are pure vectors; the scalar part of the product is therefore $\lvert e^{\theta Q_t}\rvert^2(\lvert a\rvert^2+\lvert b\rvert^2\lVert\vec U\rVert_E^2)$.

**Corollary (the norm deficit).** $\lVert\vec U\rVert_E^2=\lVert\vec Q\rVert_E^2/\lvert B\rvert^2\ge1$, with equality exactly when $\vec U$ is real, that is, exactly when $\tilde Q$ is normal.

*Proof.* $\lvert B^2\rvert=\lvert\sum_kQ_k^2\rvert\le\sum_k\lvert Q_k\rvert^2$, with equality exactly when the non-zero squares have one argument. Dividing by $\lvert B\rvert^2$ gives the inequality; if they do, $Q_k=\zeta r_k$ with $r_k\in\mathbb{R}$ and $\zeta^2$ that argument, so $B=\pm\zeta R$ with $R^2=\sum_kr_k^2$ and $\vec U=\pm(r_x,r_y,r_z)/R$ is real of Euclidean norm one. Since normality is exactly the reality of $\vec U$ (*The Biquaternion Eigenvalue Decomposition*, §*The Hermitian Case*), this is the equality case.

**Corollary (bounded and unbounded flows).** If $B$ is real and $\operatorname{Re}Q_t=0$, the Hermitian norm is bounded between $1$ and $\lVert\vec U\rVert_E^2$. If $\operatorname{Re}Q_t\neq0$ it is unbounded on one side. If $\operatorname{Im}B\neq0$ it is unbounded on both sides.

The three sources are independent. The factor $\lvert e^{\theta Q_t}\rvert^2=e^{2\theta\operatorname{Re}Q_t}$ is the dilation; the trigonometric factor grows like $e^{2\lvert\operatorname{Im}B\rvert\lvert\theta\rvert}$ when $\operatorname{Im}B\neq0$; and the deficit $\lVert\vec U\rVert_E^2-1$ is an amplitude. A decay is a negative real part of $Q_t$ in the convention $e^{+\theta\tilde Q}$; a boost is a non-zero imaginary part of $B$; a non-normal element has a larger oscillation amplitude, not a rate.

**Proposition (unitary and self-adjoint flows).** For real $\theta$, the following are equivalent:

- $e^{\theta\tilde Q}$ is unitary for the Hermitian form for every $\theta$;
- $\tilde Q^*=-\tilde Q$;
- $Q_t\in i\mathbb{R}$ and $\vec Q\in\mathbb{R}^3$.

The following are also equivalent:

- $e^{\theta\tilde Q}$ is self-adjoint for every $\theta$;
- $\tilde Q^*=\tilde Q$;
- $Q_t\in\mathbb{R}$ and $\vec Q\in i\mathbb{R}^3$.

*Proof.* If $E=e^{\theta\tilde Q}$ is unitary for every $\theta$, differentiating $EE^*=e_t$ at $\theta=0$ gives $\tilde Q+\tilde Q^*=0$. Conversely $\tilde Q^*=-\tilde Q$ gives $E^*=e^{-\theta\tilde Q}=E^{-1}$. On $Q_te_t+\vec Q$ the star conjugates the scalar part and negates and conjugates the vector part, so $\tilde Q^*=-\tilde Q$ is $\bar Q_t=-Q_t$ and $\overline{\vec Q}=\vec Q$. The self-adjoint case is the same computation with the opposite signs.

**Remark (normal is not unitary).** Normality is the reality of $\vec U$, a condition on the vector part alone; unitarity is the skew-adjointness of $\tilde Q$, a condition on both parts. The element $(1+i)\vec e_x$ is normal, with $\vec U=\vec e_x$ and $B=1+i$, but its flow is neither unitary nor self-adjoint; its Hermitian norm is $\cosh2\theta$. The element $i\vec e_x+\vec e_y+\vec e_z$ is not normal, with $B=1$ and $\lVert\vec U\rVert_E^2=3$, but its Hermitian norm is $1+2\sin^2\theta$, which is bounded. The two notions answer different questions: normality does not imply a constant norm, and non-normality does not imply growth. The dictionary between the flow and the Fourier kernel is *Relations between the Biquaternion Exponential and the Fourier Kernel*.

The differential at the origin is the identity, so $\exp$ is a local diffeomorphism near $0$ and provides exponential coordinates near the identity of the group of units $\mathbb{B}^\times$ (*Biquaternion Lie Group and Exponential Structure*).

### The Group Law

The exponential is not a homomorphism from the additive group of the algebra to the multiplicative group of the units. Its failure to be one is measured by the bracket.

**Commuting case.** If $[a,b] = 0$, then

$$
\exp(a)\exp(b) = \exp(a+b) = \exp(b)\exp(a).
$$

In particular, this holds when $a$ and $b$ lie in a common commutative subalgebra. For a single biquaternion $\tilde{Q}$, all elementary functions lie in the commutative subalgebra $\mathbb{C}[\tilde{Q}]$ generated by $e_t$ and $\tilde{Q}$, so the usual addition formula holds there.

**General case.** The Baker–Campbell–Hausdorff theorem gives, for sufficiently small $a, b$,

$$
\exp(a)\exp(b) = \exp\!\left(a + b + \frac{1}{2}[a,b] + \frac{1}{12}\bigl[a,[a,b]\bigr] - \frac{1}{12}\bigl[b,[a,b]\bigr] + \cdots\right),
$$

a convergent series of iterated brackets. Thus $\exp(a)\exp(b)$ differs from $\exp(a+b)$ by the term $\tfrac{1}{2}[a,b]$ and higher brackets; the difference vanishes whenever $[a,b] = 0$, though the converse can fail, since a non-commuting pair may still satisfy $\exp(a)\exp(b) = \exp(a+b)$ when the BCH remainder exponentiates to $e_t$ (§*The Kernel and the Image*). For instance, with $a = \vec e_x$ and $b = \vec e_y$ the product $\exp(\vec e_x)\exp(\vec e_y)$ carries a term $\sin^2 1\, \vec e_z$ that is absent from $\exp(\vec e_x+\vec e_y)$.

### The Exponential in the Two Real Directions

Let $\vec u$ be a real unit vector part, so that $\vec u^2 = -e_t$. The two real three-dimensional families of exponents — the bivector directions $\theta\vec u$ and the vector directions $\psi\, i\vec u$, with $\theta, \psi \in \mathbb{R}$ — exponentiate in closed form. They are the two real summands of the trace-free subalgebra of $\mathbb{B}$, developed in *Symmetric and Antisymmetric Decomposition of the Four General Products*.

**The bivector directions.** For real $\theta$,

$$
\exp(\theta\vec u) = \cos\theta\, e_t + \sin\theta\, \vec u,
$$

a unit quaternion in $\mathbb{H}_{\mathbb{B}}$, since $\langle\exp(\theta\vec u)\rangle_{\natural} = \cos^2\theta + \sin^2\theta = 1$. The family is periodic with period $2\pi$, since $\exp(2\pi\vec u) = e_t$, and at the half-period $\exp(\pi\vec u) = -e_t$.

**The vector directions.** With $(i\vec u)^2 = +e_t$ and real parameter $\psi \in \mathbb{R}$,

$$
\exp(\psi\, i\vec u) = \cosh\psi\, e_t + \sinh\psi\, i\vec u.
$$

This element is Hermitian, lies in $\mathbb{M}_+$, and has $\langle\exp(\psi\,i\vec u)\rangle_{\natural} = \cosh^2\psi - \sinh^2\psi = 1$. Unlike the bivector family it is not periodic and is unbounded as $\psi \to \pm\infty$. The set of these elements is not a subgroup: the product of two of them in non-parallel directions is the product of an element of the same family and one of the bivector family.

**Comparison.** A general exponent is $\tilde{Q} = \vec q + i\vec q'$ with $\vec q, \vec q'$ real vector parts; the two families commute only when $\vec q$ and $\vec q'$ are parallel, since $[\vec q, i\vec q'] = 2i\,(\vec q \times \vec q')$, and in general the closed form of §*The Exponential* with $Q_t = 0$ mixes the two families.

## The Logarithm

### Definition

The **logarithm** of a biquaternion $\tilde Q$ is an element $\tilde Q_{\log}$ of $\mathbb B$ with

$$
\exp(\tilde Q_{\log})=\tilde Q.
$$

The definition is an equation, not a formula; the formula is what solving the equation gives. The subscript is a label, not an operation: $\tilde Q_{\log}$ is a logarithm of $\tilde Q$, not a biquaternion whose scalar part is $\log Q_t$.

Write the unknown by its scalar and vector parts,

$$
\tilde Q_{\log}=Q_{\log,t}e_t+\vec Q_{\log},
\qquad
\vec Q_{\log}=Q_{\log,x}\vec e_x+Q_{\log,y}\vec e_y+Q_{\log,z}\vec e_z.
$$

By the coefficient rule of *Conventions in Mathematics*, §*The Elements and their Coefficients*, the four coordinates are complex, $Q_{\log,t}=q_{\log,t}+iq'_{\log,t}$ and likewise $Q_{\log,x},Q_{\log,y},Q_{\log,z}$, and the subscript $\log$ is carried into each coordinate; a numbered element keeps its number in front of the subscript, $\tilde Q_{1\log}$, as its coefficients keep theirs. The **scalar component** $Q_{\log,t}$ is the coefficient of $e_t$; the **vector component** $\vec Q_{\log}$ is a pure biquaternion, not a scalar, and it carries the axis and the complex angle of the logarithm.

The exponential is never $N$-degenerate, since $\langle\exp\tilde Q_1\rangle_{\natural}=\exp(2Q_{1t})\neq0$ for every $\tilde Q_1$ (§*Properties* of §*The Exponential*). Hence a logarithm can exist only on the $N$-regular set

$$
\mathbb B^\times=\{\tilde Q\in\mathbb B:\langle\tilde Q\rangle_{\natural}\neq0\}.
$$

Every unit has one, and the constructions below prove it. The logarithm is not unique, and no continuous single-valued branch exists on the whole group.

### The Scalar Part

Let $\tilde Q_{\log}$ be a logarithm of $\tilde Q$, and write $\tilde Q_{\log}=Q_{\log,t}e_t+\vec Q_{\log}$. Taking biquaternion norms in $\exp(\tilde Q_{\log})=\tilde Q$ gives

$$
\langle\tilde Q\rangle_{\natural}
=\langle\exp(\tilde Q_{\log})\rangle_{\natural}
=\exp(2Q_{\log,t}).
$$

Hence

$$
Q_{\log,t}=\frac12\operatorname{Log}\langle\tilde Q\rangle_{\natural}+\pi i n,\qquad n\in\mathbb Z,
$$

for a choice of complex logarithm of the norm. The real part of the scalar part is fixed,

$$
\operatorname{Re}Q_{\log,t}=\frac12\ln\bigl|\langle\tilde Q\rangle_{\natural}\bigr|,
$$

and the scalar part is fixed modulo $\pi i$; equivalently, its imaginary part is fixed modulo $\pi$. In the quaternion case the norm is real and positive, so the scalar part is the unique real number $\ln\sqrt{\langle\tilde q\rangle_{\natural}}$ and carries no branch. In $\mathbb B$ the scalar part carries one integer before the vector part is considered.

### The Eigenvalue Formula

The eigenvalue decomposition is that of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*, and is not derived again. Let $\tilde Q$ be a unit with $B\neq0$. The eigenvalues are $\lambda_\pm=Q_t\pm iB$, the pure root is $\vec\Xi=-i\vec U=-i\vec Q/B$, and the eigenprojections are $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$; they are primitive, orthogonal and complete, and satisfy

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-
\qquad
\tilde Q\tilde\Pi_\pm=\lambda_\pm\tilde\Pi_\pm.
$$

The unordered pair $\{\lambda_+,\lambda_-\}$ is fixed by $\tilde Q$; the ordered pair is fixed only up to $B\mapsto-B$, which exchanges $\tilde\Pi_+$ and $\tilde\Pi_-$. In particular $\lambda_\pm\neq0$.

Every logarithm $\tilde Q_{\log}$ commutes with $\tilde Q$, because $\tilde Q_{\log}\exp(\tilde Q_{\log})=\exp(\tilde Q_{\log})\tilde Q_{\log}$. Since the eigenvalues are distinct, the centraliser is $\mathbb C[\tilde Q]=\operatorname{span}_{\mathbb C}\{e_t,\tilde Q\}$ and $\tilde\Pi_\pm$ are polynomials in $\tilde Q$ (§*The Peirce Decomposition Relative to the Eigenprojection*). Hence $\tilde Q_{\log}$ has the same eigenprojections,

$$
\tilde Q_{\log}=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-,
$$

and the equation $\exp(\tilde Q_{\log})=\tilde Q$ is equivalent to $\exp\mu_\pm=\lambda_\pm$, by the polynomial calculus of §*Powers, Polynomial Calculus, and the Group of Units*. Thus

$$
\mu_\pm=\operatorname{Log}\lambda_\pm+2\pi i k_\pm,\qquad k_\pm\in\mathbb Z,
$$

and every logarithm is

$$
\boxed{\; \tilde Q_{\log}
=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-
=\frac{\mu_++\mu_-}{2}\,e_t+\frac{\mu_+-\mu_-}{2i}\,\vec U,
\qquad
\mu_\pm=\operatorname{Log}\lambda_\pm+2\pi i k_\pm \;},
$$

the second equality using $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ and $\vec\Xi=-i\vec U$. This is the **eigenvalue formula**. It is the exact biquaternion form of the quaternion formula, with the real angle replaced by the complex angle

$$
\Theta=\frac{\mu_+-\mu_-}{2i}.
$$

**The two integers.** The integers $k_+$ and $k_-$ are independent, and their sum and difference give the scalar and vector shifts:

$$
\mu_++\mu_-=\operatorname{Log}\lambda_++\operatorname{Log}\lambda_-+2\pi i(k_++k_-),
$$

$$
\frac{\mu_+-\mu_-}{2i}
=\frac{\operatorname{Log}\lambda_+-\operatorname{Log}\lambda_-}{2i}+\pi(k_+-k_-).
$$

The scalar shift is $\pi i(k_++k_-)$ and the vector shift is $\pi(k_+-k_-)\vec U$. With $m=k_++k_-$ and $n=k_+-k_-$ they form the parity-matched lattice derived above, which is not the rectangular lattice $2\pi i\mathbb Z e_t\oplus2\pi\mathbb Z\vec U$: the scalar part and the angle cannot be shifted independently.

**The polar form.** Let $R$ be a square root of $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$, and let $\Theta$ be a complex number with

$$
\cos\Theta=\frac{Q_t}{R},\qquad \sin\Theta=\frac{B}{R}.
$$

Then

$$
\tilde Q=R\bigl(\cos\Theta\,e_t+\sin\Theta\,\vec U\bigr),
$$

and every logarithm reads

$$
\tilde Q_{\log}=\operatorname{Log}R\,e_t+\Theta\,\vec U,
$$

where $\operatorname{Log}R$ is any logarithm of $R$ and $\Theta$ any solution of the two equations. The eigenvalue formula corresponds to the choices

$$
\operatorname{Log}R=\frac{\operatorname{Log}\lambda_++\operatorname{Log}\lambda_-}{2},
\qquad
\Theta=\frac{\operatorname{Log}\lambda_+-\operatorname{Log}\lambda_-}{2i}.
$$

Conversely, taking $R$ over its two square roots, $\operatorname{Log}R$ over all its branches and $\Theta$ over all solutions recovers every logarithm: the two choices of $R$ produce the even-even and the odd-odd shifts, whose union is the parity-matched lattice.

### The Degenerate Regimes

**The nilpotent regime.** Assume $B=0$ and $\vec Q\neq0$. Then $\vec Q^2=0$ and $\langle\tilde Q\rangle_{\natural}=Q_t^2$, so a unit has $Q_t\neq0$. The element is a single Jordan block with eigenvalue $Q_t$. The logarithms are

$$
\tilde Q_{\log}=\bigl(\operatorname{Log}Q_t+2\pi i k\bigr)e_t+\frac{\vec Q}{Q_t},
\qquad k\in\mathbb Z.
$$

In particular the principal choice is

$$
\operatorname{Log}\tilde Q=\operatorname{Log}Q_t\,e_t+\frac{\vec Q}{Q_t}.
$$

**Proof.** Put $\tilde Q_{\log}=a e_t+b\vec Q$. Since $\vec Q^2=0$,

$$
\exp(\tilde Q_{\log})=\exp(a)(e_t+b\vec Q).
$$

Equality with $Q_t e_t+\vec Q$ gives $\exp(a)=Q_t$ and $\exp(a)b=1$, hence $a=\operatorname{Log}Q_t+2\pi i k$ and $b=1/Q_t$. Conversely, this value exponentiates to $\tilde Q$. Every logarithm commutes with $\tilde Q$, and the centraliser of a nonzero nilpotent is exactly $\{a e_t+b\vec Q\}$, so there are no others.

**The scalar case.** Assume $\vec Q=0$, so $\tilde Q=Q_t e_t$ with $Q_t\neq0$. The centraliser is all of $\mathbb B$, and the fibre is larger than in the other two cases. A biquaternion $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ is a logarithm of $Q_t e_t$ exactly when one of the following holds:

- $\vec Q_1=0$ and $Q_{1t}=\operatorname{Log}Q_t+2\pi i k$ with $k\in\mathbb Z$;
- $\vec Q_1\neq0$, $(\vec Q_1,\vec Q_1)=(\pi n)^2$ for some $n\in\mathbb Z\setminus\{0\}$, and $Q_{1t}=\operatorname{Log}Q_t+\pi i n+2\pi i k$ with $k\in\mathbb Z$.

In the second case, writing $\vec Q_1=B_1\vec U$ with $B_1=\pm\pi n$ gives

$$
\exp\vec Q_1=\cos(\pi n)\,e_t=(-1)^n e_t,
$$

and $\exp(Q_{1t})=(-1)^n Q_t$, so the product is $Q_t e_t$. Conversely, if $\exp\tilde Q_1=Q_t e_t$, then either $\vec Q_1=0$, or $\vec Q_1\neq0$ and $\sin B_1=0$ with $\cos B_1=\pm1$, which forces $B_1\in\pi\mathbb Z\setminus\{0\}$; the scalar equation then gives $Q_{1t}$.

**The eigenvalue description.** Equivalently, the logarithms of a complex scalar are exactly the diagonalisable biquaternions whose two eigenvalues lie in $\operatorname{Log}Q_t+2\pi i\mathbb Z$. A non-diagonalisable biquaternion has $\exp\tilde Q_1=\exp(Q_{1t})(e_t+\vec Q_1)\neq Q_t e_t$, so it cannot occur. The set is the translate $\operatorname{Log}Q_t\,e_t+\ker\exp$; it is not a coset in the group sense, because $\ker\exp$ is not a subgroup.

**The fibre is not discrete.** For $\tilde Q=e_t$, the elements $2\pi\vec e_x$ and $2\pi\vec e_y$ are both logarithms, but their difference $2\pi(\vec e_x-\vec e_y)$ is not a logarithm of $e_t$: its exponential has scalar part $\cos(2\pi\sqrt2)\neq1$. Two logarithms need not differ by an element of the kernel, even though each is the principal logarithm plus a kernel element. The scalar logarithms also contain continuous families: for each $n\neq0$, the set $\{(\vec Q_1,\vec Q_1)=(\pi n)^2\}$ is a complex quadric, not a finite sphere. The quaternion spheres of logarithms of a real scalar are replaced by complex quadrics.

### The Coordinates of a Logarithm

The components in the three regimes are collected in one table. The first row is the eigenvalue formula, the second the nilpotent formula, and the last two the two kinds of scalar logarithm.

| Regime | $Q_{\log,t}$ | $\vec Q_{\log}$ | $\tilde Q_{\log}$ |
|---|---|---|---|
| $B\neq0$ | $\dfrac{\mu_++\mu_-}{2}$, $\mu_\pm=\operatorname{Log}\lambda_\pm+2\pi i k_\pm$, $k_\pm\in\mathbb Z$ | $\dfrac{\mu_+-\mu_-}{2i}\,\vec U$ | $\dfrac{\mu_++\mu_-}{2}\,e_t+\dfrac{\mu_+-\mu_-}{2i}\,\vec U$ |
| $B=0$, $\vec Q\neq0$ | $\operatorname{Log}Q_t+2\pi i k$, $k\in\mathbb Z$ | $\dfrac{\vec Q}{Q_t}$ | $(\operatorname{Log}Q_t+2\pi i k)e_t+\dfrac{\vec Q}{Q_t}$ |
| $\vec Q=0$, scalar logarithms | $\operatorname{Log}Q_t+2\pi i k$, $k\in\mathbb Z$ | $0$ | $(\operatorname{Log}Q_t+2\pi i k)e_t$ |
| $\vec Q=0$, vector logarithms | $\operatorname{Log}Q_t+\pi i n+2\pi i k$, $n\in\mathbb Z\setminus\{0\}$, $k\in\mathbb Z$ | $\vec Q_1$, $(\vec Q_1,\vec Q_1)=(\pi n)^2$ | $(\operatorname{Log}Q_t+\pi i n+2\pi i k)e_t+\vec Q_1$ |

The scalar component is complex. Its real part is fixed by the biquaternion norm,

$$
\operatorname{Re}Q_{\log,t}=\frac12\ln\bigl|\langle\tilde Q\rangle_{\natural}\bigr|,
$$

and its imaginary part is fixed modulo $\pi$; in the first row the scalar shift is $\pi i(k_++k_-)$ and the vector shift is $\pi(k_+-k_-)\vec U$, the two integers $k_++k_-$ and $k_+-k_-$ have the same parity, and that parity is what restricts the vector coordinate. The vector component is pure and carries the axis $\vec U$ and the complex angle; it is not the scalar $Q'_{\log}$ of the complex case, but its three-coordinate analogue. The last two rows are the two kinds of scalar logarithm, the scalar ones with zero vector component and the vector ones whose vector component runs over the complex quadric.

### The Domain and the Fibre

The kernel of the exponential is computed in §*The Kernel and the Image*: $\exp\tilde Q_1=e_t$ exactly when $\tilde Q_1$ is diagonalisable over $\mathbb C$ and every eigenvalue lies in $2\pi i\mathbb Z$.

| Quantity | Value |
|---|---|
| Domain | the units $\mathbb{B}^\times=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| Fibre over a point | a coset of $\ker\exp\cap\mathbb{C}[\tilde Q]$ for a non-scalar unit; $\operatorname{Log}Q_t\,e_t+\ker\exp$ for a scalar unit |
| Kernel | the diagonalisable elements with every eigenvalue in $2\pi i\mathbb{Z}$; not a subgroup |
| Principal domain | $D$: every eigenvalue has imaginary part in $(-\pi,\pi]$ |
| Existence | always, on the units |

For an element $\tilde Q_1$, write $B_1$ for a square root of $(\vec Q_1,\vec Q_1)$. In the three regimes the condition reads as follows.

| Element $\tilde Q_1$ | Condition for $\exp\tilde Q_1=e_t$ |
|---|---|
| scalar, $\vec Q_1=0$ | $Q_{1t}\in2\pi i\mathbb Z$ |
| $B_1\neq0$ | $Q_{1t}=\pi i m$, $B_1=\pi n$, $m\equiv n\pmod2$ |
| $B_1=0$, $\vec Q_1\neq0$ | never |

For the identity $\tilde Q=e_t$, the fibre is $\ker\exp$ itself: the scalar logarithms $2\pi i k\,e_t$ and the vector logarithms $(\pi i n+2\pi i k)e_t+\vec Q_1$ with $n\in\mathbb Z\setminus\{0\}$ and $(\vec Q_1,\vec Q_1)=(\pi n)^2$. The kernel is not a subgroup. For example $2\pi\vec e_x$ and $2\pi\vec e_y$ belong to it, while their sum does not.

For a non-scalar unit $\tilde Q$, the centraliser is commutative and the logarithms are

$$
\tilde Q_{\log}\in\operatorname{Log}\tilde Q+\bigl(\ker\exp\cap\mathbb C[\tilde Q]\bigr),
$$

a lattice coset: the parity-matched lattice when $B\neq0$, and $2\pi i\mathbb Z e_t$ in the nilpotent regime. For a scalar unit, the logarithms are the translate $\operatorname{Log}Q_t\,e_t+\ker\exp$ as a set; because the kernel is not a subgroup, two logarithms of the same scalar need not differ by a kernel element.

### The Principal Logarithm

Define $\operatorname{Log}\tilde Q$ by the three formulas

$$
\operatorname{Log}\tilde Q=
\begin{cases}
\dfrac{\operatorname{Log}\lambda_++\operatorname{Log}\lambda_-}{2}\,e_t+\dfrac{\operatorname{Log}\lambda_+-\operatorname{Log}\lambda_-}{2i}\,\vec U, & B\neq0,\\[2mm]
\operatorname{Log}Q_t\,e_t+\dfrac{\vec Q}{Q_t}, & B=0,\ \vec Q\neq0,\\[2mm]
\operatorname{Log}Q_t\,e_t, & \vec Q=0,
\end{cases}
$$

where every $\operatorname{Log}$ on the right is the principal complex logarithm, with argument in $(-\pi,\pi]$. This is single-valued on all of $\mathbb B^\times$ and satisfies $\exp(\operatorname{Log}\tilde Q)=\tilde Q$. Every eigenvalue of $\operatorname{Log}\tilde Q$ has imaginary part in $(-\pi,\pi]$; this is the defining property of the branch.

For example, on the principal branch the two components take the following values. The first element is oscillatory, the second lies in the nilpotent regime with $\vec Q^2=0$, and the third is scalar.

| $\tilde Q$ | $Q_{\log,t}$ | $\vec Q_{\log}$ |
|---|---|---|
| $3e_t+4\vec e_x$ | $\ln 5$ | $\arccos(3/5)\,\vec e_x$ |
| $2e_t+(1+i)(\vec e_x+i\vec e_y)$ | $\ln 2$ | $\dfrac{1+i}{2}(\vec e_x+i\vec e_y)$ |
| $(1+i)e_t$ | $\ln\sqrt2+\dfrac{\pi i}{4}$ | $0$ |

The first row has $\lambda_\pm=3\pm4i$ and $B=4$; the second has $B=0$ and $Q_t=2$; the third has $\vec Q=0$ and $Q_t=1+i$. The logarithm is reassembled as $\tilde Q_{\log}=Q_{\log,t}e_t+\vec Q_{\log}$ in each row.

**Cuts.** The principal complex logarithm is discontinuous across the negative real axis. Hence $\operatorname{Log}$ is discontinuous across the union of the walls

$$
\mathcal W
=\{\tilde Q:\lambda_+\in(-\infty,0]\}\cup\{\tilde Q:\lambda_-\in(-\infty,0]\}
$$

when $B\neq0$, and across the wall $Q_t\in(-\infty,0]$ when $B=0$. Each oscillatory wall is a real hypersurface of $\mathbb B$; the walls in the $B=0$ regimes lie in the codimension-two set $B=0$ and are lower-dimensional. On the complement of $\mathcal W$ the principal logarithm is real-analytic. Across a wall the two sides differ by $2\pi i \tilde\Pi_\pm$ in the oscillatory regime and by $2\pi i e_t$ in the two $B=0$ regimes; these are kernel elements. The cut is an artefact of the branch, not of the exponential, and it can be moved by choosing another ray in each eigenvalue plane.

**The principal angle.** In the oscillatory regime the eigenvalue formula gives

$$
\Theta=\frac{\operatorname{Log}\lambda_+-\operatorname{Log}\lambda_-}{2i}
=\frac{\operatorname{Arg}\lambda_+-\operatorname{Arg}\lambda_-}{2}
-\frac{i}{2}\ln\frac{|\lambda_+|}{|\lambda_-|}.
$$

Its real part lies in $(-\pi,\pi)$, while its imaginary part is unbounded. There is no bounded fundamental domain in the $\Theta$ plane; the principal domain is the strip in the eigenvalue plane defined next.

### The Principal Domain

Let

$$
D=\bigl\{\tilde Q_1\in\mathbb B:\text{every eigenvalue of }\tilde Q_1\text{ has imaginary part in }(-\pi,\pi]\bigr\}.
$$

Then $\exp$ maps $D$ bijectively onto $\mathbb B^\times$, and $\operatorname{Log}$ is its inverse. The interior $D^\circ$, where the imaginary parts lie in $(-\pi,\pi)$, maps onto $\mathbb B^\times\setminus\mathcal W$, and there $\operatorname{Log}$ is real-analytic.

**Proof.** For surjectivity, let $\tilde Q\in\mathbb B^\times$. If $B\neq0$, the numbers $\operatorname{Log}\lambda_\pm$ have imaginary parts in $(-\pi,\pi]$, and

$$
\tilde Q_1=(\operatorname{Log}\lambda_+)\tilde\Pi_++(\operatorname{Log}\lambda_-)\tilde\Pi_-
$$

lies in $D$ and exponentiates to $\tilde Q$. If $B=0$, the element $\operatorname{Log}Q_t\,e_t+\vec Q/Q_t$ lies in $D$ and exponentiates to $\tilde Q$.

For injectivity, let $\tilde Q_1,\tilde Q_2\in D$ with $\exp\tilde Q_1=\exp\tilde Q_2=\tilde Q$. Both commute with $\tilde Q$. If $\tilde Q$ is not scalar, they lie in the commutative centraliser, so $\tilde Q_1-\tilde Q_2$ is a kernel element; its eigenvalues are differences of eigenvalues in $(-2\pi,2\pi)$, hence are $0$. A kernel element with all eigenvalues $0$ is $0$ (in the nilpotent centraliser the kernel is scalar), so $\tilde Q_1=\tilde Q_2$. If $\tilde Q$ is scalar, the only eigenvalue in the strip that exponentiates to $Q_t$ is $\operatorname{Log}Q_t$, so both $\tilde Q_i$ have both eigenvalues equal to $\operatorname{Log}Q_t$; a non-diagonalisable element with that repeated eigenvalue would exponentiate to a non-scalar element, so both are scalar and equal. Thus $\exp$ is injective. The analyticity statement is the inverse function theorem on $D^\circ$, where the eigenvalues differ by less than $2\pi$ and the differential of the exponential is invertible.

**No global continuous branch.** The principal logarithm is defined pointwise on all units, but it is not continuous on all of them. No continuous single-valued logarithm exists on $\mathbb B^\times$. If $L$ were one, then for $\lambda\in\mathbb C^\times$ the trace $\operatorname{Tr}L(\lambda e_t)$ would be a continuous logarithm of $\lambda^2$, since

$$
\exp\bigl(\operatorname{Tr}L(\lambda e_t)\bigr)
=\det\exp L(\lambda e_t)
=\langle\lambda e_t\rangle_{\natural}
=\lambda^2.
$$

But $\lambda^2$ winds twice around the origin and has no continuous logarithm on $\mathbb C^\times$: the imaginary part would have to increase by $4\pi$ around the unit circle and return to its value. Equivalently, $\mathbb B^\times$ is homotopy equivalent to $U(2)$, whose fundamental group is $\mathbb Z$. A branch exists on the complement of any chosen walls.

### The Two Compositions

The exponential is single-valued and not injective; the logarithm is multi-valued. The two compositions behave as follows.

| Identity | Holds | Example |
|---|---|---|
| $\exp(\operatorname{Log}\tilde Q)=\tilde Q$ | always, on the units | $\tilde Q=3e_t+4\vec e_x$ |
| $\operatorname{Log}(\exp\tilde Q_1)=\tilde Q_1$ | exactly on the principal domain $D$ | $\tilde Q_1=3e_t$ |
| $\operatorname{Log}(\exp\tilde Q_1)=\tilde Q_1$ modulo the kernel | always | $\tilde Q_1=\pi i\,e_t+\pi\vec e_z$ gives $0$ |

,**Right inverse.** For every $\tilde Q\in\mathbb B^\times$,

$$
\boxed{\; \exp(\operatorname{Log}\tilde Q)=\tilde Q \;}.
$$

This is the construction of the principal logarithm: in the oscillatory regime, $\exp((\operatorname{Log}\lambda_\pm)\tilde\Pi_\pm)=\lambda_\pm \tilde\Pi_\pm$; in the nilpotent regime, $\exp(\operatorname{Log}Q_t\,e_t+\vec Q/Q_t)=Q_t e_t+\vec Q$; in the scalar case, $\exp(\operatorname{Log}Q_t)=Q_t$.

**Left inverse.** For every $\tilde Q_1\in D$,

$$
\operatorname{Log}(\exp\tilde Q_1)=\tilde Q_1.
$$

For a general $\tilde Q_1$, the principal logarithm of $\exp\tilde Q_1$ is the unique element of $D$ in the fibre, and it differs from $\tilde Q_1$ by a kernel element. In the oscillatory regime, let $\mu_\pm$ be the eigenvalues of $\tilde Q_1$ and let $m_\pm$ be the integers with $\operatorname{Im}(\mu_\pm-2\pi i m_\pm)\in(-\pi,\pi]$. Then

$$
\operatorname{Log}(\exp\tilde Q_1)=\tilde Q_1-2\pi i\bigl(m_+\tilde\Pi_++m_-\tilde\Pi_-\bigr).
$$

In the nilpotent regime, for $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ with $\vec Q_1^2=0$,

$$
\operatorname{Log}(\exp\tilde Q_1)=\tilde Q_1-2\pi i m e_t,
$$

where $m$ is the integer with $\operatorname{Im}(Q_{1t}-2\pi i m)\in(-\pi,\pi]$. In the scalar case, the principal logarithm is $\operatorname{Log}Q_t\,e_t$, and the difference $\tilde Q_1-\operatorname{Log}Q_t\,e_t$ is a kernel element, which may have a nonzero vector part.

At an eigenvalue with imaginary part exactly $\pi$, the half-open strip chooses the endpoint; this is the same convention as the principal complex logarithm.

**Caution.** The logarithm is not additive in general. For commuting $\tilde Q_1$ and $\tilde Q_2$, a sum of a logarithm of $\tilde Q_1$ and a logarithm of $\tilde Q_2$ is a logarithm of $\tilde Q_1\tilde Q_2$, and the principal values satisfy the corresponding identity only when the sum of the two principal logarithms lies in $D$. It fails for noncommuting arguments.

**Conjugation.** The principal logarithm commutes with quaternion conjugation,

$$
\operatorname{Log}(\tilde Q^{\natural})=(\operatorname{Log}\tilde Q)^{\natural},
$$

on its domain. The square root $B$ can be chosen the same for $\tilde Q$ and $\tilde Q^{\natural}$; then $\vec U$ changes sign, $\lambda_+$ and $\lambda_-$ are exchanged, and both sides change sign in the vector part.

### The Derivative

On the complement of the walls the logarithm is real-analytic, and its differential at $\tilde Q$ is the inverse of the differential of the exponential at $\operatorname{Log}\tilde Q$. It is not left or right multiplication by $\tilde Q^{-1}$.

For $B\neq0$, with the eigenprojections $\tilde\Pi_\pm$ and the eigenvalues $\lambda_\pm$,

$$
\boxed{\; d\operatorname{Log}_{\tilde Q}(H)
=\frac{\tilde\Pi_+H\tilde\Pi_+}{\lambda_+}
+\frac{\tilde\Pi_-H\tilde\Pi_-}{\lambda_-}
+\frac{\operatorname{Log}\lambda_+-\operatorname{Log}\lambda_-}{\lambda_+-\lambda_-}
\bigl(\tilde\Pi_+H\tilde\Pi_-+\tilde\Pi_-H\tilde\Pi_+\bigr) \;}.
$$

This is the Fréchet derivative of the matrix logarithm, read in the algebra. If $H$ commutes with $\tilde Q$, the cross terms vanish and

$$
d\operatorname{Log}_{\tilde Q}(H)=\tilde Q^{-1}H.
$$

If $H$ does not commute with $\tilde Q$, the cross terms need not vanish, and the derivative is not a multiplication by $\tilde Q^{-1}$ on either side.

**Example.** Take $\tilde Q=(3+i)e_t+4\vec e_x$ and $H=\vec e_y$. The eigenvalues are $\lambda_+=3+5i$ and $\lambda_-=3-3i$, and the formula gives

$$
d\operatorname{Log}_{\tilde Q}(\vec e_y)=\Delta\,\vec e_y,
\qquad
\Delta=\frac{\operatorname{Log}(3+5i)-\operatorname{Log}(3-3i)}{8i}
=0.2269718737-0.0397492979i.
$$

A central difference with step $10^{-6}$ reproduces the value to $3.5\times10^{-15}$. By contrast,

$$
\tilde Q^{-1}\vec e_y
=(0.1274509804+0.0098039216i)\vec e_y
+(-0.1568627451+0.0392156863i)\vec e_z,
$$

which has a component in $\vec e_z$ that the derivative does not have. The logarithm is a real-analytic map of eight real variables; it is not a biquaternion multiplication, and the complex identity $d\operatorname{Log}_{\tilde Q}(H)=\tilde Q^{-1}H$ is recovered only on the subspace of directions that commute with $\tilde Q$. In the nilpotent regime, write $\tilde Q=a e_t+N$ with $a=Q_t$ and $N=\vec Q$, so that $N^2=0$, and write $H=h_t e_t+\vec H$. The same series, or the resolvent integral, gives

$$
d\operatorname{Log}_{\tilde Q}(H)
=\frac{H}{a}-\frac{NH+HN}{2a^2}+\frac{NHN}{3a^3},
\qquad N^2=0.
$$

The series terminates after the third term because $N^3=0$. Multiplication by $\tilde Q^{-1}=e_t/a-N/a^2$ is $H/a-NH/a^2$, so the derivative differs from it by $(NH-HN)/(2a^2)+NHN/(3a^3)$. It agrees with the multiplication when $H$ commutes with $N$, and not on every direction that leaves the centraliser.

**The power law.** For every integer $n$,

$$
\exp(n\operatorname{Log}\tilde Q)=\tilde Q^n.
$$

Thus $n\operatorname{Log}\tilde Q$ is a logarithm of $\tilde Q^n$; the principal values of the two sides agree only when $n\operatorname{Log}\tilde Q$ lies in $D$. The identity $\log(\tilde Q^n)=n\log\tilde Q$ therefore holds between the multi-valued logarithms, and not in general between principal values.

### Summary of the Logarithm

| Case | A logarithm | Principal logarithm | Fibre |
|---|---|---|---|
| $B\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ | $\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-$, $\mu_\pm=\operatorname{Log}\lambda_\pm+2\pi i k_\pm$ | the same with principal $\operatorname{Log}\lambda_\pm$ | coset of the parity-matched lattice |
| $B\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ | none | none | empty |
| $B=0$, $\vec Q\neq0$, $Q_t\neq0$ | $(\operatorname{Log}Q_t+2\pi i k)e_t+\vec Q/Q_t$ | $\operatorname{Log}Q_t\,e_t+\vec Q/Q_t$ | $2\pi i\mathbb Z e_t$ |
| $B=0$, $\vec Q\neq0$, $Q_t=0$ | none | none | empty |
| $\vec Q=0$ | scalar and vector values of §*The Degenerate Regimes* | $\operatorname{Log}Q_t\,e_t$ | translate of $\ker\exp$ |

Every $N$-regular biquaternion has a logarithm, the Jordan case included. The $N$-degenerate biquaternion has none, the zero divisor and the pure nilpotent included. The principal logarithm is single-valued and satisfies $\exp(\operatorname{Log}\tilde Q)=\tilde Q$; it is discontinuous on the walls where an eigenvalue is a negative real number, and no continuous single-valued branch exists on the whole unit group. The ambiguity of the logarithm is the kernel of the exponential, constrained by the centraliser when the element is not scalar.

## Powers and Roots

### The Power Function

For $\tilde Q\in\mathbb B$ and $\alpha\in\mathbb C$, the **power function** is defined by

$$
\tilde Q^\alpha=\exp(\alpha\operatorname{Log}\tilde Q)
$$

on the principal branch, and by $\exp(\alpha\tilde Q_{\log})$ for any logarithm $\tilde Q_{\log}$ in the multi-valued reading. For general $\alpha$ the domain is the group of units $\mathbb B^\times$; for $\alpha$ a non-negative integer the power is also defined on all of $\mathbb B$ by repeated multiplication. The power inherits the multivaluedness of the logarithm: it is single-valued for integer $\alpha$, finite-valued for rational $\alpha$ in the generic case, and infinite-valued for irrational $\alpha$. The formulas below give the principal branch unless stated otherwise.

**The case $B\neq0$.** On the principal branch, with the principal $R$ and $\Theta$ of §*The Eigenvalue Formula*,

$$
\tilde Q^\alpha
=R^\alpha\bigl(\cos(\alpha\Theta)\,e_t+\sin(\alpha\Theta)\,\vec U\bigr),
\qquad B\neq0.
$$

Read on all logarithms, the values are

$$
\tilde Q^\alpha
=\exp(\alpha\operatorname{Log}\tilde Q)
\exp\bigl(\alpha(\pi i m\,e_t+\pi n\,\vec U)\bigr),
\qquad m\equiv n\pmod2,
$$

and the second factor is

$$
\exp\bigl(\alpha(\pi i m\,e_t+\pi n\,\vec U)\bigr)
=\exp(\alpha\pi i m)\bigl(\cos(\alpha\pi n)+\sin(\alpha\pi n)\,\vec U\bigr).
$$

For $\alpha=r/s$ rational in lowest terms this set is finite; for irrational $\alpha$ it is countably infinite; for integer $\alpha$ it collapses to the single value $\tilde Q^\alpha$ by repeated multiplication. The parity condition is the same one that governs the logarithm: the scalar and angular shifts cannot be chosen independently.

**The case $B=0$, $\vec Q\neq0$.** In the nilpotent regime the principal value is

$$
\tilde Q^\alpha
=Q_t^\alpha e_t+\alpha Q_t^{\alpha-1}\vec Q,
\qquad B=0,\quad \vec Q\neq0,
$$

with $Q_t\neq0$ required for invertibility. The linear term $\alpha Q_t^{\alpha-1}\vec Q$ is the analogue of the expansion $(1+a)^\alpha\approx1+\alpha a$ for $a^2=0$. The general values are

$$
\tilde Q^\alpha
=\exp(2\pi i\alpha k)\bigl(Q_t^\alpha e_t+\alpha Q_t^{\alpha-1}\vec Q\bigr),
\qquad k\in\mathbb Z.
$$

For integer $\alpha$ the phase is $1$ and the power is single-valued; for non-integer rational $\alpha$ the set is finite; for irrational $\alpha$ it is countably infinite.

**The case $\vec Q=0$.** If $\tilde Q=Q_t e_t$, the principal value is the ordinary complex power $Q_t^\alpha$. Read on all logarithms, the power is larger. The scalar logarithms give the values

$$
Q_t^\alpha \exp(2\pi i\alpha k),\qquad k\in\mathbb Z,
$$

and the vector logarithms of §*The Degenerate Regimes* give, for each $n\in\mathbb Z\setminus\{0\}$, each $k\in\mathbb Z$ and each $\vec Q_1$ with $(\vec Q_1,\vec Q_1)=(\pi n)^2$,

$$
\exp\bigl(\alpha(\operatorname{Log}Q_t+\pi i n+2\pi i k)\bigr)\exp(\alpha\vec Q_1).
$$

The vector part ranges over the complex quadric $(\vec Q_1,\vec Q_1)=(\pi n)^2$, so this part of the set can be continuous even when $\alpha$ is rational. In particular the square roots of $e_t$ are not two: for every root $\vec U$ of $-e_t$, the element $i\vec U$ satisfies $(i\vec U)^2=e_t$. The statement that a square root has only two branches is a non-real quaternion statement and is false in $\mathbb B$.

The three cases are collected in one table.

| Case | Principal value | Full set of values |
|---|---|---|
| Oscillatory unit, $B\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ | $R^\alpha(\cos(\alpha\Theta)e_t+\sin(\alpha\Theta)\vec U)$ | multiply by $\exp(\alpha\pi i m)(\cos(\alpha\pi n)+\sin(\alpha\pi n)\vec U)$, $m\equiv n\pmod2$ |
| Jordan unit, $B=0$, $\vec Q\neq0$, $Q_t\neq0$ | $Q_t^\alpha e_t+\alpha Q_t^{\alpha-1}\vec Q$ | multiply by $\exp(2\pi i\alpha k)$, $k\in\mathbb Z$ |
| Scalar unit, $\vec Q=0$, $Q_t\neq0$ | $Q_t^\alpha$ | scalar phases and vector quadrics described above |
| Oscillatory zero divisor, $B\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ | none | none |
| Nonzero nilpotent, $B=0$, $\vec Q\neq0$, $Q_t=0$ | none | none |

The table gives the principal branch in the middle column and the complete multi-valued set in the right column. The zero divisor and the pure nilpotent have no general power; both have the polynomial powers for non-negative integers.

### Properties

| Property | Statement |
|---|---|
| Single-valued | exactly when $\alpha\in\mathbb{Z}$; finite for rational $\alpha$, infinite for irrational $\alpha$, with continuous families on the scalar axis |
| Product law | $\tilde Q^{\alpha+\beta}=\tilde Q^\alpha\tilde Q^\beta$ for a fixed logarithm; it fails between different bases |
| Power of a power | $(\tilde Q^\alpha)^\beta=\tilde Q^{\alpha\beta}$ when the branches are compatible |
| Norm | $\langle\tilde Q^\alpha\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}^\alpha$, with compatible branches |

**Integer powers.** For integer $n$, the power function is single-valued on $\mathbb B^\times$ and equals the ordinary power $\tilde Q^n$. For non-negative $n$ the ordinary power is defined by repeated multiplication on all of $\mathbb B$, including the zero divisors; for negative $n$ it is defined on the units. The formula $\tilde Q^n=\exp(n\tilde Q_{\log})$ holds on the units for every logarithm, and the identity $\operatorname{Log}(\tilde Q^n)=n\operatorname{Log}\tilde Q$ holds when $n\operatorname{Log}\tilde Q$ lies in the principal domain.

**Non-multiplicativity.** In general,

$$
(\tilde Q_1\tilde Q_2)^\alpha\neq\tilde Q_1^\alpha\tilde Q_2^\alpha,
$$

because the logarithm is not multiplicative.

### The Roots

For $n\ge1$, a **root** of $\tilde Q$ is an element $\tilde R$ with $\tilde R^n=\tilde Q$. The count is read from the regime.

**Theorem (the roots).** Let $n\ge1$ and let $\tilde Q\in\mathbb B$. For $n=1$ the root is $\tilde Q$ itself.

1. If $B\neq0$ and $\langle\tilde Q\rangle_{\natural}\neq0$, there are exactly $n^{2}$ roots.
2. If $B\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ and $Q_t\neq0$, there are exactly $n$ roots, none of them units.
3. If $B=0$, $\vec Q\neq0$ and $Q_t\neq0$, there are exactly $n$ roots.
4. If $B=0$, $\vec Q\neq0$ and $Q_t=0$, there is none.
5. If $\vec Q=0$ and $Q_t\neq0$, there is a continuous family for $n\ge2$.
6. If $\tilde Q=0$, there is a continuous family for $n\ge2$, namely every nilpotent $\tilde R$.

*Proof.* In case 1 the element is diagonalisable with distinct eigenvalues, and a root commutes with $\tilde Q$, hence is diagonal in the same eigenbasis: each eigenvalue has $n$ roots, giving $n^{2}$. In case 2 one eigenvalue is $0$ and the other is not, so the count is $n\cdot1=n$ and every root is singular. In case 3 the element is $Q_t e_t+\vec Q$ with $\vec Q^{2}=0$; a root lies in the centraliser $\{a e_t+b\vec Q\}$ of a nonzero nilpotent (§*The Degenerate Regimes*) and has the form $a e_t+b\vec Q$, and $(a e_t+b\vec Q)^n=a^n e_t+na^{n-1}b\,\vec Q$, so $a^n=Q_t$ and $b=1/(na^{n-1})$, giving $n$ roots. In case 4 a root would have every eigenvalue $0$, hence would be nilpotent with $\tilde R^n=0\neq\tilde Q$. In case 5 a root has no nilpotent part, since $\tilde R^n$ would then have one while $Q_t e_t$ does not; it is diagonalisable with eigenvalues $\mu_\pm$ satisfying $\mu_\pm^n=Q_t$. When $\mu_+\neq\mu_-$, which is possible for $n\ge2$, the eigenprojections vary continuously with the axis, so the root set is a continuous family. In case 6 a root satisfies $\tilde R^n=0$, so $\tilde R$ is nilpotent, and every nilpotent does; this set is a continuous family.

| Case | Condition on $(Q_t,B)$ | Number of roots |
|---|---|---|
| Oscillatory unit | $B\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ | $n^{2}$ |
| Oscillatory zero divisor | $B\neq0$, $\langle\tilde Q\rangle_{\natural}=0$, $Q_t\neq0$ | $n$ |
| Jordan unit | $B=0$, $\vec Q\neq0$, $Q_t\neq0$ | $n$ |
| Nonzero nilpotent | $B=0$, $\vec Q\neq0$, $Q_t=0$ | $0$ |
| Scalar unit | $\vec Q=0$, $Q_t\neq0$ | continuous family, $n\ge2$ |
| Zero | $\tilde Q=0$ | continuous family, $n\ge2$ |

For $n=2$ the table gives the square roots: four for an oscillatory unit, two for an oscillatory zero divisor, two for a Jordan unit, none for a nonzero nilpotent, and a continuous family on the scalar axis and at $0$. In the oscillatory unit case they are $\pm R_0$ and $\pm i\vec U R_0$, where $R_0=\exp(\tfrac12\operatorname{Log}\tilde Q)$ is the principal square root; in the oscillatory zero-divisor case they are $\pm\sqrt{2Q_t}\,\tilde\Pi_\sigma$, the roots of the nonzero eigenvalue $2Q_t$; in the Jordan case they are $\pm R_0$; and the square roots of $e_t$ include $i\vec U$ for every root $\vec U$ of $-e_t$. The principal branch gives one of the four values in the oscillatory regime; the other three come from shifting the two eigenvalue logarithms independently by $2\pi i$, modulo the shifts that leave the root fixed. The two-branch picture of the non-real quaternion case does not survive the complexification.

**Consistency with the biquaternion norm.** For a fixed compatible choice of branch, the power function satisfies

$$
\langle\tilde Q^\alpha\rangle_{\natural}
=\langle\tilde Q\rangle_{\natural}^\alpha.
$$

For the principal branch in the oscillatory regime,

$$
\tilde Q^\alpha=R^\alpha\bigl(\cos(\alpha\Theta)e_t+\sin(\alpha\Theta)\vec U\bigr),
$$

so

$$
\langle\tilde Q^\alpha\rangle_{\natural}
=R^{2\alpha}\bigl(\cos^2(\alpha\Theta)+\sin^2(\alpha\Theta)\bigr)
=R^{2\alpha}
=(R^2)^\alpha
=\langle\tilde Q\rangle_{\natural}^\alpha.
$$

In the nilpotent regime,

$$
\langle\tilde Q^\alpha\rangle_{\natural}
=(Q_t^\alpha)^2+0
=Q_t^{2\alpha}
=\langle\tilde Q\rangle_{\natural}^\alpha.
$$

The identity is **branch-dependent**: the powers $R^\alpha$ and $R^{2\alpha}$, or $Q_t^\alpha$ and $Q_t^{2\alpha}$, must be chosen compatibly. The principal branch of $\tilde Q^\alpha$ satisfies it with the branch of $\langle\tilde Q\rangle_{\natural}^\alpha$ determined by the same logarithm; that branch need not be the principal branch of the scalar power. The scalar axis already shows the point: $(-e_t)^{1/2}=i e_t$ has norm $-1$, while $\langle -e_t\rangle_{\natural}=1$ and its principal square root is $1$. If a non-scalar logarithm of a scalar is used, the vector factor has norm $1$ but the scalar phase can change the two sides by a root of unity; the identity is then read with that phase.

### The $n$-th Root Limits

Let $\tilde Q$ be a unit and let $L$ be a chosen logarithm of $\tilde Q$. Then

$$
\tilde Q^{1/n}=\exp(L/n).
$$

In the Euclidean norm on $\mathbb B$,

$$
\exp(L/n)=e_t+\frac{L}{n}+O(1/n^2),
$$

so

$$
n\bigl(\tilde Q^{1/n}-e_t\bigr)\longrightarrow L.
$$

On the principal branch $L=\operatorname{Log}\tilde Q$, and the limit is the principal logarithm. The limit depends on the branch when the branch is changed; at a unit where the principal logarithm is defined, the principal root gives the principal logarithm.

The mean-root corollaries of *Quaternion Special Functions* hold with the same proof. For the principal branch,

$$
\lim_{n\to\infty}\left(\frac{e_t+\tilde Q^{1/n}}{2}\right)^n=\tilde Q^{1/2},
$$

and for several units on the principal domain,

$$
\lim_{n\to\infty}\left(\frac1k\sum_{\nu=1}^k\tilde Q_\nu^{1/n}\right)^n
=\exp\left(\frac1k\sum_{\nu=1}^k\operatorname{Log}\tilde Q_\nu\right),
$$

the right-hand side being the exponential of the mean of the principal logarithms. The modulus caution is stronger than in the quaternion case: the biquaternion norm is complex, so the modulus of the limit is not the limit of the moduli in any ordered sense. Only the algebraic identity $\langle\exp\tilde Q_1\rangle_{\natural}=\exp(2\operatorname{Sc}\tilde Q_1)$ remains.

## The Trigonometric and Hyperbolic Functions

### Definitions

The trigonometric and hyperbolic functions are defined by the same power series as in the complex case:

$$
\sin(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{(-1)^n \tilde{Q}^{2n+1}}{(2n+1)!}, \qquad \cos(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{(-1)^n \tilde{Q}^{2n}}{(2n)!},
$$

$$
\sinh(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^{2n+1}}{(2n+1)!}, \qquad \cosh(\tilde{Q}) = \sum_{n=0}^{\infty} \frac{\tilde{Q}^{2n}}{(2n)!}.
$$

These series converge for every $\tilde{Q} \in \mathbb{B}$, for the same reason as the exponential.

### The Closed Forms

The functions are the complex power series read in the commutative subalgebra $\mathbb{C}[\tilde Q]$. Equivalently, they are expressed through the exponential by

$$
\sin\tilde Q=\frac{\exp(i\tilde Q)-\exp(-i\tilde Q)}{2i},\qquad
\cos\tilde Q=\frac{\exp(i\tilde Q)+\exp(-i\tilde Q)}{2},
$$

$$
\sinh\tilde Q=\frac{\exp(\tilde Q)-\exp(-\tilde Q)}{2},\qquad
\cosh\tilde Q=\frac{\exp(\tilde Q)+\exp(-\tilde Q)}{2},
$$

where $i$ is the scalar imaginary and commutes with everything.

**The oscillatory case.** For $B\neq0$, substitute the closed form of the exponential:

$$
\sin\tilde Q=\sin Q_t\cosh B\,e_t+\cos Q_t\sinh B\,\vec U,
\qquad
\cos\tilde Q=\cos Q_t\cosh B\,e_t-\sin Q_t\sinh B\,\vec U,
$$

$$
\sinh\tilde Q=\sinh Q_t\cos B\,e_t+\cosh Q_t\sin B\,\vec U,
\qquad
\cosh\tilde Q=\cosh Q_t\cos B\,e_t+\sinh Q_t\sin B\,\vec U.
$$

**The nilpotent case.** If $B=0$, then $\vec Q^2=0$ and $\tilde Q^n=Q_t^n e_t+nQ_t^{n-1}\vec Q$ for $n\ge1$. The series truncate after the linear term:

$$
\sin\tilde Q=\sin Q_t\,e_t+\cos Q_t\,\vec Q,
\qquad
\cos\tilde Q=\cos Q_t\,e_t-\sin Q_t\,\vec Q,
$$

$$
\sinh\tilde Q=\sinh Q_t\,e_t+\cosh Q_t\,\vec Q,
\qquad
\cosh\tilde Q=\cosh Q_t\,e_t+\sinh Q_t\,\vec Q.
$$

**The scalar case.** If $\vec Q=0$, both formulas reduce to the ordinary complex functions.

The four closed forms are collected in one table.

| Function | $B\neq0$ | $B=0$ |
|---|---|---|
| $\sin\tilde Q$ | $\sin Q_t\cosh B\,e_t+\cos Q_t\sinh B\,\vec U$ | $\sin Q_te_t+\cos Q_t\vec Q$ |
| $\cos\tilde Q$ | $\cos Q_t\cosh B\,e_t-\sin Q_t\sinh B\,\vec U$ | $\cos Q_te_t-\sin Q_t\vec Q$ |
| $\sinh\tilde Q$ | $\sinh Q_t\cos B\,e_t+\cosh Q_t\sin B\,\vec U$ | $\sinh Q_te_t+\cosh Q_t\vec Q$ |
| $\cosh\tilde Q$ | $\cosh Q_t\cos B\,e_t+\sinh Q_t\sin B\,\vec U$ | $\cosh Q_te_t+\sinh Q_t\vec Q$ |

In the table, $B=\sqrt{Q_x^2+Q_y^2+Q_z^2}$ and $\vec U=\vec Q/B$.

### Identities, Periods and Zeros

| Property | Statement |
|---|---|
| Pythagorean | $\sin^2\tilde Q+\cos^2\tilde Q=e_t$, $\cosh^2\tilde Q-\sinh^2\tilde Q=e_t$ |
| Addition | the standard formulas hold when the arguments commute; they fail in general |
| Hyperbolic addition | the standard formulas hold when the arguments commute; they fail in general |
| Double angle | $\sin(2\tilde Q)=2\sin\tilde Q\cos\tilde Q$, $\cos(2\tilde Q)=\cos^2\tilde Q-\sin^2\tilde Q$, $\sinh(2\tilde Q)=2\sinh\tilde Q\cosh\tilde Q$, $\cosh(2\tilde Q)=\cosh^2\tilde Q+\sinh^2\tilde Q$ |
| Rotation | $\sin(i\tilde Q)=i\sinh\tilde Q$, $\cos(i\tilde Q)=\cosh\tilde Q$, $\sinh(i\tilde Q)=i\sin\tilde Q$, $\cosh(i\tilde Q)=\cos\tilde Q$ |
| Period of $\sin,\cos$ | $2\pi e_t$; the full period set depends on $\tilde Q$ |
| Period of $\sinh,\cosh$ | $2\pi i e_t$; the full period set depends on $\tilde Q$ |
| Zeros of $\sin$ | $Q_t\in\pi\mathbb Z$ and $B\in\pi i\mathbb Z$, or $Q_t\in\frac{\pi}{2}+\pi\mathbb Z$ and $B\in\frac{i\pi}{2}+i\pi\mathbb Z$ |
| Zeros of $\cos$ | $Q_t\in\frac{\pi}{2}+\pi\mathbb Z$ and $B\in\pi i\mathbb Z$, or $Q_t\in\pi\mathbb Z$ and $B\in\frac{i\pi}{2}+i\pi\mathbb Z$ |
| Zeros of $\sinh$ | $Q_t\in\pi i\mathbb Z$ and $B\in\pi\mathbb Z$, or $Q_t\in\frac{i\pi}{2}+i\pi\mathbb Z$ and $B\in\frac{\pi}{2}+\pi\mathbb Z$ |
| Zeros of $\cosh$ | $Q_t\in\frac{i\pi}{2}+i\pi\mathbb Z$ and $B\in\pi\mathbb Z$, or $Q_t\in\pi i\mathbb Z$ and $B\in\frac{\pi}{2}+\pi\mathbb Z$ |
| Zero divisors of $\sin$ | $\sin^2Q_t+\sinh^2B=0$ |
| Zero divisors of $\cos$ | $\cos^2Q_t+\sinh^2B=0$ |
| Zero divisors of $\sinh$ | $\sinh^2Q_t+\sin^2B=0$ |
| Zero divisors of $\cosh$ | $\cosh^2Q_t-\sin^2B=0$ |
| Boundedness | all four are unbounded, since $B$ and $Q_t$ are complex |

A value is zero or a zero divisor exactly when its biquaternion norm vanishes; for $a e_t+b\vec U$ the norm is $a^2+b^2$, which gives the four equations. The central periods are the only periods independent of the element. Further periods are read from the eigenvalues in the oscillatory regime and from the truncated forms in the nilpotent regime; they do not form a fixed lattice in $\mathbb{B}$. The zeros are collected in the table.

**Pythagorean identity.** The identity

$$
\sin^2(\tilde{Q}) + \cos^2(\tilde{Q}) = e_t
$$

holds for every $\tilde{Q} \in \mathbb{B}$.

**Proof.** Write $A = \exp(i\tilde{Q})$ and $B = \exp(-i\tilde{Q})$. Since $i\tilde{Q}$ commutes with $-i\tilde{Q}$, we have $AB = \exp(i\tilde{Q})\exp(-i\tilde{Q}) = \exp(i\tilde{Q}-i\tilde{Q}) = e_t$. Then

$$
\sin^2(\tilde{Q}) + \cos^2(\tilde{Q})
= \frac{(A - B)^2}{-4} + \frac{(A + B)^2}{4}
= \frac{-(A^2 - 2AB + B^2) + (A^2 + 2AB + B^2)}{4}
= \frac{4AB}{4}
= AB
= e_t.
$$

Alternatively, in the oscillatory regime, a direct expansion gives

$$
\sin^2(\tilde{Q}) + \cos^2(\tilde{Q}) = (\cosh^2 B - \sinh^2 B) e_t = e_t,
$$

since the vector parts cancel by antisymmetry and the scalar parts combine via the hyperbolic identity.

The reason the identity survives the non-commutativity of $\mathbb{B}$ is that both $\sin(\tilde{Q})$ and $\cos(\tilde{Q})$ lie in the **commutative subalgebra** $\mathbb{C}[\tilde{Q}]$ generated by $\tilde{Q}$, within which the standard complex-analytic identities hold. The identity fails only for expressions involving two or more independent biquaternions (see the addition formulas below).

**Hyperbolic identity.** The identity

$$
\cosh^2(\tilde{Q}) - \sinh^2(\tilde{Q}) = e_t
$$

holds for every $\tilde{Q} \in \mathbb{B}$.

**Proof.** Write $A = \exp(\tilde{Q})$ and $B = \exp(-\tilde{Q})$. Since $\tilde{Q}$ commutes with $-\tilde{Q}$, we have $AB = \exp(\tilde{Q}-\tilde{Q}) = e_t$. Then

$$
\cosh^2(\tilde{Q}) - \sinh^2(\tilde{Q})
= \frac{(A + B)^2 - (A - B)^2}{4}
= \frac{(A^2 + 2AB + B^2) - (A^2 - 2AB + B^2)}{4}
= \frac{4AB}{4}
= AB
= e_t.
$$

**Double-angle formulas.** The standard double-angle formulas hold:

$$
\sin(2\tilde{Q}) = 2\sin(\tilde{Q})\cos(\tilde{Q}), \qquad \cos(2\tilde{Q}) = \cos^2(\tilde{Q}) - \sin^2(\tilde{Q}),
$$

$$
\sinh(2\tilde{Q}) = 2\sinh(\tilde{Q})\cosh(\tilde{Q}), \qquad \cosh(2\tilde{Q}) = \cosh^2(\tilde{Q}) + \sinh^2(\tilde{Q}).
$$

These follow from the corresponding identities in the commutative subalgebra $\mathbb{C}[\tilde{Q}]$.

**Addition formulas.** The addition formulas, such as

$$
\sin(\tilde{Q}_1 + \tilde{Q}_2) = \sin(\tilde{Q}_1)\cos(\tilde{Q}_2) + \cos(\tilde{Q}_1)\sin(\tilde{Q}_2),
$$

hold **if $\tilde{Q}_1$ and $\tilde{Q}_2$ commute**. In general they fail. For instance, with $\tilde{Q}_1 = \vec e_x$ and $\tilde{Q}_2 = \vec e_y$, each is pure with complex norm $1$, so

$$
\sin(\vec e_x) = \sinh(1) \vec e_x, \qquad \cos(\vec e_x) = \cosh(1) e_t,
$$

$$
\sin(\vec e_y) = \sinh(1) \vec e_y, \qquad \cos(\vec e_y) = \cosh(1) e_t,
$$

and hence

$$
\sin(\vec e_x)\cos(\vec e_y) + \cos(\vec e_x)\sin(\vec e_y) = \sinh(1)\cosh(1)(\vec e_x + \vec e_y) = \tfrac{1}{2}\sinh(2)(\vec e_x + \vec e_y).
$$

On the other hand, $\vec e_x + \vec e_y$ is pure with complex norm $\sqrt{2}$, so

$$
\sin(\vec e_x + \vec e_y) = \frac{\sinh\sqrt{2}}{\sqrt{2}}(\vec e_x + \vec e_y).
$$

These are unequal: $\tfrac{1}{2}\sinh(2) \approx 1.813$, whereas $\sinh\sqrt{2}/\sqrt{2} \approx 1.368$. The failure is a genuine consequence of non-commutativity.

**Relation to the exponential.** The relations $\sin(\tilde{Q}) = (\exp(i\tilde{Q}) - \exp(-i\tilde{Q}))/(2i)$ and so on hold in general, because the scalar imaginary $i$ commutes with everything.

**No inequalities.** The inequalities of *Quaternion Special Functions*, §*Inequalities*, do not carry over to $\mathbb B$. They rest on the real, non-negative quaternion norm $\langle\tilde q\rangle_{\natural}$ and on the real modulus of the vector part. In the biquaternion algebra the algebraic norm $\langle\tilde Q\rangle_{\natural}$ is complex and $B$ is a complex square root; neither has an order, and the trigonometric functions take values in a complex two-dimensional algebra. The Euclidean norm can be used, but the bounds then involve $|\cosh B|$ and $|\sinh B|$ and are not the quaternion bounds. The article therefore states no inequalities in $\mathbb B$. On a real quaternion slice, where $Q_t$ and $\vec Q$ are real, the quaternion inequalities apply unchanged.

### The Other Functions

The remaining elementary functions are the quotients

$$
\tan\tilde Q=\frac{\sin\tilde Q}{\cos\tilde Q},\qquad
\cot\tilde Q=\frac{\cos\tilde Q}{\sin\tilde Q},\qquad
\sec\tilde Q=\frac{e_t}{\cos\tilde Q},\qquad
\csc\tilde Q=\frac{e_t}{\sin\tilde Q},
$$

$$
\tanh\tilde Q=\frac{\sinh\tilde Q}{\cosh\tilde Q},\qquad
\coth\tilde Q=\frac{\cosh\tilde Q}{\sinh\tilde Q},\qquad
\operatorname{sech}\tilde Q=\frac{e_t}{\cosh\tilde Q},\qquad
\operatorname{csch}\tilde Q=\frac{e_t}{\sinh\tilde Q}.
$$

They are defined wherever the denominator is $N$-regular. In $\mathbb B$ a denominator can be $N$-degenerate without being zero, so the domain is smaller than the complement of the zero set; the singularities are the $N$-degenerate values of $\cos$, $\sin$, $\cosh$ and $\sinh$.

In the oscillatory regime $B\neq0$, with $\vec U=\vec Q/B$, conjugation by the root $\vec U$ of $-e_t$ gives

$$
\tan\tilde Q=-\vec U\,\tanh(\tilde Q\vec U),
\qquad
\tanh\tilde Q=-\vec U\,\tan(\tilde Q\vec U),
$$

and the corresponding identities for the reciprocal functions, on the branches where the denominators are units. In the nilpotent and scalar regimes the functions are read from the truncated formulas of §*The Closed Forms*.

### The Inverse Functions

The inverse functions are built from the logarithm and the square root, as in the quaternion and complex cases. On a branch where the square root and the logarithm are defined,

| Function | Formula | Domain |
|---|---|---|
| $\arcsin\tilde Q$ | $-i\operatorname{Log}\bigl(i\tilde Q+(e_t-\tilde Q^2)^{1/2}\bigr)$ | where the square root and the logarithm are defined |
| $\arccos\tilde Q$ | $-i\operatorname{Log}\bigl(\tilde Q+i(e_t-\tilde Q^2)^{1/2}\bigr)$ | where the square root and the logarithm are defined |
| $\arctan\tilde Q$ | $\dfrac{1}{2i}\operatorname{Log}\bigl((e_t+i\tilde Q)(e_t-i\tilde Q)^{-1}\bigr)$ | where $e_t\pm i\tilde Q$ are units |
| $\operatorname{arsinh}\tilde Q$ | $\operatorname{Log}\bigl(\tilde Q+(\tilde Q^2+e_t)^{1/2}\bigr)$ | where the square root and the logarithm are defined |
| $\operatorname{arcosh}\tilde Q$ | $\operatorname{Log}\bigl(\tilde Q+(\tilde Q^2-e_t)^{1/2}\bigr)$ | where the square root and the logarithm are defined |
| $\operatorname{artanh}\tilde Q$ | $\dfrac12\operatorname{Log}\bigl((e_t+\tilde Q)(e_t-\tilde Q)^{-1}\bigr)$ | where $e_t\pm\tilde Q$ are units |

The square root is $\tilde Q_1^{1/2}=\exp(\frac12\operatorname{Log}\tilde Q_1)$ for an element $\tilde Q_1$ on the chosen branch. The formulas are the complex ones read in the commutative subalgebra $\mathbb C[\tilde Q]$; because that subalgebra is commutative, the complex identities that prove them remain valid. They are right inverses on their domains, for example

$$
\sin(\arcsin\tilde Q)=\tilde Q,\qquad
\tanh(\operatorname{artanh}\tilde Q)=\tilde Q,
$$

on the branch where the right-hand side is defined.

The multivaluedness comes from the logarithm and the square root. The branch points are the elements at which the argument of the square root is zero or a zero divisor, and the elements at which $e_t\pm i\tilde Q$ or $e_t\pm\tilde Q$ fail to be invertible. These sets are the complexified analogues of the quaternion branch sets: in the quaternion case the equations $\tilde q^2\pm e_t=0$ give the pair $\tilde q=\pm e_t$ and the unit sphere of pure quaternions, while in $\mathbb B$ each equation defines a complex hypersurface. On the real quaternion slice, with $Q_t$ and $\vec Q$ real, the formulas reduce to the quaternion inverse functions of *Quaternion Special Functions*; the apparent difference of notation is the difference between the sign-conjugation form used there and the complex form used here.

In the nilpotent regime the logarithm is the formula of §*The Degenerate Regimes*, and the square roots are the two values of §*Powers and Roots*; the inverse functions then solve linear equations in $\vec Q$. In the scalar case the formulas reduce to the complex inverse functions in each scalar logarithm, with the vector logarithms adding the families described in §*The Degenerate Regimes*.

## Relations to the Neighbouring Cases

### The Quaternion Case

The biquaternion algebra contains the quaternion algebra $\mathbb{H}$ as the real slice $\mathbb{H}_{\mathbb{B}}$, the fixed-point set of complex conjugation. For a quaternion $\tilde q=q_t e_t+\vec q$ with real coefficients, the complex norm is $B=\sqrt{\langle\vec q\rangle_{\natural}}$, a real non-negative number, and the elementary functions reduce to the ordinary quaternion elementary functions:

$$
\exp(\tilde q)=\exp(q_t)\bigl(\cos\rho+\sin\rho\,\vec u\bigr),
\qquad
\operatorname{Log}(\tilde q)=\ln r+\arccos\frac{q_t}{r}\,\vec u,
$$

and so on, where
$$
\rho=\sqrt{\langle\vec q\rangle_{\natural}},\qquad
r=\sqrt{\langle\tilde q\rangle_{\natural}}=\sqrt{q_t^2+\rho^2},\qquad
\vec u=\frac{\vec q}{\rho},
$$
with $\vec u$ defined for $\vec q\neq0$; for a positive real quaternion the second term of the logarithm is $0$, and the negative real axis is excluded from the branch. The formula is the principal branch on $\mathbb H\setminus(-\infty,0]$, and the biquaternion principal logarithm restricts to it on the real slice. These are the standard formulas of quaternion analysis.

### The Complex Case

The biquaternion algebra contains the complex numbers as the subspace $\mathbb{C}_{\mathbb{B}}$, which is the fixed-point set of quaternion conjugation (the scalar part). For a complex scalar $\tilde{Q} = Q_t e_t$, the vector part vanishes, and the elementary functions reduce to the ordinary complex elementary functions:

$$
\exp(Q_t e_t) = \exp(Q_t) e_t, \qquad \operatorname{Log}(Q_t e_t) = \operatorname{Log}(Q_t) e_t,
$$

and so on. The second formula is the principal branch. The full set of biquaternion logarithms of $Q_t e_t$ is much larger than the complex logarithm: it includes the vector logarithms of §*The Degenerate Regimes*, and it is not discrete. The same distinction applies to the powers of a scalar. These are the standard formulas of complex analysis only after the principal branch is selected.

### The Relation Between the Two

The quaternion case and the complex case are the two extremes of the biquaternion case: the quaternion case is the real slice, where all coefficients are real and $B=\sqrt{\langle\vec Q\rangle_{\natural}}$ is real non-negative; the complex case is the case where $\vec Q = 0$. The general biquaternion case interpolates between the two, with $B$ complex and $\vec Q$ nonzero. The interpolation is not uniform in the logarithm: the scalar case has a larger fibre than the other two, because the centraliser is the whole algebra, and its logarithm is not a lattice coset.

### Open Questions

Several questions are left open by the theory of this article.

1. **Functions of several biquaternion variables.** How do the elementary functions extend to functions of two or more biquaternion variables? The non-commutativity is a serious obstruction, and the theory is largely open.

2. **The transition between the two regimes.** Off the walls where an eigenvalue is a negative real number, the eigenvalue formula makes the degeneration $B\to0$ continuous, and the derivative formula has a confluent limit. What happens at the walls, and which uniform asymptotic expansion interpolates across them, is open.

3. **The complex norm.** What is the geometric or algebraic meaning of the complex norm $B$ when it is not real? The number $B$ is a square root of the quadratic form of the vector part, not of the biquaternion norm, and it is complex for a general biquaternion. It is the analogue of the "magnitude" of the vector part, but its complex-valuedness means it has both a modulus and a phase.

4. **The relation to the analysis.** How do the elementary functions interact with the differential operators of the analysis article? For example, what is $\tilde{\nabla} \exp(\tilde{Q})$ for a general biquaternion $\tilde{Q}$?

5. **The logarithm at the boundary of the $N$-regular set.** The logarithm exists on $\mathbb{B}^\times$ but not on the $N$-degenerate set, the zero divisor set $\mathcal{Z}$ together with the origin $0$. What is the correct object that replaces the logarithm on the boundary? The answer is likely to involve a formal logarithm or a deformation of the algebra.

6. **The derivative of the exponential in the vector directions.** The formula $\partial/\partial Q_k \exp(\tilde{Q}) = \int_0^1 \exp(s \tilde{Q}) \vec e_k \exp((1-s)\tilde{Q})\,ds$ for $k\in\{x,y,z\}$ is the biquaternion analogue of the usual identity for the derivative of the exponential. What are the consequences of this formula for the analysis of biquaternion-valued functions?

## Summary

Every direct elementary function — the exponential, the trigonometric and the hyperbolic functions — is defined by applying the scalar power series to $\tilde{Q}$, and all its values lie in the commutative subalgebra $\mathbb{C}[\tilde{Q}]$ generated by $\tilde{Q}$. This is why the standard identities of complex analysis — the Pythagorean identity, the hyperbolic identity, the double-angle formulas, the relation between the exponential and the trigonometric functions — survive the non-commutativity of $\mathbb{B}$ for a single variable; the addition formulas for two independent biquaternions do not, and fail for explicit counterexamples such as $\tilde{Q}_1 = \vec e_x$, $\tilde{Q}_2 = \vec e_y$.

The structure of $\mathbb{C}[\tilde{Q}]$ is governed by the discriminant and yields exactly two regimes. In the **oscillatory regime** $B \neq 0$ the subalgebra is $\mathbb{C} \times \mathbb{C}$, the element $\tilde{Q}$ is diagonalizable with eigenvalues $Q_t \pm iB$, and the closed forms are the oscillatory-hyperbolic expressions of the collected table, built on $\tilde{Q} = Q_t e_t + B\vec U$ with $\vec U^2 = -e_t$. In the **nilpotent regime** $B = 0$, $\vec Q \neq 0$, the subalgebra is $\mathbb{C}[\epsilon]/(\epsilon^2)$ with the nilpotent $\epsilon = \vec Q$, and every power series truncates after the linear term: the exponential becomes $\exp(Q_t)(e_t + \vec Q)$, the principal logarithm becomes $\operatorname{Log}Q_t\,e_t + \vec Q/Q_t$, and the higher functions reduce to their first-order Taylor expansions in $\vec Q$. The scalar case $\vec Q=0$ is the degenerate end of the nilpotent regime, where $\mathbb C[\tilde Q]=\mathbb C e_t$ and the logarithm is the translate of the kernel described in §*The Degenerate Regimes*, not a lattice coset.

The exponential is the model of the theory. It is never a zero divisor, it satisfies $\exp(\tilde{Q}_1+\tilde{Q}_2) = \exp(\tilde{Q}_1)\exp(\tilde{Q}_2)$ when $\tilde{Q}_1$ and $\tilde{Q}_2$ commute (the converse can fail, §*The Group Law*), and it is surjective onto the group of units: every unit has a logarithm (*Higham, Functions of Matrices*, Theorem 1.27). It is not injective. In the oscillatory regime, with $\lambda_\pm=Q_t\pm iB$ and $\tilde\Pi_\pm=\frac12(e_t\mp i\vec U)$, every logarithm is

$$
\tilde Q_{\log}=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-,
\qquad
\mu_\pm=\operatorname{Log}\lambda_\pm+2\pi i k_\pm,
$$

equivalently

$$
\tilde Q_{\log}
=\frac{\mu_++\mu_-}{2}e_t+\frac{\mu_+-\mu_-}{2i}\vec U.
$$

The principal logarithm uses the principal complex logarithm of each eigenvalue. It is single-valued and real-analytic off the walls where an eigenvalue is a negative real number, and it is the inverse of $\exp$ on the principal domain $D$ of §*The Principal Domain*. In the oscillatory regime the fibre is a coset of the parity-matched lattice

$$
\ker\exp\cap\mathbb C[\tilde Q]
=\bigl\{\pi i m\,e_t+\pi n\,\vec U:\ m,n\in\mathbb Z,\ m\equiv n\pmod2\bigr\},
$$

not the rectangular lattice of independent scalar and angle shifts. No continuous single-valued logarithm exists on all of $\mathbb B^\times$.

In the nilpotent regime the logarithm is

$$
\tilde Q_{\log}=(\operatorname{Log}Q_t+2\pi i k)e_t+\frac{\vec Q}{Q_t},
$$

and in the scalar case it is a scalar logarithm together with the vector logarithms of §*The Degenerate Regimes*; the scalar fibre is a translate of the kernel, and because the kernel is not a subgroup, two logarithms of the same scalar need not differ by a kernel element. The derivative of the logarithm is not multiplication by $\tilde Q^{-1}$: the cross terms of the eigenprojection formula survive whenever the direction does not commute with $\tilde Q$.

The power function is $\tilde Q^\alpha=\exp(\alpha \tilde Q_{\log})$ for a logarithm $\tilde Q_{\log}$. On the principal branch it is given by the formulas of §*Powers and Roots*; the full set of values adds the kernel shifts, and on the scalar axis it includes continuous families. The square root is not a two-valued function in $\mathbb B$: it has four values for a generic oscillatory unit, two for a zero divisor, two for a Jordan unit, none for a nonzero nilpotent, and continuous families on the scalar axis. Because the scalar imaginary $i$ commutes with everything, it relates the trigonometric functions to the exponential and the trigonometric to the hyperbolic functions, but only for a single argument in a common plane.

The exponential, the trigonometric and the hyperbolic functions are defined for every $\tilde{Q} \in \mathbb{B}$; the logarithm is defined only on the group of units $\langle\tilde{Q}\rangle_{\natural} \neq 0$, and the power function is defined there for every complex exponent, and on all of $\mathbb{B}$ for a non-negative integer exponent. The logarithm is many-valued, the ambiguity coming from the kernel of the exponential and, in the scalar case, from the larger centraliser. The principal branch is single-valued and discontinuous on the walls; it is the branch used by default in this article.

### Main Results

| Result | Statement |
|---|---|
| Regimes | $B\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ (distinct), $B\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ (zero divisor), $B=0,\ \vec Q\neq0,\ Q_t\neq0$ (Jordan), $B=0,\ \vec Q\neq0,\ Q_t=0$ (nilpotent), $\vec Q=0$ (scalar) |
| Spectrum | $\lambda_\pm=Q_t\pm iB$, $B^2=Q_x^2+Q_y^2+Q_z^2$; distinct exactly when $B\neq0$ |
| Eigenprojections | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, $\vec\Xi=-i\vec U$, for $B\neq0$ |
| Idempotent Principle | $f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-$ when $B\neq0$; the series truncates when $B=0$ |
| Exponential | $\exp(Q_t)(\cos B\,e_t+\sin B\,\vec U)$ if $B\neq0$; $\exp(Q_t)(e_t+\vec Q)$ if $B=0$ |
| Kernel and image | $\ker\exp$: $\exp\tilde Q_1=e_t$ exactly when $\tilde Q_1$ is diagonalizable with all eigenvalues in $2\pi i\mathbb Z$; not a subgroup. $\operatorname{im}\exp=\mathbb B^\times=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| Logarithm | eigenvalue formula for $B\neq0$ and a unit; $\operatorname{Log}Q_t\,e_t+\vec Q/Q_t$ for $B=0,\vec Q\neq0,Q_t\neq0$; scalar and vector families for $\vec Q=0$; no logarithm for a zero divisor or a nonzero nilpotent |
| Principal domain | $D$: every eigenvalue has imaginary part in $(-\pi,\pi]$; $\exp:D\to\mathbb B^\times$ is bijective |
| Fibre | a coset of $\ker\exp\cap\mathbb C[\tilde Q]$ for a non-scalar unit; the set $\operatorname{Log}Q_t\,e_t+\ker\exp$ for a scalar unit, not a coset in general |
| Derivative of the logarithm | $d\operatorname{Log}_{\tilde Q}(H)=\sum_\pm\lambda_\pm^{-1}\tilde\Pi_\pm H\tilde\Pi_\pm+\frac{\operatorname{Log}\lambda_+-\operatorname{Log}\lambda_-}{\lambda_+-\lambda_-}(\tilde\Pi_+H\tilde\Pi_-+\tilde\Pi_-H\tilde\Pi_+)$; equals $\tilde Q^{-1}H$ when $[H,\tilde Q]=0$ |
| Powers | $\tilde Q^\alpha=\exp(\alpha\operatorname{Log}\tilde Q)$ on the units; the full set is obtained by kernel shifts |
| Roots | $n^{2}$ for an oscillatory unit, $n$ for an oscillatory zero divisor or a Jordan unit, none for a nonzero nilpotent, a continuous family in the scalar case and at $0$ |
| Trigonometric functions | $\sin\tilde Q=\sin Q_t\cosh B\,e_t+\cos Q_t\sinh B\,\vec U$, $\cos\tilde Q=\cos Q_t\cosh B\,e_t-\sin Q_t\sinh B\,\vec U$ |
| Hyperbolic functions | $\sinh\tilde Q=\sinh Q_t\cos B\,e_t+\cosh Q_t\sin B\,\vec U$, $\cosh\tilde Q=\cosh Q_t\cos B\,e_t+\sinh Q_t\sin B\,\vec U$ |
| Identities | the complex identities hold in $\mathbb C[\tilde Q]$; they fail for two non-commuting arguments |
| Periods | $2\pi e_t$ for $\sin$ and $\cos$; $2\pi i e_t$ for $\sinh$ and $\cosh$; no fixed lattice |
| Inverse functions | $\arcsin\tilde Q$, $\arccos\tilde Q$, $\arctan\tilde Q$ and the hyperbolic inverses, built from the logarithm and the square root |

### Formulas

| Function | Value | Domain |
|---|---|---|
| $\exp\tilde Q$ | $B\neq0$: $\exp(Q_t)(\cos B\,e_t+\sin B\,\vec U)$; $B=0$: $\exp(Q_t)(e_t+\vec Q)$ | all $\tilde Q$ |
| $\operatorname{Log}\tilde Q$ | $B\neq0$: $\dfrac{\operatorname{Log}\lambda_++\operatorname{Log}\lambda_-}{2}e_t+\dfrac{\operatorname{Log}\lambda_+-\operatorname{Log}\lambda_-}{2i}\vec U$; $B=0$, $\vec Q\neq0$: $\operatorname{Log}Q_t\,e_t+\vec Q/Q_t$; $\vec Q=0$: $\operatorname{Log}Q_t\,e_t$ | the units |
| $\tilde Q^\alpha$ | $B\neq0$: $R^\alpha(\cos(\alpha\Theta)e_t+\sin(\alpha\Theta)\vec U)$; $B=0$, $\vec Q\neq0$: $Q_t^\alpha e_t+\alpha Q_t^{\alpha-1}\vec Q$ | the units |
| $\sin\tilde Q$ | $B\neq0$: $\sin Q_t\cosh B\,e_t+\cos Q_t\sinh B\,\vec U$; $B=0$: $\sin Q_t\,e_t+\cos Q_t\,\vec Q$ | all $\tilde Q$ |
| $\cos\tilde Q$ | $B\neq0$: $\cos Q_t\cosh B\,e_t-\sin Q_t\sinh B\,\vec U$; $B=0$: $\cos Q_t\,e_t-\sin Q_t\,\vec Q$ | all $\tilde Q$ |
| $\sinh\tilde Q$ | $B\neq0$: $\sinh Q_t\cos B\,e_t+\cosh Q_t\sin B\,\vec U$; $B=0$: $\sinh Q_t\,e_t+\cosh Q_t\,\vec Q$ | all $\tilde Q$ |
| $\cosh\tilde Q$ | $B\neq0$: $\cosh Q_t\cos B\,e_t+\sinh Q_t\sin B\,\vec U$; $B=0$: $\cosh Q_t\,e_t+\sinh Q_t\,\vec Q$ | all $\tilde Q$ |
| $\tan\tilde Q$ | $\sin\tilde Q/\cos\tilde Q$ | $\cos\tilde Q$ a unit |
| $\cot\tilde Q$ | $\cos\tilde Q/\sin\tilde Q$ | $\sin\tilde Q$ a unit |
| $\tanh\tilde Q$ | $\sinh\tilde Q/\cosh\tilde Q$ | $\cosh\tilde Q$ a unit |
| $\coth\tilde Q$ | $\cosh\tilde Q/\sinh\tilde Q$ | $\sinh\tilde Q$ a unit |
| $\operatorname{arsinh}\tilde Q$ | $\operatorname{Log}\bigl(\tilde Q+(\tilde Q^2+e_t)^{1/2}\bigr)$ | where the square root and the logarithm are defined |
| $\operatorname{arcosh}\tilde Q$ | $\operatorname{Log}\bigl(\tilde Q+(\tilde Q^2-e_t)^{1/2}\bigr)$ | where the square root and the logarithm are defined |
| $\operatorname{artanh}\tilde Q$ | $\tfrac12\operatorname{Log}\bigl((e_t+\tilde Q)(e_t-\tilde Q)^{-1}\bigr)$ | where $e_t\pm\tilde Q$ are units |

In the table, $B = \sqrt{Q_x^2 + Q_y^2 + Q_z^2}$, $\vec U = \vec Q/B$, $\lambda_\pm = Q_t \pm iB$, $R = \sqrt{Q_t^2 + B^2}$, $\cos\Theta = Q_t/R$, and $\sin\Theta = B/R$. The exponential and the four trigonometric and hyperbolic functions are defined on all of $\mathbb{B}$. The logarithm and the general power are defined on the units; for a non-negative integer exponent the power is defined on all of $\mathbb{B}$ by repeated multiplication. The $B=0$ formulas for the logarithm and the power assume $Q_t\neq0$, which is automatic for a unit.

The logarithm row gives the principal branch, with the principal complex logarithm in each eigenvalue; a general logarithm is described in §*The Eigenvalue Formula*, and the scalar case adds the vector families of §*The Degenerate Regimes*. The power row gives the principal branch; the full set of values is described in §*Powers and Roots*. On the scalar axis the principal power is the complex power, but the full power can take non-scalar values.

### Comparison with the Neighbouring Cases

The table compares the elementary functions across the three algebras; in the biquaternion column, $B^2=Q_x^2+Q_y^2+Q_z^2$, $\vec U=\vec Q/B$ and $\lambda_\pm=Q_t\pm iB$.

| Feature | Split-complex | Reduced biquaternion | Biquaternion |
|---|---|---|---|
| Algebra | $\mathbb{R}[x]/(x^2-1)\cong\mathbb{R}\times\mathbb{R}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ |
| Element | $Q=q+jq'$ | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $\tilde Q=Q_te_t+\vec Q$ |
| Eigenvalues | $\lambda_\pm=q\pm q'$ | $\lambda_1=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $\lambda_2=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | $\lambda_\pm=Q_t\pm iB$ |
| Spectral calculus | $\Phi(Q)=\Phi(\lambda_+)\Pi_++\Phi(\lambda_-)\Pi_-$ | $f(\breve Q)=f(\lambda_1)\Pi_++f(\lambda_2)\Pi_-$ | $f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-$ if $B\neq0$; truncated if $B=0$ |
| Exponential | $\exp q(\cosh q'+j\sinh q')$ | $\exp Q_{\blacktriangle}(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$ | $\exp Q_t(\cos B\,e_t+\sin B\,\vec U)$ if $B\neq0$; $\exp Q_t(e_t+\vec Q)$ if $B=0$ |
| Kernel | $\{0\}$ | $2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)$ | diagonalisable elements with eigenvalues in $2\pi i\mathbb{Z}$; not a subgroup |
| Image | $F=\{\lambda_\pm>0\}$ | $\{\lambda_1\lambda_2\neq0\}$ | $\{\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| Logarithm domain | $q>\lvert q'\rvert$ | $\lambda_1\lambda_2\neq0$ | $\langle\tilde Q\rangle_{\natural}\neq0$ |
| Logarithm | $\log\lambda_+\Pi_++\log\lambda_-\Pi_-$ | $\log\lambda_1\Pi_++\log\lambda_2\Pi_-$ | $\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-$, $\mu_\pm=\operatorname{Log}\lambda_\pm+2\pi i k_\pm$; Jordan formula if $B=0$ |
| Powers | $Q^P=\lambda_+^P\Pi_++\lambda_-^P\Pi_-$, $P\in\mathbb{R}$, single-valued | $\breve Q^s=\lambda_1^s\Pi_++\lambda_2^s\Pi_-$, multivalued for non-integer $s$ | $\tilde Q^\alpha=\exp(\alpha\operatorname{Log}\tilde Q)$, multivalued; continuous families on the scalar axis |
| Square roots | $4$, $2$, $1$ or $0$, by the signs of $\lambda_\pm$ | $4$ for a unit, $2$ for a zero divisor, $1$ for $0$ | $4$ for a generic unit, $2$ for a zero divisor or a Jordan unit, none for a nonzero nilpotent, a continuous family in the scalar case |
| Trigonometric | $\sin q\cos q'+j\cos q\sin q'$ | $\sin Q_{\blacktriangle}\cos Q_{\blacktriangledown}+j\cos Q_{\blacktriangle}\sin Q_{\blacktriangledown}$ | $\sin Q_t\cosh B\,e_t+\cos Q_t\sinh B\,\vec U$ |
| Hyperbolic | $\sinh q\cosh q'+j\cosh q\sinh q'$ | $\sinh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\cosh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}$ | $\sinh Q_t\cos B\,e_t+\cosh Q_t\sin B\,\vec U$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\tilde{Q} = Q_t e_t + \vec Q$ | Biquaternion; $\vec Q = \sum_{k\in\{x,y,z\}} Q_k \vec e_k$ the vector part |
| $B = \sqrt{Q_x^2+Q_y^2+Q_z^2}$ | Complex norm of the vector part |
| $\vec U = \vec Q/B$ | Axis of the vector part, $\vec U^2 = -e_t$, defined for $B \neq 0$ |
| $R = \sqrt{Q_t^2+B^2} = \sqrt{\langle\tilde{Q}\rangle_{\natural}}$ | A square root of the biquaternion norm; modulus of the logarithm and the power function |
| $\Theta$ | Angle of the logarithm and the power function, $\cos\Theta = Q_t/R$, $\sin\Theta = B/R$ |
| $\lambda_\pm = Q_t \pm iB$ | Eigenvalues of $\tilde Q$ in the oscillatory regime |
| $\vec\Xi = -i\vec U$ | Pure root of $+1$ attached to the axis, $\vec\Xi^2=e_t$ |
| $\tilde\Pi_\pm = \frac12(e_t \pm \vec\Xi)$ | Eigenprojections of $\tilde Q$; $\tilde\Pi_++\tilde\Pi_-=e_t$, $\tilde\Pi_+\tilde\Pi_-=0$ |
| $\operatorname{Log}\tilde Q$ | Principal logarithm, with eigenvalues in the strip $-\pi<\operatorname{Im}z\le\pi$ |
| $\tilde Q_{\log}$ | A logarithm of $\tilde Q$; the subscript labels the element, not an operation |
| $Q_{\log,t}$ | Scalar component of a logarithm, complex; $\operatorname{Re}Q_{\log,t}=\frac12\ln\lvert\langle\tilde Q\rangle_{\natural}\rvert$ |
| $\vec Q_{\log}$ | Vector component of a logarithm, pure; $\tilde Q_{\log}=Q_{\log,t}e_t+\vec Q_{\log}$ |
| $\ker\exp$ | Kernel of the exponential: $\exp\tilde Q_1=e_t$; not a subgroup |
| $\tilde Q^\alpha=\exp(\alpha\operatorname{Log}\tilde Q)$ | Power on the units |
| $\tilde R$ | A root, $\tilde R^n=\tilde Q$ |
| $D$ | Principal domain: every eigenvalue has imaginary part in $(-\pi,\pi]$; $\exp:D\to\mathbb B^\times$ is bijective |
| $\mathbb{C}[\tilde{Q}]$ | Commutative subalgebra generated by $\tilde{Q}$; it contains every value of a direct elementary function $F(\tilde{Q})$ |
| Oscillatory regime | $B \neq 0$: $\mathbb{C}[\tilde{Q}] \cong \mathbb{C} \times \mathbb{C}$, diagonalizable case |
| Nilpotent regime | $B = 0$, $\vec Q \neq 0$: $\mathbb{C}[\tilde{Q}] \cong \mathbb{C}[\epsilon]/(\epsilon^2)$, $\epsilon = \vec Q$; the element is Jordan when $Q_t\neq0$ and nilpotent when $Q_t=0$ |
| Scalar case | $\vec Q = 0$: $\mathbb{C}[\tilde{Q}] = \mathbb{C} e_t$, the one-dimensional degeneration |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm, written $N$; $N\neq 0$ is the $N$-regular set, the group of units and the domain of the logarithm and of general powers; $N=0$ is the $N$-degenerate set |
| $\tilde Q^*=\overline{\tilde Q^{\natural}}$ | Hermitian conjugation |
| $\langle X\rangle_*=\operatorname{Sc}(XX^*)$ | Hermitian norm, $\sum_\mu\lvert X_\mu\rvert^2$ |
| $\lVert\vec U\rVert_E^2=\sum_k\lvert U_k\rvert^2$ | Euclidean modulus square of the axis, $\ge1$ |

## Further Reading

- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), §*The Eigenprojectors*, for the eigenvalues, the eigenprojections and the pure root $\vec\Xi$; §*The Eigenvalue Formula* of this article, for the parity-matched lattice used there.
- [Relations between the Biquaternion Exponential and the Fourier Kernel](relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the exponential as a biquaternion Fourier kernel, the root supplied by the element, the character exponents and the Hermitian norm of the flow.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of the quaternion exponential and logarithm.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the elementary functions of biquaternions.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the exponential of complexified quaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the classification of the roots of $-1$ that serve as axes of the vector part.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the zero divisors and nilpotents.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, Philadelphia, 2008), for the principal matrix logarithm, its branch cuts, and its Fréchet derivative.
