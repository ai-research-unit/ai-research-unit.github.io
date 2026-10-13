# __Conventions in the Biquaternion Universe__

## Introduction

A framework built on a non-standard algebra, and on a non-standard choice of which part of it counts as "real", is a framework in which a reader will repeatedly find things that look wrong and are not. Two examples fix the idea. The series takes the **anti**-Hermitian subspace as the material sector, where the more familiar convention would take the Hermitian one. And the series' d'Alembertian carries a sign opposite to the one used in the articles on Weyl spinors. In both cases it is the "correction" that is the error.

This article states the conventions of the series, one to a section, and records the reason each was chosen. It states conventions only: the proofs, the properties and the physical readings of the objects it names belong to the articles cited beside them. It is meant to be read before any other article is edited, and its reader is anyone writing or revising an article of the series, for whom the conventions are load-bearing — a change that looks local, a sign or a factor of $i$, generally propagates into a dozen dependent articles.

The article is ordered as a dictionary of a single object, each section stated after the one it depends on. First the object and its writing: the algebra and its basis, then the element and its coefficients. Then its parts: the four involutions, the remarkable subspaces they cut out, and the coordinate dictionary and the sector names those subspaces carry. Then what is done with the object: the twelve products, the four forms $B,N,H,K$ that are their scalar parts and the four norms read on the diagonal, named by the generic Form and the generic Norm, and the restrictions of the central map, which the norms and the forms make precise. Then the three distinguished elements — the root, the idempotent and the nilpotent — whose glyphs the series writes. Then the three presentations of the same object, the four-vector, the 4×4 regular and the 2×2 element representation with its trace. Last the conventions a field equation inherits, the gradient and its d'Alembertian, closed by the algebra's real structure $\flat$.

The word *metric* is used at three levels in the series — the biquaternion norm, the two real sectors with their $ict$ metric, and the Clifford tool — and the distinction between them is set out in *The Four Forms, the Four Algebraic Norms and the Change of Scalars*, together with the one-way rule that the Clifford tool is a translation of the algebra and never a reason to change it.

One warning applies throughout. **A convention recorded here is not a claim that the alternative is wrong.** Several of these choices are freely made where either choice would be defensible; they are conventions, not theorems. What is not free is *consistency*: once a convention is fixed, the dependent articles inherit it, and a change to it is a change to all of them. Where a convention is instead forced — where the alternative leads to a demonstrable contradiction — the article says so explicitly, and that distinction is the difference between a convention and a result.

## The Algebra and Its Basis

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

replaces the four complex coefficients by **eight real parameters**: $q_\mu$ is the real part of $Q_\mu$, the coefficient of $e_\mu$, and $q'_\mu$ its imaginary part, the coefficient of $ie_\mu$, so the prime marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and the remarkable subspaces below are what the eight parameters are grouped into. The full set of parametrisations, and the two conventions they embody, are in *The Element and Its Coefficients* and *Remarkable Subspaces* below; nothing in them changes the split stated here.

One structural fact governs the whole series, so it is worth isolating. **The scalar unit $i$ is central**: it commutes with every element of $\mathbb{B}$, because it belongs to the $\mathbb{C}$ factor of the tensor product, while the quaternion units belong to the $\mathbb{H}$ factor. Multiplication by a *central* phase $e^{i\alpha}$ therefore commutes with every operator constructed from the algebra — in particular with the biquaternionic gradient $\tilde{\nabla}$ — and this is why the central phase is the algebra's natural continuous symmetry. The articles on Noether's theorem and the gauge principle rest on it.

The split is also a split of **roles**, and the two roles belong to the two **factors** of the tensor product and cannot be exchanged. The central unit $i$ is the scalar imaginary: it is what enters the phase $e^{iS/\hbar}$, and it multiplies a whole element from inside the centre. The three units $e_1,e_2,e_3$ are the vector directions: they are the relativistic and rotational structure, and they enter through the quaternion factor. A central scalar and a vector direction are different kinds of object — one commutes with everything, the other rotates — so no product of the four general products may read $i$ through the quaternion direction or a unit through the scalar one. The mirror statement, that the two conjugations act on the two factors separately, is the subject of *The Four General Products and Their Physical Readings*.

As a complex algebra $\mathbb{B}$ is isomorphic to the full matrix algebra,

$$
\mathbb{B} \cong M_2(\mathbb{C}),
$$

and this identification is used constantly. It is fixed by a single isomorphism, written $\mathsf{M}_2$; its four basis images, and the rule that neither the factor $i$ nor the sign is a free choice, are stated in *The 2×2 Matrix Representation* below, and the development of the representation — the general element, the remarkable subspaces as matrices, the conjugations, the trace and the determinant — is in the companion article *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. Its two **minimal left ideals** are the algebra's two chiralities; the spinor module and the mass term a field equation builds on that structure are the subject of *The Dirac Equation in Biquaternionic Form*.

## The Element and Its Coefficients

The case and the tilde of the glyph are fixed first, and the element is written after. A generic element is preferably written so that the glyph alone identifies its algebra, two features being read together: the **case** separates a real scalar from a complex one, and a **tilde** marks the quaternionic factor.

| System | Name | Generic element | Scalar–vector decomposition | Coefficients |
|---|---|---|---|---|
| $\mathbb{C}$ | Complex numbers | $A = a + ia'$ | Scalar $a$, vector $ia'$ | Real, $a, a'$ |
| $\mathbb{H}$ | Quaternions | $\tilde q = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$ | $q_0e_0 + \mathbf q$, $\mathbf q = q_1e_1 + q_2e_2 + q_3e_3$ | Real |
| $\mathbb{B}$ | Biquaternions | $\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ | $Q_0e_0 + \mathbf Q$, $\mathbf Q = Q_1e_1 + Q_2e_2 + Q_3e_3$, $Q_\mu\in\mathbb{C}$ | Complex, $Q_\mu = q_\mu + iq'_\mu$ |

Four rules are read off the table. **A complex element carries a majuscule**, $A$, the case naming the scalar sector: an upper-case glyph has a scalar sector larger than the reals, a lower-case one has the reals. **The second coordinate of a complex element carries a prime**, $A = a + ia'$. And **the quaternionic elements carry a tilde**: lower case for the quaternions, $\tilde q$, and upper case for the biquaternions, $\tilde Q$. Finally, **the element is a scalar part plus a vector part**: the scalar part is carried by the unit — $1$ in $\mathbb{C}$, $e_0$ in $\mathbb{H}$ and $\mathbb{B}$ — and the vector part by the remaining basis directions, assembled in the bold letter $\mathbf q$ or $\mathbf Q$, so that $\tilde Q = Q_0e_0 + \mathbf Q$ with $\mathbf Q = Q_1e_1 + Q_2e_2 + Q_3e_3$ and $Q_\mu = q_\mu + iq'_\mu$.

The notation of this article already reads through the convention: the coefficients $q_\mu$ are real, the coefficients $Q_\mu = q_\mu + iq'_\mu$ are complex, and a general element of $\mathbb{B}$ is written $\tilde Q$.

**The generic element and the four-momentum share the letter $\tilde{P}$.** A statement that holds for every element is written with $\tilde{P}$ or $\tilde{Q}$ — the trace pairing $\mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{Q})$, the commutator bracket $[\tilde{P},\tilde{Q}] = \tilde{P}\tilde{Q} - \tilde{Q}\tilde{P}$, the general quaternionic bilinear form $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ and the multiplicativity $\langle\tilde{P}\tilde{Q},\tilde{P}\tilde{Q}\rangle_{\natural} = \langle\tilde{P},\tilde{P}\rangle_{\natural}\,\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ — and the same letter names a four-momentum or four-vector, $\tilde{P} = m\tilde{U}$. Both roles are inherited from the mathematical corpus, where *Idempotents of the General Plain Algebra* writes the generic element $\tilde{P}$ beside the idempotent $\tilde{\Pi}$.

**What the prime marks.** The prime belongs to the **coefficients**, not to the physical coordinates. The four coefficients of a general element are complex, and writing each as a real part plus $i$ times a real part,

$$
Q_\mu = q_\mu + iq'_\mu, \qquad q_\mu, q'_\mu \in \mathbb{R}, \qquad \mu = 0, 1, 2, 3,
$$

gives $q_\mu$ as the coefficient of $e_\mu$ and $q'_\mu$ as the coefficient of $ie_\mu$ — the same rule for every $\mu$:

| Coefficient | Real part | Attached to | Imaginary part | Attached to |
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

## The Conjugations and the Adjoint

The biquaternion algebra carries four natural involutions, all of them used in the series, together with
the adjoint of an operator, which belongs to the operators and not to the algebra:

| Map | Mark | What it is |
|---|---|---|
| Complex conjugation | $\bar{\cdot}$ | The involution of the base, extended to the element |
| Quaternion conjugation | ${}^{\natural}$ | The intrinsic conjugate: it fixes the scalars and negates the vectors |
| Hermitian conjugation | ${}^{*}$ | The involution of the algebra, $\bar{\cdot}\circ{}^{\natural}$ |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | The negative of the star |
| Operator adjoint | ${}^{\dagger}$ | The adjoint of an operator, $(L_a)^{\dagger} = L_{a^{*}}$ |

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

**The biquaternion norm.** The natural sign carries the algebra's **biquaternion norm**,

$$
N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 ,
$$

used throughout the series and read on the four forms and their norms in §*The Involutions and the Four Forms* and §*The Four Algebraic Norms* below. It is **multiplicative** and complex-valued in general, and it is not an analytic norm; its unit group and its invertibility reading are *Biquaternion Norm and Invertibility*.

Each of the four involutions has a fixed space, and each of these is one of the **remarkable subspaces** of the algebra. Which involution defines which subspace, and which of them are anti-fixed, is recorded with the subspaces themselves, in *The Remarkable Subspaces* below.

## The Remarkable Subspaces

The eight real parameters of a general element group into **remarkable subspaces**: the centre, the vector subspace, the two halves of the coefficient split, and the two sectors. Each is cut out by a conjugation:

| Subspace | Defining condition | Dimension over $\mathbb{R}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $\tilde{Q}^{\natural} = \tilde{Q}$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $\bar{\tilde{Q}} = \tilde{Q}$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$, the antiquaternion subspace | $\bar{\tilde{Q}} = -\tilde{Q}$ | $4$ |
| $\mathbb{M}_+$, the Hermitian subspace | $\tilde{Q}^{*} = \tilde{Q}$ | $4$ |
| $\mathbb{M}_-$, the anti-Hermitian subspace | $\tilde{Q}^{\flat} = \tilde{Q}$ | $4$ |

The basis of each, the coefficients it takes and the physical coordinates those carry are the table of §*The Coordinate Dictionary and the Sector Names*.

**Compact and non-compact directions.** A direction is **compact** when the one-parameter group it generates is a circle and **non-compact** when it is a hyperbola. The three real vector units $e_1,e_2,e_3$ generate the compact directions, the three imaginary units $ie_1,ie_2,ie_3$ the non-compact ones, and the complex vector subspace carries both. The Lie algebra this gives is *Angular Momentum and the Lie Algebra of the Material Sector*.

The subspaces are treated one by one in the owner articles: $\mathbb{C}_{\mathbb{B}}$ in *Other Remarkable Subspaces*, §*The Complex Time Sector*; $\mathrm{Vect}(\mathbb{B})$ in §*The Complex Space Sector*; $\mathbb{H}_{\mathbb{B}}$ in §*The Real Sector*; $i\mathbb{H}_{\mathbb{B}}$ in §*The Imaginary Sector*; and the two sectors in *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*.

## The Coordinate Dictionary and the Sector Names

The dictionary between the parameters and the physical coordinates is fixed once and for all,

$$
q'_0 = c\,t, \qquad (q_1, q_2, q_3) = (x, y, z), \qquad q_0 = c\,t', \qquad (q'_1, q'_2, q'_3) = (x', y', z'),
$$

with $\mathbf{x} = x e_1 + y e_2 + z e_3$ the real spatial vector and $i\mathbf{x}' = i x' e_1 + i y' e_2 + i z' e_3$ its imaginary counterpart. The **material coordinate** $\tilde{Q} = ict\,e_0 + \mathbf{x}$ and the **informational coordinate** $\tilde{Q} = ct'\,e_0 + i\mathbf{x}'$ are the two ends of it, and each subspace keeps whichever part of the dictionary its defining condition leaves free.

| Subspace | Algebraic name | Physical name | Basis | Real parameters | Physical coordinates |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | The centre | Complex time sector | $e_0,\ ie_0$ | $q_0,\ q'_0$ | $ct',\ ict$ |
| $\mathrm{Vect}(\mathbb{B})$ | Vector | Complex space sector | $e_1,\ e_2,\ e_3,\ ie_1,\ ie_2,\ ie_3$ | $q_1,\ q_2,\ q_3,\ q'_1,\ q'_2,\ q'_3$ | $x,\ y,\ z,\ ix',\ iy',\ iz'$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion | Real sector | $e_0,\ e_1,\ e_2,\ e_3$ | $q_0,\ q_1,\ q_2,\ q_3$ | $ct',\ x,\ y,\ z$ |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion | Imaginary sector | $ie_0,\ ie_1,\ ie_2,\ ie_3$ | $q'_0,\ q'_1,\ q'_2,\ q'_3$ | $ict,\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_+$ | Hermitian | Informational sector | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $q_0,\ q'_1,\ q'_2,\ q'_3$ | $ct',\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_-$ | Anti-Hermitian | Material sector | $ie_0,\ e_1,\ e_2,\ e_3$ | $q'_0,\ q_1,\ q_2,\ q_3$ | $ict,\ x,\ y,\ z$ |

Each subspace carries an **algebraic name**, taken from the involution that defines it, and a **physical name**, taken from the role it plays; the companion articles are titled by the physical name.

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

pairs the two sectors — in this series' usage, *the sectors*, without qualification, are these two, and it is the split the relativistic articles are written in terms of. The two pairings cross: no sector is a half, and each sector draws its scalar slot from one half and its vector slots from the other, as *The Element and Its Coefficients* above records.

**The choice of which subspace is "real".** The convention that has to be flagged is that $\mathbb{M}_-$ is the *anti*-Hermitian subspace, so that the framework's "real" part is the part built on $i$ times a Hermitian element, where the more familiar convention takes the Hermitian part as real. The two differ only by the central factor $i$, and there is no mathematical error either way. What is unusual is that the convention is applied to the **field** rather than to the generators. Once it is, $\mathbb{M}_-$ is fixed by $\flat$ and $\mathbb{M}_+$ is not, and that is what makes $\mathbb{M}_-$ the framework's material subspace. A reader who "restores" the Hermitian convention will find the whole series inverted. Do not.

## The Twelve Products and Their Names

The algebra carries **four general products** — one to each of the four choices of the two slots, the first factor read as it stands or through ${}^{\natural}$ and the second as it stands or through ${}^{*}$ — and each of the four splits into a **symmetric part** and an **antisymmetric part**, so that the complex space carries **twelve products** in all. The names are these, with the three-letter code the band articles write them by:

| The general product | Its symmetric part | Its antisymmetric part |
|---|---|---|
| The general plain bilinear product ($\mathrm{GPA}$) | The symmetric plain bilinear product ($\mathrm{SPA}$) | The antisymmetric plain bilinear product ($\mathrm{APA}$) |
| The general quaternionic bilinear product ($\mathrm{GQA}$) | The symmetric quaternionic bilinear product ($\mathrm{SQA}$) | The antisymmetric quaternionic bilinear product ($\mathrm{AQA}$) |
| The general plain sesquilinear product ($\mathrm{GPS}$) | The symmetric plain sesquilinear product ($\mathrm{SPS}$) | The antisymmetric plain sesquilinear product ($\mathrm{APS}$) |
| The general quaternionic sesquilinear product ($\mathrm{GQS}$) | The symmetric quaternionic sesquilinear product ($\mathrm{SQS}$) | The antisymmetric quaternionic sesquilinear product ($\mathrm{AQS}$) |

**The code is read letter by letter.** The first letter says which of the three operations of a row — $\mathrm G$ the general product, $\mathrm S$ its symmetric part, $\mathrm A$ its antisymmetric part; the second says which of the two products — $\mathrm P$ the plain one, whose first slot is read as it stands, and $\mathrm Q$ the quaternionic one, whose first slot carries ${}^{\natural}$; and the third says the family — $\mathrm A$ the **algebra** over $\mathbb{C}$, whose three products are $\mathbb{C}$-bilinear, and $\mathrm S$ the **sesqualgebra** over $(\mathbb{C},\bar{\cdot})$, whose three products are sesquilinear. The four general products are the multiplications of the four general structures of the band; the eight parts are the symmetric and antisymmetric products beside them; and the twelve codes together name the twelve algebraic structures of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The products themselves — their coordinates, their laws, their units and their images — are *The 12 Products of the Biquaternion Complex Space*, and the grid of the four general products is *The Four General Products and the Degree-2 Forms of the Biquaternion Space*.

## The Involutions and the Four Forms

The algebra carries four conjugations, and on it there are four forms, indexed by a pair of maps, one in each slot of the pairing. One rule ties the two lists together, and that rule is what lets the series say which form is the metric and which is the inner product without having to choose.

**The setting.** $\mathbb{B}$ is a $\mathbb{C}$-algebra whose centre is $\mathbb{C}$, so every complex scalar is central, $\lambda\tilde{Q} = \tilde{Q}\lambda$ for all $\lambda \in \mathbb{C}$, which is the property that makes "$\mathbb{C}$-bilinear" well defined on $\mathbb{B}$; the scalar part $\mathrm{Sc}(\tilde{Q}) = \tilde{Q}_0$ is $\mathbb{C}$-linear. The centre is treated in *Other Remarkable Subspaces*, §*The Complex Time Sector*, and the forms of the algebra in *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* and its mathematical twin *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and, on the side of positivity, in *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

**The definition of a form.** A form reads a conjugation in each slot, so the definition is indexed by a pair: for $a$ in the first slot and $b$ in the second,

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
| Identity | — | $\tilde{Q} \mapsto \tilde{Q}$ | Automorphism | $\mathbb{C}$-**linear** |
| Complex conjugation | $\bar{\cdot}$ | $Q_\mu \mapsto \bar{Q}_\mu$ | **Automorphism**: conjugation on the scalars, identity on the quaternion factor | $\mathbb{C}$-**antilinear** |
| Quaternion conjugation | ${}^{\natural}$ | $Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$ | **Anti-automorphism**: identity on the scalars, conjugation on the quaternion factor | $\mathbb{C}$-**linear** |
| Hermitian conjugation | ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ | $\bar{Q}_0e_0 - \bar{Q}_1e_1 - \bar{Q}_2e_2 - \bar{Q}_3e_3$ | **Anti-automorphism** | $\mathbb{C}$-**antilinear** |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | $-\tilde{Q}^{*}$ | **Neither** | $\mathbb{C}$-**antilinear** |

The fourth column is what the two questions separate. The bar acts on the scalars and on nothing else, so it is an order-two automorphism, $\mathbb{C}$-antilinear and **not** an anti-automorphism. The natural sign and the star are the two genuine **involutions of the ring**, $(\tilde{P}\tilde{Q})^a = \tilde{Q}^a\tilde{P}^a$, the quaternion conjugation being the reversing one. The anti-Hermitian sign is neither: it reverses with a twist, $(\tilde{P}\tilde{Q})^{\flat} = -\tilde{Q}^{\flat}\tilde{P}^{\flat}$, so it is an involution of the underlying real vector space and nothing more. The four maps and the sign, their fixed and anti-fixed spaces, and the lattice they form are *Comparison of the Remarkable Subspaces*.

**The generic form.** The series writes a **generic form** $\mathrm{Form}(\tilde{P},\tilde{Q})$, the form of the statement at hand, of which the four below are the instances; the matching generic norm is stated with the norms in §*The Four Algebraic Norms*.

**The four forms.** Each of the four pairs gives one form. The four are written with the single bracket $\langle\cdot,\cdot\rangle$, whose subscript records the pair — nothing for $(\mathrm{id},\mathrm{id})$, ${}^{\natural}$ for $({}^{\natural},\mathrm{id})$, ${}^{*}$ for $(\mathrm{id},{}^{*})$ and $\natural*$ for $({}^{\natural},{}^{*})$ — and they carry the short names $B$, $N$, $H$ and $K$:

| Form | Pair $(a,b)$ | Definition | Type over $\mathbb{C}$ | Value on $\mathbb{M}_-$ |
|---|---|---|---|---|
| $B$, the general plain bilinear form | $(\mathrm{id},\mathrm{id})$ | $B(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle = \mathrm{Sc}(\tilde{P}\tilde{Q}) = P_0Q_0 - P_1Q_1 - P_2Q_2 - P_3Q_3$ | $\mathbb{C}$-**bilinear** | $-c^2t^2-x^2-y^2-z^2$, signature $(0,4)$ |
| $N$, the general quaternionic bilinear form | $({}^{\natural},\mathrm{id})$ | $N(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}) = P_0Q_0 + P_1Q_1 + P_2Q_2 + P_3Q_3$ | $\mathbb{C}$-**bilinear** | $-c^2t^2+x^2+y^2+z^2$, signature $(3,1)$ |
| $H$, the general plain sesquilinear form | $(\mathrm{id},{}^{*})$ | $H(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{*} = \mathrm{Sc}(\tilde{P}\tilde{Q}^{*}) = P_0\bar{Q}_0 + P_1\bar{Q}_1 + P_2\bar{Q}_2 + P_3\bar{Q}_3$ | $\mathbb{C}$-**sesquilinear** | $c^2t^2+x^2+y^2+z^2$, signature $(4,0)$ |
| $K$, the general quaternionic sesquilinear form | $({}^{\natural},{}^{*})$ | $K(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}) = P_0\bar{Q}_0 - P_1\bar{Q}_1 - P_2\bar{Q}_2 - P_3\bar{Q}_3$ | $\mathbb{C}$-**sesquilinear** | $c^2t^2-x^2-y^2-z^2$, signature $(1,3)$ |

Each is the trace form of its own pair up to the factor of the trace convention, $2h_{a,b}(\tilde{P},\tilde{Q}) = \mathrm{Tr}(\tilde{P}^{a}\tilde{Q}^{b})$, the rows being read in the order $(a,b) = (\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$.

Throughout the series a signature is written $(p,q)$ with the **positive** directions counted first, so that $(-,-,-,-)$ is $(0,4)$.

**Where the four are proved and named.** The classification of the four, their Gram matrices, their signatures, their isometry groups, their Witt classes, and their reading as Hermitian forms over the algebra with respect to their own involutions are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, with its twin *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*.

**What is forced and what is chosen.** The two bilinear forms are $\mathbb{C}$-bilinear in both slots and the two sesquilinear forms are linear in the first slot and sesquilinear in the second. That is not a choice but a consequence of the $\mathbb{C}$-linearity of the natural sign together with the centrality of $\mathbb{C}$ in $\mathbb{B}$; its verification is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. Multiplication by $i$ reverses the sign of the two bilinear forms and leaves the two sesquilinear forms unchanged, since the centrality of $i$ puts either a factor $i^2 = -1$ on both slots or on neither.

## The Four Algebraic Norms

**The definition of a norm.** The norm of a form is that form read at its two equal arguments,

$$
\mathrm{Norm}(\tilde{Q}) = \mathrm{Form}(\tilde{Q},\tilde{Q}) ,
$$

and the convention is one of **notation, not of substance**: the pair is the form and the norm of the statement at hand, and the four forms above and the four norms below are its instances.

**The four algebraic norms.** Each pair gives one norm, the diagonal of its form. **One letter, two arities:** a letter names the form when it carries two arguments and the algebraic norm when it carries one, so $B$ is the form $B(\tilde{P},\tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q})$ and the norm $B(\tilde{Q}) = B(\tilde{Q},\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle$, and the same holds for $N$, $H$ and $K$. Read with one argument, the value lies in $\mathbb{C}$ for the two bilinear norms and in $\mathbb{R}$ for the two sesquilinear norms, because a sesquilinear form has a real diagonal. The four names are those of the four forms with *algebraic norm* in place of *form*:

| Norm | Pair $(a,b)$ | Definition | Value | Value in |
|---|---|---|---|---|
| $B$, the general plain bilinear algebraic norm | $(\mathrm{id},\mathrm{id})$ | $B(\tilde{Q}) = B(\tilde{Q},\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle = \mathrm{Sc}(\tilde{Q}\tilde{Q})$ | $Q_0^2 - Q_1^2 - Q_2^2 - Q_3^2$ | $\mathbb{C}$ |
| $N$, the general quaternionic bilinear algebraic norm | $({}^{\natural},\mathrm{id})$ | $N(\tilde{Q}) = N(\tilde{Q},\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$ | $\mathbb{C}$ |
| $H$, the general plain sesquilinear algebraic norm | $(\mathrm{id},{}^{*})$ | $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{*} = \mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})$ | $\lvert Q_0\rvert^2 + \lvert Q_1\rvert^2 + \lvert Q_2\rvert^2 + \lvert Q_3\rvert^2$ | $\mathbb{R}$ |
| $K$, the general quaternionic sesquilinear algebraic norm | $({}^{\natural},{}^{*})$ | $K(\tilde{Q}) = K(\tilde{Q},\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural*} = \mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q}^{*})$ | $\lvert Q_0\rvert^2 - \lvert Q_1\rvert^2 - \lvert Q_2\rvert^2 - \lvert Q_3\rvert^2$ | $\mathbb{R}$ |

The third is also called the Hermitian algebraic norm and the fourth the Krein algebraic norm, and the four letters are the short names. The other sense of the word, the **topological norm**, is the square root of the definite one, $\lVert\tilde{Q}\rVert_E = \bigl(H(\tilde{Q})\bigr)^{1/2}$, and it is *The Norm Defined by a Form*.

## The Central Map and Its Restrictions

The scalar imaginary $i$ is central, so multiplication by it is **one** $\mathbb{C}$-linear map of the algebra, and the movements the series reads in four places are its restrictions to the subspaces. The generator satisfies $(ie_0)^2=-e_0$, so its powers close on four values and the group $e^{i\theta}e_0$ of the centre interpolates between them. The remarkable subspaces carry the restrictions.

| Subspace | $i\,\cdot$ | The name |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the complex time sector | Itself | The global phase |
| $\mathrm{Vect}(\mathbb{B})$, the complex space sector | Itself | The duality rotation |
| $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ | Each other | The Wick rotation |
| $\mathbb{M}_-$ and $\mathbb{M}_+$ | Each other | The material–informational exchange |

The rule that ties the names is a rule about the generator and not about the subspaces: the map is central, so it acts the same way in every subspace, and it is a scalar that acts through the centre and never through the quaternion directions; a non-central generator would give one rotation per carrier. It is a rotation and not a projection, a collapse or a measurement — a loss of information is a non-invertible map and belongs to *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*.

**The relation to the Wick rotation.** The coordinate continuation $t \mapsto -i\tau$ of *Interpretation of the Wick Rotation in the Biquaternion Universe*, and the two senses in which the series uses the phrase *Wick rotation* — the exchange of the real and imaginary sectors, on the whole element, and the continuation of the time coordinate, a relabeling of one coordinate — are set out there. The two share one generator and one temporal sign flip, and they are not the same map.

The phase gate of the gate articles is a rotation about $e_3$, a non-central generator, and it must not be identified with the central rotation.

## The Special Elements: Root, Idempotent and Nilpotent

### The Root Convention

The roots carry a symbol of their own, beside the idempotent $\tilde{\Pi}$ (§*The Idempotent Convention*) and the nilpotent $\tilde{\nu}$ (§*The Nilpotent Convention*): the **xi**, in the two cases.

A **root of $-1$** of the algebra is an element $\tilde{\Xi}$ with $\tilde{\Xi}^2 = -1$. More generally a **root of a central value** $\lambda$ is an element with $\tilde{\Xi}^2 = \lambda e_0$. The roots of the three central values $-1, 0, +1$ are those of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general root is that of *Square Roots of a General Element in the General Plain Algebra*; the roots the series uses are the roots of $-1$.

**The square is read in a named product**, the algebra product unless the statement names another, as for the nilpotents (§*The Nilpotent Convention*), and the class is relative to the product; the roots of a value in the four general products are those of *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The case rule splits the glyph, as it does in the mathematical corpus.** The roots of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde{\Xi}$, the glyph the series uses; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde{\xi}$; and those of the complex, split-complex and dual layers carry the plain capital, $\Xi$, no tilde being written where there is no quaternionic factor — the only tilde-free layer with a root of $-1$ being $\mathbb{C}$, whose two roots are the central $\pm i$. The series works in $\mathbb{B}$ and writes $\tilde{\Xi}$ throughout; the other two glyphs are the mathematical corpus's, and the layer fixes the glyph.

**The coordinates carry the letter of the root**: in $\mathbb{B}$ a root is $\tilde{\Xi} = \Xi_0e_0 + \Xi_1e_1 + \Xi_2e_2 + \Xi_3e_3$ with $\Xi_\mu = \xi_\mu + i\xi'_\mu$, its scalar part $\Xi_0$ and its vector part $\boldsymbol{\Xi} = \boldsymbol{\xi} + i\boldsymbol{\xi}'$.

**The subscript of a root is always numeric** where more than one occurs, as for the idempotents and the nilpotents, and a sign is never written as a subscript.

The root glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde{\Xi}$ | A root of $-1$ of the biquaternion or split-biquaternion layer |
| $\tilde{\xi}$ | A root of $-1$ of the quaternion or split-quaternion layer |
| $\Xi$ | A root of $-1$ of the complex, split-complex or dual layer, where no tilde is written |

The convention is one of **notation, not of substance**: an element written $\tilde{\Xi}$ is not a different kind of object from one written $\tilde{Q}$, only an element known to be a root of $-1$.

### The Idempotent Convention

The convention of *The Element and Its Coefficients* fixes the case and the tilde of a generic element. The idempotents carry a symbol of their own, and the series uses it throughout.

An **idempotent** of the algebra is an element $\tilde{\Pi}$ with $\tilde{\Pi}^2 = \tilde{\Pi}$; a **projector** is a Hermitian idempotent, $\tilde{\Pi}^{*} = \tilde{\Pi}$, and the rank-one projectors of $\mathbb{M}_+$ are the **pure states** of the informational sector.

**The case rule splits the glyph, as it does in the mathematical corpus.** The idempotents of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde{\Pi}$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde{\pi}$; and those of the complex, split-complex and dual layers carry the plain capital, $\Pi$, no tilde being written where there is no quaternionic factor. The series works in $\mathbb{B}$ and writes $\tilde{\Pi}$ throughout; the other two glyphs are the mathematical corpus's, and the layer fixes the glyph.

A non-zero idempotent $\tilde{\Pi}$ generates the **minimal left ideal** $\mathbb{B}\tilde{\Pi}$, which is the state module of the companion articles; the standard pair, the classification of the idempotents, the polarisation identity, the Peirce decomposition, the matrix units and the projective geometry of the pure states are those of *Idempotents of the General Plain Algebra* and its companions in the mathematical corpus.

**The subscript of an idempotent is always numeric**: a pair is $\tilde{\Pi}_1, \tilde{\Pi}_2$, a second pair in the same statement takes the next numbers, $\tilde{\Pi}_3, \tilde{\Pi}_4$, and the sign $\pm$ is never written as a subscript, a family indexed by a direction being written with its argument, $\tilde{\Pi}_{1,2}(\hat{\mu})$.

The idempotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde{\Pi}$ | An idempotent, a projector or a pure state of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde{\Pi}$ it generates |
| $\tilde{\pi}$ | An idempotent of the quaternion or split-quaternion layer, in the mathematical corpus |
| $\Pi$ | An idempotent of the complex, split-complex or dual layer, in the mathematical corpus |

The convention is one of **notation, not of substance**: an element written $\tilde{\Pi}$ is not a different kind of object from one written $\tilde{Q}$, only an element known to be idempotent, and the glyph records that knowledge at the point of use; a passage that needs a generic idempotent variable writes $\tilde{\Pi}$.

### The Nilpotent Convention

The nilpotents carry a symbol of their own, beside the idempotent $\tilde{\Pi}$ (§*The Idempotent Convention*): the lower-case $\tilde{\nu}$ of the quaternion and split-quaternion layers and the upper-case $\tilde{\Upsilon}$ of the biquaternion and split-biquaternion layers. **The capital is an upsilon and not a $Y$.**

A **nilpotent** of the algebra is an element $\tilde{\nu}$ whose square vanishes,

$$
\tilde{\nu}^2 = 0 .
$$

**The square is read in a named product**, the algebra product unless the statement names another, as in the mathematical corpus (§*The Nilpotent Convention* of *Conventions in Mathematics*), and the class is relative to the product. A nilpotent is never a projector, a Hermitian nilpotent being zero, and it is never a state; the nilpotent is the partner of the idempotent in a minimal left ideal, $\mathbb{B}\tilde{\Upsilon}_2 = \mathbb{B}\tilde{\Pi}_1$.

**The subscript of a nilpotent is always numeric**, as for the idempotents: a pair is $\tilde{\nu}_1, \tilde{\nu}_2$, a second pair in the same statement takes the next numbers, and a sign is never written as a subscript.

The nilpotents have no classification of the idempotent kind and no sphere of pure states; which set the square-zero elements form depends on the product. The nilpotents of a state module are those of *The Biquaternion Vacuum as a Minimal Idempotent*, and the spin-down state of *Spin-1/2 Quantum Physics in Biquaternionic Form* is a nilpotent of the ideal of that vacuum.

The nilpotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde{\Upsilon}$ | A nilpotent of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde{\Upsilon}$ it generates |
| $\tilde{\nu}$ | A nilpotent of the quaternion or split-quaternion layer |
| $\Upsilon$ | A nilpotent of the complex, split-complex or dual layer, where no tilde is written |

The convention is one of **notation, not of substance**: an element written $\tilde{\nu}$ is not a different kind of object from one written $\tilde{Q}$, only an element known to be nilpotent.

The standard pair of nilpotents is $\tilde{\Upsilon}_1$ and $\tilde{\Upsilon}_2$, the off-diagonal Peirce units of *Ideals and Peirce Decomposition of the General Plain Algebra* exchanged by the star. The truncated ladder of *The Biquaternion Vacuum as a Minimal Idempotent* and of the Fock, vacuum and matrix-representation articles is this pair: those articles write it $\tilde{\Upsilon}_1$ and $\tilde{\Upsilon}_2$ wherever the algebra element is meant, and keep the ladder letters for the abstract operators.

## The Four-Vector Representation

The algebra is read as the quadruple of its complex coefficients, in *The Four-Vector Element Representation of Biquaternions*. Each unit is one coordinate place,

$$
e_0 \longleftrightarrow (1,0,0,0), \qquad e_1 \longleftrightarrow (0,1,0,0), \qquad e_2 \longleftrightarrow (0,0,1,0), \qquad e_3 \longleftrightarrow (0,0,0,1),
$$

so that an element is its quadruple of coefficients,

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu \;\longleftrightarrow\; (Q^0, Q^1, Q^2, Q^3), \qquad Q^0 = Q_0, \quad (Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3),
$$

and the index is written in the upper position. **No index is raised or lowered anywhere in the series.** On $\mathbb{C}^4$ there is no pairing with which to move one, and the $ict$ convention is what puts the metric into the coefficient — $(ict, \mathbf{x})$ rather than a contraction rule — so that the interval is the sum of squares with no explicit scalar product. The article owns the product in components and the column-and-dual-row convention.

## The 4×4 Matrix Representation

Multiplication is read as a linear map on that quadruple, in *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The four units act by

$$
\mathsf{M}_4(e_0) = I_4 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \qquad
\mathsf{M}_4(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix},
$$

$$
\mathsf{M}_4(e_2) = \begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix}, \qquad
\mathsf{M}_4(e_3) = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix},
$$

and each of the three vector matrices squares to $-I_4$, as $e_k^2 = -e_0$ requires. For a general element, left multiplication by $\tilde{Q}$ is the matrix $\mathsf{M}_4(\tilde{Q})$ whose $\nu$-th column is the column of $\tilde{Q}e_\nu$,

$$
\mathsf{M}_4(\tilde{Q})\,\cdot\,\text{(column of } \tilde{R}) = \text{column of } \tilde{Q}\tilde{R},
$$

and right multiplication is the same construction with $e_\nu\tilde{Q}$, giving $\mathsf{M}_4^{R}(e_0) = I_4$ and $\mathsf{M}_4^{R}(e_k) = \eta\,\mathsf{M}_4(e_k)^{\mathsf{T}}\eta$, with $\eta = \operatorname{diag}(-1,+1,+1,+1)$. The two sides are distinguished on purpose and are not interchangeable: $\mathsf{M}_4^{R}(\tilde{Q})$ is not $\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$, and what relates them is the metric, not a relabelling.

The determinant and the trace of the two regular matrices, the relation between $\mathsf{M}_4^{R}$ and $\mathsf{M}_4$, and the volume identity $\det\mathsf{M}_4(\tilde{Q}) = N(\tilde{Q})^2$ are *The $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*.

## The 2×2 Matrix Representation

The algebra is read as the complex $2 \times 2$ matrices, under the isomorphism

$$
\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C}),
$$

in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and this is the representation every numerical check in the series is performed with. The four unit images are fixed here, once, because every article depends on them agreeing. The three vector units are the Pauli matrices times $-i$:

$$
\mathsf{M}_2(e_0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\mathsf{M}_2(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

with the central scalar mapping to $\mathsf{M}_2(i) = iI_2$. Because $\mathsf{M}_2$ is $\mathbb{C}$-linear, the Hermitian units require no separate choice, $\mathsf{M}_2(ie_k) = i\,\mathsf{M}_2(e_k)$.

**The trace is the trace of this image.** The series writes

$$
\operatorname{Tr}(\tilde{Q}) := \operatorname{Tr}\mathsf{M}_2(\tilde{Q}).
$$

On the units $\operatorname{Tr}(e_0) = 2$ and $\operatorname{Tr}(e_k) = 0$, so on a general element $\operatorname{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$. That factor $2$ is not a normalisation but a consequence of $\mathsf{M}_2(e_0) = I_2$: it comes with the four images above, it cannot be divided out, and every pairing in the series is written with it, the Born rule $p = \operatorname{Tr}(\tilde{P}\tilde{\rho})$ among them. An unsubscripted trace means this one; a regular matrix has its own, written with its subscript. The unrestricted identity $\operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2)$ is recorded with its verification in the article just named.

**The determinant is the norm.** The determinant of the image is the biquaternion norm, $\det\mathsf{M}_2(\tilde{Q})=N(\tilde{Q})$, and it is multiplicative, which is what makes the matrix model compute every norm in the series. The invertibility criterion, the group of units and the unit-norm group are read from it; the derivations are *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

**The assignment is forced, not chosen.** $e_k^2 = -e_0$ requires the factor $i$ and $e_1e_2 = e_3$ fixes the sign, so neither the factor nor the sign in the three vector images could have been otherwise. A reviewer must not "correct" the assignment by making the three images real, nor by negating all three. *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* derives both.

**Never conjugate the matrix entries on their own.** Conjugating the entries of $\mathsf{M}_2(\tilde{Q})$ is *not* the image of any involution of the algebra: it negates the images of $e_1$ and $e_3$ while leaving $\mathsf{M}_2(e_2)$, which has real entries, untouched, and so it destroys the sector dictionary. The four conjugations $\natural$, $\bar{\phantom{Q}}$, ${}^{*}$ and $\flat$ are evaluated through the matrix formulas recorded in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, never by conjugating entries.

**The realisation is a convention of presentation, not of content.** The isomorphisms that preserve the subspace dictionary are the $\mathsf{M}_2' = S\mathsf{M}_2 S^{-1}$ with $S$ unitary up to a nonzero complex scalar, and an arbitrary invertible $S$ destroys the dictionary. The practical consequence is that a mistake of translation between the algebra and its matrices is repaired **here** — by correcting the assignment or the explicit factors of $i$ — and never by altering the biquaternion norm, the $ict$ assignment or the sector split.

**A bare $\mathsf{M}_2$ means this isomorphism and nothing else.** A plain $\mathsf{M}_2$, with no subscript, superscript or tilde, is reserved throughout the series for this isomorphism alone. The other uses a reader may meet are marked differently: $\varphi$ is an abstract homomorphism on the mathematics pages and an angle in the Thomas-precession exercise, $\tilde{\Phi} = \varphi\,e_0$ is the central scalar field of the Higgs articles, and $\Phi_{\tilde{U}}$ is the quantum channel of the gates article. None of these is the isomorphism, and a bare $\mathsf{M}_2$ is not any of them.

## The Gradient and the d'Alembertian

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

the whole of it **scalar**: it multiplies by $e_0$ and acts coefficient by coefficient, $\Box\tilde{F} = \sum_\mu(\Box F_\mu)e_\mu$, and it is the norm of the gradient, $\Box = \langle\tilde{\nabla},\tilde{\nabla}\rangle_{\natural}$ (*Biquaternion Norm and Invertibility*). The operator is $\partial^2/\partial Q_0^2 + \Delta_Q$ on the whole algebra; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. On the material sector $\mathbb{M}_-$, where $Q_0 = ict$ and $Q_k = q_k$, the derivative $\partial^2/\partial Q_0^2 = -c^{-2}\partial_t^2$ and the same operator reads

$$
\Box\big|_{\mathbb{M}_-} = \Delta - c^{-2}\partial_t^2 = \partial_{ict}^2 + \Delta ,
$$

a plus on the spatial part and a minus on the time part. **The $ict$ substitution — and with it the form $\Box = \partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$ — is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial Q_0^2 + \Delta_Q$. On $\mathbb{M}_-$, where the series does its work, that form is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series.

The operator is one, and every article writes it the same way. The Weyl-spinor exercise works in real time $x^0 = ct$ with the standard metric $(+,-,-,-)$; in those variables $\partial_{ict}^2 = -\partial_0^2$, so the same operator is

$$
\Box = \partial_{ict}^2 + \Delta = -\partial_0^2 + \nabla^2 ,
$$

and the mass equation is the series equation $\left(\Box - m^2c^2/\hbar^2\right)\psi = 0$. **No article of the series defines a second d'Alembertian**, and no mass-term sign is left to a local convention.

## The Real Structure $\flat$

### What $\flat$ Is

The map

$$
\tilde{\Psi}^\flat = -\tilde{\Psi}^{*} = -\overline{\tilde{\Psi}^{\natural}}
$$

is the **anti-Hermitian conjugation**, the negative of the star, and the algebra's **real structure** (§*The Conjugations and the Adjoint*). The sign convention on the two sectors is what makes $\mathbb{M}_-$ the material sector, and $\flat$'s fixed space is that sector (§*The Remarkable Subspaces*).

### What $\flat$ Is For

$\flat$ is retained for conjugation and for the definition of the $\mathbb{M}_\pm$ split itself, for the trace and the bilinear pairings, and for the real-form question of Dirac versus Majorana fermions, which the companion articles on chirality, the neutrino and the CPT theorem develop. In every case the coupling built on $\flat$ pairs $\tilde{\Psi}$ with $\tilde{\Psi}^\flat$.

### What $\flat$ Is Not

$\flat$ is **not** the mass. The two roles were conflated in the retired form $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$, and separating them is the content of the mass-term convention of *The Dirac Equation in Biquaternionic Form*. A reader who finds $\flat$ in an article should expect conjugation, a bilinear, or the sector split — never a mass.

$\flat$ is **not** the charge conjugation either. It has the **shape** of a charge-conjugation pairing — it pairs an element with its own conjugate — but the operation called charge conjugation is the conjugate-linear pseudoautomorphism $\bar A=\Pi A^{*}\Pi^{-1}$, whose module form is $C[\psi]=i\gamma^{2}\psi^{*}$, and the operation is owned by *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*. The four levels of the name — the algebra's real structure $\flat$, the Clifford pseudoautomorphism, the module operation $C$, and the module real structure $\bar{\cdot}$ — are tabulated in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*.

**$\flat$ and the Klein four.** The four involutions $\{1,\bar{\cdot},{}^{\natural},{}^{*}\}$ form a **Klein four group** under composition, and $\flat=-{}^{*}$ is the **fourth character** and not a fourth element: it is minus the star, and its fixed space is the material sector. A reviewer must not treat $\flat$ as an independent involution. The Klein four and the four block characters are *Relations Between Subspaces*; the two $\mathbb{Z}_2$ decompositions that cannot be aligned are *The Centre of the Biquaternion Algebra as the Classical Sector*.

## Summary

The conventions of the series are one object read in order, from the object itself to the two clauses a field equation inherits.

**The object and its parts.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, over complex coefficients. The scalar unit $i$ is central, which is what makes the central phase the algebra's continuous symmetry, and multiplication by it is one map whose restrictions are the global phase and the exchanges and duality rotations of the sectors (§*The Central Map and Its Restrictions*). The conjugations cut the algebra into the remarkable subspaces of §*The Remarkable Subspaces*, each carrying its own real parameters and its slice of the coordinate dictionary, with $q'_0 = ct$, $q_0 = ct'$, $(q_1,q_2,q_3) = (x,y,z)$ and $(q'_1,q'_2,q'_3) = (x',y',z')$. The algebra carries four forms, not two — the general plain bilinear $B$, the general quaternionic bilinear $N$, the Hermitian $H$ and the Krein $K$ — read on the diagonal as the four norms, of which $N$ is the biquaternion norm. The matrix representation $\mathsf{M}_2$ is fixed by its four basis images, with the Hermitian units following as $\mathsf{M}_2(ie_k) = i\,\mathsf{M}_2(e_k)$; the residual freedom is a unitary change of basis of $\mathbb{C}^2$ and nothing further, so the sector dictionary cannot be altered by re-choosing it.

**The presentations, the gradient and the metric levels.** The algebra is written in three presentations — the coefficient quadruple, the $4\times4$ regular matrix and the $2\times2$ image $\mathsf{M}_2$ — each developed in its own article, and it is the trace of $\mathsf{M}_2$ that the series calls the trace. The material coordinate is $\tilde{Q} = ict\,e_0 + \mathbf{x}$, using the $ict$ convention so that the Minkowski interval is the biquaternion norm, vanishing on the zero-divisor cone. The series d'Alembertian is $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_0^2 + \Delta_Q$, read on the material sector as $\partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$; every article uses this one operator, with the mass equation $\left(\Box - m^2c^2/\hbar^2\right)\psi = 0$. The algebra's real structure is $\flat = -{}^{*}$, and the mass term built on $\flat$ and then retired, with the dispersion that retired it, is recorded in *The Dirac Equation in Biquaternionic Form* and *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*. The three levels of the word *metric* are set out in *The Four Forms, the Four Algebraic Norms and the Change of Scalars*, and the tool is never a reason to change a convention of the framework.

The theme is single. In a framework whose algebra and sector assignment are non-standard, the most likely error is a correction of something that is deliberate. The conventions recorded above are the places where that is most likely to happen.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q}$ | An element of the algebra. The same symbol serves for the general element and for an element of any of the subspaces, whichever the passage at hand is about; the complex coefficients are $Q_\mu$, the real parameters of a four-dimensional subspace are $q_\mu$ and $q'_\mu$, the prime marking the slot that carries the $i$. |
| $\tilde{P}$ | A four-momentum or four-vector, $\tilde{P} = m\tilde{U}$, and a generic element in a statement that holds for every element (see §*The Element and Its Coefficients*) |
| $\tilde{\Pi}$ | An idempotent, projector or pure state, $\tilde{\Pi}^2 = \tilde{\Pi}$, and the minimal left ideal $\mathbb{B}\tilde{\Pi}$ it generates (see §*The Idempotent Convention*). By the case rule the quaternion layer of the mathematical corpus writes $\tilde{\pi}$ and the tilde-free layers $\Pi$ |
| $\tilde{\nu}$ | A nilpotent of the quaternion or split-quaternion layer, $\tilde{\nu}^2 = 0$ (see §*The Nilpotent Convention*) |
| $\tilde{\Upsilon}$ | A nilpotent of the biquaternion or split-biquaternion layer, the upper-case glyph of the same letter; not a $Y$ |
| $\tilde{\Xi}$ | A root of $-1$ of the biquaternion or split-biquaternion layer, $\tilde{\Xi}^2 = -1$ (see §*The Root Convention*) |
| $\tilde{\xi}$ | A root of $-1$ of the quaternion or split-quaternion layer |
| $\tilde{Q}^{\natural}, \bar{\tilde{Q}}, \tilde{Q}^{*}, \tilde{Q}^{\flat}$ | Quaternion (the natural sign), complex, Hermitian and anti-Hermitian conjugation |
| $\tilde{Q}^{\natural} \mapsto \epsilon M^{\mathsf T}\epsilon^{-1}$, $\bar{\tilde{Q}} \mapsto \epsilon\overline{M}\epsilon^{-1}$ | The two conjugations dressed by the antisymmetric form; $\epsilon = \mathsf{M}_2(-e_2)$ |
| $\tilde{Q}^{*} \mapsto M^\dagger$, $\tilde{Q}^\flat \mapsto -M^\dagger$ | The two undressed ones. Entrywise conjugation of $M$ alone is not the image of any involution |
| $\flat = -{}^{*}$ | The anti-Hermitian conjugation, the algebra's real structure |
| $\mathbb{C}_{\mathbb{B}} = \{Q_0 e_0\}$ | Centre subspace, fixed points of quaternion conjugation; the centre of $\mathbb{B}$ and the complex time sector; parameters $q_0, q'_0$ with $q_0 = ct'$ and $q'_0 = ct$ |
| $\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\}$ | The vector subspace, i.e. the complex space sector: anti-fixed points of quaternion conjugation, real dimension six; parameters $q_k, q'_k$ with $(q_k) = (x,y,z)$ and $(q'_k) = (x',y',z')$. |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, i.e. the real sector (the real half): fixed points of complex conjugation, all four coefficients real |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion subspace, i.e. the imaginary sector (the imaginary half): anti-fixed points of complex conjugation, all four coefficients purely imaginary; not a subalgebra. $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, a split that crosses the $\mathbb{M}_\pm$ split |
| $\mathbb{M}_+ = \{ \tilde{Q} : \tilde{Q}^{*} = \tilde{Q} \}$ | Hermitian subspace, the informational sector; basis $e_0, ie_1, ie_2, ie_3$, parameters $q_0, q'_1, q'_2, q'_3$ (real), with $q_0 = ct'$ |
| $\mathbb{M}_- = \{ \tilde{Q} : \tilde{Q}^\flat = \tilde{Q} \}$ | Anti-Hermitian subspace, the material sector; basis $ie_0, e_1, e_2, e_3$, parameters $q'_0, q_1, q_2, q_3$ (real), with $q'_0 = ct$ |
| $\tilde{Q} = ict\,e_0 + \mathbf{x}$ | The material coordinate, $\mathbf{x} = x e_1 + y e_2 + z e_3$ |
| $(ct')\,e_0 + i\mathbf{x}'$ | The informational coordinate, $\mathbf{x}' = x' e_1 + y' e_2 + z' e_3$; the temporal coefficient $ct'$ is real and the spatial ones imaginary, the mirror of the material coordinate |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$ | Biquaternion norm, level 1 of the three levels of the word *metric* (§*The Metric: Three Levels* of *The Four Forms, the Four Algebraic Norms and the Change of Scalars*) |
| $\mathrm{Form}(\tilde{P},\tilde{Q})$, $\mathrm{Norm}(\tilde{Q})=\mathrm{Form}(\tilde{Q},\tilde{Q})$ | The generic form and the generic norm, instantiated one to a general product by the four forms and the four norms $B$, $N$, $H$, $K$ (§*The Four Algebraic Norms*, §*The Involutions and the Four Forms*) |
| $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ | The twelve products, the four general products and their symmetric and antisymmetric parts (§*The Twelve Products and Their Names*) |
| $B = \langle\tilde{P},\tilde{Q}\rangle = \mathrm{Sc}(\tilde{P}\tilde{Q}) = P_0Q_0 - P_1Q_1 - P_2Q_2 - P_3Q_3$ | The general plain bilinear form, the form of the plain product and of the identity conjugation |
| $N = \langle\tilde{P},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}) = P_0Q_0 + P_1Q_1 + P_2Q_2 + P_3Q_3$ | The general quaternionic bilinear form, the form of the biquaternion norm, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$ |
| $H = \langle\tilde{P},\tilde{Q}\rangle_{*} = \mathrm{Sc}(\tilde{P}\tilde{Q}^{*}) = P_0\bar{Q}_0 + P_1\bar{Q}_1 + P_2\bar{Q}_2 + P_3\bar{Q}_3$ | The general plain sesquilinear form, the form the series calls the Hermitian form |
| $K = \langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}) = P_0\bar{Q}_0 - P_1\bar{Q}_1 - P_2\bar{Q}_2 - P_3\bar{Q}_3$ | The general quaternionic sesquilinear form, the form the series calls the Krein form; on $\mathbb{M}_-$ it is the negative of the interval, $\langle\tilde{T},\tilde{T}\rangle_{\natural*} = -\langle\tilde{T},\tilde{T}\rangle_{\natural}$ |
| $J = {}^{\natural}$ | The fundamental symmetry, $\langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \langle\tilde{P}^{\natural},\tilde{Q}\rangle_{*}$, $J^2 = \mathrm{id}$, $\mathbb{C}$-linear |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric, signature $(-,+,+,+)$ (level 2) |
| $g$ | Clifford metric of the $\gamma^\mu$ (level 3); an optional tool, not a framework convention. $\mathrm{diag}(+1,-1,-1,-1)$ throughout — the $\mathbb{M}_+$ form, matching the objects the tool represents |
| $\tilde{\nabla} = \sum_{\mu=0}^{3} e_\mu\partial/\partial Q_\mu$, $\tilde{\nabla}^{\natural} = e_0\partial/\partial Q_0 - e_k\partial/\partial Q_k$ | Biquaternionic gradient and its quaternion conjugate, the two factors of the d'Alembertian |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_0^2 + \Delta_Q$ | The d'Alembertian, a scalar operator; on the material sector it reads $\partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$, the series convention |
| $\mathrm{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ | Trace pairing, unrestricted; the case $\tilde{P}\in\mathbb{M}_+$, $\tilde{Q}\in\mathbb{M}_+$ is the real one. $\mathrm{Tr}(e_0) = 2$ |
| $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ | The matrix representation, with $\mathsf{M}_2(e_0) = I_2$ and $\mathsf{M}_2(e_k)$ as given above; the Hermitian units follow as $\mathsf{M}_2(ie_k) = i\,\mathsf{M}_2(e_k)$. Fixed up to a unitary change of basis, and no further |
| $Q^\mu$ | The coefficients of an element, in the upper position, $Q^0 = Q_0$ and $(Q^1,Q^2,Q^3) = (Q_1,Q_2,Q_3)$; never raised or lowered, there being no metric on $\mathbb{C}^4$ |
| $SL(2,\mathbb{C})$ | Unit-norm biquaternions, the Lorentz group on $\mathbb{M}_-$ |

## Further Reading

- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the original quaternion algebra and its units.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents, minimal left ideals, and the conjugations of a Clifford algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for real structures and real forms on Clifford algebras.
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), companion article, for the relations among the subspaces defined here — their coordinate blocks, intersections, spans, gradings and biquaternion norms.
- *The Four-Vector Element Representation of Biquaternions* (`articles_physics/the-four-vector-element-representation-of-biquaternions.md`), companion article, for the coefficient space, the column and the dual row, and the index that is never raised or lowered.
- *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_physics/the-4x4-matrix-element-representation-of-biquaternions.md`), companion article, for the two regular matrices, the relation between them, and the reduction into the two chiralities.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), companion article, for the isomorphism $\mathsf{M}_2$, the trace and the determinant, and the ideals as columns.