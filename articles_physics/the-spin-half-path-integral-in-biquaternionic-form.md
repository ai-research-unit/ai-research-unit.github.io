# __The Spin-Half Path Integral in Biquaternionic Form__

## Introduction

The path integral expresses the propagator of a quantum system as a sum over histories, each weighted by $e^{iS/\hbar}$. For a particle with position degrees of freedom the histories are trajectories, and the action is the integral of a Lagrangian. For a **spin**, there is no position; the histories must be built from the state space itself, and the natural choice is the space of **spin coherent states** — the sphere of directions of the spin. The resulting path integral is the subject of this article, in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the read-list articles.

The spin path integral has one feature that distinguishes it from the particle path integral and that ties it to the geometric phase: the kinetic term of the action is not a total derivative. It is the **Wess–Zumino term**

$$
S_{WZ} = i\hbar\int_0^T\langle z(t)|\,\partial_t\,|z(t)\rangle\,dt,
$$

whose value over a closed loop is $-\hbar$ times one half the oriented solid angle, i.e. the geometric phase. The path integral thus contains the geometric phase as a piece of its action, and the classical equations of motion come from varying the whole action, Wess–Zumino term included.

This article establishes:

1. **The coherent-state path integral for spin-1/2.** The resolution of identity on $\mathbb{CP}^1$, the overlap, the action $S = \int(i\hbar\langle z|\dot z\rangle - \langle z|\tilde{H}|z\rangle)dt$, and the measure.
2. **The Wess–Zumino term is the geometric phase.** For a closed loop of the star, $\int i\langle z|\dot z\rangle\,dt = -\Omega_{\mathrm{sgn}}/2$, exactly the solid-angle phase of the spin-1/2 holonomy; verified below on a one-parameter family of loops.
3. **The saddle point is Larmor precession.** Varying the action with the Wess–Zumino term included gives the classical equation $\dot{\mathbf{r}} = \gamma\,\mathbf{r}\times\mathbf{B}$ (the Bloch/Larmor equation), so the classical spin is the saddle point of the spin path integral.
4. **The spinor (Grassmann) form.** The same propagator can be written as a path integral over a two-component spinor with the constraint $\bar\psi\psi = 1$; the two forms are related by the change of variables $\zeta = \psi_2/\psi_1$.
5. **The double cover is visible in the path integral.** The coherent-state integral is over the sphere of idempotents and loses the phase; the spinor integral is over the double cover and retains it. The Wess–Zumino term is the obstruction to writing the action purely in terms of the idempotent.
6. **Topological consequences.** The Wess–Zumino term is a topological term whose coefficient is the spin; it controls spin tunnelling and the quenching of the tunnelling amplitude, and it is the same object as the curvature quantisation of the geometric-phase articles.

The notation is that of the read-list articles: $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$, $\tilde{P}_\pm(\hat\mu) = \tfrac12(e_0\pm i\hat\mu)$, $\tilde{\rho} = \tfrac12(e_0+i\mathbf{r})$, the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, and the isomorphism $\Phi$ with $ie_k\mapsto\sigma_k$.

The companion articles supply the pieces:
- Companion article *The Path Integral in Biquaternionic Form*, for the path integral in the algebra and its classical limit.
- Companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, for the spin algebra and the two-state space.
- Companion article *The Berry Phase and Geometric Phases in Biquaternionic Form*, for the geometric phase that the Wess–Zumino term reproduces.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the trace pairing used in the coherent-state overlap.

## The Propagator and Its Path Integral

### The Coherent States

The spin-1/2 coherent states are the states of definite spin along a direction $\hat{n}$, written in the stereographic coordinate $\zeta$ as

$$
|\zeta\rangle = \frac{1}{\sqrt{1+|\zeta|^2}}\left(|{+}\rangle + \zeta\,|{-}\rangle\right),
\qquad
\zeta = \tan\frac{\theta}{2}\,e^{i\phi},
$$

so that $|\zeta\rangle$ has Bloch vector $\hat{n}(\zeta)$ and its idempotent is $\tilde{P}_+(\hat{n})$. The parameter $\zeta$ ranges over $\mathbb{CP}^1$ — the sphere of directions — with the north pole at $\zeta = 0$ and the south pole at $\zeta = \infty$. The two-component spinor $(\cos\tfrac{\theta}{2},\,\sin\tfrac{\theta}{2}e^{i\phi})$ is the lift of $|\zeta\rangle$ to the double cover, as in the Majorana construction.

### The Overlap and the Measure

The overlap of two coherent states is

$$
\langle z'|z\rangle = \frac{1+\bar z' z}{\sqrt{(1+|z'|^2)(1+|z|^2)}},
$$

and the resolution of the identity on the spin-1/2 Hilbert space is

$$
\mathbb{1} = \frac{2}{\pi}\int_{\mathbb{CP}^1}\frac{d^2z}{(1+|z|^2)^2}\,|z\rangle\langle z|,
$$

where $d^2z$ is the ordinary area element in the complex plane. The measure is the invariant measure of $\mathbb{CP}^1$ in the coordinate $z$, and the factor $2$ is $2j+1$ at $j = \tfrac{1}{2}$. Both statements are standard; they are the input that makes the coherent-state path integral well defined.

### The Discretised Integral

Discretise the time interval $[0,T]$ into $N$ slices of width $\epsilon = T/N$. Inserting $\mathbb{1}$ at each intermediate time and using the short-time limit of the propagator,

$$
\langle z_{k+1}|e^{-i\epsilon\tilde{H}/\hbar}|z_k\rangle
\approx \langle z_{k+1}|z_k\rangle\,e^{-i\epsilon\langle z_k|\tilde{H}|z_k\rangle/\hbar},
$$

the propagator becomes

$$
K(z_f,T;z_i,0) = \lim_{N\to\infty}\left(\frac{2}{\pi}\right)^{\!N}\int\prod_{k=1}^{N-1}\frac{d^2z_k}{(1+|z_k|^2)^2}\prod_{k=0}^{N-1}\langle z_{k+1}|z_k\rangle\,e^{-\frac{i\epsilon}{\hbar}\langle z_k|\tilde{H}|z_k\rangle},
$$

with $z_0 = z_i$, $z_N = z_f$. This is the spin-1/2 path integral in its fully explicit form.

## The Coherent-State Action

### The Continuum Limit

In the continuum limit the product of overlaps contributes

$$
\prod_k\langle z_{k+1}|z_k\rangle
\;\longrightarrow\;
\exp\!\left(-\int_0^T\langle z|\partial_t|z\rangle\,dt\right)
= \exp\!\left(\frac{i}{\hbar}S_{WZ}\right),
$$

where the last equality defines the Wess–Zumino term of this article. The action is therefore

$$
S[z] = \int_0^T\left(i\hbar\,\langle z|\partial_t|z\rangle - \langle z|\tilde{H}(t)|z\rangle\right)dt,
$$

and the propagator is $K = \int\mathcal{D}[z]\,e^{iS[z]/\hbar}$ with the measure inherited from the resolution of the identity.

### The Wess–Zumino Term

For the spin-1/2 coherent state the integrand is elementary. With $\zeta = r e^{i\phi}$ at fixed $r$,

$$
\langle z|\partial_t|z\rangle = \frac{\bar z\,\dot z - z\,\dot{\bar z}}{2(1+|z|^2)} = \frac{i\,\dot\phi\,r^2}{1+r^2},
$$

so that

$$
i\hbar\langle z|\partial_t|z\rangle
= -\hbar\,\frac{r^2}{1+r^2}\,\dot\phi
= -\hbar\,\sin^2\frac{\theta}{2}\,\dot\phi .
$$

Over a closed loop at fixed $\theta = \theta_0$, traversed once counterclockwise,

$$
S_{WZ} = i\hbar\oint\langle z|\partial_t|z\rangle\,dt
= -\hbar\cdot 2\pi\sin^2\frac{\theta_0}{2}
= -\hbar\cdot\frac{\Omega}{2},
\qquad
\Omega = 2\pi(1-\cos\theta_0).
$$

The Wess–Zumino term is therefore $-\hbar$ times one half the solid angle: the geometric phase of the closed loop. The identification was verified numerically for $\theta_0 = 0.4,\,1.0,\,1.57,\,2.2,\,2.9$, where $\int i\langle z|\dot z\rangle dt$ equals $-\Omega/2$ for every value.

This is the central structural fact of the spin path integral. The "kinetic" term of the action is not a total derivative and is not expressible in terms of the star $\hat{n}$ alone; it is the phase of the spinor. The path integral does not merely accommodate the geometric phase — it is built from it.

### The Hamiltonian Term

For a spin in a magnetic field the Hamiltonian is

$$
\tilde{H} = -\frac{\hbar\omega_L}{2}\,i\,\hat{n}_0\cdot\mathbf{e}
= -\gamma B\,\tilde{S}(\hat{n}_0),
$$

and its coherent-state expectation is

$$
\langle z|\tilde{H}|z\rangle = -\frac{\hbar\omega_L}{2}\,\hat{n}(z)\cdot\hat{n}_0,
$$

the classical Zeeman energy of a dipole along $\hat{n}(z)$. The action is thus

$$
S[z] = \int_0^T\left[-\hbar\sin^2\frac{\theta}{2}\,\dot\phi + \frac{\hbar\omega_L}{2}\,\hat{n}(z)\cdot\hat{n}_0\right]dt,
$$

the first term geometric and the second dynamical.

## The Saddle Point and the Classical Limit

### The Equations of Motion

Varying $S$ with respect to $\zeta$ and $\bar\zeta$ gives the classical equation of motion. The Wess–Zumino term supplies the symplectic structure: writing the geometric part as a one-form in the star coordinates, its exterior derivative is the area form of the sphere,

$$
\omega = -\frac{\hbar}{2}\,\sin\theta\; d\theta\wedge d\phi ,
$$

which is $\hbar$ times the Berry curvature of the geometric-phase analysis. The Hamiltonian term supplies the energy. The resulting equation is the precession

$$
\dot{\mathbf{r}} = \gamma\,\mathbf{r}\times\mathbf{B}
= \omega_L\,\mathbf{r}\times\hat{n}_0,
$$

the Larmor/Bloch equation for the classical spin, with $|\mathbf{r}| = 1$. The classical spin is the saddle point of the spin-1/2 path integral, and its dynamics is precession on the sphere.

### The Classical Limit as a Phase-Space Problem

The pair (symplectic form $\omega$, energy $\langle H\rangle$) makes the sphere a classical phase space of one degree of freedom, the spin; the path integral is its quantisation. This is the statement that a spin-1/2 is a one-degree-of-freedom phase space with a curved symplectic form, and the factor $\hbar$ in $\omega$ is the loop-counting parameter of the semiclassical expansion. The leading WKB approximation to the propagator is $e^{iS_{\mathrm{cl}}/\hbar}$ with $S_{\mathrm{cl}}$ the action along the classical path, and the next-order fluctuation determinant is the van Vleck factor.

## The Spinor Path Integral

### Grassmann Formulation

The same propagator admits a second path integral, over a two-component spinor with anticommuting (Grassmann) coefficients,

$$
K = \int\mathcal{D}\bar\psi\,\mathcal{D}\psi\; e^{\frac{i}{\hbar}S[\bar\psi,\psi]},
\qquad
S = \int\left(i\hbar\,\bar\psi\,\dot\psi - \langle\psi|\tilde{H}|\psi\rangle\right)dt,
$$

subject to the constraint $\bar\psi\psi = 1$, which fixes the norm of the spinor. The constraint is the statement that the state is pure; without it the integral would describe a mixed or a many-component system. The Grassmann variables are the algebraic expression of the spinor's anticommuting nature, and the integral over them is the standard fermionic path integral of a two-level system.

### Relation to the Coherent-State Form

The two path integrals are related by the change of variables

$$
\zeta = \frac{\psi_2}{\psi_1},
$$

which is precisely the stereographic coordinate of the Majorana construction. The coherent-state integral is the projection of the spinor integral onto $\mathbb{CP}^1$: the spinor carries three real parameters (two for the direction, one phase), the constraint $\bar\psi\psi=1$ removes one, and the overall phase is the coordinate along the fibres of the double cover. The coherent-state integral forgets the phase, and the Wess–Zumino term is what remains of it in the action. This is the precise sense in which the double cover is visible in the path integral: the two formulations differ by the fibre, and the fibre integral reproduces the Wess–Zumino term.

### The Biquaternion Reading

In the algebra the coherent state is the idempotent $\tilde{P}_+(\hat{n}(z))$, so the coherent-state path integral is an integral over the sphere of idempotents, with the trace pairing supplying the energy $\mathrm{Tr}(\tilde{P}\tilde{H})$. The spinor integral is the lift to the double cover. The saddle point is a rotor in $\mathbb{H}_{\mathbb{B}}$ — the unit real quaternion that carries $\hat{n}_0$ into $\hat{n}(t)$ — and the Wess–Zumino term is the central phase of that rotor along the path. The biquaternion algebra thus holds both integrals at once: the idempotent is the point, the spinor is the lift, and the geometric phase is the fibre.

## Topological Consequences

### The Wess–Zumino Term Is a Theta Term

The Wess–Zumino term cannot be written as the integral of a local function of $\hat{n}$ alone, because the symplectic form of the sphere is not exact: its integral over the whole sphere has magnitude

$$
\left|\int_{S^2}\omega\right| = 2\pi\hbar,
$$

the flux of a unit-charge monopole, and the Chern number of the spin-1/2 band is non-zero. The Wess–Zumino term is therefore a **topological term** — a theta term — whose coefficient is the spin $j$ in units of $\hbar$; for spin-1/2 the coefficient gives the half-integer phase $\Omega/2$. The quantisation problem of a spin is the quantisation of a phase space with a non-exact symplectic form, and the spin-1/2 phase is the simplest case.

### Spin Tunnelling and Its Quenching

For a spin in a magnetic field with an easy-axis anisotropy the classical ground states are two opposite directions, and the tunnelling between them is described by an instanton (a "sphaleron" trajectory on the sphere). The on-shell action of the instanton contains the Wess–Zumino term, which contributes an imaginary part proportional to the solid angle swept. For a half-integer spin this imaginary part is an odd multiple of $i\pi$, so the two instanton amplitudes cancel and the tunnelling is **quenched**; for an integer spin the phase is a multiple of $2\pi$ and the tunnelling survives. This is the standard Kramers-degeneracy statement in path-integral language, and it is the cleanest physical consequence of the topological term. The framework reproduces it; it does not alter it.

## What the Algebra Adds and What It Does Not

**Standard physics, transcribed.** The coherent-state path integral, the measure, the Wess–Zumino term, the saddle-point precession, the Grassmann formulation, and the spin-tunnelling quenching are all standard.

**What the algebra organises.**

- **The action is algebraic data.** The energy is the trace pairing $\mathrm{Tr}(\tilde{P}\tilde{H})$, the path is a curve of idempotents, and the Wess–Zumino term is the central phase of the rotor along the curve. The two-level path integral is the quantisation of this data.
- **The double cover is the two formulations.** The idempotent integral and the spinor integral are the sphere and its double cover; the Wess–Zumino term is the fibre.
- **The topological term is the curvature.** The non-exactness of the symplectic form is the non-zero Chern number of the geometric-phase analysis, and the coefficient $j = \tfrac12$ is the spin.
- **The saddle point is a rotor.** Larmor precession is conjugation by a time-dependent unit real quaternion, the classical limit of the quantum evolution.

**What the algebra does not supply.** The Hamiltonian, the magnetic field and the initial and final states are external data. The path integral is a representation of the dynamics, not a substitute for the dynamics.

## Open Questions

1. **The path integral on the double cover.** The spinor integral has a gauge redundancy — the overall phase — and the coherent-state integral fixes it by projection. Is there a first-principles derivation of the Wess–Zumino term as the gauge field of this redundancy, in the algebra's language?

2. **Semiclassical corrections.** The one-loop determinant around the classical spin path is standard for the spin coherent-state integral. Does its algebraic form have a natural reading in terms of the idempotent fluctuations?

3. **Many spin-1/2 particles.** The path integral of $N$ spin-1/2 particles, symmetric or not, is the many-body problem; the symmetric sector is the constellation of the Majorana representation. Whether the algebraic formulation extends to a multi-idempotent integral is open and borders on the informational subcategory.

4. **Finite temperature.** The spin partition function at finite temperature is a path integral on a circle in imaginary time. Does the topological term survive the compactification, and does it control the low-temperature density of states?

5. **Empirical contact.** As everywhere in the series, the reformulation reproduces the standard predictions; whether it implies a measurable deviation is open.

## Summary

The path integral for a spin-1/2 is an integral over histories in the space of coherent states $|\zeta\rangle$ on $\mathbb{CP}^1$:

$$
K = \int\mathcal{D}[z]\,e^{\frac{i}{\hbar}S[z]},
\qquad
S[z] = \int_0^T\left(i\hbar\,\langle z|\partial_t|z\rangle - \langle z|\tilde{H}|z\rangle\right)dt,
$$

with the invariant measure $\frac{2}{\pi}\frac{d^2z}{(1+|z|^2)^2}$ from the resolution of identity. The kinetic term is the **Wess–Zumino term**, and over a closed loop it equals

$$
S_{WZ} = -\hbar\cdot\frac{\Omega}{2},
\qquad \Omega = 2\pi(1-\cos\theta_0),
$$

one half the oriented solid angle: the geometric phase. This was verified numerically for five values of $\theta_0$.

The saddle point of $S$ is the classical Larmor precession $\dot{\mathbf{r}} = \gamma\,\mathbf{r}\times\mathbf{B}$, obtained from the symplectic form $\omega = -\tfrac{\hbar}{2}\sin\theta\,d\theta\wedge d\phi$ and the classical Zeeman energy $\langle\tilde{H}\rangle = -\tfrac{\hbar\omega_L}{2}\hat{n}\cdot\hat{n}_0$. The same propagator can be written as a Grassmann integral over a two-component spinor with $\bar\psi\psi=1$, related to the coherent-state form by $\zeta = \psi_2/\psi_1$.

In the biquaternion algebra the coherent-state integral is an integral over the sphere of idempotents $\tilde{P}_+(\hat{n})$ with energy $\mathrm{Tr}(\tilde{P}\tilde{H})$, and the spinor integral is its lift to the double cover; the Wess–Zumino term is the central phase of the rotor along the path. The term is topological: the symplectic form of the sphere is not exact, its total integral has magnitude $2\pi\hbar$, and the coefficient of the term is the spin. For a half-integer spin this makes the tunnelling instanton action imaginary by an odd multiple of $i\pi$, quenching the tunnelling between opposite classical states.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_+$ | Hermitian (informational) subspace |
| $\mathbb{H}_{\mathbb{B}}$ | Unit real quaternions; the classical rotors |
| $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$ | Spin-1/2 operator |
| $|\zeta\rangle$ | Spin coherent state with Bloch vector $\hat{n}(\zeta)$ |
| $\zeta = \tan\tfrac{\theta}{2}e^{i\phi} = \psi_2/\psi_1$ | Stereographic coordinate |
| $\langle z'|z\rangle = \dfrac{1+\bar z' z}{\sqrt{(1+|z'|^2)(1+|z|^2)}}$ | Coherent-state overlap |
| $\mathbb{1} = \tfrac{2}{\pi}\int\tfrac{d^2z}{(1+|z|^2)^2}|z\rangle\langle z|$ | Resolution of identity (spin-1/2) |
| $S_{WZ} = i\hbar\oint\langle z|\partial_t|z\rangle dt = -\hbar\tfrac{\Omega}{2}$ | Wess–Zumino term |
| $\omega = -\tfrac{\hbar}{2}\sin\theta\,d\theta\wedge d\phi$ | Symplectic form of the sphere |
| $\dot{\mathbf{r}} = \gamma\,\mathbf{r}\times\mathbf{B}$ | Classical Larmor precession |
| $\bar\psi,\psi$ | Grassmann spinor variables, $\bar\psi\psi=1$ |
| $\left|\int_{S^2}\omega\right| = 2\pi\hbar$ | Monopole flux; non-exactness of $\omega$ |

## Further Reading

- J. R. Klauder, "Path Integrals and Stationary-Phase Approximations for Spin," *Physical Review D* **19** (1979) 2349–2356, for the spin coherent-state path integral.
- H. Kuratsuji and T. Suzuki, "Path Integral in the Representation of SU(2) Coherent State and Classical Dynamics in a Generalized Phase Space," *Journal of Mathematical Physics* **21** (1980) 472–476, for the coherent-state measure and the classical limit.
- E. Fradkin, *Field Theories of Condensed Matter Physics* (Cambridge, 2013), for the Wess–Zumino term of the spin path integral and its topological role.
- A. Auerbach, *Interacting Electrons and Quantum Magnetism* (Springer, 1994), for the spin coherent-state path integral and the quenching of spin tunnelling.
- A. Altland and B. Simons, *Condensed Matter Field Theory* (Cambridge, 2010), for the Grassmann path integral of a two-level system and the semiclassical expansion.
- F. D. M. Haldane, "Nonlinear Field Theory of Large-Spin Heisenberg Antiferromagnets: Semiclassically Quantized Solitons of the One-Dimensional Easy-Axis Néel State," *Physical Review Letters* **50** (1983) 1153–1156, for the Wess–Zumino term and the topological quantisation of spin.
- L. S. Schulman, *Techniques and Applications of Path Integration* (Wiley, 1981), for the general path-integral formalism on curved state spaces.
- A. Shapere and F. Wilczek, *Geometric Phases in Physics* (World Scientific, 1989), for the geometric phase as the Wess–Zumino term of the spin path integral.
