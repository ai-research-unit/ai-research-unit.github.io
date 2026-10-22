# __Reduced Biquaternion Elementary Functions__

## Introduction

This article introduces the elementary functions of a reduced biquaternion variable as a collection of named functions: the exponential, the logarithm, the trigonometric and hyperbolic functions, the power functions and the roots. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Complex analysis is assumed: holomorphic functions, power series, the complex exponential and logarithm, and the branch structure of the argument are used throughout. The order of presentation follows the dependency order: the exponential and the logarithm first, with the powers and roots that come from them, then the trigonometric and hyperbolic functions, then the relations to the complex and split-complex cases.

Three facts govern the whole article. First, the algebra is **commutative**, so the functional equations, the addition formulas and the differentiation rules hold for all arguments, with no ordering correction. Second, the exponential is **not injective**: its kernel is the rank-two lattice

$$
\ker\exp=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z},
$$

so the logarithm exists on the unit group and is unique only modulo this lattice. Third, the exponential is **computed by a closed form**,

$$
\exp(Q_{\blacktriangle}+jQ_{\blacktriangledown})=e^{Q_{\blacktriangle}}\bigl(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown}\bigr),
$$

which reduces every elementary function to ordinary complex functions of the two coefficients.

Throughout the element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$, the bar is $\bar{\breve Q}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$, the reduced norm is $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$, and the squared Euclidean norm is $\langle\breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}$. The two numbers $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ are the **circular components**; they multiply componentwise,

$$
(Q_{\blacktriangle}+jQ_{\blacktriangledown})(Q_{2\blacktriangle}+jQ_{2\blacktriangledown})
=(Q_{\blacktriangle}Q_{2\blacktriangle}+Q_{\blacktriangledown}Q_{2\blacktriangledown})
+j(Q_{\blacktriangle}Q_{2\blacktriangledown}+Q_{\blacktriangledown}Q_{2\blacktriangle}),
$$

with components $Q_{+}Q_{2+}$ and $Q_{-}Q_{2-}$. The element is a unit exactly when $Q_{\blacktriangle}^{2}\neq Q_{\blacktriangledown}^{2}$, that is exactly when both circular components are non-zero.

**Boundaries.** The algebra and its bar are *Introduction to the Algebra of the Reduced Biquaternions*; the norm and the unit criterion are *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the zero divisors are *Zero Divisors of the Algebra of the Reduced Biquaternions*. The exponential polar decomposition is *Exponential Polar Decomposition of Reduced Biquaternions*, where the kernel and the principal domain are treated. The complex member is *Complex Special Functions*, and the split-complex member is *Split-Complex Special Functions*. The higher special functions are *Reduced Biquaternion Higher Special Functions*.

The plan is as follows. The exponential and the logarithm are defined and their two compositions established (§*The Reduced Biquaternion Exponential and Logarithm*); the powers and the roots follow from the logarithm (§*Powers and Roots*); the trigonometric and hyperbolic functions follow (§*The Trigonometric and Hyperbolic Functions*), with their periods, zeros and inverses; the relations to the complex line and the split-complex plane are recorded (§*The Two Planes*); the formulas are collected and the notation is tabulated (§*Summary*, §*Summary of Notation*).

Every numerical value displayed below was recomputed in double precision.

## The Reduced Biquaternion Exponential and Logarithm

### The Exponential

The **reduced biquaternion exponential** is defined for $\breve Q\in\mathbb{B}_{\mathrm{r}}$ by the power series

$$
\exp\breve Q=\sum_{n=0}^{\infty}\frac{\breve Q^{n}}{n!}.
$$

The series converges absolutely in the Euclidean norm for every $\breve Q$, because the algebra is finite-dimensional and the series converges in each coefficient. The function is entire, and it satisfies

$$
\exp(\breve Q_1+\breve Q_2)=\exp\breve Q_1\,\exp\breve Q_2,\qquad \exp 0=1.
$$

The functional equation holds for **all** arguments because the algebra is commutative; no ordering correction is needed. The derivative at $\breve Q$ is left multiplication by $\exp\breve Q$:

$$
d\exp_{\breve Q}(\breve H)=\exp(\breve Q)\,\breve H.
$$

This follows from $\exp(\breve Q+t\breve H)=\exp\breve Q\,\exp(t\breve H)$ and $\exp(t\breve H)=1+t\breve H+O(t^{2})$.

For $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$ the series splits by the binomial theorem, because $Q_{\blacktriangle}$ and $jQ_{\blacktriangledown}$ commute:

$$
\exp(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\sum_{k,l}\frac{Q_{\blacktriangle}^{k}(jQ_{\blacktriangledown})^{l}}{k!\,l!}
=e^{Q_{\blacktriangle}}\bigl(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown}\bigr).
$$

This is the **reduced Euler formula**. It is the bridge between the exponential and the trigonometric and hyperbolic functions. In particular,

$$
\exp(i\theta)=\cos\theta+i\sin\theta,\qquad
\exp(ij\beta)=\cos\beta+ij\sin\beta,\qquad
\exp(j\phi)=\cosh\phi+j\sinh\phi.
$$

The first two are the elliptic directions, the third the hyperbolic direction.

**Periods.** The exponential is periodic with the lattice

$$
\ker\exp=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}.
$$

In particular $\exp(\breve Q+2\pi i)=\exp\breve Q$ and $\exp(\breve Q+\pi i(1+j))=\exp\breve Q$. The scalar period $2\pi i$ and the split period $2\pi ij$ generate a sublattice of index two; the period $\pi i(1+j)$ is half of their sum.

**Example.** For $\breve Q=j\ln2$ the closed form gives

$$
\exp(j\ln2)=\cosh(\ln2)+j\sinh(\ln2)=\tfrac54+\tfrac34 j,
$$

that is $1.25+0.75j$. This is the hyperbolic exponential $\cosh(\ln2)+j\sinh(\ln2)$, and it is the point of the future hyperbola at boost $\ln2$.

### The Logarithm

A **logarithm** of a unit $\breve Q$ is an element $\breve Q_{\log}$ with $\exp\breve Q_{\log}=\breve Q$. The definition is an equation, not a formula; the formula is what solving the equation gives.

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

The equation $\exp(Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown})=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is, by the closed form,

$$
e^{Q_{\log\blacktriangle}}\cosh Q_{\log\blacktriangledown}=Q_{\blacktriangle},\qquad e^{Q_{\log\blacktriangle}}\sinh Q_{\log\blacktriangledown}=Q_{\blacktriangledown}.
$$

Adding and subtracting the two equations gives

$$
e^{Q_{\log\blacktriangle}+Q_{\log\blacktriangledown}}=Q_{+},\qquad e^{Q_{\log\blacktriangle}-Q_{\log\blacktriangledown}}=Q_{-}.
$$

Hence, for any choices of the complex logarithms,

$$
Q_{\log\blacktriangle}+Q_{\log\blacktriangledown}=\log(Q_{+}),\qquad Q_{\log\blacktriangle}-Q_{\log\blacktriangledown}=\log(Q_{-}),
$$

and therefore

$$
Q_{\log\blacktriangle}=\frac{\log(Q_{+})+\log(Q_{-})}{2},\qquad
Q_{\log\blacktriangledown}=\frac{\log(Q_{+})-\log(Q_{-})}{2}.
$$

Assembling the two coefficients, the logarithm is

$$
\breve Q_{\log}=\frac{\log(Q_{+})+\log(Q_{-})}{2}
+j\,\frac{\log(Q_{+})-\log(Q_{-})}{2},
$$

which is the **global result**: it holds for every unit $\breve Q$ and every choice of the complex logarithm in each circular component.

A logarithm exists exactly when both $Q_{+}$ and $Q_{-}$ are non-zero, that is exactly when $\breve Q$ is a **unit**. The general solution is

$$
\breve Q_{\log}=\operatorname{Log}\breve Q+2\pi i k+\pi i(1+j)l,\qquad k,l\in\mathbb{Z},
$$

with the **principal logarithm**

$$
\operatorname{Log}\breve Q=\frac{\operatorname{Log}(Q_{+})+\operatorname{Log}(Q_{-})}{2}
+j\,\frac{\operatorname{Log}(Q_{+})-\operatorname{Log}(Q_{-})}{2},
$$

where $\operatorname{Log}$ on the right is the principal complex logarithm, with argument in $(-\pi,\pi]$.

**The four components.** For the principal branch, taking the real and imaginary parts of the two coefficients gives the four real components of the logarithm:

| component | name | value from $Q_{+},Q_{-}$ | value in $(\rho,\phi,\alpha,\beta)$ |
|---|---|---|---|
| $q_{\log\blacktriangle}$ | logarithmic scale | $\tfrac12\ln\lvert Q_{+}Q_{-}\rvert=\tfrac12\ln\lvert\langle\breve Q\rangle_{\mathrm{ts}}\rvert$ | $\ln\rho$ |
| $q'_{\log\blacktriangle}$ | scalar phase | $\tfrac12\bigl(\operatorname{Arg}(Q_{+})+\operatorname{Arg}(Q_{-})\bigr)$ | $\alpha$ |
| $q_{\log\blacktriangledown}$ | boost | $\tfrac12\ln\lvert Q_{+}/Q_{-}\rvert$ | $\phi$ |
| $q'_{\log\blacktriangledown}$ | split phase | $\tfrac12\bigl(\operatorname{Arg}(Q_{+})-\operatorname{Arg}(Q_{-})\bigr)$ | $\beta$ |

Here $\rho=\sqrt{\lvert Q_{+}Q_{-}\rvert}=\sqrt{\lvert\langle\breve Q\rangle_{\mathrm{ts}}\rvert}$ and $\operatorname{Arg}$ is the principal argument in $(-\pi,\pi]$. For another branch, the pair $(\alpha,\beta)$ is shifted by a lattice vector. The logarithm is the sum of the four basis terms,

$$
\breve Q_{\log}=q_{\log\blacktriangle}+jq_{\log\blacktriangledown}+iq'_{\log\blacktriangle}+ijq'_{\log\blacktriangledown}
=\ln\rho+j\phi+i\alpha+ij\beta,
$$

and the exponential reassembles them:

$$
\breve Q=\exp\breve Q_{\log}=\rho\bigl(\cosh\phi+j\sinh\phi\bigr)\bigl(\cos\alpha+i\sin\alpha\bigr)\bigl(\cos\beta+ij\sin\beta\bigr).
$$

The component $q_{\log\blacktriangle}=\ln\rho$ sets the overall size, $q_{\log\blacktriangledown}=\phi$ the relative scale of the two circular components, and the two primed components are the phases $\alpha$ and $\beta$.

**Example.** For $\breve Q=3+4i+j(1-i)$ the coefficients are $Q_{\blacktriangle}=3+4i$ and $Q_{\blacktriangledown}=1-i$, so $Q_{+}=4+3i$ and $Q_{-}=2+5i$. The principal complex logarithms are

$$
\operatorname{Log}(4+3i)=1.6094379+0.6435011\,i,\qquad
\operatorname{Log}(2+5i)=1.6836479+1.1902899\,i,
$$

so

$$
\operatorname{Log}\breve Q=1.6465429+0.9168955\,i-0.0371050\,j-0.2733944\,ij.
$$

Exponentiating gives $3+4i+j(1-i)$ up to rounding. The general logarithm adds $2\pi i k+\pi i(1+j)l$.

The **kernel** of the exponential is the rank-two lattice

$$
\ker\exp=2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}\cong\mathbb{Z}^{2}.
$$

In the circular components it is generated by the two elementary periods of the two components, and the scalar and split periods $2\pi i$, $2\pi ij$ span only a sublattice of index two. The logarithm exists on the whole unit group and is never unique: the ambiguity is one integer per circular component. This is the exact replacement of the single integer $2\pi i\mathbb{Z}$ of the complex case; the split-complex case has no ambiguity because its exponential is injective.

### The Two Compositions

The word "inverse" covers two identities, and the exponential and the logarithm satisfy them in opposite strengths.

**Right inverse.** For every unit $\breve Q$,

$$
\exp(\operatorname{Log}\breve Q)=\breve Q.
$$

**Proof.** In the circular components, $\exp(\operatorname{Log}(Q_{\pm}))=Q_{\pm}$ by the complex identity, and the two components reassemble.

**Left inverse, up to the kernel.** For every $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$,

$$
\operatorname{Log}(\exp\breve Q_{\log})=\breve Q_{\log}
$$

exactly when $\breve Q_{\log}$ lies in the **principal domain**

$$
D=\Bigl\{Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}:\lvert\operatorname{Im}Q_{\log\blacktriangle}\rvert+\lvert\operatorname{Im}Q_{\log\blacktriangledown}\rvert\le\pi\Bigr\},
$$

with the boundary taken half-open. For a general $\breve Q_{\log}$, the two sides differ by an element of the kernel:

$$
\operatorname{Log}(\exp\breve Q_{\log})=\breve Q_{\log}+2\pi i k+\pi i(1+j)l
$$

for the integers that bring the two phases into the principal diamond.

**Proof.** Both sides are logarithms of $\exp\breve Q_{\log}$, so they differ by an element of $\ker\exp$. The principal value is the representative whose two phases lie in the half-open diamond.

The asymmetry is the content of the word "multivalued". The exponential forgets two integers, one for each circular component; the principal logarithm chooses one representative. The split-complex exponential forgets none, and the complex exponential forgets one.

| identity | holds? | example |
|---|---|---|
| $\exp(\operatorname{Log}\breve Q)=\breve Q$ | always, on the units | $\breve Q=3+4i+j(1-i)$ above |
| $\operatorname{Log}(\exp\breve Q_{\log})=\breve Q_{\log}$ | exactly in the principal domain $D$ | $\breve Q_{\log}=i\pi$ |
| $\operatorname{Log}(\exp\breve Q_{\log})=\breve Q_{\log}$ modulo the kernel | always | $\breve Q_{\log}=i\pi(1+j)$ gives $0$ |

### The Principal Logarithm

The principal logarithm is defined on the whole unit group by the formula with the principal argument in each circular component. It is real-analytic on the complement of the two walls

$$
W_{+}=\{Q_{+}\in(-\infty,0)\},\qquad W_{-}=\{Q_{-}\in(-\infty,0)\},
$$

each of real dimension three, and it is discontinuous across them. A branch that continued analytically across a wall would have to continue by a period and would not be single-valued. The walls are the exact analogue of the negative real axis of $\mathbb{C}$: there is one wall for each circular component, and the jump across $W_{+}$ is $\pi i(1+j)$, across $W_{-}$ is $\pi i(1-j)$, both kernel elements.

The principal logarithm is not defined at $Q_{+}=0$ or $Q_{-}=0$, which are the zero divisors. On the unit group it is defined everywhere, including on the walls, where continuity fails but the inverse identity holds.

A single-valued branch exists on a domain when each circular component lies in a simply connected domain of $\mathbb{C}^{\times}$. The maximal domains are the complements of rays in the two components, and the principal branch uses the negative real ray in both. No single-valued branch exists on the whole unit group, because the unit group has fundamental group $\mathbb{Z}^{2}$; the obstruction is the kernel lattice, not a failure of local invertibility. The exponential is a covering map onto the unit group, and the logarithm is its multivalued inverse.

**Example.** For $\breve Q=-1$ the principal logarithm is $i\pi$, the upper endpoint of the first phase. Approaching $-1$ through $Q_{+}$ in the upper half-plane gives phase $\pi$; approaching through the lower half-plane gives phase $-\pi$. The two limits differ by $2\pi i$, so the principal branch cannot be continued continuously across $W_{+}$. The other circular component produces the same phenomenon on $W_{-}$.

### The Derivative of the Logarithm

On the complement of the walls the principal logarithm is differentiable, and its derivative is left multiplication by $\breve Q^{-1}$:

$$
d\operatorname{Log}_{\breve Q}(\breve H)=\breve Q^{-1}\breve H.
$$

In the circular components,

$$
\bigl(d\operatorname{Log}_{\breve Q}\breve H\bigr)_{\pm}=\frac{H_{\pm}}{Q_{\pm}}.
$$

**Proof.** The exponential is a local biholomorphism with derivative left multiplication by $\exp\breve Q_{\log}=\breve Q$; the inverse function theorem gives the derivative of the inverse as left multiplication by $\breve Q^{-1}$.

**Chain rule check.** Differentiating $\exp(\operatorname{Log}\breve Q)=\breve Q$ gives

$$
\exp(\operatorname{Log}\breve Q)\,d\operatorname{Log}_{\breve Q}=\mathrm{id},
$$

hence $d\operatorname{Log}_{\breve Q}=\breve Q^{-1}$. The same computation applies to any branch of the logarithm, and it shows that all branches have the same derivative.

The formula is the exact analogue of $\operatorname{Log}'Q=1/Q$ in $\mathbb{C}$, applied twice. The logarithm is holomorphic in each circular component, and the two Wirtinger derivatives with respect to the conjugates of the components annihilate it.

### Powers and Roots

For a unit $\breve Q$ and a complex exponent $s$, a **power** is

$$
\breve Q^{s}=\exp(s\,\breve Q_{\log})=e^{sQ_{\log\blacktriangle}}\bigl(\cosh(sQ_{\log\blacktriangledown})+j\sinh(sQ_{\log\blacktriangledown})\bigr),
$$

for a choice of the logarithm $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$. The two circular components of the power are

$$
(Q_{+})^{s},\qquad (Q_{-})^{s},
$$

with $(Q_{\pm})^{s}=\exp(s\log(Q_{\pm}))$ and a branch chosen in each component. An element of the algebra is determined by its two circular components, so these two numbers define $\breve Q^{s}$ completely.

Because a logarithm is determined modulo the kernel, the set of values is

$$
\breve Q^{s}=\exp(s\operatorname{Log}\breve Q)\exp\bigl(s(2\pi i k+\pi i(1+j)l)\bigr),\qquad k,l\in\mathbb{Z}.
$$

The factor

$$
\exp\bigl(s(2\pi i k+\pi i(1+j)l)\bigr)
$$

equals $1$ for every $k,l$ exactly when $s$ is an integer. If $s=p/q$ is rational in lowest terms, the two circular components contribute $q$ values each, and the power takes $q^{2}$ values; otherwise the set of values is infinite. The principal branch uses $\operatorname{Log}\breve Q$.

For an integer $n\ge0$, $\breve Q^{n}$ is the ordinary iterated product and is a polynomial in $\breve Q$; for $n<0$ it is the inverse power on the units. For a fixed choice of logarithm,

$$
\breve Q^{s+t}=\breve Q^{s}\breve Q^{t}.
$$

The second law $(\breve Q^{s})^{t}=\breve Q^{st}$ is not an identity of sets in general: it holds when both exponents are integers, and a fixed branch can differ by the two circular-component factors $e^{2\pi i t(k+l)}$ and $e^{2\pi i tk}$, where $k,l$ are the integers of the logarithm chosen for $\breve Q^{s}$.

**Example.** For $\breve Q=j$ and $s=1/2$ the circular components are $1$ and $-1$. The square roots of the first are $\pm1$, of the second $\pm i$, and the four square roots are

$$
\breve R=\frac{\eta_{1}+\eta_{2}i}{2}+j\,\frac{\eta_{1}-\eta_{2}i}{2},
\qquad \eta_{1},\eta_{2}\in\{\pm1\},
$$

each satisfying $\breve R^{2}=j$. One of them is $\breve R=(1+i)/2+j(1-i)/2$, which is $\exp(\tfrac12\operatorname{Log}j)$.

**Theorem (the roots).** Let $n\ge1$ and let $\breve Q\in\mathbb{B}_{\mathrm{r}}$.

1. If $\breve Q$ is a unit, the equation $\breve R^{n}=\breve Q$ has exactly $n^{2}$ solutions: the elements whose circular components are
$$
\eta_{1}(Q_{+})^{1/n},\qquad \eta_{2}(Q_{-})^{1/n},
$$
where $\eta_{1},\eta_{2}$ range over the $n$-th roots of unity and $(Q_{\pm})^{1/n}$ is one fixed $n$-th root in each component.
2. If exactly one circular component of $\breve Q$ is zero, the equation has exactly $n$ solutions.
3. If $\breve Q=0$, the equation has the single solution $\breve R=0$.

*Proof.* The equation splits into $R_{+}^{n}=Q_{+}$ and $R_{-}^{n}=Q_{-}$ in the two circular components. In $\mathbb{C}$, the equation $z^{n}=q$ has $n$ roots when $q\neq0$ and the single root $0$ when $q=0$. The two components are independent, so the counts multiply in case 1, reduce to one factor in case 2, and give $1$ in case 3.

A unit therefore has four square roots, and a zero divisor on one circular component has two square roots. The roots of $-1$ are four, not two: they are the two scalar roots $\pm i$ and the two split-imaginary roots $\pm ij$.

## The Trigonometric and Hyperbolic Functions

### Trigonometric Functions

The **reduced biquaternion sine** and **cosine** are defined by

$$
\sin\breve Q=\frac{\exp(i\breve Q)-\exp(-i\breve Q)}{2i},\qquad
\cos\breve Q=\frac{\exp(i\breve Q)+\exp(-i\breve Q)}{2}.
$$

Both are entire. They satisfy

$$
\sin'\breve Q=\cos\breve Q,\qquad \cos'\breve Q=-\sin\breve Q,
$$

$$
\sin(\breve Q_1+\breve Q_2)=\sin\breve Q_1\cos\breve Q_2+\cos\breve Q_1\sin\breve Q_2,
$$

$$
\cos(\breve Q_1+\breve Q_2)=\cos\breve Q_1\cos\breve Q_2-\sin\breve Q_1\sin\breve Q_2,
$$

$$
\sin^{2}\breve Q+\cos^{2}\breve Q=1.
$$

In the coefficients,

$$
\sin(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\sin Q_{\blacktriangle}\cos Q_{\blacktriangledown}+j\cos Q_{\blacktriangle}\sin Q_{\blacktriangledown},
$$

$$
\cos(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\cos Q_{\blacktriangle}\cos Q_{\blacktriangledown}-j\sin Q_{\blacktriangle}\sin Q_{\blacktriangledown}.
$$

The formulas follow from the addition formulas and from $\cos(jQ_{\blacktriangledown})=\cos Q_{\blacktriangledown}$, $\sin(jQ_{\blacktriangledown})=j\sin Q_{\blacktriangledown}$.

The functions act on the two circular components separately, so $2\pi$ is a period in each component; in the algebra the periods are

$$
\mathcal{P}_{\sin}=\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j),
$$

of rank two and index two in the lattice $\pi\mathbb{Z}+\pi j\mathbb{Z}$. A period may act in one circular component alone, which is impossible in the complex case with its single period $2\pi$.

The zeros are read in each component: $\sin\breve Q=0$ exactly when both $Q_{+}$ and $Q_{-}$ lie in $\pi\mathbb{Z}$, and $\cos\breve Q=0$ exactly when both lie in $\frac{\pi}{2}+\pi\mathbb{Z}$.

**Unboundedness.** Unlike the real case, $\sin$ and $\cos$ are unbounded on the algebra. For real $t$,

$$
\sin(jt)=j\sinh t,\qquad \cos(jt)=\cosh t,
$$

and both grow exponentially in $\lvert t\rvert$.

### Hyperbolic Functions

The **reduced biquaternion hyperbolic sine** and **cosine** are defined by

$$
\sinh\breve Q=\frac{\exp(\breve Q)-\exp(-\breve Q)}{2},\qquad
\cosh\breve Q=\frac{\exp(\breve Q)+\exp(-\breve Q)}{2}.
$$

Both are entire, and they satisfy

$$
\sinh'\breve Q=\cosh\breve Q,\qquad \cosh'\breve Q=\sinh\breve Q,
$$

$$
\cosh(\breve Q_1+\breve Q_2)=\cosh\breve Q_1\cosh\breve Q_2+\sinh\breve Q_1\sinh\breve Q_2,
$$

$$
\cosh^{2}\breve Q-\sinh^{2}\breve Q=1.
$$

In the coefficients,

$$
\sinh(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\sinh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\cosh Q_{\blacktriangle}\sinh Q_{\blacktriangledown},
$$

$$
\cosh(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\cosh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}.
$$

The relation between the two families is the complex one, applied coefficientwise:

$$
\sin(i\breve Q)=i\sinh\breve Q,\qquad \cos(i\breve Q)=\cosh\breve Q,\qquad
\sinh(i\breve Q)=i\sin\breve Q,\qquad \cosh(i\breve Q)=\cos\breve Q.
$$

The period lattice is

$$
\mathcal{P}_{\sinh}=\pi i\mathbb{Z}(1+j)\oplus\pi i\mathbb{Z}(1-j),
$$

which is the kernel of the exponential. The zeros are read in each component: $\sinh\breve Q=0$ exactly when both $Q_{+}$ and $Q_{-}$ lie in $i\pi\mathbb{Z}$, and $\cosh\breve Q=0$ exactly when both lie in $i\frac{\pi}{2}+i\pi\mathbb{Z}$.

### The Reduction and the Identities

Every trigonometric and hyperbolic identity that holds for commuting complex arguments holds for all reduced biquaternion arguments. The proof is the formula in the coefficients: the identity holds in $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and the two coefficients reassemble. In particular the Pythagorean identities, the addition formulas and the double-angle formulas hold without restriction.

The two period lattices are the two lattices of the algebra: $\pi\mathbb{Z}(1+j)\oplus\pi\mathbb{Z}(1-j)$ for the trigonometric functions and $\pi i$ times it for the hyperbolic functions. The first is the period lattice of the trigonometric functions; the second is the kernel of the exponential and the period lattice of the hyperbolic functions.

### Other Trigonometric and Hyperbolic Functions

The remaining functions are the quotients

$$
\tan\breve Q=\frac{\sin\breve Q}{\cos\breve Q},\qquad \cot\breve Q=\frac{\cos\breve Q}{\sin\breve Q},
$$

$$
\tanh\breve Q=\frac{\sinh\breve Q}{\cosh\breve Q},\qquad \coth\breve Q=\frac{\cosh\breve Q}{\sinh\breve Q}.
$$

They are defined wherever the denominator is a unit. The poles of $\tan$ and $\cot$ are therefore the sets where $\cos\breve Q$ or $\sin\breve Q$ fails to be a unit, that is where one circular component of the denominator vanishes; each such set is the union of two families of complex planes. The same rule applies to the hyperbolic functions.

### Inverse Trigonometric and Hyperbolic Functions

The inverse functions are defined by the same formulas as in the complex case, with the branch choices made independently in the two circular components:

$$
\arcsin\breve Q=-i\operatorname{Log}\bigl(i\breve Q+\sqrt{1-\breve Q^{2}}\bigr),\qquad
\arccos\breve Q=-i\operatorname{Log}\bigl(\breve Q+i\sqrt{1-\breve Q^{2}}\bigr),
$$

$$
\arctan\breve Q=\frac{1}{2i}\operatorname{Log}\frac{1+i\breve Q}{1-i\breve Q},
$$

$$
\operatorname{arsinh}\breve Q=\operatorname{Log}\bigl(\breve Q+\sqrt{\breve Q^{2}+1}\bigr),\qquad
\operatorname{arcosh}\breve Q=\operatorname{Log}\bigl(\breve Q+\sqrt{\breve Q^{2}-1}\bigr),
$$

$$
\operatorname{artanh}\breve Q=\frac12\operatorname{Log}\frac{1+\breve Q}{1-\breve Q}.
$$

The square roots and logarithms are multivalued, and the formulas are read in the circular components, where they reduce to the ordinary complex inverse functions. The domain of each is the set of $\breve Q$ for which both component expressions are defined; the branch cuts are inherited from the two complex components.

**Example.** For $\breve Q=2j$ the equation $\sinh\breve Q=1$ has the solution

$$
\breve Q=\operatorname{arsinh}(2j)=\operatorname{Log}\bigl(2j+\sqrt{5}\bigr)
=j\ln(\sqrt5+2),
$$

because $(2j)^{2}+1=5$. The two circular components of $\sqrt5+2j$ are $\sqrt5+2$ and $\sqrt5-2$, both positive, so the logarithm is the split-complex logarithm and the value is $j\ln(\sqrt5+2)\approx1.4436354752\,j$, unique modulo the kernel.

## The Two Planes

### The Complex Line

If the split coefficient vanishes, $\breve Q=Q_{\blacktriangle}$, then both circular components equal $Q_{\blacktriangle}$ and every elementary function reduces to the ordinary complex function:

$$
f(\breve Q)=f(Q_{\blacktriangle}).
$$

The reduced biquaternion function therefore restricts to the complex function on the complex line $\mathbb{C}=\mathbb{R}\{1,i\}$. The principal logarithm restricts to the principal complex logarithm, including the value $\operatorname{Log}(-1)=i\pi$ on the negative real axis.

### The Split-Complex Plane

If both coefficients are real, the element lies in the split-complex plane $\mathbb{D}=\mathbb{R}\{1,j\}$; write $\breve Q=q_{\blacktriangle}+jq_{\blacktriangledown}$ with $q_{\blacktriangle},q_{\blacktriangledown}\in\mathbb{R}$. Then $Q_{+}=q_{\blacktriangle}+q_{\blacktriangledown}$ and $Q_{-}=q_{\blacktriangle}-q_{\blacktriangledown}$ are real. The exponential is

$$
\exp(q_{\blacktriangle}+jq_{\blacktriangledown})=e^{q_{\blacktriangle}}\bigl(\cosh q_{\blacktriangledown}+j\sinh q_{\blacktriangledown}\bigr).
$$

On the future cone $q_{\blacktriangle}>\lvert q_{\blacktriangledown}\rvert$ both circular components are positive, and the principal logarithm is the split-complex logarithm

$$
\log(q_{\blacktriangle}+jq_{\blacktriangledown})=\tfrac12\ln(q_{\blacktriangle}^{2}-q_{\blacktriangledown}^{2})+\tfrac12 j\ln\frac{q_{\blacktriangle}+q_{\blacktriangledown}}{q_{\blacktriangle}-q_{\blacktriangledown}}.
$$

Outside the future cone the reduced biquaternion logarithm still exists as long as the element is a unit, but it is complex-valued and is not the split-complex real logarithm; on the past cone both components are negative and the principal logarithm is

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

The complex line $\mathbb{R}\{1,i\}$ and the split-complex plane $\mathbb{R}\{1,j\}$ are two real two-planes in $\mathbb{B}_{\mathrm{r}}$, and they intersect in the real axis $\mathbb{R}$. In the circular components the complex line is the diagonal

$$
\{(Q_{+},Q_{-}):Q_{+}=Q_{-}\},
$$

that is $Q_{\blacktriangledown}=0$, while the split-complex plane is the real pair $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{R}$, that is $Q_{\pm}\in\mathbb{R}$.

The two planes therefore test different degenerations of the same pair of complex functions: the complex line sets the two components equal, and the split-complex plane makes them real and independent.

## Summary

Every elementary function of a reduced biquaternion variable is a pair of ordinary complex functions of the two circular components $Q_{+}$ and $Q_{-}$, written in the algebra. The exponential is

$$
\exp(Q_{\blacktriangle}+jQ_{\blacktriangledown})=e^{Q_{\blacktriangle}}\bigl(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown}\bigr),
$$

and the functional equation holds for all arguments because the algebra is commutative. The trigonometric and hyperbolic functions are

$$
\sin(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\sin Q_{\blacktriangle}\cos Q_{\blacktriangledown}+j\cos Q_{\blacktriangle}\sin Q_{\blacktriangledown},\qquad
\cos(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\cos Q_{\blacktriangle}\cos Q_{\blacktriangledown}-j\sin Q_{\blacktriangle}\sin Q_{\blacktriangledown},
$$

$$
\sinh(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\sinh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\cosh Q_{\blacktriangle}\sinh Q_{\blacktriangledown},\qquad
\cosh(Q_{\blacktriangle}+jQ_{\blacktriangledown})=\cosh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangle}\sinh Q_{\blacktriangledown},
$$

and their identities, period lattices and zeros are read in the two components.

The logarithm exists exactly on the units, $Q_{\pm}\neq0$, and is

$$
\operatorname{Log}\breve Q=\frac{\operatorname{Log}(Q_{+})+\operatorname{Log}(Q_{-})}{2}
+j\,\frac{\operatorname{Log}(Q_{+})-\operatorname{Log}(Q_{-})}{2}
$$

for the principal branch. The kernel is the rank-two lattice $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$, so the principal logarithm is unique only in the principal diamond $\lvert\operatorname{Im}Q_{\log\blacktriangle}\rvert+\lvert\operatorname{Im}Q_{\log\blacktriangledown}\rvert\le\pi$. The values of the power are $\exp(s\operatorname{Log}\breve Q+s\kappa)$ with $\kappa$ in the kernel, and the equation $\breve R^{n}=\breve Q$ has $n^{2}$ solutions for a unit, in particular four square roots.

On the complex line the functions restrict to the complex ones, on the split-complex plane to the split-complex ones. The algebra is commutative, so no commutator correction occurs; the price of the richer algebra is the rank-two lattice of the logarithm and the two period lattices of the trigonometric functions.

**Formulas.**

| Function | Value | Domain |
|---|---|---|
| $\exp\breve Q$ | $e^{Q_{\blacktriangle}}(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$, equivalently $e^{Q_{\log\blacktriangle}}(\cosh Q_{\log\blacktriangledown}+j\sinh Q_{\log\blacktriangledown})$ for $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ | all $\breve Q$ |
| $\exp(\breve Q_1+\breve Q_2)$ | $\exp\breve Q_1\exp\breve Q_2$ | all $\breve Q_1,\breve Q_2$, the algebra being commutative |
| $\exp(i\theta)$ | $\cos\theta+i\sin\theta$ | $\theta\in\mathbb{R}$ |
| $\exp(ij\beta)$ | $\cos\beta+ij\sin\beta$ | $\beta\in\mathbb{R}$ |
| $\exp(j\phi)$ | $\cosh\phi+j\sinh\phi$ | $\phi\in\mathbb{R}$ |
| $\cos\breve Q,\ \sin\breve Q$ | $\cos Q_{\blacktriangle}\cos Q_{\blacktriangledown}-j\sin Q_{\blacktriangle}\sin Q_{\blacktriangledown}$, $\sin Q_{\blacktriangle}\cos Q_{\blacktriangledown}+j\cos Q_{\blacktriangle}\sin Q_{\blacktriangledown}$ | all $\breve Q$ |
| $\cosh\breve Q,\ \sinh\breve Q$ | $\cosh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}$, $\sinh Q_{\blacktriangle}\cosh Q_{\blacktriangledown}+j\cosh Q_{\blacktriangle}\sinh Q_{\blacktriangledown}$ | all $\breve Q$ |
| $\operatorname{Log}\breve Q$ | $\frac{\operatorname{Log}(Q_{+})+\operatorname{Log}(Q_{-})}{2}+j\frac{\operatorname{Log}(Q_{+})-\operatorname{Log}(Q_{-})}{2}$ | the units; analytic off $Q_{\pm}\in(-\infty,0]$ |
| $\log\breve Q$ | the same with a branch choice in each component | units, branch choice |
| $\ker\exp$ | $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$ | the period lattice |
| $\breve Q^{s}$ | $\exp(s\operatorname{Log}\breve Q+s\kappa)$ with $\kappa\in\ker\exp$ | units, branch choice |
| $\breve R$ with $\breve R^{n}=\breve Q$ | $n^{2}$ solutions for a unit | $n\ge1$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}$ | the reduced biquaternion algebra, basis $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ij=ji$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | an element, $Q_{\blacktriangle}$ scalar part, $Q_{\blacktriangledown}$ split part |
| $Q_{+}$, $Q_{-}$ | the two circular components |
| $\bar{\breve Q}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$ | the bar |
| $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | the reduced norm |
| $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$ | the squared Euclidean norm |
| $\breve Q_{\log}=Q_{\log\blacktriangle}+jQ_{\log\blacktriangledown}$ | a logarithm, with $Q_{\log\blacktriangle}=q_{\log\blacktriangle}+iq'_{\log\blacktriangle}=\ln\rho+i\alpha$ and $Q_{\log\blacktriangledown}=q_{\log\blacktriangledown}+iq'_{\log\blacktriangledown}=\phi+i\beta$ |
| $q_{\log\blacktriangle},q'_{\log\blacktriangle},q_{\log\blacktriangledown},q'_{\log\blacktriangledown}$ | the four real components of the logarithm: $\ln\rho,\alpha,\phi,\beta$ |
| $\exp\breve Q=e^{Q_{\blacktriangle}}(\cosh Q_{\blacktriangledown}+j\sinh Q_{\blacktriangledown})$ | the exponential |
| $\exp(j\phi)=\cosh\phi+j\sinh\phi$ | the hyperbolic exponential |
| $\exp(i\theta)=\cos\theta+i\sin\theta$ | the scalar elliptic exponential |
| $\exp(ij\beta)=\cos\beta+ij\sin\beta$ | the $ij$ elliptic exponential |
| $\operatorname{Log}\breve Q$ | the principal logarithm |
| $2\pi i\mathbb{Z}\oplus\pi i(1+j)\mathbb{Z}$ | the kernel of the exponential |
| $\lvert\operatorname{Im}Q_{\log\blacktriangle}\rvert+\lvert\operatorname{Im}Q_{\log\blacktriangledown}\rvert\le\pi$ | the principal diamond |
| $\sin\breve Q,\ \cos\breve Q,\ \sinh\breve Q,\ \cosh\breve Q$ | trigonometric and hyperbolic functions |
| $\breve Q^{s}$ | the power function |
| $\breve R$ | a root of $\breve R^{n}=\breve Q$ |
| $\eta_{1},\eta_{2}$ | $n$-th roots of unity of the two components |

## Further Reading

- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the exponential, the trigonometric functions and the logarithm of one complex variable.
- Lars V. Ahlfors, *Complex Analysis*, 3rd edition (McGraw-Hill, 1979), for the branch structure of the logarithm and the power functions.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the exponential and the elementary functions of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the reduction of the elementary functions.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the exponential of the hypercomplex algebras and the comparison with the division-algebra cases.
