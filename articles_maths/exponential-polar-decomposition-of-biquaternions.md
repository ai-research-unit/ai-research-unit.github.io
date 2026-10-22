# __Exponential Polar Decomposition of Biquaternions__

## Introduction

This article treats the **exponential polar decomposition** of an invertible biquaternion: the writing

$$
\tilde Q=r\,e^{i\alpha}\,e^{i\frac{\psi}{2}\vec u_{\mathrm b}}\,e^{\frac{\theta}{2}\vec u_{\mathrm r}},
\qquad r>0,\quad \alpha\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],\quad \psi\ge0,\quad \theta\in[0,2\pi],
$$

with $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ unit vectors of $\mathbb{R}^{3}$. The four exponentials are the four factors of the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Biquaternions*,

$$
\tilde Q=r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad \zeta=e^{i\alpha},\quad \tilde U_{\mathrm b}=e^{i\frac{\psi}{2}\vec u_{\mathrm b}},\quad \tilde u_{\mathrm r}=e^{\frac{\theta}{2}\vec u_{\mathrm r}},
$$

read with the parameters of each factor displayed. The scale is $r=e^{\ln r}$, the central phase is $\zeta=e^{i\alpha}$, the boost is the Hermitian positive unit-norm element of rapidity $\psi$ and axis $\vec u_{\mathrm b}$, and the rotor is the unit real quaternion of angle $\theta$ and axis $\vec u_{\mathrm r}$.

The exponential and the logarithm themselves — the series, the closed forms, the kernel and the matrix logarithm — are defined and computed in *Biquaternion Elementary Functions*, §*The Exponential* and §*The Logarithm*; this article does not define them again. It uses the closed form

$$
\exp(\tilde X)=e^{X_t}\bigl(\cos B\,e_t+\sin B\,\vec u\bigr),
\qquad B=\sqrt{X_x^{2}+X_y^{2}+X_z^{2}},\quad \vec u=\frac{\vec X}{B},
$$

for $B\neq0$, and $\exp(\tilde X)=e^{X_t}(e_t+\vec X)$ for $B=0$, with the complex cosine and sine. The closed forms of the boost and of the rotor are the two real directions of *Biquaternion Elementary Functions*, §*The Exponential in the Two Real Directions*.

The quaternion case of *Exponential Polar Decomposition of Quaternions* amalgamates the scale and the rotor into a single exponential, $\tilde q=\exp(\ln r+\vec v)$, because the logarithmic scale is real and central and the remaining exponent is one pure quaternion. **The biquaternion case does not amalgamate.** The boost exponent $i\frac{\psi}{2}\vec u_{\mathrm b}$ and the rotor exponent $\frac{\theta}{2}\vec u_{\mathrm r}$ do not commute unless the two axes are parallel or antiparallel, so

$$
e^{i\frac{\psi}{2}\vec u_{\mathrm b}}e^{\frac{\theta}{2}\vec u_{\mathrm r}}
\neq e^{i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}}
$$

in general. The four exponents are therefore four, and the decomposition is a product of four exponentials. A single logarithm of $\tilde Q$ still exists — the group of units is $\mathrm{GL}_2(\mathbb{C})$, which is exponential — but it is not the sum of the four exponents; the difference is the Baker–Campbell–Hausdorff correction, computed in §*The Two Logarithms*.

The article states the four exponentials and their ranges (§*The Four Exponentials*), proves existence and uniqueness (§*Existence and Uniqueness*), separates the Cartan logarithm from the single logarithm (§*The Two Logarithms*), describes the kernel and the fibre (§*The Kernel and the Fibre*), reads the group law as the bracket of the two kinds of exponent (§*The Group Law*), gives the matrix picture (§*The Matrix Picture*), reads the parameters as coordinates on the group of units (§*The Exponential Coordinates*), and works one example in which the two logarithms are compared (§*Worked Example*).

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x\vec e_y=\vec e_z$, and central imaginary $i$, $i^{2}=-1$; a general element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients. The quaternion conjugation is $\tilde Q^{\natural}=Q_te_t-\vec Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\overline{Q_t}e_t+\overline{\vec Q}$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$. The norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_{\mu}Q_\mu^{2}$, and $\tilde Q$ is invertible exactly when $\langle\tilde Q\rangle_{\natural}\neq0$. The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf M_2(e_t)=I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$, with $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ and $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$. Every numerical value displayed below was recomputed in double precision.

## The Four Exponentials

### The Scale and the Phase

The scale is the positive real exponential

$$
r=e^{\ln r},\qquad \ln r\in\mathbb{R},
$$

and it is central: it multiplies every element of the algebra by $r$ and every image of the sandwich by $r^{2}$. In the exponential picture it is the one central factor that is neither periodic nor bounded, and the logarithmic scale is the same in the quaternion case.

The phase is the central unitary exponential

$$
\zeta=e^{i\alpha},\qquad \alpha\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],
$$

the branch of *Modulus–Unit Polar Decomposition of Biquaternions*: the closed right half of the unit circle with the point $-i$ removed. The interval is half-open and has length $\pi$, not $2\pi$, because the sign it leaves out is absorbed by the rotor; the element $-1$ is the rotor of angle $2\pi$, not a phase. The phase is periodic in $\alpha$ with period $2\pi$, and the branch selects one representative of each pair $\{\alpha,\alpha+\pi\}$ up to the central sign.

The two central exponentials commute with everything, so they may be written on either side of the two non-central ones. Their product is the complex modulus $\Rho=re^{i\alpha}$, with $r=\lvert\Rho\rvert$ and $\alpha=\arg\Rho$ in the branch.

### The Boost

Let $\vec u_{\mathrm b}$ be a unit vector of $\mathbb{R}^{3}$ and $\psi\ge0$. The **boost** is

$$
\tilde U_{\mathrm b}=e^{i\frac{\psi}{2}\vec u_{\mathrm b}}
=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}.
$$

The exponent is Hermitian and pure, $i\frac{\psi}{2}\vec u_{\mathrm b}$, and its square is the positive real number $\frac{\psi^{2}}{4}$:

$$
\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)^{2}
=-\frac{\psi^{2}}{4}\,\vec u_{\mathrm b}^{\,2}=\frac{\psi^{2}}{4}\,e_t,
$$

because $\vec u_{\mathrm b}^{\,2}=-e_t$. This is the hyperbolic case of the exponential: the argument $B$ of the closed form is $\pm i\frac{\psi}{2}$, purely imaginary, and the complex cosine and sine are the hyperbolic cosine and $i$ times the hyperbolic sine. The result is Hermitian, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, positive, of norm one, and unbounded as $\psi\to\infty$. It is not periodic, and $\psi\mapsto\tilde U_{\mathrm b}$ is injective on $[0,\infty)$.

The rapidity is recovered from the factor by

$$
\cosh\frac{\psi}{2}=\operatorname{Sc}\tilde U_{\mathrm b},\qquad
\sinh\frac{\psi}{2}=\bigl\lvert\operatorname{Vect}\tilde U_{\mathrm b}\bigr\rvert,
\qquad
\psi=2\operatorname{arcosh}\bigl(\operatorname{Sc}\tilde U_{\mathrm b}\bigr),
$$

the second identity because the vector part is $i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ and its coefficientwise modulus is $\sinh\frac{\psi}{2}$. The axis is the normalised vector part divided by $i$.

### The Rotor

Let $\vec u_{\mathrm r}$ be a unit vector of $\mathbb{R}^{3}$ and $\theta\in[0,2\pi]$. The **rotor** is

$$
\tilde u_{\mathrm r}=e^{\frac{\theta}{2}\vec u_{\mathrm r}}
=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r}.
$$

The exponent is real and pure, $\frac{\theta}{2}\vec u_{\mathrm r}$, and its square is $-\frac{\theta^{2}}{4}e_t$: this is the circular case of the exponential, with $B=\pm\frac{\theta}{2}$, real, and the complex cosine and sine the ordinary ones. The result is a unit real quaternion, unitary as well as norm-one; the rotation it induces is periodic with period $2\pi$ in $\theta$, while the rotor itself is $4\pi$-periodic. The angle is recovered by

$$
\cos\frac{\theta}{2}=\operatorname{Sc}\tilde u_{\mathrm r},\qquad
\sin\frac{\theta}{2}=\bigl\lvert\operatorname{Vect}\tilde u_{\mathrm r}\bigr\rvert,
\qquad
\theta=2\arccos\bigl(\operatorname{Sc}\tilde u_{\mathrm r}\bigr),
$$

and the axis is the normalised vector part.

### The Word

The four exponentials multiply in the order scale, phase, boost, rotor,

$$
\tilde Q=r\,e^{i\alpha}\,e^{i\frac{\psi}{2}\vec u_{\mathrm b}}\,e^{\frac{\theta}{2}\vec u_{\mathrm r}}.
$$

The table collects the data.

| factor | exponent | range | closed form | character |
|---|---|---|---|---|
| scale $r$ | $\ln r$ | $\mathbb{R}$ | $e^{\ln r}$ | central, non-compact, aperiodic |
| phase $\zeta$ | $i\alpha$ | $(-\frac{\pi}{2},\frac{\pi}{2}]$ | $\cos\alpha+i\sin\alpha$ | central, compact, period $2\pi$ |
| boost $\tilde U_{\mathrm b}$ | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\psi\ge0$, $\lvert\vec u_{\mathrm b}\rvert=1$ | $\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | Hermitian positive, non-compact, aperiodic |
| rotor $\tilde u_{\mathrm r}$ | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\lvert\vec u_{\mathrm r}\rvert=1$ | $\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | unitary, compact; the rotation has period $2\pi$ |

The two central factors commute with the two non-central ones and with each other. The boost and the rotor commute exactly when their axes are parallel or antiparallel:

$$
\Bigl[i\frac{\psi}{2}\vec u_{\mathrm b},\frac{\theta}{2}\vec u_{\mathrm r}\Bigr]
=\frac{i\psi\theta}{4}\,[\vec u_{\mathrm b},\vec u_{\mathrm r}]
=\frac{i\psi\theta}{2}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r},
$$

which vanishes exactly when $\vec u_{\mathrm b}\times\vec u_{\mathrm r}=0$, that is, when the axes are parallel or antiparallel, or one of the two parameters is zero. In that case, and only in that case, the four exponentials amalgamate into one:

$$
\tilde Q=\exp\Bigl(\ln r+i\alpha+\frac{\theta+i\psi}{2}\vec u\Bigr),
\qquad \vec u_{\mathrm b}=\vec u_{\mathrm r}=\vec u,
$$

with the complex angle $\frac{\theta+i\psi}{2}$ and $\vec u^{2}=-e_t$; for opposite axes, replace $\theta$ by $-\theta$. The right-hand side is the exponential of a single element, read through the complex cosine and sine. When the axes are not parallel, no single exponent of this shape exists, and the word stays a product.

## Existence and Uniqueness

**Theorem (the exponential polar decomposition).** Every invertible biquaternion $\tilde Q$ has a unique writing

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\tilde U_{\mathrm b}$ Hermitian positive of norm one, and $\tilde u_{\mathrm r}$ a unit real quaternion. Consequently it has the exponential writing above, with the rapidity $\psi\ge0$, the angle $\theta\in[0,2\pi]$, and the two axes; the axes are unique when $\psi>0$ and $\theta\notin\{0,2\pi\}$.

**Proof.** The algebraic statement is the theorem of *Modulus–Unit Polar Decomposition of Biquaternions*. For the exponential statement, write the unit factor as $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde U_{\mathrm b}$ Hermitian positive of norm one and $\tilde u_{\mathrm r}$ unitary of norm one. The matrix image of $\tilde U$ lies in $SL(2,\mathbb{C})$, and the two matrix images lie in the positive definite cone and in $SU(2)$; this is the global Cartan decomposition $SL(2,\mathbb{C})=P\cdot K$, which is unique because $P\cap K=\{e_t\}$. A Hermitian positive element of norm one is $\exp$ of a unique Hermitian traceless element, and a unitary element of determinant one is $\exp$ of an anti-Hermitian traceless element, with the angle $\theta\in[0,2\pi]$; the endpoint $\theta=2\pi$ is the central rotor $-1$, where the axis is undefined and the logarithm is not the principal one. The scale and the phase are the polar coordinates of the complex modulus, unique in the branch.

The theorem is the exponential form of the modulus–unit decomposition: the algebraic article gives the factors, and the Cartan decomposition gives the coordinates on the unit fibre. The count of parameters is

$$
\underbrace{1}_{\ln r}+\underbrace{1}_{\alpha}+\underbrace{1+2}_{\psi,\vec u_{\mathrm b}}+\underbrace{1+2}_{\theta,\vec u_{\mathrm r}}=8,
$$

the real dimension of $\mathbb{B}^{\times}$.

**Degeneracies.** The axis of the boost is undefined at $\psi=0$, where the boost is the identity, and the axis of the rotor is undefined at $\theta=0$, where the rotor is the identity, and at $\theta=2\pi$, where the rotor is $-e_t$ for every axis. These are the usual coordinate singularities of polar coordinates; the element itself is smooth there, and the word is unique. The angle $\theta=2\pi$ is the only point at which the rotor is central without being the identity, and it is the point the branch of the phase leaves to the rotor.

**The boundary.** The word is defined on the complement of the null cone. As an element approaches the cone, the scale vanishes and the rapidity diverges: the limit is a rank-one null element, either a complex multiple of a minimal idempotent or a nilpotent, treated in *Idempotents and the Boundary of the Polar Decomposition of Biquaternions*. The polar word has no limit at the boundary; it has boundary values, reached with $r\to0$ and $\psi\to\infty$ at the rate $re^{\psi/2}\to R$ with $0<R<\infty$.

## The Two Logarithms

### The Cartan Logarithm

The first logarithm is a **pair**, not an element. Write the unit factor as $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and put

$$
\tilde H=\operatorname{Log}\tilde U_{\mathrm b}=i\frac{\psi}{2}\vec u_{\mathrm b},
\qquad
\tilde K=\operatorname{Log}\tilde u_{\mathrm r}=\frac{\theta}{2}\vec u_{\mathrm r}.
$$

The pair $(\tilde H,\tilde K)$ is the **Cartan logarithm** of $\tilde U$. It is unique with the ranges of the theorem, except at the central rotor $-e_t$, where the axis is undefined. It consists of a Hermitian traceless element and an anti-Hermitian traceless element, and it satisfies

$$
\tilde U=e^{\tilde H}e^{\tilde K}.
$$

The name is the one of the Cartan decomposition: the Lie algebra of $SL(2,\mathbb{C})$ splits as

$$
\mathfrak{sl}(2,\mathbb{C})=\mathfrak{k}\oplus\mathfrak{p},
\qquad
\mathfrak{k}=\{\tilde X:\tilde X^{*}=-\tilde X,\ \operatorname{Sc}\tilde X=0\},
\qquad
\mathfrak{p}=\{\tilde X:\tilde X^{*}=\tilde X,\ \operatorname{Sc}\tilde X=0\},
$$

of real dimensions $3$ and $3$. The rotor exponent lies in $\mathfrak{k}$, the boost exponent in $\mathfrak{p}$, and the group decomposition $SL(2,\mathbb{C})=e^{\mathfrak p}e^{\mathfrak k}$ is global and unique. The full algebra splits as

$$
\mathbb{B}=\mathbb{R}e_t\ \oplus\ i\mathbb{R}e_t\ \oplus\ \mathfrak p\ \oplus\ \mathfrak k,
$$

with the scale exponent in the first summand, the phase exponent in the second, the boost exponent in the third and the rotor exponent in the fourth. This is the exponential reading of the four coordinate blocks of *The Polar Decomposition and Remarkable Subspaces*.

### The Single Logarithm

The second logarithm is an element. Since $\mathbb{B}\cong M_2(\mathbb{C})$ and every invertible complex matrix has a logarithm, the exponential

$$
\exp:\mathbb{B}\longrightarrow\mathbb{B}^{\times}
$$

is surjective. For every invertible $\tilde Q$ there is an element $\operatorname{Log}\tilde Q$ with

$$
\exp\bigl(\operatorname{Log}\tilde Q\bigr)=\tilde Q,
$$

and it is unique only after a branch is fixed. The principal branch is fixed by the eigenvalues: the matrix image has eigenvalues

$$
\lambda_\pm=Q_t\pm iB,\qquad B=\sqrt{Q_x^{2}+Q_y^{2}+Q_z^{2}},
$$

and the principal logarithm takes the arguments of $\lambda_\pm$ in $(-\pi,\pi]$. The eigenvalues may coincide, and then the matrix may fail to be diagonalisable; the logarithm still exists, and it is computed on the Jordan form, as the example below shows.

A single logarithm is related to the Cartan logarithm by

$$
\operatorname{Log}\tilde Q=\ln r+i\alpha+\operatorname{Log}\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)
$$

for a compatible choice of branches; the principal branch of $\tilde Q$ may differ from the sum by $2\pi i$ times an integer combination of the eigenprojections. The last term is a logarithm of the unit factor inside $\mathfrak{gl}(2,\mathbb{C})$, not inside $\mathfrak{sl}(2,\mathbb{C})$: its trace may be a nonzero multiple of $2\pi i$, and this trace obstruction is what makes the norm-one group not globally exponential even though the group of units is.

### The Defect

The sum of the four exponents is the **formal exponent**

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}.
$$

It is the element the quaternion case would call the logarithm. Here it is not one:

$$
\exp\bigl(\tilde Q_{\log}\bigr)\neq\tilde Q
\qquad\text{unless}\qquad
[\vec u_{\mathrm b},\vec u_{\mathrm r}]=0\quad\text{or}\quad\psi\theta=0.
$$

The defect is the Baker–Campbell–Hausdorff correction. To first order,

$$
\operatorname{Log}\bigl(e^{\tilde H}e^{\tilde K}\bigr)
=\tilde H+\tilde K+\tfrac12[\tilde H,\tilde K]+\cdots,
$$

and the first correction is again a boost, because

$$
\tfrac12[\tilde H,\tilde K]
=\frac{i\psi\theta}{4}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}
\in\mathfrak p .
$$

So the sum of a boost and a rotor exponent is corrected by another boost, and the true logarithm is not the sum of the four exponents. The correction vanishes exactly when the axes are parallel or antiparallel, or one of the two parameters vanishes, which is the amalgamation of the previous section. The higher terms are the iterated commutators; the series is the one of *Biquaternion Lie Group and Exponential Structure*, §*The Correspondence with the Lie Algebra*.

The defect is not a rounding effect. In the worked example below the four exponents sum to an element whose exponential misses the element by $0.54$ in the largest coefficient, while the true logarithm reproduces it to $2.2\times10^{-16}$.

## The Kernel and the Fibre

The exponential is not injective. Its kernel is the set of exponents that exponentiate to the identity. The elementary article computes it: $\exp(\tilde X)=e_t$ exactly when $\tilde X$ is diagonalisable over $\mathbb{C}$ and every eigenvalue lies in $2\pi i\mathbb{Z}$. In the algebra the kernel contains

| exponent | exponential | reason |
|---|---|---|
| $2\pi i\,e_t$ | $e_t$ | the complex period of the phase |
| $2\pi\vec u$, $\vec u^{2}=-e_t$ | $e_t$ | the period of the rotor, $\cos2\pi=1$ and $\sin2\pi=0$ |
| $\pi i\,e_t+\pi\vec u$ | $e_t$ | the two eigenvalues $\pi i(1\pm1)$ are multiples of $2\pi i$ |
| $2\pi i k\,e_t+2\pi j\vec u$ | $e_t$ | the sum of two commuting periods |

The kernel is **not a subgroup**. It is not closed under addition, because $\exp$ is not a homomorphism: the sum of two kernel elements need not lie in the kernel. It is a union of conjugacy classes of the diagonal matrices $\operatorname{diag}(2\pi i m,2\pi i n)$, and it meets the null cone: the element $\pi i e_t+\pi\vec e_z$ has norm zero and exponentiates to the identity.

The fibre over an element is not a coset of the kernel either. For an element with distinct eigenvalues $\lambda_\pm$ and eigenprojections $\Pi_\pm$, the logarithms are

$$
\operatorname{Log}\tilde Q+2\pi i\bigl(k\Pi_+ + l\Pi_-\bigr),
\qquad k,l\in\mathbb{Z},
$$

one integer lattice for each eigendirection. For a diagonalisable element with a repeated eigenvalue the fibre contains a continuous family of conjugates, because the two eigenvalues of the logarithm may differ by $2\pi i$; for a non-diagonalisable Jordan block it is discrete, one point for each choice of the logarithm of the scalar eigenvalue. The polar parameters do not cut the fibre of the exponential to one point: the four exponents sum to the formal exponent, which is not a logarithm. What they cut to one point, up to the degeneracies of the axes, is the fibre of the **word map** $(r,\alpha,\psi,\vec u_{\mathrm b},\theta,\vec u_{\mathrm r})\mapsto r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$: $r$ by positivity, $\alpha$ by the branch, $\psi$ by $\psi\ge0$, and $\theta$ by $[0,2\pi]$. The exponential polar decomposition is therefore a **section** of the word map, a global coordinate system on $\mathbb{B}^{\times}$; it is neither a section of the exponential nor a quotient.

## The Group Law

The product of two words is

$$
\bigl(r_1e^{i\alpha_1}e^{\tilde H_1}e^{\tilde K_1}\bigr)
\bigl(r_2e^{i\alpha_2}e^{\tilde H_2}e^{\tilde K_2}\bigr)
=r_1r_2\,e^{i(\alpha_1+\alpha_2)}\,e^{\tilde H_1}e^{\tilde K_1}e^{\tilde H_2}e^{\tilde K_2}.
$$

The central factors add. The non-central ones do not: the middle product $e^{\tilde K_1}e^{\tilde H_2}$ has to be re-split as a boost times a rotor, and the re-splitting is the Cartan decomposition of a product of two exponentials. The first correction is the commutator,

$$
e^{\tilde K_1}e^{\tilde H_2}
=e^{\tilde H_2+[\tilde K_1,\tilde H_2]+\cdots}e^{\tilde K_1+\cdots},
$$

so the rotor of the first word changes the boost of the second by a term in $\mathfrak p$: the boost is conjugated, not added. The rotor itself is unchanged at second order; its correction is of higher order. The parameters of the product are not the sums of the parameters.

The brackets of the two summands close as a **symmetric pair**:

| bracket | lies in | reading |
|---|---|---|
| $[\mathfrak k,\mathfrak k]$ | $\mathfrak k$ | two rotors compose to a rotor |
| $[\mathfrak p,\mathfrak p]$ | $\mathfrak k$ | two boosts compose to a boost times a rotor |
| $[\mathfrak k,\mathfrak p]$ | $\mathfrak p$ | the commutator of a rotor and a boost is a boost |

The first row is the subgroup $SU(2)$ of the rotor. The second is the Thomas–Wigner rotation: the product of two boosts is a boost times a rotor, and the residual rotor is the one computed in *The Polar Decomposition and Remarkable Subspaces*, §*The Boost Family and the Rotor Group*. The third is the statement that the boost set is a symmetric space and not a group: the commutator of an infinitesimal boost and an infinitesimal rotation is an infinitesimal boost, so the boost directions are stable under the adjoint action of the rotor, while the boost set itself is not closed under multiplication.

## The Matrix Picture

The matrix model turns the exponential into the matrix exponential, because $\mathsf M_2$ is a $\mathbb{C}$-algebra homomorphism:

$$
\mathsf M_2\bigl(\exp\tilde X\bigr)=\exp\bigl(\mathsf M_2(\tilde X)\bigr).
$$

The polar word becomes the polar decomposition of $\mathrm{GL}_2(\mathbb{C})$,

$$
\mathsf M_2(\tilde Q)=r\,e^{i\alpha}\,\mathsf M_2(\tilde U_{\mathrm b})\,\mathsf M_2(\tilde u_{\mathrm r}),
$$

with $\mathsf M_2(\tilde U_{\mathrm b})$ positive definite of determinant one and $\mathsf M_2(\tilde u_{\mathrm r})$ unitary of determinant one. The four exponents are the four summands of the decomposition of the Lie algebra

$$
\mathfrak{gl}_2(\mathbb{C})=\mathfrak{u}(2)\oplus\mathfrak{H},
\qquad
\mathfrak{u}(2)=\{X:X^{\dagger}=-X\},
\qquad
\mathfrak{H}=\{X:X^{\dagger}=X\},
$$

of real dimensions $4$ and $4$. The exponents of the scale and the boost lie in $\mathfrak H$, those of the phase and the rotor in $\mathfrak u(2)$; the central real line is the scale, the central imaginary line is the phase, and the traceless parts are the boost and the rotor.

| matrix object | algebra object | dimension | factor |
|---|---|---|---|
| positive determinant-one matrix | Hermitian positive unit-norm element | $3$ | boost |
| unitary determinant-one matrix | unit real quaternion | $3$ | rotor |
| positive real scalar | scale | $1$ | $r$ |
| unit complex scalar | phase | $1$ | $\zeta$ |

The exponential is surjective onto $\mathrm{GL}_2(\mathbb{C})$ because every invertible matrix has a logarithm, and it is not injective because the logarithm is multivalued. The determinant gives

$$
\det\mathsf M_2\bigl(\exp\tilde X\bigr)=\exp\bigl(\operatorname{tr}\mathsf M_2(\tilde X)\bigr)\neq0,
$$

so the image lies in the units, and the trace is the logarithmic scale of the determinant. The eigenvalues of $\mathsf M_2(\tilde Q)$ are $Q_t\pm iB$, and the Jordan type at $B=0$ decides the shape of the fibre: distinct eigenvalues give a two-dimensional lattice, a double eigenvalue with a nontrivial Jordan block gives a discrete family, and a scalar matrix gives a continuous family of conjugates.

## The Exponential Coordinates

The four parameters are coordinates on the group of units, and their ranges make the map a bijection up to the degeneracies of the axes. The coordinate lines are the four one-parameter families:

- the **scale line** $r\mapsto re^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a half-line, non-compact;
- the **phase circle** $\alpha\mapsto r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a circle of length $2\pi$ before the branch cuts it to $\pi$;
- the **boost hyperbola** $\psi\mapsto r e^{i\alpha}e^{i\frac{\psi}{2}\vec u_{\mathrm b}}\tilde u_{\mathrm r}$, a non-compact ray;
- the **rotor arc** $\theta\mapsto r e^{i\alpha}\tilde U_{\mathrm b}e^{\frac{\theta}{2}\vec u_{\mathrm r}}$, a great semicircle from $e_t$ to $-e_t$.

The topology is read from the polar decomposition, not from the word. The positive cone $P$ is homeomorphic to $\mathbb{R}^{3}$ and the rotor sphere $K=SU(2)$ is $S^{3}$, so

$$
SL(2,\mathbb{C})\simeq \mathbb{R}^{3}\times S^{3}.
$$

The group of units retracts onto $U(2)$, and the determinant splits $U(2)\cong U(1)\times SU(2)$ as a space, so

$$
\mathbb{B}^{\times}\simeq U(2)\cong S^{1}\times S^{3}.
$$

The branch of the modulus makes $\tilde Q\mapsto(\Rho,\tilde U)$ a bijection onto $\mathcal H\times SL(2,\mathbb{C})$, but not a homeomorphism: on the cut the phase jumps by the factor $-1$ and the rotor changes sign, so the circular direction is carried by the phase, and the branch coordinate does not see it continuously. The fundamental group of the group of units is therefore $\mathbb{Z}$, carried by the phase alone; the rotor contributes the simply connected factor $S^{3}$, and the scale and the boost are the two non-compact directions. This is the exponential reading of the homotopy statement of *Modulus–Unit Polar Decomposition of Biquaternions*, §*The Group of Units and the Unitary Group*.

The **conformal factor** of the action is also read in the coordinates. The sandwich of $\tilde Q$ multiplies the quadratic form of either half by

$$
r^{4}=e^{4\ln r}=\bigl\lvert\langle\tilde Q\rangle_{\natural}\bigr\rvert^{2},
$$

so lengths are multiplied by $r^{2}=\lvert\langle\tilde Q\rangle_{\natural}\rvert$. The scale exponent is thus a quarter of the logarithm of the conformal factor: the form scales by $e^{4\ln r}$ and lengths by $e^{2\ln r}$. The phase, the boost and the rotor are isometries of the form; only the scale moves it.

## Worked Example

### The Element and Its Four Factors

Take the element of *Modulus–Unit Polar Decomposition of Biquaternions*,

$$
\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y .
$$

Its norm is $2i$, its modulus is $\Rho=1+i$, and

$$
r=\sqrt{2},\qquad \alpha=\frac{\pi}{4},\qquad
\tilde U=e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y .
$$

The Hermitian element and the two non-central factors are

$$
\tilde U\tilde U^{*}=2e_t-i\vec e_x+i\vec e_y+i\vec e_z,\qquad
\tilde U_{\mathrm b}=\frac{3e_t-i\vec e_x+i\vec e_y+i\vec e_z}{\sqrt{6}},\qquad
\tilde u_{\mathrm r}=\sqrt{\frac{2}{3}}\,e_t+\frac{1}{\sqrt{6}}\vec e_x+\frac{1}{\sqrt{6}}\vec e_y .
$$

The parameters of the two exponentials are

$$
\psi=2\operatorname{arcosh}\frac{3}{\sqrt{6}}=\operatorname{arcosh}2=\ln(2+\sqrt{3})=1.3169578969,
\qquad
\vec u_{\mathrm b}=\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt{3}},
$$

and

$$
\theta=2\arccos\sqrt{\frac{2}{3}}=\arccos\frac{1}{3}=1.2309594173,
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt{2}} .
$$

The two closed forms reproduce the factors:

$$
e^{i\frac{\psi}{2}\vec u_{\mathrm b}}
=\sqrt{\frac{3}{2}}\,e_t+\frac{i}{\sqrt{6}}\bigl(-\vec e_x+\vec e_y+\vec e_z\bigr)
=\tilde U_{\mathrm b},
\qquad
e^{\frac{\theta}{2}\vec u_{\mathrm r}}
=\sqrt{\frac{2}{3}}\,e_t+\frac{1}{\sqrt{6}}\bigl(\vec e_x+\vec e_y\bigr)
=\tilde u_{\mathrm r},
$$

each to $10^{-16}$ in the four coefficients. The word is therefore

$$
\tilde Q=\sqrt{2}\,e^{i\frac{\pi}{4}}\,
e^{i\frac{1.3169578969}{2}\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt{3}}}\,
e^{\frac{1.2309594173}{2}\frac{\vec e_x+\vec e_y}{\sqrt{2}}} .
$$

### The Two Logarithms

The four exponents sum to the formal exponent

$$
\tilde Q_{\log}
=0.3465735903+0.7853981634\,i
+\bigl(0.4352098757-0.3801729982\,i\bigr)\vec e_x
+\bigl(0.4352098757+0.3801729982\,i\bigr)\vec e_y
+0.3801729982\,i\,\vec e_z .
$$

Its exponential is **not** the element: the largest coefficient of $\exp(\tilde Q_{\log})-\tilde Q$ is $0.5425679115$. The failure is the commutator of the boost and the rotor, not a rounding effect.

The true logarithm is much simpler, because the vector part of $\tilde Q$ is null:

$$
\langle\vec Q\rangle_{\natural}=Q_x^{2}+Q_y^{2}+Q_z^{2}=1+i^{2}=0 .
$$

So $\tilde Q=(1+i)(e_t+\vec N)$ with $\vec N=\frac{1}{1+i}(\vec e_x+i\vec e_y)$ and $\vec N^{2}=0$. The logarithm of a unipotent element truncates,

$$
\operatorname{Log}\tilde Q
=\ln\sqrt{2}+i\frac{\pi}{4}+\vec N
=0.3465735903+0.7853981634\,i
+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y ,
$$

and

$$
\exp\bigl(\operatorname{Log}\tilde Q\bigr)=\tilde Q
$$

to $2.2\times10^{-16}$ in every coefficient. The single logarithm differs from the formal exponent by at most $0.3802$ in a coefficient, and the formal exponent misses the element by $0.54$; the difference is the Baker–Campbell–Hausdorff defect of the aligned formula.

The table collects the values.

| quantity | value |
|---|---|
| $r$ | $\sqrt{2}=1.4142135624$ |
| $\alpha$ | $\pi/4=0.7853981634$ |
| $\psi$ | $\ln(2+\sqrt{3})=1.3169578969$ |
| $\vec u_{\mathrm b}$ | $(-\vec e_x+\vec e_y+\vec e_z)/\sqrt{3}$ |
| $\theta$ | $\arccos(1/3)=1.2309594173$ |
| $\vec u_{\mathrm r}$ | $(\vec e_x+\vec e_y)/\sqrt{2}$ |
| $\exp(\tilde Q_{\log})-\tilde Q$ | $0.5425679115$ in the largest coefficient |
| $\exp(\operatorname{Log}\tilde Q)-\tilde Q$ | $2.2\times10^{-16}$ in every coefficient |

The example is the one of the algebraic article, so the four factors agree with the table there. It is also the simplest case in which the two logarithms can be compared: the vector part is null, the matrix has a single eigenvalue and a nontrivial Jordan block, and the logarithm is nevertheless unique once the scalar branch is fixed.

## Summary

Every invertible biquaternion is a product of four exponentials,

$$
\tilde Q=r\,e^{i\alpha}\,e^{i\frac{\psi}{2}\vec u_{\mathrm b}}\,e^{\frac{\theta}{2}\vec u_{\mathrm r}},
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and unit axes. The writing is unique, and its four parameters are coordinates on $\mathbb{B}^{\times}$: one real scale, one phase angle, one rapidity and one angle, with two axes. The scale and the phase are central; the boost is Hermitian positive of norm one; the rotor is a unit real quaternion.

The boost and the rotor exponents commute exactly when the axes are parallel or antiparallel, or one of the two parameters vanishes, and only then do the four exponentials amalgamate into one, with the complex angle $\frac{\theta+i\psi}{2}$ (with $\theta$ replaced by $-\theta$ for opposite axes). In general the sum of the four exponents is not a logarithm of the element: the single logarithm differs from it by the Baker–Campbell–Hausdorff correction, whose first term is $\frac{i\psi\theta}{4}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$, a boost. A single logarithm nevertheless exists, because $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$ is exponential; it is not unique, and the four parameters select a canonical word, not a canonical logarithm.

The kernel of the exponential is the set of diagonalisable elements with eigenvalues in $2\pi i\mathbb{Z}$; it contains $2\pi i e_t$, $2\pi\vec u$ for every root of $-1$, and the null element $\pi i e_t+\pi\vec u$. It is not a subgroup, and the fibre of the exponential is not a coset of it. The group law is the bracket of a symmetric pair: two rotors compose to a rotor, two boosts to a boost times a rotor, and the bracket of a rotor and a boost lies in the boost directions. The exponential coordinates exhibit the homotopy type $S^{1}\times S^{3}$ of the group of units, with the phase carrying the fundamental group, and the conformal factor of the sandwich is $r^{4}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=r e^{i\alpha}e^{i\frac{\psi}{2}\vec u_{\mathrm b}}e^{\frac{\theta}{2}\vec u_{\mathrm r}}$ | the exponential polar decomposition |
| $r=e^{\ln r}$ | the scale, positive and central |
| $\zeta=e^{i\alpha}$ | the central phase, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$ |
| $\tilde U_{\mathrm b}=e^{i\frac{\psi}{2}\vec u_{\mathrm b}}$ | the boost, Hermitian positive of norm one |
| $\tilde u_{\mathrm r}=e^{\frac{\theta}{2}\vec u_{\mathrm r}}$ | the rotor, a unit real quaternion |
| $\psi$, $\vec u_{\mathrm b}$ | rapidity and axis of the boost |
| $\theta$, $\vec u_{\mathrm r}$ | angle and axis of the rotor |
| $\Rho=re^{i\alpha}$ | the complex modulus, $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$ |
| $\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ | the formal exponent, not a logarithm in general |
| $(\tilde H,\tilde K)$ | the Cartan logarithm, $\tilde H=i\frac{\psi}{2}\vec u_{\mathrm b}$, $\tilde K=\frac{\theta}{2}\vec u_{\mathrm r}$ |
| $\operatorname{Log}\tilde Q$ | a single logarithm, $\exp(\operatorname{Log}\tilde Q)=\tilde Q$ |
| $\mathfrak k$, $\mathfrak p$ | the anti-Hermitian and Hermitian traceless summands of $\mathfrak{sl}(2,\mathbb{C})$ |
| $B=\sqrt{Q_x^{2}+Q_y^{2}+Q_z^{2}}$ | the complex norm of the vector part |
| $\mathsf M_2$ | the matrix model, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ |
| $P$, $K$ | the positive cone and $SU(2)$ in $SL(2,\mathbb{C})=P\cdot K$ |

## Further Reading

- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the algebraic word, the modulus–unit writing, the four factors and the theorem of existence and uniqueness.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm, the closed forms, the kernel and the two real directions.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the exponential map of the group of units, the failure of surjectivity on the norm-one group and the Baker–Campbell–Hausdorff series.
- [Exponential Polar Decomposition of Quaternions](exponential-polar-decomposition-of-quaternions.html), for the quaternion case, where the four factors reduce to two and the exponents amalgamate.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the Hermitian positive and unitary factors and the Cartan decomposition of the exponents.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the four exponents read against the four coordinate blocks, and for the product of two boosts.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the sandwich, its kernel and the matrices of the Lorentz action.
- [Idempotents and the Boundary of the Polar Decomposition of Biquaternions](idempotents-and-the-boundary-of-the-polar-decomposition-of-biquaternions.html), for the null cone, where the rapidity diverges and the word has no limit.
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html), for the norm, the zero divisors and the two eigenvalue branches.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the root convention and the branch of the argument.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y, for the polar decomposition of a complexified quaternion.
