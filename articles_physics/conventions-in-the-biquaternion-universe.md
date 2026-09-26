# __Conventions in the Biquaternion Universe__

## Introduction

A framework built on a non-standard algebra, and on a non-standard choice of which part of it counts as "real", is a framework in which a reader will repeatedly find things that look wrong and are not. Two examples fix the idea. The series takes the **anti**-Hermitian subspace as the material sector, where the more familiar convention would take the Hermitian one. And the series' d'Alembertian carries a sign opposite to the one used in the article on Weyl spinors, so that two mass-term equations which look like sign errors are in fact the same equation. In both cases it is the "correction" that is the error.

This article collects the conventions of the series in one place, states each one, and gives the reason it was chosen. It is meant to be read before any other article is edited, and it has two readers in mind. The first is a reader who meets an equation in a companion article that looks wrong. The second is anyone writing or revising an article in the series, for whom the conventions are load-bearing: a change that looks local — a sign, an operator definition, a factor of $i$ — generally propagates into a dozen dependent articles.

The article is organised in two parts. The first gives the **algebraic** conventions: the algebra, its basis, its conjugations, the six subspaces, the three representations of the algebra, and the trace. The second gives the **spacetime and field-theoretic** conventions: the metric, the d'Alembertian, the convention for the Dirac mass term, and the algebra's real structure.

One warning applies throughout. **A convention recorded here is not a claim that the alternative is wrong.** Several of these choices are freely made where either choice would be defensible; they are conventions, not theorems. What is not free is *consistency*: once a convention is fixed, the dependent articles inherit it, and a change to it is a change to all of them. Where a convention is instead forced — where the alternative leads to a demonstrable contradiction — the article says so explicitly, and that distinction is the difference between a convention and a result.

## The Algebraic Conventions

### The Algebra and Its Basis

The framework is set in the **biquaternion algebra**

$$
\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H},
$$

the complexification of the quaternions. Every element is written in the basis

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

where $e_0 = 1$ and $e_1, e_2, e_3$ are the quaternion units,

$$
e_1^2 = e_2^2 = e_3^2 = -e_0, \qquad e_1e_2 = -e_2e_1 = e_3,
$$

and the four coefficients $Q_\mu$ are **complex** numbers. The scalar imaginary, denoted $i$, is the complex unit of the complexification:

$$
i^2 = -1.
$$

Everything that follows turns on how each complex coefficient is split, so the split is fixed here, at the outset. Writing every coefficient as a real part plus $i$ times a real part,

$$
Q_0 = q_0 + iq'_0, \qquad Q_1 = q_1 + iq'_1, \qquad Q_2 = q_2 + iq'_2, \qquad Q_3 = q_3 + iq'_3, \qquad q_\mu, q'_\mu \in \mathbb{R},
$$

replaces the four complex coefficients by **eight real parameters**: $q_\mu$ is the real part of $Q_\mu$, the coefficient of $e_\mu$, and $q'_\mu$ its imaginary part, the coefficient of $ie_\mu$, so the prime marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and the six subspaces below are what the eight parameters are grouped into. The full set of parametrisations, and the two conventions they embody, are in *The Six Subspaces* and *The Prime Convention* below; nothing in them changes the split stated here.

One structural fact governs the whole series, so it is worth isolating. **The scalar unit $i$ is central**: it commutes with every element of $\mathbb{B}$, because it belongs to the $\mathbb{C}$ factor of the tensor product, while the quaternion units belong to the $\mathbb{H}$ factor. Multiplication by a *central* phase $e^{i\alpha}$ therefore commutes with every operator constructed from the algebra — in particular with the biquaternionic gradient $\tilde{\nabla}$ — and this is why the central phase is the algebra's natural continuous symmetry. The articles on Noether's theorem and the gauge principle rest on it.

As a complex algebra $\mathbb{B}$ is isomorphic to the full matrix algebra,

$$
\mathbb{B} \cong M_2(\mathbb{C}),
$$

and this identification is used constantly. It is fixed by a single isomorphism, written $\Phi$; its four basis images, and the rule that neither the factor $i$ nor the sign is a free choice, are stated in *The 2×2 Matrix Representation* below, and the development of the representation — the general element, the six subspaces as matrices, the conjugations, the trace and the determinant — is in the companion article *The 2×2 Matrix Representation of Biquaternions*. Its two **minimal left ideals** are the algebra's two chiralities. They are the reason the Dirac field is carried by the spinor module rather than by the whole algebra, and the reason the mass term has the shape it has, as discussed below.

### The Conjugations and the Fixed Spaces

The algebra carries four natural involutions, all of them used in the series:

| Name | Notation | Definition |
|---|---|---|
| Quaternion conjugation | $\bar{\tilde{Q}}$ | $e_k \mapsto -e_k$, $k = 1, 2, 3$, $i$ fixed |
| Complex conjugation | $\tilde{Q}^*$ | $i \mapsto -i$, $e_k$ fixed |
| Hermitian conjugation | $\tilde{Q}^\dagger$ | $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*}$ |
| Anti-Hermitian conjugation | $\tilde{Q}^\flat$ | $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ |

Each involution has a fixed space, and each of these is a named **real** subspace of the algebra:

| involution | its fixed space | name | real dim |
|---|---|---|---|
| quaternion conjugation $\bar{\cdot}$ | $\mathbb{C}_{\mathbb{B}}$ | center subspace | $2$ |
| quaternion conjugation $\bar{\cdot}$, anti-fixed | $\mathrm{Vect}(\mathbb{B})$ | vector subspace | $6$ |
| complex conjugation ${}^{*}$ | $\mathbb{H}_{\mathbb{B}}$ | quaternion subspace | $4$ |
| complex conjugation ${}^{*}$, anti-fixed | $i\mathbb{H}_{\mathbb{B}}$ | antiquaternion subspace | $4$ |
| Hermitian conjugation $\dagger$ | $\mathbb{M}_+$ | informational subspace | $4$ |
| anti-Hermitian conjugation $\flat$ | $\mathbb{M}_-$ | material subspace | $4$ |

The vector subspace is the **anti**-fixed space of quaternion conjugation, the elements with $\bar{\tilde{Q}} = -\tilde{Q}$, and the antiquaternion subspace is the **anti**-fixed space of complex conjugation — the elements with $\tilde{Q}^* = -\tilde{Q}$. Neither is the fixed space of an involution of its own; four of the six subspaces are fixed spaces and two are anti-fixed spaces.

The table is a list of **definitions**, not of relations. How the subspaces meet, span and cross is the subject of *Relations Between Subspaces*; the parametrisation each one carries is recorded in *The Six Subspaces* below.

### The Six Subspaces

The eight real parameters of a general element group into **six subspaces**: the two-dimensional center subspace, the six-dimensional vector subspace, and four four-dimensional ones. Each is listed here under both of its names, the **algebraic** one from the property that defines it and the **physical** one from the role it plays, together with its defining condition, its basis, its own real parameters, and the physical coordinates those parameters carry.

The dictionary between the parameters and the physical coordinates is fixed once and for all,

$$
q'_0 = c\,t, \qquad (q_1, q_2, q_3) = (x, y, z), \qquad q_0 = c\,t', \qquad (q'_1, q'_2, q'_3) = (x', y', z'),
$$

with $\mathbf{x} = x e_1 + y e_2 + z e_3$ the real spatial vector and $i\mathbf{x}' = i x' e_1 + i y' e_2 + i z' e_3$ its imaginary counterpart. The **material coordinate** $\tilde{Q} = ict\,e_0 + \mathbf{x}$ and the **informational coordinate** $\tilde{Q} = ct'\,e_0 + i\mathbf{x}'$ are the two ends of it, and each subspace keeps whichever part of the dictionary its defining condition leaves free.

| subspace | physical interpretation | defining condition | basis | real parameters | physical coordinates |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (center) | complex time sector | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_0,\ ie_0$ | $q_0,\ q'_0$ | $ct',\ ict$ |
| $\mathrm{Vect}(\mathbb{B})$ (vector) | complex space sector | $\bar{\tilde{Q}} = -\tilde{Q}$ | $e_1,\ e_2,\ e_3,\ ie_1,\ ie_2,\ ie_3$ | $q_1,\ q_2,\ q_3,\ q'_1,\ q'_2,\ q'_3$ | $x,\ y,\ z,\ ix',\ iy',\ iz'$ |
| $\mathbb{H}_{\mathbb{B}}$ (quaternion) | real sector | $\tilde{Q}^* = \tilde{Q}$ | $e_0,\ e_1,\ e_2,\ e_3$ | $q_0,\ q_1,\ q_2,\ q_3$ | $ct',\ x,\ y,\ z$ |
| $i\mathbb{H}_{\mathbb{B}}$ (antiquaternion) | imaginary sector | $\tilde{Q}^* = -\tilde{Q}$ | $ie_0,\ ie_1,\ ie_2,\ ie_3$ | $q'_0,\ q'_1,\ q'_2,\ q'_3$ | $ict,\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_+$ (Hermitian) | informational sector | $\tilde{Q}^\dagger = \tilde{Q}$ | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $q_0,\ q'_1,\ q'_2,\ q'_3$ | $ct',\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_-$ (anti-Hermitian) | material sector | $\tilde{Q}^\flat = \tilde{Q}$ | $ie_0,\ e_1,\ e_2,\ e_3$ | $q'_0,\ q_1,\ q_2,\ q_3$ | $ict,\ x,\ y,\ z$ |

**The center $\mathbb{C}_{\mathbb{B}}$** — fixed by quaternion conjugation $\bar{\cdot}$, the elements with no vector part at all,

$$
\mathbb{C}_{\mathbb{B}} = \{\tilde{Q} : \bar{\tilde{Q}} = \tilde{Q}\} = \{Q_0e_0\} = \mathbb{R}e_0 \oplus \mathbb{R}(ie_0), \qquad Q_0 = q_0 + iq'_0 \in \mathbb{C}.
$$

It is two-dimensional over $\mathbb{R}$ — purely scalar, carrying no spatial direction of the dictionary and both temporal ones, so that its two parameters are the two time coordinates together,

$$
\tilde{Q} = q_0e_0 + q'_0(ie_0) = ct'\,e_0 + ict\,e_0 \in \mathbb{C}_{\mathbb{B}}, \qquad \mathbb{C}_{\mathbb{B}} = T_{\mathrm{i}} \oplus T_{\mathrm{m}} .
$$

It is the **center** in the algebraic sense — the elements commuting with everything, $[\tilde{C}, \tilde{Q}] = 0$ for all $\tilde{Q} \in \mathbb{B}$ — which is what makes it the home of the scalars; and that is not an artefact of the parametrisation, since $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ with the quaternions having center $\mathbb{R}$ gives the center of $\mathbb{B}$ as $\mathbb{C} \otimes_\mathbb{R} \mathbb{R}e_0 = \mathbb{C}_{\mathbb{B}}$ itself. It is therefore a subalgebra isomorphic to $\mathbb{C}$ — a field, and the only commutative one among the six subspaces — preserved by every conjugation the algebra has: $\bar{\cdot}$ fixes it pointwise, ${}^{*}$ and with it $\dagger$ negates its second line $ie_0$ while fixing $e_0$, and $\flat$ reverses the two. Under $\Phi$ it is exactly the preimage of the scalar matrices, $\Phi(\mathbb{C}_{\mathbb{B}}) = \mathbb{C}I_2$, so the continuous **central phase** — the global $U(1)$, whose element $e^{i\theta}e_0$ lies here — is a motion within the center, fixed by $\bar{\cdot}$ and conjugated by ${}^{*}$. Its two lines are also the two directions common to three of the six subspaces, $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R}e_0$ and $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_0)$.

**The vector subspace $\mathrm{Vect}(\mathbb{B})$** — the only one of the six that is not fixed by a conjugation: it is the **anti**-fixed space of quaternion conjugation, the elements with $\bar{\tilde{Q}} = -\tilde{Q}$, whose fixed space is the center above. Equivalently it is the complement of the center, the elements with no scalar part,

$$
\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\} = \{Q_1e_1 + Q_2e_2 + Q_3e_3\}, \qquad Q_k \in \mathbb{C},
$$

of real dimension six — three complex dimensions, the only subspace of the six that is not four- or two-dimensional. Its six parameters take both spatial blocks,

$$
\tilde{Q} = q_1e_1 + q_2e_2 + q_3e_3 + q'_1(ie_1) + q'_2(ie_2) + q'_3(ie_3) = \mathbf{x} + i\mathbf{x}' \in \mathrm{Vect}(\mathbb{B}), \qquad \mathrm{Vect}(\mathbb{B}) = X_{\mathrm{m}} \oplus X_{\mathrm{i}},
$$

the material space and the informational space together, so it is the spatial counterpart of the center, which is the two temporal blocks together. With the center it gives the third decomposition of the algebra, $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, the decomposition into scalar and traceless part; it is closed under the commutator, being the derived subspace $[\mathbb{B},\mathbb{B}]$, but not under multiplication.

**The quaternion subspace $\mathbb{H}_{\mathbb{B}}$** — fixed by ${}^{*}$, basis $e_0, e_1, e_2, e_3$; all four coefficients **real**, the condition that no coefficient carries the central $i$. Its four parameters take the informational time together with the material space,

$$
\tilde{Q} = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = (ct')\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 = ct'\,e_0 + \mathbf{x} \in \mathbb{H}_{\mathbb{B}}, \qquad q_\mu \in \mathbb{R}.
$$

It is a subalgebra — a copy of $\mathbb{H}$ inside $\mathbb{B}$, hence a division algebra — and it is the home of the rotation rotors. Being free of the central $i$, it carries the Euclidean signature $(4,0)$: the $ict$ convention is not available inside it, and its physical coordinate is the pair $(ct', \mathbf{x})$, with the temporal coefficient real and the spatial ones real.

**The antiquaternion subspace $i\mathbb{H}_{\mathbb{B}}$** — anti-fixed by ${}^{*}$, the elements with $\tilde{Q}^* = -\tilde{Q}$; basis $ie_0, ie_1, ie_2, ie_3$; all four coefficients **purely imaginary**, the condition that every coefficient carries the central $i$. Its four parameters take the material time together with the informational space, the reverse assignment,

$$
\tilde{Q} = iq'_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = ic\,t\,e_0 + ix'\,e_1 + iy'\,e_2 + iz'\,e_3 = ict\,e_0 + i\mathbf{x}' \in i\mathbb{H}_{\mathbb{B}}, \qquad q'_\mu \in \mathbb{R}.
$$

It is not a subalgebra but a module over $\mathbb{H}_{\mathbb{B}}$, since the product of two of its elements is real.

**The informational subspace $\mathbb{M}_+$** — the **Hermitian** subspace, fixed by $\dagger$; equivalently the eigenspace of $\dagger$ with eigenvalue $+1$, the elements with $\tilde{Q}^\dagger = \tilde{Q}$. Basis $e_0, ie_1, ie_2, ie_3$; scalar part **real**, vector part **purely imaginary**, so its four parameters are the informational coordinate,

$$
\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + (ix')\,e_1 + (iy')\,e_2 + (iz')\,e_3 = ct'\,e_0 + i\mathbf{x}' \in \mathbb{M}_+, \qquad q_0 = ct', \quad (q'_1, q'_2, q'_3) = (x', y', z').
$$

It carries the Hermitian operators, states and observables. Multiplication by the central $i$ exchanges the two sectors, $i\mathbb{M}_- = \mathbb{M}_+$, and reverses the sign of the norm form; the two coordinates above are the two ends of that exchange.

**The material subspace $\mathbb{M}_-$** — the **anti-Hermitian** subspace, fixed by $\flat$; equivalently the eigenspace of $\dagger$ with eigenvalue $-1$, the elements with $\tilde{Q}^\dagger = -\tilde{Q}$. Basis $ie_0, e_1, e_2, e_3$; scalar part **purely imaginary**, vector part **real**, so its four parameters are the four-position,

$$
\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = ic\,t\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 = ict\,e_0 + \mathbf{x} \in \mathbb{M}_-, \qquad q'_0 = ct, \quad (q_1, q_2, q_3) = (x, y, z).
$$

It carries the spacetime coordinate and the four-vectors of the series. Because $\flat$ is the algebra's **real structure** (*The Real Structure $\flat$*, below), $\mathbb{M}_-$ is its fixed space — the algebra's real form — and that is the sense in which the series calls this subspace **real**: not that its coefficients are real, which they are not, but that it is fixed by the real structure. The two readings must be kept apart, since the subspace of real *coefficients* is $\mathbb{H}_{\mathbb{B}}$, a different subspace of the same algebra.

Between them these six parametrisations use the eight real numbers that a general element carries. $\mathbb{C}_{\mathbb{B}}$ is the center and $\mathrm{Vect}(\mathbb{B})$ is what remains, the two of them giving the scalar–vector split; $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are the **real and imaginary halves**, from the coefficient split $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$; and $\mathbb{M}_+$ and $\mathbb{M}_-$ are the **sectors**. The two names of each subspace, and the two collective names, are set out in *The Naming Convention* below. Each is treated in its own article — $\mathbb{C}_{\mathbb{B}}$ in *The Center Subspace $\mathbb{C}_{\mathbb{B}}$ as the Complex Time Sector*, $\mathrm{Vect}(\mathbb{B})$ in *The Vector Subspace $\mathrm{Vect}(\mathbb{B})$ as the Complex Space Sector*, $\mathbb{H}_{\mathbb{B}}$ in *The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$ as the Real Sector*, $i\mathbb{H}_{\mathbb{B}}$ in *The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$ as the Imaginary Sector*, $\mathbb{M}_+$ in *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, and $\mathbb{M}_-$ in *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*. Two further conventions attach to the eight numbers: how they are primed, and what the subspaces are called.

### The Prime Convention

**What the prime marks.** The prime belongs to the **coefficients**, not to the physical coordinates. The four coefficients of a general element are complex, and writing each as a real part plus $i$ times a real part,

$$
Q_\mu = q_\mu + iq'_\mu, \qquad q_\mu, q'_\mu \in \mathbb{R}, \qquad \mu = 0, 1, 2, 3,
$$

gives $q_\mu$ as the coefficient of $e_\mu$ and $q'_\mu$ as the coefficient of $ie_\mu$ — the same rule for every $\mu$:

| coefficient | real part | attached to | imaginary part | attached to |
|---|---|---|---|---|
| $Q_0$ | $q_0$ | $e_0$ | $q'_0$ | $ie_0$ |
| $Q_1$ | $q_1$ | $e_1$ | $q'_1$ | $ie_1$ |
| $Q_2$ | $q_2$ | $e_2$ | $q'_2$ | $ie_2$ |
| $Q_3$ | $q_3$ | $e_3$ | $q'_3$ | $ie_3$ |

The primed parameter is the one attached to $ie_\mu$, so **the prime marks the slot that carries the $i$**. It is not a label of a subspace, and it has nothing to do with the physical coordinates: the primes live on the $q$'s, which index the four basis elements, while $x, y, z, t, t'$ name the physical directions those $q$'s are read as. Grouped by the algebra's real-and-imaginary split, the four unprimed parameters are the coordinates of the quaternion subspace and the four primed ones those of the antiquaternion subspace,

$$
q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 \in \mathbb{H}_{\mathbb{B}}, \qquad iq'_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 \in i\mathbb{H}_{\mathbb{B}} .
$$

**The three-and-one pattern.** The two subspaces of the coefficient split are uniform: $\mathbb{H}_{\mathbb{B}}$ is carried entirely by unprimed parameters, $i\mathbb{H}_{\mathbb{B}}$ entirely by primed ones. Each of the two sectors, by contrast, is mixed, because each takes its scalar slot from one side of that split and its three vector slots from the other. The informational sector is $q_0e_0 + iq'_ke_k$ — unprimed scalar, primed vectors — and the material sector is $iq'_0e_0 + q_ke_k$ — primed scalar, unprimed vectors. Read by parameter, the primed set $\{q'_0, q'_1, q'_2, q'_3\}$ is therefore one material slot (the material time $q'_0$) and three informational ones (the informational space $q'_k$), rather than four belonging to a single sector; that mixed ownership is the same statement as the crossing of the two decompositions.

**The alternative, and why it is not used.** $\mathbb{H}_{\mathbb{B}}$, which takes its scalar slot from $\mathbb{M}_+$ and its vector slots from $\mathbb{M}_-$, would be split across the two primes under the alternative labelling, so that it could no longer be written with a single name. That alternative makes the prime mark the **sector** — all-primed for $\mathbb{M}_+$ against all-unprimed for $\mathbb{M}_-$ — which is uniform in the opposite direction, and the corpus has used that labelling too. It is not kept, because it makes the prime mean "informational" rather than "imaginary", and the prime then no longer tracks the $i$: the informational time $ct'$ would be carried by a primed parameter although it is real, and the material time $ict$ by an unprimed one although it is imaginary. The present convention keeps the prime glued to the $i$, at the price of a mixed prime status inside each sector. The crossing itself, and the alternatives it allows, are examined in *Relations Between Subspaces*.

### The Naming Convention

Each of the six subspaces carries two names: an **algebraic** one, taken from the property that defines it, and a **physical** one, taken from the role it plays. The six companion articles are titled by the physical name.

| subspace | algebraic name (from its defining property) | physical name (from its role) |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | the center: fixed space of $\bar{\cdot}$, commuting with everything | complex time sector: the two temporal directions |
| $\mathrm{Vect}(\mathbb{B})$ | vector: anti-fixed space of $\bar{\cdot}$, the traceless part | complex space sector: the two spatial blocks |
| $\mathbb{H}_{\mathbb{B}}$ | quaternion: fixed space of ${}^{*}$, a copy of $\mathbb{H}$ inside $\mathbb{B}$ | real sector: the Euclidean, or Wick-rotated, reading of the four-vector space |
| $i\mathbb{H}_{\mathbb{B}}$ | antiquaternion: anti-fixed space of ${}^{*}$ | imaginary sector: the part written with purely imaginary coefficients |
| $\mathbb{M}_+$ | Hermitian: fixed space of $\dagger$, $\tilde{Q}^\dagger = \tilde{Q}$ | informational sector: carries the Hermitian operators, states and observables |
| $\mathbb{M}_-$ | anti-Hermitian: fixed space of $\flat$, $\tilde{Q}^\dagger = -\tilde{Q}$ | material sector: carries the spacetime coordinate and the four-vectors |

**The algebraic names.** These are intrinsic. Each states which involution fixes the subspace, or where the subspace sits in the algebra, and none of them carries an interpretation: the center is the fixed space of $\bar{\cdot}$, the set of elements that commute with everything, and the vector subspace is its anti-fixed space, equivalently the traceless part, equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$; the quaternion and antiquaternion subspaces are the fixed and anti-fixed spaces of ${}^{*}$; and the Hermitian and anti-Hermitian subspaces are the fixed spaces of $\dagger$ and $\flat$.

**The physical names.** These are the interpretation, and they are the ones the series uses in prose and in the titles of its articles. Each records a role. The **complex time** and **complex space** sectors are the two temporal directions and the two spatial blocks respectively, so named because they carry the temporal and the spatial part of the physical dictionary; the **real sector** is the part of the algebra free of the central $i$, carrying a Euclidean four-dimensional geometry in which no direction is singled out as time, which is what the Wick rotation produces, and the **imaginary sector** is its complement in the coefficient split, the part every coefficient of which carries the $i$; and the **informational sector** carries the Hermitian operators, states and observables, with signature $(1,3)$, while the **material sector** carries the four-positions and four-vectors, and its norm form has signature $(3,1)$.

**The collective names.** Two of the three decompositions of the algebra pair up the subspaces and give the pairs a name of their own. The first needs none beyond the names of its two members:

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})
$$

pairs the center with the traceless part. The decomposition

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}
$$

is the real-and-imaginary split of the coefficients, and its two members are called the **real and imaginary halves** of the algebra: $\mathbb{H}_{\mathbb{B}}$, written with real coefficients throughout, and $i\mathbb{H}_{\mathbb{B}}$, written with purely imaginary ones. The third,

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-
$$

pairs the two sectors — in this series' usage, *the sectors*, without qualification, are these two, and it is the split the relativistic articles are written in terms of. The two pairings cross: no sector is a half, and each sector draws its scalar slot from one half and its vector slots from the other, as *The Prime Convention* above records.

**The choice of which subspace is "real".** The convention that has to be flagged is that $\mathbb{M}_-$ is the *anti*-Hermitian subspace, so that the framework's "real" part is the part built on $i$ times a Hermitian element. The more familiar convention takes the Hermitian part as real. The two differ only by the central factor $i$, and there is no mathematical error either way: an anti-Hermitian generator is the standard choice for the Lie algebra of a unitary group, and it is $\mathbb{M}_-$ that carries that role here. What is unusual is that the convention is applied to the **field** rather than to the generators. Once it is, $\mathbb{M}_-$ is fixed by $\flat$ and $\mathbb{M}_+$ is not, and that is what makes $\mathbb{M}_-$ the framework's material subspace. A reader who "restores" the Hermitian convention will find the whole series inverted. Do not.

### The Four-Vector Representation

The algebra is read as the quadruple of its complex coefficients, in *The Four-Vector Representation of Biquaternions*. Each unit is one coordinate place,

$$
e_0 \longleftrightarrow (1,0,0,0), \qquad e_1 \longleftrightarrow (0,1,0,0), \qquad e_2 \longleftrightarrow (0,0,1,0), \qquad e_3 \longleftrightarrow (0,0,0,1),
$$

so that an element is its quadruple of coefficients,

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu \;\longleftrightarrow\; (Q^0, Q^1, Q^2, Q^3), \qquad Q^0 = Q_0, \quad (Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3),
$$

and the index is written in the upper position. **No index is raised or lowered anywhere in the series.** On $\mathbb{C}^4$ there is no pairing with which to move one, and the $ict$ convention is what puts the metric into the coefficient — $(ict, \mathbf{x})$ rather than a contraction rule — so that the interval is the sum of squares with no explicit scalar product. The article owns the product in components and the column-and-dual-row convention.

### The 4×4 Regular Matrix Representation

Multiplication is read as a linear map on that quadruple, in *The 4×4 Regular Matrix Representation of Biquaternions*. The four units act by

$$
\rho_L(e_0) = I_4 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \qquad
\rho_L(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix},
$$

$$
\rho_L(e_2) = \begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix}, \qquad
\rho_L(e_3) = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix},
$$

and each of the three vector matrices squares to $-I_4$, as $e_k^2 = -e_0$ requires. For a general element, left multiplication by $\tilde{Q}$ is the matrix $\rho_L(\tilde{Q})$ whose $\nu$-th column is the column of $\tilde{Q}e_\nu$,

$$
\rho_L(\tilde{Q})\,\cdot\,\text{(column of } \tilde{R}) = \text{column of } \tilde{Q}\tilde{R},
$$

and right multiplication is the same construction with $e_\nu\tilde{Q}$, giving $\rho_R(e_0) = I_4$ and $\rho_R(e_k) = \eta\,\rho_L(e_k)^{\mathsf{T}}\eta$, with $\eta = \operatorname{diag}(-1,+1,+1,+1)$. The two sides are distinguished on purpose and are not interchangeable: $\rho_R(\tilde{Q})$ is not $\rho_L(\tilde{Q})^{\mathsf{T}}$, and what relates them is the metric, not a relabelling. That relation, and the determinant and trace of the two matrices, belong to the article just named.

### The 2×2 Matrix Representation

The algebra is read as the complex $2 \times 2$ matrices, under the isomorphism

$$
\Phi : \mathbb{B} \to M_2(\mathbb{C}),
$$

in *The 2×2 Matrix Representation of Biquaternions*, and this is the representation every numerical check in the series is performed with. The four unit images are fixed here, once, because every article depends on them agreeing. The three vector units are the Pauli matrices times $-i$:

$$
\Phi(e_0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\Phi(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad
\Phi(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\Phi(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$
<!-- CONVENTION — the matrix basis: the four basis images are asserted, and the images of the Hermitian units follow from them as Phi(i e_k) = i Phi(e_k) by C-linearity, needing no new choice. Both the factor i and the sign are forced (e_k^2 = -e_0 and e_1 e_2 = e_3), so a reviewer must not "correct" the assignment by making the three images real, nor by negating all three, and must not treat the choice as free. -->

with the central scalar mapping to $\Phi(i) = iI_2$. Because $\Phi$ is $\mathbb{C}$-linear, the Hermitian units require no separate choice, $\Phi(ie_k) = i\,\Phi(e_k)$.

**The trace is the trace of this image.** The series writes

$$
\operatorname{Tr}(\tilde{Q}) := \operatorname{Tr}\Phi(\tilde{Q}).
$$

On the units $\operatorname{Tr}(e_0) = 2$ and $\operatorname{Tr}(e_k) = 0$, so on a general element $\operatorname{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$. That factor $2$ is not a normalisation but a consequence of $\Phi(e_0) = I_2$: it comes with the four images above, it cannot be divided out, and every pairing in the series is written with it, the Born rule $p = \operatorname{Tr}(\tilde{P}\tilde{\rho})$ among them. An unsubscripted trace means this one; a regular matrix has its own, written with its subscript. The unrestricted identity $\operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2)$ is recorded with its verification in the article just named.

**The assignment is forced, not chosen.** Neither the factor $i$ nor the sign in the three vector images could have been otherwise: $e_k^2 = -e_0$ requires the factor, and $e_1e_2 = e_3$ fixes the sign. A reviewer must not "correct" the assignment by making the three images real, nor by negating all three. *The 2×2 Matrix Representation of Biquaternions* derives both.

**Never conjugate the matrix entries on their own.** Conjugating the entries of $\Phi(\tilde{Q})$ is *not* the image of any involution of the algebra: it negates the images of $e_1$ and $e_3$ while leaving $\Phi(e_2)$, which has real entries, untouched, and so it destroys the sector dictionary. The four conjugations $\bar{\phantom{Q}}$, ${}^*$, $\dagger$ and $\flat$ are evaluated through the matrix formulas recorded in *The 2×2 Matrix Representation of Biquaternions*, never by conjugating entries.

**The realisation is a convention of presentation, not of content.** The isomorphisms that preserve the subspace dictionary are the $\Phi' = S\Phi S^{-1}$ with $S$ unitary up to a nonzero complex scalar, and the scalar cancels in $S \cdot S^{-1}$. An arbitrary invertible $S$ destroys the dictionary, and so does a genuine squeeze $S = UP$ with $U$ unitary and $P$ positive definite and $\neq I$: both keep the center, which is scalars, and neither preserves the quaternion subspace or either sector. The practical consequence is that a mistake of translation between the algebra and its matrices is repaired **here** — by correcting the assignment or the explicit factors of $i$ — and never by altering the norm form, the $ict$ assignment or the sector split.

**A bare $\Phi$ means this isomorphism and nothing else.** A plain $\Phi$, with no subscript, superscript or tilde, is reserved throughout the series for this isomorphism alone. The other uses a reader may meet are marked differently: $\varphi$ is an abstract homomorphism on the mathematics pages and an angle in the Thomas-precession exercise, $\tilde{\Phi} = \varphi\,e_0$ is the central scalar field of the Higgs articles, and $\Phi_{\tilde{U}}$ is the quantum channel of the gates article. None of these is the isomorphism, and a bare $\Phi$ is not any of them.

## The Spacetime Conventions

What remains are the conventions of the forms the physics is written with, once the coordinate dictionary of *The Six Subspaces* above has fixed which parameters carry $ict$ and $\mathbf{x}$ and which carry $ct'$ and $i\mathbf{x}'$. The basis $e_0, e_1, e_2, e_3$ and the $ict$ assignment are the conventions on which every relativistic article depends; the metric, the d'Alembertian and the mass term are the conventions built on them.

### The Metric: Three Levels

The word "metric" appears at three distinct levels in the series, and most of the disagreements below are the result of the levels being conflated. They are separated here in order of priority, because the first is the convention of the framework and the third is only a convention of translation.

**Level 1 — the norm form on $\mathbb{B}$.** The algebra carries the complex-linear norm form

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2 ,
$$

and with all four coefficients $Q_\mu$ complex its Gram matrix is the **identity**:

$$
\mathrm{diag}(+1,+1,+1,+1).
$$

This is the metric of the biquaternion universe, and it is the framework's primary convention. It is a metric **on $\mathbb{C}$** — a complex bilinear form — and read that way every one of its four entries is positive: on $\mathbb{B}$ there is no minus sign in the form itself, and none is needed. That is precisely what the complex coefficients buy. A *real* direction has to be labelled positive or negative in advance, and that labelling becomes a convention that can be chosen wrongly; a complex coefficient carries its own sign in the coefficient, so all four directions can start out on an equal footing and no such commitment is required. Two cautions about reading it. It is not positive definite and it is not a norm in the analytic sense — it vanishes on the nonzero zero divisors, which is why $\mathbb{B}$ is not a normed division algebra. And the Hermitian form $\sum_\mu |Q_\mu|^2$ is a *different* object: real-valued, positive definite, and $\mathbb{C}$-antilinear in its first argument. It is used only where a positive-definite inner product on a complex vector space is needed, and it is not the norm form of the algebra.

**Level 2 — the real sectors.** A minus appears only once a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$. The two four-dimensional real sectors are exactly such choices, and the same level-1 form reads off differently on each:

| Sector | Basis | $N$ on the basis | Signature |
|---|---|---|---|
| $\mathbb{M}_-$ (material) | $ie_0,\ e_1,\ e_2,\ e_3$ | $-1,+1,+1,+1$ | $(-,+,+,+)$ |
| $\mathbb{M}_+$ (informational) | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $+1,-1,-1,-1$ | $(+,-,-,-)$ |

Read as a statement about **objects** rather than directions: an element of $\mathbb{M}_-$ carries the metric $(-,+,+,+)$, and an element of $\mathbb{M}_+$ carries $(+,-,-,-)$. This is not a separate choice made sector by sector — it is the one level-1 form read on two different real bases, and the two readings are mirror images of one another through the identity below.

The Minkowski interval is not postulated at this level either. It is the level-1 form read on the material sector with the time coordinate written $ict$: the four-position is $\tilde{Q} = ict\,e_0 + \mathbf{x}$, whose scalar coefficient $ict$ is imaginary, and

$$
N(\tilde{Q}) = (ict)^2 + x^2 + y^2 + z^2 = -c^2t^2 + \mathbf{x}^2 ,
$$

with the minus arising from $i^2 = -1$ alone. Multiplication by $i$ exchanges the sectors, $i\mathbb{M}_+ = \mathbb{M}_-$, and reverses the sign of the form, $N(i\tilde{Q}) = -N(\tilde{Q})$; the mirror relation between the two signatures is that identity. The Lorentzian signature is therefore an *output* of the biquaternion conventions, not an input to them.

For contractions of four-vectors in the $ict$ coordinate the series writes this level-2 form as

$$
\eta = \mathrm{diag}(-1,+1,+1,+1),
$$

and at this level the series is uniform: the $ict$ metric is $(-,+,+,+)$ throughout. The two articles outside the relativistic core that carry a symbol $g = \mathrm{diag}(-1,+1,+1,+1)$ — the companion articles on the Higgs mechanism and on the Newman–Penrose formalism — mean **this** object, the $ict$-coordinate metric for index contractions, and not a Clifford metric, as their own notation tables state. They are not part of the level-3 disagreement below.

**Level 3 — the Clifford metric of the $\gamma^\mu$.** When the series writes gamma matrices it needs a further symbol $g$, defined by $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$. This is a property of the chosen generators and not of the biquaternion algebra, and it is best regarded as a **tool** rather than a convention: it can be used or not, depending on the situation, and where it is used it should not dictate any convention of the framework. The biquaternion formulation requires no gamma matrices; they are a translation into the language of the standard Dirac literature, convenient when comparing with that literature or borrowing a standard result, and dispensable otherwise. The freedom this level carries is exactly the freedom the framework treats as presentation: replacing every generator by $i\gamma^\mu$ takes $g$ to $-g$ and leaves the biquaternion algebra, the norm form, the sector split, the chirality operator and the whole of levels 1 and 2 invariant.

The value the series now uses is the standard **mostly-minus**

$$
g = \mathrm{diag}(+1,-1,-1,-1),
$$

so that $(\gamma^0)^2 = +I_4$ and $(\gamma^k)^2 = -I_4$. Two reasons fix it. First, **it is the form of the objects the tool represents**: the Clifford vectors correspond to the *Hermitian* subspace $\mathbb{M}_+$ — the dictionary's own identification is $x_\mu\gamma^\mu = \gamma^0\Phi(w)$ with $w \in \mathbb{M}_+$ — and $(+,-,-,-)$ is the $\mathbb{M}_+$ form, so the square of a Clifford vector agrees with the norm form of the biquaternion it represents with **no relative sign**. Second, it is the standard particle-physics convention, so articles transcribing standard results inherit the standard sign without adjustment, and the name $\mathrm{Cl}_{1,3}$ is correct in the usual counting, $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$.

The opposite sign, $g = \mathrm{diag}(-1,+1,+1,+1)$, is **not in use**. It pairs the generators with the material sector, which is a real form they do not belong to; the price is a relative minus sign between the square of a Clifford vector and the norm form of the biquaternion it represents, a mixed sign pattern in the timelike bivectors, and a non-standard naming of the algebra. It is recorded here only because the series used it previously, in the article that defines the gamma matrices and the Dirac equation, in the Dirac-algebra dictionary, and in the mathematics article *Biquaternion Algebraic Representations*; those three have been aligned to the value above.

A difference at this level would **not** be an error at level 1 or level 2, and half the reason for separating the levels is to stop it being read as one: the norm form, the $ict$ metric and the sector structure are the same for either sign. The sign decides only which *real* Clifford form the generators generate — $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ for $(+,-,-,-)$, $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ for $(-,+,+,+)$ — and the even subalgebra, which is $\mathbb{B}$ itself, is the same for both, so no dictionary entry and no biquaternion identity depends on it.

The order of authority is therefore one-way. The algebra and its level-1 and level-2 conventions are the framework; the gamma matrices and their metric are a translation of it, adopted per article for whatever the article is doing. The tool serves the framework and not the reverse: a Clifford computation is never a reason to change a biquaternion convention, and where the two appear to disagree, the disagreement is in the translation and is resolved by adjusting the generators, the adjoint, or the explicit factors of $i$ — never by altering the norm form, the $ict$ assignment, or the sector split.

One consequence does reach the physics, and it is the only place where a level-3 choice is not free. The Dirac adjoint is $\bar{\psi} = \psi^\dagger\gamma^0$, so it carries $\gamma^0$ and changes with the convention. With the mostly-minus generators $\bar{\psi}\gamma^0\psi = +\psi^\dagger\psi$, the positive number density; with the mostly-plus generators the same expression gives $-\psi^\dagger\psi$. A spinor bilinear written as $\bar{\psi}\Gamma\psi$ therefore requires the adjoint to be defined consistently with the generators in use. No article in the series currently writes a spinor bilinear in the mostly-plus convention, so no statement in the series is in error on this count; the point is recorded so that one is not introduced. This sign is not part of the freedom that $\gamma^\mu \mapsto i\gamma^\mu$ leaves behind.

### The d'Alembertian, and a Known Sign Collision

The series' d'Alembertian is defined through the biquaternionic gradient:

$$
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2 ,
$$

the **series convention**, used by the Klein–Gordon article, the Dirac article, and the great majority of the series.

The article *Exercise: Chirality and the Weyl Spinors* uses a different one:

$$
\Box_{\text{Weyl}} = \partial_0^2 - \nabla^2 ,
$$

in natural units with the standard quantum-field-theory metric $(+,-,-,-)$. The two are related by

$$
\Box_{\text{Weyl}} = -\,\Box_{\text{series}} .
$$

Since an overall factor $-1$ does not change the kernel, the two mass-term equations

$$
(\Box + m^2)\psi = 0 \quad \text{(the Weyl-spinor exercise)}, \qquad \left(\Box - \frac{m^2c^2}{\hbar^2}\right)\psi = 0 \quad \text{(the series)}
$$

have the **same solution set**. They are the same equation written in two sign conventions.

This is the single most likely place for a spurious "correction" in the whole series. The rule is: **check the local definition of $\Box$ before touching a mass-term sign.** Reciprocal markers sit at both articles recording this, so that neither is "aligned" to the other in isolation.

## The Dirac Mass Term: the Linear, Chirality-Off-Diagonal Convention

### The Convention

The biquaternionic Dirac equation for a **massless** field is

$$
\tilde{\nabla}\tilde{\Psi} = 0 ,
$$

which is identical in form to the source-free biquaternion Maxwell equation. For a field of mass $m$ the equation is **linear** in the field and **off-diagonal between the chiralities**. Writing $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$, the massive equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

the **canonical form** of the series. Its massless limit is $\tilde{\nabla}\tilde{\Psi} = 0$.

Two features of this convention are load-bearing, and both are stated as standing rules.

**(i) The mass term is linear.** Because it is linear in the field, the continuous central phase passes through it: the vector $U(1)$ symmetry is **exact for the massive field**,

$$
\partial_\mu j^\mu = 0 \quad \text{on shell, for all } m,
$$

and what the mass breaks is not the vector symmetry but the **axial** one,

$$
\partial_\mu j_5^\mu = 2im\,\bar{\Psi}\gamma_5\Psi ,
$$

which vanishes only at $m = 0$. A single plane wave cannot exhibit this breaking: its bilinears are $x$-independent, so both divergences vanish identically and the distinction is invisible. The breaking is visible on a **superposition**, which is how it should be checked.

**(ii) The mass term is off-diagonal between the chiralities.** It relates $\tilde{\Psi}_L$ to $\tilde{\Psi}_R$; it never pairs a field with its own conjugate.

### Why Linear and Off-Diagonal

The off-diagonal form is **forced**, not chosen, and the argument is purely algebraic.

Left multiplication by an element of $\mathbb{B}$ *preserves* each minimal left ideal. Since those ideals are the two chiralities, no combination of the form $a\tilde{\Psi}_L + b\tilde{\Psi}_R$ can relate one chirality to the other: left multiplication maps each into itself. A mass term that couples the chiralities therefore has to act as a **right** multiplication, which is exactly what the pair above does. Equivalently, restricted to the strict spinor module — a single minimal left ideal — the mass is simply linear.

This is the structural reason why the **spinor module**, and not the whole algebra, is the natural carrier of the Dirac field. On that module the pair is the matrix equation $(\not\partial - m)\psi = 0$ with $\psi = (\psi_L, \psi_R)$ the pair of Weyl spinors, and the off-diagonal structure is the statement that the mass couples the two Weyl spinors.

### What Is Not the Mass Term

The series previously wrote the massive equation as a single **antilinear** equation in one field,

$$
\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat , \qquad \tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger ,
$$

using the algebra's anti-Hermitian conjugation. **This is not the mass term, and it must not be restored as one.** The reason is not that it is antilinear — a Majorana mass is also antilinear and is perfectly physical. The reason is its dispersion relation.

For that equation, the central-phase plane waves do **not** sit on the physical mass shell. Solving the two-frequency system for a single-mode field gives nullity $0$ on the timelike shell $k_0^2 = k^2 + m^2$ but nullity $4$ on the **spacelike** shell $k^2 = k_0^2 + m^2$. Its solutions therefore lie on the spacelike locus. An equation whose central-phase solutions are spacelike is not the Dirac equation, and it contradicts the four-momentum kinematics the rest of the series uses. The spacelike dispersion is a property of that equation, not a typographical error, and re-deriving it by hand (pure real arithmetic suffices) reproduces the nullities. It is exactly why the equation was retired as the mass term.

**The diagnosis is the dispersion, not the antilinearity.** This distinction matters, because the antilinear structure itself is retained — it is the algebra's real structure, and it has genuine uses, as the next section records.

### What Dependent Articles Inherit

The three consequences below propagate into every article that touches the Dirac equation. They are the reason this convention cannot be changed locally.

1. **The vector $U(1)$ is conserved for the massive field.** The old claim that the mass breaks the phase symmetry belonged to the retired antilinear equation. In the linear form, the central phase passes through the mass term and commutes with $\tilde{\nabla}$, so the vector current is conserved on shell at all $m$.
2. **The axial current is what the mass breaks**, with $\partial_\mu j_5^\mu = 2im\bar{\Psi}\gamma_5\Psi$, and it is checked on a superposition.
3. **The mass is the off-diagonal coupling between the two central ideals** of $\mathbb{B} \cong M_2(\mathbb{C})$ — the two chiralities, that is, the algebra's central splitting. It breaks exactly the symmetry that rotates those two ideals, and *not* the central $U(1)$ the algebra canonically carries.

## The Real Structure $\flat$

### What $\flat$ Is

The map

$$
\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger = -\bar{\tilde{\Psi}}^{\,*}
$$

is the **anti-Hermitian conjugation**. It is not merely a sign variant of $\dagger$; it has its own algebraic character:

- it is a $\mathbb{C}$-**antilinear** involution, $(\alpha\tilde{A} + \beta\tilde{B})^\flat = \alpha^*\tilde{A}^\flat + \beta^*\tilde{B}^\flat$;
- it is **order-reversing with a twist**, $(\tilde{A}\tilde{B})^\flat = -\tilde{B}^\flat\tilde{A}^\flat$, the sign being the only difference from an ordinary anti-automorphism;
- it acts by a **sign on the two sectors**,
$$
\tilde{\Psi}^\flat = +\tilde{\Psi}\ \ (\tilde{\Psi} \in \mathbb{M}_-), \qquad
\tilde{\Psi}^\flat = -\tilde{\Psi}\ \ (\tilde{\Psi} \in \mathbb{M}_+);
$$
- consequently its **fixed space is the anti-Hermitian sector $\mathbb{M}_-$**.

The map $\flat$ is the algebra's **real structure**, and its shape is that of a charge-conjugation (Majorana) pairing: it relates a field to its own conjugate. The sign convention on the two sectors is what makes $\mathbb{M}_-$ the fixed space, and hence what makes $\mathbb{M}_-$ the material sector — the two conventions are the same convention seen twice.

### What $\flat$ Is For

$\flat$ is retained in the framework for what it is genuinely for:

- conjugation, and the definition of the $\mathbb{M}_\pm$ split itself;
- the trace and the bilinear pairings;
- the real-form question of Dirac versus Majorana fermions, which the companion articles on chirality, the neutrino and the CPT theorem develop.

In every case the coupling built on $\flat$ pairs $\tilde{\Psi}$ with $\tilde{\Psi}^\flat$. Because $\flat$ is antilinear, such a coupling is **not invariant under the continuous central phase** — which is precisely the difference between a Majorana-type pairing and an ordinary Dirac mass, and precisely why $\flat$ cannot serve as the mass term of the Dirac equation.

### What $\flat$ Is Not

$\flat$ is **not** the mass. The two roles were conflated in the retired form $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$, and separating them is the content of the mass-term convention above. A reader who finds $\flat$ in an article should expect conjugation, a Majorana pairing, a bilinear, or the sector split — never a Dirac mass.

## Summary

The conventions of the series fall into two groups.

**Algebraic.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, over complex coefficients. The scalar unit $i$ is central, which is what makes the central phase the algebra's continuous symmetry. The conjugations cut the algebra into six real subspaces: the two-dimensional center subspace $\mathbb{C}_{\mathbb{B}}$; the six-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$; and four distinguished four-dimensional ones, named $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$. Each carries its own real parameters and its own slice of the coordinate dictionary, with $q'_0 = ct$, $q_0 = ct'$, $(q_1,q_2,q_3) = (x,y,z)$ and $(q'_1,q'_2,q'_3) = (x',y',z')$. With complex coefficients the norm form $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ is the identity matrix on $\mathbb{B}$; its Minkowski signature appears only on the real sectors, and the $i$ is what supplies the minus. The matrix representation $\Phi$ is fixed by its four basis images, with the Hermitian units following as $\Phi(ie_k) = i\,\Phi(e_k)$; the residual freedom is a unitary change of basis of $\mathbb{C}^2$ and nothing further, so the sector dictionary cannot be altered by re-choosing it. The algebra has three representations — the coefficient quadruple, the regular matrix, and the matrix image $\Phi$ — each developed in its own article, and it is the trace of $\Phi$ that the series calls the trace.

**Spacetime and fields.** The material coordinate is $\tilde{Q} = ict\,e_0 + \mathbf{x}$, using the $ict$ convention so that the Minkowski interval is the norm form, of signature $(3,1)$, vanishing on the zero-divisor cone. The $ict$ metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$. The series d'Alembertian is $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$; the Weyl-spinor exercise uses the opposite sign, $\Box = \partial_0^2 - \nabla^2$, and the two mass-term signs are the same equation. The Clifford metric $g$ is a level-3 tool rather than a convention, adopted where an article translates into gamma matrices, and its value is the standard mostly-minus $\mathrm{diag}(+1,-1,-1,-1)$ throughout the series — the $\mathbb{M}_+$ form, since the Clifford vectors correspond to the Hermitian subspace, so that the square of a Clifford vector agrees with the norm form of the biquaternion it represents with no relative sign. The opposite sign is not in use. Either way the norm form, the $ict$ metric and the sector structure are unchanged, and the tool never dictates them. The Dirac mass term is **linear and chirality-off-diagonal**, $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$; it conserves the vector $U(1)$ and breaks the axial symmetry. The retired antilinear form $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ was retired for its spacelike dispersion, and $\flat = -\dagger$ is retained as the algebra's real structure.

The theme is single. In a framework whose algebra and sector assignment are non-standard, the most likely error is a correction of something that is deliberate. The conventions recorded above are the places where that is most likely to happen.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q}$ | An element of the algebra. The same symbol serves for the general element and for an element of any of the subspaces, whichever the passage at hand is about; the complex coefficients are $Q_\mu$, the real parameters of a four-dimensional subspace are $q_\mu$ and $q'_\mu$, the prime marking the slot that carries the $i$. |
| $\bar{\tilde{Q}}, \tilde{Q}^*, \tilde{Q}^\dagger, \tilde{Q}^\flat$ | Quaternion, complex, Hermitian and anti-Hermitian conjugation |
| $\bar{\tilde{Q}} \mapsto \epsilon M^{\mathsf T}\epsilon^{-1}$, $\tilde{Q}^* \mapsto \epsilon\overline{M}\epsilon^{-1}$ | The two conjugations dressed by the antisymmetric form; $\epsilon = \Phi(-e_2)$ |
| $\tilde{Q}^\dagger \mapsto M^\dagger$, $\tilde{Q}^\flat \mapsto -M^\dagger$ | The two undressed ones. Entrywise conjugation of $M$ alone is not the image of any involution |
| $\flat = -\dagger$ | The anti-Hermitian conjugation, the algebra's real structure |
| $\mathbb{C}_{\mathbb{B}} = \{Q_0 e_0\}$ | Center subspace, fixed points of quaternion conjugation; the center of $\mathbb{B}$ and the complex time sector; parameters $q_0, q'_0$ with $q_0 = ct'$ and $q'_0 = ct$ |
| $\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\}$ | The vector subspace, i.e. the complex space sector: anti-fixed points of quaternion conjugation, real dimension six; parameters $q_k, q'_k$ with $(q_k) = (x,y,z)$ and $(q'_k) = (x',y',z')$. Equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, i.e. the real sector (the real half): fixed points of complex conjugation, all four coefficients real; a subalgebra, and the home of the rotation rotors |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion subspace, i.e. the imaginary sector (the imaginary half): anti-fixed points of complex conjugation, all four coefficients purely imaginary; a module over $\mathbb{H}_{\mathbb{B}}$, not a subalgebra. $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, a split that crosses the $\mathbb{M}_\pm$ split |
| $\mathbb{M}_+ = \{ \tilde{Q} : \tilde{Q}^\dagger = \tilde{Q} \}$ | Hermitian subspace, the informational sector; basis $e_0, ie_1, ie_2, ie_3$, parameters $q_0, q'_1, q'_2, q'_3$ (real), with $q_0 = ct'$ |
| $\mathbb{M}_- = \{ \tilde{Q} : \tilde{Q}^\flat = \tilde{Q} \}$ | Anti-Hermitian subspace, the material sector; basis $ie_0, e_1, e_2, e_3$, parameters $q'_0, q_1, q_2, q_3$ (real), with $q'_0 = ct$ |
| $\tilde{Q} = ict\,e_0 + \mathbf{x}$ | The material coordinate, $\mathbf{x} = x e_1 + y e_2 + z e_3$ |
| $(ct')\,e_0 + i\mathbf{x}'$ | The informational coordinate, $\mathbf{x}' = x' e_1 + y' e_2 + z' e_3$; the temporal coefficient $ct'$ is real and the spatial ones imaginary, the mirror of the material coordinate |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form; identity matrix $\mathrm{diag}(+1,+1,+1,+1)$ as a metric on $\mathbb{C}$ (level 1), signature $(3,1)$ on $\mathbb{M}_-$ (level 2) and $(1,3)$ on $\mathbb{M}_+$ |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric, signature $(-,+,+,+)$ (level 2) |
| $g$ | Clifford metric of the $\gamma^\mu$ (level 3); an optional tool, not a framework convention. $\mathrm{diag}(+1,-1,-1,-1)$ throughout — the $\mathbb{M}_+$ form, matching the objects the tool represents |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}$ | Biquaternionic gradient and its conjugate |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$ | d'Alembertian, series convention |
| $\Box_{\text{Weyl}} = -\Box$ | d'Alembertian of the Weyl-spinor exercise, opposite sign |
| $\mathrm{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ | Trace pairing, unrestricted; the case $\tilde{P}\in\mathbb{M}_+$, $\tilde{Q}\in\mathbb{M}_+$ is the real one. $\mathrm{Tr}(e_0) = 2$ |
| $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ | The matrix representation, with $\Phi(e_0) = I_2$ and $\Phi(e_k)$ as given above; the Hermitian units follow as $\Phi(ie_k) = i\,\Phi(e_k)$. Fixed up to a unitary change of basis, and no further |
| $Q^\mu$ | The coefficients of an element, in the upper position, $Q^0 = Q_0$ and $(Q^1,Q^2,Q^3) = (Q_1,Q_2,Q_3)$; never raised or lowered, there being no metric on $\mathbb{C}^4$ |
| $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$ | Chiral decomposition of the Dirac field |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$ | The linear, chirality-off-diagonal mass term (canonical form) |
| $SL(2,\mathbb{C})$ | Unit-norm biquaternions, the Lorentz group on $\mathbb{M}_-$ |

## Further Reading

- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the original quaternion algebra and its units.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and its mass term.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard treatment of spinors and the chiral structure of the Dirac field.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard particle-physics metric and gamma-matrix conventions.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the metric and normalisation conventions of quantum field theory, and the consequences of changing them.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents, minimal left ideals, and the conjugations of a Clifford algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for real structures and real forms on Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the Dirac equation and its mass term.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in geometric algebra.
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), companion article, for the relations among the subspaces defined here — their coordinate blocks, intersections, spans, gradings and norm forms.
- *The Four-Vector Representation of Biquaternions* (`articles_physics/the-four-vector-representation-of-biquaternions.md`), companion article, for the coefficient space, the column and the dual row, and the index that is never raised or lowered.
- *The 4×4 Regular Matrix Representation of Biquaternions* (`articles_physics/the-4x4-regular-matrix-representation-of-biquaternions.md`), companion article, for the two regular matrices, the relation between them, and the reduction into the two chiralities.
- *The 2×2 Matrix Representation of Biquaternions* (`articles_physics/the-2x2-matrix-representation-of-biquaternions.md`), companion article, for the isomorphism $\Phi$, the trace and the determinant, and the ideals as columns.
