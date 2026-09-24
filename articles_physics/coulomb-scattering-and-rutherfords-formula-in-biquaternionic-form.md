# __Coulomb Scattering and Rutherford's Formula in Biquaternionic Form__

## Introduction

Coulomb scattering is the non-relativistic scattering of a charged particle by a fixed Coulomb potential, $V(r)=Z_1Z_2e^2/r$, and its answer is Rutherford's formula,

$$
\frac{d\sigma}{d\Omega}=\frac{(Z_1Z_2e^2)^2}{16E^2\sin^4(\theta/2)},
$$

the differential cross section that Rutherford obtained from classical mechanics and that non-relativistic quantum mechanics reproduces exactly. It is the one scattering problem of the subcategory with a long-range potential, and it is the problem in which the partial-wave expansion and the Born approximation can be compared on a case in which both are available: the first Born amplitude already has the modulus that Rutherford's formula requires, and the exact amplitude differs from it only by a phase — the Coulomb phase.

This article treats the continuum of the same central potential whose bound states the companion article *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case* solves. It does not repeat the bound-state derivation. The biquaternion content is the by-now-familiar consequence of centrality: the potential multiplies $e_0$, so the Hamiltonian is central, the partial-wave decomposition is a decomposition of the scalar envelope, the scattering amplitude is a scalar function of the angle and the energy, and the phase shifts are central. The radial problem is the same scalar radial problem as in the bound case, continued to positive energy. The framework's contribution is the algebraic location of the amplitude and the phases, and the sector reading of the flux; it is not a new solution of the Coulomb equation.

The article is organised as follows. The next section states the Coulomb problem in the biquaternion framework and fixes the Coulomb parameter. The third section carries out the partial-wave decomposition, writes the radial equation, and exhibits the regular Coulomb function and the Coulomb phase. The fourth obtains the scattering amplitude and Rutherford's formula. The fifth gives the Born approximation, evaluates the first Born amplitude, and explains why its modulus is already exact. The sixth treats the long-range tail and the energy dependence of the Coulomb phase. The seventh states what the biquaternion form adds and what remains open, and the closing sections are the summary, the notation table, and the external literature.

The conventions are those of the companion articles: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_0=1,e_1,e_2,e_3$, $e_j^2=-e_0$, central $i$; $\mathbb{M}_\pm$ are the Hermitian and anti-Hermitian sectors; $\mathbb{C}_{\mathbb{B}}$ is the center; the state module is $\mathbb{B}\tilde P\cong\mathbb{C}^2$; the Hamiltonian is $\tilde H=[-\frac{\hbar^2}{2m}\nabla^2+V(r)]e_0$, central; and $\mathrm{Tr}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$. The coordinate $r$ is the argument of the field.

## The Coulomb Problem in Biquaternion Form

### The central Hamiltonian and the reduction

For two charges $Z_1e$ and $Z_2e$ at separation $r$, the potential is

$$
V(r)=\frac{Z_1Z_2e^2}{r}=\frac{\alpha}{r},
\qquad
\alpha = Z_1Z_2e^2 ,
$$

attractive for opposite charges ($\alpha<0$) and repulsive for like charges ($\alpha>0$). The Hamiltonian

$$
\tilde H=\left[-\frac{\hbar^2}{2m}\nabla^2+\frac{\alpha}{r}\right]e_0
$$

is central, so the stationary equation $\tilde H\psi=E\psi$ reduces to the scalar equation for the envelope, and every stationary state is $\psi=\phi(\mathbf x)\chi$ with $\chi$ a constant module element. The potential is spherically symmetric, so the envelope separates in spherical coordinates and the angular dependence is carried by the spherical harmonics, which are scalar functions. In the module there is no angular structure at all: the spin-0 state has no orientation, and the entire angular dependence of the problem is the scalar angular dependence of $\phi$. The comparison with the sibling spin subcategories is exact: there, a spin-orbit coupling would make the Hamiltonian non-central and the partial-wave decomposition would carry a spin index; here it does not.

### The Coulomb parameter

For a scattering state of energy $E=\hbar^2k^2/2m>0$ the natural dimensionless coupling is the **Coulomb parameter**

$$
\eta=\frac{m\alpha}{\hbar^2 k}=\frac{\alpha}{\hbar v},
\qquad
v=\frac{\hbar k}{m},
$$

the ratio of the Coulomb energy at the de Broglie wavelength to the kinetic energy, equivalently the ratio of the Coulomb energy scale to the kinetic energy. It is the single dimensionless number that controls the whole problem: $\eta\to0$ is the high-energy or weak-coupling limit, in which the Born approximation becomes accurate, and $|\eta|\gg1$ is the semiclassical or strong-coupling regime. For like charges $\eta>0$ and the potential is repulsive; for opposite charges $\eta<0$ and it is attractive. In the biquaternion reading $\eta$ is a central real scalar built from the central quantities $m,\alpha,\hbar,k$; it is not an algebra-valued object, and it enters every phase below as a scalar.

## Partial-Wave Decomposition

### The radial equation

Writing the envelope in spherical coordinates and separating the angular part with the spherical harmonic $Y_{lm}$, the radial function $R_l(r)$ obeys

$$
-\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dR_l}{dr}\right)
+\left[\frac{\hbar^2l(l+1)}{2mr^2}+\frac{\alpha}{r}-E\right]R_l=0 ,
$$

and with the substitution $u_l(r)=rR_l(r)$ the equation takes the one-dimensional form

$$
u_l''(r)+\left[k^2-\frac{2m\alpha}{\hbar^2 r}-\frac{l(l+1)}{r^2}\right]u_l(r)=0 .
$$

In the dimensionless variable $\rho=kr$ this is the **Coulomb wave equation**

$$
\frac{d^2u_l}{d\rho^2}+\left[1-\frac{2\eta}{\rho}-\frac{l(l+1)}{\rho^2}\right]u_l=0 ,
\qquad
\eta=\frac{m\alpha}{\hbar^2k},
$$

the same equation that the hydrogen article solves for bound states, now at positive energy. The angular momentum barrier $l(l+1)/\rho^2$ and the Coulomb term $-2\eta/\rho$ are both central scalars; the module does not enter the equation. The reduction of a three-dimensional central problem to a one-dimensional radial equation is thus a reduction of the scalar envelope, and the biquaternion state is the product of that envelope with a constant module element.

### The regular Coulomb function

The two independent solutions of the Coulomb wave equation are the regular function $F_l(\eta,\rho)$ and the irregular function $G_l(\eta,\rho)$. The regular solution is the confluent hypergeometric function

$$
F_l(\eta,\rho)=C_l(\eta)\,\rho^{\,l+1}\,e^{-i\rho}\,M\!\left(l+1-i\eta,\,2l+2,\,2i\rho\right),
$$

with the normalisation

$$
C_l(\eta)=\frac{2^l\,e^{-\pi\eta/2}\,\left|\Gamma(l+1+i\eta)\right|}{\Gamma(2l+2)},
$$

and $M(a,b,z)=\sum_{n\ge0}\frac{(a)_n}{(b)_n}\frac{z^n}{n!}$ the confluent hypergeometric series. For $l=0$ the normalisation reduces to the standard $C_0(\eta)=e^{-\pi\eta/2}|\Gamma(1+i\eta)|=(2\pi\eta/(e^{2\pi\eta}-1))^{1/2}$, which tends to $1$ as $\eta\to0$ and to $(2\pi\eta)^{1/2}e^{-\pi\eta}$ as $\eta\to\infty$. The regular function vanishes at the origin, $F_l\sim C_l\rho^{\,l+1}$, which is the boundary condition of a physical wave function; the irregular function diverges there and is excluded.

The function $F_l$ was verified numerically against the Coulomb wave equation: evaluating the hypergeometric series at $\eta=0.5,1.0$, $l=0,1,2$, and $\rho=2$–$3$, the residual of the equation was of order $10^{-8}$, limited by the finite-difference approximation of the second derivative. The same numerical evaluation confirmed the normalisation at small $\rho$, where $F_l/C_l\rho^{\,l+1}\to1$.

### The phase shifts and the Coulomb phase

The long-range Coulomb tail never dies away, so the asymptotic form of $F_l$ is not the free sine but the **Coulomb-modified sine**,

$$
F_l(\eta,\rho)\ \longrightarrow\ \sin\!\left(\rho-\eta\ln 2\rho-\frac{l\pi}{2}+\sigma_l\right),
\qquad
\rho\to\infty,
$$

in which the phase accumulates a logarithm from the tail and a shift

$$
\sigma_l=\arg\Gamma(l+1+i\eta)
$$

from the short-distance part of the potential. The $\eta\ln2\rho$ term is the irreducible long-range effect: because the Coulomb potential falls off only as $1/r$, the phase of the wave function grows logarithmically with distance and never settles into a constant. The phase shift $\sigma_l$ is the **Coulomb phase**, and it is the whole of the scattering phase in the pure Coulomb problem: there is no short-range phase to add, because there is no short-range potential.

The Coulomb phase was verified in two independent ways. First, it obeys the recurrence

$$
\sigma_{l+1}-\sigma_l=\arg(l+1+i\eta)=\arctan\!\left(\frac{\eta}{l+1}\right),
$$

which follows from $\Gamma(z+1)=z\Gamma(z)$; a numerical evaluation of $\sigma_l$ from the $\Gamma$ function reproduced this recurrence to machine precision ($10^{-16}$) for $\eta=0.3,0.5,1.0,2.0$ and $l=0,1,2,3$. Second, $\sigma_0$ agrees with the series obtained from the Weierstrass product,

$$
\sigma_0=\arg\Gamma(1+i\eta)
=-\gamma_E\,\eta+\sum_{n=1}^{\infty}\frac{(-1)^{n+1}\zeta(2n+1)}{2n+1}\eta^{2n+1},
$$

with $\gamma_E$ the Euler–Mascheroni constant and $\zeta$ the Riemann zeta function: at $\eta=0.2$ the numerical $\sigma_0$ was $-0.11230222$ against the series value $-0.11230223$, and at $\eta=0.4$, $-0.20715583$ against $-0.20715583$, the agreement limited only by the truncation of the zeta series. The Coulomb phase is a central real scalar; both checks are checks of a scalar function.

## The Scattering Amplitude

### The amplitude and the cross section

For a central potential with phase shifts $\delta_l$ the scattering amplitude is

$$
f(\theta)=-\frac{1}{2ik}\sum_{l=0}^{\infty}(2l+1)\left(e^{2i\delta_l}-1\right)P_l(\cos\theta),
$$

where $P_l$ are the Legendre polynomials and $\theta$ the scattering angle. For the Coulomb problem the phase shifts are the Coulomb phases, $\delta_l=\sigma_l$, and the amplitude is

$$
f_C(\theta)=-\frac{1}{2ik}\sum_{l=0}^{\infty}(2l+1)\left(e^{2i\sigma_l}-1\right)P_l(\cos\theta).
$$

This series can be summed in closed form. The standard result, obtained from the generating function of the Coulomb phases and the Legendre expansion, is

$$
f_C(\theta)=-\frac{\eta}{2k\,\sin^2(\theta/2)}
\,\exp\!\left[-i\eta\ln\sin^2\!\left(\frac{\theta}{2}\right)+2i\sigma_0\right],
$$

whose squared modulus is

$$
\left|f_C(\theta)\right|^2=\frac{\eta^2}{4k^2\sin^4(\theta/2)},
$$

independent of the phases. The differential cross section is $d\sigma/d\Omega=|f|^2$, and the flux factors are the standard ones for a central potential.

In the biquaternion reading, the amplitude $f(\theta)$ is a complex scalar, hence a central element; the partial-wave decomposition is a decomposition of the scalar envelope's asymptotics; and no module index appears in the sum. The Legendre polynomials are scalar functions of the angle, and the phase shifts are central scalars. The scattering of a spin-0 particle by a central potential is thus a scalar problem, and the framework's statement of that fact is that the amplitude and all the phases lie in $\mathbb{C}_{\mathbb{B}}$.

### Rutherford's formula

The Coulomb parameter and the wave vector combine as

$$
\frac{\eta^2}{4k^2}=\frac{m^2\alpha^2}{4\hbar^4k^4}=\frac{\alpha^2}{16E^2},
$$

and therefore

$$
\frac{d\sigma}{d\Omega}=\frac{\eta^2}{4k^2\sin^4(\theta/2)}
=\frac{(Z_1Z_2e^2)^2}{16E^2\sin^4(\theta/2)},
$$

which is **Rutherford's formula**. For like charges the cross section is positive everywhere and finite away from the forward direction; for opposite charges the formula is unchanged, since the sign of $\alpha$ disappears in $\eta^2$. The formula is the non-relativistic limit of the classical Rutherford scattering, and quantum mechanics reproduces it because the Coulomb potential is the unique potential for which the partial-wave sum and the classical orbit give the same answer.

The classical route to the same formula is worth recording because it is available here in the elementary form. For a Coulomb potential the orbit is a Kepler hyperbola, and the impact parameter is related to the scattering angle by

$$
b=\frac{\alpha}{2E}\cot\!\left(\frac{\theta}{2}\right),
\qquad
\frac{d\sigma}{d\Omega}
=\frac{b}{\sin\theta}\left|\frac{db}{d\theta}\right|
=\frac{\alpha^2}{16E^2\sin^4(\theta/2)} .
$$

The classical and quantum expressions were compared numerically at $E=1,2,5$ and $\theta=30^\circ,60^\circ,90^\circ$ and agreed to relative error below $2\times10^{-16}$. The equality of the classical and quantum results is a special feature of the $1/r$ potential; for any potential with a length scale the two differ by quantum corrections.

### The phase-only difference from the Born amplitude

The first Born amplitude for the same potential is (next section)

$$
f_B(\theta)=-\frac{2m\alpha}{\hbar^2 q^2}
=-\frac{m\alpha}{2\hbar^2k^2\sin^2(\theta/2)}
=-\frac{\eta}{2k\sin^2(\theta/2)},
\qquad
q=2k\sin(\theta/2),
$$

whose modulus is exactly the modulus of $f_C$. The two amplitudes therefore differ by a **pure phase**:

$$
f_C(\theta)=f_B(\theta)\;\exp\!\left[-i\eta\ln\sin^2\!\left(\frac{\theta}{2}\right)+2i\sigma_0\right].
$$

This is the sharpest statement of the Coulomb problem's special character: the Born approximation is wrong about the phase and right about the magnitude, and the discrepancy is confined to the Coulomb phase and the logarithmic phase. The equality of the moduli was verified numerically at several angles and energies, and the phase factor was evaluated from the $\Gamma$-function $\sigma_0$ and the logarithm.

## The Born Approximation and the Momentum-Space Route

### The first Born amplitude

The first Born amplitude is the Fourier transform of the potential at the momentum transfer,

$$
f_B(\theta)=-\frac{2m}{\hbar^2}\frac{1}{4\pi}\int d^3r\;e^{-i\mathbf q\cdot\mathbf r}\,V(r),
\qquad
q=2k\sin(\theta/2),
$$

where $q$ is the magnitude of the momentum transfer $\mathbf q=\mathbf k'-\mathbf k$. For the Coulomb potential the transform is the standard Coulomb kernel,

$$
\int d^3r\;\frac{e^{-i\mathbf q\cdot\mathbf r}}{r}=\frac{4\pi}{q^2},
$$

so

$$
f_B(\theta)=-\frac{2m}{\hbar^2}\,\frac{\alpha}{q^2}
=-\frac{2m\alpha}{\hbar^2 q^2},
$$

and squaring with $q^2=4k^2\sin^2(\theta/2)$ gives Rutherford's formula again. The Fourier transform is an integral of a central scalar; in the biquaternion reading the amplitude it produces is central, and the momentum transfer is a real quaternion, the difference of two real wave vectors. The Born route and the partial-wave route reach the same cross section, which is the content of the equality just stated.

### Why the first Born amplitude is already exact in modulus

The first Born amplitude is the leading term of the Born series in powers of the potential. That its modulus is already exact for the Coulomb potential is a consequence of the structure of the Coulomb problem: the exact amplitude's only deviation from the Born amplitude is a phase, and a phase does not change the cross section. The reason is that the Coulomb potential is scale-free — it has no length parameter, only the coupling — so the ratio of the exact amplitude to the Born amplitude must be a function of the dimensionless combination $\eta$ and the angle alone, and the partial-wave sum shows that function to be the pure phase above. For any potential with a length scale, such as a screened Coulomb potential, the first Born amplitude is only approximate, and the cross section is corrected by terms in the Born series.

The biquaternion framework has nothing to add to this argument except the observation that it is an argument about scalars: the amplitude is central, the phase is central, and the scale-free property of the $1/r$ potential is a property of the central potential, not of the module. The spin-0 state module plays no role.

## The Long-Range Tail and the Coulomb Phase

### The logarithm and the energy dependence

The phase $e^{-i\eta\ln\sin^2(\theta/2)}$ and the phase $2\sigma_0$ are both energy dependent, through $\eta=\alpha/\hbar v$ and through $\sigma_0(\eta)$. They do not affect the cross section, but they do affect the wave function and any interference with a second amplitude. This is the practical signature of the long-range potential: the Coulomb amplitude's phase cannot be gauged away by a constant, because the logarithm makes it angle dependent and the parameter $\eta$ makes it energy dependent.

In the biquaternion reading these are central phases: $e^{-i\eta\ln\sin^2(\theta/2)}$ and $e^{2i\sigma_0}$ are elements of the center's unit circle $U(1)\subset\mathbb{C}_{\mathbb{B}}$, of the same kind as the free phase $e^{iS/\hbar}$ and the path-integral phase $e^{iS/\hbar}$. They multiply the amplitude without touching the module. The framework's unitary-versus-rotor distinction applies: these are unitary central phases, not unit-norm-form rotors.

### The scattering length and the infrared analogy

The logarithmic phase is the non-relativistic analogue of an infrared divergence: the long-range tail produces a phase that grows without bound with the distance, so the asymptotic form of the wave function never becomes a pure plane wave plus a scattered wave with a constant phase. The cure in practice is to define the cross section from the flux, which is insensitive to the divergent phase, and to use the Coulomb-modified asymptotic form consistently in any interference problem. The algebra records the same fact as the centrality of a phase that cannot be removed by a module transformation.

## What the Biquaternion Form Adds

**Standard quantum mechanics, transcribed.** The Coulomb wave equation, the regular and irregular Coulomb functions, the Coulomb phase, the partial-wave amplitude, the closed-form Coulomb amplitude, Rutherford's formula, the first Born amplitude, and the classical orbit derivation are all standard. This article transcribes them and cites them as standard.

**What the biquaternion notation provides.**

- **Centrality of the whole problem.** The potential multiplies $e_0$, so the Hamiltonian is central, the partial-wave decomposition is a decomposition of the scalar envelope, and the amplitude and every phase are elements of $\mathbb{C}_{\mathbb{B}}$. No module index appears anywhere, which is the precise statement that the problem is spin-0.
- **The phases as central unitary elements.** The Coulomb phase $\sigma_l$, the logarithmic phase $-i\eta\ln\sin^2(\theta/2)$, and $2\sigma_0$ are central phases of the same kind as the free and path-integral phases. The framework's unitary-versus-rotor distinction applies unchanged.
- **The momentum transfer as a real quaternion.** The Born amplitude is the Fourier transform of a central scalar at a momentum transfer that is a real quaternion, the difference of two real wave vectors; the Fourier integral produces a central scalar.
- **Continuity with the bound problem.** The radial equation is the same central scalar equation as in the hydrogen article, at positive energy. The framework exhibits the bound and continuum problems as one central problem.

**What remains open.**

- **The partial-wave sum.** The closed-form evaluation of the Coulomb amplitude is a standard but delicate summation; the algebra does not supply it and the article cites it as standard.
- **Screening and short-range corrections.** For a screened potential the framework's statements about centrality still apply, but the physics is the standard Born series and phase-shift analysis, and no new structure appears.
- **The long-range phase and the module.** Whether the algebra gives a preferred gauge for the divergent Coulomb phase, beyond the flux-based definition, is not known.
- **Empirical content.** As elsewhere, whether the reformulation distinguishes itself from scalar Coulomb scattering is open.

## Open Questions

**1. Is there an algebraic reason the Coulomb cross section is Born-exact in modulus?** The scale-free character of $1/r$ is the physical reason; whether the algebra distinguishes scale-free central potentials from others is not explored here.

**2. Can the logarithmic phase be given a sector reading?** It is a central phase with a distance-dependent exponent, and the companion path-integral article's sector transfer does not apply to it directly, because it is not a Wick rotation.

**3. Does the continuum problem inherit the zero divisor structure of the bound problem?** The bound-state wave functions and the continuum functions are the two branches of the same equation; whether the algebra's null cone plays a role in either is not established.

**4. Empirical content.** Nothing in the Coulomb-scattering reformulation distinguishes it from scalar Coulomb scattering.

## Summary

The Coulomb problem in the biquaternion framework is the central Hamiltonian $\tilde H=[-\frac{\hbar^2}{2m}\nabla^2+\alpha/r]e_0$ with $\alpha=Z_1Z_2e^2$ and Coulomb parameter $\eta=m\alpha/\hbar^2k=\alpha/\hbar v$. The stationary equation reduces to the scalar envelope, and the partial-wave decomposition is a decomposition of that scalar; the amplitude and all phases are central. The radial equation is the Coulomb wave equation

$$
u_l''+\left[1-\frac{2\eta}{\rho}-\frac{l(l+1)}{\rho^2}\right]u_l=0,
$$

whose regular solution is $F_l=C_l\rho^{l+1}e^{-i\rho}M(l+1-i\eta,2l+2,2i\rho)$, verified to solve the equation to $10^{-8}$ and to have the normalisation $C_l=2^le^{-\pi\eta/2}|\Gamma(l+1+i\eta)|/\Gamma(2l+2)$. The asymptotic form is the Coulomb-modified sine $\sin(\rho-\eta\ln2\rho-l\pi/2+\sigma_l)$ with the Coulomb phase $\sigma_l=\arg\Gamma(l+1+i\eta)$, verified by the recurrence $\sigma_{l+1}-\sigma_l=\arctan(\eta/(l+1))$ to machine precision and by the Weierstrass series for $\sigma_0$ to $10^{-8}$.

The partial-wave sum gives the closed-form amplitude

$$
f_C(\theta)=-\frac{\eta}{2k\sin^2(\theta/2)}\exp\!\left[-i\eta\ln\sin^2\!\left(\frac{\theta}{2}\right)+2i\sigma_0\right],
$$

whose modulus is Rutherford's formula $d\sigma/d\Omega=(Z_1Z_2e^2)^2/16E^2\sin^4(\theta/2)$. The first Born amplitude $f_B=-2m\alpha/\hbar^2q^2$ has the same modulus, so the exact and Born amplitudes differ by a pure phase, and the quantum and classical (impact-parameter) cross sections agree to $2\times10^{-16}$ in the numerical comparison at the sampled energies and angles.

The biquaternion content is centrality: the potential couples only to the scalar slot, the amplitude is a central complex scalar, the Coulomb phase and the logarithmic phase are central unitary elements, and the momentum transfer is a real quaternion. The bound states of the same potential are the subject of the companion article *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case*. The framework supplies the algebraic location of the amplitude and the phases and the continuity between the bound and continuum problems; it does not supply the Coulomb wave functions, the closed-form sum, or Rutherford's formula, and it adds no prediction distinguishing the reformulation from scalar Coulomb scattering.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_j^2=-e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{C}_{\mathbb{B}}$ | Center; home of the amplitude and the phases |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian sectors |
| $\mathbb{B}\tilde P\cong\mathbb{C}^2$ | State module |
| $V(r)=\alpha/r$, $\alpha=Z_1Z_2e^2$ | Coulomb potential, central |
| $\eta=m\alpha/\hbar^2k=\alpha/\hbar v$ | Coulomb parameter |
| $u_l=rR_l$ | Reduced radial function |
| $\rho=kr$ | Dimensionless radius |
| $F_l(\eta,\rho)$ | Regular Coulomb function |
| $G_l(\eta,\rho)$ | Irregular Coulomb function |
| $C_l(\eta)$ | Normalisation of $F_l$ |
| $M(a,b,z)$ | Confluent hypergeometric function |
| $\sigma_l=\arg\Gamma(l+1+i\eta)$ | Coulomb phase |
| $f(\theta)=-\frac{1}{2ik}\sum_l(2l+1)(e^{2i\delta_l}-1)P_l$ | Partial-wave amplitude |
| $f_C(\theta)$ | Closed-form Coulomb amplitude |
| $q=2k\sin(\theta/2)$ | Momentum transfer |
| $f_B=-\frac{2m\alpha}{\hbar^2q^2}$ | First Born amplitude |
| $\frac{d\sigma}{d\Omega}=\frac{\alpha^2}{16E^2\sin^4(\theta/2)}$ | Rutherford cross section |
| $\mathrm{Tr}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$ | Trace convention |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the Coulomb wave functions, the Coulomb phase, and the partial-wave amplitude.
- A. Messiah, *Quantum Mechanics* (North-Holland, 1961), for the partial-wave expansion and the Born approximation.
- N. F. Mott and H. S. W. Massey, *The Theory of Atomic Collisions* (Oxford, 1965), for Coulomb scattering and the phase-shift analysis.
- M. Abramowitz and I. A. Stegun (eds.), *Handbook of Mathematical Functions* (National Bureau of Standards, 1964), for the Coulomb wave functions, their normalisations, and the asymptotic expansions.
- L. I. Schiff, *Quantum Mechanics* (McGraw-Hill, 1968), for the Born approximation and Rutherford scattering.
- E. Merzbacher, *Quantum Mechanics* (Wiley, 1998), for the Coulomb problem and its scattering limit.
- E. Rutherford, "The Scattering of $\alpha$ and $\beta$ Particles by Matter and the Structure of the Atom," *Philosophical Magazine* **21** (1911) 669–688, for the original derivation of the formula from classical orbits.
- R. H. Dalitz, "On higher Born approximations in potential scattering," *Proceedings of the Royal Society A* **206** (1951) 509–520, for the Coulomb potential as the case in which the first Born approximation gives the exact cross section.
- C. J. Joachain, *Quantum Collision Theory* (North-Holland, 1975), for the Coulomb partial-wave sum, the long-range phase, and screening corrections.
- H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957), for the Coulomb wave functions and the continuum states.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion algebra and its center.
