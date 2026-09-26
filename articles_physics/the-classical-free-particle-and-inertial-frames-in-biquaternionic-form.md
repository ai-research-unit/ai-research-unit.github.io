# __The Classical Free Particle and Inertial Frames in Biquaternionic Form__

## Introduction

The free particle is the simplest mechanical system, and it is the system on which the notion of an inertial frame is built. Newton's first law says that a particle subject to no force moves with constant velocity; a frame in which that statement holds is inertial; and the principle of relativity says that no inertial frame is preferred. The content of the law is therefore as much about the frames as about the particle.

In the biquaternion framework the worldline of a point particle is a curve in the **material sector** $\mathbb{M}_-$, the anti-Hermitian subspace of $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. The position of the particle is the biquaternion

$$
\tilde{X}(t) = ic\,t\,e_0 + \mathbf{x}(t),
$$

with $\mathbf{x} = x\,e_1 + y\,e_2 + z\,e_3$ a real pure quaternion. The free particle is the case in which this curve is a straight timelike line, and the four-velocity is a constant element of $\mathbb{M}_-$.

This article writes the free particle and the inertial-frame structure in that language. The material is standard — the four-velocity, the four-momentum, the mass-shell constraint, and the Lorentz transformation are those of the companion articles — and the article's interest is structural. Two facts are worth extracting in advance.

1. **The free particle is entirely in the material sector.** Its position, velocity and momentum lie in $\mathbb{M}_-$, and no vector direction of the informational sector $\mathbb{M}_+$ is occupied. This is what makes the free particle the **spin-zero benchmark** of the present subcategory: a structureless point particle has no internal vector that could precess, and the entire content of the mechanics is the material worldline.
2. **The non-relativistic limit of a Lorentz boost is not a rotation but a shear.** Expanding the boost rotor in the ratio of the frame velocity to the speed of light gives, to first order, the Galilean transformation $\mathbf{x} \mapsto \mathbf{x} - \mathbf{V}t$ with the time untouched. That map does not preserve the biquaternion norm form, so it is not a rotor conjugation, and the Galilean group is therefore not a subgroup of the biquaternion rotor group. It is a **contraction** of it. The contraction is what the non-relativistic limit costs algebraically, and it is visible directly in the algebra.

The conventions are those of the read list. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = \epsilon_{jkl}e_l$ for $j \neq k$; the scalar imaginary $i$ is central with $i^2 = -e_0$. The anti-Hermitian subspace $\mathbb{M}_-$ consists of $i q_0 e_0 + \mathbf{q}$ with $q_0 \in \mathbb{R}$ and $\mathbf{q}$ a real pure quaternion, and the Hermitian subspace $\mathbb{M}_+$ of $h_0 e_0 + i\mathbf{h}$ with $h_0, \mathbf{h}$ real. They are complementary, $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$, and exchanged by the scalar imaginary, $i\mathbb{M}_\pm = \mathbb{M}_\mp$. The real-quaternion subalgebra is $\mathbb{H}_{\mathbb{B}}$, the centre is $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$, and the trace satisfies $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ for $\tilde{P}, \tilde{H} \in \mathbb{M}_+$. The symbol $c$ denotes the speed of light in the medium, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ the vacuum speed of light; in vacuum $c = c_0$. The symbol $\mathbf{v}$ is reserved for particle velocities and $\mathbf{V}$ for frame velocities.

<!-- CONVENTION — vector-square notation: in this article $\mathbf{v}^2$, $\mathbf{V}^2$, $\mathbf{x}^2$ and $d\mathbf{x}^2$ denote the Euclidean squares $|\mathbf{v}|^2$, $|\mathbf{V}|^2$, $|\mathbf{x}|^2$, $|d\mathbf{x}|^2$, as in $\gamma = 1/\sqrt{1-\mathbf{v}^2/c^2}$ and $N(d\tilde{X}) = -c^2dt^2 + d\mathbf{x}^2$, following *Relativistic Mechanics in Biquaternionic Form*. This is not the quaternion square, which is $\mathbf{v}\mathbf{v} = -|\mathbf{v}|^2e_0$ and carries a sign; a reviewer must not replace the Euclidean reading with the product. -->

## The Worldline in the Material Sector

### The Position

The four-position of a particle is the element

$$
\tilde{X}(t) = ic\,t\,e_0 + x(t)\,e_1 + y(t)\,e_2 + z(t)\,e_3 \in \mathbb{M}_- ,
$$

written compactly as $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$. Its scalar coefficient is the imaginary time coordinate $ict$ and its vector part $\mathbf{x}$ is real. Both features are the definition of membership in $\mathbb{M}_-$, and both are inherited from the conventions of the framework: the temporal direction of the material sector is the imaginary scalar $ie_0$, and its spatial directions are the three real vectors $e_1, e_2, e_3$.

The norm form of the displacement between two nearby events is the invariant interval,

$$
N(d\tilde{X}) = d\tilde{X}\,\overline{d\tilde{X}} = (ic\,dt)^2 + d\mathbf{x}^2 = -c^2\,dt^2 + d\mathbf{x}^2 ,
$$

whose Lorentzian signature is a consequence of $i^2 = -1$ rather than an independent postulate. A worldline is **timelike**, **null** or **spacelike** according to whether $N(d\tilde{X})$ is negative, zero or positive along it. The null directions are the zero divisors of the algebra, and they form the light cone of the material sector.

### The Four-Velocity and the Parameter Along the Worldline

The natural parameter along a timelike worldline is the **proper time** $\tau$, defined by

$$
d\tau = \frac{dt}{\gamma}, \qquad \gamma = \frac{1}{\sqrt{1 - \mathbf{v}^2/c^2}}, \qquad \mathbf{v} = \frac{d\mathbf{x}}{dt} .
$$

The four-velocity is the derivative of the four-position with respect to proper time,

$$
\tilde{U} = \frac{d\tilde{X}}{d\tau} = \gamma\left(ic\,e_0 + \mathbf{v}\right) = ic\,\gamma\,e_0 + \gamma\mathbf{v} \in \mathbb{M}_- ,
$$

again an element of the material sector: imaginary scalar part $i\gamma c$, real vector part $\gamma\mathbf{v}$. Its norm form is fixed,

$$
\tilde{U}\overline{\tilde{U}} = \gamma^2\left(-c^2 + \mathbf{v}^2\right) = -c^2 ,
$$

which is the biquaternion form of the relativistic normalization $u^\mu u_\mu = -c^2$. The normalization is a **constraint**, not an identity: it selects the four-velocities of physical particles from among all elements of $\mathbb{M}_-$.

The four-momentum is the mass times the four-velocity,

$$
\tilde{P} = m\tilde{U} = i\frac{E}{c}\,e_0 + \mathbf{p}, \qquad E = \gamma m c^2, \qquad \mathbf{p} = \gamma m\mathbf{v},
$$

and it too lies in $\mathbb{M}_-$. Its norm form is the mass-shell relation,

$$
\tilde{P}\overline{\tilde{P}} = m^2\,\tilde{U}\overline{\tilde{U}} = -m^2 c^2 .
$$

The four-vectors of relativistic kinematics, and the constraints they satisfy, are those of the companion article *Relativistic Mechanics in Biquaternionic Form*; they are recalled here only so that the free particle can be located within them.

### The Straight Line

The free particle is defined by the vanishing of the four-force,

$$
\tilde{F} = \frac{d\tilde{P}}{d\tau} = 0 .
$$

Since $\tilde{P} = m\tilde{U}$ and $m$ is constant, this says that the four-velocity is constant, $\tilde{U} = \tilde{U}_0$, and integrating once gives the straight worldline

$$
\tilde{X}(t) = \tilde{X}_0 + \tilde{U}_0\,\tau(t), \qquad \mathbf{x}(t) = \mathbf{x}_0 + \mathbf{v}\,t ,
$$

with $\mathbf{v}$ a constant real vector. In words: the free particle moves with constant velocity along a straight line, which is Newton's first law transcribed into the algebra. The scalar part of $\tilde{X}$ carries the time, the vector part carries the uniform motion, and the two are related by the constraint that the four-velocity have norm $-c^2$.

Differentiating the constraint along the worldline expresses the orthogonality of the four-force to the four-momentum,

$$
\tilde{F}\overline{\tilde{P}} + \tilde{P}\overline{\tilde{F}} = 0 ,
$$

which is the biquaternion form of $f^\mu p_\mu = 0$. For the free particle both terms vanish separately; for a forced particle the identity says that a four-force can turn the four-momentum but cannot change its norm, and hence cannot change the rest mass.

### The Causal Character of the Free Worldline

The norm form classifies the free worldline, and the classification is preserved by every rotor conjugation. A massive free particle has $\tilde{U}\overline{\tilde{U}} = -c^2 < 0$ and traces a **timelike** straight line, staying inside the light cone of every event on it. A massless free particle has $N(\tilde{U}) = 0$ and traces a **null** straight line, lying on the cone. In the algebra the null four-velocities are precisely the zero divisors of $\mathbb{B}$: $\tilde{U}\overline{\tilde{U}} = 0$ with $\tilde{U} \neq 0$, so a massless free particle's four-velocity is a nonzero element that annihilates on the right. The null direction of a zero divisor is a genuine feature of the complexified algebra, and it is the algebraic home of the light cone rather than an added structure.

The three cases are invariant under frame changes because the rotor action preserves the norm form. A boost cannot turn a timelike worldline into a spacelike one, and it cannot create or destroy a zero divisor. The free particle's causal character is therefore a frame-independent property, which is the Minkowski statement that the interval's sign is a Lorentz invariant.

For the non-relativistic limit the classification degenerates along with the boost. Since the Galilean shear does not preserve the norm form, it does not preserve the sign of $N(\tilde{X})$; and since it leaves the scalar direction untouched, a vector that was timelike can be sheared into one whose norm form has either sign. The non-relativistic world has no light cone in the algebraic sense, only the simultaneity foliation $t = \text{const}$ that the shear respects. The cone reappears only as the limit of a sequence of cones that flatten with $c \to \infty$, which is the same degeneration seen from the other side.

## Inertial Frames as Rotors

### Frames and the Lorentz Transformation

An inertial frame is a choice of how to split the four-position into a time coordinate and a space coordinate. In the biquaternion framework such a choice is implemented by a **rotor**, that is, by a unit-norm-form biquaternion

$$
\tilde{\Lambda} \in \mathbb{B}, \qquad \tilde{\Lambda}\overline{\tilde{\Lambda}} = e_0 ,
$$

which acts on the material sector by **rotor conjugation**,

$$
\tilde{X} \;\longmapsto\; \tilde{X}' = \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger .
$$

The set of such rotors is the group $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group, and the action preserves $\mathbb{M}_-$ and the norm form: if $\tilde{X} \in \mathbb{M}_-$ then $\tilde{X}' \in \mathbb{M}_-$, and $N(\tilde{X}') = N(\tilde{X})$. The group lives in the full algebra $\mathbb{B}$ — neither sector is closed under multiplication — and it acts on the material sector, which is a module rather than an algebra.

The different Lorentz transformations have rotors in different subspaces. A **pure boost** along the unit direction $\hat{\mathbf{u}}$ has the rotor

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} \in \mathbb{M}_+ ,
$$

which is Hermitian, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$, and hence acts by $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}$. The rapidity $\psi$ is related to the frame velocity $V = V\hat{\mathbf{u}}$ by

$$
\cosh\psi = \gamma_V, \qquad \sinh\psi = \gamma_V\frac{V}{c}, \qquad \tanh\psi = \frac{V}{c}, \qquad \gamma_V = \frac{1}{\sqrt{1 - V^2/c^2}} .
$$

A **pure spatial rotation** has a rotor in the real-quaternion subalgebra,

$$
R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat{\mathbf{n}} \in \mathbb{H}_{\mathbb{B}} ,
$$

which is unitary, $R^{-1} = \overline{R} = R^\dagger$, and acts on the vector part by $R\mathbf{x}R^{-1}$, rotating $\mathbf{x}$ by the angle $\theta$ about the axis $\hat{\mathbf{n}}$. A general Lorentz transformation has its rotor in the full algebra. The classification is that of the companion article *The Lorentz Transformation as a Biquaternionic Rotation*, and the action of the real-quaternion rotors on the vector part is the same adjoint action that the companion article *The Reflection and the Rotation in Biquaternionic Form* develops.

### The Relativity Principle

The principle of relativity is the statement that the free-particle equation is form-invariant under the rotor action. If $\tilde{X}(\tau)$ is a straight worldline in one inertial frame, then $\tilde{X}'(\tau) = \tilde{\Lambda}\tilde{X}(\tau)\tilde{\Lambda}^\dagger$ is a straight worldline in another, because the action is linear and commutes with the derivative with respect to $\tau$:

$$
\frac{d\tilde{X}'}{d\tau} = \tilde{\Lambda}\frac{d\tilde{X}}{d\tau}\tilde{\Lambda}^\dagger = \tilde{\Lambda}\tilde{U}\tilde{\Lambda}^\dagger = \tilde{U}' .
$$

The four-velocity of the transformed worldline is the rotor conjugate of the original four-velocity, its norm is unchanged by the preceding section, and the mass-shell constraint therefore reads the same in every inertial frame. This is the algebraic content of the statement that the free particle cannot distinguish inertial frames: the equation $\tilde{U} = \text{const}$ is the same equation after the transformation, with the transformed constant.

The composition of frames is the composition of rotors. Two successive rotor conjugations compose as

$$
\tilde{\Lambda}_2\left(\tilde{\Lambda}_1\tilde{X}\tilde{\Lambda}_1^\dagger\right)\tilde{\Lambda}_2^\dagger = (\tilde{\Lambda}_2\tilde{\Lambda}_1)\,\tilde{X}\,(\tilde{\Lambda}_2\tilde{\Lambda}_1)^\dagger ,
$$

and the product $\tilde{\Lambda}_2\tilde{\Lambda}_1$ is again a unit-norm biquaternion, since the norm form is multiplicative. The composition of frames is therefore the group multiplication of $SL(2,\mathbb{C})$, and it is here that the double cover shows: the rotors $\tilde{\Lambda}$ and $-\tilde{\Lambda}$ implement the same Lorentz transformation, because the signs cancel in the conjugation.

## The Non-Relativistic Limit: the Boost Becomes a Shear

The free particle has a non-relativistic limit, and its transformation law has one too. The limit is instructive because the transformation does **not** remain a rotor conjugation.

### Expanding the Boost Rotor

Let the frame move with small velocity $V \ll c$ along $\hat{\mathbf{u}}$, so that the rapidity is small, $\psi \approx V/c$. Expanding the boost rotor,

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} = e_0 + \frac{iV}{2c}\,\hat{\mathbf{u}} + O\!\left(\frac{V^2}{c^2}\right) .
$$

To first order in $V/c$ the rotor is Hermitian, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$, so the action on a material vector is $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}$, and hence

$$
\tilde{X}' = \tilde{X} + \frac{iV}{2c}\left(\hat{\mathbf{u}}\tilde{X} + \tilde{X}\hat{\mathbf{u}}\right) + O\!\left(\frac{V^2}{c^2}\right) .
$$

Now let $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$. The scalar $ic\,t\,e_0$ is central, so $\hat{\mathbf{u}}$ commutes with it; the real vector $\mathbf{x}$ is a pure quaternion, so $\hat{\mathbf{u}}$ anticommutes with it. Therefore

$$
\hat{\mathbf{u}}\tilde{X} + \tilde{X}\hat{\mathbf{u}} = 2ic\,t\,\hat{\mathbf{u}} + \left(\hat{\mathbf{u}}\mathbf{x} + \mathbf{x}\hat{\mathbf{u}}\right) = 2ic\,t\,\hat{\mathbf{u}} ,
$$

and the correction is

$$
\tilde{X}' = \tilde{X} + \frac{iV}{2c}\cdot 2ic\,t\,\hat{\mathbf{u}} = \tilde{X} - Vt\,\hat{\mathbf{u}} .
$$

Reading off the components,

$$
ic\,t' = ic\,t + O\!\left(\frac{V^2}{c^2}\right), \qquad \mathbf{x}' = \mathbf{x} - \mathbf{V}\,t + O\!\left(\frac{V^2}{c^2}\right) .
$$

This is the **Galilean transformation**: the time coordinate is untouched and the position is shifted by $-\mathbf{V}t$. The exact boost transformation, of which this is the leading term, is the standard one,

$$
c\,t' = \cosh\psi\;c\,t - \sinh\psi\;x_\parallel, \qquad x_\parallel' = \cosh\psi\;x_\parallel - \sinh\psi\;c\,t, \qquad \mathbf{x}_\perp' = \mathbf{x}_\perp ,
$$

where $x_\parallel$ is the component along $\hat{\mathbf{u}}$ and $\mathbf{x}_\perp$ the perpendicular part; the Galilean form is its $V/c \to 0$ limit.

### The Shear Is Not a Rotation

The striking feature of the result is not the relation itself but what it is not. The Galilean boost is the limit of a family of rotor conjugations, but the limit is not a rotor conjugation, and this can be checked independently.

A rotor conjugation preserves the norm form, $N(\tilde{X}') = N(\tilde{X})$. The Galilean shear does not:

$$
N(\tilde{X}') = (ic\,t)^2 + (\mathbf{x} - \mathbf{V}t)^2 = N(\tilde{X}) - 2t\,\mathbf{V}\cdot\mathbf{x} + t^2\mathbf{V}^2 .
$$

The change $2t\,\mathbf{V}\cdot\mathbf{x} - t^2\mathbf{V}^2$ is nonzero for a generic worldline, so no unit-norm biquaternion implements the map. Equivalently, the shear leaves the scalar direction $ie_0$ of the material sector untouched while changing the vector directions, which is exactly what a rotation in a Minkowski plane does not do. The Galilean boost is a **shear of the material sector along its scalar direction**, and the scalar direction is the one the shear fixes.

This is the algebraic form of a familiar statement. The Galilean group is the **contraction** $c \to \infty$ of the Poincaré group, not a subgroup of it: as the invariant speed recedes, the boosts flatten into shears, the timelike and spacelike distinctions lose their sharpness, and the light cone opens into the family of simultaneity hyperplanes. In the biquaternion language the contraction is visible as the degeneration of the rotor condition: the boost rotors approach the elementary shears $e_0 + \tfrac{iV}{2c}\hat{\mathbf{u}}$, which have unit norm to first order in $V/c$ but not to second, and which act on $\mathbb{M}_-$ without preserving its norm form.

### What Survives the Contraction

Three structures survive intact, and it is worth naming them because they are the ones the non-relativistic articles use.

**The spatial rotation subgroup survives exactly.** A real-quaternion rotor is unitary and rotationally acts on the real vector part alone; it is unchanged by the contraction, and it remains a genuine conjugation in the limit. The rotations are the compact part of both groups, and the contraction touches only the non-compact part.

**The time coordinate survives as a scalar parameter.** In the limit the scalar direction $ie_0$ of $\mathbb{M}_-$ is inert: the shear fixes it, and it can be treated as a real parameter $t$ multiplying the constant $ic$. The non-relativistic world is therefore $\mathbb{R} \times \mathbb{R}^3$, realized in the algebra as $ie_0\mathbb{R} \oplus \mathrm{span}\{e_1, e_2, e_3\}$, which is exactly the material sector read as one scalar direction plus three vector directions.

**The centrality of the scalar imaginary survives.** The scalar $i$ commutes with every element at every order in $V/c$, so the central phase $e^{i\alpha}$ and the sector exchange $i\mathbb{M}_\pm = \mathbb{M}_\mp$ are untouched by the contraction. The limit is a limit of the action on $\mathbb{M}_-$, not of the algebra.

## The Free Particle as the Spin-Zero Benchmark

The free particle is the case against which the rest of this subcategory is calibrated, and its structural features are worth stating in the framework's terms, because they are what "spin zero" means here.

**The configuration is entirely material.** The four-position, four-velocity and four-momentum all lie in the anti-Hermitian sector $\mathbb{M}_-$. The informational sector $\mathbb{M}_+$ contains no part of the free particle's kinematic configuration. The vector slots $ie_1, ie_2, ie_3$ of $\mathbb{M}_+$ — the directions an internal vector degree of freedom would occupy — are empty.

**There is no internal vector.** A particle with intrinsic spin would carry an internal real vector in $\mathbb{M}_+$, of the form $i\mathbf{s}$, and the direction of that vector would be a further dynamical variable with its own precession. The free particle has no such variable. Its only vector is the external position $\mathbf{x}$, and its only dynamics is the uniform translation of that vector. The effects of the present subcategory are exactly those a **structureless point particle** shows: no intrinsic angular momentum, hence no intrinsic magnetism, and no multipole structure.

**The invariance is the Poincaré invariance.** The free particle's symmetry group is the full Poincaré group: translations of the origin, rotor conjugations of $SL(2,\mathbb{C})$, and the discrete transformations. In the algebra, the translations are shifts of $\tilde{X}$ by a constant element of $\mathbb{M}_-$ and the rotor conjugations are the action described above. The rotations and the boosts are the compact and non-compact parts of the same rotor group, and the contraction of the boosts to shears is the only part of the symmetry that fails to survive the non-relativistic limit.

It is worth recording what the framework does **not** add here. The free particle is a transcription: its trajectory, its conserved four-momentum, and its transformation law are the standard ones, and the biquaternion form predicts nothing beyond them. What the transcription isolates is the location of each object — the worldline in $\mathbb{M}_-$, the frame as a rotor in $\mathbb{B}$, the boost rotor in $\mathbb{M}_+$, the rotation rotor in $\mathbb{H}_{\mathbb{B}}$ — and the single structural fact that the Galilean limit is a contraction rather than a subgroup.

## Correspondence with the Standard Formulation

The transcription is transparent under the isomorphism $\Phi$ of the algebra with $M_2(\mathbb{C})$, and the following table collects it.

| Standard object | Biquaternion object | Location |
|---|---|---|
| Event $x^\mu = (ct, \mathbf{x})$ | $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$ | $\mathbb{M}_-$ |
| Interval $dx^\mu dx_\mu$ | $N(d\tilde{X}) = d\tilde{X}\overline{d\tilde{X}}$ | norm form on $\mathbb{M}_-$ |
| Four-velocity $u^\mu$ | $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | $\mathbb{M}_-$ |
| Mass shell $u^\mu u_\mu = -c^2$ | $\tilde{U}\overline{\tilde{U}} = -c^2$ | constraint in $\mathbb{M}_-$ |
| Four-momentum $p^\mu = (E/c, \mathbf{p})$ | $\tilde{P} = i(E/c)e_0 + \mathbf{p}$ | $\mathbb{M}_-$ |
| Four-force $f^\mu$ | $\tilde{F} = d\tilde{P}/d\tau$ | $\mathbb{M}_-$ |
| Lorentz transformation $\Lambda^\mu{}_\nu$ | rotor conjugation $\tilde{\Lambda}(\cdot)\tilde{\Lambda}^\dagger$ | rotor in $\mathbb{B}$ |
| Boost | $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | $\mathbb{M}_+$ |
| Spatial rotation | $R(\cdot)R^{-1}$ | $\mathbb{H}_{\mathbb{B}}$ |
| Galilean boost (NR limit) | $\mathbf{x} \mapsto \mathbf{x} - \mathbf{V}t$, $t \mapsto t$ | shear of $\mathbb{M}_-$ |

The table shows that the algebra makes no new prediction for the free particle. Its value is classificatory: it separates the objects that live in the material sector from the transformations that act on it, and it separates the compact rotations, which survive the non-relativistic limit exactly, from the boosts, which do not.

## Summary

The free particle in biquaternionic form is a straight timelike worldline in the material sector,

$$
\tilde{X}(t) = ic\,t\,e_0 + \mathbf{x}_0 + \mathbf{v}\,t \in \mathbb{M}_- ,
$$

with four-velocity $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ and four-momentum $\tilde{P} = m\tilde{U} = i(E/c)e_0 + \mathbf{p}$, both in $\mathbb{M}_-$, and constrained by the mass-shell relation $\tilde{P}\overline{\tilde{P}} = -m^2c^2$. The free particle satisfies $\tilde{F} = d\tilde{P}/d\tau = 0$, which is Newton's first law.

Inertial frames are the unit-norm biquaternions $\tilde{\Lambda} \in SL(2,\mathbb{C})$, acting on the material sector by rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$. The action is linear, preserves $\mathbb{M}_-$ and preserves the norm form, and it commutes with the proper-time derivative, so the free-particle equation is form-invariant: this is the relativity principle. Compositions of frames compose as rotor products.

The non-relativistic limit of a boost is a **shear**, not a rotation. Expanding the boost rotor to first order in $V/c$ gives $\tilde{\Lambda} = e_0 + \tfrac{iV}{2c}\hat{\mathbf{u}}$, and acting on $\tilde{X} = ict\,e_0 + \mathbf{x}$ produces the Galilean transformation $\mathbf{x}' = \mathbf{x} - \mathbf{V}t$, $t' = t$. The shear does not preserve the norm form, $N(\tilde{X}') = N(\tilde{X}) - 2t\,\mathbf{V}\cdot\mathbf{x} + t^2\mathbf{V}^2$, so no unit-norm biquaternion implements it. The Galilean group is therefore a contraction of the rotor group, not a subgroup: the rotations survive exactly, the time coordinate becomes an inert scalar parameter, and the centrality of $i$ is untouched.

The free particle occupies only the material sector, carries no internal vector, and is the spin-zero benchmark for the subcategory: its effects are those of a structureless point particle, with no intrinsic angular momentum and hence no intrinsic magnetism.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2 = -e_0$ |
| $\mathbb{M}_-$ | Anti-Hermitian (material) sector: $iq_0e_0 + \mathbf{q}$, $\mathbf{q}$ real |
| $\mathbb{M}_+$ | Hermitian (informational) sector: $h_0e_0 + i\mathbf{h}$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subalgebra (rotation rotors) |
| $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$ | Four-position, a curve in $\mathbb{M}_-$ |
| $\tau$, $\gamma$ | Proper time; Lorentz factor $1/\sqrt{1-\mathbf{v}^2/c^2}$ |
| $\mathbf{v}$, $\mathbf{V}$ | Particle velocity; frame velocity |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity, in $\mathbb{M}_-$; $\tilde{U}\overline{\tilde{U}} = -c^2$ |
| $\tilde{P} = m\tilde{U} = i(E/c)e_0 + \mathbf{p}$ | Four-momentum; $\tilde{P}\overline{\tilde{P}} = -m^2c^2$ |
| $\tilde{F} = d\tilde{P}/d\tau$ | Four-force; $\tilde{F} = 0$ for the free particle |
| $\tilde{\Lambda} \in \mathbb{B}$, $\tilde{\Lambda}\overline{\tilde{\Lambda}} = e_0$ | Lorentz rotor; frame transformation |
| $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation (frame change) |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost rotor, in $\mathbb{M}_+$; $\tanh\psi = V/c$ |
| $R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$ | Rotation rotor, in $\mathbb{H}_{\mathbb{B}}$ |
| $N(\tilde{X}) = \tilde{X}\overline{\tilde{X}}$ | Norm form; invariant interval on $\mathbb{M}_-$ |
| $\mathbf{x}' = \mathbf{x} - \mathbf{V}t$ | Galilean shear (non-relativistic limit) |
| $SL(2,\mathbb{C})$ | Unit-norm biquaternions, the Lorentz group |

## Further Reading

- Isaac Newton, *Philosophiae Naturalis Principia Mathematica* (1687), for the first law and the notion of an inertial frame.
- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the special theory of relativity and the relativity principle.
- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional worldline formulation.
- E. T. Whittaker, *A History of the Theories of Aether and Electricity* (Nelson, 1951), for the Galilean and Lorentz transformation groups and the contraction.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard relativistic kinematics and the four-velocity constraint.
- Jean-Marc Lévy-Leblond, "Galilei group and Galilean invariance," in *Group Theory and its Applications, Vol. II* (Academic Press, 1971), for the Galilean group as a contraction of the Poincaré group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even Clifford algebra and its rotor group.
