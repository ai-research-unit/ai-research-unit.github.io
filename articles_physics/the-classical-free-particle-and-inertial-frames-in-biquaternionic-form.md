# __The Classical Free Particle and Inertial Frames in Biquaternionic Form__

## Introduction

The free particle is the simplest mechanical system, and it is the system on which the notion of an inertial frame is built. Newton's first law says that a particle subject to no force moves with constant velocity; a frame in which that statement holds is inertial; and the principle of relativity says that no inertial frame is preferred. The content of the law is therefore as much about the frames as about the particle.

In the biquaternion framework the worldline of a point particle is a curve in the **material sector** $\mathbb{B}_{\Phi}$, the anti-Hermitian subspace of $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. The position of the particle is the biquaternion

$$
\tilde R_\Phi(r'_t) = i r'_{t}\,e_t + r_x(r'_t)\,\vec e_x+r_y(r'_t)\,\vec e_y+r_z(r'_t)\,\vec e_z,
$$

with $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ a real pure quaternion. The free particle is the case in which this curve is a straight timelike line, and the four-velocity is a constant element of $\mathbb{B}_{\Phi}$.

This article writes the free particle and the inertial-frame structure in that language. The material is standard — the four-velocity, the four-momentum, the mass-shell constraint, and the Lorentz transformation are those of the companion articles — and the article's interest is structural. Two facts are worth extracting in advance.

1. **The free particle is entirely in the material sector.** Its position, velocity and momentum lie in $\mathbb{B}_{\Phi}$, and no vector direction of the informational sector $\mathbb{B}_{\Psi}$ is occupied. This is what makes the free particle the **spin-zero benchmark** of the present subcategory: a structureless point particle has no internal vector that could precess, and the entire content of the mechanics is the material worldline.
2. **The non-relativistic limit of a Lorentz boost is not a rotation but a shear.** Expanding the boost rotor in the ratio of the frame velocity to the speed of light gives, to first order, the Galilean transformation $(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) \mapsto (r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - \tfrac{\vec V}{c}\,r'_t$ with the time untouched. That map does not preserve the biquaternion norm, so it is not a rotor conjugation, and the Galilean group is therefore not a subgroup of the biquaternion rotor group. It is a **contraction** of it. The contraction is what the non-relativistic limit costs algebraically, and it is visible directly in the algebra.

The conventions are those of the read list. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_\eta^2 = -e_t$ and $\vec e_j \vec e_\eta = \epsilon_{j\eta l}\vec e_l$ for $j \neq k$; the scalar imaginary $i$ is central with $i^2 = -e_t$. The anti-Hermitian subspace $\mathbb{B}_{\Phi}$ consists of $i r'_t e_t + \vec r_\Phi$ with $r'_t \in \mathbb{R}$ and $\vec r_\Phi$ a real pure quaternion, and the Hermitian subspace $\mathbb{B}_{\Psi}$ of $r_t e_t + i\vec r_\Psi$ with $r_t, \vec r_\Psi$ real. They are complementary, $\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi}$, and exchanged by the scalar imaginary, $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$. The real-quaternion subalgebra is $\mathbb{B}_{H}$, the centre is $\mathbb{B}_{C} = \mathrm{span}_\mathbb{R}\{e_t, ie_t\}$, and the trace satisfies $\mathrm{Tr}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})=2\,\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})$ for $\tilde{H}_{\Psi,1},\tilde{H}_{\Psi,2} \in \mathbb{B}_{\Psi}$. The symbol $c$ denotes the speed of light in the medium, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ the vacuum speed of light; in vacuum $c = c_0$. The symbol $\vec v$ is reserved for particle velocities and $\vec V$ for frame velocities.

## The Worldline in the Material Sector

### The Position

The four-position of a particle is the element

$$
\tilde R_\Phi(r'_t) = i r'_{t}\,e_t + r_x(r'_t)\,\vec e_x + r_y(r'_t)\,\vec e_y + r_z(r'_t)\,\vec e_z \in \mathbb{B}_{\Phi} ,
$$

written compactly as $\tilde R_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$. Its scalar coefficient is the imaginary time coordinate $i r'_t$ and its vector part $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ is real. Both features are the definition of membership in $\mathbb{B}_{\Phi}$, and both are inherited from the conventions of the framework: the temporal direction of the material sector is the imaginary scalar $ie_t$, and its spatial directions are the three real vectors $\vec e_x, \vec e_y, \vec e_z$.

The biquaternion norm of the displacement between two nearby events is the invariant interval,

$$
\langle d\tilde R_\Phi\rangle_{\natural} = d\tilde R_\Phi\,(d\tilde R_\Phi)^{\natural} = (i\,dr'_t)^2 +dr_x^2+dr_y^2+dr_z^2 = -d{r'_{t}}^2 +dr_x^2+dr_y^2+dr_z^2 ,
$$

whose Lorentzian signature is a consequence of $i^2 = -1$ rather than an independent postulate. A worldline is **timelike**, **null** or **spacelike** according to whether $\langle d\tilde R_\Phi\rangle_{\natural}$ is negative, zero or positive along it. The null directions are the zero divisors of the algebra, and they form the light cone of the material sector.

### The Four-Velocity and the Parameter Along the Worldline

The natural parameter along a timelike worldline is the **proper time** $\tau$, defined by

$$
d\tau = \frac{dr'_t}{c\,\gamma}, \qquad \gamma = \frac{1}{\sqrt{1 - \vec v^2/c^2}}, \qquad \vec v = c\,\frac{d(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)}{dr'_t} .
$$

The four-velocity is the derivative of the four-position with respect to proper time,

$$
\tilde{V}_{\Phi} = \frac{d\tilde R_\Phi}{d\tau} = \gamma\left(ic\,e_t + \vec v\right) = ic\,\gamma\,e_t + \gamma\vec v \in \mathbb{B}_{\Phi} ,
$$

again an element of the material sector: imaginary scalar part $i\gamma c$, real vector part $\gamma\vec v$. Its biquaternion norm is fixed,

$$
\boxed{\;\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = \gamma^2\left(-c^2 + \vec v^2\right) = -c^2\;},
$$

which is the biquaternion form of the relativistic normalization $\sum_\mu\varepsilon_\mu v_\mu v_\mu = -c^2$. The normalization is a **constraint**, not an identity: it selects the four-velocities of physical particles from among all elements of $\mathbb{B}_{\Phi}$.

The four-momentum is the mass times the four-velocity,

$$
\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = i\frac{E}{c}\,e_t + \vec p, \qquad E = \gamma m c^2, \qquad \vec p = \gamma m\vec v,
$$

and it too lies in $\mathbb{B}_{\Phi}$. Its biquaternion norm is the mass-shell relation,

$$
\boxed{\;\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = m^2\,\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -m^2 c^2\;}.
$$

The four-vectors of relativistic kinematics, and the constraints they satisfy, are those of the companion article *Relativistic Mechanics in Biquaternionic Form*; they are recalled here only so that the free particle can be located within them.

### The Straight Line

The free particle is defined by the vanishing of the four-force,

$$
\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = \frac{d\tilde{P}_{\Phi}}{d\tau} = 0 .
$$

Since $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi}$ and $m$ is constant, this says that the four-velocity is constant, $\tilde{V}_{\Phi} = \tilde{V}_{\Phi,0}$, and integrating once gives the straight worldline

$$
\tilde R_\Phi(r'_t) = \tilde{R}_{\Phi,0} + \tilde{V}_{\Phi,0}\,\tau(r'_t), \qquad (r_x(r'_t)\,\vec e_x+r_y(r'_t)\,\vec e_y+r_z(r'_t)\,\vec e_z) = r_{0x}\,\vec e_x+r_{0y}\,\vec e_y+r_{0z}\,\vec e_z + \vec v\,r'_t ,
$$

with $\vec v$ a constant real vector. In words: the free particle moves with constant velocity along a straight line, which is Newton's first law transcribed into the algebra. The scalar part of $\tilde R_\Phi$ carries the time, the vector part carries the uniform motion, and the two are related by the constraint that the four-velocity have norm $-c^2$.

Differentiating the constraint along the worldline expresses the orthogonality of the four-force to the four-momentum,

$$
\tilde{\mathcal F}_{\Phi,\mathrm{frc}}\,\tilde{P}_{\Phi}^{\natural} + \tilde{P}_{\Phi}\,\tilde{\mathcal F}_{\Phi,\mathrm{frc}}^{\natural} = 0 ,
$$

which is the biquaternion form of $\sum_\mu\varepsilon_\mu f_\mu p_\mu = 0$. For the free particle both terms vanish separately; for a forced particle the identity says that a four-force can turn the four-momentum but cannot change its norm, and hence cannot change the rest mass.

### The Causal Character of the Free Worldline

The biquaternion norm classifies the free worldline, and the classification is preserved by every rotor conjugation. A massive free particle has $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -c^2 < 0$ and traces a **timelike** straight line, staying inside the light cone of every event on it. A massless free particle has $\langle\tilde{V}_{\Phi}\rangle_{\natural} = 0$ and traces a **null** straight line, lying on the cone. In the algebra the null four-velocities are precisely the zero divisors of $\mathbb{B}$: $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = 0$ with $\tilde{V}_{\Phi} \neq 0$, so a massless free particle's four-velocity is a nonzero element that annihilates on the right. The null direction of a zero divisor is a genuine feature of the complexified algebra, and it is the algebraic home of the light cone rather than an added structure.

The three cases are invariant under frame changes because the rotor action preserves the biquaternion norm. A boost cannot turn a timelike worldline into a spacelike one, and it cannot create or destroy a zero divisor. The free particle's causal character is therefore a frame-independent property, which is the Minkowski statement that the interval's sign is a Lorentz invariant.

For the non-relativistic limit the classification degenerates along with the boost. Since the Galilean shear does not preserve the biquaternion norm, it does not preserve the sign of $\langle\tilde R_\Phi\rangle_{\natural}$; and since it leaves the scalar direction untouched, a vector that was timelike can be sheared into one whose biquaternion norm has either sign. The non-relativistic world has no light cone in the algebraic sense, only the simultaneity foliation $r'_t = \text{const}$ that the shear respects. The cone reappears only as the limit of a sequence of cones that flatten with $c \to \infty$, which is the same degeneration seen from the other side.

## Inertial Frames as Rotors

### Frames and the Lorentz Transformation

An inertial frame is a choice of how to split the four-position into a time coordinate and a space coordinate. In the biquaternion framework such a choice is implemented by a **rotor**, that is, by the Lorentz rotor $\tilde U_{\mathrm{lor}}=\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, a unit-norm biquaternion

$$
\tilde U_{\mathrm{lor}} \in \mathbb{B}, \qquad \tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural} = e_t ,
$$

which acts on the material sector by **rotor conjugation**,

$$
\tilde R_\Phi \;\longmapsto\; \tilde{R}_{\Phi,2} = \tilde U_{\mathrm{lor}}\,\tilde R_\Phi\,\tilde U_{\mathrm{lor}}{}^{*} .
$$

The set of such rotors is the group $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group, and the action preserves $\mathbb{B}_{\Phi}$ and the biquaternion norm: if $\tilde R_\Phi \in \mathbb{B}_{\Phi}$ then $\tilde{R}_{\Phi,2} \in \mathbb{B}_{\Phi}$, and $\langle\tilde{R}_{\Phi,2}\rangle_{\natural} = \langle\tilde R_\Phi\rangle_{\natural}$. The group lives in the full algebra $\mathbb{B}$ — neither sector is closed under multiplication — and it acts on the material sector, which is a module rather than an algebra.

The different Lorentz transformations have rotors in different subspaces. A **pure boost** along the unit direction $\vec u_{\mathrm b}$ has the rotor

$$
\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b} \in \mathbb{B}_{\Psi} ,
$$

which is Hermitian, $\tilde U_{\Psi,\mathrm b}^{*} = \tilde U_{\Psi,\mathrm b}$, and hence acts by $\tilde R_\Phi \mapsto \tilde U_{\Psi,\mathrm b}\tilde R_\Phi\tilde U_{\Psi,\mathrm b}$. The rapidity $\theta_{\mathrm{rpd}}$ is related to the frame velocity $V = V\vec u_{\mathrm b}$ by

$$
\cosh\theta_{\mathrm{rpd}} = \gamma_V, \qquad \sinh\theta_{\mathrm{rpd}} = \gamma_V\frac{V}{c}, \qquad \tanh\theta_{\mathrm{rpd}} = \frac{V}{c}, \qquad \gamma_V = \frac{1}{\sqrt{1 - V^2/c^2}} .
$$

A **pure spatial rotation** has a rotor in the real-quaternion subalgebra,

$$
R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\vec u_{\mathrm r} \in \mathbb{B}_{H} ,
$$

which is $*$-unitary, $R^{-1} = R^{\natural} = R^{*}$, and acts on the vector part by $R(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)R^{*}$, rotating $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ by the angle $\theta$ about the axis $\vec u_{\mathrm r}$. A general Lorentz transformation has its rotor in the full algebra. The classification is that of the companion article *The Lorentz Transformation as a Biquaternionic Rotation*, and the action of the real-quaternion rotors on the vector part is the same adjoint action that the companion article *The Reflection and the Rotation in Biquaternionic Form* develops.

### The Relativity Principle

The principle of relativity is the statement that the free-particle equation is form-invariant under the rotor action. If $\tilde R_\Phi(\tau)$ is a straight worldline in one inertial frame, then $\tilde{R}_{\Phi,2}(\tau) = \tilde U_{\mathrm{lor}}\tilde R_\Phi(\tau)\tilde U_{\mathrm{lor}}{}^{*}$ is a straight worldline in another, because the action is linear and commutes with the derivative with respect to $\tau$:

$$
\frac{d\tilde{R}_{\Phi,2}}{d\tau} = \tilde U_{\mathrm{lor}}\frac{d\tilde R_\Phi}{d\tau}\tilde U_{\mathrm{lor}}{}^{*} = \tilde U_{\mathrm{lor}}\tilde{V}_{\Phi}\tilde U_{\mathrm{lor}}{}^{*} = \tilde{V}_{\Phi,2} .
$$

The four-velocity of the transformed worldline is the rotor conjugate of the original four-velocity, its norm is unchanged by the preceding section, and the mass-shell constraint therefore reads the same in every inertial frame. This is the algebraic content of the statement that the free particle cannot distinguish inertial frames: the equation $\tilde{V}_{\Phi} = \text{const}$ is the same equation after the transformation, with the transformed constant.

The composition of frames is the composition of rotors. Two successive rotor conjugations compose as

$$
\tilde U_2\left(\tilde U_1\tilde R_\Phi\tilde U_1^{*}\right)\tilde U_2^{*} = (\tilde U_2\tilde U_1)\,\tilde R_\Phi\,(\tilde U_2\tilde U_1)^{*} ,
$$

and the product $\tilde U_2\tilde U_1$ is again a unit-norm biquaternion, since the biquaternion norm is multiplicative. The composition of frames is therefore the group multiplication of $SL(2,\mathbb{C})$, and it is here that the double cover shows: the rotors $\tilde U_{\mathrm{lor}}$ and $-\tilde U_{\mathrm{lor}}$ implement the same Lorentz transformation, because the signs cancel in the conjugation.

## The Non-Relativistic Limit: the Boost Becomes a Shear

The free particle has a non-relativistic limit, and its transformation law has one too. The limit is instructive because the transformation does **not** remain a rotor conjugation.

### Expanding the Boost Rotor

Let the frame move with small velocity $V \ll c$ along $\vec u_{\mathrm b}$, so that the rapidity is small, $\theta_{\mathrm{rpd}} \approx V/c$. Expanding the boost rotor,

$$
\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b} = e_t + \frac{iV}{2c}\,\vec u_{\mathrm b} + O\!\left(\frac{V^2}{c^2}\right) .
$$

To first order in $V/c$ the rotor is Hermitian, $\tilde U_{\Psi,\mathrm b}^{*} = \tilde U_{\Psi,\mathrm b}$, so the action on a material vector is $\tilde R_\Phi \mapsto \tilde U_{\Psi,\mathrm b}\tilde R_\Phi\tilde U_{\Psi,\mathrm b}$, and hence

$$
\tilde{R}_{\Phi,2} = \tilde R_\Phi + \frac{iV}{2c}\left(\vec u_{\mathrm b}\tilde R_\Phi + \tilde R_\Phi\vec u_{\mathrm b}\right) + O\!\left(\frac{V^2}{c^2}\right) .
$$

Now let $\tilde R_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$. The scalar $i r'_{t}\,e_t$ is central, so $\vec u_{\mathrm b}$ commutes with it; the real vector $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ is a pure quaternion, so $\vec u_{\mathrm b}$ anticommutes with it. Therefore

$$
\vec u_{\mathrm b}\tilde R_\Phi + \tilde R_\Phi\vec u_{\mathrm b} = 2i r'_{t}\,\vec u_{\mathrm b} + \left(\vec u_{\mathrm b}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) + (r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\vec u_{\mathrm b}\right) = 2i r'_{t}\,\vec u_{\mathrm b} ,
$$

and the correction is

$$
\tilde{R}_{\Phi,2} = \tilde R_\Phi + \frac{iV}{2c}\cdot 2i r'_{t}\,\vec u_{\mathrm b} = \tilde R_\Phi - \frac{V}{c}r'_t\,\vec u_{\mathrm b} .
$$

Reading off the components,

$$
\boxed{\;i r'_{t}_2 = i r'_{t} + O\!\left(\frac{V^2}{c^2}\right), \qquad (r_{2x}\,\vec e_x+r_{2y}\,\vec e_y+r_{2z}\,\vec e_z) = r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z - \tfrac{\vec V}{c}\,r'_t + O\!\left(\frac{V^2}{c^2}\right)\;}.
$$

This is the **Galilean transformation**: the time coordinate is untouched and the position is shifted by $-\tfrac{\vec V}{c}r'_t$, the shear angle being the boost parameter $\vec V/c$. The exact boost transformation, of which this is the leading term, is the standard one,

$$
r'_{t,2} = \cosh\theta_{\mathrm{rpd}}\;r'_t - \sinh\theta_{\mathrm{rpd}}\;x_\parallel, \qquad x_{\parallel,2} = \cosh\theta_{\mathrm{rpd}}\;x_\parallel - \sinh\theta_{\mathrm{rpd}}\;r'_t, \qquad (r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)_{\perp,2} = (r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)_\perp ,
$$

where $x_\parallel$ is the component along $\vec u_{\mathrm b}$ and $(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)_\perp$ the perpendicular part; the Galilean form is its $V/c \to 0$ limit.

### The Shear Is Not a Rotation

The striking feature of the result is not the relation itself but what it is not. The Galilean boost is the limit of a family of rotor conjugations, but the limit is not a rotor conjugation, and this can be checked independently.

A rotor conjugation preserves the biquaternion norm, $\langle\tilde{R}_{\Phi,2}\rangle_{\natural} = \langle\tilde R_\Phi\rangle_{\natural}$. The Galilean shear does not:

$$
\boxed{\;\langle\tilde{R}_{\Phi,2}\rangle_{\natural} = (i r'_{t})^2 + |r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z - \tfrac{\vec V}{c}r'_t|^2 = \langle\tilde R_\Phi\rangle_{\natural} - 2\tfrac{r'_t}{c}\,\vec V\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) + {r'_{t}}^2\tfrac{\vec V^2}{c^2}\;}.
$$

The change $2\tfrac{r'_t}{c}\,\vec V\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - {r'_{t}}^2\tfrac{\vec V^2}{c^2}$ is nonzero for a generic worldline, so no unit-norm biquaternion implements the map. Equivalently, the shear leaves the scalar direction $ie_t$ of the material sector untouched while changing the vector directions, which is exactly what a rotation in a Minkowski plane does not do. The Galilean boost is a **shear of the material sector along its scalar direction**, and the scalar direction is the one the shear fixes.

This is the algebraic form of a familiar statement. The Galilean group is the **contraction** $c \to \infty$ of the Poincaré group, not a subgroup of it: as the invariant speed recedes, the boosts flatten into shears, the timelike and spacelike distinctions lose their sharpness, and the light cone opens into the family of simultaneity hyperplanes. In the biquaternion language the contraction is visible as the degeneration of the rotor condition: the boost rotors approach the elementary shears $e_t + \tfrac{iV}{2c}\vec u_{\mathrm b}$, which have unit norm to first order in $V/c$ but not to second, and which act on $\mathbb{B}_{\Phi}$ without preserving its biquaternion norm.

### What Survives the Contraction

Three structures survive intact, and it is worth naming them because they are the ones the non-relativistic articles use.

**The spatial rotation subgroup survives exactly.** A real-quaternion rotor is $*$-unitary and rotationally acts on the real vector part alone; it is unchanged by the contraction, and it remains a genuine conjugation in the limit. The rotations are the compact part of both groups, and the contraction touches only the non-compact part.

**The time coordinate survives as a scalar parameter.** In the limit the scalar direction $ie_t$ of $\mathbb{B}_{\Phi}$ is inert: the shear fixes it, and it can be treated as a real parameter $r'_t$ multiplying the constant $ic$. The non-relativistic world is therefore $\mathbb{R} \times \mathbb{R}^3$, realized in the algebra as $ie_t\mathbb{R} \oplus \mathrm{span}\{\vec e_x, \vec e_y, \vec e_z\}$, which is exactly the material sector read as one scalar direction plus three vector directions.

**The centrality of the scalar imaginary survives.** The scalar $i$ commutes with every element at every order in $V/c$, so the central phase $\exp(i\alpha)$ and the sector exchange $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$ are untouched by the contraction. The limit is a limit of the action on $\mathbb{B}_{\Phi}$, not of the algebra.

## The Free Particle as the Spin-Zero Benchmark

The free particle is the case against which the rest of this subcategory is calibrated, and its structural features are worth stating in the framework's terms, because they are what "spin zero" means here.

**The configuration is entirely material.** The four-position, four-velocity and four-momentum all lie in the anti-Hermitian sector $\mathbb{B}_{\Phi}$. The informational sector $\mathbb{B}_{\Psi}$ contains no part of the free particle's kinematic configuration. The vector slots $i\vec e_x, i\vec e_y, i\vec e_z$ of $\mathbb{B}_{\Psi}$ — the directions an internal vector degree of freedom would occupy — are empty.

**There is no internal vector.** A particle with intrinsic spin would carry an internal real vector in $\mathbb{B}_{\Psi}$, of the form $i\vec s$, and the direction of that vector would be a further dynamical variable with its own precession. The free particle has no such variable. Its only vector is the external position $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, and its only dynamics is the uniform translation of that vector. The effects of the present subcategory are exactly those a **structureless point particle** shows: no intrinsic angular momentum, hence no intrinsic magnetism, and no multipole structure.

**The invariance is the Poincaré invariance.** The free particle's symmetry group is the full Poincaré group: translations of the origin, rotor conjugations of $SL(2,\mathbb{C})$, and the discrete transformations. In the algebra, the translations are shifts of $\tilde R_\Phi$ by a constant element of $\mathbb{B}_{\Phi}$ and the rotor conjugations are the action described above. The rotations and the boosts are the compact and non-compact parts of the same rotor group, and the contraction of the boosts to shears is the only part of the symmetry that fails to survive the non-relativistic limit.

It is worth recording what the framework does **not** add here. The free particle is a transcription: its trajectory, its conserved four-momentum, and its transformation law are the standard ones, and the biquaternion form predicts nothing beyond them. What the transcription isolates is the location of each object — the worldline in $\mathbb{B}_{\Phi}$, the frame as a rotor in $\mathbb{B}$, the boost rotor in $\mathbb{B}_{\Psi}$, the rotation rotor in $\mathbb{B}_{H}$ — and the single structural fact that the Galilean limit is a contraction rather than a subgroup.

## Correspondence with the Standard Formulation

The transcription is transparent under the isomorphism $\mathsf{M}_2$ of the algebra with $M_2(\mathbb{C})$, and the following table collects it.

| Standard object | Biquaternion object | Location |
|---|---|---|
| Event $x_\mu = (r'_{t}, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ | $\tilde R_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | $\mathbb{B}_{\Phi}$ |
| Interval $\sum_\mu\varepsilon_\mu dx_\mu dx_\mu$ | $\langle d\tilde R_\Phi\rangle_{\natural} = d\tilde R_\Phi(d\tilde R_\Phi)^{\natural}$ | biquaternion norm on $\mathbb{B}_{\Phi}$ |
| Four-velocity $v_\mu$ | $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | $\mathbb{B}_{\Phi}$ |
| Mass shell $\sum_\mu\varepsilon_\mu v_\mu v_\mu = -c^2$ | $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -c^2$ | constraint in $\mathbb{B}_{\Phi}$ |
| Four-momentum $p_\mu = (E/c, \vec p)$ | $\tilde{P}_{\Phi} = i(E/c)e_t + \vec p$ | $\mathbb{B}_{\Phi}$ |
| Four-force $f_\mu$ | $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$ | $\mathbb{B}_{\Phi}$ |
| Lorentz transformation $\Lambda_{\mu\nu}$ | rotor conjugation $\tilde U_{\mathrm{lor}}(\cdot)\tilde U_{\mathrm{lor}}{}^{*}$ | rotor in $\mathbb{B}$ |
| Boost | $\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | $\mathbb{B}_{\Psi}$ |
| Spatial rotation | $R(\cdot)R^{*}$ | $\mathbb{B}_{H}$ |
| Galilean boost (NR limit) | $(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) \mapsto (r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - \tfrac{\vec V}{c}r'_t$, $r'_t \mapsto r'_t$ | shear of $\mathbb{B}_{\Phi}$ |

The table shows that the algebra makes no new prediction for the free particle. Its value is classificatory: it separates the objects that live in the material sector from the transformations that act on it, and it separates the compact rotations, which survive the non-relativistic limit exactly, from the boosts, which do not.

## Summary

The free particle in biquaternionic form is a straight timelike worldline in the material sector,

$$
\tilde R_\Phi(r'_t) = i r'_{t}\,e_t + r_{0x}\,\vec e_x+r_{0y}\,\vec e_y+r_{0z}\,\vec e_z + \vec v\,r'_t \in \mathbb{B}_{\Phi} ,
$$

with four-velocity $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ and four-momentum $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = i(E/c)e_t + \vec p$, both in $\mathbb{B}_{\Phi}$, and constrained by the mass-shell relation $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^2c^2$. The free particle satisfies $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau = 0$, which is Newton's first law.

Inertial frames are the unit-norm biquaternions $\tilde U_{\mathrm{lor}} \in SL(2,\mathbb{C})$, acting on the material sector by rotor conjugation $\tilde R_\Phi \mapsto \tilde U_{\mathrm{lor}}\tilde R_\Phi\tilde U_{\mathrm{lor}}{}^{*}$. The action is linear, preserves $\mathbb{B}_{\Phi}$ and preserves the biquaternion norm, and it commutes with the proper-time derivative, so the free-particle equation is form-invariant: this is the relativity principle. Compositions of frames compose as rotor products.

The non-relativistic limit of a boost is a **shear**, not a rotation. Expanding the boost rotor to first order in $V/c$ gives $\tilde U_{\Psi,\mathrm b} = e_t + \tfrac{iV}{2c}\vec u_{\mathrm b}$, and acting on $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ produces the Galilean transformation $r_{2x}\,\vec e_x+r_{2y}\,\vec e_y+r_{2z}\,\vec e_z - \tfrac{\vec V}{c}r'_t$, $r'_{t,2} = r'_t$. The shear does not preserve the biquaternion norm, $\langle\tilde{R}_{\Phi,2}\rangle_{\natural} = \langle\tilde R_\Phi\rangle_{\natural} - 2\tfrac{r'_t}{c}\,\vec V\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) + {r'_{t}}^2\tfrac{\vec V^2}{c^2}$, so no unit-norm biquaternion implements it. The Galilean group is therefore a contraction of the rotor group, not a subgroup: the rotations survive exactly, the time coordinate becomes an inert scalar parameter, and the centrality of $i$ is untouched.

The free particle occupies only the material sector, carries no internal vector, and is the spin-zero benchmark for the subcategory: its effects are those of a structureless point particle, with no intrinsic angular momentum and hence no intrinsic magnetism.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\eta^2 = -e_t$, $\vec e_j \vec e_\eta = \epsilon_{j\eta l}\vec e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2 = -e_t$ |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian (material) sector: $i r'_t e_t + \vec r_\Phi$, $\vec r_\Phi$ real |
| $\mathbb{B}_{\Psi}$ | Hermitian (informational) sector: $r_t\,e_t + i\vec r_\Psi$ |
| $\mathbb{B}_{H}$ | Real-quaternion subalgebra (rotation rotors) |
| $\tilde R_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position, a curve in $\mathbb{B}_{\Phi}$ |
| $\tau$, $\gamma$ | Proper time; Lorentz factor $1/\sqrt{1-\vec v^2/c^2}$ |
| $\vec v$, $\vec V$ | Particle velocity; frame velocity |
| $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | Four-velocity, in $\mathbb{B}_{\Phi}$; $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -c^2$ |
| $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = i(E/c)e_t + \vec p$ | Four-momentum; $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^2c^2$ |
| $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$ | Four-force; $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = 0$ for the free particle |
| $\tilde U_{\mathrm{lor}} \in \mathbb{B}$, $\tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}{}^{\natural} = e_t$ | Lorentz rotor; frame transformation |
| $\tilde R_\Phi \mapsto \tilde U_{\mathrm{lor}}\tilde R_\Phi\tilde U_{\mathrm{lor}}{}^{*}$ | Rotor conjugation (frame change) |
| $\tilde U_{\Psi,\mathrm b} = \cosh\frac{\theta_{\mathrm{rpd}}}{2} + i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | Boost rotor, in $\mathbb{B}_{\Psi}$; $\tanh\theta_{\mathrm{rpd}} = V/c$ |
| $R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\vec u_{\mathrm r}$ | Rotation rotor, in $\mathbb{B}_{H}$ |
| $\langle\tilde R_\Phi\rangle_{\natural} = \tilde R_\Phi\tilde{R}_\Phi^{\natural}$ | Biquaternion norm; invariant interval on $\mathbb{B}_{\Phi}$ |
| $r_{2x}\,\vec e_x+r_{2y}\,\vec e_y+r_{2z}\,\vec e_z - \tfrac{\vec V}{c}r'_t$ | Galilean shear (non-relativistic limit) |
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
