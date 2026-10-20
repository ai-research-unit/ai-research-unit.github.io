# __Larmor Precession and the Classical Magnetic Moment in Biquaternionic Form__

## Introduction

A magnetic moment placed in a magnetic field experiences a torque, and a torque on a moment that is rigidly tied to an angular momentum makes the momentum precess. This is the **Larmor precession**, and it is the simplest motion of an intrinsic magnetic moment. Its frequency, the **Larmor frequency** $\omega_L = |\gamma|B$, is fixed by the gyromagnetic ratio $\gamma$ of the system, and it is the quantity on which magnetic resonance, the Einstein–de Haas and Barnett effects, and the classical account of the gyromagnetic factor all rest.

This article treats the magnetic moment and its precession as **classical** and **non-quantum** objects. The moment is the moment of a current distribution, or an intrinsic moment attributed to the body; it is a vector in the material sector, and its equation of motion is the classical torque equation. Nothing in the article requires a spinor, a Hilbert space, or a quantum state. The quantum treatment of the same precession — the evolution of an idempotent under a Hermitian Hamiltonian, and the trace formula that gives $\langle S_x\rangle(t')$ — is the subject of the companion articles *Spin-1/2 Quantum Physics in Biquaternionic Form* and *Exercise: Spin Precession in a Magnetic Field*; it is cited here and not reproduced.

The biquaternion algebra contributes three things to the classical subject, and they are the reason the article is in this framework rather than in three-vector notation. First, the moment and the field are both pure real quaternions, and a **single quaternion product** yields the two bilinears of the magnetic coupling at once: its scalar part is the energy $-\vec\mu\cdot\vec B$, and its vector part is the torque $\vec\mu\times\vec B$. Second, the precession equation acquires the form of a **commutator**, $d\vec\mu/dt' = \tfrac{1}{2}[\vec\mu,\vec\omega_G]$, which is the classical Poisson-bracket evolution realized inside the algebra. Third, the solution is a **rotor conjugation**, $\vec\mu(t') = \tilde u(t')\,\vec\mu(0)\,\tilde u(t')^{*}$, with a unit real quaternion whose half-angle is the same half-angle that appears throughout the series. The third point is what ties this article to the two that follow it: the rotor is the same object in the classical and in the spin-$\tfrac{1}{2}$ description, which is why the classical moment and the intrinsic moment obey the same precession law.

The conventions are those of the foundational articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_\mu^2 = -e_t$, and the scalar imaginary is $i$ (central, $i^2 = -1$). The material sector is the anti-Hermitian subspace $\mathbb{M}_-$ and the informational sector is the Hermitian subspace $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$. The real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the fixed space of complex conjugation, the home of the rotation rotors. The magnetic induction is $\vec B = \mu\vec H$, and the field strength is written in the canonical form $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ of the article *The Field-Strength Biquaternion and Its Invariants*.

## The Magnetic Moment of a Current Distribution

### Definition

For a steady current distribution of density $\vec j(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, the **magnetic moment** is

$$
\vec\mu = \frac{1}{2}\int \vec r\times\vec j\,d^3x .
$$

For a planar loop carrying current $I$ and bounding a vector area $\vec A$, the integral gives the elementary result

$$
\vec\mu = I\,\vec A,
$$

and for a charge $ϙ$ moving on a circle of radius $\rho$ with angular frequency $\omega$, it gives

$$
\mu = \frac{1}{2}\,ϙ\rho^2\omega .
$$

Both are the standard formulae of magnetostatics, and both will be used below. The moment is an **axial vector**: it is built from a cross product, so it changes sign under a reflection of space while a polar vector does not.

### The Moment as a Pure Real Quaternion

The axial vectors of the material sector are represented in the biquaternion algebra by the **pure real quaternions**,

$$
\vec\mu = \mu_1 \vec e_x + \mu_2 \vec e_y + \mu_3 \vec e_z \in \mathbb{H}_{\mathbb{B}},
\qquad
\vec B = B_x \vec e_x + B_y \vec e_y + B_z \vec e_z \in \mathbb{H}_{\mathbb{B}} .
$$

This is the same slot that carries the three real spatial directions $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ of the material coordinate $\tilde{R} = ict'\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, and it is the slot in which the magnetic field appears in the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$. The moment and the induction are therefore elements of the *same* real subspace, and their bilinears can be formed with the ordinary quaternion product.

For a pure real quaternion $\vec a$ and a pure real quaternion $\vec b$, the quaternion product splits into a scalar and a vector part,

$$
\vec a\,\vec b = -\,\vec a\cdot\vec b\,e_t + \vec a\times\vec b,
$$

with the scalar part the negative of the dot product and the vector part the cross product. Applied to the moment and the induction, this one identity contains the whole of the classical magnetic coupling:

$$
\vec\mu\,\vec B = -\,\vec\mu\cdot\vec B\,e_t + \vec\mu\times\vec B.
$$


### The Moment of a Rigid Rotor

The classical moment of a body in rigid rotation is the case that fixes the gyromagnetic ratio. If the body rotates with angular velocity $\vec\omega$ and carries charge density $\rho_c$, the local current is $\vec j = \rho_c\,\vec\omega\times\vec r$, and the moment is

$$
\vec\mu = \frac{1}{2}\int \rho_c(\vec r)\,\vec r\times(\vec\omega\times\vec r)\,d^3x
= \frac{1}{2}\,\mathcal{M}\,\vec\omega,
$$

where

$$
\mathcal{M}_{ij} = \int \rho_c(\vec r)\left(r^2\delta_{ij} - r_i r_j\right)d^3x
$$

is the **charge inertia tensor**, the charge-weighted analogue of the mass inertia tensor

$$
I_{ij} = \int \rho_m(\vec r)\left(r^2\delta_{ij} - r_i r_j\right)d^3x .
$$

The mechanical angular momentum is $\vec L = I\,\vec\omega$. The two tensors are the entire classical input of the gyromagnetic problem: whether the ratio of the moment to the angular momentum is the orbital value $ϙ/2m$ or something else is decided by whether $\mathcal{M}$ is proportional to $I$. That question is taken up in the article *The Classical Origin of g = 2 in Biquaternionic Form*; here it is enough to record that the moment of a rigid rotor is a pure real quaternion like any other axial vector.

### The Moment of a Spin

A body may also carry an **intrinsic** magnetic moment, one that is not the moment of any rigid motion of its charge. Such a moment is attributed to the body rather than computed from a current distribution, and it is the intrinsic case that the later articles of this subcategory treat. Its biquaternion representative is the vector slot with the central factor,

$$
i\,\vec\mu = \mu_k\,i \vec e_k = \mu_1\,i \vec e_x + \mu_2\,i \vec e_y + \mu_3\,i \vec e_z \in \mathbb{M}_+ ,
$$

the imaginary pure quaternion being the informational-sector twin of the real pure quaternion $\vec\mu = \mu_k\vec e_k$. The two descriptions are exchanged by multiplication by $i$, exactly as the two sectors are; both describe the same physical moment, and the choice between them is a choice of which sector's representative is being written. For a moment tied to an intrinsic angular momentum $\vec S$, the coefficient is the gyromagnetic ratio,

$$
\vec\mu = \gamma\,\vec S,
$$

and the precession law below is the same for the intrinsic and the convective moment.

## Energy and Torque

### The Two Bilinears of One Product

The coupling of a magnetic moment to a magnetic field is

$$
E = -\,\vec\mu\cdot\vec B,
$$

and the torque it exerts is

$$
\vec\tau = \vec\mu\times\vec B.
$$

In the biquaternion algebra both are read off the **same product** $\vec\mu\,\vec B$:

$$
E = \mathrm{Sc}\!\left(\vec\mu\,\vec B\right),
\qquad
\vec\tau = \mathrm{Vect}\!\left(\vec\mu\,\vec B\right),
$$

where $\mathrm{Sc}$ and $\mathrm{Vect}$ are the scalar and vector parts. The energy is the scalar part and the torque the vector part, and no second product is needed. This is the biquaternion form of the elementary fact that the magnetic interaction is a single bilinear of two axial vectors, whose symmetric part is the energy and whose antisymmetric part is the torque.

The energy has its minimum when the moment is aligned with the field, $E = -\mu B$, and its maximum when it is anti-aligned, $E = +\mu B$; the torque vanishes in both cases because $\vec\mu\times\vec B = 0$ there. These two alignments are the stable and unstable equilibria of the moment in the field, and the precession below is the motion about a tilted configuration, in which the energy is constant and the torque does no work.

### The Work and the Conservation of Energy

Because the torque is always perpendicular to the moment, $\vec\tau\cdot\vec\mu = 0$, and because the torque is also perpendicular to the field, the energy $E = -\vec\mu\cdot\vec B$ is conserved in a static uniform field:

$$
\frac{dU}{dt'} = -d\vec\mu/dt'\cdot\vec B = -\left(\gamma\,\vec\mu\times\vec B\right)\cdot\vec B = 0 .
$$

The magnitude of the moment is likewise conserved, since the equation of motion is a rotation; the biquaternion statement is that the biquaternion norm $\langle\vec\mu\rangle_{\natural} = \vec\mu\vec\mu^{\natural} = |\vec\mu|^2$ is constant. A moment of fixed length and fixed energy precesses on a cone about the field direction, and the next sections find the cone's angular frequency.

## The Larmor Equation

### Derivation from the Torque

The angular momentum of the system is $\vec S$, and the moment is tied to it by $\vec\mu = \gamma\vec S$. The torque equation $d\vec S/dt' = \vec\tau$ becomes

$$
d\vec S/dt' = \vec\mu\times\vec B = \gamma\,\vec S\times\vec B,
$$

and multiplying by $\gamma$ gives the equation for the moment itself:

$$
\boxed{\;d\vec\mu/dt' = \gamma\,\vec\mu\times\vec B = \vec\mu\times\left(\gamma\vec B\right).\;}
$$

This is the **Larmor equation**. Its content is that the moment precesses about the field direction with angular velocity

$$
\vec\omega_L = -\,\gamma\,\vec B,
$$

the minus sign expressing the fact that the rotation sense is opposite to the field when $\gamma$ is positive. Equivalently, the moment rotates about $\vec B$ with angular frequency $\omega_L = |\gamma|\,B$, in the sense fixed by the sign of $\gamma$.


### The Biquaternion Commutator Form

The cross product in the Larmor equation is the vector part of a quaternion product, and the equation can therefore be written as a commutator. For pure real quaternions the commutator is twice the cross product,

$$
[\,\vec\mu,\vec\omega\,] = 2\,\vec\mu\times\vec\omega,
$$

so that, defining the **Larmor generator**

$$
\vec\omega_G = \gamma\,B_x\vec e_x + \gamma\,B_y\vec e_y + \gamma\,B_z\vec e_z = \gamma\,\vec B \in \mathbb{H}_{\mathbb{B}},
$$

the Larmor equation reads

$$
\boxed{\;d\vec\mu/dt' = \tfrac{1}{2}\left[\,\vec\mu,\;\vec\omega_G\,\right].\;}
$$

The equation of motion is thus an **inner derivation** of the algebra, $d\vec\mu/dt' = -\mathrm{ad}_{\vec\omega_G/2}(\vec\mu) = \mathrm{ad}_{\vec\omega_L/2}(\vec\mu)$. The Larmor generator $\vec\omega_G$ is the negative of the angular velocity $\vec\omega_L = -\gamma\vec B$ of the precession: the first is the element written in the bracket, the second generates the derivation, and the two are listed separately in the notation table. Its antisymmetry is manifest — a commutator changes sign when its arguments are exchanged — and its trace vanishes, $\mathrm{Tr}[\vec\mu,\vec\omega_G] = 0$, which is the algebraic statement that the rotation preserves the biquaternion norm.

This is the classical bracket form of the dynamics. The Hamiltonian of the moment in the field is $H = -\gamma\,\vec S\cdot\vec B$, and the classical evolution of any observable is $df/dt' = \{f,H\}$; the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator* shows that the components of angular momentum satisfy $\{S_i,S_j\} = \epsilon_{ijk}S_k$, from which

$$
dS_{i}/dt' = \{S_i,H\} = -\gamma B_j\,\{S_i,S_j\} = -\gamma B_j\,\epsilon_{ijk}S_k = \gamma\,(\vec S\times\vec B)_i,
$$

which is the Larmor equation again. The biquaternion commutator $\tfrac{1}{2}[\vec\mu,\vec\omega_G]$ is that Poisson bracket written in the algebra, and it is the same bracket that the quantum article realizes as $[\tilde{S}_i,\tilde{S}_j] = i\hbar\,\epsilon_{ijk}\tilde{S}_k$.

### The Time-Dependence of the Moment

Writing the solution of the Larmor equation directly, the moment at time $t'$ is the initial moment rotated about the field direction by the angle $-\gamma B t'$:

$$
\vec\mu(t') = \mathcal{R}\!\left(-\gamma B t',\;\vec u_B\right)\vec\mu(0),
$$

where $\mathcal{R}(\theta,\vec u)$ is the right-handed rotation through $\theta$ about $\vec u$. For a moment initially making an angle $\alpha$ with the field, the component along the field is constant, $\mu_\parallel = \mu\cos\alpha$, and the transverse component rotates uniformly,

$$
\mu_\perp(t') = \mu\sin\alpha\left(\cos\gamma B t',\;-\sin\gamma B t'\right)
$$

in a right-handed basis whose third axis is $\vec u_B$. The signed rate $\gamma B$ carries the sense of the rotation and the Larmor frequency $\omega_L = |\gamma|B$ its magnitude; the motion is the uniform precession of a cone at that frequency.

## The Rotor Solution

### The Rotation Rotor

The rotor algebra is stated here explicitly, because the precession solution and the reciprocal effects of the following article are both written in it. A rotation through angle $\theta$ about the unit real axis $\vec u$ is produced by the **unit real quaternion**

$$
\tilde u(\theta,\vec u) = \cos\frac{\theta}{2}\,e_t + \sin\frac{\theta}{2}\;\vec u_k \vec e_k
= \exp\!\left(\frac{\theta}{2}\,\vec u_k \vec e_k\right),
$$

acting on a pure real vector by **rotor conjugation**,

$$
\vec v \;\longmapsto\; \tilde u\,\vec v\,\tilde u^{*} ,
\qquad
\tilde u\,\tilde u^{*} = e_t .
$$

The conjugation rotates $\vec v$ through the angle $\theta$ about $\vec u$ in the right-handed sense. Two elementary properties are used repeatedly. First, the rotor is normalized, $\langle\tilde u\rangle_{\natural} = \tilde u\tilde u^{\natural} = e_t$, so the conjugation preserves the biquaternion norm of every vector it acts on. Second, the half-angle makes the rotor a **double cover** of the rotation: $\tilde u(\theta + 2\pi,\vec u) = -\tilde u(\theta,\vec u)$, and the two rotors $\pm\tilde u$ produce the same rotation. The rotation group is therefore $\mathbb{H}_{\mathbb{B}}^1/\{\pm e_t\}$, with $\mathbb{H}_{\mathbb{B}}^1$ the group of unit real quaternions, which is $SU(2)$.


### The Precession as a Rotor

The Larmor precession is the rotor conjugation

$$
\vec\mu(t') = \tilde u_L(t')\,\vec\mu(0)\,\tilde u_L(t')^{*},
\qquad
\tilde u_L(t') = \exp\!\left(-\,\frac{\gamma B t'}{2}\,\vec u_{B,k} \vec e_k\right),
$$

with $\vec u_B = \vec B/B$ the field direction. Differentiating the rotor gives

$$
d\tilde u_L/dt' = -\,\frac{\gamma B}{2}\,\vec u_{B,k} \vec e_k\,\tilde u_L
= -\,\frac{1}{2}\,\vec\omega_G\,\tilde u_L,
\qquad \vec\omega_G = \gamma\,\vec B,
$$

and hence

$$
d\vec\mu/dt' = d\tilde u_L/dt'\,\vec\mu_0\,\tilde u_L^{*}
+ \tilde u_L\,\vec\mu_0\,\left(d\tilde u_L/dt'\right)^{*}
= \tfrac{1}{2}\left[\,\vec\mu(t'),\;\vec\omega_G\,\right],
$$

the commutator form of the previous section, recovered from the rotor. The rotor therefore **solves** the Larmor equation, and the solution is a one-parameter group of unit real quaternions generated by the field.

The angle swept by the rotor in time $t'$ is $\gamma B t'/2$, while the moment itself turns through $\gamma B t'$; the factor of two between the two angles is the same half-angle that makes the rotor a double cover, and it is the algebraic fact on which the account of the gyromagnetic factor rests. On the period of the motion, the moment returns to its initial direction after $t' = 2\pi/(\gamma B)$, while the rotor has turned through only $\pi$ and has changed sign; only after a second period does the rotor return to $+\tilde u_L$.

### The Sign and the Field Direction

The rotor $\tilde u_L(t')$ rotates by the angle $-\gamma B t'$ about $\vec u_B$. For a proton, whose $\gamma$ is positive, the moment precesses in the negative sense about the field — clockwise when the field points toward the viewer — which is the standard Larmor sense. The inertia of the moment, in other words, carries it past the field direction rather than dragging it back, and the motion is a precession and not an alignment. The numerical values of the Larmor frequency are the standard ones: $\gamma_p/2\pi = 42.577$ MHz T$^{-1}$ for the proton, so that a field of $1$ T gives $\omega_L = 2\pi\times 42.577$ MHz, and $\gamma_e/2\pi = 28.025$ GHz T$^{-1}$ for the electron's spin.

## The Larmor Theorem

### The Rotating Frame

The precession law has a second interpretation, which is the content of the **Larmor theorem**. Consider a frame rotating with angular velocity $\vec\Omega$ with respect to the laboratory, and let $\vec\mu_{\rm rot}$ be the moment as seen in that frame. The moment in the laboratory is obtained by the rotor of the frame, $\vec\mu = \tilde u_\Omega\,\vec\mu_{\rm rot}\,\tilde u_\Omega^{*}$ with $\tilde u_\Omega = \exp(\tfrac{1}{2}\Omega t'\,\vec u_{\Omega,k} \vec e_k)$, and the derivative separates into the frame's own rotation and the additional motion seen in the frame,

$$
d\vec\mu/dt' = \tfrac{1}{2}\left[\vec\Omega,\vec\mu\right]
+ \tilde u_\Omega\left(d\vec\mu_{\rm rot}/dt'\right)\tilde u_\Omega^{*} ,
\qquad \vec\Omega = \Omega_k \vec e_k .
$$

Substituting the Larmor equation $d\vec\mu/dt' = \tfrac{1}{2}[\vec\mu,\vec\omega_G]$ and collecting the generator of the frame's own motion gives

$$
\tilde u_\Omega\,d\vec\mu_{\rm rot}/dt'\,\tilde u_\Omega^{*}
= \tfrac{1}{2}\left[\vec\mu,\,\vec\omega_G + \vec\Omega\right].
$$

If the frame rotates at exactly

$$
\vec\Omega = -\gamma\,\vec B = \vec\omega_L ,
$$

the right-hand side vanishes, and the moment is **at rest in the rotating frame**. This is the Larmor theorem: the effect of a uniform magnetic field on a magnetic moment is equivalent to a rotation of the frame at the Larmor frequency, and in that frame the moment is stationary.

### What the Theorem Does and Does Not Say

The theorem is exact for a single moment in a uniform field, and it extends to a collection of moments only when they share the same gyromagnetic ratio: the frame that is at rest for one value of $\gamma$ is not at rest for another, so a medium with several species has one Larmor frame per species. The theorem is also the kinematic basis of magnetic resonance: a small transverse field rotating at $\vec\omega_L$, the same rate and the same sense as the Larmor frame, appears static in that frame and can therefore tip the moment away from the field, while a field at any other frequency averages away. The rotating-frame construction is the classical basis of the resonance experiments; the quantum treatment of the same frame is given in the companion article *Exercise: Spin Precession in a Magnetic Field*, and the half-angle rotor used here is the same one.

The theorem is a statement about the *frame*, not about the moment: the moment is a material vector and does not change its magnitude in any frame. In the biquaternion description the frame rotation and the precession are two rotor conjugations, and their composition is again a rotor conjugation; the content of the theorem is that the two generators add — the generator of the motion in the rotating frame is $\vec\omega_G + \vec\Omega$ — while the angular velocity it corresponds to is the difference $\vec\omega_L - \vec\Omega$, the frame's rate subtracted from the Larmor rate. At $\vec\Omega = \vec\omega_L$ the generator vanishes and the moment is at rest.

## The Gyromagnetic Ratio

### Definition

The gyromagnetic ratio is the constant of proportionality between the moment and the angular momentum,

$$
\vec\mu = \gamma\,\vec S,
$$

and it is conventional to express it through the dimensionless **gyromagnetic factor** $g$ by

$$
\vec\mu = g\,\frac{ϙ}{2m}\,\vec S,
\qquad\text{so that}\qquad
\gamma = g\,\frac{ϙ}{2m},
$$

where $ϙ$ and $m$ are the charge and mass of the carrier. For a purely orbital or convective current, the classical theorem of the next article gives $\gamma = ϙ/2m$, that is $g = 1$; for an intrinsic moment, the same articles give $\gamma = ϙ/m$, that is $g = 2$. The Larmor frequency is then $\omega_L = |g|\,|ϙ|B/2m$ for the spin, and one Bohr magneton,

$$
\mu_B = \frac{e\hbar}{2m_e} = 9.274010\times10^{-24}\ \text{J T}^{-1},
$$

per unit spin for the electron.

### The Orbital Value, and a Preview

For a rigid rotor with proportional charge and mass densities, the moment and the angular momentum are related by the ratio of the two inertia tensors, and the moment is $\vec\mu = (ϙ/2m)\vec L$. The Larmor frequency of an orbital moment is therefore fixed by $ϙ/2m$ and does not require any intrinsic structure. The intrinsic case is different: a moment attributed to the body is not a convective current, and the value of $\gamma$ is not fixed by any charge density. The companion article *The Einstein–de Haas and Barnett Effects in Biquaternionic Form* treats the reciprocal pair of effects in which a change of an intrinsic moment rotates the body and a rotation of the body magnetizes it; the companion article *The Classical Origin of g = 2 in Biquaternionic Form* accounts for the fact that the intrinsic gyromagnetic ratio is twice the orbital one. Both presuppose the Larmor equation derived here, and both work with the same rotor.

## Relation to the Quantum Treatment

The precession of a spin-$\tfrac{1}{2}$ in a magnetic field is treated in the sibling quantum category, in the companion articles *Spin-1/2 Quantum Physics in Biquaternionic Form* and *Exercise: Spin Precession in a Magnetic Field*. There the state is an idempotent $P = \tfrac{1}{2}(e_t + i\vec u)$ of $\mathbb{M}_+$, the Hamiltonian is the Hermitian element $\tilde{H} = -\gamma B_0\tilde{S}_z$ with $\tilde{S}_z = \tfrac{\hbar}{2}i\vec e_z$, the evolution is the rotor conjugation $\tilde{Ϛ}(t') = \tilde{U}(t')\tilde{Ϛ}(0)\tilde{U}(t')^{*}$ with $\tilde{U}(t') = \exp(-i\tilde{H}t'/\hbar)$, and the expectation value is the normalised plain form, read as the trace pairing $\langle\tilde{S}_x\rangle = \mathrm{Tr}(\tilde{Ϛ}\tilde{S}_x)$. The evolved Bloch vector is $\vec r(t') = \cos(\gamma B t')\vec e_x - \sin(\gamma B t')\vec e_y$, which is the precession derived here, with the same frequency and the same sense.

The two treatments agree because they are the same rotor. The classical moment of this article lives in $\mathbb{H}_{\mathbb{B}}$ as a real pure quaternion and is rotated by $\tilde u_L(t') = \exp(-\tfrac{1}{2}\gamma B t'\,\vec u_{B,k} \vec e_k)$; the quantum state lives in $\mathbb{M}_+$ and is rotated by $\tilde{U}(t')$, whose vector part is the same unit real quaternion. The factor $i$ that separates the two representatives is the sector exchange, not a physical difference. What the quantum treatment adds is the Born rule and the state; what this article adds is that the precession needs neither, because the moment of a classical current distribution obeys the same Larmor equation as the mean spin. The two are different derivations of one motion, and the classical one is the subject of this subcategory.

## Summary

The magnetic moment of a current distribution is an axial vector, and in the biquaternion framework it is a pure real quaternion $\vec\mu = \mu_k \vec e_k$ in the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the same slot that carries the magnetic induction $\vec B = B_k \vec e_k$. The two bilinears of the magnetic coupling are the scalar and vector parts of the single quaternion product,

$$
\vec\mu\,\vec B = -\,\vec\mu\cdot\vec B\,e_t + \vec\mu\times\vec B,
$$

so that the energy is $E = \mathrm{Sc}(\vec\mu\vec B) = -\vec\mu\cdot\vec B$ and the torque is $\vec\tau = \mathrm{Vect}(\vec\mu\vec B) = \vec\mu\times\vec B$.

The torque equation for a moment tied to an angular momentum by $\vec\mu = \gamma\vec S$ is the **Larmor equation**

$$
d\vec\mu/dt' = \gamma\,\vec\mu\times\vec B,
\qquad \vec\omega_L = -\,\gamma\,\vec B,
$$

which in the algebra is the commutator

$$
d\vec\mu/dt' = \tfrac{1}{2}\left[\vec\mu,\vec\omega_G\right],
\qquad \vec\omega_G = \gamma\,\vec B.
$$

The equation is solved by the **rotor conjugation**

$$
\vec\mu(t') = \tilde u_L(t')\,\vec\mu(0)\,\tilde u_L(t')^{*},
\qquad
\tilde u_L(t') = \exp\!\left(-\,\frac{\gamma B t'}{2}\,\vec u_{B,k} \vec e_k\right),
$$

with $\tilde u_L$ a unit real quaternion; the moment turns through $\gamma B t'$ while the rotor turns through half that angle, the double-cover half-angle of the algebra. The biquaternion norm $\langle\vec\mu\rangle_{\natural}$ and the energy $E$ are conserved, so the moment precesses on a cone about the field at the Larmor frequency $\omega_L = |\gamma|B$. The **Larmor theorem** states that in a frame rotating at $\vec\Omega = -\gamma\vec B$ the moment is at rest; the generator of the motion in that frame is the sum $\vec\omega_G + \vec\Omega$ of the Larmor and frame generators, whose corresponding angular velocity is the difference $\vec\omega_L - \vec\Omega$, and the theorem is exact for a single moment in a uniform field.

The gyromagnetic ratio is $\gamma = g\,ϙ/2m$, with $g = 1$ for a convective moment and $g = 2$ for an intrinsic one. The Larmor equation derived here is the common premise of the companion articles *The Einstein–de Haas and Barnett Effects in Biquaternionic Form* and *The Classical Origin of g = 2 in Biquaternionic Form*, and its rotor is the same half-angle rotor that the quantum treatment of spin precession employs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$, $\vec e_\mu \vec e_\nu = \epsilon_{\mu\nu\lambda}\vec e_\lambda$ $(\mu\neq\nu)$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, home of the rotation rotors |
| $\vec\mu = \mu_k \vec e_k$ | Classical magnetic moment (pure real quaternion) |
| $i\,\vec\mu = \mu_k\,i \vec e_k$ | Intrinsic moment's informational-sector representative |
| $\vec B = B_k \vec e_k = \mu\vec H$ | Magnetic induction (pure real quaternion) |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion |
| $\vec j, \rho_c, \rho_m$ | Current density; charge and mass densities |
| $\mathcal{M}_{ij} = \int\rho_c(r^2\delta_{ij}-r_ir_j)$ | Charge inertia tensor |
| $I_{ij} = \int\rho_m(r^2\delta_{ij}-r_ir_j)$ | Mass inertia tensor |
| $\vec L = I\vec\omega$ | Mechanical angular momentum |
| $\gamma$, $g$ | Gyromagnetic ratio; gyromagnetic factor ($\gamma = g\,ϙ/2m$) |
| $\vec\omega_L = -\gamma\vec B$ | Larmor angular velocity |
| $\omega_L = \lvert\gamma\rvert B$ | Larmor frequency |
| $\vec\omega_G = \gamma\vec B$ | Larmor generator (Larmor equation) |
| $\tilde u(\theta,\vec u) = \cos\tfrac{\theta}{2}e_t + \sin\tfrac{\theta}{2}\vec u_k\vec e_k$ | Rotation rotor (unit real quaternion) |
| $\mathcal{R}(\theta,\vec u)$ | Three-vector rotation through $\theta$ about $\vec u$ |
| $\vec\mu(t') = \tilde u_L\vec\mu(0)\tilde u_L^{*}$ | Precession as rotor conjugation |
| $E = -\vec\mu\cdot\vec B = \mathrm{Sc}(\vec\mu\vec B)$ | Magnetic energy |
| $\vec\tau = \vec\mu\times\vec B = \mathrm{Vect}(\vec\mu\vec B)$ | Magnetic torque |
| $\mu_B = e\hbar/2m_e$ | Bohr magneton |

## Further Reading

- J. Larmor, "On the theory of the magnetic influence on spectra; and on the radiation from moving ions," *Philosophical Magazine* **44** (1897) 503–512, for the original statement of the precession and the theorem that bears its name.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the magnetic moment, the torque, and the Larmor theorem in the classical theory.
- L. D. Landau and E. M. Lifshitz, *Electrodynamics of Continuous Media* (Pergamon, 1984), for the magnetic moment of a current distribution and the definition of the magnetization.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the magnetic moment of a current loop and of a general steady current distribution.
- R. P. Feynman, R. B. Leighton, and M. Sands, *The Feynman Lectures on Physics*, Vol. II (Addison-Wesley, 1964), for the elementary treatment of the magnetic moment and the torque.
- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the rigid-body inertia tensor and the gyroscopic precession of a symmetric top.
- C. Cohen-Tannoudji, B. Diu, and F. Laloë, *Quantum Mechanics* (Wiley, 1977), for the Larmor precession of a spin in the quantum formalism.
- J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin magnetic moment, the Larmor frequency, and the rotating-frame treatment of magnetic resonance.
- E. M. Purcell, *Electricity and Magnetism* (Cambridge, 2013), for the magnetic moment and the precession in a field, at the level of the Berkeley Physics Course.
- A. Abragam, *The Principles of Nuclear Magnetism* (Oxford, 1961), for the Larmor frequency of nuclear moments and the rotating-frame description used in magnetic resonance.
