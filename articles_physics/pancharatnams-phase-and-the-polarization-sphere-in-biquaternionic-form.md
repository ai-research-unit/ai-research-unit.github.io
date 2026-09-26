# __Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form__

## Introduction

When polarized light is passed through a sequence of polarizers, the interference phase between the initial and final beams contains a part that is not accumulated by propagation. Pancharatnam showed in 1956 that for three polarizations the effect is a phase equal to minus one half of the solid angle of the spherical triangle they define on the **Poincaré sphere**, the sphere whose points are the polarization states of a monochromatic beam. This **Pancharatnam phase** is the optical geometric phase, and it is classical: it is observed by the shift of interference fringes, with no reference to photons or to a quantised field.

The Poincaré sphere is a level set of the norm form of the biquaternion algebra. The polarization state of a beam is described by its coherence (Stokes) biquaternion, a Hermitian element of the algebra whose norm-form value measures the degree of polarization. The fully polarized states — the points of the Poincaré sphere — are exactly the **norm-form cone** of the Hermitian sector, the same cone that the companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* identifies with the idempotent states; the unpolarized state is the centre, and the partially polarized states fill the interior. The Pancharatnam phase is the **holonomy** of the natural connection on the cone, and its curvature is half the area form of the sphere:

1. The coherence biquaternion is $\tilde\rho=\frac12(S_0e_0+i\mathbf S\cdot\tilde e)\in\mathbb{M}_+$ with Stokes parameters $S_0,\mathbf S$; the norm form is $N(\tilde\rho)=\frac14(S_0^2-\mathbf S^2)$.
2. The fully polarized (pure) states are $N(\tilde\rho)=0$, the cone; after normalisation they are the Poincaré sphere.
3. Pancharatnam's in-phase criterion defines the natural connection on the ray space; its curvature is $-\frac12d\Omega$, half the area form, so the phase around a circuit is $-\frac12$ times the enclosed solid angle.
4. The three-polarizer phase is the same statement for a spherical triangle, and Girard's theorem turns it into a sum of angles.

The article is classical optics in the algebra. The "state" of a beam is its classical coherence matrix, the connection lives on the classical ray space, and the interference is classical. The companion article on the Berry phase develops the quantum two-level system, which shares the geometry; here the physics is a light beam, two polarizers, and an interferometer.

The conventions are those of the read list. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; $i$ is central, $i^2=-1$; ${}^\dagger$ is Hermitian conjugation; $\mathbb{M}_+$ is the Hermitian sector, $\mathbb{M}_-$ the anti-Hermitian one; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace. The norm form is $N(\tilde X)=\tilde X\bar{\tilde X}$. The Poincaré sphere is parametrised by the unit Stokes vector $\hat{\mathbf n}=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$.

The companion articles are:
- Companion article *The Symplectic Form and the Biquaternion Norm-Form Cone*, for the norm-form cone and its role as a level set.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian sector, the idempotents, and the cone.
- Companion article *Hannay's Angles and the Classical Geometric Phase in Biquaternionic Form*, for the classical dynamical counterpart, whose holonomy is the solid angle itself.
- Companion article *The Berry Phase and Geometric Phases in Biquaternionic Form*, for the quantum two-level reading of the same connection.

## Polarization of a Plane Wave and the Stokes Parameters

A monochromatic plane wave propagating along $e_3$ has a transverse complex electric field

$$
\mathbf E=(E_x,E_y,0),\qquad E_x,E_y\in\mathbb{C}.
$$

Its polarization is the ray of the **Jones vector** $\mathbf J=(E_x,E_y)$: two Jones vectors that differ by an overall complex phase describe the same polarization. The four **Stokes parameters** are the real bilinears

$$
S_0=|E_x|^2+|E_y|^2,\qquad S_1=|E_x|^2-|E_y|^2,
$$
$$
S_2=E_xE_y^*+E_x^*E_y,\qquad S_3=i\left(E_xE_y^*-E_x^*E_y\right),
$$

with the sign convention fixed once and for all. They satisfy

$$
S_1^2+S_2^2+S_3^2\le S_0^2 ,
$$

with equality for **fully polarized** light, and $\mathbf S=0$ for **unpolarized** light. The **degree of polarization** is

$$
P=\frac{\sqrt{S_1^2+S_2^2+S_3^2}}{S_0},
$$

$P=1$ for a fully polarized beam and $P=0$ for an unpolarized one. For a fully polarized beam the normalised Stokes vector $\hat{\mathbf n}=\mathbf S/S_0$ is a unit vector, and the map $\mathbf J\mapsto\hat{\mathbf n}$ sends rays to points of the unit sphere: the **Poincaré sphere**. Right and left circular polarizations are the poles, linear polarizations form the equator, and the antipode of a polarization is the orthogonal one.

The quantity $\langle A|B\rangle=\mathbf J_A^\dagger\mathbf J_B$ is the overlap of two Jones vectors; its modulus is $\sqrt{S_0^AS_0^B}$ times the cosine of half the angle between the Poincaré points of the two beams, and it sets the visibility of the interference between them.

## The Coherence Biquaternion and the Poincaré Sphere

### The Coherence Biquaternion

The polarization of a beam is encoded in its **coherence matrix** $\rho=\mathbf J\mathbf J^\dagger/S_0$ for a fully polarized beam, or in the ensemble average for a partially polarized one. It is Hermitian, positive semidefinite, and of unit trace, so it is an element of the Hermitian sector $\mathbb{M}_+$. Writing the two independent Hermitian combinations as the algebra basis, the coherence biquaternion is

$$
\tilde\rho=\tfrac12\left(S_0e_0+i\,S_1e_1+i\,S_2e_2+i\,S_3e_3\right)
=\tfrac12\left(S_0e_0+i\,\mathbf S\cdot\tilde e\right),
\qquad \tilde\rho=\tilde\rho^\dagger .
$$

The factor $i$ on the vector part is what makes the vector part Hermitian: the units $e_k$ are anti-Hermitian, so $ie_k$ is Hermitian, and the coefficients $S_k$ are real. The scalar part $S_0/2$ is real.

### The Norm Form

The norm form of the coherence biquaternion is

$$
N(\tilde\rho)=\tilde\rho\bar{\tilde\rho}
=\tfrac14\left(S_0^2-S_1^2-S_2^2-S_3^2\right)
=\tfrac14\left(S_0^2-\mathbf S^2\right).
$$

This is the algebra's **indefinite** form on $\mathbb{M}_+$: with $\tilde X=x_0e_0+i\mathbf x\cdot\tilde e$, the norm form is $N(\tilde X)=x_0^2-|\mathbf x|^2$, of signature $(1,3)$ on the four real parameters. The **degree of polarization** is read off it:

$$
P^2=1-\frac{4N(\tilde\rho)}{S_0^2}.
$$

### The Cone as the Poincaré Sphere

The fully polarized states are $P=1$, that is

$$
N(\tilde\rho)=0 .
$$

This is the **norm-form cone** of $\mathbb{M}_+$, and it is exactly the cone of idempotents: a rank-one projection satisfies $\tilde\rho^2=\tilde\rho$ and $N(\tilde\rho)=0$, and conversely a Hermitian element of the cone with unit trace is a pure state. Normalising $S_0=1$, the cone is

$$
S_1^2+S_2^2+S_3^2=1 ,
$$

which is the **Poincaré sphere**. The identification is therefore

$$
\boxed{\;\text{fully polarized states}=\text{the norm-form cone of }\mathbb{M}_+=\text{the Poincaré sphere}\;}
$$

for the beam, and the same cone is the idempotent manifold of the sector. The unpolarized state $S_0\neq0$, $\mathbf S=0$ is the centre of the ball; the partially polarized states are the interior points $0<P<1$; and the closure of the interior is the ball of radius $S_0$, with the cone as its boundary. Depolarization moves the coherence biquaternion inward along a radius, and the cone is the extremal boundary where the coherence is complete.

## Pancharatnam's In-Phase Criterion

Two beams with Jones vectors $\mathbf J_A$ and $\mathbf J_B$ can interfere. The intensity of the sum is

$$
|\mathbf J_A+\mathbf J_B|^2=|\mathbf J_A|^2+|\mathbf J_B|^2+2\,\mathrm{Re}\,\langle A|B\rangle ,
$$

so the interference term is governed by the complex overlap $\langle A|B\rangle$. Pancharatnam's criterion defines the **phase difference** between two polarization states as

$$
\arg\langle A|B\rangle=\arg\left(\mathbf J_A^\dagger\mathbf J_B\right),
$$

with the convention that states are **in phase** when $\langle A|B\rangle$ is real and positive. This is the natural definition because it is the phase that appears in the interference of the two beams: when $\langle A|B\rangle$ is real and positive the beams add constructively.

The criterion is not transitive, and that is the source of the geometric phase. If $A$ is in phase with $B$ and $B$ with $C$, then $A$ need not be in phase with $C$: the product

$$
\langle A|B\rangle\langle B|C\rangle\langle C|A\rangle
$$

is in general complex, and its argument is the **Pancharatnam phase** of the circuit $A\to B\to C\to A$,

$$
\gamma_{\mathrm{Panch}}=-\arg\Bigl(\langle A|B\rangle\langle B|C\rangle\langle C|A\rangle\Bigr).
$$

The phase is a property of the closed circuit of polarization states and not of the individual overlaps. It is the discrete version of the holonomy of a connection, and the next sections identify the connection.

## The Pancharatnam Connection and Its Curvature

### The Connection on the Ray Space

For a smooth family of polarizations, write the two-component amplitude in the circular basis, $(E_R,E_L)$, in the standard form with the Poincaré angles $(\theta,\phi)$ of the state,

$$
(E_R,E_L)=\left(\cos\tfrac{\theta}{2},\ \sin\tfrac{\theta}{2}\,e^{i\phi}\right),
$$

normalised to $S_0=1$; the phase of the first component is a choice of gauge, and the second is the relative phase. The circular basis is the one in which the axes of the parametrisation are the axes of the sphere: the polar component of the Stokes vector is the difference of the two intensities and the equatorial pair is carried by their relative phase, so that, with the two circular senses named in the sign convention of $S_3$, the amplitude above carries exactly the Stokes vector $\hat{\mathbf n}=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$. Differentiating,

$$
\langle J|\partial_\theta J\rangle=0,\qquad
\langle J|\partial_\phi J\rangle=i\sin^2\tfrac{\theta}{2}.
$$

The **Pancharatnam connection** is the imaginary part of the overlap with the derivative. In the horizontal gauge, the gauge in which the amplitude accumulated along the azimuthal circles carries no phase beyond the connection, it is

$$
\mathcal A=i\,\langle J|dJ\rangle
=i\,\langle J|\partial_\phi J\rangle\,d\phi
=-\sin^2\tfrac{\theta}{2}\,d\phi
=-\tfrac12\left(1-\cos\theta\right)d\phi .
$$

The connection is real, as it must be for a phase; it is the connection whose parallel transport keeps neighbouring states in Pancharatnam's sense of being in phase. The overall phase of $\mathbf J$ is the gauge freedom, and $\mathcal A$ is gauge-dependent, but its integral around a closed circuit is not.

### The Criterion and the Transport

The in-phase criterion is itself a rule of transport. If the state at $t+dt$ is to be in phase with the state at $t$, then the overlap $\langle J(t)|J(t+dt)\rangle$ must be real and positive, that is

$$
\mathrm{Im}\,\langle J|\dot J\rangle=0
$$

along the transport. A family of states satisfying this condition is **horizontal** for the connection: it is the family obtained by Pancharatnam transport, and the prescription is the optical analogue of parallel transport. The connection $\mathcal A=i\langle J|dJ\rangle$ is the one-form whose integral gives the residual phase when the states are compared in a fixed gauge rather than along the horizontal transport.

The residual phase is a property of closed circuits only. If the representatives are changed, $|J_k\rangle\to e^{i\chi_k}|J_k\rangle$, the overlaps change by $e^{i(\chi_{k+1}-\chi_k)}$, and the product around a closed sequence is unchanged because the phases telescope. Hence the Pancharatnam phase of a circuit is gauge invariant, while the phase $\arg\langle A|B\rangle$ of a pair is not: the physical content of a pair of states is the interference visibility $|\langle A|B\rangle|$, and the physical content of a circuit is the closed-loop phase. This is the same distinction that the symplectic article draws between the potential and the symplectic form: the local object is gauge dependent, the loop integral is not.

### The Curvature and the Half-Solid-Angle Rule

The curvature of the connection is

$$
\mathcal F=d\mathcal A
=-\tfrac12\sin\theta\,d\theta\wedge d\phi
=-\tfrac12\,d\Omega ,
$$

where $d\Omega=\sin\theta\,d\theta\wedge d\phi$ is the area form of the unit sphere. The curvature is a constant multiple of the area form, so the holonomy of any closed circuit is $-1/2$ times the enclosed solid angle:

$$
\gamma_{\mathrm{Panch}}=\oint\mathcal A
=\int\!\!\int_{\text{enclosed}}\mathcal F
=-\frac12\,\Omega_{\text{enclosed}} .
$$

This is **Pancharatnam's half-solid-angle rule**. The factor $\tfrac12$ is the signature of the double cover: the curvature is half the area form, so the total flux over the whole sphere is $2\pi$ rather than $4\pi$, and the connection is the vector potential of a half-strength monopole at the centre of the Poincaré sphere. The same factor appeared in the companion article on the Berry phase and, in the double cover of the rotor, in the rigid-body article.

### Verification on the Sphere

Two checks fix the sign and the factor.

**Latitude circle.** For a circuit of constant polar angle $\theta_0$,

$$
\gamma_{\mathrm{Panch}}=\oint\mathcal A
=-\tfrac12\left(1-\cos\theta_0\right)\cdot2\pi
=-\tfrac12\,\Omega ,
$$

with $\Omega=2\pi(1-\cos\theta_0)$ the solid angle of the cap. Numerically, accumulating the discrete overlaps $\langle J(\theta_0,\phi_k)|J(\theta_0,\phi_{k+1})\rangle$ around the circle reproduces $\pm\Omega/2$ precisely; the sign is the one fixed by the convention $\gamma_{\mathrm{Panch}}=-\arg\prod_k\langle J_k|J_{k+1}\rangle$.

**Spherical triangle.** For three states $A,B,C$, the discrete product

$$
\arg\Bigl(\langle A|B\rangle\langle B|C\rangle\langle C|A\rangle\Bigr)
$$

equals $+\Omega_{ABC}/2$, where $\Omega_{ABC}$ is the signed solid angle of the triangle they define, positive for the orientation $A\to B\to C$; hence $\gamma_{\mathrm{Panch}}=-\Omega_{ABC}/2$. This is Pancharatnam's original three-polarizer result. Girard's theorem for a spherical triangle of angles $\alpha,\beta,\gamma$ gives

$$
\Omega_{ABC}=\alpha+\beta+\gamma-\pi ,
$$

so the phase is read off the angles of the triangle on the Poincaré sphere, which is what makes the effect measurable: the angles are the orientations of the polarizers in the laboratory.

## The Three-Polarizer Experiment

The experimental realisation is a sequence of three polarizers with axes $A$, $B$, $C$, followed by an analyser. The beam that passes is the projection of the input onto the three successive directions; the resulting complex amplitude is proportional to

$$
\langle A|B\rangle\langle B|C\rangle\langle C|A\rangle ,
$$

and its phase is the Pancharatnam phase. Rotating one polarizer around the sphere changes the enclosed solid angle and therefore the interference phase; the fringe shift measures the solid angle directly.

Three cases of the rule are worth recording. For **three linear polarizers equally spaced** in azimuth (axes at $0^\circ,60^\circ,120^\circ$) all three states lie on the equator, the circuit is degenerate, and the enclosed region is a hemisphere; the product $\langle A|B\rangle\langle B|C\rangle\langle C|A\rangle$ is real and negative, so the Pancharatnam phase is $\pi$, that is, $-\frac12$ of the hemisphere's solid angle $2\pi$. For **three polarizers whose axes return to the start**, the circuit is traversed out and back, the enclosed area vanishes, and the phase returns to zero modulo $2\pi$. For a circuit whose enclosed region is a **hemisphere** — for instance a circuit that lies on a great circle, or any circuit that splits the sphere into two halves of equal area — the phase reaches $\pi$ in magnitude, which is the largest value the half-solid-angle rule gives when the enclosed solid angle is taken as the smaller of the two regions (at most $2\pi$); the sign distinguishes the two senses of encirclement. The effect is classical and its magnitude is a pure number times the solid angle.

## The Norm-Form Reading of the Phase

The geometric phase has an algebraic reading in terms of the norm form. The circuit of polarization states is a circuit on the cone $N(\tilde\rho)=0$ of the Hermitian sector, and the connection's curvature, $-\frac12$ times the area form of the sphere, is a structure on that cone. The cone is the extremal boundary of the coherence ball, and the phase is an obstruction to flattening the boundary: it is the curvature of the natural connection on the cone. In the language of the preceding articles, the connection lives on the level set of the norm form, exactly as the Souriau form does on the coadjoint orbit and the Hannay connection does on the sphere of directions.

The analogy with the dynamical case is exact at the level of the geometry. For the classical spin of the companion article the transported object is the vector $\tilde S$, and the holonomy of a circuit is the **full** solid angle $\Omega$. For the optical case the transported object is the **ray** $\mathbf J$ — the amplitude, not its Stokes vector — and the holonomy is half the solid angle, $-\Omega/2$. The factor of $2$ between the two is the double cover: the amplitude is the spinor whose bilinear is the Stokes vector, and the transport of the spinor is half as fast in phase as the transport of its bilinear. The two articles describe one geometry with two objects, the vector and the spinor, and the ratio of the phases is the ratio of their squares.

## What Is Structural and What Is Familiar

**Familiar, rewritten.** The Stokes parameters, the degree of polarization, the Poincaré sphere, the use of the Jones vector, and the interference of polarized beams are standard classical optics, cited as such. Pancharatnam's discovery of the phase and its measurement through polarizer sequences are standard, and the relation of the phase to the solid angle is the standard half-solid-angle rule.

**Structurally the algebra's.**

1. The coherence matrix is an element of the Hermitian sector $\mathbb{M}_+$; written as a biquaternion, it is $\tilde\rho=\frac12(S_0e_0+i\mathbf S\cdot\tilde e)$.
2. The norm form on $\mathbb{M}_+$ is indefinite, $N(\tilde\rho)=\frac14(S_0^2-\mathbf S^2)$, and the **degree of polarization** is $P^2=1-4N(\tilde\rho)/S_0^2$.
3. The fully polarized states are the **norm-form cone** $N(\tilde\rho)=0$, which after normalisation is the Poincaré sphere; it is simultaneously the idempotent manifold of the sector. The unpolarized state is the centre, and the partially polarized states are the interior.
4. The Pancharatnam connection on the cone has curvature $-\frac12\,d\Omega$, half the area form, so the phase around a circuit is $-\frac12$ of the enclosed solid angle, and the three-polarizer rule and Girard's theorem follow.
5. The half-strength curvature and the half-solid-angle rule are the double-cover factor: the amplitude is the spinor of the Stokes vector, and the dynamical counterpart of the same geometry gives the full solid angle.

## Summary

Pancharatnam's phase is the classical optical geometric phase, and in the biquaternion algebra it is the holonomy of the natural connection on the norm-form cone of the Hermitian sector.

- A beam's polarization is described by its coherence biquaternion $\tilde\rho=\frac12(S_0e_0+i\mathbf S\cdot\tilde e)\in\mathbb{M}_+$, with $N(\tilde\rho)=\frac14(S_0^2-\mathbf S^2)$ and degree of polarization $P^2=1-4N(\tilde\rho)/S_0^2$.
- The fully polarized states are the cone $N(\tilde\rho)=0$, which is the Poincaré sphere after normalisation and the idempotent manifold of $\mathbb{M}_+$; the unpolarized state is the centre and the partially polarized states the interior.
- Pancharatnam's in-phase criterion, $\arg\langle A|B\rangle$, defines the connection $\mathcal A=i\langle J|dJ\rangle=-\frac12(1-\cos\theta)d\phi$ on the ray space, in the horizontal gauge of the amplitude written in the circular basis.
- The curvature is $\mathcal F=-\frac12\sin\theta\,d\theta\wedge d\phi=-\frac12\,d\Omega$, so the phase around a circuit is $-\frac12$ of the enclosed solid angle; the three-state rule is $\gamma_{\mathrm{Panch}}=-\arg(\langle A|B\rangle\langle B|C\rangle\langle C|A\rangle)=-\Omega_{ABC}/2$, and Girard's theorem gives $\Omega_{ABC}=\alpha+\beta+\gamma-\pi$.
- The dynamical counterpart (Hannay's angle) transports the Stokes vector rather than the amplitude and accumulates the full solid angle; the factor $\tfrac12$ is the double cover, the amplitude being the spinor of the Stokes vector.

The phase is classical: it is measured by the shift of interference fringes of an ordinary light beam through ordinary polarizers, and it is computed from the geometry of the Poincaré sphere.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbf J=(E_x,E_y)$ | Jones vector of the beam |
| $S_0,\mathbf S=(S_1,S_2,S_3)$ | Stokes parameters |
| $P=\sqrt{\mathbf S^2}/S_0$ | Degree of polarization |
| $\tilde\rho=\frac12(S_0e_0+i\mathbf S\cdot\tilde e)\in\mathbb{M}_+$ | Coherence biquaternion |
| $N(\tilde\rho)=\frac14(S_0^2-\mathbf S^2)$ | Norm form; indefinite on $\mathbb{M}_+$ |
| $N(\tilde\rho)=0$ | Cone: fully polarized states = Poincaré sphere = idempotents |
| $\hat{\mathbf n}=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$ | Unit Stokes vector on the Poincaré sphere |
| $\mathbf J(\theta,\phi)=(\cos\frac\theta2,\sin\frac\theta2e^{i\phi})$ | Normalised Jones vector |
| $\mathcal A=-\frac12(1-\cos\theta)d\phi$ | Pancharatnam connection |
| $\mathcal F=-\frac12\sin\theta\,d\theta\wedge d\phi$ | Curvature, half the area form |
| $\gamma_{\mathrm{Panch}}=-\frac12\Omega$ | Pancharatnam phase (half-solid-angle rule) |
| $\Omega_{ABC}=\alpha+\beta+\gamma-\pi$ | Signed solid angle of a spherical triangle (Girard's theorem) |

## Further Reading

- S. Pancharatnam, "Generalized theory of interference, and its applications," *Proceedings of the Indian Academy of Sciences A* **44** (1956) 247–262, for the phase and the three-polarizer result.
- M. V. Berry, "The adiabatic limit and the semiclassical limit," *Journal of Physics A* **17** (1984) 1225–1233, for the geometric phase in the adiabatic transport of polarization.
- M. V. Berry, "Quantal phase factors accompanying adiabatic changes," *Proceedings of the Royal Society A* **392** (1984) 45–57, for the geometric phase of which Pancharatnam's is the optical instance.
- R. Bhandari, "Polarization of light and topological phases," *Physics Reports* **281** (1997) 1–64, for a review of Pancharatnam's phase and its experiments.
- A. Shapere and F. Wilczek (eds.), *Geometric Phases in Physics* (World Scientific, 1989), for the unified treatment of the optical and quantum phases.
- M. Born and E. Wolf, *Principles of Optics* (Cambridge, 1999), for the Stokes parameters, the Poincaré sphere, and the coherence matrix.
- G. B. Airy, "On the composition and resolution of streams of polarized light from different sources," *Transactions of the Cambridge Philosophical Society* **9** (1852) 399, for the early interference of polarized beams.
- J. H. Hannay, "Angle variable holonomy in adiabatic excursion of an integrable Hamiltonian," *Journal of Physics A* **18** (1985) 221–230, for the dynamical counterpart of the same geometry.
