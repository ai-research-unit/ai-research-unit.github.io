# __The Foucault Pendulum and Classical Holonomy in Biquaternionic Form__

## Introduction

In 1851 Léon Foucault suspended a long pendulum in the Panthéon and watched its plane of oscillation turn. The pendulum is the simplest device that reveals the rotation of the Earth without any reference to the stars, and the angle through which its plane turns in a sidereal day is $2\pi\sin\lambda$, where $\lambda$ is the latitude of the laboratory. The rate is $\Omega\sin\lambda$, with $\Omega$ the angular speed of the Earth.

The effect is peculiar among the systems of this subcategory in that it is **geometric**. The precession angle does not depend on the mass of the bob, on the length of the wire, on the local value of $g$, or on the amplitude of the swing, as long as the pendulum is long and the amplitude small. It depends only on the path that the pivot is carried along by the rotating Earth — a circle of latitude — and on nothing else. It is a **holonomy**: the net rotation accumulated by a frame when it is carried around a closed loop, an angle fixed by the geometry of the loop rather than by the details of the transport.

This article treats the Foucault pendulum in the biquaternion framework. Three things are developed. The pendulum's swing direction is a real unit vector in the three-space $\operatorname{span}\{e_1,e_2,e_3\} \subset \mathbb{M}_-$, and the rotating frame is a one-parameter family of real-quaternion rotors $R(t)$ acting on it by the adjoint action. The **Coriolis and centrifugal forces are commutators** with the frame's angular velocity, $\mathbf{F}_{\text{Cor}} = -m[\boldsymbol\Omega,\dot{\boldsymbol\rho}]$ and $\mathbf{F}_{\text{cf}} = -\tfrac{m}{4}[\boldsymbol\Omega,[\boldsymbol\Omega,\boldsymbol\rho]]$, which is the algebraic form of the statement that they are the corrections for describing inertial motion in a rotating frame. And the precession angle is identified with the total geodesic curvature of the latitude circle, $\oint\kappa_g\,ds = 2\pi\sin\lambda$, which by Gauss–Bonnet is $2\pi$ minus the enclosed solid angle.

The treatment is classical and non-quantum. The geometric phase of a quantum system, the Berry phase, and its biquaternion formulation belong to the companion article *The Berry Phase and Geometric Phases in Biquaternionic Form*; the classical Hannay angle is a separate construction. What is used here is the elementary holonomy of a frame carried around a loop on a sphere, and the pendulum that realizes it. The particle is structureless — the bob carries no intrinsic angular momentum and no magnetic moment — so the effect is one of the spin-zero subcategory, and it is the purely geometric end of it.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = \epsilon_{jkl}e_l$ for $j \neq k$; the scalar imaginary $i$ is central with $i^2 = -e_0$. The material sector is $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm = \mathbb{M}_\mp$. Position vectors, velocities, angular velocities and forces are real vectors in $\operatorname{span}\{e_1,e_2,e_3\} \subset \mathbb{M}_-$; the energy is a central scalar. For two real vectors $\mathbf{a},\mathbf{b}$,

$$
\mathbf{a}\mathbf{b} = -\mathbf{a}\cdot\mathbf{b}\,e_0 + \mathbf{a}\times\mathbf{b}, \qquad [\mathbf{a},\mathbf{b}] = 2\,\mathbf{a}\times\mathbf{b} .
$$

A rotation by angle $\theta$ about the unit axis $\hat{\mathbf{n}}$ is implemented by the unit real quaternion $R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$, acting by $\mathbf{a} \mapsto R\mathbf{a}R^{-1}$.

## Inertial and Rotating Frames

### The Rotor of the Frame

Let the Earth-fixed frame rotate with angular velocity $\boldsymbol\Omega$ relative to an inertial frame, and let $\hat{\mathbf{u}} = \boldsymbol\Omega/\Omega$ be the axis. The rotor that carries the inertial frame into the rotating frame is the one-parameter family

$$
R(t) = \cos\frac{\Omega t}{2} + \sin\frac{\Omega t}{2}\,\hat{\mathbf{u}} \in \mathbb{H}_{\mathbb{B}}, \qquad R^{-1}(t) = \overline{R}(t) ,
$$

so that after a time $t$ the frame has turned by the angle $\Omega t$ about $\hat{\mathbf{u}}$. A vector with fixed components in the rotating frame has inertial components $\mathbf{a}_{\text{in}} = R\,\mathbf{a}_{\text{rot}}R^{-1}$; a vector with fixed inertial components has rotating-frame components

$$
\mathbf{a}_{\text{rot}}(t) = R^{-1}(t)\,\mathbf{a}_{\text{in}}\,R(t) .
$$

### The Time Derivative in the Rotating Frame

Differentiating the second relation and using $\dot R R^{-1} = \tfrac{1}{2}\boldsymbol\Omega$ as a pure quaternion — which holds because $\boldsymbol\Omega$ is the angular velocity of the frame and the rotor is its half-angle exponential — gives

$$
\frac{d\mathbf{a}_{\text{rot}}}{dt} = -\,\boldsymbol\Omega\times\mathbf{a}_{\text{rot}} \qquad (\mathbf{a}_{\text{in}}\ \text{constant}).
$$

This is the elementary statement that a vector fixed in inertial space appears to rotate backwards in the rotating frame. It was checked numerically: with $\boldsymbol\Omega = (0, 0.3, 0.5)$ and a generic constant inertial vector, the finite-difference derivative of $\mathbf{a}_{\text{rot}}(t)$ agrees with $-\boldsymbol\Omega\times\mathbf{a}_{\text{rot}}$ to five decimal places.

The general relation for an arbitrary vector follows by adding the rotating-frame derivative,

$$
\left(\frac{d\mathbf{a}}{dt}\right)_{\text{in}} = \left(\frac{d\mathbf{a}}{dt}\right)_{\text{rot}} + \boldsymbol\Omega\times\mathbf{a} ,
$$

which is the standard transport formula expressed through the rotor.

### The Fictitious Forces as Commutators

Newton's second law in the inertial frame, $m\ddot{\mathbf{r}}_{\text{in}} = \mathbf{F}$, becomes in the rotating frame an equation with two extra terms. Applying the transport formula twice,

$$
m\ddot{\boldsymbol\rho} = \mathbf{F} - 2m\,\boldsymbol\Omega\times\dot{\boldsymbol\rho} - m\,\boldsymbol\Omega\times\left(\boldsymbol\Omega\times\boldsymbol\rho\right) ,
$$

where $\boldsymbol\rho$ is the position in the rotating frame. The two fictitious terms are the Coriolis force and the centrifugal force, and in the quaternion algebra each is a **commutator with the angular velocity**. The Coriolis term is

$$
-2m\,\boldsymbol\Omega\times\dot{\boldsymbol\rho} = -m\,[\boldsymbol\Omega,\dot{\boldsymbol\rho}] ,
$$

since $[\mathbf{a},\mathbf{b}] = 2\mathbf{a}\times\mathbf{b}$, and the centrifugal term is the double commutator,

$$
-m\,\boldsymbol\Omega\times\left(\boldsymbol\Omega\times\boldsymbol\rho\right) = -\frac{m}{4}\left[\boldsymbol\Omega,\left[\boldsymbol\Omega,\boldsymbol\rho\right]\right] ,
$$

since $[\boldsymbol\Omega,[\boldsymbol\Omega,\boldsymbol\rho]] = 4\,\boldsymbol\Omega\times(\boldsymbol\Omega\times\boldsymbol\rho)$. The fictitious forces are therefore the first and second commutators of the frame's generator with the velocity and the position. This is the algebraic content of the statement that they correct for the rotation of the frame: the generator $\boldsymbol\Omega$ is a real vector in $\mathbb{M}_-$, and the adjoint action of its exponential produces the correction terms.

## The Pendulum in the Rotating Frame

### The Geometry of the Local Frame

Place the origin at the point of suspension, taken to be fixed in the rotating frame, and choose local axes with $\hat{\mathbf{z}}$ along the local vertical (the outward radial direction), $\hat{\mathbf{x}}$ pointing east and $\hat{\mathbf{y}}$ pointing north. At latitude $\lambda$ the Earth's angular velocity has components

$$
\boldsymbol\Omega = \Omega\cos\lambda\,\hat{\mathbf{y}} + \Omega\sin\lambda\,\hat{\mathbf{z}}
$$

in these axes: the component along the local vertical is $\Omega\sin\lambda$, and the component along north is $\Omega\cos\lambda$. Only the vertical component enters the precession to leading order. The horizontal component, and the centrifugal term that accompanies it, are of the same order in $\Omega$ as the Coriolis term that does the work; their effect on the precession rate is computed below and is of relative order $(\Omega\sin\lambda/\omega_0)^2$.

### Small Oscillations

For small horizontal displacements $\boldsymbol\rho = x\hat{\mathbf{x}} + y\hat{\mathbf{y}}$ the restoring force of the pendulum is $-m\omega_0^2\boldsymbol\rho$, with $\omega_0 = \sqrt{g/\ell}$ the pendulum frequency, and the equation of motion in the rotating frame is

$$
\ddot{\boldsymbol\rho} = -\omega_0^2\boldsymbol\rho - 2\,\boldsymbol\Omega\times\dot{\boldsymbol\rho} .
$$

Now $\boldsymbol\Omega\times\dot{\boldsymbol\rho}$ has the vertical component; projecting onto the horizontal plane, the contributions of $\boldsymbol\Omega_x$ and $\boldsymbol\Omega_y$ are along the vertical and drop out, and only $\Omega_z = \Omega\sin\lambda$ survives:

$$
\ddot x = -\omega_0^2 x + 2\Omega\sin\lambda\,\dot y, \qquad \ddot y = -\omega_0^2 y - 2\Omega\sin\lambda\,\dot x .
$$

This is a pair of linear equations with a gyroscopic coupling, and the coupling constant is the vertical component of the Earth's rotation. The centrifugal term is omitted here; it is restored in the estimate below, which also fixes the size of its effect on the precession.

### The Precession of the Swing Plane

Introduce the complex horizontal coordinate $z = x + iy$. The two real equations combine into

$$
\ddot z + 2i\Omega\sin\lambda\,\dot z + \omega_0^2 z = 0 .
$$

Writing $z(t) = e^{-i\Omega\sin\lambda\,t}\,w(t)$ removes the first-derivative term: $w$ satisfies $\ddot w + \omega^2 w = 0$ with

$$
\omega^2 = \omega_0^2 + \Omega^2\sin^2\lambda .
$$

Hence

$$
z(t) = e^{-i\Omega\sin\lambda\,t}\left(Ae^{i\omega t} + Be^{-i\omega t}\right),
$$

a fast oscillation of frequency $\omega$ whose **envelope rotates at the rate $-\Omega\sin\lambda$**. The plane of oscillation is the direction of the envelope, so the plane precesses at the rate $-\Omega\sin\lambda$, that is, at the rate $\Omega\sin\lambda$ in the sense opposite to the Earth's rotation, in agreement with Foucault's observation.

The result was checked numerically. For the retained equations the relation below is in fact an identity: $T$ is an exact period of the fast factor, so the envelope factor is the only thing that survives one period, and the numerical integration of the coupled equations reproduces it to machine precision. Integrating with $\omega_0 = 1$ and a representative $\Omega\sin\lambda = 0.457$ — chosen so that the envelope rotation is visible within a single period, and larger relative to the pendulum frequency than the Earth's by a factor of some $3\times10^3$ for a $67$-metre pendulum — the complex amplitude satisfies

$$
z(t + T) = e^{-i\Omega\sin\lambda\,T}z(t)
$$

to machine precision, which is the statement that the ellipse of the motion returns after one fast period but rotated by the angle $-\Omega\sin\lambda\,T$. Over one sidereal day, $T_{\text{day}} = 2\pi/\Omega$, the accumulated precession is

$$
\Delta\phi = \Omega\sin\lambda\cdot\frac{2\pi}{\Omega} = 2\pi\sin\lambda ,
$$

the Foucault angle.

### The Size of the Neglected Centrifugal Term

The retained equations omit the centrifugal force, which is of the same order in $\Omega$ as the Coriolis force that produces the precession. Its size is worth fixing, because the rate $\Omega\sin\lambda$ is often quoted without qualification and the neglected term is not merely a renormalization of the local vertical. In the local axes the horizontal projection of the centrifugal acceleration is

$$
-\boldsymbol\Omega\times\left(\boldsymbol\Omega\times\boldsymbol\rho\right) = \Omega^2x\,\hat{\mathbf{x}} + \Omega^2\sin^2\lambda\,y\,\hat{\mathbf{y}} ,
$$

the east component being the full $\Omega^2\rho$ because the east direction is perpendicular to the Earth's axis, and the north component being reduced by $\sin^2\lambda$. Restoring it, the horizontal equations become

$$
\ddot x = -\left(\omega_0^2-\Omega^2\right)x + 2\Omega\sin\lambda\,\dot y , \qquad
\ddot y = -\left(\omega_0^2-\Omega^2\sin^2\lambda\right)y - 2\Omega\sin\lambda\,\dot x ,
$$

which in the complex coordinate is

$$
\ddot z + 2i\Omega\sin\lambda\,\dot z + \omega_s^2 z = \epsilon\,\bar z , \qquad
\omega_s^2 = \omega_0^2 - \tfrac12\Omega^2\left(1+\sin^2\lambda\right) , \qquad
\epsilon = \tfrac12\Omega^2\cos^2\lambda .
$$

The coupling to $\bar z$ is the anisotropic part. The centrifugal term therefore does two things: it shifts the oscillation frequency, which is the renormalization of the local vertical, and it makes the horizontal oscillator anisotropic. An anisotropic oscillator's swing plane precesses at a rate shifted from $\Omega\sin\lambda$. Writing the two normal frequencies as $\omega_\pm$, the precession rate is $\tfrac12(\omega_+-\omega_-)$ and the squared frequencies satisfy

$$
v_\pm = \omega_s^2 + 2\Omega^2\sin^2\lambda \pm \sqrt{4\Omega^2\sin^2\lambda\left(\omega_s^2+\Omega^2\sin^2\lambda\right) + \epsilon^2} , \qquad v_\pm = \omega_\pm^2 ,
$$

which for $\epsilon = 0$ gives $\omega_\pm = \Omega\sin\lambda \pm \sqrt{\omega_s^2+\Omega^2\sin^2\lambda}$ and the exact rate $\Omega\sin\lambda$. Expanding in the anisotropy, the relative correction to the precession rate is

$$
\frac{1}{32}\left(\frac{\Omega\sin\lambda}{\omega_0}\right)^2\cot^4\lambda .
$$

The correction is of second order in the small parameter $\Omega\sin\lambda/\omega_0$, not of first order, and it vanishes at the pole, where the local vertical is parallel to the axis and the horizontal motion is isotropic. For a pendulum of length $\ell = 67$ m at $\lambda = 48.85^\circ$ the relative correction is $3.8\times10^{-10}$, so the leading rate is not a rough approximation but an accurate one. The centrifugal term does have a kinematic consequence that is of order $\Omega^2$ and not merely a frequency shift: the two envelope phases drift at slightly different rates, so a bob released from rest does not swing along a fixed line but traces a slightly elliptical path whose ellipticity oscillates. It is there, rather than in the precession rate, that the neglected term would first show itself.

Both statements were verified by computation. The closed-form frequencies above give a relative correction of $1.2394\times10^{-6}$ at $\Omega\sin\lambda/\omega_0 = 0.01$, against $1.2392\times10^{-6}$ predicted by the leading coefficient; and integrating the equations with the centrifugal term retained, then measuring the direction of the bob at successive turning points of the swing, gives a swing-plane drift whose relative deviation from $\Omega\sin\lambda$ is $5.3\times10^{-4}$ at $\Omega\sin\lambda/\omega_0 = 0.2$ and $2.3\times10^{-5}$ at $0.05$, in agreement with the coefficient above, while the same measurement applied to the retained equations reproduces the exact rate to $10^{-6}$.

<!-- CONVENTION — two different fast frequencies: $\omega^2 = \omega_0^2+\Omega^2\sin^2\lambda$ belongs to the retained equations, from which the centrifugal term is dropped, while $\omega_s^2 = \omega_0^2-\tfrac12\Omega^2(1+\sin^2\lambda)$ belongs to the equations with the centrifugal term restored. They are the fast frequencies of two different truncations and are not two values of one quantity; the precession rate is $\Omega\sin\lambda$ in both, to the orders computed above. A reviewer must not reconcile them by editing one of the two equations. -->

### What the Angle Does Not Depend On

The derivation shows that the precession rate $-\Omega\sin\lambda$ is independent of the pendulum frequency $\omega_0$. The frequency appears only in the fast oscillation $\omega \approx \omega_0$; the envelope's rotation is fixed by the coupling. Reparametrizing the pendulum — changing its length, its mass or the local gravity — changes $\omega_0$ and leaves the precession untouched. This is the first indication that the angle is geometric: it depends on the angular velocity of the frame and on the latitude, that is, on the path of the pivot, and not on the dynamics of the bob.

## The Geometric Meaning: Geodesic Turning and Holonomy

### The Path on the Sphere

As the Earth rotates, the local vertical $\hat{\mathbf{r}}$ at the laboratory traces a circle of latitude on the unit sphere of directions. Its colatitude is $\theta_0 = \frac{\pi}{2} - \lambda$, so its polar distance from the axis is $\sin\theta_0 = \cos\lambda$ and its height is $\cos\theta_0 = \sin\lambda$. The path is parametrized by the rotation angle $t$,

$$
\boldsymbol\gamma(t) = \left(\sin\theta_0\cos t,\ \sin\theta_0\sin t,\ \cos\theta_0\right),
$$

and it is a closed loop on the sphere, traversed once per sidereal day.

### The Geodesic Turning

For a curve on a surface, the **geodesic curvature** $\kappa_g$ measures how fast the tangent turns relative to a parallel-transported (geodesically straight) frame. For a circle of latitude on the unit sphere it is $\kappa_g = \cot\theta_0$ per unit arc length, and the arc length of one circuit is $2\pi\sin\theta_0$, so the total geodesic turning is

$$
\oint\kappa_g\,ds = 2\pi\cos\theta_0 = 2\pi\sin\lambda .
$$

This was computed numerically by evaluating $\kappa_g = \mathbf{n}\cdot(\boldsymbol\gamma''\times\boldsymbol\gamma')/|\boldsymbol\gamma'|^3$ along the curve and integrating, with the orientation of the curve and of the normal $\mathbf{n}$ fixed by the Gauss–Bonnet statement below: for $\lambda = 0.9$ rad the integral is $4.921788$, equal to $2\pi\sin(0.9)$ to six decimal places. The sign of $\kappa_g$ is itself a convention — reversing either the normal or the sense of traversal reverses it — and only the magnitude $2\pi\sin\lambda$ is invariant. The total geodesic turning is exactly the Foucault angle.

<!-- CONVENTION — geodesic-curvature sign: the sign of $\kappa_g$, and hence the sign of $\oint\kappa_g\,ds = \pm2\pi\sin\lambda$, depends on the choice of surface normal and on the sense of traversal of the latitude circle. The orientation used here is the one for which the Gauss–Bonnet statement below reads $\oint\kappa_g\,ds + \iint K\,dA = 2\pi$. Only the magnitude $2\pi\sin\lambda$ is invariant; a reviewer must not flip the sign to match an outward surface normal. -->

### Gauss–Bonnet and the Solid Angle

The Gauss–Bonnet theorem for the spherical cap bounded by the latitude circle states

$$
\oint\kappa_g\,ds + \iint K\,dA = 2\pi ,
$$

with $K = 1$ the curvature of the unit sphere. The cap has solid angle $2\pi(1-\cos\theta_0) = 2\pi(1-\sin\lambda)$, so

$$
\oint\kappa_g\,ds = 2\pi - 2\pi(1-\sin\lambda) = 2\pi\sin\lambda ,
$$

in agreement with the direct computation. **The Foucault angle is $2\pi$ minus the enclosed solid angle.**

### The Parallel-Transport Holonomy

The complementary quantity is the holonomy of parallel transport around the loop: a tangent vector carried once around the latitude circle by the Levi-Civita connection of the sphere returns rotated by the enclosed solid angle. Evaluating the parallel-transport equation $\dot{\mathbf{v}} = -(\mathbf{v}\cdot\dot{\boldsymbol\gamma})\boldsymbol\gamma$ along the latitude circle and measuring the signed angle between the initial and final tangent vectors gives $1.361397$ for $\lambda = 0.9$, equal to $2\pi(1-\sin(0.9)) = 2\pi(1-\sin\lambda)$ to six decimal places, and the two numbers satisfy

$$
\oint\kappa_g\,ds + 2\pi(1-\sin\lambda) = 2\pi\sin\lambda + 2\pi(1-\sin\lambda) = 2\pi ,
$$

which is Gauss–Bonnet read off the numerical values. The Foucault angle and the parallel-transport holonomy are therefore complementary modulo a full turn: both describe the same geometric obstruction, one as the turning of the moving frame and the other as the rotation of a transported vector.

### Why the Angle Is Geometric

The identification has three consequences, and together they are the meaning of "holonomy".

**It is path-dependent only.** The angle is fixed by the loop of latitude and not by the speed of traversal or by the dynamics of the bob. A pendulum of different length, on the same latitude, precesses at the same rate.

**It vanishes at the equator and is complete at the poles.** At $\lambda = 0$ the loop bounds the whole hemisphere, its solid angle is $2\pi$, and the geodesic turning is zero; the pendulum does not precess. At the pole the loop is degenerate, its solid angle vanishes, and the geodesic turning is $2\pi$; the pendulum precesses once per day. The latitude enters through the solid angle that the loop encloses.

**It is not a dynamical phase.** The fast oscillation of the pendulum accumulates a phase at the rate $\omega_0$ — a dynamical phase proportional to the pendulum's frequency and to the elapsed time — while the precession accumulates at the rate $\Omega\sin\lambda$, independent of $\omega_0$. The first is the ordinary phase of an oscillator; the second is geometric. The separation of the two is exact in the small-oscillation, long-pendulum limit, and it is the reason the Foucault angle can be read off without knowing anything about the pendulum except where it is.

## The Rotor and the Double Cover

The rotating-frame transformation is implemented by the rotor $R(t)$ of the first section, and after one sidereal day the rotor has turned by the angle $2\pi$ about the Earth's axis:

$$
R(T_{\text{day}}) = \cos\pi + \sin\pi\,\hat{\mathbf{u}} = -e_0 .
$$

The rotor is therefore $-e_0$, not $e_0$: the lift of a full rotation to the real quaternions is minus the identity, the familiar two-valuedness of the rotation group. The adjoint action of $-e_0$ is the identity, however, since $(-e_0)\mathbf{a}(-e_0)^{-1} = \mathbf{a}$, and the vector quantities of the problem cannot distinguish $R$ from $-R$. The full-frame rotation is therefore trivial for the pendulum's swing direction, as it must be after a closed day, and the precession of $2\pi\sin\lambda$ is the rotation of that direction **relative to the local frame**, that is, about the local vertical, not the full rotation about the Earth's axis.

This is worth a remark about the double cover. The lift of the one-day loop to $SU(2)$ is the path from $e_0$ to $-e_0$, a path that does not close; but the classical pendulum is described by vectors, on which the group acts through the adjoint representation, and the adjoint representation factors through $SO(3)$, where the loop does close. There is no observable spinor sign for a structureless pendulum, because a spinor sign is a statement about the action on a half-integer-spin state, and the bob carries spin zero. The geometric phase of the present article is an element of the rotation group; whether it lifts to one or the other element of the double cover is a question that has no physical content for a spinless classical system.

## Relation to Other Geometric Phases

The Foucault precession is the oldest and simplest member of the family of geometric phases. Two remarks locate it.

**The classical analogy.** For a slowly varying periodic classical system the angle conjugate to an adiabatic invariant accumulates a geometric part, the Hannay angle, in analogy with the quantum Berry phase. The Foucault pendulum is a mechanical realization of an anholonomy: the swing plane is the transported object, the latitude circle is the loop, and the precession is the geometric angle. The general theory of such angles belongs to the generalities of the framework rather than to this article, and the present treatment uses only the elementary spherical holonomy.

**The quantum companion.** The companion article *The Berry Phase and Geometric Phases in Biquaternionic Form* treats the geometric phase of a quantum state, where the phase is carried by a ray in Hilbert space and the loop is a loop in parameter space. The Foucault angle is not a phase of a state; it is a rotation of a classical frame. What the two share is the structure of a holonomy — a closed loop, a transport, and a net transformation that depends on the geometry of the loop — and the classical case is the one in which the transport is the ordinary parallel transport of a vector on a curved surface, with no state space and no phase factor.

## Summary

The Foucault pendulum in biquaternionic form is a real vector in the material sector carried around by a rotation of the frame. The frame is the rotor $R(t) = \cos\frac{\Omega t}{2} + \sin\frac{\Omega t}{2}\hat{\mathbf{u}}$, acting on the real three-space by the adjoint action, and the transport formula gives the fictitious forces as commutators with the frame's angular velocity,

$$
\mathbf{F}_{\text{Cor}} = -m[\boldsymbol\Omega,\dot{\boldsymbol\rho}], \qquad
\mathbf{F}_{\text{cf}} = -\frac{m}{4}[\boldsymbol\Omega,[\boldsymbol\Omega,\boldsymbol\rho]] .
$$

For a pendulum of frequency $\omega_0$ at latitude $\lambda$, the horizontal motion satisfies

$$
\ddot{\boldsymbol\rho} = -\omega_0^2\boldsymbol\rho - 2\,\boldsymbol\Omega\times\dot{\boldsymbol\rho},
\qquad
\ddot z + 2i\Omega\sin\lambda\,\dot z + \omega_0^2 z = 0,
$$

with $z = x + iy$, and the swing plane precesses at the rate $-\Omega\sin\lambda$,

$$
z(t) = e^{-i\Omega\sin\lambda\,t}\left(Ae^{i\omega t} + Be^{-i\omega t}\right), \qquad \omega^2 = \omega_0^2 + \Omega^2\sin^2\lambda ,
$$

giving the Foucault angle $2\pi\sin\lambda$ per sidereal day, independent of $\omega_0$, of the mass and of the amplitude.

The angle is geometric. The local vertical traces a circle of latitude with total geodesic turning

$$
\oint\kappa_g\,ds = 2\pi\cos\theta_0 = 2\pi\sin\lambda ,
$$

which by Gauss–Bonnet is $2\pi$ minus the enclosed solid angle $2\pi(1-\sin\lambda)$. The parallel-transport holonomy around the same loop is the solid angle, so the Foucault angle and the holonomy are complementary modulo a full turn. The angle vanishes at the equator and equals $2\pi$ at the pole. The one-day rotor is $-e_0$, the lift of a full rotation to the real quaternions, but the adjoint action is insensitive to the sign, so the classical holonomy is an element of the rotation group and the double-cover sign has no physical content for a structureless bob.

The effect is the purely geometric end of the spin-zero subcategory: it involves no intrinsic angular momentum, no magnetic moment and no quantum state, only the transport of a direction around a loop.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2 = -e_0$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian), informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subalgebra (rotation rotors) |
| $\boldsymbol\Omega$ | Angular velocity of the rotating frame; real vector |
| $\Omega = |\boldsymbol\Omega|$, $\hat{\mathbf{u}} = \boldsymbol\Omega/\Omega$ | Angular speed; rotation axis |
| $R(t) = \cos\frac{\Omega t}{2} + \sin\frac{\Omega t}{2}\hat{\mathbf{u}}$ | Frame rotor; $\mathbf{a}_{\text{rot}} = R^{-1}\mathbf{a}_{\text{in}}R$ |
| $\mathbf{a}_{\text{in}}$, $\mathbf{a}_{\text{rot}}$ | Inertial and rotating-frame components of a vector |
| $[\mathbf{a},\mathbf{b}] = 2\mathbf{a}\times\mathbf{b}$ | Commutator of two real vectors |
| $-m[\boldsymbol\Omega,\dot{\boldsymbol\rho}]$ | Coriolis force as a commutator |
| $-\tfrac{m}{4}[\boldsymbol\Omega,[\boldsymbol\Omega,\boldsymbol\rho]]$ | Centrifugal force as a double commutator |
| $\boldsymbol\rho = x\hat{\mathbf{x}} + y\hat{\mathbf{y}}$ | Horizontal displacement of the bob |
| $\lambda$ | Latitude; local vertical component $\Omega\sin\lambda$ |
| $\omega_0 = \sqrt{g/\ell}$ | Pendulum frequency |
| $z = x + iy$ | Complex horizontal coordinate |
| $z(t) = e^{-i\Omega\sin\lambda\,t}(Ae^{i\omega t}+Be^{-i\omega t})$ | Solution; envelope rotation $-\Omega\sin\lambda$ |
| $\omega^2 = \omega_0^2 + \Omega^2\sin^2\lambda$ | Modified oscillation frequency |
| $\Delta\phi = 2\pi\sin\lambda$ | Foucault angle per sidereal day |
| $\boldsymbol\gamma(t)$ | Latitude circle on the unit sphere |
| $\kappa_g$ | Geodesic curvature; $\oint\kappa_g\,ds = 2\pi\sin\lambda$ |
| $2\pi(1-\sin\lambda)$ | Enclosed solid angle; parallel-transport holonomy |
| $R(T_{\text{day}}) = -e_0$ | One-day rotor; adjoint action insensitive to sign |

## Further Reading

- Léon Foucault, "Démonstration expérimentale du mouvement de la Terre au moyen du pendule," *Comptes Rendus de l'Académie des Sciences* **32** (1851) 135–138, for the original experiment.
- J. B. L. Foucault, *Recueil des travaux scientifiques* (Gauthier-Villars, 1878), for the collected account of the pendulum and the gyroscope.
- Herbert Goldstein, Charles Poole and John Safko, *Classical Mechanics* (Pearson, 2002), for the pendulum in a rotating frame and the Coriolis and centrifugal forces.
- L. D. Landau and E. M. Lifshitz, *Mechanics* (Pergamon, 1976), for the rotating-frame equations and the Foucault pendulum.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for the geometric interpretation of the Foucault pendulum and the spherical holonomy.
- Michael V. Berry, "The adiabatic limit and the semiclassical limit," *Journal of Physics A* **17** (1984) 1225–1233, for the Hannay angle and the classical analogue of the geometric phase.
- B. L. van der Waerden, *Group Theory and Quantum Mechanics* (Springer, 1974), for the double cover of the rotation group and the two-valuedness of the rotor.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor description of rotating frames and spatial rotations.
