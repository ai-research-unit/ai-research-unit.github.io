# __The Field-Strength Biquaternion and Its Invariants__

## Introduction

The companion article *Maxwell's Equations in the Biquaternionic Formulation* introduced the **field-strength biquaternion**

$$
\tilde{F} = \vec F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H
$$

as the single biquaternionic object that carries the electromagnetic field, and showed that, in a medium with permittivity $\epsilon$ and permeability $\mu$, the four Maxwell equations collapse into the one equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$. In that article $\tilde{F}$ appears as a means to an end: the compact rewriting of the field equations. This article studies $\tilde{F}$ for its own sake.

Two features make the field strength worth treating separately. First, $\tilde{F}$ is *not* a four-vector. Unlike the four-potential $\tilde{A}$, whose scalar part is imaginary and whose vector part is real, the field-strength biquaternion has **vanishing scalar part** and a **mixed real/imaginary vector part**: its imaginary half carries the electric field and its real half the magnetic field. The field strength is therefore a different kind of object from the kinematic four-vectors that live in the material subspace $\mathbb{M}_-$, and its Lorentz transformation law is correspondingly different. Second, the **biquaternion norm** evaluated on $\tilde{F}$ is a complex scalar whose real and imaginary parts are the two classical Lorentz invariants, $E^2 - c^2B^2$ and $\vec E\cdot\vec B$, up to the medium factors $-\epsilon$ and $-2\epsilon c$. The algebraic apparatus built to describe the Minkowski metric thus delivers the electromagnetic invariants as well.

This article is the declared foundation for three later articles on electromagnetism in media, on the Lorentz force, and on radiation from accelerated charges. It therefore fixes the field-strength notation once and for all. The **canonical objects** are: the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$; the electric and magnetic fields $\vec E$ and $\vec H$, together with the magnetic induction $\vec B = \mu\vec H$; the medium speed of light $c = 1/\sqrt{\epsilon\mu}$; the Riemann–Silberstein vector $\vec N = \vec E + ic\vec B$; the two invariants $I_1 = \vec E^2 - c^2\vec B^2$ and $I_2 = \vec E\cdot\vec B$; and the energy density $W$ and Poynting vector $\vec S$. Nothing in this list is new notation; the first three come unchanged from the Maxwell article, and the rest are assembled from them.

The conventions are those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_\mu^2 = -e_t$, and scalar imaginary $i$ commuting with the quaternion units. The three-dimensional complex **vector part** of $\mathbb{B}$ is denoted by its components $\vec F = \sum_\mu F_\mu \vec e_\mu$, with the usual quaternion product $\vec F\vec G = -\vec F\cdot\vec G + \vec F\times\vec G$ for pure vectors. The conjugations are the quaternion conjugate ${}^{\natural}$, the complex conjugate $\bar{\cdot}$, and the Hermitian conjugate ${}^{*} = ({}^{\natural})^{\,*} = \bar{\cdot}{}^{\natural}$, with the four real fixed-point subspaces $\mathbb{C}_{\mathbb{B}}$ (scalars), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector) and $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector). The symbol $c$ always denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$; in vacuum it reduces to $c_0 = 1/\sqrt{\epsilon_0\mu_0}$.

## The Field-Strength Biquaternion

The definition is the one of the Maxwell article, repeated here because everything that follows depends on it:

$$
\tilde{F} = \vec F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H
= \sum_{\mu=1}^{3} F_\mu\, \vec e_\mu,
\qquad
F_\mu = i\sqrt{\epsilon}\,E_\mu - \sqrt{\mu}\,H_\mu .
$$

Its scalar part vanishes identically,

$$
\mathrm{Sc}(\tilde{F}) = 0,
$$

so $\tilde{F}$ is a **pure-vector** biquaternion. Its three complex components $F_\mu$ each combine an electric and a magnetic piece: the electric contribution $i\sqrt{\epsilon}\,E_\mu$ is **purely imaginary** and the magnetic contribution $-\sqrt{\mu}\,H_\mu$ is **real**. The factor of $i$ on the electric part is the same factor that appears in the complex time coordinate $ict'$. In the $ict'$ convention the time direction is the imaginary direction, and the electric field carries the time index of the field tensor, so it is the electric part that acquires the factor $i$ while the magnetic part remains real. This is the algebraic reason for the asymmetric appearance of $\tilde{F}$.

The normalization factors $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are the natural ones for a medium. Each term has the dimension of the square root of an energy density, since $\epsilon E^2$ and $\mu H^2$ are both energy densities; consequently $\tilde{F}$ has dimension $\sqrt{\text{energy density}}$, and the biquaternion norm calculated below has dimension of an energy density. With the constitutive relation $\vec B = \mu\vec H$ the magnetic term may also be written $\sqrt{\mu}\,\vec H = \vec B/\sqrt{\mu}$, so the field strength can equally be regarded as the pair $(\sqrt{\epsilon}\,\vec E, \vec B/\sqrt{\mu})$.

The field strength is not an independent object: it is obtained from the potential biquaternion $\tilde{A} = i\phi/c + \vec A$ by differentiation. In the biquaternion algebra the construction is

$$
\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A} - \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right),
$$

the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$, where $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$ is the biquaternionic gradient and $\tilde{\nabla}^{\natural}$ its quaternion conjugate. In tensor language the same object is the antisymmetric rank-two tensor

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu,
\qquad
F^{\mu\nu} =
\begin{pmatrix}
0 & iE_x/c & iE_y/c & iE_z/c \\
-iE_x/c & 0 & B_z & -B_y \\
-iE_y/c & -B_z & 0 & B_x \\
-iE_z/c & B_y & -B_x & 0
\end{pmatrix}.
$$

The tensor has six independent components — three electric and three magnetic — which is exactly the information carried by the three complex components $F_\mu$ of the pure-vector biquaternion. As the Maxwell article notes, the precise identification of $\vec F$ with the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$ depends on the normalization of the potential and on the sign convention for the fields; the unambiguous definition used here is the tensor formula together with the component combination $F_\mu = i\sqrt{\epsilon}E_\mu - \sqrt{\mu}H_\mu$.

## The Place of the Field Strength in the Algebra

The biquaternion algebra decomposes in several ways, and it is worth locating $\tilde{F}$ precisely in these decompositions, because its peculiar properties are consequences of its position.

**The vector part.** The pure-vector biquaternions form the complex three-dimensional subspace

$$
\mathrm{Vect}(\mathbb{B}) = \mathbb{C}\vec e_x \oplus \mathbb{C}\vec e_y \oplus \mathbb{C}\vec e_z,
$$

of real dimension six. It is *not* one of the four fixed-point subspaces $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}, \mathbb{M}_+$ and $\mathbb{M}_-$; those are real subspaces containing a scalar direction, of which three are four-dimensional, whereas the vector subspace contains no scalar at all. The field strength lies entirely in this subspace, and the classical statement that the electromagnetic field has six independent components is exactly the statement that $\tilde{F}$ is a general element of $\mathrm{Vect}(\mathbb{B})$.

**The Hermitian decomposition.** The vector part intersects the two complementary subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ in the three-dimensional real subspaces

$$
\mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_+ = \mathrm{span}_{\mathbb{R}}\{i\vec e_x, i\vec e_y, i\vec e_z\},
\qquad
\mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_- = \mathrm{span}_{\mathbb{R}}\{\vec e_x, \vec e_y, \vec e_z\}.
$$

The first consists of the pure **imaginary** vectors and the second of the pure **real** vectors. The two pieces of $\tilde{F}$ fall into these two intersections:

$$
\tilde{F} = \underbrace{i\sqrt{\epsilon}\,\vec E}_{\in\,\mathbb{M}_+} \;+\; \underbrace{\left(-\sqrt{\mu}\,\vec H\right)}_{\in\,\mathbb{M}_-}.
$$

The electric part is therefore **Hermitian** and the magnetic part **anti-Hermitian**, and $\tilde{F}$ is neither. Explicitly,

$$
\tilde{F}^{*} = -\vec F^* = i\sqrt{\epsilon}\,\vec E + \sqrt{\mu}\,\vec H,
$$

so that the Hermitian and anti-Hermitian parts of the field strength are

$$
\tfrac{1}{2}\left(\tilde{F} + \tilde{F}^{*}\right) = i\sqrt{\epsilon}\,\vec E,
\qquad
\tfrac{1}{2}\left(\tilde{F} - \tilde{F}^{*}\right) = -\sqrt{\mu}\,\vec H.
$$

This expresses a familiar fact: the electric field transforms like the Hermitian sector and the magnetic field like the anti-Hermitian sector. It also shows why $\tilde{F}$ cannot lie in $\mathbb{M}_-$: the material subspace contains the real vectors but not the imaginary ones, and the electric half of the field strength uses the imaginary vector directions.

**The real/complex decomposition.** Equivalently, with respect to the complex conjugation $\bar{\cdot}$ that fixes $\mathbb{H}_{\mathbb{B}}$,

$$
\tilde{F} = \underbrace{\left(-\sqrt{\mu}\,\vec H\right)}_{\in\,\mathbb{H}_{\mathbb{B}}} \;+\; \underbrace{i\sqrt{\epsilon}\,\vec E}_{\in\,i\mathbb{H}_{\mathbb{B}}},
$$

The scalar subspace $\mathbb{C}_{\mathbb{B}}$ receives no contribution, which is again $\mathrm{Sc}(\tilde{F}) = 0$; the decomposition used is $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$. Thus the field strength uses the vector parts of $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ and the electric and magnetic halves of $\mathbb{M}_+$ and $\mathbb{M}_-$ respectively, and it touches $\mathbb{C}_{\mathbb{B}}$ not at all.

**The biparavector interpretation: the field as a sum of two spacetime planes.** The two halves just separated are not merely subspaces; each is a **family of planes**, and the separation of the field into an electric and a magnetic part is the separation of a biparavector into a timelike and a spacelike plane. In the paravector presentation of the algebra (*Paravectors and the Geometry of Spacetime*), a **biparavector** is the product of two orthogonal paravectors and represents a plane in spacetime; with $\gamma_\mu = i\vec e_\mu$ there are six independent planes,

$$
\left\{e_t\gamma_\mu,\ \gamma_\mu\gamma_\nu\right\} = \left\{i\vec e_x,\ i\vec e_y,\ i\vec e_z\right\} \cup \left\{\vec e_z,\ \vec e_x,\ \vec e_y\right\},
$$

using $\gamma_2\gamma_1 = -\vec e_y \vec e_x = \vec e_z$ and its cyclic companions. The first three, the planes containing the time direction, have the form $e_t\gamma_\mu$ and are the pure **imaginary** vectors, that is the real span of $\{i\vec e_\mu\} = \mathrm{Vect}(\mathbb{B})\cap\mathbb{M}_+$. The last three, the purely spatial planes, have the form $\gamma_\mu\gamma_\nu$ and are the pure **real** vectors, that is the real span of $\{\vec e_\mu\} = \mathrm{Vect}(\mathbb{B})\cap\mathbb{M}_-$.

Comparing with the decomposition above, the electric and magnetic halves of the field are exactly the two families of planes:

$$
\tilde{F} \;=\; \underbrace{i\sqrt{\epsilon}\,\vec E}_{\text{timelike planes}\;\in\,\mathbb{M}_+} \;-\; \underbrace{\sqrt{\mu}\,\vec H}_{\text{spacelike planes}\;\in\,\mathbb{M}_-}.
$$

The electric part is a combination of the three planes that contain the time direction, and the magnetic part a combination of the three that do not. This is the plane-geometric form of the algebra asymmetry: the electric field is a *boost-type* object and the magnetic field a *rotation-type* object, in the sense that the timelike planes generate the Lorentz boosts and the spacelike planes the rotations (*Symmetric and Antisymmetric Decomposition of the Four General Products*). The six components of the field are the six planes, and the field is a sum of one plane of each type.

Two familiar facts are read off from the plane type and are recorded here because the corpus states them separately elsewhere. The **quaternion conjugate** of the field reverses the electric planes and fixes the magnetic ones,

$$
\tilde{F}^{\natural} = -i\sqrt{\epsilon}\,\vec E + \sqrt{\mu}\,\vec H,
$$

because the conjugate negates the vector part of each coefficient and the electric part is the imaginary vector while the magnetic part is the real vector; read on the fields this is $\vec E\to-\vec E$, $\vec H\to\vec H$, the polar-vector and axial-vector behaviour of the electric and magnetic fields. The **duality rotation** of the later section, $\tilde{F}\mapsto \exp(i\varphi)\tilde{F}$, rotates one family of planes into the other: at $\varphi = \pi/2$ the factor is the central $i$, which carries $\mathbb{M}_+$ to $\mathbb{M}_-$ and exchanges the two families exactly, while for general $\varphi$ it rotates the electric planes into the magnetic ones and back. This is why the duality rotation is a symmetry of the source-free vacuum equations and not of the equations with electric sources: it moves the field along the cylinder of constant $I_1+iI_2$ without preserving the planes separately.

## The Biquaternion Norm and the Two Invariants

The biquaternion norm on $\mathbb{B}$ is

$$
\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\,\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu^2 .
$$

For a pure-vector biquaternion the quaternion conjugate is $\tilde{F}^{\natural} = -\vec F$, and the quaternion product of two pure vectors is $\vec F\vec G = -\vec F\cdot\vec G + \vec F\times\vec G$. Hence

$$
\tilde{F}\,\tilde{F}^{\natural} = \vec F(-\vec F) = \vec F\cdot\vec F = \sum_{\mu=1}^{3} F_\mu^2,
$$

because $\vec F\times\vec F = 0$. The cross term drops out for the biquaternion norm of a vector, and one is left with the **general plain bilinear form**

$$
\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural} = \sum_{\mu=1}^{3} F_\mu^2,
$$

which is a complex scalar. Substituting $F_\mu = i\sqrt{\epsilon}E_\mu - \sqrt{\mu}H_\mu$ and expanding,

$$
\boxed{\;\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural} = \sum_{\mu=1}^{3}\left(i\sqrt{\epsilon}E_\mu - \sqrt{\mu}H_\mu\right)^2
= -\epsilon\,\vec E^2 + \mu\,\vec H^2 - 2i\sqrt{\epsilon\mu}\,\vec E\cdot\vec H\;}.
$$

This is the central computation of the article. Written with the magnetic induction $\vec B = \mu\vec H$ and the medium speed of light $c = 1/\sqrt{\epsilon\mu}$, the real and imaginary parts become

$$
\mathrm{Re}\,\langle\tilde{F}\rangle_{\natural} = -\epsilon\left(\vec E^2 - c^2\vec B^2\right),
\qquad
\mathrm{Im}\,\langle\tilde{F}\rangle_{\natural} = -2\epsilon c\,\vec E\cdot\vec B.
$$

The two real quantities appearing here are the two classical **Lorentz invariants** of the electromagnetic field, up to the factors $-\epsilon$ and $-2\epsilon c$:

$$
\boxed{\;I_1 = \vec E^2 - c^2\vec B^2\;},
\qquad
\boxed{\;I_2 = \vec E\cdot\vec B\;}
$$

so that

$$
\langle\tilde{F}\rangle_{\natural} = -\epsilon\left[\,I_1 + 2ic\,I_2\,\right],
\qquad
I_1 = -\frac{1}{\epsilon}\,\mathrm{Re}\,\langle\tilde{F}\rangle_{\natural},
\qquad
I_2 = -\frac{1}{2\epsilon c}\,\mathrm{Im}\,\langle\tilde{F}\rangle_{\natural}.
$$

The biquaternion norm is a single complex number, and it carries exactly two real invariants. It is the *fully contracted* object built from the field strength with no derivatives and no extra vectors, so these are the only two independent invariants of the field; any other algebraic invariant is a function of $I_1$ and $I_2$.

**The conjugate biquaternion norm.** The quaternion norm is not the only natural quadratic object here. Because quaternion conjugation fixes the scalar part, conjugation acts on the vector components by $\tilde{F}^{\natural} = -\vec F$; complex conjugation, by contrast, acts on the coefficients, $\tilde{F}^* = \vec F^*$. For the biquaternion norm of the complex-conjugate field,

$$
\langle\tilde{F}^*\rangle_{\natural} = \langle\tilde{F}\rangle_{\natural}^*,
$$

so the biquaternion norm and its conjugate carry the same two real invariants. Equivalently, the reverse product is $\tilde{F}^{\natural}\tilde{F} = \tilde{F}\tilde{F}^{\natural} = \langle\tilde{F}\rangle_{\natural}$ for a pure vector. The two invariants are therefore the two real components of the complex biquaternion norm.

**Vanishing of the biquaternion norm.** Because $\tilde{F}$ is a pure vector,

$$
\tilde{F}^2 = -\vec F\cdot\vec F = -\langle\tilde{F}\rangle_{\natural},
$$

so the biquaternion norm vanishes if and only if $\tilde{F}$ squares to zero. A nonzero element of $\mathbb{B}$ whose biquaternion norm vanishes is a **zero divisor**, and $\tilde{F}$ is nilpotent in that case. Thus

$$
\langle\tilde{F}\rangle_{\natural} = 0
\quad\Longleftrightarrow\quad
I_1 = 0 \ \text{ and }\ I_2 = 0
\quad\Longleftrightarrow\quad
\tilde{F} \text{ is a zero divisor}.
$$

The vanishing of the biquaternion norm is therefore the algebraic statement that the field is a **null (radiative) field**: $\vec E\perp\vec B$ and $|\vec E| = c|\vec B|$ pointwise. This is the same zero-divisor cone that underlies the light cone of $\mathbb{M}_-$, now realized inside the field-strength space. It is the algebraic seed of the radiation theory and will reappear in the later article on radiation from accelerated charges.

## The Polar Reading of the Field

The field strength is neither Hermitian nor anti-Hermitian: its electric half lies in $\mathbb{M}_+$ and its magnetic half in $\mathbb{M}_-$. That is exactly the case in which the Cartan pairing carries information, and it gives a reading of the field that the invariants alone do not.

Write the Cartan pair of the field as

$$
\tilde F=\tilde F_H\tilde F_0,\qquad
\tilde F_H=\sqrt{\tilde F\tilde F^{*}}\ge0,\qquad
\tilde F_0=\tilde F_H^{+}\tilde F .
$$

The amplitude $\tilde F_H$ is Hermitian positive and the phase $\tilde F_0$ is unitary. On the invertible part $\langle\tilde F\rangle_{\natural}\neq0$ the pair is unique; on the null cone the generalized form replaces $\tilde F_0$ by a partial isometry.

**The amplitude carries the intensity and the boost.** The trace of its square is four times the energy density, $\operatorname{Tr}\tilde F_H^{2}=2\langle\tilde F,\tilde F\rangle_{*}=4W$, and its determinant is the modulus of the complex invariant,

$$
\langle\tilde F_H\rangle_{\natural}=\det\mathsf{M}_2(\tilde F_H)=\lvert\langle\tilde F\rangle_{\natural}\rvert
=\epsilon\sqrt{I_1^{2}+4c^{2}I_2^{2}}\ \ge 0 .
$$

The norm of the amplitude is real and non-negative even though the norm of the field is complex. The two singular values of $\tilde F$ are the eigenvalues of $\tilde F_H$, and they are fixed by $W$ and by $\lvert\langle\tilde F\rangle_{\natural}\rvert$: the energy density gives their sum of squares and the invariant modulus gives their product. The amplitude is therefore the part of the field that the operator-to-state map keeps, up to its overall scale.

**The phase is the duality angle and the polarization rotation.** The unitary factor is $\tilde F_0=\exp(i\alpha)\tilde u_{\mathrm r}$; its central phase is the duality angle, $\alpha=\tfrac12\arg\langle\tilde F\rangle_{\natural}$, and its rotor is the rotation of the polarization plane. A duality rotation $\tilde F\mapsto\exp(i\theta)\tilde F$ leaves $\tilde F_H$ unchanged and multiplies $\tilde F_0$ by $\exp(i\theta)$; it is a motion along the phase fibre, not a change of amplitude. This is the polar form of the statement that $I_1$ and $I_2$ rotate into one another while $I_1^{2}+4c^{2}I_2^{2}$ is fixed.

**The null field is a pure state.** On the cone, $I_1=I_2=0$, the amplitude is a scaled idempotent and the phase is a partial isometry, so the state $\tilde F\tilde F^{*}/2\langle\tilde F,\tilde F\rangle_{*}$ is pure. The radiative field is the zero divisor of the field space, and the operator-to-state map sends it to the boundary of the Bloch ball. This is the same cone that the massless spectrum article reads as the lightlike limit.

**The boundary.** The split is canonical in the algebra, and it is not a Lorentz-covariant factorisation: the field is a bivector in the tensor reading, its Lorentz action is not the four-vector congruence, and it does not act on $\tilde F_H$ and $\tilde F_0$ separately by one and the same operation. Only the invariants, and the modulus $\lvert\langle\tilde F\rangle_{\natural}\rvert$, are invariant. The polar split is also not the self-dual/anti-self-dual split: the latter uses the Hodge star and separates the two helicities, while the Cartan phase is the compact unitary quotient. The two decompositions answer different questions and must not be identified.

## Lorentz Invariance of the Invariants

The claim that $I_1$ and $I_2$ are Lorentz invariants is standard and can be checked directly. Under a boost with velocity $\vec v$ and Lorentz factor

$$
\gamma = \frac{1}{\sqrt{1 - \vec v^2/c^2}},
$$

the fields transform as

$$
\vec E_2 = \gamma\left(\vec E + \vec v\times\vec B\right) - \frac{\gamma-1}{\vec v^2}\left(\vec v\cdot\vec E\right)\vec v,
$$

$$
\vec B_2 = \gamma\left(\vec B - \frac{1}{c^2}\,\vec v\times\vec E\right) - \frac{\gamma-1}{\vec v^2}\left(\vec v\cdot\vec B\right)\vec v.
$$

The components parallel to the boost are unchanged, while the transverse components acquire a contribution from the other field. Substituting these expressions into $I_1$ and $I_2$, the cross terms cancel and the factors combine to $1/\gamma^2$ in precisely the way required, giving

$$
\vec E_2^2 - c^2\vec B_2^2 = \vec E^2 - c^2\vec B^2,
\qquad
\vec E_2\cdot\vec B_2 = \vec E\cdot\vec B.
$$

Both invariants are therefore unchanged. This is consistent with, and can be derived from, the rotor-conjugation transformation of the four-potential established in the Maxwell article: the field strength is built from $\tilde{A}$ by differentiation, and differentiating a quantity that transforms by rotor conjugation produces a field that transforms in the antisymmetric-tensor representation, whose two independent scalar contractions are exactly $I_1$ and $I_2$.

There is a discrete subtlety worth recording. Under the **proper orthochronous** Lorentz group both $I_1$ and $I_2$ are invariant. Under **parity**, however, the electric field is a polar vector and the magnetic induction an axial vector, so $\vec E\to-\vec E$ and $\vec B\to\vec B$. Hence

$$
I_1 \to I_1,
\qquad
I_2 \to -I_2 .
$$

The quantity $I_1$ is an ordinary scalar and $I_2$ is a **pseudoscalar**. Both are invariants of the proper orthochronous group; only $I_1$ is invariant under parity.

## The Riemann–Silberstein Vector

The two real fields can be combined into one complex three-vector, and this combination is the form in which the invariants look simplest. Define the **Riemann–Silberstein vector**

$$
\vec N = \vec E + ic\,\vec B.
$$

The field-strength biquaternion is an overall constant multiple of it. Indeed, using $\vec B = \mu\vec H$ and $c = 1/\sqrt{\epsilon\mu}$,

$$
i\sqrt{\epsilon}\,\vec N = i\sqrt{\epsilon}\left(\vec E + ic\vec B\right)
= i\sqrt{\epsilon}\,\vec E - \sqrt{\epsilon}\,c\,\vec B
= i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H
= \tilde{F},
$$

because $\sqrt{\epsilon}\,c\,\mu = \sqrt{\mu}$. Thus

$$
\tilde{F} = i\sqrt{\epsilon}\,\vec N.
$$

This is the sense in which the Riemann–Silberstein vector and the field-strength biquaternion are **the same object**: they differ only by the constant $i\sqrt{\epsilon}$, so they carry identical information and have proportional invariants. The complex vector was introduced by Ludwik Silberstein in 1907, and the biquaternion formulation is its natural algebraic home: the complex vector is the vector part of a biquaternion with vanishing scalar part.

The biquaternion norm is now immediate. Since $\vec N$ is a complex three-vector,

$$
\vec N\cdot\vec N = \left(\vec E + ic\vec B\right)\cdot\left(\vec E + ic\vec B\right)
= \vec E^2 - c^2\vec B^2 + 2ic\,\vec E\cdot\vec B
= I_1 + 2ic\,I_2,
$$

and therefore

$$
\langle\tilde{F}\rangle_{\natural} = \left(i\sqrt{\epsilon}\right)^2 \vec N\cdot\vec N = -\epsilon\left(I_1 + 2ic\,I_2\right),
$$

in agreement with the direct computation. The two invariants are the real and imaginary parts of the complex number $\vec N\cdot\vec N$, up to constant factors.

The Riemann–Silberstein vector also linearizes the source-free field equations. In vacuum or in a homogeneous medium with no free sources, Maxwell's equations give $\mathrm{rot}\,\vec E = -\partial/\partial t'\vec B$ and $\mathrm{rot}\,\vec B = c^{-2}\partial/\partial t'\vec E$, and combining these,

$$
i\,\partial/\partial t' \vec N = c\,\mathrm{rot}\,\vec N,
\qquad
\mathrm{div}\,\vec N = 0 .
$$

The first equation has the form of a Schrödinger equation whose Hamiltonian is $c\,\mathrm{rot}$; the second is the transverse (divergence-free) condition inherited from $\mathrm{div}\,\vec D = 0$ and $\mathrm{div}\,\vec B = 0$. This is the form in which the radiative content of the field is most transparent, and the null condition $\vec N\cdot\vec N = 0$ is precisely the condition that the complex vector be a null vector of the complexified spatial metric. A field whose Riemann–Silberstein vector is null, i.e. for which $\langle\tilde{F}\rangle_{\natural} = 0$, is a radiation field.

Finally, the antisymmetric field tensor decomposes into its **self-dual and anti-self-dual parts**. Define the Hodge dual by its action on the fields,
$$
\star:\ (\vec E,\vec B) \mapsto (c\,\vec B, -\vec E/c),
\qquad
\star^2 = -1,
$$
which is the $\theta = \pi/2$ case of the duality rotation below. On the Riemann–Silberstein vector the dual is multiplication by $-i$,
$$
\vec N(\star F) = -i\,\vec N,
\qquad
\vec N^*(\star F) = +i\,\vec N^* .
$$
The two combinations $F \pm i\star F$ are therefore the two parts, of opposite chirality,
$$
F + i\,\star F \ \longleftrightarrow\ 2\vec N = 2(\vec E + ic\vec B),
\qquad
F - i\,\star F \ \longleftrightarrow\ 2\vec N^* = 2(\vec E - ic\vec B),
$$
with $\star(F \pm i\star F) = \mp i\,(F \pm i\star F)$. The $\vec N$ part ($\star F = -iF$) is the **self-dual** half and the $\vec N^*$ part ($\star F = +iF$) the **anti-self-dual** half; the two halves are the two helicities of the radiation field. For a real field the two parts are complex conjugates of one another, so $\vec N^*$ adds no new data: $\vec N$ alone already carries the six real field components of $(\vec E,\vec B)$. On the complexified field space they are instead independent, and transform separately under the Lorentz group in the two three-dimensional complex representations — the two chiralities.

*Convention.* The dual is defined here by its action on $(\vec E,\vec B)$, the real-time convention with $\star^2 = -1$, which is the form in which the self-dual/anti-self-dual split is standard. Two sign conventions are in circulation for the star. We use the one in which $\star$ is the $\theta = \pi/2$ duality rotation, giving $\star\vec N = -i\vec N$; the **self-dual** half is then the $\vec N$ combination $F + i\star F$ ($\star$-eigenvalue $-i$) and the **anti-self-dual** half the $\vec N^*$ combination $F - i\star F$ ($\star$-eigenvalue $+i$). With the opposite sign of $\epsilon^{\mu\nu\rho\sigma}$ the two names are exchanged and nothing else changes. The component-wise dual read off from the $ict'$ tensor above, $(\star F)_{0k} = B_k$, is $-i$ times this one and has $\star^2 = +1$; it is the same decomposition, with the two parts appearing as the real $\pm1$ eigenfields $F \pm \star F$ instead of the complex ones $F \pm i\star F$.

## Duality Rotation

Maxwell's equations in a homogeneous medium possess a continuous symmetry that rotates the electric and magnetic parts into one another. For a real angle $\theta$, define

$$
\vec E \mapsto \vec E\cos\theta + c\,\vec B\sin\theta,
\qquad
\vec B \mapsto \vec B\cos\theta - \frac{1}{c}\,\vec E\sin\theta .
$$

In terms of the Riemann–Silberstein vector this is a phase rotation,

$$
\vec N \mapsto \exp(-i\theta)\,\vec N,
\qquad
\vec N^* \mapsto \exp(+i\theta)\,\vec N^*,
$$

as one checks by expanding $\exp(-i\theta)(\vec E + ic\vec B)$. The object that transforms with $\exp(+i\theta)$ is the complex conjugate $\vec N^* = \vec E - ic\vec B$, not the quaternion conjugate $\bar{\vec N}$, which for a pure vector is $\bar{\vec N} = -\vec N$ and therefore transforms with $\exp(-i\theta)$. The special case $\theta = \pi/2$,

$$
\vec E \mapsto c\,\vec B,
\qquad
\vec B \mapsto -\frac{1}{c}\,\vec E,
$$

is the classical **electric–magnetic duality** transformation.

The transformation is a symmetry of the **source-free** Maxwell equations. Under it, $\mathrm{rot}\,\vec E_{\mathrm d} = -\partial/\partial t'\vec B_{\mathrm d}$ and $\mathrm{rot}\,\vec B_{\mathrm d} = c^{-2}\partial/\partial t'\vec E_{\mathrm d}$ are preserved, the two terms of each equation matching after use of $c^2 = 1/(\epsilon\mu)$. With free electric charges and currents present, the transformation is *not* a symmetry: it would map an electric charge into a magnetic charge. Duality relates solutions of the source-free equations, and it relates the electric and magnetic parts of a given solution.

The effect of the duality rotation on the invariants is clean. Writing $\vec N\cdot\vec N = I_1 + 2icI_2$, the phase rotation gives

$$
\vec N\cdot\vec N \mapsto \exp(-2i\theta)\,\vec N\cdot\vec N,
$$

so that

$$
I_1 \mapsto I_1\cos 2\theta + 2c\,I_2\sin 2\theta,
\qquad
2c\,I_2 \mapsto 2c\,I_2\cos 2\theta - I_1\sin 2\theta .
$$

In other words, the pair $(I_1,\,2cI_2)$ rotates by the doubled angle $2\theta$; the quantity

$$
I_1^2 + 4c^2 I_2^2 = \left|\vec N\cdot\vec N\right|^2 = \frac{1}{\epsilon^2}\left|\langle\tilde{F}\rangle_{\natural}\right|^2
$$

is invariant under duality as well as under Lorentz transformations. Each of $I_1$ and $I_2$ is separately Lorentz invariant, but duality mixes them; only the combination above is invariant under both. Equivalently, in biquaternion language,

$$
\langle\tilde{F}\rangle_{\natural} \mapsto \exp(-2i\theta)\,\langle\tilde{F}\rangle_{\natural},
$$

since the scalar $\exp(-i\theta)$ commutes with quaternion conjugation, which fixes scalars. Duality is not a Lorentz transformation: it is an independent $\mathrm{U}(1)$ symmetry of the source-free equations that rotates the complex biquaternion norm.

## How the Invariants Constrain the Field

The two invariants are the complete set of local, derivative-free invariants of the electromagnetic field, and they classify the field into a small number of types. The classification is Lorentz invariant, because $I_1$ and $I_2$ are.

**Null fields.** If $I_1 = 0$ and $I_2 = 0$, then $\vec E\perp\vec B$ and $|\vec E| = c|\vec B|$ at every event. Both invariants vanish, the biquaternion norm vanishes, and the field-strength biquaternion is a zero divisor. No Lorentz transformation can remove either field, because killing one would force the other to vanish as well by the invariant relation; the field is a pure radiation field in every frame. This is the case of greatest interest for the later article on radiation.

**Electric and magnetic types.** Suppose $I_2 = 0$ but $I_1 \neq 0$. Then $\vec E$ and $\vec B$ are perpendicular. If $I_1 > 0$, the electric magnitude dominates, and there is a Lorentz frame in which $\vec B = 0$: the field is purely electric, with $\vec E^2 = I_1$ in that frame. If instead $I_1 < 0$, there is a frame in which $\vec E = 0$: the field is purely magnetic, with $c^2\vec B^2 = -I_1$. In either case the invariant fixes the magnitude of the surviving field in its rest frame.

**Generic fields.** If $I_2 \neq 0$, no frame can make either field vanish, because $I_2$ would then vanish too. Instead there is a frame in which $\vec E$ and $\vec B$ are **parallel**. In that frame $I_2 = E_0 B_0$ (with signs) and $I_1 = E_0^2 - c^2B_0^2$, and eliminating $B_0$ gives a quadratic equation for $E_0^2$,

$$
E_0^4 - I_1 E_0^2 - c^2 I_2^2 = 0,
$$

whose positive root is

$$
E_0^2 = \frac{I_1 + \sqrt{I_1^2 + 4c^2 I_2^2}}{2},
\qquad
B_0 = \frac{I_2}{E_0}.
$$

The magnitudes are therefore completely determined by the two invariants. This is the precise sense in which the invariants constrain the field: they do not determine the field, but they determine the *type* of its Lorentz orbit and the field magnitudes in the frame in which that type is displayed.

**What the invariants do not constrain.** The invariants are two functions of the six real field components, so many distinct fields share the same pair $(I_1, I_2)$: they determine the local Lorentz type but not the field. They are pointwise kinematical quantities, not dynamical ones, and they are not in general conserved by the free-field evolution — a field that is null at one instant need not be null at the next.

**Contrast with the energy density.** The biquaternion norm is indefinite and complex: it can vanish, and it gives the Lorentz invariants. The **Hermitian form** is a different quadratic object, and it gives the positive energy. For the pure vector $\tilde{F}$,

$$
\tilde{F}\tilde{F}^{*} = 2W\,e_t + \frac{2i}{c}\,\vec S,
\qquad
\tilde{F}^{*}\tilde{F} = 2W\,e_t - \frac{2i}{c}\,\vec S,
$$

with the energy density and Poynting vector

$$
W = \frac{1}{2}\left(\epsilon\,\vec E^2 + \mu\,\vec H^2\right) = \frac{1}{2}\left\|\tilde{F}\right\|_E^2,
\qquad
\vec S = \vec E\times\vec H.
$$

The scalar part of $\tilde{F}\tilde{F}^{*}$ is $2W$, twice the (non-negative) energy density, and its vector part is $\frac{2i}{c}\vec S$, $\frac{2}{c}$ times the imaginary unit times the Poynting vector; the result is an element of $\mathbb{M}_+$, as every Hermitian form must be. The contrast is instructive: the biquaternion norm is a Lorentz-invariant complex scalar that can vanish, while the Hermitian form is an $\mathbb{M}_+$-valued object whose scalar part is strictly positive and whose transformation law is not that of a scalar. The first classifies the field; the second measures it. This is the biquaternion expression of the familiar fact that the electromagnetic energy density is positive-definite, whereas the invariant $I_1$ is indefinite.

**The energy–momentum biquaternion, and the second route to the invariants.** Half the Hermitian form is itself an element of the algebra, and it is the object the electro-gravimagnetic programme calls the **energy–momentum biquaternion**:

$$
\tilde{\Sigma} = \tfrac{1}{2}\,\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\,\vec S .
$$

It is Hermitian, $\tilde{\Sigma}^{*} = \tilde{\Sigma}$, with real scalar part $W$ and imaginary vector part $(i/c)\vec S$. For an element of that shape the biquaternion norm is real — and indefinite — and

$$
\langle\tilde{\Sigma}\rangle_{\natural} = \tilde{\Sigma}\circ\tilde{\Sigma}^{\natural} = W^2 - \frac{\|\vec S\|^2}{c^2} = \frac{\epsilon^2}{4}\,I_1^2 + \frac{\epsilon}{\mu}\,I_2^2 ,
$$

The last equality is the point of the paragraph: the Hermitian form is not a scalar under Lorentz transformations, but its contraction **is**, and the contraction returns the two invariants. The energy density and the Poynting vector are therefore tied to the same pair $(I_1, I_2)$ that classifies the field. The programme states the same relation with its pseudonorm; on a Hermitian element that pseudonorm and the corpus's norm $\langle\cdot\rangle_{\natural}$ agree, so the two forms are one statement, and in vacuum ($\epsilon = \mu = 1$) it reads $\langle\tilde{\Sigma}\rangle_{\natural} = \tfrac14 I_1^2 + I_2^2$.

## Summary

The field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ is a pure-vector biquaternion with vanishing scalar part. It lies in the six-dimensional real vector part of $\mathbb{B}$, decomposed into an imaginary electric piece in the Hermitian subspace $\mathbb{M}_+$ and a real magnetic piece in the anti-Hermitian subspace $\mathbb{M}_-$. This is why the field strength is neither a four-vector nor an element of $\mathbb{M}_-$: it is an antisymmetric rank-two tensor, whose two halves occupy the two complementary sectors of the algebra.

The biquaternion norm of the field strength is the complex scalar

$$
\boxed{\;\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural} = \tilde{F}\tilde{F}^{\natural} = \sum_{\mu=1}^{3} F_\mu^2
= -\epsilon\left(I_1 + 2ic\,I_2\right)\;},
\qquad
I_1 = \vec E^2 - c^2\vec B^2,
\qquad
I_2 = \vec E\cdot\vec B.
$$

Its real and imaginary parts are the two Lorentz invariants of the field; the biquaternion norm and its complex conjugate carry the same pair. Both are invariant under the proper orthochronous Lorentz group, $I_1$ is parity-even and $I_2$ is a pseudoscalar. The biquaternion norm vanishes exactly when the field is null, in which case the field-strength biquaternion is a zero divisor.

The same object is, up to the constant $i\sqrt{\epsilon}$, the Riemann–Silberstein vector $\vec N = \vec E + ic\vec B$, whose self-product $\vec N\cdot\vec N = I_1 + 2icI_2$ is the complex number whose real and imaginary parts are the invariants, and which obeys the source-free equation $i\partial/\partial t'\vec N = c\,\mathrm{rot}\,\vec N$ with $\mathrm{div}\,\vec N = 0$.

Duality is the rotation $\vec N\mapsto \exp(-i\theta)\vec N$; at $\theta = \pi/2$ it is the classical electric–magnetic duality. It is a symmetry of the source-free Maxwell equations, and it rotates the pair $(I_1, 2cI_2)$ by the angle $2\theta$, leaving $I_1^2 + 4c^2I_2^2$ invariant. Finally, the invariants classify the field into null, electric, magnetic, and generic types, and fix the field magnitudes in the frame that displays each type; they are the complete set of local, derivative-free invariants, but they are not a complete description of the field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}}$ | Complex (scalar) subspace |
| $\mathrm{Vect}(\mathbb{B})$ | Complex three-dimensional vector part |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}$ | Biquaternionic gradient and its quaternion conjugate |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\vec E, \vec H, \vec B = \mu\vec H$ | Electric field, magnetic field, magnetic induction |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural} = \tilde{F}\tilde{F}^{\natural}$ | Biquaternion norm (complex scalar) |
| $I_1 = \vec E^2 - c^2\vec B^2$ | First Lorentz invariant (scalar) |
| $I_2 = \vec E\cdot\vec B$ | Second Lorentz invariant (pseudoscalar) |
| $\vec N = \vec E + ic\vec B$ | Riemann–Silberstein vector, $\tilde{F} = i\sqrt{\epsilon}\,\vec N$ |
| $\star$ | Hodge dual, $\star(\vec E,\vec B) = (c\vec B, -\vec E/c)$, $\star^2 = -1$ |
| $W = \tfrac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$ | Electromagnetic energy density |
| $\vec S = \vec E\times\vec H$ | Poynting vector |
| $\tilde{\Sigma} = \tfrac{1}{2}\tilde{F}\tilde{F}^{*} = W e_t + \tfrac{i}{c}\vec S$ | Energy–momentum biquaternion (Hermitian); $\langle\tilde{\Sigma}\rangle_{\natural} = W^2 - \|\vec S\|^2/c^2$ |
| $\vec v$ | Boost (frame) velocity |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, and 24 (1907) 783–784, for the original complex-vector formulation of the electromagnetic field.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for a modern account of the complex-vector and duality structure.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard treatment of the field invariants and the transformation of the fields.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the invariant classification of the field and the existence of frames in which the fields are parallel or one vanishes.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra treatment of the field strength and its invariants.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and the bivector structure of the field.
- [The General Polar Decomposition, the Amplitude and the Operator-to-State Map](the-general-polar-decomposition-amplitude-and-the-operator-to-state-map.html), for the state that a non-Hermitian operator defines and its purity strata.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time* (Cambridge, 1984), for the self-dual and anti-self-dual decomposition of the field tensor.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the representation theory of the Lorentz group and its two three-dimensional complex representations.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations.
- L. A. Alexeyeva, "Biquaternions algebra and its applications by solving of some theoretical physics equations", *Clifford Analysis, Clifford Algebras and Their Applications* **7**(1) (2012) 19–39 (arXiv:1302.0523), for the energy–momentum biquaternion $\tilde{\Sigma}$, its pseudonorm and its identification with the two field invariants.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for the biquaternionic treatment of the field and its energy–momentum.
