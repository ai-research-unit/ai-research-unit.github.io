# __The Null Four-Momentum: What the Cone Derives and What It Does Not__

## Introduction

A massless particle carries a four-momentum of vanishing biquaternion norm: a **null four-momentum**, an element of the material sector that lies on the zero-divisor cone. The photon is the leading case, and every massless field of the framework shares the same null shell; the roster is *The Cone and the Massless Particles in the Biquaternioid Structures over $\mathbb{C}$*'s. The identification is a statement about the zero-divisor cone, and the cone is the one object in this series that carries a long list of derived results. It is therefore worth asking, carefully, how much of the massless characterization the cone actually delivers.

The question is not idle. The companion article *The Photon in Biquaternionic Form* records, in its accounting of what is derived and what is imported, the row **masslessness $m=0$: represented, an input**. Nothing in that article connects the row to the cone results, and the cone article does not draw the verdict either. The two facts sit in different files. This article joins them and separates them: the cone **marks** the massless case, and the marking is exact and non-trivial, but the cone does not **choose** it.

The answer is a division, and it is stated at the outset.

What the cone derives, on its own and without further input:

- the massless shell is the zero-divisor cone, and it is the only shell that is one;
- the propagation speed is $c$, and $c$ is the same in every inertial frame, from the multiplicativity of the norm;
- a null four-momentum has no rest frame;
- a particle on the null shell moves at $c$ for every momentum, not merely in a limit;
- the null four-momentum is a multiple of an idempotent of the informational sector.

What the cone does not derive:

- the value $m=0$ itself — the algebra represents every value of $m$ on the same footing;
- the existence of a mass scale at all — the cone is scale-invariant, so the algebra cannot manufacture one;
- the physical selection of the massless branch over the massive one;
- the reduction from four polarization directions to two.

The distinction between the first list and the second is the distinction between a structure and a value. The cone is a structure; the masslessness of a particle is a value that the structure distinguishes but does not supply.

## The Four-Momentum and the Shell

### The four-momentum biquaternion

The four-momentum of a particle of rest mass $m$ and velocity $\vec v$ is the element of the material sector $\mathbb{M}_-$

$$
\tilde{P} \;=\; m\tilde{V} \;=\; \gamma m\left(ic\,e_t + \vec v\right) \;=\; i\,\frac{E}{c}\,e_t + \vec p,
$$

with $\gamma = (1-\vec v^2/c^2)^{-1/2}$, $E=\gamma mc^2$ the relativistic energy and $\vec p=\gamma m\vec v$ the three-momentum. The scalar part of $\tilde{P}$ is purely imaginary and the vector part is real, which is exactly the defining shape of the material sector; the same holds for the four-velocity $\tilde{V}$. The four-velocity is the four-momentum divided by one number, $m$, and that single number is where the mass enters.

### The norm is the shell

Because the biquaternion norm of a four-vector of the material sector is $\langle\tilde{R}\rangle_{\natural} = -c^2t^2 +x^2+y^2+z^2$ for $\tilde{R}=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, the norm of the four-momentum is

$$
\langle\tilde{P}\rangle_{\natural} \;=\; -\frac{E^2}{c^2} + \vec p^2 \;=\; -m^2c^2,
$$

the last equality being the ordinary mass-shell relation $E^2=\vec p^2c^2+m^2c^4$. The four-velocity carries the same norm for every particle, $\langle\tilde{V}\rangle_{\natural}=-c^2$, and the two statements are the same statement multiplied by $m^2$:

$$
\langle\tilde{P}\rangle_{\natural} = \langle m\tilde{V}\rangle_{\natural} = m^2\langle\tilde{V}\rangle_{\natural} = -m^2c^2,
$$

the middle step being the multiplicativity of the norm. This is worth pausing on. The four-velocity is a **fixed** element of the sector's geometry, of the same norm for every particle; the mass is a scale factor on it; and the algebra's own multiplicativity converts the fixed geometric statement into the mass-dependent shell.

### Mass is the value of the norm

The mass-shell relation, read backwards, says

$$
m^2c^2 = -\langle\tilde{P}\rangle_{\natural}.
$$

Mass is the negative of the norm of the four-momentum, up to the constant $c^2$. The norm is the framework's only invariant attached to a four-momentum, so in this interpretation **mass is the value of the invariant** — the invariant is the shell, and the mass is which shell. A particle is characterized, so far as the algebra's quadratic form is concerned, by one real number: the value of $\langle\cdot\rangle_{\natural}$ on its four-momentum.

## Four Things the Cone Derives

### The massless shell is the zero-divisor cone

Set $m=0$ in the shell. The condition becomes $\langle\tilde{P}\rangle_{\natural}=0$, which is $E=c|\vec p|$, and $\langle\tilde{P}\rangle_{\natural}=0$ on a nonzero element of $\mathbb{B}$ is precisely the definition of a zero divisor. So the massless shell is the part of the zero-divisor set that lies in the material sector, which is the light cone. This identification is the subject of *The Light Cone as the Biquaternion Zero-Divisor Cone* and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, and it is restated here only to fix what the cone owns.

What the cone adds to the bare equation $E=c|\vec p|$ is that the equation is not an accident of the units but the statement that the four-momentum is not invertible in the algebra, and that the non-invertibility is the same non-invertibility that the wave operator exhibits.

**Uniqueness of the shell.** Among the level sets of $\langle\cdot\rangle_{\natural}$ on $\mathbb{M}_-$, the null set is the only cone. The set $N = -m^2c^2$ with $m\neq0$ is a two-sheeted hyperboloid, disconnected and with a positive minimum gap from the origin; the set $N=0$ is a cone, and it is the only level set with the apex at the origin and with scaling invariance. So the algebra does not merely admit the massless case; it **singles it out geometrically** as the degenerate level. It singles it out and does not select it, and that gap is the subject of the next section.

### The propagation speed is $c$, and is frame-independent

For a four-wavevector $\tilde P=i(\omega/c)e_t+\vec k$, the cone article establishes $\Box f(\mathrm{Sc}(\tilde P\tilde{R}^{\natural})) = \langle\tilde P\rangle_{\natural}f''$ for every smooth $f$, so the wave equation holds for every phase exactly when $\langle\tilde P\rangle_{\natural}=0$, that is $\omega=c|\vec k|$. That is where the propagation speed comes from, and it is taken as given here.

What this article isolates is why the same $c$ governs every frame. The rotor conjugation $\tilde{Q}\mapsto\tilde U\tilde{Q}\tilde U^{*}$ with $\tilde U$ of unit norm acts on the sector, and the norm is multiplicative, so

$$
N\!\left(\tilde U\tilde{Q}\tilde U^{*}\right) = \langle\tilde U\rangle_{\natural}\,\langle\tilde{Q}\rangle_{\natural}\,\langle\tilde U^{*}\rangle_{\natural} = \left|\langle\tilde U\rangle_{\natural}\right|^2\langle\tilde{Q}\rangle_{\natural},
$$

using $\langle\tilde U^{*}\rangle_{\natural}=\overline{\langle\tilde U\rangle_{\natural}}$ and $\langle\tilde U\rangle_{\natural}=1$. The norm, and therefore its zero set, is invariant. A null four-momentum is null in every frame, so the condition $\omega=c|\vec k|$ is frame-independent, and the speed read off it is the same for every inertial observer. The constancy of the speed of light is thus not a second postulate laid beside the first; it is the multiplicativity of the norm applied to the invariance group of the cone.

The argument is short but it is doing real work. In the metric formulation the invariance of the light cone under the Lorentz group and the constancy of $c$ are two statements, and their agreement is a consistency to be checked. Here there is one statement: the norm is multiplicative and the rotor has unit norm. The cone article states the invariance; the point made here is the consequence for the speed, and the fact that the speed is a *derived* frame-independent number rather than a separate kinematical postulate.

### A null four-momentum has no rest frame

A rest frame is a frame in which the vector part of the four-momentum vanishes, $\vec p=0$. In such a frame $\langle\tilde{P}\rangle_{\natural} = -E^2/c^2$, which is strictly negative whenever $E\neq0$. But $\langle\cdot\rangle_{\natural}$ is invariant, so if $\tilde{P}$ is null in one frame it is null in every frame, and no frame can produce the negative value. Hence a null four-momentum has no rest frame: the transformation that would annihilate $\vec p$ does not exist in the group that preserves the cone. This is the algebraic form of the statement that light has no rest frame, and it is a consequence of the two facts already established, the invariance of the norm and the sign of the norm at rest.

The **physical interpretation** is immediate. A rest frame for the photon would be a frame in which it is at rest, and in that frame its four-momentum would be timelike, hence not null, hence not the four-momentum of a photon. The cone forbids it. This is not an extra rule about photons; it is the statement that "null" and "at rest" are contradictory values of one invariant.

### The massless particle moves at $c$, for every momentum

The speed follows from the shell. With $E=\left(\vec p^2c^2+m^2c^4\right)^{1/2}$ and $v = |\vec p|c^2/E$,

$$
\frac{v}{c} = \frac{|\vec p|c}{\sqrt{\vec p^2c^2+m^2c^4}} .
$$

At $m=0$ the expression is exactly $1$ for every $|\vec p|$, with no limiting procedure: the null shell is $E=c|\vec p|$ at every momentum, so the speed is $c$ at every momentum. For $m>0$ the speed increases monotonically towards $c$ as $m\to0$ but never reaches it, as the table shows with $c=1$, $|\vec p|=1$.

| $m$ | $E$ | $v/c$ | $\langle\tilde{P}\rangle_{\natural}$ |
|---|---|---|---|
| $1$ | $1.414214$ | $0.707107$ | $-1.000000$ |
| $0.5$ | $1.118034$ | $0.894427$ | $-0.250000$ |
| $0.1$ | $1.004988$ | $0.995037$ | $-0.010000$ |
| $0.01$ | $1.000050$ | $0.999950$ | $-0.000100$ |
| $0.001$ | $1.000000$ | $0.999999$ | $-0.000001$ |
| $0$ | $1.000000$ | $1.000000$ | $0.000000$ |


## What the Cone Does Not Derive

### Mass is a value, not a structure

Every statement in the previous section is a statement about the *shape* of the theory: which locus is special, which quantity is invariant, which configurations are forbidden. None of them is a statement about the *value* of $m$. The mass enters the four-momentum as a single free real multiplicative constant on the four-velocity, $\tilde{P}=m\tilde{V}$, and the algebra treats every value alike. A massive four-momentum is exactly as native to $\mathbb{M}_-$ as a null one: the check above confirmed that $\tilde{P}=i(E/c)e_t+\vec p$ lies in the material sector for every $m$, null or not, with $N=-m^2c^2$ in every case.

The cone marks the value $m=0$ and only that value. Distinguishing a value is not supplying it. The cone tells us that if a particle is massless its four-momentum is a zero divisor; it does not tell us that any particle is massless.

### The algebra has no mass scale

There is a structural reason behind the previous paragraph, and it is stronger than a statement about what the cone happens to say. The norm is homogeneous of degree two,

$$
\langle\lambda\tilde{Q}\rangle_{\natural} = \lambda^2\langle\tilde{Q}\rangle_{\natural}
$$

The null set is therefore invariant under every rescaling: if $\tilde{Q}$ is null then so is $\lambda\tilde{Q}$, for every $\lambda$. The cone is a scale-invariant object, and an algebra whose special locus is scale-invariant contains no preferred scale. To generate a mass scale one must put one in, and the framework does: the mass term is a term in the Lagrangian or the field equation, not in the algebra. The companion articles record the two choices side by side — *Canonical Quantization of the Biquaternion Maxwell Field* for the massless case and *Canonical Quantization of the Biquaternion Proca Field* for the massive one — and the difference is precisely the presence of a term the algebra does not contain.

This is the cleanest statement of the article. The framework's algebra cannot fix the photon's mass, because it cannot fix any mass; the value is empirical and is inserted where a scale must enter, that is, in the dynamics.

### The choice of the null branch, and the Proca alternative

The cone marks the massless shell, and the marking is sharp: the null shell is the only level set that is a cone, the only one on which the algebra fails to be invertible, and the only one that survives rescaling. If one takes "the algebra singles out the cone" as a physical principle, the massless case is preferred. But the framework does not take that step, and the companion photon article is explicit that it does not: masslessness is listed there as **represented**, not derived, and the Proca alternative as **equally writable**.

The honest statement is therefore a conditional. *If* the field is massless, *then* the cone is its shell, its speed is $c$ in every frame, it has no rest frame, and its four-momentum is a zero divisor. The conditional is fully derived. Its antecedent is supplied from outside. Writing $m$ as a free parameter and then setting it to zero is an act of physics, not of algebra, and no result in this series reverses it.

### The reduction to two polarizations

A separate input, often blurred with masslessness, is the transversality of the physical modes. The cone says nothing about it, and the reduction itself belongs to *The Photon in Biquaternionic Form*, which owns both the space in which it happens — the four polarization directions of $\mathbb{M}_-$ with the indefinite metric $\zeta=(-1,+1,+1,+1)$ — and the gauge gap by which it is made. This article records only the status of the reduction for the null element: it is imported, and it is not a consequence of the cone. Masslessness is what makes the removal natural, since it is what makes helicity Lorentz invariant, but natural is not the same as derived.

## The Null Four-Momentum as the Canonical Zero Divisor

### The null momentum is an idempotent multiple

The null element has a second face, and it is the one that connects the material and informational sectors. For a null four-momentum $\tilde{P}=i(E/c)e_t+\vec p$ with $\vec u=\vec p/|\vec p|$,

$$
\tilde{P} \;=\; 2i\,\frac{E}{c}\,\tilde\Pi(-\vec u),
\qquad
\tilde\Pi(\vec u) \;=\; \tfrac{1}{2}\left(e_t + i\vec u\right),
$$

an imaginary multiple of an idempotent of the informational sector. The idempotent satisfies $\tilde\Pi^2=\tilde\Pi$, is Hermitian, and has norm zero, so the null four-momentum is a scalar multiple of a **rank-one projector**.

This is what makes the identification "the photon's four-momentum is a zero divisor" more than a restatement of $E=c|\vec p|$. The null momentum is, up to the factor $2iE/c$, a **pure state** of the informational sector: the flagpole interpretation of the companion article *The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*, where the null direction and the projector are two faces of one object. The photon's lightlike momentum and a rank-one projector are the same element read in two sectors.

### What this gives and what it does not

What it gives is a genuine structural coincidence: the algebra's non-invertible elements in the material sector are in one-to-one correspondence with the projectors of the informational sector, up to a scale. The cone of the material sector is the scaled image of the projector sphere of the informational sector. That is a strong internal linkage between the two sectors, and it is derived.

What it does not give is a dynamics. The projector is a description of the momentum, not an equation of motion, and the identification of the projector with a quantum state is the interpretive step the informational-sector article owns. Whether the photon should be thought of as "a projector with an energy" is an interpretation of the algebra, not a result of it; the corpus states the interpretation and does not derive it.

## The Accounting

The division of the article, in one table. Each row is a statement about the photon as a null element, with its status and the place it comes from.

| Statement | Status | Where it comes from |
|---|---|---|
| The four-momentum is an element of $\mathbb{M}_-$ | Derived | the sector's definition; verified for every $m$ |
| The mass shell is the level set $N=-m^2c^2$ | Derived | the norm of the four-momentum |
| Mass is the value of the invariant, $m^2c^2=-\langle\tilde{P}\rangle_{\natural}$ | Derived | the shell, read backwards |
| The massless shell is the zero-divisor cone | Derived | the norm's vanishing set; the cone article |
| The null shell is the only shell that is a cone | Derived | scaling invariance; verified |
| The propagation speed is $c$ | Given | the cone article's $\Box$ computation |
| The speed $c$ is frame-independent | Derived | multiplicativity of the norm; verified on 100 rotors |
| A null four-momentum has no rest frame | Derived | invariance of $\langle\cdot\rangle_{\natural}$ and the sign of $\langle\cdot\rangle_{\natural}$ at rest; verified |
| The massless particle moves at $c$ for every $|\vec p|$ | Derived | the null shell; verified on 100 momenta |
| The null momentum is a scaled idempotent of $\mathbb{M}_+$ | Derived | the idempotent form of the real cone; verified |
| The value $m=0$ | Inserted | the field equation; not fixed by the algebra |
| Any mass scale at all | Inserted | the algebra is scale-invariant; no scale is native |
| The choice of the null branch over the massive one | Inserted | a physical selection the algebra does not make |
| The reduction to two transverse polarizations | Inserted | the subsidiary gauge condition |
| Quantization, the ladder, the number operator | Outside | the photon article's accounting, not revisited here |

## Boundaries

- **The subject is one element.** This article owns the null four-momentum as an object: the shell as the norm condition $N=-m^2c^2$, mass as the value of the invariant, the null momentum as a scaled idempotent of $\mathbb{M}_+$, the absence of a rest frame, the frame-independence of $c$ from the multiplicativity of the norm, the scale-invariance argument, and the verdict that the cone marks but does not choose masslessness.
- **The cone as a set is *The Cone and the Massless Particles in the Biquaternioid Structures over $\mathbb{C}$*'s to define.** The cone's two jobs in the two bands, the rank across the twelve rows, the nilpotent index and the roster of massless particles are stated there, and this article states them where its argument needs them; it takes the cone's boundary of invertibility from that article and from *The Light Cone as the Biquaternion Zero-Divisor Cone*.
- **The quantum photon is *The Photon in Biquaternionic Form*'s to define.** The polarisation space, circular polarisation, the helicity operator, the self-dual split, the ladder and the gauge are stated there; this article states the reduction to two polarisations only as far as it needs it, to record that the reduction is not a consequence of the cone.
- **The flagpole identity is elsewhere.** That the null direction and the projector are two faces of one object is *The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*.
- **Not claimed.** No dynamics: the projector describes a momentum, not an equation of motion. No derivation of $m=0$, of any mass scale, or of the choice of the null branch. The speed $c$ is taken from the cone article's $\Box$ computation.

## Summary

The four-momentum of a massless particle is $\tilde{P}=i(E/c)e_t+\vec p$, an element of the material sector whose biquaternion norm is $-m^2c^2$; mass is the value of the invariant, and the massless shell is the level set $N=0$, which is the zero-divisor cone. The cone derives, without further input, that the massless shell is the only level set that is a cone, that the propagation speed is $c$ and is the same in every frame by the multiplicativity of the norm, that a null four-momentum has no rest frame, and that a massless particle moves at $c$ for every momentum. The null four-momentum is moreover a scaled idempotent of the informational sector, so the cone of the material sector is the scaled image of the projector sphere, and the lightlike momentum and a rank-one pure state are one element read in two sectors.

The cone does not derive masslessness. The mass enters as a single free real scale on the four-velocity, $\tilde{P}=m\tilde{V}$, and the algebra treats every value alike; there is a structural reason, namely that the norm is homogeneous and the cone is scale-invariant, so the algebra contains no preferred scale and cannot manufacture one. The mass term is a term in the dynamics, and the massless and massive cases are the Maxwell and Proca alternatives, equally writable. The cone **marks** the massless case — sharply, uniquely, and non-trivially — and does not **choose** it. The correct statement is a conditional whose antecedent is empirical: if the field is massless, then the cone is its shell and all the derived consequences follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm |
| $\mathbb{M}_- = \mathrm{span}_\mathbb{R}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ | Material (anti-Hermitian) sector |
| $\mathbb{M}_+ = \mathrm{span}_\mathbb{R}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ | Informational (Hermitian) sector |
| $\tilde{R}=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Material coordinate; $\langle\tilde{R}\rangle_{\natural}=-c^2t^2+x^2+y^2+z^2$ |
| $\langle\tilde{R}\rangle_{\natural}=0$ | The light cone; the material part of the zero-divisor set $\mathcal{Z}$ |
| $\tilde{P}=m\tilde{V}=i\frac{E}{c}e_t+\vec p$ | Four-momentum, in $\mathbb{M}_-$; $E=\gamma mc^2$, $\vec p=\gamma m\vec v$ |
| $\tilde{V}=\gamma(ic\,e_t+\vec v)$ | Four-velocity, in $\mathbb{M}_-$; $\langle\tilde{V}\rangle_{\natural}=-c^2$ |
| $\langle\tilde{P}\rangle_{\natural}=-E^2/c^2+\vec p^2=-m^2c^2$ | Mass shell as a norm condition |
| $m^2c^2=-\langle\tilde{P}\rangle_{\natural}$ | Mass as the value of the invariant |
| $E=c\lvert\vec p\rvert$ | The null shell, $m=0$; equivalently $\langle\tilde{P}\rangle_{\natural}=0$ |
| $v=\lvert\vec p\rvert c^2/E$ | Speed from the shell; $v=c$ exactly at $m=0$ |
| $\tilde P=i\frac{\omega}{c}e_t+\vec k$ | Four-wavevector; $\langle\tilde P\rangle_{\natural}=0\Leftrightarrow\omega=c\lvert\vec k\rvert$ |
| $\tilde U\tilde U^{\natural}=e_t$ | Lorentz rotor (unit norm) |
| $\tilde{Q}\mapsto\tilde U\tilde{Q}\tilde U^{*}$ | Rotor conjugation; $\langle\cdot\rangle_{\natural}$ invariant, so the cone and $c$ are frame-independent |
| $\tilde\Pi(\vec u)=\tfrac{1}{2}(e_t+i\vec u)$ | Idempotent of $\mathbb{M}_+$; $\tilde\Pi^2=\tilde\Pi$, $\langle\tilde\Pi\rangle_{\natural}=0$ |
| $\tilde{P}=2i\frac{E}{c}\tilde\Pi(-\vec u)$, $\vec u=\vec p/\lvert\vec p\rvert$ | The null momentum as a scaled projector |
| $\langle\lambda\tilde{Q}\rangle_{\natural}=\lambda^2\langle\tilde{Q}\rangle_{\natural}$ | Homogeneity; the cone is scale-invariant, so no mass scale is native |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathcal{Z}=\{\tilde{Q}\neq0 : \langle\tilde{Q}\rangle_{\natural}=0\}$ | Zero-divisor set |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the light cone and the null interval.
- Albert Einstein, "Zur Elektrodynamik bewegter Körper", *Annalen der Physik* **17** (1905) 891–921, for the independence of the speed of light from the state of motion of the emitter.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for isotropic vectors and zero divisors in $\mathbb{C}\otimes\mathbb{H}$ and $M_2(\mathbb{C})$.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for idempotents, minimal ideals and the structure of matrix algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the null cone, the factorization of the wave operator, and the null direction as a projector in the spacetime algebra.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the characteristic cone and null directions.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* **22** (1907) 579–586, and Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* **46** (2013) 053001, for the null field and the massless shell.
- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* **7** (1936) 347–353, for the massive vector field whose mass term the algebra does not contain.
- The companion articles of this series: *The Light Cone as the Biquaternion Zero-Divisor Cone*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *The Photon in Biquaternionic Form*; *The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*; *The Local Complex Structure and the Speed of Light*; *Relativistic Mechanics in Biquaternionic Form*; *Zero Divisors as a Physical Locus in Biquaternionic Form*; *Canonical Quantization of the Biquaternion Proca Field*; *Conventions in the Biquaternion Universe*.
