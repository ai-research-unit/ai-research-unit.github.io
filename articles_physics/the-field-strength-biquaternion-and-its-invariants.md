# __The Field-Strength Biquaternion and Its Invariants__

## Introduction

The companion article *Maxwell's Equations in the Biquaternionic Formulation* introduced the **field-strength biquaternion**

$$
\tilde{F} = \vec F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H
$$

as the single biquaternionic object that carries the electromagnetic field, and showed that, in a medium with permittivity $\epsilon$ and permeability $\mu$, the four Maxwell equations collapse into a single equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$. In that article $\tilde{F}$ appears as a means to an end: the compact rewriting of the field equations. This article studies $\tilde{F}$ for its own sake.

Two features make the field strength worth treating separately. First, $\tilde{F}$ is *not* a four-vector. Unlike the four-potential $\tilde{A}$, whose scalar part is imaginary and whose vector part is real, the field-strength biquaternion has **vanishing scalar part** and a **mixed real/imaginary vector part**: its imaginary half carries the electric field and its real half the magnetic field. The field strength is therefore a different kind of object from the kinematic four-vectors that live in the material subspace $\mathbb{M}_-$, and its Lorentz transformation law is correspondingly different. Second, the **biquaternion norm** (the quaternionic norm of the conventions) evaluated on $\tilde{F}$ is a complex scalar whose real and imaginary parts are the two classical Lorentz invariants, $\vec E^2 - c^2\vec B^2$ and $\vec E\cdot\vec B$, up to the medium factors $-\epsilon$ and $-2\epsilon c$. The algebraic apparatus built to describe the Minkowski metric thus delivers the electromagnetic invariants as well.

This article is the declared foundation for three later articles on electromagnetism in media, on the Lorentz force, and on radiation from accelerated charges. It therefore fixes the field-strength notation once and for all. The **canonical objects** are: the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$; the electric and magnetic fields $\vec E$ and $\vec H$, together with the magnetic induction $\vec B = \mu\vec H$; the medium speed of light $c = 1/\sqrt{\epsilon\mu}$; the Riemann–Silberstein vector $\vec N = \vec E + ic\vec B$; the two invariants $I_1 = \vec E^2 - c^2\vec B^2$ and $I_2 = \vec E\cdot\vec B$; and the energy density $W$ and Poynting vector $\vec S$. Nothing in this list is new notation; the first three come unchanged from the Maxwell article, and the rest are assembled from them.

The conventions are those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_k^2 = -e_t$, and scalar imaginary $i$ commuting with the quaternion units and satisfying $i^2=-1$; every product of two factors of $i$ below is reduced by that relation. The three-dimensional complex **vector part** of $\mathbb{B}$ is denoted by its components $\vec F = \sum_k F_k \vec e_k$, with the usual quaternion product $\vec F\vec G = -\vec F\cdot\vec G + \vec F\times\vec G$ for pure vectors. The conjugations are the quaternion conjugate ${}^{\natural}$, the complex conjugate $\bar{\cdot}$, and the Hermitian conjugate ${}^{*} = ({}^{\natural})^{\,*} = \bar{\cdot}{}^{\natural}$, with the four real fixed-point subspaces $\mathbb{C}_{\mathbb{B}}$ (scalars), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector) and $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector). The symbol $c$ always denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$; in vacuum it reduces to $c_0 = 1/\sqrt{\epsilon_0\mu_0}$.

## The Field-Strength Biquaternion

The definition is the one of the Maxwell article, repeated here because everything that follows depends on it:

$$
\tilde{F} = \vec F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H
= \sum_{k=1}^{3} F_k\, \vec e_k,
\qquad
F_k = i\sqrt{\epsilon}\,E_k - \sqrt{\mu}\,H_k .
$$

Its scalar part vanishes identically,

$$
\mathrm{Sc}(\tilde{F}) = 0,
$$

so $\tilde{F}$ is a **pure-vector** biquaternion. Its three complex components $F_k$ each combine an electric and a magnetic piece: the electric contribution $i\sqrt{\epsilon}\,E_k$ is **purely imaginary** and the magnetic contribution $-\sqrt{\mu}\,H_k$ is **real**. The factor of $i$ on the electric part is the same factor that appears in the complex time coordinate $ict'$. In the $ict'$ convention the time direction is the imaginary direction, and the electric field carries the time index of the field tensor, so it is the electric part that acquires the factor $i$ while the magnetic part remains real. This is the algebraic reason for the asymmetric appearance of $\tilde{F}$.

The normalization factors $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are the natural ones for a medium. Each term has the dimension of the square root of an energy density, since $\epsilon E^2$ and $\mu H^2$ are both energy densities; consequently $\tilde{F}$ has dimension $\sqrt{\text{energy density}}$, and the biquaternion norm calculated below has the dimension of an energy density. With the constitutive relation $\vec B = \mu\vec H$ the magnetic term may also be written $\sqrt{\mu}\,\vec H = \vec B/\sqrt{\mu}$, so the field strength can equally be regarded as the pair $(\sqrt{\epsilon}\,\vec E, \vec B/\sqrt{\mu})$.

The field strength is not an independent object: it is obtained from the potential biquaternion $\tilde{A} = i\phi/c + \vec A$ by differentiation. Let

$$
\tilde{\nabla} = e_t\frac{\partial}{\partial Q_t} + \vec e_x\frac{\partial}{\partial Q_x} + \vec e_y\frac{\partial}{\partial Q_y} + \vec e_z\frac{\partial}{\partial Q_z}
$$

be the biquaternionic gradient and $\tilde{\nabla}^{\natural}$ its quaternion conjugate. The construction is

$$
\tilde{F} = \frac{1}{\sqrt{\mu}}\Bigl(\tilde{\nabla}^{\natural}\tilde{A} - \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right)\Bigr).
$$

This is the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$ divided by $\sqrt\mu$. In cell notation the same construction is $L_{\tilde{\nabla}^{\natural}}\tilde{A}$ with the scalar part removed, where $L_a$ is the left multiplication $L_a\psi=a\psi$. In Heaviside–Lorentz units, where the two medium parameters are $1$, this is the familiar $\tilde{F}=\tilde{\nabla}^{\natural}\tilde{A}-\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ of the companion articles. In a medium with $\sqrt\mu\ne1$ the division is not optional, because $\tilde{F}$ and $\mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})$ then differ in dimension.

In tensor language the same object is the antisymmetric rank-two tensor

$$
F_{\mu\nu} = \partial/\partial Q_\mu A_\nu - \partial/\partial Q_\nu A_\mu,
\qquad
F_{\mu\nu} =
\begin{pmatrix}
0 & iE_x/c & iE_y/c & iE_z/c \\
-iE_x/c & 0 & B_z & -B_y \\
-iE_y/c & -B_z & 0 & B_x \\
-iE_z/c & B_y & -B_x & 0
\end{pmatrix}.
$$

The tensor has six independent components — three electric and three magnetic — which is exactly the information carried by the three complex components $F_k$ of the pure-vector biquaternion. The identification is exact, with one constant: $\mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})=\sqrt{\mu}\,\tilde{F}$ identically. Indeed, $\partial/\partial Q_t=-(i/c)\partial/\partial t'$ and $A_0=+i\phi/c$ give $\mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})=(i/c)\vec E-\vec B$, and $\sqrt{\mu}/c=\mu\sqrt{\epsilon}$. The tensor formula and the component combination $F_k = i\sqrt{\epsilon}E_k - \sqrt{\mu}H_k$ are then the same statement read component by component, $F_{0k}=iE_k/c$ and $F_{jk}=\epsilon_{jkl}B_l$.

## The Place of the Field Strength in the Algebra

The biquaternion algebra decomposes in several ways, and it is worth locating $\tilde{F}$ precisely in these decompositions, because its peculiar properties are consequences of its position.

**The vector part.** The pure-vector biquaternions form the complex three-dimensional subspace

$$
\mathrm{Vect}(\mathbb{B}) = \mathbb{C}\vec e_x \oplus \mathbb{C}\vec e_y \oplus \mathbb{C}\vec e_z,
$$

of real dimension six. It is *not* one of the four fixed-point subspaces $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}, \mathbb{M}_+$ and $\mathbb{M}_-$; those are real subspaces that contain the scalar line, of dimensions two and four, whereas the vector subspace contains no scalar at all. The field strength lies entirely in this subspace, and the classical statement that the electromagnetic field has six independent components is exactly the statement that $\tilde{F}$ is a general element of $\mathrm{Vect}(\mathbb{B})$.

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
\tilde{F}^{*} = -\overline{\vec F} = i\sqrt{\epsilon}\,\vec E + \sqrt{\mu}\,\vec H,
$$

so that the Hermitian and anti-Hermitian parts of the field strength are

$$
\tfrac{1}{2}\left(\tilde{F} + \tilde{F}^{*}\right) = i\sqrt{\epsilon}\,\vec E,
\qquad
\tfrac{1}{2}\left(\tilde{F} - \tilde{F}^{*}\right) = -\sqrt{\mu}\,\vec H.
$$

The split holds in the frame in which the decomposition is taken and is not Lorentz invariant: a boost mixes the two sectors. The same display shows why $\tilde{F}$ cannot lie in $\mathbb{M}_-$: the material subspace contains the real vectors but not the imaginary ones, and the electric half of the field strength uses the imaginary vector directions.

**The real/complex decomposition.** Equivalently, with respect to the complex conjugation $\bar{\cdot}$ that fixes $\mathbb{H}_{\mathbb{B}}$,

$$
\tilde{F} = \underbrace{\left(-\sqrt{\mu}\,\vec H\right)}_{\in\,\mathbb{H}_{\mathbb{B}}} \;+\; \underbrace{i\sqrt{\epsilon}\,\vec E}_{\in\,i\mathbb{H}_{\mathbb{B}}}.
$$

The scalar subspace $\mathbb{C}_{\mathbb{B}}$ receives no contribution, which is again $\mathrm{Sc}(\tilde{F}) = 0$. The decomposition used is $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$. Thus the field strength uses the vector parts of $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the electric and magnetic halves of $\mathbb{M}_+$ and $\mathbb{M}_-$, and it touches $\mathbb{C}_{\mathbb{B}}$ not at all.

**The biparavector interpretation: the field as two families of planes.** The two halves just separated are not merely subspaces; each is a **family of planes**. The separation of the field into an electric and a magnetic part is the separation of the biparavector into a timelike and a spacelike part. In the paravector presentation of the algebra (*Paravectors and the Geometry of Spacetime*), a **biparavector** is the product of two orthogonal paravectors and represents a plane in spacetime. With the paravector directions $i\vec e_k$ there are six independent planes,

$$
\{e_t\,i\vec e_k\}_{k=x,y,z}=\{i\vec e_x,i\vec e_y,i\vec e_z\},
\qquad
\{(i\vec e_j)(i\vec e_k)\}_{(j,k)=(y,x),(z,y),(x,z)}=\{\vec e_z,\vec e_x,\vec e_y\},
$$

using $(i\vec e_j)(i\vec e_k)=-\vec e_j\vec e_k$ and $i^2=-1$. The first three, the planes containing the time direction, have the form $e_t\,i\vec e_k = i\vec e_k$ and are the pure **imaginary** vectors, that is the real span of $\{i\vec e_k\} = \mathrm{Vect}(\mathbb{B})\cap\mathbb{M}_+$. The last three, the purely spatial planes, have the form $(i\vec e_j)(i\vec e_k)$ and are the pure **real** vectors, that is the real span of $\{\vec e_k\} = \mathrm{Vect}(\mathbb{B})\cap\mathbb{M}_-$.

Comparing with the decomposition above, the electric and magnetic halves of the field are exactly the two families of planes:

$$
\tilde{F} \;=\; \underbrace{i\sqrt{\epsilon}\,\vec E}_{\text{timelike planes}\;\in\,\mathbb{M}_+} \;-\; \underbrace{\sqrt{\mu}\,\vec H}_{\text{spacelike planes}\;\in\,\mathbb{M}_-}.
$$

The electric part is a real-linear combination of the three planes that contain the time direction, and the magnetic part a real-linear combination of the three that do not. This is the plane-geometric form of the algebra asymmetry: the electric part lies in the timelike-plane family and the magnetic part in the spacelike-plane family, the two families that generate the Lorentz boosts and the rotations respectively (*Symmetric and Antisymmetric Decomposition of the Four General Products*). The six components of the field are the six planes, and a general field is a real-linear combination of all six.

Two familiar facts are read off from the plane type. The **quaternion conjugate** of the field reverses the electric planes and fixes the magnetic ones,

$$
\tilde{F}^{\natural} = -i\sqrt{\epsilon}\,\vec E + \sqrt{\mu}\,\vec H,
$$

because the conjugate negates the vector part of each coefficient and the electric part is the imaginary vector while the magnetic part is the real vector. Read on the fields this is $\vec E\to-\vec E$ and $\vec H\to\vec H$, which is the same sign pattern that parity gives the polar electric field and the axial magnetic field. The **duality rotation** of the later section, $\tilde{F}\mapsto \exp(-i\varphi)\tilde{F}$, turns the electric planes into the magnetic ones and back. At $\varphi = \pi/2$ the factor is $-i$, which carries $\mathbb{M}_+$ to $\mathbb{M}_-$ and back, so the two families are exchanged: with unit impedance the exchange is the exact swap $\vec E\mapsto\vec H$, $\vec H\mapsto-\vec E$, and in a general medium the impedance factor $Z=\sqrt{\mu/\epsilon}$ enters. This is why the duality rotation is a symmetry of the source-free vacuum equations and not of the equations with electric sources: it moves the field along a circle in the $(I_1,\,2cI_2)$-plane, at constant $I_1^2+4c^2I_2^2$, without preserving the planes separately.

## The Biquaternion Norm and the Two Invariants

The biquaternion norm on $\mathbb{B}$ is

$$
\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}\bigl(\tilde{Q}\,\tilde{Q}^{\natural}\bigr) = Q_t^2+Q_x^2+Q_y^2+Q_z^2 .
$$

The central element $\tilde{Q}\tilde{Q}^{\natural}$ equals $\langle\tilde{Q}\rangle_{\natural} e_t$. For a pure-vector biquaternion the quaternion conjugate is $\tilde{F}^{\natural} = -\vec F$, and the quaternion product of two pure vectors is $\vec F\vec G = -\vec F\cdot\vec G + \vec F\times\vec G$. Hence

$$
\tilde{F}\,\tilde{F}^{\natural} = \langle\tilde{F}\rangle_{\natural} e_t,
\qquad
\langle\tilde{F}\rangle_{\natural} = \vec F\cdot\vec F = \sum_{k=1}^{3} F_k^2,
$$

because $\vec F\times\vec F = 0$, which removes the cross term. One is left with the **quaternionic norm**, a complex scalar. Substituting $F_k = i\sqrt{\epsilon}E_k - \sqrt{\mu}H_k$ and expanding, with $(i\sqrt{\epsilon})^2=-\epsilon$ from $i^2=-1$,

$$
\boxed{\;\langle\tilde{F}\rangle_{\natural} = \sum_{k=1}^{3}\left(i\sqrt{\epsilon}E_k - \sqrt{\mu}H_k\right)^2
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

**The conjugate biquaternion norm.** The quaternion norm is not the only natural quadratic object here. On a pure vector $\tilde{F}^{\natural} = -\vec F$, and the Hermitian conjugate also conjugates the coefficients, $\tilde{F}^* = -\overline{\vec F}$; that global minus is the one every real vector carries under ${}^{*}$. For the biquaternion norm of the complex-conjugate field,

$$
\langle\tilde{F}^*\rangle_{\natural} = \langle\tilde{F}\rangle_{\natural}^*,
$$

so the biquaternion norm and its conjugate carry the same two real invariants. Equivalently, for a pure vector the two products coincide, $\tilde{F}^{\natural}\tilde{F} = \tilde{F}\tilde{F}^{\natural} = \langle\tilde{F}\rangle_{\natural} e_t$. The two invariants are therefore the two real components of the complex biquaternion norm.

**Vanishing of the biquaternion norm.** Because $\tilde{F}$ is a pure vector,

$$
\tilde{F}^2 = -\vec F\cdot\vec F = -\langle\tilde{F}\rangle_{\natural} e_t,
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

The electric half of the field strength lies in $\mathbb{M}_+$ and its magnetic half in $\mathbb{M}_-$, and that mixed case is exactly the one in which the Cartan pairing carries information. The pairing gives a reading of the field that the invariants alone do not.

Write the general polar decomposition of the field as

$$
\tilde F=\tilde F_H\tilde F_0,\qquad
\tilde F_H=\sqrt{\tilde F\tilde F^{*}}\ge0,\qquad
\tilde F_0=\tilde F_H^{+}\tilde F ,
$$

where ${}^{+}$ is the Moore–Penrose inverse, which is $\tilde F_H^{-1}$ where $\tilde F$ is invertible. The amplitude is Hermitian positive semidefinite and the phase is a partial isometry. Off the null cone the amplitude is positive definite and the phase is $*$-unitary, and the pair is the Cartan pairing; on the cone the same formulas give the generalized pair.

**The amplitude carries the intensity and the invariant modulus.** The trace of its square is four times the energy density, $\operatorname{Tr}(\tilde F_H^{2})=2\langle\tilde F,\tilde F\rangle_{*}=4W$ (with $\operatorname{Tr}=2\operatorname{Sc}$), and its determinant is the modulus of the complex invariant,

$$
\langle\tilde F_H\rangle_{\natural}=\det\mathsf{M}_2(\tilde F_H)=\lvert\langle\tilde F\rangle_{\natural}\rvert
=\epsilon\sqrt{I_1^{2}+4c^{2}I_2^{2}}\ \ge 0 .
$$

The norm of the amplitude is real and non-negative even though the norm of the field is complex. The two singular values of $\tilde F$ are the eigenvalues of $\tilde F_H$, and they are fixed by $W$ and by $\lvert\langle\tilde F\rangle_{\natural}\rvert$: the energy density gives their sum of squares and the invariant modulus gives their product. The amplitude is therefore the part of the field that the invariants determine, and the phase is the part they leave free.

**The phase is the duality angle and the polarization.** The $*$-unitary factor is $\tilde F_0=\exp(i\alpha)\tilde u_{\mathrm r}$, whose central phase is the duality angle, $\alpha=\tfrac12\arg\langle\tilde F\rangle_{\natural}$ up to the branch, and whose rotor $\tilde u_{\mathrm r}$ carries the polarization state of the field. A duality rotation $\tilde F\mapsto\exp(-i\theta)\tilde F$ leaves $\tilde F_H$ unchanged and multiplies $\tilde F_0$ by $\exp(-i\theta)$, so it shifts $\alpha$ by $-\theta$; it is a motion along the phase fibre, not a change of amplitude. This is the polar form of the statement that $I_1$ and $I_2$ rotate into one another while $I_1^{2}+4c^{2}I_2^{2}$ is fixed.

**The null field is a pure state.** On the cone, $I_1=I_2=0$, the amplitude is a scaled idempotent and the phase is a partial isometry, so the state $\tilde F\tilde F^{*}/\bigl(2\langle\tilde F,\tilde F\rangle_{*}\bigr)$ is pure. The radiative field is the zero divisor of the field space, and the operator-to-state map sends it to the boundary of the Bloch ball. This is the same cone that the massless spectrum article reads as the lightlike limit.

**The boundary.** The split is canonical in the algebra, and it is not a Lorentz-covariant factorisation: the field is a bivector in the tensor reading, its Lorentz action is not the four-vector congruence, and it does not act on $\tilde F_H$ and $\tilde F_0$ separately by one and the same operation. The two invariants, and the modulus $\lvert\langle\tilde F\rangle_{\natural}\rvert$ that is their combination, are the only invariant data of the split. The polar split is also not the self-dual/anti-self-dual split: the latter uses the Hodge star and separates the two helicities, while the Cartan phase is the compact $*$-unitary quotient. The two decompositions answer different questions and must not be identified.

## Lorentz Invariance of the Invariants

The claim that $I_1$ and $I_2$ are Lorentz invariants is standard and can be checked directly. Under a boost with velocity $\vec v$, speed $v=\lvert\vec v\rvert$, and Lorentz factor

$$
\gamma = \frac{1}{\sqrt{1 - v^2/c^2}},
$$

the fields transform as

$$
\begin{aligned}
\vec E_2 &= \gamma\left(\vec E + \vec v\times\vec B\right) - \frac{\gamma-1}{v^2}\left(\vec v\cdot\vec E\right)\vec v,\\
\vec B_2 &= \gamma\left(\vec B - \frac{1}{c^2}\,\vec v\times\vec E\right) - \frac{\gamma-1}{v^2}\left(\vec v\cdot\vec B\right)\vec v.
\end{aligned}
$$

The factor $\gamma$ here is a number, not one of the frame cells that carry the $\gamma$ names in *The Gamma Formulation* below. The components parallel to the boost are unchanged, while the transverse components acquire a contribution from the other field. Substituting these expressions into $I_1$ and $I_2$ and using $1-v^2/c^2=1/\gamma^2$, the cross terms cancel and the factors combine, giving

$$
\vec E_2^2 - c^2\vec B_2^2 = \vec E^2 - c^2\vec B^2,
\qquad
\vec E_2\cdot\vec B_2 = \vec E\cdot\vec B.
$$

Both invariants are therefore unchanged. This is consistent with the rotor-conjugation transformation of the four-potential established in the Maxwell article. The field strength is built from $\tilde{A}$ by differentiation. Differentiating a quantity that transforms by rotor conjugation produces a field that transforms in the antisymmetric-tensor representation, whose two independent scalar contractions are exactly $I_1$ and $I_2$.

**Scope of the invariance.** A material medium selects a rest frame, and a boost changes the medium. The transformation above is the formal Lorentz transformation of the field tensor with $c$ the medium speed. In vacuum it is the physical Lorentz group and the invariance is exact. In a homogeneous medium it is the covariance of the field tensor at fixed $\epsilon$ and $\mu$, and the phrase *Lorentz invariant* is used in that formal sense. The classification below inherits the same scope.

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

where $(i\sqrt{\epsilon})^2=-\epsilon$ by $i^2=-1$, in agreement with the direct computation. The two invariants are the real and imaginary parts of the complex number $\vec N\cdot\vec N$, up to constant factors.

The Riemann–Silberstein vector also linearizes the source-free field equations. In vacuum or in a homogeneous medium with no free sources, Maxwell's equations give $\mathrm{rot}\,\vec E = -\partial/\partial t'\vec B$ and $\mathrm{rot}\,\vec B = c^{-2}\partial/\partial t'\vec E$, and combining these,

$$
i\,\partial/\partial t' \vec N = c\,\mathrm{rot}\,\vec N,
\qquad
\mathrm{div}\,\vec N = 0 .
$$

The first equation has the form of a Schrödinger equation whose Hamiltonian is $c\,\mathrm{rot}$; the second is the transverse (divergence-free) condition inherited from $\mathrm{div}\,\vec D = 0$ and $\mathrm{div}\,\vec B = 0$. This is the form in which the radiative content of the field is most transparent, and the null condition $\vec N\cdot\vec N = 0$ is precisely the condition that the complex vector be a null vector of the complexified spatial metric. A field whose Riemann–Silberstein vector is null, i.e. for which $\langle\tilde{F}\rangle_{\natural} = 0$, is a radiation field.

Finally, the antisymmetric field tensor decomposes into its **self-dual and anti-self-dual parts**. Define the Hodge dual by its action on the fields:

$$
\star:\ (\vec E,\vec B) \mapsto (c\,\vec B, -\vec E/c),
\qquad
\star^2 = -1.
$$

This is the $\theta = \pi/2$ case of the duality rotation below. On the Riemann–Silberstein vector the dual is multiplication by $-i$:

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

with $\star(F \pm i\star F) = \mp i\,(F \pm i\star F)$. The $\vec N$ part ($\star F = -iF$) is the **self-dual** half and the $\vec N^*$ part ($\star F = +iF$) the **anti-self-dual** half; the two halves are the two helicities of the radiation field. For a real field the two parts are complex conjugates of one another, so $\vec N^*$ adds no new data: $\vec N$ alone already carries the six real field components of $(\vec E,\vec B)$. On the complexified field space they are instead independent, and each carries one of the two three-dimensional complex representations of the Lorentz group — the two chiralities. The biquaternion proof uses the antisymmetric-tensor action of the Lorentz group, not the four-vector rotor conjugation.

*Convention.* The dual is defined here by its action on $(\vec E,\vec B)$, with $\star^2=-1$. This is the real-time convention, and it is the $\theta=\pi/2$ case of the duality rotation below, $\star\vec N=-i\vec N$. With this sign the **self-dual** half is $F+i\star F$ ($\star$-eigenvalue $-i$) and the **anti-self-dual** half is $F-i\star F$ ($\star$-eigenvalue $+i$). Reversing the sign of $\epsilon_{\mu\nu\rho\sigma}$ exchanges the two names and changes nothing else. The component-wise dual read off from the $ict'$ tensor, $(\star_{ict'}F)_{0k}=B_k$, is $-i\star$ and has $\star_{ict'}^2=+1$; it is the same decomposition, with the two parts appearing as the eigenfields $F\pm\star_{ict'}F$ of eigenvalue $\pm1$ instead of the eigenfields $F\pm i\star F$ of eigenvalue $\mp i$.

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

as one checks by expanding $\exp(-i\theta)(\vec E + ic\vec B)$. The object that transforms with $\exp(+i\theta)$ is the complex conjugate $\vec N^* = \vec E - ic\vec B$, not the quaternion conjugate $\vec N^{\natural}$, which for a pure vector is $\vec N^{\natural} = -\vec N$ and therefore transforms with $\exp(-i\theta)$; the two symbols are distinct, ${}^{*}$ conjugating the coefficients of the complex vector and ${}^{\natural}$ negating it. The special case $\theta = \pi/2$,

$$
\vec E \mapsto c\,\vec B,
\qquad
\vec B \mapsto -\frac{1}{c}\,\vec E,
$$

is the classical **electric–magnetic duality** transformation.

The transformation is a symmetry of the **source-free** Maxwell equations. Writing $\vec E_\theta,\vec B_\theta$ for the rotated fields, the two equations are preserved, $\mathrm{rot}\,\vec E_\theta = -\partial/\partial t'\,\vec B_\theta$ and $\mathrm{rot}\,\vec B_\theta = c^{-2}\partial/\partial t'\,\vec E_\theta$, the two terms of each matching after use of $c^2 = 1/(\epsilon\mu)$. With free electric charges and currents present, the transformation is *not* a symmetry: it would map an electric charge into a magnetic charge. Duality relates solutions of the source-free equations, and it relates the electric and magnetic parts of a given solution.

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

In other words, the pair $(I_1,\,2cI_2)$ rotates by the angle $-2\theta$; the quantity

$$
I_1^2 + 4c^2 I_2^2 = \left|\vec N\cdot\vec N\right|^2 = \frac{1}{\epsilon^2}\left|\langle\tilde{F}\rangle_{\natural}\right|^2
$$

is invariant under duality as well as under Lorentz transformations. Each of $I_1$ and $I_2$ is separately Lorentz invariant, but duality mixes them; only the combination above is invariant under both. Equivalently, in biquaternion language,

$$
\langle\tilde{F}\rangle_{\natural} \mapsto \exp(-2i\theta)\,\langle\tilde{F}\rangle_{\natural},
$$

since the scalar $\exp(-i\theta)$ is central and therefore commutes with quaternion conjugation. Duality is not a Lorentz transformation: it is an independent $\mathrm{U}(1)$ symmetry of the source-free equations that rotates the complex biquaternion norm.

## How the Invariants Constrain the Field

The two invariants are the complete set of local, derivative-free invariants of the electromagnetic field, and they classify the field into a small number of types. The classification is invariant under the Lorentz action just described, because $I_1$ and $I_2$ are.

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

The scalar part of $\tilde{F}\tilde{F}^{*}$ is $2W$, twice the (non-negative) energy density, and its vector part is $\frac{2i}{c}\vec S$, $\frac{2}{c}$ times the imaginary unit times the Poynting vector; the result is an element of $\mathbb{M}_+$, as every Hermitian form must be. The contrast is instructive: the biquaternion norm is a Lorentz-invariant complex scalar that can vanish, while the Hermitian form is an $\mathbb{M}_+$-valued object whose scalar part is non-negative — and positive unless the field vanishes — and whose transformation law is not that of a scalar. The first classifies the field; the second measures it. This is the biquaternion expression of the familiar fact that the electromagnetic energy density is positive-definite, whereas the invariant $I_1$ is indefinite.

**The energy–momentum biquaternion, and the second route to the invariants.** Half the Hermitian form is itself an element of the algebra, and it is the object the electro-gravimagnetic programme calls the **energy–momentum biquaternion**:

$$
\tilde{\Sigma} = \tfrac{1}{2}\,\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\,\vec S .
$$

It is Hermitian, $\tilde{\Sigma}^{*} = \tilde{\Sigma}$, with real scalar part $W$ and imaginary vector part $(i/c)\vec S$. For an element of that shape the biquaternion norm is real — and indefinite — and

$$
\langle\tilde{\Sigma}\rangle_{\natural} = \mathrm{Sc}\bigl(\tilde{\Sigma}\tilde{\Sigma}^{\natural}\bigr) = W^2 - \frac{\|\vec S\|^2}{c^2} = \frac{\epsilon^2}{4}\,I_1^2 + \frac{\epsilon}{\mu}\,I_2^2 .
$$

The last equality is the point of the paragraph: the Hermitian form is not a scalar under Lorentz transformations, but its contraction **is**, and the contraction returns the two invariants. The energy density and the Poynting vector are therefore tied to the same pair $(I_1, I_2)$ that classifies the field. The programme states the same relation with its pseudonorm; on a Hermitian element that pseudonorm and the corpus's norm $\langle\cdot\rangle_{\natural}$ agree, so the two forms are one statement, and in vacuum ($\epsilon = \mu = 1$) it reads $\langle\tilde{\Sigma}\rangle_{\natural} = \tfrac14 I_1^2 + I_2^2$.

### The Flow the Field Generates: The Four Types

**The field is a generator, not only a value.** The real span of $\vec e_x,\vec e_y,\vec e_z,i\vec e_x,i\vec e_y,i\vec e_z$ is the bivector part of $\mathrm{Cl}^{+}_{1,3}$, which is the Lie algebra of the Lorentz group. The field therefore defines a one-parameter subgroup of the group acting at the event where it is evaluated, and the subgroup has two spellings that differ by the factor of two of *Norm and Pairing Conventions*: the rotor $U(t)=\exp(\tfrac12 t\tilde F)$ of the unit group, acting by $\tilde X\mapsto U(t)\tilde XU(t)^{*}$, and the matrix $\Lambda(t)=\exp(tG)$ of that congruence in the defining representation, where $G$ is the generator with one index raised. The half sits in the rotor because the exponent angle of a rotor is half the rapidity it generates; the matrix carries the full parameter. The spectrum is fixed by the two invariants alone. Let $\sigma+i\omega$ be the principal square root of $\vec N\cdot\vec N$, so that $\sigma\ge0$ and

$$
\sigma^2-\omega^2=I_1,\qquad \sigma\omega=c\,I_2,\qquad \sigma^2+\omega^2=\sqrt{I_1^2+4c^2I_2^2},
$$

with $\omega$ carrying the sign of $I_2$ when $I_2\ne0$.

**The two rates.** The eigenvalues of the generator of $\Lambda$ are $\pm\sigma/c$ and $\pm i\omega/c$, so

$$
\operatorname{Tr}\Lambda(t)=2\cosh\frac{t\sigma}{c}+2\cos\frac{t\omega}{c},\qquad \det\Lambda(t)=1 ,
$$

which is the quickest check of a computed flow. The characteristic polynomial is $(\lambda^2-\sigma^2/c^2)(\lambda^2+\omega^2/c^2)$, which is the form that *The Lorentz Force in Biquaternion Form* writes as $\lambda^4-(I_1/c^2)\lambda^2-I_2^2/c^2$; eigenvalues are convention-independent, so the two articles carry the same two numbers. Those numbers are **rates of the flow**, a rapidity per unit $t$ and an angle per unit $t$, and the rotor stores half of each.

**The type of the field is the type of its own flow.**

| invariants | $(\sigma,\omega)$ | flow $\Lambda(t)$ | field type |
|---|---|---|---|
| $I_2=0$, $I_1>0$ | $\omega=0$ | boost along $\vec E$, rapidity rate $\sigma/c$ | electric |
| $I_2=0$, $I_1<0$ | $\sigma=0$ | rotation about $\vec B$, rate $\omega/c$ | magnetic |
| $I_1=I_2=0$ | $0,\,0$ | null rotation | null |
| otherwise | $\sigma,\omega\neq0$ | boost composed with rotation | generic |

**These are the four classical types of a one-parameter Lorentz transformation** — hyperbolic, elliptic, parabolic and loxodromic in Herglotz's naming, the classification that *A Brief History of Biquaternions in Physics* records from Herglotz as the four types of a Möbius transformation. The table is therefore not new data on the field. It is the classification of the paragraphs above followed through the exponential rather than left in the algebra, and the two descriptions coincide row by row. Three contributions are separable here and are kept apart: the classification of the one-parameter transformations is Herglotz's, the closed form of the exponential in terms of the two invariants, with its two regimes and its null limit, is Jadczyk and Szulga's, and the reading of the field-strength biquaternion itself as the element of the algebra is this corpus's. The axis of each flow is a line, not an oriented vector: the boost axis is the electric direction and the rotation axis the magnetic one, while the sense of each is that of the exponential itself and is not fixed by the invariants.

**The null row is where the two spellings of one rotation are told apart.** There $\tilde F^2=0$, so the rotor is $e_t+\tfrac12t\tilde F$ and the congruence is unipotent. In the defining representation the same flow has $(\Lambda-I_4)^3=0$ with $(\Lambda-I_4)^2\neq0$, the Jordan form $J_3(1)\oplus J_1(1)$ of the degenerate case in *The Sandwich Exponential of an N-Regular, Spectrally Degenerate Biquaternion*. Both statements describe one null rotation; what differs is the representation that carries it, and the difference is the same one that makes $\tilde F$ a zero divisor while the matrix $G$ is not.

**The flow fixes its own generator, and that separates the flow from the field.** Because $U(t)$ is a power series in $\tilde F$ it commutes with it, so the subgroup it generates leaves the tensor at the event unchanged: the flow moves frames and not the field. What the flow is not is a worldline. The worldline of a charge is the flow of the generator multiplied by the scalar $ϙ/m$ acting on the four-momentum, in *The Lorentz Force in Biquaternion Form*; the two generators differ by that scalar, and they agree only in a uniform field, since otherwise the field varies along the motion and the exponent is an ordered product rather than a single exponential.

**The invariants and the flow determine each other, with one exception.** From $(I_1,I_2)$ the pair $(\sigma^2,\omega^2)$ is recovered, and from the conjugacy class of the flow the pair is recovered as $I_1=\sigma^2-\omega^2$ and $cI_2=\sigma\omega$; the pair therefore determines the flow up to conjugacy and is determined by it. The exception is the null row, where $(0,0)$ is shared by the vanishing field, whose flow is the identity, and by a null field, whose flow is a nontrivial unipotent subgroup; there the pair does not separate the two, and the Jordan form does.

**Checks.** Over $100$ random fields with $c$ drawn from $[0.6,1.8]$ and $t=0.4,0.9$, the trace of $\Lambda(t)$ agreed with $2\cosh(t\sigma/c)+2\cos(t\omega/c)$ to $3\times10^{-15}$ and $\det\Lambda(t)=1$ held to $8\times10^{-15}$; the coefficient of $\lambda^2$ in the characteristic polynomial agreed with $-I_1/c^2$ to $2\times10^{-15}$; the sign of $\omega$ followed the sign of $I_2$ in every case. A pure electric field of unit magnitude along $(1,2,2)$ gave a boost along that axis with $\operatorname{Tr}\Lambda=2\cosh(0.5)+2$, and a pure magnetic field of magnitude two along $(2,2,1)$ a rotation fixing that axis with $\operatorname{Tr}\Lambda=2+2\cos(0.8)$, each to machine precision. A null field gave $\tilde F^2=0$ in the algebra, a generator squaring to something nonzero and cubing to zero in the defining representation, and an exponential truncating at $I_4+tG+\tfrac12t^2G^2$; a generic field gave four distinct eigenvalues. For the rotor the congruence was checked directly: the matrix of $\tilde X\mapsto U(s)\tilde XU(s)^{*}$ with $U(s)=\exp(s\tilde F)$ has trace $2\cosh(2s\sigma)+2\cos(2s\omega)$ at $c=1$ to $5\times10^{-15}$, which is the factor of two displayed.

**Boundary.** The section adds an interpretation and no dynamics. It does not refine the classification of the paragraphs above, and it computes no flow that the field equations ask for. What it records is that the pair which already fixed the frame displaying the field also fixes what the field generates: the invariants are the spectral data of the flow. The standard forms of the four types, their normalisations and their classification up to conjugacy are not developed here; they are Minguzzi's, and *Further Reading* cites them.

## The Gamma Formulation

The body of this article writes the field as an element of $\mathbb{B}$; its cell reading is the left multiplication $L_{\tilde F}$. The gamma names are attached to the frame cells only here.

The cells come in two families, the left multiplications $L_a$ and the right multiplications $R_b$,

$$
L_a\psi=a\psi,\qquad R_b\psi=\psi b .
$$

Two cells multiply by multiplying the left factors and the right factors, with the right order reversed,

$$
L_aR_b\,L_cR_d=L_{ac}R_{db},
$$

because $R_bR_d=R_{db}$. Every two-sided operator is a sum of the sixteen products,

$$
M=\sum_{\mu,\nu}c_{\mu\nu}(M)\,L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
M=\sum_{\mu,\nu}c_{\mu\nu}(M)\,L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}},
$$

where $e_\mu$ runs over the four basis elements $e_t,\vec e_x,\vec e_y,\vec e_z$, so the coefficient matrix $c(M)$ is unique. A cell is a pure tensor of rank one; the cells form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four cells.

The gamma cells are

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

In the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

Every generator carries exactly one factor of $i$, so a product of two generators carries $i^2=-1$ and is a plain cell. For example,

$$
\gamma_0\gamma_1=i^2L_{e_t\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}
=-L_{\vec e_x}^{\mathrm{pau}}R_{-\vec e_z}^{\mathrm{pau}}=+L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same identities in the axis-free display:

$$
\gamma_0\gamma_1=i^2L_{e_t\vec e_x}^{\mathrm{axf}}R_{\vec e_y\vec e_x}^{\mathrm{axf}}
=-L_{\vec e_x}^{\mathrm{axf}}R_{-\vec e_z}^{\mathrm{axf}}=+L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

The same collapse gives the squares and the Clifford relations,

$$
\gamma_0^2=e_t,\qquad
\gamma_1^2=\gamma_2^2=\gamma_3^2=-e_t,\qquad
\gamma_5^2=e_t,
$$

$$
\{\gamma_\mu,\gamma_\nu\}=2\eta_{\mu\nu}e_t,\qquad
\{\gamma_5,\gamma_\mu\}=0,
$$

with $\eta=\operatorname{diag}(+1,-1,-1,-1)$, and the volume element

$$
\gamma_0\gamma_1\gamma_2\gamma_3=-i\gamma_5 .
$$

A single $i$ also collapses when it multiplies a generator:

$$
i\gamma_0=-L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
i\gamma_1=-L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
i\gamma_2=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
i\gamma_3=-L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
i\gamma_5=+L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

Read in the axis-free display:

$$
i\gamma_0=-L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
i\gamma_1=-L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
i\gamma_2=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
i\gamma_3=-L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
i\gamma_5=+L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

$\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell $\Gamma$, the involution that grades the Dirac module (*Chirality: The Conjugate Pair*). The central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object; being central, it acts on the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ as $\operatorname{diag}(-I_2,I_2)$, and $\gamma_5$ is its representative there.

**The two Dirac equations.** The two families separate the corpus's two Dirac equations. The one-sided pair acts with the left family alone,

$$
L_{\tilde\nabla}\tilde\Psi_R=m\tilde\Psi_L,\qquad
L_{\tilde\nabla^{\natural}}\tilde\Psi_L=m\tilde\Psi_R,
$$

where both derivatives act from the left, the mass is $m$, and $\tilde\Psi_R$ and $\tilde\Psi_L$ are the two chirality halves. The two-sided equation carries the mass through the right family. It holds for a biquaternion-valued Dirac field $F$, which is not the field strength $\tilde F$ of this article,

$$
\left(iL_{e_t}^{\mathrm{pau}}\frac{\partial}{\partial t'}+\sum_kL_{\vec e_k}^{\mathrm{pau}}\frac{\partial}{\partial Q_k}\right)F
-mi\,R_{\vec e_z}^{\mathrm{pau}}\bar F=0,
$$

The same expressions, in the axis-free display:

$$
\left(iL_{e_t}^{\mathrm{axf}}\frac{\partial}{\partial t'}+\sum_kL_{\vec e_k}^{\mathrm{axf}}\frac{\partial}{\partial Q_k}\right)F
-mi\,R_{\vec e_z}^{\mathrm{axf}}\bar F=0,
$$

where the derivative acts from the left, the mass acts from the right through $\vec e_z$, and $\bar F$ is the coefficient conjugate. The two equations share the frame but not the operator: the one-sided pair splits the field into chirality halves; the two-sided equation is antilinear in its mass term and carries the chirality in the right multiplication.

The dictionary is complex-linear, so over $\mathbb{C}$ the five generators generate the whole of $M_4(\mathbb{C})$. Over $\mathbb{R}$ the sixteen products of the five generators span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, and the sixteen cells $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ span the opposite real form $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ (*Matrix Representations and Conventions*).

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ is a pure-vector biquaternion with vanishing scalar part. It lies in the six-dimensional real vector part of $\mathbb{B}$, decomposed into an imaginary electric piece in the Hermitian subspace $\mathbb{M}_+$ and a real magnetic piece in the anti-Hermitian subspace $\mathbb{M}_-$. This is why the field strength is neither a four-vector nor an element of $\mathbb{M}_-$: it is an antisymmetric rank-two tensor, whose two halves occupy the two complementary sectors of the algebra.

The biquaternion norm of the field strength is the complex scalar

$$
\boxed{\;\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural} = \mathrm{Sc}\bigl(\tilde{F}\tilde{F}^{\natural}\bigr) = \sum_{k=1}^{3} F_k^2
= -\epsilon\left(I_1 + 2ic\,I_2\right)\;},
\qquad
I_1 = \vec E^2 - c^2\vec B^2,
\qquad
I_2 = \vec E\cdot\vec B.
$$

Its real and imaginary parts are the two invariants of the field; the biquaternion norm and its complex conjugate carry the same pair. Both are invariant under the proper orthochronous Lorentz group — exactly in vacuum, formally in a medium; see §*Lorentz Invariance of the Invariants* — and $I_1$ is parity-even while $I_2$ is a pseudoscalar. The biquaternion norm vanishes exactly when the field is null, in which case the field-strength biquaternion is a zero divisor.

The same object is, up to the constant $i\sqrt{\epsilon}$, the Riemann–Silberstein vector $\vec N = \vec E + ic\vec B$, whose self-product $\vec N\cdot\vec N = I_1 + 2icI_2$ carries the two invariants, and which obeys the source-free equation $i\partial/\partial t'\vec N = c\,\mathrm{rot}\,\vec N$ with $\mathrm{div}\,\vec N = 0$.

Duality is the rotation $\vec N\mapsto \exp(-i\theta)\vec N$; at $\theta = \pi/2$ it is the classical electric–magnetic duality. It is a symmetry of the source-free Maxwell equations, and it rotates the pair $(I_1, 2cI_2)$ by the angle $-2\theta$, leaving $I_1^2 + 4c^2I_2^2$ invariant.

The field also has a polar reading, $\tilde F=\tilde F_H\tilde F_0$: the amplitude carries the intensity and the invariant modulus, and the phase carries the duality angle and the polarization. The gamma cells supply the Clifford frame, in which the field has a cell reading and the two Dirac equations are the one-sided pair and the two-sided equation.

Finally, the invariants classify the field into null, electric, magnetic, and generic types, and fix the field magnitudes in the frame that displays each type; they are the complete set of local, derivative-free invariants, but they are not a complete description of the field. The same pair fixes what the field generates: since the field is an element of the Lorentz Lie algebra, its exponential is a one-parameter subgroup whose type — hyperbolic, elliptic, parabolic or loxodromic — is the type of the field, so the classification followed through the exponential agrees row by row with the classification in the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
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
| $\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural} = \mathrm{Sc}(\tilde{F}\tilde{F}^{\natural}) = \sum_k F_k^2$ | Biquaternion norm (complex scalar) |
| $I_1 = \vec E^2 - c^2\vec B^2$ | First Lorentz invariant (scalar) |
| $I_2 = \vec E\cdot\vec B$ | Second Lorentz invariant (pseudoscalar) |
| $\vec N = \vec E + ic\vec B$ | Riemann–Silberstein vector, $\tilde{F} = i\sqrt{\epsilon}\,\vec N$ |
| $\sigma,\omega$ | The square root of the complex norm, $\sigma+i\omega=\sqrt{\vec N\cdot\vec N}$ with $\sigma\ge0$: $\sigma^2-\omega^2=I_1$ and $\sigma\omega=cI_2$; the flow's rapidity rate is $\sigma/c$ and its angle rate $\omega/c$ |
| $U(t)$, $\Lambda(t)$ | The rotor $U(t)=\exp(\tfrac12t\tilde F)$ and the Lorentz matrix $\Lambda(t)=e^{tG}$ of its congruence, $G$ the generator with one index raised |
| $\star$ | Hodge dual, $\star(\vec E,\vec B) = (c\vec B, -\vec E/c)$, $\star^2 = -1$ |
| $W = \tfrac{1}{2}(\epsilon\vec E^2 + \mu\vec H^2)$ | Electromagnetic energy density |
| $\vec S = \vec E\times\vec H$ | Poynting vector |
| $\tilde{\Sigma} = \tfrac{1}{2}\tilde{F}\tilde{F}^{*} = W e_t + \tfrac{i}{c}\vec S$ | Energy–momentum biquaternion (Hermitian); $\langle\tilde{\Sigma}\rangle_{\natural} = W^2 - \|\vec S\|^2/c^2$ |
| $\tilde F_H, \tilde F_0$ | Amplitude and phase of the general polar decomposition, $\tilde F=\tilde F_H\tilde F_0$ |
| $\tilde u_{\mathrm r}$ | Unit real quaternion rotor, the polarization factor of $\tilde F_0$ |
| $\gamma = 1/\sqrt{1-v^2/c^2}$ | Lorentz factor (a number, not a gamma cell) |
| $\vec v$ | Boost velocity, speed $v=\lvert\vec v\rvert$ |
| $L_a, R_b$ | Left and right multiplication cells, $L_a\psi=a\psi$, $R_b\psi=\psi b$ |
| $\gamma_0,\dots,\gamma_3,\gamma_5$ | The five gamma generators, frame of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, listed in §*The Gamma Formulation* |
| $c(M)$ | Coefficient matrix of the two-sided operator $M$ |
| $\Gamma = \gamma_5 = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, representative of $\chi_{\mathrm{ad}}$ on the Dirac module |
| $F$ | Biquaternion-valued Dirac field of the two-sided equation, not the field strength |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | The general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | The general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, and 24 (1907) 783–784, for the original complex-vector formulation of the electromagnetic field.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for a modern account of the complex-vector and duality structure.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard treatment of the field invariants and the transformation of the fields.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the invariant classification of the field and the existence of frames in which the fields are parallel or one vanishes.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra treatment of the field strength and its invariants.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and the bivector structure of the field.
- [The General Polar Decomposition, the Amplitude and the Operator-to-State Map](the-general-polar-decomposition-the-amplitude-and-the-operator-to-state-map.html), for the state that a non-Hermitian operator defines and its purity strata.
- [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html), for the gamma frame, the central grading and the chiral halves.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the one-sided and two-sided equations and the mass term.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time* (Cambridge, 1984), for the self-dual and anti-self-dual decomposition of the field tensor.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the representation theory of the Lorentz group and its two three-dimensional complex representations.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations.
- L. A. Alexeyeva, "Biquaternions algebra and its applications by solving of some theoretical physics equations", *Clifford Analysis, Clifford Algebras and Their Applications* **7**(1) (2012) 19–39 (arXiv:1302.0523), for the energy–momentum biquaternion $\tilde{\Sigma}$, its pseudonorm and its identification with the two field invariants.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for the biquaternionic treatment of the field and its energy–momentum.
- Arkadiusz Jadczyk and Jerzy Szulga, "A Comment on 'On the Rotation Matrix in Minkowski Space-time' by Özdemir and Erdoğdu", arXiv:1412.5581 [physics.gen-ph] (2014), for the exponential of a Lorentz generator in closed form in terms of the two field invariants, its two regimes and its null limit, and the identification of the four field types with the four types of the one-parameter flow; the identities of §*The Flow the Field Generates* were recomputed here, and the identification of the field-strength biquaternion with the generator is the corpus's, not the source's.
- E. Minguzzi, "Relativistic Chasles' Theorem and the Conjugacy Classes of the Inhomogeneous Lorentz Group", arXiv:1205.4131 [gr-qc] (2013), for the classification of Lorentz generators into standard forms up to conjugacy, which §*The Flow the Field Generates* cites and does not derive.
