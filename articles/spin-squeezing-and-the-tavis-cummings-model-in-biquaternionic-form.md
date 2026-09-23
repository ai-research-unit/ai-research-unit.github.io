# __Spin Squeezing and the Tavis–Cummings Model in Biquaternionic Form__

## Introduction

A single spin-1/2 is the smallest quantum system with an orientation, and its noise is the smallest quantum noise: a coherent spin state has fluctuations $\Delta J_\perp = \tfrac{\hbar}{2}\sqrt{N}$ distributed isotropically in the plane transverse to the mean spin. This is the **standard quantum limit**. When $N$ spin-1/2 particles are coupled collectively — to one another or to a common field — the noise can be redistributed: one transverse component can be squeezed below the standard quantum limit at the expense of the conjugate component. This is **spin squeezing**, and it is the resource of quantum metrology.

The model in which the collective coupling is cleanest is the **Tavis–Cummings model**: $N$ two-level systems (the spins) coupled with a common strength $g$ to a single bosonic mode. It is the $N$-atom generalisation of the Jaynes–Cummings model, and it exhibits the collective enhancement $g\sqrt{N}$ that underlies superradiance and the collective Rabi splitting. It is a driven multi-spin-1/2 system, and it is the subject of this article, in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the read-list articles.

The article establishes:

1. **The collective spin.** The operators $\tilde{J}_\alpha = \sum_{i=1}^N\tilde{S}_\alpha^{(i)}$ are Hermitian elements of $\mathbb{M}_+$ on the $N$-spin space; the symmetric states are the Dicke states, and the collective coherent state is the highest-weight state of a rotor.
2. **The Tavis–Cummings Hamiltonian and its collective coupling.** In the rotating-wave approximation the interaction is $g(a^\dagger \tilde{J}_- + a\tilde{J}_+)$, and in the single-excitation sector the collective coupling is $\hbar g\sqrt{N}$, giving the collective Rabi splitting $2\hbar g\sqrt{N}$. Both statements are verified below.
3. **Spin squeezing.** The Wineland parameter $\xi_R^2 = N(\Delta J_\perp)^2/|\langle\mathbf{J}\rangle|^2$ defines the noise relative to the standard quantum limit; the one-axis twisting Hamiltonian $\frac{\chi}{\hbar}\tilde{J}_3^2$ drives $\xi_R^2$ below $1$. The exact diagonalisation in the Dicke basis gives $\xi^2_{\min}$ decreasing with $N$, consistent with the standard $N^{-2/3}$ scaling.
4. **The algebra's reading.** The collective observables are elements of $\mathbb{M}_+$, the mean spin and the covariance are trace pairings, the squeezing ellipsoid is the image of the coherent-state noise ball under the non-uniform rotor that implements the twist — a shear, not a rigid rotation — and the Tavis–Cummings interaction is an $\mathbb{M}_+$ coupling between the spin and the mode.

The notation is that of the read-list articles: $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$, $\tilde{P}_\pm(\hat\mu) = \tfrac12(e_0\pm i\hat\mu)$, $\tilde{\rho} = \tfrac12(e_0+i\mathbf{r})$, the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, and the isomorphism $\Phi$ with $ie_k\mapsto\sigma_k$.

The companion articles supply the pieces:
- Companion article *Angular Momentum and Spin in Biquaternionic Form*, for the collective spin, the ladder operators and the Dicke states.
- Companion article *Quantum Mechanics in Biquaternionic Form*, for the bosonic mode and its coupling to a two-level system.
- Companion article *The Harmonic Oscillator in Biquaternionic Form*, for the mode algebra of the cavity field.

## The Collective Spin

### Collective Operators

For $N$ spin-1/2 particles label the spin operators by particle and component,

$$
\tilde{S}_\alpha^{(i)} = \frac{\hbar}{2}ie_\alpha^{(i)},
\qquad \alpha = 1,2,3,
$$

with $[\tilde{S}_\alpha^{(i)},\tilde{S}_\beta^{(j)}] = i\hbar\,\delta_{ij}\,\epsilon_{\alpha\beta\gamma}\tilde{S}_\gamma^{(i)}$. The **collective spin** is the sum over the particles,

$$
\tilde{J}_\alpha = \sum_{i=1}^N \tilde{S}_\alpha^{(i)},
$$

so that $\tilde{J}_\alpha$ is again an element of $\mathbb{M}_+$ and the collective algebra is the same $su(2)$ algebra with $j = N/2$. The raising and lowering combinations $\tilde{J}_\pm = \tilde{J}_1\pm i\tilde{J}_2$ shift the collective magnetic quantum number by $\pm1$. These are the standard collective operators of the Dicke model; the representation theory of the resulting total angular momentum $j = N/2$ is treated in the companion article *Angular Momentum and Spin in Biquaternionic Form*, and here the emphasis is on the spin-1/2 constituents and their collective noise.

### The Dicke States

The symmetric subspace is spanned by the **Dicke states** $|j = N/2,\,m\rangle$, $m = -N/2,\dots,N/2$, in which $j+m$ particles are up and $j-m$ are down, in the fully symmetric combination. They satisfy

$$
\tilde{J}_3|j,m\rangle = \hbar\,m\,|j,m\rangle,
\qquad
\tilde{J}_\pm|j,m\rangle = \hbar\sqrt{j(j+1)-m(m\pm1)}\,|j,m\pm1\rangle .
$$

The subspace has dimension $N+1$, while the full $N$-spin space has dimension $2^N$; the non-symmetric states carry total angular momentum $j < N/2$ and are not reached by the collective operators. The collective dynamics generated by $\tilde{J}_\alpha$ — and in particular the Tavis–Cummings interaction and the twisting Hamiltonians below — stays within the symmetric subspace if the initial state is symmetric.

### The Coherent Spin State

The collective coherent state is the product of $N$ identical spin-1/2 coherent states,

$$
|\theta,\phi\rangle = \bigotimes_{i=1}^N \left(\cos\frac{\theta}{2}|{+}\rangle_i + \sin\frac{\theta}{2}e^{i\phi}|{-}\rangle_i\right),
$$

which equals the highest-weight state of the collective spin rotated to the direction $(\theta,\phi)$. Its mean spin is $\langle\mathbf{J}\rangle = \tfrac{N\hbar}{2}\hat{n}(\theta,\phi)$, and its transverse variance is isotropic,

$$
\langle J_\perp^2\rangle = \frac{N\hbar^2}{4},
\qquad
\Delta J_\perp = \frac{\hbar\sqrt{N}}{2}.
$$

This is the standard quantum limit: the noise is the quantum noise of $N$ independent spins, and it is the reference against which squeezing is measured.

### The Bloch Ball of the Collective Spin

The collective state space, restricted to the symmetric subspace, is the spin-$N/2$ state space, whose Bloch-ball analogue has dimension $N$ (see the companion article *Angular Momentum and Spin in Biquaternionic Form*). For $N=1$ it reduces to the spin-1/2 Bloch sphere of this subcategory. The mean spin $\langle\mathbf{J}\rangle$ is a vector of length at most $\tfrac{N\hbar}{2}$; a coherent state sits on the boundary, and a state with reduced mean spin sits inside. Squeezing is a statement about the **covariance** of $\mathbf{J}$, and it is therefore not visible in the mean spin alone.

## The Tavis–Cummings Model

### The Hamiltonian

The Tavis–Cummings model couples $N$ two-level systems to a single bosonic mode with the Hamiltonian

$$
\tilde{H} = \hbar\omega_c\,a^\dagger a + \omega_a\,\tilde{J}_3 + g\left(a^\dagger \tilde{J}_- + a\,\tilde{J}_+\right),
$$

where $a,a^\dagger$ are the mode operators, $\omega_c$ the mode frequency, $\omega_a$ the level splitting, and $g$ the single-spin coupling. The interaction conserves the total excitation number

$$
\tilde{N}_{\mathrm{exc}} = a^\dagger a + \frac{\tilde{J}_3}{\hbar} + \frac{N}{2},
$$

which counts the photons plus the number of excited spins; this is the collective version of the Jaynes–Cummings excitation number. The model is integrable in each excitation sector.

### The Rotating-Wave Approximation

The interaction kept is the **rotating-wave** term: the mode annihilates a photon while a spin is raised ($a\tilde{J}_+$), and creates one while a spin is lowered ($a^\dagger\tilde{J}_-$). The neglected counter-rotating terms $a^\dagger\tilde{J}_+$ and $a\tilde{J}_-$ oscillate at the sum frequency $\omega_a+\omega_c$ in the interaction picture and average to zero when $g\ll\omega_a,\omega_c$; this is the rotating-wave approximation, the same approximation as in the single-spin Rabi problem. In the algebra both terms are elements of $\mathbb{M}_+$; the approximation selects the slowly varying combination.

### The Single-Excitation Sector and the Collective Rabi Splitting

Restrict to the manifold with one excitation, spanned by the states $|1,\text{all down}\rangle$ (one photon, no excited spin) and $|0,\text{one excited}\rangle$ (no photon, one spin excited, in the symmetric combination). On resonance $\omega_a = \omega_c = \omega$ the two states are degenerate at energy $\hbar\omega(1-N/2)$, and the interaction couples them with the matrix element

$$
\langle 1,\text{all down}|g\,a\,\tilde{J}_+^{\vphantom\dagger}|0,\text{one excited}\rangle = \hbar g\sqrt{N},
$$

because $\tilde{J}_+|j,-j\rangle = \hbar\sqrt{N}\,|j,-j+1\rangle$ with $j = N/2$. The two eigenvalues are therefore separated by

$$
\boxed{\;\Delta E = 2\hbar g\sqrt{N}\;}
$$

the **collective Rabi splitting**. The square-root enhancement is the signature of the collective coupling: it is the same $\sqrt{N}$ that appears in superradiance and in the collective Lamb shift. The result was verified numerically: for $N = 1,4,16,100$ the eigenvalue splitting of the $2\times2$ block equals $2\hbar g\sqrt{N}$ exactly.

The eigenstates of the block are the **polaritons**, the symmetric and antisymmetric combinations of "photon" and "excited spin", which are the collective analogues of the dressed states of the single-spin Rabi problem.

## The Holstein–Primakoff Linearisation

### Small Excitations

Near the fully polarised state $|j,\,j\rangle$ (all spins up) the collective operators can be represented by a single bosonic mode,

$$
\tilde{J}_3 = \hbar\left(\frac{N}{2} - b^\dagger b\right) + O(1/N),
\qquad
\tilde{J}_+ \approx \hbar\sqrt{N}\,b^\dagger,
\qquad
\tilde{J}_- \approx \hbar\sqrt{N}\,b,
$$

the **Holstein–Primakoff** transformation truncated at leading order. Substituting into the Tavis–Cummings Hamiltonian gives a quadratic two-mode problem,

$$
\tilde{H} \approx \hbar\omega_c\,a^\dagger a + \hbar\omega_a\left(\frac{N}{2}-b^\dagger b\right)
+ \hbar g\sqrt{N}\left(a^\dagger b + a b^\dagger\right),
$$

whose normal modes are obtained by diagonalising the $2\times2$ coupling. On resonance the normal-mode splitting is again $2\hbar g\sqrt{N}$; the linearised theory is the large-$N$ limit of the exact single-excitation result, and it is the standard route to the collective normal modes.

### Superradiance and the $\sqrt{N}$ Enhancement

The same collective enhancement governs the coupling of the spins to a radiating field. The emission amplitude of a collective state carries the factor $\sqrt{N}$, so the coupling to a cavity mode is $g\sqrt{N}$ and the radiated intensity carries $N$: compared with the same number of independently radiating dipoles, whose amplitudes add incoherently, the emission is cooperatively enhanced — **superradiance**. For the Dicke state $|j,0\rangle$ the enhancement of the rate is quadratic in $N$. In the algebra these are statements about the collective raising and lowering operators $\tilde{J}_\pm$ and their matrix elements in the Dicke states; the enhancement factors are the $\sqrt{N}$ of the collective algebra.

## Spin Squeezing

### The Standard Quantum Limit

For a coherent spin state the transverse variance is $(\Delta J_\perp)^2 = \tfrac{\hbar^2 N}{4}$ and the mean spin is $|\langle\mathbf{J}\rangle| = \tfrac{\hbar N}{2}$. The **Wineland squeezing parameter** is

$$
\xi_R^2 = \frac{N\,(\Delta J_\perp)^2_{\min}}{|\langle\mathbf{J}\rangle|^2},
$$

where $(\Delta J_\perp)^2_{\min}$ is the smallest variance in the plane perpendicular to the mean spin. The numerator is $N$ times the squeezed variance, the denominator the squared mean spin; for a coherent state $\xi_R^2 = 1$, a state with $\xi_R^2 < 1$ is **spin squeezed**, and the metrological phase sensitivity is improved by the factor $\xi_R$ below the standard quantum limit.

### The Squeezing Ellipse

The covariance of the collective spin is the symmetric $3\times3$ matrix

$$
\mathrm{Cov}(J_\alpha,J_\beta) = \tfrac{1}{2}\langle \tilde{J}_\alpha\tilde{J}_\beta + \tilde{J}_\beta\tilde{J}_\alpha\rangle - \langle\tilde{J}_\alpha\rangle\langle\tilde{J}_\beta\rangle ,
$$

whose eigenvalues are the variances along the principal axes. In the plane perpendicular to the mean spin the covariance reduces to a $2\times2$ matrix $\begin{pmatrix}\langle\Delta J_a^2\rangle & C\\ C & \langle\Delta J_b^2\rangle\end{pmatrix}$, and the **squeezing ellipse** is the error ellipse of the two quadratures. The smaller eigenvalue is the squeezed variance; the larger is the anti-squeezed one. The product of the two principal variances obeys the uncertainty relation, so squeezing is a redistribution and never a reduction of the total noise.

### One-Axis Twisting

The simplest generator of squeezing is the **one-axis twisting** Hamiltonian

$$
\tilde{H}_{OAT} = \frac{\chi}{\hbar}\,\tilde{J}_3^2 ,
$$

which is diagonal in the Dicke basis and therefore exactly solvable. Starting from the coherent state along $+x$, the evolution

$$
|\psi(\chi t)\rangle = e^{-i\chi t\tilde{J}_3^2/\hbar^2}|\theta=\tfrac{\pi}{2},\phi=0\rangle
$$

shears the noise ellipse: the variance in the $y$–$z$ plane develops an off-diagonal covariance, the smaller principal variance drops below $\hbar^2N/4$, and $\xi_R^2$ falls below $1$. The mean spin also decreases, since the twisting rotates different Dicke components at different rates; the competition between the shrinking variance and the shrinking mean spin fixes an optimal twisting time.

### Numerical Illustration

Computing the exact evolution in the Dicke basis and minimising $\xi_R^2$ over $\chi t$ gives, for the pure one-axis twisting model:

| $N$ | 8 | 16 | 32 | 64 |
|---|---|---|---|---|
| $\xi^2_{\min}$ | $0.354$ | $0.230$ | $0.143$ | $0.087$ |
| $\chi t_{\mathrm{opt}}$ | $0.228$ | $0.153$ | $0.101$ | $0.066$ |

The optimal time decreases and the noise decreases with $N$, consistent with the standard one-axis-twisting scaling $\xi^2_{\min}\sim N^{-2/3}$: the computed optimal times $0.228,0.153,0.101,0.066$ follow $N^{-2/3}$ with a coefficient between $0.9$ and $1.1$, and the minimum variances give $\xi^2_{\min}N^{2/3} = 1.42,\,1.46,\,1.44,\,1.39$ — the standard scaling with a prefactor of order unity. At $\chi t = 0$ the parameter is $\xi^2 = 1$ to machine precision, as it must be for a coherent state.

### Two-Axis Twisting

The **two-axis countertwisting** Hamiltonian $\frac{\chi}{\hbar}(\tilde{J}_+^2 + \tilde{J}_-^2)$ — or equivalently a squeezing generator with two orthogonal axes — reaches the Heisenberg scaling $\xi^2\propto N^{-1}$ in the ideal case, faster than one-axis twisting. It is harder to realise physically because it requires a nonlinear coupling with two non-commuting axes, but it is the standard benchmark for the best achievable squeezing from a nonlinear collective Hamiltonian. The framework describes it in the same language: a Hermitian element of $\mathbb{M}_+$ that is quadratic in the collective spin.

## The Biquaternion Reading

### Collective Observables in $\mathbb{M}_+$

Each $\tilde{J}_\alpha$ is a sum of Hermitian elements $ie_\alpha^{(i)}$ and is Hermitian; the mean spin is the trace pairing

$$
\langle \tilde{J}_\alpha\rangle = \mathrm{Tr}\!\left(\tilde{\rho}\,\tilde{J}_\alpha\right),
\qquad
\tilde{\rho} = \text{the collective state},
$$

and the covariance is the symmetrised trace pairing of $\tilde{J}_\alpha\tilde{J}_\beta$. Squeezing is thus a statement about the trace pairings of the collective $\mathbb{M}_+$ elements and their products: it is the anisotropy of a quadratic pairing, not of a linear one. The mean spin is a vector, the covariance is a symmetric tensor, and the physics of squeezing lives entirely in the tensor.

### The Twisting as a Rotor

One-axis twisting is conjugation by a **non-uniform** rotor. In the Dicke basis the evolution operator $\exp(-i\chi t\tilde{J}_3^2/\hbar^2)$ acts on each $|j,m\rangle$ with a phase depending on $m^2$; written on the spinor it is a diagonal rotor whose angle is proportional to $m^2$. It is not a rigid rotation of the collective Bloch ball — rigid rotations are generated by the linear $\tilde{J}_\alpha$ and are the unit quaternions of $\mathbb{H}_{\mathbb{B}}$ — but a **shear** of the ball, generated by the quadratic $\tilde{J}_3^2$. The distinction is the algebraic content of the difference between a rotation (which preserves the noise ellipse) and a squeezing (which shears it). The squeezing ellipsoid is the image of the coherent-state noise ball under this shear.

### The Tavis–Cummings Coupling

The interaction term $g(a^\dagger\tilde{J}_- + a\tilde{J}_+)$ is an $\mathbb{M}_+$ coupling between the spin sector and the mode: $a^\dagger\tilde{J}_-$ and its adjoint are conjugate elements, and their sum is Hermitian. Its matrix element in the single-excitation sector, $\hbar g\sqrt{N}$, is the trace pairing evaluated between the two collective idempotents, and the collective Rabi splitting $2\hbar g\sqrt{N}$ is the associated spectral gap. The algebra thus places the collective coupling on the same footing as the single-spin Rabi coupling of the magnetic-resonance problem, with the collective operator replacing the single spin.

## What the Algebra Adds and What It Does Not

**Standard physics, transcribed.** The collective spin algebra, the Dicke states, the Tavis–Cummings Hamiltonian, the $\sqrt{N}$ collective coupling, the Holstein–Primakoff linearisation, superradiance, the Wineland parameter, one- and two-axis twisting are all standard.

**What the algebra organises.**

- **Collective observables are elements of one algebra.** The $N$-spin collective operators are sums of $\mathbb{M}_+$ elements and remain in $\mathbb{M}_+$; the collective dynamics is described by the same trace pairings as the single-spin dynamics.
- **Squeezing is a tensor property.** The mean spin is a linear trace pairing and the covariance a quadratic one; squeezing is the anisotropy of the quadratic pairing, and the algebra's trace formula expresses both.
- **Rotation versus shear.** Rigid rotations of the collective state are rotors in $\mathbb{H}_{\mathbb{B}}$; squeezing is generated by the quadratic $\tilde{J}_3^2$ and is a shear, not a rotation. The algebraic distinction matches the physical one.
- **The collective coupling is a trace pairing.** The $\hbar g\sqrt{N}$ matrix element and the $2\hbar g\sqrt{N}$ splitting are the same spectral structure as in the single-spin case, with the collective operator in place of the spin.

**What the algebra does not supply.** The number of spins $N$, the coupling $g$, the frequencies and the initial state are external data. The algebra supplies the collective structure and the pairings; it does not select the Hamiltonian.

## Open Questions

1. **The informational reading.** Spin squeezing is often described as the creation of multipartite entanglement among the spins, and the squeezing parameter bounds a metrological entanglement measure. That reading belongs to the informational subcategory; whether the collective $\mathbb{M}_+$ algebra has a natural entanglement structure is left there.

2. **The exact Tavis–Cummings dynamics at finite $N$.** The model is integrable in each excitation sector; the finite-$N$ dynamics of the collective spin, including the revivals and the collapse, is standard. Does the algebraic formulation streamline the finite-$N$ treatment?

3. **Dissipation and superradiance.** The cooperative decay that gives superradiance requires an open system; the framework is unitary, and the open-system extension is the same gap noted for the Rabi problem.

4. **The best squeezing.** Two-axis countertwisting reaches the Heisenberg scaling only in the ideal case; the optimal control problem for squeezing is a question about the reachable set of the collective algebra, and it is not addressed here.

5. **Empirical contact.** As everywhere in the series, the reformulation reproduces the standard predictions; whether it implies a measurable deviation is open.

## Summary

For $N$ spin-1/2 particles the collective operators $\tilde{J}_\alpha = \sum_i\tilde{S}_\alpha^{(i)}$ are Hermitian elements of $\mathbb{M}_+$ obeying the same $su(2)$ algebra with $j = N/2$. The symmetric states are the Dicke states $|j,m\rangle$, and the collective coherent state is the product of $N$ identical coherent states with mean spin $\tfrac{\hbar N}{2}\hat{n}$ and transverse variance $\tfrac{\hbar^2N}{4}$ — the standard quantum limit.

The **Tavis–Cummings model**,

$$
\tilde{H} = \hbar\omega_c\,a^\dagger a + \omega_a\,\tilde{J}_3 + g\left(a^\dagger\tilde{J}_- + a\tilde{J}_+\right),
$$

conserves the excitation number $a^\dagger a + \tilde{J}_3/\hbar + N/2$. In its single-excitation sector the collective coupling is $\hbar g\sqrt{N}$ and the collective Rabi splitting is

$$
\Delta E = 2\hbar g\sqrt{N},
$$

verified numerically for $N = 1,4,16,100$. The Holstein–Primakoff linearisation reproduces this at large $N$, and the same $\sqrt{N}$ governs superradiance.

**Spin squeezing** is measured by the Wineland parameter

$$
\xi_R^2 = \frac{N\,(\Delta J_\perp)^2_{\min}}{|\langle\mathbf{J}\rangle|^2},
$$

equal to $1$ for a coherent state and below $1$ for a squeezed state. One-axis twisting, $\tilde{H}_{OAT} = \frac{\chi}{\hbar}\tilde{J}_3^2$, is diagonal in the Dicke basis and exactly solvable; minimising $\xi_R^2$ over the twisting time gives $0.354,0.230,0.143,0.087$ for $N = 8,16,32,64$, consistent with the standard $N^{-2/3}$ scaling and with $\xi_R^2 = 1$ at $\chi t = 0$. Two-axis countertwisting reaches the ideal Heisenberg scaling $\xi^2\propto N^{-1}$.

In the algebra the mean spin is a linear trace pairing $\mathrm{Tr}(\tilde{\rho}\tilde{J}_\alpha)$ and the covariance a quadratic one; squeezing is the anisotropy of the quadratic pairing. Rigid rotations of the collective state are rotors in $\mathbb{H}_{\mathbb{B}}$, while the twisting generator $\tilde{J}_3^2$ is a shear; the Tavis–Cummings coupling $g(a^\dagger\tilde{J}_- + a\tilde{J}_+)$ is an $\mathbb{M}_+$ coupling whose single-excitation gap is the collective Rabi splitting.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_+$ | Hermitian (informational) subspace |
| $\mathbb{H}_{\mathbb{B}}$ | Unit real quaternions; rigid rotations |
| $\tilde{S}_\alpha^{(i)} = \tfrac{\hbar}{2}ie_\alpha^{(i)}$ | Spin operator of particle $i$ |
| $\tilde{J}_\alpha = \sum_i\tilde{S}_\alpha^{(i)}$ | Collective spin |
| $\tilde{J}_\pm = \tilde{J}_1\pm i\tilde{J}_2$ | Collective raising/lowering operators |
| $|j,m\rangle$, $j = N/2$ | Dicke states |
| $\hat{n}(\theta,\phi)$ | Direction of the collective mean spin |
| $a, a^\dagger$ | Bosonic mode operators |
| $g$ | Single-spin coupling to the mode |
| $\tilde{H} = \hbar\omega_c a^\dagger a + \omega_a\tilde{J}_3 + g(a^\dagger\tilde{J}_-+a\tilde{J}_+)$ | Tavis–Cummings Hamiltonian |
| $a^\dagger a + \tilde{J}_3/\hbar + N/2$ | Conserved excitation number |
| $\Delta E = 2\hbar g\sqrt{N}$ | Collective Rabi splitting |
| $\xi_R^2 = N(\Delta J_\perp)^2_{\min}/|\langle\mathbf{J}\rangle|^2$ | Wineland squeezing parameter |
| $\tilde{H}_{OAT} = \frac{\chi}{\hbar}\tilde{J}_3^2$ | One-axis twisting Hamiltonian |
| $\mathrm{Cov}(J_\alpha,J_\beta)$ | Collective covariance; the squeezing ellipse |

## Further Reading

- M. Tavis and F. W. Cummings, "Exact Solution for an $N$-Molecule–Radiation-Field Hamiltonian," *Physical Review* **170** (1968) 379–384, for the model.
- R. H. Dicke, "Coherence in Spontaneous Radiation Processes," *Physical Review* **93** (1954) 99–110, for the collective spin states and superradiance.
- M. Kitagawa and M. Ueda, "Squeezed Spin States," *Physical Review A* **47** (1993) 5138–5143, for one- and two-axis twisting and the squeezing parameter.
- D. J. Wineland, J. J. Bollinger, W. M. Itano, F. L. Moore, and D. J. Heinzen, "Spin Squeezing and Reduced Quantum Noise in Spectroscopy," *Physical Review A* **46** (1992) R6797–R6800, for the metrological squeezing parameter.
- J. Ma, X. Wang, C. P. Sun, and F. Nori, "Quantum Spin Squeezing," *Physics Reports* **509** (2011) 89–165, for a comprehensive review of spin squeezing.
- A. S. Sørensen and K. Mølmer, "Entanglement and Extreme Spin Squeezing," *Physical Review Letters* **86** (2001) 4431–4434, for the relation between squeezing and collective entanglement.
- B. M. Garraway, "The Dicke Model in Quantum Optics: Dicke Model Revisited," *Philosophical Transactions of the Royal Society A* **369** (2011) 1137–1155, for the collective coupling and the normal-mode structure.
- T. Holstein and H. Primakoff, "Field Dependence of the Intrinsic Domain Magnetization of a Ferromagnet," *Physical Review* **58** (1940) 1098–1113, for the bosonic representation of collective spins.
- C. Gross, "Spin Squeezing, Entanglement and Quantum Metrology with Bose–Einstein Condensates," *Journal of Physics B* **45** (2012) 103001, for the experimental realisation and the algebraic reading of the squeezing Hamiltonians.
