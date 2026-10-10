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

replaces the four complex coefficients by **eight real parameters**: $q_\mu$ is the real part of $Q_\mu$, the coefficient of $e_\mu$, and $q'_\mu$ its imaginary part, the coefficient of $ie_\mu$, so the prime marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and the six subspaces below are what the eight parameters are grouped into. The full set of parametrisations, and the two conventions they embody, are in *The element and its coefficients* and *The Six Subspaces* below; nothing in them changes the split stated here.

One structural fact governs the whole series, so it is worth isolating. **The scalar unit $i$ is central**: it commutes with every element of $\mathbb{B}$, because it belongs to the $\mathbb{C}$ factor of the tensor product, while the quaternion units belong to the $\mathbb{H}$ factor. Multiplication by a *central* phase $e^{i\alpha}$ therefore commutes with every operator constructed from the algebra — in particular with the biquaternionic gradient $\tilde{\nabla}$ — and this is why the central phase is the algebra's natural continuous symmetry. The articles on Noether's theorem and the gauge principle rest on it.

The split is also a split of **roles**, and the two roles belong to the two **factors** of the tensor product and cannot be exchanged. The central unit $i$ is the scalar imaginary: it is what enters the phase $e^{iS/\hbar}$, and it multiplies a whole element from inside the centre. The three units $e_1,e_2,e_3$ are the vector directions: they are the relativistic and rotational structure, and they enter through the quaternion factor. A central scalar and a vector direction are different kinds of object — one commutes with everything, the other rotates — so no product of the four general products may read $i$ through the quaternion direction or a unit through the scalar one. The mirror statement in *The Four General Products and Their Physical Readings* is that the two conjugations act on the two factors separately: the coefficient conjugation $\bar{\cdot}$ conjugates $i$ and fixes the units, while the natural conjugation ${}^{\natural}$ negates the units and fixes $i$, and this separation is what keeps the two roles apart. Read physically, the phase and the relativistic generators are carried by two separate parts of one element, which is why the framework can hold a quantum phase and a Lorentz structure together without identifying them.

As a complex algebra $\mathbb{B}$ is isomorphic to the full matrix algebra,

$$
\mathbb{B} \cong M_2(\mathbb{C}),
$$

and this identification is used constantly. It is fixed by a single isomorphism, written $\Phi$; its four basis images, and the rule that neither the factor $i$ nor the sign is a free choice, are stated in *The 2×2 Matrix Representation* below, and the development of the representation — the general element, the six subspaces as matrices, the conjugations, the trace and the determinant — is in the companion article *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. Its two **minimal left ideals** are the algebra's two chiralities. They are the reason the Dirac field is carried by the spinor module rather than by the whole algebra, and the reason the mass term has the shape it has, as discussed below.

### The element and its coefficients

The case and the tilde of the glyph are fixed first, and the element is written after. A generic element is preferably written so that the glyph alone identifies its algebra, two features being read together: the **case** separates a real scalar from a complex one, and a **tilde** marks the quaternionic factor.

| System | Name | Generic element | Coefficients |
|---|---|---|---|
| $\mathbb{C}$ | complex numbers | $A = a + ia'$ | real, $a, a'$ |
| $\mathbb{H}$ | quaternions | $\tilde q = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$ | real |
| $\mathbb{B}$ | biquaternions | $\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ | complex, $Q_\mu = q_\mu + iq'_\mu$ |

Three rules are read off the table. **A complex element carries a majuscule**, $A$, the case naming the scalar sector: an upper-case glyph has a scalar sector larger than the reals, a lower-case one has the reals. **The second coordinate of a complex element carries a prime**, $A = a + ia'$. And **the quaternionic elements carry a tilde**: lower case for the quaternions, $\tilde q$, and upper case for the biquaternions, $\tilde Q$.

The notation of this article already reads through the convention: the coefficients $q_\mu$ are real, the coefficients $Q_\mu = q_\mu + iq'_\mu$ are complex, and a general element of $\mathbb{B}$ is written $\tilde Q$.

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

This is a **preferred convention** — a preference, not a strict rule, not to be enforced by rewriting other articles: the basis $e_0, \dots, e_3$, the central unit $i$, the Euclidean vector $\mathbf{x}$, the coefficients $q_\mu, q'_\mu$, indices such as $\mu, \nu, k$, and the ladder operators $\tilde a, \tilde a^{\dagger}$ keep their established symbols.

### The Conjugations and the Adjoint

The biquaternion algebra carries four natural involutions, all of them used in the series, together with
the adjoint of an operator, which belongs to the operators and not to the algebra:

| Map | Mark | What it is |
|---|---|---|
| complex conjugation | $\bar{\cdot}$ | the involution of the base, extended to the element |
| quaternion conjugation | ${}^{\natural}$ | the intrinsic conjugate: it fixes the scalars and negates the vectors |
| Hermitian conjugation | ${}^{*}$ | the involution of the algebra, $\bar{\cdot}\circ{}^{\natural}$ |
| anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | the negative of the star |
| operator adjoint | ${}^{\dagger}$ | the adjoint of an operator, $(L_a)^{\dagger} = L_{a^{*}}$ |

Which of the marks has a sense depends on the system, since a mark degenerates wherever the structure it conjugates is absent. The examples below fix it system by system.

**The complex numbers $\mathbb{C}$.** Only the bar has a sense, the algebra carrying a single non-trivial involution:

$$
\bar A = a - ia' .
$$

**The quaternions $\mathbb{H}$.** Only the natural sign has a sense, the coefficients being real and the conjugation intrinsic to the quaternion factor:

$$
\tilde q^{\natural} = q_0e_0 - q_1e_1 - q_2e_2 - q_3e_3 .
$$

**The biquaternions $\mathbb{B}$.** All four have a sense, the bar conjugating the coefficient, which is complex:

$$
\bar{\tilde Q} = \bar Q_0e_0 + \bar Q_1e_1 + \bar Q_2e_2 + \bar Q_3e_3, \qquad \tilde Q^{\natural} = Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3,
$$

$$
\tilde Q^{*} = \overline{\tilde Q^{\natural}} = \bar Q_0e_0 - \bar Q_1e_1 - \bar Q_2e_2 - \bar Q_3e_3, \qquad \tilde Q^{\flat} = -\tilde Q^{*} .
$$

The dagger is the **general adjoint**. It is written on an operator and never on an element, and it is the same in every system. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. Where the adjoint in view is the obvious one, the text writes the two marks together, the dagger first and the star second, so that the coincidence is apparent on the page: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$ and $\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q}^{*}=\Theta_{\tilde Q^{*}}$ (*One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*).

**The mark is not a fifth conjugation.** The four conjugations of the algebra are the bar, the natural sign, the star and the flat; there is no other. An object that is also an operator — the left multiplication $L_a$, the right multiplication $R_a$, the sandwich $\operatorname{H}_{\tilde{Q}}$ — carries the dagger as that operator, and the mark then belongs to the operator and not to the element that generates it: $(L_a)^{\dagger}=L_{a^{*}}$, which is also $(L_a)^{*}$, the adjoint in view being the one of the definite form. Where a text writes a dagger on an element, the writing is an abuse, and the mark that was meant is the star, the Hermitian conjugation, or the natural sign, the quaternion conjugation, according to the conjugation in view. The series writes the elements with the four marks of the table and reserves the dagger for the general adjoint of the operators.

Each of the four involutions has a fixed space, and each of these is one of the **six subspaces** of the algebra. Which involution defines which subspace, and which of them are anti-fixed, is recorded with the subspaces themselves, in *The Six Subspaces* below.

### The Six Subspaces

The eight real parameters of a general element group into **six subspaces**: the two-dimensional centre subspace, the six-dimensional vector subspace, and four four-dimensional ones. Each is listed here under both of its names, the **algebraic** one from the property that defines it and the **physical** one from the role it plays, together with its defining condition, its basis, its own real parameters, and the physical coordinates those parameters carry.

The dictionary between the parameters and the physical coordinates is fixed once and for all,

$$
q'_0 = c\,t, \qquad (q_1, q_2, q_3) = (x, y, z), \qquad q_0 = c\,t', \qquad (q'_1, q'_2, q'_3) = (x', y', z'),
$$

with $\mathbf{x} = x e_1 + y e_2 + z e_3$ the real spatial vector and $i\mathbf{x}' = i x' e_1 + i y' e_2 + i z' e_3$ its imaginary counterpart. The **material coordinate** $\tilde{Q} = ict\,e_0 + \mathbf{x}$ and the **informational coordinate** $\tilde{Q} = ct'\,e_0 + i\mathbf{x}'$ are the two ends of it, and each subspace keeps whichever part of the dictionary its defining condition leaves free.

| subspace | physical interpretation | defining condition | basis | real parameters | physical coordinates |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | complex time sector | $\tilde{Q}^{\natural} = \tilde{Q}$ | $e_0,\ ie_0$ | $q_0,\ q'_0$ | $ct',\ ict$ |
| $\mathrm{Vect}(\mathbb{B})$ (vector) | complex space sector | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $e_1,\ e_2,\ e_3,\ ie_1,\ ie_2,\ ie_3$ | $q_1,\ q_2,\ q_3,\ q'_1,\ q'_2,\ q'_3$ | $x,\ y,\ z,\ ix',\ iy',\ iz'$ |
| $\mathbb{H}_{\mathbb{B}}$ (quaternion) | real sector | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_0,\ e_1,\ e_2,\ e_3$ | $q_0,\ q_1,\ q_2,\ q_3$ | $ct',\ x,\ y,\ z$ |
| $i\mathbb{H}_{\mathbb{B}}$ (antiquaternion) | imaginary sector | $\bar{\tilde{Q}} = -\tilde{Q}$ | $ie_0,\ ie_1,\ ie_2,\ ie_3$ | $q'_0,\ q'_1,\ q'_2,\ q'_3$ | $ict,\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_+$ (Hermitian) | informational sector | $\tilde{Q}^{*} = \tilde{Q}$ | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $q_0,\ q'_1,\ q'_2,\ q'_3$ | $ct',\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_-$ (anti-Hermitian) | material sector | $\tilde{Q}^\flat = \tilde{Q}$ | $ie_0,\ e_1,\ e_2,\ e_3$ | $q'_0,\ q_1,\ q_2,\ q_3$ | $ict,\ x,\ y,\ z$ |

**Compact and non-compact directions.** The six subspaces do not divide the same way at the level of their generators, and the distinction is worth fixing here because it recurs in the quantum readings. A direction is **compact** when the one-parameter group it generates is a circle and **non-compact** when it is a hyperbola; on the algebra the two are separated by the sign of the invariant form, negative on the compact rotation directions and positive on the non-compact boost directions. The three real vector units $e_1,e_2,e_3$ generate the compact $\mathfrak{su}(2)$ of the rotations, the three imaginary units $ie_1,ie_2,ie_3$ the non-compact boosts, and the complex vector subspace carries both. Recomputed on the six basis directions: the invariant form is $-8$ on each real vector direction and $+8$ on each imaginary one, with all off-diagonal entries zero, on $100$ of $100$ of the basis checks. The dichotomy has a second use in the framework: the compact unitary slice is what makes the internal charge discrete, its irreducible labels being discrete, while the non-compact directions are what make the rapidity continuous (*Particle Types, Discrete Charge and Three-Particle Couplings*). The owner is *Angular Momentum and the Lie Algebra of the Material Sector*.

**The centre $\mathbb{C}_{\mathbb{B}}$** — fixed by quaternion conjugation $\natural$, the elements with no vector part at all,

$$
\mathbb{C}_{\mathbb{B}} = \{\tilde{Q} : \tilde{Q}^{\natural} = \tilde{Q}\} = \{Q_0e_0\} = \mathbb{R}e_0 \oplus \mathbb{R}(ie_0), \qquad Q_0 = q_0 + iq'_0 \in \mathbb{C}.
$$

It is two-dimensional over $\mathbb{R}$ — purely scalar, carrying no spatial direction of the dictionary and both temporal ones, so that its two parameters are the two time coordinates together,

$$
\tilde{Q} = q_0e_0 + q'_0(ie_0) = ct'\,e_0 + ict\,e_0 \in \mathbb{C}_{\mathbb{B}}, \qquad \mathbb{C}_{\mathbb{B}} = T_{\mathrm{i}} \oplus T_{\mathrm{m}} .
$$

It is the **centre** in the algebraic sense — the elements commuting with everything, $[\tilde{C}, \tilde{Q}] = 0$ for all $\tilde{Q} \in \mathbb{B}$ — which is what makes it the home of the scalars; and that is not an artefact of the parametrisation, since $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ with the quaternions having centre $\mathbb{R}$ gives the centre of $\mathbb{B}$ as $\mathbb{C} \otimes_\mathbb{R} \mathbb{R}e_0 = \mathbb{C}_{\mathbb{B}}$ itself. It is therefore a subalgebra isomorphic to $\mathbb{C}$ — a field, and the only commutative one among the six subspaces — preserved by every conjugation the algebra has: $\natural$ fixes it pointwise, $\bar{\cdot}$ and with it ${}^{*}$ negates its second line $ie_0$ while fixing $e_0$, and $\flat$ reverses the two. Under $\Phi$ it is exactly the preimage of the scalar matrices, $\Phi(\mathbb{C}_{\mathbb{B}}) = \mathbb{C}I_2$, so the continuous **central phase** — the global $U(1)$, whose element $e^{i\theta}e_0$ lies here — is a motion within the centre, fixed by $\natural$ and conjugated by $\bar{\cdot}$. Its two lines are also the two directions common to three of the six subspaces, $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R}e_0$ and $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_0)$.

**The vector subspace $\mathrm{Vect}(\mathbb{B})$** — one of the two of the six that are not fixed by a conjugation: it is the **anti**-fixed space of quaternion conjugation, the elements with $\tilde{Q}^{\natural} = -\tilde{Q}$, whose fixed space is the centre above. Equivalently it is the complement of the centre, the elements with no scalar part,

$$
\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\} = \{Q_1e_1 + Q_2e_2 + Q_3e_3\}, \qquad Q_k \in \mathbb{C},
$$

of real dimension six — three complex dimensions, the only subspace of the six that is not four- or two-dimensional. Its six parameters take both spatial blocks,

$$
\tilde{Q} = q_1e_1 + q_2e_2 + q_3e_3 + q'_1(ie_1) + q'_2(ie_2) + q'_3(ie_3) = \mathbf{x} + i\mathbf{x}' \in \mathrm{Vect}(\mathbb{B}), \qquad \mathrm{Vect}(\mathbb{B}) = X_{\mathrm{m}} \oplus X_{\mathrm{i}},
$$

the material space and the informational space together, so it is the spatial counterpart of the centre, which is the two temporal blocks together. With the centre it gives the third decomposition of the algebra, $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, the decomposition into scalar and traceless part; it is closed under the commutator, being the derived subspace $[\mathbb{B},\mathbb{B}]$, but not under multiplication.

**The quaternion subspace $\mathbb{H}_{\mathbb{B}}$** — fixed by $\bar{\cdot}$, basis $e_0, e_1, e_2, e_3$; all four coefficients **real**, the condition that no coefficient carries the central $i$. Its four parameters take the informational time together with the material space,

$$
\tilde{Q} = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = (ct')\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 = ct'\,e_0 + \mathbf{x} \in \mathbb{H}_{\mathbb{B}}, \qquad q_\mu \in \mathbb{R}.
$$

It is a subalgebra — a copy of $\mathbb{H}$ inside $\mathbb{B}$, hence a division algebra — and it is the home of the rotation rotors. Being free of the central $i$, it carries the Euclidean signature $(4,0)$: the $ict$ convention is not available inside it, and its physical coordinate is the pair $(ct', \mathbf{x})$, with the temporal coefficient real and the spatial ones real.

**The antiquaternion subspace $i\mathbb{H}_{\mathbb{B}}$** — anti-fixed by $\bar{\cdot}$, the elements with $\bar{\tilde{Q}} = -\tilde{Q}$; basis $ie_0, ie_1, ie_2, ie_3$; all four coefficients **purely imaginary**, the condition that every coefficient carries the central $i$. Its four parameters take the material time together with the informational space, the reverse assignment,

$$
\tilde{Q} = iq'_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = ic\,t\,e_0 + ix'\,e_1 + iy'\,e_2 + iz'\,e_3 = ict\,e_0 + i\mathbf{x}' \in i\mathbb{H}_{\mathbb{B}}, \qquad q'_\mu \in \mathbb{R}.
$$

It is not a subalgebra but a module over $\mathbb{H}_{\mathbb{B}}$, since the product of two of its elements is real.

**The informational subspace $\mathbb{M}_+$** — the **Hermitian** subspace, fixed by ${}^{*}$; equivalently the eigenspace of ${}^{*}$ with eigenvalue $+1$, the elements with $\tilde{Q}^{*} = \tilde{Q}$. Basis $e_0, ie_1, ie_2, ie_3$; scalar part **real**, vector part **purely imaginary**, so its four parameters are the informational coordinate,

$$
\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + (ix')\,e_1 + (iy')\,e_2 + (iz')\,e_3 = ct'\,e_0 + i\mathbf{x}' \in \mathbb{M}_+, \qquad q_0 = ct', \quad (q'_1, q'_2, q'_3) = (x', y', z').
$$

It carries the Hermitian operators, states and observables. Multiplication by the central $i$ exchanges the two sectors, $i\mathbb{M}_- = \mathbb{M}_+$, and reverses the sign of the biquaternion norm; the two coordinates above are the two ends of that exchange.

**The material subspace $\mathbb{M}_-$** — the **anti-Hermitian** subspace, fixed by $\flat$; equivalently the eigenspace of ${}^{*}$ with eigenvalue $-1$, the elements with $\tilde{Q}^{*} = -\tilde{Q}$. Basis $ie_0, e_1, e_2, e_3$; scalar part **purely imaginary**, vector part **real**, so its four parameters are the four-position,

$$
\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = ic\,t\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 = ict\,e_0 + \mathbf{x} \in \mathbb{M}_-, \qquad q'_0 = ct, \quad (q_1, q_2, q_3) = (x, y, z).
$$

It carries the spacetime coordinate and the four-vectors of the series. Because $\flat$ is the algebra's **real structure** (*The Real Structure $\flat$*, below), $\mathbb{M}_-$ is its fixed space — the algebra's real form — and that is the sense in which the series calls this subspace **real**: not that its coefficients are real, which they are not, but that it is fixed by the real structure. The two readings must be kept apart, since the subspace of real *coefficients* is $\mathbb{H}_{\mathbb{B}}$, a different subspace of the same algebra.

Between them these six parametrisations use the eight real numbers that a general element carries. $\mathbb{C}_{\mathbb{B}}$ is the centre and $\mathrm{Vect}(\mathbb{B})$ is what remains, the two of them giving the scalar–vector split; $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are the **real and imaginary halves**, from the coefficient split $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$; and $\mathbb{M}_+$ and $\mathbb{M}_-$ are the **sectors**. Each is treated in its own article — the first four in *The Four Other Remarkable Subspaces*, $\mathbb{C}_{\mathbb{B}}$ in its §*The Complex Time Sector*, $\mathrm{Vect}(\mathbb{B})$ in §*The Complex Space Sector*, $\mathbb{H}_{\mathbb{B}}$ in §*The Real Sector* and $i\mathbb{H}_{\mathbb{B}}$ in §*The Imaginary Sector*, and the two sectors in *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*. The two further conventions that attach to the eight numbers are set out below: what the subspaces are called, and how they are primed.

Each of the six subspaces carries two names: an **algebraic** one, taken from the property that defines it, and a **physical** one, taken from the role it plays. The companion articles are titled by the physical name.

| subspace | algebraic name (from its defining property) | physical name (from its role) |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | the centre: fixed space of $\natural$, commuting with everything | complex time sector: the two temporal directions |
| $\mathrm{Vect}(\mathbb{B})$ | vector: anti-fixed space of $\natural$, the traceless part | complex space sector: the two spatial blocks |
| $\mathbb{H}_{\mathbb{B}}$ | quaternion: fixed space of $\bar{\cdot}$, a copy of $\mathbb{H}$ inside $\mathbb{B}$ | real sector: the Euclidean, or Wick-rotated, reading of the four-vector space |
| $i\mathbb{H}_{\mathbb{B}}$ | antiquaternion: anti-fixed space of $\bar{\cdot}$ | imaginary sector: the part written with purely imaginary coefficients |
| $\mathbb{M}_+$ | Hermitian: fixed space of ${}^{*}$, $\tilde{Q}^{*} = \tilde{Q}$ | informational sector: carries the Hermitian operators, states and observables |
| $\mathbb{M}_-$ | anti-Hermitian: fixed space of $\flat$, $\tilde{Q}^{*} = -\tilde{Q}$ | material sector: carries the spacetime coordinate and the four-vectors |

**The algebraic names.** These are intrinsic. Each states which involution fixes the subspace, or where the subspace sits in the algebra, and none of them carries an interpretation: the centre is the fixed space of $\natural$, the set of elements that commute with everything, and the vector subspace is its anti-fixed space, equivalently the traceless part, equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$; the quaternion and antiquaternion subspaces are the fixed and anti-fixed spaces of $\bar{\cdot}$; and the Hermitian and anti-Hermitian subspaces are the fixed spaces of ${}^{*}$ and $\flat$.

**The physical names.** These are the interpretation, and they are the ones the series uses in prose and in the titles of its articles. Each records a role. The **complex time** and **complex space** sectors are the two temporal directions and the two spatial blocks respectively, so named because they carry the temporal and the spatial part of the physical dictionary; the **real sector** is the part of the algebra free of the central $i$, carrying a Euclidean four-dimensional geometry in which no direction is singled out as time, which is what the Wick rotation produces, and the **imaginary sector** is its complement in the coefficient split, the part every coefficient of which carries the $i$; and the **informational sector** carries the Hermitian operators, states and observables, with signature $(1,3)$, while the **material sector** carries the four-positions and four-vectors, and its biquaternion norm has signature $(3,1)$.

**The collective names.** Two of the three decompositions of the algebra pair up the subspaces and give the pairs a name of their own. The first needs none beyond the names of its two members:

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})
$$

pairs the centre with the traceless part. The decomposition

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}
$$

is the real-and-imaginary split of the coefficients, and its two members are called the **real and imaginary halves** of the algebra: $\mathbb{H}_{\mathbb{B}}$, written with real coefficients throughout, and $i\mathbb{H}_{\mathbb{B}}$, written with purely imaginary ones. The third,

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-
$$

pairs the two sectors — in this series' usage, *the sectors*, without qualification, are these two, and it is the split the relativistic articles are written in terms of. The two pairings cross: no sector is a half, and each sector draws its scalar slot from one half and its vector slots from the other, as *The element and its coefficients* above records.

**The choice of which subspace is "real".** The convention that has to be flagged is that $\mathbb{M}_-$ is the *anti*-Hermitian subspace, so that the framework's "real" part is the part built on $i$ times a Hermitian element. The more familiar convention takes the Hermitian part as real. The two differ only by the central factor $i$, and there is no mathematical error either way: an anti-Hermitian generator is the standard choice for the Lie algebra of a unitary group, and it is $\mathbb{M}_-$ that carries that role here. What is unusual is that the convention is applied to the **field** rather than to the generators. Once it is, $\mathbb{M}_-$ is fixed by $\flat$ and $\mathbb{M}_+$ is not, and that is what makes $\mathbb{M}_-$ the framework's material subspace. A reader who "restores" the Hermitian convention will find the whole series inverted. Do not.

### The Idempotent Convention

The convention of *The element and its coefficients* fixes the case and the tilde of a generic element. The idempotents carry a symbol of their own, and the series uses it throughout.

An **idempotent** of the algebra is an element $\tilde{\Pi}$ with $\tilde{\Pi}^2 = \tilde{\Pi}$; a **projector** is a Hermitian idempotent, $\tilde{\Pi}^{*} = \tilde{\Pi}$, and the rank-one projectors of $\mathbb{M}_+$ are the **pure states** of the informational sector,

$$
\tilde{\Pi}_\pm(\hat{\mu}) = \tfrac{1}{2}\bigl(e_0 \pm i\,\hat{\mu}\bigr), \qquad \hat{\mu}\in\mathbb{R}^3,\ |\hat{\mu}| = 1 .
$$

A non-zero idempotent $\tilde{\Pi}$ generates the **minimal left ideal** $\mathbb{B}\tilde{\Pi}$, which is the state module of the companion articles; the classification of the idempotents, the polarisation identity, the Peirce decomposition and the projective geometry of the pure states are those of *Biquaternion Idempotents and Projections* and its companions in the mathematical corpus.

The upper-case tilde is therefore **split between two roles**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde{\Pi}$ | an idempotent, a projector or a pure state, and the minimal left ideal $\mathbb{B}\tilde{\Pi}$ it generates |
| $\tilde{P}$ | a four-momentum or four-vector, $\tilde{P} = m\tilde{U}$, and a *generic* element wherever a statement holds for every element |

The generic element keeps its $\tilde{P}$ in the statements that hold for all elements: the trace pairing $\mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{Q})$, the commutator bracket $[\tilde{P},\tilde{Q}] = \tilde{P}\tilde{Q} - \tilde{Q}\tilde{P}$, the general quaternionic bilinear form $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ and the multiplicativity $\langle\tilde{P}\tilde{Q},\tilde{P}\tilde{Q}\rangle_{\natural} = \langle\tilde{P},\tilde{P}\rangle_{\natural}\,\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$. The same letter is the four-momentum. Both roles are inherited from the mathematical corpus, where *Biquaternion Idempotents and Projections* writes the idempotent $\tilde{\Pi}$ and the generic element $\tilde{P}$ side by side.

The convention is one of **notation, not of substance**: an element written $\tilde{\Pi}$ is not a different kind of object from one written $\tilde{Q}$, only an element known to be idempotent, and the glyph records that knowledge at the point of use. Where a passage needs a generic idempotent variable it may write $\tilde{\Pi}$, and where it needs a generic element it writes $\tilde{P}$ or $\tilde{Q}$.

### The Four-Vector Representation

The algebra is read as the quadruple of its complex coefficients, in *The Four-Vector Element Representation of Biquaternions*. Each unit is one coordinate place,

$$
e_0 \longleftrightarrow (1,0,0,0), \qquad e_1 \longleftrightarrow (0,1,0,0), \qquad e_2 \longleftrightarrow (0,0,1,0), \qquad e_3 \longleftrightarrow (0,0,0,1),
$$

so that an element is its quadruple of coefficients,

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu \;\longleftrightarrow\; (Q^0, Q^1, Q^2, Q^3), \qquad Q^0 = Q_0, \quad (Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3),
$$

and the index is written in the upper position. **No index is raised or lowered anywhere in the series.** On $\mathbb{C}^4$ there is no pairing with which to move one, and the $ict$ convention is what puts the metric into the coefficient — $(ict, \mathbf{x})$ rather than a contraction rule — so that the interval is the sum of squares with no explicit scalar product. The article owns the product in components and the column-and-dual-row convention.

### The 4×4 Regular Matrix Representation

Multiplication is read as a linear map on that quadruple, in *The 4×4 Regular Matrix Element Representation of Biquaternions*. The four units act by

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

**The volume of the regular representation.** The regular matrix carries its own determinant, and it is the square of the norm: $\det\rho_L(\tilde{Q})=N(\tilde{Q})^{2}$, because the regular representation of $\mathbb{B}\cong M_2(\mathbb{C})$ on its own four complex dimensions is the tensor square of $\Phi$, $\rho_L\cong\Phi\otimes I_2$. The factor reflects the doubled carrier: each complex dimension of $\Phi$ appears twice, and so does the volume. The regular matrices of unit norm are therefore the volume-preserving linear maps of the doubled carrier, which is the group-theoretic form of the statement that a rotor acts on the algebra and on its matrix model with the same determinant. Recomputed on $100$ random elements: $\det\rho_L(\tilde{Q})=N(\tilde{Q})^{2}$ on $100$ of $100$.

### The 2×2 Matrix Representation

The algebra is read as the complex $2 \times 2$ matrices, under the isomorphism

$$
\Phi : \mathbb{B} \to M_2(\mathbb{C}),
$$

in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and this is the representation every numerical check in the series is performed with. The four unit images are fixed here, once, because every article depends on them agreeing. The three vector units are the Pauli matrices times $-i$:

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

**The determinant is the norm.** The determinant of the image is the biquaternion norm, $\det\Phi(\tilde{Q})=N(\tilde{Q})$, and it is **multiplicative**, $\det\Phi(\tilde{P}\tilde{Q})=N(\tilde{P})N(\tilde{Q})$; that is the matrix form of the norm's multiplicativity, and the reason the matrix model computes every norm in the series. Two corollaries are read here. The invertibility criterion is the nonsingularity of the image, so the group of units is the general linear group $\mathrm{GL}(2,\mathbb{C})$. The unit-norm elements form $\mathrm{SL}(2,\mathbb{C})$ in the matrix model, so the rotor group is the **volume-preserving** linear group and the norm is the volume form it preserves: a Lorentz transformation of the material sector is a determinant-one matrix. Recomputed on $100$ random elements: $\det\Phi(\tilde{Q})=N(\tilde{Q})$ on $100$ of $100$, and a unit-norm element has determinant one on $100$ of $100$.

**The assignment is forced, not chosen.** Neither the factor $i$ nor the sign in the three vector images could have been otherwise: $e_k^2 = -e_0$ requires the factor, and $e_1e_2 = e_3$ fixes the sign. A reviewer must not "correct" the assignment by making the three images real, nor by negating all three. *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* derives both.

**Never conjugate the matrix entries on their own.** Conjugating the entries of $\Phi(\tilde{Q})$ is *not* the image of any involution of the algebra: it negates the images of $e_1$ and $e_3$ while leaving $\Phi(e_2)$, which has real entries, untouched, and so it destroys the sector dictionary. The four conjugations $\natural$, $\bar{\phantom{Q}}$, ${}^{*}$ and $\flat$ are evaluated through the matrix formulas recorded in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, never by conjugating entries.

**The realisation is a convention of presentation, not of content.** The isomorphisms that preserve the subspace dictionary are the $\Phi' = S\Phi S^{-1}$ with $S$ unitary up to a nonzero complex scalar, and the scalar cancels in $S \cdot S^{-1}$. An arbitrary invertible $S$ destroys the dictionary, and so does a genuine squeeze $S = UP$ with $U$ unitary and $P$ positive definite and $\neq I$: both keep the centre, which is scalars, and neither preserves the quaternion subspace or either sector. The practical consequence is that a mistake of translation between the algebra and its matrices is repaired **here** — by correcting the assignment or the explicit factors of $i$ — and never by altering the biquaternion norm, the $ict$ assignment or the sector split.

**A bare $\Phi$ means this isomorphism and nothing else.** A plain $\Phi$, with no subscript, superscript or tilde, is reserved throughout the series for this isomorphism alone. The other uses a reader may meet are marked differently: $\varphi$ is an abstract homomorphism on the mathematics pages and an angle in the Thomas-precession exercise, $\tilde{\Phi} = \varphi\,e_0$ is the central scalar field of the Higgs articles, and $\Phi_{\tilde{U}}$ is the quantum channel of the gates article. None of these is the isomorphism, and a bare $\Phi$ is not any of them.

## The Spacetime Conventions

What remains are the conventions of the forms the physics is written with, once the coordinate dictionary of *The Six Subspaces* above has fixed which parameters carry $ict$ and $\mathbf{x}$ and which carry $ct'$ and $i\mathbf{x}'$. The basis $e_0, e_1, e_2, e_3$ and the $ict$ assignment are the conventions on which every relativistic article depends; the forms, the metric levels, the d'Alembertian and the mass term are the conventions built on them.

### The Involutions and the Four Forms

The algebra carries four conjugations, and on it there are four forms, indexed by a pair of maps, one in each slot of the pairing. One rule ties the two lists together, and that rule is what lets the series say which form is the metric and which is the inner product without having to choose.

**The setting.** $\mathbb{B}$ is a $\mathbb{C}$-algebra whose centre is $\mathbb{C}$, so every complex scalar is central, $\lambda\tilde{Q} = \tilde{Q}\lambda$ for all $\lambda \in \mathbb{C}$, which is the property that makes "$\mathbb{C}$-bilinear" well defined on $\mathbb{B}$; the scalar part $\mathrm{Sc}(\tilde{Q}) = \tilde{Q}_0$ is $\mathbb{C}$-linear. The centre is treated in *The Four Other Remarkable Subspaces*, §*The Complex Time Sector*, and the forms of the algebra in *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* and its mathematical twin *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and, on the side of positivity, in *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

**The rule.** A form reads a conjugation in each slot, so the rule is indexed by a pair: for $a$ in the first slot and $b$ in the second, put

$$
h_{a,b}(\tilde{P},\tilde{Q}) = \mathrm{Sc}\bigl(\tilde{P}^{a}\tilde{Q}^{b}\bigr), \qquad a \in \{\mathrm{id},{}^{\natural}\}, \quad b \in \{\mathrm{id},{}^{*}\}.
$$

The scalars are central and $\mathrm{Sc}$ is $\mathbb{C}$-linear, so the type of $h_{a,b}$ over $\mathbb{C}$ is decided by the $\mathbb{C}$-linearity of the maps entering the two slots; both first-slot maps are $\mathbb{C}$-linear, so the type is decided by $b$ alone:

$$
h_{a,\mathrm{id}} \ \ \mathbb{C}\text{-bilinear}, \qquad h_{a,{}^{*}} \ \ \mathbb{C}\text{-sesquilinear}.
$$

A $\mathbb{C}$-linear $b$ carries a scalar out of the second slot without conjugating it, $h_{a,\mathrm{id}}(\tilde{P},\lambda\tilde{Q}) = \lambda h_{a,\mathrm{id}}(\tilde{P},\tilde{Q})$, while $b = {}^{*}$ conjugates it, $h_{a,{}^{*}}(\tilde{P},\lambda\tilde{Q}) = \bar\lambda h_{a,{}^{*}}(\tilde{P},\tilde{Q})$; in the first slot no scalar is conjugated, $h_{a,b}(\lambda\tilde{P},\tilde{Q}) = \lambda h_{a,b}(\tilde{P},\tilde{Q})$.

**The four conjugations.** The tensor product $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is built from two rings that each carry two involutions, the identity and the conjugation, so it carries $2\times 2 = 4$, together with the derived anti-Hermitian sign:

| Map | Mark | Action | As a ring map | Over $\mathbb{C}$ |
|---|---|---|---|---|
| identity | — | $\tilde{Q} \mapsto \tilde{Q}$ | automorphism | $\mathbb{C}$-linear |
| complex conjugation | $\bar{\cdot}$ | $Q_\mu \mapsto \bar{Q}_\mu$ | **automorphism**: conjugation on the scalars, identity on the quaternion factor | $\mathbb{C}$-antilinear |
| quaternion conjugation | ${}^{\natural}$ | $Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$ | **anti-automorphism**: identity on the scalars, conjugation on the quaternion factor | $\mathbb{C}$-linear |
| Hermitian conjugation | ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ | $\bar{Q}_0e_0 - \bar{Q}_1e_1 - \bar{Q}_2e_2 - \bar{Q}_3e_3$ | **anti-automorphism** | $\mathbb{C}$-antilinear |
| anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | $-\tilde{Q}^{*}$ | **neither** | $\mathbb{C}$-antilinear |

The fourth column is what the two questions separate, and it is worth stating plainly because the two are easy to conflate. The bar multiplies and reverses nothing, $\overline{\tilde{P}\tilde{Q}} = \bar{\tilde{P}}\bar{\tilde{Q}}$, since it acts on the scalars and on nothing else: it is an order-two automorphism of the algebra over $\mathbb{R}$, $\mathbb{C}$-antilinear, and **not** an anti-automorphism. The natural sign and the star are the two genuine **involutions of the ring** in the strict sense, $(\tilde{P}\tilde{Q})^a = \tilde{Q}^a\tilde{P}^a$. Which of the four multiplies and which reverses is decided by which factor of the tensor product the map touches, the quaternion conjugation being the reversing one. The anti-Hermitian sign is neither: it reverses with a twist, $(\tilde{P}\tilde{Q})^{\flat} = -\tilde{Q}^{\flat}\tilde{P}^{\flat}$, so it is an involution of the underlying real vector space and nothing more. The four maps and the sign, their fixed and anti-fixed spaces, and the lattice they form are the subject of *Comparison of the Six Subspaces*.

**The four forms.** Reading the rule off the table gives exactly four forms, one for each pair $(a,b)$, written in the mathematics articles with one bracket $\langle\cdot,\cdot\rangle$ whose subscript records the pair, the natural conjugation ${}^{\natural}$ for a non-identity first slot and the star ${}^{*}$ for a non-identity second slot, and carrying the short names $B$ (the general plain bilinear), $N$ (the general quaternionic bilinear), $H$ (the general plain sesquilinear, the Hermitian form) and $K$ (the general quaternionic sesquilinear, the Krein form),

$$
\begin{aligned}
B(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle &= \mathrm{Sc}(\tilde{P}\tilde{Q}) = P_0Q_0 - P_1Q_1 - P_2Q_2 - P_3Q_3,\\
N(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{\natural} &= \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}) = P_0Q_0 + P_1Q_1 + P_2Q_2 + P_3Q_3,\\
H(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{*} &= \mathrm{Sc}(\tilde{P}\tilde{Q}^{*}) = P_0\bar{Q}_0 + P_1\bar{Q}_1 + P_2\bar{Q}_2 + P_3\bar{Q}_3,\\
K(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{\natural*} &= \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}) = P_0\bar{Q}_0 - P_1\bar{Q}_1 - P_2\bar{Q}_2 - P_3\bar{Q}_3.
\end{aligned}
$$

each being the trace form of its own pair up to the factor of the trace convention, $2h_{a,b}(\tilde{P},\tilde{Q}) = \mathrm{Tr}(\tilde{P}^{a}\tilde{Q}^{b})$, with the four rows read off in the order $(a,b) = (\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$. Their types and their readings on the algebra and on the material sector are then:

| Form | Definition | Pair $(a,b)$ | Type over $\mathbb{C}$ | On $\mathbb{B}$ | On $\mathbb{M}_-$ |
|---|---|---|---|---|---|
| $B = \langle\tilde{P},\tilde{Q}\rangle$, the general plain bilinear form | $\mathrm{Sc}(\tilde{P}\tilde{Q})$ | $(\mathrm{id},\mathrm{id})$ | $\mathbb{C}$-**bilinear** | complex, Gram $\mathrm{E}$ | $-c^2t^2-x^2-y^2-z^2$, signature $(0,4)$ |
| $N = \langle\tilde{P},\tilde{Q}\rangle_{\natural}$, the general quaternionic bilinear form | $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})$ | $({}^{\natural},\mathrm{id})$ | $\mathbb{C}$-**bilinear** | complex, Gram $I_4$ | $-c^2t^2+x^2+y^2+z^2$, signature $(3,1)$ |
| $H = \langle\tilde{P},\tilde{Q}\rangle_{*}$, the general plain sesquilinear form | $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$ | $(\mathrm{id},{}^{*})$ | $\mathbb{C}$-**sesquilinear**, positive definite | signature $(8,0)$ | $c^2t^2+x^2+y^2+z^2$, signature $(4,0)$ |
| $K = \langle\tilde{P},\tilde{Q}\rangle_{\natural*}$, the general quaternionic sesquilinear form | $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*})$ | $({}^{\natural},{}^{*})$ | $\mathbb{C}$-**sesquilinear**, indefinite | signature $(2,6)$ | $c^2t^2-x^2-y^2-z^2$, signature $(1,3)$ |

Each pairing has its quadratic form on the diagonal, and the four norms are then:

| Norm | Definition | Value |
|---|---|---|
| $\langle\tilde{Q},\tilde{Q}\rangle$, the general plain bilinear algebraic norm | $\mathrm{Sc}(\tilde{Q}\tilde{Q})$ | $Q_0^2 - Q_1^2 - Q_2^2 - Q_3^2$ |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, the general quaternionic bilinear algebraic norm | $\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$ |
| $\langle\tilde{Q},\tilde{Q}\rangle_{*}$, the general plain sesquilinear algebraic norm | $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})$ | $\lvert Q_0\rvert^2 + \lvert Q_1\rvert^2 + \lvert Q_2\rvert^2 + \lvert Q_3\rvert^2$ |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}$, the general quaternionic sesquilinear algebraic norm | $\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q}^{*})$ | $\lvert Q_0\rvert^2 - \lvert Q_1\rvert^2 - \lvert Q_2\rvert^2 - \lvert Q_3\rvert^2$ |

Four readings follow, and the names of the involutions must not be allowed to settle them in advance.

**The general plain bilinear form, from the identity.** $\langle\tilde{P},\tilde{Q}\rangle = \mathrm{Sc}(\tilde{P}\tilde{Q}) = P_0Q_0 - P_1Q_1 - P_2Q_2 - P_3Q_3$ is the scalar part of the plain product, the form of the identity conjugation, and it is the fourth form that the older count of three passed over. Its Gram matrix in the complex basis is $\mathrm{E} = \operatorname{diag}(1,-1,-1,-1)$, its signature on $\mathbb{B}$ is $(4,4)$, and on the material sector it is the **negative** Euclidean square,

$$
\langle\tilde{T},\tilde{T}\rangle = -(c^2t^2+x^2+y^2+z^2), \qquad \tilde{T} = ict\,e_0 + \mathbf{x},
$$

of signature $(0,4)$. It is the form of the plain product, and it differs from the general quaternionic bilinear form by the sign of the vector part alone, $\langle\tilde{P},\tilde{Q}\rangle = \mathrm{Sc}(\tilde{P}\tilde{Q})$ against $\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$.

**The general quaternionic bilinear form, from the natural sign.** $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ is the $\mathbb{C}$-**bilinear** form associated with the biquaternion norm, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$ (*Biquaternion Norm and Invertibility*); it is level 1 of the metric below, and its Gram matrix in the complex basis $e_0,e_1,e_2,e_3$ is the identity. Its diagonal is generally complex, so it carries no positivity and is no analytic norm; its unit group is the set of elements of norm one, $\{\tilde{\Lambda} : \langle\tilde{\Lambda},\tilde{\Lambda}\rangle_{\natural} = 1\}$, which is $\mathrm{SL}(2,\mathbb{C})$ — the norm is the determinant of the matrix realization — the group the notation table calls the Lorentz group on $\mathbb{M}_-$. It is the form of symmetry and duality.

**The general plain sesquilinear form, from the star.** $\langle\tilde{P},\tilde{Q}\rangle_{*} = \mathrm{Sc}(\tilde{P}\tilde{Q}^{*}) = P_0\bar{Q}_0 + P_1\bar{Q}_1 + P_2\bar{Q}_2 + P_3\bar{Q}_3$ is the form the series calls the Hermitian form, the *different* object of the level-1 caution below. It is genuinely positive definite, real with $\langle\tilde{Q},\tilde{Q}\rangle_{*} = \lvert Q_0\rvert^2 + \lvert Q_1\rvert^2 + \lvert Q_2\rvert^2 + \lvert Q_3\rvert^2$ strictly positive for $\tilde{Q} \neq 0$, and it is the internal Hilbert-space structure that the Born rule and the unitary evolution use; its isometry group is $\{\tilde{U} : \tilde{U}^{*}\tilde{U} = e_0\} = U(2)$, the unitary slice of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*. On the material sector it is the **Euclidean** square, $\langle\tilde{T},\tilde{T}\rangle_{*} = c^2t^2+x^2+y^2+z^2$.

**The general quaternionic sesquilinear form, from the bar.** $\langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}) = P_0\bar{Q}_0 - P_1\bar{Q}_1 - P_2\bar{Q}_2 - P_3\bar{Q}_3$ is real on the diagonal and indefinite, of signature $(2,6)$ on $\mathbb{B}$. On the material sector it is the negative of the biquaternion norm,

$$
\langle\tilde{T},\tilde{T}\rangle_{\natural*} = c^2t^2 - x^2 - y^2 - z^2 = -\langle\tilde{T},\tilde{T}\rangle_{\natural}, \qquad \tilde{T} = ict\,e_0 + \mathbf{x},
$$

so the four forms read on the material sector are the interval $\langle\tilde{T},\tilde{T}\rangle_{\natural}$ of level 2, its negative, the Euclidean square and its negative. A space carrying a definite form and the form $\langle\cdot,\cdot\rangle_{\natural*}$ in this relation is a **Krein space**, and this form is accordingly the **Krein form** of the algebra: the definite form is the Hilbert structure, the Krein form the physical metric, and the passage between them is the fundamental symmetry below. The name is Mark Grigorievich Krein's (1907–1989), not Felix Klein's. The framework's own indefinite object at levels 1 and 2 is the biquaternion norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$; the last two forms are recorded here because they complete the classification, and because they are what the plain product and the bar, and not the star, produce. Its isometry group is the Pin group, the companion of the unitary slice that is the group of the star form. The Witt classes of the four forms, their isometry groups, and their reading as Hermitian forms over the algebra with respect to their own involutions are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**The fundamental symmetry.** The two sesquilinear forms are related by the natural sign:

$$
\langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \langle\tilde{P}^{\natural},\tilde{Q}\rangle_{*}, \qquad J = {}^{\natural}, \qquad J^2 = \mathrm{id}, \qquad J \ \ \mathbb{C}\text{-linear}, \qquad \langle J\tilde{P},\tilde{Q}\rangle_{*} = \langle\tilde{P},J\tilde{Q}\rangle_{*},
$$

so $J$ is a $\mathbb{C}$-linear involution and is self-adjoint for the positive form. That is exactly the **fundamental symmetry** of a Krein space, the data of an indefinite-metric space with a definite form attached: the Krein form is the definite one with the sign twisted by $J$, the two are simultaneously diagonal in the basis adapted to the sectors, and the pair $(\langle\cdot,\cdot\rangle_{*}, J)$ is equivalent to the pair $(\langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural*})$. On the material sector $J$ is the spatial reflection, $J = \mathrm{diag}(+1,-1,-1,-1)$ in the basis $ie_0, e_1, e_2, e_3$, which is the sign pattern of the $ict$ metric $\eta$ read with the opposite overall sign.

**Why the general quaternionic bilinear form is bilinear, computed.** Three ingredients are used in each slot, and all three are $\mathbb{C}$-linear: the natural sign, $(\lambda\tilde{R})^{\natural} = \lambda\tilde{R}^{\natural}$; the centrality of $\mathbb{C}$ in $\mathbb{B}$, $\lambda\tilde{X} = \tilde{X}\lambda$; and the scalar part, $\mathrm{Sc}(\lambda\tilde{X}) = \lambda\,\mathrm{Sc}(\tilde{X})$. In the first slot,

$$
\langle\lambda\tilde{P},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}\bigl(\lambda\tilde{P}\tilde{Q}^{\natural}\bigr) = \lambda\,\mathrm{Sc}\bigl(\tilde{P}\tilde{Q}^{\natural}\bigr) = \lambda\,\langle\tilde{P},\tilde{Q}\rangle_{\natural},
$$

and in the second,

$$
\langle\tilde{P},\lambda\tilde{Q}\rangle_{\natural} = \mathrm{Sc}\bigl(\tilde{P}(\lambda\tilde{Q})^{\natural}\bigr) = \mathrm{Sc}\bigl(\tilde{P}\lambda\tilde{Q}^{\natural}\bigr) = \lambda\,\mathrm{Sc}\bigl(\tilde{P}\tilde{Q}^{\natural}\bigr) = \lambda\,\langle\tilde{P},\tilde{Q}\rangle_{\natural},
$$

so a scalar pulls out of both slots without conjugation and the general quaternionic bilinear form is $\mathbb{C}$-bilinear. For the two sesquilinear forms the same computation conjugates $\lambda$ in the second slot, $\langle\tilde{P},\lambda\tilde{Q}\rangle_{*} = \mathrm{Sc}\bigl(\tilde{P}\bar\lambda\tilde{Q}^{*}\bigr) = \bar\lambda\,\langle\tilde{P},\tilde{Q}\rangle_{*}$, so those two are linear in the first slot and sesquilinear in the second. The bilinearity of the general quaternionic bilinear form is therefore not a convention that could have been made differently: it is the exact consequence of the $\mathbb{C}$-linearity of the natural sign together with the centrality of $\mathbb{C}$ in $\mathbb{B}$, which is the point the Krein form makes from the other side.

### The Physical Reading of the Four Forms

The four forms are read as four physical structures, and the readings, with the two algebras and the two sesqualgebras, are collected in *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*; here they are named once, with the article that owns each. The **general plain bilinear form** is the *composition* of two operations, the form of the plain product, and its reading is *Why the Material Composition Is Oriented and Cannot Measure*; the **general quaternionic bilinear form** is the *interval*: the polar form of the biquaternion norm, the metric of the material sector of signature $(3,1)$, its zero set the light cone and its norm the mass (*Mass, Rank and the Positivity of the Dagger*); the **general plain sesquilinear form** is the *probability*: the Born pairing of a state and an observable, positive definite, the form the trace formula and the unitary evolution use (*The Born Rule as a Trace Formula*); the **general quaternionic sesquilinear form** is the *gauge calibration*: the indefinite Krein pairing the gauge side carries, real on the diagonal and unable to normalise a state (*Why the Fourth Product Is a Gauge Structure and Not a State Space*).

Three statements belong to the reading and are carried by none of its four entries alone. **The readings are bound to the sectors.** On $\mathbb{M}_-$ the interval is the metric, of signature $(3,1)$, and the probability form is the Euclidean square; on $\mathbb{M}_+$ the probability is the Born pairing and the interval is the mirror form, indefinite of signature $(1,3)$, its one positive direction the temporal one. The four forms read on the six subspaces at once are *The Six Subspaces and the Four Forms*. **The central imaginary sorts the four forms into two classes.** Multiplication by $i$ reverses the sign of the two bilinear forms, $\langle i\tilde{P},i\tilde{Q}\rangle = -\langle\tilde{P},\tilde{Q}\rangle$ and $\langle i\tilde{P},i\tilde{Q}\rangle_{\natural} = -\langle\tilde{P},\tilde{Q}\rangle_{\natural}$, and leaves the two sesquilinear forms unchanged, $\langle i\tilde{P},i\tilde{Q}\rangle_{*} = \langle\tilde{P},\tilde{Q}\rangle_{*}$ and $\langle i\tilde{P},i\tilde{Q}\rangle_{\natural*} = \langle\tilde{P},\tilde{Q}\rangle_{\natural*}$; the metric and the composition therefore move with the Wick exchange and the probability and the gauge calibration do not. **A change of the local complex structure moves the same pair.** The complex structure of the algebra is fixed and the embedding of the algebra in physical spacetime is not: in a material medium the map from physical time to the imaginary scalar direction carries the local scale $c = 1/\sqrt{\epsilon\mu}$, and this is the sense in which the complex structure is *local* (*Electromagnetism in Media — The Local Complex Structure at Work*). A change of the local complex structure meets the four forms as the central imaginary does — it reverses the sign of the two bilinear forms and leaves the two sesquilinear forms unchanged — and it leaves the zero-divisor cone one locus of the algebra while the physical wave cone the cone corresponds to moves with $c$. The invariant content of the framework is therefore the sesquilinear pair, the probability and the gauge calibration, together with the cone; the interval and the composition are the frame-dependent pair, their sign and their normalisation being data of the local complex structure rather than of the algebra. The vacuum is the limiting member of the family, and the two sectors are the limiting case of the same statement, a change of frame between them being a central rotation. **A symmetric pairing is not automatically a metric, and an indefinite form is not a state space.** The metric of the flat framework is $\langle\cdot,\cdot\rangle_{\natural}$ on $\mathbb{M}_-$, and the only one of the four forms that defines normalisable states is the positive one (*The States the Indefinite Metric Cannot Normalise*). The companion statements on the subspaces, with the area pairing and the two times, are *The Four Other Remarkable Subspaces*.

**The two sesquilinear forms are two pairings of the state side, and they differ in what they can measure.** The plain sesquilinear form is positive definite and pushes down to the rays of the state module, so it is the form a **probability** is read with: the transition weight between two states is the modulus squared of its normalised value, and its projective invariants are the ones a measurement uses (*The Born Rule as a Trace Formula*, *The Pancharatnam Phase and the Geometric Phase in Biquaternionic Form*). The quaternionic sesquilinear form is indefinite and does not push down to the rays; it is a **calibration** rather than a probability, real on the diagonal of the sector it is read on and unable to assign a positive weight to every nonzero state, and it is the form a gauge fixing uses (*Why the Fourth Product Is a Gauge Structure and Not a Metric*). The distinction is exactly the definiteness of the level-2 form on the state sector: a probability is available where the form is definite and only a calibration where it is indefinite. Recomputed on $100$ random informational elements: the plain sesquilinear form is positive definite on the state sector and the quaternionic one takes both signs, on $100$ of $100$.

### The Metric: Three Levels

The word "metric" appears at three distinct levels in the series, and most of the disagreements below are the result of the levels being conflated. They are separated here in order of priority, because the first is the convention of the framework and the third is only a convention of translation.

**Level 1 — the biquaternion norm on $\mathbb{B}$.** The algebra carries the complex-linear biquaternion norm

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu=0}^{3} Q_\mu^2 ,
$$

and with all four coefficients $Q_\mu$ complex its Gram matrix is the **identity**:

$$
\mathrm{diag}(+1,+1,+1,+1).
$$

This is the metric of the biquaternion universe, and it is the framework's primary convention. It is a metric **on $\mathbb{C}$** — a $\mathbb{C}$-bilinear form — and read that way every one of its four entries is positive: on $\mathbb{B}$ there is no minus sign in the form itself, and none is needed. That is precisely what the complex coefficients buy. A *real* direction has to be labelled positive or negative in advance, and that labelling becomes a convention that can be chosen wrongly; a complex coefficient carries its own sign in the coefficient, so all four directions can start out on an equal footing and no such commitment is required. Two cautions about reading it. It is not positive definite and it is not a norm in the analytic sense — it vanishes on the nonzero zero divisors, which is why $\mathbb{B}$ is not a normed division algebra. And the Hermitian form $\lvert Q_0\rvert^2 + \lvert Q_1\rvert^2 + \lvert Q_2\rvert^2 + \lvert Q_3\rvert^2$ is a *different* object: real-valued, positive definite, and $\mathbb{C}$-antilinear in its first argument. It is used only where a positive-definite inner product on a complex vector space is needed, and it is not the biquaternion norm of the algebra. The forms of the algebra, with the involution that produces each, are classified in *The Involutions and the Four Forms* above.

**Level 2 — the real sectors.** A minus appears only once a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$. The two four-dimensional real sectors are exactly such choices, and the same level-1 form reads off differently on each:

| Sector | Basis | The norm on the basis | Signature |
|---|---|---|---|
| $\mathbb{M}_-$ (material) | $ie_0,\ e_1,\ e_2,\ e_3$ | $-1,+1,+1,+1$ | $(-,+,+,+)$ |
| $\mathbb{M}_+$ (informational) | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $+1,-1,-1,-1$ | $(+,-,-,-)$ |

Throughout the series a signature is written $(p,q)$ with the **positive** directions counted first, so that the two rows above are $(3,1)$ for $\mathbb{M}_-$ and $(1,3)$ for $\mathbb{M}_+$. The parenthetical count and the $(\pm)$ string are two writings of one fact, $(3,1) = (-,+,+,+)$ and $(1,3) = (+,-,-,-)$, and are never to be read against one another. A group name is not ordered this way, since $\mathrm{O}(3,1)$ and $\mathrm{O}(1,3)$ are two names of one group; the series accordingly writes the Lorentz group indifferently as $\mathrm{SO}(3,1)$ or $\mathrm{SO}^+(1,3)$.

Read as a statement about **objects** rather than directions: an element of $\mathbb{M}_-$ carries the metric $(-,+,+,+)$, and an element of $\mathbb{M}_+$ carries $(+,-,-,-)$. This is not a separate choice made sector by sector — it is the one level-1 form read on two different real bases, and the two readings are mirror images of one another through the identity below.

The Minkowski interval is not postulated at this level either. It is the level-1 form read on the material sector with the time coordinate written $ict$: the four-position is $\tilde{Q} = ict\,e_0 + \mathbf{x}$, whose scalar coefficient $ict$ is imaginary, and

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = (ict)^2 + x^2 + y^2 + z^2 = -c^2t^2 + \mathbf{x}^2 ,
$$

with the minus arising from $i^2 = -1$ alone. Multiplication by $i$ exchanges the sectors, $i\mathbb{M}_+ = \mathbb{M}_-$, and reverses the sign of the form, $\langle i\tilde{Q},i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$; the mirror relation between the two signatures is that identity. The Lorentzian signature is therefore an *output* of the biquaternion conventions, not an input to them. **The exchange read as a clock.** The same identity has a reading in time. The two times are the real and the imaginary parts of one central coordinate, $z = ct' + i\,ct$, and multiplication by $i$ is the quarter turn of that plane, so the material time and the informational time exchange roles and each sector is read against the phase of the other. The exchange fixes the reference and the period and not the arrow — it is invertible and of order four, and which of the two slices is physical is a choice of axis — and the reading is central and global, so it is silent on the relative rates of clocks in relative motion, which are the business of *The Relativistic Exchange of Information and Clock Synchronisation in Biquaternionic Form*. The generator is read in *The Central Rotation: Phase, Duality and the Wick Rotation as One Generator*, and the clock reading in *Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*.

For contractions of four-vectors in the $ict$ coordinate the series writes this level-2 form as

$$
\eta = \mathrm{diag}(-1,+1,+1,+1),
$$

and at this level the series is uniform: the $ict$ metric is $(-,+,+,+)$ throughout. The two articles outside the relativistic core that carry a symbol $g = \mathrm{diag}(-1,+1,+1,+1)$ — the companion articles on the Higgs mechanism and on the Newman–Penrose formalism — mean **this** object, the $ict$-coordinate metric for index contractions, and not a Clifford metric, as their own notation tables state. They are not part of the level-3 disagreement below.

**Level 3 — the Clifford metric of the $\gamma^\mu$.** When the series writes gamma matrices it needs a further symbol $g$, defined by $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$. This is a property of the chosen generators and not of the biquaternion algebra, and it is best regarded as a **tool** rather than a convention: it can be used or not, depending on the situation, and where it is used it should not dictate any convention of the framework. The biquaternion formulation requires no gamma matrices; they are a translation into the language of the standard Dirac literature, convenient when comparing with that literature or borrowing a standard result, and dispensable otherwise. The freedom this level carries is exactly the freedom the framework treats as presentation: replacing every generator by $i\gamma^\mu$ takes $g$ to $-g$ and leaves the biquaternion algebra, the biquaternion norm, the sector split, the chirality operator and the whole of levels 1 and 2 invariant.

The value the series now uses is the standard **mostly-minus**

$$
g = \mathrm{diag}(+1,-1,-1,-1),
$$

so that $(\gamma^0)^2 = +I_4$ and $(\gamma^k)^2 = -I_4$. Two reasons fix it. First, **it is the form of the objects the tool represents**: the Clifford vectors correspond to the *Hermitian* subspace $\mathbb{M}_+$ — the dictionary's own identification is $x_\mu\gamma^\mu = \gamma^0\Phi(w)$ with $w \in \mathbb{M}_+$ — and $(+,-,-,-)$ is the $\mathbb{M}_+$ form, so the square of a Clifford vector agrees with the biquaternion norm of the biquaternion it represents with **no relative sign**. Second, it is the standard particle-physics convention, so articles transcribing standard results inherit the standard sign without adjustment, and the name $\mathrm{Cl}_{1,3}$ is correct in the usual counting, $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$.

The opposite sign, $g = \mathrm{diag}(-1,+1,+1,+1)$, is **not in use**. It pairs the generators with the material sector, which is a real form they do not belong to; the price is a relative minus sign between the square of a Clifford vector and the biquaternion norm of the biquaternion it represents, a mixed sign pattern in the timelike bivectors, and a non-standard naming of the algebra. It is recorded here only because the series used it previously, in the article that defines the gamma matrices and the Dirac equation, in the Dirac-algebra dictionary, and in the corresponding mathematics article on the Clifford realization of the algebra; those have been aligned to the value above.

A difference at this level would **not** be an error at level 1 or level 2, and half the reason for separating the levels is to stop it being read as one: the biquaternion norm, the $ict$ metric and the sector structure are the same for either sign. The sign decides only which *real* Clifford form the generators generate — $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ for $(+,-,-,-)$, $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ for $(-,+,+,+)$ — and the even subalgebra, which is $\mathbb{B}$ itself, is the same for both, so no dictionary entry and no biquaternion identity depends on it.

The order of authority is therefore one-way. The algebra and its level-1 and level-2 conventions are the framework; the gamma matrices and their metric are a translation of it, adopted per article for whatever the article is doing. The tool serves the framework and not the reverse: a Clifford computation is never a reason to change a biquaternion convention, and where the two appear to disagree, the disagreement is in the translation and is resolved by adjusting the generators, the adjoint, or the explicit factors of $i$ — never by altering the biquaternion norm, the $ict$ assignment, or the sector split.

One consequence does reach the physics, and it is the only place where a level-3 choice is not free. The Dirac adjoint is $\bar{\psi} = \psi^\dagger\gamma^0$, so it carries $\gamma^0$ and changes with the convention. With the mostly-minus generators $\bar{\psi}\gamma^0\psi = +\psi^\dagger\psi$, the positive number density; with the mostly-plus generators the same expression gives $-\psi^\dagger\psi$. A spinor bilinear written as $\bar{\psi}\Gamma\psi$ therefore requires the adjoint to be defined consistently with the generators in use. No article in the series currently writes a spinor bilinear in the mostly-plus convention, so no statement in the series is in error on this count; the point is recorded so that one is not introduced. This sign is not part of the freedom that $\gamma^\mu \mapsto i\gamma^\mu$ leaves behind.

**The levels are also distinguished by the law the form obeys.** Beyond their sign, the levels differ in what they do under a product. The level-1 norm is **multiplicative**, $N(\tilde{P}\tilde{Q})=N(\tilde{P})N(\tilde{Q})$, so its level sets multiply and the unit-norm elements form a group; the level-2 interval inherits this multiplicativity on the material sector, which is why a Lorentz transformation preserves the interval and why the rotors are exactly the unit-norm elements. The level-2 Euclidean square and the level-3 Clifford metric are **not** multiplicative, and the positivity of the Hermitian form is what replaces multiplicativity on the state side: the Born weight is not a product of weights but the trace of a product, a pairing rather than a homomorphism. A form that multiplies gives a group of isometries; a form that does not gives a pairing and a Born rule. Recomputed on $100$ random pairs: the norm is multiplicative on $100$ of $100$, and the sesquilinear square fails multiplicativity on $100$ of $100$.

### The d'Alembertian

The series' d'Alembertian is built from the **biquaternionic gradient**

$$
\tilde{\nabla} = e_0\frac{\partial}{\partial Q_0} + e_1\frac{\partial}{\partial Q_1} + e_2\frac{\partial}{\partial Q_2} + e_3\frac{\partial}{\partial Q_3} = \sum_{\mu=0}^{3} e_\mu\frac{\partial}{\partial Q_\mu}
$$

and its **quaternion conjugate**

$$
\tilde{\nabla}^{\natural} = e_0\frac{\partial}{\partial Q_0} - e_1\frac{\partial}{\partial Q_1} - e_2\frac{\partial}{\partial Q_2} - e_3\frac{\partial}{\partial Q_3},
$$

the involution of the norm. It is this conjugate and no other that the series composes with (*Biquaternion Analysis*, §*The Biquaternionic Gradient*, §*The Quaternion Conjugate of the Gradient* and §*The d'Alembertian*), and the two orders agree:

$$
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \frac{\partial^2}{\partial Q_0^2} + \Delta_Q ,
$$

the whole of it **scalar**: it multiplies by $e_0$ and acts coefficient by coefficient, $\Box\tilde{F} = \sum_\mu(\Box F_\mu)e_\mu$, and it is the norm of the gradient, $\Box = \langle\tilde{\nabla},\tilde{\nabla}\rangle_{\natural}$ (*Biquaternion Norm and Invertibility*). That formal expression is a **Euclidean** Laplacian in the coordinates $Q_\mu$; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. On the material sector $\mathbb{M}_-$, where $Q_0 = ict$ and $Q_k = q_k$, the derivative $\partial^2/\partial Q_0^2 = -c^{-2}\partial_t^2$ and the same operator reads

$$
\Box\big|_{\mathbb{M}_-} = \Delta - c^{-2}\partial_t^2 = \partial_{ict}^2 + \Delta ,
$$

a plus on the spatial part and a minus on the time part. On $\mathbb{M}_+$, where the imaginary coordinate is spacelike, the two signs are exchanged; on $\mathbb{H}_{\mathbb{B}}$, where every $Q_\mu$ is real, $\Box$ is the ordinary Euclidean four-dimensional Laplacian. **The $ict$ substitution — and with it the reading $\Box = \partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$ — is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial Q_0^2 + \Delta_Q$. On $\mathbb{M}_-$, where the series does its work, that reading is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series.

The operator is one, and every article writes it the same way. The Weyl-spinor exercise works in real time $x^0 = ct$ with the standard metric $(+,-,-,-)$; in those variables $\partial_{ict}^2 = -\partial_0^2$, so the same operator is

$$
\Box = \partial_{ict}^2 + \Delta = -\partial_0^2 + \nabla^2 ,
$$

and the mass equation is the series equation $\left(\Box - m^2c^2/\hbar^2\right)\psi = 0$. **No article of the series defines a second d'Alembertian**, and no mass-term sign is left to a local convention.

## The Dirac Mass Term: the Linear, Chirality-Off-Diagonal Convention

### The Convention

The biquaternionic Dirac equation for a **massless** field is

$$
\tilde{\nabla}\tilde{\Psi} = 0 ,
$$

which is identical in form to the source-free biquaternion Maxwell equation. For a field of mass $m$ the equation is **linear** in the field and **off-diagonal between the chiralities**. Writing $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$, the massive equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
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
\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat , \qquad \tilde{\Psi}^\flat = -\tilde{\Psi}^{*} ,
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
\tilde{\Psi}^\flat = -\tilde{\Psi}^{*} = -\overline{\tilde{\Psi}^{\natural}}
$$

is the **anti-Hermitian conjugation**. It is not merely a sign variant of ${}^{*}$; it has its own algebraic character:

- it is a $\mathbb{C}$-**antilinear** involution, $(\alpha\tilde{A} + \beta\tilde{B})^\flat = \bar{\alpha}\tilde{A}^\flat + \bar{\beta}\tilde{B}^\flat$;
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

$\flat$ is **not** the charge conjugation either. It has the **shape** of a charge-conjugation pairing — it pairs an element with its own conjugate — but the operation called charge conjugation is the conjugate-linear pseudoautomorphism $\bar A=\Pi A^{*}\Pi^{-1}$, whose module form is $C[\psi]=i\gamma^{2}\psi^{*}$, and the operation is owned by *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*. The four levels of the name — the algebra's real structure $\flat$, the Clifford pseudoautomorphism, the module operation $C$, and the module real structure $\bar{\cdot}$ — are tabulated in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*.

**$\flat$ and the Klein four.** The four involutions $\{1,\bar{\cdot},{}^{\natural},{}^{*}\}$ form a **Klein four group** under composition, and $\flat=-{}^{*}$ is the **fourth character** and not a fourth element: it is minus the star, the star composed with the central sign, and its fixed space is the material sector. The correction matters because $\flat$ is often met as if it were an independent involution. It is not, and the four characters on the four coordinate blocks are the corpus's discrete-symmetry labels, with parity, time reversal and charge conjugation read as three of the four. Recomputed on the four basis blocks: the four involutions give four independent sign patterns and $\flat$ gives the pattern $+,-,+,-$, the fourth character, distinct from the other three and equal to minus the star's pattern. The owners are *Relations Between Subspaces* for the Klein four and the block characters, and *The Centre of the Biquaternion Algebra as the Classical Sector* for the two $\mathbb{Z}_2$ decompositions that cannot be aligned.

## Physical Readings

The article can also be read as the dictionary that says where each physical reading is taken. The three levels of the word metric are three physical jobs and not three objects: the complex-linear norm on $\mathbb{B}$ is the universal form of the algebra, the level-2 form on the real sectors is the interval with its signature, and the level-3 form is a convention of translation into the gamma-matrix literature. The freedom of level 3 and the freedom of a change of the local complex structure are then one statement read at two levels: neither moves the algebra, and both are movements of the embedding rather than of the physics. Five further readings of the conventions can be named.

- **Trace-factor-two reading.** The factor $\mathrm{Tr}(e_0)=2$ of the trace convention is read as the count of the two minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$, that is, of the two chiralities, so every pairing of the series carries the two-slot structure as a factor of two. Boundary: the factor is a property of the isomorphism $\Phi$, and the count is of ideals and not of particles.
- **Signature-dial reading.** The fundamental symmetry $J={}^{\natural}$ is read as the signature dial: the indefinite form of the Krein pair is the definite form with its sign twisted by $J$, so the signature of the physical metric is data of one involution of the algebra and not an independent input. Boundary: $J$ is the fundamental symmetry of the pair of forms, and the reading does not claim that it selects the sector, which is fixed by $\flat$.
- **Norm-as-scale-and-mass reading.** The biquaternion norm is complex on the algebra and real on the material sector, where it is the interval; its value on a four-momentum is the mass, and its modulus is what a conformal (Weyl) rescaling acts on, a change of the unit of length. Because the local complex structure fixes $c=1/\sqrt{\epsilon\mu}$, a medium rescales the norm while leaving the sesquilinear pair and the cone's algebraic locus untouched: the norm is read as the local scale, and the mass as its material value. Boundary: the norm is indefinite and its value is not a probability; the owners are *Biquaternion Norm and Invertibility*, *The Local Complex Structure and the Speed of Light* and *Electromagnetism in Media — The Local Complex Structure at Work*.
- **Inertia reading.** A signature is not decoration: the inertia of a form — how many positive, negative and null directions it admits — is what decides how many timelike, spacelike and null directions the theory that uses the form has, and the four forms of the algebra therefore carry four different physical direction-counts. The classifier is *Inertia and the Witt Invariant: What a Signature Allows a Spectrum to Carry*, and the same form read on the six subspaces is *The Six Subspaces and the Four Forms*. Boundary: the reading counts directions of a form and does not assign a particle to each.
- **Which null set is the cone.** The word *cone* in the series is the zero set of the norm, $N(\tilde{Q})=0$, equivalently the set of zero divisors, equivalently $\det\Phi(\tilde{Q})=0$; it is not the zero set of the general plain bilinear form. On the material sector the latter is negative definite, $\mathrm{Sc}(\tilde{T}\tilde{T})=-(c^{2}t^{2}+\lvert\mathbf x\rvert^{2})$, so a nonzero real four-vector is never null for it — verified on $100$ lightlike material elements, all of which have $\lvert\mathrm{Sc}(\tilde{T}\tilde{T})\rvert$ bounded away from zero while $N(\tilde{T})=0$. What ends at the cone is invertibility: $N(\tilde{Q})=0$ is exactly the condition that the acting map $L_{\tilde Q}$ has no inverse, so $c$ names an algebraic boundary of the composition and not a state. Boundary: the cone is invariant under a change of the local complex structure, which moves the physical wave cone it corresponds to together with $c$; the owner is *Biquaternion Norm and Invertibility*, with the interval reading in *The Interval as the Square and the Charge of the Material Composition*.

## Summary

The conventions of the series fall into two groups.

**Algebraic.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, over complex coefficients. The scalar unit $i$ is central, which is what makes the central phase the algebra's continuous symmetry. The conjugations cut the algebra into six real subspaces: the two-dimensional centre subspace $\mathbb{C}_{\mathbb{B}}$; the six-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$; and four distinguished four-dimensional ones, named $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$. Each carries its own real parameters and its own slice of the coordinate dictionary, with $q'_0 = ct$, $q_0 = ct'$, $(q_1,q_2,q_3) = (x,y,z)$ and $(q'_1,q'_2,q'_3) = (x',y',z')$. With complex coefficients the biquaternion norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$ is the identity matrix on $\mathbb{B}$; its Minkowski signature appears only on the real sectors, and the $i$ is what supplies the minus. The algebra carries four forms, not two: the general plain bilinear form, from the identity; the $\mathbb{C}$-bilinear polar form of the norm, from the $\mathbb{C}$-linear natural sign; the positive-definite Hermitian form, from the star; and the Krein form, from the bar, each classified by the $\mathbb{C}$-linearity of the involution that produces it. The matrix representation $\Phi$ is fixed by its four basis images, with the Hermitian units following as $\Phi(ie_k) = i\,\Phi(e_k)$; the residual freedom is a unitary change of basis of $\mathbb{C}^2$ and nothing further, so the sector dictionary cannot be altered by re-choosing it. The algebra has three representations — the coefficient quadruple, the regular matrix, and the matrix image $\Phi$ — each developed in its own article, and it is the trace of $\Phi$ that the series calls the trace.

**Spacetime and fields.** The material coordinate is $\tilde{Q} = ict\,e_0 + \mathbf{x}$, using the $ict$ convention so that the Minkowski interval is the biquaternion norm, of signature $(3,1)$, vanishing on the zero-divisor cone. The $ict$ metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$. The series d'Alembertian is $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_0^2 + \Delta_Q$, read on the material sector as $\partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$, and written by the Weyl-spinor exercise in real time as $-\partial_0^2 + \nabla^2$; every article uses this one operator, with the mass equation $\left(\Box - m^2c^2/\hbar^2\right)\psi = 0$. The Clifford metric $g$ is a level-3 tool rather than a convention, adopted where an article translates into gamma matrices, and its value is the standard mostly-minus $\mathrm{diag}(+1,-1,-1,-1)$ throughout the series — the $\mathbb{M}_+$ form, since the Clifford vectors correspond to the Hermitian subspace, so that the square of a Clifford vector agrees with the biquaternion norm of the biquaternion it represents with no relative sign. The opposite sign is not in use. Where an article that does not translate into gamma matrices nevertheless writes a coordinate metric $g_{\mu\nu}$ as the relativity text does — *The Higgs Mechanism in Biquaternionic Form* and *The Newman–Penrose Formalism in Biquaternionic Form* do — the object written is the level-2 $ict$ metric of this page, $\mathrm{diag}(-1,+1,+1,+1)$, under the relativity text's symbol, and not the level-3 tool, which is $\mathrm{diag}(+1,-1,-1,-1)$: the levels are told apart by the article's own statement of which one it uses, never by the letter. Either way the biquaternion norm, the $ict$ metric and the sector structure are unchanged, and the tool never dictates them. The Dirac mass term is **linear and chirality-off-diagonal**, $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$; it conserves the vector $U(1)$ and breaks the axial symmetry. The retired antilinear form $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ was retired for its spacelike dispersion, and $\flat = -{}^{*}$ is retained as the algebra's real structure.

The theme is single. In a framework whose algebra and sector assignment are non-standard, the most likely error is a correction of something that is deliberate. The conventions recorded above are the places where that is most likely to happen.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q}$ | An element of the algebra. The same symbol serves for the general element and for an element of any of the subspaces, whichever the passage at hand is about; the complex coefficients are $Q_\mu$, the real parameters of a four-dimensional subspace are $q_\mu$ and $q'_\mu$, the prime marking the slot that carries the $i$. |
| $\tilde{\Pi}$ | An idempotent, projector or pure state, $\tilde{\Pi}^2 = \tilde{\Pi}$, and the minimal left ideal $\mathbb{B}\tilde{\Pi}$ it generates; a four-momentum and a generic element keep $\tilde{P}$ (see *The Idempotent Convention*) |
| $\tilde{Q}^{\natural}, \bar{\tilde{Q}}, \tilde{Q}^{*}, \tilde{Q}^{\flat}$ | Quaternion (the natural sign), complex, Hermitian and anti-Hermitian conjugation |
| $\tilde{Q}^{\natural} \mapsto \epsilon M^{\mathsf T}\epsilon^{-1}$, $\bar{\tilde{Q}} \mapsto \epsilon\overline{M}\epsilon^{-1}$ | The two conjugations dressed by the antisymmetric form; $\epsilon = \Phi(-e_2)$ |
| $\tilde{Q}^{*} \mapsto M^\dagger$, $\tilde{Q}^\flat \mapsto -M^\dagger$ | The two undressed ones. Entrywise conjugation of $M$ alone is not the image of any involution |
| $\flat = -{}^{*}$ | The anti-Hermitian conjugation, the algebra's real structure |
| $\mathbb{C}_{\mathbb{B}} = \{Q_0 e_0\}$ | Centre subspace, fixed points of quaternion conjugation; the centre of $\mathbb{B}$ and the complex time sector; parameters $q_0, q'_0$ with $q_0 = ct'$ and $q'_0 = ct$ |
| $\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\}$ | The vector subspace, i.e. the complex space sector: anti-fixed points of quaternion conjugation, real dimension six; parameters $q_k, q'_k$ with $(q_k) = (x,y,z)$ and $(q'_k) = (x',y',z')$. Equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, i.e. the real sector (the real half): fixed points of complex conjugation, all four coefficients real; a subalgebra, and the home of the rotation rotors |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion subspace, i.e. the imaginary sector (the imaginary half): anti-fixed points of complex conjugation, all four coefficients purely imaginary; a module over $\mathbb{H}_{\mathbb{B}}$, not a subalgebra. $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, a split that crosses the $\mathbb{M}_\pm$ split |
| $\mathbb{M}_+ = \{ \tilde{Q} : \tilde{Q}^{*} = \tilde{Q} \}$ | Hermitian subspace, the informational sector; basis $e_0, ie_1, ie_2, ie_3$, parameters $q_0, q'_1, q'_2, q'_3$ (real), with $q_0 = ct'$ |
| $\mathbb{M}_- = \{ \tilde{Q} : \tilde{Q}^\flat = \tilde{Q} \}$ | Anti-Hermitian subspace, the material sector; basis $ie_0, e_1, e_2, e_3$, parameters $q'_0, q_1, q_2, q_3$ (real), with $q'_0 = ct$ |
| $\tilde{Q} = ict\,e_0 + \mathbf{x}$ | The material coordinate, $\mathbf{x} = x e_1 + y e_2 + z e_3$ |
| $(ct')\,e_0 + i\mathbf{x}'$ | The informational coordinate, $\mathbf{x}' = x' e_1 + y' e_2 + z' e_3$; the temporal coefficient $ct'$ is real and the spatial ones imaginary, the mirror of the material coordinate |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$ | Biquaternion norm; identity matrix $\mathrm{diag}(+1,+1,+1,+1)$ as a metric on $\mathbb{C}$ (level 1), signature $(3,1)$ on $\mathbb{M}_-$ (level 2) and $(1,3)$ on $\mathbb{M}_+$ |
| $B = \langle\tilde{P},\tilde{Q}\rangle = \mathrm{Sc}(\tilde{P}\tilde{Q}) = P_0Q_0 - P_1Q_1 - P_2Q_2 - P_3Q_3$ | The general plain bilinear form, the form of the plain product and of the identity conjugation; Gram matrix $\mathrm{E}$; signature $(4,4)$ on $\mathbb{B}$ and $(0,4)$ on $\mathbb{M}_-$ |
| $N = \langle\tilde{P},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}) = P_0Q_0 + P_1Q_1 + P_2Q_2 + P_3Q_3$ | The general quaternionic bilinear form, the form of the norm, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$; unit group $\mathrm{SL}(2,\mathbb{C})$ |
| $H = \langle\tilde{P},\tilde{Q}\rangle_{*} = \mathrm{Sc}(\tilde{P}\tilde{Q}^{*}) = P_0\bar{Q}_0 + P_1\bar{Q}_1 + P_2\bar{Q}_2 + P_3\bar{Q}_3$ | The general plain sesquilinear form, the positive-definite Hermitian form of the star, signature $(8,0)$ on $\mathbb{B}$ and $(4,0)$ on $\mathbb{M}_-$; unit group $U(2)$; the internal Hilbert-space structure |
| $K = \langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}) = P_0\bar{Q}_0 - P_1\bar{Q}_1 - P_2\bar{Q}_2 - P_3\bar{Q}_3$ | The general quaternionic sesquilinear form, the indefinite Krein form of the bar; signature $(2,6)$ on $\mathbb{B}$ and $(1,3)$ on $\mathbb{M}_-$; $\langle\tilde{T},\tilde{T}\rangle_{\natural*} = -\langle\tilde{T},\tilde{T}\rangle_{\natural}$ on $\mathbb{M}_-$ |
| $J = {}^{\natural}$ | The fundamental symmetry, $\langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \langle\tilde{P}^{\natural},\tilde{Q}\rangle_{*}$, $J^2 = \mathrm{id}$, $\mathbb{C}$-linear and self-adjoint for $\langle\cdot,\cdot\rangle_{*}$ |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric, signature $(-,+,+,+)$ (level 2) |
| $g$ | Clifford metric of the $\gamma^\mu$ (level 3); an optional tool, not a framework convention. $\mathrm{diag}(+1,-1,-1,-1)$ throughout — the $\mathbb{M}_+$ form, matching the objects the tool represents |
| $\tilde{\nabla} = \sum_{\mu=0}^{3} e_\mu\partial/\partial Q_\mu$, $\tilde{\nabla}^{\natural} = e_0\partial/\partial Q_0 - e_k\partial/\partial Q_k$ | Biquaternionic gradient and its quaternion conjugate, the two factors of the d'Alembertian |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_0^2 + \Delta_Q$ | The d'Alembertian, a scalar operator; on the material sector it reads $\partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$, the series convention |
| $\mathrm{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ | Trace pairing, unrestricted; the case $\tilde{P}\in\mathbb{M}_+$, $\tilde{Q}\in\mathbb{M}_+$ is the real one. $\mathrm{Tr}(e_0) = 2$ |
| $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ | The matrix representation, with $\Phi(e_0) = I_2$ and $\Phi(e_k)$ as given above; the Hermitian units follow as $\Phi(ie_k) = i\,\Phi(e_k)$. Fixed up to a unitary change of basis, and no further |
| $Q^\mu$ | The coefficients of an element, in the upper position, $Q^0 = Q_0$ and $(Q^1,Q^2,Q^3) = (Q_1,Q_2,Q_3)$; never raised or lowered, there being no metric on $\mathbb{C}^4$ |
| $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$ | Chiral decomposition of the Dirac field |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | The linear, chirality-off-diagonal mass term (canonical form) |
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
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), companion article, for the relations among the subspaces defined here — their coordinate blocks, intersections, spans, gradings and biquaternion norms.
- *The Four-Vector Element Representation of Biquaternions* (`articles_physics/the-four-vector-element-representation-of-biquaternions.md`), companion article, for the coefficient space, the column and the dual row, and the index that is never raised or lowered.
- *The 4×4 Regular Matrix Element Representation of Biquaternions* (`articles_physics/the-4x4-regular-matrix-element-representation-of-biquaternions.md`), companion article, for the two regular matrices, the relation between them, and the reduction into the two chiralities.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), companion article, for the isomorphism $\Phi$, the trace and the determinant, and the ideals as columns.
