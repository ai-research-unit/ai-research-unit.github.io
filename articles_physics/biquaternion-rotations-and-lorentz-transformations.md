# __Biquaternion Rotations and Lorentz Transformations__

## Introduction

The biquaternion norm fixes what a motion is: the isometries of the form are the transformations that preserve $N$, and they are the rotations, the Lorentz transformations and the reflections. This article reads those motions, together with the double covers that carry them and the reflection formula the norm supplies.

The article is the Geometry slot of the Lie-theoretic block: the algebra is *Biquaternion Lie Algebra*, the group and its exponential are *Biquaternion Lie Group and Exponential Structure*, and the topology of the group is *The Biquaternion Unit Group as a Topological Group*. The reflections and the Cartan–Dieudonné theorem are stated generally in *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* of Part II, and their biquaternion case is worked here; the Clifford reading of the algebra is *The Clifford Structure of the Biquaternion Algebra*; the transformation group in full is in *Biquaternion Automorphisms and Derivations*; and the finite groups of units, together with the figures they determine, are *Biquaternion Orders and Finite Groups of Units*.

The article also owns the **dagger sandwich** $\operatorname{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$, the action of an arbitrary unit of the algebra on the algebra regarded as an eight-dimensional real vector space. Its carrier, its kernel, its invariants, its action on the six distinguished subspaces and the operators of a boost and of a rotation are read below. The inner automorphism $\tilde T\mapsto\tilde{Q}\tilde T\tilde{Q}^{-1}$ and its contrast with the sandwich are in *Biquaternion Automorphisms and Derivations*, the matrix congruence in *The 2×2 Matrix Element Representation of Biquaternions*, and the four factors of a single element in *The Polar Element Representation of Biquaternions*.

Physically the sandwich $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ is the Lorentz transformation of the material sector: the boost is the change of inertial frame and the rotor is the spatial rotation, so that a four-vector of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* is carried from one frame to another by a biquaternion multiplication. The doubling of the half-angle is the geometric origin of the spinor double cover: the same motion is realised twice in $\mathbb{B}^{\times}_1$, once as $\tilde{\Lambda}$ and once as $-\tilde{\Lambda}$, which is why the carrier of the state of *Biquaternion Quantum Fields* is a spinor and not a vector.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## The Double Covers and the Lorentz Group

The relevant subgroups are: $\mathbb{B}^\times$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $\mathbb{B}^\times_1$, the unit-norm elements (complex dimension $3$, real dimension $6$); the rotation group $S^3$, the unit-norm real quaternions (real dimension $3$); and the center $\mathbb{C}^\times e_0$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$S^3$ is the maximal compact subgroup of $\mathbb{B}^\times_1$, with Lie algebra the compact rotation subalgebra $\mathrm{K}$ of *Biquaternion Lie Algebra*, §*The Trace-Free Subalgebra*. The center $\{\pm e_0\}$ is discrete, and

$$
\mathbb{B}^\times_1/\{\pm e_0\} \cong SO^+(1,3),
$$

the proper orthochronous Lorentz group, of real dimension $6$. Hence $\mathbb{B}^\times_1$ is a two-sheeted cover of $SO^+(1,3)$ and, being simply connected, is its universal cover: it is the spin group of Lorentzian signature,

$$
\mathbb{B}^\times_1 \cong \mathrm{Spin}(1,3), \qquad \mathrm{B}_0 \cong \mathrm{so}(1,3).
$$

The Lorentz action is rotor conjugation, $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ for $\tilde{\Lambda} \in \mathbb{B}^\times_1$, which preserves $\mathbb{M}_-$ and $N(\tilde{Q})$; its compact part is the rotation family and its non-compact part the hyperbolic rotations, with closed forms in *Biquaternion Elementary Functions*, §*The Exponential in the Two Real Directions*.

## The Rotor and the Sandwich Action

A rotation is performed by conjugation, and the conjugating element is read as a **rotor**. A unit quaternion $q\in S^3$ acts on a biquaternion by the sandwich
$$
\tilde{Q}\mapsto q\,\tilde{Q}\,q^{-1},
$$
and on the imaginary part this is the rotation of $\mathbb{R}^3$ through the angle $\theta$ when $q=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\hat{n}$. Two features are visible in the formula. The angle appears **halved** in the rotor, since the rotation is applied once for the left factor and once for the right, and a full turn of the rotor, $q\mapsto-q$, is the identity rotation: the map $S^3\to SO(3)$ is two-to-one, which is the double cover $SU(2)\to SO(3)$ of the double covers above. The unit quaternions carry the rotations of the definite form, and their complexification carries the motions of the indefinite one; the construction, with the versor and the sandwich action, is that of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* of Part II.

## The Dagger Sandwich

### Left Multiplication as the Reference

The simplest way to make an element act is to multiply by it, $\tilde T \mapsto \tilde{Q}\tilde T$. That map is the regular representation, it is faithful, and its matrix is the $4 \times 4$ regular matrix of *The 4×4 Regular Matrix Element Representation of Biquaternions*. It is recorded here only as the reference column of the comparison table below, since it is an algebra endomorphism rather than an automorphism and it does not preserve the sector structure either.

### The Map on the Whole Algebra

For a unit $\tilde{Q}$, the **sandwich**, or **dagger sandwich**, is

$$
\operatorname{H}_{\tilde{Q}}(\tilde T) = \tilde{Q}\,\tilde T\,\tilde{Q}^{*} ,
$$

and for a rotor $\tilde{\Lambda}$ it is the **rotor conjugation** of the Lorentz group articles, which they write $\operatorname{H}_{\tilde{\Lambda}}$,

$$
\operatorname{H}_{\tilde{\Lambda}}(\tilde T) = \tilde{\Lambda}\,\tilde T\,\tilde{\Lambda}^{*} .
$$

Since $\tilde{\Lambda}^{*} = \overline{\tilde{\Lambda}^{\natural}}$, and the two involutions commute with the biquaternion norm in the way the following sections record, rotor conjugation is the map those articles write as the action of a rotor on a four-vector, now regarded as a map on the whole algebra. Off the rotor slice the sandwich multiplies the interval by the positive factor $|N(\tilde{Q})|^2$ and is a similarity rather than an isometry; on the rotor slice it is the Lorentz action itself.

### The Comparison Table

| | left multiplication $\tilde{Q}\tilde T$ | the sandwich $\operatorname{H}_{\tilde{Q}}$ |
|---|---|---|
| type | algebra endomorphism | no, but an action of the group of units |
| image of $e_0$ | $\tilde{Q}$ | $\tilde{Q}\tilde{Q}^{*}$, in $\mathbb{M}_+$ |
| preserves the biquaternion norm | scales by $N(\tilde{Q})$ | scales by $|N(\tilde{Q})|^2$ |
| preserves the rank | yes | yes |
| kernel on the units | $\{e_0\}$ | the central circle $U(1)e_0$ |
| kernel on the rotors | $\{e_0\}$ | $\{\pm e_0\}$ |
| preserves the two sectors | no | yes |
| preserves the product $\tilde T\tilde V$ | yes | only for unitary $\tilde{Q}$ |

Left multiplication is recorded for comparison only, as the regular representation of *The 4×4 Regular Matrix Element Representation of Biquaternions*. The last two lines are the content of this section: the sandwich is the Lorentz action, and it conserves the interval in place of the product.

## The Sandwich Is the Lorentz Action

### On the Material Sector

Rotor conjugation is the four-vector action of the series, and the identification is established in *The Lorentz Group as Biquaternion Norm Automorphisms* and *The Lorentz Group in Biquaternionic Form*; what is needed here are the three properties, each of which transfers a fact about the biquaternion norm to the operator language.

**Proposition.** For every rotor $\tilde{\Lambda}$, $\operatorname{H}_{\tilde{\Lambda}}$ maps $\mathbb{M}_-$ to itself, maps $\mathbb{M}_+$ to itself, and satisfies $N\big(\operatorname{H}_{\tilde{\Lambda}}(\tilde T)\big) = |N(\tilde{\Lambda})|^2N(\tilde T) = \langle\tilde T,\tilde T\rangle_{\natural} = N(\tilde T)$.

**Proof.** For $\tilde T^{*} = \pm \tilde T$, the image satisfies $\left(\tilde{\Lambda}\tilde T\tilde{\Lambda}^{*}\right)^\dagger = \tilde{\Lambda}\tilde T^{*}\tilde{\Lambda}^{*} = \pm\tilde{\Lambda}\tilde T\tilde{\Lambda}^{*}$, which gives both sector statements. For the biquaternion norm, multiplicativity gives $N(\operatorname{H}_{\tilde{\Lambda}}\tilde T) = N(\tilde{\Lambda})N(\tilde T)N(\tilde{\Lambda}^{*})$, and $N(\tilde{\Lambda}^{*}) = \overline{N(\tilde{\Lambda})}$ because ${}^{*}$ is the composite of $\bar{\phantom{Q}}$, which fixes $N$, with $\bar{\cdot}$, which conjugates it; with $N(\tilde{\Lambda}) = 1$ the factor is one.

The proposition is the mathematical content of the statement that a rotor is a Lorentz transformation of the material sector, and of the Hermitian sector as well: the informational sector is carried to itself by the same action, which is the operator form of the statement that a Lorentz transformation acts on Hermitian forms exactly as it acts on four-vectors.

### The Biquaternion Norm as a Scaled Invariant

Off the unit-norm slice the action is not an isometry but a similarity: $N$ is multiplied by the positive real $|N(\tilde{Q})|^2$. A general unit of $\mathbb{B}$ therefore acts on the two sectors by a transformation that preserves the causal type of every element and rescales the biquaternion norm by one fixed positive factor, and the dilations are the real line that the unit-norm condition removes. This is the reason the physics articles restrict to $N(\tilde{\Lambda}) = 1$ without loss: on that slice the dilation is the identity, and nothing else is lost except the central circle, which acts as the identity anyway.

### The Kernel on the Whole Algebra

On the four-dimensional material sector the kernel of the sandwich is $\{\pm e_0\}$, and that is the statement of the double cover. On the whole eight-dimensional algebra the kernel is larger, and the difference shows what the action on the whole algebra sees that the action on a single sector cannot.

**Theorem.** $\operatorname{H}_{\tilde{Q}} = \mathrm{id}$ on $\mathbb{B}$ if and only if $\tilde{Q} = e^{i\theta}e_0$.

**Proof.** $\operatorname{H}_{\tilde{Q}}(\tilde T) = \tilde T$ for all $\tilde T$ forces $\tilde{Q}\tilde{Q}^{*} = e_0$ on taking $\tilde T = e_0$, so $\tilde{Q}$ is unitary, and forces $\tilde{Q}\tilde T = \tilde T\tilde{Q}$ for all $\tilde T$, so $\tilde{Q}$ is central; a central unitary is a complex number of modulus one. The converse is immediate.

The kernel of the action on the algebra is thus the central circle, of one real dimension, while the action on the material sector has the two-element kernel. Restricting the action to a sector can only shrink the kernel, and the two-element kernel of the Lorentz action is what remains of the circle after the sector is taken.

## What the Sandwich Does to the Six Subspaces

### The Table

| subspace | $\operatorname{H}_{\tilde{Q}}$, general unit | $\operatorname{H}_{\hat{q}}$, real unit quaternion |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | no | yes |
| $\mathrm{Vect}(\mathbb{B})$ (vector subspace) | no | yes |
| $\mathbb{H}_{\mathbb{B}}$ (quaternions) | no | yes |
| $i\mathbb{H}_{\mathbb{B}}$ (antiquaternions) | no | yes |
| $\mathbb{M}_+$ (informational) | yes | yes |
| $\mathbb{M}_-$ (material) | yes | yes |

### Why the Two Sectors Are the Invariant Subspaces

The sectors are the fixed spaces of ${}^{*}$ and $\flat$, and the sandwich is built out of ${}^{*}$, so it preserves them; the computation in the proof of the sector proposition is the whole reason. It preserves nothing else among the six, because it is not an automorphism and has no reason to.

### Why the Centre and the Vector Subspace Are Not Preserved

They are the two pieces of the scalar–vector decomposition, and both are defined without reference to an involution: the centre is the set of elements commuting with everything, and the vector subspace is the traceless part, equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$. A map that respects composition respects both, and the sandwich does not respect composition. Applied to $e_0$ it returns $\tilde{Q}\tilde{Q}^{*}$, whose scalar part is a positive real and whose vector part is generally non-zero: the unit leaves the centre, and the centre is carried into the Hermitian sector.

### Why the Two Halves Need a Unitary Element

The two halves $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are the fixed spaces of the real structure $*$, so the sandwich preserves them exactly when it commutes with $*$, which is the condition that $\tilde{Q}\tilde{Q}^{*}$ be central. That happens exactly for the unitary elements, $\tilde{Q} = e^{i\alpha}\hat{q}$, which are the four-dimensional family whose operators form the rotation group

$$
\left\{\operatorname{H}_{\tilde{Q}} : \tilde{Q} = e^{i\alpha}\hat{q}\right\} \cong SU(2)/\{\pm e_0\} \cong SO(3) ,
$$

acting on the three-dimensional rotation space. For a unitary element the sandwich is multiplicative, hence an automorphism of the algebra, and it preserves all six subspaces, as the table's second column records. **A boost does not preserve the two halves**, and that is the sharpest single way in which the two geometric generators differ.

### A Boost Carries the Centre into the Sectors

The failure is worth exhibiting, since the centre is where the algebra's own time axis lives. For the boost rotor of the next section, $\operatorname{H}_{\tilde{\Lambda}}(e_0) = \tilde{\Lambda}^2 = \cosh\psi\,e_0 + i\sinh\psi\,\hat{\mathbf{u}}$, which is Hermitian of biquaternion norm one: the unit has been carried from the centre into the informational sector. It is the same computation as the statement that the sandwich moves the time axis, which the section on the product takes up.

## The Operator of a Boost

### The Boost Rotor

The corpus's pure boost along the unit real direction $\hat{\mathbf{u}}$, of rapidity $\psi$, is the rotor

$$
\tilde{\Lambda} = \exp\!\left(\frac{\psi}{2}i\hat{\mathbf{u}}\right) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} ,
\qquad \tanh\psi = \frac{u}{c} ,
$$

which is Hermitian, of unit norm, and lies in the informational sector $\mathbb{M}_+$. The factor of $i$ in its vector part is what distinguishes it from a rotation rotor, for which the vector part is real.

### The Four-Position Goes to the Rest Frame

The action of the boost rotor on a four-position is the boost relation of the series. With $\tilde{Q} = ict\,e_0 + \mathbf{x}$ the four-position of a world line of velocity $\mathbf{v}$, and $\tilde{\Lambda}$ the boost rotor along $\hat{\mathbf{v}}$ of rapidity $\psi$ with $\tanh\psi = |\mathbf{v}|/c$,

$$
\tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*} = ic\tau\,e_0 ,
\qquad \tau = t\sqrt{1 - \beta^2} ,
$$

the proper time, so the action carries the four-position from the lab frame to the rest frame. In components, and writing $\beta = |\mathbf{v}|/c$,

$$
ct' = ct\cosh\psi - z\sinh\psi , \qquad z' = z\cosh\psi - ct\sinh\psi ,
$$

for a boost along $e_3$, which is the standard pair of formulas in the corpus's sign convention. The light cone is preserved by the action: a null four-vector is null in every frame, because $N$ is scaled by a positive factor and so vanishes if and only if it vanished.

## The Operator of a Rotation

### The Rotor and the Angle

A pure spatial rotation about the unit real direction $\hat{\mathbf{n}}$ through the angle $\theta$ is the rotor

$$
\tilde{R} = \exp\!\left(\frac{\theta}{2}\hat{\mathbf{n}}\right) = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat{\mathbf{n}} ,
$$

a real unit quaternion lying in $\mathbb{H}_{\mathbb{B}}$. The rotation rotor is unitary, $\tilde{R}^{*} = \tilde{R}^{\natural} = \tilde{R}^{-1}$, which is the property that makes the sandwich preserve the product of two elements of the algebra, as the section on the product shows. Its operator rotates the spatial part of a four-vector:

$$
\tilde{R}\,\tilde{Q}\,\tilde{R}^{*} = icte_0 + \mathbf{x}\cos\theta + \left(\hat{\mathbf{n}}\times\mathbf{x}\right)\sin\theta + \hat{\mathbf{n}}\left(\hat{\mathbf{n}}\cdot\mathbf{x}\right)\left(1-\cos\theta\right),
$$

and it leaves the scalar part untouched. The angle in the operator is twice the half-angle in the element, which is the doubling that the spinor double cover rests on.

### Why the Rotation Doubles and the Boost Does Not

The two geometric rotors are the trigonometric exponential of a real unit direction and the hyperbolic exponential of an imaginary unit direction, and they behave differently under the sandwich, for a reason that is one line long. A rotation rotor is **unitary**, $\tilde{R}^{*} = \tilde{R}^{-1}$, and its sandwich gives the rotation of double the half-angle. A boost rotor is **Hermitian**, $\tilde{\Lambda}^{*} = \tilde{\Lambda}$, so its sandwich is $\tilde{\Lambda}\tilde T\tilde{\Lambda}$ — the element on both sides rather than an element and its inverse — and it gives the boost of rapidity $\psi$, not of $2\psi$. The difference is the same difference as the one between the orthogonal and the pseudo-orthogonal group: the doubling of the angle is a property of the compact factor, and the hyperbolic factor has no doubling because the element is already Hermitian.

The statement is confirmed by the numbers. For a rotation rotor with $\theta = \pi/3$, the action on $e_1$ about $e_3$ gives $\frac12e_1 + \frac{\sqrt3}{2}e_2$, which is the rotation through $\pi/3$; and for the boost rotor of the previous section, the action on the four-position gives $ct' = ct\sqrt{1-\beta^2}$ with $\beta = 0.6$, that is, $0.8$, the boost of the element's own rapidity and not of twice it.

### Both Vector Halves Rotate Together

Because the scalar imaginary $i$ is central, $\operatorname{H}_{\hat{q}}(i\mathbf{w}) = i\,\operatorname{H}_{\hat{q}}(\mathbf{w})$. The rotation therefore acts on the imaginary vector part $ie_k$ and on the real vector part $e_k$ by the same rotation of the same three-dimensional space, so the six-dimensional vector subspace is carried to itself by a single rotation acting complex-linearly. This is the operator statement of the fact that the quaternion rotation group acts on the complexified three-dimensional space, and it is why a rotation is an operator of the algebra rather than merely of the real slice.

## The Interval Is Preserved, the Product Is Not

### Multiplicativity Is the Fixed Time Axis

**Theorem.** For a unit $\tilde{Q}$, the sandwich preserves the product of two elements of the algebra,

$$
\operatorname{H}_{\tilde{Q}}(\tilde T\tilde V) = \operatorname{H}_{\tilde{Q}}(\tilde T)\,\operatorname{H}_{\tilde{Q}}(\tilde V) \qquad \text{for all } \tilde T, \tilde V ,
$$

if and only if $\tilde{Q}$ is unitary, $\tilde{Q}^{*}\tilde{Q} = e_0$; and that is the case exactly when the sandwich fixes the time axis, $\operatorname{H}_{\tilde{Q}}(ie_0) = ie_0$.

**Proof.** The two sides differ only in the middle factor, since $\operatorname{H}_{\tilde{Q}}(\tilde T)\operatorname{H}_{\tilde{Q}}(\tilde V) = \tilde{Q}\tilde T(\tilde{Q}^{*}\tilde{Q})\tilde V\tilde{Q}^{*}$ while $\operatorname{H}_{\tilde{Q}}(\tilde T\tilde V) = \tilde{Q}\tilde T\tilde V\tilde{Q}^{*}$, so equality for all $\tilde T,\tilde V$ is equivalent to $\tilde{Q}^{*}\tilde{Q} = e_0$. In that case $\operatorname{H}_{\tilde{Q}}(ie_0) = i\tilde{Q}\tilde{Q}^{*} = ie_0$, and conversely $\operatorname{H}_{\tilde{Q}}(ie_0) = i\tilde{Q}\tilde{Q}^{*}$ equals $ie_0$ only for $\tilde{Q}\tilde{Q}^{*} = e_0$, which is the same condition.

The unitary elements are exactly the central multiples of the real unit quaternions, $\tilde{Q} = e^{i\alpha}\hat{q}$, and for those the sandwich is the rotation of the previous section. **A rotation therefore preserves the product and the interval; a boost preserves the interval and no longer the product.**

### The Numbers

For the boost rotor $\tilde{\Lambda} = \cosh\frac{\psi}{2}e_0 + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ the failure is measurable and computable. Along $\hat{\mathbf{u}} = \hat{\mathbf{u}}_3$,

$$
\operatorname{H}_{\tilde{\Lambda}}(ie_0) = i\cosh\psi\,e_0 - \sinh\psi\,\hat{\mathbf{u}} ,
\qquad
\operatorname{H}_{\tilde{\Lambda}}(\Delta z\,\hat{\mathbf{u}}) = -i\Delta z\sinh\psi\,e_0 + \Delta z\cosh\psi\,\hat{\mathbf{u}} ,
$$

with the same coefficient $\sinh\psi = \gamma\beta$ in the two lines: $\gamma\beta$ is at once the spatial part acquired by the time axis and the time part acquired by a spatial step, which in the four-vector language is the simultaneity shift $\Delta t = -\gamma v\Delta z/c^2$. The failure of the product has the same coefficient, since

$$
\operatorname{H}_{\tilde{\Lambda}}(\tilde T\tilde V) - \operatorname{H}_{\tilde{\Lambda}}(\tilde T)\operatorname{H}_{\tilde{\Lambda}}(\tilde V) = \tilde{\Lambda}\tilde T\left(e_0 - \tilde{\Lambda}^2\right)\tilde V\tilde{\Lambda} ,
\qquad
e_0 - \tilde{\Lambda}^2 = (1-\cosh\psi)e_0 - i\sinh\psi\,\hat{\mathbf{u}} ,
$$

so the defect is first order in the rapidity, exactly as the simultaneity shift is, while the time dilation $\gamma - 1$ is second order. For a boost of $\beta = 0.6$, where $\gamma = 1.25$ and $\sinh\psi = \gamma\beta = 0.75$: the time axis acquires the spatial part $-0.75$, a step of unit length along the direction of motion acquires the time part $-0.75$, and the defect of the product is of the same size. All three vanish together, at $\beta = 0$.

### Why This Is the Relativity of Time

The dagger sandwich preserves the product of two elements exactly when the acting element is unitary, which is exactly when it fixes the time axis. As soon as the time axis moves — that is, as soon as there is a boost — the sandwich preserves the interval but not the product. In that sense the relativity of time is built into the difference between the two structures that a sandwich can respect: the product holds only in the frame where the time axis is fixed.

Read on the algebra, the statement is that the unit $e_0$ and its scalar imaginary $ie_0$ are not frame-independent objects: they carry the rest frame with them. A rotation leaves both alone, and with them the product of the algebra; a boost carries $ie_0$ to the four-velocity of the moving frame, and no map that does that can respect the multiplication. The interval $N$ is the objective object, and it is exactly what survives.

## Orbits and the Mass Shell

### The Two Invariants

The sandwich preserves the rank of the matrix image always, and it preserves the biquaternion norm itself on the rotor slice; on the material sector it preserves the sign and the vanishing of the biquaternion norm of a four-vector, which is what the causal classification needs. These two invariants cut the elements into the classes the physics articles use.

| class | biquaternion norm $N(\tilde{Q})$ | physical reading |
|---|---|---|
| timelike | $N < 0$, in the corpus's sign convention for $ict\,e_0 + \mathbf{x}$ | a world line of a massive particle |
| null | $N = 0$, $\tilde{Q}\neq 0$ | a point of the light cone, a zero divisor of rank one |
| spacelike | $N > 0$ | a separation outside the cone |
| zero | $\tilde{Q} = 0$ | the origin |

### The Mass Shell and the Light Cone as Single Orbits

Two of the classes are single orbits of the Lorentz action, and the statement is the operator form of a familiar one. The non-zero null elements of $\mathbb{M}_-$ are all conjugate under rotor conjugation, which is the statement that the light cone is one geometric object and not a union of cones attached to individual points; and the timelike elements of a fixed biquaternion norm are all conjugate, which is the mass shell statement that every four-velocity of a given mass is carried to every other by a Lorentz transformation. A general rotor of $SL(2,\mathbb{C})$ acting on the rest four-velocity $i\,mc\,e_0$ gives

$$
\tilde{\Lambda}\,(imc\,e_0)\,\tilde{\Lambda}^{*} ,
$$

of biquaternion norm $N = -m^2c^2$, which is the four-velocity of a massive particle of mass $m$: the orbit of the rest four-velocity is the mass shell. The invariance of $N$ under the action is exactly the on-shell condition, and the reason the mass shell is a single orbit rather than a family of orbits parametrised by direction is that the rotors act transitively on the timelike elements of a fixed biquaternion norm.

### The Rank and the Zero Divisors

The rank-one stratum of the algebra is the set of non-zero elements with $N = 0$, and the corpus calls it the biquaternion null cone; the material-sector part of it is the light cone. Both actions preserve the rank, so no operator can move an element off the cone into an element that is not a zero divisor, and the whole cone is a single orbit of the Lorentz action. The identification of the light cone with the zero-divisor cone, and the use of that identification in the causal structure of the framework, are the subject of *The Light Cone as the Biquaternion Zero-Divisor Cone*.

## Ordering and the Wigner Rotor

### Composition of Operators

**Proposition.** $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}} = \operatorname{H}_{\tilde{Q}\tilde{R}}$.

**Proof.** $\tilde{Q}(\tilde{R}\tilde T\tilde{R}^{*})\tilde{Q}^{*} = (\tilde{Q}\tilde{R})\tilde T(\tilde{Q}\tilde{R})^\dagger$.

The physical consequence is that the operators compose as the elements do, so an operator can be decomposed by decomposing its element. In particular the product of two boosts is a rotor, and the polar representation of that product has a rotor factor: **the Wigner rotation**.

### Two Orthogonal Boosts

Take the two pure boosts

$$
\tilde{\Lambda}_1 = \exp\!\left(\frac{0.7}{2}ie_1\right) , \qquad \tilde{\Lambda}_2 = \exp\!\left(\frac{0.9}{2}ie_2\right) ,
$$

of rapidities $0.7$ along $e_1$ and $0.9$ along $e_2$. Their product $\tilde{\Lambda}_1\tilde{\Lambda}_2$ is a rotor, and its polar representation $\tilde{\Lambda}_1\tilde{\Lambda}_2 = B\hat{q}$ has

$$
\hat{q} = \cos\frac{\theta_W}{2} - \sin\frac{\theta_W}{2}e_3 , \qquad \theta_W = 0.281950221701 \ \text{rad} ,
$$

a rotation about $-e_3$; the reversed order gives the same angle with the axis $+e_3$. The angle is not a free parameter, and it is fixed in closed form by the two rapidities:

$$
\cos\theta_W = \frac{\cosh 0.7 + \cosh 0.9}{1 + \cosh 0.7\cosh 0.9} = 0.960514656248 , \qquad \theta_W = 0.281950221701 ,
$$

which agrees with the polar decomposition of the product to twelve digits. The operator statement is that the composite of two boost operators is a boost operator followed by a rotation operator, and that the rotation is not optional: two successive non-collinear boosts are not a boost.

### Thomas Precession

The Wigner rotor is the kinematic content of Thomas precession, and the operator reading makes the bookkeeping automatic: composing the two boosts and reading off the rotor factor is the whole computation, and the rotor factor acts on the spinor by left multiplication with the half-angle. The precession rate of a spinning particle in a circular orbit, the factor of one half that distinguishes the Thomas value from the naive one, and the comparison with the Bargmann–Michel–Telegdi equation are the subject of *Thomas Precession as a Biquaternion Rotor Effect* and *The Thomas Precession*, and the closed form of the Wigner angle above is the element they use.

## The Operator and the Polar Representation

The two subjects meet in the kernel statement of the section on the Lorentz action, and the meeting is a dictionary.

| polar datum of $\tilde{Q} = re^{i\alpha}B\hat{q}$ | the sandwich $\operatorname{H}_{\tilde{Q}}$ |
|---|---|
| scale $r$ | the dilation $|N(\tilde{Q})|^2 = r^4$ of the interval |
| phase $e^{i\alpha}$ | not seen |
| boost $B$ | the boost factor of the action |
| rotor $\hat{q}$ | the rotation factor of the action |

The operator sees the boost and the rotor of the element, in that order, and it sees the scale only as the single dilation $r^4$ of the interval; the phase it does not see at all, which is the kernel statement above. Stated in the language of the polar articles: the polar representation exhibits four factors because one element carries them, and the operator carries the same four with the phase lost and the scale collapsed into the dilation of the interval. The two readings are companions, and each is the other's explanation of a factor count.

## Reflections

The sandwich also realises the **reflections**, on the subspaces where the multiplication is Clifford. Let $v\in\mathbb{B}$ with $N(v)=1$; the reflection in the hyperplane $v^{\perp}$ is the linear map
$$
\rho_v(\tilde T)=-v\,\tilde T\,v^{-1}=-v\,\tilde T\,\bar{v},
$$
the second equality using $v^{-1}=\bar{v}/N(v)=\bar{v}$ for a norm-one element.

**Theorem.** For $v$ with $N(v)=1$ the map $\rho_v$ preserves the biquaternion norm and its polar form, satisfies $\rho_v(v)=-v$, and fixes pointwise every element that anticommutes with $v$; its square is the conjugation $\rho_v^2(\tilde T)=v^2\tilde Tv^{-2}$.

**Proof.** Since $v$ is invertible, $\rho_v$ is a linear automorphism, and $N(\rho_v(\tilde T))=N(v)N(\tilde T)N(v)^{-1}=N(\tilde T)$ by multiplicativity of the norm, whence the polar form is preserved too; the statement $\rho_v(v)=-vvv^{-1}=-v$ is immediate. If $\tilde T$ anticommutes with $v$, then $-v\tilde Tv^{-1}=\tilde Tv\,v^{-1}=\tilde T$, so $\tilde T$ is fixed. The square is $\rho_v(\rho_v(\tilde T))=v(v\tilde Tv^{-1})v^{-1}=v^2\tilde Tv^{-2}$, a conjugation by $v^2$, and it is the identity exactly when $v^2$ is a scalar.

**Remark (which subspaces carry the reflections).** For the formula to be a genuine reflection, orthogonality and anticommutation must coincide on the ambient subspace. This happens when the multiplication is Clifford there: on the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$ and its real form $\mathbb{R}\{e_1,e_2,e_3\}$ one has
$$
v\tilde T+\tilde Tv=-2B(v,\tilde T)\,e_0,
$$
so the hyperplane $v^{\perp}$ is exactly the set of elements anticommuting with $v$, and $\rho_v$ fixes $v^{\perp}$ pointwise, negates $v$, and has complex-linear determinant $-1$. Here $v^2=-\bigl(\sum_k v_k^2\bigr)e_0$ is a scalar, so $\rho_v$ is an involution. On the quaternion and Hermitian subspaces the elements do not anticommute, and a norm-one element acts there by conjugation as a rotation rather than as a reflection. On the algebra as a whole, likewise, $\rho_v$ has determinant $+1$ for every $v$ with $N(v)=1$, so the maps attached to the finite groups of units are rotations and not reflections; and on $\mathbb{H}_{\mathbb{B}}$ the norm-one element $e_0$ is central, so $\rho_{e_0}=-\mathrm{id}$ and nothing is fixed.

**Theorem (Cartan–Dieudonné in the biquaternion algebra).** On the complex three-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$ and on its real form $\mathbb{R}\{e_1,e_2,e_3\}$, every isometry is a product of at most three reflections $\rho_v$ with $N(v)=1$.

**Proof.** On these subspaces $N(v)=v_1^2+v_2^2+v_3^2$ is a non-degenerate form, and by the theorem above the maps $\rho_v$ with $N(v)=1$ are its reflections in the hyperplanes $v^{\perp}$; the Cartan–Dieudonné theorem, stated for a general vector space in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, then gives generation by at most $\dim W=3$ reflections.

**Remark.** The reflections of this section are attached to the odd part $\mathrm{Vect}(\mathbb{B})$; the Lorentz reflections are not of the shape $\rho_v$ and live in the Clifford layer, not in $\mathbb{B}$.

## Rotations, Boosts and the Two-Sided Action

Over the reals the trace-free subalgebra splits into the compact rotation directions $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ and the hyperbolic directions $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ (*Biquaternion Lie Algebra*). A **rotation** is the motion generated by the first, an element of the compact group $S^3$ of the rotation family; a **boost**, or hyperbolic rotation, is the motion generated by the second, an isometry of the indefinite form that fixes a timelike direction and leaves the light cone invariant. Both are boosts or rotations of the form the algebra carries, and together they generate the Lorentz group $SO^+(1,3)$ of the double covers above; the rotations are the isometries of the definite form, the boosts those of the indefinite one, and the closed forms of their exponentials are in *Biquaternion Elementary Functions*.

A **two-sided** action, $\tilde{Q}\mapsto u\,\tilde{Q}\,v$ with $u,v\in S^3$ independent, is a four-dimensional rotation: the pair $(u,v)$ acts on $\mathbb{B}\cong\mathbb{R}^8$ preserving the Euclidean form, with kernel $\{\pm(e_0,e_0)\}$, so the two-sided action realises
$$
(S^3\times S^3)/\{\pm e_0\}\cong SO(4)
$$
on the algebra. The one-sided action is its diagonal restriction, and the Lorentzian motions are obtained from the complexification instead.
**Physical reading: the motions of the framework.** The isometries of the norm are the physical motions: $S^3=Sp(1)$ supplies the spatial rotations of the material sector, and $\mathbb{B}^{\times}_1\cong Spin(1,3)$ supplies the Lorentz transformations, the boosts being the hyperbolic directions of the trace-free subalgebra. The two-sided action is the Euclidean reading the informational sector $\mathbb{M}_+$ carries, and its diagonal restriction is the Lorentzian one. Because the rotor acts by conjugation the angle is halved and the map to $SO^+(1,3)$ is two-to-one: the double cover is not an accident of the parametrisation but the statement that a $2\pi$ rotation returns a vector and reverses a spinor, the fact behind the spin-$\tfrac{1}{2}$ behaviour of *Biquaternion Non Relativistic Quantum Theory*.

## Worked Examples

### A Boost Rotor Acting on a Four-Position

Let $\beta = 0.6$ along $e_3$, so that $\psi = \operatorname{artanh}0.6$, $\cosh\frac{\psi}{2} = 1.060660172$ and $\sinh\frac{\psi}{2} = 0.353553391$, and let $\tilde{Q} = ict\,e_0 + 0.6ct\,e_3$ with $ct = 1$. Then

$$
\tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*} = i\tau e_0 , \qquad \tau = \sqrt{1-0.36} = 0.8 ,
$$

so that $ct' = 0.8$ and $z' = 2.8\times10^{-17}$, the residual of a zero. The example is the corpus's own numerical check of the boost rotor, and it exhibits the action as the statement that the four-position of a moving particle is carried to its rest frame.

### A Rotation Rotor Acting on a Four-Vector

Let $\tilde{R} = \cos\frac{\pi}{6} + \sin\frac{\pi}{6}e_3$, of angle $\theta = \pi/3$, and let $\tilde{Q} = 2ie_0 + e_1 + 0.5e_3$. Then

$$
\tilde{R}\,\tilde{Q}\,\tilde{R}^{*} = 2ie_0 + 0.5e_1 + 0.866025404e_2 + 0.5e_3 ,
$$

so the temporal and $e_3$ components are untouched and the spatial part is rotated through $\pi/3$ in the $(e_1,e_2)$ plane: the values are $\cos\frac{\pi}{3} = 0.5$ and $\sin\frac{\pi}{3} = 0.866025404$. The biquaternion norm is unchanged, $N = -4 + 1 + 0.25 = -2.75$ before and after.

### A Boost Rotor Acting on a Null Four-Vector

With $\tilde{\Lambda} = \frac53e_0 + \frac43ie_3$, of biquaternion norm $N = \frac{25}{9} - \frac{16}{9} = 1$ and hence of rapidity $\psi = 2\ln 3$, for which $\beta = \tanh\psi = \frac{40}{41}$, and with the null four-vector $\tilde{Q} = ie_0 + e_1$, the sandwich gives

$$
\operatorname{H}_{\tilde{\Lambda}}(\tilde{Q}) = \frac{41}{9}ie_0 + e_1 - \frac{40}{9}e_3 ,
\qquad
\frac{41}{9} = \cosh\psi , \quad \frac{40}{9} = \sinh\psi .
$$

The image is anti-Hermitian, so it is again a four-vector, as the sector proposition requires; its biquaternion norm is $-\frac{1681}{81} + 1 + \frac{1600}{81} = 0$, so the null vector is still null, as the invariance of the cone requires; and the spatial direction $e_1$, transverse to the boost, is untouched. The numerical values are $\frac{41}{9} = 4.5555\ldots$ and $\frac{40}{9} = 4.4444\ldots$. The example is the boost of the corpus's normalisation with $\beta = \frac{40}{41}$, applied to a lightlike four-vector.

### The Wigner Angle

For the two boosts of rapidities $0.7$ and $0.9$ about orthogonal axes, the polar decomposition of the product gives a rotor of angle $0.281950221701$ rad, and

$$
\cos\theta_W = \frac{\cosh 0.7 + \cosh 0.9}{1+\cosh0.7\cosh0.9} = \frac{1.255169006 + 1.433086385}{1 + 1.798800804} = 0.960514656 ,
$$

which gives the same angle. The angle vanishes when either rapidity vanishes and when the two axes are collinear, both of which are immediate from the closed form, and it is largest for two boosts of comparable rapidity about orthogonal axes.

### The Double Cover

Let $\tilde{R}$ be any rotation rotor and consider $-\tilde{R}$. Since $-\tilde{R}$ is a central multiple of $\tilde{R}$, and a central multiple scales the sandwich by the squared modulus of its complex factor, $\operatorname{H}_{-\tilde{R}} = \operatorname{H}_{\tilde{R}}$, while $-\tilde{R}\neq\tilde{R}$ as algebra elements. The two rotors therefore represent the same operator and are not the same physical element, which is the statement that the rotation group has a two-fold cover by the rotors. On the material sector the same computation is the standard double cover of the Lorentz group, and the kernel statement for the whole algebra is its refinement.

## Summary

The motions of the biquaternion algebra are the isometries of its biquaternion norm, and they are the rotations and the Lorentz transformations. The unit quaternions $S^3=Sp(1)$ carry the rotations of the definite form by the sandwich $\tilde{Q}\mapsto q\tilde{Q}q^{-1}$, in which the angle is halved and $\pm q$ gives the same rotation: the map $S^3\to SO(3)$ is the double cover $SU(2)\to SO(3)$. Complexifying, the norm-one group $\mathbb{B}^\times_1$ carries the rotations of the indefinite form, and $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ with $\mathbb{B}^\times_1\cong Spin(1,3)$, so that the double cover of the proper orthochronous Lorentz group is realised inside the algebra; the trace-free subalgebra splits into the compact rotation directions and the hyperbolic directions, and it is the boosts generated by the latter that are the isometries of the indefinite form.

The action of an arbitrary unit on the whole algebra is the **dagger sandwich** $\operatorname{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$, and on the norm-one slice it is the Lorentz action written above. It is the only two-sided sandwich $\tilde T\mapsto A\tilde TB$ that carries the Hermitian sectors into themselves; it preserves $\mathbb{M}_+$ and $\mathbb{M}_-$ and no other of the six subspaces; it scales the biquaternion norm by $|N(\tilde{Q})|^2$ and preserves it on the rotor slice; and its kernel is the central circle $U(1)e_0$, which reduces to $\{\pm e_0\}$ on the slice and is the double cover. It is multiplicative exactly for the unitary elements, which are exactly those that fix the time axis; a boost therefore preserves the interval and not the product, and that single fact is the algebra's form of the relativity of simultaneity. The operators compose as their elements do, so two non-collinear boosts compose to a boost followed by the rotation the series calls the Wigner rotation.

The two-sided action $\tilde{Q}\mapsto u\tilde{Q}v$ with independent unit quaternions preserves the Euclidean form and gives $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$; the one-sided action is its diagonal restriction. The reflections are the maps $\rho_v(\tilde T)=-v\tilde Tv^{-1}=-v\tilde T\bar v$ with $N(v)=1$, defined on the Clifford vector subspace $\mathrm{Vect}(\mathbb{B})$ and its real form, where orthogonality and anticommutation coincide; on that subspace every isometry is a product of at most three of them, by Cartan–Dieudonné. The construction is that of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* of Part II, and the full symmetry group of the algebra, wider than its isometries, is in *Biquaternion Automorphisms and Derivations*. Physically these motions are the changes of reference frame and the rotations of the framework: the boost is the change of inertial frame, the rotor the spatial rotation, the two-sided action the Euclidean reading of the informational sector, and the halving of the angle the geometric origin of the spinor double cover.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q})$ | Biquaternion norm; the invariant of the motions |
| $S^3=Sp(1)$ | Unit quaternions; rotors of the definite form |
| $q\tilde{Q}q^{-1}$ | Sandwich action; rotor conjugation |
| $\rho_v(\tilde T)=-v\tilde Tv^{-1}=-v\tilde T\bar v$ | Reflection in $v^{\perp}$ on $\mathrm{Vect}(\mathbb{B})$, $N(v)=1$ |
| $v\tilde T+\tilde Tv=-2B(v,\tilde T)e_0$ | Anticommutation as orthogonality on $\mathrm{Vect}(\mathbb{B})$; then $v^{\perp}=\{\tilde T:\tilde Tv=-v\tilde T\}$ |
| Cartan–Dieudonné | Every isometry of $\mathrm{Vect}(\mathbb{B})$ is at most three reflections $\rho_v$ |
| $S^3\to SO(3)$ | Double cover $SU(2)\to SO(3)$; $\pm q$ give the same rotation |
| $\mathbb{B}^\times_1\cong Spin(1,3)$ | Norm-one group as the spin group; double cover of $SO^+(1,3)$ |
| $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ | Proper orthochronous Lorentz group |
| $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Rotation directions; compact |
| $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | Hyperbolic (boost) directions |
| $u\tilde{Q}v$ | Two-sided action; preserves the Euclidean form |
| $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$ | Two-sided action as four-dimensional rotations |
| $\operatorname{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$ | The dagger sandwich; the action of a unit on the whole algebra |
| $\operatorname{H}_{z\tilde{Q}}=\lvert z\rvert^2\operatorname{H}_{\tilde{Q}}$ | Central phase invisible; the modulus is the dilation |
| $N(\operatorname{H}_{\tilde{Q}}(\tilde T))=\lvert N(\tilde{Q})\rvert^2N(\tilde T)$ | Scaling of the biquaternion norm; an isometry on the rotor slice |
| $U(1)=\{e^{i\theta}e_0\}$ | Kernel of the sandwich; $\{\pm e_0\}$ on the norm-one slice |
| $\hat{\mathbf{n}},\theta$ | Axis and angle of a rotation rotor, $\tilde{R}=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\hat{\mathbf{n}}$ |
| $\hat{\mathbf{u}},\psi$ | Axis and rapidity of a boost rotor, $\tilde{\Lambda}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, $\tanh\psi=u/c$ |
| $\theta_W$ | The Wigner angle of two successive boosts |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the quaternion bilinear form, $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=N(\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the complex sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the complex bilinear form, the scalar part of the complex bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
