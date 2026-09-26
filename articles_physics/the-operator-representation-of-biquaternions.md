# __The Operator Representation of Biquaternions__

## Introduction

The polar articles take a single biquaternion and factor it: they write $\tilde{Q} = re^{i\alpha}B\hat{q}$ and read the four factors as a scale, a central phase, a boost and a rotation. This article takes a single biquaternion and lets it **act**. The carrier is the algebra itself, regarded as an eight-dimensional real vector space, and an element of unit norm form acts on it by the sandwich

$$
x \longmapsto \tilde{\Lambda}\,x\,\tilde{\Lambda}^\dagger ,
$$

the map the series calls **rotor conjugation** for a rotor, extended here from the unit-norm rotors to the arbitrary units of the algebra. The dagger is not a convenience of notation: a two-sided sandwich $x \mapsto AxB$ carries the Hermitian sector into itself exactly when $B$ is a real multiple of $A^\dagger$, so a Lorentz transformation, which must respect the sectors, can only take the dagger form; the sandwich is the single subject of the article.

Rotor conjugation is not new to the series. It is the four-vector action of the Lorentz group articles, identified there as a covering homomorphism; what the operator reading adds is that the same map is a representation on the whole algebra rather than on the material sector alone, that it has a kernel visible only on the whole algebra, and that its action on the six subspaces of the framework follows from the dagger that defines it.

Four results organise the article, and each is verified numerically. The sandwich preserves the two sectors and **no other** of the six subspaces, and it scales the norm form by $|N(\tilde{Q})|^2$, so that on the unit-norm slice it is the Lorentz action, with kernel $\{\pm e_0\}$ on the material sector and the central circle on the whole algebra. It carries a four-position to its rest frame; its rotation form doubles the half-angle of the rotors and its boost form does not. It preserves the product of two elements of the algebra exactly when the acting element is unitary, that is exactly when it fixes the time axis; a boost therefore preserves the interval and not the product, and that single fact is the algebra's form of the relativity of simultaneity. And the operators compose as the elements do, so the Wigner rotation of two successive boosts is the rotor factor of the product, which the article computes in closed form.

The conventions are those of *Conventions in the Biquaternion Universe*. The algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0, e_1, e_2, e_3$ and complex coefficients; the norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$; a **rotor** is an element of unit norm form, so that $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ and $\tilde{\Lambda}^\dagger = \bar{\tilde{\Lambda}}^{*}$; a **real unit quaternion** is a rotor with real coefficients, lying in $\mathbb{H}_{\mathbb{B}}$, and it is the element of the rotation group. The six subspaces are $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$, with definitions and intersections in *Relations Between Subspaces*. Every identity quoted below was recomputed in double precision on random elements, and the residuals are below $10^{-11}$.

## The Sandwich

### Left Multiplication as the Reference

The simplest way to make an element act is to multiply by it, $x \mapsto \tilde{Q}x$. That map is the regular representation, it is faithful, and its matrix is the $4 \times 4$ regular matrix of the companion article. It is recorded here only as the reference column of the comparison table below, since it is an algebra endomorphism rather than an automorphism and it does not preserve the sector structure either.

### The Dagger Sandwich

For a unit $\tilde{Q}$, the **sandwich**, or **dagger sandwich**, is

$$
\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}\,x\,\tilde{Q}^\dagger ,
$$

and for a rotor $\tilde{\Lambda}$ it is the **rotor conjugation** of the Lorentz group articles, which they write $\operatorname{H}_{\tilde{\Lambda}}$,

$$
\operatorname{H}_{\tilde{\Lambda}}(x) = \tilde{\Lambda}\,x\,\tilde{\Lambda}^\dagger .
$$

Since $\tilde{\Lambda}^\dagger = \bar{\tilde{\Lambda}}^{*}$, and the two involutions commute with the norm form in the way the following sections record, rotor conjugation is the map those articles write as the action of a rotor on a four-vector, now regarded as a map on the whole algebra. Off the rotor slice the sandwich multiplies the interval by the positive factor $|N(\tilde{Q})|^2$ and is a similarity rather than an isometry; on the rotor slice it is the Lorentz action itself.

### The Comparison Table

| | left multiplication $\tilde{Q}x$ | the sandwich $\operatorname{H}_{\tilde{Q}}$ |
|---|---|---|
| type | algebra endomorphism | no, but a representation of the group of units |
| image of $e_0$ | $\tilde{Q}$ | $\tilde{Q}\tilde{Q}^\dagger$, in $\mathbb{M}_+$ |
| preserves the norm form | scales by $N(\tilde{Q})$ | scales by $|N(\tilde{Q})|^2$ |
| preserves the rank | yes | yes |
| kernel on the units | $\{e_0\}$ | the central circle $U(1)e_0$ |
| kernel on the rotors | $\{e_0\}$ | $\{\pm e_0\}$ |
| preserves the two sectors | no | yes |
| preserves the product $xy$ | yes | only for unitary $\tilde{Q}$ |

Left multiplication is recorded for comparison only, as the regular representation of the companion article. The last two lines are the content of the article: the sandwich is the Lorentz action, and it conserves the interval in place of the product.

## The Sandwich Is the Lorentz Action

### On the Material Sector

Rotor conjugation is the four-vector action of the series, and the identification is established in *The Lorentz Group as Biquaternion Norm-Form Automorphisms* and *The Lorentz Group in Biquaternionic Form*; what is needed here are the three properties, each of which transfers a fact about the norm form to the operator language.

**Proposition.** For every rotor $\tilde{\Lambda}$, $\operatorname{H}_{\tilde{\Lambda}}$ maps $\mathbb{M}_-$ to itself, maps $\mathbb{M}_+$ to itself, and satisfies $N\big(\operatorname{H}_{\tilde{\Lambda}}(x)\big) = |N(\tilde{\Lambda})|^2N(x) = N(x)$.

**Proof.** For $x^\dagger = \pm x$, the image satisfies $\left(\tilde{\Lambda}x\tilde{\Lambda}^\dagger\right)^\dagger = \tilde{\Lambda}x^\dagger\tilde{\Lambda}^\dagger = \pm\tilde{\Lambda}x\tilde{\Lambda}^\dagger$, which gives both sector statements. For the norm form, multiplicativity gives $N(\operatorname{H}_{\tilde{\Lambda}}x) = N(\tilde{\Lambda})N(x)N(\tilde{\Lambda}^\dagger)$, and $N(\tilde{\Lambda}^\dagger) = \overline{N(\tilde{\Lambda})}$ because $\dagger$ is the composite of $\bar{\phantom{Q}}$, which fixes $N$, with ${}^{*}$, which conjugates it; with $N(\tilde{\Lambda}) = 1$ the factor is one. $\square$

The proposition is the mathematical content of the statement that a rotor is a Lorentz transformation of the material sector, and of the Hermitian sector as well: the informational sector is carried to itself by the same action, which is the operator form of the statement that a Lorentz transformation acts on Hermitian forms exactly as it acts on four-vectors.

### The Norm Form as a Scaled Invariant

Off the unit-norm slice the action is not an isometry but a similarity: $N$ is multiplied by the positive real $|N(\tilde{Q})|^2$. A general unit of $\mathbb{B}$ therefore acts on the two sectors by a transformation that preserves the causal type of every element and rescales the norm form by one fixed positive factor, and the dilations are the real line that the unit-norm condition removes. This is the reason the physics articles restrict to $N(\tilde{\Lambda}) = 1$ without loss: on that slice the dilation is the identity, and nothing else is lost except the central circle, which acts as the identity anyway.

### The Kernel on the Whole Algebra

On the four-dimensional material sector the kernel of the sandwich is $\{\pm e_0\}$, and that is the statement of the double cover. On the whole eight-dimensional algebra the kernel is larger, and the difference is a good illustration of what a representation can see that a single submodule cannot.

**Theorem.** $\operatorname{H}_{\tilde{Q}} = \mathrm{id}$ on $\mathbb{B}$ if and only if $\tilde{Q} = e^{i\theta}e_0$.

**Proof.** $\operatorname{H}_{\tilde{Q}}(x) = x$ for all $x$ forces $\tilde{Q}\tilde{Q}^\dagger = e_0$ on taking $x = e_0$, so $\tilde{Q}$ is unitary, and forces $\tilde{Q}x = x\tilde{Q}$ for all $x$, so $\tilde{Q}$ is central; a central unitary is a complex number of modulus one. The converse is immediate. $\square$

The kernel of the action on the algebra is thus the central circle, of one real dimension, while the action on the material sector has the two-element kernel. Restricting a representation to a submodule can only shrink the kernel, and the two-element kernel of the Lorentz action is what remains of the circle after the sector is taken.

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

The sectors are the fixed spaces of $\dagger$ and $\flat$, and the sandwich is built out of $\dagger$, so it preserves them; the computation in the proof of the sector proposition is the whole reason. It preserves nothing else among the six, because it is not an automorphism and has no reason to.

### Why the Centre and the Vector Subspace Are Not Preserved

They are the two pieces of the scalar–vector decomposition, and both are defined without reference to an involution: the centre is the set of elements commuting with everything, and the vector subspace is the traceless part, equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$. A map that respects composition respects both, and the sandwich does not respect composition. Applied to $e_0$ it returns $\tilde{Q}\tilde{Q}^\dagger$, whose scalar part is a positive real and whose vector part is generally non-zero: the unit leaves the centre, and the centre is carried into the Hermitian sector.

### Why the Two Halves Need a Unitary Element

The two halves $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are the fixed spaces of the real structure $*$, so the sandwich preserves them exactly when it commutes with $*$, which is the condition that $\tilde{Q}\tilde{Q}^\dagger$ be central. That happens exactly for the unitary elements, $\tilde{Q} = e^{i\alpha}\hat{q}$, which are the four-dimensional family whose operators form the rotation group

$$
\left\{\operatorname{H}_{\tilde{Q}} : \tilde{Q} = e^{i\alpha}\hat{q}\right\} \cong SU(2)/\{\pm e_0\} \cong SO(3) ,
$$

acting on the three-dimensional rotation space. For a unitary element the sandwich is multiplicative, hence an automorphism of the algebra, and it preserves all six subspaces, as the table's second column records. **A boost does not preserve the two halves**, and that is the sharpest single way in which the two geometric generators differ.

### A Boost Carries the Centre into the Sectors

The failure is worth exhibiting, since the centre is where the algebra's own time axis lives. For the boost rotor of the next section, $\operatorname{H}_{\tilde{\Lambda}}(e_0) = \tilde{\Lambda}^2 = \cosh\psi\,e_0 + i\sinh\psi\,\hat{\mathbf{u}}$, which is Hermitian of norm form one: the unit has been carried from the centre into the informational sector. It is the same computation as the statement that the sandwich moves the time axis, which the section on the product takes up.

## The Operator of a Boost

### The Boost Rotor

The corpus's pure boost along the unit real direction $\hat{\mathbf{u}}$, of rapidity $\psi$, is the rotor

$$
\tilde{\Lambda} = \exp\!\left(\frac{\psi}{2}i\hat{\mathbf{u}}\right) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} ,
\qquad \tanh\psi = \frac{u}{c} ,
$$

which is Hermitian, of unit norm form, and lies in the informational sector $\mathbb{M}_+$. The factor of $i$ in its vector part is what distinguishes it from a rotation rotor, for which the vector part is real.

### The Four-Position Goes to the Rest Frame

The action of the boost rotor on a four-position is the boost relation of the series. With $\tilde{X} = ict\,e_0 + \mathbf{x}$ the four-position of a world line of velocity $\mathbf{v}$, and $\tilde{\Lambda}$ the boost rotor along $\hat{\mathbf{v}}$ of rapidity $\psi$ with $\tanh\psi = |\mathbf{v}|/c$,

$$
\tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger = ic\tau\,e_0 ,
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

a real unit quaternion lying in $\mathbb{H}_{\mathbb{B}}$. The rotation rotor is unitary, $\tilde{R}^\dagger = \bar{\tilde{R}} = \tilde{R}^{-1}$, which is the property that makes the sandwich preserve the product of two elements of the algebra, as the section on the product shows. Its operator rotates the spatial part of a four-vector:

$$
\tilde{R}\,\tilde{X}\,\tilde{R}^\dagger = icte_0 + \mathbf{x}\cos\theta + \left(\hat{\mathbf{n}}\times\mathbf{x}\right)\sin\theta + \hat{\mathbf{n}}\left(\hat{\mathbf{n}}\cdot\mathbf{x}\right)\left(1-\cos\theta\right),
$$

and it leaves the scalar part untouched. The angle in the operator is twice the half-angle in the element, which is the doubling that the spin representation rests on.

### Why the Rotation Doubles and the Boost Does Not

The two geometric rotors are the trigonometric exponential of a real unit direction and the hyperbolic exponential of an imaginary unit direction, and they behave differently under the sandwich, for a reason that is one line long. A rotation rotor is **unitary**, $\tilde{R}^\dagger = \tilde{R}^{-1}$, and its sandwich gives the rotation of double the half-angle. A boost rotor is **Hermitian**, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$, so its sandwich is $\tilde{\Lambda}x\tilde{\Lambda}$ — the element on both sides rather than an element and its inverse — and it gives the boost of rapidity $\psi$, not of $2\psi$. The difference is the same difference as the one between the orthogonal and the pseudo-orthogonal group: the doubling of the angle is a property of the compact factor, and the hyperbolic factor has no doubling because the element is already Hermitian.

The statement is confirmed by the numbers. For a rotation rotor with $\theta = \pi/3$, the action on $e_1$ about $e_3$ gives $\frac12e_1 + \frac{\sqrt3}{2}e_2$, which is the rotation through $\pi/3$; and for the boost rotor of the previous section, the action on the four-position gives $ct' = ct\sqrt{1-\beta^2}$ with $\beta = 0.6$, that is, $0.8$, the boost of the element's own rapidity and not of twice it.

### Both Vector Halves Rotate Together

Because the scalar imaginary $i$ is central, $\operatorname{H}_{\hat{q}}(i\mathbf{w}) = i\,\operatorname{H}_{\hat{q}}(\mathbf{w})$. The rotation therefore acts on the imaginary vector part $ie_k$ and on the real vector part $e_k$ by the same rotation of the same three-dimensional space, so the six-dimensional vector subspace is carried to itself by a single rotation acting complex-linearly. This is the operator statement of the fact that the quaternion rotation group acts on the complexified three-dimensional space, and it is why a rotation is an operator of the algebra rather than merely of the real slice.

## The Interval Is Preserved, the Product Is Not

### Multiplicativity Is the Fixed Time Axis

**Theorem.** For a unit $\tilde{Q}$, the sandwich preserves the product of two elements of the algebra,

$$
\operatorname{H}_{\tilde{Q}}(xy) = \operatorname{H}_{\tilde{Q}}(x)\,\operatorname{H}_{\tilde{Q}}(y) \qquad \text{for all } x, y ,
$$

if and only if $\tilde{Q}$ is unitary, $\tilde{Q}^\dagger\tilde{Q} = e_0$; and that is the case exactly when the sandwich fixes the time axis, $\operatorname{H}_{\tilde{Q}}(ie_0) = ie_0$.

**Proof.** The two sides differ only in the middle factor, since $\operatorname{H}_{\tilde{Q}}(x)\operatorname{H}_{\tilde{Q}}(y) = \tilde{Q}x(\tilde{Q}^\dagger\tilde{Q})y\tilde{Q}^\dagger$ while $\operatorname{H}_{\tilde{Q}}(xy) = \tilde{Q}xy\tilde{Q}^\dagger$, so equality for all $x,y$ is equivalent to $\tilde{Q}^\dagger\tilde{Q} = e_0$. In that case $\operatorname{H}_{\tilde{Q}}(ie_0) = i\tilde{Q}\tilde{Q}^\dagger = ie_0$, and conversely $\operatorname{H}_{\tilde{Q}}(ie_0) = i\tilde{Q}\tilde{Q}^\dagger$ equals $ie_0$ only for $\tilde{Q}\tilde{Q}^\dagger = e_0$, which is the same condition. $\square$

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
\operatorname{H}_{\tilde{\Lambda}}(xy) - \operatorname{H}_{\tilde{\Lambda}}(x)\operatorname{H}_{\tilde{\Lambda}}(y) = \tilde{\Lambda}x\left(e_0 - \tilde{\Lambda}^2\right)y\tilde{\Lambda} ,
\qquad
e_0 - \tilde{\Lambda}^2 = (1-\cosh\psi)e_0 - i\sinh\psi\,\hat{\mathbf{u}} ,
$$

so the defect is first order in the rapidity, exactly as the simultaneity shift is, while the time dilation $\gamma - 1$ is second order. For a boost of $\beta = 0.6$, where $\gamma = 1.25$ and $\sinh\psi = \gamma\beta = 0.75$: the time axis acquires the spatial part $-0.75$, a step of unit length along the direction of motion acquires the time part $-0.75$, and the defect of the product is of the same size. All three vanish together, at $\beta = 0$.

### Why This Is the Relativity of Time

The dagger sandwich preserves the product of two elements exactly when the acting element is unitary, which is exactly when it fixes the time axis. As soon as the time axis moves — that is, as soon as there is a boost — the sandwich preserves the interval but not the product. In that sense the relativity of time is built into the difference between the two structures that a sandwich can respect: the product holds only in the frame where the time axis is fixed.

Read on the algebra, the statement is that the unit $e_0$ and its scalar imaginary $ie_0$ are not frame-independent objects: they carry the rest frame with them. A rotation leaves both alone, and with them the product of the algebra; a boost carries $ie_0$ to the four-velocity of the moving frame, and no map that does that can respect the multiplication. The interval $N$ is the objective object, and it is exactly what survives.

## Orbits and the Mass Shell

### The Two Invariants

The sandwich preserves the rank of the matrix image always, and it preserves the norm form itself on the rotor slice; on the material sector it preserves the sign and the vanishing of the norm form of a four-vector, which is what the causal classification needs. These two invariants cut the elements into the classes the physics articles use.

| class | norm form $N(\tilde{X})$ | physical reading |
|---|---|---|
| timelike | $N < 0$, in the corpus's sign convention for $ict\,e_0 + \mathbf{x}$ | a world line of a massive particle |
| null | $N = 0$, $\tilde{X}\neq 0$ | a point of the light cone, a zero divisor of rank one |
| spacelike | $N > 0$ | a separation outside the cone |
| zero | $\tilde{X} = 0$ | the origin |

### The Mass Shell and the Light Cone as Single Orbits

Two of the classes are single orbits of the Lorentz action, and the statement is the operator form of a familiar one. The non-zero null elements of $\mathbb{M}_-$ are all conjugate under rotor conjugation, which is the statement that the light cone is one geometric object and not a union of cones attached to individual points; and the timelike elements of a fixed norm form are all conjugate, which is the mass shell statement that every four-velocity of a given mass is carried to every other by a Lorentz transformation. A general rotor of $SL(2,\mathbb{C})$ acting on the rest four-velocity $i\,mc\,e_0$ gives

$$
\tilde{\Lambda}\,(imc\,e_0)\,\tilde{\Lambda}^\dagger ,
$$

of norm form $N = -m^2c^2$, which is the four-velocity of a massive particle of mass $m$: the orbit of the rest four-velocity is the mass shell. The invariance of $N$ under the action is exactly the on-shell condition, and the reason the mass shell is a single orbit rather than a family of orbits parametrised by direction is that the rotors act transitively on the timelike elements of a fixed norm form.

### The Rank and the Zero Divisors

The rank-one stratum of the algebra is the set of non-zero elements with $N = 0$, and the corpus calls it the biquaternion null cone; the material-sector part of it is the light cone. Both actions preserve the rank, so no operator can move an element off the cone into an element that is not a zero divisor, and the whole cone is a single orbit of the Lorentz action. The identification of the light cone with the zero-divisor cone, and the use of that identification in the causal structure of the framework, are the subject of *The Light Cone as the Biquaternion Zero-Divisor Cone*.

## Ordering and the Wigner Rotor

### Composition of Operators

**Proposition.** $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}} = \operatorname{H}_{\tilde{Q}\tilde{R}}$.

**Proof.** $\tilde{Q}(\tilde{R}x\tilde{R}^\dagger)\tilde{Q}^\dagger = (\tilde{Q}\tilde{R})x(\tilde{Q}\tilde{R})^\dagger$. $\square$

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

The operator sees the boost and the rotor of the element, in that order, and it sees the scale only as the single dilation $r^4$ of the interval; the phase it does not see at all, which is the kernel statement of the third section. Stated in the language of the polar articles: the polar representation exhibits four factors because one element carries them, and the operator carries the same four with the phase lost and the scale collapsed into the dilation of the interval. The two articles are companions, and each is the other's explanation of a factor count.

## Worked Examples

### A Boost Rotor Acting on a Four-Position

Let $\beta = 0.6$ along $e_3$, so that $\psi = \operatorname{artanh}0.6$, $\cosh\frac{\psi}{2} = 1.060660172$ and $\sinh\frac{\psi}{2} = 0.353553391$, and let $\tilde{X} = ict\,e_0 + 0.6ct\,e_3$ with $ct = 1$. Then

$$
\tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger = i\tau e_0 , \qquad \tau = \sqrt{1-0.36} = 0.8 ,
$$

so that $ct' = 0.8$ and $z' = 2.8\times10^{-17}$, the residual of a zero. The example is the corpus's own numerical check of the boost rotor, and it exhibits the action as the statement that the four-position of a moving particle is carried to its rest frame.

### A Rotation Rotor Acting on a Four-Vector

Let $\tilde{R} = \cos\frac{\pi}{6} + \sin\frac{\pi}{6}e_3$, of angle $\theta = \pi/3$, and let $\tilde{X} = 2ie_0 + e_1 + 0.5e_3$. Then

$$
\tilde{R}\,\tilde{X}\,\tilde{R}^\dagger = 2ie_0 + 0.5e_1 + 0.866025404e_2 + 0.5e_3 ,
$$

so the temporal and $e_3$ components are untouched and the spatial part is rotated through $\pi/3$ in the $(e_1,e_2)$ plane: the values are $\cos\frac{\pi}{3} = 0.5$ and $\sin\frac{\pi}{3} = 0.866025404$. The norm form is unchanged, $N = -4 + 1 + 0.25 = -2.75$ before and after.

### A Boost Rotor Acting on a Null Four-Vector

With $\tilde{\Lambda} = \frac53e_0 + \frac43ie_3$, of norm form $N = \frac{25}{9} - \frac{16}{9} = 1$ and hence of rapidity $\psi = 2\ln 3$, for which $\beta = \tanh\psi = \frac{40}{41}$, and with the null four-vector $\tilde{X} = ie_0 + e_1$, the sandwich gives

$$
\operatorname{H}_{\tilde{\Lambda}}(\tilde{X}) = \frac{41}{9}ie_0 + e_1 - \frac{40}{9}e_3 ,
\qquad
\frac{41}{9} = \cosh\psi , \quad \frac{40}{9} = \sinh\psi .
$$

The image is anti-Hermitian, so it is again a four-vector, as the sector proposition requires; its norm form is $-\frac{1681}{81} + 1 + \frac{1600}{81} = 0$, so the null vector is still null, as the invariance of the cone requires; and the spatial direction $e_1$, transverse to the boost, is untouched. The numerical values are $\frac{41}{9} = 4.5555\ldots$ and $\frac{40}{9} = 4.4444\ldots$. The example is the boost of the corpus's normalisation with $\beta = \frac{40}{41}$, applied to a lightlike four-vector.

### The Wigner Angle

For the two boosts of rapidities $0.7$ and $0.9$ about orthogonal axes, the polar decomposition of the product gives a rotor of angle $0.281950221701$ rad, and

$$
\cos\theta_W = \frac{\cosh 0.7 + \cosh 0.9}{1+\cosh0.7\cosh0.9} = \frac{1.255169006 + 1.433086385}{1 + 1.798800804} = 0.960514656 ,
$$

which gives the same angle. The angle vanishes when either rapidity vanishes and when the two axes are collinear, both of which are immediate from the closed form, and it is largest for two boosts of comparable rapidity about orthogonal axes.

### The Double Cover

Let $\tilde{R}$ be any rotation rotor and consider $-\tilde{R}$. Since $-\tilde{R}$ is a central multiple of $\tilde{R}$, and a central multiple scales the sandwich by the squared modulus of its complex factor, $\operatorname{H}_{-\tilde{R}} = \operatorname{H}_{\tilde{R}}$, while $-\tilde{R}\neq\tilde{R}$ as algebra elements. The two rotors therefore represent the same operator and are not the same physical element, which is the statement that the rotation group has a two-fold cover by the rotors. On the material sector the same computation is the standard double cover of the Lorentz group, and the article's kernel statement for the whole algebra is its refinement.

## Summary

An element of the biquaternion algebra acts on the algebra by the sandwich

$$
\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}\,x\,\tilde{Q}^\dagger ,
$$

and the sandwich is the Lorentz action of the series written on the whole algebra. Among the two-sided sandwiches it is the only form that preserves the two sectors, and that is why no other form is used.

It **preserves the two sectors and no other of the six subspaces**, it scales the norm form by $|N(\tilde{Q})|^2$, and on the unit-norm slice it is the action of $SL(2,\mathbb{C})$, with kernel $\{\pm e_0\}$ on the material sector and the central circle on the whole algebra, so that it is blind to the central phase and to nothing else. It carries a four-position to its rest frame, and the mass shell and the light cone are single orbits of it.

The **rotation** form of the sandwich doubles the half-angle of its rotor, preserves all six subspaces, and preserves the product of two elements of the algebra; the **boost** form does not double, and it preserves the interval in place of the product. The two cases are one criterion: the sandwich preserves the product exactly when the acting element is unitary, which is exactly when it fixes the time axis. A boost carries the time axis to the four-velocity of the moving frame, and it is that motion, and not any failure of the formalism, that the relativity of simultaneity expresses.

The operators compose as their elements do, $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}} = \operatorname{H}_{\tilde{Q}\tilde{R}}$, so the composite of two boost operators is a boost followed by a rotation — the Wigner rotation — and the closed form of the Wigner angle is the rotor factor of a product of two rotors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $8$-dimensional over $\mathbb{R}$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | the norm form, the determinant of the matrix image |
| $\tilde{\Lambda}$, $N(\tilde{\Lambda}) = 1$ | a Lorentz rotor, $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ |
| $\hat{q}$ | a unit real quaternion, the rotation rotor |
| $B = \sqrt{\tilde{Q}\tilde{Q}^\dagger}$ | the boost factor, Hermitian positive of unit norm form |
| $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^\dagger$ | the sandwich, the Lorentz action of the series |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and antiquaternion subspaces |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the informational and material sectors |
| $\hat{\mathbf{n}}$, $\theta$ | the axis and angle of a rotation rotor, $R = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$ |
| $\hat{\mathbf{u}}$, $\psi$ | the axis and rapidity of a boost rotor, $\Lambda = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, $\tanh\psi = u/c$ |
| $\theta_W$ | the Wigner angle of two successive boosts |

## Further Reading

- *The Polar Representation of Biquaternions* (`articles_physics/the-polar-representation-of-biquaternions.md`), for the four factors of one element
- *The Polar Representation in Subspaces* (`articles_physics/the-polar-representation-in-subspaces.md`), immediately before the present article in the menu, for the four factors read in the six subspaces
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), for the six subspaces, their intersections and the invariant subspace structure the operators act on
- *The Lorentz Group as Biquaternion Norm-Form Automorphisms* (`articles_physics/the-lorentz-group-as-biquaternion-norm-form-automorphisms.md`), for rotor conjugation as a homomorphism with kernel $\{\pm e_0\}$ on the material sector
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the boosts, the rotations and the group structure of the rotors
- *The Lorentz Transformation as a Biquaternionic Rotation* (`articles_physics/the-lorentz-transformation-as-a-biquaternionic-rotation.md`), for the component formulas of a boost and the relation between a rotor and a four-velocity
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the sector that the sandwich preserves
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`), for the sector that carries the four-vectors
- *The Light Cone as the Biquaternion Zero-Divisor Cone* (`articles_physics/the-light-cone-as-the-biquaternion-zero-divisor-cone.md`), for the null orbit and the rank-one stratum
- *Thomas Precession as a Biquaternion Rotor Effect* (`articles_physics/thomas-precession-as-a-biquaternion-rotor-effect.md`), for the Wigner rotor in kinematics
- *The Thomas Precession* (`articles_physics/exercise-the-thomas-precession.md`), for the worked exercise
- *Integer Spin Quantization and the Adjoint Action on the Material Sector* (`articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.md`), for the adjoint action and its use in quantization
- *The 2×2 Matrix Representation of Biquaternions* (`articles_physics/the-2x2-matrix-representation-of-biquaternions.md`), for the matrix image of the sandwich as a similarity
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the conventions used throughout
- *Introduction to the Biquaternion Universe* (`articles_physics/introduction-to-the-biquaternion-universe.md`), for the map of the series
- *Biquaternion Operator Representation* (`articles_maths/biquaternion-operator-representation.md`), the companion article, for the same sandwich treated algebraically
