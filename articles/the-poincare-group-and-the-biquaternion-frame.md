# __The Poincaré Group and the Biquaternion Frame__

## Introduction

The biquaternion description of a Lorentz transformation is a description of the **homogeneous** part of relativistic kinematics: it reorients a frame and changes its state of motion, but it holds the origin fixed. A change of inertial frame also shifts the origin, and the group that contains both operations is the **Poincaré group**, the ten-parameter group of transformations
$$
x^\mu \;\longmapsto\; \Lambda^\mu{}_\nu\,x^\nu + a^\mu
$$
of Minkowski space. The question this article answers is how much of that group the biquaternion algebra $\mathbb{B}$ contains.

The homogeneous factor is contained exactly. The unit-norm biquaternions are $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group $SO^+(1,3)$, and rotor conjugation
$$
\tilde{X}\;\longmapsto\;\tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger,
\qquad \tilde{X}\in\mathbb{M}_-,\quad \tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0,
$$
is that group's action on the material sector $\mathbb{M}_-$. This is the content of the companion article *The Biquaternion Lorentz Group — Structure and Representations*, and it is recalled below rather than rederived.

The translation factor is **not** a rotation in this algebra. A rotor conjugation is linear in $\tilde{X}$ and fixes $\tilde{X}=0$; a shift $\tilde{X}\mapsto\tilde{X}+\tilde{a}$ is affine and does not fix the origin unless $\tilde{a}=0$. No unit-norm biquaternion generates a shift, and the obstruction is quantitative as well as qualitative: the restricted Poincaré group has real dimension ten, while the group of unit-norm biquaternions has real dimension six, so no assignment of a rotor to each Poincaré element can be faithful. The translation must be carried as an extra datum, an element $\tilde{a}\in\mathbb{M}_-$ placed beside the rotor. The group law on the resulting pairs is a **semidirect product**,
$$
\text{Poincaré}\;\cong\;SL(2,\mathbb{C})\ltimes\mathbb{R}^4,
\qquad \mathbb{R}^4\cong(\mathbb{M}_-,+),
$$
with the homogeneous factor acting on the translations by rotor conjugation. The algebra supplies the first factor and the vector representation by which it acts on the second; together these determine the semidirect product, but the second factor is not itself built from rotors.

Whether the translation can nonetheless be represented *inside* an algebra of the same kind — as an additive shift in a suitable module, or as a rotor after adjoining new generators, as the dual quaternions do for Euclidean rigid motions — is the open question. The article states it as open and does not resolve it.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_1e_2=e_3$, and the scalar imaginary is $i$, which commutes with the quaternion units. The anti-Hermitian and Hermitian subspaces are
$$
\mathbb{M}_-=\{\tilde{Q}:\tilde{Q}^\dagger=-\tilde{Q}\},\qquad
\mathbb{M}_+=\{\tilde{Q}:\tilde{Q}^\dagger=\tilde{Q}\},
$$
and $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace, the fixed-point set of complex conjugation. The trace formula of the informational sector is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. Throughout, $c=1/\sqrt{\epsilon\mu}$ denotes the speed of light in the medium and $c_0$ the vacuum speed of light.

## The Homogeneous Part, Recalled

Rotor conjugation restricted to $\mathbb{M}_-$ is linear in $\tilde{X}$, it preserves the subspace $\mathbb{M}_-$, and it preserves the norm form, $\tilde{X}'\bar{\tilde{X}'}=\tilde{X}\bar{\tilde{X}}$; it is an inner automorphism of $\mathbb{B}$ in the unitary sector, where $\tilde{R}^\dagger=\tilde{R}^{-1}$ and the map is conjugation, but a boost rotor is Hermitian, $\tilde{B}^\dagger=\tilde{B}$, and acts by the twisted map $\tilde{X}\mapsto\tilde{B}\tilde{X}\tilde{B}$, which is linear but not multiplicative and so is not an algebra automorphism. The map
$$
\Pi:\ SL(2,\mathbb{C})\longrightarrow SO^+(1,3),\qquad
\Pi(\tilde{\Lambda}):\ \tilde{X}\longmapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger
$$
is a surjective two-to-one homomorphism with kernel $\{\pm e_0\}$; the two-to-one cover is the reason the biquaternion description of the Lorentz group is a description of $SL(2,\mathbb{C})$ and not of $SO^+(1,3)$ directly. The homomorphism property
$$
\Pi(\tilde{\Lambda}_2\tilde{\Lambda}_1)=\Pi(\tilde{\Lambda}_2)\circ\Pi(\tilde{\Lambda}_1)
$$
is what makes the product of rotors compose Lorentz transformations, and it is the homogeneous half of the group law derived below.

Three families of rotors are distinguished by the subspace they occupy. A pure boost along the unit direction $\hat{\mathbf{u}}\in\mathbb{H}_{\mathbb{B}}$ with rapidity $\psi$,
$$
\tilde{B}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}},
$$
is Hermitian, hence lies in $\mathbb{M}_+$, and is unit-norm. A pure spatial rotation about $\hat{\mathbf{n}}\in\mathbb{H}_{\mathbb{B}}$ by angle $\theta$,
$$
\tilde{R}=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\,\hat{\mathbf{n}},
$$
is a unit real quaternion, lying in $\mathbb{H}_{\mathbb{B}}$. A general rotor has the Cartan decomposition $\tilde{\Lambda}=\tilde{B}\tilde{R}$ into a boost and a rotation. The boosts are closed under inverse but not under multiplication: the product of two non-collinear boosts is a boost times a rotation, the Thomas–Wigner rotation, whose angle and axis are derived in the parent article. What matters here is only that all of these transformations are algebraic in the rotor and linear in the four-vector they act on.

## Pairs and the Group Law

A Poincaré transformation acts on the material sector by the affine map
$$
\tilde{X}\;\longmapsto\;\tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger+\tilde{a},
\qquad \tilde{\Lambda}\in SL(2,\mathbb{C}),\quad \tilde{a}\in\mathbb{M}_-,
$$
and we write it as the pair $(\tilde{\Lambda},\tilde{a})$. The displacement $\tilde{a}$ is a four-vector and lives in the same subspace as the four-position, $\mathbb{M}_-$; that is the only subspace available to it, and it is the additive data the rotor cannot supply.

Composing two such maps, applying $(\tilde{\Lambda}_1,\tilde{a}_1)$ first and $(\tilde{\Lambda}_2,\tilde{a}_2)$ second, gives
$$
\tilde{\Lambda}_2\bigl(\tilde{\Lambda}_1\tilde{X}\tilde{\Lambda}_1^\dagger+\tilde{a}_1\bigr)\tilde{\Lambda}_2^\dagger+\tilde{a}_2
=\bigl(\tilde{\Lambda}_2\tilde{\Lambda}_1\bigr)\tilde{X}\bigl(\tilde{\Lambda}_2\tilde{\Lambda}_1\bigr)^\dagger
+\tilde{\Lambda}_2\tilde{a}_1\tilde{\Lambda}_2^\dagger+\tilde{a}_2 .
$$
The result is again a transformation of the same form, because $\tilde{\Lambda}_2\tilde{\Lambda}_1$ is unit-norm and $\tilde{\Lambda}_2\tilde{a}_1\tilde{\Lambda}_2^\dagger$ lies in $\mathbb{M}_-$. The composition law is therefore
$$
\boxed{\ (\tilde{\Lambda}_2,\tilde{a}_2)\circ(\tilde{\Lambda}_1,\tilde{a}_1)
=\bigl(\tilde{\Lambda}_2\tilde{\Lambda}_1,\ \tilde{\Lambda}_2\tilde{a}_1\tilde{\Lambda}_2^\dagger+\tilde{a}_2\bigr)\ }
$$
with the right factor applied first. Several features of this law are worth isolating.

- **The rotors multiply.** The homogeneous slot composes by biquaternion multiplication, as in the parent article.
- **The translations are not simply added.** The first displacement is carried through the second rotor before the second displacement is added, so the translation slot of the product is $\Pi(\tilde{\Lambda}_2)\tilde{a}_1+\tilde{a}_2$, not $\tilde{a}_1+\tilde{a}_2$.
- **The identity** is $(e_0,0)$, and the **inverse** is
$$
(\tilde{\Lambda},\tilde{a})^{-1}=\bigl(\bar{\tilde{\Lambda}},\ -\bar{\tilde{\Lambda}}\,\tilde{a}\,\bar{\tilde{\Lambda}}^\dagger\bigr),
$$
as one verifies directly: the inverse rotor is the quaternion conjugate, and the displacement is carried back through it.
- **Associativity** is inherited from composition of maps on $\mathbb{M}_-$; it was also checked on concrete elements.

This law makes the set of pairs a group. It is a group of **pairs**, not a group of biquaternions: the first slot uses the algebra's multiplication and the second uses the vector-space addition. The algebra appears twice in different roles, and the group structure joins them.

## Translation Is Not a Rotation

It is not an accident of parametrisation that the translation is separated out. Three statements, of increasing strength, show that no multiplicative gadget in $\mathbb{B}$ can produce it.

**A rotor conjugation cannot shift.** Conjugation fixes the origin: $\tilde{\Lambda}\,0\,\tilde{\Lambda}^\dagger=0$ for every rotor. A shift by $\tilde{a}\ne0$ sends $0$ to $\tilde{a}$. Since both maps are linear-plus-constant and they disagree at one point, no rotor conjugation equals a nonzero translation.

**Conjugation preserves the norm form pointwise; a shift does not.** For any rotor, $N(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger)=N(\tilde{X})$. A shift changes the norm form of a single element:
$$
N(\tilde{X}+\tilde{a})=N(\tilde{X})+\mathrm{Sc}\bigl(\tilde{X}\bar{\tilde{a}}+\tilde{a}\bar{\tilde{X}}\bigr)+N(\tilde{a}),
$$
and the correction terms vanish for all $\tilde{X}$ only when $\tilde{a}=0$. The norm form of a four-vector is origin-dependent; only the norm form of a **difference** is intrinsic. This is why the affine map, and not a linear one, is the physically correct transformation: the interval $(\tilde{X}_1-\tilde{X}_2)\overline{(\tilde{X}_1-\tilde{X}_2)}$ is unchanged by the shift, since the displacements cancel, and a Poincaré transformation preserves it.

**No homomorphism into the rotor group can be faithful.** Suppose one attempts to attach to every Poincaré element a unit-norm biquaternion, so that the Lorentz part of the action is rotor conjugation. Its homogeneous part is then a Lie-group homomorphism from the restricted Poincaré group into $SL(2,\mathbb{C})$. The restricted Poincaré group is connected of real dimension $10$; $SL(2,\mathbb{C})$, as a real Lie group, has dimension $6$ (equivalently $8$ for $\mathbb{B}^\times\cong GL(2,\mathbb{C})$). A Lie-group homomorphism from a connected group of dimension $10$ to a group of dimension $6$ has a kernel of dimension at least $4$. It therefore cannot be injective: a subgroup of dimension at least four acts trivially, and the ten parameters cannot all be distinguished. The group of unit-norm biquaternions is simply too small to hold the Poincaré group.

The infinitesimal statement should be distinguished from the finite one. The translation generators $P_\mu$ do belong to the Lie algebra of the Poincaré group, which is the semidirect sum
$$
\mathfrak{p}=\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}\ \ltimes\ \mathbb{R}^4,
\qquad [P_\mu,P_\nu]=0,
$$
with the Lorentz generators acting on $P_\mu$ through the vector representation and the boosts not closing among themselves. On fields, the finite translation is the Taylor operator $\exp(a^\mu\partial_\mu)$, and on a plane wave of four-wavevector $\tilde{K}\in\mathbb{M}_-$ it is multiplication by the central phase $\exp\!\bigl(i\,\mathrm{Sc}(\tilde{K}\tilde{a})\bigr)$ — a unit-modulus scalar in the algebra, not a biquaternion factor multiplying the field. With the series' plane-wave convention $\tilde{\Phi}=\tilde{\Phi}_0\exp\!\bigl(i\,\mathrm{Sc}(\tilde{K}\tilde{X})\bigr)$ and shift $\tilde{X}\mapsto\tilde{X}+\tilde{a}$, the multiplier is $e^{\,i\,\mathrm{Sc}(\tilde{K}\tilde{a})}$; the shift in the opposite direction gives its conjugate. The pairing is $\mathrm{Sc}(\tilde{K}\tilde{a})$, not $\mathrm{Sc}(\tilde{K}\bar{\tilde{a}})$: for $\tilde{K},\tilde{a}\in\mathbb{M}_-$ the latter equals $-(k_0a_0)+\mathbf{k}\cdot\mathbf{a}$, which is real, so the factor $\exp(\mathrm{Sc}(\tilde{K}\bar{\tilde{a}}))$ is a positive real number rather than a unit-modulus phase, and a translation multiplier must have unit modulus. So the translation is present in the infinitesimal algebra and acts finitely on field space, but it is not an element of the finite-dimensional rotor group.

## The Semidirect Structure

Write $N$ for the set of pure translations,
$$
N=\{(e_0,\tilde{a}):\tilde{a}\in\mathbb{M}_-\}\cong(\mathbb{M}_-,+)\cong\mathbb{R}^4 .
$$
$N$ is an abelian subgroup, and it is **normal**. To see the conjugation action, let $\tilde{b}\in\mathbb{M}_-$ and consider $g=(\tilde{\Lambda},\tilde{b})$. Using the law and the inverse,
$$
(\tilde{\Lambda},\tilde{b})\,(e_0,\tilde{a})\,(\tilde{\Lambda},\tilde{b})^{-1}
=\bigl(e_0,\ \tilde{\Lambda}\tilde{a}\tilde{\Lambda}^\dagger\bigr).
$$
The displacement slot returns to $e_0$: the residual translations $\tilde{b}$ cancel, and what survives is exactly the rotor conjugation of $\tilde{a}$. In other words, the homogeneous factor acts on the translation subgroup by the **vector representation** $\Pi$ on $\mathbb{M}_-$ — the same action that defines four-vectors. The semidirect product is therefore
$$
P_+^{\uparrow}\cong SL(2,\mathbb{C})\ltimes_{\Pi}\mathbb{R}^4,
$$
which is the double cover of the restricted Poincaré group $SO^+(1,3)\ltimes\mathbb{R}^4$. The whole structure is determined by data already present in $\mathbb{B}$: the group $SL(2,\mathbb{C})$ of unit-norm biquaternions, and the conjugation action $\Pi$ of that group on the subspace $\mathbb{M}_-$. The algebra does not need to be told what a translation is; it needs only to be told that there is one, in the form of an additive copy of $\mathbb{M}_-$.

The product is **not** direct. A translation and a homogeneous transformation fail to commute:
$$
(\tilde{\Lambda},0)\circ(e_0,\tilde{a})=(\tilde{\Lambda},\tilde{\Lambda}\tilde{a}\tilde{\Lambda}^\dagger),
\qquad
(e_0,\tilde{a})\circ(\tilde{\Lambda},0)=(\tilde{\Lambda},\tilde{a}),
$$
and these agree only when $\tilde{a}$ is fixed by $\Pi(\tilde{\Lambda})$. Equivalently, the commutator of a pure Lorentz transformation with a pure translation is the pure translation by $\Pi(\tilde{\Lambda})\tilde{a}-\tilde{a}$. For a boost and a displacement transverse to it this is nonzero whenever the displacement has a time component; for the boost $\tilde{B}$ along $e_1$ with rapidity $\psi=0.9$ used below, a displacement $\tilde{a}=0.4\,ie_0+0.25e_1-0.35e_2+0.15e_3$ gives $\Pi(\tilde{B})\tilde{a}-\tilde{a}=-0.0834\,ie_0-0.3023\,e_1$. The nonvanishing of this commutator is the group-theoretic content of the statement that translations are not merely added: a change of frame drags the origin with it.

## A Composition Checked Directly

The group law is verified here on a case chosen for the check, not on a case from which the law was read off. Take $c=1$ and the two transformations
$$
g_1=(\tilde{R},\tilde{a}_1),\qquad g_2=(\tilde{B},\tilde{a}_2),
$$
with
$$
\tilde{R}=\cos(0.4)+\sin(0.4)\,e_3,
\qquad
\tilde{B}=\cosh(0.45)+i\sinh(0.45)\,e_1,
$$
a rotation about $e_3$ by $\theta=0.8$ and a boost along $e_1$ by rapidity $\psi=0.9$, and with displacements
$$
\tilde{a}_1=0.5\,i\,e_0+0.7\,e_1,\qquad
\tilde{a}_2=-0.3\,i\,e_0+0.6\,e_2 .
$$
Thus $g_1$ is a rotation combined with a translation and $g_2$ is a boost combined with a translation in an independent spatial direction.

The composed law predicts the pair $g_2\circ g_1=(\tilde{B}\tilde{R},\ \tilde{B}\tilde{a}_1\tilde{B}^\dagger+\tilde{a}_2)$ with
$$
\tilde{B}\tilde{R}=1.0159+0.4286\,ie_1-0.1812\,ie_2+0.4295\,e_3,
$$
$$
\tilde{B}\tilde{a}_1\tilde{B}^\dagger+\tilde{a}_2=-0.3020\,ie_0+0.4899\,e_1+0.6000\,e_2 .
$$
Applying the two maps in turn to $\tilde{X}=0.2\,ie_0+0.3\,e_1+0.4\,e_2+0.5\,e_3$, and the composed map to the same point, gives identical results. Two features make the structure visible.

First, the boost acting on the displacement has changed both its time component and its spatial component: the pair $(0.5i,\,0.7,\,0,\,0)$ has become $(-0.0020i,\,0.4899,\,0,\,0)$. A shift of origin is itself a four-vector, and its components mix under a boost; this is the relativity of simultaneity appearing as a statement about the composition of frame transformations. The second displacement $\tilde{a}_2$ is simply added afterwards, as the law requires.

Second, the rotor of the composite is not symmetric in the two factors. Reversing the order gives $\tilde{R}\tilde{B}=1.0159+0.4286\,ie_1+0.1812\,ie_2+0.4295\,e_3$: the same angle, but the opposite sign on the $ie_2$ term. This is the Thomas–Wigner rotation of the parent article, entering here through the sign of one component of the composite rotor. The group law reproduces it without being told to.

## The Frame Reading

A biquaternion **frame** is the data of an orientation and a state of motion together with an origin: a rotor $\tilde{\Lambda}$ that carries the reference frame to the frame in question, and a displacement $\tilde{a}$ that carries the reference origin to its origin. A Poincaré transformation is a change of frame, and the pair $(\tilde{\Lambda},\tilde{a})$ is exactly that change. In this reading the two slots have distinct jobs: the rotor is a multiplicative object, an element of the group of unit-norm biquaternions, while the displacement is an additive object, an element of the vector space $\mathbb{M}_-$. The group law says that frame changes compose in the familiar way — orientations compose multiplicatively, origins transform as four-vectors and then add.

The rotor attached to a frame is not independent of its state of motion. For a frame whose four-velocity is $\tilde{U}=\gamma(ic\,e_0+\mathbf{v})$, the boost rotor that carries the rest frame to it is
$$
\tilde{\Lambda}=\sqrt{-\tfrac{i}{c}\bar{\tilde{U}}},
$$
the square root being multivalued by sign, with the branch selected by $\mathrm{Sc}(\tilde{\Lambda})>0$. This relation, established in *The Lorentz Transformation as a Biquaternionic Rotation*, populates the multiplicative slot from the material data; the additive slot is populated by the position of the origin. The limitation is felt here: the rotor is a biquaternion, the origin is not.

## What the Frame Captures, and What It Does Not

**Captured exactly.** The biquaternion algebra contains the connected, restricted Lorentz group: its unit-norm elements are $SL(2,\mathbb{C})$, its conjugation action on $\mathbb{M}_-$ is the vector representation, and the covering homomorphism onto $SO^+(1,3)$ is two-to-one with kernel $\{\pm e_0\}$. The material sector $\mathbb{M}_-$ carries the four-vectors, their interval, and the light cone as the zero-divisor set. Because the semidirect product is determined by $SL(2,\mathbb{C})$ together with the representation $\Pi$ on $\mathbb{M}_-$, the biquaternion frame determines the full restricted Poincaré group once the translation factor is supplied; in that precise sense the group is a property of the algebra even though its elements are pairs rather than rotors.

**Not captured as rotors.** The translation is additive. It is not a conjugation and not a product of rotors, and no faithful homomorphism of the Poincaré group into $\mathbb{B}^\times$ exists at all; the dimension count settles this. The discrete inversions are also outside the connected rotor group: the spatial inversion $t\mapsto t$, $\mathbf{x}\mapsto-\mathbf{x}$ is implemented on $\mathbb{M}_-$ by quaternion conjugation $\tilde{X}\mapsto\bar{\tilde{X}}$, which is an algebra **anti**-automorphism, not an inner automorphism, and it is this that places spatial inversion outside $SL(2,\mathbb{C})$. The cover of the Lorentz group is therefore a cover of its connected part, and an extension of the group by spatial inversion requires that anti-automorphism as well.

**Beyond the finite-dimensional frame.** The biquaternion algebra is finite-dimensional, and its representations are the finite-dimensional ones; the biquaternion algebra itself carries the four-vector representation $(\tfrac12,\tfrac12)$. The physically realized unitary representations of the Poincaré group — Wigner's classification by mass and spin — are infinite-dimensional, and the finite-dimensional frame does not contain them. The informational sector uses the same algebra, with states in $\mathbb{M}_+$ and expectation values $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, but that operator algebra is finite-dimensional too: it is the algebra of a single qubit, not of a field. The Poincaré action on the material sector and the Born rule of the informational sector are two uses of one algebra, and both stop at the finite-dimensional objects it contains.

## Translation as a Rotation: The Open Question

The remaining question is whether the translation can be made multiplicative after all, by changing the algebra or the reading. Several routes are visible, and none is decided here.

**The additive reading inside $\mathbb{B}$.** The plainest reading is the one used throughout: the displacement is an element of $\mathbb{M}_-$, translations are addition, and the algebra supplies not the translation but the action by which the homogeneous part drags it. This is complete and internally consistent. Its cost is that the Poincaré group then does not embed as a Lie subgroup of $\mathbb{B}^\times$, so none of the rotor machinery — composition by multiplication, the double cover, the trace and norm forms — applies to translations.

**A larger Clifford algebra.** The dual quaternions are the model for a different reading in the Euclidean case: adjoining a nilpotent element $\varepsilon$ with $\varepsilon^2=0$ to the quaternions makes translations multiplicative, and the Euclidean rigid motions become unit dual quaternions acting by a single product law. Whether a Lorentzian analogue exists, and what it costs, is not settled here. Any enlargement is forced: the restricted Poincaré group has ten real dimensions and the unit group of $\mathbb{B}$ has six, so the new algebra must be strictly larger. Candidate settings in the literature include Clifford algebras with additional nilpotent or null generators, and conformal extensions in which translations appear as parabolic products of generalized inversions rather than as pure rotors. What such a construction would do to the two-sector structure $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$, and whether the enlarged objects still deserve to be called biquaternions, are exactly the questions that are open.

**Translation in field space.** In quantum theory the finite translation is already multiplicative on a different space: on momentum-space fields it is multiplication by the central phase $\exp\!\bigl(i\,\mathrm{Sc}(\tilde{K}\tilde{a})\bigr)$, and its generator is a derivation, not an inner derivation of $\mathbb{B}$. This realization lives on an infinite-dimensional representation, outside the finite-dimensional frame treated here.

The honest summary is that the biquaternion frame answers the homogeneous question exactly and the translation question not at all: the biquaternions supply the first factor of the semidirect product and the action on the second, and whether the second can be absorbed into a biquaternion-like algebra, and which one, is open. No choice among the candidates is made here.

## Summary

The Poincaré group is the ten-parameter group of affine isometries of Minkowski space, and its restricted connected form is the semidirect product $SO^+(1,3)\ltimes\mathbb{R}^4$; its double cover is $SL(2,\mathbb{C})\ltimes\mathbb{R}^4$. The biquaternion algebra $\mathbb{B}$ contains the homogeneous factor exactly: the unit-norm biquaternions are $SL(2,\mathbb{C})$, rotor conjugation $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ is the action on the material sector $\mathbb{M}_-$, and $\Pi$ is the two-to-one covering map onto $SO^+(1,3)$.

Translation is not a rotation in this algebra. A rotor conjugation is linear and fixes the origin; a shift is affine and does not. Conjugation preserves the norm form pointwise while a shift preserves only the norm form of differences, which is why the interval survives translation; and no faithful assignment of rotors to Poincaré elements exists, because the group has ten real dimensions and the rotor group six.

The correct object is the pair $(\tilde{\Lambda},\tilde{a})$, with $\tilde{a}\in\mathbb{M}_-$, acting by $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger+\tilde{a}$, and composing by
$$
(\tilde{\Lambda}_2,\tilde{a}_2)\circ(\tilde{\Lambda}_1,\tilde{a}_1)
=\bigl(\tilde{\Lambda}_2\tilde{\Lambda}_1,\ \tilde{\Lambda}_2\tilde{a}_1\tilde{\Lambda}_2^\dagger+\tilde{a}_2\bigr).
$$
The pure translations form a normal abelian subgroup, and conjugation by a homogeneous transformation acts on it by the vector representation $\Pi$, so the group is the semidirect product $SL(2,\mathbb{C})\ltimes_{\Pi}\mathbb{R}^4$. The group law was verified on a rotation, a boost, and two translations chosen for the check; the composite translation mixed as a four-vector under the boost, and the composite rotor showed the Thomas–Wigner asymmetry on reversal of the order.

What the frame captures is the connected homogeneous group and its action; what it does not capture as a rotor is the translation. Whether an enlarged algebra can absorb the translation multiplicatively, as dual quaternions do in the Euclidean case, is stated as open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector), home of four-vectors and displacements |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector), home of boost rotors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, home of rotation rotors |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\tilde{\Lambda}\in SL(2,\mathbb{C})$ | Unit-norm biquaternion (Lorentz rotor) |
| $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation (four-vector action) |
| $\Pi:SL(2,\mathbb{C})\to SO^+(1,3)$ | Two-to-one covering homomorphism, kernel $\{\pm e_0\}$ |
| $\tilde{B}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost rotor (Hermitian, in $\mathbb{M}_+$) |
| $\tilde{R}=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\hat{\mathbf{n}}$ | Rotation rotor (unit real quaternion) |
| $\tilde{U}=\gamma(ic\,e_0+\mathbf{v})$, $\tilde{\Lambda}=\sqrt{-\frac{i}{c}\bar{\tilde{U}}}$ | Four-velocity and its frame rotor |
| $\tilde{a}\in\mathbb{M}_-$ | Translation (displacement) |
| $(\tilde{\Lambda},\tilde{a})$ | Poincaré transformation, acting by $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger+\tilde{a}$ |
| $(\tilde{\Lambda}_2,\tilde{a}_2)\circ(\tilde{\Lambda}_1,\tilde{a}_1)=(\tilde{\Lambda}_2\tilde{\Lambda}_1,\tilde{\Lambda}_2\tilde{a}_1\tilde{\Lambda}_2^\dagger+\tilde{a}_2)$ | Poincaré group law |
| $SL(2,\mathbb{C})\ltimes_{\Pi}\mathbb{R}^4$ | Semidirect structure of the (covering) restricted Poincaré group |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (informational sector) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- E. P. Wigner, "On Unitary Representations of the Inhomogeneous Lorentz Group," *Annals of Mathematics* **40** (1939) 149–204, for the Poincaré group and its unitary representations.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the Poincaré group, its Lie algebra, and the semidirect structure.
- Wu-Ki Tung, *Group Theory in Physics* (World Scientific, 1985), for the inhomogeneous Lorentz group and its representations.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for semidirect products of Lie groups and the dimension argument for homomorphisms.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor description of the Lorentz and Poincaré groups.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for rotors, the conformal extension, and translations as generators in a larger algebra.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of the Lorentz group and spacetime transformations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebraic framework and the double cover of the Lorentz group.
- Ben Kenwright, "A Beginner's Guide to Dual-Quaternions" (2012), for the Euclidean analogue in which translations become multiplicative.
