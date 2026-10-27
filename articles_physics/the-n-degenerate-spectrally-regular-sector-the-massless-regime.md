# __The Massless Regime: Light Rays__

## Introduction

The cell $\Sigma_{01}$ is the set of elements with vanishing norm and non-vanishing vector square: $N=0$ and $B^2\neq0$. The element is a zero divisor, and it has two distinct eigenvalues, one of which is zero. It is a non-zero multiple of a primitive idempotent,

$$
\tilde Q=\kappa\,\tilde\Pi,
\qquad
\tilde\Pi^2=\tilde\Pi,
\qquad
\kappa=2Q_t\neq0,
$$

and its spectrum is $\{\kappa,0\}$. On the material slice it is the light cone minus the apex: a massless momentum, with one light-cone frequency zero and the other $2E/c$.

The physical content is the **light ray**: a rank-one element, a direction and a scale, one null mode and one frozen mode, no inverse and no generator. The article reads the cell, the idempotent, the zero divisor, the spectrum and the boundary. It proves nothing; the sector theorems are those of *The N-Degenerate, Spectrally Regular Sector*, and the cone is that of *The Zero-Divisor Cone and the Massless Spectrum*.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The definition, the five descriptions and the geometry of the cell | [The N-Degenerate, Spectrally Regular Sector](../articles_maths/the-n-degenerate-spectrally-regular-sector.html) |
| The zero-divisor cone, its rulings and the massless limit | [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html) |
| The primitive idempotents and the minimal left ideals | [The Minimal Left Ideals](../articles_maths/the-minimal-left-ideals.html) |
| The spectrum and the two-term writing | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| The independence of the two conditions | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html) |
| The four-vector dictionary and the light cone | [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The spectral reading of a four-momentum | [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html) |
| The indefinite form and the cone | [The Krein Form and the Indefinite Structure](the-krein-form-and-the-indefinite-structure.html) |

## The Cell

The cell is

$$
\Sigma_{01}=\{N=0,\ B^2\neq0\}
=\{Q_t^2+B^2=0,\ B^2\neq0\}.
$$

On the null cone $N=0$ one has $Q_t^2=-B^2$, so $B^2\neq0$ is equivalent to $Q_t\neq0$. The cell is the null cone minus the doubly degenerate cone:

$$
\Sigma_{01}=\mathcal N\setminus\mathcal S
=\{\kappa\tilde\Pi\ :\ \kappa\in\mathbb{C}^\times,\ \tilde\Pi^2=\tilde\Pi,\ \tilde\Pi\neq0,e_t\}.
$$

Every element of the cell is a non-zero complex multiple of a primitive idempotent. The scalar part is $c/2$, and the idempotent is recovered as

$$
\tilde\Pi=\frac{\tilde Q}{2Q_t}=\frac{\tilde Q}{c}.
$$

The cell is of real dimension six. It is the interior of the null cone in the sense of the cone's smooth part: the apex and the nilpotent directions are removed. Its closure is the full null cone, and the removed set is the cell $\Sigma_{00}$.

An element of the cell has the characteristic polynomial

$$
p_{\tilde Q}(X)=X(X-c),
\qquad
\lambda_+=\kappa,
\qquad
\lambda_-=0,
$$

with $\kappa=2Q_t\neq0$. The two eigenvalues are distinct, so the cell is spectrally regular; one of them is zero, so the element is not invertible. The spectral idempotents are

$$
e_+=\tilde\Pi=\frac{\tilde Q}{c},
\qquad
e_-=e_t-\tilde\Pi,
\qquad
e_+e_-=0,
\qquad
e_++e_-=e_t,
$$

and the spectral decomposition has one term,

$$
\tilde Q=\kappa\,\tilde\Pi+0\,e_-.
$$

This is the only cell in which the spectrum is regular and one coefficient is zero.

## The Light Ray

### The Idempotent

The idempotent $\tilde\Pi$ is primitive: it is not a sum of two non-zero orthogonal idempotents. In the matrix model it is a rank-one projector. Its left ideal

$$
S_+=\mathbb{B}\tilde\Pi
$$

is a minimal left ideal, a complex plane. The element acts on it as the scalar $\kappa$:

$$
\tilde Q\,X=\kappa\,X
\qquad
(X\in S_+).
$$

On the complementary ideal

$$
S_-=\mathbb{B}e_-,
\qquad
e_-=e_t-\tilde\Pi,
$$

the element acts as zero:

$$
\tilde Q\,X=0
\qquad
(X\in S_-).
$$

The left multiplication $L_{\tilde Q}$ therefore has a two-dimensional image $S_+$ and a two-dimensional kernel $S_-$. The element itself is rank one in the matrix model; the operator is a projection onto a plane followed by the scalar $\kappa$.

### The Reading

The structure is the algebraic form of a **light ray**:

- **A direction.** The idempotent is the direction. It is a point of the projective null cone, the celestial sphere of the momentum. The direction is the only frame data the element carries.
- **A scale and a phase.** The coefficient $\kappa$ is complex. Its modulus is the energy scale, and its phase is a gauge: multiplying $\tilde\Pi$ by a phase and $\kappa$ by the inverse phase gives the same element. The physical ray has a direction and an energy, not a phase.
- **One null mode.** The eigenvalue $\kappa$ is the non-zero light-cone frequency, $2E/c$ on the material slice. The eigenvalue $0$ is the frozen mode. The two-term writing has one term because the second coefficient vanishes.
- **No inverse.** The element is a zero divisor: there is a non-zero $X$ with $\tilde Q X=0$, and no $\tilde Q^{-1}$. The process has no inverse; the kernel is the information that the element annihilates.
- **No generator.** The exponential is invertible, so a non-invertible element has no logarithm. The light ray has no one-parameter group and no generator in the algebra.

### The Massless Limit

On the material slice, the massless momentum is

$$
\tilde P=i\frac{E}{c}e_t+\frac{E}{c}\,\hat p,
\qquad
B=\frac{E}{c},
\qquad
N=0,
$$

with $\hat p$ a real unit vector. The idempotent is

$$
\tilde\Pi=\frac{1}{2}\left(e_t-i\hat p\right).
$$

The idempotent is the null flag along $\hat p$; the opposite sign belongs to the opposite null direction. The spectrum is

$$
\lambda_+=2i\frac{E}{c},
\qquad
\lambda_-=0,
$$

and the spectral writing is one term,

$$
\tilde P=2i\frac{E}{c}\,\tilde\Pi.
$$

The massless limit of the Doppler pair is a limit of the coefficients, not a failure of the decomposition: $\nu_-\to0$ and $\nu_+\to2E/c$. The cell is the boundary of the two-mode cell at $N=0$, and the limit is continuous in the element.

The idempotent is not a Hermitian pure state on the material slice. It is a null flag: $\tilde\Pi^*\neq\tilde\Pi$ in general, and its matrix is rank one but not self-adjoint. The physical reading is a light ray, not a density matrix.

## The Zero Divisor

The cell is the smooth part of the zero-divisor cone. The vanishing of the norm is the vanishing of the product with the conjugate:

$$
\tilde Q\tilde Q^{\natural}=N e_t=0.
$$

The element is a zero divisor, and its annihilator is the complementary ideal:

$$
\tilde Q\,S_-=0,
\qquad
\dim_{\mathbb{C}}S_-=2.
$$

The reading is information loss. The element maps the four-dimensional algebra onto a two-dimensional plane and annihilates the other two dimensions. The kernel is not a defect of the description; it is the structure of the ray. A light ray has a direction and a scale, and it carries no longitudinal mode.

The cone is ruled by the null lines $\mathbb{C}\tilde Q$. Each line is a ray; the idempotent is the normalised representative. The rulings are the fibers of the projection to the celestial sphere, and the scale is the coordinate along the ruling. The cell is the total space of a bundle over the celestial sphere with fiber $\mathbb{C}^\times$.

## Products and the Boundary

The cell is not closed under products. The product of two elements of the cell is null,

$$
\Sigma_{01}\cdot\Sigma_{01}\subseteq\mathcal N=\Sigma_{01}\cup\Sigma_{00},
$$

and both outcomes occur. The product of two scaled idempotents is a scaled idempotent when the idempotents compose to an idempotent, and zero when they are orthogonal. The product is never a unit.

The boundary of the cell is the doubly degenerate cell $\Sigma_{00}$: the apex and the nilpotent directions. The cell is the boundary of the unit group at $N=0$: a path in $\Sigma_{11}$ that reaches $N=0$ lands here, unless it also reaches $B=0$, in which case it lands in $\Sigma_{00}$.

The cell is the interior of the null cone minus its singular part. Its closure is the full cone; the removed set is the set of elements with one mode, which is the other degenerate cell.

## Physical Interpretations

- **The cell is a light ray.** $N=0$ and $B\neq0$: a massless momentum, one non-zero light-cone frequency and one zero frequency, a direction and an energy.
- **The element is a scaled idempotent.** The idempotent is the direction, the coefficient is the scale and the phase. The ray is the projective class of the element.
- **The zero divisor is information loss.** The element annihilates a two-dimensional ideal and maps onto a two-dimensional ideal. The longitudinal mode is absent.
- **The spectrum has one zero.** The two-term writing survives with one term; the massless limit is a limit of coefficients, not a breakdown of the spectral decomposition.
- **There is no inverse and no generator.** The element is not invertible, and the exponential is invertible, so no logarithm exists. The ray is not a reversible process.
- **The idempotent is a null flag, not a state.** On the material slice it is not Hermitian; it is a rank-one projector in the matrix model, not a density matrix. The physical reading is a ray, not a pure state.
- **The cone is ruled.** The rays are the null lines; the celestial sphere is the base, the scale is the fiber. The cell is the smooth part of the cone.
- **The cell is the boundary of the unit group.** A massive element reaching the light cone lands here; a massless element is the limit of a moving massive one.

## Limits

The light-ray reading needs the material slice and the massless dispersion relation $E=\lvert\vec p\rvert c$. In the full algebra the cell is the null cone minus the spectral cone, and the names energy and momentum are readings of $Q_t$ and $B$.

The idempotent is not a physical pure state on the material slice. It is a null flag, and its matrix is not self-adjoint. The pure states of the informational sector are the Hermitian idempotents, which lie in a different cell.

The zero divisor is not a division by zero in a physical theory. It is a non-invertible element; the algebra supplies the kernel and the image, not a physical singularity.

No dynamics is supplied. The cell says what a massless element is at an instant; it does not say how it propagates, and it does not supply a wave equation.

The cell is not a particle count. One zero eigenvalue is one frozen mode, not an empty state and not a second particle.

## Summary

- $\Sigma_{01}=\{N=0,\ B^2\neq0\}$ is the null cone minus the spectral cone: zero divisors with two distinct eigenvalues, of real dimension six.
- Every element is a non-zero multiple of a primitive idempotent, $\tilde Q=\kappa\tilde\Pi$ with $\kappa=2Q_t\neq0$, and the spectrum is $\{\kappa,0\}$.
- The idempotent is the direction, the coefficient is the scale and phase; the ray is the projective class.
- The left multiplication has a two-dimensional image and a two-dimensional kernel; the element is rank one in the matrix model.
- The element is not invertible, has no logarithm and no generator; the process is not reversible.
- On the material slice it is a massless momentum: one light-cone frequency zero, the other $2E/c$; the massless limit of the Doppler pair.
- The idempotent is a null flag, not a Hermitian pure state; the physical reading is a ray, not a density matrix.
- The cone is ruled by the null lines; the cell is the smooth part, with the doubly degenerate cell as boundary.
- The cell supplies no dynamics, no wave equation and no particle count.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Sigma_{01}$ | the cell $N=0$, $B^2\neq0$ |
| $\tilde Q=\kappa\tilde\Pi$ | the scaled idempotent |
| $\kappa=2Q_t$ | the non-zero eigenvalue, the complex scale |
| $\lambda_+=\kappa,\ \lambda_-=0$ | the spectrum |
| $e_+=\tilde\Pi,\ e_-=e_t-\tilde\Pi$ | the spectral idempotents |
| $S_+=\mathbb{B}\tilde\Pi$ | the image, a minimal left ideal |
| $S_-=\mathbb{B}e_-$ | the kernel, the complementary ideal |
| $\mathcal N=\{N=0\}$ | the null cone |

## Further Reading

- [The Four Regimes of an Element: Mass and Motion](the-four-regimes-of-an-element-mass-and-motion.html), for the partition and the other three cells.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone, its rulings and the massless limit.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the massless limit of the Doppler pair.
- [The Vacuum and the Nilpotent Ladder](the-n-degenerate-spectrally-degenerate-sector-the-vacuum-and-the-nilpotent-ladder.html), for the boundary of the cell.
- [Mass in Motion: The Two-Mode Regime](the-n-regular-spectrally-regular-sector-mass-in-motion.html), for the cell whose boundary this is.
- [The Minimal Left Ideals](../articles_maths/the-minimal-left-ideals.html), for the primitive idempotents and the spinor spaces.
