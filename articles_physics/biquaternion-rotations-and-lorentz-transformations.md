# __Biquaternion Rotations and Lorentz Transformations__

## Introduction

The biquaternion norm fixes what a motion is: the isometries of the form are the transformations that preserve $\langle\cdot\rangle_{\natural}$, and they are the rotations, the Lorentz transformations and the reflections. This article reads those motions, together with the double covers that carry them and the reflection formula the norm supplies.

The article is the Geometry slot of the Lie-theoretic block: the algebra is *The 12 Products of the Biquaternioid Complex Space*, the group and its exponential are *Biquaternion Lie Group and Exponential Structure*, and the topology of the group is *The Biquaternion Unit Group as a Topological Group*. The reflections and the Cartan–Dieudonné theorem are stated generally in *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* of Part II, and their biquaternion case is worked here; the Clifford interpretation of the algebra is *Biquaternion Other Algebraic Element Representations*; the transformation group in full is in *Biquaternion Automorphisms and Derivations*; and the finite groups of units, together with the figures they determine, are *Biquaternion Orders and Finite Groups of Units*.

The article also owns the **dagger sandwich** $\operatorname{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$, the action of an arbitrary unit of the algebra on the algebra regarded as an eight-dimensional real vector space. Its carrier, its kernel, its invariants, its action on the remarkable subspaces and the operators of a boost and of a rotation are read below. The inner automorphism $\tilde T\mapsto\tilde{Q}\tilde T\tilde{Q}^{-1}$ and its contrast with the sandwich are in *Biquaternion Automorphisms and Derivations*, the matrix congruence in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and the four factors of a single element in *The Polar Element Representation of Biquaternions*.

Physically the sandwich $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$ is the Lorentz transformation of the material sector: the boost is the change of inertial frame and the rotor is the spatial rotation, so that a four-vector of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* is carried from one frame to another by a biquaternion multiplication. The doubling of the half-angle is the geometric origin of the spinor double cover: the same motion is realised twice in $\mathbb{B}^{\times}_1$, once as $\tilde{U}$ and once as $-\tilde{U}$, which is why the carrier of the state in the Biquaternion Quantum Fields category is a spinor and not a vector.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written $\tilde{Q}=Q_te_t+\vec Q$ with $\vec Q=\sum_{k=1}^3 Q_k \vec e_k$. The products are $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^2=-e_t$. The quaternion conjugation is $\tilde{Q}^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$, the coefficient conjugation $\bar{\tilde{Q}}$ conjugates the four coefficients, and the Hermitian conjugation is their composite, $\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}$; the fixed space of ${}^{*}$ is the Hermitian sector $\mathbb{M}_+$ and its anti-fixed space the anti-Hermitian sector $\mathbb{M}_-$. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural}=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$, of polar form $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu P_\mu Q_\mu$, and $\tilde{Q}$ is a unit exactly when $\langle\tilde{Q}\rangle_{\natural}\neq0$ (*The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone*). The elements with four real coefficients form the **quaternion layer** $\mathbb{H}_{\mathbb{B}}=\{Q_te_t+\vec Q:Q_t,Q_x,Q_y,Q_z\in\mathbb{R}\}$, a copy of the quaternion algebra $\mathbb{H}$ inside $\mathbb{B}$; its unit sphere is the set of **unit quaternions**, $Sp(1)=\{\tilde u_{\mathrm r}\in\mathbb{H}_{\mathbb{B}}:\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{\natural}=e_t\}$, whose elements this article calls **rotors**, and the norm-one group of the algebra is $\mathbb{B}^\times_1=\{\tilde{Q}:\langle\tilde{Q}\rangle_{\natural}=e_t\}$. The pure elements, those with no scalar part, form the vector subspace $\mathrm{Vect}(\mathbb{B})=\{\tilde{Q}:Q_t=0\}$, and the unit pure quaternion, the axis of a rotor, is written $\vec u$. The four-position of a world line is $\tilde{Q}=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, with $c$ the speed of light and $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ its spatial part.

---

## The Double Covers and the Lorentz Group

The relevant subgroups are: $\mathbb{B}^\times$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $\mathbb{B}^\times_1$, the unit-norm elements (complex dimension $3$, real dimension $6$); the rotation group $Sp(1)$, the unit-norm real quaternions (real dimension $3$); and the centre $\mathbb{C}^\times e_t$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$Sp(1)$ is the maximal compact subgroup of $\mathbb{B}^\times_1$, with Lie algebra the compact rotation subalgebra $\mathrm{K}$ of *The 12 Products of the Biquaternioid Complex Space*. The centre $\{\pm e_t\}$ is discrete, and

$$
\mathbb{B}^\times_1/\{\pm e_t\} \cong SO^+(1,3),
$$

the proper orthochronous Lorentz group, of real dimension $6$. Hence $\mathbb{B}^\times_1$ is a two-sheeted cover of $SO^+(1,3)$ and, being simply connected, is its universal cover: it is the spin group of Lorentzian signature,

$$
\mathbb{B}^\times_1 \cong \mathrm{Spin}(1,3), \qquad \mathrm{B}_0 \cong \mathrm{so}(1,3).
$$

The Lorentz action is rotor conjugation, $\tilde{Q} \mapsto \tilde{U}\tilde{Q}\tilde{U}^{*}$ for $\tilde{U} \in \mathbb{B}^\times_1$, which preserves $\mathbb{M}_-$ and $\langle\tilde{Q}\rangle_{\natural}$; its compact part is the rotation family and its non-compact part the hyperbolic rotations, with closed forms in *Biquaternion Elementary Functions*, §*The Exponential in the Two Real Directions*.

## The Rotor and the Sandwich Action

A rotation is performed by conjugation, and the conjugating element is read as a **rotor**. A unit quaternion $\tilde u_{\mathrm r}$, an element of the unit sphere $Sp(1)$ of the quaternion layer, acts on a biquaternion by the sandwich
$$
\tilde{Q}\mapsto \tilde u_{\mathrm r}\,\tilde{Q}\,\tilde u_{\mathrm r}^{-1},
$$
and on the imaginary part this is the rotation of $\mathbb{R}^3$ through the angle $\theta$ when $\tilde u_{\mathrm r}=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r}$. Two features are visible in the formula. The angle appears **halved** in the rotor, since the rotation is applied once for the left factor and once for the right, and a full turn of the rotor, $\tilde u_{\mathrm r}\mapsto-\tilde u_{\mathrm r}$, is the identity rotation: the map $Sp(1)\to SO(3)$ is two-to-one, which is the double cover $SU(2)\to SO(3)$ of the double covers above. The unit quaternions carry the rotations of the definite form, and their complexification carries the motions of the indefinite one; the construction, with the versor and the sandwich action, is that of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* of Part II.

## The Dagger Sandwich

### Left Multiplication as the Reference

The simplest way to make an element act is to multiply by it, $\tilde T \mapsto \tilde{Q}\tilde T$. That map is the regular representation, it is faithful, and its matrix is the $4 \times 4$ regular matrix of *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. It is recorded here only as the reference column of the comparison table below, since it is an algebra endomorphism rather than an automorphism and it does not preserve the sector structure either.

### The Map on the Whole Algebra

For a unit $\tilde{Q}$, the **sandwich**, or **dagger sandwich**, is

$$
\operatorname{H}_{\tilde{Q}}(\tilde T) = \tilde{Q}\,\tilde T\,\tilde{Q}^{*} ,
$$

and for a rotor $\tilde{U}$ it is the **rotor conjugation** of the Lorentz group articles, which they write $\operatorname{H}_{\tilde{U}}$,

$$
\operatorname{H}_{\tilde{U}}(\tilde T) = \tilde{U}\,\tilde T\,\tilde{U}^{*} .
$$

Since $\tilde{U}^{*} = \overline{\tilde{U}^{\natural}}$, and the two involutions commute with the biquaternion norm in the way the following sections record, rotor conjugation is the map those articles write as the action of a rotor on a four-vector, now regarded as a map on the whole algebra. Off the rotor slice the sandwich multiplies the interval by the positive factor $|\langle\tilde{Q}\rangle_{\natural}|^2$ and is a similarity rather than an isometry; on the rotor slice it is the Lorentz action itself.

### The Comparison Table

| | left multiplication $\tilde{Q}\tilde T$ | the sandwich $\operatorname{H}_{\tilde{Q}}$ |
|---|---|---|
| type | algebra endomorphism | no, but an action of the group of units |
| image of $e_t$ | $\tilde{Q}$ | $\tilde{Q}\tilde{Q}^{*}$, in $\mathbb{M}_+$ |
| preserves the biquaternion norm | scales by $\langle\tilde{Q}\rangle_{\natural}$ | scales by $|\langle\tilde{Q}\rangle_{\natural}|^2$ |
| preserves the rank | yes | yes |
| kernel on the units | $\{e_t\}$ | the central circle $\mathrm{U}(1)e_t$ |
| kernel on the rotors | $\{e_t\}$ | $\{\pm e_t\}$ |
| preserves the two sectors | no | yes |
| preserves the product $\tilde T\tilde V$ | yes | only for unitary $\tilde{Q}$ |

Left multiplication is recorded for comparison only, as the regular representation of *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The last two lines are the content of this section: the sandwich is the Lorentz action, and it conserves the interval in place of the product.

## The Sandwich Is the Lorentz Action

### On the Material Sector

Rotor conjugation is the four-vector action of the series, and the identification is established in *The Lorentz Group as Biquaternion Norm Automorphisms* and *The Lorentz Group in Biquaternionic Form — Structure and Representations*; what is needed here are the three properties, each of which transfers a fact about the biquaternion norm to the operator language.

**Proposition.** For every rotor $\tilde{U}$, $\operatorname{H}_{\tilde{U}}$ maps $\mathbb{M}_-$ to itself, maps $\mathbb{M}_+$ to itself, and satisfies $N\big(\operatorname{H}_{\tilde{U}}(\tilde T)\big) = |\langle\tilde{U}\rangle_{\natural}|^2\langle\tilde T\rangle_{\natural} = \langle\tilde T,\tilde T\rangle_{\natural} = \langle\tilde T\rangle_{\natural}$.

**Proof.** For $\tilde T^{*} = \pm \tilde T$, the image satisfies $\left(\tilde{U}\tilde T\tilde{U}^{*}\right)^{*} = \tilde{U}\tilde T^{*}\tilde{U}^{*} = \pm\tilde{U}\tilde T\tilde{U}^{*}$, which gives both sector statements. For the biquaternion norm, multiplicativity gives $\langle\operatorname{H}_{\tilde{U}}\tilde T\rangle_{\natural} = \langle\tilde{U}\rangle_{\natural}\langle\tilde T\rangle_{\natural}\langle\tilde{U}^{*}\rangle_{\natural}$, and $\langle\tilde{U}^{*}\rangle_{\natural} = \overline{\langle\tilde{U}\rangle_{\natural}}$ because ${}^{*}$ is the composite of $\natural$, which fixes $\langle\cdot\rangle_{\natural}$, with $\bar{\cdot}$, which conjugates it; with $\langle\tilde{U}\rangle_{\natural} = 1$ the factor is one.

The proposition is the mathematical content of the statement that a rotor is a Lorentz transformation of the material sector, and of the Hermitian sector as well: the informational sector is carried to itself by the same action, which is the operator form of the statement that a Lorentz transformation acts on Hermitian forms exactly as it acts on four-vectors.

### The Biquaternion Norm as a Scaled Invariant

Off the unit-norm slice the action is not an isometry but a similarity: $\langle\cdot\rangle_{\natural}$ is multiplied by the positive real $|\langle\tilde{Q}\rangle_{\natural}|^2$. A general unit of $\mathbb{B}$ therefore acts on the two sectors by a transformation that preserves the causal type of every element and rescales the biquaternion norm by one fixed positive factor, and the dilations are the real line that the unit-norm condition removes. This is the reason the physics articles restrict to $\langle\tilde{U}\rangle_{\natural} = 1$ without loss: on that slice the dilation is the identity, and nothing else is lost except the central circle, which acts as the identity anyway.

### The Kernel on the Whole Algebra

On the four-dimensional material sector the kernel of the sandwich is $\{\pm e_t\}$, and that is the statement of the double cover. On the whole eight-dimensional algebra the kernel is larger, and the difference shows what the action on the whole algebra sees that the action on a single sector cannot.

**Theorem.** $\operatorname{H}_{\tilde{Q}} = \mathrm{id}$ on $\mathbb{B}$ if and only if $\tilde{Q} = \exp(i\theta)e_t$.

**Proof.** $\operatorname{H}_{\tilde{Q}}(\tilde T) = \tilde T$ for all $\tilde T$ forces $\tilde{Q}\tilde{Q}^{*} = e_t$ on taking $\tilde T = e_t$, so $\tilde{Q}$ is unitary, and forces $\tilde{Q}\tilde T = \tilde T\tilde{Q}$ for all $\tilde T$, so $\tilde{Q}$ is central; a central unitary is a complex number of modulus one. The converse is immediate.

The kernel of the action on the algebra is thus the central circle, of one real dimension, while the action on the material sector has the two-element kernel. Restricting the action to a sector can only shrink the kernel, and the two-element kernel of the Lorentz action is what remains of the circle after the sector is taken.

## What the Sandwich Does to the Remarkable Subspaces

### The Table

| subspace | $\operatorname{H}_{\tilde{Q}}$, general unit | $\operatorname{H}_{\tilde u_{\mathrm r}$, real unit quaternion |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | no | yes |
| $\mathrm{Vect}(\mathbb{B})$ (vector subspace) | no | yes |
| $\mathbb{H}_{\mathbb{B}}$ (quaternions) | no | yes |
| $i\mathbb{H}_{\mathbb{B}}$ (antiquaternions) | no | yes |
| $\mathbb{M}_+$ (informational) | yes | yes |
| $\mathbb{M}_-$ (material) | yes | yes |

### Why the Two Sectors Are the Invariant Subspaces

The sectors are the fixed spaces of ${}^{*}$ and $\flat$, and the sandwich is built out of ${}^{*}$, so it preserves them; the computation in the proof of the sector proposition is the whole reason. It preserves nothing else among the remarkable subspaces, because it is not an automorphism and has no reason to.

### Why the Centre and the Vector Subspace Are Not Preserved

They are the two pieces of the scalar–vector decomposition, and both are defined without reference to an involution: the centre is the set of elements commuting with everything, and the vector subspace is the traceless part, equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$. A map that respects composition respects both, and the sandwich does not respect composition. Applied to $e_t$ it returns $\tilde{Q}\tilde{Q}^{*}$, whose scalar part is a positive real and whose vector part is generally non-zero: the unit leaves the centre, and the centre is carried into the Hermitian sector.

### Why the Two Halves Need a Unitary Element

The two halves $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are the fixed spaces of the real structure $*$, so the sandwich preserves them exactly when it commutes with $*$, which is the condition that $\tilde{Q}\tilde{Q}^{*}$ be central. That happens exactly for the unitary elements, $\tilde{Q} = \exp(i\alpha)\tilde u_{\mathrm r}$, which are the four-dimensional family whose operators form the rotation group

$$
\left\{\operatorname{H}_{\tilde{Q}} : \tilde{Q} = \exp(i\alpha)\tilde u_{\mathrm r}\right\} \cong SU(2)/\{\pm e_t\} \cong SO(3) ,
$$

acting on the three-dimensional rotation space. For a unitary element the sandwich is multiplicative, hence an automorphism of the algebra, and it preserves all remarkable subspaces, as the table's second column records. **A boost does not preserve the two halves**, and that is the sharpest single way in which the two geometric generators differ.

### A Boost Carries the Centre into the Sectors

The failure is worth exhibiting, since the centre is where the algebra's own time axis lives. For the boost rotor of the next section, $\operatorname{H}_{\tilde{U}}(e_t) = \tilde{U}^2 = \cosh\psi\,e_t + i\sinh\psi\,\vec u_{\mathrm b}$, which is Hermitian of biquaternion norm one: the unit has been carried from the centre into the informational sector. It is the same computation as the statement that the sandwich moves the time axis, which the section on the product takes up.

## The Operator of a Boost

### The Boost Rotor

The corpus's pure boost along the unit real direction $\vec u_{\mathrm b}$, of rapidity $\psi$, is the rotor

$$
\tilde{U} = \exp\!\left(\frac{\psi}{2}i\vec u_{\mathrm b}\right) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b} ,
\qquad \tanh\psi = \frac{v_b}{c} ,
$$

which is Hermitian, of unit norm, and lies in the informational sector $\mathbb{M}_+$. The factor of $i$ in its vector part is what distinguishes it from a rotation rotor, for which the vector part is real.

### The Four-Position Goes to the Rest Frame

The action of the boost rotor on a four-position is the boost relation of the series. With $\tilde{Q} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ the four-position of a world line of velocity $\vec v$, and $\tilde{U}$ the boost rotor along $\vec u_v$ of rapidity $\psi$ with $\tanh\psi = |\vec v|/c$,

$$
\tilde{U}\,\tilde{Q}\,\tilde{U}^{*} = ic\tau\,e_t ,
\qquad \tau = t\sqrt{1 - \beta^2} ,
$$

the proper time, so the action carries the four-position from the lab frame to the rest frame. In components, and writing $\beta = |\vec v|/c$,

$$
ct' = ct\cosh\psi - z\sinh\psi , \qquad z' = z\cosh\psi - ct\sinh\psi ,
$$

for a boost along $\vec e_z$, which is the standard pair of formulas in the corpus's sign convention. The light cone is preserved by the action: a null four-vector is null in every frame, because $\langle\cdot\rangle_{\natural}$ is scaled by a positive factor and so vanishes if and only if it vanished.

## The Operator of a Rotation

### The Rotor and the Angle

A pure spatial rotation about the unit real direction $\vec u_{\mathrm r}$ through the angle $\theta$ is the rotor

$$
\tilde u_{\mathrm r} = \exp\!\left(\frac{\theta}{2}\vec u_{\mathrm r}\right) = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\vec u_{\mathrm r} ,
$$

a real unit quaternion lying in $\mathbb{H}_{\mathbb{B}}$. The rotation rotor is unitary, $\tilde u_{\mathrm r}^{*} = \tilde u_{\mathrm r}^{\natural} = \tilde u_{\mathrm r}^{-1}$, which is the property that makes the sandwich preserve the product of two elements of the algebra, as the section on the product shows. Its operator rotates the spatial part of a four-vector:

$$
\tilde u_{\mathrm r}\,\tilde{Q}\,\tilde u_{\mathrm r}^{*} = icte_t + (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\cos\theta + \left(\vec u_{\mathrm r}\times(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\right)\sin\theta + \vec u_{\mathrm r}\left(\vec u_{\mathrm r}\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\right)\left(1-\cos\theta\right),
$$

and it leaves the scalar part untouched. The angle in the operator is twice the half-angle in the element, which is the doubling that the spinor double cover rests on.

### Why the Rotation Doubles and the Boost Does Not

The two geometric rotors are the trigonometric exponential of a real unit direction and the hyperbolic exponential of an imaginary unit direction, and they behave differently under the sandwich, for a reason that is one line long. A rotation rotor is **unitary**, $\tilde u_{\mathrm r}^{*} = \tilde u_{\mathrm r}^{-1}$, and its sandwich gives the rotation of double the half-angle. A boost rotor is **Hermitian**, $\tilde{U}^{*} = \tilde{U}$, so its sandwich is $\tilde{U}\tilde T\tilde{U}$ — the element on both sides rather than an element and its inverse — and it gives the boost of rapidity $\psi$, not of $2\psi$. The difference is the same difference as the one between the orthogonal and the pseudo-orthogonal group: the doubling of the angle is a property of the compact factor, and the hyperbolic factor has no doubling because the element is already Hermitian.

The statement is confirmed by the numbers. For a rotation rotor with $\theta = \pi/3$, the action on $\vec e_x$ about $\vec e_z$ gives $\frac12\vec e_x + \frac{\sqrt3}{2}\vec e_y$, which is the rotation through $\pi/3$; and for the boost rotor of the previous section, the action on the four-position gives $ct' = ct\sqrt{1-\beta^2}$ with $\beta = 0.6$, that is, $0.8$, the boost of the element's own rapidity and not of twice it.

### Both Vector Halves Rotate Together

Because the scalar imaginary $i$ is central, $\operatorname{H}_{\tilde u_{\mathrm r}(i\vec w) = i\,\operatorname{H}_{\tilde u_{\mathrm r}(\vec w)$. The rotation therefore acts on the imaginary vector part $i\vec e_k$ and on the real vector part $\vec e_k$ by the same rotation of the same three-dimensional space, so the six-dimensional vector subspace is carried to itself by a single rotation acting complex-linearly. This is the operator statement of the fact that the quaternion rotation group acts on the complexified three-dimensional space, and it is why a rotation is an operator of the algebra rather than merely of the real slice.

## The Interval Is Preserved, the Product Is Not

### Multiplicativity Is the Fixed Time Axis

**Theorem.** For a unit $\tilde{Q}$, the sandwich preserves the product of two elements of the algebra,

$$
\operatorname{H}_{\tilde{Q}}(\tilde T\tilde V) = \operatorname{H}_{\tilde{Q}}(\tilde T)\,\operatorname{H}_{\tilde{Q}}(\tilde V) \qquad \text{for all } \tilde T, \tilde V ,
$$

if and only if $\tilde{Q}$ is unitary, $\tilde{Q}^{*}\tilde{Q} = e_t$; and that is the case exactly when the sandwich fixes the time axis, $\operatorname{H}_{\tilde{Q}}(ie_t) = ie_t$.

**Proof.** The two sides differ only in the middle factor, since $\operatorname{H}_{\tilde{Q}}(\tilde T)\operatorname{H}_{\tilde{Q}}(\tilde V) = \tilde{Q}\tilde T(\tilde{Q}^{*}\tilde{Q})\tilde V\tilde{Q}^{*}$ while $\operatorname{H}_{\tilde{Q}}(\tilde T\tilde V) = \tilde{Q}\tilde T\tilde V\tilde{Q}^{*}$, so equality for all $\tilde T,\tilde V$ is equivalent to $\tilde{Q}^{*}\tilde{Q} = e_t$. In that case $\operatorname{H}_{\tilde{Q}}(ie_t) = i\tilde{Q}\tilde{Q}^{*} = ie_t$, and conversely $\operatorname{H}_{\tilde{Q}}(ie_t) = i\tilde{Q}\tilde{Q}^{*}$ equals $ie_t$ only for $\tilde{Q}\tilde{Q}^{*} = e_t$, which is the same condition.

The unitary elements are exactly the central multiples of the real unit quaternions, $\tilde{Q} = \exp(i\alpha)\tilde u_{\mathrm r}$, and for those the sandwich is the rotation of the previous section. **A rotation therefore preserves the product and the interval; a boost preserves the interval and no longer the product.**

### The Numbers

For the boost rotor $\tilde{U} = \cosh\frac{\psi}{2}e_t + i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ the failure is measurable and computable. Along $\vec u_{\mathrm b} = \vec u_z$,

$$
\operatorname{H}_{\tilde{U}}(ie_t) = i\cosh\psi\,e_t - \sinh\psi\,\vec u_{\mathrm b} ,
\qquad
\operatorname{H}_{\tilde{U}}(\Delta z\,\vec u_{\mathrm b}) = -i\Delta z\sinh\psi\,e_t + \Delta z\cosh\psi\,\vec u_{\mathrm b} ,
$$

with the same coefficient $\sinh\psi = \gamma\beta$ in the two lines: $\gamma\beta$ is at once the spatial part acquired by the time axis and the time part acquired by a spatial step, which in the four-vector language is the simultaneity shift $\Delta t = -\gamma v\Delta z/c^2$. The failure of the product has the same coefficient, since

$$
\operatorname{H}_{\tilde{U}}(\tilde T\tilde V) - \operatorname{H}_{\tilde{U}}(\tilde T)\operatorname{H}_{\tilde{U}}(\tilde V) = \tilde{U}\tilde T\left(e_t - \tilde{U}^2\right)\tilde V\tilde{U} ,
\qquad
e_t - \tilde{U}^2 = (1-\cosh\psi)e_t - i\sinh\psi\,\vec u_{\mathrm b} ,
$$

so the defect is first order in the rapidity, exactly as the simultaneity shift is, while the time dilation $\gamma - 1$ is second order. For a boost of $\beta = 0.6$, where $\gamma = 1.25$ and $\sinh\psi = \gamma\beta = 0.75$: the time axis acquires the spatial part $-0.75$, a step of unit length along the direction of motion acquires the time part $-0.75$, and the defect of the product is of the same size. All three vanish together, at $\beta = 0$.

### Why This Is the Relativity of Time

The dagger sandwich preserves the product of two elements exactly when the acting element is unitary, which is exactly when it fixes the time axis. As soon as the time axis moves — that is, as soon as there is a boost — the sandwich preserves the interval but not the product. In that sense the relativity of time is built into the difference between the two structures that a sandwich can respect: the product holds only in the frame where the time axis is fixed.

Read on the algebra, the statement is that the unit $e_t$ and its scalar imaginary $ie_t$ are not frame-independent objects: they carry the rest frame with them. A rotation leaves both alone, and with them the product of the algebra; a boost carries $ie_t$ to the four-velocity of the moving frame, and no map that does that can respect the multiplication. The interval $\langle\cdot\rangle_{\natural}$ is the objective object, and it is exactly what survives.

## Orbits and the Mass Shell

### The Two Invariants

The sandwich preserves the rank of the matrix image always, and it preserves the biquaternion norm itself on the rotor slice; on the material sector it preserves the sign and the vanishing of the biquaternion norm of a four-vector, which is what the causal classification needs. These two invariants cut the elements into the classes the physics articles use.

| class | biquaternion norm $\langle\tilde{Q}\rangle_{\natural}$ | physical interpretation |
|---|---|---|
| timelike | $N < 0$, in the corpus's sign convention for $ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | a world line of a massive particle |
| null | $N = 0$, $\tilde{Q}\neq 0$ | a point of the light cone, a zero divisor of rank one |
| spacelike | $N > 0$ | a separation outside the cone |
| zero | $\tilde{Q} = 0$ | the origin |

### The Mass Shell and the Light Cone as Single Orbits

Two of the classes are single orbits of the Lorentz action, and the statement is the operator form of a familiar one. The non-zero null elements of $\mathbb{M}_-$ are all conjugate under rotor conjugation, which is the statement that the light cone is one geometric object and not a union of cones attached to individual points; and the timelike elements of a fixed biquaternion norm are all conjugate, which is the mass shell statement that every four-velocity of a given mass is carried to every other by a Lorentz transformation. A general rotor of $SL(2,\mathbb{C})$ acting on the rest four-velocity $i\,mc\,e_t$ gives

$$
\tilde{U}\,(imc\,e_t)\,\tilde{U}^{*} ,
$$

of biquaternion norm $N = -m^2c^2$, which is the four-velocity of a massive particle of mass $m$: the orbit of the rest four-velocity is the mass shell. The invariance of $\langle\cdot\rangle_{\natural}$ under the action is exactly the on-shell condition, and the reason the mass shell is a single orbit rather than a family of orbits parametrised by direction is that the rotors act transitively on the timelike elements of a fixed biquaternion norm.

### The Rank and the Zero Divisors

The rank-one stratum of the algebra is the set of non-zero elements with $N = 0$, and the corpus calls it the biquaternion null cone; the material-sector part of it is the light cone. Both actions preserve the rank, so no operator can move an element off the cone into an element that is not a zero divisor, and the whole cone is a single orbit of the Lorentz action. The identification of the light cone with the zero-divisor cone, and the use of that identification in the causal structure of the framework, are the subject of *The Light Cone as the Biquaternion Zero-Divisor Cone*.

## Ordering and the Wigner Rotor

### Composition of Operators

**Proposition.** $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde u_{\mathrm r}} = \operatorname{H}_{\tilde{Q}\tilde u_{\mathrm r}}$.

**Proof.** $\tilde{Q}(\tilde u_{\mathrm r}\tilde T\tilde u_{\mathrm r}^{*})\tilde{Q}^{*} = (\tilde{Q}\tilde u_{\mathrm r})\tilde T(\tilde{Q}\tilde u_{\mathrm r})^{*}$.

The physical consequence is that the operators compose as the elements do, so an operator can be decomposed by decomposing its element. In particular the product of two boosts is a rotor, and the polar representation of that product has a rotor factor: **the Wigner rotation**.

### Two Orthogonal Boosts

Take the two pure boosts

$$
\tilde{U}_1 = \exp\!\left(\frac{0.7}{2}i\vec e_x\right) , \qquad \tilde{U}_2 = \exp\!\left(\frac{0.9}{2}i\vec e_y\right) ,
$$

of rapidities $0.7$ along $\vec e_x$ and $0.9$ along $\vec e_y$. Their product $\tilde{U}_1\tilde{U}_2$ is a rotor, and its polar representation $\tilde{U}_1\tilde{U}_2 = B\tilde u_{\mathrm r}$ has

$$
\tilde u_{\mathrm r} = \cos\frac{\theta_W}{2} - \sin\frac{\theta_W}{2}\vec e_z , \qquad \theta_W = 0.281950221701 \ \text{rad} ,
$$

a rotation about $-\vec e_z$; the reversed order gives the same angle with the axis $+\vec e_z$. The angle is not a free parameter, and it is fixed in closed form by the two rapidities:

$$
\cos\theta_W = \frac{\cosh 0.7 + \cosh 0.9}{1 + \cosh 0.7\cosh 0.9} = 0.960514656248 , \qquad \theta_W = 0.281950221701 ,
$$

which agrees with the polar decomposition of the product to twelve digits. The operator statement is that the composite of two boost operators is a boost operator followed by a rotation operator, and that the rotation is not optional: two successive non-collinear boosts are not a boost.

### Thomas Precession

The Wigner rotor is the kinematic content of Thomas precession, and the operator interpretation makes the bookkeeping automatic: composing the two boosts and reading off the rotor factor is the whole computation, and the rotor factor acts on the spinor by left multiplication with the half-angle. The precession rate of a spinning particle in a circular orbit, the factor of one half that distinguishes the Thomas value from the naive one, and the comparison with the Bargmann–Michel–Telegdi equation are the subject of *Thomas Precession as a Biquaternion Rotor Effect* and *Exercise: The Thomas Precession*, and the closed form of the Wigner angle above is the element they use.

## The Operator and the Polar Representation

The two subjects meet in the kernel statement of the section on the Lorentz action, and the meeting is a dictionary.

| polar datum of $\tilde{Q} = r\exp(i\alpha)B\tilde u_{\mathrm r}$ | the sandwich $\operatorname{H}_{\tilde{Q}}$ |
|---|---|
| scale $r$ | the dilation $|\langle\tilde{Q}\rangle_{\natural}|^2 = r^4$ of the interval |
| phase $\exp(i\alpha)$ | not seen |
| boost $B$ | the boost factor of the action |
| rotor $\tilde u_{\mathrm r}$ | the rotation factor of the action |

The operator sees the boost and the rotor of the element, in that order, and it sees the scale only as the single dilation $r^4$ of the interval; the phase it does not see at all, which is the kernel statement above. Stated in the language of the polar articles: the polar representation exhibits four factors because one element carries them, and the operator carries the same four with the phase lost and the scale collapsed into the dilation of the interval. The two interpretations are companions, and each is the other's explanation of a factor count.

## Reflections

The sandwich also realises the **reflections**, on the subspaces where the multiplication is Clifford. Let $v\in\mathbb{B}$ with $\langle v\rangle_{\natural}=1$; the reflection in the hyperplane $v^{\perp}$ is the linear map
$$
\rho_v(\tilde T)=-v\,\tilde T\,v^{-1}=-v\,\tilde T\,v^{\natural},
$$
the second equality using $v^{-1}=v^{\natural}/\langle v\rangle_{\natural}=v^{\natural}$ for a norm-one element.

**Theorem.** For $v$ with $\langle v\rangle_{\natural}=1$ the map $\rho_v$ preserves the biquaternion norm and its polar form, satisfies $\rho_v(v)=-v$, and fixes pointwise every element that anticommutes with $v$; its square is the conjugation $\rho_v^2(\tilde T)=v^2\tilde Tv^{-2}$.

**Proof.** Since $v$ is invertible, $\rho_v$ is a linear automorphism, and $\langle\rho_v(\tilde T)\rangle_{\natural}=\langle v\rangle_{\natural}\langle\tilde T\rangle_{\natural}\langle v\rangle_{\natural}^{-1}=\langle\tilde T\rangle_{\natural}$ by multiplicativity of the norm, whence the polar form is preserved too; the statement $\rho_v(v)=-vvv^{-1}=-v$ is immediate. If $\tilde T$ anticommutes with $v$, then $-v\tilde Tv^{-1}=\tilde Tv\,v^{-1}=\tilde T$, so $\tilde T$ is fixed. The square is $\rho_v(\rho_v(\tilde T))=v(v\tilde Tv^{-1})v^{-1}=v^2\tilde Tv^{-2}$, a conjugation by $v^2$, and it is the identity exactly when $v^2$ is a scalar.

**Remark (which subspaces carry the reflections).** For the formula to be a genuine reflection, orthogonality and anticommutation must coincide on the ambient subspace. This happens when the multiplication is Clifford there: on the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{\vec e_x,\vec e_y,\vec e_z\}$ and its real form $\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ one has
$$
v\tilde T+\tilde Tv=-2\langle v,\tilde T\rangle\,e_t,
$$
so the hyperplane $v^{\perp}$ is exactly the set of elements anticommuting with $v$, and $\rho_v$ fixes $v^{\perp}$ pointwise, negates $v$, and has complex-linear determinant $-1$. Here $v^2=-\bigl(\sum_k v_k^2\bigr)e_t$ is a scalar, so $\rho_v$ is an involution. On the quaternion and Hermitian subspaces the elements do not anticommute, and a norm-one element acts there by conjugation as a rotation rather than as a reflection. On the algebra as a whole, likewise, $\rho_v$ has determinant $+1$ for every $v$ with $\langle v\rangle_{\natural}=1$, so the maps attached to the finite groups of units are rotations and not reflections; and on $\mathbb{H}_{\mathbb{B}}$ the norm-one element $e_t$ is central, so $\rho_{e_t}=-\mathrm{id}$ and nothing is fixed.

**Theorem (Cartan–Dieudonné in the biquaternion algebra).** On the complex three-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$ and on its real form $\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, every isometry is a product of at most three reflections $\rho_v$ with $\langle v\rangle_{\natural}=1$.

**Proof.** On these subspaces $\langle v\rangle_{\natural}=v_1^2+v_2^2+v_3^2$ is a non-degenerate form, and by the theorem above the maps $\rho_v$ with $\langle v\rangle_{\natural}=1$ are its reflections in the hyperplanes $v^{\perp}$; the Cartan–Dieudonné theorem, stated for a general vector space in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, then gives generation by at most $\dim W=3$ reflections.

**Remark.** The reflections of this section are attached to the odd part $\mathrm{Vect}(\mathbb{B})$; the Lorentz reflections are not of the shape $\rho_v$ and live in the Clifford layer, not in $\mathbb{B}$.

## Rotations, Boosts and the Two-Sided Action

Over the reals the trace-free subalgebra splits into the compact rotation directions $\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and the hyperbolic directions $\mathrm{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ (*The 12 Products of the Biquaternioid Complex Space*). A **rotation** is the motion generated by the first, an element of the compact group $Sp(1)$ of the rotation family; a **boost**, or hyperbolic rotation, is the motion generated by the second, an isometry of the indefinite form that fixes a timelike direction and leaves the light cone invariant. Both are boosts or rotations of the form the algebra carries, and together they generate the Lorentz group $SO^+(1,3)$ of the double covers above; the rotations are the isometries of the definite form, the boosts those of the indefinite one, and the closed forms of their exponentials are in *Biquaternion Elementary Functions*.

A **two-sided** action, $\tilde{Q}\mapsto \tilde u_{\mathrm r}\,\tilde{Q}\,\tilde v$ with $\tilde u_{\mathrm r},\tilde v\in Sp(1)$ independent, is a four-dimensional rotation: the pair $(\tilde u_{\mathrm r},\tilde v)$ acts on $\mathbb{B}\cong\mathbb{R}^8$ preserving the Euclidean form, with kernel $\{\pm(e_t,e_t)\}$, so the two-sided action realises
$$
(Sp(1)\times Sp(1))/\{\pm e_t\}\cong SO(4)
$$
on the algebra. The one-sided action is its diagonal restriction, and the Lorentzian motions are obtained from the complexification instead.
**Physical interpretation: the motions of the framework.** The isometries of the norm are the physical motions: $Sp(1)$ supplies the spatial rotations of the material sector, and $\mathbb{B}^{\times}_1\cong Spin(1,3)$ supplies the Lorentz transformations, the boosts being the hyperbolic directions of the trace-free subalgebra. The two-sided action is the Euclidean interpretation the informational sector $\mathbb{M}_+$ carries, and its diagonal restriction is the Lorentzian one. Because the rotor acts by conjugation the angle is halved and the map to $SO^+(1,3)$ is two-to-one: the double cover is not an accident of the parametrisation but the statement that a $2\pi$ rotation returns a vector and reverses a spinor, the fact behind the spin-$\tfrac{1}{2}$ behaviour of the Biquaternion Non Relativistic Quantum Theory category.

## Worked Examples

### A Boost Rotor Acting on a Four-Position

Let $\beta = 0.6$ along $\vec e_z$, so that $\psi = \operatorname{artanh}0.6$, $\cosh\frac{\psi}{2} = 1.060660172$ and $\sinh\frac{\psi}{2} = 0.353553391$, and let $\tilde{Q} = ict\,e_t + 0.6ct\,\vec e_z$ with $ct = 1$. Then

$$
\tilde{U}\,\tilde{Q}\,\tilde{U}^{*} = i\tau e_t , \qquad \tau = \sqrt{1-0.36} = 0.8 ,
$$

so that $ct' = 0.8$ and $z' = 2.8\times10^{-17}$, the residual of a zero. The example is the corpus's own numerical check of the boost rotor, and it exhibits the action as the statement that the four-position of a moving particle is carried to its rest frame.

### A Rotation Rotor Acting on a Four-Vector

Let $\tilde u_{\mathrm r} = \cos\frac{\pi}{6} + \sin\frac{\pi}{6}\vec e_z$, of angle $\theta = \pi/3$, and let $\tilde{Q} = 2ie_t + \vec e_x + 0.5\vec e_z$. Then

$$
\tilde u_{\mathrm r}\,\tilde{Q}\,\tilde u_{\mathrm r}^{*} = 2ie_t + 0.5\vec e_x + 0.866025404\vec e_y + 0.5\vec e_z ,
$$

so the temporal and $\vec e_z$ components are untouched and the spatial part is rotated through $\pi/3$ in the $(\vec e_x,\vec e_y)$ plane: the values are $\cos\frac{\pi}{3} = 0.5$ and $\sin\frac{\pi}{3} = 0.866025404$. The biquaternion norm is unchanged, $N = -4 + 1 + 0.25 = -2.75$ before and after.

### A Boost Rotor Acting on a Null Four-Vector

With $\tilde{U} = \frac53e_t + \frac43i\vec e_z$, of biquaternion norm $N = \frac{25}{9} - \frac{16}{9} = 1$ and hence of rapidity $\psi = 2\ln 3$, for which $\beta = \tanh\psi = \frac{40}{41}$, and with the null four-vector $\tilde{Q} = ie_t + \vec e_x$, the sandwich gives

$$
\operatorname{H}_{\tilde{U}}(\tilde{Q}) = \frac{41}{9}ie_t + \vec e_x - \frac{40}{9}\vec e_z ,
\qquad
\frac{41}{9} = \cosh\psi , \quad \frac{40}{9} = \sinh\psi .
$$

The image is anti-Hermitian, so it is again a four-vector, as the sector proposition requires; its biquaternion norm is $-\frac{1681}{81} + 1 + \frac{1600}{81} = 0$, so the null vector is still null, as the invariance of the cone requires; and the spatial direction $\vec e_x$, transverse to the boost, is untouched. The numerical values are $\frac{41}{9} = 4.5555\ldots$ and $\frac{40}{9} = 4.4444\ldots$. The example is the boost of the corpus's normalisation with $\beta = \frac{40}{41}$, applied to a lightlike four-vector.

### The Wigner Angle

For the two boosts of rapidities $0.7$ and $0.9$ about orthogonal axes, the polar decomposition of the product gives a rotor of angle $0.281950221701$ rad, and

$$
\cos\theta_W = \frac{\cosh 0.7 + \cosh 0.9}{1+\cosh0.7\cosh0.9} = \frac{1.255169006 + 1.433086385}{1 + 1.798800804} = 0.960514656 ,
$$

which gives the same angle. The angle vanishes when either rapidity vanishes and when the two axes are collinear, both of which are immediate from the closed form, and it is largest for two boosts of comparable rapidity about orthogonal axes.

### The Double Cover

Let $\tilde u_{\mathrm r}$ be any rotation rotor and consider $-\tilde u_{\mathrm r}$. Since $-\tilde u_{\mathrm r}$ is a central multiple of $\tilde u_{\mathrm r}$, and a central multiple scales the sandwich by the squared modulus of its complex factor, $\operatorname{H}_{-\tilde u_{\mathrm r}} = \operatorname{H}_{\tilde u_{\mathrm r}}$, while $-\tilde u_{\mathrm r}\neq\tilde u_{\mathrm r}$ as algebra elements. The two rotors therefore represent the same operator and are not the same physical element, which is the statement that the rotation group has a two-fold cover by the rotors. On the material sector the same computation is the standard double cover of the Lorentz group, and the kernel statement for the whole algebra is its refinement.

## Physical Readings

The double covers read as the two frame groups of the framework: $SU(2)\to SO(3)$ is the material rotation and $\mathrm{SL}(2,\mathbb{C})\to SO^+(1,3)$ is the full change of frame, and the rotor is the acting element of a change of frame. Read on the clock, a rotation preserves the central phase and the norm, so a frame change moves the material ledger and leaves the temporal phase and the probability form where they were; read on the split, the rotors that preserve each sector are the superselection-preserving operations (*The Material-Informational Split as a Superselection Structure in Biquaternionic Form*).

Two further readings of the boost operator follow. Its **spectrum** is read as the Doppler/redshift factors: the boost rotor stores the half-rapidity and its eigenvalues are the red- and blue-shift factors of the frame change, and the **doubling** of the eigenvalue pair is read as the two-way light travel, the two null directions the boost slides along. The interpretation is the operator form of the Doppler factor of *The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation* and *Exercise: The Relativistic Doppler Effect*.

Read on the period, one algebra carries two periods: the central rotation is of order four, while a rotor through $2\pi$ about any axis is $-e_t$, so the phase of the centre repeats after $2\pi$ and the spinor after $4\pi$. Read physically, the double cover is the statement that the phase and the spinor are two interpretations of one rotation with two periods, the half-integer spins living where $-e_t$ acts as $-\mathrm{id}$ and the integer spins where it acts as $+\mathrm{id}$ (*The Spinor Module in Biquaternionic Form and Its Lorentz Action*, *The Spin–Statistics Theorem in Biquaternionic Form*). Boundary: the double cover is proved above; the interpretation juxtaposes the two periods and adds no group.

**A change of frame is a conjugation, and that is what makes a symmetry a change of description.** Every motion of the framework is a two-sided action, $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$: the acting element meets the element on both sides at once. Read physically, the two-sidedness is the relational character of the framework's symmetries — a one-sided multiplication carries the element, while a sandwich carries the frame the element is described in, so a change of frame relabels the description and leaves the invariants where they were. When the two sides are inverse to each other the sandwich is the **inner automorphism** $\tilde{Q}\mapsto\tilde{g}\tilde{Q}\tilde{g}^{-1}$, and by Skolem–Noether every $\mathbb{C}$-linear algebra automorphism of $\mathbb{B}$ is of that form (*Biquaternion Automorphisms and Derivations*, *The Lorentz Group as Biquaternion Norm Automorphisms*). Every inner automorphism fixes the centre pointwise, so the algebra's symmetries of the description are exactly its conjugations, and the central phase is the invariant that no change of description can move.

**A rotation is a conjugation and a boost is not.** The dagger sandwich and the inner automorphism coincide exactly when the rotor is real, $\tilde u_{\mathrm r}^{-1}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{*}$, which holds for the rotations and fails for the boosts, where $\tilde{B}^{-1}=\tilde{B}^{\natural}\neq\tilde{B}^{*}=\tilde{B}$ (*The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone*). Read physically, a rotation is at once a motion and an algebra symmetry, whereas a boost is a motion that is not one: the boost preserves the norm and the central phase and does not preserve the product. That is the algebraic form of the statement that a change of velocity changes the description and not the object.

**Boundary.** The interpretation is a statement about the units. The measurement update is two-sided too, $\tilde{Ϛ}\mapsto\tilde{P}\tilde{Ϛ}\tilde{P}/\mathrm{Tr}(\tilde{P}\tilde{Ϛ}\tilde{P})$, but $\tilde{P}$ is an idempotent with $\langle\tilde{P}\rangle_{\natural}=0$ and no inverse, so it is not a symmetry and is not an instance of this interpretation; it is a filter, and it is owned by *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*. Over $\mathbb{R}$ the automorphisms also include the coefficient conjugation $\bar{\cdot}$, which is $\mathbb{C}$-antilinear and not inner, so the identification of a symmetry with a conjugation is a statement about the $\mathbb{C}$-linear automorphisms.

## Summary

The motions of the biquaternion algebra are the isometries of its biquaternion norm, and they are the rotations and the Lorentz transformations. The unit quaternions $Sp(1)$ carry the rotations of the definite form by the sandwich $\tilde{Q}\mapsto \tilde u_{\mathrm r}\tilde{Q}\tilde u_{\mathrm r}^{-1}$, in which the angle is halved and $\pm\tilde u_{\mathrm r}$ gives the same rotation: the map $Sp(1)\to SO(3)$ is the double cover $SU(2)\to SO(3)$. Complexifying, the norm-one group $\mathbb{B}^\times_1$ carries the rotations of the indefinite form, and $\mathbb{B}^\times_1/\{\pm e_t\}\cong SO^+(1,3)$ with $\mathbb{B}^\times_1\cong Spin(1,3)$, so that the double cover of the proper orthochronous Lorentz group is realised inside the algebra; the trace-free subalgebra splits into the compact rotation directions and the hyperbolic directions, and it is the boosts generated by the latter that are the isometries of the indefinite form.

The action of an arbitrary unit on the whole algebra is the **dagger sandwich** $\operatorname{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$, and on the norm-one slice it is the Lorentz action written above. It is the only two-sided sandwich $\tilde T\mapsto A\tilde TB$ that carries the Hermitian sectors into themselves; it preserves $\mathbb{M}_+$ and $\mathbb{M}_-$ and no other of the remarkable subspaces; it scales the biquaternion norm by $|\langle\tilde{Q}\rangle_{\natural}|^2$ and preserves it on the rotor slice; and its kernel is the central circle $\mathrm{U}(1)e_t$, which reduces to $\{\pm e_t\}$ on the slice and is the double cover. It is multiplicative exactly for the unitary elements, which are exactly those that fix the time axis; a boost therefore preserves the interval and not the product, and that single fact is the algebra's form of the relativity of simultaneity. The operators compose as their elements do, so two non-collinear boosts compose to a boost followed by the rotation the series calls the Wigner rotation.

The two-sided action $\tilde{Q}\mapsto \tilde u_{\mathrm r}\tilde{Q}\tilde v$ with independent unit quaternions preserves the Euclidean form and gives $(Sp(1)\times Sp(1))/\{\pm e_t\}\cong SO(4)$; the one-sided action is its diagonal restriction. The reflections are the maps $\rho_v(\tilde T)=-v\tilde Tv^{-1}=-v\tilde Tv^{\natural}$ with $\langle v\rangle_{\natural}=1$, defined on the Clifford vector subspace $\mathrm{Vect}(\mathbb{B})$ and its real form, where orthogonality and anticommutation coincide; on that subspace every isometry is a product of at most three of them, by Cartan–Dieudonné. The construction is that of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* of Part II, and the full symmetry group of the algebra, wider than its isometries, is in *Biquaternion Automorphisms and Derivations*. Physically these motions are the changes of reference frame and the rotations of the framework: the boost is the change of inertial frame, the rotor the spatial rotation, the two-sided action the Euclidean interpretation of the informational sector, and the halving of the angle the geometric origin of the spinor double cover.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde{Q}\rangle_{\natural}$ | Biquaternion norm; the invariant of the motions |
| $Sp(1)$ | Unit quaternions; rotors of the definite form |
| $\tilde u_{\mathrm r}\tilde{Q}\tilde u_{\mathrm r}^{-1}$ | Sandwich action; rotor conjugation |
| $\rho_v(\tilde T)=-v\tilde Tv^{-1}=-v\tilde Tv^{\natural}$ | Reflection in $v^{\perp}$ on $\mathrm{Vect}(\mathbb{B})$, $\langle v\rangle_{\natural}=1$ |
| $v\tilde T+\tilde Tv=-2\langle v,\tilde T\rangle e_t$ | Anticommutation as orthogonality on $\mathrm{Vect}(\mathbb{B})$; then $v^{\perp}=\{\tilde T:\tilde Tv=-v\tilde T\}$ |
| Cartan–Dieudonné | Every isometry of $\mathrm{Vect}(\mathbb{B})$ is at most three reflections $\rho_v$ |
| $Sp(1)\to SO(3)$ | Double cover $SU(2)\to SO(3)$; $\pm\tilde u_{\mathrm r}$ give the same rotation |
| $\mathbb{B}^\times_1\cong Spin(1,3)$ | Norm-one group as the spin group; double cover of $SO^+(1,3)$ |
| $\mathbb{B}^\times_1/\{\pm e_t\}\cong SO^+(1,3)$ | Proper orthochronous Lorentz group |
| $\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | Rotation directions; compact |
| $\mathrm{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ | Hyperbolic (boost) directions |
| $\tilde u_{\mathrm r}\tilde{Q}\tilde v$ | Two-sided action; preserves the Euclidean form |
| $(Sp(1)\times Sp(1))/\{\pm e_t\}\cong SO(4)$ | Two-sided action as four-dimensional rotations |
| $\operatorname{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$ | The dagger sandwich; the action of a unit on the whole algebra |
| $\operatorname{H}_{z\tilde{Q}}=\lvert z\rvert^2\operatorname{H}_{\tilde{Q}}$ | Central phase invisible; the modulus is the dilation |
| $\langle\operatorname{H}_{\tilde{Q}}(\tilde T)\rangle_{\natural}=\lvert \langle\tilde{Q}\rangle_{\natural}\rvert^2\langle\tilde T\rangle_{\natural}$ | Scaling of the biquaternion norm; an isometry on the rotor slice |
| $\mathrm{U}(1)=\{\exp(i\theta)e_t\}$ | Kernel of the sandwich; $\{\pm e_t\}$ on the norm-one slice |
| $\vec u_{\mathrm r},\theta$ | Axis and angle of a rotation rotor, $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ |
| $\vec u_{\mathrm b},\psi$ | Axis and rapidity of a boost rotor, $\tilde{U}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$, $\tanh\psi=v_b/c$ |
| $\tilde u_{\mathrm r}$ | The rotation rotor of the polar form, a unit real quaternion, the compact factor of $\tilde{Q}=r\exp(i\alpha)B\tilde u_{\mathrm r}$ |
| $\theta_W$ | The Wigner angle of two successive boosts |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\langle\tilde{Q}\rangle_{\natural}$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
