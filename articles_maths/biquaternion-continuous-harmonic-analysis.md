# __Biquaternion Continuous Harmonic Analysis__

## Introduction

This article treats the Fourier transform of a biquaternion-valued function of real variables. It owns the kernel: the definition, the closed form, the Peirce form, the classification of the roots it is indexed by, and the analytic theorems that the continuous index set allows and a finite sum does not — an integral with a convergence hypothesis, inversion, Plancherel, and the reading of the transform as a function of the differential operators.

**The root of the kernel is a root of $1$.** The kernel is built from an element whose square is the unit, and from the complex scalar $i$ beside it,

$$
W(t,\omega)=\exp(-2\pi i\,\tilde{Ζ}\,\omega t),\qquad \tilde{Ζ}^2=e_t .
$$

The element the exponent needs is $i\tilde{Ζ}$, whose square is $-e_t$; the sign is carried by the scalar, and no element whose square is $-1$ is ever named. Three consequences run through the article.

**The root is a pair of idempotents.** The halving map sends a root to an idempotent and back, and the pair attached to a root is $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$. The kernel is then a pair of conjugate unit complex numbers, one on each Peirce ideal,

$$
W(t,\omega)=e^{-2\pi i\omega t}\,\tilde\Pi_+ + e^{+2\pi i\omega t}\,\tilde\Pi_- ,
$$

and the transform is a pair of ordinary complex transforms on those ideals. The factorization into complex transforms is not a change of basis imposed from outside: it is the transform read in the coordinates the root supplies.

**The isometry has a criterion that names the root.** The Peirce split is orthogonal for the Euclidean form exactly when the root is Hermitian, and Plancherel holds for exactly those roots: the criterion is the star-invariance of one element.

Three objects are treated: the one-unit kernel $W(t,\omega)$ in $n$ variables; the two-unit kernel, which assigns one root to each of two variables and is not reducible to the one-unit case; and the transform of a finite measure, whose failure of positivity is the same indefiniteness that governs the vanishing-norm issue. The objects are an algebra, a kernel, and the integrals defined from them.

Throughout, a biquaternion is written

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = Q_t e_t + \vec Q, \qquad \vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z.
$$

The scalar imaginary is $i$, which commutes with the quaternion units. The quaternion conjugate is $\tilde{Q}^{\natural} = Q_t e_t - \vec Q$, the coefficient conjugate is $\bar{\cdot}$, and the Hermitian conjugation is $*=\bar{\cdot}\circ{}^{\natural}$. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural}$, a complex scalar.

**Notation.** The root of $1$ is written $\tilde{Ζ}$, and a pure root $\vec{Ζ}$, the arrow taking priority over the tilde; every root other than the central pair $\pm e_t$ is pure, so the arrow is written wherever purity is used. The letters $e_t$ and $i$ are the unit and the scalar imaginary, so the root collides with neither.

## The Fourier Kernel

### The Root of One

**Definition (the root of one).** An element $\tilde{Ζ}\in\mathbb{B}$ is a **root of $1$** when $\tilde{Ζ}^2=e_t$, the square being taken in the algebra product.

**Proposition (the roots of one).** A root of $1$ has a vanishing vector part, and is then $\pm e_t$, or a vanishing scalar part. In the second case it is a **pure root**, written $\vec{Ζ}$, and it satisfies $(\vec{Ζ},\vec{Ζ})=-1$. Writing $\vec{Ζ}=\vec p+i\vec p'$ over two real vectors, the pure roots are the pairs

$$
\vec p\cdot\vec p'=0,\qquad \lVert\vec p'\rVert^{2}-\lVert\vec p\rVert^{2}=1 ,
$$

a family of real dimension four, which contains the purely imaginary unit vectors $i\vec u$ over the real unit vectors $\vec u$.

*Proof.* The square is $\tilde{Ζ}^{2}=\bigl(Q_t^{2}-(\vec{Ζ},\vec{Ζ})\bigr)e_t+2Q_t\vec{Ζ}$. A square equal to $e_t$ has a vanishing vector part, so $2Q_t\vec{Ζ}=0$: either $Q_t=0$ or $\vec{Ζ}=0$. If $\vec{Ζ}=0$ then $Q_t^{2}=1$ and the root is central. If $Q_t=0$ then $-(\vec{Ζ},\vec{Ζ})=1$, which is the pure case, and splitting $\vec{Ζ}$ into its real and imaginary parts gives $\lVert\vec p\rVert^{2}-\lVert\vec p'\rVert^{2}=-1$ and $\vec p\cdot\vec p'=0$.

**The dichotomy is the point of the parameter.** The two families are disjoint and exhaustive, so every statement about the kernel has two cases and no third.

**Definition (the Hermitian root).** A root is **Hermitian** when $\tilde{Ζ}^{*}=\tilde{Ζ}$.

**Proposition (the Hermitian roots).** The Hermitian roots of $1$ are the central pair $\pm e_t$ and the purely imaginary unit vectors $\pm i\vec u$ over the real unit vectors $\vec u$.

*Proof.* A pure root has $\tilde{Ζ}^{*}=\bar{\tilde{Ζ}}^{\natural}=-\bar{\tilde{Ζ}}=-\vec p+i\vec p'$, so the Hermitian condition is $\vec p=0$, and the root condition $\lVert\vec p'\rVert^{2}-\lVert\vec p\rVert^{2}=1$ gives $\lVert\vec p'\rVert=1$. The central roots are fixed by the star.

For a Hermitian root the pair is a pair of Hermitian idempotents, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$, that is, a pair of pure states. §*The Plancherel Theorem* shows that this is exactly the condition for the transform to be an isometry, and §*The Transform of a Measure* for the transform of a positive measure to be positive definite.

**The sign of the root.** Replacing $\tilde{Ζ}$ by $-\tilde{Ζ}$ exchanges $\tilde\Pi_+$ and $\tilde\Pi_-$ and conjugates the kernel, $W(t,\omega;-\tilde{Ζ})=\overline{W(t,\omega;\tilde{Ζ})}$ for a pure root. The two transforms carry the same information.

### Definition

Fix a root of $1$ once and for all. The **biquaternion Fourier kernel** is the function

$$
W(t, \omega) = \exp\left(-2\pi i\,\tilde{Ζ}\,\omega t\right), \qquad t, \omega \in \mathbb{R}.
$$

Because $\tilde{Ζ}^2 = e_t$, the kernel takes the closed form

$$
W(t, \omega) = \cos(2\pi \omega t) \, e_t - i\sin(2\pi \omega t) \, \tilde{Ζ},
$$

the cosine and sine being the ordinary real ones.

**The inverse.** The kernel is invertible at every point, with

$$
W(t, \omega)^{-1} = \cos(2\pi \omega t) \, e_t + i\sin(2\pi \omega t) \, \tilde{Ζ} = W(t, -\omega),
$$

which follows from $\tilde{Ζ}^2 = e_t$ alone: the two factors multiply to $(\cos^{2}+\sin^{2})e_t$. This is a closed form that holds for **every** root, and it is the form the inverse transform uses. It is the identity in the commutative algebra $\mathbb{C}[\tilde{Ζ}]$ and uses nothing else.

**The conjugate and the norm, for a pure root.** When the root is pure, the quaternion conjugation of the kernel is this inverse and the natural norm is the unit:

$$
W(t, \omega)^{\natural} = W(t, \omega)^{-1}, \qquad \langle W(t, \omega)\rangle_{\natural} = e_t ,
$$

because $\vec{Ζ}^{\natural}=-\vec{Ζ}$ for a pure element. **The central roots $\tilde{Ζ}=\pm e_t$ are the exception**: the kernel is the complex scalar $e^{\mp 2\pi i\omega t}e_t$, which the quaternion conjugation fixes rather than inverts, and the inverse is the coefficient conjugate $\overline{W}$. The natural norm there is $W^{2}=e^{\mp4\pi i\omega t}e_t$, a unit and not $e_t$. The distinction affects only that pair, and the statements below that use the conjugation of the kernel are stated for a pure root.

**The Peirce form.** Substituting $\tilde{Ζ}=\tilde\Pi_+-\tilde\Pi_-$, and using $\tilde{Ζ}\tilde\Pi_\pm=\pm\tilde\Pi_\pm$,

$$
W(t, \omega) = e^{-2\pi i \omega t}\,\tilde\Pi_+ + e^{+2\pi i \omega t}\,\tilde\Pi_- .
$$

The kernel is a pair of conjugate unit complex numbers, one on each Peirce ideal, and it is never a zero divisor.

### The Kernel as the Exponential of an Element

The kernel is an exponential, and a spectrally regular element supplies its own root and rate.

**Proposition (the element's kernel).** Let $\tilde Q=Q_te_t+\vec Q$ with $B^{2}=(\vec Q,\vec Q)\neq0$, let $B$ be a square root of $B^{2}$, and put $\tilde{Ζ}=-i\vec Q/B$. Then $\tilde{Ζ}$ is a pure root of $1$ and, for every complex $\theta$,

$$
e^{\theta\tilde Q}
=e^{\theta Q_t}\,W\!\left(\theta,-\frac{B}{2\pi}\right)
=e^{\theta Q_t}\,W\!\left(-\theta,\frac{B}{2\pi}\right).
$$

*Proof.* The vector part squares to $\vec Q^{2}=-(\vec Q,\vec Q)e_t=-B^{2}e_t$, so $\tilde{Ζ}^{2}=(-i)^{2}\vec Q^{2}/B^{2}=e_t$, and $\tilde{Ζ}$ is pure because $\vec Q$ is. By the closed form of the kernel, $W(\theta,-B/2\pi)=\exp(i\tilde{Ζ}B\theta)=\exp(\vec Q\theta)$, which is the vector part of the exponent; multiplying by $e^{\theta Q_t}$ and comparing with the closed form of the exponential of a biquaternion gives the identity.

**The root the element supplies is pure, and not always Hermitian.** The root $\tilde{Ζ}=-i\vec Q/B$ has no scalar part, so the central roots $\pm e_t$ are never the root of a regular element. It is Hermitian exactly when $\vec Q/B$ is real, that is, exactly when the element is normal, and this is the junction with §*The Plancherel Theorem*: the isometry holds exactly for the elements whose flow is normal. The dictionary is set out in *Relations between the Biquaternion Exponential and the Fourier Kernel*.

**The cone.** At $B=0$ there is no root and no frequency. The flow is the truncated $e^{\theta Q_t}(e_t+\theta\vec N)$ with $\vec N=\vec Q$ and $\vec N^{2}=0$, and the root-free closed form extends to $B=0$. The kernel does not: the root is the direction $-i\vec Q/B$, undefined on the cone. For $\vec Q=\epsilon\vec e_x$ and $\vec Q=\epsilon\vec e_y$ with $\epsilon\to0$ the roots tend to $-i\vec e_x$ and to $-i\vec e_y$, and the two kernels differ at every $t$ where $\sin(2\pi\omega t)\neq0$. **No limit exists.**

**Boundary.** The identity is pointwise in the element: it identifies the kernel of the transform with the flow of one regular element, and it changes no inversion, Plancherel or convolution statement.

## The Continuous Transform Pair

### Definition

Let $f : \mathbb{R} \to \mathbb{B}$ be a biquaternion-valued function. The **continuous biquaternion Fourier transform** of $f$ is

$$
F(\omega) = \int_{-\infty}^{\infty} W(t, \omega) f(t) \, dt = \int_{-\infty}^{\infty} \exp\left(-2\pi i\tilde{Ζ}\omega t\right) f(t) \, dt, \qquad \omega \in \mathbb{R},
$$

provided the integral converges. The **inverse transform** is

$$
f(t) = \int_{-\infty}^{\infty} W(t, \omega)^{-1} F(\omega) \, d\omega,
$$

provided the integral converges. The inverse is written $W^{-1}$ and never the conjugation, because the two agree only for a pure root, where $W^{-1}=W^{\natural}$; at the central roots the kernel is a complex scalar and only the coefficient conjugation inverts it.

The placement of the kernel on the **left** of $f(t)$ is a choice. An alternative transform has the kernel on the right:

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) \, W(t, \omega) \, dt.
$$

The two transforms are related as in the discrete case: the conjugate of the left-kernel transform of $f$ is the right-kernel transform of the conjugate of $f$, with a sign change in the kernel, because $\overline{K(t,\omega) f(t)} = \overline{f(t)}\,\overline{K(t,\omega)}$ reverses the order.

### Convergence

The integral defining the transform converges absolutely if $f$ is integrable, that is, if

$$
\int_{-\infty}^{\infty} \lVert f(t)\rVert \, dt < \infty,
$$

where $\lVert\cdot\rVert$ is the Euclidean norm of the eight real coordinates. Under this condition the transform $F$ is bounded and uniformly continuous:

$$
\lVert F(\omega)\rVert \leq \int_{-\infty}^{\infty} \lVert f(t)\rVert \, dt, \qquad \omega \in \mathbb{R}.
$$

The convergence of the inverse requires the conditions of the complex case, $f$ integrable and continuous at $t$ and $F$ integrable, and under them the inverse formula holds at every point of continuity of $f$.

### The Riemann–Lebesgue Lemma

**Theorem (Riemann–Lebesgue).** If $f : \mathbb{R} \to \mathbb{B}$ is integrable, then

$$
\lim_{\lvert\omega\rvert \to \infty} \lVert F(\omega)\rVert = 0.
$$

*Proof.* The kernel is bounded and the integrand is integrable, and the standard proof applies component-wise, in either of the two Peirce coordinates, where the kernel is a scalar $e^{\mp2\pi i\omega t}$.

### The Inversion Theorem

**Theorem (inversion).** Let $f : \mathbb{R} \to \mathbb{B}$ be integrable and continuous at a point $t \in \mathbb{R}$, and let $F$ be integrable. Then

$$
\boxed{\; f(t) = \int_{-\infty}^{\infty} W(t, \omega)^{-1} F(\omega) \, d\omega \;}.
$$

*Proof.* Split $f=\tilde\Pi_+f+\tilde\Pi_-f$ into its Peirce components. The kernel commutes with the two idempotents and acts on them by the two scalars, so the transform separates,

$$
F(\omega) = \int_{-\infty}^{\infty} e^{-2\pi i\omega s}\,\tilde\Pi_+ f(s) \, ds + \int_{-\infty}^{\infty} e^{+2\pi i\omega s}\,\tilde\Pi_- f(s) \, ds ,
$$

a pair of ordinary complex transforms of the two components, the second at the frequency $-\omega$. Each is inverted by the classical inversion theorem under the stated hypotheses, in the ℂ² coordinates of its ideal, and the two results add to $\tilde\Pi_+f(t)+\tilde\Pi_-f(t)=f(t)$.

The theorem is unconditional in the root: it uses only the closed form of the kernel, which holds at every root. What it does not give is an isometry, and that is the next subsection.

### The Plancherel Theorem

**Theorem (Plancherel).** Let the root be **Hermitian**, $\tilde{Ζ}^{*}=\tilde{Ζ}$, the central pair or a purely imaginary unit vector. Then the transform extends uniquely to an isometry of $L^{2}(\mathbb{R}, \mathbb{B})$ onto itself, with

$$
\boxed{\; \int_{-\infty}^{\infty} \lVert f(t)\rVert^{2} \, dt = \int_{-\infty}^{\infty} \lVert F(\omega)\rVert^{2} \, d\omega \;}.
$$

*Proof.* For a Hermitian root the two idempotents are Hermitian, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$, and the Peirce split is orthogonal for the Euclidean form:

$$
\lVert f(t)\rVert^{2} = \lVert \tilde\Pi_+ f(t)\rVert^{2} + \lVert \tilde\Pi_- f(t)\rVert^{2},
$$

because the cross terms are scalar parts of $P_+XX^{*}P_-^{*}=P_+XX^{*}P_-$, which vanish since $P_+P_-=0$. On each ideal the kernel is the scalar $e^{\mp2\pi i\omega t}$, so the transform of $\tilde\Pi_\pm f$ is the ordinary complex transform of a ℂ²-valued function, a complex isometry by the classical theorem. Summing the two isometries and using the orthogonality gives the displayed identity, and the extension is unique because the integrable functions are dense.

**The genuinely non-Hermitian roots.** Off the Hermitian roots the transform is still invertible, by §*The Inversion Theorem*, but it is **not** an isometry for the Euclidean norm. The identity above fails at the first step: the Peirce split is not orthogonal, and the quantity the transform preserves is

$$
\lVert \tilde\Pi_+ f\rVert^{2} + \lVert \tilde\Pi_- f\rVert^{2},
$$

a positive form that agrees with the Euclidean one only for a Hermitian root. The failure is measured by the size of the root: a pure root has $\lVert\tilde{Ζ}\rVert^{2}=1+2\lVert\vec p\rVert^{2}$, so the Hermitian roots are the pure roots of Euclidean norm one, and the excess is the amplitude that *Relations between the Biquaternion Exponential and the Fourier Kernel* calls the norm deficit.

**Corollary (Parseval).** For a Hermitian root and $f, g \in L^{2}(\mathbb{R}, \mathbb{B})$,

$$
\int_{-\infty}^{\infty} \langle f(t), g(t)\rangle_{*} \, dt = \int_{-\infty}^{\infty} \langle F(\omega), G(\omega)\rangle_{*} \, d\omega ,
$$

where $\langle X, Y\rangle_{*}=\mathrm{Sc}(XY^{*})$ is the Hermitian pairing whose diagonal is the square of the Euclidean norm.

## Factorization into Complex Fourier Transforms

### The Change of Basis

Let $\tilde{Ζ}$ be a pure root. Choose two more pure elements $\nu$ and $\zeta$ with

$$
(\tilde{Ζ},\nu)=(\nu,\zeta)=(\zeta,\tilde{Ζ})=0, \qquad \tilde{Ζ}\nu=\zeta, \qquad \tilde{Ζ}\zeta=\nu ,
$$

the last identity being $\tilde{Ζ}^{2}\nu=\nu$. The four elements $\{e_t,\tilde{Ζ},\nu,\zeta\}$ are a basis of $\mathbb{B}$ over $\mathbb{C}$, and each of the three vector elements is pure with square $-e_t$, so the Gram matrix of the bilinear form $(X,Y)=\mathrm{Sc}(X^{\natural}Y)$ in this basis is

$$
\mathrm{diag}(1,-1,-1,-1).
$$

The basis is Euclidean-orthonormal exactly for a Hermitian root, and for a non-Hermitian pure root its vector elements have Euclidean norm greater than one. Any biquaternion is written in it as

$$
\tilde{Q} = Q_t e_t + Q_Z \tilde{Ζ} + Q_\nu \nu + Q_\zeta \zeta,
$$

with $Q_t, Q_Z, Q_\nu, Q_\zeta \in \mathbb{C}$. Left multiplication by $\tilde{Ζ}$ acts on the basis by $\tilde{Ζ}e_t=\tilde{Ζ}$, $\tilde{Ζ}\tilde{Ζ}=e_t$, $\tilde{Ζ}\nu=\zeta$, $\tilde{Ζ}\zeta=\nu$: it is the identity on the two planes $\operatorname{span}\{e_t,\tilde{Ζ}\}$ and $\operatorname{span}\{\nu,\zeta\}$ up to the exchange of each pair, and its eigenvalues are $\pm1$ with multiplicity four each. That is the Peirce structure read in coordinates, and it is why the root of $1$ needs no nilpotent pair.

### The Factorization

Substituting the closed form of the kernel and the expansion of $f$ in the basis,

$$
F(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, e_t - i\sin(2\pi \omega t) \, \tilde{Ζ}\right) \left(w(t) e_t + Q_Z(t) \tilde{Ζ} + Q_\nu(t) \nu + Q_\zeta(t) \zeta\right) dt ,
$$

and collecting by basis element, using $\tilde{Ζ}\tilde{Ζ}=e_t$, $\tilde{Ζ}\nu=\zeta$, $\tilde{Ζ}\zeta=\nu$, gives four components:

$$
F(\omega) = F_0(\omega) e_t + F_Z(\omega) \tilde{Ζ} + F_\nu(\omega) \nu + F_\zeta(\omega) \zeta ,
$$

where

$$
F_0(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, w(t) + i\sin(2\pi \omega t) \, Q_Z(t)\right) dt,
$$

$$
F_Z(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, Q_Z(t) - i\sin(2\pi \omega t) \, w(t)\right) dt,
$$

$$
F_\nu(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, Q_\nu(t) + i\sin(2\pi \omega t) \, Q_\zeta(t)\right) dt,
$$

$$
F_\zeta(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, Q_\zeta(t) - i\sin(2\pi \omega t) \, Q_\nu(t)\right) dt.
$$

The four sums have the same shape: a cosine times one coefficient plus or minus $i$ times a sine times its partner. The pairs are $(w,Q_Z)$, $(Q_Z,w)$, $(Q_\nu,Q_\zeta)$ and $(Q_\zeta,Q_\nu)$.

### The Complex Fourier Transforms

Writing the cosine and the sine as exponential sums, each of the four components is a combination of ordinary complex transforms at $\omega$ and at $-\omega$:

$$
F_\bullet(\omega) = \frac{1}{2}\bigl(\hat{G}_\bullet(\omega) + \hat{G}_\bullet(-\omega)\bigr) + \frac{1}{2}\bigl(\hat{H}_\bullet(-\omega) - \hat{H}_\bullet(\omega)\bigr),
\qquad
\hat{G}_\bullet(\omega) = \int_{-\infty}^{\infty} e^{-2\pi i \omega t} G_\bullet(t) \, dt ,
$$

with $(G_\bullet, H_\bullet)$ equal to $(w, Q_Z)$, $(Q_Z, w)$, $(Q_\nu, Q_\zeta)$ and $(Q_\zeta, Q_\nu)$ for the four components. The sign of the second bracket is the sign of $i$ in the closed form of the kernel, which is the sign the root of $1$ carries as a scalar.

The factorization shows that the biquaternion transform is the ordinary complex transform applied entrywise to the coefficients, once the basis is chosen. **The non-trivial content is the root and the basis it forces**, not the operation.

### The Number of Complex Transforms

The count is the same at every root: **four** scalar complex transforms, the four complex coefficients of the expansion above. Read through the Peirce pair instead, it is two complex transforms on the two ideals, each ideal being a complex plane, and the two readings agree: at the central root one idempotent vanishes, one ideal carries the whole algebra, and the same four appear.

## The Convolution Theorem

### Definition of Convolution

Let $f, g : \mathbb{R} \to \mathbb{B}$ be two biquaternion-valued functions. The **convolution** of $f$ and $g$ is

$$
(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau,
$$

provided the integral converges. The convolution is **not commutative** in general, because the biquaternion product is not commutative.

### The Convolution Theorem

**Theorem (convolution theorem).** Let $f, g : \mathbb{R} \to \mathbb{B}$ be integrable, assume the kernel is **central on the values**, $W(t,\omega)a = aW(t,\omega)$ for every value $a$ of $f$ and $g$ and every $t, \omega$, and let $\mathcal{F}$ denote the continuous biquaternion Fourier transform with the kernel on the left:

$$
\mathcal{F}[f](\omega) = \int_{-\infty}^{\infty} W(t, \omega) f(t) \, dt.
$$

Then

$$
\boxed{\; \mathcal{F}[f * g](\omega) = \mathcal{F}[f](\omega) \cdot \mathcal{F}[g](\omega) \;},
$$

where the product on the right is the biquaternion product.

*Proof.* Compute

$$
\mathcal{F}[f * g](\omega) = \int_{-\infty}^{\infty} W(t, \omega) \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau \, dt.
$$

Apply Fubini's theorem and change variables $t = \tau + s$:

$$
\mathcal{F}[f * g](\omega) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} W(\tau + s, \omega) f(\tau) g(s) \, ds \, d\tau.
$$

The kernel is multiplicative in the time argument, $W(\tau + s, \omega) = W(\tau, \omega) W(s, \omega)$, and central on the values, so $W(s,\omega)$ moves past $f(\tau)$. Then

$$
\mathcal{F}[f * g](\omega) = \int_{-\infty}^{\infty} W(\tau, \omega) f(\tau) \, d\tau \cdot \int_{-\infty}^{\infty} W(s, \omega) g(s) \, ds = \mathcal{F}[f](\omega) \cdot \mathcal{F}[g](\omega).
$$

**Corollary (right-kernel case).** For the transform with the kernel on the right and the same hypothesis,

$$
\mathcal{F}_{\text{right}}[f * g](\omega) = \mathcal{F}_{\text{right}}[f](\omega) \cdot \mathcal{F}_{\text{right}}[g](\omega).
$$

The order is not reversed: the same computation moves the kernel past $g$ and leaves $f$ in front. Without the hypothesis no placement of the kernel gives a theorem, because the two integrals cannot be separated.

### Consequences

Under the hypothesis, convolution becomes **biquaternion multiplication** in the frequency domain; the convolution itself is associative, distributive over addition, and not commutative. The hypothesis is satisfied at the central roots, where the kernel is a complex scalar, and by every pair of functions whose values lie in $\mathbb{C}[\tilde{Ζ}]$; it fails for arbitrary values at a genuine root, and the failure is the one described in the discrete article.

## The Relation to the Differential Operators

The continuous Fourier transform is the natural tool for analysing the differential operators of the analysis article. This is the main structural content of the continuous theory.

### The Gradient

Let $\tilde{\nabla}$ be the biquaternion gradient on a four-dimensional subspace $V \subset \mathbb{B}$, with coordinates $Q_t, Q_x, Q_y, Q_z$. For a function $F_{\mathrm{fn}} : V \to \mathbb{B}$, the Fourier transform in the variable $Q_t$ (with the other coordinates treated as parameters, or with a full four-dimensional transform) diagonalizes the partial derivative $\partial/\partial Q_t$:

$$
\mathcal{F}[\partial/\partial Q_t F_{\mathrm{fn}}](\omega) = 2\pi i\,\tilde{Ζ}\,\omega \, \mathcal{F}[F_{\mathrm{fn}}](\omega),
$$

the sign being that of integration by parts: the forward kernel $\exp(-2\pi i\tilde{Ζ}\omega t)$ gives the plus sign shown, and the sign reverses if the exponent of the kernel is reversed.

If the transform is taken in all four variables, the gradient becomes multiplication by the biquaternion

$$
2\pi i\,\tilde{Ζ} \left(\omega_0 e_t + \omega_1 \vec e_x + \omega_2 \vec e_y + \omega_3 \vec e_z\right),
$$

where $\omega_0, \omega_1, \omega_2, \omega_3$ are the frequency variables conjugate to $Q_t, Q_x, Q_y, Q_z$. The structural fact is that the gradient becomes a biquaternion-valued multiplier.

### The d'Alembertian

The d'Alembertian $\Box = \partial^2/\partial Q_t^2 + \Delta$ is the four-dimensional Laplacian of the analysis article, a scalar operator, and it commutes with the Fourier transform. One sign convention governs every symbol below: the symbol of $\partial_\mu$ is $2\pi i\tilde{Ζ}\omega_\mu$, so the symbol of $\partial_\mu^2$ is $-(2\pi\omega_\mu)^{2}e_t$, the sign being carried by $\tilde{Ζ}^{2}=e_t$. Under the transform,

$$
\boxed{\; \mathcal{F}[\Box F_{\mathrm{fn}}](\omega) = -(2\pi)^2 \left(\omega_0^2 + \omega_1^2 + \omega_2^2 + \omega_3^2\right) \mathcal{F}[F_{\mathrm{fn}}](\omega) \;}.
$$

The multiplier is a negative scalar and it vanishes only at $\omega=0$: $\Box$ is elliptic, and a solution of $\Box F_{\mathrm{fn}}=0$ whose transform is a function has transform supported at the origin. **The operator whose symbol vanishes on a cone is the hyperbolic one**, $\partial_t^2-\Delta$, with symbol

$$
-4\pi^2 \left(\omega_0^2 - \omega_1^2 - \omega_2^2 - \omega_3^2\right),
$$

whose zero set is the **null cone** $\omega_0^2 = \omega_1^2 + \omega_2^2 + \omega_3^2$; the transform of a solution is supported there. The two operators differ by the sign of $\Delta$, and that sign is the sign $\tilde{Ζ}^{2}=e_t$ supplies through the square of the imaginary scalar.

### The Square of the Gradient

The square of the gradient $\tilde{\nabla}^2 = (\partial^2/\partial Q_t^2 - \Delta) + 2\sum_k \vec e_k \partial^2/(\partial Q_t\,\partial Q_k)$ is a biquaternion-valued operator. Under the transform, it becomes multiplication by

$$
\left(-(2\pi \omega_0)^2 + (2\pi)^2 (\omega_1^2 + \omega_2^2 + \omega_3^2)\right) e_t - 2 \sum_k \vec e_k (2\pi \omega_0)(2\pi \omega_k),
$$

which is the square of the gradient symbol $2\pi i\tilde{Ζ}(\omega_0 e_t + \sum_k\omega_k\vec e_k)$, a biquaternion-valued multiplier, when $\tilde{Ζ}$ commutes with $\vec\omega$.

### The Convective Derivative

The convective derivative $\tilde{D} = \tilde Q_3^{\natural} \tilde{\nabla}$ becomes multiplication by the biquaternion

$$
\tilde Q_3^{\natural} \cdot 2\pi i\tilde{Ζ} (\omega_0 e_t + \omega_1 \vec e_x + \omega_2 \vec e_y + \omega_3 \vec e_z),
$$

which depends on the parameter biquaternion $\tilde Q_3$ and on the frequency variables. The multiplier is a biquaternion, and its vanishing determines the frequency set of the operator, that is the real zero set of the symbol.

### The General Principle

The continuous transform **diagonalizes the constant-coefficient differential operators** on the four-dimensional subspaces: the symbol is a biquaternion-valued function of the frequency variables, and the solutions of the operator equation are determined by the support of the transform on the zero set of the symbol. This is the principle of the symbol article, and it is why the transform is the tool for the operators of the analysis article.

## The Vanishing-Norm Issue

### Functions of Vanishing Norm

A function $f : \mathbb{R} \to \mathbb{B}$ may take values of vanishing norm on a set of positive measure. On such a set the values are zero divisors: for some $t$ there is a nonzero biquaternion $\tilde{Q}(t)$ with $f(t)\tilde{Q}(t) = 0$ or $\tilde{Q}(t)f(t) = 0$. Since the kernel is a unit, the product $W(t,\omega)f(t)$ is a zero divisor too.

None of this damages the transform. The inversion theorem is a statement about the kernel and holds for every integrable $f$; what a zero-divisor value damages is the arithmetic after the transform, where a null element has no inverse to divide by.

### Consequences for the Transform

- **The transform is invertible whatever values the function takes**, the inversion being a property of the kernel and not of the samples.
- **What a zero-divisor value blocks is the division of the transform**, not its recovery: a spectrum that is a null element at some frequency cannot be divided by there.

### Structural Interpretation

The vanishing-norm issue is a genuinely biquaternionic feature: the complex and quaternion algebras are division algebras, and the biquaternion algebra is not. A definite subspace removes the difficulty of division, since on $\mathbb{B}_{H}$ the norm is a sum of real squares and every nonzero value is a unit; on $\mathbb{B}_{\Phi}$ the values of vanishing norm lie on a cone, and the division is available off it.

### The Open Question

Whether the spectrum of such a function can avoid the null cone is not decided by the norms of its values. It depends on the cancellations in the integral $\int W(t, \omega) f(t) \, dt$, and it is not settled here.

## The Two-Dimensional Kernel with One Unit per Variable

The transform above carries one real variable and one root. The two-variable transform carries two variables and assigns one root to each, and in the biquaternion algebra that assignment is a genuine choice, because the roots of $1$ fall into the two families classified above.

**Definition.** Let $\tilde{Ζ}_1$ and $\tilde{Ζ}_2$ be roots of $1$ in $\mathbb{B}$, not necessarily distinct and not necessarily commuting. For a function $f : \mathbb{R}^2 \to \mathbb{B}$, the **two-unit transform** is

$$
F(\omega_1, \omega_2) = \int_{\mathbb{R}^2} W_1(Q_x, \omega_1) \, W_2(Q_y, \omega_2) \, f(Q_x, Q_y) \, dQ_x dQ_y,
\qquad
W_k(Q_k, \omega_k) = \exp(-2\pi i \tilde{Ζ}_k \omega_k Q_k),
$$

the order of the two kernel factors being part of the definition, because they need not commute. The discrete case places one kernel on each side of $f$; the placement is a convention here as it is for the one-unit transform, and the left-left placement is the one used below. The **two-unit kernel** is their product $K = W_1 W_2$.

**Closed form.** With $\theta_k = 2\pi \omega_k Q_k$,

$$
K = \cos\theta_1 \cos\theta_2 \, e_t - i\cos\theta_1 \sin\theta_2 \, \tilde{Ζ}_2 - i\sin\theta_1 \cos\theta_2 \, \tilde{Ζ}_1 - \sin\theta_1 \sin\theta_2 \, \tilde{Ζ}_1 \tilde{Ζ}_2 .
$$

The first term is central and the next two are pure, because the roots are pure; the fourth carries the product $\tilde{Ζ}_1\tilde{Ζ}_2$, which is a unit when the two roots commute and a general element when they do not.

**Reduction to the one-unit kernel.** If the two roots coincide, $\tilde{Ζ}_1 = \tilde{Ζ}_2 = \tilde{Ζ}$, the exponents add and $K$ is the kernel $W$ read on the linear form $\omega_1 Q_x + \omega_2 Q_y$, which is the kernel of the two-dimensional transform of the discrete case. The one-unit theory is the case in which the two roots are equal, and the two-unit transform is its refinement.

**The kernel is invertible for every pair of roots.** The natural norm is multiplicative, $\langle K\rangle_{\natural} = \langle W_1\rangle_{\natural} \langle W_2\rangle_{\natural}$, and the inverse is the kernel with both frequencies negated and the two factors exchanged:

$$
K(\omega)^{-1} = W_2(Q_y, -\omega_2) \, W_1(Q_x, -\omega_1).
$$

For two pure roots the kernel is on the natural unit sphere,

$$
\langle K\rangle_{\natural} = e_t, \qquad K(\omega)^{\natural} = K(\omega)^{-1},
$$

and this holds for every pair of pure roots, commuting or not. The unit-norm property is thus a property of each factor and is inherited by the product.

**Frequency reversal.** Reversing the sign of the frequencies conjugates the kernel **and exchanges the two factors**, $K(\omega)^{\natural} = K_{\mathrm{ex}}(-\omega)$, where $K_{\mathrm{ex}}$ is the kernel with the two roots interchanged. For two pure roots the identity is exact, and it reduces to $W(t,\omega)^{\natural} = W(t,-\omega)$ when there is one root to exchange. The form without the exchange needs in addition that the factors commute, so it fails for two pure roots that are neither equal nor opposite.

## The Transform of a Measure, and the Failure of Positivity

**Definition.** Let $\mu$ be a finite positive measure on $\mathbb{R}^n$ and let $\tilde{Ζ}$ be a pure root of $1$. The **transform of the measure** is

$$
G(\omega) = \int_{\mathbb{R}^n} \chi_\omega(\tilde{Q}) \, d\mu(\tilde{Q}), \qquad \chi_\omega(\tilde{Q}) = \exp\bigl(-2\pi i\,\tilde{Ζ}\, \langle \omega, \tilde{Q} \rangle\bigr).
$$

Because $\chi_0 = e_t$ at every point, $G(0) = \mu(\mathbb{R}^n) \, e_t$: the value at zero frequency is the total integral, a positive real multiple of the identity.

**The quadratic form.** For coefficients $A_1, \dots, A_N$ in the centre $\mathbb{B}_{C}$ (the complex scalars $A_k = \varkappa_{\mathrm{crd},k} e_t$, $\varkappa_{\mathrm{crd},k} \in \mathbb{C}$) and frequencies $\omega_1, \dots, \omega_N$,

$$
\sum_{k,l=1}^{N} \bar A_k A_l \, G(\omega_k - \omega_l) \;=\; \int_{\mathbb{R}^n} \langle Z(\tilde{Q})\rangle_{\natural} \, d\mu(\tilde{Q}),
\qquad
Z(\tilde{Q}) = \sum_{k=1}^{N} A_k \chi_{\omega_k}(\tilde{Q}) ,
$$

the right-hand side being the integral of the **biquaternion norm** of the trigonometric sum. The identity is one line, because $\bar\chi_\omega \chi_\eta = \chi_{\eta - \omega}$ for a pure root, so each term of the sum reassembles a product inside the modulus. It is the exact content of the classical statement that the Fourier transform of a measure is a positive-definite function.

**The Hermitian case.** If the root is Hermitian, $\tilde{Ζ}=i\vec u$ over a real unit vector, and the coefficients are real, then $Z = a e_t - b\vec u$ with $a$ and $b$ real and the integrand is $a^{2}+b^{2}\ge0$: the form is non-negative. That is the hypothesis the classical theorem of Bochner runs on, and the quaternion form of the statement is the subject of *Quaternion Harmonic Analysis*.

**The biquaternion case: the form is the norm, and the norm is indefinite.** For $\mathbb{B}$ the integrand is the norm itself, and the norm is complex-valued:

$$
\langle\tilde{Q}\rangle_{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2, \qquad \Re \langle\tilde{Q}\rangle_{\natural} = \sum_{\mu\in\{t,x,y,z\}} (\Re Q_\mu)^2 - \sum_{\mu\in\{t,x,y,z\}} (\Im Q_\mu)^2
$$

in the eight real components of $\tilde{Q}$. The failure needs no zero divisor and no exceptional value. At $N=1$, with the scalar imaginary for coefficient,

$$
A_1 = i: \qquad \bar A_1 A_1 \, G(0) = i^2 \, \mu(\mathbb{R}^n) = -\mu(\mathbb{R}^n) \, e_t ,
$$

which is negative for every non-zero measure, because $\langle i\rangle_{\natural} = -1$. The scalar imaginary is a unit of the algebra — the element whose presence makes the algebra biquaternionic — and the norm is negative on it. Hence **the transform of a measure is not a positive-definite function for $\mathbb{B}$**, and the positivity a Bochner-type hypothesis would need is not available. The absence is the same indefiniteness the vanishing-norm section records, read at a different value: the norm vanishes on the null cone and it is negative on the centre.

**The repair, and what it costs.** Positivity returns when the norm is replaced by a definite pairing, whose integrand is a sum of squares of moduli,

$$
\lVert Z(\tilde{Q})\rVert^2 = \sum_{\mu\in\{t,x,y,z\}} \lvert Z_\mu(\tilde{Q}) \rvert^2 \ge 0 ,
$$

so the Euclidean quadratic form is non-negative, and $\lVert\cdot\rVert$ is the pairing this article already uses for convergence. What the exchange costs is the norm and not the algebra: the Euclidean form is not the biquaternion norm of the transform, and it is not multiplicative on the product, $\lVert ZW\rVert\neq\lVert Z\rVert\lVert W\rVert$ in general, the Hermitian idempotent $\tilde\Pi=\tfrac12(e_t+i\vec e_x)$ giving $\lVert\tilde\Pi^{2}\rVert=\tfrac12$ against $\lVert\tilde\Pi\rVert^{2}=\tfrac14$. It is nonetheless the scalar part of the sesquilinear product, $\lVert Z\rVert^{2}=\mathrm{Sc}(ZZ^{*})=\langle Z,Z\rangle_{*}$, and with the Hermitian conjugation in the second slot it is the pairing that makes the transform of a positive measure positive definite exactly for the Hermitian roots; the criterion and its proof are *The General Plain Sesqualgebra (gps) over $\mathbb{C}$*.

**Two hypotheses.** The identity requires central coefficients, because the coefficient has to commute with the kernel; for quaternion-valued coefficients the products $A_k\chi_{\omega_k}$ do not reassemble and the two sides differ by terms of order one on random data. It requires a single root as well: with two roots, one per variable, the collapse $\bar\chi_\omega\chi_\eta=\chi_{\eta-\omega}$ fails as soon as the two differ. The Bochner-type positivity is therefore a one-root, central-coefficient statement even for $\mathbb{H}$, and for $\mathbb{B}$ it fails under those hypotheses as well.

## The Relation to the Discrete Transform

### Sampling

If $f$ is of bounded variation and $F$ is its continuous transform, the discrete transform of the samples $f(nT)$ converges to $F$ as the sampling interval $T$ tends to zero. **This is quoted, not proved here**; its hypotheses are the Riemann integrability of $f$ together with the bounded variation that makes the Riemann sums converge.

### Periodization

Conversely, the discrete transform of the samples $f(nT)$ is the periodization of the continuous transform:

$$
F_{\text{disc}}[x] = \frac{1}{T} \sum_{k \in \mathbb{Z}} F\left(\frac{x}{NT} + \frac{k}{T}\right).
$$

This is Poisson summation, and it holds in the biquaternion case with the same proof, the kernel being the ordinary complex kernel in each Peirce coordinate.

### The Sampling Theorem

**The sampling theorem**, quoted: a function whose continuous transform is supported in a bounded interval $[-\beta, \beta]$ is reconstructed from its samples at the rate $1/(2\beta)$, by

$$
f(t) = \sum_{n \in \mathbb{Z}} f(nT) \operatorname{sinc}\left(\frac{t - nT}{T}\right),
$$

where the sinc is the ordinary real one. The half-width is written $\beta$ and not $W$, because $W$ is the kernel, and not $b$, because $b$ is reserved for a magnitude in the root parametrisation. The biquaternion case holds under the same hypotheses with the same proof, the reconstruction being componentwise in a basis adapted to the root.

## Open Questions

1. **Divisibility of the spectrum.** The transform is invertible for every integrable $f$, so what is open is whether a spectrum can avoid the null cone, that is whether a convolution can be undone pointwise.

2. **The support of the transform of solutions of $\tilde{\nabla}F_{\mathrm{fn}} = 0$.** The transform of a solution is supported on a set determined by the symbol of the gradient. What is the structure of this set?

3. **Plancherel for the other roots.** The isometry is stated for the Hermitian roots; for the other pure roots the transform preserves the Peirce norm $\lVert\tilde\Pi_+f\rVert^{2}+\lVert\tilde\Pi_-f\rVert^{2}$ and no Euclidean one, and the sharp form of the loss is open.

4. **Two roots that do not commute.** The two-unit transform is defined for every pair, and its factorisation is proved only when the two commute or coincide; whether it still reduces to a fixed finite family of complex transforms is open.

5. **The relation to the analysis article.** The connection is established at the level of symbols. What are the consequences for the structure of the solutions themselves?

6. **The Clifford algebra framework.** How does the biquaternion continuous Fourier transform fit into the general theory of Clifford algebra Fourier transforms?

7. **Positivity for the transform of a measure.** The quadratic form is the integral of the norm, and the norm is indefinite, so the biquaternionic Bochner hypothesis has no apparent source. **Answered** in *The General Plain Sesqualgebra (gps) over $\mathbb{C}$*: the pairing is the general plain sesquilinear form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$, whose diagonal is the Euclidean form of the section above, and with the Hermitian conjugation in the second slot the transform of a positive measure is positive definite exactly for the Hermitian roots and not for the others. What is restored is the positivity, not the norm identity: the failure at $A=i$ is root-independent and survives the exchange.

## Summary

The continuous biquaternion Fourier transform is defined by the kernel $W(t, \omega) = \exp(-2\pi i\tilde{Ζ}\omega t)$, where $\tilde{Ζ}$ is a root of $1$ in $\mathbb{B}$. The root of $1$ is the parameter, not a root of $-1$: the scalar $i$ in the exponent carries the sign, and the algebra element carries only the square $e_t$.

The roots of $1$ are the central pair $\pm e_t$ and the pure elements $\vec{Ζ}$ with $(\vec{Ζ},\vec{Ζ})=-1$, so the parameter has two families and no third. The root is an idempotent pair through the halving map, the kernel is a pair of conjugate unit complex numbers on the two Peirce ideals, and the transform is a pair of ordinary complex transforms there, that is four scalar complex transforms.

The transform is invertible for every integrable function, whatever values it takes; the inverse uses $W^{-1}$ and not the quaternion conjugation, which inverts only for a pure root. It satisfies the Riemann–Lebesgue lemma, the inversion theorem and the Plancherel theorem for the Hermitian roots, and it factorises into four complex Fourier transforms.

The convolution theorem holds under the centrality of the kernel on the values, with the non-commutativity requiring careful placement of the kernel. The transform diagonalizes the constant-coefficient differential operators: the gradient becomes a biquaternion-valued multiplier, the d'Alembertian a negative scalar multiplier vanishing only at the origin, the hyperbolic operator $\partial_t^2 - \Delta$ a multiplier vanishing on the null cone, and the convective derivative a biquaternion-valued multiplier depending on its parameter.

The vanishing-norm issue does not obstruct the inversion: what a zero-divisor value obstructs is the pointwise division of a spectrum.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, $M_2(\mathbb{C})$ as a complex algebra |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | the unit and the three vector units, $\vec e_k^{2}=-e_t$ |
| $i$ | the complex scalar imaginary |
| $\tilde{Ζ}$ | a root of $1$, $\tilde{Ζ}^{2}=e_t$ |
| $\vec{Ζ}$ | a pure root of $1$, $(\vec{Ζ},\vec{Ζ})=-1$ |
| $\vec p, \vec p'$ | the real and imaginary parts of $\vec{Ζ}=\vec p+i\vec p'$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ | the idempotent pair of the root, $\tilde{Ζ}=\tilde\Pi_+-\tilde\Pi_-$ |
| $\tilde\Pi_\pm\mathbb{B}$ | the two Peirce ideals, each a complex plane |
| $W(t,\omega)=\exp(-2\pi i\tilde{Ζ}\omega t)$ | the biquaternion Fourier kernel |
| $\cos\theta\,e_t-i\sin\theta\,\tilde{Ζ}$ | its closed form, $\theta=2\pi\omega t$ |
| $W(t,-\omega)=W(t,\omega)^{-1}$ | the inverse kernel |
| $\nu, \zeta$ | two pure directions completing $\tilde{Ζ}$ to a basis |
| $F(\omega)$ | the transform of $f(t)$ |
| $W_1, W_2$, $K=W_1W_2$ | the two-unit kernel and its product |
| $\chi_\omega$ | the character of the measure transform |
| $\natural$ | the quaternion conjugation, $e_t\mapsto e_t$, $\vec e_k\mapsto-\vec e_k$ |
| $*$ | the Hermitian conjugation, $\bar{\cdot}\circ\natural$ |
| $\langle\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$ | the natural norm, a complex scalar |
| $\lVert\cdot\rVert$ | the Euclidean norm of the eight real coordinates |
| $\langle X,Y\rangle_{*}=\mathrm{Sc}(XY^{*})$ | the Hermitian pairing |
| $\beta$ | the half-width of the support in the sampling theorem |

## Further Reading

- [Biquaternion Discrete Harmonic Analysis](biquaternion-discrete-harmonic-analysis.html), for the discrete transform, its inversion, its convolution theorem and the same Peirce factorization on a finite index set.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the de Moivre formula and the idempotents of the biquaternion algebra.
- [Relations between the Biquaternion Exponential and the Fourier Kernel](relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the dictionary between the flow of an element and the kernel at the root the element supplies.
- [Special Element and Peirce Conventions](special-element-and-peirce-conventions.html), for the root glyph, the idempotent family and the Peirce table.
- [The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root](the-bochner-theorem-for-the-biquaternion-transform-the-hermitian-form-and-the-root.html), for the positivity criterion.
- *The General Plain Sesqualgebra (gps) over $\mathbb{C}$*, for the sesquilinear form that repairs the positivity.
- [Harmonic Analysis over Hypercomplex Systems](harmonic-analysis-over-hypercomplex-systems.html), for the place of the transform among the eight systems, and [Biquaternion Analysis](biquaternion-analysis.html), for the differential operators whose symbols the transform multiplies by.
- [Quaternion Harmonic Analysis](quaternion-harmonic-analysis.html), for the quaternion case, the two-variable transform and its Bochner theorem.
