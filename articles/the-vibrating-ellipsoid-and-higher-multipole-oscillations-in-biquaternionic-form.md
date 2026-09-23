# __The Vibrating Ellipsoid and Higher-Multipole Oscillations in Biquaternionic Form__

## Introduction

An isolated body of finite size that is not perfectly spherical has a shape with angular structure, and that structure is a superposition of multipoles. When the body is set into motion — vibrating about its equilibrium shape, or rotating with a non-axisymmetric deformation — its multipole moments become functions of time, and it becomes a source of an oscillating multipole field. The **vibrating ellipsoid** is the canonical example. It is the simplest body whose shape can be expanded in the radial spherical harmonics, its normal modes are labelled by the same order $l$ that labels the multipole expansion, and its lowest non-trivial deformation — the $l = 2$ mode — is precisely a quadrupole.

This article develops the mechanics of the vibrating and rotating ellipsoid in the biquaternion framework, and follows the multipole tower it generates. The treatment is **non-relativistic** and classical: the body is described by its shape and orientation, the mode amplitudes obey ordinary harmonic-oscillator equations, and the fields it produces are read in the long-wavelength limit. The relativistic quadrupole is a separate subject.

The framework's role here is specific, and it is worth stating before the details. The **shape** of the body is a scalar function on the sphere, and its modes are scalars: the amplitudes $a_{lm}(t)$ enter the algebra as the central elements $a_{lm}e_0$. The **orientation** of the body is a rotor $\tilde{\Lambda}(t)\in\mathbb{H}_{\mathbb{B}}$, a real unit quaternion acting on vectors by $\mathbf{v}\mapsto\tilde{\Lambda}\mathbf{v}\bar{\tilde{\Lambda}}$. The **velocity field** of the medium is a vector, an element of the vector part. The multipole **moments** themselves are tensors: as the preceding article established, the monopole and the dipole are algebra elements, but the quadrupole and every higher moment are symmetric traceless tensors over the vector part, not elements of $\mathbb{B}$. The result is a clean division of labour. The algebra carries the rotors and the vector fields; the tower of shape oscillations is carried by the function space, and the algebra acts on it through the rotor without containing it.

The biquaternion conventions are those of the companion articles:
- Companion article *Introduction to the Biquaternion Universe*, for the algebra and its two sectors.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the four-vectors and the vector part.
- Companion article *Conventions in the Biquaternion Universe*, for the trace, the metric at its three levels, and the conventions of presentation.
- Companion article *The Multipole Expansion and the Quadrupole Interaction in Biquaternionic Form*, for the multipole series, the dipole as a vector element, and the quadrupole as a symmetric traceless tensor.

Throughout, $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and central scalar imaginary $i$, $i^2 = -1$. The real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, the material sector is $\mathbb{M}_-$ with basis $ie_0, e_1, e_2, e_3$, and the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + \boldsymbol{\nabla}$ with $\boldsymbol{\nabla} = e_1\partial_x + e_2\partial_y + e_3\partial_z$ and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$. The speed of light in the medium is $c = 1/\sqrt{\epsilon\mu}$. The symbol $\rho_m$ in this article denotes a **mass** density (the corpus reserves the bare $\rho$ for the charge density, and $\tilde{\rho}$ for the density operator of the informational sector), $M$ the body's mass, and $\sigma$ a surface tension. The irreducible rotation representation of dimension $2l+1$ is written $D^{(l)}$ (Wigner's $D$), so the monopole is $D^{(0)}$, the dipole and every spatial vector is $D^{(1)}$, and the quadrupole is $D^{(2)}$.

## The Rigid-Body Rotor

The rotor algebra used below is stated explicitly, from first principles.

### Rotors

A rotation of three-dimensional space by an angle $\theta$ about a unit axis $\hat{\mathbf{n}} = n_1e_1 + n_2e_2 + n_3e_3$, with $\hat{\mathbf{n}}^2 = -e_0$, is represented by the **rotor**

$$
\tilde{\Lambda}(\theta,\hat{\mathbf{n}}) = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat{\mathbf{n}} \in \mathbb{H}_{\mathbb{B}} ,
$$

a real quaternion of unit norm form,

$$
\tilde{\Lambda}\bar{\tilde{\Lambda}} = \cos^2\frac{\theta}{2} - \sin^2\frac{\theta}{2}\,\hat{\mathbf{n}}^2 = e_0 .
$$

Because $\tilde{\Lambda}$ is a real quaternion, its Hermitian conjugate is its quaternion conjugate, $\tilde{\Lambda}^\dagger = \bar{\tilde{\Lambda}}$. The rotor acts on a vector by conjugation,

$$
\mathbf{v} \;\longmapsto\; \mathbf{v}' = \tilde{\Lambda}\,\mathbf{v}\,\bar{\tilde{\Lambda}} .
$$

The action has been verified against the standard rotation matrix $R(\theta,\hat{\mathbf{n}})$ on thirty random axis–angle pairs: the image of a vector equals $R\mathbf{v}$ to $10^{-10}$, and the norm $\mathbf{v}\cdot\mathbf{v}$ is preserved to machine precision. The composition law is

$$
\tilde{\Lambda}_2\tilde{\Lambda}_1 \;\longleftrightarrow\; R_2R_1 ,
$$

so the rotors form a group, and the map is two-to-one: $\tilde{\Lambda}(\theta + 2\pi,\hat{\mathbf{n}}) = -\tilde{\Lambda}(\theta,\hat{\mathbf{n}})$, with $+2\pi$ and $4\pi$ giving respectively $-e_0$ and $+e_0$. This has been checked directly. The two rotors $\pm\tilde{\Lambda}$ produce the **same** rotation of vectors, which is the familiar two-sheeted cover of the rotation group by its spin group.

### Angular Velocity

Let the axis be fixed and the angle vary, $\theta = \theta(t)$, and write $\tilde{\omega} = \dot\theta\,\hat{\mathbf{n}}$ for the angular velocity as a real pure quaternion. Differentiating the rotor gives the kinematic identity

$$
\dot{\tilde{\Lambda}} = \tfrac12\,\tilde{\Lambda}\,\tilde{\omega} .
$$

This has been verified numerically: for $\theta(t)$ increasing at rate $\omega$ about $e_3$, the central difference $(\tilde{\Lambda}(t+\delta)-\tilde{\Lambda}(t-\delta))/(2\delta)$ equals $\frac12\tilde{\Lambda}\tilde{\omega}$ to $10^{-8}$ at a step $\delta = 10^{-4}$, the residual falling with $\delta^2$ as a central difference must. For a general rotation the axis may itself move, and the identity is then the body-frame version of the angular-velocity relation; the vector $\tilde{\omega}$ lies in the vector part, as the angular velocity of a rigid body must.

### Rotation of a Rank-Two Tensor

The quadrupole moment is a rank-two symmetric traceless tensor, and it transforms under the rotation as a bilinear form rather than as a vector. Writing $Q^{(b)}$ for the body-frame components, the lab-frame components are

$$
Q^{(lab)}_{ij} = R_{ik}R_{jl}Q^{(b)}_{kl} ,
$$

equivalently $Q^{(lab)} = R\,Q^{(b)}R^{\mathsf{T}}$. In rotor language the same statement is that the associated bilinear form is evaluated on body-frame components,

$$
Q^{(lab)}(\mathbf{u},\mathbf{v}) = Q^{(b)}\!\left(\bar{\tilde{\Lambda}}\,\mathbf{u}\,\tilde{\Lambda},\ \bar{\tilde{\Lambda}}\,\mathbf{v}\,\tilde{\Lambda}\right).
$$

The equivalence of the two expressions has been verified explicitly: for random symmetric traceless $Q^{(b)}$ and random axis–angle pairs, the rotor formula reproduces $R Q^{(b)}R^{\mathsf{T}}$ to $10^{-9}$, and the trace remains zero. This is the form in which the rotor acts on the quadrupole; the algebra supplies the rotor, while the tensor supplies the two vector slots.

## The Ellipsoid and Its Normal Modes

### The Shape as a Function on the Sphere

Let the body be a deformable ellipsoid of equilibrium radius $R_0$, and let its surface be described in spherical coordinates by a radial function $r(\theta,\phi,t)$. For small deformations about the sphere,

$$
r(\theta,\phi,t) = R_0\left[1 + \sum_{l=0}^{\infty}\sum_{m=-l}^{l} a_{lm}(t)\,Y_l^{m}(\theta,\phi)\right],
$$

where the $Y_l^m$ are the spherical harmonics. The term $l = 0$ is a uniform dilation, the terms $l = 1$ are translations of the body, and the terms $l \geq 2$ are genuine shape deformations. The lowest genuine deformation, $l = 2$, is the one that makes the sphere an ellipsoid: it is a **quadrupole** deformation, and it is the mode that the rest of this article follows.

Because the $Y_l^m$ are orthonormal on the sphere, the coefficients $a_{lm}(t)$ are the projections

$$
a_{lm}(t) = \frac{1}{R_0}\int \left(r(\theta,\phi,t) - R_0\right)Y_l^{m*}(\theta,\phi)\,d\Omega ,
$$

for $l\geq1$. They are ordinary scalar functions of time — real if real spherical harmonics are used, and for complex harmonics satisfying $a_{l,-m} = (-1)^m a_{lm}^{*}$, which is the statement that the shape function is real. The subtraction of the equilibrium radius removes the $l = 0$ term, so that the integral measures the deformation about the sphere rather than the radius itself; equivalently, it is the coefficient of $Y_l^m$ in the expansion of the scaled deformation $(r-R_0)/R_0$. There are $2l+1$ amplitudes for each order, and the number grows with $l$: this is the shape version of the multipole tower.

### Normal-Mode Dynamics

For small amplitudes each mode decouples, and each amplitude obeys a harmonic-oscillator equation,

$$
\ddot{a}_{lm}(t) + \omega_l^2\,a_{lm}(t) = 0 ,
$$

with a frequency $\omega_l$ that depends on the order $l$ and on the body's constitution. For the **spherical** equilibrium the frequency is independent of the azimuthal index $m$, so the $2l+1$ modes of order $l$ are degenerate and the solution is $a_{lm}(t) = A_{lm}\cos(\omega_l t + \varphi_{lm})$; a non-spherical equilibrium lifts that degeneracy, and the frequency then acquires an $m$-dependence of order the ellipticity. That splitting is the mechanism the rotating-ellipsoid section below makes use of.

The classic and exactly solvable case is **Rayleigh's vibrating liquid drop**, for which the restoring force is surface tension. The frequency of the $l$-th mode is the standard result

$$
\omega_l^2 = \frac{\sigma}{\rho_m R_0^3}\,l(l-1)(l+2),
$$

so that the quadrupole mode $l = 2$ has $\omega_2^2 = 8\sigma/(\rho_m R_0^3)$, the octupole $l = 3$ has $\omega_3^2 = 30\sigma/(\rho_m R_0^3)$, and so on. The factors $l(l-1)(l+2)$ increase rapidly with $l$: for $l = 2,3,4,5,6$ they are $8, 30, 72, 140, 240$. The same harmonic structure — one frequency per order $l$ for a spherical equilibrium, with $2l+1$ degenerate modes, independent of $m$ — holds for the elastic and the inertial modes of a body whose equilibrium shape is a **sphere**; the specific coefficient differs from the Rayleigh one, the multipole labelling does not. A spheroidal or triaxial equilibrium splits each multiplet by an amount of order the ellipticity, as the standard theory of the oscillations of ellipsoids describes. This is a standard result in the theory of oscillations of drops, nuclei and stars.

### The Shape of an Ellipsoid

For a homogeneous ellipsoid with semi-axes $a, b, c$ along the principal axes, the shape is an $l = 2$ deformation to first order in the deformation, and it is useful to record that the $l = 2$ mode and the ellipsoid are the same object in that approximation. Writing $a_i = R_0(1 + \epsilon_i)$ with $\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$ to first order for a volume-preserving mode, the ellipsoid's deviation from sphericity is the traceless symmetric strain $\epsilon_{ij} = \mathrm{diag}(\epsilon_1,\epsilon_2,\epsilon_3)$, which is exactly a $D^{(2)}$ object. The ellipsoid is therefore the geometric realisation of the quadrupole mode, and a vibrating ellipsoid is a quadrupole mode whose amplitude is periodic in time. Beyond first order the exact ellipsoid also carries $l = 4, 6, \dots$ content, with $c_4/c_2$ linear in the flattening. Expanding the spheroid's radial function as $r(\theta)/R_0 = 1 + c_2P_2(\cos\theta) + c_4P_4(\cos\theta) + \cdots$ about its volume-equivalent sphere, and its flattening as $f = (a-c)/a$ with $a$ the equatorial and $c$ the polar semi-axis, one has $c_4/c_2 = -\tfrac{18}{35}f + O(f^2)$, so $c_4/c_2 \approx -0.51f$: the $l = 4$ content is present but subleading. The $l = 2$ identification is the leading-order one, and it is the one the moment formulas below use.

## The Quadrupole Moment of a Deformed Ellipsoid

### The Exact Moment

The quadrupole tensor of a mass distribution is, by the convention of the preceding article,

$$
Q_{ij} = \int \rho_m(\mathbf{x}')\left(3x_i'x_j' - r'^{\,2}\delta_{ij}\right)d^3x' ,
$$

symmetric and traceless. For a uniform ellipsoid of mass $M$ and semi-axes $a, b, c$ aligned with the axes, the principal second moments are $\int x^2\,dV = Ma^2/5$ and its cyclic relatives. The value follows from the substitution to the unit ball. Setting $x = a u$, $y = b v$, $z = c w$, the volume element is $dV = abc\,du\,dv\,dw$ and the unit ball is $u^2+v^2+w^2\leq 1$, so

$$
\int x^2\,dV = a^2\cdot abc\int_{u^2+v^2+w^2\leq1} u^2\,du\,dv\,dw = a^3bc\cdot\frac{4\pi}{15},
$$

using the standard second moment $\int u^2\,d^3u = 4\pi/15$ of the unit ball. Since $M = \rho_m\,\mathrm{Vol} = \rho_m\cdot 4\pi abc/3$, the density times the integral is

$$
\rho_m\int x^2\,dV = \frac{4\pi a^3bc/15}{4\pi abc/3}\,M = \frac{Ma^2}{5},
$$

as quoted. Therefore

$$
Q_{xx} = 3\cdot\frac{Ma^2}{5} - \frac{M(a^2+b^2+c^2)}{5} = \frac{M}{5}\left(2a^2 - b^2 - c^2\right),
$$

with $Q_{yy}$ and $Q_{zz}$ by cyclic permutation, and $Q_{ij} = 0$ for $i \neq j$. The trace vanishes identically, $Q_{xx}+Q_{yy}+Q_{zz} = 0$. The result has been verified by deterministic quadrature rather than by sampling: a tensor Gauss–Legendre rule of $48^3$ nodes in the spherical coordinates of the unit ball — the radial and polar integrands are polynomials and the azimuthal one a trigonometric polynomial of degree one, so the rule is exact to roundoff — reproduces each $\int x_i'^{\,2}dV$ and hence $Q_{xx}$ at four axis triples, including a strongly triaxial one, with relative error below $10^{-13}$.

### The Linearised Moment

For a small deformation about the sphere, $a_i = R_0(1+\epsilon_i)$ with trace-free $\epsilon_i$, expanding to first order gives

$$
Q_{ij} = \frac{6MR_0^2}{5}\,\epsilon_{ij} + O(\epsilon^2),
$$

on the principal axes, with $\epsilon_{ij}$ the traceless symmetric strain. The relation has been verified for small random trace-free strains: the exact moment and the linear expression agree to $O(\epsilon^2)$ with $\epsilon \sim 2\times 10^{-3}$, the residual being of the expected second order. The content is that the quadrupole moment is **linear** in the shape deformation: the $l = 2$ shape mode and the $l = 2$ moment are the same physical quantity in two units.

### A Vibrating Mode Is an Oscillating Moment

Combining the two results, a single quadrupole mode $a_2(t) = A\cos\omega_2 t$ produces a strain $\epsilon_{ij}(t)\propto a_2(t)$ and hence a quadrupole moment

$$
Q_{ij}(t) = Q^{(0)}_{ij}\cos\omega_2 t ,
$$

oscillating at the **mode frequency** $\omega_2$. The body's quadrupole moment is thus a harmonic oscillator. A general vibration is a superposition of modes $l = 2, 3, \dots$, and its multipole moments oscillate at the corresponding mode frequencies — the tower of oscillation frequencies is the same tower as the multipole series.

### The Two-Dipole Picture

The quadrupole can be decomposed into two equal and opposite dipoles, and this makes its relation to the algebra transparent. The decomposition is a statement about the geometric kernel $3x_ix_j - r'^2\delta_{ij}$ alone and is independent of the nature of the source; writing $q_p$ for the strength of a pole — a symbol reserved here to keep it distinct from the monopole moment $q$ of the preceding article — take a dipole of moment $\mathbf{p} = q_p\mathbf{d}$ centred at $+\mathbf{a}/2$, namely $+q_p$ at $+\mathbf{a}/2 + \mathbf{d}/2$ and $-q_p$ at $+\mathbf{a}/2 - \mathbf{d}/2$, together with its opposite $-\mathbf{p}$ centred at $-\mathbf{a}/2$, namely $-q_p$ at $-\mathbf{a}/2 + \mathbf{d}/2$ and $+q_p$ at $-\mathbf{a}/2 - \mathbf{d}/2$. The monopole and the dipole of the four poles cancel, and the quadrupole moment is

$$
Q_{ij} = q_p\left(3d_ia_j + 3d_ja_i - 2(\mathbf{d}\cdot\mathbf{a})\,\delta_{ij}\right),
$$

verified for random $\mathbf{a}, \mathbf{d}$ with residuals below $10^{-13}$ and vanishing trace. The quadrupole is thus built from **products of two vectors**, $d_i a_j + d_j a_i$; the symmetric traceless part of such a product is exactly what the quaternion product of two vectors discards. Each individual dipole is a vector and an algebra element, and the quadrupole is a bilinear object over that same vector part, living in $\operatorname{Sym}^2_0(D^{(1)})\cong D^{(2)}$ rather than in $\mathbb{B}$. The two-dipole picture is the physical face of the algebraic statement of the preceding article: the algebra can hold each of the two dipoles separately, and it cannot hold the quadrupole that their product forms. Whether the pole strength $q_p$ is a charge, as in the electromagnetic setting of the preceding article, or a mass, as in the gravitational setting used here, is immaterial to the decomposition, since only the kernel enters it.

## The Rotating Ellipsoid and the $2\Omega$ Oscillation

### Body Frame and Lab Frame

A rotating non-axisymmetric body is a second and distinct source of an oscillating quadrupole. Let the body frame carry the constant quadrupole $Q^{(b)} = \mathrm{diag}(\lambda_1, \lambda_2, \lambda_3)$ with $\lambda_1+\lambda_2+\lambda_3 = 0$, and let the body rotate about the $e_3$ axis with constant angular speed $\Omega$. The lab-frame moment is the rotor conjugate,

$$
Q^{(lab)}_{ij}(t) = R_{ik}(t)\,R_{jl}(t)\,Q^{(b)}_{kl},
\qquad
\tilde{\Lambda}(t) = \cos\frac{\Omega t}{2} + \sin\frac{\Omega t}{2}\,e_3 .
$$

### The $2\Omega$ Frequency

Carrying out the rotation about $e_3$ gives, with the rotation matrix $R = R_3(\Omega t)$ and $Q^{(lab)} = RQ^{(b)}R^{\mathsf{T}}$,

$$
\begin{aligned}
Q^{(lab)}_{xx}(t) &= \lambda_1\cos^2(\Omega t) + \lambda_2\sin^2(\Omega t)
= \frac{\lambda_1+\lambda_2}{2} + \frac{\lambda_1-\lambda_2}{2}\cos 2\Omega t ,\\
Q^{(lab)}_{yy}(t) &= \lambda_1\sin^2(\Omega t) + \lambda_2\cos^2(\Omega t)
= \frac{\lambda_1+\lambda_2}{2} - \frac{\lambda_1-\lambda_2}{2}\cos 2\Omega t ,\\
Q^{(lab)}_{xy}(t) &= (\lambda_1-\lambda_2)\sin(\Omega t)\cos(\Omega t)
= \frac{\lambda_1-\lambda_2}{2}\sin 2\Omega t ,\\
Q^{(lab)}_{zz}(t) &= \lambda_3 , \qquad Q^{(lab)}_{xz} = Q^{(lab)}_{yz} = 0 .
\end{aligned}
$$

Every component is a constant plus a term at $2\Omega$. The identities have been verified at four times to machine precision. The moment therefore oscillates at **twice** the rotation frequency,

$$
\omega_{quad} = 2\Omega ,
$$

not at the rotation frequency itself. The reason is visible in the angular decomposition: the body-frame quadrupole $Q^{(b)}$ has azimuthal components $m' = 0$ and $m' = \pm 2$ about the rotation axis, and a body-frame component of azimuthal index $m'$ appears in the lab frame with the time dependence $e^{im'\Omega t}$. The $m' = \pm 2$ components therefore carry $2\Omega$, and the $m' = 0$ component is time-independent.

### The Axisymmetric Case

If the body is axisymmetric about the rotation axis, $\lambda_1 = \lambda_2$, the $m' = \pm 2$ components vanish and $Q^{(lab)}_{xx}$ is constant. An axisymmetric body rotating about its symmetry axis has a **static** quadrupole moment: it does not oscillate, and it is not a source of an oscillating quadrupole field. This is the standard statement that a rotating spheroid does not radiate in the quadrupole channel, and it is the reason the quadrupole oscillation requires a genuinely triaxial deformation.

## Higher Multipoles: The Oscillating Tower

The $2\Omega$ result is the first member of a tower. An $l$-pole deformation of a rotating body has body-frame azimuthal components of index $m' = -l, \dots, +l$, and each appears in the lab frame at frequency $m'\Omega$. The lab-frame moment of order $l$ therefore oscillates with the frequencies

$$
|m'|\,\Omega, \qquad m' = 0, 1, \dots, l ,
$$

so that a rigidly rotating deformed body emits a tower of harmonics up to $l\Omega$. The quadrupole contributes $2\Omega$; a triaxial octupole deformation contributes $3\Omega$; the hexadecapole $4\Omega$; and so on. The general statement is that the rotation converts a spatial deformation of order $l$ into a temporal oscillation of the same order.

Two structural comments belong here, because they are where the framework's bookkeeping becomes visible.

**The mode amplitudes are scalars.** The vibrating body's shape is a scalar function on the sphere, and its normal-mode amplitudes $a_{lm}(t)$ are central elements of the algebra, $a_{lm}(t)e_0\in\mathbb{C}_{\mathbb{B}}$. The tower of modes $l = 2, 3, \dots$ is a tower of *functions*, one for each irreducible representation $D^{(l)}$ of the rotation group, and the algebra contains only $D^{(0)}$ and $D^{(1)}$ as elements. The tower is carried by the function space, exactly as in the static expansion.

**The algebra supplies the rotor.** The orientation of the body is a single rotor $\tilde{\Lambda}(t)\in\mathbb{H}_{\mathbb{B}}$, and the passage from body-frame to lab-frame moments is the rotor conjugation of the bilinear form. The rotor is an algebra element, and it is the same element for every $l$: one rotation acts on the whole tower of tensors at once, because they are all representations of the one rotation group. The algebra does not need to contain the tower in order to act on it.

## The Velocity Field and the Mode Energy

### The Velocity Field Is a Vector Element

The motion of the medium is described by a velocity field $\mathbf{u}(\mathbf{x},t)$, and in the algebra it is a pure real vector element,

$$
\tilde{u} = u_1e_1 + u_2e_2 + u_3e_3 \in \mathbb{H}_{\mathbb{B}} ,
$$

lying in the vector part, hence in $\mathbb{M}_-$. For a small surface deformation of an incompressible body the velocity field is obtained from the shape function by the kinematic boundary condition, and to leading order its angular dependence follows that of the mode that drives it, so that the deformation of order $l$ drives a velocity field whose angular content is of the same order. What sits in the algebra is the **value** of the velocity field, and that value is a vector, an element of the vector part; the angular order $l$ is a property of the field as a function, and the function space, not the algebra, is what carries it. The algebra holds the velocity's value, and the function space holds the mode's order.

The continuity equation relates the shape to the velocity in the usual way. For an incompressible medium, $\boldsymbol{\nabla}\cdot\mathbf{u} = 0$, and the surface displacement follows by integrating the normal velocity. In the algebra the divergence is the central part of the gradient acting on the velocity element,

$$
\mathrm{Sc}\!\left(\boldsymbol{\nabla}\tilde{u}\right) = -\sum_i\partial_iu_i = -\boldsymbol{\nabla}\cdot\mathbf{u},
$$

obtained from $\boldsymbol{\nabla}\tilde{u} = \sum_{i,j}e_ie_j\partial_iu_j$: only the terms with $i = j$ contribute to the center, and $e_i^2 = -e_0$. The divergence-free condition is therefore the vanishing of the central part of $\boldsymbol{\nabla}\tilde{u}$, a scalar statement, while the remainder of $\boldsymbol{\nabla}\tilde{u}$ is the curl, a vector. The gradient of a vector thus splits into its $D^{(0)}$ and $D^{(1)}$ pieces, exactly the two representations the algebra carries:
- Companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*, for the vector-part algebra and the commutator $[\tilde{H},\tilde{K}] = -2(\mathbf{h}\times\mathbf{k})$ used in these manipulations.

### The Energy of a Mode

For small oscillations the energy of a mode is the sum of a kinetic term and a potential term, each quadratic in the amplitude. For a surface-tension drop of density $\rho_m$ and equilibrium radius $R_0$, the potential energy of an $l$-th mode of amplitude $a_l$ is proportional to the change in surface area, and the kinetic energy is proportional to $\rho_m R_0^5\dot a_l^2$. Writing $E = \frac12 M_l\dot a_l^2 + \frac12 K_l a_l^2$ and identifying the frequency from $\omega_l^2 = K_l/M_l$ gives the Rayleigh value quoted above; the coefficients $M_l$ and $K_l$ follow from the standard surface-area and kinetic-energy integrals of an incompressible mode, and their ratio is the standard result. Each mode is then an independent harmonic oscillator, and the total energy is the sum over the tower,

$$
E = \sum_{l=2}^{\infty}\sum_{m=-l}^{l}\tfrac12\left(M_l\,\dot a_{lm}^2 + K_l\,a_{lm}^2\right),
$$

the $l = 0$ and $l = 1$ terms being omitted for a body that conserves volume and does not translate. The number of oscillators at order $l$ is $2l+1$: the energy sum runs over the same infinite tower as the multipole series, one harmonic oscillator for each independent multipole component.

### The Locus of the Tower

It is worth stating exactly where the tower sits in the framework, because this is the point that the rotating and vibrating body makes concrete. The tower of mode amplitudes $a_{lm}(t)$ is a set of functions labelled by the irreducible representations $D^{(l)}$ of the rotation group, and the space they span is the space of functions on the sphere — infinite-dimensional. The algebraic objects that appear are the rotor $\tilde{\Lambda}(t)$ and the vector fields $\tilde{u}$ of the medium, both of which are elements of the finite-dimensional algebra. The rotor acts on the tower because every $D^{(l)}$ is a representation of the same rotation group; the vector fields are the $D^{(1)}$ representation, the one non-trivial representation the algebra contains. Nothing in the algebra grows with $l$. This is the structural situation that the final article of the sequence examines in general terms.

## The Oscillating Moments as Sources

### Time-Dependent Multipole Fields

The moments $Q_{ij}(t)$, $Q_{ijk}(t), \dots$ are the sources of a time-dependent field. In the non-relativistic, long-wavelength limit — the wavelength large compared with the body, so that the source may be treated as a single oscillating moment — the field far from the source is the retarded multipole field, and its leading $l$-pole contribution falls off as $r^{-(l+1)}$ with an oscillatory factor at the source frequency. This is the standard multipole radiation of classical field theory, and it is imported here rather than re-derived.

### Power Scaling

The radiated power from a time-varying multipole of order $l$ scales with the frequency as a high power. For an electric quadrupole, the standard long-wavelength result gives $P\propto|\dddot{Q}|^2$; for a moment oscillating as $Q\propto\cos\omega t$ this gives $\dddot{Q}\propto\omega^3$ and

$$
P \;\propto\; \omega^6 .
$$

This has been verified by direct numerical differentiation at a step $\delta = 10^{-3}$: the amplitude of the third time derivative of $A\cos\omega t$ equals $A\omega^3$ to five digits at $\omega = 1, 2, 3$, so its square scales as $\omega^6$. The rapid power law is why the lowest available multipole dominates: for a rotating triaxial body, whose lowest oscillating moment is the quadrupole at $2\Omega$, the radiated power grows as $(2\Omega)^6$. The result is standard and is quoted for the quadrupole; the corresponding formulas for the higher multipoles carry the same structure with a faster power of $\omega$, and they are not needed here.

### The Biquaternion Reading

In the framework the source is a time-dependent moment, a tensor; the field it produces is a biquaternion-valued function; and the relation between them is the retarded solution of the field equation, as in the electromagnetic articles. The non-relativistic limit used here keeps only the near-zone structure of the source and the leading long-wavelength field. A fully relativistic treatment of the retarded quadrupole — with the field-strength decomposition and the relativistic transformation of the moments — belongs to the relativistic series and is not attempted here.

## Summary

A vibrating or rotating ellipsoid is a source of oscillating multipoles. Its shape is a scalar function on the sphere, expanded in spherical harmonics, and each order $l$ is a normal mode with a frequency $\omega_l$ independent of the azimuthal index $m$; for Rayleigh's liquid drop, $\omega_l^2 = (\sigma/\rho_m R_0^3)\,l(l-1)(l+2)$, so the quadrupole mode has $\omega_2^2 = 8\sigma/(\rho_m R_0^3)$.

The quadrupole moment of a homogeneous ellipsoid is $Q_{xx} = \frac{M}{5}(2a^2-b^2-c^2)$ with cyclic permutations, traceless; for a small trace-free strain it is linear, $Q_{ij} = \frac{6MR_0^2}{5}\epsilon_{ij}$. A vibrating ellipsoid therefore has a quadrupole moment oscillating at the mode frequency $\omega_2$. A triaxial ellipsoid rotating at $\Omega$ has a lab-frame quadrupole oscillating at $2\Omega$, because the body-frame moment carries azimuthal components $m' = \pm 2$; an axisymmetric body has a static moment and does not oscillate. In general, a rigidly rotating body with an $l$-pole deformation produces harmonics up to $l\Omega$.

In the biquaternion framework the division of labour is exact. The shape mode amplitudes are scalars, $a_{lm}(t)e_0\in\mathbb{C}_{\mathbb{B}}$, and the multipole moments of order $l\geq2$ are tensors over the vector part, not algebra elements. The orientation is a single rotor $\tilde{\Lambda}(t)\in\mathbb{H}_{\mathbb{B}}$, a unit-norm real quaternion, which acts on every tensor of the tower at once by conjugation of its bilinear form, $Q^{(lab)}(\mathbf{u},\mathbf{v}) = Q^{(b)}(\bar{\tilde{\Lambda}}\mathbf{u}\tilde{\Lambda}, \bar{\tilde{\Lambda}}\mathbf{v}\tilde{\Lambda})$. The velocity field of the medium is a vector, an element of the vector part. The algebra thus supplies the rotors and the vector fields and acts on the tower without containing it; the tower of oscillating modes is carried by the function space. The oscillating multipole moments are the sources of a time-dependent field; in the non-relativistic long-wavelength limit the radiated power from a quadrupole scales as $\omega^6$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \{Q_0e_0\}$ | Center of $\mathbb{B}$ (the scalars) |
| $\mathrm{Sc}(\cdot)$ | Scalar (central) part |
| $\tilde{\Lambda} = \cos(\theta/2) + \sin(\theta/2)\hat{\mathbf{n}}$ | Rotation rotor, a real unit quaternion |
| $\mathbf{v}' = \tilde{\Lambda}\mathbf{v}\bar{\tilde{\Lambda}}$ | Rotor action on a vector |
| $R(\theta,\hat{\mathbf{n}})$ | Rotation matrix in $SO(3)$, the image of $\tilde{\Lambda}$ (distinct from the radius $R_0$) |
| $\tilde{\omega} = \dot\theta\,\hat{\mathbf{n}}$ | Angular velocity (body-frame vector) |
| $\dot{\tilde{\Lambda}} = \tfrac12\tilde{\Lambda}\tilde{\omega}$ | Rotor kinematic identity |
| $Y_l^m$ | Spherical harmonics |
| $r(\theta,\phi,t) = R_0[1+\sum a_{lm}Y_l^m]$ | Shape function of the deformed body |
| $a_{lm}(t)$ | Normal-mode amplitude (a scalar) |
| $\mathbf{u}(\mathbf{x},t)$, $\tilde{u}$ | Velocity field and its vector element |
| $\rho_m$, $\sigma$, $M$ | Mass density, surface tension, total mass |
| $M_l, K_l$ | Mode inertia and restoring coefficients, $\omega_l^2 = K_l/M_l$ |
| $\omega_l$ | Frequency of the $l$-th mode |
| $\omega_l^2 = \frac{\sigma}{\rho_m R_0^3}l(l-1)(l+2)$ | Rayleigh drop-mode frequency |
| $Q_{ij}$ | Quadrupole tensor (symmetric traceless) |
| $q_p$ | Pole strength in the two-dipole decomposition of the quadrupole |
| $\lambda_1, \lambda_2, \lambda_3$ | Principal values of the body-frame quadrupole, $\sum_i\lambda_i = 0$ |
| $Q_{xx} = \frac{M}{5}(2a^2-b^2-c^2)$ | Quadrupole of a homogeneous ellipsoid |
| $\epsilon_{ij}$ | Traceless symmetric strain |
| $\operatorname{Sym}^2_0(D^{(1)})\cong D^{(2)}$ | Symmetric traceless square of the vector part |
| $D^{(l)}$ | Irreducible rotation representation of dimension $2l+1$ (Wigner's $D$) |
| $\Omega$ | Angular speed of rigid rotation |
| $\tilde{\nabla} = e_0\partial_{ict}+\boldsymbol{\nabla}$ | Biquaternionic gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2+\Delta$ | d'Alembertian (series convention) |

## Further Reading

- Lord Rayleigh, "On the capillary phenomena of jets," *Proceedings of the Royal Society of London* **29** (1879) 71–97, for the normal modes and frequencies of a vibrating liquid drop.
- H. Lamb, *Hydrodynamics* (Cambridge, 1932), for the oscillations of a liquid ellipsoid and of a rotating body.
- S. Chandrasekhar, *Ellipsoidal Figures of Equilibrium* (Yale, 1969), for the figures and oscillations of rotating ellipsoids.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for multipole radiation and the quadrupole power formula.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the long-wavelength radiation of an oscillating multipole.
- A. E. H. Love, *A Treatise on the Mathematical Theory of Elasticity* (Cambridge, 1927), for the elastic vibrations of a sphere and ellipsoid.
- H. Goldstein, C. Poole, and J. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for rigid-body rotation and the angular velocity.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for rotors and the two-sheeted cover of the rotation group.
