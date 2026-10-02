
# __Quaternion Harmonic Analysis__

## Introduction

This article introduces harmonic analysis on the quaternion space as the study of the Fourier transform, convolution, and the function spaces on which they act, with the non-commutative structure playing an essential role. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape. Two quaternion Fourier transforms are treated: the transform on $\mathbb{H} \cong \mathbb{R}^4$ with a single unit in the kernel, and the two-dimensional transform of signal and image processing, which assigns one unit to each variable.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra is assumed from the article on quaternion algebra, and the scalar-vector decomposition is used throughout. The article is stated for the quaternion algebra over the real numbers, and the complexification is mentioned only where it clarifies the structure.

Throughout this article, the quaternion algebra is denoted $\mathbb{H}$, and its basis is $e_0 = 1, e_1, e_2, e_3$. The scalar imaginary of the complex numbers is denoted $i$, so that it does not collide with the quaternion units.

**Remark.** In the biquaternion case the Fourier kernel is obstructed on the null cone, where the norm vanishes and the symbol of the transform is not invertible. Here the quaternion norm is positive definite, every non-zero $\xi$ is invertible, and the kernel is everywhere defined; there is no vanishing-norm restriction to record.

## The Additive Group and Its Characters

### Additive Structure

The quaternion space $\mathbb{H}$ is a locally compact abelian group under addition, isomorphic to $\mathbb{R}^4$. Its **characters** are the continuous homomorphisms into the circle group. Since the additive group of $\mathbb{H}$ is just $\mathbb{R}^4$, the characters are the ordinary four-dimensional Fourier characters:

$$
\chi_\xi(\tilde q) = e^{2\pi i \operatorname{Re}(\xi^{\natural} \tilde q)}, \qquad \xi \in \mathbb{H},
$$

where the exponential is the ordinary complex exponential, and the pairing is

$$
\langle \xi, \tilde q \rangle = \operatorname{Re}(\xi^{\natural} \tilde q) = \xi_0 q_0 + \xi_1 q_1 + \xi_2 q_2 + \xi_3 q_3.
$$

Note the sign: the quaternion conjugation $\xi^{\natural} = \xi_0 - \boldsymbol{\xi}$ gives $\xi^{\natural} \tilde q = (\xi_0 - \boldsymbol{\xi})(q_0 + \mathbf{q})$, whose real part is $\xi_0 q_0 + \boldsymbol{\xi} \cdot \mathbf{q}$. So the pairing is the ordinary Euclidean pairing on $\mathbb{R}^4$.

So at the level of the additive group, quaternion harmonic analysis is the same as Fourier analysis on $\mathbb{R}^4$. The non-commutative structure of $\mathbb{H}$ enters only when the algebra structure is used, as in the quaternion Fourier transform and the convolution theorem.

### The Quaternion Characters

The **quaternion characters** are the homomorphisms into the multiplicative group of $\mathbb{H}$:

$$
\chi_\xi(\tilde q) = e^{2\pi \omega \operatorname{Re}(\xi^{\natural} \tilde q)}, \qquad \xi \in \mathbb{H},
$$

where $\omega$ is a fixed unit pure quaternion and the exponential is the quaternion exponential. Because $\omega^2 = -1$, this is

$$
\chi_\xi(\tilde q) = \cos(2\pi \operatorname{Re}(\xi^{\natural} \tilde q)) + \omega \sin(2\pi \operatorname{Re}(\xi^{\natural} \tilde q)).
$$

These characters are **bounded** in the quaternion norm, because they take values on the unit sphere $\mathbb{S}^3$. This is the fundamental difference from the split complex case, where the characters are unbounded, and the similarity with the complex case, where the characters take values in the compact circle.

So the quaternion case is intermediate between the complex case and the split complex case: the characters are bounded, but the algebra is non-commutative, and the transform depends on the choice of the unit pure quaternion $\omega$.

## The Quaternion Fourier Transform

### Definition

The **quaternion Fourier transform** of a function $f : \mathbb{H} \to \mathbb{H}$ is

$$
\hat{f}(\xi) = \int_{\mathbb{H}} f(\tilde q) e^{-2\pi \omega \operatorname{Re}(\xi^{\natural} \tilde q)} \, dq,
$$

where $dq$ is Lebesgue measure on $\mathbb{H} \cong \mathbb{R}^4$, $\omega$ is a fixed unit pure quaternion, and the exponential is the quaternion exponential.

Because the exponential depends on the choice of $\omega$, there are infinitely many quaternion Fourier transforms, one for each unit pure quaternion. The most common choices are:

- **Left-sided transform.** $\hat{f}(\xi) = \int f(\tilde q) e^{-2\pi \omega \operatorname{Re}(\xi^{\natural} \tilde q)} \, dq$, with the exponential on the right.
- **Right-sided transform.** $\hat{f}(\xi) = \int e^{-2\pi \omega \operatorname{Re}(\xi^{\natural} \tilde q)} f(\tilde q) \, dq$, with the exponential on the left.
- **Two-sided transform.** $\hat{f}(\xi) = \int e^{-2\pi \omega_1 \operatorname{Re}(\xi^{\natural} \tilde q)} f(\tilde q) e^{-2\pi \omega_2 \operatorname{Re}(\xi^{\natural} \tilde q)} \, dq$, with two distinct unit pure quaternions $\omega_1$ and $\omega_2$.

The three transforms are related but not equivalent, and the choice depends on the application. The two-sided transform is the most general, and it is the one that diagonalizes the quaternion Cauchy–Riemann operator.

### The Structure of the Transform

Write $f(\tilde q) = f_0(\tilde q) + f_1(\tilde q) e_1 + f_2(\tilde q) e_2 + f_3(\tilde q) e_3$ with $f_\mu : \mathbb{H} \to \mathbb{R}$. Then the quaternion Fourier transform decomposes into four real Fourier transforms, one for each component, with the kernel depending on the choice of $\omega$.

For the simplest case $\omega = e_1$, the kernel is

$$
e^{-2\pi e_1 \operatorname{Re}(\xi^{\natural} \tilde q)} = \cos(2\pi \operatorname{Re}(\xi^{\natural} \tilde q)) - e_1 \sin(2\pi \operatorname{Re}(\xi^{\natural} \tilde q)).
$$

So the transform is

$$
\hat{f}(\xi) = \int f(\tilde q) \cos(2\pi \operatorname{Re}(\xi^{\natural} \tilde q)) \, dq - e_1 \int f(\tilde q) \sin(2\pi \operatorname{Re}(\xi^{\natural} \tilde q)) \, dq.
$$

The first integral is the cosine transform, and the second is the sine transform. Both are real-valued when $f$ is real-valued, and both are ordinary four-dimensional Fourier transforms. So the quaternion Fourier transform is the ordinary Fourier transform on $\mathbb{R}^4$, tensored with the quaternion algebra.

### Basic Properties

**Linearity.** The transform is linear over $\mathbb{R}$, but not over $\mathbb{H}$, because $\mathbb{H}$ is non-commutative.

**Translation.** If $f_a(\tilde q) = f(\tilde q - a)$, then $\hat{f}_a(\xi) = \hat{f}(\xi) e^{-2\pi \omega \operatorname{Re}(\xi^{\natural} a)}$ for the transform defined above, the kernel factor multiplying on the right because the kernel itself stands on the right.

**Modulation.** If $f_\xi(\tilde q) = e^{2\pi \omega \operatorname{Re}(\xi^{\natural} \tilde q)} f(\tilde q)$, then $\hat{f}_\xi(\eta) = \hat{f}(\eta - \xi)$.

**Scaling.** If $f_\lambda(\tilde q) = f(\lambda \tilde q)$ for $\lambda \in \mathbb{H}^\times$, then

$$
\widehat{f_\lambda}(\xi) = \frac{1}{|\lambda|^4} \hat{f}(\bar{\lambda}^{-1}\xi).
$$

**Conjugation equivariance.** If $f_u(\tilde q) = f(u \tilde q u^{-1})$ for a unit quaternion $u$, then $\hat{f}_u(\xi) = \hat{f}(u \xi u^{-1})$. The transform commutes with the conjugation action of the unit group.

**Conjugation.** $\widehat{\bar{f}}(\xi) = \overline{\hat{f}(-\xi)}$.

### The Plancherel Theorem

**Theorem.** The quaternion Fourier transform extends uniquely to a unitary operator

$$
\mathcal{F} : L^2(\mathbb{H}) \to L^2(\mathbb{H}),
$$

with

$$
\|\hat{f}\|_2 = \|f\|_2, \qquad \langle \hat{f}, \hat{g} \rangle = \langle f, g \rangle.
$$

This is the Plancherel theorem for $\mathbb{R}^4$, written in quaternion notation. The non-commutativity does not affect the $L^2$ theory, because the transform is defined by an integral against a bounded kernel.

### The Inversion Theorem

**Theorem.** If $f \in L^1(\mathbb{H})$ and $\hat{f} \in L^1(\mathbb{H})$, then

$$
f(\tilde q) = \int_{\mathbb{H}} \hat{f}(\xi) e^{2\pi \omega \operatorname{Re}(\xi^{\natural} \tilde q)} \, d\xi
$$

for almost every $\tilde q$.

The inversion formula holds because the kernel is bounded and the transform is essentially the ordinary Fourier transform on $\mathbb{R}^4$.

### The Two-Dimensional Transform with One Unit per Variable

The transform above acts on $\mathbb{H}\cong\mathbb{R}^4$ and uses a single unit $\omega$. Signal and image processing uses a different quaternion Fourier transform: the variable is $\mathbb{R}^2$, one unit is assigned to each variable, and the product is written in a fixed order,

$$
\mathcal{F}(f)(\omega_1,\omega_2) = \int_a^b\int_a^b f(x_1,x_2)\, e^{-2\pi e_1 \omega_1 x_1} e^{-2\pi e_2 \omega_2 x_2}\, dx_1 dx_2,
$$

for $f : [a,b]\times[a,b] \to \mathbb{H}$. The order is part of the definition: the two exponential factors rotate in different planes, and $e_1e_2 = e_3 = -e_2e_1$, so they do not commute. The factor $2\pi$ sits in the kernel, as everywhere in this article; the signal-processing literature writes the same kernel without it, which is the substitution $\omega_i \mapsto 2\pi\omega_i$.

The transform above has the kernel on the **right** of $f$; call it $\mathcal{F}_{\mathrm{r}}$. The mirror form $\mathcal{F}_{\mathrm{l}}$ has the kernel on the **left**, and it is a genuinely different transform, not a relabelling of the same one. The literature's names are the reverse of this article's: Ell and Sangwine call the transform whose exponential stands on the left of the signal the *left-sided* one, while the list of the three transforms above names the kernel-right transform left-sided. The words **kernel-right** and **kernel-left** are used below.

**The Closed Form.** With $c_i = 2\pi\omega_ix_i$, the kernel splits into four real-coefficient terms,

$$
e^{-2\pi e_1 \omega_1 x_1}e^{-2\pi e_2 \omega_2 x_2} = \cos c_1\cos c_2 - e_1\sin c_1\cos c_2 - e_2\cos c_1\sin c_2 + e_3\sin c_1\sin c_2,
$$

and the transform is the sum $\mathcal{F}(f) = \Phi_0 + \Phi_1 + \Phi_2 + \Phi_3$ of the four integrals over $[a,b]^2$

$$
\Phi_0 = \int f\cos c_1\cos c_2, \qquad \Phi_1 = -\int f e_1\sin c_1\cos c_2,
$$
$$
\Phi_2 = -\int f e_2\cos c_1\sin c_2, \qquad \Phi_3 = \int f e_3\sin c_1\sin c_2 .
$$

Each term multiplies the whole of the $\mathbb{H}$-valued $f$ on the right by $1$, $e_1$, $e_2$ or $e_3$: the four terms are the four components of one $\mathbb{H}$-valued transform, not four real transforms.

**The sign of the $e_3$ term is the whole difference between the two orders.** The kernel-left form is the same object with the opposite sign on $e_3$,

$$
e^{-2\pi e_2 \omega_2 x_2}e^{-2\pi e_1 \omega_1 x_1} = \cos c_1\cos c_2 - e_1\sin c_1\cos c_2 - e_2\cos c_1\sin c_2 - e_3\sin c_1\sin c_2,
$$

and the two kernels are conjugates,

$$
\overline{e^{-2\pi e_1 \omega_1 x_1}e^{-2\pi e_2 \omega_2 x_2}} = e^{2\pi e_2 \omega_2 x_2}e^{2\pi e_1 \omega_1 x_1},
$$

where the right-hand side is the kernel-left form at $(-\omega_1,-\omega_2)$. Both identities are exact and were verified on independent samples.

**The Ten Reversal Identities.** Reversing one or both frequencies and adding or subtracting the two transforms isolates the individual terms. With the argument $(\omega_1,\omega_2)$ suppressed,

| Combination | Equals |
|---|---|
| $\mathcal{F}(\omega_1,\omega_2)+\mathcal{F}(\omega_1,-\omega_2)$ | $2(\Phi_0+\Phi_1)$ |
| $\mathcal{F}(\omega_1,\omega_2)-\mathcal{F}(\omega_1,-\omega_2)$ | $2(\Phi_2+\Phi_3)$ |
| $\mathcal{F}(\omega_1,\omega_2)+\mathcal{F}(-\omega_1,\omega_2)$ | $2(\Phi_0+\Phi_2)$ |
| $\mathcal{F}(\omega_1,\omega_2)-\mathcal{F}(-\omega_1,\omega_2)$ | $2(\Phi_1+\Phi_3)$ |
| $\mathcal{F}(\omega_1,\omega_2)+\mathcal{F}(-\omega_1,-\omega_2)$ | $2(\Phi_0+\Phi_3)$ |
| $\mathcal{F}(\omega_1,\omega_2)-\mathcal{F}(-\omega_1,-\omega_2)$ | $2(\Phi_1+\Phi_2)$ |
| $\mathcal{F}(\omega_1,-\omega_2)+\mathcal{F}(-\omega_1,-\omega_2)$ | $2(\Phi_0-\Phi_2)$ |
| $\mathcal{F}(\omega_1,-\omega_2)-\mathcal{F}(-\omega_1,-\omega_2)$ | $2(\Phi_1-\Phi_3)$ |
| $\mathcal{F}(-\omega_1,\omega_2)+\mathcal{F}(-\omega_1,-\omega_2)$ | $2(\Phi_0-\Phi_1)$ |
| $\mathcal{F}(-\omega_1,\omega_2)-\mathcal{F}(-\omega_1,-\omega_2)$ | $2(\Phi_2-\Phi_3)$ |

All ten hold to round-off. They are the parity bookkeeping of the kernel: reversal of $\omega_2$ flips the terms built on $\sin c_2$, that is $\Phi_2$ and $\Phi_3$; reversal of $\omega_1$ flips $\Phi_1$ and $\Phi_3$; the two reversals together flip $\Phi_1$ and $\Phi_2$; and adding and subtracting the resulting pairs separates the four terms.

**The Side of the Kernel Is Not Optional.** The reversal relation $\mathcal{F}(f)(-\omega_1,-\omega_2) = \mathcal{F}_{\mathrm{l}}(f)(\omega_1,\omega_2)$ is often printed, and it is derived by replacing $e^{2\pi e_1\omega_1x_1}e^{2\pi e_2\omega_2x_2}$ with $e^{-2\pi e_2\omega_2x_2}e^{-2\pi e_1\omega_1x_1}$. That replacement is invalid: the two are conjugates, as the identity above shows. Numerically, on a $10\times10$ grid at $(\omega_1,\omega_2) = (0.09,0.13)$ the two sides differ by about $10$ for $f \equiv 1$ and by about $12$ for a general quaternionic $f$.

What is true is weaker. For $f$ whose values commute with the kernel — in particular for any scalar-valued $f$ — the two sides are conjugates of one another,

$$
\mathcal{F}_{\mathrm{r}}(f)(-\omega_1,-\omega_2) = \overline{\mathcal{F}_{\mathrm{l}}(f)(\omega_1,\omega_2)},
$$

which was checked exactly for $f \equiv 1$ and for a scalar-valued $f$. For a general $\mathbb{H}$-valued $f$ the two orderings differ by the commutator of the values with the kernel as well: for $f = e_1$ at one point and one frequency the two orderings differ by about $0.8$, so the two sides are not related by conjugation at all. The same slip recurs in the reversal property of the measure transform below, and again in the step that interchanges an integral against a measure with an integral over frequency.

**The Riemann–Lebesgue Lemma with a Rate.** The lemma above is qualitative. In the two-dimensional case the decay rate is explicit, and the kernel standing on the right of $f$ makes the integration by parts unambiguous. If $f$ vanishes at the boundary of the square and $\omega_1 \ne 0$, then

$$
\mathcal{F}(f)(\omega_1,\omega_2) = -\frac{1}{2\pi e_1\omega_1}\int_a^b\int_a^b \partial_{x_1}f(x_1,x_2)\, e^{-2\pi e_1\omega_1x_1}e^{-2\pi e_2\omega_2x_2}\, dx_1 dx_2,
$$

because the boundary terms vanish, so

$$
\lvert \mathcal{F}(f)(\omega_1,\omega_2)\rvert \le \lVert f\rVert_{L^1}, \qquad \lvert \mathcal{F}(f)(\omega_1,\omega_2)\rvert \le \frac{\lVert \partial_{x_1}f\rVert_{L^1}}{2\pi\lvert\omega_1\rvert},
$$

and the same with $x_2$ and $\omega_2$. Hence $\mathcal{F}(f)$ is bounded and uniformly continuous, and it tends to zero as either frequency tends to infinity, uniformly in the other frequency. The first bound holds for every frequency; the second only for $\omega_i \ne 0$. Both were checked for $f = (1-x_1^2)^2(1-x_2^2)^2$ on $[-1,1]^2$, where $\lVert f\rVert_{L^1} = (16/15)^2 = 1.1378$ and $\lVert \partial_{x_1}f\rVert_{L^1} = 32/15 = 2.1333$, at six frequencies including the cases $\omega_1 = 0$ and $\omega_2 = 0$.

### The Transform of a Measure

**Definition.** Let $\mu$ be a finite positive Borel measure on $\mathbb{R}^2$. Its two transforms are

$$
\mathcal{F}_{\mathrm{r}}(\mu)(\omega_1,\omega_2) = \int_{\mathbb{R}^2} e^{-2\pi e_1\omega_1x_1}e^{-2\pi e_2\omega_2x_2}\, d\mu(x_1,x_2),
$$
$$
\mathcal{F}_{\mathrm{l}}(\mu)(\omega_1,\omega_2) = \int_{\mathbb{R}^2} e^{-2\pi e_2\omega_2x_2}e^{-2\pi e_1\omega_1x_1}\, d\mu(x_1,x_2).
$$

For a measure with density $f$ these are the transforms of the previous subsection. Written against $d\mu$ they are defined for measures with no density, which is what the Fourier analysis of probability measures needs. The kernel has modulus one, so both integrals converge absolutely.

**Normalisation and boundedness.** $\mathcal{F}_{\mathrm{r}}(\mu)(0,0) = \mathcal{F}_{\mathrm{l}}(\mu)(0,0) = \mu(\mathbb{R}^2)$, so both are $1$ for a probability measure; and $\lvert \mathcal{F}_{\mathrm{r}}(\mu)(\omega_1,\omega_2)\rvert \le \mu(\mathbb{R}^2)$, likewise on the left.

**Reversal.** $\mathcal{F}_{\mathrm{r}}(\mu)(-\omega_1,-\omega_2) = \overline{\mathcal{F}_{\mathrm{l}}(\mu)(\omega_1,\omega_2)}$, and likewise with the two orders exchanged: reversal of the frequency conjugates and exchanges the orders. The relation is often printed without the conjugation, which is the same slip as above; with the conjugation it is exact on a seven-point probability measure.

**Cosine and $e_3$ parts.** $\mathcal{F}_{\mathrm{r}}(\mu)(\omega_1,\omega_2)+\mathcal{F}_{\mathrm{r}}(\mu)(-\omega_1,-\omega_2)$ equals $2\int(\cos c_1\cos c_2 + e_3\sin c_1\sin c_2)\,d\mu$, and $\mathcal{F}_{\mathrm{r}}(\mu)(\omega_1,\omega_2)+\mathcal{F}_{\mathrm{l}}(\mu)(-\omega_1,-\omega_2)$ equals $2\int\cos c_1\cos c_2\,d\mu$. Both are exact, and they are the measure form of the first and fifth reversal identities above.

**Positive definiteness.** A bounded continuous $\mathbb{H}$-valued function $g$ on $\mathbb{R}^2$ is **positive definite** when

$$
\sum_{k<l} z_k \bar z_l\, g(\lambda_k-\lambda_l) + \sum_{k>l} g(\lambda_k-\lambda_l)\, z_k \bar z_l + \sum_k \lvert z_k\rvert^2 g(0,0) \ge 0
$$

for every finite set $\lambda_1,\dots,\lambda_N \in \mathbb{R}^2$ and every $z_1,\dots,z_N \in \mathbb{H}$. Three features separate this from the commutative statement: the coefficients are quaternions rather than complex numbers; the two sums are kept apart because $z_k\bar z_l g$ and $g\,z_l\bar z_k$ are different products, so the quadratic form is not the square of a single sum; and the diagonal term carries $g(0,0)$, which for the transform of a measure is $\mu(\mathbb{R}^2)$. Written with $\mu(\mathbb{R}^2)$ in the diagonal from the outset, the property is tied to the measure it is meant to produce; with $g(0,0)$ it is a property of $g$ alone, which is what an existence theorem needs.

**Theorem.** $\mathcal{F}_{\mathrm{r}}(\mu)$ and $\mathcal{F}_{\mathrm{l}}(\mu)$ are positive definite and bounded.

**Why two points are enough to see it, and why the printed proof for more points does not go through.** For $N=2$ the sum is $X+\overline{X}+\lvert z_1\rvert^2g(0,0)+\lvert z_2\rvert^2g(0,0)$ with $X = z_1\bar z_2\,g(\lambda_1-\lambda_2)$, and $\lvert g\rvert \le g(0,0)$, so the sum is at least $(\lvert z_1\rvert-\lvert z_2\rvert)^2 g(0,0) \ge 0$. For general $N$ the source bounds the sum below by $\sum_k\lvert z_k\rvert^2 - 2\sum_{k<l}\lvert z_k\rvert\lvert z_l\rvert$ and then asserts an induction; that lower bound is negative, being $3-6 = -3$ for $N = 3$ with all $\lvert z_k\rvert = 1$. Random draws at $N = 3$ gave a positive minimum in every trial, so the statement is consistent with the numerical evidence, but the induction as printed is not established.

**What a Bochner–Minlos theorem is, and what is proved here.** The classical theorem says that a functional on a nuclear space that is continuous, normalised and positive definite **is** the Fourier transform of a unique probability measure; the substance is the existence direction, in which positivity of the quadratic form produces the measure. A quaternion form of the theorem is stated in the literature for functionals on the dual of the sequence space $s$ of quaternion sequences with $\lVert p\rVert_m^2 = \sum_n (1+n^2)^m\lvert p_n\rvert^2$ and $s = \bigcap_m s_m$, and what is proved there is the converse direction: a probability measure on the dual is given, and its functional is shown to be normalised, continuous in the Fréchet topology and positive definite. With the measure written into the definition of positive definiteness, the theorem cannot be run in the existence direction, and that direction, which needs the nuclear structure of the test space, is not proved. Nothing in this article depends on the claim.

## The Convolution Theorem

### Definition

The **convolution** of $f, g : \mathbb{H} \to \mathbb{H}$ is

$$
(f * g)(\tilde q) = \int_{\mathbb{H}} f(\tilde q - r) g(r) \, dr,
$$

whenever the integral converges. This is the convolution on the additive group $\mathbb{H} \cong \mathbb{R}^4$.

### Basic Properties

**Non-commutativity.** The convolution is not commutative in general, because $\mathbb{H}$ is not commutative: $f * g \neq g * f$ in general. It is commutative only when one of the functions takes values in the center of $\mathbb{H}$, which is $\mathbb{R}$.

**Associativity.** $(f * g) * h = f * (g * h)$.

**Young's inequality.** If $1/p + 1/\tilde q = 1/r + 1$ with $1 \leq p, \tilde q, r \leq \infty$, then

$$
\|f * g\|_r \leq \|f\|_p \|g\|_q,
$$

where the norms are the ordinary $L^p$ norms on $\mathbb{R}^4$.

**Convolution theorem.** For functions for which the quaternion Fourier transform is defined,

$$
\widehat{f * g}(\xi) = \hat{f}(\xi) \hat{g}(\xi),
$$

with the same ordering on both sides for the left-sided transform. For the two-sided transform, the statement is more complicated, because the two kernels do not commute.

**Proof.** Write the definition, apply Fubini, and change variables.

### The Structure of the Convolution Theorem

The convolution theorem for the quaternion Fourier transform is the same as for the complex Fourier transform on $\mathbb{R}^4$, except that the multiplication on the right is quaternion multiplication, which is non-commutative. So the convolution theorem says that the transform turns convolution into quaternion multiplication, and the non-commutativity of the convolution is a reflection of the non-commutativity of $\mathbb{H}$.

### Approximate Identities

A sequence $(\phi_n)$ in $L^1(\mathbb{H})$ is an **approximate identity** if

$$
\int_{\mathbb{H}} \phi_n = 1, \qquad \sup_n \|\phi_n\|_1 < \infty, \qquad \int_{|\tilde q| > \delta} |\phi_n(\tilde q)| \, dq \to 0
$$

for every $\delta > 0$.

**Theorem.** If $(\phi_n)$ is an approximate identity and $f \in L^p(\mathbb{H})$ for $1 \leq p < \infty$, then

$$
\|f * \phi_n - f\|_p \to 0.
$$

This is the same as in the real case, because the additive group of $\mathbb{H}$ is just $\mathbb{R}^4$.

## Distributions

### Definition

A **tempered distribution** on $\mathbb{H}$ is a continuous linear functional on the Schwartz space $\mathcal{S}(\mathbb{H})$. The space of tempered distributions is denoted $\mathcal{S}'(\mathbb{H})$. It includes all functions in $L^p(\mathbb{H})$ for $1 \leq p \leq \infty$, all finite measures, and all derivatives of such objects.

### Operations on Distributions

**Differentiation.** For $T \in \mathcal{S}'(\mathbb{H})$ and $\phi \in \mathcal{S}(\mathbb{H})$,

$$
\langle \partial_\mu T, \phi \rangle = -\langle T, \partial_\mu \phi \rangle, \qquad \mu = 0, 1, 2, 3.
$$

**Multiplication by a function.** For $f \in C^\infty(\mathbb{H})$ with polynomial growth and $T \in \mathcal{S}'(\mathbb{H})$,

$$
\langle f T, \phi \rangle = \langle T, f \phi \rangle.
$$

**Quaternion Fourier transform.** For $T \in \mathcal{S}'(\mathbb{H})$ and $\phi \in \mathcal{S}(\mathbb{H})$,

$$
\langle \hat{T}, \phi \rangle = \langle T, \hat{\phi} \rangle.
$$

The quaternion Fourier transform is a bijection $\mathcal{S}'(\mathbb{H}) \to \mathcal{S}'(\mathbb{H})$.

### The Delta Distribution

The **delta distribution** $\delta$ is the tempered distribution

$$
\langle \delta, \phi \rangle = \phi(0).
$$

Its quaternion Fourier transform is the constant function $1$, and the quaternion Fourier transform of $1$ is $\delta$. The delta is the identity for convolution: $\delta * T = T$ for every tempered distribution $T$.

### The Cauchy Kernel

The **Cauchy kernel** is the distribution

$$
E(\tilde q) = \frac{\tilde{q}^{\natural}}{|\tilde q|^4},
$$

which satisfies

$$
D E = 2\pi^2 \delta_0
$$

in the sense of distributions, where $D$ is the quaternion Cauchy–Riemann operator. It is the fundamental solution of the Cauchy–Riemann operator, and it is the quaternion analogue of the kernel $1/z$ in complex analysis.

## The Quaternion Hilbert Transform

### Definition

The **quaternion Hilbert transform** of $f : \mathbb{H} \to \mathbb{H}$ is defined by the principal value integral

$$
Hf(\tilde q) = \frac{1}{\pi^2} \, \text{p.v.} \int_{\mathbb{H}} \frac{(r - \tilde q)^{-1}}{|r - \tilde q|^2} f(r) \, dr,
$$

where the integral is over the quaternion space and the principal value is taken with respect to the singularity at $r = \tilde q$.

### Basic Properties

**Boundedness.** $H$ is bounded on $L^p(\mathbb{H})$ for $1 < p < \infty$, with

$$
\|Hf\|_p \leq C_p \|f\|_p.
$$

**Fourier multiplier.** In terms of the quaternion Fourier transform,

$$
\widehat{Hf}(\xi) = -\omega \operatorname{sgn}(\xi) \hat{f}(\xi),
$$

where $\operatorname{sgn}$ is the sign function on the real part.

### The Relation to the Cauchy–Riemann Operator

The quaternion Hilbert transform is the boundary value of the Cauchy integral for monogenic functions. It is the quaternion analogue of the Hilbert transform in complex analysis, and it is used in the theory of boundary value problems for the Cauchy–Riemann operator.

## Maximal Functions

### The Quaternion Maximal Function

The **quaternion Hardy–Littlewood maximal function** of $f \in L^1_{\mathrm{loc}}(\mathbb{H})$ is

$$
Mf(\tilde q) = \sup_{r > 0} \frac{1}{|B(\tilde q, r)|} \int_{B(\tilde q, r)} |f(r)| \, dr,
$$

where $B(\tilde q, r)$ is the Euclidean ball of radius $r$ centered at $\tilde q$, and $|B(\tilde q, r)|$ is its volume.

### The Maximal Inequality

**Theorem (Hardy–Littlewood, quaternion version).** There exists a constant $C > 0$ such that for every $f \in L^1(\mathbb{H})$ and every $\lambda > 0$,

$$
|\{\tilde q : Mf(\tilde q) > \lambda\}| \leq \frac{C}{\lambda} \|f\|_1.
$$

This is a **weak $(1,1)$** estimate. It implies that $M$ is bounded on $L^p(\mathbb{H})$ for $1 < p \leq \infty$.

**Theorem.** For $1 < p \leq \infty$, there exists $C_p > 0$ such that

$$
\|Mf\|_p \leq C_p \|f\|_p.
$$

**Proof.** The case $p = \infty$ is trivial. The case $1 < p < \infty$ follows from the weak $(1,1)$ estimate and the trivial $L^\infty$ estimate by interpolation.

### The Structure of the Maximal Function

Because the additive group of $\mathbb{H}$ is just $\mathbb{R}^4$, the maximal function theory is identical to the real theory on $\mathbb{R}^4$. The non-commutativity of $\mathbb{H}$ does not affect the maximal function, because the maximal function is defined in terms of the Euclidean norm, which does not see the algebra structure.

## The Calderón–Zygmund Theory

### Singular Integrals

A **quaternion Calderón–Zygmund operator** is a bounded operator $T : L^2(\mathbb{H}) \to L^2(\mathbb{H})$ with a kernel $K : \mathbb{H} \times \mathbb{H} \to \mathbb{H}$ such that

$$
Tf(\tilde q) = \int_{\mathbb{H}} K(\tilde q, r) f(r) \, dr
$$

for $\tilde q \notin \operatorname{supp} f$, and $K$ satisfies the size and smoothness estimates

$$
|K(\tilde q, r)| \leq \frac{C}{|\tilde q - r|^4},
$$

$$
|K(\tilde q, r) - K(\tilde q', r)| \leq C \frac{|\tilde q - \tilde q'|^\delta}{|\tilde q - r|^{4+\delta}}, \qquad |\tilde q - \tilde q'| < \frac{1}{2} |\tilde q - r|,
$$

and the analogous estimate in the second variable, for some $\delta > 0$. The power $4$ is the dimension of $\mathbb{H}$ as a real vector space.

**Theorem (Calderón–Zygmund, quaternion version).** Every quaternion Calderón–Zygmund operator is bounded on $L^p(\mathbb{H})$ for $1 < p < \infty$, and satisfies a weak $(1,1)$ estimate.

**Examples.** The quaternion Hilbert transform, the quaternion Riesz transforms, and the Beurling–Ahlfors transform are quaternion Calderón–Zygmund operators.

### The Structure of the Theory

Because the additive group of $\mathbb{H}$ is just $\mathbb{R}^4$, the Calderón–Zygmund theory is identical to the real theory on $\mathbb{R}^4$, with the dimension adjusted from $n$ to $4$. The non-commutativity of $\mathbb{H}$ does not affect the kernel estimates, because they are in terms of the Euclidean norm, which does not see the algebra structure. The non-commutativity affects only the multiplication of the kernel with the function, and this is a minor modification.

## The Mellin Transform

### Definition

The **quaternion Mellin transform** of a function $f : (0, \infty) \to \mathbb{H}$ is

$$
\mathcal{M} f(s) = \int_0^\infty t^{s-1} f(t) \, dt,
$$

where the power is the quaternion power. Because the variable $t$ is real and the quaternion $s$ appears only in the exponent, the integral converges for $s_0$ in the appropriate range.

### Relation to the Quaternion Fourier Transform

Under the change of variables $t = e^x$, the Mellin transform becomes the quaternion Fourier transform on the real line:

$$
\mathcal{M} f(\sigma + \omega \tau) = \int_{-\infty}^\infty e^{(\sigma + \omega \tau) x} f(e^x) \, dx = \hat{g}(\tau),
$$

where $g(x) = e^{\sigma x} f(e^x)$ and $\omega$ is a unit pure quaternion. So the Mellin transform is the quaternion Fourier transform in logarithmic coordinates.

### The Mellin Convolution

The **quaternion Mellin convolution** is

$$
(f \star g)(x) = \int_0^\infty f(x/y) g(y) \frac{dy}{y}.
$$

It satisfies

$$
\mathcal{M}(f \star g)(s) = \mathcal{M} f(s) \, \mathcal{M} g(s),
$$

which is the multiplicative analogue of the convolution theorem.

## The Radon Transform

### Definition

The **quaternion Radon transform** of a function $f : \mathbb{H} \to \mathbb{H}$ is

$$
Rf(\theta, t) = \int_{L(\theta, t)} f(\tilde q) \, ds,
$$

where $L(\theta, t)$ is the hyperplane with normal direction $\theta \in \mathbb{S}^3$ and signed distance $t$ from the origin, and $ds$ is the Euclidean surface measure.

### The Fourier Slice Theorem

**Theorem (Fourier Slice, quaternion version).** The one-dimensional quaternion Fourier transform of $Rf(\theta, \cdot)$ is the restriction of the four-dimensional quaternion Fourier transform of $f$ to the line through the origin in direction $\theta$:

$$
\widehat{Rf(\theta, \cdot)}(\sigma) = \hat{f}(\sigma \theta).
$$

**Proof.** Write the definition of the Radon transform, take the quaternion Fourier transform in $t$, and change variables.

The Fourier slice theorem is the mathematical basis of quaternion tomography, the analogue of computed tomography for the quaternion space.

### The Inversion Formula

**Theorem.** For suitable $f$,

$$
f(\tilde q) = \frac{1}{2} \int_{\mathbb{S}^3} \int_{-\infty}^\infty \widehat{Rf(\theta, \cdot)}(\sigma) |\sigma|^3 e^{2\pi \omega \operatorname{Re}(\bar{\theta} \tilde q)} \, d\sigma \, d\theta,
$$

where $d\theta$ is the surface measure on the unit sphere $\mathbb{S}^3$. The factor $|\sigma|^3$ is the ramp filter in dimension four, and it is the source of the high-frequency amplification in quaternion tomography.

## The Wavelet Transform

### Definition

The **quaternion continuous wavelet transform** of $f \in L^2(\mathbb{H})$ with respect to a wavelet $\psi \in L^2(\mathbb{H})$ is

$$
W_\psi f(a, b) = \frac{1}{|a|^2} \int_{\mathbb{H}} f(\tilde q) (\psi\left( \frac{\tilde q - b}{a} \right))^{\natural} \, dq, \qquad a \in \mathbb{H}^\times, \; b \in \mathbb{H}.
$$

The parameter $a$ is the **scale**, and $b$ is the **translation**. The wavelet $\psi$ is assumed to satisfy the **admissibility condition**

$$
C_\psi = \int_{\mathbb{H}} \frac{|\hat{\psi}(\xi)|^2}{|\xi|^4} \, d\xi < \infty,
$$

where $\hat{\psi}$ is the quaternion Fourier transform.

### The Inversion Formula

**Theorem.** If $\psi$ is admissible and $f \in L^2(\mathbb{H})$, then

$$
f(\tilde q) = \frac{1}{C_\psi} \int_{\mathbb{H}^\times} \int_{\mathbb{H}} W_\psi f(a, b) \frac{1}{|a|^2} \psi\left( \frac{\tilde q - b}{a} \right) \frac{da \, db}{|a|^4}.
$$

The inversion formula reconstructs $f$ from its wavelet transform.

### The Quaternion Wavelet Transform

The quaternion wavelet transform is used in quaternion signal processing, where it provides both magnitude and phase information, and in the analysis of quaternion-valued images, where the three imaginary components encode the color channels.

## The Structure Principle

The pattern in all the definitions above is the same: whenever the analysis depends only on the additive group structure and the Euclidean norm, the quaternion case is identical to the real case on $\mathbb{R}^4$. Whenever the analysis involves the algebra structure, the non-commutativity of $\mathbb{H}$ makes the theory richer but more complicated.

**Theorem (Structure Principle for quaternion harmonic analysis).** Let $\mathcal{T}$ be a transform or operator defined on functions on $\mathbb{R}^n$ that depends only on the additive group structure and the Euclidean norm. Then the quaternion analogue of $\mathcal{T}$ is identical to $\mathcal{T}$ on $\mathbb{R}^4$, stated in quaternion notation. If $\mathcal{T}$ depends on the algebra structure, then the quaternion analogue depends on the choice of the unit pure quaternion $\omega$, and the non-commutativity of $\mathbb{H}$ prevents the simple identities that hold in the commutative case.

**Consequences.**

- The maximal function, the Calderón–Zygmund theory, and the wavelet transform are identical to the real theory on $\mathbb{R}^4$, because they depend only on the additive group and the Euclidean norm.
- The Fourier transform, the convolution theorem, and the Radon transform depend on the choice of $\omega$, and the non-commutativity of $\mathbb{H}$ makes the identities more complicated than in the complex case.
- The quaternion Fourier transform is the ordinary Fourier transform on $\mathbb{R}^4$ tensored with $\mathbb{H}$, and the non-commutativity enters only in the ordering of the factors.

This is the fundamental structural fact about quaternion harmonic analysis: the additive group is $\mathbb{R}^4$, so the analysis is the ordinary analysis on $\mathbb{R}^4$, and the quaternion structure enters only through the algebra of the coefficients.

## Summary

Harmonic analysis on the quaternion space is the study of the Fourier transform, of convolution, and of the function spaces on which the two act, with the non-commutative structure in an essential role. The space is first a locally compact abelian group under addition, isomorphic to $\mathbb{R}^4$, and its characters are the exponentials from which the transform is built.

The quaternion Fourier transform is defined with a kernel built from the quaternion exponential, and it is developed together with convolution, the Schwartz space and its tempered distributions, the Hilbert transform, the Hardy–Littlewood maximal function, and the Calderón–Zygmund theory of singular integrals. The transform is then extended to the Mellin transform on the multiplicative half-line, the Radon transform along hyperplanes, and the continuous wavelet transform.

Inside the transform section a second quaternion Fourier transform is recorded: the two-dimensional transform of signal and image processing, which assigns one unit to each variable and whose product kernel must be written in a fixed order. Its closed form, its ten reversal identities and its explicit Riemann–Lebesgue decay rate are given, together with the transform of a finite positive measure and the positive definiteness that belongs to it. That positive definiteness is the half of a Bochner–Minlos statement that a measure can supply; the existence direction, which would produce the measure from positivity, is not available here.

The section on the structure principle states what organises the subject: whenever the analysis depends only on the additive group structure and the Euclidean norm, the quaternion case agrees with the real case on $\mathbb{R}^4$, and the non-commutativity enters only through the kernel of the transform.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | General quaternion |
| $\omega$ | Unit pure quaternion |
| $\chi_\xi(\tilde q) = e^{2\pi \omega \operatorname{Re}(\xi^{\natural} \tilde q)}$ | Quaternion character |
| $\hat{f}$ | Quaternion Fourier transform |
| $\mathcal{F}(f)(\omega_1,\omega_2)$ | Two-dimensional quaternion Fourier transform, one unit per variable |
| $\Phi_0,\dots,\Phi_3$ | The four terms of the two-dimensional kernel |
| $\mathcal{F}_{\mathrm{r}}(\mu), \mathcal{F}_{\mathrm{l}}(\mu)$ | Transform of a finite positive measure $\mu$, kernel right and kernel left |
| $f * g$ | Convolution |
| $\delta$ | delta distribution |
| $E(\tilde q) = \tilde{q}^{\natural}/\lvert \tilde q\rvert^4$ | Cauchy kernel |
| $D$ | Quaternion Cauchy–Riemann operator |
| $Hf$ | Quaternion Hilbert transform |
| $Mf$ | Quaternion maximal function |
| $\mathcal{M} f$ | Quaternion Mellin transform |
| $Rf$ | Quaternion Radon transform |
| $W_\psi f$ | Quaternion wavelet transform |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford theory.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the role of the spinor-valued first-order operator in geometry.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton, 1971), for the classical treatment of the Fourier transform on $\mathbb{R}^n$.
- Todd A. Ell and Stephen J. Sangwine, *Quaternion Fourier Transforms for Signal and Image Processing* (Wiley, 2014), for the engineering applications.
- Todd A. Ell, "Quaternion-Fourier transforms for analysis of two-dimensional linear time-invariant partial differential systems", in *Proceedings of the 32nd IEEE Conference on Decision and Control* (1993), 1830–1841, for the two-dimensional transform with one unit per variable.
- S. Georgiev, J. Morais, K. I. Kou, and W. Sprößig, "Bochner–Minlos theorem and quaternion Fourier transform", in *Quaternion and Clifford–Fourier Transforms and Wavelets*, Trends in Mathematics (Springer, 2013), 105–120, for the closed form and the reversal identities of that transform, for its decay estimate, and for the measure-theoretic direction recorded above.
- Salomon Bochner, "Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse", *Mathematische Annalen* **108** (1933), 378–410, and R. A. Minlos, *Trudy Moskovskogo Matematicheskogo Obshchestva* **8** (1959), 497–518, for the classical Bochner–Minlos theorem.

