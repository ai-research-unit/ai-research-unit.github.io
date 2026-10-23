# __Reduced Biquaternion Elementary Functions__

## Introduction

This article defines the elementary functions of a reduced biquaternion variable: the exponential, the logarithm, the powers and roots, and the trigonometric and hyperbolic functions. Each function is defined once, its basic properties are recorded, and its value is read on the two eigenvalues.

The article rests on *Eigenbasis of a Reduced Biquaternion*, §*The Spectrum and the Characteristic Polynomial*, §*The Eigenprojections* and §*Powers, Polynomial Calculus, and the Group of Units*: the eigenvalues $\lambda_1=Q_+$ and $\lambda_2=Q_-$, the central idempotents $\Pi_\pm$, the decomposition $\breve Q=\lambda_1\Pi_++\lambda_2\Pi_-$, and the spectral calculus. They are collected in §*The Eigenvalue Data* and used here without proof. The algebra and its bar are *Introduction to the Algebra of the Reduced Biquaternions*; the norm and the unit criterion are *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the zero divisors are *Zero Divisors of the Algebra of the Reduced Biquaternions*.

Every claim is either proved or stated as a definition. Complex analysis is assumed: holomorphic functions, power series, the complex exponential and logarithm, and the branch structure of the argument are used throughout.

**Plan.** The spectral setting is recalled first, with the two regimes and the Idempotent Principle (§*The Spectral Setting*). The exponential and the logarithm follow, with their kernels, images and fibres (§*The Exponential*, §*The Logarithm*); the powers and roots follow from the logarithm (§*Powers and Roots*); the trigonometric and hyperbolic functions and their inverses follow (§*The Trigonometric and Hyperbolic Functions*); the relations to the complex line and the split-complex plane close the theory (§*Relations to the Neighbouring Cases*). The results are collected in tables in §*Summary*, including the comparison with the split-complex and biquaternion cases.

Every numerical value displayed below was recomputed in double precision.

**Notation.** A reduced biquaternion is written $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$ and $j^{2}=1$. The bar is $\bar{\breve Q}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$, and the norm is $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$.

## The Spectral Setting

### The Eigenvalue Data

The spectral data are those of *Eigenbasis of a Reduced Biquaternion*, §*The Spectrum and the Characteristic Polynomial*, §*The Eigenprojections* and §*Powers, Polynomial Calculus, and the Group of Units*. The definitions, the decomposition and their proofs are there; this article uses them and does not repeat them. The table collects the results in the form used below.

| Quantity | Value |
|---|---|
| Spectrum | $\sigma(\breve Q)=\{\lambda_1,\lambda_2\}$ |
| Eigenvalues | $\lambda_1=Q_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $\lambda_2=Q_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$, central, primitive, orthogonal, complete |
| Eigenvalue decomposition | $\breve Q=\lambda_1\Pi_++\lambda_2\Pi_-$ |
| Characteristic polynomial | $p_{\breve Q}(X)=(X-\lambda_1)(X-\lambda_2)$ |
| Distinctness | $\lambda_1\neq\lambda_2$ exactly when $Q_{\blacktriangledown}\neq0$ |
| Norm | $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=\lambda_1\lambda_2$ |
| Unit criterion | $\breve Q$ is a unit exactly when $\lambda_1\lambda_2\neq0$ |
| Polynomial calculus | $f(\breve Q)=f(\lambda_1)\Pi_++f(\lambda_2)\Pi_-$ for every polynomial $f$ |
| Lattice | $\ker\exp=2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)$ |

Multiplication is componentwise in the idempotent basis,
$$
\bigl(Q_+\Pi_++Q_-\Pi_-\bigr)\bigl(Q_{2+}\Pi_++Q_{2-}\Pi_-\bigr)
=Q_+Q_{2+}\Pi_++Q_-Q_{2-}\Pi_-,
$$
and the reduced norm is $\langle\breve Q\rangle_{\mathrm{ts}}=\lambda_1\lambda_2$. The bar is $\bar{\breve Q}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$, and the squared Euclidean norm is $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$.

### The Regimes

The characteristic polynomial is $(X-\lambda_1)(X-\lambda_2)$, and the algebra has two spectral regimes; the distinct regime splits into the units and the zero divisors. The table gives what each regime changes for the functions below; the spectral data of each regime are those of *Eigenbasis of a Reduced Biquaternion*, §*Degenerate Regimes*.

| Regime | Condition | Consequence for the functions |
|---|---|---|
| Distinct, not a zero divisor | $Q_{\blacktriangledown}\neq0$, $\lambda_1\lambda_2\neq0$ | $\log$ is defined on the unit group; the powers and roots read two nonzero eigenvalues |
| Zero divisor | $Q_{\blacktriangledown}\neq0$, $\lambda_1\lambda_2=0$ | $\exp$ does not reach it, so $\log$ is undefined; a trigonometric or hyperbolic value may be a zero divisor |
| Scalar | $Q_{\blacktriangledown}=0$ | one eigenvalue; the two-term spectral form is a non-unique refinement |

The algebra is **reduced**: if $\breve X^{2}=0$, both eigenvalues of $\breve X$ are zero, hence $\breve X=0$. There is no nilpotent regime, in contrast with the biquaternions. The distinct regime splits into the units and the zero divisors according to whether the norm vanishes, and the scalar regime is the only spectral degeneration. In the scalar regime the two-term spectral form is a non-unique refinement of the one-term decomposition; the functions below are unaffected, because their spectral form is continuous in $\lambda_1,\lambda_2$.

### The Idempotent Principle

Every elementary function of this article is the spectral function of its complex counterpart. The rule is stated once.

**Theorem (Idempotent Principle).** Let $f(x)=\sum c_nx^n$ be a complex power series with radius of convergence $\rho$, and let $\lvert\lambda_1\rvert,\lvert\lambda_2\rvert<\rho$. Then

$$
\boxed{\;
f(\breve Q)=f(\lambda_1)\Pi_++f(\lambda_2)\Pi_-
\;}.
$$

**Proof.** The polynomial calculus of *Eigenbasis of a Reduced Biquaternion*, §*Powers, Polynomial Calculus, and the Group of Units*, gives $\breve Q^n=\lambda_1^n\Pi_++\lambda_2^n\Pi_-$ for every $n\geq0$. Summing termwise and using $\Pi_+^2=\Pi_+$, $\Pi_-^2=\Pi_-$, $\Pi_+\Pi_-=0$ and $\Pi_++\Pi_-=1$ gives the display; the rearrangement is legitimate because the series converges absolutely in each component. For a function defined by an integral, an inverse or another complex formula, the display is the definition of its reduced biquaternion extension, and the value is defined exactly when both eigenvalue expressions are defined.

This is the **Idempotent Principle** of the algebra, and it is the exact analogue of *Split-Complex Elementary Functions*, §*The Idempotent Principle*, with two real eigenvalues replaced by two complex ones. It is the only rule the rest of the article uses.

The rule explains both structural facts of the algebra. Multiplication is commutative, so the functional equations hold for all arguments, with no ordering correction. And every identity between elementary functions that holds in the complex plane holds after the substitution $\lambda_i$ in both components.

## The Exponential

### Definition

The **reduced biquaternion exponential** is defined for $\breve Q\in\mathbb{B}_{\mathrm{r}}$ by the power series

$$
\exp\breve Q=\sum_{n=0}^{\infty}\frac{\breve Q^{n}}{n!}.
$$

The series converges absolutely in the Euclidean norm for every $\breve Q$. The function is entire, and it satisfies

$$
\exp(\breve Q_1+\breve Q_2)=\exp\breve Q_1\,\exp\breve Q_2,\qquad \exp 0=1,\qquad
d\exp_{\breve Q}(\breve H)=\exp(\breve Q)\,\breve H.
$$

The functional equation holds for **all** arguments because the algebra is commutative; no ordering correction is needed. The derivative follows from $\exp(\breve Q+t\breve H)=\exp\breve Q\,\exp(t\breve H)$ and $\exp(t\breve H)=1+t\breve H+O(t^{2})$.

### The Closed Form

By the Idempotent Principle applied to the exponential series,

$$
\boxed{\exp\breve Q=\exp(\lambda_1)\Pi_++\exp(\lambda_2)\Pi_-
=\frac{\exp(\lambda_1)+\exp(\lambda_2)}{2}+\frac{\exp(\lambda_1)-\exp(\lambda_2)}{2}j}.
$$

Since $\lambda_1+\lambda_2=2Q_{\blacktriangle}$ and $\lambda_1-\lambda_2=2Q_{\blacktriangledown}$, this is the **reduced Euler formula**

$$
\exp(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\exp(Q_{\blacktriangle})\bigl(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown}\bigr).
$$

It is the bridge between the exponential and the trigonometric and hyperbolic functions. In particular,

$$
\exp(i\theta)=\cos\theta+i\sin\theta,\qquad
\exp(ij\beta)=\cos\beta+ij\sin\beta,\qquad
\exp(j\phi)=\cosh\phi+j\sinh\phi.
$$

The first two are the elliptic directions, the third the hyperbolic direction.

### The Kernel and the Image

By the spectral formula, $\exp\breve Q_{\log}=1$ exactly when both eigenvalues of $\breve Q_{\log}$ lie in $2\pi i\mathbb{Z}$. Hence

$$
\ker\exp=2\pi i\bigl(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-\bigr)
=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}.
$$

In particular $\exp(\breve Q+2\pi i)=\exp\breve Q$ and $\exp(\breve Q+\pi i(1+j))=\exp\breve Q$. The scalar period $2\pi i$ and the split period $2\pi ij$ generate the sublattice of index two on which the two integer coefficients have the same parity; the period $\pi i(1+j)$ is half of their sum.

| Quantity | Value |
|---|---|
| Kernel | $2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^{2}$ |
| Image | the unit group $\mathbb{B}_{\mathrm{r}}^{\times}=\{\breve Q:\lambda_1\lambda_2\neq0\}$ |
| Periods | the kernel |
| Injective | no |
| Surjective onto the image | yes |

**Example.** For $\breve Q=j\ln2$ the closed form gives

$$
\exp(j\ln2)=\cosh(\ln2)+j\sinh(\ln2)=\tfrac54+\tfrac34 j,
$$

that is $1.25+0.75j$. This is the point of the future hyperbola at boost $\ln2$.

### Properties

| Property | Statement |
|---|---|
| Multiplicativity | $\exp(\breve Q_1+\breve Q_2)=\exp\breve Q_1\,\exp\breve Q_2$ for all $\breve Q_1,\breve Q_2$ |
| Non-vanishing | $\exp\breve Q$ is a unit for every $\breve Q$ |
| Norm | $\langle\exp\breve Q\rangle_{\mathrm{ts}}=\exp(2Q_{\blacktriangle})=\exp(\lambda_1+\lambda_2)$ |
| Derivative | $d\exp_{\breve Q}(\breve H)=\exp(\breve Q)\,\breve H$ |
| Injective | no; the kernel is the period lattice |
| Periods | the kernel $2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)$ |

## The Logarithm

### Definition

A **logarithm** of a unit $\breve Q$ is an element $\breve Q_{\log}$ with $\exp\breve Q_{\log}=\breve Q$. By the Idempotent Principle, the equation is solved independently in each idempotent component:

$$
\breve Q_{\log}=\log(\lambda_1)\Pi_++\log(\lambda_2)\Pi_-,
$$

where $\log(\lambda_1)$ and $\log(\lambda_2)$ are any complex logarithms of the two eigenvalues. Conversely every such choice gives a logarithm, because $\exp$ acts on each component by the complex exponential. The definition is an equation, not a formula; the eigenvalue decomposition supplies the formula.

The element and its logarithm carry two different pairs of complex coordinates, and they must not be mixed. By the coefficient rule of *Conventions in Mathematics*, a prime marks the imaginary coordinate of a complex coefficient:

$$
\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown},\qquad
\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown},
$$

$$
Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle},\quad
Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown},\qquad
Q_{\log\blacktriangle}=q_{\log\blacktriangle}+iq'_{\log\blacktriangle},\quad
Q_{\log\blacktriangledown}=q_{\log\blacktriangledown}+iq'_{\log\blacktriangledown}.
$$

The double subscript is a label, not an operation: $q_{\log\blacktriangle}$ is the real part of the scalar coefficient $Q_{\log\blacktriangle}$ of the logarithm, not the logarithm of the coefficient $Q_{\blacktriangle}$.

### The Scalar Part

Let $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ be a logarithm of $\breve Q$. Taking reduced norms in $\exp\breve Q_{\log}=\breve Q$ gives
$$
\langle\breve Q\rangle_{\mathrm{ts}}
=\langle\exp\breve Q_{\log}\rangle_{\mathrm{ts}}
=\exp(2Q_{\log\blacktriangle}).
$$
Hence
$$
2Q_{\log\blacktriangle}=\operatorname{Log}(\lambda_1\lambda_2)+2\pi i m,
$$
so the scalar coefficient is fixed by the norm up to $\pi i$; its imaginary part is fixed modulo $\pi$, and the split coefficient carries the remaining integer.

### The Eigenvalue Formula

In the basis $1,j$ the spectral logarithm is

$$
Q_{\log\blacktriangle}=\frac{\log(\lambda_1)+\log(\lambda_2)}{2},\qquad
Q_{\log\blacktriangledown}=\frac{\log(\lambda_1)-\log(\lambda_2)}{2},
$$

and therefore

$$
\breve Q_{\log}=\frac{\log(\lambda_1)+\log(\lambda_2)}{2}
+j\,\frac{\log(\lambda_1)-\log(\lambda_2)}{2}.
$$

This is the **global result**: it holds for every unit $\breve Q$ and every choice of the complex logarithm in each eigenvalue. Substitution into the reduced Euler formula recovers $\breve Q$.

A logarithm exists exactly when both eigenvalues are nonzero, that is exactly when $\breve Q$ is a **unit**. The general solution is

$$
\breve Q_{\log}=\operatorname{Log}\breve Q+2\pi i k+\pi i(1+j)l,\qquad k,l\in\mathbb{Z},
$$

with the **principal logarithm**

$$
\boxed{\;
\operatorname{Log}\breve Q=\frac{\operatorname{Log}(\lambda_1)+\operatorname{Log}(\lambda_2)}{2}
+j\,\frac{\operatorname{Log}(\lambda_1)-\operatorname{Log}(\lambda_2)}{2}
\;},
$$

where $\operatorname{Log}$ on the right is the principal complex logarithm, with argument in $(-\pi,\pi]$.

### The Coordinates of a Logarithm

For the principal branch, taking the real and imaginary parts of the two coefficients gives the four real components of the logarithm.

| Component | Name | Value from $\lambda_1,\lambda_2$ | Value in $(\rho,\phi,\alpha,\beta)$ |
|---|---|---|---|
| $q_{\log\blacktriangle}$ | logarithmic scale | $\tfrac12\ln\lvert \lambda_1\lambda_2\rvert=\tfrac12\ln\lvert\langle\breve Q\rangle_{\mathrm{ts}}\rvert$ | $\ln\rho$ |
| $q'_{\log\blacktriangle}$ | scalar phase | $\tfrac12\bigl(\operatorname{Arg}(\lambda_1)+\operatorname{Arg}(\lambda_2)\bigr)$ | $\alpha$ |
| $q_{\log\blacktriangledown}$ | boost | $\tfrac12\ln\lvert \lambda_1/\lambda_2\rvert$ | $\phi$ |
| $q'_{\log\blacktriangledown}$ | split phase | $\tfrac12\bigl(\operatorname{Arg}(\lambda_1)-\operatorname{Arg}(\lambda_2)\bigr)$ | $\beta$ |

Here $\rho=\sqrt{\lvert \lambda_1\lambda_2\rvert}=\sqrt{\lvert\langle\breve Q\rangle_{\mathrm{ts}}\rvert}$ and $\operatorname{Arg}$ is the principal argument in $(-\pi,\pi]$. For another branch, the pair $(\alpha,\beta)$ is shifted by a lattice vector. The logarithm is the sum of the four basis terms,

$$
\breve Q_{\log}=q_{\log\blacktriangle}+jq_{\log\blacktriangledown}+iq'_{\log\blacktriangle}+ijq'_{\log\blacktriangledown}
=\ln\rho+j\phi+i\alpha+ij\beta,
$$

and the exponential reassembles them:

$$
\breve Q=\exp\breve Q_{\log}=\rho\bigl(\cosh\phi+j\sinh\phi\bigr)\bigl(\cos\alpha+i\sin\alpha\bigr)\bigl(\cos\beta+ij\sin\beta\bigr).
$$

The component $q_{\log\blacktriangle}=\ln\rho$ sets the overall size, $q_{\log\blacktriangledown}=\phi$ the relative scale of the two eigenvalues, and the two primed components are the phases $\alpha$ and $\beta$.

**Example.** For $\breve Q=3+4i+j(1-i)$ the coefficients are $Q_{\blacktriangle}=3+4i$ and $Q_{\blacktriangledown}=1-i$, so $\lambda_1=4+3i$ and $\lambda_2=2+5i$. The principal complex logarithms are

$$
\operatorname{Log}(4+3i)=1.6094379+0.6435011\,i,\qquad
\operatorname{Log}(2+5i)=1.6836479+1.1902899\,i,
$$

so

$$
\operatorname{Log}\breve Q=1.6465429+0.9168955\,i-0.0371050\,j-0.2733944\,ij.
$$

Exponentiating gives $3+4i+j(1-i)$ up to rounding. The general logarithm adds $2\pi i k+\pi i(1+j)l$.

### The Domain and the Fibre

The logarithm exists on the whole unit group and is never unique. The general solution above is a coset of the kernel, and the kernel is a rank-two lattice.

| Quantity | Value |
|---|---|
| Domain | the units $\mathbb{B}_{\mathrm{r}}^{\times}=\{\breve Q:\lambda_1\lambda_2\neq0\}$ |
| Fibre over a point | $\operatorname{Log}\breve Q+\ker\exp$, a coset of $\mathbb{Z}^{2}$ |
| Kernel | $2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$ |
| Principal domain | $\lvert\operatorname{Im}\lambda_1\rvert\le\pi$ and $\lvert\operatorname{Im}\lambda_2\rvert\le\pi$, boundary half-open |
| Existence | always, on the units |

The fibre does not shrink in the scalar regime. Even when $\lambda_1=\lambda_2$, the two eigenvalue logarithms may be chosen independently, and a difference of $2\pi i$ between them produces a nonzero split coefficient $\pi i(k-l)$ in the logarithm. The scalar regime of the algebra is not the scalar case of the biquaternion logarithm: here the centraliser is the whole algebra in both regimes, because the algebra is commutative, and the two integers survive.

### The Principal Logarithm

The principal logarithm is defined on the whole unit group by the formula with the principal argument in each eigenvalue. It is real-analytic on the complement of the two walls

$$
W_{+}=\{\lambda_1\in(-\infty,0)\},\qquad W_{-}=\{\lambda_2\in(-\infty,0)\},
$$

each of real dimension three, and it is discontinuous across them. A branch that continued analytically across a wall would have to continue by a period and would not be single-valued. The walls are the exact analogue of the negative real axis of $\mathbb{C}$: there is one wall for each eigenvalue, and the jump across $W_{+}$ is $\pi i(1+j)$, across $W_{-}$ is $\pi i(1-j)$, both kernel elements.

The principal logarithm is not defined at $\lambda_1=0$ or $\lambda_2=0$, which are the zero divisors. On the unit group it is defined everywhere, including on the walls, where continuity fails but the inverse identity holds.

A single-valued branch exists on a domain when each eigenvalue lies in a simply connected domain of $\mathbb{C}^{\times}$. The maximal domains are the complements of rays in the two eigenvalues, and the principal branch uses the negative real ray in both. No single-valued branch exists on the whole unit group, because the unit group has fundamental group $\mathbb{Z}^{2}$; the obstruction is the kernel lattice, not a failure of local invertibility. The exponential is a covering map onto the unit group, and the logarithm is its multivalued inverse.

**Example.** For $\breve Q=-1$ the principal logarithm is $i\pi$, the upper endpoint of the first phase. Approaching $-1$ through $\lambda_1$ in the upper half-plane gives phase $\pi$; approaching through the lower half-plane gives phase $-\pi$. The two limits differ by $2\pi i$, so the principal branch cannot be continued continuously across $W_{+}$. The other eigenvalue produces the same phenomenon on $W_{-}$.

### The Principal Domain

Let $\mu_1,\mu_2$ be the eigenvalues of $\breve Q_{\log}$ and let
$$
D=\bigl\{\breve Q_{\log}:\lvert\operatorname{Im}\mu_1\rvert\le\pi,\ \lvert\operatorname{Im}\mu_2\rvert\le\pi\bigr\},
$$
with the boundary taken half-open. In the coordinates $(q'_{\log\blacktriangle},q'_{\log\blacktriangledown})$ this is the diamond
$$
\lvert q'_{\log\blacktriangle}+q'_{\log\blacktriangledown}\rvert\le\pi,
\qquad
\lvert q'_{\log\blacktriangle}-q'_{\log\blacktriangledown}\rvert\le\pi.
$$
The exponential maps $D$ bijectively onto the unit group, and $\operatorname{Log}$ is its inverse. The interior maps onto the complement of the two walls, where the principal logarithm is real-analytic.

### The Two Compositions

The word "inverse" covers two identities, and the exponential and the logarithm satisfy them in opposite strengths.

| Identity | Holds | Example |
|---|---|---|
| $\exp(\operatorname{Log}\breve Q)=\breve Q$ | always, on the units | $\breve Q=3+4i+j(1-i)$ |
| $\operatorname{Log}(\exp\breve Q_{\log})=\breve Q_{\log}$ | exactly in the principal domain $D$ | $\breve Q_{\log}=i\pi$ |
| $\operatorname{Log}(\exp\breve Q_{\log})=\breve Q_{\log}$ modulo the kernel | always | $\breve Q_{\log}=i\pi(1+j)$ gives $0$ |

**Right inverse.** For every unit $\breve Q$,

$$
\exp(\operatorname{Log}\breve Q)=\breve Q.
$$

**Proof.** In the eigenvalue coordinates, $\exp(\operatorname{Log}(\lambda_i))=\lambda_i$ by the complex identity, and the two components reassemble.

**Left inverse, up to the kernel.** For every $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$,

$$
\operatorname{Log}(\exp\breve Q_{\log})=\breve Q_{\log}
$$

exactly when $\breve Q_{\log}$ lies in the principal diamond $D$ of §*The Domain and the Fibre*, with the boundary taken half-open. For a general $\breve Q_{\log}$, the two sides differ by an element of the kernel:

$$
\operatorname{Log}(\exp\breve Q_{\log})=\breve Q_{\log}+2\pi i k+\pi i(1+j)l
$$

for the integers that bring the two phases into the principal diamond.

**Proof.** Both sides are logarithms of $\exp\breve Q_{\log}$, so they differ by an element of $\ker\exp$. The principal value is the representative whose two phases lie in the half-open diamond.

The asymmetry is the content of the word "multivalued". The exponential forgets two integers, one for each eigenvalue; the principal logarithm chooses one representative. The split-complex exponential forgets none, and the complex exponential forgets one.

### The Derivative

On the complement of the walls the principal logarithm is differentiable, and its derivative is left multiplication by $\breve Q^{-1}$:

$$
d\operatorname{Log}_{\breve Q}(\breve H)=\breve Q^{-1}\breve H.
$$

In the eigenvalue coordinates,

$$
\bigl(d\operatorname{Log}_{\breve Q}\breve H\bigr)_{+}=\frac{H_{+}}{\lambda_1},\qquad
\bigl(d\operatorname{Log}_{\breve Q}\breve H\bigr)_{-}=\frac{H_{-}}{\lambda_2}.
$$

**Proof.** The exponential is a local biholomorphism with derivative left multiplication by $\exp\breve Q_{\log}=\breve Q$; the inverse function theorem gives the derivative of the inverse as left multiplication by $\breve Q^{-1}$.

**Chain rule check.** Differentiating $\exp(\operatorname{Log}\breve Q)=\breve Q$ gives

$$
\exp(\operatorname{Log}\breve Q)\,d\operatorname{Log}_{\breve Q}=\mathrm{id},
$$

hence $d\operatorname{Log}_{\breve Q}=\breve Q^{-1}$. The same computation applies to any branch of the logarithm, and it shows that all branches have the same derivative.

The formula is the exact analogue of $\operatorname{Log}'Q=1/Q$ in $\mathbb{C}$, applied twice. The logarithm is holomorphic in each eigenvalue, and the two Wirtinger derivatives with respect to the conjugates of the eigenvalues annihilate it.

### Summary of the Logarithm

| Case | A logarithm | Principal logarithm | Fibre |
|---|---|---|---|
| Unit, $\lambda_1\lambda_2\neq0$ | $\mu_1\Pi_++\mu_2\Pi_-$, $\mu_i=\operatorname{Log}\lambda_i+2\pi i k_i$ | the same with principal $\operatorname{Log}\lambda_i$ | coset of $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$ |
| Zero divisor, exactly one eigenvalue $0$ | none | none | empty |
| Zero, $\lambda_1=\lambda_2=0$ | none | none | empty |

## Powers and Roots

### The Power Function

For a unit $\breve Q$ and a complex exponent $s$, a **power** is the spectral function

$$
\breve Q^{s}=\lambda_1^{s}\Pi_++\lambda_2^{s}\Pi_-
=\exp(s\,\breve Q_{\log})
=\exp(sQ_{\log\blacktriangle})\bigl(\cosh(sQ_{\log\blacktriangledown})+j\sinh(sQ_{\log\blacktriangledown})\bigr),
$$

for a choice of the logarithm $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$. The two eigenvalues of the power are $\lambda_1^{s}$ and $\lambda_2^{s}$, with $\lambda_i^{s}=\exp(s\log(\lambda_i))$ and a branch chosen in each eigenvalue. An element of the algebra is determined by its two eigenvalues, so these two numbers define $\breve Q^{s}$ completely.

Because a logarithm is determined modulo the kernel, the set of values is

$$
\breve Q^{s}=\exp(s\operatorname{Log}\breve Q)\exp\bigl(s(2\pi i k+\pi i(1+j)l)\bigr),\qquad k,l\in\mathbb{Z}.
$$

The factor $\exp(s(2\pi i k+\pi i(1+j)l))$ equals $1$ for every $k,l$ exactly when $s$ is an integer. If $s=m/n$ is rational in lowest terms, the two eigenvalues contribute $n$ values each, and the power takes $n^{2}$ values; otherwise the set of values is infinite. The principal branch uses $\operatorname{Log}\breve Q$.

### Properties

| Property | Statement |
|---|---|
| Single-valued | exactly when $s\in\mathbb{Z}$; finite for rational $s$ and infinite for irrational $s$ |
| Product law | $\breve Q^{s+t}=\breve Q^{s}\breve Q^{t}$ for a fixed logarithm |
| Power of a power | $(\breve Q^{s})^{t}=\breve Q^{st}$ when both exponents are integers; fixed branches differ by the two eigenvalue factors |
| Norm | $\langle\breve Q^{s}\rangle_{\mathrm{ts}}=\langle\breve Q\rangle_{\mathrm{ts}}^{s}$, with compatible branches |

For an integer $n\ge0$, $\breve Q^{n}$ is the ordinary iterated product and is a polynomial in $\breve Q$; for $n<0$ it is the inverse power on the units. For a fixed choice of logarithm, the product law holds. The second law is not an identity of sets in general: a fixed branch of $\breve Q^{s}$ can differ by the two factors
$$
\exp(2\pi i\,t k_1),\qquad \exp(2\pi i\,t k_2),
$$
where $k_1,k_2$ are the integers of the logarithm chosen for $\breve Q^{s}$.

### The Roots

**Theorem (the roots).** Let $n\ge1$ and let $\breve Q\in\mathbb{B}_{\mathrm{r}}$.

1. If $\breve Q$ is a unit, the equation $\breve R^{n}=\breve Q$ has exactly $n^{2}$ solutions: the elements whose eigenvalues are
   $$
   \eta_{1}\lambda_1^{1/n},\qquad \eta_{2}\lambda_2^{1/n},
   $$
   where $\eta_{1},\eta_{2}$ range over the $n$-th roots of unity and $\lambda_i^{1/n}$ is one fixed $n$-th root in each eigenvalue.
2. If exactly one eigenvalue of $\breve Q$ is zero, the equation has exactly $n$ solutions.
3. If $\breve Q=0$, the equation has the single solution $\breve R=0$.

*Proof.* The equation splits into $R_1^{n}=\lambda_1$ and $R_2^{n}=\lambda_2$ in the two eigenvalues. In $\mathbb{C}$, the equation $z^{n}=q$ has $n$ roots when $q\neq0$ and the single root $0$ when $q=0$. The two components are independent, so the counts multiply in case 1, reduce to one factor in case 2, and give $1$ in case 3.

| Case | Condition on $(\lambda_1,\lambda_2)$ | Number of roots |
|---|---|---|
| unit | $\lambda_1\neq0$, $\lambda_2\neq0$ | $n^{2}$ |
| zero divisor | exactly one eigenvalue $0$ | $n$ |
| zero | $\lambda_1=\lambda_2=0$ | $1$ |

A unit therefore has four square roots, and a zero divisor on one eigenvalue has two square roots. The roots of $-1$ are four, not two: they are the two scalar roots $\pm i$ and the two split-imaginary roots $\pm ij$.

**Example.** For $\breve Q=j$ and $s=1/2$ the eigenvalues are $1$ and $-1$. The square roots of the first are $\pm1$, of the second $\pm i$, and the four square roots are

$$
\breve R=\frac{\eta_{1}+\eta_{2}i}{2}+j\,\frac{\eta_{1}-\eta_{2}i}{2},
\qquad \eta_{1},\eta_{2}\in\{\pm1\},
$$

each satisfying $\breve R^{2}=j$. One of them is $\breve R=(1+i)/2+j(1-i)/2$, which is $\exp(\tfrac12\operatorname{Log}j)$.

## The Trigonometric and Hyperbolic Functions

### Definitions

The **reduced biquaternion sine**, **cosine**, **hyperbolic sine** and **hyperbolic cosine** are defined by

$$
\sin\breve Q=\frac{\exp(i\breve Q)-\exp(-i\breve Q)}{2i},\qquad
\cos\breve Q=\frac{\exp(i\breve Q)+\exp(-i\breve Q)}{2},
$$

$$
\sinh\breve Q=\frac{\exp(\breve Q)-\exp(-\breve Q)}{2},\qquad
\cosh\breve Q=\frac{\exp(\breve Q)+\exp(-\breve Q)}{2}.
$$

By the Idempotent Principle they are

$$
\sin\breve Q=\sin(\lambda_1)\Pi_++\sin(\lambda_2)\Pi_-,\qquad
\cos\breve Q=\cos(\lambda_1)\Pi_++\cos(\lambda_2)\Pi_-,
$$

$$
\sinh\breve Q=\sinh(\lambda_1)\Pi_++\sinh(\lambda_2)\Pi_-,\qquad
\cosh\breve Q=\cosh(\lambda_1)\Pi_++\cosh(\lambda_2)\Pi_-,
$$

with the complex functions on the two eigenvalues. All four are entire, and

$$
\sin'\breve Q=\cos\breve Q,\quad \cos'\breve Q=-\sin\breve Q,\quad
\sinh'\breve Q=\cosh\breve Q,\quad \cosh'\breve Q=\sinh\breve Q.
$$

### The Closed Forms

The coefficient forms follow from the spectral form and from $\cos(jQ_{\blacktriangledown})=\cos Q_{\blacktriangledown}$, $\sin(jQ_{\blacktriangledown})=j\sin Q_{\blacktriangledown}$.

| Function | Spectral form | Coefficient form |
|---|---|---|
| $\sin\breve Q$ | $\sin(\lambda_1)\Pi_++\sin(\lambda_2)\Pi_-$ | $\sin Q_{\blacktriangle}\cos Q_{\blacktriangledown}+j\cos Q_{\blacktriangle}\sin Q_{\blacktriangledown}$ |
| $\cos\breve Q$ | $\cos(\lambda_1)\Pi_++\cos(\lambda_2)\Pi_-$ | $\cos Q_{\blacktriangle}\cos Q_{\blacktriangledown}-j\sin Q_{\blacktriangle}\sin Q_{\blacktriangledown}$ |
| $\sinh\breve Q$ | $\sinh(\lambda_1)\Pi_++\sinh(\lambda_2)\Pi_-$ | $\sinh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\cosh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}$ |
| $\cosh\breve Q$ | $\cosh(\lambda_1)\Pi_++\cosh(\lambda_2)\Pi_-$ | $\cosh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}$ |

The four functions are pairs of ordinary complex functions at the eigenvalues. This is why every identity below holds without a commutator correction.

### Identities, Periods and Zeros

| Property | Statement |
|---|---|
| Pythagorean | $\sin^{2}\breve Q+\cos^{2}\breve Q=1$, $\cosh^{2}\breve Q-\sinh^{2}\breve Q=1$ |
| Addition | $\sin(\breve Q_1+\breve Q_2)=\sin\breve Q_1\cos\breve Q_2+\cos\breve Q_1\sin\breve Q_2$, $\cos(\breve Q_1+\breve Q_2)=\cos\breve Q_1\cos\breve Q_2-\sin\breve Q_1\sin\breve Q_2$ |
| Hyperbolic addition | $\sinh(\breve Q_1+\breve Q_2)=\sinh\breve Q_1\cosh\breve Q_2+\cosh\breve Q_1\sinh\breve Q_2$, $\cosh(\breve Q_1+\breve Q_2)=\cosh\breve Q_1\cosh\breve Q_2+\sinh\breve Q_1\sinh\breve Q_2$ |
| Double angle | $\sin(2\breve Q)=2\sin\breve Q\cos\breve Q$, $\cos(2\breve Q)=\cos^{2}\breve Q-\sin^{2}\breve Q$, $\sinh(2\breve Q)=2\sinh\breve Q\cosh\breve Q$, $\cosh(2\breve Q)=\cosh^{2}\breve Q+\sinh^{2}\breve Q$ |
| Rotation | $\sin(i\breve Q)=i\sinh\breve Q$, $\cos(i\breve Q)=\cosh\breve Q$, $\sinh(i\breve Q)=i\sin\breve Q$, $\cosh(i\breve Q)=\cos\breve Q$ |
| Period of $\sin,\cos$ | $\mathcal{P}_{\sin}=\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j)$ |
| Period of $\sinh,\cosh$ | $\mathcal{P}_{\sinh}=\pi i\mathbb{Z}(1+j)\oplus\pi i\mathbb{Z}(1-j)=\ker\exp$ |
| Zeros of $\sin$ | both $\lambda_1,\lambda_2\in\pi\mathbb{Z}$ |
| Zeros of $\cos$ | both $\lambda_1,\lambda_2\in\frac{\pi}{2}+\pi\mathbb{Z}$ |
| Zeros of $\sinh$ | both $\lambda_1,\lambda_2\in i\pi\mathbb{Z}$ |
| Zeros of $\cosh$ | both $\lambda_1,\lambda_2\in i\frac{\pi}{2}+i\pi\mathbb{Z}$ |
| Zero divisors of $\sin$ | $\lambda_1\in\pi\mathbb{Z}$ or $\lambda_2\in\pi\mathbb{Z}$ |
| Zero divisors of $\cos$ | $\lambda_1\in\frac{\pi}{2}+\pi\mathbb{Z}$ or $\lambda_2\in\frac{\pi}{2}+\pi\mathbb{Z}$ |
| Zero divisors of $\sinh$ | $\lambda_1\in i\pi\mathbb{Z}$ or $\lambda_2\in i\pi\mathbb{Z}$ |
| Zero divisors of $\cosh$ | $\lambda_1\in i\frac{\pi}{2}+i\pi\mathbb{Z}$ or $\lambda_2\in i\frac{\pi}{2}+i\pi\mathbb{Z}$ |
| Boundedness | all four are unbounded: $\sin$ and $\cos$ since $\sin(it)=i\sinh t$ and $\cos(it)=\cosh t$; $\sinh$ and $\cosh$ on the real split direction |

An equality requires both eigenvalue equations, while a zero divisor requires only one. The period lattices are read in the eigenvalues: $\mathcal{P}_{\sin}$ has eigenvalue image $(2\pi\mathbb{Z})^{2}$, and $\mathcal{P}_{\sinh}$ has eigenvalue image $(2\pi i\mathbb{Z})^{2}$. The first is the period lattice of the trigonometric functions, of rank two and index two in $\pi\mathbb{Z}+\pi j\mathbb{Z}$; the second is the kernel of the exponential. A period may act in one eigenvalue alone, which is impossible in the complex case with its single period $2\pi$.

### The Other Functions

The remaining functions are the quotients

$$
\tan\breve Q=\frac{\sin\breve Q}{\cos\breve Q},\qquad \cot\breve Q=\frac{\cos\breve Q}{\sin\breve Q},
\qquad
\tanh\breve Q=\frac{\sinh\breve Q}{\cosh\breve Q},\qquad \coth\breve Q=\frac{\cosh\breve Q}{\sinh\breve Q},
$$

$$
\sec\breve Q=\frac{1}{\cos\breve Q},\qquad \csc\breve Q=\frac{1}{\sin\breve Q},
\qquad
\operatorname{sech}\breve Q=\frac{1}{\cosh\breve Q},\qquad \operatorname{csch}\breve Q=\frac{1}{\sinh\breve Q}.
$$

They are defined wherever the denominator is a unit. The poles of $\tan$ and $\cot$ are therefore the sets where $\cos\breve Q$ or $\sin\breve Q$ fails to be a unit, that is where one eigenvalue of the denominator vanishes; each such set is the union of two families of complex planes. The same rule applies to the hyperbolic functions.

### The Inverse Functions

The inverse functions are defined by the same formulas as in the complex case, with the branch choices made independently in the two eigenvalues.

| Function | Formula | Domain |
|---|---|---|
| $\arcsin\breve Q$ | $-i\operatorname{Log}\bigl(i\breve Q+\sqrt{1-\breve Q^{2}}\bigr)$ | where both eigenvalue expressions are defined |
| $\arccos\breve Q$ | $-i\operatorname{Log}\bigl(\breve Q+i\sqrt{1-\breve Q^{2}}\bigr)$ | where both eigenvalue expressions are defined |
| $\arctan\breve Q$ | $\dfrac{1}{2i}\operatorname{Log}\dfrac{1+i\breve Q}{1-i\breve Q}$ | where $1\pm i\breve Q$ are units |
| $\operatorname{arsinh}\breve Q$ | $\operatorname{Log}\bigl(\breve Q+\sqrt{\breve Q^{2}+1}\bigr)$ | where both eigenvalue expressions are defined |
| $\operatorname{arcosh}\breve Q$ | $\operatorname{Log}\bigl(\breve Q+\sqrt{\breve Q^{2}-1}\bigr)$ | where both eigenvalue expressions are defined |
| $\operatorname{artanh}\breve Q$ | $\dfrac12\operatorname{Log}\dfrac{1+\breve Q}{1-\breve Q}$ | where $1\pm\breve Q$ are units |

The square roots and logarithms are multivalued, and the formulas are read in the two eigenvalues, where they reduce to the ordinary complex inverse functions. The domain of each is the set of $\breve Q$ for which both eigenvalue expressions are defined; the branch cuts are inherited from the two eigenvalues.

**Example.** The equation $\sinh\breve Q=2j$ has the solution

$$
\breve Q=\operatorname{arsinh}(2j)=\operatorname{Log}\bigl(2j+\sqrt{5}\bigr)
=j\ln(\sqrt5+2),
$$

because $(2j)^{2}+1=5$. The two eigenvalues of $\sqrt5+2j$ are $\sqrt5+2$ and $\sqrt5-2$, both positive, so the logarithm is the split-complex logarithm and the value is $j\ln(\sqrt5+2)\approx1.4436354752\,j$ for the principal square root and the principal logarithm. The other choice of square root gives the other branch of the multivalued $\operatorname{arsinh}$; for each fixed square root, the logarithm is unique modulo the kernel.

## Relations to the Neighbouring Cases

### The Complex Line

If the split coefficient vanishes, $\breve Q=Q_{\blacktriangle}$, then both eigenvalues equal $Q_{\blacktriangle}$, that is $\lambda_1=\lambda_2$, and every elementary function reduces to the ordinary complex function:

$$
f(\breve Q)=f(Q_{\blacktriangle}).
$$

The reduced biquaternion function therefore restricts to the complex function on the complex line $\mathbb{C}=\mathbb{R}\{1,i\}$. The principal logarithm restricts to the principal complex logarithm, including the value $\operatorname{Log}(-1)=i\pi$ on the negative real axis.

The full set of logarithms of a scalar is larger: it is $\operatorname{Log}\breve Q+\ker\exp$, and the kernel contains the split direction $\pi i(1+j)$, so non-scalar logarithms exist. The same distinction applies to the powers.

### The Split-Complex Plane

If both coefficients are real, the element lies in the split-complex plane $\mathbb{D}=\mathbb{R}\{1,j\}$; write $\breve Q=q_{\blacktriangle}+jq_{\blacktriangledown}$ with $q_{\blacktriangle},q_{\blacktriangledown}\in\mathbb{R}$. Then $\lambda_1=q_{\blacktriangle}+q_{\blacktriangledown}$ and $\lambda_2=q_{\blacktriangle}-q_{\blacktriangledown}$ are real. The exponential is

$$
\exp(q_{\blacktriangle}+jq_{\blacktriangledown})=\exp(q_{\blacktriangle})\bigl(\cosh q_{\blacktriangledown}+j\sinh q_{\blacktriangledown}\bigr).
$$

On the future cone $q_{\blacktriangle}>\lvert q_{\blacktriangledown}\rvert$ both eigenvalues are positive, and the principal logarithm is the split-complex logarithm

$$
\log(q_{\blacktriangle}+jq_{\blacktriangledown})=\tfrac12\ln(q_{\blacktriangle}^{2}-q_{\blacktriangledown}^{2})+\tfrac12 j\ln\frac{q_{\blacktriangle}+q_{\blacktriangledown}}{q_{\blacktriangle}-q_{\blacktriangledown}}.
$$

Outside the future cone the reduced biquaternion logarithm still exists as long as the element is a unit, but it is complex-valued and is not the split-complex real logarithm; on the past cone both eigenvalues are negative and the principal logarithm is

$$
\log(q_{\blacktriangle}+jq_{\blacktriangledown})=\tfrac12\ln(q_{\blacktriangle}^{2}-q_{\blacktriangledown}^{2})+i\pi+\tfrac12 j\ln\frac{q_{\blacktriangle}+q_{\blacktriangledown}}{q_{\blacktriangle}-q_{\blacktriangledown}}.
$$

The trigonometric functions on the split-complex plane remain trigonometric in both real variables, and the hyperbolic functions remain hyperbolic:

$$
\cos(q_{\blacktriangle}+jq_{\blacktriangledown})=\cos q_{\blacktriangle}\cos q_{\blacktriangledown}-j\sin q_{\blacktriangle}\sin q_{\blacktriangledown},
$$

$$
\sin(q_{\blacktriangle}+jq_{\blacktriangledown})=\sin q_{\blacktriangle}\cos q_{\blacktriangledown}+j\cos q_{\blacktriangle}\sin q_{\blacktriangledown},
$$

$$
\cosh(q_{\blacktriangle}+jq_{\blacktriangledown})=\cosh q_{\blacktriangle}\cosh q_{\blacktriangledown}+j\sinh q_{\blacktriangle}\sinh q_{\blacktriangledown},
$$

$$
\sinh(q_{\blacktriangle}+jq_{\blacktriangledown})=\sinh q_{\blacktriangle}\cosh q_{\blacktriangledown}+j\cosh q_{\blacktriangle}\sinh q_{\blacktriangledown}.
$$

### The Relation Between the Two

The complex line $\mathbb{R}\{1,i\}$ and the split-complex plane $\mathbb{R}\{1,j\}$ are two real two-planes in $\mathbb{B}_{\mathrm{r}}$, and they intersect in the real axis $\mathbb{R}$. In the eigenvalue coordinates the complex line is the diagonal

$$
\{(\lambda_1,\lambda_2):\lambda_1=\lambda_2\},
$$

that is $Q_{\blacktriangledown}=0$, while the split-complex plane is the real pair $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{R}$, that is $\lambda_1,\lambda_2\in\mathbb{R}$.

The two planes therefore test different degenerations of the same pair of complex functions: the complex line sets the two eigenvalues equal, and the split-complex plane makes them real and independent.

## Summary

Every elementary function of a reduced biquaternion variable is a pair of ordinary complex functions of the two eigenvalues $\lambda_1=Q_+$ and $\lambda_2=Q_-$, written in the idempotent basis. The exponential is
$$
\exp(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\exp(Q_{\blacktriangle})\bigl(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown}\bigr),
$$
and the functional equation holds for all arguments because the algebra is commutative. Its kernel is the rank-two lattice $2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)$, and its image is the whole unit group.

The logarithm exists exactly on the units, $\lambda_1\lambda_2\neq0$, and is
$$
\operatorname{Log}\breve Q=\frac{\operatorname{Log}(\lambda_1)+\operatorname{Log}(\lambda_2)}{2}
+j\,\frac{\operatorname{Log}(\lambda_1)-\operatorname{Log}(\lambda_2)}{2}
$$
for the principal branch. The fibre is a coset of the kernel, so the logarithm is unique only on the principal domain, where every eigenvalue has imaginary part in $(-\pi,\pi]$. The values of the power are $\exp(s\operatorname{Log}\breve Q+s\kappa)$ with $\kappa$ in the kernel, and the equation $\breve R^{n}=\breve Q$ has $n^{2}$ solutions for a unit, in particular four square roots.

The trigonometric and hyperbolic functions are read at the two eigenvalues. Their identities hold without restriction, the trigonometric period lattice is $\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j)$, and the hyperbolic period lattice is its multiple by $i$ and equals the kernel. On the complex line the functions restrict to the complex ones; on the split-complex plane the hyperbolic functions restrict to the split-complex hyperbolic ones, while the trigonometric functions remain trigonometric in the two real coordinates.

### Main Results

| Result | Statement |
|---|---|
| Regimes | distinct unit, zero divisor, scalar; the algebra is reduced, so there is no nilpotent regime |
| Spectrum | $\sigma(\breve Q)=\{\lambda_1,\lambda_2\}=\{Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown}\}$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Idempotent Principle | $f(\breve Q)=f(\lambda_1)\Pi_++f(\lambda_2)\Pi_-$ for every complex power series |
| Exponential | $\exp\breve Q=\exp(\lambda_1)\Pi_++\exp(\lambda_2)\Pi_-=\exp Q_{\blacktriangle}(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$ |
| Kernel and image | $\ker\exp=2\pi i(\mathbb{Z}\Pi_+\oplus\mathbb{Z}\Pi_-)\cong\mathbb{Z}^{2}$; $\operatorname{im}\exp=\mathbb{B}_{\mathrm{r}}^{\times}$ |
| Logarithm | $\operatorname{Log}\breve Q=\frac{\operatorname{Log}\lambda_1+\operatorname{Log}\lambda_2}{2}+j\frac{\operatorname{Log}\lambda_1-\operatorname{Log}\lambda_2}{2}$ on the units |
| Principal domain | every eigenvalue has imaginary part in $(-\pi,\pi]$; $\exp:D\to\mathbb{B}_{\mathrm{r}}^{\times}$ is bijective |
| Fibre | $\operatorname{Log}\breve Q+\ker\exp$, a coset of $\mathbb{Z}^{2}$ |
| Derivative of the logarithm | $d\operatorname{Log}_{\breve Q}(\breve H)=\breve Q^{-1}\breve H$ |
| Powers | $\breve Q^{s}=\lambda_1^{s}\Pi_++\lambda_2^{s}\Pi_-$; $n^{2}$ values for $s=m/n$ in lowest terms |
| Roots | $n^{2}$ for a unit, $n$ for a one-eigenvalue zero divisor, $1$ for $0$ |
| Trigonometric functions | $\sin\breve Q=\sin\lambda_1\Pi_++\sin\lambda_2\Pi_-$, $\cos\breve Q=\cos\lambda_1\Pi_++\cos\lambda_2\Pi_-$ |
| Hyperbolic functions | $\sinh\breve Q=\sinh\lambda_1\Pi_++\sinh\lambda_2\Pi_-$, $\cosh\breve Q=\cosh\lambda_1\Pi_++\cosh\lambda_2\Pi_-$ |
| Identities | $\sin^2\breve Q+\cos^2\breve Q=1$, $\cosh^2\breve Q-\sinh^2\breve Q=1$, the addition and double-angle formulas |
| Periods | $\mathcal{P}_{\sin}=\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j)$; $\mathcal{P}_{\sinh}=\ker\exp$ |
| Inverse functions | $\arcsin\breve Q$, $\arccos\breve Q$, $\arctan\breve Q$ and the hyperbolic inverses, built from the logarithm and the square root |

### Formulas

| Function | Value | Domain |
|---|---|---|
| $\exp\breve Q$ | $\exp(Q_{\blacktriangle})(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$ | all $\breve Q$ |
| $\operatorname{Log}\breve Q$ | $\frac{\operatorname{Log}\lambda_1+\operatorname{Log}\lambda_2}{2}+j\frac{\operatorname{Log}\lambda_1-\operatorname{Log}\lambda_2}{2}$ | the units |
| $\breve Q^{s}$ | $\exp(s\operatorname{Log}\breve Q+s\kappa)$ with $\kappa\in\ker\exp$ | the units, with a branch choice |
| $\sin\breve Q$ | $\sin Q_{\blacktriangle}\cos Q_{\blacktriangledown}+j\cos Q_{\blacktriangle}\sin Q_{\blacktriangledown}$ | all $\breve Q$ |
| $\cos\breve Q$ | $\cos Q_{\blacktriangle}\cos Q_{\blacktriangledown}-j\sin Q_{\blacktriangle}\sin Q_{\blacktriangledown}$ | all $\breve Q$ |
| $\sinh\breve Q$ | $\sinh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\cosh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}$ | all $\breve Q$ |
| $\cosh\breve Q$ | $\cosh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}$ | all $\breve Q$ |
| $\tan\breve Q$ | $\sin\breve Q/\cos\breve Q$ | $\cos\breve Q$ a unit |
| $\cot\breve Q$ | $\cos\breve Q/\sin\breve Q$ | $\sin\breve Q$ a unit |
| $\tanh\breve Q$ | $\sinh\breve Q/\cosh\breve Q$ | $\cosh\breve Q$ a unit |
| $\coth\breve Q$ | $\cosh\breve Q/\sinh\breve Q$ | $\sinh\breve Q$ a unit |
| $\operatorname{arsinh}\breve Q$ | $\operatorname{Log}(\breve Q+\sqrt{\breve Q^{2}+1})$ | where the square root and the logarithm are defined |
| $\operatorname{arcosh}\breve Q$ | $\operatorname{Log}(\breve Q+\sqrt{\breve Q^{2}-1})$ | where the square root and the logarithm are defined |
| $\operatorname{artanh}\breve Q$ | $\tfrac12\operatorname{Log}\dfrac{1+\breve Q}{1-\breve Q}$ | where $1\pm\breve Q$ are units |

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
| $\mathbb{B}_{\mathrm{r}}$ | the reduced biquaternion algebra, basis $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ij=ji$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | an element, $Q_{\blacktriangle}$ scalar part, $Q_{\blacktriangledown}$ split part |
| $Q_{+}$, $Q_{-}$ | the eigenvalues $\lambda_1=Q_+$, $\lambda_2=Q_-$, read also as idempotent coordinates |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the central idempotents, $\breve Q=\lambda_1\Pi_++\lambda_2\Pi_-$ |
| $\lambda_1,\lambda_2$ | the eigenvalues, $\lambda_1=Q_+$, $\lambda_2=Q_-$ |
| $\bar{\breve Q}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$ | the bar |
| $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | the reduced norm |
| $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$ | the squared Euclidean norm |
| $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ | a logarithm, with $Q_{\log\blacktriangle}=q_{\log\blacktriangle}+iq'_{\log\blacktriangle}=\ln\rho+i\alpha$ and $Q_{\log\blacktriangledown}=q_{\log\blacktriangledown}+iq'_{\log\blacktriangledown}=\phi+i\beta$ |
| $q_{\log\blacktriangle},q'_{\log\blacktriangle},q_{\log\blacktriangledown},q'_{\log\blacktriangledown}$ | the four real components of the logarithm: $\ln\rho,\alpha,\phi,\beta$ |
| $\exp\breve Q=\exp(Q_{\blacktriangle})(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$ | the exponential |
| $\operatorname{Log}\breve Q$ | the principal logarithm |
| $D$ | the principal diamond $\lvert\operatorname{Im}Q_{\log\blacktriangle}\rvert+\lvert\operatorname{Im}Q_{\log\blacktriangledown}\rvert\le\pi$ |
| $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$ | the kernel of the exponential |
| $\mathcal{P}_{\sin}$ | $\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j)$, the period lattice of $\sin$ and $\cos$ |
| $\mathcal{P}_{\sinh}$ | $\pi i\mathbb{Z}(1+j)\oplus\pi i\mathbb{Z}(1-j)=\ker\exp$, the period lattice of $\sinh$ and $\cosh$ |
| $\sin\breve Q,\ \cos\breve Q,\ \sinh\breve Q,\ \cosh\breve Q$ | trigonometric and hyperbolic functions |
| $\sec\breve Q,\ \csc\breve Q,\ \operatorname{sech}\breve Q,\ \operatorname{csch}\breve Q$ | Reciprocal functions |
| $\breve Q^{s}$ | the power function |
| $\breve R$ | a root of $\breve R^{n}=\breve Q$ |
| $\eta_{1},\eta_{2}$ | $n$-th roots of unity of the two eigenvalues |

## Further Reading

- [Eigenbasis of a Reduced Biquaternion](eigenbasis-of-a-reduced-biquaternion.html), for the eigenvalue decomposition, the central idempotents and the polynomial calculus used throughout.
- [Exponential Polar Decomposition of Reduced Biquaternions](exponential-polar-decomposition-of-reduced-biquaternions.html), for the polar reading of the logarithm.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the exponential, the trigonometric functions and the logarithm of one complex variable.
- Lars V. Ahlfors, *Complex Analysis*, 3rd edition (McGraw-Hill, 1979), for the branch structure of the logarithm and the power functions.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the exponential and the elementary functions of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the reduction of the elementary functions.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the exponential of the hypercomplex algebras and the comparison with the division-algebra cases.
