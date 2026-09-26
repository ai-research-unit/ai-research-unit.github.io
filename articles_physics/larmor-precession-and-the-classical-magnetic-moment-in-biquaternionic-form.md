# __Larmor Precession and the Classical Magnetic Moment in Biquaternionic Form__

## Introduction

A magnetic moment placed in a magnetic field experiences a torque, and a torque on a moment that is rigidly tied to an angular momentum makes the momentum precess. This is the **Larmor precession**, and it is the simplest motion of an intrinsic magnetic moment. Its frequency, the **Larmor frequency** $\omega_L = |\gamma|B$, is fixed by the gyromagnetic ratio $\gamma$ of the system, and it is the quantity on which magnetic resonance, the Einstein–de Haas and Barnett effects, and the classical account of the gyromagnetic factor all rest.

This article treats the magnetic moment and its precession as **classical** and **non-quantum** objects. The moment is the moment of a current distribution, or an intrinsic moment attributed to the body; it is a vector in the material sector, and its equation of motion is the classical torque equation. Nothing in the article requires a spinor, a Hilbert space, or a quantum state. The quantum treatment of the same precession — the evolution of an idempotent under a Hermitian Hamiltonian, and the trace formula that gives $\langle S_x\rangle(t)$ — is the subject of the companion articles *Spin-1/2 Quantum Mechanics in Biquaternionic Form* and *Exercise: Spin Precession in a Magnetic Field*; it is cited here and not reproduced.

The biquaternion algebra contributes three things to the classical subject, and they are the reason the article is in this framework rather than in three-vector notation. First, the moment and the field are both pure real quaternions, and a **single quaternion product** yields the two bilinears of the magnetic coupling at once: its scalar part is the energy $-\boldsymbol{\mu}\cdot\mathbf{B}$, and its vector part is the torque $\boldsymbol{\mu}\times\mathbf{B}$. Second, the precession equation acquires the form of a **commutator**, $\dot{\tilde{\boldsymbol{\mu}}} = \tfrac{1}{2}[\tilde{\boldsymbol{\mu}},\tilde{\boldsymbol{\omega}}_L]$, which is the classical Poisson-bracket evolution realized inside the algebra. Third, the solution is a **rotor conjugation**, $\tilde{\boldsymbol{\mu}}(t) = \tilde{R}(t)\,\tilde{\boldsymbol{\mu}}(0)\,\tilde{R}(t)^\dagger$, with a unit real quaternion whose half-angle is the same half-angle that appears throughout the series. The third point is what ties this article to the two that follow it: the rotor is the same object in the classical and in the spin-$\tfrac{1}{2}$ description, which is why the classical moment and the intrinsic moment obey the same precession law.

The conventions are those of the foundational articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and the scalar imaginary is $i$ (central, $i^2 = -1$). The material sector is the anti-Hermitian subspace $\mathbb{M}_-$ and the informational sector is the Hermitian subspace $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$. The real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the fixed space of complex conjugation, the home of the rotation rotors. The magnetic induction is $\mathbf{B} = \mu\mathbf{H}$, and the field strength is written in the canonical form $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ of the article *The Field-Strength Biquaternion and Its Invariants*.

## The Magnetic Moment of a Current Distribution

### Definition

For a steady current distribution of density $\mathbf{j}(\mathbf{x})$, the **magnetic moment** is

$$
\boldsymbol{\mu} = \frac{1}{2}\int \mathbf{r}\times\mathbf{j}\,d^3x .
$$

For a planar loop carrying current $I$ and bounding a vector area $\mathbf{A}$, the integral gives the elementary result

$$
\boldsymbol{\mu} = I\,\mathbf{A},
$$

and for a charge $q$ moving on a circle of radius $\rho$ with angular frequency $\omega$, it gives

$$
\mu = \frac{1}{2}\,q\rho^2\omega .
$$

Both are the standard formulae of magnetostatics, and both will be used below. The moment is an **axial vector**: it is built from a cross product, so it changes sign under a reflection of space while a polar vector does not.

### The Moment as a Pure Real Quaternion

The axial vectors of the material sector are represented in the biquaternion algebra by the **pure real quaternions**,

$$
\tilde{\boldsymbol{\mu}} = \mu_1 e_1 + \mu_2 e_2 + \mu_3 e_3 \in \mathbb{H}_{\mathbb{B}},
\qquad
\mathbf{B} = B_1 e_1 + B_2 e_2 + B_3 e_3 \in \mathbb{H}_{\mathbb{B}} .
$$

This is the same slot that carries the three real spatial directions $\mathbf{x} = x e_1 + y e_2 + z e_3$ of the material coordinate $\tilde{X} = ict\,e_0 + \mathbf{x}$, and it is the slot in which the magnetic field appears in the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$. The moment and the induction are therefore elements of the *same* real subspace, and their bilinears can be formed with the ordinary quaternion product.

For a pure real quaternion $\mathbf{a}$ and a pure real quaternion $\mathbf{b}$, the quaternion product splits into a scalar and a vector part,

$$
\mathbf{a}\,\mathbf{b} = -\,\mathbf{a}\cdot\mathbf{b} + \mathbf{a}\times\mathbf{b},
$$

with the scalar part the negative of the dot product and the vector part the cross product. Applied to the moment and the induction, this one identity contains the whole of the classical magnetic coupling:

$$
\tilde{\boldsymbol{\mu}}\,\mathbf{B} = -\,\boldsymbol{\mu}\cdot\mathbf{B} + \boldsymbol{\mu}\times\mathbf{B}.
$$

<!-- CONVENTION — moment and field in H_B: the classical magnetic moment and the magnetic induction are both written as pure real quaternions in the real-quaternion subspace H_B, the slot of the material axial vectors. The intrinsic (spin) moment of the informational sector uses the same vector slot but with the central factor i, as mu_k i e_k in M_+. The two representatives differ by the central i that exchanges the sectors, i M_+ = M_-, and a reviewer must not "align" them by dropping the i: the real representative carries the material description, the imaginary one the observable, and the factor between them is the sector exchange. -->

### The Moment of a Rigid Rotor

The classical moment of a body in rigid rotation is the case that fixes the gyromagnetic ratio. If the body rotates with angular velocity $\boldsymbol{\omega}$ and carries charge density $\rho_c$, the local current is $\mathbf{j} = \rho_c\,\boldsymbol{\omega}\times\mathbf{r}$, and the moment is

$$
\boldsymbol{\mu} = \frac{1}{2}\int \rho_c(\mathbf{r})\,\mathbf{r}\times(\boldsymbol{\omega}\times\mathbf{r})\,d^3x
= \frac{1}{2}\,\hat{\Pi}\,\boldsymbol{\omega},
$$

where

$$
\hat{\Pi}_{ij} = \int \rho_c(\mathbf{r})\left(r^2\delta_{ij} - r_i r_j\right)d^3x
$$

is the **charge inertia tensor**, the charge-weighted analogue of the mass inertia tensor

$$
\hat{I}_{ij} = \int \rho_m(\mathbf{r})\left(r^2\delta_{ij} - r_i r_j\right)d^3x .
$$

The mechanical angular momentum is $\mathbf{L} = \hat{I}\,\boldsymbol{\omega}$. The two tensors are the entire classical input of the gyromagnetic problem: whether the ratio of the moment to the angular momentum is the orbital value $q/2m$ or something else is decided by whether $\hat{\Pi}$ is proportional to $\hat{I}$. That question is taken up in the article *The Classical Origin of g = 2 in Biquaternionic Form*; here it is enough to record that the moment of a rigid rotor is a pure real quaternion like any other axial vector.

### The Moment of a Spin

A body may also carry an **intrinsic** magnetic moment, one that is not the moment of any rigid motion of its charge. Such a moment is attributed to the body rather than computed from a current distribution, and it is the intrinsic case that the later articles of this subcategory treat. Its biquaternion representative is the vector slot with the central factor,

$$
i\,\mathbf{m} = \mu_k\,i e_k = \mu_1\,i e_1 + \mu_2\,i e_2 + \mu_3\,i e_3 \in \mathbb{M}_+ ,
$$

the imaginary pure quaternion being the informational-sector twin of the real pure quaternion $\mathbf{m} = \mu_ke_k$. The two descriptions are exchanged by multiplication by $i$, exactly as the two sectors are; both describe the same physical moment, and the choice between them is a choice of which sector's representative is being written. For a moment tied to an intrinsic angular momentum $\mathbf{S}$, the coefficient is the gyromagnetic ratio,

$$
\boldsymbol{\mu} = \gamma\,\mathbf{S},
$$

and the precession law below is the same for the intrinsic and the convective moment.

## Energy and Torque

### The Two Bilinears of One Product

The coupling of a magnetic moment to a magnetic field is

$$
U = -\,\boldsymbol{\mu}\cdot\mathbf{B},
$$

and the torque it exerts is

$$
\boldsymbol{\tau} = \boldsymbol{\mu}\times\mathbf{B}.
$$

In the biquaternion algebra both are read off the **same product** $\tilde{\boldsymbol{\mu}}\,\mathbf{B}$:

$$
U = \mathrm{Sc}\!\left(\tilde{\boldsymbol{\mu}}\,\mathbf{B}\right),
\qquad
\boldsymbol{\tau} = \mathrm{Vect}\!\left(\tilde{\boldsymbol{\mu}}\,\mathbf{B}\right),
$$

where $\mathrm{Sc}$ and $\mathrm{Vect}$ are the scalar and vector parts. The energy is the scalar part and the torque the vector part, and no second product is needed. This is the biquaternion form of the elementary fact that the magnetic interaction is a single bilinear of two axial vectors, whose symmetric part is the energy and whose antisymmetric part is the torque.

The energy has its minimum when the moment is aligned with the field, $U = -\mu B$, and its maximum when it is anti-aligned, $U = +\mu B$; the torque vanishes in both cases because $\boldsymbol{\mu}\times\mathbf{B} = 0$ there. These two alignments are the stable and unstable equilibria of the moment in the field, and the precession below is the motion about a tilted configuration, in which the energy is constant and the torque does no work.

### The Work and the Conservation of Energy

Because the torque is always perpendicular to the moment, $\boldsymbol{\tau}\cdot\boldsymbol{\mu} = 0$, and because the torque is also perpendicular to the field, the energy $U = -\boldsymbol{\mu}\cdot\mathbf{B}$ is conserved in a static uniform field:

$$
\frac{dU}{dt} = -\dot{\boldsymbol{\mu}}\cdot\mathbf{B} = -\left(\gamma\,\boldsymbol{\mu}\times\mathbf{B}\right)\cdot\mathbf{B} = 0 .
$$

The magnitude of the moment is likewise conserved, since the equation of motion is a rotation; the biquaternion statement is that the norm form $N(\tilde{\boldsymbol{\mu}}) = \tilde{\boldsymbol{\mu}}\bar{\tilde{\boldsymbol{\mu}}} = |\boldsymbol{\mu}|^2$ is constant. A moment of fixed length and fixed energy precesses on a cone about the field direction, and the next sections find the cone's angular frequency.

## The Larmor Equation

### Derivation from the Torque

The angular momentum of the system is $\mathbf{S}$, and the moment is tied to it by $\boldsymbol{\mu} = \gamma\mathbf{S}$. The torque equation $\dot{\mathbf{S}} = \boldsymbol{\tau}$ becomes

$$
\dot{\mathbf{S}} = \boldsymbol{\mu}\times\mathbf{B} = \gamma\,\mathbf{S}\times\mathbf{B},
$$

and multiplying by $\gamma$ gives the equation for the moment itself:

$$
\boxed{\;\dot{\boldsymbol{\mu}} = \gamma\,\boldsymbol{\mu}\times\mathbf{B} = \boldsymbol{\mu}\times\left(\gamma\mathbf{B}\right).\;}
$$

This is the **Larmor equation**. Its content is that the moment precesses about the field direction with angular velocity

$$
\boldsymbol{\omega}_L = -\,\gamma\,\mathbf{B},
$$

the minus sign expressing the fact that the rotation sense is opposite to the field when $\gamma$ is positive. Equivalently, the moment rotates about $\mathbf{B}$ with angular frequency $\omega_L = |\gamma|\,B$, in the sense fixed by the sign of $\gamma$.

<!-- CONVENTION — precession sense: the Larmor equation is written dot(mu) = gamma mu x B, so the angular-velocity vector is bold-omega_L = -gamma B and a moment with positive gamma precesses *negatively* about B (clockwise when viewed along B). The sign is the same one that appears in the quantum exercise, where the evolution is exp(-iHt/hbar) with H = -gamma B_0 S_z and the Bloch vector rotates as (cos(gamma B t), -sin(gamma B t)), the signed rate being gamma B. A reviewer must not "fix" the minus sign in bold-omega_L = -gamma B: it is the physically correct sense and it agrees with the quantum article. -->

### The Biquaternion Commutator Form

The cross product in the Larmor equation is the vector part of a quaternion product, and the equation can therefore be written as a commutator. For pure real quaternions the commutator is twice the cross product,

$$
[\,\tilde{\boldsymbol{\mu}},\tilde{\boldsymbol{\omega}}\,] = 2\,\boldsymbol{\mu}\times\boldsymbol{\omega},
$$

so that, defining the **Larmor biquaternion**

$$
\tilde{\boldsymbol{\omega}}_L = \gamma\,B_1e_1 + \gamma\,B_2e_2 + \gamma\,B_3e_3 = \gamma\,\mathbf{B} \in \mathbb{H}_{\mathbb{B}},
$$

the Larmor equation reads

$$
\boxed{\;\dot{\tilde{\boldsymbol{\mu}}} = \tfrac{1}{2}\left[\,\tilde{\boldsymbol{\mu}},\;\tilde{\boldsymbol{\omega}}_L\,\right].\;}
$$

The equation of motion is thus an **inner derivation** of the algebra, $\dot{\tilde{\boldsymbol{\mu}}} = \mathrm{ad}_{\tilde{\boldsymbol{\omega}}_L/2}(\tilde{\boldsymbol{\mu}})$. The generator $\tilde{\boldsymbol{\omega}}_L$ is the negative of the angular velocity $\boldsymbol{\omega}_L = -\gamma\mathbf{B}$ of the precession: the first is the generator of the derivation, the second the rotation vector of the cone, and the two are listed separately in the notation table. Its antisymmetry is manifest — a commutator changes sign when its arguments are exchanged — and its trace vanishes, $\mathrm{Tr}[\tilde{\boldsymbol{\mu}},\tilde{\boldsymbol{\omega}}_L] = 0$, which is the algebraic statement that the rotation preserves the norm form.

This is the classical bracket form of the dynamics. The Hamiltonian of the moment in the field is $H = -\gamma\,\mathbf{S}\cdot\mathbf{B}$, and the classical evolution of any observable is $\dot{f} = \{f,H\}$; the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator* shows that the components of angular momentum satisfy $\{S_i,S_j\} = \epsilon_{ijk}S_k$, from which

$$
\dot{S}_i = \{S_i,H\} = -\gamma B_j\,\{S_i,S_j\} = -\gamma B_j\,\epsilon_{ijk}S_k = \gamma\,(\mathbf{S}\times\mathbf{B})_i,
$$

which is the Larmor equation again. The biquaternion commutator $\tfrac{1}{2}[\tilde{\boldsymbol{\mu}},\tilde{\boldsymbol{\omega}}_L]$ is that Poisson bracket written in the algebra, and it is the same bracket that the quantum article realizes as $[\tilde{S}_i,\tilde{S}_j] = i\hbar\,\epsilon_{ijk}\tilde{S}_k$.

### The Time-Dependence of the Moment

Writing the solution of the Larmor equation directly, the moment at time $t$ is the initial moment rotated about the field direction by the angle $-\gamma B t$:

$$
\boldsymbol{\mu}(t) = \mathcal{R}\!\left(-\gamma B t,\;\hat{\mathbf{B}}\right)\boldsymbol{\mu}(0),
$$

where $\mathcal{R}(\theta,\hat{\mathbf{n}})$ is the right-handed rotation through $\theta$ about $\hat{\mathbf{n}}$. For a moment initially making an angle $\alpha$ with the field, the component along the field is constant, $\mu_\parallel = \mu\cos\alpha$, and the transverse component rotates uniformly,

$$
\mu_\perp(t) = \mu\sin\alpha\left(\cos\gamma B t,\;-\sin\gamma B t\right)
$$

in a right-handed basis whose third axis is $\hat{\mathbf{B}}$. The signed rate $\gamma B$ carries the sense of the rotation and the Larmor frequency $\omega_L = |\gamma|B$ its magnitude; the motion is the uniform precession of a cone at that frequency.

## The Rotor Solution

### The Rotation Rotor

The rotor algebra is stated here explicitly, because the precession solution and the reciprocal effects of the following article are both written in it. A rotation through angle $\theta$ about the unit real axis $\hat{\mathbf{n}}$ is produced by the **unit real quaternion**

$$
\tilde{R}(\theta,\hat{\mathbf{n}}) = \cos\frac{\theta}{2}\,e_0 + \sin\frac{\theta}{2}\;\hat{n}_k e_k
= \exp\!\left(\frac{\theta}{2}\,\hat{n}_k e_k\right),
$$

acting on a pure real vector by **rotor conjugation**,

$$
\mathbf{v} \;\longmapsto\; \tilde{R}\,\mathbf{v}\,\tilde{R}^\dagger ,
\qquad
\tilde{R}\,\tilde{R}^\dagger = e_0 .
$$

The conjugation rotates $\mathbf{v}$ through the angle $\theta$ about $\hat{\mathbf{n}}$ in the right-handed sense. Two elementary properties are used repeatedly. First, the rotor is normalized, $N(\tilde{R}) = \tilde{R}\bar{\tilde{R}} = e_0$, so the conjugation preserves the norm form of every vector it acts on. Second, the half-angle makes the rotor a **double cover** of the rotation: $\tilde{R}(\theta + 2\pi,\hat{\mathbf{n}}) = -\tilde{R}(\theta,\hat{\mathbf{n}})$, and the two rotors $\pm\tilde{R}$ produce the same rotation. The rotation group is therefore $\mathbb{H}_{\mathbb{B}}^1/\{\pm e_0\}$, with $\mathbb{H}_{\mathbb{B}}^1$ the group of unit real quaternions, which is $SU(2)$.

<!-- CONVENTION — rotor sign and action: the rotation rotor is R(theta,n) = cos(theta/2) e_0 + sin(theta/2) n_k e_k and acts by R v R_dag, rotating a pure real vector by +theta about n in the right-handed sense. Both the sign of the sine and the right-handedness are conventions of the series, fixed by the spatial rotation rotors of *Angular Momentum and Spin in Biquaternionic Form*. A reviewer must not flip the sign of the sine to "make it a rotation by theta": with the sine positive the conjugation is a right-handed rotation by +theta, and all the rotation formulae of the series depend on it. -->

### The Precession as a Rotor

The Larmor precession is the rotor conjugation

$$
\tilde{\boldsymbol{\mu}}(t) = \tilde{R}_L(t)\,\tilde{\boldsymbol{\mu}}(0)\,\tilde{R}_L(t)^\dagger,
\qquad
\tilde{R}_L(t) = \exp\!\left(-\,\frac{\gamma B t}{2}\,\hat{B}_k e_k\right),
$$

with $\hat{\mathbf{B}} = \mathbf{B}/B$ the field direction. Differentiating the rotor gives

$$
\dot{\tilde{R}}_L = -\,\frac{\gamma B}{2}\,\hat{B}_k e_k\,\tilde{R}_L
= -\,\frac{1}{2}\,\tilde{\boldsymbol{\omega}}_L\,\tilde{R}_L,
\qquad \tilde{\boldsymbol{\omega}}_L = \gamma\,\mathbf{B},
$$

and hence

$$
\dot{\tilde{\boldsymbol{\mu}}} = \dot{\tilde{R}}_L\,\tilde{\boldsymbol{\mu}}_0\,\tilde{R}_L^\dagger
+ \tilde{R}_L\,\tilde{\boldsymbol{\mu}}_0\,\dot{\tilde{R}}_L^\dagger
= \tfrac{1}{2}\left[\,\tilde{\boldsymbol{\mu}}(t),\;\tilde{\boldsymbol{\omega}}_L\,\right],
$$

the commutator form of the previous section, recovered from the rotor. The rotor therefore **solves** the Larmor equation, and the solution is a one-parameter group of unit real quaternions generated by the field.

The angle swept by the rotor in time $t$ is $\gamma B t/2$, while the moment itself turns through $\gamma B t$; the factor of two between the two angles is the same half-angle that makes the rotor a double cover, and it is the algebraic fact on which the account of the gyromagnetic factor rests. On the period of the motion, the moment returns to its initial direction after $t = 2\pi/(\gamma B)$, while the rotor has turned through only $\pi$ and has changed sign; only after a second period does the rotor return to $+\tilde{R}_L$.

### The Sign and the Field Direction

The rotor $\tilde{R}_L(t)$ rotates by the angle $-\gamma B t$ about $\hat{\mathbf{B}}$. For a proton, whose $\gamma$ is positive, the moment precesses in the negative sense about the field — clockwise when the field points toward the viewer — which is the standard Larmor sense. The inertia of the moment, in other words, carries it past the field direction rather than dragging it back, and the motion is a precession and not an alignment. The numerical values of the Larmor frequency are the standard ones: $\gamma_p/2\pi = 42.577$ MHz T$^{-1}$ for the proton, so that a field of $1$ T gives $\omega_L = 2\pi\times 42.577$ MHz, and $\gamma_e/2\pi = 28.025$ GHz T$^{-1}$ for the electron's spin.

## The Larmor Theorem

### The Rotating Frame

The precession law has a second reading, which is the content of the **Larmor theorem**. Consider a frame rotating with angular velocity $\boldsymbol{\Omega}$ with respect to the laboratory, and let $\tilde{\boldsymbol{\mu}}_{\rm rot}$ be the moment as seen in that frame. The moment in the laboratory is obtained by the rotor of the frame, $\tilde{\boldsymbol{\mu}} = \tilde{R}_\Omega\,\tilde{\boldsymbol{\mu}}_{\rm rot}\,\tilde{R}_\Omega^\dagger$ with $\tilde{R}_\Omega = \exp(\tfrac{1}{2}\Omega t\,\hat{\Omega}_k e_k)$, and the derivative separates into the frame's own rotation and the additional motion seen in the frame,

$$
\dot{\tilde{\boldsymbol{\mu}}} = \tfrac{1}{2}\left[\tilde{\boldsymbol{\Omega}},\tilde{\boldsymbol{\mu}}\right]
+ \tilde{R}_\Omega\left(\dot{\tilde{\boldsymbol{\mu}}}_{\rm rot}\right)\tilde{R}_\Omega^\dagger ,
\qquad \tilde{\boldsymbol{\Omega}} = \Omega_k e_k .
$$

Substituting the Larmor equation $\dot{\tilde{\boldsymbol{\mu}}} = \tfrac{1}{2}[\tilde{\boldsymbol{\mu}},\tilde{\boldsymbol{\omega}}_L]$ and collecting the generator of the frame's own motion gives

$$
\tilde{R}_\Omega\,\dot{\tilde{\boldsymbol{\mu}}}_{\rm rot}\,\tilde{R}_\Omega^\dagger
= \tfrac{1}{2}\left[\tilde{\boldsymbol{\mu}},\,\tilde{\boldsymbol{\omega}}_L + \tilde{\boldsymbol{\Omega}}\right].
$$

If the frame rotates at exactly

$$
\boldsymbol{\Omega} = -\gamma\,\mathbf{B} = \boldsymbol{\omega}_L ,
$$

the right-hand side vanishes, and the moment is **at rest in the rotating frame**. This is the Larmor theorem: the effect of a uniform magnetic field on a magnetic moment is equivalent to a rotation of the frame at the Larmor frequency, and in that frame the moment is stationary.

### What the Theorem Does and Does Not Say

The theorem is exact for a single moment in a uniform field, and it extends to a collection of moments only when they share the same gyromagnetic ratio: the frame that is at rest for one value of $\gamma$ is not at rest for another, so a medium with several species has one Larmor frame per species. The theorem is also the kinematic basis of magnetic resonance: a small transverse field rotating at $\boldsymbol{\omega}_L$, the same rate and the same sense as the Larmor frame, appears static in that frame and can therefore tip the moment away from the field, while a field at any other frequency averages away. The rotating-frame construction is the classical basis of the resonance experiments; the quantum treatment of the same frame is given in the companion article *Exercise: Spin Precession in a Magnetic Field*, and the half-angle rotor used here is the same one.

The theorem is a statement about the *frame*, not about the moment: the moment is a material vector and does not change its magnitude in any frame. In the biquaternion description the frame rotation and the precession are two rotor conjugations, and their composition is again a rotor conjugation; the content of the theorem is that the two generators add — the generator of the motion in the rotating frame is $\tilde{\boldsymbol{\omega}}_L + \tilde{\boldsymbol{\Omega}}$ — while the angular velocity it corresponds to is the difference $\boldsymbol{\omega}_L - \boldsymbol{\Omega}$, the frame's rate subtracted from the Larmor rate. At $\boldsymbol{\Omega} = \boldsymbol{\omega}_L$ the generator vanishes and the moment is at rest.

## The Gyromagnetic Ratio

### Definition

The gyromagnetic ratio is the constant of proportionality between the moment and the angular momentum,

$$
\boldsymbol{\mu} = \gamma\,\mathbf{S},
$$

and it is conventional to express it through the dimensionless **gyromagnetic factor** $g$ by

$$
\boldsymbol{\mu} = g\,\frac{q}{2m}\,\mathbf{S},
\qquad\text{so that}\qquad
\gamma = g\,\frac{q}{2m},
$$

where $q$ and $m$ are the charge and mass of the carrier. For a purely orbital or convective current, the classical theorem of the next article gives $\gamma = q/2m$, that is $g = 1$; for an intrinsic moment, the same articles give $\gamma = q/m$, that is $g = 2$. The Larmor frequency is then $\omega_L = |g|\,|q|B/2m$ for the spin, and one Bohr magneton,

$$
\mu_B = \frac{e\hbar}{2m_e} = 9.274010\times10^{-24}\ \text{J T}^{-1},
$$

per unit spin for the electron.

### The Orbital Value, and a Preview

For a rigid rotor with proportional charge and mass densities, the moment and the angular momentum are related by the ratio of the two inertia tensors, and the moment is $\boldsymbol{\mu} = (q/2m)\mathbf{L}$. The Larmor frequency of an orbital moment is therefore fixed by $q/2m$ and does not require any intrinsic structure. The intrinsic case is different: a moment attributed to the body is not a convective current, and the value of $\gamma$ is not fixed by any charge density. The companion article *The Einstein–de Haas and Barnett Effects in Biquaternionic Form* treats the reciprocal pair of effects in which a change of an intrinsic moment rotates the body and a rotation of the body magnetizes it; the companion article *The Classical Origin of g = 2 in Biquaternionic Form* accounts for the fact that the intrinsic gyromagnetic ratio is twice the orbital one. Both presuppose the Larmor equation derived here, and both work with the same rotor.

## Relation to the Quantum Treatment

The precession of a spin-$\tfrac{1}{2}$ in a magnetic field is treated in the sibling quantum category, in the companion articles *Spin-1/2 Quantum Mechanics in Biquaternionic Form* and *Exercise: Spin Precession in a Magnetic Field*. There the state is an idempotent $P = \tfrac{1}{2}(e_0 + i\hat{\mathbf{n}})$ of $\mathbb{M}_+$, the Hamiltonian is the Hermitian element $\tilde{H} = -\gamma B_0\tilde{S}_z$ with $\tilde{S}_z = \tfrac{\hbar}{2}ie_3$, the evolution is the rotor conjugation $\tilde{\rho}(t) = \tilde{U}(t)\tilde{\rho}(0)\tilde{U}(t)^\dagger$ with $\tilde{U}(t) = \exp(-i\tilde{H}t/\hbar)$, and the expectation value is the trace pairing $\langle\tilde{S}_x\rangle = \mathrm{Tr}(\tilde{\rho}\tilde{S}_x)$. The evolved Bloch vector is $\mathbf{r}(t) = \cos(\gamma B t)e_1 - \sin(\gamma B t)e_2$, which is the precession derived here, with the same frequency and the same sense.

The two treatments agree because they are the same rotor. The classical moment of this article lives in $\mathbb{H}_{\mathbb{B}}$ as a real pure quaternion and is rotated by $\tilde{R}_L(t) = \exp(-\tfrac{1}{2}\gamma B t\,\hat{B}_k e_k)$; the quantum state lives in $\mathbb{M}_+$ and is rotated by $\tilde{U}(t)$, whose vector part is the same unit real quaternion. The factor $i$ that separates the two representatives is the sector exchange, not a physical difference. What the quantum treatment adds is the Born rule and the state; what this article adds is that the precession needs neither, because the moment of a classical current distribution obeys the same Larmor equation as the mean spin. The two are different derivations of one motion, and the classical one is the subject of this subcategory.

## Summary

The magnetic moment of a current distribution is an axial vector, and in the biquaternion framework it is a pure real quaternion $\tilde{\boldsymbol{\mu}} = \mu_k e_k$ in the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the same slot that carries the magnetic induction $\mathbf{B} = B_k e_k$. The two bilinears of the magnetic coupling are the scalar and vector parts of the single quaternion product,

$$
\tilde{\boldsymbol{\mu}}\,\mathbf{B} = -\,\boldsymbol{\mu}\cdot\mathbf{B} + \boldsymbol{\mu}\times\mathbf{B},
$$

so that the energy is $U = \mathrm{Sc}(\tilde{\boldsymbol{\mu}}\mathbf{B}) = -\boldsymbol{\mu}\cdot\mathbf{B}$ and the torque is $\boldsymbol{\tau} = \mathrm{Vect}(\tilde{\boldsymbol{\mu}}\mathbf{B}) = \boldsymbol{\mu}\times\mathbf{B}$.

The torque equation for a moment tied to an angular momentum by $\boldsymbol{\mu} = \gamma\mathbf{S}$ is the **Larmor equation**

$$
\dot{\boldsymbol{\mu}} = \gamma\,\boldsymbol{\mu}\times\mathbf{B},
\qquad \boldsymbol{\omega}_L = -\,\gamma\,\mathbf{B},
$$

which in the algebra is the commutator

$$
\dot{\tilde{\boldsymbol{\mu}}} = \tfrac{1}{2}\left[\tilde{\boldsymbol{\mu}},\tilde{\boldsymbol{\omega}}_L\right],
\qquad \tilde{\boldsymbol{\omega}}_L = \gamma\,\mathbf{B}.
$$

The equation is solved by the **rotor conjugation**

$$
\tilde{\boldsymbol{\mu}}(t) = \tilde{R}_L(t)\,\tilde{\boldsymbol{\mu}}(0)\,\tilde{R}_L(t)^\dagger,
\qquad
\tilde{R}_L(t) = \exp\!\left(-\,\frac{\gamma B t}{2}\,\hat{B}_k e_k\right),
$$

with $\tilde{R}_L$ a unit real quaternion; the moment turns through $\gamma B t$ while the rotor turns through half that angle, the double-cover half-angle of the algebra. The norm form $N(\tilde{\boldsymbol{\mu}})$ and the energy $U$ are conserved, so the moment precesses on a cone about the field at the Larmor frequency $\omega_L = |\gamma|B$. The **Larmor theorem** states that in a frame rotating at $\boldsymbol{\Omega} = -\gamma\mathbf{B}$ the moment is at rest; the generator of the motion in that frame is the sum $\tilde{\boldsymbol{\omega}}_L + \tilde{\boldsymbol{\Omega}}$ of the Larmor and frame generators, whose corresponding angular velocity is the difference $\boldsymbol{\omega}_L - \boldsymbol{\Omega}$, and the theorem is exact for a single moment in a uniform field.

The gyromagnetic ratio is $\gamma = g\,q/2m$, with $g = 1$ for a convective moment and $g = 2$ for an intrinsic one. The Larmor equation derived here is the common premise of the companion articles *The Einstein–de Haas and Barnett Effects in Biquaternionic Form* and *The Classical Origin of g = 2 in Biquaternionic Form*, and its rotor is the same half-angle rotor that the quantum treatment of spin precession employs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, home of the rotation rotors |
| $\tilde{\boldsymbol{\mu}} = \mu_k e_k$ | Classical magnetic moment (pure real quaternion) |
| $i\,\mathbf{m} = \mu_k\,i e_k$ | Intrinsic moment's informational-sector representative |
| $\mathbf{B} = B_k e_k = \mu\mathbf{H}$ | Magnetic induction (pure real quaternion) |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion |
| $\mathbf{j}, \rho_c, \rho_m$ | Current density; charge and mass densities |
| $\hat{\Pi}_{ij} = \int\rho_c(r^2\delta_{ij}-r_ir_j)$ | Charge inertia tensor |
| $\hat{I}_{ij} = \int\rho_m(r^2\delta_{ij}-r_ir_j)$ | Mass inertia tensor |
| $\mathbf{L} = \hat{I}\boldsymbol{\omega}$ | Mechanical angular momentum |
| $\gamma$, $g$ | Gyromagnetic ratio; gyromagnetic factor ($\gamma = g\,q/2m$) |
| $\boldsymbol{\omega}_L = -\gamma\mathbf{B}$ | Larmor angular velocity |
| $\omega_L = |\gamma|B$ | Larmor frequency |
| $\tilde{\boldsymbol{\omega}}_L = \gamma\mathbf{B}$ | Larmor biquaternion (Larmor equation) |
| $\tilde{R}(\theta,\hat{\mathbf{n}}) = \cos\tfrac{\theta}{2}e_0 + \sin\tfrac{\theta}{2}\hat{n}_ke_k$ | Rotation rotor (unit real quaternion) |
| $\mathcal{R}(\theta,\hat{\mathbf{n}})$ | Three-vector rotation through $\theta$ about $\hat{\mathbf{n}}$ |
| $\tilde{\boldsymbol{\mu}}(t) = \tilde{R}_L\tilde{\boldsymbol{\mu}}(0)\tilde{R}_L^\dagger$ | Precession as rotor conjugation |
| $U = -\boldsymbol{\mu}\cdot\mathbf{B} = \mathrm{Sc}(\tilde{\boldsymbol{\mu}}\mathbf{B})$ | Magnetic energy |
| $\boldsymbol{\tau} = \boldsymbol{\mu}\times\mathbf{B} = \mathrm{Vect}(\tilde{\boldsymbol{\mu}}\mathbf{B})$ | Magnetic torque |
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
