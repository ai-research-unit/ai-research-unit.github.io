# __The N-Degenerate, Spectrally Regular Sector: The Massless Regime__

## Introduction

The cell $\Sigma_{01}$ is the set of elements with vanishing norm and non-vanishing vector square: $N=0$ and $B^2\neq0$. The element is a zero divisor, and it has two distinct eigenvalues, one of which is zero. It is a non-zero multiple of a primitive idempotent,

$$
\tilde Q=\kappa\,\tilde\Pi,
\qquad
\tilde\Pi^2=\tilde\Pi,
\qquad
\kappa=2Q_t\neq0,
$$

and its spectrum is $\{\kappa,0\}$. On the material slice it is the light cone minus the apex: a massless momentum, with one light-cone eigenvalue zero and the other $2iE/c$.

The physical content is the **light ray**: a rank-one element, a direction and a scale, one non-zero light-cone mode and one frozen mode, no inverse and no generator. The article reads the cell, the idempotent, the zero divisor, the spectrum and the boundary. It proves nothing; the sector theorems are those of *The N-Degenerate, Spectrally Regular Sector*, and the cone is that of *The Zero-Divisor Cone and the Massless Spectrum*.

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

Every element of the cell is a non-zero complex multiple of a primitive idempotent. The scalar part is $\kappa/2$, and the idempotent is recovered as

$$
\tilde\Pi=\frac{\tilde Q}{2Q_t}=\frac{\tilde Q}{\kappa}.
$$

The cell is of real dimension six. It is the null cone with the apex and the nilpotent directions removed. Its closure is the full null cone, and the removed set is the cell $\Sigma_{00}$.

An element of the cell has the characteristic polynomial

$$
p_{\tilde Q}(X)=X(X-\kappa),
\qquad
\lambda_+=\kappa,
\qquad
\lambda_-=0,
$$

with $\kappa=2Q_t\neq0$. The two eigenvalues are distinct, so the cell is spectrally regular; one of them is zero, so the element is not invertible. The spectral idempotents are

$$
e_+=\tilde\Pi=\frac{\tilde Q}{\kappa},
\qquad
e_-=e_t-\tilde\Pi,
\qquad
e_+e_-=0,
\qquad
e_++e_-=e_t.
$$

The spectral decomposition is the two-term writing with a vanishing second coefficient,

$$
\tilde Q=\kappa\,\tilde\Pi+0\,e_-,
$$

and the idempotent $e_-$ is present and non-trivial. This is the only cell in which the spectrum is regular and one coefficient is zero.

## The Light Ray

### The Idempotent

The idempotent $\tilde\Pi$ is primitive: it is not a sum of two non-zero orthogonal idempotents. In the matrix model it is a rank-one idempotent. Let $\vec\Upsilon_\pm$ be the normalised nilpotents of the Peirce pair, with

$$
\vec\Upsilon_+\vec\Upsilon_-=e_-,
\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi,
\qquad
e_-=e_t-\tilde\Pi.
$$

The two spinor spaces are

$$
S_+=\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}e_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}e_-.
$$

Each is a minimal left ideal, a complex plane. On each, the left action is $\operatorname{diag}(\kappa,0)$:

$$
\tilde Q\,\tilde\Pi=\kappa\tilde\Pi,
\qquad
\tilde Q\,\vec\Upsilon_+=0,
\qquad
\tilde Q\,\vec\Upsilon_-=\kappa\vec\Upsilon_-,
\qquad
\tilde Q\,e_-=0.
$$

The left action is therefore $\kappa$ on the line of $\tilde\Pi$ and on the nilpotent line of $S_-$, and zero on the line of $e_-$ and on the nilpotent line of $S_+$; on each spinor space it is $\operatorname{diag}(\kappa,0)$ in the displayed basis. The right action is different: $R_{\tilde Q}$ is $\kappa$ on all of $S_+$ and zero on $S_-$,

$$
\tilde\Pi\,\tilde Q=\kappa\tilde\Pi,
\qquad
\vec\Upsilon_+\,\tilde Q=\kappa\vec\Upsilon_+,
\qquad
\vec\Upsilon_-\,\tilde Q=0,
\qquad
e_-\,\tilde Q=0.
$$

Consequently $L_{\tilde Q}$ has image the right ideal $\tilde\Pi\mathbb{B}$ (spanned by $\tilde\Pi$ and $\vec\Upsilon_-$) and kernel the plane spanned by $\vec\Upsilon_+$ and $e_-$; $R_{\tilde Q}$ has image $S_+$ and kernel $S_-$. The element itself is rank one in the matrix model; each one-sided multiplication is a projection onto a plane followed by the scalar $\kappa$.

### The Reading

The structure is the algebraic form of a **light ray**:

- **A direction.** The idempotent is the direction. It is a point of the complex projective null quadric away from the nilpotent conic $Q_t=0$; on the real material slice this is the celestial sphere of the momentum. The direction is the only frame data the element carries.
- **A scale and a phase.** The coefficient $\kappa$ is complex and fixed by the element, $\kappa=2Q_t$. On the material slice $\kappa=2iE/c$: its modulus is the energy scale and its phase is the fixed factor $i$ of the anti-Hermitian sector. The phase is not a gauge — rescaling $\tilde\Pi$ by a phase destroys idempotence — and a complex rescaling of $\tilde Q$ changes the element, although it leaves the projective null line unchanged. The physical momentum has a direction and an energy; the phase attached to a spinor representative is the little-group phase, not a gauge of $\tilde Q$.
- **One null mode.** The eigenvalue $\kappa$ is the non-zero light-cone eigenvalue, $2iE/c$ on the material slice. The eigenvalue $0$ is the frozen mode. The spectral writing has two terms, with the second coefficient zero; the idempotent $e_-$ is present but carries weight zero.
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

The idempotent is the Hermitian rank-one projector along $\hat p$; the opposite sign belongs to the opposite null direction. The spectrum is

$$
\lambda_+=2i\frac{E}{c},
\qquad
\lambda_-=0,
$$

and the non-zero term of the spectral writing is

$$
\tilde P=2i\frac{E}{c}\,\tilde\Pi,
$$

with the other coefficient zero.

The massless limit of the Doppler pair is a limit of the eigenvalues, not a failure of the decomposition: $\lambda_-\to0$ and $\lambda_+\to2iE/c$. The cell is the boundary of the two-mode cell at $N=0$, and the limit is continuous in the element.

On the material slice the idempotent is Hermitian: $\tilde\Pi=\tfrac12(e_t-i\hat p)$ satisfies $\tilde\Pi^*=\tilde\Pi$, and it is rank one and trace one. It is a pure boundary state of the informational sector: a rank-one Hermitian density matrix of zero norm. The element $\tilde P=2iE/c\,\tilde\Pi$ is anti-Hermitian, so the momentum is not a state; the state is the idempotent, and the momentum is an imaginary multiple of it.

## The Zero Divisor

The cell is the zero-divisor cone with its vertex and its nilpotent directions removed. The vanishing of the norm is the vanishing of the product with the conjugate:

$$
\tilde Q\tilde Q^{\natural}=N e_t=0.
$$

The element is a zero divisor. Its left annihilator is the plane

$$
\ker L_{\tilde Q}=\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}e_-,
\qquad
\dim_{\mathbb{C}}\ker L_{\tilde Q}=2,
$$

while its right annihilator is $S_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}e_-$. The two planes meet in the line $\mathbb{C}e_-$.

The reading is information loss. The left multiplication maps the four-dimensional algebra onto the right ideal $\tilde\Pi\mathbb{B}$, spanned by $\tilde\Pi$ and $\vec\Upsilon_-$, and annihilates the plane spanned by $\vec\Upsilon_+$ and $e_-$. The kernel is not a defect of the description; it is the structure of the ray. A light ray has a direction and a scale, and it carries no longitudinal mode.

The cone is ruled by the null lines $\mathbb{C}\tilde Q$. Each line is a ray; the idempotent is the normalised representative. The null lines are the fibers of the projection to the complex projective null quadric, and the scale is the coordinate along the fiber. The cell is the total space of a $\mathbb{C}^\times$-bundle over the complement of the nilpotent conic ($Q_t=0$) in that quadric; on the real material slice the base is the celestial sphere.

## Products and the Boundary

The cell is not closed under products. The product of two elements of the cell is null,

$$
\Sigma_{01}\cdot\Sigma_{01}\subseteq\mathcal N=\Sigma_{01}\cup\Sigma_{00},
$$

and all three outcomes occur. The product of two scaled idempotents can be a scaled idempotent (when the product is a non-zero idempotent), zero (when the idempotents are orthogonal), or a non-zero nilpotent (when the product squares to zero but does not vanish). The product is never a unit.

The boundary of the cell is the doubly degenerate cell $\Sigma_{00}$: the apex and the nilpotent directions. The cell lies on the boundary of the unit group at $N=0$: a path in $\Sigma_{11}$ that reaches $N=0$ lands here, unless it also reaches $B=0$, in which case it lands in $\Sigma_{00}$.

The cell is the null cone minus its vertex and its nilpotent directions. Its closure is the full cone; the removed set is the doubly degenerate cell.

## Physical Interpretations

- **The cell is a light ray.** $N=0$ and $B\neq0$: a massless momentum, one non-zero light-cone frequency and one zero frequency, a direction and an energy.
- **The element is a scaled idempotent.** The idempotent is the direction, the coefficient is the complex scale, and the ray is the projective class of the element.
- **The zero divisor is information loss.** The left multiplication annihilates a two-dimensional right ideal and maps onto a two-dimensional right ideal. The longitudinal mode is absent.
- **The spectrum has one zero.** The two-term writing survives with a vanishing second coefficient; the massless limit is a limit of eigenvalues, not a breakdown of the spectral decomposition.
- **There is no inverse and no generator.** The element is not invertible, and the exponential is invertible, so no logarithm exists. The ray is not a reversible process.
- **The idempotent is the pure boundary state.** On the material slice it is Hermitian, rank one and trace one; the momentum is an imaginary multiple of it, so the element is anti-Hermitian while the state is Hermitian. The physical reading is a ray with an energy; the state is the idempotent.
- **The cone is ruled.** The rays are the null lines; the complex projective null quadric is the base, the real celestial sphere is its material slice, and the scale is the fiber. The cell is the generic part of the cone.
- **The cell lies on the boundary of the unit group.** A massive element reaching the light cone lands here unless it also reaches the nilpotent directions; a massless element is the limit of a moving massive one.

## Limits

The light-ray reading needs the material slice and the massless dispersion relation $E=\lvert\vec p\rvert c$. In the full algebra the cell is the null cone minus the spectral cone, and the names energy and momentum are readings of $Q_t$ and $B$.

On the material slice the idempotent is a Hermitian pure state, while the element is an imaginary multiple of it and is not itself a state. Over the complex algebra a general primitive idempotent need not be Hermitian, and then it is a null flag rather than a physical state.

The zero divisor is not a division by zero in a physical theory. It is a non-invertible element; the algebra supplies the kernel and the image, not a physical singularity.

No dynamics is supplied. The cell says what a massless element is at an instant; it does not say how it propagates, and it does not supply a wave equation.

The cell is not a particle count. One zero eigenvalue is one frozen mode, not an empty state and not a second particle.

## Summary

- $\Sigma_{01}=\{N=0,\ B^2\neq0\}$ is the null cone minus the spectral cone: zero divisors with two distinct eigenvalues, of real dimension six.
- Every element is a non-zero multiple of a primitive idempotent, $\tilde Q=\kappa\tilde\Pi$ with $\kappa=2Q_t\neq0$, and the spectrum is $\{\kappa,0\}$.
- The idempotent is the direction, the coefficient is the complex scale, and the ray is the projective class.
- The left multiplication has a two-dimensional image and a two-dimensional kernel; the element is rank one in the matrix model.
- The element is not invertible, has no logarithm and no generator; the process is not reversible.
- On the material slice it is a massless momentum: one light-cone eigenvalue zero, the other $2iE/c$; the massless limit of the Doppler pair.
- On the real slice the idempotent is a Hermitian pure boundary state; the momentum is an imaginary multiple of it, and a general complex idempotent is a null flag.
- The cone is ruled by the null lines; the cell is the generic part, with the doubly degenerate cell as boundary.
- The cell supplies no dynamics, no wave equation and no particle count.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Sigma_{01}$ | the cell $N=0$, $B^2\neq0$ |
| $\tilde Q=\kappa\tilde\Pi$ | the scaled idempotent |
| $\kappa=2Q_t$ | the non-zero eigenvalue, the complex scale |
| $\lambda_+=\kappa,\ \lambda_-=0$ | the spectrum |
| $e_+=\tilde\Pi,\ e_-=e_t-\tilde\Pi$ | the spectral idempotents |
| $S_+=\mathbb{B}\tilde\Pi$ | the first spinor space, a minimal left ideal |
| $S_-=\mathbb{B}e_-$ | the second spinor space, a minimal left ideal, and the right annihilator |
| $\vec\Upsilon_\pm$ | the normalised nilpotents, $\vec\Upsilon_+\vec\Upsilon_-=e_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi$ |
| $\tilde\Pi\mathbb{B}$ | the image of $L_{\tilde Q}$, a minimal right ideal |
| $\ker L_{\tilde Q}$ | the left annihilator, spanned by $\vec\Upsilon_+$ and $e_-$ |
| $\mathcal N=\{N=0\}$ | the null cone |

## Further Reading

- [The Four Regimes of an Element: Mass and Motion](the-four-regimes-of-an-element-mass-and-motion.html), for the partition and the other three cells.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone, its rulings and the massless limit.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the massless limit of the Doppler pair.
- [The N-Degenerate, Spectrally Degenerate Sector: The Vacuum and the Nilpotent Ladder](the-n-degenerate-spectrally-degenerate-sector-the-vacuum-and-the-nilpotent-ladder.html), for the boundary of the cell.
- [The N-Regular, Spectrally Regular Sector: Mass in Motion](the-n-regular-spectrally-regular-sector-mass-in-motion.html), for the cell whose boundary this is.
- [The Minimal Left Ideals](../articles_maths/the-minimal-left-ideals.html), for the primitive idempotents and the spinor spaces.
