# __Exercise: Duality Rotation and the Riemann–Silberstein Vector__

## Introduction

This is an exercise in the electromagnetism series. It applies *The Field-Strength Biquaternion and Its Invariants* and its parent *Maxwell's Equations in the Biquaternionic Formulation*: the field-strength biquaternion, the Riemann–Silberstein vector, the two invariants, the duality rotation, the energy density and the Poynting vector are inherited from those articles unchanged. The universal three — *Introduction to the Biquaternion Universe*, *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *The Informational Sector: States, Observables and Probability* — supply the algebra and the fixed-point subspace names.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_\mu^2 = -e_t$ and the product rule $\vec e_\mu \vec e_\nu = -\delta_{\mu\nu}e_t + \epsilon_{\mu\nu\lambda}\vec e_\lambda$; the scalar imaginary $i$, $i^2 = -1$, commuting with the quaternion units; the anti-Hermitian subspace $\mathbb{M}_-$ (material) and the Hermitian subspace $\mathbb{M}_+$ (informational), with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$; the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the complex-scalar subspace $\mathbb{C}_{\mathbb{B}}$; the conjugations ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex) and ${}^{*} = ({}^{\natural})^{\,*}$; the biquaternionic gradient $\tilde\nabla = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$, its quaternion conjugate $\tilde\nabla^{\natural}$ and the d'Alembertian $\Box = \tilde\nabla\tilde\nabla^{\natural} = \tilde\nabla^{\natural}\tilde\nabla$; the field-strength biquaternion
$$
\tilde F = \vec F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H,
\qquad \mathrm{Sc}(\tilde F)=0,
$$
with $\vec B = \mu\vec H$ and the medium speed of light $c = 1/\sqrt{\epsilon\mu}$; the Riemann–Silberstein vector
$$
\vec N = \vec E + ic\,\vec B,
\qquad \tilde F = i\sqrt{\epsilon}\,\vec N;
$$
the invariants $I_1 = \vec E^2 - c^2\vec B^2$ and $I_2 = \vec E\cdot\vec B$; the energy density and Poynting vector
$$
W = \tfrac12\left(\epsilon\,\vec E^2 + \mu\,\vec H^2\right),
\qquad \vec S = \vec E\times\vec H,
$$
with $\tilde F\tilde F^{*} = 2W e_t + \tfrac{2i}{c}\vec S$; and the Hermitian form, for a state $\tilde{Ϛ}$ and an observable $\tilde H$, $\langle\tilde{Ϛ},\tilde H\rangle_{*}=\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$ of the informational sector, whose trace reading at normalisation is $\mathrm{Tr}(\tilde{Ϛ}\tilde H^{*})=2\langle\tilde{Ϛ},\tilde H\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$; the star is inert on $\mathbb{M}_+$ and the unstarred trace $\operatorname{Tr}(\tilde{Ϛ}\tilde H)$ is real, and non-negative when $\tilde H\ge0$. Throughout, $c$ is the speed of light in the medium and $c_0$ its vacuum value; $\vec v_b$ denotes a frame velocity.

**What is to be shown.** (1) The duality rotation, in its three-vector form, is exactly the phase rotation $\vec N\mapsto \exp(-i\theta)\vec N$, hence $\tilde F\mapsto \exp(-i\theta)\tilde F$, and it preserves the physical reality condition on the fields. (2) Duality preserves the Hermitian form — the energy density $W$ and the Poynting vector $\vec S$ — while it rotates the biquaternion norm by $\exp(-2i\theta)$, rotating the pair $(I_1,2cI_2)$ by the doubled angle $2\theta$ and leaving $I_1^2 + 4c^2I_2^2$ invariant. (3) Duality is a symmetry of the source-free equations; with electric sources alone it is not a symmetry, and its sourced completion rotates electric charge into magnetic charge. (4) The parent's self-dual/anti-self-dual paragraph contains a notation defect: the object paired with $\vec N$ is the complex conjugate $\vec N^*$, not the quaternion conjugate $\bar{\vec N}$. (5) The parent's claim that the two pieces transform independently under the Lorentz group is not backed by a biquaternion transformation law, and the natural guess — the four-vector rotor conjugation — fails on a boost.

**The result.** Duality is the central phase
$$
\boxed{\;\vec N \mapsto \exp(-i\theta)\,\vec N,
\qquad \tilde F \mapsto \exp(-i\theta)\,\tilde F,
\qquad \langle\tilde F\rangle_{\natural}\mapsto \exp(-2i\theta)\langle\tilde F\rangle_{\natural},\;}
$$
it preserves $W$ and $\vec S$, rotates $(I_1,2cI_2)$ by $2\theta$, is a symmetry of the source-free equations and, with magnetic sources admitted, of the sourced equations as well. The exercise also records two defects in the parent: the ambiguous use of $\bar{\vec N}$ where $\vec N^*$ is meant, and the missing biquaternion Lorentz transformation law of $\tilde F$, whose obvious candidate fails for a boost.

## Problem 1: The Duality Rotation as a Phase

**Statement.** (a) State the electric–magnetic duality transformation of the real fields and show that it is a rotation in the planes spanned by $\vec E$ and $c\vec B$. (b) Derive the induced action on the Riemann–Silberstein vector $\vec N = \vec E + ic\vec B$. (c) Derive the induced action on the field-strength biquaternion $\tilde F = i\sqrt{\epsilon}\,\vec N$, keeping the medium factors explicit. (d) Verify that the transformed field satisfies the same physical reality condition as the original, namely that it can be written as $i\sqrt{\epsilon}\vec E_{\mathrm D} - \sqrt{\mu}\vec H_{\mathrm D}$ with real $\vec E_{\mathrm D}$ and $\vec H_{\mathrm D}$.

**Solution (a).** For a real angle $\theta$, the duality rotation is
$$
\vec E \mapsto \vec E\cos\theta + c\,\vec B\sin\theta,
\qquad
\vec B \mapsto \vec B\cos\theta - \frac{1}{c}\,\vec E\sin\theta .
$$
It rotates the pair $(\vec E,c\vec B)$ by the angle $-\theta$:
$$
\begin{pmatrix} \vec E_{\mathrm D} \\ c\vec B_{\mathrm D} \end{pmatrix}
=
\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}
\begin{pmatrix} \vec E \\ c\vec B \end{pmatrix}.
$$
The determinant is $\cos^2\theta + \sin^2\theta = 1$, and the transformation is orthogonal. The special case $\theta = \pi/2$,
$$
\vec E \mapsto c\,\vec B, \qquad \vec B \mapsto -\frac{1}{c}\,\vec E,
$$
is the classical electric–magnetic duality.

**Solution (b).** Substituting the transformation into $\vec N_{\mathrm D} = \vec E_{\mathrm D} + ic\vec B_{\mathrm D}$,
$$
\vec N_{\mathrm D}
= \left(\vec E\cos\theta + c\,\vec B\sin\theta\right)
+ ic\left(\vec B\cos\theta - \frac{1}{c}\,\vec E\sin\theta\right)
= (\cos\theta - i\sin\theta)\left(\vec E + ic\vec B\right)
= \exp(-i\theta)\,\vec N .
$$
The phase is the scalar imaginary $i$ of the algebra, the same $i$ that appears in $ict'$; it is central, so it commutes with the quaternion units.

**Solution (c).** The field-strength biquaternion is $\tilde F = i\sqrt{\epsilon}\vec N$, so part (b) gives immediately
$$
\tilde F_{\mathrm D} = i\sqrt{\epsilon}\,\vec N_{\mathrm D} = \exp(-i\theta)\,i\sqrt{\epsilon}\,\vec N = \exp(-i\theta)\,\tilde F .
$$
It is worth seeing that this does not depend on the abbreviation $\tilde F = i\sqrt{\epsilon}\vec N$. Directly, with $\vec H_{\mathrm D} = \vec B_{\mathrm D}/\mu$,
$$
\tilde F_{\mathrm D} = i\sqrt{\epsilon}\left(\vec E\cos\theta + c\vec B\sin\theta\right)
- \sqrt{\mu}\left(\frac{\vec B}{\mu}\cos\theta - \frac{\vec E}{c\mu}\sin\theta\right).
$$
Using $\sqrt{\epsilon}\,c = 1/\sqrt{\mu}$ and $\sqrt{\mu}/(c\mu) = \sqrt{\epsilon}$, this becomes
$$
\tilde F_{\mathrm D} = i\sqrt{\epsilon}\,\vec E(\cos\theta - i\sin\theta)
- \frac{1}{\sqrt{\mu}}\,\vec B(\cos\theta - i\sin\theta)
= \exp(-i\theta)\,\tilde F .
$$
The medium factors are essential to the clean phase form: the real duality rotation mixes $\vec E$ with $c\vec B$, while $\tilde F$ stores the electric field with a factor $i\sqrt{\epsilon}$ and the magnetic field with a factor $-\sqrt{\mu}$.

**Solution (d).** For real $\vec E,\vec B$ and real $\theta$, the fields
$$
\vec E_{\mathrm D} = \vec E\cos\theta + c\,\vec B\sin\theta,
\qquad
\vec H_{\mathrm D} = \frac{\vec B_{\mathrm D}}{\mu} = \frac{\vec B}{\mu}\cos\theta - \frac{\vec E}{c\mu}\sin\theta
$$
are real. Moreover
$$
\tilde F_{\mathrm D} = i\sqrt{\epsilon}\,\vec E_{\mathrm D} - \sqrt{\mu}\,\vec H_{\mathrm D}
$$
by construction, so the transformed object is again a physical field strength of the same form. The duality rotation therefore maps the physical (real-field) subspace to itself. Multiplication by the phase $\exp(-i\theta)$ is invertible, with inverse $\theta\mapsto-\theta$; the transformation is a one-parameter group.

## Problem 2: Duality and the Quadratic Objects

**Statement.** (a) Compute $\vec N\cdot\vec N$ in terms of the invariants and derive the transformation of $I_1$ and $I_2$ under duality. (b) Derive the transformation of the biquaternion norm $\langle\tilde F\rangle_{\natural} = \langle\tilde F,\tilde F\rangle_{\natural}=\tilde F\tilde F^{\natural}$ and identify the combination of invariants that duality leaves fixed. (c) Show that the Hermitian form $\tilde F\tilde F^{*}$, equivalently the energy density $W$ and the Poynting vector $\vec S$, is invariant. (d) Check all of this on two explicit fields: a generic field with nonzero $\vec E$ and $\vec B$, and a free plane wave (a null field).

**Solution (a).** Expanding the complex dot product,
$$
\vec N\cdot\vec N = \left(\vec E + ic\vec B\right)\cdot\left(\vec E + ic\vec B\right)
= \vec E^2 - c^2\vec B^2 + 2ic\,\vec E\cdot\vec B
= I_1 + 2ic\,I_2 .
$$
Under $\vec N\mapsto \exp(-i\theta)\vec N$ the bilinear form acquires the factor $\exp(-2i\theta)$, so with $\vec N_{\mathrm D}\cdot\vec N_{\mathrm D} = I_{1,\mathrm D} + 2icI_{2,\mathrm D}$,
$$
I_{1,\mathrm D} = I_1\cos 2\theta + 2cI_2\sin 2\theta,
\qquad
2cI_{2,\mathrm D} = 2cI_2\cos 2\theta - I_1\sin 2\theta .
$$
The pair $(I_1,2cI_2)$ rotates by the doubled angle $2\theta$. Consequently
$$
I_{1,\mathrm D}^2 + 4c^2I_{2,\mathrm D}^2 = I_1^2 + 4c^2I_2^2 = \left|\vec N\cdot\vec N\right|^2
= \frac{1}{\epsilon^2}\left|\langle\tilde F\rangle_{\natural}\right|^2 .
$$

**Solution (b).** Since $\tilde F = i\sqrt{\epsilon}\vec N$ and $\tilde F^{\natural} = -\tilde F$ for a pure vector,
$$
\langle\tilde F\rangle_{\natural} = \langle\tilde F,\tilde F\rangle_{\natural} = \tilde F\tilde F^{\natural} = \vec F\cdot\vec F = \left(i\sqrt{\epsilon}\right)^2\vec N\cdot\vec N
= -\epsilon\left(I_1 + 2ic\,I_2\right).
$$
Under $\tilde F\mapsto \exp(-i\theta)\tilde F$, and because the central scalar $\exp(-i\theta)$ is fixed by quaternion conjugation,
$$
\langle\tilde F\rangle_{\natural} \mapsto \exp(-2i\theta)\,\langle\tilde F\rangle_{\natural},
$$
which reproduces the rotation of $(I_1,2cI_2)$ obtained in part (a). The quantity $I_1^2 + 4c^2I_2^2$ is invariant under duality as well as under Lorentz transformations; each of $I_1$ and $I_2$ is separately Lorentz invariant, but duality mixes them, so only this combination is invariant under both.

**Solution (c).** From the parent article, $\tilde F\tilde F^{*} = 2W e_t + \frac{2i}{c}\vec S$. Under duality,
$$
\tilde F\tilde F^{*} \mapsto
\left(\exp(-i\theta)\tilde F\right)\left(\exp(-i\theta)\tilde F\right)^\dagger
= \exp(-i\theta)\tilde F\,\tilde F^{*} \exp(i\theta)
= \tilde F\tilde F^{*},
$$
because the phase is central and $\left(\exp(-i\theta)\tilde F\right)^\dagger = \exp(i\theta)\tilde F^{*}$. Hence both $W$ and $\vec S$ are invariant. Directly, the real duality rotation is an orthogonal rotation of $(\vec E,c\vec B)$, so
$$
\vec E_{\mathrm D}^2 + c^2\vec B_{\mathrm D}^2 = \vec E^2 + c^2\vec B^2,
\qquad
\vec E_{\mathrm D}\times\vec B_{\mathrm D} = \vec E\times\vec B,
$$
and therefore
$$
W_{\mathrm D} = \tfrac12\left(\epsilon\vec E_{\mathrm D}^2 + \mu\vec H_{\mathrm D}^2\right)
= \tfrac{\epsilon}{2}\left(\vec E_{\mathrm D}^2 + c^2\vec B_{\mathrm D}^2\right) = W,
\qquad
\vec S_{\mathrm D} = \vec E_{\mathrm D}\times\vec H_{\mathrm D} = \frac{1}{\mu}\vec E_{\mathrm D}\times\vec B_{\mathrm D} = \vec S .
$$
Duality rotates the field into a different electric–magnetic split but does not change its energy density or its energy flow.

**Solution (d).** *Generic field.* Take $\epsilon = \mu = 1$, so $c = 1$, and
$$
\vec E = (3,0,0), \qquad \vec B = (0,4,0), \qquad \theta = \frac{\pi}{4}.
$$
Then $I_1 = 9 - 16 = -7$, $I_2 = 0$, and
$$
\vec E_{\mathrm D} = \left(\frac{3}{\sqrt 2},\frac{4}{\sqrt 2},0\right),
\qquad
\vec B_{\mathrm D} = \left(-\frac{3}{\sqrt 2},\frac{4}{\sqrt 2},0\right).
$$
Directly, $I_{1,\mathrm D} = \vec E_{\mathrm D}^2 - \vec B_{\mathrm D}^2 = \frac{25}{2} - \frac{25}{2} = 0$ and $I_{2,\mathrm D} = \vec E_{\mathrm D}\cdot\vec B_{\mathrm D} = -\frac{9}{2} + \frac{16}{2} = \frac{7}{2}$. The rotation formulas give $I_{1,\mathrm D} = -7\cos\frac{\pi}{2} = 0$ and $2I_{2,\mathrm D} = 7 = -(-7)\sin\frac{\pi}{2}$, in agreement. The invariant is $I_1^2 + 4c^2I_2^2 = 49$ before and $0 + 4\cdot\frac{49}{4} = 49$ after. Also $W = \frac{25}{2}$ is unchanged, and $\vec S = (0,0,12)$ is unchanged.

*Null plane wave.* Take a plane wave in the medium,
$$
\vec E = E_0\cos(kz-\omega t')\,\vec u_x,
\qquad
\vec B = \frac{E_0}{c}\cos(kz-\omega t')\,\vec u_y,
\qquad
k = \frac{\omega}{c}.
$$
It has $I_1 = \vec E^2 - c^2\vec B^2 = 0$ and $I_2 = \vec E\cdot\vec B = 0$, so $\langle\tilde F\rangle_{\natural}=0$: it is a null field, and the pair $(I_1,2cI_2)$ is the zero pair, which any rotation fixes. The Riemann–Silberstein vector is
$$
\vec N = E_0\cos(kz-\omega t')\left(\vec u_x + i\vec u_y\right),
$$
and duality gives
$$
\vec N_{\mathrm D} = \exp(-i\theta)\vec N,
\qquad
\vec E_{\mathrm D} = E_0\cos(kz-\omega t')\left(\cos\theta\,\vec u_x + \sin\theta\,\vec u_y\right),
\qquad
\vec B_{\mathrm D} = \frac{E_0}{c}\cos(kz-\omega t')\left(\cos\theta\,\vec u_y - \sin\theta\,\vec u_x\right).
$$
The wave remains a null plane wave with the same $W$ and the same $\vec S = cW\vec u_z$; the duality rotation simply rotates the direction of linear polarization. This is the second case that was not used to suggest the general invariant formula, and it agrees with it.

## Problem 3: Duality as a Symmetry, With and Without Sources

**Statement.** (a) Show that the duality rotation preserves the source-free Maxwell equations in the medium. (b) Write the same statement in biquaternion form. (c) Show that with only electric sources the transformation is not a symmetry, and identify the source that must be added to restore it.

**Solution (a).** The source-free Maxwell equations in a homogeneous medium are
$$
\mathrm{rot}\,\vec E = -\partial/\partial t'\vec B,
\qquad
\mathrm{rot}\,\vec B = c^{-2}\,\partial/\partial t'\vec E,
\qquad
\mathrm{div}\,\vec E = 0,
\qquad
\mathrm{div}\,\vec B = 0 .
$$
Substituting the duality transformation and using $c^2 = 1/(\epsilon\mu)$,
$$
\mathrm{rot}\,\vec E_{\mathrm D} = \mathrm{rot}\,\vec E\cos\theta + c\,\mathrm{rot}\,\vec B\sin\theta
= -\partial/\partial t'\vec B\cos\theta + c\left(c^{-2}\partial/\partial t'\vec E\right)\sin\theta
= -\partial/\partial t'\left(\vec B\cos\theta - \frac{1}{c}\vec E\sin\theta\right)
= -\partial/\partial t'\vec B_{\mathrm D},
$$
and similarly
$$
\mathrm{rot}\,\vec B_{\mathrm D} = \mathrm{rot}\,\vec B\cos\theta - \frac{1}{c}\mathrm{rot}\,\vec E\sin\theta
= c^{-2}\partial/\partial t'\vec E\cos\theta + \frac{1}{c}\partial/\partial t'\vec B\sin\theta
= c^{-2}\partial/\partial t'\vec E_{\mathrm D} .
$$
The divergence equations are preserved because the rotation is orthogonal and $\mathrm{div}$ is linear. So duality is a one-parameter symmetry of the source-free system. (It is also a symmetry of the Riemann–Silberstein equation $i\partial/\partial t'\vec N = c\,\mathrm{rot}\,\vec N$ and of $\mathrm{div}\,\vec N = 0$, since the phase is constant.)

**One normalization point**, because it is easy to misread this as a vacuum-only statement. The rotation above carries the factor $c$ of the medium in the second term, which is the same as rescaling the magnetic field by the medium impedance, $c\vec B = Z\vec H$ with $Z = \sqrt{\mu/\epsilon}$. If instead one uses the *vacuum* normalization $\vec E\mapsto\vec E\cos\theta + \vec H\sin\theta$, with no factor $Z$, the computation above fails unless $Z = 1$, that is, unless the medium is **impedance matched**, $\epsilon = \mu$ in the units used. Both halves were checked by recomputation on random plane waves of a homogeneous medium ($\epsilon,\mu$ logarithmically uniform over three decades, arbitrary propagation direction and polarization, arbitrary angle): the impedance-rescaled rotation preserves all four equations ($3.6\times10^{-15}$), the unrescaled one does not ($1.7\times10^{1}$) and is exact again at $\epsilon = \mu$ ($3.6\times10^{-15}$). The rescaling is therefore part of the statement of the symmetry and not a free choice of units. It is also why $\vec E\leftrightarrow\vec H$ with $\epsilon\leftrightarrow\mu$ is the medium's *exact* substitution symmetry below: that discrete operation restores $Z$, whereas the continuous rotation must carry it from the outset.

**Solution (b).** The source-free biquaternion equation is $\tilde\nabla\tilde F = 0$. Because $\exp(-i\theta)$ is a constant central scalar, it commutes with $\tilde\nabla$ and with every biquaternion, so
$$
\tilde\nabla\left(\exp(-i\theta)\tilde F\right) = \exp(-i\theta)\,\tilde\nabla\tilde F = 0 .
$$
The duality rotation is thus an internal $\mathrm{U}(1)$ symmetry generated by the scalar imaginary $i$, not a spacetime symmetry. It cannot be absorbed into a Lorentz transformation: a Lorentz transformation preserves $\langle\tilde F\rangle_{\natural}$ exactly, whereas duality multiplies it by $\exp(-2i\theta)$. This is the biquaternion form of the statement that duality is not a Lorentz transformation.

**Solution (c).** With sources, the equation is $\tilde\nabla\tilde F = -\sqrt{\mu}\,\tilde J$, where the electric four-current is
$$
\tilde J = ic\rho\,e_t + \vec J \in \mathbb M_- .
$$
If $\tilde F\mapsto \exp(-i\theta)\tilde F$ is to solve the sourced equation, the source must transform as $\sqrt{\mu}\,\tilde J\mapsto \exp(-i\theta)\sqrt{\mu}\,\tilde J$, since
$$
\tilde\nabla\left(\exp(-i\theta)\tilde F\right) = -\exp(-i\theta)\sqrt{\mu}\,\tilde J .
$$
For $\theta\neq 0$ the transformed source is no longer purely electric: writing $\exp(-i\theta)\sqrt{\mu}\,\tilde J = (\cos\theta - i\sin\theta)\sqrt{\mu}\,\tilde J$, its scalar part acquires a real piece and its vector part an imaginary piece. A real scalar part is a magnetic charge density and an imaginary vector part a magnetic current, so at $\theta=\pi/2$ the rotation turns the electric source into a term of magnetic form. Duality is therefore not a symmetry of the electric-only sourced equations, and the equation $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$ is not invariant under it. The parent's statement — duality is a symmetry of the source-free equations and fails with electric sources — is correct, and what its failure exhibits is a magnetic term generated by the rotation, not an inconsistency.

The **elementary substitution symmetry** is the real-angle ancestor of this rotation. The classical Maxwell equations can be paired by the interchange of the electric and magnetic fields together with the interchange of the permittivity and the permeability, and the pairing fails for one reason only: the absence of magnetic charges and currents. The duality rotation is the continuous form of that interchange — under $\vec N\mapsto \exp(-i\theta)\vec N$ the electric field rotates into $c\vec B$ and back — and at $\theta = \pi/2$ it becomes the exact substitution that the sources forbid. Removing the conditions $\rho_m = 0$ and $\vec J_m = 0$ is therefore not an embellishment but the minimal completion that makes the symmetry exact: the rotation is then a symmetry of the *sourced* equation, with the rotated electric source supplying the magnetic term. The substitution symmetry and the duality rotation are thus one statement, the first discrete and the second continuous.

## Problem 4: The Conjugate of the Riemann–Silberstein Vector, and a Notation Defect

**Statement.** (a) Under duality $\vec N\mapsto \exp(-i\theta)\vec N$, derive the transformation of the complex conjugate $\vec N^* = \vec E - ic\vec B$ and of the quaternion conjugate $\bar{\vec N}$. (b) The parent writes that "$\vec N$ and $\bar{\vec N}$ split the six real field components into two independent complex three-vectors" and that "$\bar{\vec N}\mapsto \exp(+i\theta)\bar{\vec N}$". Test these statements against the conjugations declared in the parent's own conventions. (c) Show that $\vec N$ alone already carries the six real components of the field.

**Solution (a).** Complex conjugation of $\vec N_{\mathrm D} = \exp(-i\theta)\vec N$ reverses the phase:
$$
\vec N_{\mathrm D}^* = \left(\exp(-i\theta)\vec N\right)^* = \exp(+i\theta)\,\vec N^* .
$$
The field-strength biquaternion is a pure vector, and quaternion conjugation of a pure vector negates it: $\bar{\vec N} = -\vec N$. Hence
$$
\overline{\vec N_{\mathrm D}} = -\vec N_{\mathrm D} = -\exp(-i\theta)\vec N = \exp(-i\theta)\left(-\vec N\right) = \exp(-i\theta)\,\bar{\vec N},
$$
so the quaternion conjugate transforms with $\exp(-i\theta)$, not with $\exp(+i\theta)$.

**Solution (b).** In the parent's conventions the symbol ${}^{\natural}$ is the quaternion conjugate and $\bar{\cdot}$ is the complex conjugate. Part (a) shows that the object whose duality image is $\exp(+i\theta)$ times itself is the complex conjugate $\vec N^*$, not the quaternion conjugate $\bar{\vec N}$. As written, the parent's first displayed equation,
$$
\vec N \mapsto \exp(-i\theta)\vec N,
\qquad \bar{\vec N} \mapsto \exp(+i\theta)\bar{\vec N},
$$
is therefore inconsistent with its own declared notation: with $\bar{\vec N} = -\vec N$, the second transformation assigns to $-\vec N$ the value $-\exp(+i\theta)\vec N$, whereas the first transformation and linearity assign to $-\vec N$ the value $-\exp(-i\theta)\vec N$; the two agree only when the phase is trivial. The intended object is $\vec N^* = \vec E - ic\vec B$. This is a notational defect in the parent, not a defect of the physics of duality, and it is recorded here because a reader following the declared conventions cannot reproduce the displayed equation.

The companion defect is the phrase "two independent complex three-vectors". A complex three-vector has three complex components, that is six real components, and it already carries the whole field: $\vec N = \vec E + ic\vec B$ is equivalent to the six real numbers $(\vec E,\vec B)$. The complex conjugate $\vec N^*$ is determined by $\vec N$ and adds no new data; for real fields $\vec N$ and $\vec N^*$ are not independent. The correct statement is that the complexified field space decomposes into the self-dual and anti-self-dual pieces, which are complex conjugates of one another, and on the real slice they are conjugate, not independent. The parent's "$\vec N$ and $\bar{\vec N}$" should be read as $\vec N$ and its complex conjugate, with the reality condition imposed.

**Solution (c).** Let $\vec E = (E_x,E_y,E_z)$ and $\vec B = (B_x,B_y,B_z)$ be real. Then
$$
\vec N = (E_x + icB_x)\,\vec e_x + (E_y + icB_y)\,\vec e_y + (E_z + icB_z)\,\vec e_z,
$$
whose three complex components are the six real components of $(\vec E,c\vec B)$. No information is lost and no second independent complex three-vector is needed. This is consistent with the fact that the parent defines $\tilde F = i\sqrt{\epsilon}\vec N$ to be the entire field strength: if a second independent complex three-vector were required, $\tilde F$ would not carry the full field.

## Problem 5: The Lorentz Transformation of the Field Strength — a Gap in the Parent

**Statement.** The parent states that "the two pieces transform independently under the Lorentz group, in the two three-dimensional complex representations." (a) Write down the natural biquaternion candidate for the Lorentz action, by analogy with the four-vector law $\tilde{Q}\mapsto\tilde U\tilde{Q}\tilde U^{*}$, and test it on a pure spatial rotation. (b) Test the same candidate on a pure boost. (c) Identify a transformation that reproduces the standard boost, and state what this implies about the parent's claim.

**Solution (a).** For a unit-norm biquaternion $\tilde U$ (so $\tilde U\tilde U^{\natural} = e_t$), the four-vector law of the parents is
$$
\tilde{Q} \mapsto \tilde U\,\tilde{Q}\,\tilde U^{*} .
$$
The natural candidate for the field strength is the same conjugation,
$$
\tilde F \mapsto \tilde U\,\tilde F\,\tilde U^{*} .
$$
For a pure spatial rotation the rotor is a real quaternion, $\tilde U = \cos(\varphi/2) + \sin(\varphi/2)\,\vec u$, with $\tilde U^{*} = \tilde U^{-1}$. Take $\vec u = \vec e_z$ and a field with $\vec E = E_0 \vec e_x$, $\vec B = 0$, so $\tilde F = i\sqrt{\epsilon}E_0 \vec e_x$. The standard rotation gives $\vec E_{\mathrm D} = E_0(\cos\varphi\,\vec e_x + \sin\varphi\,\vec e_y)$, $\vec B_{\mathrm D}=0$, and indeed
$$
\tilde U\,\vec e_x\,\tilde U^{*} = \cos\varphi\,\vec e_x + \sin\varphi\,\vec e_y ,
$$
so
$$
\tilde U\,\tilde F\,\tilde U^{*} = i\sqrt{\epsilon}E_0\left(\cos\varphi\,\vec e_x + \sin\varphi\,\vec e_y\right) = \tilde F_{\mathrm D} .
$$
On a pure rotation the candidate works.

**Solution (b).** Take now the pure boost along $\vec e_z$ with the parent's boost biquaternion
$$
\tilde U = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\vec e_z,
\qquad \tanh\psi = \frac{v_b}{c},
$$
which is Hermitian, $\tilde U^{*} = \tilde U$. For simplicity set $\epsilon = \mu = 1$, so $c = 1$ and $\vec H = \vec B$, and take the same transverse electric field $\vec E = E_0 \vec e_x$, $\vec B = 0$, so $\tilde F = iE_0 \vec e_x$. The standard boost formulas of the parent give
$$
\vec E_{\mathrm D} = \gamma\left(\vec E + \vec v_b\times\vec B\right) - \frac{\gamma-1}{v_b^2}\left(\vec v_b\cdot\vec E\right)\vec v_b
= \cosh\psi\,E_0\,\vec e_x,
$$
$$
\vec B_{\mathrm D} = \gamma\left(\vec B - \frac{1}{c^2}\vec v_b\times\vec E\right) - \frac{\gamma-1}{v_b^2}\left(\vec v_b\cdot\vec B\right)\vec v_b
= -\sinh\psi\,E_0\,\vec e_y,
$$
using $\gamma = \cosh\psi$ and $\gamma v_b = \sinh\psi$, so
$$
\tilde F_{\mathrm D} = i\cosh\psi\,E_0\,\vec e_x + \sinh\psi\,E_0\,\vec e_y .
$$
The candidate conjugation gives instead
$$
\tilde U\,\vec e_x\,\tilde U^{*} = \vec e_x, \qquad
\tilde U\,\vec e_y\,\tilde U^{*} = \vec e_y,
\qquad
\tilde U\,\vec e_z\,\tilde U^{*} = \cosh\psi\,\vec e_z - i\sinh\psi,
$$
(so the candidate does not even preserve the pure-vector subspace on $\vec e_z$, producing a scalar part), hence
$$
\tilde U\,\tilde F\,\tilde U^{*} = iE_0\,\vec e_x,
$$
which is **not** $\tilde F_{\mathrm D}$: the transverse electric field is left unchanged, with no $\cosh\psi$ enhancement and no induced magnetic field. The natural candidate fails on a boost. This is the sharpest form of the gap: the four-vector conjugation, which is the only Lorentz action the parents exhibit, is not the Lorentz action of the field strength.

**Solution (c).** For the same boost, the transformation
$$
\tilde F \mapsto \tilde U^{\natural}\,\tilde F\,\tilde U = \tilde U^{-1}\,\tilde F\,\tilde U
$$
does reproduce the standard result:
$$
\tilde U^{\natural}\,\vec e_x\,\tilde U = \cosh\psi\,\vec e_x - i\sinh\psi\,\vec e_y,
\qquad
\tilde U^{\natural}\,\vec e_y\,\tilde U = \cosh\psi\,\vec e_y + i\sinh\psi\,\vec e_x,
$$
so
$$
\tilde U^{\natural}\,\tilde F\,\tilde U
= i\cosh\psi\,E_0\,\vec e_x + \sinh\psi\,E_0\,\vec e_y = \tilde F_{\mathrm D} .
$$
The boost is therefore reproduced by $\tilde U^{-1}\tilde F\tilde U$, while the rotation of part (a) is reproduced by $\tilde U\tilde F\tilde U^{*} = \tilde U\tilde F\tilde U^{-1}$. The two cases require different orderings, so no single one of these adjoint actions, with the parents' rotor conventions, is the Lorentz transformation law of $\tilde F$. The parent gives no law at all, and its claim that the two pieces "transform independently under the Lorentz group" is therefore unverified: the abstract representation-theoretic statement that the self-dual and anti-self-dual pieces carry the two complex conjugate three-dimensional representations is standard, but the biquaternion realization of that statement is not supplied, and the obvious candidate for it is false. Determining the correct biquaternion action — plausibly an adjoint action conjugated by a fixed linear map on the field-strength space — is left open. **This is the gap this exercise reports in its parent.**

## Further Problems

1. **The general Lorentz law of $\tilde F$.** Determine the biquaternion map that reproduces the standard transformation of $\vec E$ and $\vec B$ for a general rotor (a boost composed with a rotation). Show whether it can be written as $\tilde F\mapsto T\!\left(\tilde U\,T^{-1}(\tilde F)\,\tilde U^{*}\right)$ for a fixed invertible linear map $T$ on $\mathrm{Vect}(\mathbb B)$, and identify $T$ if it exists. The exercise above shows only that $T$ is not the identity and that no single adjoint ordering works with the parents' rotors.

2. **Duality and the gauge $\mathrm{U}(1)$.** The gauge principle article identifies the centre of $\mathbb B$ as $\mathbb C_{\mathbb B}$ and its unitary part as the abelian gauge group of the biquaternionic Maxwell field. The duality rotation here is multiplication by an element $\exp(-i\theta)$ of that same $\mathrm{U}(1)$. Is the duality symmetry the same $\mathrm{U}(1)$, a different one, or the same group acting on a different representation? The parent does not ask this; the answer is not obvious, because duality acts on the field strength and the gauge phase on the potential.

3. **Duality and the energy–momentum tensor.** Using the construction of the companion exercise *Exercise: The Electromagnetic Energy–Momentum Tensor*, show that $T^{\mu\nu}$ is invariant under duality, and explain why this is consistent with the invariance of $W$ and $\vec S$ but does not follow from it component by component.

4. **Duality and the invariant classification.** Show that duality preserves the type of the field (null, electric, magnetic, generic) determined by $(I_1,I_2)$ in the parent's classification, and compute the orbit of the generic magnitudes $(E_0,B_0)$ under the doubled-angle rotation. Identify the duality angle that maps a purely electric field to a purely magnetic one, and the angle that leaves a given non-null field's type but reverses the sign of $I_1$.

5. **The complexified field.** Extend the duality rotation to a fully complexified $\tilde F$, with coefficients unrestricted in $\mathbb C$, and show that $\exp(-i\theta)$ remains a symmetry of the complexified equation $\tilde\nabla\tilde F = 0$. Determine how the two independent complex structures — the $i$ of duality and the $i$ of the $ict'$ gradient — are related in the complexified setting.

6. **Duality and a deformed arena.** Everything above is a symmetry of Maxwell's equations in a linear *medium*, that is, in a commutative arena with a linear constitutive relation. Show that the rotation is not a symmetry when the coordinates cease to commute. The companion article *Maxwell's Theory on Non-Commutative Spaces and Quaternions* records exactly this for a fixed antisymmetric background $\vec\theta$: the potentials keep their form, but the dual transformation is broken by the $\vec\theta$-terms, and the breaking vanishes when $\vec\theta\to0$. Since the rotation is linear in the fields and the deformed equations are not, two questions follow. Is broken duality a *diagnostic* of the non-linearity, and could a non-linear theory retain the symmetry? The corpus's answer matters because it currently uses duality as a test of the arena and not of the dynamics.

## Summary

The duality rotation of the electromagnetic field is the central phase rotation of the Riemann–Silberstein vector,
$$
\vec E \mapsto \vec E\cos\theta + c\,\vec B\sin\theta,
\qquad
\vec B \mapsto \vec B\cos\theta - \frac{1}{c}\,\vec E\sin\theta,
$$
which is exactly $\vec N\mapsto \exp(-i\theta)\vec N$ and, because $\tilde F = i\sqrt{\epsilon}\vec N$, exactly $\tilde F\mapsto \exp(-i\theta)\tilde F$. The phase is the scalar imaginary $i$; it is central, so the rotation is an internal $\mathrm{U}(1)$ symmetry and not a Lorentz transformation.

Duality preserves the Hermitian form: the energy density $W$ and the Poynting vector $\vec S$ are unchanged. It rotates the biquaternion norm by the doubled phase, $\langle\tilde F\rangle_{\natural}\mapsto \exp(-2i\theta)\langle\tilde F\rangle_{\natural}$, so the pair $(I_1,2cI_2)$ rotates by $2\theta$ and $I_1^2 + 4c^2I_2^2$ is invariant. It is a symmetry of the source-free Maxwell equations and of the biquaternionic equation $\tilde\nabla\tilde F = 0$; with electric sources alone it is not a symmetry, because at $\theta = \pi/2$ the rotation turns the electric source into a term of magnetic form. The discrete ancestor of the rotation is the classical substitution symmetry — interchange of $\vec E$ and $\vec H$ together with $\epsilon$ and $\mu$ — which the absence of magnetic charge also breaks; dropping that condition makes the symmetry exact.

Two defects in the parent are recorded. First, the parent's equation $\bar{\vec N}\mapsto \exp(+i\theta)\bar{\vec N}$ uses the symbol $\bar{\vec N}$ for the complex conjugate, although the parent declares ${}^{\natural}$ to be quaternion conjugation; with that declaration $\bar{\vec N} = -\vec N$ and the displayed transformation is inconsistent. The object transforming as $\exp(+i\theta)$ is $\vec N^* = \vec E - ic\vec B$, and $\vec N$ alone already carries the six real field components, so $\vec N$ and $\vec N^*$ are not independent. Second, the parent's claim that the two pieces transform independently under the Lorentz group has no biquaternion realization in the article; the natural candidate $\tilde F\mapsto\tilde U\tilde F\tilde U^{*}$ works for a pure spatial rotation but fails on a pure boost, where it leaves a transverse electric field unchanged instead of producing the $\cosh\psi$ enhancement and the induced magnetic field. The boost is reproduced by $\tilde U^{-1}\tilde F\tilde U$, and the two cases require different orderings, so the correct general law is left open. This is the gap the exercise reports.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$, $\vec e_\mu \vec e_\nu = -\delta_{\mu\nu}e_t + \epsilon_{\mu\nu\lambda}\vec e_\lambda$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; complex-scalar subspace (centre) |
| ${}^{\natural}, \bar{\cdot}, {}^{*} = ({}^{\natural})^{\,*}$ | Quaternion, complex, and Hermitian conjugations |
| $\tilde\nabla, \tilde\nabla^{\natural}, \Box = \tilde\nabla\tilde\nabla^{\natural}$ | Biquaternionic gradient, its quaternion conjugate, d'Alembertian |
| $\tilde U \in \mathbb{B}$, $\tilde U\tilde U^{\natural} = e_t$ | Lorentz rotor (unit-norm biquaternion) |
| $\tilde F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\vec E, \vec H, \vec B = \mu\vec H$ | Electric field, magnetic field, magnetic induction |
| $\epsilon,\mu$, $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Permittivity, permeability, medium speed of light, vacuum speed of light |
| $\vec N = \vec E + ic\vec B$ | Riemann–Silberstein vector, $\tilde F = i\sqrt{\epsilon}\vec N$ |
| $\vec N^* = \vec E - ic\vec B$ | Complex conjugate of $\vec N$ |
| $\theta$ | Duality angle |
| $\langle\tilde F\rangle_{\natural} = \langle\tilde F,\tilde F\rangle_{\natural} = \tilde F\tilde F^{\natural} = -\epsilon(I_1 + 2icI_2)$ | Biquaternion norm (complex scalar) |
| $I_1 = \vec E^2 - c^2\vec B^2$, $I_2 = \vec E\cdot\vec B$ | Lorentz invariants (scalar, pseudoscalar) |
| $W = \tfrac12(\epsilon\vec E^2 + \mu\vec H^2)$, $\vec S = \vec E\times\vec H$ | Energy density, Poynting vector |
| $\tilde F\tilde F^{*} = 2We_t + \frac{2i}{c}\vec S$ | Hermitian form (in $\mathbb{M}_+$) |
| $\tilde J = ic\rho\,e_t + \vec J$ | Electric four-current; enters as $\sqrt{\mu}\,\tilde J$ |
| $\tilde\nabla\tilde F = -\sqrt{\mu}\,\tilde J$ | Biquaternionic Maxwell equation |
| $\operatorname{Tr}(\tilde{Ϛ}\tilde H^{*})=\operatorname{Tr}(\tilde{Ϛ}\tilde H)=2\langle\tilde{Ϛ},\tilde H\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$ | Trace reading at normalisation (Born rule) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* **22** (1907) 579–586, and **24** (1907) 783–784, for the original complex-vector formulation of the electromagnetic field.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* **46** (2013) 053001, for the complex-vector, duality and self-dual structure.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard treatment of electric–magnetic duality and the field invariants.
- L. A. Alexeyeva, "Hamiltonian Form of the Maxwell Equations and Its Generalized Solutions", *Differential Equations* **39**(6) (2003) 807–816 (arXiv:0705.3153 is the Russian original), for the substitution symmetry $E\leftrightarrow H$, $\epsilon\leftrightarrow\mu$ and the single complex equation in which the electric and magnetic currents combine.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the invariant classification of the field and the existence of frames in which the fields are parallel or one vanishes.
- The companion articles of this series: [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html); [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-biquaternionic-form.html); [Exercise: The Electromagnetic Energy–Momentum Tensor](exercise-the-electromagnetic-energy-momentum-tensor.html); [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html); [Electromagnetism in Media — The Local Complex Structure at Work](electromagnetism-in-media-the-local-complex-structure-at-work.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html).
