# __Hannay's Angles and the Classical Geometric Phase in Biquaternionic Form__

## Introduction

A classical system whose parameters are cycled slowly acquires, besides the phase it would have from its own dynamics, an extra angle that depends only on the cycle. This is **Hannay's angle**, found by Hannay in 1985 as the classical counterpart of Berry's adiabatic phase. The setting is a Hamiltonian written in action-angle variables, $H(\theta,I;R)$, in which $R$ is a set of parameters that vary slowly and return to their starting values. The action $I$ is an adiabatic invariant; the angle $\theta$ advances with the instantaneous frequency and, after a closed cycle of $R$, carries an additional shift that is a functional of the cycle alone. Hannay's angle is the **classical geometric phase**.

This article develops the subject in the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. The algebra enters through the simplest nontrivial adiabatic classical system, the classical spin on its coadjoint orbit. Its state is a real pure quaternion $\tilde S$ with $N(\tilde S)=\mathbf S^2$, its dynamics is the rotor flow of the companion articles, and the adiabatic transport of the spin direction defines a rotor whose **holonomy** is the Hannay angle. The rotor description makes the geometry of the effect explicit:

1. The spin direction is the image of a fixed axis under a rotor, $\hat{\mathbf n}=\tilde Re_3\bar{\tilde R}$.
2. Adiabatic following chooses a rotor field over the sphere of directions; the Hannay angle is minus the accumulated twist of that rotor about the direction, equivalently the holonomy of the transport.
3. For a cycle of direction that subtends a solid angle $\Omega$, the twist accumulates to $-\Omega$ and the Hannay angle is $\Omega$; the spinor holonomy is half of it, by the double cover.

The article is classical. The relation to the quantum Berry phase is used as the standard statement $-\partial\gamma/\partial I$ relating the two phases, and the Berry phase itself is not developed; the companion article on the Berry phase owns the quantum side. No state space, no measurement, and no commutator appear.

The conventions are those of the read list. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; $i$ is central, $i^2=-1$; $\mathbb{M}_-$ and $\mathbb{M}_+$ are the anti-Hermitian and Hermitian sectors; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace. The rotor is $\tilde R\in\mathbb{H}_{\mathbb{B}}$ with $N(\tilde R)=e_0$, acting by $\tilde X\mapsto\tilde R\tilde X\bar{\tilde R}$; the body-frame angular velocity is $\tilde\omega_b=+2\bar{\tilde R}\dot{\tilde R}$, the logarithmic derivative that makes the body axes turn by $d\tilde e_k/dt=\boldsymbol\omega\times\tilde e_k$ in the corpus rotation convention. The coadjoint orbit of the spin is the level set $N(\tilde S)=S^2$ of the norm form, with the Poisson bracket $\{S_i,S_j\}=\varepsilon_{ijk}S_k$.

The companion articles are:
- Companion article *Rigid-Body Dynamics and the Biquaternion Rotor*, for the rotor, the angular velocity, and the Euler-angle parametrisation.
- Companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*, for the rotor flow and the coadjoint orbit.
- Companion article *The Berry Phase and Geometric Phases in Biquaternionic Form*, for the quantum counterpart and the connection on the state space.
- Companion article *The Symplectic Form and the Biquaternion Norm-Form Cone*, for the orbit as a level set of the norm form and the Souriau form.

## The Adiabatic Theorem and Action-Angle Variables

Let a system have action-angle variables $(\theta,I)=(\theta_1,\dots,\theta_n;I_1,\dots,I_n)$, with $\theta$ periodic and $I$ the canonical conjugate, and let its Hamiltonian depend on a set of parameters $R$,

$$
H=H_0(\theta,I;R).
$$

The **frequency** of the $k$-th angle is

$$
\omega_k(I,R)=\frac{\partial H_0}{\partial I_k},
$$

and Hamilton's equations are

$$
\dot I_k=-\frac{\partial H_0}{\partial\theta_k},\qquad \dot\theta_k=\omega_k(I,R).
$$

Now let the parameters vary slowly and periodically: $R=R(\epsilon t)$ with $\epsilon\ll1$ and $R(T)=R(0)$ after a period $T$. For a time-independent $H_0$, $I$ is exactly conserved; for slowly varying parameters, the **adiabatic theorem for classical systems** states that $I$ is conserved to all orders in $\epsilon$, and the angle evolves as

$$
\theta_k(t)=\theta_k(0)+\int_0^t\omega_k\!\left(I,R(\epsilon t')\right)dt'+\Delta\theta_k .
$$

The first two terms are dynamical: they are the phase accumulated at the instantaneous frequency. The third term is the **Hannay angle**. It is independent of the speed of the cycle to leading order, depends only on the geometric cycle of $R$, and is the classical geometric phase. Its general expression, derived by Hannay and confirmed in the examples, is

$$
\boxed{\;\Delta\theta_k=-\frac{\partial}{\partial I_k}\oint\mathcal A_\mu(R)\,dR^\mu\;}
$$

where $\mathcal A_\mu$ is the **Berry connection** of the quantum system obtained by quantising the same classical problem, and $\gamma=\oint\mathcal A_\mu dR^\mu$ is the Berry phase. Hannay's angle is thus the derivative of the Berry phase with respect to the action. This is the precise sense in which the classical geometric phase is the classical counterpart of the quantum one: the quantum phase is the action-integral of the classical angle.

The wording is worth making precise. The configuration space is that of the parameters $R$; the Berry connection is a one-form on it, and its integral around the cycle is the phase. The derivative with respect to the action produces the classical angle. For a system with several angles, the derivative is with respect to the corresponding action, and the Hannay angle of each angle is the corresponding component of the gradient.

## The Derivation in Outline

The derivation of Hannay's formula is standard, and the following sketch records its structure; the original papers supply the details.

Write the slow parameter motion explicitly, $R=R(\epsilon t)$, and expand the angle and action in powers of $\epsilon$:

$$
\theta=\theta^{(0)}+\epsilon\,\theta^{(1)}+\cdots,\qquad
I=I^{(0)}+\epsilon\,I^{(1)}+\cdots .
$$

At order $\epsilon^0$, $\dot\theta^{(0)}=\omega(I^{(0)},R)$ and $I^{(0)}$ is constant: the adiabatic invariant. The correction $I^{(1)}$ is determined by integrating $-\partial H_0/\partial\theta$ along the fast motion, averaged over the fast angle. Substituting $R(\epsilon t)$ and expanding $\omega(I,R)$ about $I^{(0)}$, so that $\omega=\omega(I^{(0)},R)+\epsilon\,(\partial\omega/\partial I)\,I^{(1)}+\cdots$, the first-order angle obeys

$$
\frac{d\theta^{(1)}}{dt}=\frac{\partial\omega}{\partial I}\,I^{(1)}+\cdots,
$$

with the sum over the components of $I$, and its average over the cycle produces the Hannay angle. The result is the one stated: the integral around the cycle of the connection, differentiated with respect to the action. Two features of the derivation are worth emphasising. First, the angle is a geometric object because the leading contribution is a closed line integral in parameter space; a change of the speed of the cycle changes the dynamical part $\int\omega\,dt$ but not the closed integral. Second, the same connection appears in the quantum problem, which is why the classical angle is the action-derivative of the quantum phase; the derivation can be carried out either from the classical adiabatic perturbation theory or from the stationary-phase evaluation of the quantum propagator, and the two agree.

For the special case in which the parameter space is a sphere of directions and the Hamiltonian is linear in the spin, the derivation can be made completely explicit, and the next sections do so in the rotor language.

## The Biquaternion Setting: Orbit and Rotor

### The Coadjoint Orbit

The classical spin is a point of the coadjoint orbit of the rotation group. In the algebra it is a real pure quaternion

$$
\tilde S\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-,\qquad N(\tilde S)=\mathbf S^2=S^2 ,
$$

and the orbit is the level set $N(\tilde S)=S^2$, a sphere of radius $S$. The symplectic form is the Souriau form of the companion article, and the Poisson bracket is $\{S_i,S_j\}=\varepsilon_{ijk}S_k$. A Hamiltonian linear in the spin,

$$
H=\boldsymbol\omega\cdot\mathbf S=\tfrac12\,\mathrm{Sc}\!\left(\bar{\tilde\omega}\,\tilde S+\bar{\tilde S}\,\tilde\omega\right),
$$

generates the flow

$$
\dot{\tilde S}=\boldsymbol\omega\times\mathbf S ,
$$

the rigid rotation of the spin about the axis $\boldsymbol\omega$ at frequency $|\boldsymbol\omega|$. This is the rotor flow: for $H=2\mathbf G\cdot\mathbf S$ with $\mathbf G$ the generator, the flow is $\tilde S\mapsto e^{t\tilde G}\tilde S e^{-t\tilde G}$, and the angular velocity of the spin is $\boldsymbol\omega$.

### The Slow Parameter and the Rotor

Let the field direction vary slowly: $\boldsymbol\omega(t)=\omega_0\hat{\mathbf n}(\epsilon t)$ with $|\boldsymbol\omega|=\omega_0$ constant and $\epsilon\ll1$. The spin follows the direction adiabatically, and the direction defines a rotor field

$$
\hat{\mathbf n}=\tilde R\,e_3\,\bar{\tilde R},\qquad \tilde R\in\mathbb{H}_{\mathbb{B}},\quad N(\tilde R)=e_0 ,
$$

defined up to the rotations about $e_3$ (the one-parameter subgroup generated by $e_3$). This freedom is exactly the freedom of a frame about the direction, and the Hannay angle is the statement of how it is fixed by the adiabatic transport.

The **adiabatic (geodesic) rotor** is the rotor that carries $e_3$ to $\hat{\mathbf n}$ by the shortest rotation, the one of least angle; the remaining freedom of rotating about $\hat{\mathbf n}$ is fixed by that requirement, and the residual turn about the direction relative to parallel transport is what the Hannay angle measures. For a direction of polar angle $\theta_0$ and azimuth $\phi$,

$$
\tilde R_g=\cos\frac{\theta_0}{2}+\sin\frac{\theta_0}{2}\,\hat{\mathbf m},
\qquad
\hat{\mathbf m}=\frac{e_3\times\hat{\mathbf n}}{\sin\theta_0}=-\sin\phi\,e_1+\cos\phi\,e_2 ,
$$

which satisfies $\tilde R_ge_3\bar{\tilde R}_g=\hat{\mathbf n}$ directly.

## The Rotor Holonomy and the Solid Angle

### The Twist of the Geodesic Frame

The body-frame angular velocity of the geodesic rotor is $\tilde\omega_b=+2\bar{\tilde R}_g\dot{\tilde R}_g$. Along a cycle of constant polar angle $\theta_0$ with azimuth $\phi(t)$ increasing, a direct computation gives

$$
\tilde\omega_b=-\dot\phi\left(\sin\theta_0\cos\phi\,e_1+\sin\theta_0\sin\phi\,e_2+(1-\cos\theta_0)\,e_3\right),
$$

in the body frame; the only component that matters for the phase is the one about the direction $\hat{\mathbf n}$, which is the coefficient of the body axis $e_3$ that the rotor carries to $\hat{\mathbf n}$. That component is

$$
\omega_b^{\parallel}=-(1-\cos\theta_0)\,\dot\phi .
$$

It is the rate at which the geodesic frame turns about the direction relative to the frame that is carried parallel; integrating around the cycle,

$$
\Delta\theta_{\mathrm{Hannay}}=-\oint\omega_b^{\parallel}\,dt
=\oint(1-\cos\theta_0)\,d\phi
=2\pi(1-\cos\theta_0)=\Omega ,
$$

the **solid angle** subtended by the cycle of directions. This is Hannay's angle for the classical spin: it equals the solid angle of the loop on the sphere of directions.

### Parallel Transport and the Holonomy

The interpretation is the holonomy of a connection. The transport of a frame along a curve on the sphere is **parallel** when the frame does not rotate about the direction of the curve's motion beyond the motion itself; the geodesic rotor above is the frame of minimal rotation, and the frame carried by parallel transport is rotated relative to it by the accumulated twist, so that the geodesic frame turns about the direction at the rate $\omega_b^\parallel$ relative to the transported frame. The accumulated angle is the **holonomy** of the rotor bundle over the sphere, and it is the integral of the connection one-form

$$
\mathcal A=(1-\cos\theta)\,d\phi
$$

around the loop. The curvature of this connection is $d\mathcal A=\sin\theta\,d\theta\wedge d\phi$, the area form of the unit sphere, so the holonomy equals the enclosed area, the solid angle — by Stokes' theorem. This is the classical geometric phase written as a holonomy, and it is independent of the speed of the cycle and of the details of the path, depending only on the enclosed area.

### The Body-Frame Reading of the Connection

The connection one-form is visible in the rotor itself. For a rotor field $\tilde R(t)$ with body-frame angular velocity $\tilde\omega_b=+2\bar{\tilde R}\dot{\tilde R}$, the algebra-valued one-form

$$
\bar{\tilde R}\,d\tilde R=+\tfrac12\,\tilde\omega_b\,dt
$$

is the pullback of the connection, and the Hannay angle is the integral of its component along the generator that stabilises the direction. Writing $\tilde\omega_b=\omega_b^{\parallel}\hat{\mathbf n}+\tilde\omega_b^{\perp}$ with $\tilde\omega_b^{\perp}$ the part orthogonal to $\hat{\mathbf n}$, the angle is $-\int\omega_b^{\parallel}dt$; the orthogonal part is the precession that changes the direction and carries no phase. This is exactly the rigid-body statement of the preceding article: the twist of a transported frame about its own axis is the component of the body angular velocity along that axis, and the Hannay angle is minus the accumulated twist, because the transported frame is the one that is carried and the geodesic frame is the one that is referred to the direction. The parallel-transport prescription — set the twist to zero and measure the holonomy — is the same prescription that makes the transport of a rigid body or a swinging plane geometrically meaningful.

### The Sign and the Orientation

The sign of the Hannay angle is fixed by two independent conventions, and both must be stated. The first is the orientation of the loop: reversing the sense of the cycle reverses the sign of the enclosed area and of the angle. The second is the reference for the "dynamical" advance: the angle variable's natural advance over a closed cycle of parameters includes a full turn $2\pi$, so an angle that is computed as a remainder can differ from the solid angle by $2\pi$. This is why the uniformly precessing spin gives the remainder $-2\pi\cos\theta_0$ in the rotating frame and the solid angle $\Omega=2\pi(1-\cos\theta_0)$ once the frame's own $2\pi$ is restored. The physically meaningful statement is that the angle is the holonomy, defined modulo $2\pi$, and that its representative in $[0,2\pi)$ is the solid angle.

### Any Loop: Stokes and the Constant Curvature

The connection $\mathcal A=(1-\cos\theta)d\phi$ has curvature

$$
\mathcal F=d\mathcal A=\sin\theta\,d\theta\wedge d\phi ,
$$

the area form of the unit sphere. By Stokes' theorem the holonomy of any loop is the integral of $\mathcal F$ over the enclosed region,

$$
\Delta\theta_{\mathrm{Hannay}}=\int\!\!\int_{\text{enclosed}}\sin\theta\,d\theta\wedge d\phi
=\Omega_{\text{enclosed}} ,
$$

so the Hannay angle is the enclosed solid angle for **every** loop, not only for a small circle. The reason the shape does not matter is that the curvature is constant: a connection whose curvature is a constant multiple of the area form has a holonomy that depends only on the enclosed area. The flux of $\mathcal F$ over the whole sphere is $4\pi$, so the connection is the vector potential of a unit-strength monopole at the centre of the sphere; the spinor holonomy is half of it, a monopole of half-unit strength, which is the double cover again. This is the classical face of the same monopole picture that the companion article *The Berry Phase and Geometric Phases in Biquaternionic Form* develops on the state space.

The constancy of the curvature also shows why the angle is robust: no matter how the parameter field is realised — a spin in a precessing field, a polarised wave transported around a loop of directions, a rigid body carried around a path of orientations — the accumulated angle is the enclosed solid angle, because the geometry of the sphere of directions is fixed. What the particular system supplies is the identification of the loop, not the value of its holonomy.

### The Foucault Pendulum

The best-known mechanical instance is the Foucault pendulum. Let $\lambda$ be the latitude and $\alpha=\frac{\pi}{2}-\lambda$ the colatitude; the local vertical $\hat{\mathbf u}$ makes the angle $\alpha$ with the Earth's axis, so once per sidereal day it traces the circle of polar angle $\alpha$ on the sphere of directions, and that circle is the loop of the transport. The swing direction is horizontal and is fixed in inertial space to the accuracy of the adiabatic approximation, and its transport is parallel in the sense that matters for the angle: a parallel-transported tangent vector has no component of its spatial angular velocity along the local vertical. The two prescriptions agree in the turn about $\hat{\mathbf u}$, which is what the angle measures, and differ only in the transverse component, of the order of the slowness. The ground frame, by contrast, turns about $\hat{\mathbf u}$ at the rate

$$
\Omega_{\mathrm E}\cos\alpha=\Omega_{\mathrm E}\sin\lambda ,
$$

so the swing plane turns relative to the ground at that rate, and the precession is $2\pi\sin\lambda$ per sidereal day: it vanishes at the equator and is a full turn at the pole.

The same number is the holonomy of the loop. The parallel transport of a tangent vector around a circle of polar angle $\alpha$ on the unit sphere turns it by the enclosed solid angle

$$
\Omega_{\mathrm{F}}=2\pi(1-\cos\alpha)=2\pi(1-\sin\lambda)
\pmod{2\pi},
$$

and the signed turn read in the co-rotating frame is $-2\pi\cos\alpha=-2\pi\sin\lambda$. The two differ by a full turn and describe the same rotation of the swing plane: at $\lambda=45^\circ$ they are $106^\circ$ and $254^\circ$, which differ by exactly $360^\circ$. The pendulum therefore supplies the standard textbook value $2\pi\sin\lambda$ of the precession and the solid-angle form $\Omega_{\mathrm{F}}$ of the holonomy at once, the two being equal as rotations; the sign and the mod-$2\pi$ freedom are the ones already fixed in "The Sign and the Orientation" above.

## The Spin Example and the Double Cover

### Uniform Precession

The same solid-angle result can be obtained from the exact solution for a uniformly precessing field, which makes the adiabatic limit transparent. Take

$$
\hat{\mathbf n}(t)=\left(\sin\theta_0\cos\epsilon t,\ \sin\theta_0\sin\epsilon t,\ \cos\theta_0\right),
\qquad
\boldsymbol\omega=\omega_0\hat{\mathbf n}(t).
$$

In the frame rotating about $e_3$ at rate $\epsilon$, the field is static and the effective angular velocity is

$$
\boldsymbol\omega_{\mathrm{eff}}=\omega_0\hat{\mathbf n}(0)-\epsilon\,e_3 ,
\qquad
|\boldsymbol\omega_{\mathrm{eff}}|=\sqrt{\omega_0^2-2\omega_0\epsilon\cos\theta_0+\epsilon^2}
=\omega_0-\epsilon\cos\theta_0+O(\epsilon^2).
$$

Over one period $T=2\pi/\epsilon$ the spin precesses about the effective direction by the angle

$$
\Theta=|\boldsymbol\omega_{\mathrm{eff}}|\,T=\frac{2\pi\omega_0}{\epsilon}-2\pi\cos\theta_0+O(\epsilon).
$$

The first term is the dynamical precession; the second is the geometric remainder. Adding the $2\pi$ by which the frame itself returns (the angle variable's natural advance over the closed parameter cycle) gives the Hannay angle

$$
\Delta\theta_{\mathrm{Hannay}}=-2\pi\cos\theta_0+2\pi=2\pi(1-\cos\theta_0)=\Omega ,
$$

in agreement with the twist computation. The two computations use different methods — the exact rotating-frame solution and the holonomy of the rotor — and give the same answer.

### The Double Cover

The factor of $2$ between the vector angle and the spinor phase is the double cover of the rotor group. The spin-$\tfrac12$ state is a spinor in the algebra, and its adiabatic phase around the same cycle is half the classical angle,

$$
\gamma_{\text{spinor}}=-\frac{\Omega}{2},
$$

with the sign fixed by the orientation convention; the classical vector angle is $\Omega$. The two are related by the standard correspondence: the spin-$S$ coherent state has Berry phase $-S\Omega$, and Hannay's angle is the derivative with respect to the action,

$$
\Delta\theta_{\mathrm{Hannay}}=-\frac{\partial}{\partial S}\left(-S\Omega\right)=\Omega .
$$

For $S=\tfrac12$ the Berry phase is $-\Omega/2$, matching the companion article on the Berry phase, and the classical Hannay angle is the derivative that removes the $\tfrac12$: the classical spin knows the full solid angle, and the spinor knows half of it. This is the same factor of $2$ that appears in the rotor article as the sign $\tilde R\to-\tilde R$ at a $2\pi$ rotation.

## Adiabatic Invariants and the Norm Form

The adiabatic invariant of the spin is the norm form. The magnitude $S$ is

$$
S=\sqrt{N(\tilde S)}=\sqrt{\mathbf S^2},
$$

and it is conserved not only in the adiabatic limit but exactly, because it is the Casimir of the bracket $\{S_i,S_j\}=\varepsilon_{ijk}S_k$ and is therefore a constant of motion for every Hamiltonian on the orbit. For a general action-angle system the adiabatic invariant $I_k$ is the action $\oint p_k\,dq_k$; for the spin on its orbit, the distinguished invariant is the norm form, and it is the action with respect to which the Hannay angle is differentiated. The statement "the Hannay angle is the derivative of the phase with respect to the action" therefore reads, in the algebra, "differentiate with respect to the square root of the norm form".

For the adiabatic transport of a general rotor — a rigid body carried around a loop of orientations — the same structure holds: the transport is parallel with respect to a connection on the group, the holonomy is an element of $SU(2)$ (a rotor), and its rotation angle is the classical geometric phase. The Foucault pendulum is the standard mechanical instance; the falling-cat and bicycle-wheel problems are the standard instances of a rotor holonomy, in which a body is reoriented by internal motion with no net angular momentum. Their mechanical details are standard and are not developed here, and the algebraic content is the one developed here.

## The Classical Character of the Phase

Hannay's angle is a property of a classical trajectory. It is measured by observing the orientation of the motion after a cycle — the plane of a pendulum's swing, the phase of a spin precessing in a slowly turned field — and it requires no measurement postulate and no state space. The connection and curvature used to compute it are the same objects that appear in the quantum theory, but that is a statement about the mathematical form of the two theories, not about their physical content: the classical angle is the integral of a one-form on the parameter space, and it is classical because the trajectory is.

The one place where the quantum counterpart enters the discussion is the formula $\Delta\theta=-\partial\gamma/\partial I$, which relates the classical angle to the Berry phase of the quantised system. The formula is used as a standard result that organises the two phases; the quantum side is developed in the companion article on the Berry phase and is not repeated here.

## Summary

Hannay's angle is the classical geometric phase of an adiabatically cycled system, and in the biquaternion algebra it is the holonomy of the rotor that carries a fixed axis to the slowly varying direction.

- Action-angle variables $(\theta,I)$ with slowly cycled parameters $R$ have an adiabatic invariant $I$ and an angle $\theta$ that acquires, after a closed cycle, the Hannay angle $\Delta\theta_k=-\partial_k\oint\mathcal A_\mu dR^\mu$, the action-derivative of the Berry phase.
- The classical spin is a point of the coadjoint orbit $N(\tilde S)=S^2$, with $H=\boldsymbol\omega\cdot\mathbf S$ generating the rotor flow $\dot{\mathbf S}=\boldsymbol\omega\times\mathbf S$.
- The direction $\hat{\mathbf n}=\tilde Re_3\bar{\tilde R}$ defines a rotor field; the geodesic (shortest) rotor is $\tilde R_g=\cos\frac{\theta_0}{2}+\sin\frac{\theta_0}{2}\hat{\mathbf m}$ with $\hat{\mathbf m}$ in the plane perpendicular to $e_3$, and its body-frame twist about the direction is $\omega_b^{\parallel}=-(1-\cos\theta_0)\dot\phi$, so that the Hannay angle is $-\oint\omega_b^{\parallel}dt=\Omega$.
- Integrating the twist around a cycle of solid angle $\Omega$ gives Hannay's angle $\Delta\theta_{\mathrm{Hannay}}=\Omega$, the holonomy of the connection $\mathcal A=(1-\cos\theta)d\phi$ with curvature $\sin\theta\,d\theta\wedge d\phi$.
- The exact rotating-frame solution of the uniformly precessing field gives the same $\Omega$.
- The spinor phase is half the classical angle, $\gamma=-\Omega/2$ for spin-$\tfrac12$, the factor $2$ being the double cover $\tilde R\to-\tilde R$; the general relation is $\gamma=-S\Omega$ and $\Delta\theta=-\partial_S\gamma=\Omega$.
- The adiabatic invariant is the norm form, $S=\sqrt{N(\tilde S)}$; the Hannay angle is the derivative of the phase with respect to it.

The phase is classical: it is the holonomy of a transport on the space of directions, computed from the classical trajectory, and it needs no quantum postulate.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\theta_k,I_k)$ | Action-angle variables |
| $R$ | Slowly cycled parameters |
| $\omega_k=\partial H_0/\partial I_k$ | Instantaneous frequencies |
| $\Delta\theta_k=-\partial_k\oint\mathcal A_\mu dR^\mu$ | Hannay's angle |
| $\mathcal A_\mu$ | Berry connection of the quantised problem |
| $\gamma=\oint\mathcal A_\mu dR^\mu$ | Berry phase (quantum counterpart) |
| $\tilde S\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-$, $N(\tilde S)=S^2$ | Classical spin on its coadjoint orbit |
| $\hat{\mathbf n}=\tilde Re_3\bar{\tilde R}$ | Slowly varying direction |
| $\tilde R_g$ | Geodesic (untwisted) rotor field |
| $\tilde\omega_b=+2\bar{\tilde R}\dot{\tilde R}$ | Body-frame angular velocity (twist) |
| $\omega_b^{\parallel}=-(1-\cos\theta_0)\dot\phi$ | Twist about the direction |
| $\Omega=2\pi(1-\cos\theta_0)$ | Solid angle of the cycle; Hannay angle |
| $\mathcal A=(1-\cos\theta)d\phi$ | Connection on the sphere of directions |

## Further Reading

- J. H. Hannay, "Angle variable holonomy in adiabatic excursion of an integrable Hamiltonian," *Journal of Physics A* **18** (1985) 221–230, for the classical geometric phase and the derivation of the angle.
- M. V. Berry, "Quantal phase factors accompanying adiabatic changes," *Proceedings of the Royal Society A* **392** (1984) 45–57, for the quantum phase and its connection.
- M. V. Berry, "Classical adiabatic angles and quantal adiabatic phase," *Journal of Physics A* **18** (1985) 15–27, for the relation between the classical and quantum phases.
- A. Shapere and F. Wilczek (eds.), *Geometric Phases in Physics* (World Scientific, 1989), for the collected development of Berry, Hannay, and related phases.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for action-angle variables and the adiabatic theorem for classical systems.
- V. I. Arnold, V. V. Kozlov, and A. I. Neishtadt, *Mathematical Aspects of Classical and Celestial Mechanics* (Springer, 2006), for adiabatic invariance and averaging.
- M. V. Berry, "The adiabatic limit and the semiclassical limit," *Journal of Physics A* **17** (1984) 1225–1233, for the geometric-phase treatment of the Foucault pendulum and of polarized light.
- J. E. Marsden and T. S. Ratiu, *Introduction to Mechanics and Symmetry* (Springer, 1999), for holonomy and geometric phases in Hamiltonian systems.
