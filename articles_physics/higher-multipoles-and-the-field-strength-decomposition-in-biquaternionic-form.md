# __Higher Multipoles and the Field-Strength Decomposition in Biquaternionic Form__

## Introduction

The field of any bounded source is a superposition of multipoles. Order by order, the field is decomposed into the contributions of a total charge, a dipole, a quadrupole, and so on, and the order $l$ labels an irreducible representation $D^{(l)}$ of the rotation group acting on the field's angular dependence. The field-strength biquaternion $\tilde{F}$ carries the same field in the algebra, and it admits two decompositions that the multipole series has to be read against: the **Hermitian decomposition** into its electric and magnetic halves, and the **self-dual decomposition** into its two chiralities. The purpose of this article is to put the multipole tower and those two decompositions side by side and to show how they fit.

The result is a clean division of labour and a sharp compatibility statement, and it is worth stating at the outset.

- The **multipole series** is a decomposition of the **function space**. The field at each point is a biquaternion value, but the order $l$ is a property of the field's angular map, and the tower lives in the infinite-dimensional space of functions on the sphere, $L^2(S^2) = \bigoplus_{l\ge0}D^{(l)}$. The value algebra is finite, $\mathbb{B} = D^{(0)}\oplus D^{(1)}$, and it carries the monopole and the dipole and no higher order.

- The **Hermitian decomposition** of $\tilde{F}$ separates the electric and magnetic **fields**: the electric part is the Hermitian summand $\mathbb{M}_+$ and the magnetic part the anti-Hermitian summand $\mathbb{M}_-$. It is a decomposition of the field components, and it is not the same distinction as the electric and magnetic **multipole types**. For a static source the two agree — a static charge distribution gives a Hermitian field strength and a stationary current an anti-Hermitian one — but a radiating multipole of either type has both a Hermitian and an anti-Hermitian part.

- The **self-dual decomposition** is the split into the two chiralities and is the Lorentz-covariant one. For radiation the two halves are the two helicities of the field, and a circularly polarised multipole of definite helicity lies entirely in one half. The electric and magnetic multipole types are the parity-even and parity-odd combinations of the two helicities; since a boost does not preserve parity, it mixes the two types while it preserves the chiralities.

The two decompositions are independent — they are different splittings of the same six real field components — and the multipole series is compatible with both. The article works this out, order by order, and records what belongs to the algebra and what is imported from the standard theory of multipole radiation.

The conventions are those of the companion articles:

- Companion article *Introduction to the Biquaternion Universe*, for the algebra and its two sectors.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the four-vectors and the material sector.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian sector.
- Companion article *Conventions in the Biquaternion Universe*, for the metric at its three levels, the d'Alembertian, and the conventions of presentation.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the potential and field-strength biquaternions.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for $\tilde{F}$, the Riemann–Silberstein vector, the self-dual decomposition, and the invariants.
- Companion article *Radiation from Accelerated Charges in Biquaternionic Form*, for the retarded solution and the radiation field.
- Companion article *The Spinor Representation of the Lorentz Group in Biquaternionic Form*, for the two complex three-dimensional representations of the Lorentz group.

Throughout, $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$; the central scalar imaginary is $i$, $i^2 = -1$; the material sector is $\mathbb{M}_-$, the informational sector $\mathbb{M}_+$, and the center is $\mathbb{C}_{\mathbb{B}}$; the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + \boldsymbol{\nabla}$, with $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$; and the speed of light is $c = 1/\sqrt{\epsilon\mu}$. The irreducible rotation representation of dimension $2l+1$ is $D^{(l)}$; the electric and magnetic multipoles of order $l$ are written $E_l$ and $M_l$.

## The Multipole Series of a Localised Source

### The Expansion in Spherical Harmonics

Let a bounded source radiate at a single frequency. Outside the source the field satisfies the source-free equations, and the scalar potentials that generate it are expanded in spherical harmonics with radial functions that solve Bessel's equation. The angular dependence of the field is therefore the direct sum

$$
L^2(S^2) = \bigoplus_{l=0}^{\infty} D^{(l)} ,
\qquad
\dim_{\mathbb{C}} D^{(l)} = 2l+1 ,
$$

each $D^{(l)}$ appearing once. The coefficients of the expansion are the **multipole moments**, functionals of the source:

$$
q_{lm} = \int \rho(\mathbf{x}')\,r'^{\,l}\,Y_l^{m*}(\hat{\mathbf{x}}')\,d^3x' ,
$$

the electric moments, together with the magnetic moments built from the current. The potential of the source at a field point outside it is a sum of two radial behaviours for each $l$: the irregular solution, which is the near-zone multipole field of the source, and the outgoing spherical wave, which is its radiation. The angular order $l$ is common to both; the multipole order is a property of the angular map, and the near-to-far transition is a property of the radial function. This is the standard multipole expansion and is transcribed rather than re-derived.

For radiation the cleanest bookkeeping is through the **radiation vector** of the electromagnetic series,

$$
\mathbf{F}(\hat{\mathbf{n}}) = \int \mathbf{J}(\mathbf{x}')\,e^{-ik\hat{\mathbf{n}}\cdot\mathbf{x}'}\,d^3x' ,
\qquad
k = \frac{\omega}{c} ,
$$

whose expansion in powers of $k\hat{\mathbf{n}}\cdot\mathbf{x}'$ is the multipole series in the long-wavelength limit. The term of order $k^n$ contributes the two types of multipole of neighbouring orders,

$$
k^0:\ E_1 ,
\qquad
k^1:\ M_1,\ E_2 ,
\qquad
k^2:\ M_2,\ E_3 ,
\qquad
\ldots
\qquad
k^n:\ M_n,\ E_{n+1} .
$$

The pairing is worth holding on to: at each order in $k$ the field carries an electric multipole of order $l$ and a magnetic multipole of order $l-1$. The electric quadrupole and the magnetic dipole are partners at order $k$, the electric octupole and the magnetic quadrupole at order $k^2$, and so on. The electric dipole stands alone at order $k^0$, because there is no magnetic monopole.

### The Vector Spherical Harmonics

On the sphere the two transverse families that carry the radiation are the **vector spherical harmonics**

$$
\mathbf{X}_{lm} = \frac{1}{\sqrt{l(l+1)}}\,\mathbf{L}\,Y_{lm} ,
\qquad
\mathbf{L} = -i\,\mathbf{r}\times\boldsymbol{\nabla} ,
$$

which are tangential, $\mathbf{X}_{lm}\cdot\hat{\mathbf{r}} = 0$, together with their rotated partners $\hat{\mathbf{r}}\times\mathbf{X}_{lm}$ and the radial family $\hat{\mathbf{r}}Y_{lm}$. Any vector field on the sphere decomposes into these three families; the radiation field is transverse, so its radial family is absent, and it is a sum of the two tangential families. One family is the **electric** $l$-pole and the other the **magnetic** $l$-pole. In the common convention the magnetic $l$-pole has its magnetic field along $\mathbf{X}_{lm}$ and its electric field along $\hat{\mathbf{r}}\times\mathbf{X}_{lm}$, and the electric $l$-pole interchanges the two. The two families carry opposite parity: an electric $l$-pole has parity $(-1)^l$ and a magnetic $l$-pole parity $(-1)^{l+1}$. This is standard vector-harmonic analysis, and it is cited as standard.

### The Multipole Fields and Their Angular Momentum

The far field of an electric $l$-pole and of a magnetic $l$-pole each falls off as $r^{-1}$ and has the angular structure of degree $l$; both carry a definite total angular momentum. A multipole of order $l$ radiates quanta of $j = l$, with the multipole moment transforming as an irreducible tensor operator of rank $l$. The angular momentum is shared between the multipole order and the vector character of the field: the field strength is a vector, a spin-one object, and one of the $l$ units of an $l$-pole quantum reflects the vector character of the field in which the multipole is written. This is the sense in which the whole multipole series above the monopole belongs to the sector of **spin-one-and-above origin**: the electric dipole is rank one, the quadrupole rank two, and each order $l$ is built from $l$ spin-one vector ingredients.

The radiated power of an $l$-pole has the characteristic high-frequency behaviour

$$
P_{E_l},\ P_{M_l} \ \propto\ \omega^{2l+2} ,
$$

so that each successive order is suppressed by two further powers of $\omega$ relative to the electric dipole. Together with the pairing $E_{l+1}\leftrightarrow M_l$ at order $k^l$, this is the standard long-wavelength taxonomy of multipole radiation.

## The Field-Strength Biquaternion and Its Two Decompositions

### The Field Strength as a Value of the Algebra

The field strength in a medium is the pure-vector biquaternion

$$
\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H} ,
\qquad
\mathbf{H} = \frac{\mathbf{B}}{\mu} ,
$$

with vanishing scalar part. It is an element of the vector part of $\mathbb{B}$, which is three complex dimensions, six real dimensions, and it carries the six real field components of $(\mathbf{E},\mathbf{B})$. Its two pieces are the electric piece, which is imaginary and lies in the Hermitian sector $\mathbb{M}_+$, and the magnetic piece, which is real and lies in the anti-Hermitian sector $\mathbb{M}_-$:

$$
i\sqrt{\epsilon}\,\mathbf{E} \in \mathbb{M}_+ ,
\qquad
-\sqrt{\mu}\,\mathbf{H} \in \mathbb{M}_- ,
\qquad
\mathbb{M}_+ \cap \mathbb{M}_- = \{0\} .
$$

This is the first of the two decompositions, and it is the algebraic form of the distinction between the two fields.

### The Hermitian Decomposition

The split into electric and magnetic pieces is the projection onto the two real subspaces by the Hermitian conjugate,

$$
\tfrac{1}{2}\left(\tilde{F} + \tilde{F}^\dagger\right) = i\sqrt{\epsilon}\,\mathbf{E} ,
\qquad
\tfrac{1}{2}\left(\tilde{F} - \tilde{F}^\dagger\right) = -\sqrt{\mu}\,\mathbf{H} ,
$$

with $\tilde{F}^\dagger = i\sqrt{\epsilon}\,\mathbf{E} + \sqrt{\mu}\,\mathbf{H}$. The Hermitian conjugate is thus the algebraic operation that separates the two fields. The decomposition is **not** Lorentz-covariant: a boost mixes the two summands, because it mixes $\mathbf{E}$ and $\mathbf{B}$. It is, however, rotation-covariant: a spatial rotation acts on $\mathbf{E}$ and $\mathbf{H}$ separately, so the split survives the rotation subgroup.

### The Self-Dual Decomposition

The second decomposition is by the Hodge dual. With the duality operation defined by its action on the fields,

$$
\star:\ (\mathbf{E},\mathbf{B})\ \longmapsto\ \left(c\,\mathbf{B},\ -\frac{\mathbf{E}}{c}\right) ,
\qquad
\star^2 = -1 ,
$$

the two combinations of opposite chirality are built from the **Riemann–Silberstein vector** and its conjugate,

$$
\mathbf{V} = \mathbf{E} + ic\,\mathbf{B} ,
\qquad
\mathbf{V}^* = \mathbf{E} - ic\,\mathbf{B} ,
$$

on which the dual acts by a phase,

$$
\star\mathbf{V} = -i\,\mathbf{V} ,
\qquad
\star\mathbf{V}^* = +i\,\mathbf{V}^* .
$$

The self-dual combination $F + i\star F$ corresponds to $2\mathbf{V}$ and the anti-self-dual combination $F - i\star F$ corresponds to $2\mathbf{V}^*$. For the real physical field the two chiralities are the field strength and its dagger,

$$
\tilde{F} = i\sqrt{\epsilon}\,\mathbf{V} ,
\qquad
\tilde{F}^\dagger = i\sqrt{\epsilon}\,\mathbf{V}^* ,
$$

so that the self-dual half is the field strength itself and the anti-self-dual half is obtained from it by the dagger. The identity uses $\tilde{F}^\dagger = -\tilde{F}^* = i\sqrt{\epsilon}\,\mathbf{E}+\sqrt{\mu}\,\mathbf{H}$ together with $\sqrt{\mu}\,\mathbf{H} = \sqrt{\epsilon}\,c\,\mathbf{B}$, so it holds for the real field; on the **complexified** field space the two halves are the independent projections of $F$ and the dagger is no longer the operation that produces the second from the first. For a real field, $\mathbf{V}^* = \overline{\mathbf{V}}$: the two chiralities are complex conjugates and carry the same six real components, so either alone encodes the whole field. On the complexified field space they are independent, and it is there that the decomposition is a genuine splitting; on the real field space it is the statement that the field is encoded by a single complex vector, its Riemann–Silberstein vector.

### The Relation of the Two Decompositions

The two decompositions are different, and it is their difference that organises the multipole series.

- The **Hermitian** split is a decomposition over the **real** field space: it separates the two real three-dimensional subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$, it is rotation-covariant, and it is not boost-covariant.
- The **self-dual** split is a decomposition over the **complexified** field space: it separates the two complex three-dimensional eigenspaces of $\star$, it is boost-covariant (in fact Lorentz-covariant), and it is not the same splitting as the first.

The two ways of cutting the same six dimensions are related by the definition $\mathbf{V} = \mathbf{E} + ic\mathbf{B}$, so that the electric and magnetic fields are recovered as

$$
\mathbf{E} = \frac{\mathbf{V} + \mathbf{V}^*}{2} = \frac{\mathbf{V} + \overline{\mathbf{V}}}{2} ,
\qquad
\mathbf{B} = \frac{\mathbf{V} - \mathbf{V}^*}{2ic} = \frac{\mathbf{V} - \overline{\mathbf{V}}}{2ic}
$$

for a real field. Each decomposition is a covariant splitting in its own category — rotations for the first, Lorentz transformations for the second — and the multipole series is expressed most economically in the second.

The invariants sit naturally in the self-dual vector. The two field invariants are the real and imaginary parts of $\mathbf{V}\cdot\mathbf{V}$,

$$
\mathbf{V}\cdot\mathbf{V} = \left(\mathbf{E}^2 - c^2\mathbf{B}^2\right) + 2ic\,\mathbf{E}\cdot\mathbf{B} = I_1 + 2ic\,I_2 ,
$$

and the norm form of the field-strength biquaternion vanishes exactly when the Riemann–Silberstein vector is null, which is the condition for a radiation field.

## The Multipole Tower and the Two Decompositions

### The Function Space and the Value Algebra

The multipole order $l$ lives in the function space, and this is the first thing to keep straight. The field is a biquaternion-valued function, $\tilde{F}:\mathbb{R}^{3,1}\to\mathbb{B}$, and its angular content is a decomposition of the space of functions on the sphere, $L^2(S^2) = \bigoplus_l D^{(l)}$. The value algebra is much smaller:

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}) = D^{(0)}\oplus D^{(1)} ,
\qquad
\dim_{\mathbb{C}}\mathbb{B} = 4 .
$$

A four-dimensional rotation module cannot contain a $D^{(l)}$ with $l\ge2$: the smallest such representation has dimension five. The multipole moments are functionals of the source, not elements of the value algebra, and the tower is infinite because the function space is infinite-dimensional while the value space is not. The two spaces are of different dimensions and do different jobs: the algebra is the **value space** of the field, and the function space is its **angular content**. There is no contradiction in an infinite tower of multipole orders being carried by an algebra-valued field whose algebra is four-dimensional.

### Where the Electric and Magnetic Multiplets Sit

At each order $l\ge1$ the field carries two multiplet types, an electric one and a magnetic one, and the two decompositions of $\tilde{F}$ relate to them in different ways.

**The multipole types and the Hermitian decomposition.** The electric and magnetic multipole types are distinguished by **parity**: an electric $l$-pole has parity $(-1)^l$ and a magnetic $l$-pole parity $(-1)^{l+1}$, and in the vector-spherical-harmonic basis the magnetic family is $\mathbf{X}_{lm}$ and the electric family $\hat{\mathbf{r}}\times\mathbf{X}_{lm}$. This is *not* the Hermitian split of the field strength. The Hermitian split separates the electric **field** from the magnetic **field**, $\tfrac{1}{2}(\tilde{F}+\tilde{F}^\dagger) = i\sqrt{\epsilon}\mathbf{E}$ and $\tfrac{1}{2}(\tilde{F}-\tilde{F}^\dagger) = -\sqrt{\mu}\mathbf{H}$, and a radiating multipole of either type has both an electric and a magnetic field. The two distinctions coincide only in the static limit: a static charge distribution has $\mathbf{B} = 0$, so its multipole fields are purely Hermitian, and a stationary current has $\mathbf{E} = 0$, so its multipole fields are purely anti-Hermitian. In that limit, and only there, the electric multipoles $E_l$ are Hermitian fields and the magnetic multipoles $M_l$ anti-Hermitian ones.

**The multipole types and the self-dual decomposition.** In the radiation field the two chiral halves are the two **helicities**. For each order $l$ the self-dual part carries one circular polarisation and the anti-self-dual part the other, and the electric and magnetic multiplet types are the parity-even and parity-odd combinations of the two helicity amplitudes, related to them by the same linear transformation that relates linear to circular polarisation. The reason is that parity exchanges the two chiral halves. Spatial inversion acts on the fields by $\mathbf{E}\mapsto-\mathbf{E}$ and $\mathbf{B}\mapsto\mathbf{B}$, so on the Riemann–Silberstein vector it acts as

$$
\mathbf{V}\ \longmapsto\ -\mathbf{V}^* ,
$$

and therefore

$$
\mathbf{V}+\mathbf{V}^*\ \longmapsto\ -\left(\mathbf{V}+\mathbf{V}^*\right) ,
\qquad
\mathbf{V}-\mathbf{V}^*\ \longmapsto\ +\left(\mathbf{V}-\mathbf{V}^*\right) .
$$

A single chirality is therefore exchanged with the other and has no definite parity, and only a combination of the two has one. Those combinations are the electric and magnetic multipole types: the electric $l$-pole has parity $(-1)^l$ and the magnetic $l$-pole parity $(-1)^{l+1}$, so the correspondence between the two combinations and the two types is fixed only together with the order, the angular part contributing a factor $(-1)^l$ on top of the vector character computed above. The pointwise combinations $\mathbf{V}\pm\mathbf{V}^*$ are the parity eigenstates of the **field components** — the polar $\mathbf{E}$ and the axial $\mathbf{B}$ — and this is not the same as the electric/magnetic multipole distinction, for the same reason as before: a static electric quadrupole has $\mathbf{B} = 0$, so it lies entirely in one pointwise combination, yet its multipole type is a single parity class of order two. The self-dual split is the Lorentz-covariant one; the electric and magnetic types are not separately covariant, because a boost does not preserve parity and therefore rotates the two types into one another while leaving the two helicities alone.

**Compatibility with the function space.** The two decompositions act on the value algebra — into its two real sectors, and into its two complex chiral eigenspaces — while the order $l$ labels the angular content in a fixed frame. The two are of different kinds, and one of them is frame-dependent. The rotation subgroup preserves the order and acts on the electric and magnetic multiplets of an order independently; a boost does not preserve the order, because it transforms the argument of the field as well as its value, so a pure $l$-pole of one frame carries other orders in another. The two decompositions of the value thus act within the angular decomposition of a given frame, and the covariant statement is carried by the field strength and its chiral halves rather than by the tower.

### The Radiation Field

For radiation the two decompositions meet a third property. In the far zone the field is transverse and balanced, $\mathbf{E}\cdot\mathbf{B} = 0$ and $\mathbf{E}^2 = c^2\mathbf{B}^2$, so both invariants vanish and

$$
\mathbf{V}\cdot\mathbf{V} = 0 ,
\qquad
N(\tilde{F}) = \tilde{F}\bar{\tilde{F}} = 0 .
$$

The field-strength biquaternion of a radiation field is a **zero divisor**: a radiation field is null, whether it is an electric or a magnetic multipole, and the null property is shared by the whole far-zone tower.

A further simplification occurs for definite helicity. With the corpus's $e^{-i\omega t}$ convention, for which a positive-frequency plane wave has $\mathbf{B} = \hat{\mathbf{n}}\times\mathbf{E}/c$, a circularly polarised wave of one handedness satisfies $\mathbf{B} = -i\,\mathbf{E}/c$ as a complex amplitude and the other handedness satisfies $\mathbf{B} = +i\,\mathbf{E}/c$. For the first,

$$
\mathbf{V}^* = \mathbf{E} - ic\,\mathbf{B} = 0 ,
$$

and the field is purely self-dual; the opposite helicity gives $\mathbf{V} = 0$ and a purely anti-self-dual field. A circularly polarised $l$-pole of definite helicity therefore sits entirely in one chiral half, described by a single null complex vector. The helicity is the $\star$-eigenvalue, and the two chiral halves of the field strength are the two helicities of the radiation.

## Covariance of the Decomposition

### How the Two Halves Transform

Under a Lorentz boost with biquaternion $\tilde{\Lambda}\in\mathbb{M}_+$ the field strength transforms in the bivector representation,

$$
\tilde{F}' = \bar{\tilde{\Lambda}}\,\tilde{F}\,\tilde{\Lambda} ,
$$

and the two chiralities transform independently. In terms of the Riemann–Silberstein vector, the boost is a complex rotation

$$
\mathbf{V}' = \Lambda\,\mathbf{V} ,
\qquad
\mathbf{V}^{*\prime} = \Lambda^{*}\,\mathbf{V}^* ,
\qquad
\Lambda \in SO(3,\mathbb{C}) ,
$$

with $\Lambda$ a complex orthogonal matrix of unit determinant, $\Lambda^{\mathsf{T}}\Lambda = I_3$, $\det\Lambda = 1$. The matrices for the two chiralities are complex conjugates of one another, so on the complexified field space the two halves rotate independently and do not mix; this is the statement that the self-dual and anti-self-dual combinations transform in the two complex three-dimensional representations of the Lorentz group, the two chiralities. The verification is direct: a boost of a vector with $\mathbf{V}^* = 0$ keeps $\mathbf{V}^{*\prime} = 0$, and a boost of a vector with $\mathbf{V} = 0$ keeps $\mathbf{V}' = 0$, so each eigenspace of $\star$ is preserved.

The Hermitian decomposition, by contrast, is not preserved. A boost with velocity $\mathbf{v}$ gives

$$
\mathbf{E}' = \gamma\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right) - \frac{\gamma-1}{v^2}\left(\mathbf{v}\cdot\mathbf{E}\right)\mathbf{v} ,
\qquad
\mathbf{B}' = \gamma\left(\mathbf{B} - \frac{1}{c^2}\,\mathbf{v}\times\mathbf{E}\right) - \frac{\gamma-1}{v^2}\left(\mathbf{v}\cdot\mathbf{B}\right)\mathbf{v} ,
$$

with $\gamma = (1-v^2/c^2)^{-1/2}$, so a purely electric field acquires a magnetic part and vice versa. This is the algebraic content of the statement that the two summands $\mathbb{M}_+$ and $\mathbb{M}_-$ are not separately Lorentz-covariant.

### The Mixing of the Electric and Magnetic Multiplets

The consequence for the multipole series is that a boost mixes the electric and magnetic multiplets: $E_l$ into $M_l$ and back. The two types are parity classes — an electric $l$-pole has parity $(-1)^l$ and a magnetic $l$-pole parity $(-1)^{l+1}$ — and a boost does not preserve parity, so it rotates one into the other.

For the dipole the mixing is classical. A charge distribution translating with velocity $\mathbf{v}$ has current $\mathbf{J} = \rho\mathbf{v}$, so its magnetic dipole moment is

$$
\mathbf{m} = \frac{1}{2}\int\mathbf{x}'\times\mathbf{J}\,d^3x' = \frac{1}{2}\,\mathbf{p}\times\mathbf{v} ,
$$

the magnetic dipole generated from the electric dipole by the motion. For the quadrupole the same structure holds: a translating electric quadrupole carries a magnetic quadrupole moment. With a rest-frame planar quadrupole built from charges $+q$ at $(\pm a,0,0)$ and $-q$ at $(0,\pm a,0)$, whose only non-vanishing second moments are $D'_{xx} = 2qa^2$ and $D'_{yy} = -2qa^2$, the boost leaves $D_{xx}$ and $D_{yy}$ unchanged — they are transverse to a boost along $z$ — while the magnetic quadrupole built from the traceless part of $\int\rho\,x_i(\mathbf{x}\times\mathbf{v})_j$ acquires a non-vanishing component proportional to $(D_{xx}-D_{yy})v$, and therefore to the electric quadrupole moment times the velocity. The electric quadrupole and the magnetic quadrupole are tied together by the boost, exactly as the electric and magnetic dipoles are.

At the level of the field the mixing of the two multipole types is a consequence of the boost's mixing of the electric and magnetic **fields**, that is, of the non-invariance of the Hermitian split. This is consistent with the parity bookkeeping: the electric multipole type is parity-even or parity-odd according to $l$, the magnetic type has the opposite parity, and a boost does not preserve parity. The covariant packaging of the moments is the standard covariant multipole tensor, and on the field side the covariant object is the self-dual field strength; in both cases the electric and magnetic labels are frame-dependent.

### The Order Is Not a Lorentz Invariant

The rotation subgroup preserves the angular decomposition. A rotation acts on the field components by a position-independent matrix and leaves the time slice fixed, so it maps a multiplet of order $l$ into itself and acts on the electric and magnetic multiplets of that order separately. A boost is different. It too acts on the field components with position-independent coefficients, but it also transforms the argument of the field, so the field is read on another time slice and at an aberrated direction, and the angular decomposition changes with it. A pure multipole of one frame therefore carries other orders in another.

The quadrupole is its own illustration. Its rest-frame potential is the degree-two solid harmonic $\Phi \propto (3z^2-r^2)/r^5$, and a boost along $z$ gives, on the sphere $r'=1$,

$$
\Phi'(\mathbf{x}')\big|_{r'=1}\ \propto\ \frac{(2\gamma^2+1)u^2-1}{\left(1+(\gamma^2-1)u^2\right)^{5/2}} ,
\qquad
u = \cos\theta' ,
$$

which is no longer a polynomial of degree two in $u$: its angular content is $l = 2,4,6,\ldots$, with the $l=2,4,6$ weights $1.13$, $0.78$ and $0.33$ at $\gamma = 1.5$. The simplest case shows the same effect: the potential of a uniformly moving point charge is not spherically symmetric but carries $l = 0,2,4,\ldots$ in the lab frame. The multipole order is thus a label of the source's rest frame, and only the rotation subgroup acts within a fixed order.

What survives is the algebra of the value. The field-strength biquaternion, its two Hermitian sectors, its two chiral halves and its invariants all transform covariantly; it is the decomposition of the field into angular orders that is frame-dependent, because it is tied to a choice of time slice and of direction.

### The Order Counting and the Two Kinds of Pairing

Two different pairings of electric and magnetic multiplets appear in the subject, and it is important not to conflate them.

- The **covariant pairing** combines the electric and magnetic moments of a given rank into the covariant multipole tensor of that rank, so that neither is separately Lorentz-covariant; a boost rotates the two types into one another. This pairing is a statement about the **source moments**, which are frame-dependent.
- The **long-wavelength pairing** pairs $E_{l+1}$ with $M_l$ at the same order in $k$ in the radiation vector, because the expansion of the phase $e^{-ik\hat{\mathbf{n}}\cdot\mathbf{x}'}$ couples the rank-$(n+1)$ symmetric moment to the rank-$n$ antisymmetric moment. This pairing is a statement about the **field** in a fixed frame.

Both are standard, and they answer different questions. The first says that the electric and magnetic moments of an order are not separately covariant; the second says which multipoles dominate at a given order in the long-wavelength expansion. The quadrupole illustrates both: it is paired with the magnetic quadrupole by covariance, and with the magnetic dipole by the order counting.

## The Lowest Orders

### $l = 0$: The Monopole Is Purely Electric

The monopole is the total charge, and it has no magnetic partner: there is no magnetic monopole. Its field is the spherically symmetric Coulomb field, it radiates nothing by charge conservation, and in the algebra it is the electric piece $i\sqrt{\epsilon}\,\mathbf{E}\in\mathbb{M}_+$ with no anti-Hermitian part. The self-dual decomposition assigns it a Riemann–Silberstein vector that is purely radial and, being non-radiating, not null. The monopole is the one multipole whose Hermitian half is the whole field.

### $l = 1$: The Electric and Magnetic Dipoles

The dipole is the first order with two multiplet types. In a static or stationary setting the electric dipole field is purely Hermitian and the magnetic dipole field purely anti-Hermitian, so the two types sit in the two sectors $\mathbb{M}_\pm$; in radiation each type has both parts. In the radiation vector they are the two lowest contributions,

$$
\mathbf{F}_{E1} = -i\omega\,\mathbf{p} ,
\qquad
\mathbf{F}_{M1} = ik\,\hat{\mathbf{n}}\times\mathbf{m} ,
$$

and the far fields are the transverse dipole patterns. The two moments combine into the antisymmetric rank-two tensor whose time–space entries are the electric dipole components and whose space–space entries are the magnetic ones; it is this six-component object, not the electric or the magnetic dipole separately, that transforms in a representation of the Lorentz group. A boost rotates $\mathbf{p}$ into $\mathbf{m}$ within this block, and the electric and magnetic dipole labels are frame-dependent.

### $l = 2$: The Electric and Magnetic Quadrupoles

The quadrupole is the first order whose moment is not an algebra element. Its electric part is the symmetric traceless tensor $Q_{ij}$, five components, and its magnetic part a rank-two structure built from the current, the magnetic quadrupole moment $M_{ij}$, also five components; they are the two $D^{(2)}$ multiplets of the order, of opposite parity. In the radiation vector the electric quadrupole appears at order $k$ with the magnetic dipole,

$$
\mathbf{F}_{E2} = -\frac{k\omega}{6}\,\mathbf{Q}(\hat{\mathbf{n}}) ,
\qquad
[\mathbf{Q}(\hat{\mathbf{n}})]_i = Q_{ij}n_j ,
$$

and the magnetic quadrupole appears at the next order with the electric octupole. Both quadrupole types radiate with power $\propto\omega^6$, both have the degree-two angular pattern, and they have opposite parity, $(-1)^2 = +1$ for the electric and $(-1)^3 = -1$ for the magnetic. In the radiation field the two types are the parity-even and parity-odd combinations of the two helicity amplitudes of the order, and a boost rotates them into one another while preserving the helicities.

The quadrupole is also where the algebra's limitation becomes explicit. The moment $Q_{ij}$ is a tensor over the vector part, not an element of $\mathbb{B}$, and the value algebra contains no $D^{(2)}$. The field it produces is nonetheless a biquaternion-valued function whose angular content is degree two; the order lives in the function space, the value in the algebra.

### The Pattern for General $l$

The pattern of the lowest orders is the pattern for all of them.

- At each order $l\ge1$ there is an electric multiplet $E_l$ and a magnetic multiplet $M_l$, each of complex dimension $2l+1$, of opposite parity.
- The electric and magnetic multipole types are the parity-even and parity-odd combinations of the two helicity amplitudes; a boost rotates the two types into one another and preserves the helicities. Their covariant packaging is the covariant multipole tensor, and the self-dual field strength is the corresponding covariant object on the field side. The order $l$ itself is a rest-frame label, not a Lorentz invariant.
- In a static or stationary setting the electric multipole field is purely Hermitian and the magnetic multipole field purely anti-Hermitian, so the two types are the two sectors $\mathbb{M}_\pm$; in radiation each type has both parts.
- In the long-wavelength expansion the electric multiplet $E_{l+1}$ is paired with the magnetic multiplet $M_l$ at order $k^l$, and both radiate with power $\propto\omega^{2l+2}$.
- For radiation the field is null, $N(\tilde{F}) = 0$, and a definite-helicity multipole lies entirely in one chiral half; the helicity is the eigenvalue of $\star$.

The tower grows without bound in the function space, while the value algebra stays four-dimensional, and the two decompositions of the value — Hermitian and self-dual — act on each order of the tower in the way described: the first separates the two fields, the second separates the two helicities.

## Summary

The multipole series of a bounded source is the decomposition of the field's angular dependence into irreducible rotation representations, $L^2(S^2) = \bigoplus_{l\ge0}D^{(l)}$, with one electric multiplet $E_l$ and one magnetic multiplet $M_l$ at each order $l\ge1$. The order $l$ is a property of the function space; the value of the field at a point is an element of the four-dimensional algebra $\mathbb{B} = D^{(0)}\oplus D^{(1)}$, which carries the monopole and the dipole and no higher order, and the multipole moments are functionals of the source rather than algebra elements.

The field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ admits two decompositions of its six-real-dimensional vector part. The **Hermitian decomposition** separates the electric and magnetic fields,

$$
\tfrac{1}{2}\left(\tilde{F}+\tilde{F}^\dagger\right) = i\sqrt{\epsilon}\,\mathbf{E}\in\mathbb{M}_+ ,
\qquad
\tfrac{1}{2}\left(\tilde{F}-\tilde{F}^\dagger\right) = -\sqrt{\mu}\,\mathbf{H}\in\mathbb{M}_- ,
$$

and is rotation-covariant but not boost-covariant. It coincides with the electric/magnetic multipole distinction only in the static limit: a static charge distribution gives a purely Hermitian field strength and a stationary current a purely anti-Hermitian one, while a radiating multipole of either type has both parts. The **self-dual decomposition** uses the Hodge dual $\star:(\mathbf{E},\mathbf{B})\mapsto(c\mathbf{B},-\mathbf{E}/c)$, $\star^2 = -1$, and the Riemann–Silberstein vector $\mathbf{V} = \mathbf{E}+ic\mathbf{B}$ with $\star\mathbf{V} = -i\mathbf{V}$; its two halves are $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{V}$ and $\tilde{F}^\dagger = i\sqrt{\epsilon}\,\mathbf{V}^*$ with $\mathbf{V}^* = \mathbf{E}-ic\mathbf{B}$. It is Lorentz-covariant, and for radiation its two halves are the two helicities, so that a circularly polarised multipole of definite helicity lies entirely in one half.

Under a boost, $\tilde{F}' = \bar{\tilde{\Lambda}}\tilde{F}\tilde{\Lambda}$, the two chiralities transform independently, $\mathbf{V}' = \Lambda\mathbf{V}$ with $\Lambda\in SO(3,\mathbb{C})$, $\Lambda^{\mathsf{T}}\Lambda = I_3$, $\det\Lambda = 1$, and $\mathbf{V}^{*\prime} = \Lambda^{*}\mathbf{V}^*$, while the Hermitian halves mix: the electric and magnetic multipole types rotate into one another, with the dipole illustration $\mathbf{m} = \tfrac{1}{2}\mathbf{p}\times\mathbf{v}$ and the quadrupole analogue, because a boost does not preserve parity. The covariant pairing combines $E_l$ and $M_l$ into the covariant multipole tensor of rank $l$; the long-wavelength pairing in the radiation vector is $E_{l+1}\leftrightarrow M_l$ at order $k^l$. The order $l$ is not a Lorentz invariant: it is a rest-frame label, since a boost transforms the argument of the field as well as its value. A radiation field is null, $N(\tilde{F}) = 0$.

The multipole series and the two decompositions act on different spaces. The decompositions split the value algebra — into its two real sectors and its two chiral halves — and they are the covariant statements; the order $l$ labels the angular decomposition in a fixed frame, and only the rotation subgroup preserves it. A boost mixes the electric and magnetic types, because it mixes the fields and does not preserve parity, and it also changes the angular decomposition, because it transforms the argument of the field. The multipole order is a rest-frame label, and the covariant packaging of the moments is the covariant multipole tensor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\dim_{\mathbb{C}} = 4$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | Center and complex vector part of $\mathbb{B}$ |
| $\tilde{\nabla} = e_0\partial_{ict}+\boldsymbol{\nabla}$ | Biquaternionic gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2+\Delta$ | d'Alembertian (series convention) |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion (pure vector) |
| $\tilde{F}^\dagger$ | Hermitian conjugate of $\tilde{F}$ |
| $\mathbf{V} = \mathbf{E}+ic\mathbf{B}$ | Riemann–Silberstein vector (self-dual) |
| $\mathbf{V}^* = \mathbf{E}-ic\mathbf{B}$ | Anti-self-dual combination, $\mathbf{V}^* = \overline{\mathbf{V}}$ for a real field |
| $\star$ | Hodge dual, $\star(\mathbf{E},\mathbf{B}) = (c\mathbf{B},-\mathbf{E}/c)$, $\star^2 = -1$ |
| $I_1, I_2$ | Field invariants, $\mathbf{V}\cdot\mathbf{V} = I_1+2icI_2$ |
| $N(\tilde{F}) = \tilde{F}\bar{\tilde{F}}$ | Norm form; $N(\tilde{F}) = 0$ for a radiation field |
| $D^{(l)}$ | Irreducible rotation representation of dimension $2l+1$ |
| $L^2(S^2) = \bigoplus_l D^{(l)}$ | Angular function space (infinite-dimensional) |
| $E_l$, $M_l$ | Electric and magnetic multiplets of order $l$ |
| $q_{lm}$ | Electric multipole moment of the source |
| $\mathbf{X}_{lm} = \mathbf{L}Y_{lm}/\sqrt{l(l+1)}$ | Vector spherical harmonic (magnetic family) |
| $\hat{\mathbf{r}}\times\mathbf{X}_{lm}$ | Electric family of vector spherical harmonics |
| $\mathbf{F}(\hat{\mathbf{n}}) = \int\mathbf{J}\,e^{-ik\hat{\mathbf{n}}\cdot\mathbf{x}'}d^3x'$ | Radiation vector |
| $k = \omega/c$ | Wavenumber |
| $\mathbf{p}$, $\mathbf{m}$ | Electric and magnetic dipole moments |
| $Q_{ij}$, $M_{ij}$ | Electric and magnetic quadrupole moments |
| $\tilde{\Lambda}\in\mathbb{M}_+$ | Boost biquaternion, $\tilde{F}' = \bar{\tilde{\Lambda}}\tilde{F}\tilde{\Lambda}$ |
| $\Lambda\in SO(3,\mathbb{C})$ | Complex rotation of the self-dual vector, $\mathbf{V}' = \Lambda\mathbf{V}$ |

## Further Reading

- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the multipole expansion, the vector spherical harmonics, and the electric and magnetic multipole radiation fields.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the multipole expansion of the retarded field and the radiation of electric and magnetic multipoles.
- S. R. de Groot and L. G. Suttorp, *Foundations of Electrodynamics* (North-Holland, 1972), for the covariant multipole expansion and the transformation of the multipole moments.
- I. Bialynicki-Birula and Z. Bialynicka-Birula, *Quantum Electrodynamics* (Pergamon, 1975), for the Riemann–Silberstein vector and the photon helicity description.
- M. E. Rose, *Elementary Theory of Angular Momentum* (Wiley, 1957), for the irreducible representations $D^{(l)}$, the vector spherical harmonics, and the selection rules.
- A. R. Edmonds, *Angular Momentum in Quantum Mechanics* (Princeton, 1957), for the classification of electric and magnetic multipole radiation by parity and angular momentum.
- W. Heitler, *The Quantum Theory of Radiation* (Oxford, 1954), for the multipole fields of a radiating source and the emission of definite helicity.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time* (Cambridge, 1984), for the self-dual and anti-self-dual decomposition of the field tensor and the two chiralities.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for $M_2(\mathbb{C})$, the biquaternion algebra, and its representation content.
