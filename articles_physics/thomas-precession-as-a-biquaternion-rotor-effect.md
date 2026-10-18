# __Thomas Precession as a Biquaternion Rotor Effect__

## Introduction

A particle that moves on a curved worldline carries an instantaneous rest frame whose orientation changes from one event to the next even when no torque acts on it. The rotation of that frame relative to the laboratory is the **Thomas precession**, and its angular velocity is fixed by the acceleration and the velocity alone,

$$
\vec\omega_T=\frac{1}{c^{2}}\left(\frac{\gamma^{2}}{\gamma+1}\right)\vec a\times\vec v,
\qquad
\gamma=\frac{1}{\sqrt{1-\vec v^{2}/c^{2}}} ,
$$

with $\vec a=d\vec v/dt$ the laboratory acceleration and $c=1/\sqrt{\epsilon\mu}$ the speed of light in the medium. The effect is purely **kinematic**: it involves no force, no moment, and no field, and it is present for every accelerated particle. Its non-relativistic limit is $\vec\omega_T=\tfrac{1}{2c^{2}}\vec a\times\vec v$, the "Thomas half", and it is the kinematic part of the spin–orbit coupling and of the classical precession of a relativistic spin in an electromagnetic field.

The purpose of this article is to exhibit the Thomas precession as what it algebraically is: a **rotor effect**. The argument has three steps, and none of them leaves the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$.

The first step is that the transformation that carries the laboratory to the instantaneous rest frame of a particle is a **unit-norm biquaternion** $\tilde U_{\vec v}$, and for a pure boost it is Hermitian and lies in the informational sector $\mathbb{M}_+$. A single boost therefore contains no rotation: it is a boost, and a boost is not a rotation.

The second step is that the composition of two boosts is **not** a boost. The product $\tilde U_{1}\tilde U_{2}$ of two boost rotors is a unit-norm biquaternion, so it admits the **polar decomposition** $\tilde U_{1}\tilde U_{2}=\tilde U_{\mathrm b}\tilde{u}$ into a pure boost $\tilde U_{\mathrm b}$ and a rotation $\tilde{u}\in\mathbb{H}_{\mathbb{B}}$, and the rotation factor is present whenever the two boost directions are not collinear. The rotation is the **Thomas–Wigner rotation**, its exact angle is a rational function of the two rapidities and the angle between the directions, and it is the algebraic expression of the fact that the boosts do not form a subgroup.

The third step is to **take the continuous limit**. The rest frames at two laboratory times $t$ and $t+dt$ are related by the interval rotor $\tilde{M}=\tilde U_{\vec v+d\vec v}\tilde U_{\vec v}^{-1}$, whose rotation factor is the Thomas–Wigner rotation of the interval. Expanding the exact product to first order in $dt$ gives $\vec\omega_T$, with the axis $\vec u_{\vec a\times\vec v}$ and the coefficient $\gamma^{2}/(\gamma+1)$; the "Thomas half" is the value of that coefficient at $\gamma=1$. The whole of the Thomas precession is thus the linearization of a quaternion product.

Three boundaries are respected. The **Wigner rotation as an information-theoretic object** belongs to the sibling quantum series, `Biquaternion Relativistic Quantum Theory`, subcategory on informational aspects; the present article is the kinematic statement. The **cover of the Lorentz group** and its topology belong to `Biquaternion Relativistic Non Quantum Theory`, subcategory `generalities`; here the cover is used only through the statement that the boost rotors are unit-norm biquaternions and that $SL(2,\mathbb{C})$ is a double cover of $SO^{+}(1,3)$. The **Larmor precession** of a magnetic moment in a magnetic field is a non-relativistic effect and belongs to `Biquaternion Non Relativistic Non Quantum Theory`, subcategory on effects with intrinsic magnetism; it appears here only as the non-relativistic limit against which the Thomas term is read.

The article is organized as follows. The next section fixes the boost rotor and the instantaneous rest frame. The following section develops the composition of two boosts and the exact Wigner angle. The next two sections take the continuous limit and identify the Thomas rotor. The remaining sections treat uniform circular motion, the connection to the spin of a relativistic particle, and the factor $\tfrac12$ in the spin–orbit coupling, and separate what the algebra supplies from what is standard relativistic kinematics.

**Conventions.** We use those of the foundational articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_\mu^{2}=-e_t$ and $\vec e_\mu \vec e_\nu=\epsilon_{\mu\nu\lambda}\vec e_\lambda$ for $\mu\neq\nu$, and the scalar imaginary is $i$, central and with $i^{2}=-1$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector, home of the four-vectors) and $\mathbb{M}_+$ (Hermitian, the informational sector, home of the boost rotors), with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace, the home of the rotation rotors, and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$ is the central scalar subspace. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$, the quaternion conjugate is $\tilde{Q}^{\natural}$, and the Hermitian conjugate is $\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}$. The four-velocity is $\tilde{V}=\gamma(ic\,e_t+\vec v)$ with $\langle\tilde{V}\rangle_{\natural}=-c^{2}$, the four-momentum is $\tilde{P}=m\tilde{V}=iE/c\,e_t+\vec p$, and the four-force is $\tilde{K}_{\mathrm{f}}=d\tilde{P}/d\tau\in\mathbb{M}_-$. Throughout, $\tau$ is proper time, $t$ laboratory time, $\vec v$ the particle velocity, $\vec a=d\vec v/dt$ its laboratory acceleration, $\vec u$ a unit direction, and $\psi$ a rapidity with $\tanh\psi=v/c$. The trace pairing on the informational sector is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H) = 2\langle\tilde{P},\tilde{H}\rangle$.

## The Boost Rotor and the Instantaneous Rest Frame

The **boost rotor** of a frame moving with velocity $\vec v_b$ is the unit-norm biquaternion

$$
\tilde U_{\vec v_b}=\cosh\frac{\psi_b}{2}+i\sinh\frac{\psi_b}{2}\,\vec u,
\qquad
\tanh\psi_b=\frac{v_b}{c},
\qquad
\vec u=\frac{\vec v_b}{v_b},
$$

which is Hermitian, $\tilde U_{\vec v_b}^{*}=\tilde U_{\vec v_b}$, lies in $\mathbb{M}_+$, and has unit norm, $\tilde U_{\vec v_b}\tilde U^{\natural}_{\vec v_b}=e_t$. It acts on a four-vector by **rotor conjugation**,

$$
\tilde{Q}'\;=\;\tilde U_{\vec v_b}\,\tilde{Q}\,\tilde U_{\vec v_b}^{*},
$$

and the conjugation preserves the material sector $\mathbb{M}_-$. When the four-vector acted upon is a four-velocity $\tilde{V}=\gamma(ic\,e_t+\vec v)$, the conjugation produces the standard parallel–perpendicular Lorentz transformation (Companion article *Exercise: Boosting a Four-Velocity and Rapidity Composition*, for the composition of boosts and the frame four-velocity), and in the collinear case the rapidities subtract, $v'=c\tanh(\psi_v-\psi_b)$.


The rotor associated with a four-velocity is the positive Hermitian square root

$$
\tilde U_{\vec v}=\sqrt{-\frac{i}{c}\,\tilde{V}^{\natural}}
=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\,\vec u_v,
\qquad
\tilde U_{\vec v}\,\tilde{V}\,\tilde U_{\vec v}^{*}=ic\,e_t ,
$$

and it is the **laboratory-to-rest** rotor. The four-velocity fixes the Hermitian representative uniquely only up to sign and leaves the orientation of the rest frame free: if $\tilde{Q}$ is any unit-norm rotor with $\tilde{Q}\tilde{V}\tilde{Q}^{*}=ic\,e_t$, then so is $\tilde{Q}\tilde{u}$ for every rotation $\tilde{u}\in\mathbb{H}_{\mathbb{B}}$, because a rotation fixes the rest four-velocity $ic\,e_t$. A single four-velocity therefore determines a **boost but not a rotation**, and the orientation of the rest frame is not seen by any one of them. The Thomas precession is precisely the statement that this orientation is nevertheless determined by the **worldline**: the rest frames at successive events are related by a rotation, and it is visible only in the comparison of two of them.

## The Composition of Two Boosts and the Wigner Rotor

Let

$$
\tilde U_{k}=\cosh\frac{\psi_k}{2}+i\sinh\frac{\psi_k}{2}\,\vec u_k,
\qquad k=1,2,
$$

be two boost rotors. Because the product of two unit-norm biquaternions is unit-norm, the product $\tilde U_{1}\tilde U_{2}$ is a unit-norm biquaternion, and it admits the **polar decomposition**

$$
\tilde U_{1}\tilde U_{2}=\tilde U_{\mathrm b}\,\tilde{u},
\qquad
\tilde U_{\mathrm b}\in\mathbb{M}_+ \ \text{a pure boost},
\qquad
\tilde{u}\in\mathbb{H}_{\mathbb{B}}\ \text{a rotation}.
$$

The product is Hermitian, and hence a pure boost with no rotation factor, if and only if the two directions are parallel or antiparallel. Otherwise the real vector part $\vec q=s_1s_2\,\vec u_x\times\vec u_y$ (with $c_k=\cosh\tfrac{\psi_k}{2}$, $s_k=\sinh\tfrac{\psi_k}{2}$) is non-zero, and the polar decomposition carries exactly that part into the rotation factor. The rotation $\tilde{u}$ is the **Thomas–Wigner rotation** of the pair of boosts.

For two boosts of equal rapidity $\psi$ whose directions make an angle $\theta$, the angle $\omega$ of $\tilde{u}$ is

$$
\tan\frac{\omega}{2}
=\frac{\sinh^{2}\dfrac{\psi}{2}\,\sin\theta}
{\cosh^{2}\dfrac{\psi}{2}+\sinh^{2}\dfrac{\psi}{2}\,\cos\theta},
$$

and its axis is the normal to the plane of the two boost directions. The general case of unequal rapidities is the same formula with two different rapidities, and it is derived in Companion article *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*, for the composition law and the finite Wigner angle. The formula has two instructive limits: for small rapidity it gives $\omega\approx\tfrac{1}{2}\psi^{2}\sin\theta$, a purely relativistic effect vanishing as $v^{2}/c^{2}$, and for large rapidity it saturates at $\omega\to\theta$, the angle between the two directions.

Two features of this composition law matter for what follows. First, the **rotation factor is a compact-group element**, an element of the same $SU(2)$ that carries the topology of the cover; the boost part is contractible, and every obstruction in the composition of boosts is carried by the rotation directions. Second, the rotation factor is **absent for a single boost**: a boost is Hermitian, its polar rotation factor is trivial, and no orientation is generated. The Wigner rotation is a property of a pair, or of a path, and it is the compositional side of the same compact structure whose topological side is the two-sheeted cover.

At equal rapidity $\psi=1.0$ and angle $\theta=0.7$ the polar decomposition of the product gives $\omega=0.235423658$, equal to the formula to the printed digits; at unequal rapidities and angles $(\psi_1,\psi_2,\varphi)=(0.5,1.2,1.1)$, $(2.0,0.7,2.0)$, $(3.0,1.1,0.9)$ and $(0.3,2.5,1.7)$ the same agreement is found, so the general formula is not merely the symmetric special case. The extracted rotation vector lies along the normal to the plane of the two boost directions in every case, with the sense fixed by the order of the product.

## The Rotor Between Neighbouring Rest Frames

Let a particle have laboratory velocity $\vec v(t)$, and let $\tilde U_{\vec v}$ be its lab-to-rest rotor. The rest frame at laboratory time $t+dt$ is reached from the rest frame at time $t$ by the **interval rotor**

$$
\tilde{M}
=\tilde U_{\vec v+d\vec v}\,\tilde U_{\vec v}^{-1}
=\tilde U_{\vec v+d\vec v}\,\tilde U^{\natural}_{\vec v},
\qquad
d\vec v=\vec a\,dt .
$$

Indeed, if $\tilde{Q}'=\tilde U_{\vec v}\tilde{Q}\tilde U_{\vec v}^{*}$ are the components of a four-vector in the rest frame at $t$, then the components in the rest frame at $t+dt$ are

$$
\tilde{Q}''=\tilde U_{\vec v+d\vec v}\tilde{Q}\tilde U_{\vec v+d\vec v}^{*}
=\tilde{M}\tilde{Q}'\tilde{M}^{*},
$$

so $\tilde{M}$ is the transformation between the two rest frames. It is unit-norm, and its polar decomposition

$$
\tilde{M}=\tilde U_{\mathrm b}\,\tilde{u},
\qquad
\tilde U_{\mathrm b}\in\mathbb{M}_+,
\qquad
\tilde{u}\in\mathbb{H}_{\mathbb{B}},
$$

separates the boost that accounts for the change of speed from the **rotation of the rest frame's spatial triad**. The rotation factor $\tilde{u}$ is the Thomas–Wigner rotation of the interval $dt$, and its angle is given by the exact formula of the preceding section with the two boost directions $\vec u_{\vec v+d\vec v}$ and $-\vec u_v$. The axis is the normal to those two directions, which is the direction orthogonal to the plane spanned by $\vec v$ and $\vec a$.

The interval rotor makes precise in what sense the Thomas precession is a rotor effect. The worldline supplies, event by event, a lab-to-rest rotor; the product of two of them contains a rotation; and the rotation is the holonomy of the boost path. The rotation is not put in by hand, and it is not a consequence of any dynamical postulate: it is what the quaternion product yields when two non-collinear boosts are composed.

## The Continuous Limit: The Thomas Precession Rate

The Thomas precession is the angular velocity obtained from the interval rotor in the limit $dt\to0$. Write the two boost directions and rapidities as in Companion article *Exercise: The Thomas Precession*, for the direct expansion of the interval rotor: $\vec u_x=\vec u_{\vec v+d\vec v}$, $\vec u_y=-\vec u_v$, with rapidities $\psi_1=\psi+d\psi$ and $\psi_2=\psi$, and let $\varphi$ be the angle between them, so that $\varphi=\pi-\delta$ with

$$
\delta=\frac{|\vec a_\perp|}{v}\,dt+O(dt^{2}),
\qquad
\vec a_\perp=\vec a-\frac{\vec a\cdot\vec v}{v^{2}}\vec v,
$$

the perpendicular part of the acceleration. Since only the perpendicular acceleration changes the direction of the velocity, $d\psi=\gamma^{2}(\vec a\cdot\vec u_v)dt/c$, and to leading order

$$
\sin\varphi=\delta+O(dt^{3}),
\qquad
\cos\varphi=-1+O(dt^{2}).
$$

Substituting into the exact Wigner-angle formula, the numerator is $\sinh^{2}\tfrac{\psi}{2}\,\delta+O(dt^{2})$, the $d\psi$ terms cancel between the two products in the denominator, and the denominator is $1+O(dt^{2})$. Hence

$$
\tan\frac{\theta_W}{2}=\sinh^{2}\frac{\psi}{2}\,\delta+O(dt^{2})
\;\Longrightarrow\;
\theta_W=(\gamma-1)\frac{|\vec a_\perp|}{v}\,dt+O(dt^{2}),
$$

where $2\sinh^{2}\tfrac{\psi}{2}=\cosh\psi-1=\gamma-1$. The angular velocity is therefore

$$
\omega_T=\frac{d\theta_W}{dt}=(\gamma-1)\frac{|\vec a_\perp|}{v}
=\frac{\gamma-1}{v^{2}}\,|\vec a\times\vec v|,
\qquad
\frac{\gamma-1}{v^{2}}=\frac{\gamma^{2}}{c^{2}(\gamma+1)},
$$

and restoring the vector character with the axis $\vec u_{\vec a\times\vec v}$ gives the boxed result

$$
\boxed{\;\vec\omega_T=\frac{1}{c^{2}}\left(\frac{\gamma^{2}}{\gamma+1}\right)\vec a\times\vec v.\;}
$$

The **Thomas half** is the non-relativistic value of the coefficient: as $v\to0$ one has $\gamma\to1$ and $\gamma^{2}/(\gamma+1)\to\tfrac12$, so

$$
\vec\omega_T\;\approx\;\frac{1}{2c^{2}}\,\vec a\times\vec v
\qquad (v\ll c).
$$

The factor $\tfrac12$ is not inserted by hand: it is the limit of $\gamma^{2}/(\gamma+1)$, and it arises in the expansion through the cancellation of the $d\psi$ terms in the denominator, which leaves the value $1$ rather than the larger $\cosh\psi$ that a first guess might produce.

Only the **transverse** acceleration precesses the frame. Since $\vec a\times\vec v=\vec a_\perp\times\vec v$, a purely longitudinal acceleration gives $\vec\omega_T=0$: it changes the rapidity but not the direction of the velocity, and a boost along the instantaneous direction generates no rotation. This is the first sign that a collinear configuration cannot test the direction of $\vec\omega_T$.

The interval rotor $\tilde{M}=\tilde U_{\vec v+d\vec v}\tilde U^{\natural}_{\vec v}$ is formed directly as a $2\times2$ complex matrix in the representation $\mathsf{M}_2(\vec e_\mu)=-i\sigma_k$, $\mathsf{M}_2(i)=iI_2$, and its polar decomposition $\tilde{M}=\tilde U_{\mathrm b}\tilde{u}$, $\tilde U_{\mathrm b}=\sqrt{\tilde{M}\tilde{M}^{*}}$, $\tilde{u}=\tilde U_{\mathrm b}^{-1}\tilde{M}$, is carried out at $dt=10^{-5}$ for random non-collinear pairs $(\vec v,\vec a)$ with $|\vec v|<c$. The rotation vector of $\tilde{u}$ agrees with $\vec\omega_T\,dt$ in both magnitude and direction to better than $10^{-10}$ in units $c=1$; the collinear case gives zero on both sides. The sign is testable only off the collinear line, and it is the axis $\vec a\times\vec v$ that the exact product selects.

## The Thomas Rotor

The precession can be written as a rotor conjugation in the same half-angle form used throughout the series. Let $\vec u_\omega=\vec u_{\vec a\times\vec v}$ be the unit axis and $\theta_T(t)$ the accumulated angle, $d\theta_T=\omega_T\,dt$. A spatial triad that is carried rigidly by the instantaneous rest frame rotates relative to the laboratory according to

$$
\frac{d\vec r}{dt}=\vec\omega_T\times\vec r,
\qquad
\vec r=r_\mu \vec e_\mu\in\mathbb{H}_{\mathbb{B}},
$$

and, for constant $\vec\omega_T$, the solution is the rotor conjugation

$$
\vec r(t)=\tilde{u}_T(t)\,\vec r(0)\,\tilde{u}_T(t)^{*},
\qquad
\tilde{u}_T(t)=\exp\!\left(\frac{\theta_T(t)}{2}\,\vec u_{\omega,\mu}\vec e_\mu\right),
$$

with $\tilde{u}_T$ a unit real quaternion. The frame turns through $\theta_T$ while the rotor turns through half that angle: this is the double-cover half-angle of the algebra, the same one that appears in the Larmor rotor and in the spin-$\tfrac12$ evolution. The generator form is the commutator

$$
\frac{d\vec r}{dt}=\tfrac{1}{2}\left[\vec r,\vec\omega_T\right],
\qquad
\vec\omega_T=-\omega_{T,\mu}\vec e_\mu ,
$$

the sign being the one that makes the generator the negative of the physical angular velocity, exactly as in the Larmor equation.

The half-angle is where the two descriptions of the rotation meet. On a **vector** of the material sector the rotor acts by conjugation, and $\tilde{u}_T$ and $-\tilde{u}_T$ produce the same rotation; the rest frame's triad is insensitive to the sign. On a **spinor**, the rotor acts by one-sided multiplication, $\psi\mapsto\mathsf{M}_2(\tilde{u}_T)\psi$, and the sign is visible: a rotation through $2\pi$ returns the vector to itself but the spinor to its negative. The one-sided action and the spinor module are the subject of Companion article *The Spinor Representation of the Lorentz Group in Biquaternionic Form*, for the defining spinor module and the one-sided Lorentz action; here it is enough to record that the kinematic rotation of the frame and the one-sided rotation of a state are the same rotor, and that the information-theoretic interpretation of the Wigner rotation belongs to the sibling quantum series.

## Uniform Circular Motion

The cleanest instance is uniform circular motion. Let the particle move on a circle of radius $R$ with constant speed $v$, angular velocity $\vec\Omega=\Omega\,\vec e_z$, so that

$$
\vec v=\vec\Omega\times\vec r,
\qquad
\vec a=-\Omega^{2}\vec r,
\qquad
|\vec r|=R,
\qquad
\vec a\cdot\vec v=0 .
$$

Then

$$
\vec a\times\vec v=(-\Omega^{2}\vec r)\times(\vec\Omega\times\vec r)
=-\Omega^{2}R^{2}\vec\Omega
=-\Omega v^{2}\vec e_z,
$$

and the rate becomes

$$
\vec\omega_T
=\frac{\gamma^{2}}{\gamma+1}\left(-\Omega\frac{v^{2}}{c^{2}}\right)\vec e_z
=-(\gamma-1)\,\Omega\,\vec e_z,
$$

using $\gamma^{2}v^{2}/c^{2}=\gamma^{2}-1=(\gamma-1)(\gamma+1)$. The precession is therefore **retrograde**: it is opposite in sense to the orbital motion. Over one orbit the laboratory time is $T=2\pi/\Omega$, and the frame turns through

$$
\Delta\theta_T=-(\gamma-1)\,\Omega\,T=-2\pi(\gamma-1),
$$

so a full turn of the orbit advances the rest frame by $-2\pi(\gamma-1)$ radians, i.e. by $-(\gamma-1)$ of a full turn. In the non-relativistic limit $\gamma-1\approx v^{2}/2c^{2}$, and the precession is $-v^{2}/2c^{2}$ of the orbital rate: **half the orbital rate, opposite in sense**. This is the kinematic content of the Thomas half, now in its exact circular form.

## The Spin of a Relativistic Particle

The Thomas precession is a kinematic effect of any accelerated worldline, but its historical and physical importance is that a **spin-$\tfrac12$ particle** carries an intrinsic magnetic moment tied to an intrinsic angular momentum, and the orientation of that angular momentum is referred to the instantaneous rest frame. Any direction that is attached to the rest frame — that is, defined by the succession of pure boosts along the worldline — inherits the precession $\vec\omega_T$. The observed laboratory precession of the spin is the sum of this kinematic contribution and the dynamical torque computed in the rest frame, and the Thomas term is the kinematic one.

The cleanest statement of the division of labour uses the gyromagnetic factor $g$. A magnetic moment $\vec\mu=\gamma_g\,\vec S$ with $\gamma_g=g\,ϙ/2m$ is torqued in the instantaneous rest frame, where the spin precesses at the rest-frame Larmor rate, while the rest frame itself rotates relative to the laboratory at the Thomas rate. In a purely magnetic field the laboratory spin precession that results is the sum of the rest-frame Larmor rotation and the Thomas rotation of the frame. For the special value $g=2$ the two contributions combine so that the spin remains aligned with the velocity: the spin and the momentum precess together, and there is no precession of the spin relative to the momentum. This is the property that makes $g=2$ the "normal" value and the quantity $g-2$ the anomalous moment, and it is the reason the kinematic Thomas term must be included before any classical model of the intrinsic moment can be compared with experiment.

The general equation of motion that contains all of this is the **Bargmann–Michel–Telegdi equation**, the covariant equation for the spin four-vector of a classical charged particle in an electromagnetic field. It is the subject of Companion article *The Classical Spinning Particle: The Bargmann–Michel–Telegdi Equation in Biquaternionic Form*, for the general equation of motion of a classical spin, of which the present kinematic precession is the free-field piece. The Larmor precession of a moment in a magnetic field, treated as a non-relativistic effect in Companion article *Larmor Precession and the Classical Magnetic Moment in Biquaternionic Form*, for the non-relativistic precession, is the non-relativistic limit of the same dynamics, and its rotor is the same half-angle rotor.

## The Thomas Half and the Spin–Orbit Coupling

The factor $\tfrac12$ in the spin–orbit coupling of the hydrogen atom is the standard physical consequence of the Thomas precession. A naive transformation to the instantaneous rest frame of an electron moving in the electrostatic field of the nucleus yields a magnetic field $\vec B'\approx-\vec v\times\vec E/c^{2}$ in the rest frame, and the Larmor coupling of the spin to that field gives a spin–orbit term **twice** the observed value. The Thomas precession contributes the opposite half, leaving the observed coefficient. Companion article *Exercise: The Non-Relativistic Limit and the Pauli Equation*, for the spin–orbit term and the Thomas factor, records the result in exactly this form: the coefficient of the spin–orbit term carries the "Thomas factor of $\tfrac12$", and a naive Lorentz transformation to the instantaneous rest frame would give twice that value. The present article supplies the kinematics behind the factor: the leading Thomas rate is half of $\vec a\times\vec v/c^{2}$, and its exact circular form is $\vec\omega_T=-(\gamma-1)\vec\Omega$.

Two further companions complete the classical picture. Companion article *The Classical Origin of g = 2 in Biquaternionic Form*, for the intrinsic gyromagnetic ratio, accounts for why that ratio is twice the convective one, which is the value at which the Larmor and Thomas contributions cancel in the spin-follows-velocity sense. Companion article *The Relativistic Particle in an External Field, in Biquaternionic Form*, for the accelerated worldline and the four-force, supplies the rest-frame sequence whose holonomy is computed here.

## What the Rotor Supplies, and What Is Standard

It is useful to separate the algebraic content of the derivation from the standard relativistic kinematics that it reproduces.

**Supplied by the algebra.**

- The boost rotor is a Hermitian unit-norm biquaternion in $\mathbb{M}_+$, and a **single** boost contains no rotation; the rotation is created by composition.
- The product of two boost rotors admits a unique polar decomposition $\tilde U_{\mathrm b}\tilde{u}$ into a pure boost and a rotation of $\mathbb{H}_{\mathbb{B}}$, and the rotation factor is the Wigner rotation.
- The exact Wigner angle and its axis follow from the quaternion product with $\vec e_\mu \vec e_\nu=\epsilon_{\mu\nu\lambda}\vec e_\lambda$ and $\vec e_\mu^{2}=-e_t$, without any matrix or tensor apparatus; the whole of the Thomas precession is the first-order term of that product.
- The interval rotor $\tilde{M}=\tilde U_{\vec v+d\vec v}\tilde U^{\natural}_{\vec v}$ is the rotor between neighbouring rest frames, and its rotation factor is the Thomas–Wigner rotor.
- The half-angle rotor $\tilde{u}_T$ that carries the frame, and its double-valued sign, are the same rotor that acts one-sidedly on the spinor module.

**Standard relativistic kinematics transcribed.**

- The Thomas precession rate $\vec\omega_T=c^{-2}\gamma^{2}(\gamma+1)^{-1}\vec a\times\vec v$, its non-relativistic limit $\tfrac{1}{2c^{2}}\vec a\times\vec v$, and the retrograde circular result $-2\pi(\gamma-1)$ per orbit are the standard results of Thomas and of the subsequent literature.
- The connection to the spin–orbit factor $\tfrac12$ and to the anomalous magnetic moment is standard atomic and particle physics.
- The polar decomposition of $SL(2,\mathbb{C})$, the contraction onto $SU(2)$, and the fibration of the Lorentz group over hyperbolic three-space are standard Lie-group theory, recorded in the companion article on the two-sheeted cover.

**Interpretation.** The Thomas precession is the **holonomy** of the boost path: the boost manifold is contractible, but the composition of boosts is obstructed by a rotation, and the continuous accumulation of that obstruction along a worldline is the precession. The algebra makes the obstruction explicit as a quaternion product; it does not, and is not claimed to, replace the standard kinematics.

## Open Questions

1. **The Wigner rotation as a holonomy.** The Wigner angle of a finite pair of boosts depends only on the two boost vectors; the accumulated angle along a worldline depends on the path. Is there a natural biquaternion expression of the path dependence, as a parallel transport on the boost manifold, that makes the Thomas precession manifestly the curvature of that manifold?

2. **Higher representations.** The rotor of $\mathbb{H}_{\mathbb{B}}$ carries the vector representation of the rotation group by conjugation and the spin-$\tfrac12$ representation by one-sided multiplication. How does the Thomas rotation act on the higher $(j,j')$ carriers, which are not modules over $\mathbb{B}$, and does the correspondence between the kinematic and spinor descriptions extend?

3. **The sign and the two sheets.** The sign of a rotor on the $2\pi$ loop is invisible on every material vector and visible only on the spinor. Is there a classical, non-quantum object whose transport detects the sign, or is the spinor module necessary?

4. **A gravitational analogue.** The Thomas precession is the kinematic rotation of a boosted frame; the corresponding effect for a curved spacetime is the geodetic precession of a gyroscope. Does the biquaternion rotor formulation of the present article extend to a weak-field metric, and does the holonomy interpretation survive?

5. **Empirical content.** Every result here reproduces standard relativistic kinematics. The framework's claim is structural, and any deviation would have to appear as a modification of the boost composition or of the spin coupling; none is visible at the level developed.

## Summary

The Thomas precession is a **rotor effect**. The transformation from the laboratory to the instantaneous rest frame of a particle of velocity $\vec v$ is the Hermitian unit-norm biquaternion

$$
\tilde U_{\vec v}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\,\vec u_v
=\sqrt{-\frac{i}{c}\,\tilde{V}^{\natural}},
\qquad
\tanh\psi=\frac{v}{c},
\qquad
\tilde U_{\vec v}\tilde{V}\tilde U_{\vec v}^{*}=ic\,e_t ,
$$

and a single boost contains no rotation. The composition of two non-collinear boosts is a unit-norm biquaternion with polar decomposition $\tilde U_1\tilde U_2=\tilde U_{\mathrm b}\tilde{u}$, and the rotation factor $\tilde{u}\in\mathbb{H}_{\mathbb{B}}$ is the Thomas–Wigner rotation, of exact angle

$$
\tan\frac{\omega}{2}
=\frac{\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\sin\varphi}
{\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2}+\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\varphi},
$$

about the normal to the plane of the two boost directions. The rest frames at two neighbouring laboratory times are related by the interval rotor

$$
\tilde{M}=\tilde U_{\vec v+d\vec v}\,\tilde U^{\natural}_{\vec v}=\tilde U_{\mathrm b}\tilde{u},
\qquad
d\vec v=\vec a\,dt,
$$

whose rotation factor is the Thomas–Wigner rotation of the interval. Its continuous limit is the Thomas precession

$$
\boxed{\;\vec\omega_T=\frac{1}{c^{2}}\left(\frac{\gamma^{2}}{\gamma+1}\right)\vec a\times\vec v,\;}
\qquad
\vec\omega_T\approx\frac{1}{2c^{2}}\,\vec a\times\vec v\quad(v\ll c),
$$

along $\vec a\times\vec v$, with only the transverse acceleration contributing. The precession is realised by the half-angle rotor $\tilde{u}_T=\exp(\tfrac{1}{2}\theta_T\vec u_{\omega,\mu}\vec e_\mu)$ acting by conjugation on the rest-frame triad, with the same double-cover half-angle that acts one-sidedly on the spinor. For uniform circular motion the frame is retrograde, $\vec\omega_T=-(\gamma-1)\vec\Omega$, turning through $-2\pi(\gamma-1)$ per orbit, i.e. half the orbital rate opposite in sense in the non-relativistic limit. The kinematic precession is the origin of the factor $\tfrac12$ in the spin–orbit coupling, and it is the free-field piece of the general spin equation of motion treated in the companion article on the Bargmann–Michel–Telegdi equation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$, $\vec e_\mu \vec e_\nu=\epsilon_{\mu\nu\lambda}\vec e_\lambda$ $(\mu\neq\nu)$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; central scalar subspace |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\tilde{Q}^{\natural}$, $\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}$ | Quaternion conjugate, Hermitian conjugate |
| $\tilde{V}=\gamma(ic\,e_t+\vec v)$ | Four-velocity, $\langle\tilde{V}\rangle_{\natural}=-c^2$ |
| $\tilde{P}=m\tilde{V}=iE/c\,e_t+\vec p$ | Four-momentum |
| $\tilde{K}_{\mathrm{f}}=d\tilde{P}/d\tau$ | Four-force, in $\mathbb{M}_-$ |
| $c$, $c_0$ | Speed of light in the medium; in vacuum |
| $\gamma=(1-\vec v^2/c^2)^{-1/2}$ | Lorentz factor |
| $\psi$, $\tanh\psi=v/c$ | Rapidity |
| $\tilde U_{\vec v_b}=\cosh\frac{\psi_b}{2}+i\sinh\frac{\psi_b}{2}\vec u$ | Boost rotor, Hermitian, in $\mathbb{M}_+$ |
| $\tilde U_{\vec v}$ | Lab-to-rest rotor, $\tilde U_{\vec v}\tilde{V}\tilde U_{\vec v}^{*}=ic\,e_t$ |
| $\tilde U_1\tilde U_2=\tilde U_{\mathrm b}\tilde{u}$ | Polar decomposition of a composition of boosts |
| $\tilde{u}\in\mathbb{H}_{\mathbb{B}}$ | Thomas–Wigner rotation (unit real quaternion) |
| $\varphi$, $\theta_W$, $\omega$ | Angle between boost directions; Wigner angle |
| $\vec a=d\vec v/dt$, $\vec a_\perp$ | Laboratory acceleration; its part perpendicular to $\vec v$ |
| $\tilde{M}=\tilde U_{\vec v+d\vec v}\tilde U^{\natural}_{\vec v}$ | Interval rotor between neighbouring rest frames |
| $\vec\omega_T=\frac{\gamma^2}{c^2(\gamma+1)}\vec a\times\vec v$ | Thomas precession angular velocity |
| $\vec\Omega$ | Orbital angular velocity (circular motion) |
| $\tilde{u}_T=\exp(\tfrac{1}{2}\theta_T\vec u_{\omega,\mu}\vec e_\mu)$ | Thomas rotor (half-angle) |
| $\vec r=r_\mu\vec e_\mu$ | Material spatial vector |
| $g$, $\gamma_g=gq/2m$ | Gyromagnetic factor and ratio |
| $\mathrm{Sc}$, $\mathrm{Tr}$ | Scalar part, trace; $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H) = 2\langle\tilde{P},\tilde{H}\rangle$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- L. H. Thomas, "The motion of the spinning electron," *Nature* **117** (1926) 514, for the original resolution of the spin–orbit factor of two.
- L. H. Thomas, "The kinematics of an electron with an axis," *Philosophical Magazine* **3** (1927) 1–22, for the kinematic derivation of the precession that bears his name.
- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group," *Annals of Mathematics* **40** (1939) 149–204, for the composition of Lorentz transformations and the rotation that accompanies it.
- V. Bargmann, L. Michel, and V. L. Telegdi, "Precession of the polarization of particles moving in a homogeneous electromagnetic field," *Physical Review Letters* **2** (1959) 435–436, for the covariant spin equation whose kinematic part is the Thomas precession.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the relativistic kinematics and the precession of a spinning particle.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the composition of Lorentz transformations, the Thomas precession, and its role in the spin–orbit coupling.
- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the kinematic treatment of the Thomas precession.
- W. Rindler, *Relativistic Kinematics* (Pergamon, 1966), and *Essential Relativity* (Springer, 1977), for the geometry of the boost transformations and the Wigner rotation.
- A. Ben-Menahem, "Wigner rotation and Thomas precession," *American Journal of Physics* **53** (1985) 62–68, for a direct derivation of the Wigner-angle formula and the precession rate.
- G. B. Malykin, "Thomas precession: correct and incorrect solutions," *Physics–Uspekhi* **49** (2006) 837–853, for a critical survey of the derivations and the common sign errors.
- C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of boosts and the composition of Lorentz transformations.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the double cover $SL(2,\mathbb{C})\to SO^+(1,3)$ and the half-angle rotors.
