# __The Exponential Word and Its Boundary__

## Introduction

Every biquaternion off the zero-divisor cone is an ordered product of four exponentials: a positive scale, a central phase, a Hermitian boost and a real quaternion rotor. The product carries eight real parameters, the real dimension of the algebra, and it is a parametrization of the group of units.

The parametrization fails in two ways, and they are different. The four exponents do not add: the exponential of their sum is not the product, because the boost and the rotor do not commute. And the parametrization does not reach the cone: on the cone the scale collapses and the rapidity diverges, so the word has boundary values rather than a value.

The article reads the word, the defect and the boundary. The decomposition, the defect and the boundary limits are those of *Exponential Polar Decomposition of Biquaternions* and *The Polar Decomposition of Biquaternions*. The article owns the physical reading and its limits.

**Placement.** The article belongs to the Algebra block of the category, after *The Polar Decomposition and Its Three Pairings* and before *The Exponential, the Logarithm and the Generator*. It is the boundary companion of the polar article: that article reads the four factors in the interior, and this one reads what happens at the edge.

**Conventions.** The word is

$$
\tilde Q=r\,e^{i\alpha}\,\tilde B\,\tilde u_{\mathrm r},
\qquad
\tilde B=\exp\left(i\frac{\psi}{2}\vec u_{\mathrm b}\right),
\qquad
\tilde u_{\mathrm r}=\exp\left(\frac{\theta}{2}\vec u_{\mathrm r}\right),
$$

with $r>0$, $\alpha\in(-\pi/2,\pi/2]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ unit real pure quaternions, the roots of $-e_t$. The axis sphere is the set of such $\vec u$. The norm is $\langle\tilde Q\rangle_{\natural}=r^2e^{2i\alpha}$, and the element is a unit exactly when $r\neq0$.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The four factors, their ranges and the uniqueness of the word | [The Polar Decomposition of Biquaternions](../articles_maths/modulus-unit-polar-decomposition-of-biquaternions.html) |
| The exponential word, the defect and the single logarithm | [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html) |
| The kernel, the fibre and the section of the word map | [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html) |
| The two strata of the zero-divisor cone | [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html) |
| The minimal idempotents and the pure roots of $+1$ | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| The exponential closed forms and the kernel | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |

## The Word

The four factors and their ranges are collected in one table.

| # | Factor | Name | Exponent | Range | Real dimension | Action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | $r$ | scale | — | $r>0$ | $1$ | dilation by $r^2$ |
| 2 | $e^{i\alpha}$ | central phase | $i\alpha$ | $\alpha\in(-\pi/2,\pi/2]$ | $1$ | multiplication by a scalar |
| 3 | $\tilde B=e^{i\psi\vec u_{\mathrm b}/2}$ | boost | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\psi\ge0$ | $3$ | congruence by $\tilde B$ |
| 4 | $\tilde u_{\mathrm r}=e^{\theta\vec u_{\mathrm r}/2}$ | rotor | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$ | $3$ | conjugation by $\tilde u_{\mathrm r}$ |

The parameters count $1+1+3+3=8$, the real dimension of $\mathbb{B}$. The map from the parameter space to the units is surjective. It is not injective: the boost axis is undefined at $\psi=0$, the rotor axis is undefined at $\theta=0$, and the phase branch identifies the two square roots of the norm. Apart from those degeneracies, the word is unique once the branch is fixed.

The word is a **section of the word map**, not a section of the exponential. It cuts the fibre of the parameter-to-element map to one point, up to the axis degeneracies. It does not cut the fibre of the exponential: the four exponents sum to the formal exponent, and that sum is not a logarithm.

## The Defect

The formal exponent is the sum of the four exponents,

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}.
$$

It is the element that the quaternion case would call the logarithm. Here it is not one:

$$
\exp\left(\tilde Q_{\log}\right)\neq\tilde Q
\qquad\text{unless}\qquad
[\vec u_{\mathrm b},\vec u_{\mathrm r}]=0
\quad\text{or}\quad
\psi\theta=0.
$$

The defect is the Baker–Campbell–Hausdorff correction. To first order,

$$
\operatorname{Log}\left(\exp\tilde H\exp\tilde K\right)
=\tilde H+\tilde K+\frac12[\tilde H,\tilde K]+\cdots,
$$

and for $\tilde H=i\frac{\psi}{2}\vec u_{\mathrm b}$ and $\tilde K=\frac{\theta}{2}\vec u_{\mathrm r}$ the first correction is

$$
\frac12[\tilde H,\tilde K]
=\frac{i\psi\theta}{4}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r},
$$

which is again a boost. The sum of a boost exponent and a rotor exponent is corrected by another boost, and the true logarithm is not the sum of the four exponents.

| Case | Defect | Why |
| --- | --- | --- |
| axes parallel or antiparallel | zero | the exponents commute |
| $\psi=0$ or $\theta=0$ | zero | one factor is the identity |
| general axes, $\psi\theta\neq0$ | nonzero | the commutator is a boost |

The defect is not a rounding effect. It is the statement that the word is not a homomorphism: the product of two words is not the word of the product, and the four parameters of a product are not the sums of the four parameters of the factors. The word is a parametrization, and the group law in those parameters carries the correction.

## The Cone

The word is defined if and only if the element is a unit. On the cone the scale vanishes, the rapidity diverges, and the word has no value. The cone has two strata.

| Stratum | Condition | Normal form | Real dimension | What it is |
| --- | --- | --- | --- | --- |
| idempotent | $Q_t\neq0$ | $\tilde Q=2Q_t\tilde\Pi$, $\tilde\Pi^2=\tilde\Pi$ | $6$ | a complex multiple of a minimal idempotent |
| nilpotent | $Q_t=0$ | $\tilde Q=N$, $N^2=0$ | $4$ | a lightlike displacement |

The idempotent stratum is open and dense in the cone; the nilpotent stratum is a closed subvariety of codimension two and lies in its closure. The two are disjoint, and the scalar part distinguishes them pointwise.

The two strata are the two ways a word can degenerate. The idempotent stratum is the limit of a boost that diverges while the scale collapses; the nilpotent stratum is the limit of a unipotent line after rescaling.

## The Boundary Limits

Take a unit complex number $\zeta$, a scale $R>0$, and the family

$$
\tilde Q(\psi)=R\,e^{-\psi/2}\,\zeta\,e^{i\psi/2\,\vec u_{\mathrm b}}\,\tilde u_{\mathrm r},
\qquad
\psi>0.
$$

Every member is a unit, and the limit is

$$
\tilde Q(\psi)\longrightarrow
\frac{R\zeta}{2}\left(e_t+i\vec u_{\mathrm b}\right)\tilde u_{\mathrm r}
\qquad(\psi\to\infty).
$$

The limit is a nonzero null element of rank one. Its stratum is decided by the rotor. Write

$$
\tilde u_{\mathrm r}=a\,e_t+b\,\vec u_{\mathrm b}+\tilde u_\perp,
\qquad
a,b\in\mathbb{R},
\qquad
\tilde u_\perp\ \text{orthogonal to}\ \vec u_{\mathrm b}.
$$

Then the trace of the limit is $R\zeta(a-ib)$, and

| Rotor condition | Limit | Stratum |
| --- | --- | --- |
| $a-ib\neq0$ | a nonzero complex multiple of a minimal idempotent | idempotent |
| $a-ib=0$, that is $a=b=0$ | a nonzero nilpotent | nilpotent |

The second row is the case in which the rotor anticommutes with the boost axis. The first is the case in which it does not. The relative orientation of the boost and the rotor therefore decides which stratum the boundary value lands on, and the rate is the same for both.

The norm of the family is

$$
\langle\tilde Q(\psi)\rangle_{\natural}=R^2e^{-\psi}\zeta^2,
$$

so the distance to the cone is exponential in the rapidity. The word approaches the boundary along the exponential coordinate line of the boost, with the scale line compensating. The boost is the non-compact factor that drives the word to the boundary, and the scale is the factor that keeps the element finite.

## The Exponential Limit

The idempotents are not values of the exponential, because every exponential is a unit and an idempotent is not. They are limits of values:

$$
\tilde\Pi_+=\frac12\left(e_t+i\vec u\right)
=\lim_{\psi\to\infty}\frac{\exp\left(i\frac{\psi}{2}\vec u\right)}{2\cosh\frac{\psi}{2}}
=\lim_{\psi\to\infty}e^{-\psi/2}\exp\left(i\frac{\psi}{2}\vec u\right).
$$

The idempotent is the direction of an infinite boost, with the scale removed. The nilpotent stratum has its own version. For $N^2=0$,

$$
\exp(tN)=e_t+tN
$$

for every complex $t$, a unipotent line. The line is invertible for every finite $t$ and tends to infinity with $t$; it never reaches $N$. The rescaled limit does:

$$
N=\lim_{t\to\infty}\frac{\exp(tN)-e_t}{t}.
$$

The two strata are therefore reached only at infinity: the idempotent by the divergence of the boost, the nilpotent by the rescaled divergence of the unipotent line.

## Physical Readings

- **The word is a parametrization of the units.** The four factors are the scale, the phase, the rapidity and the rotation. The reading is the physical description of an element in eight real numbers, with the boost stored with half its rapidity and acting twice.
- **The defect is the non-additivity of generators.** The four exponents do not add because a boost and a rotation do not commute. The reading is that the generator of a product is not the sum of the generators, and the correction is a boost.
- **The cone is the massless wall.** The scale collapses and the rapidity diverges as the element approaches the null cone. The reading is the absence of a rest frame at the speed of light, and the word's failure is the same failure as the boost parametrisation at $\beta=1$.
The physical limit that realises the theorem, with the mass and the energy of the massive family, is [The Massless Limit as a Boundary Value of the Polar Word](the-massless-limit-as-a-boundary-value-of-the-polar-word.html).

- **The two strata are two kinds of boundary point.** The idempotent stratum is a complex multiple of a minimal idempotent, the algebraic form of the photon; the nilpotent stratum is a lightlike displacement, not a four-momentum. The reading is the massless spectrum's two boundary behaviours, and they must not be identified.
- **The stratum is selected by the rotor, not by the rate.** The same divergence reaches an idempotent or a nilpotent according to the relative orientation of the rotor and the boost axis. The reading is that the boundary value depends on the path, not only on the point.
- **The rate is not selected by the algebra.** The family can approach the cone at any exponential rate that keeps $re^{\psi/2}$ finite. The reading is that the algebra supplies the boundary values, not the approach.

## Limits

The word is not a homomorphism. The product of two words is not the word of the product, and the four parameters of a product are not the sums of the four parameters. The defect is the Baker–Campbell–Hausdorff correction, and it is not a rounding effect.

The boundary value is not a value. The word has no continuous extension to the cone, and the limit depends on the path. A statement about a boundary point is a statement about a family, not about the point alone.

The word is defined off the cone and nowhere on it. The failure is the absence of a rest frame, not a singularity of the algebra.

The branch $\alpha\in(-\pi/2,\pi/2]$ is a convention. The other square root of the norm is the same element with the other branch, and the choice is not physical.

The algebra supplies no rate, no dynamics and no massless particle. It supplies the parametrization, the defect, the two strata and the boundary values. The rate, the path and the identification of a stratum with a physical particle are supplied by the model, not by the algebra.

## Summary

- Every unit is $r e^{i\alpha}\tilde B\tilde u_{\mathrm r}$, with $1+1+3+3=8$ real parameters.
- The word is surjective onto the units and not injective at the degenerate axes; it is a section of the word map, not of the exponential.
- The formal exponent is the sum of the four exponents, and its exponential is not the element; the defect is the Baker–Campbell–Hausdorff correction, whose first term is a boost.
- The defect vanishes when the boost and rotor axes commute or when one of the two parameters vanishes.
- The word is defined off the zero-divisor cone; on the cone the scale collapses and the rapidity diverges.
- The cone has two strata: the idempotent stratum, a complex multiple of a minimal idempotent, and the nilpotent stratum, a square-zero lightlike displacement.
- The boundary limit of the family $R e^{-\psi/2}\zeta e^{i\psi\vec u_{\mathrm b}/2}\tilde u_{\mathrm r}$ is $\frac{R\zeta}{2}(e_t+i\vec u_{\mathrm b})\tilde u_{\mathrm r}$; it is an idempotent when the rotor does not anticommute with the boost axis and a nilpotent when it does.
- The rate of approach is exponential and is not selected by the algebra.
- The idempotent is the direction of an infinite boost; the nilpotent is the rescaled limit of the unipotent line.
- The word is a parametrization, not a homomorphism, and the boundary value is not a value.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $r$ | the positive scale, $r=\lvert N\rvert^{1/2}$ |
| $\alpha$ | the central phase, $\alpha=\tfrac12\arg N\in(-\pi/2,\pi/2]$ |
| $\tilde B=e^{i\psi\vec u_{\mathrm b}/2}$ | the Hermitian positive boost factor |
| $\tilde u_{\mathrm r}=e^{\theta\vec u_{\mathrm r}/2}$ | the unit real quaternion rotor |
| $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$ | the boost and rotor axes, unit real pure quaternions |
| $\psi$, $\theta$ | the stored rapidity and the rotation angle |
| $\tilde Q_{\log}$ | the formal exponent, the sum of the four exponents |
| $\tilde\Pi=\tfrac12(e_t+\vec\Xi)$ | a minimal idempotent, $\vec\Xi^2=e_t$ |
| $N$ | a nonzero nilpotent, $N^2=0$ |

## Further Reading

- [The Polar Decomposition of Biquaternions](../articles_maths/modulus-unit-polar-decomposition-of-biquaternions.html), for the four factors, their ranges and the uniqueness.
- [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html), for the defect, the boundary limits and the two strata.
- [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html), for the exponential and the kernel.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the minimal idempotents.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the physical reading of the four factors in the interior.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the two strata read physically.
- [The Exponential, the Logarithm and the Generator](the-exponential-the-logarithm-and-the-generator.html), for the logarithm side of the same boundary.
