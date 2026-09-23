# __Exercise: Duality Rotation and the Riemann–Silberstein Vector__

## Introduction

This is an exercise in the electromagnetism series. It applies *The Field-Strength Biquaternion and Its Invariants* and its parent *Maxwell's Equations in the Biquaternionic Formulation*: the field-strength biquaternion, the Riemann–Silberstein vector, the two invariants, the duality rotation, the energy density and the Poynting vector are inherited from those articles unchanged. The universal three — *Introduction to the Biquaternion Universe*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — supply the algebra and the fixed-point subspace names.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and the product rule $e_je_k = -\delta_{jk}e_0 + \epsilon_{jkm}e_m$; the scalar imaginary $i$, $i^2 = -1$, commuting with the quaternion units; the anti-Hermitian subspace $\mathbb{M}_-$ (material) and the Hermitian subspace $\mathbb{M}_+$ (informational), with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$; the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the complex-scalar subspace $\mathbb{C}_{\mathbb{B}}$; the conjugations $\bar{\cdot}$ (quaternion), ${}^*$ (complex) and ${}^\dagger = \bar{\cdot}^{\,*}$; the biquaternionic gradient $\tilde\nabla = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate $\bar{\tilde\nabla}$ and the d'Alembertian $\Box = \tilde\nabla\bar{\tilde\nabla} = \bar{\tilde\nabla}\tilde\nabla$; the field-strength biquaternion
$$
\tilde F = \mathbf F = i\sqrt{\epsilon}\,\mathbf E - \sqrt{\mu}\,\mathbf H,
\qquad \mathrm{Sc}(\tilde F)=0,
$$
with $\mathbf B = \mu\mathbf H$ and the medium speed of light $c = 1/\sqrt{\epsilon\mu}$; the Riemann–Silberstein vector
$$
\mathbf V = \mathbf E + ic\,\mathbf B,
\qquad \tilde F = i\sqrt{\epsilon}\,\mathbf V;
$$
the invariants $I_1 = \mathbf E^2 - c^2\mathbf B^2$ and $I_2 = \mathbf E\cdot\mathbf B$; the energy density and Poynting vector
$$
W = \tfrac12\left(\epsilon\,\mathbf E^2 + \mu\,\mathbf H^2\right),
\qquad \mathbf S = \mathbf E\times\mathbf H,
$$
with $\tilde F\tilde F^\dagger = 2W e_0 + \tfrac{2i}{c}\mathbf S$; and the trace formula $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$ of the informational sector. Throughout, $c$ is the speed of light in the medium and $c_0$ its vacuum value; $\mathbf v$ (and $\mathbf u$) denotes a frame velocity.

**What is to be shown.** (1) The duality rotation, in its three-vector form, is exactly the phase rotation $\mathbf V\mapsto e^{-i\theta}\mathbf V$, hence $\tilde F\mapsto e^{-i\theta}\tilde F$, and it preserves the physical reality condition on the fields. (2) Duality preserves the Hermitian form — the energy density $W$ and the Poynting vector $\mathbf S$ — while it rotates the norm form by $e^{-2i\theta}$, rotating the pair $(I_1,2cI_2)$ by the doubled angle $2\theta$ and leaving $I_1^2 + 4c^2I_2^2$ invariant. (3) Duality is a symmetry of the source-free equations; with electric sources alone it is not a symmetry, and its sourced completion rotates electric charge into magnetic charge. (4) The parent's self-dual/anti-self-dual paragraph contains a notation defect: the object paired with $\mathbf V$ is the complex conjugate $\mathbf V^*$, not the quaternion conjugate $\bar{\mathbf V}$. (5) The parent's claim that the two pieces transform independently under the Lorentz group is not backed by a biquaternion transformation law, and the natural guess — the four-vector rotor conjugation — fails on a boost.

**The result.** Duality is the central phase
$$
\boxed{\;\mathbf V \mapsto e^{-i\theta}\,\mathbf V,
\qquad \tilde F \mapsto e^{-i\theta}\,\tilde F,
\qquad N(\tilde F)\mapsto e^{-2i\theta}N(\tilde F),\;}
$$
it preserves $W$ and $\mathbf S$, rotates $(I_1,2cI_2)$ by $2\theta$, is a symmetry of the source-free equations and, with magnetic sources admitted, of the sourced equations as well. The exercise also records two defects in the parent: the ambiguous use of $\bar{\mathbf V}$ where $\mathbf V^*$ is meant, and the missing biquaternion Lorentz transformation law of $\tilde F$, whose obvious candidate fails for a boost.

## Problem 1: The Duality Rotation as a Phase

**Statement.** (a) State the electric–magnetic duality transformation of the real fields and show that it is a rotation in the planes spanned by $\mathbf E$ and $c\mathbf B$. (b) Derive the induced action on the Riemann–Silberstein vector $\mathbf V = \mathbf E + ic\mathbf B$. (c) Derive the induced action on the field-strength biquaternion $\tilde F = i\sqrt{\epsilon}\,\mathbf V$, keeping the medium factors explicit. (d) Verify that the transformed field satisfies the same physical reality condition as the original, namely that it can be written as $i\sqrt{\epsilon}\mathbf E' - \sqrt{\mu}\mathbf H'$ with real $\mathbf E'$ and $\mathbf H'$.

**Solution (a).** For a real angle $\theta$, the duality rotation is
$$
\mathbf E \mapsto \mathbf E\cos\theta + c\,\mathbf B\sin\theta,
\qquad
\mathbf B \mapsto \mathbf B\cos\theta - \frac{1}{c}\,\mathbf E\sin\theta .
$$
It rotates the pair $(\mathbf E,c\mathbf B)$ by the angle $-\theta$:
$$
\begin{pmatrix} \mathbf E' \\ c\mathbf B' \end{pmatrix}
=
\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}
\begin{pmatrix} \mathbf E \\ c\mathbf B \end{pmatrix}.
$$
The determinant is $\cos^2\theta + \sin^2\theta = 1$, and the transformation is orthogonal. The special case $\theta = \pi/2$,
$$
\mathbf E \mapsto c\,\mathbf B, \qquad \mathbf B \mapsto -\frac{1}{c}\,\mathbf E,
$$
is the classical electric–magnetic duality.

**Solution (b).** Substituting the transformation into $\mathbf V' = \mathbf E' + ic\mathbf B'$,
$$
\mathbf V'
= \left(\mathbf E\cos\theta + c\,\mathbf B\sin\theta\right)
+ ic\left(\mathbf B\cos\theta - \frac{1}{c}\,\mathbf E\sin\theta\right)
= (\cos\theta - i\sin\theta)\left(\mathbf E + ic\mathbf B\right)
= e^{-i\theta}\,\mathbf V .
$$
The phase is the scalar imaginary $i$ of the algebra, the same $i$ that appears in $ict$; it is central, so it commutes with the quaternion units.

**Solution (c).** The field-strength biquaternion is $\tilde F = i\sqrt{\epsilon}\mathbf V$, so part (b) gives immediately
$$
\tilde F' = i\sqrt{\epsilon}\,\mathbf V' = e^{-i\theta}\,i\sqrt{\epsilon}\,\mathbf V = e^{-i\theta}\,\tilde F .
$$
It is worth seeing that this does not depend on the abbreviation $\tilde F = i\sqrt{\epsilon}\mathbf V$. Directly, with $\mathbf H' = \mathbf B'/\mu$,
$$
\tilde F' = i\sqrt{\epsilon}\left(\mathbf E\cos\theta + c\mathbf B\sin\theta\right)
- \sqrt{\mu}\left(\frac{\mathbf B}{\mu}\cos\theta - \frac{\mathbf E}{c\mu}\sin\theta\right).
$$
Using $\sqrt{\epsilon}\,c = 1/\sqrt{\mu}$ and $\sqrt{\mu}/(c\mu) = \sqrt{\epsilon}$, this becomes
$$
\tilde F' = i\sqrt{\epsilon}\,\mathbf E(\cos\theta - i\sin\theta)
- \frac{1}{\sqrt{\mu}}\,\mathbf B(\cos\theta - i\sin\theta)
= e^{-i\theta}\,\tilde F .
$$
The medium factors are essential to the clean phase form: the real duality rotation mixes $\mathbf E$ with $c\mathbf B$, while $\tilde F$ stores the electric field with a factor $i\sqrt{\epsilon}$ and the magnetic field with a factor $-\sqrt{\mu}$.

**Solution (d).** For real $\mathbf E,\mathbf B$ and real $\theta$, the fields
$$
\mathbf E' = \mathbf E\cos\theta + c\,\mathbf B\sin\theta,
\qquad
\mathbf H' = \frac{\mathbf B'}{\mu} = \frac{\mathbf B}{\mu}\cos\theta - \frac{\mathbf E}{c\mu}\sin\theta
$$
are real. Moreover
$$
\tilde F' = i\sqrt{\epsilon}\,\mathbf E' - \sqrt{\mu}\,\mathbf H'
$$
by construction, so the transformed object is again a physical field strength of the same form. The duality rotation therefore maps the physical (real-field) subspace to itself. Multiplication by the phase $e^{-i\theta}$ is invertible, with inverse $\theta\mapsto-\theta$; the transformation is a one-parameter group.

## Problem 2: Duality and the Quadratic Objects

**Statement.** (a) Compute $\mathbf V\cdot\mathbf V$ in terms of the invariants and derive the transformation of $I_1$ and $I_2$ under duality. (b) Derive the transformation of the norm form $N(\tilde F)=\tilde F\bar{\tilde F}$ and identify the combination of invariants that duality leaves fixed. (c) Show that the Hermitian form $\tilde F\tilde F^\dagger$, equivalently the energy density $W$ and the Poynting vector $\mathbf S$, is invariant. (d) Check all of this on two explicit fields: a generic field with nonzero $\mathbf E$ and $\mathbf B$, and a free plane wave (a null field).

**Solution (a).** Expanding the complex dot product,
$$
\mathbf V\cdot\mathbf V = \left(\mathbf E + ic\mathbf B\right)\cdot\left(\mathbf E + ic\mathbf B\right)
= \mathbf E^2 - c^2\mathbf B^2 + 2ic\,\mathbf E\cdot\mathbf B
= I_1 + 2ic\,I_2 .
$$
Under $\mathbf V\mapsto e^{-i\theta}\mathbf V$ the bilinear form acquires the factor $e^{-2i\theta}$, so with $\mathbf V'\cdot\mathbf V' = I_1' + 2icI_2'$,
$$
I_1' = I_1\cos 2\theta + 2cI_2\sin 2\theta,
\qquad
2cI_2' = 2cI_2\cos 2\theta - I_1\sin 2\theta .
$$
The pair $(I_1,2cI_2)$ rotates by the doubled angle $2\theta$. Consequently
$$
I_1'^2 + 4c^2I_2'^2 = I_1^2 + 4c^2I_2^2 = \left|\mathbf V\cdot\mathbf V\right|^2
= \frac{1}{\epsilon^2}\left|N(\tilde F)\right|^2 .
$$

**Solution (b).** Since $\tilde F = i\sqrt{\epsilon}\mathbf V$ and $\bar{\tilde F} = -\tilde F$ for a pure vector,
$$
N(\tilde F) = \tilde F\bar{\tilde F} = \mathbf F\cdot\mathbf F = \left(i\sqrt{\epsilon}\right)^2\mathbf V\cdot\mathbf V
= -\epsilon\left(I_1 + 2ic\,I_2\right).
$$
Under $\tilde F\mapsto e^{-i\theta}\tilde F$, and because the central scalar $e^{-i\theta}$ is fixed by quaternion conjugation,
$$
N(\tilde F) \mapsto e^{-2i\theta}\,N(\tilde F),
$$
which reproduces the rotation of $(I_1,2cI_2)$ obtained in part (a). The quantity $I_1^2 + 4c^2I_2^2$ is invariant under duality as well as under Lorentz transformations; each of $I_1$ and $I_2$ is separately Lorentz invariant, but duality mixes them, so only this combination is invariant under both.

**Solution (c).** From the parent article, $\tilde F\tilde F^\dagger = 2W e_0 + \frac{2i}{c}\mathbf S$. Under duality,
$$
\tilde F\tilde F^\dagger \mapsto
\left(e^{-i\theta}\tilde F\right)\left(e^{-i\theta}\tilde F\right)^\dagger
= e^{-i\theta}\tilde F\,\tilde F^\dagger e^{i\theta}
= \tilde F\tilde F^\dagger,
$$
because the phase is central and $\left(e^{-i\theta}\tilde F\right)^\dagger = e^{i\theta}\tilde F^\dagger$. Hence both $W$ and $\mathbf S$ are invariant. Directly, the real duality rotation is an orthogonal rotation of $(\mathbf E,c\mathbf B)$, so
$$
\mathbf E'^2 + c^2\mathbf B'^2 = \mathbf E^2 + c^2\mathbf B^2,
\qquad
\mathbf E'\times\mathbf B' = \mathbf E\times\mathbf B,
$$
and therefore
$$
W' = \tfrac12\left(\epsilon\mathbf E'^2 + \mu\mathbf H'^2\right)
= \tfrac{\epsilon}{2}\left(\mathbf E'^2 + c^2\mathbf B'^2\right) = W,
\qquad
\mathbf S' = \mathbf E'\times\mathbf H' = \frac{1}{\mu}\mathbf E'\times\mathbf B' = \mathbf S .
$$
Duality rotates the field into a different electric–magnetic split but does not change its energy density or its energy flow.

**Solution (d).** *Generic field.* Take $\epsilon = \mu = 1$, so $c = 1$, and
$$
\mathbf E = (3,0,0), \qquad \mathbf B = (0,4,0), \qquad \theta = \frac{\pi}{4}.
$$
Then $I_1 = 9 - 16 = -7$, $I_2 = 0$, and
$$
\mathbf E' = \left(\frac{3}{\sqrt 2},\frac{4}{\sqrt 2},0\right),
\qquad
\mathbf B' = \left(-\frac{3}{\sqrt 2},\frac{4}{\sqrt 2},0\right).
$$
Directly, $I_1' = \mathbf E'^2 - \mathbf B'^2 = \frac{25}{2} - \frac{25}{2} = 0$ and $I_2' = \mathbf E'\cdot\mathbf B' = -\frac{9}{2} + \frac{16}{2} = \frac{7}{2}$. The rotation formulas give $I_1' = -7\cos\frac{\pi}{2} = 0$ and $2I_2' = 7 = -(-7)\sin\frac{\pi}{2}$, in agreement. The invariant is $I_1^2 + 4c^2I_2^2 = 49$ before and $0 + 4\cdot\frac{49}{4} = 49$ after. Also $W = \frac{25}{2}$ is unchanged, and $\mathbf S = (0,0,12)$ is unchanged.

*Null plane wave.* Take a plane wave in the medium,
$$
\mathbf E = E_0\cos(kz-\omega t)\,\hat{\mathbf x},
\qquad
\mathbf B = \frac{E_0}{c}\cos(kz-\omega t)\,\hat{\mathbf y},
\qquad
k = \frac{\omega}{c}.
$$
It has $I_1 = \mathbf E^2 - c^2\mathbf B^2 = 0$ and $I_2 = \mathbf E\cdot\mathbf B = 0$, so $N(\tilde F)=0$: it is a null field, and the pair $(I_1,2cI_2)$ is the zero pair, which any rotation fixes. The Riemann–Silberstein vector is
$$
\mathbf V = E_0\cos(kz-\omega t)\left(\hat{\mathbf x} + i\hat{\mathbf y}\right),
$$
and duality gives
$$
\mathbf V' = e^{-i\theta}\mathbf V,
\qquad
\mathbf E' = E_0\cos(kz-\omega t)\left(\cos\theta\,\hat{\mathbf x} + \sin\theta\,\hat{\mathbf y}\right),
\qquad
\mathbf B' = \frac{E_0}{c}\cos(kz-\omega t)\left(\cos\theta\,\hat{\mathbf y} - \sin\theta\,\hat{\mathbf x}\right).
$$
The wave remains a null plane wave with the same $W$ and the same $\mathbf S = cW\hat{\mathbf z}$; the duality rotation simply rotates the direction of linear polarization. This is the second case that was not used to suggest the general invariant formula, and it agrees with it.

## Problem 3: Duality as a Symmetry, With and Without Sources

**Statement.** (a) Show that the duality rotation preserves the source-free Maxwell equations in the medium. (b) Write the same statement in biquaternion form. (c) Show that with only electric sources the transformation is not a symmetry, and identify the source that must be added to restore it.

**Solution (a).** The source-free Maxwell equations in a homogeneous medium are
$$
\mathrm{rot}\,\mathbf E = -\partial_t\mathbf B,
\qquad
\mathrm{rot}\,\mathbf B = c^{-2}\,\partial_t\mathbf E,
\qquad
\mathrm{div}\,\mathbf E = 0,
\qquad
\mathrm{div}\,\mathbf B = 0 .
$$
Substituting the duality transformation and using $c^2 = 1/(\epsilon\mu)$,
$$
\mathrm{rot}\,\mathbf E' = \mathrm{rot}\,\mathbf E\cos\theta + c\,\mathrm{rot}\,\mathbf B\sin\theta
= -\partial_t\mathbf B\cos\theta + c\left(c^{-2}\partial_t\mathbf E\right)\sin\theta
= -\partial_t\left(\mathbf B\cos\theta - \frac{1}{c}\mathbf E\sin\theta\right)
= -\partial_t\mathbf B',
$$
and similarly
$$
\mathrm{rot}\,\mathbf B' = \mathrm{rot}\,\mathbf B\cos\theta - \frac{1}{c}\mathrm{rot}\,\mathbf E\sin\theta
= c^{-2}\partial_t\mathbf E\cos\theta + \frac{1}{c}\partial_t\mathbf B\sin\theta
= c^{-2}\partial_t\mathbf E' .
$$
The divergence equations are preserved because the rotation is orthogonal and $\mathrm{div}$ is linear. So duality is a one-parameter symmetry of the source-free system. (It is also a symmetry of the Riemann–Silberstein equation $i\partial_t\mathbf V = c\,\mathrm{rot}\,\mathbf V$ and of $\mathrm{div}\,\mathbf V = 0$, since the phase is constant.)

**Solution (b).** The source-free biquaternion equation is $\tilde\nabla\tilde F = 0$. Because $e^{-i\theta}$ is a constant central scalar, it commutes with $\tilde\nabla$ and with every biquaternion, so
$$
\tilde\nabla\left(e^{-i\theta}\tilde F\right) = e^{-i\theta}\,\tilde\nabla\tilde F = 0 .
$$
The duality rotation is thus an internal $U(1)$ symmetry generated by the scalar imaginary $i$, not a spacetime symmetry. It cannot be absorbed into a Lorentz transformation: a Lorentz transformation preserves $N(\tilde F)$ exactly, whereas duality multiplies it by $e^{-2i\theta}$. This is the biquaternion form of the statement that duality is not a Lorentz transformation.

**Solution (c).** With sources, the equation is $\tilde\nabla\tilde F = -\tilde R$, where the electric source is
$$
\tilde R = \frac{i\rho}{\sqrt{\epsilon}}\,e_0 + \sqrt{\mu}\,\mathbf J \in \mathbb M_- .
$$
If $\tilde F\mapsto e^{-i\theta}\tilde F$ is to solve the sourced equation, the source must transform as $\tilde R\mapsto e^{-i\theta}\tilde R$, since
$$
\tilde\nabla\left(e^{-i\theta}\tilde F\right) = -e^{-i\theta}\tilde R .
$$
For $\theta\neq 0$ the transformed source is no longer purely electric: writing $e^{-i\theta}\tilde R = (\cos\theta - i\sin\theta)\tilde R$, its scalar part acquires a real piece and its vector part an imaginary piece. This is exactly the form of the magnetic contribution to the combined source introduced below, $i\tilde R_m = -\frac{\rho_m}{\sqrt{\mu}} + i\sqrt{\epsilon}\,\mathbf J_m$: a real scalar part is a magnetic charge density and an imaginary vector part is a magnetic current. Thus duality is not a symmetry of the electric-only sourced equations, and its completion requires magnetic charge. With a magnetic source $\tilde R_m = i\rho_m/\sqrt{\mu}\,e_0 + \sqrt{\epsilon}\,\mathbf J_m$ and the combined source $\tilde{\mathcal R} = \tilde R + i\tilde R_m$, the equation $\tilde\nabla\tilde F = -\tilde{\mathcal R}$ is duality covariant, and at $\theta = \pi/2$ the rotation exchanges electric and magnetic charge. This is developed in the companion article *The Magnetic Monopole in Biquaternionic Form*; the point here is only that the parent's statement — duality is a symmetry of the source-free equations and fails with electric sources — is correct, and that its failure is the appearance of magnetic charge, not an inconsistency.

## Problem 4: The Conjugate of the Riemann–Silberstein Vector, and a Notation Defect

**Statement.** (a) Under duality $\mathbf V\mapsto e^{-i\theta}\mathbf V$, derive the transformation of the complex conjugate $\mathbf V^* = \mathbf E - ic\mathbf B$ and of the quaternion conjugate $\bar{\mathbf V}$. (b) The parent writes that "$\mathbf V$ and $\bar{\mathbf V}$ split the six real field components into two independent complex three-vectors" and that "$\bar{\mathbf V}\mapsto e^{+i\theta}\bar{\mathbf V}$". Test these statements against the conjugations declared in the parent's own conventions. (c) Show that $\mathbf V$ alone already carries the six real components of the field.

**Solution (a).** Complex conjugation of $\mathbf V' = e^{-i\theta}\mathbf V$ reverses the phase:
$$
\mathbf V'^* = \left(e^{-i\theta}\mathbf V\right)^* = e^{+i\theta}\,\mathbf V^* .
$$
The field-strength biquaternion is a pure vector, and quaternion conjugation of a pure vector negates it: $\bar{\mathbf V} = -\mathbf V$. Hence
$$
\overline{\mathbf V'} = -\mathbf V' = -e^{-i\theta}\mathbf V = e^{-i\theta}\left(-\mathbf V\right) = e^{-i\theta}\,\bar{\mathbf V},
$$
so the quaternion conjugate transforms with $e^{-i\theta}$, not with $e^{+i\theta}$.

**Solution (b).** In the parent's conventions the symbol $\bar{\cdot}$ is the quaternion conjugate and ${}^*$ is the complex conjugate. Part (a) shows that the object whose duality image is $e^{+i\theta}$ times itself is the complex conjugate $\mathbf V^*$, not the quaternion conjugate $\bar{\mathbf V}$. As written, the parent's first displayed equation,
$$
\mathbf V \mapsto e^{-i\theta}\mathbf V,
\qquad \bar{\mathbf V} \mapsto e^{+i\theta}\bar{\mathbf V},
$$
is therefore inconsistent with its own declared notation: with $\bar{\mathbf V} = -\mathbf V$, the second transformation assigns to $-\mathbf V$ the value $-e^{+i\theta}\mathbf V$, whereas the first transformation and linearity assign to $-\mathbf V$ the value $-e^{-i\theta}\mathbf V$; the two agree only when the phase is trivial. The intended object is $\mathbf V^* = \mathbf E - ic\mathbf B$. This is a notational defect in the parent, not a defect of the physics of duality, and it is recorded here because a reader following the declared conventions cannot reproduce the displayed equation.

The companion defect is the phrase "two independent complex three-vectors". A complex three-vector has three complex components, that is six real components, and it already carries the whole field: $\mathbf V = \mathbf E + ic\mathbf B$ is equivalent to the six real numbers $(\mathbf E,\mathbf B)$. The complex conjugate $\mathbf V^*$ is determined by $\mathbf V$ and adds no new data; for real fields $\mathbf V$ and $\mathbf V^*$ are not independent. The correct statement is that the complexified field space decomposes into the self-dual and anti-self-dual pieces, which are complex conjugates of one another, and on the real slice they are conjugate, not independent. The parent's "$\mathbf V$ and $\bar{\mathbf V}$" should be read as $\mathbf V$ and its complex conjugate, with the reality condition imposed.

**Solution (c).** Let $\mathbf E = (E_1,E_2,E_3)$ and $\mathbf B = (B_1,B_2,B_3)$ be real. Then
$$
\mathbf V = (E_1 + icB_1)\,e_1 + (E_2 + icB_2)\,e_2 + (E_3 + icB_3)\,e_3,
$$
whose three complex components are the six real components of $(\mathbf E,c\mathbf B)$. No information is lost and no second independent complex three-vector is needed. This is consistent with the fact that the parent defines $\tilde F = i\sqrt{\epsilon}\mathbf V$ to be the entire field strength: if a second independent complex three-vector were required, $\tilde F$ would not carry the full field.

## Problem 5: The Lorentz Transformation of the Field Strength — a Gap in the Parent

**Statement.** The parent states that "the two pieces transform independently under the Lorentz group, in the two three-dimensional complex representations." (a) Write down the natural biquaternion candidate for the Lorentz action, by analogy with the four-vector law $\tilde X\mapsto\tilde\Lambda\tilde X\tilde\Lambda^\dagger$, and test it on a pure spatial rotation. (b) Test the same candidate on a pure boost. (c) Identify a transformation that reproduces the standard boost, and state what this implies about the parent's claim.

**Solution (a).** For a unit-norm biquaternion $\tilde\Lambda$ (so $\tilde\Lambda\bar{\tilde\Lambda} = e_0$), the four-vector law of the parents is
$$
\tilde X \mapsto \tilde\Lambda\,\tilde X\,\tilde\Lambda^\dagger .
$$
The natural candidate for the field strength is the same conjugation,
$$
\tilde F \mapsto \tilde\Lambda\,\tilde F\,\tilde\Lambda^\dagger .
$$
For a pure spatial rotation the rotor is a real quaternion, $\tilde\Lambda = \cos(\varphi/2) + \sin(\varphi/2)\,\hat{\mathbf u}$, with $\tilde\Lambda^\dagger = \tilde\Lambda^{-1}$. Take $\hat{\mathbf u} = e_3$ and a field with $\mathbf E = E_0 e_1$, $\mathbf B = 0$, so $\tilde F = i\sqrt{\epsilon}E_0 e_1$. The standard rotation gives $\mathbf E' = E_0(\cos\varphi\,e_1 + \sin\varphi\,e_2)$, $\mathbf B'=0$, and indeed
$$
\tilde\Lambda\,e_1\,\tilde\Lambda^\dagger = \cos\varphi\,e_1 + \sin\varphi\,e_2 ,
$$
so
$$
\tilde\Lambda\,\tilde F\,\tilde\Lambda^\dagger = i\sqrt{\epsilon}E_0\left(\cos\varphi\,e_1 + \sin\varphi\,e_2\right) = \tilde F' .
$$
On a pure rotation the candidate works.

**Solution (b).** Take now the pure boost along $e_3$ with the parent's boost biquaternion
$$
\tilde\Lambda = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,e_3,
\qquad \tanh\psi = \frac{u}{c},
$$
which is Hermitian, $\tilde\Lambda^\dagger = \tilde\Lambda$. For simplicity set $\epsilon = \mu = 1$, so $c = 1$ and $\mathbf H = \mathbf B$, and take the same transverse electric field $\mathbf E = E_0 e_1$, $\mathbf B = 0$, so $\tilde F = iE_0 e_1$. The standard boost formulas of the parent give
$$
\mathbf E' = \gamma\left(\mathbf E + \mathbf u\times\mathbf B\right) - \frac{\gamma-1}{u^2}\left(\mathbf u\cdot\mathbf E\right)\mathbf u
= \cosh\psi\,E_0\,e_1,
$$
$$
\mathbf B' = \gamma\left(\mathbf B - \frac{1}{c^2}\mathbf u\times\mathbf E\right) - \frac{\gamma-1}{u^2}\left(\mathbf u\cdot\mathbf B\right)\mathbf u
= -\sinh\psi\,E_0\,e_2,
$$
using $\gamma = \cosh\psi$ and $\gamma u = \sinh\psi$, so
$$
\tilde F' = i\cosh\psi\,E_0\,e_1 + \sinh\psi\,E_0\,e_2 .
$$
The candidate conjugation gives instead
$$
\tilde\Lambda\,e_1\,\tilde\Lambda^\dagger = e_1, \qquad
\tilde\Lambda\,e_2\,\tilde\Lambda^\dagger = e_2,
\qquad
\tilde\Lambda\,e_3\,\tilde\Lambda^\dagger = \cosh\psi\,e_3 - i\sinh\psi,
$$
(so the candidate does not even preserve the pure-vector subspace on $e_3$, producing a scalar part), hence
$$
\tilde\Lambda\,\tilde F\,\tilde\Lambda^\dagger = iE_0\,e_1,
$$
which is **not** $\tilde F'$: the transverse electric field is left unchanged, with no $\cosh\psi$ enhancement and no induced magnetic field. The natural candidate fails on a boost. This is the sharpest form of the gap: the four-vector conjugation, which is the only Lorentz action the parents exhibit, is not the Lorentz action of the field strength.

**Solution (c).** For the same boost, the transformation
$$
\tilde F \mapsto \bar{\tilde\Lambda}\,\tilde F\,\tilde\Lambda = \tilde\Lambda^{-1}\,\tilde F\,\tilde\Lambda
$$
does reproduce the standard result:
$$
\bar{\tilde\Lambda}\,e_1\,\tilde\Lambda = \cosh\psi\,e_1 - i\sinh\psi\,e_2,
\qquad
\bar{\tilde\Lambda}\,e_2\,\tilde\Lambda = \cosh\psi\,e_2 + i\sinh\psi\,e_1,
$$
so
$$
\bar{\tilde\Lambda}\,\tilde F\,\tilde\Lambda
= i\cosh\psi\,E_0\,e_1 + \sinh\psi\,E_0\,e_2 = \tilde F' .
$$
The boost is therefore reproduced by $\tilde\Lambda^{-1}\tilde F\tilde\Lambda$, while the rotation of part (a) is reproduced by $\tilde\Lambda\tilde F\tilde\Lambda^\dagger = \tilde\Lambda\tilde F\tilde\Lambda^{-1}$. The two cases require different orderings, so no single one of these adjoint actions, with the parents' rotor conventions, is the Lorentz transformation law of $\tilde F$. The parent gives no law at all, and its claim that the two pieces "transform independently under the Lorentz group" is therefore unverified: the abstract representation-theoretic statement that the self-dual and anti-self-dual pieces carry the two complex conjugate three-dimensional representations is standard, but the biquaternion realization of that statement is not supplied, and the obvious candidate for it is false. Determining the correct biquaternion action — plausibly an adjoint action conjugated by a fixed linear map on the field-strength space — is left open. **This is the gap this exercise reports in its parent.**

## Further Problems

1. **The general Lorentz law of $\tilde F$.** Determine the biquaternion map that reproduces the standard transformation of $\mathbf E$ and $\mathbf B$ for a general rotor (a boost composed with a rotation). Show whether it can be written as $\tilde F\mapsto T\!\left(\tilde\Lambda\,T^{-1}(\tilde F)\,\tilde\Lambda^\dagger\right)$ for a fixed invertible linear map $T$ on $\mathrm{Vect}(\mathbb B)$, and identify $T$ if it exists. The exercise above shows only that $T$ is not the identity and that no single adjoint ordering works with the parents' rotors.

2. **Duality and the gauge $U(1)$.** The gauge principle article identifies the center of $\mathbb B$ as $\mathbb C_{\mathbb B}$ and its unitary part as the abelian gauge group of the biquaternionic Maxwell field. The duality rotation here is multiplication by an element $e^{-i\theta}$ of that same $U(1)$. Is the duality symmetry the same $U(1)$, a different one, or the same group acting on a different representation? The parent does not ask this; the answer is not obvious, because duality acts on the field strength and the gauge phase on the potential.

3. **Duality and the energy–momentum tensor.** Using the construction of the companion exercise *Exercise: The Electromagnetic Energy–Momentum Tensor*, show that $T^{\mu\nu}$ is invariant under duality, and explain why this is consistent with the invariance of $W$ and $\mathbf S$ but does not follow from it component by component.

4. **Duality and the invariant classification.** Show that duality preserves the type of the field (null, electric, magnetic, generic) determined by $(I_1,I_2)$ in the parent's classification, and compute the orbit of the generic magnitudes $(E_0,B_0)$ under the doubled-angle rotation. Identify the duality angle that maps a purely electric field to a purely magnetic one, and the angle that leaves a given non-null field's type but reverses the sign of $I_1$.

5. **The complexified field.** Extend the duality rotation to a fully complexified $\tilde F$, with coefficients unrestricted in $\mathbb C$, and show that $e^{-i\theta}$ remains a symmetry of the complexified equation $\tilde\nabla\tilde F = 0$. Determine how the two independent complex structures — the $i$ of duality and the $i$ of the $ict$ gradient — are related in the complexified setting.

## Summary

The duality rotation of the electromagnetic field is the central phase rotation of the Riemann–Silberstein vector,
$$
\mathbf E \mapsto \mathbf E\cos\theta + c\,\mathbf B\sin\theta,
\qquad
\mathbf B \mapsto \mathbf B\cos\theta - \frac{1}{c}\,\mathbf E\sin\theta,
$$
which is exactly $\mathbf V\mapsto e^{-i\theta}\mathbf V$ and, because $\tilde F = i\sqrt{\epsilon}\mathbf V$, exactly $\tilde F\mapsto e^{-i\theta}\tilde F$. The phase is the scalar imaginary $i$; it is central, so the rotation is an internal $U(1)$ symmetry and not a Lorentz transformation.

Duality preserves the Hermitian form: the energy density $W$ and the Poynting vector $\mathbf S$ are unchanged. It rotates the norm form by the doubled phase, $N(\tilde F)\mapsto e^{-2i\theta}N(\tilde F)$, so the pair $(I_1,2cI_2)$ rotates by $2\theta$ and $I_1^2 + 4c^2I_2^2$ is invariant. It is a symmetry of the source-free Maxwell equations and of the biquaternionic equation $\tilde\nabla\tilde F = 0$; with electric sources alone it is not a symmetry, and its sourced completion requires magnetic charge, which is rotated into electric charge at $\theta = \pi/2$.

Two defects in the parent are recorded. First, the parent's equation $\bar{\mathbf V}\mapsto e^{+i\theta}\bar{\mathbf V}$ uses the symbol $\bar{\mathbf V}$ for the complex conjugate, although the parent declares $\bar{\cdot}$ to be quaternion conjugation; with that declaration $\bar{\mathbf V} = -\mathbf V$ and the displayed transformation is inconsistent. The object transforming as $e^{+i\theta}$ is $\mathbf V^* = \mathbf E - ic\mathbf B$, and $\mathbf V$ alone already carries the six real field components, so $\mathbf V$ and $\mathbf V^*$ are not independent. Second, the parent's claim that the two pieces transform independently under the Lorentz group has no biquaternion realization in the article; the natural candidate $\tilde F\mapsto\tilde\Lambda\tilde F\tilde\Lambda^\dagger$ works for a pure spatial rotation but fails on a pure boost, where it leaves a transverse electric field unchanged instead of producing the $\cosh\psi$ enhancement and the induced magnetic field. The boost is reproduced by $\tilde\Lambda^{-1}\tilde F\tilde\Lambda$, and the two cases require different orderings, so the correct general law is left open. This is the gap the exercise reports.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = -\delta_{jk}e_0 + \epsilon_{jkm}e_m$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; complex-scalar subspace (center) |
| $\bar{\cdot}, {}^*, {}^\dagger = \bar{\cdot}^{\,*}$ | Quaternion, complex, and Hermitian conjugations |
| $\tilde\nabla, \bar{\tilde\nabla}, \Box = \tilde\nabla\bar{\tilde\nabla}$ | Biquaternionic gradient, its quaternion conjugate, d'Alembertian |
| $\tilde\Lambda \in \mathbb{B}$, $\tilde\Lambda\bar{\tilde\Lambda} = e_0$ | Lorentz rotor (unit-norm biquaternion) |
| $\tilde F = i\sqrt{\epsilon}\,\mathbf E - \sqrt{\mu}\,\mathbf H$ | Field-strength biquaternion (pure vector) |
| $\mathbf{E}, \mathbf{H}, \mathbf{B} = \mu\mathbf H$ | Electric field, magnetic field, magnetic induction |
| $\epsilon,\mu$, $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Permittivity, permeability, medium speed of light, vacuum speed of light |
| $\mathbf V = \mathbf E + ic\mathbf B$ | Riemann–Silberstein vector, $\tilde F = i\sqrt{\epsilon}\mathbf V$ |
| $\mathbf V^* = \mathbf E - ic\mathbf B$ | Complex conjugate of $\mathbf V$ |
| $\theta$ | Duality angle |
| $N(\tilde F) = \tilde F\bar{\tilde F} = -\epsilon(I_1 + 2icI_2)$ | Norm form (complex scalar) |
| $I_1 = \mathbf E^2 - c^2\mathbf B^2$, $I_2 = \mathbf E\cdot\mathbf B$ | Lorentz invariants (scalar, pseudoscalar) |
| $W = \tfrac12(\epsilon\mathbf E^2 + \mu\mathbf H^2)$, $\mathbf S = \mathbf E\times\mathbf H$ | Energy density, Poynting vector |
| $\tilde F\tilde F^\dagger = 2We_0 + \frac{2i}{c}\mathbf S$ | Hermitian form (in $\mathbb{M}_+$) |
| $\tilde R = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\mathbf J$ | Electric source biquaternion |
| $\tilde R_m = \frac{i\rho_m}{\sqrt{\mu}}e_0 + \sqrt{\epsilon}\mathbf J_m$ | Magnetic source biquaternion |
| $\tilde{\mathcal R} = \tilde R + i\tilde R_m$ | Combined source, duality covariant |
| $\tilde\nabla\tilde F = -\tilde R$ | Biquaternionic Maxwell equation |
| $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula (Born rule) |

## Further Reading

- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* **22** (1907) 579–586, and **24** (1907) 783–784, for the original complex-vector formulation of the electromagnetic field.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* **46** (2013) 053001, for the complex-vector, duality and self-dual structure.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard treatment of electric–magnetic duality and the field invariants.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the invariant classification of the field and the existence of frames in which the fields are parallel or one vanishes.
- The companion articles of this series: *The Field-Strength Biquaternion and Its Invariants*; *Maxwell's Equations in the Biquaternionic Formulation*; *The Magnetic Monopole in Biquaternionic Form*; *Exercise: The Electromagnetic Energy–Momentum Tensor*; *The Lorentz Transformation as a Biquaternionic Rotation*; *Electromagnetism in Media — The Local Complex Structure at Work*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *Introduction to the Biquaternion Universe*.
