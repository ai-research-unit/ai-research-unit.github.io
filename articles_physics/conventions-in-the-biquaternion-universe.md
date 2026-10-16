# __Conventions in the Biquaternion Universe__

## Introduction

A framework built on a non-standard algebra, and on a non-standard choice of which part of it counts as "real", is a framework in which a reader will repeatedly find things that look wrong and are not. Two examples fix the idea. The series takes the **anti**-Hermitian subspace as the material sector, where the more familiar convention would take the Hermitian one. And the series' d'Alembertian carries a sign opposite to the one used in the articles on Weyl spinors. In both cases it is the "correction" that is the error.

This article states the conventions of the series, one to a section, and records the reason each was chosen. It states conventions only: the proofs, the properties and the physical readings of the objects it names belong to the articles cited beside them. It is meant to be read before any other article is edited, and its reader is anyone writing or revising an article of the series, for whom the conventions are load-bearing — a change that looks local, a sign or a factor of $i$, generally propagates into a dozen dependent articles.

The article is ordered as a dictionary of a single object, each section stated after the one it depends on. First the object and its writing: the algebra and its basis, then the element and its coefficients. Then its parts: the four involutions, the remarkable subspaces they cut out, and the coordinate dictionary and the sector names those subspaces carry. Then what is done with the object: the twelve products, the four forms that are their scalar parts and the four norms read on the diagonal, named by the generic Form and the generic Norm, and the restrictions of the central map, which the norms and the forms make precise. Then the three distinguished elements — the root, the idempotent and the nilpotent — whose glyphs the series writes. Then the three presentations of the same object, the four-vector, the 4×4 regular and the 2×2 element representation with its trace. Last the conventions a field equation inherits, the gradient and its d'Alembertian, closed by the algebra's real structure $\flat$.

The word *metric* is used at three levels in the series — the biquaternion norm, the two real sectors with their $ict$ metric, and the Clifford tool — and the distinction between them is set out in *The Four Forms, the Four Algebraic Norms and the Change of Scalars*, together with the one-way rule that the Clifford tool is a translation of the algebra and never a reason to change it.

One warning applies throughout. **A convention recorded here is not a claim that the alternative is wrong.** Several of these choices are freely made where either choice would be defensible; they are conventions, not theorems. What is not free is *consistency*: once a convention is fixed, the dependent articles inherit it, and a change to it is a change to all of them. Where a convention is instead forced — where the alternative leads to a demonstrable contradiction — the article says so explicitly, and that distinction is the difference between a convention and a result.

## The Algebra and Its Basis

The framework is set in the **biquaternion algebra**

$$
\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H},
$$

the complexification of the quaternions. Every element is written in the basis

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z,
$$

where $e_t = 1$ and $\vec e_x, \vec e_y, \vec e_z$ are the quaternion units,

$$
\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t, \qquad \vec e_x\vec e_y = -\vec e_y\vec e_x = \vec e_z,
$$

and the four coefficients $Q_\mu$ are **complex** numbers. The scalar imaginary, denoted $i$, is the complex unit of the complexification:

$$
i^2 = -1.
$$

Everything that follows turns on how each complex coefficient is split, so the split is fixed here, at the outset. Writing every coefficient as a real part plus $i$ times a real part,

$$
Q_t = q_t + iq'_t, \qquad Q_x = q_x + iq'_x, \qquad Q_y = q_y + iq'_y, \qquad Q_z = q_z + iq'_z, \qquad q_\mu, q'_\mu \in \mathbb{R},
$$

replaces the four complex coefficients by **eight real parameters**: $q_\mu$ is the real part of $Q_\mu$, the coefficient of $e_\mu$, and $q'_\mu$ its imaginary part, the coefficient of $ie_\mu$, so the prime marks the parameter that carries the $i$. As a real vector space $\mathbb{B}$ is eight-dimensional, and the remarkable subspaces below are what the eight parameters are grouped into. The full set of parametrisations, and the two conventions they embody, are in *The Elements and their Coefficients* and *Remarkable Subspaces* below; nothing in them changes the split stated here.

One structural fact governs the whole series, so it is worth isolating. **The scalar unit $i$ is central**: it commutes with every element of $\mathbb{B}$, because it belongs to the $\mathbb{C}$ factor of the tensor product, while the quaternion units belong to the $\mathbb{H}$ factor. Multiplication by a *central* phase $\exp(i\alpha)$ therefore commutes with every operator constructed from the algebra — in particular with the biquaternionic gradient $\tilde{\nabla}$ — and this is why the central phase is the algebra's natural continuous symmetry. The articles on Noether's theorem and the gauge principle rest on it.

The split is also a split of **roles**, and the two roles belong to the two **factors** of the tensor product and cannot be exchanged. The central unit $i$ is the scalar imaginary: it is what enters the phase $\exp(iS/\hbar)$, and it multiplies a whole element from inside the centre. The three units $\vec e_x,\vec e_y,\vec e_z$ are the vector directions: they are the relativistic and rotational structure, and they enter through the quaternion factor. A central scalar and a vector direction are different kinds of object — one commutes with everything, the other rotates — so no product of the four general products may read $i$ through the quaternion direction or a unit through the scalar one. The mirror statement, that the two conjugations act on the two factors separately, is the subject of *The Four General Products and Their Physical Readings*.

As a complex algebra $\mathbb{B}$ is isomorphic to the full matrix algebra,

$$
\mathbb{B} \cong M_2(\mathbb{C}),
$$

and this identification is used constantly. It is fixed by a single isomorphism, written $\mathsf{M}_2$; its four basis images, and the rule that neither the factor $i$ nor the sign is a free choice, are stated in *The 2×2 Matrix Representation* below, and the development of the representation — the general element, the remarkable subspaces as matrices, the conjugations, the trace and the determinant — is in the companion article *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. Its two **minimal left ideals** are the algebra's two chiralities; the spinor module and the mass term a field equation builds on that structure are the subject of *The Dirac Equation in Biquaternionic Form*.

## The Elements and their Coefficients

The case and the tilde of the glyph are fixed first, and the element is written after. A generic element is preferably written so that the glyph alone identifies its algebra, two features being read together: the **case** separates a real scalar from a complex one, and a **tilde** marks the quaternionic factor.

| System | Name | Generic element | Scalar–vector decomposition | Coefficients |
|---|---|---|---|---|
| $\mathbb{C}$ | Complex numbers | $A = a + ia'$ | Scalar $a$, vector $ia'$ | Real, $a, a'$ |
| $\mathbb{H}$ | Quaternions | $\tilde q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $q_te_t + \vec q$, $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | Real, $q_\mu$ |
| $\mathbb{B}_{\mathrm{r}}$ | Reduced biquaternions | $T = A + Bj$ | Scalar $A$, vector $Bj$ | Complex, $A = a + ia'$, $B = b + ib'$ |
| $\mathbb{B}$ | Biquaternions | $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $Q_te_t + \vec Q$, $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$, $Q_\mu\in\mathbb{C}$ | Complex, $Q_\mu = q_\mu + iq'_\mu$ |

**The four coordinates are labelled $t, x, y, z$.** So that a sum over the coordinates of a quaternion or of a biquaternion shows at once which unit each term carries, the coefficients take the labels of the physical directions in place of the numbers: $Q_t$ with $e_t$, and $Q_x, Q_y, Q_z$ with $\vec e_x, \vec e_y, \vec e_z$. A sum over the four therefore runs over those labels,

$$
\tilde Q = \sum_{\mu \in \{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $\mu$ the label and $e_\mu$ the unit it carries — the arrowless $e_t$ at $\mu = t$ and the arrowed $\vec e_\mu$ at $\mu = x, y, z$. The same rule reads a quaternion, $\tilde q = \sum_{\mu} q_\mu e_\mu$, and a four-vector of the algebra, and the primed coefficients follow the same labels, $Q_\mu = q_\mu + iq'_\mu$: the label marks the direction and the prime marks the slot that carries the $i$.

Five rules are read off the table. **A complex element carries a majuscule**, $A$ or $B$, the case naming the scalar sector: an upper-case glyph has a scalar sector larger than the reals, a lower-case one has the reals. **The second coordinate of a complex element carries a prime**, $A = a + ia'$. And **the quaternionic elements carry a tilde**: lower case for the quaternions, $\tilde q$, and upper case for the biquaternions, $\tilde Q$; **the reduced biquaternion element carries no tilde**, $T = A + Bj$, its algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ being commutative and having no quaternionic factor, its second unit being the hyperbolic $j$, $j^{2} = +1$ and $ji = ij$, so that the basis is $1, i, j, ij$. Finally, **the element is a scalar part plus a vector part**: the scalar part is carried by the unit — $1$ in $\mathbb{C}$ and $\mathbb{B}_{\mathrm{r}}$, $e_t$ in $\mathbb{H}$ and $\mathbb{B}$ — and the vector part by the remaining basis directions, carrying the arrow, $\vec q$ or $\vec Q$, so that $\tilde Q = Q_te_t + \vec Q$ with $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ and $Q_\mu = q_\mu + iq'_\mu$. **A pure element carries the arrow.** A pure element is one with no scalar part, a vector of its layer, and it is written with the arrow of the vector part: $\vec q$ and $\vec Q$ are the pure elements of the quaternion and of the biquaternion layers, standing by themselves (§*Pure Elements and their Coefficients*). The arrow names the vector part of a named element, $\vec{Q}$ in $\tilde{Q} = Q_te_t + \vec{Q}$, and it names the same object when the element is read on its own; the arrow and the tilde are never stacked.

**The element with its vector.** The rules collect into a scalar part beside a vector part,

$$
\tilde q = q_te_t + \vec q , \qquad \tilde Q = Q_te_t + \vec Q , \qquad T = A + Bj .
$$

with

$$
\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z , \qquad \vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z .
$$

The first is the general quaternion, the second the general biquaternion, and the third the general reduced biquaternion, each written as a scalar part beside a vector part.

The notation of this article already reads through the convention: the coefficients $q_\mu$ are real, the coefficients $Q_\mu = q_\mu + iq'_\mu$ are complex, the two coordinates $A = a + ia'$ and $B = b + ib'$ of the reduced biquaternion $T$ are complex, and a general element of $\mathbb{B}$ is written $\tilde Q$.

**The generic element is $\tilde{Q}$.** A statement that holds for every element is written with $\tilde{Q}$; a statement that needs two writes them $\tilde{Q}_1$ and $\tilde{Q}_2$, and a third takes the next number. The trace pairing is $\operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2)$, the commutator bracket $[\tilde{Q}_1,\tilde{Q}_2] = \tilde{Q}_1\tilde{Q}_2 - \tilde{Q}_2\tilde{Q}_1$, the general quaternionic bilinear form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ and the multiplicativity $\langle\tilde{Q}_1\tilde{Q}_2\rangle_{\natural} = \langle\tilde{Q}_1\rangle_{\natural}\,\langle\tilde{Q}_2\rangle_{\natural}$. The argument of an operator, the dummy of an annihilator, the second entry of a bracket and the element a field or a map is applied to carry the same glyph: $L_{\tilde Q}(\tilde Q_1) = \tilde Q \bullet \tilde Q_1$, $\{\tilde Q_1 : \tilde Q \star \tilde Q_1 = 0\}$, $[\tilde Q, \tilde Q_1]$. **The letter $\tilde P$ is never a generic element**; it is the four-momentum, $\tilde P = m\tilde V$. The letters $X$, $Y$, $Z$ and $W$ name no element of the algebra here.

**The preferred notation of a physical quantity.** The glyphs of the elements are kept for the algebra, and a physical quantity that would borrow one is written with a letter of its own. The **electric charge** takes the archaic qoppa: the minuscule $ϙ$ (U+03D9) for a charge and the majuscule $Ϙ$ (U+03D8) for a total charge or a charge operator, the two cases of the one letter, so that $q$ and $Q$ stay with the elements; the chiral charges are $ϙ_L$ and $ϙ_R$, and the charge operator of a chiral module is $Ϙ = ϙ_LP_L + ϙ_RP_R$. The **exchange momentum is written $k$**: the minuscule $q$ belongs to the elements — the coefficient $q_\mu$ and the quaternion-layer element $\tilde q$ — so the momentum carried by an exchanged boson at a vertex, and a momentum transfer, take the letter of a mode momentum, written $k^\mu$ as a four-vector and $\vec k$ as a three-vector; where the two wave vectors of a scattering are themselves written $\vec k$ and $\vec k'$, the transfer is written as their difference $\vec k'-\vec k$. The other physical quantities keep the letters of the table below, and where a physical quantity is itself an element of the algebra it carries the glyph of an element, as the four-position $\tilde{Q} = ict\,e_t + \vec x$.

**The letters of the physical quantities.** The glyphs are fixed one to a quantity, so that a reader meets the same letter for the same thing in every article.

| Physical quantity | Symbol | Meaning and note |
|---|---|---|
| Electric charge | $ϙ$ | The minuscule of the archaic qoppa, a physical quantity and not an element of the algebra (U+03D9) |
| Total charge, charge operator | $Ϙ$ | The majuscule of the same letter; the chiral charges are $ϙ_L, ϙ_R$ and the charge operator of a chiral module is $Ϙ = ϙ_LP_L + ϙ_RP_R$ (U+03D8) |
| Mass | $m$ | The rest mass, as in the mass equation $(\Box - m^2c^2/\hbar^2)\psi = 0$ |
| The circle constant | $\pi$ | The number; not the idempotent, which is written $\tilde\Pi$ |
| Reduced Planck constant | $\hbar$ | Turns the action into the phase $\exp(iS/\hbar)$, and the mass into a wavenumber |
| Speed of light | $c$ | Enters through the material time, $\tilde Q = ict\,e_t + \vec x$ |
| Energy | $E$ | The energy of a particle or of a normal mode |
| Momentum, four-momentum | $\vec p$, $\tilde P$ | $\tilde P = m\tilde V$ |
| Position | $\vec x$ | The spatial part of the material coordinate, $\tilde Q = ict\,e_t + \vec x$ |
| Four-velocity | $\tilde V$ | Normalised by $\langle\tilde V\rangle_{\natural} = -c^2$ |
| Rotation quaternion | $\tilde U$ | The unitary rotor, $\tilde U\in\mathrm{SU}(2)$; a unit element of the layers, not the generic element $\tilde Q$ |
| Scalar and vector potential | $\phi$, $\vec A$ | The electromagnetic potential of the minimal-coupling articles |
| Field strength | $\tilde F$ | The biquaternion of the two Maxwell fields, the electric sector real and the magnetic one imaginary |
| An algebra-valued field | $\tilde\Psi$, $\tilde\Phi$, $\tilde U$ | A field whose value at every point is an element of the algebra keeps the element tilde, since the tilde marks the value; the domain and the codomain are read from the accompanying arrow, as in $\tilde\Psi : \mathbb{R}^{1,3} \to \mathbb{B}$ |
| Riemann–Silberstein vector | $\vec N$ | The complex field vector $\vec N = \vec E + ic\vec B$ of the electromagnetic articles; its letter is not that of a velocity, and a velocity is never written $\vec N$ |
| Action | $S$ | The exponent of the central phase and the classical action of the stationary-phase articles |
| Gauge couplings | $g$, $g'$ | The standard weak and hypercharge couplings; the framework's own coupling is $\kappa$ |
| Framework coupling | $\kappa$ | $\kappa = ϙ/\hbar$, the coefficient of the biquaternionic covariant derivative |
| Weak mixing angle | $\theta_W$ | The rotation that separates the photon from the $Z$ |
| Boltzmann constant, inverse temperature | $k_B$, $\beta$ | $\beta = \hbar/(k_BT)$, the corpus convention with $\hbar$ retained |
| Atomic number, nuclear charge number | $\mathfrak{Z}$ | The number of elementary charges of the nucleus, the nuclear charge being $\mathfrak{Z}ϙ$; the plain $Z$ is the $Z$ boson, $\mathbb{Z}$ the integers and $\mathcal{Z}$ the light-cone set |
| Multipole moments, quadrupole | $\mathcal{Q}_{lm}$, $\mathcal{Q}_{ij}$ | The charge moments of the multipole articles, spherical and Cartesian; not the generic element $\tilde Q$ |
| Heat | $\mathcal{Q}$ | The heat of the thermodynamic articles, as in $\mathcal{Q} = T\,\Delta S$ |
| Supercharge, BRST charge | $\mathcal{Q}$ | The odd generator of the supersymmetry and BRST articles, with $\{\mathcal{Q},\mathcal{Q}^\dagger\} = H$ and $\mathcal{Q}^2 = 0$ |
| Canonical coordinates | $\xi$, $\eta$ | The old and the new canonical variables of a transformation, and the transformation function $\langle \xi'\vert \eta'\rangle$ |
| Mode momentum | $k$ | The integration momentum of a mode expansion, $\int d^3k$ |
| Exchange momentum, momentum transfer | $k^\mu$, $\vec k$ | The momentum carried by an exchanged boson at a vertex, or transferred in a scattering; the letter of a mode momentum, and never $q$, which belongs to the elements |
| Quadratic Zeeman coupling | $\zeta$ | The spin-1 coupling of the quadratic Zeeman term, $\zeta \propto B^2$ |
| Signature indices | $p$, $q$ | The counts of positive and negative directions, as in $\mathrm{Cl}_{n,m}$ and $O(n,m)$; the $q$ here is the signature index, not the element $\tilde q$ |

**What the prime marks.** The prime belongs to the **coefficients**, not to the physical coordinates. The four coefficients of a general element are complex, and writing each as a real part plus $i$ times a real part,

$$
Q_\mu = q_\mu + iq'_\mu, \qquad q_\mu, q'_\mu \in \mathbb{R}, \qquad \mu \in \{t, x, y, z\},
$$

gives $q_\mu$ as the coefficient of $e_\mu$ and $q'_\mu$ as the coefficient of $ie_\mu$ — the same rule for every $\mu$:

| Coefficient | Real part | Attached to | Imaginary part | Attached to |
|---|---|---|---|---|
| $Q_t$ | $q_t$ | $e_t$ | $q'_t$ | $ie_t$ |
| $Q_x$ | $q_x$ | $\vec e_x$ | $q'_x$ | $i\vec e_x$ |
| $Q_y$ | $q_y$ | $\vec e_y$ | $q'_y$ | $i\vec e_y$ |
| $Q_z$ | $q_z$ | $\vec e_z$ | $q'_z$ | $i\vec e_z$ |

The primed parameter is the one attached to $ie_\mu$, so **the prime marks the slot that carries the $i$**. It is not a label of a subspace, and it has nothing to do with the physical coordinates: the primes live on the $q$'s, which index the four basis elements, while $x, y, z, t, t'$ name the physical directions those $q$'s are read as. Grouped by the algebra's real-and-imaginary split, the four unprimed parameters are the coordinates of the quaternion subspace and the four primed ones those of the antiquaternion subspace,

$$
q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z \in \mathbb{H}_{\mathbb{B}}, \qquad iq'_te_t + iq'_x\vec e_x + iq'_y\vec e_y + iq'_z\vec e_z \in i\mathbb{H}_{\mathbb{B}} .
$$

**The three-and-one pattern.** The two subspaces of the coefficient split are uniform: $\mathbb{H}_{\mathbb{B}}$ is carried entirely by unprimed parameters, $i\mathbb{H}_{\mathbb{B}}$ entirely by primed ones. Each of the two sectors, by contrast, is mixed, because each takes its scalar slot from one side of that split and its three vector slots from the other. The informational sector is $q_te_t + iq'_k\vec e_k$ — unprimed scalar, primed vectors — and the material sector is $iq'_te_t + q_k\vec e_k$ — primed scalar, unprimed vectors. Read by parameter, the primed set $\{q'_t, q'_x, q'_y, q'_z\}$ is therefore one material slot (the material time $q'_t$) and three informational ones (the informational space $q'_k$), rather than four belonging to a single sector; that mixed ownership is the same statement as the crossing of the two decompositions.

**The alternative, and why it is not used.** $\mathbb{H}_{\mathbb{B}}$, which takes its scalar slot from $\mathbb{M}_+$ and its vector slots from $\mathbb{M}_-$, would be split across the two primes under the alternative labelling, so that it could no longer be written with a single name. That alternative makes the prime mark the **sector** — all-primed for $\mathbb{M}_+$ against all-unprimed for $\mathbb{M}_-$ — which is uniform in the opposite direction, and the corpus has used that labelling too. It is not kept, because it makes the prime mean "informational" rather than "imaginary", and the prime then no longer tracks the $i$: the informational time $ct'$ would be carried by a primed parameter although it is real, and the material time $ict$ by an unprimed one although it is imaginary. The present convention keeps the prime glued to the $i$, at the price of a mixed prime status inside each sector. The crossing itself, and the alternatives it allows, are examined in *Relations Between Subspaces*.

This is a **preferred convention** — a preference, not a strict rule, not to be enforced by rewriting other articles: the basis $e_t, \dots, \vec e_z$, the central unit $i$, the Euclidean vector $\vec x$, the coefficients $q_\mu, q'_\mu$, indices such as $\mu, k$, and the ladder operators $\tilde a, \tilde a^{\dagger}$ keep their established symbols.

**It is allowed to add subscripts when several elements of the same kind are used.** Where a statement carries more than one generic element, the occurrences are told apart by a subscript, $\tilde{Q}_1, \tilde{Q}_2, \dots$, and a second family in the same statement takes the next numbers.

## Pure Elements and their Coefficients

A **pure element** is an element with no scalar part. The scalar part of an element of $\mathbb{B}$ is carried by $e_t$, so a pure element is one whose $e_t$-coefficient vanishes, $\mathrm{Sc}(\tilde{Q}) = Q_t = 0$, and which is carried by the three vector directions alone. The pure elements are exactly the elements of the **vector subspace** $\mathrm{Vect}(\mathbb{B})$, the anti-fixed space of quaternion conjugation,

$$
\vec{Q}^{\natural} = -\vec{Q},
$$

of real dimension six; the pure quaternions of the quaternion layer are the vectors of $\mathbb{R}^{3}$.

**The glyph drops the tilde and carries the arrow.** The tilde marks the quaternionic factor of an element that is read with its scalar part beside its vector part; a pure element is read on its vector part alone, so it is written with the arrow and without the tilde, $\vec q$ in the quaternion layer and $\vec Q$ in the biquaternion layer. The case is unchanged, and the arrow is the only mark: the vector part of a named element and a pure element standing by itself are one object, written with the one glyph, so a pure element is never written with a tilde.

**The arrow is reserved for pure elements.** Three rules follow from this. First, **the arrow marks a pure element and nothing else**: an element with a nonzero scalar part is never written with an arrow, whatever its magnitude or its role. Second, **a unit element carries the arrow only if it is pure**: the unit pure quaternion $\vec u$ and the unit pure biquaternion $\vec U$ carry it, whereas a unit element that has a scalar part — a rotor $\tilde q$ of unit norm, say — carries no arrow, its unit length being carried by the construction that names it. Third, **a unit in the direction of an element takes that element as a subscript**, written $\vec u_{e}$ as in $\vec u_B$ for the unit along the field $B$; the subscript names the element whose direction is taken, and the arrow on $\vec u$ records that the unit is pure.

| System | Name | Pure element | Pure unit element | Scalar part | Coefficients |
|---|---|---|---|---|---|
| $\mathbb{H}$ | Quaternions | $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $\vec u$ | $q_t = 0$ | Real, $q_\mu$ |
| $\mathbb{B}$ | Biquaternions | $\vec{Q} = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $\vec U$ | $Q_t = 0$ | Complex, $Q_\mu = q_\mu + iq'_\mu$ |

Three rules are read off the table. **A pure element is the vector part of an element read on its own.** For $\tilde{Q} = Q_te_t + \vec{Q}$ the vector part $\vec{Q}$ is a pure biquaternion, and for $\tilde q = q_te_t + \vec q$ the vector part $\vec q$ is a pure quaternion; the vector part of a named element and a pure element standing by itself are one object, and the arrow names both. **A pure element is anti-fixed by quaternion conjugation**, $\vec{Q}^{\natural} = -\vec{Q}$, having no scalar part to be fixed. **The arrow marks purity, not magnitude.** A pure element is of arbitrary magnitude; a unit pure element — a unit pure quaternion $\vec u$ — carries no second mark, its unit length being carried by the construction.

**The pure glyphs.** The arrow is laid on the glyph of a special element on the same case rule that governs the layer: the pure root is $\vec\Xi$ in the biquaternion layer and $\vec\xi$ in the quaternion layer, and the pure nilpotent is $\vec\Upsilon$ in the biquaternion layer and $\vec\nu$ in the quaternion layer.

**The arrow has priority over the tilde.** Where an element is pure, the arrow is written whatever else the element is, and the tilde of a special glyph is dropped: a pure root is $\vec\Xi$ and a pure nilpotent is $\vec\Upsilon$ (or $\vec\xi$ and $\vec\nu$ in the quaternion layer), never $\tilde\Xi$ or $\tilde\Upsilon$. The tilde belongs to the general element, read with its scalar part beside its vector part, and a pure element has no scalar part to be read against; purity therefore decides the mark. The special conventions that write the root $\tilde\Xi$ or the nilpotent $\tilde\Upsilon$ name the **general** element of that class, which need not be pure, and an element that is at once special and pure is written with the arrow and only the arrow.

A pure glyph is given from the quaternions to the biquaternions only, the layers this convention reaches; the commutative layers carry their imaginary part in a single coefficient, $A = a + ia'$.

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
\tilde q^{\natural} = q_te_t - q_x\vec e_x - q_y\vec e_y - q_z\vec e_z .
$$

**The biquaternions $\mathbb{B}$.** All four have a sense, the bar conjugating the coefficient, which is complex:

$$
\bar{\tilde Q} = \bar Q_te_t + \bar Q_x\vec e_x + \bar Q_y\vec e_y + \bar Q_z\vec e_z, \qquad \tilde Q^{\natural} = Q_te_t - Q_x\vec e_x - Q_y\vec e_y - Q_z\vec e_z,
$$

$$
\tilde Q^{*} = \overline{\tilde Q^{\natural}} = \bar Q_te_t - \bar Q_x\vec e_x - \bar Q_y\vec e_y - \bar Q_z\vec e_z, \qquad \tilde Q^{\flat} = -\tilde Q^{*} .
$$

The dagger is the **general adjoint**. It is written on an operator and never on an element, and it is the same in every system. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. Where the adjoint in view is the obvious one, the text writes the two marks together, the dagger first and the star second, so that the coincidence is apparent on the page: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$ and $\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q}^{*}=\Theta_{\tilde Q^{*}}$ (*One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*).

**The mark is not a fifth conjugation.** The four conjugations of the algebra are the bar, the natural sign, the star and the flat; there is no other. An object that is also an operator — the left multiplication $L_a$, the right multiplication $R_a$, the sandwich $\operatorname{H}_{\tilde{Q}}$ — carries the dagger as that operator, and the mark then belongs to the operator and not to the element that generates it: $(L_a)^{\dagger}=L_{a^{*}}$, which is also $(L_a)^{*}$, the adjoint in view being the one of the definite form. Where a text writes a dagger on an element, the writing is an abuse, and the mark that was meant is the star, the Hermitian conjugation, or the natural sign, the quaternion conjugation, according to the conjugation in view. The series writes the elements with the four marks of the table and reserves the dagger for the general adjoint of the operators.

**The biquaternion norm.** The natural sign carries the algebra's **biquaternion norm**,

$$
\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 ,
$$

used throughout the series and read on the four forms and their norms in §*The Involutions and the Four Forms* and §*The Four Algebraic Norms* below. It is **multiplicative** and complex-valued in general, and it is not an analytic norm; its unit group and its invertibility reading are *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone*.

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

**Compact and non-compact directions.** A direction is **compact** when the one-parameter group it generates is a circle and **non-compact** when it is a hyperbola. The three real vector units $\vec e_x,\vec e_y,\vec e_z$ generate the compact directions, the three imaginary units $i\vec e_x,i\vec e_y,i\vec e_z$ the non-compact ones, and the complex vector subspace carries both. The Lie algebra this gives is *The Biquaternioid Antisymmetric Plain Algebra (APA) over $\mathbb{C}$*.

The subspaces are treated one by one in the owner articles: $\mathbb{C}_{\mathbb{B}}$ in *Other Remarkable Subspaces*, §*The Complex Time Sector $\mathbb{C}_{\mathbb{B}}$*; $\mathrm{Vect}(\mathbb{B})$ in §*The Complex Space Sector $\mathrm{Vect}(\mathbb{B})$*; $\mathbb{H}_{\mathbb{B}}$ in §*The Real Sector $\mathbb{H}_{\mathbb{B}}$*; $i\mathbb{H}_{\mathbb{B}}$ in §*The Imaginary Sector $i\mathbb{H}_{\mathbb{B}}$*; and the two sectors in *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*.

## The Coordinate Dictionary and the Sector Names

The dictionary between the parameters and the physical coordinates is fixed once and for all,

$$
q'_t = c\,t, \qquad (q_x, q_y, q_z) = (x, y, z), \qquad q_t = c\,t', \qquad (q'_x, q'_y, q'_z) = (x', y', z'),
$$

with $\vec x = x \vec e_x + y \vec e_y + z \vec e_z$ the real spatial vector and $i\vec x' = i x' \vec e_x + i y' \vec e_y + i z' \vec e_z$ its imaginary counterpart. The **material coordinate** $\tilde{Q} = ict\,e_t + \vec x$ and the **informational coordinate** $\tilde{Q} = ct'\,e_t + i\vec x'$ are the two ends of it, and each subspace keeps whichever part of the dictionary its defining condition leaves free.

| Subspace | Algebraic name | Physical name | Basis | Real parameters | Physical coordinates |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | The centre | Complex time sector | $e_t,\ ie_t$ | $q_t,\ q'_t$ | $ct',\ ict$ |
| $\mathrm{Vect}(\mathbb{B})$ | Vector | Complex space sector | $\vec e_x,\ \vec e_y,\ \vec e_z,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q_x,\ q_y,\ q_z,\ q'_x,\ q'_y,\ q'_z$ | $x,\ y,\ z,\ ix',\ iy',\ iz'$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion | Real sector | $e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $q_t,\ q_x,\ q_y,\ q_z$ | $ct',\ x,\ y,\ z$ |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion | Imaginary sector | $ie_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q'_t,\ q'_x,\ q'_y,\ q'_z$ | $ict,\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_+$ | Hermitian | Informational sector | $e_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q_t,\ q'_x,\ q'_y,\ q'_z$ | $ct',\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_-$ | Anti-Hermitian | Material sector | $ie_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $q'_t,\ q_x,\ q_y,\ q_z$ | $ict,\ x,\ y,\ z$ |

Each subspace carries an **algebraic name**, taken from the involution that defines it, and a **physical name**, taken from the role it plays; the companion articles are titled by the physical name.

**The informational coordinate under operator names.** Quantum physics writes the informational coordinate in the letters of an operator rather than of a coordinate: its four real parameters are named $h_0, h_1, h_2, h_3$ in place of $q_t, q'_x, q'_y, q'_z$, and the element is

$$
\tilde{H} = h_0e_t + ih_1\vec e_x + ih_2\vec e_y + ih_3\vec e_z, \qquad h_0, h_1, h_2, h_3 \in \mathbb{R},
$$

or, with the vector part assembled,

$$
\tilde{H} = h_0e_t + i\vec h , \qquad \vec h = h_1\vec e_x + h_2\vec e_y + h_3\vec e_z ,
$$

with $h_0 = ct'$ and $h_k = x'_k$. This is the informational coordinate $ct'\,e_t + i\vec x'$ of the table under the coefficient names of an operator, and its matrix image, under the unit images of §*The 2×2 Matrix Representation* ($\mathsf{M}_2(e_t) = I_2$ and the vector units $-i$ times the Pauli matrices $\sigma_1, \sigma_2, \sigma_3$), is the general Hermitian $2\times2$ matrix $h_0I_2 + h_1\sigma_1 + h_2\sigma_2 + h_3\sigma_3$ of *The Native Qubit and the Defining Module of the Biquaternion Algebra*. The tilde is required, because $H$ without it is the Hamiltonian, and $h$ without a subscript is the Planck constant.

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

pairs the two sectors — in this series' usage, *the sectors*, without qualification, are these two, and it is the split the relativistic articles are written in terms of. The two pairings cross: no sector is a half, and each sector draws its scalar slot from one half and its vector slots from the other, as *The Elements and their Coefficients* above records.

**The choice of which subspace is "real".** The convention that has to be flagged is that $\mathbb{M}_-$ is the *anti*-Hermitian subspace, so that the framework's "real" part is the part built on $i$ times a Hermitian element, where the more familiar convention takes the Hermitian part as real. The two differ only by the central factor $i$, and there is no mathematical error either way. What is unusual is that the convention is applied to the **field** rather than to the generators. Once it is, $\mathbb{M}_-$ is fixed by $\flat$ and $\mathbb{M}_+$ is not, and that is what makes $\mathbb{M}_-$ the framework's material subspace. A reader who "restores" the Hermitian convention will find the whole series inverted. Do not.

**The observed and its reading.** A **material element** is an element of $\mathbb{M}_-$; it is what is observed. Its **observable** is the Hermitian representative $iA\in\mathbb{M}_+$, whose eigenvalues are the real readings. The two are one quantity in two writings, and the central $i$ is the exchange between them.

## The Twelve Products and Their Names

The algebra carries **four general products** — one to each of the four choices of the two slots, the first factor read as it stands or through ${}^{\natural}$ and the second as it stands or through ${}^{*}$ — and each of the four splits into a **symmetric part** and an **antisymmetric part**, so that the complex space carries **twelve products** in all. The names are these, with the three-letter code the band articles write them by:

| The general product | Its symmetric part | Its antisymmetric part |
|---|---|---|
| The general plain bilinear product ($\mathrm{GPA}$) | The symmetric plain bilinear product ($\mathrm{SPA}$) | The antisymmetric plain bilinear product ($\mathrm{APA}$) |
| The general quaternionic bilinear product ($\mathrm{GQA}$) | The symmetric quaternionic bilinear product ($\mathrm{SQA}$) | The antisymmetric quaternionic bilinear product ($\mathrm{AQA}$) |
| The general plain sesquilinear product ($\mathrm{GPS}$) | The symmetric plain sesquilinear product ($\mathrm{SPS}$) | The antisymmetric plain sesquilinear product ($\mathrm{APS}$) |
| The general quaternionic sesquilinear product ($\mathrm{GQS}$) | The symmetric quaternionic sesquilinear product ($\mathrm{SQS}$) | The antisymmetric quaternionic sesquilinear product ($\mathrm{AQS}$) |

**The code is read letter by letter.** The first letter says which of the three operations of a row — $\mathrm G$ the general product, $\mathrm S$ its symmetric part, $\mathrm A$ its antisymmetric part; the second says which of the two products — $\mathrm P$ the plain one, whose first slot is read as it stands, and $\mathrm Q$ the quaternionic one, whose first slot carries ${}^{\natural}$; and the third says the family — $\mathrm A$ the **algebra** over $\mathbb{C}$, whose three products are $\mathbb{C}$-bilinear, and $\mathrm S$ the **sesqualgebra** over $(\mathbb{C},\bar{\cdot})$, whose three products are sesquilinear. The four general products are the multiplications of the four general structures of the band; the eight parts are the symmetric and antisymmetric products beside them; and the twelve codes together name the twelve algebraic structures of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

The products themselves — their coordinates, their laws, their units and their images — are *The 12 Products of the Biquaternioid Complex Space*, and the grid of the four general products is *The Four General Products and the Degree-2 Forms of the Biquaternion Space*.

**The same code on the reduced biquaternion space.** The construction is not special to $\mathbb{B}$. On the commutative algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C}$ — the reduced biquaternions, equivalently the tessarines or the double-complex numbers — the same four general products exist, $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$, and each splits into a symmetric and an antisymmetric part by the two exchanges. Because the algebra is **commutative**, four of the twelve codes name no new operation there: $\mathrm{SPA} = \mathrm{GPA}$ and $\mathrm{SQS} = \mathrm{GQS}$, while $\mathrm{APA} = 0$ and $\mathrm{AQS} = 0$. The space therefore carries **eight distinct algebraic structures** — $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ and the four live halves $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ — and the twelve slots, the four that collapse and the eight that remain are *The 12 Products of the Reduced Biquaternioid Complex Space* and *The Algebraic Structures over the Reduced Biquaternioid $\mathbb{C}$ Space* of the mathematical corpus, whose category is *Reduced Biquaternions*. The letter $\mathrm Q$ keeps its sense there — the first slot read through ${}^{\natural}$, the tessarine conjugation $e\mapsto-e$ — as in the band above.

## The Involutions and the Four Forms

The algebra carries four conjugations, and on it there are four forms, each applying one conjugation to each of its two arguments, so the two lists are one list read twice. One rule ties the two lists together, and that rule is what lets the series say which form is the metric and which is the inner product without having to choose.

**The setting.** $\mathbb{B}$ is a $\mathbb{C}$-algebra whose centre is $\mathbb{C}$, so every complex scalar is central, $\lambda\tilde{Q} = \tilde{Q}\lambda$ for all $\lambda \in \mathbb{C}$, which is the property that makes "$\mathbb{C}$-bilinear" well defined on $\mathbb{B}$; the scalar part $\mathrm{Sc}(\tilde{Q}) = Q_t$ is $\mathbb{C}$-linear. The centre is treated in *Other Remarkable Subspaces*, §*The Complex Time Sector $\mathbb{C}_{\mathbb{B}}$*, and the forms of the algebra in *Hermitian Forms over the Biquaternioid Algebra and the Unitary Witt Group with Hermitian Adjoint* and its mathematical twin *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and, on the side of positivity, in *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint*.

**The four conjugations.** The tensor product $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is built from two rings that each carry two involutions, the identity and the conjugation, so it carries $2\times 2 = 4$, together with the derived anti-Hermitian sign:

| Map | Mark | Action | As a ring map | Over $\mathbb{C}$ |
|---|---|---|---|---|
| Identity | — | $\tilde{Q} \mapsto \tilde{Q}$ | Automorphism | $\mathbb{C}$-**linear** |
| Complex conjugation | $\bar{\cdot}$ | $Q_\mu \mapsto \bar{Q}_\mu$ | **Automorphism**: conjugation on the scalars, identity on the quaternion factor | $\mathbb{C}$-**antilinear** |
| Quaternion conjugation | ${}^{\natural}$ | $Q_te_t - Q_x\vec e_x - Q_y\vec e_y - Q_z\vec e_z$ | **Anti-automorphism**: identity on the scalars, conjugation on the quaternion factor | $\mathbb{C}$-**linear** |
| Hermitian conjugation | ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ | $\bar{Q}_te_t - \bar{Q}_x\vec e_x - \bar{Q}_y\vec e_y - \bar{Q}_z\vec e_z$ | **Anti-automorphism** | $\mathbb{C}$-**antilinear** |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | $-\tilde{Q}^{*}$ | **Neither** | $\mathbb{C}$-**antilinear** |

The fourth column is what the two questions separate. The bar acts on the scalars and on nothing else, so it is an order-two automorphism, $\mathbb{C}$-antilinear and **not** an anti-automorphism. The quaternion conjugation and the Hermitian conjugation are the two genuine **involutions of the ring**, $(\tilde{Q}_1\tilde{Q}_2)^{\natural} = \tilde{Q}_2^{\natural}\tilde{Q}_1^{\natural}$ and $(\tilde{Q}_1\tilde{Q}_2)^{*} = \tilde{Q}_2^{*}\tilde{Q}_1^{*}$, the quaternion conjugation being the one that touches only the quaternion factor. The anti-Hermitian sign is neither: it reverses with a twist, $(\tilde{Q}_1\tilde{Q}_2)^{\flat} = -\tilde{Q}_2^{\flat}\tilde{Q}_1^{\flat}$, so it is an involution of the underlying real vector space and nothing more. The four maps and the sign, their fixed and anti-fixed spaces, and the lattice they form are *Comparison of the Remarkable Subspaces*.

**The generic form.** The series writes a **generic form** $\mathrm{Form}(\tilde{Q}_1,\tilde{Q}_2)$, the form of the statement at hand, of which the four below are the instances; the matching generic norm is stated with the norms in §*The Four Algebraic Norms*.

**The four forms, written out.** Each conjugation applied to the first argument and each to the second gives one form. The four are written with the single bracket $\langle\cdot,\cdot\rangle$, whose subscript records the pair of conjugations — nothing when the identity sits in both, ${}^{\natural}$ when the quaternion conjugation sits in the first, ${}^{*}$ when the Hermitian conjugation sits in the second, and $\natural*$ when both sit.

The **plain form** applies the identity to both arguments:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2) = Q_{1t}Q_{2t} - Q_{1x}Q_{2x} - Q_{1y}Q_{2y} - Q_{1z}Q_{2z},
$$

$\mathbb{C}$-**bilinear** in both arguments; on $\mathbb{M}_-$ it is $-c^2t^2-x^2-y^2-z^2$, signature $(0,4)$.

The **quaternionic form** applies the quaternion conjugation to the first argument and the identity to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural} = \mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2) = Q_{1t}Q_{2t} + Q_{1x}Q_{2x} + Q_{1y}Q_{2y} + Q_{1z}Q_{2z},
$$

$\mathbb{C}$-**bilinear** in both arguments; on $\mathbb{M}_-$ it is $-c^2t^2+x^2+y^2+z^2$, signature $(3,1)$.

The **Hermitian form** applies the identity to the first argument and the Hermitian conjugation to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*}) = Q_{1t}\bar{Q}_{2t} + Q_{1x}\bar{Q}_{2x} + Q_{1y}\bar{Q}_{2y} + Q_{1z}\bar{Q}_{2z},
$$

$\mathbb{C}$-**sesquilinear**, linear in the first argument and antilinear in the second; on $\mathbb{M}_-$ it is $c^2t^2+x^2+y^2+z^2$, signature $(4,0)$.

The **Krein form** applies the quaternion conjugation to the first argument and the Hermitian conjugation to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*} = \mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2^{*}) = Q_{1t}\bar{Q}_{2t} - Q_{1x}\bar{Q}_{2x} - Q_{1y}\bar{Q}_{2y} - Q_{1z}\bar{Q}_{2z},
$$

$\mathbb{C}$-**sesquilinear**, linear in the first argument and antilinear in the second; on $\mathbb{M}_-$ it is $c^2t^2-x^2-y^2-z^2$, signature $(1,3)$.

Each form is the trace of its own product up to the factor $2$ of the trace convention,

$$
2\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2), \qquad 2\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural} = \operatorname{Tr}(\tilde{Q}_1^{\natural}\tilde{Q}_2),
$$

$$
2\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2^{*}), \qquad 2\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*} = \operatorname{Tr}(\tilde{Q}_1^{\natural}\tilde{Q}_2^{*}).
$$

**The type is decided by the second argument.** The scalars are central and $\mathrm{Sc}$ is $\mathbb{C}$-linear, so a conjugation that is $\mathbb{C}$-linear passes a complex scalar out of its argument unchanged, while a conjugation that is $\mathbb{C}$-antilinear conjugates it. The identity and the quaternion conjugation are $\mathbb{C}$-linear and the Hermitian conjugation is $\mathbb{C}$-antilinear, so a scalar leaving the second argument comes out barred in exactly the two sesquilinear forms:

$$
\langle\tilde{Q}_1,\lambda\tilde{Q}_2\rangle = \lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle, \qquad \langle\tilde{Q}_1,\lambda\tilde{Q}_2\rangle_{\natural} = \lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural},
$$

$$
\langle\tilde{Q}_1,\lambda\tilde{Q}_2\rangle_{*} = \bar\lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}, \qquad \langle\tilde{Q}_1,\lambda\tilde{Q}_2\rangle_{\natural*} = \bar\lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*} .
$$

In the first argument no scalar is conjugated, every first-slot conjugation being $\mathbb{C}$-linear:

$$
\langle\lambda\tilde{Q}_1,\tilde{Q}_2\rangle = \lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle, \qquad \langle\lambda\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} .
$$

Throughout the series a signature is written $(n,m)$ with the **positive** directions counted first, so that $(-,-,-,-)$ is $(0,4)$.

**Where the four are proved and named.** The classification of the four, their Gram matrices, their signatures, their isometry groups, their Witt classes, and their reading as Hermitian forms over the algebra with respect to their own involutions are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, with its twin *Hermitian Forms over the Biquaternioid Algebra and the Unitary Witt Group with Hermitian Adjoint*.

**What is forced and what is chosen.** The two bilinear forms are $\mathbb{C}$-bilinear in both slots and the two sesquilinear forms are linear in the first slot and sesquilinear in the second. That is not a choice but a consequence of the $\mathbb{C}$-linearity of the natural sign together with the centrality of $\mathbb{C}$ in $\mathbb{B}$; its verification is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. Multiplication by $i$ reverses the sign of the two bilinear forms and leaves the two sesquilinear forms unchanged, since the centrality of $i$ puts either a factor $i^2 = -1$ on both slots or on neither.

## The Base and Its Units

The base is written with the letter $e$, one unit to a direction. The scalar unit is $e_t = 1$ and the three vector units are $\vec e_x, \vec e_y, \vec e_z$; the arrow is the only mark that separates the scalar unit from the vector units. A general element is written in the base,

$$
\tilde Q = Q_t e_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $e_\mu$ the unit of the direction $\mu$ — the arrowless $e_t$ at $\mu = t$ and the arrowed $\vec e_\mu$ at $\mu = x, y, z$. The three vector units close on the scalar unit and on one another,

$$
e_t = 1, \qquad \vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t , \qquad \vec e_x\vec e_y = -\vec e_y\vec e_x = \vec e_z ,
$$

and cyclically, the space index running over $k = x, y, z$. **The notation is the unit along the axis.** A coefficient carries the name of the direction it multiplies, as in $\vec v = v_x\hat x + v_y\hat y + v_z\hat z$ of the vector calculus: $Q_x$ is the coefficient of $\vec e_x$, the label on the unit names the direction and the label on the coefficient names the same direction, so $q_x = x$ reads without ambiguity. **The base letter is $e$ and the unit-element letter is $u$, and the two are never exchanged.** The base units carry $e$, so $e$ is not available for the exponential, which is written $\exp(\cdot)$; a unit element of a layer carries the glyph of the unit element, $\tilde u$ or $\tilde U$ (§*The Unitary Convention*).

## The Four Algebraic Norms and the Unitary Convention

**The definition of a norm.** The norm of a form is that form read at its two equal arguments,

$$
\mathrm{Norm}(\tilde{Q}) = \mathrm{Form}(\tilde{Q},\tilde{Q}) ,
$$

and the convention is one of **notation, not of substance**: the pair is the form and the norm of the statement at hand, and the four forms above and the four norms below are its instances.

**The four algebraic norms.** Each pair gives one norm, the diagonal of its form. **One bracket, two arities:** the bracket names the form when it carries two arguments and the algebraic norm when it carries one, so the plain bracket is the form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ and the norm $\langle\tilde{Q}\rangle = \langle\tilde{Q},\tilde{Q}\rangle$, and the same holds for the Hermitian, the quaternionic and the Krein. Read with one argument, the value lies in $\mathbb{C}$ for the two bilinear norms and in $\mathbb{R}$ for the two sesquilinear norms, because a sesquilinear form has a real diagonal. The four names are those of the four forms with *norm* in place of *form*:

| Norm | Conjugations, first and second argument | Definition | Value | Value in |
|---|---|---|---|---|
| the plain norm | identity, identity | $\langle\tilde{Q}\rangle = \langle\tilde{Q},\tilde{Q}\rangle = \mathrm{Sc}(\tilde{Q}\tilde{Q})$ | $Q_t^2 - Q_x^2 - Q_y^2 - Q_z^2$ | $\mathbb{C}$ |
| the quaternionic norm | quaternion, identity | $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2$ | $\mathbb{C}$ |
| the Hermitian norm | identity, Hermitian | $\langle\tilde{Q}\rangle_{*} = \langle\tilde{Q},\tilde{Q}\rangle_{*} = \mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})$ | $\lvert Q_t\rvert^2 + \lvert Q_x\rvert^2 + \lvert Q_y\rvert^2 + \lvert Q_z\rvert^2$ | $\mathbb{R}$ |
| the Krein norm | quaternion, Hermitian | $\langle\tilde{Q}\rangle_{\natural*} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural*} = \mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q}^{*})$ | $\lvert Q_t\rvert^2 - \lvert Q_x\rvert^2 - \lvert Q_y\rvert^2 - \lvert Q_z\rvert^2$ | $\mathbb{R}$ |

Read on one argument the four are the plain norm, the Hermitian norm, the quaternionic norm and the Krein norm. The other sense of the word, the **topological norm**, is the square root of the definite one, $\lVert\tilde{Q}\rVert_E = \bigl(\langle\tilde{Q}\rangle_{*}\bigr)^{1/2}$, and it is *The Norm Defined by a Form*. The four products, their forms and their norms go together, one to a row:

| Product | Form | Norm |
|---|---|---|
| the general plain bilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the plain norm $\langle\tilde{Q}\rangle$ |
| the general plain sesquilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the Hermitian norm $\langle\tilde{Q}\rangle_{*}$ |
| the general quaternionic bilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the quaternionic norm $\langle\tilde{Q}\rangle_{\natural}$ |
| the general quaternionic sesquilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}$ | the Krein norm $\langle\tilde{Q}\rangle_{\natural*}$ |

### The Unitary Convention

A unit element carries its own glyph, the **$u$** in the two cases, beside the root $\tilde\Xi$, the idempotent $\tilde\Pi$ and the nilpotent $\tilde\nu$, as in the mathematical corpus (§*The Unitary Convention* of *Conventions in Mathematics*): the letter $u$ is reserved for a unit element, and a general element is $\tilde q$ or $\tilde Q$. **The exponential is written $\exp(\cdot)$**, never $e^{\cdot}$, the letter $e$ being the base $e_t,\vec e_x,\vec e_y,\vec e_z$ and the electric charge. A unit element is an element of norm one, and the norm is the one in view: the glyph is the generic norm read at the central value $e_t$, so it names no set until the norm is named, and the four norms of the biquaternion layer give four level sets:

| Norm | the condition $\mathrm{Norm}(\tilde U)=e_t$ | the norm-one elements |
|---|---|---|
| $\langle\tilde Q\rangle$ | $Q_t^2-Q_x^2-Q_y^2-Q_z^2=e_t$ | the complex hyperboloid of the plain norm |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2=e_t$ | $\mathbb{B}^{\times}_1$, the norm-one units |
| $\langle\tilde Q\rangle_{*}$ | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2=1$ | the unit sphere of the Hermitian norm |
| $\langle\tilde Q\rangle_{\natural*}$ | $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2=1$ | the indefinite level set of the Krein norm |

The two bilinear norms are complex-valued, so their condition is $=e_t$; the two sesquilinear norms are real-valued, so theirs is $=1$. In the quaternion layer the level set is $Sp(1)=\{\tilde u\in\mathbb{H}:\tilde u\tilde u^{\natural}=e_t\}=S^{3}=\mathrm{SU}(2)$, and **the rotors are these elements**: an orientation rotor, of norm $e_t$, is a unit real quaternion and is written $\tilde u$.

**The group condition is narrower than the norm-one condition.** Where the sesquilinear form is preserved, $\tilde U^{*}\tilde U=e_t$, the norm-one elements that do so form the **unitary group**, written without the tilde of an element,

$$
U(\mathbb{B})=\{\tilde U:\tilde U^{*}\tilde U=e_t\}\cong U(2)=S^{1}\cdot S^{3},\qquad S^{1}\cap S^{3}=\{\pm e_t\},
$$

of real dimension $4$. The name **unitary** is the name of that group; the glyph $\tilde U$ is the wider norm-one element. The norm and the group condition exist only where their involution does: the bar alone over $\mathbb{C}$ and the split-complex numbers, the natural sign alone over $\mathbb{H}$ and the split-quaternions, all four marks over $\mathbb{B}$ and the split-biquaternions.

**The case rule splits the glyph**, as for the elements: $\tilde U$ in the biquaternion and split-biquaternion layers, $\tilde u$ in the quaternion and split-quaternion ones, and $U$ in the complex, split-complex, dual and reduced biquaternion ones. The pure case carries the arrow, $\vec u$ and $\vec U$.

**The coordinates carry the letter of the unit element**: in $\mathbb{B}$ it is $\tilde U = U_te_t + U_x\vec e_x + U_y\vec e_y + U_z\vec e_z$ with $U_\mu = u_\mu + iu'_\mu$ and vector part $\vec U = \vec u_\mu + i\vec u'_\mu$; in $\mathbb{H}$ it is $\tilde u = u_te_t + u_x\vec e_x + u_y\vec e_y + u_z\vec e_z$ with real $u_\mu$. **A coordinate carries the label of its direction**, as the base does: the scalar coordinate is $U_t$ and the vector coordinates are $U_x, U_y, U_z$, and likewise $u_t, u_x, u_y, u_z$ for the quaternion-layer element $\tilde u$; a role label is written in the upright roman where the statement names a role. **It is allowed to add subscripts when several unit elements are used**, $\tilde U_1, \tilde U_2$.

**The letter $u$ names a unit element and nothing else.** A velocity, a speed, a Lorentz factor and a rapidity are never written $u$ or $U$: the letter of a motion is $v$, and the four-velocity is the element $\tilde V$. A unitary group is written $U(1)$, $SU(2)$, $SU(3)$, and its Lie algebra in the upright roman, $\mathrm{u}(1)$, $\mathrm{su}(2)$, $\mathrm{su}(3)$.

## The Central Map and Its Restrictions

The scalar imaginary $i$ is central, so multiplication by it is **one** $\mathbb{C}$-linear map of the algebra, and the movements the series reads in four places are its restrictions to the subspaces. The generator satisfies $(ie_t)^2=-e_t$, so its powers close on four values and the group $\exp(i\theta)e_t$ of the centre interpolates between them. The remarkable subspaces carry the restrictions.

| Subspace | $i\,\cdot$ | The name |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the complex time sector | Itself | The global phase |
| $\mathrm{Vect}(\mathbb{B})$, the complex space sector | Itself | The duality rotation |
| $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ | Each other | The Wick rotation |
| $\mathbb{M}_-$ and $\mathbb{M}_+$ | Each other | The material–informational exchange |

The rule that ties the names is a rule about the generator and not about the subspaces: the map is central, so it acts the same way in every subspace, and it is a scalar that acts through the centre and never through the quaternion directions; a non-central generator would give one rotation per carrier. It is a rotation and not a projection, a collapse or a measurement — a loss of information is a non-invertible map and belongs to *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*.

**The relation to the Wick rotation.** The coordinate continuation $t \mapsto -i\tau$ of *Interpretation of the Wick Rotation in the Biquaternion Universe*, and the two senses in which the series uses the phrase *Wick rotation* — the exchange of the real and imaginary sectors, on the whole element, and the continuation of the time coordinate, a relabeling of one coordinate — are set out there. The two share one generator and one temporal sign flip, and they are not the same map.

The phase gate of the gate articles is a rotation about $\vec e_z$, a non-central generator, and it must not be identified with the central rotation.

## The Special Elements: Root, Idempotent and Nilpotent

### The Root Convention

The roots carry a symbol of their own, beside the idempotent $\tilde{\Pi}$ (§*The Idempotent Convention*) and the nilpotent $\tilde{\nu}$ (§*The Nilpotent Convention*): the **xi**, in the two cases.

A **root of $1$** of the algebra is an element $\tilde{\Xi}$ with $\tilde{\Xi}^2 = 1$. More generally a **root of a central value** $\lambda$ is an element with $\tilde{\Xi}^2 = \lambda e_t$. The roots of the three central values $-1, 0, +1$ are those of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general root is that of *Square Roots of a General Element in the Biquaternion Algebra*; the roots the series uses are the roots of $1$.

**The square is read in a named product**, the algebra product unless the statement names another, as for the nilpotents (§*The Nilpotent Convention*), and the class is relative to the product; the roots of a value in the four general products are those of *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

**The case rule splits the glyph, as it does for the elements, the idempotents and the nilpotents.** The roots of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde{\Xi}$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde{\xi}$; and those of the complex, split-complex, dual and reduced biquaternion layers carry the plain capital, $\Xi$, no tilde being written where there is no quaternionic factor. The layer fixes the glyph.

**The coordinates carry the letter of the root**: in $\mathbb{B}$ the root is $\tilde{\Xi} = \Xi_te_t + \Xi_x\vec e_x + \Xi_y\vec e_y + \Xi_z\vec e_z$ with $\Xi_\mu = \xi_\mu + i\xi'_\mu$, its scalar part $\Xi_t$ and its vector part $\vec\Xi = \vec\xi + i\vec\xi'$; in $\mathbb{H}$ it is $\tilde\xi = \xi_te_t + \xi_x\vec e_x + \xi_y\vec e_y + \xi_z\vec e_z$ with real $\xi_\mu$.

**It is allowed to add subscripts when several roots are used.** **The subscript of a root is numeric when it counts and a role label when it names.** Where more than one occurs the roots are numbered, $\tilde\Xi_1, \tilde\Xi_2$, as for the nilpotents and for the idempotent pairs other than the complete sign pair of §*The Idempotent Convention*; where a root plays a named role, it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The root glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde{\Xi}$ | A root of $1$ of the biquaternion or split-biquaternion layer |
| $\tilde{\xi}$ | A root of $1$ of the quaternion or split-quaternion layer |
| $\Xi$ | A root of $1$ of the complex, split-complex, dual or reduced biquaternion layer, where no tilde is written |

The convention is one of **notation, not of substance**: an element written $\tilde{\Xi}$ is not a different kind of object from one written $\tilde{Q}$, only an element known to be a root of $1$.

### The Idempotent Convention

The convention of *The Elements and their Coefficients* fixes the case and the tilde of a generic element. The idempotents carry a symbol of their own, and the series uses it throughout.

An **idempotent** of the algebra is an element $\tilde{\Pi}$ with $\tilde{\Pi}^2 = \tilde{\Pi}$; a **projector** is a Hermitian idempotent, $\tilde{\Pi}^{*} = \tilde{\Pi}$, and the rank-one projectors of $\mathbb{M}_+$ are the **pure states** of the informational sector.

**The case rule splits the glyph, as it does in the mathematical corpus.** The idempotents of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde{\Pi}$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde{\pi}$; and those of the complex, split-complex, dual and reduced biquaternion layers carry the plain capital, $\Pi$, no tilde being written where there is no quaternionic factor. The series works in $\mathbb{B}$ and writes $\tilde{\Pi}$ throughout; the other two glyphs are the mathematical corpus's, and the layer fixes the glyph.

A non-zero idempotent $\tilde{\Pi}$ generates the **minimal left ideal** $\mathbb{B}\tilde{\Pi}$, which is the state module of the companion articles; the standard pair, the classification of the idempotents, the polarisation identity, the Peirce decomposition, the matrix units and the projective geometry of the pure states are those of *Square Roots of One and the Idempotents of the Biquaternion Algebra* and its companions in the mathematical corpus.

**The coordinates carry the letter of the idempotent**: in $\mathbb{B}$ the idempotent is $\tilde{\Pi} = \Pi_te_t + \Pi_x\vec e_x + \Pi_y\vec e_y + \Pi_z\vec e_z$ with $\Pi_\mu = \pi_\mu + i\pi'_\mu$, its scalar part $\Pi_t$ and its vector part $\vec\Pi = \vec\pi + i\vec\pi'$; in $\mathbb{H}$ it is $\tilde\pi = \pi_te_t + \pi_x\vec e_x + \pi_y\vec e_y + \pi_z\vec e_z$ with real $\pi_\mu$.

**It is allowed to add subscripts when several idempotents are used.** **The subscript of an idempotent is numeric when it counts and a role label when it names, but for the two members of a complete sign pair.** A pair is $\tilde{\Pi}_1, \tilde{\Pi}_2$; a second pair in the same statement takes the next numbers, $\tilde{\Pi}_3, \tilde{\Pi}_4$; and a family indexed by a direction is written with its argument, $\tilde{\Pi}_{1,2}(\vec u)$. When a pair is **complete**, $\tilde{\Pi}_+ + \tilde{\Pi}_- = e_t$, its two members may be written $\tilde{\Pi}_+$ and $\tilde{\Pi}_-$: the subscript $+$ names the member attached to $+1$ and the subscript $-$ the member attached to $-1$. A pair that is not complete may be numbered, labelled or signed as the statement requires. A role label is written in upright roman, as for a unit element.

The idempotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde{\Pi}$ | An idempotent, a projector or a pure state of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde{\Pi}$ it generates |
| $\tilde{\pi}$ | An idempotent of the quaternion or split-quaternion layer, in the mathematical corpus |
| $\Pi$ | An idempotent of the complex, split-complex, dual or reduced biquaternion layer, in the mathematical corpus |

The convention is one of **notation, not of substance**: an element written $\tilde{\Pi}$ is not a different kind of object from one written $\tilde{Q}$, only an element known to be idempotent, and the glyph records that knowledge at the point of use; a passage that needs a generic idempotent variable writes $\tilde{\Pi}$.

### The Nilpotent Convention

The nilpotents carry a symbol of their own, beside the idempotent $\tilde{\Pi}$ (§*The Idempotent Convention*): the lower-case $\tilde{\nu}$ of the quaternion and split-quaternion layers and the upper-case $\tilde{\Upsilon}$ of the biquaternion and split-biquaternion layers. **The capital is an upsilon and not a $Y$.**

A **nilpotent** of the algebra is an element $\tilde{\nu}$ whose square vanishes,

$$
\tilde{\nu}^2 = 0 .
$$

**The square is read in a named product**, the algebra product unless the statement names another, as in the mathematical corpus (§*The Nilpotent Convention* of *Conventions in Mathematics*), and the class is relative to the product. A nilpotent is never a projector, a Hermitian nilpotent being zero, and it is never a state; the nilpotent is the partner of the idempotent in a minimal left ideal, $\mathbb{B}\vec{\Upsilon}_2 = \mathbb{B}\tilde{\Pi}_1$.

**The coordinates carry the letter of the nilpotent**: in $\mathbb{B}$ the nilpotent is $\tilde{\Upsilon} = \Upsilon_te_t + \Upsilon_x\vec e_x + \Upsilon_y\vec e_y + \Upsilon_z\vec e_z$ with $\Upsilon_\mu = \nu_\mu + i\nu'_\mu$, its scalar part $\Upsilon_t$ and its vector part $\vec\Upsilon = \vec\nu + i\vec\nu'$; in $\mathbb{H}$ it is $\tilde\nu = \nu_te_t + \nu_x\vec e_x + \nu_y\vec e_y + \nu_z\vec e_z$ with real $\nu_\mu$.

**It is allowed to add subscripts when several nilpotents are used.** **The subscript of a nilpotent is numeric when it counts and a role label when it names**, as for the idempotents apart from their complete sign pair: where more than one occurs a pair is $\tilde{\nu}_1, \tilde{\nu}_2$, a second pair in the same statement takes the next numbers, and where a nilpotent plays a named role it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The nilpotents have no classification of the idempotent kind and no sphere of pure states; which set the square-zero elements form depends on the product. The nilpotents of a state module are those of *The Biquaternion Vacuum as a Minimal Idempotent*, and the spin-down state of *Spin-1/2 Quantum Physics in Biquaternionic Form* is a nilpotent of the ideal of that vacuum.

The nilpotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde{\Upsilon}$ | A nilpotent of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde{\Upsilon}$ it generates |
| $\tilde{\nu}$ | A nilpotent of the quaternion or split-quaternion layer |
| $\vec{\Upsilon}$, $\vec{\nu}$ | A pure nilpotent, written with the arrow and without the tilde by the priority rule of §*Pure Elements and their Coefficients* |
| $\Upsilon$ | A nilpotent of the complex, split-complex or dual layer, where no tilde is written |

The convention is one of **notation, not of substance**: an element written $\tilde{\nu}$ is not a different kind of object from one written $\tilde{Q}$, only an element known to be nilpotent.

The standard pair of nilpotents is $\vec{\Upsilon}_1$ and $\vec{\Upsilon}_2$, the off-diagonal Peirce units of *Ideals and Peirce Decomposition of the Biquaternion Algebra* exchanged by the star. The truncated ladder of *The Biquaternion Vacuum as a Minimal Idempotent* and of the Fock, vacuum and matrix-representation articles is this pair: those articles write it $\vec{\Upsilon}_1$ and $\vec{\Upsilon}_2$ wherever the algebra element is meant, and keep the ladder letters for the abstract operators.

**The standard pair carries the arrow, not the tilde.** The two Peirce units are pure, $\vec{\Upsilon}_1 = \tfrac12(i\vec e_x - \vec e_y)$ and $\vec{\Upsilon}_2 = \tfrac12(i\vec e_x + \vec e_y)$, with no scalar part, so by §*Pure Elements and their Coefficients* the arrow takes priority over the tilde and the tilde is dropped; the pair is written $\vec{\Upsilon}_1, \vec{\Upsilon}_2$ and never $\tilde{\Upsilon}_1, \tilde{\Upsilon}_2$. The tilde is kept for the general nilpotent $\tilde{\Upsilon}$, which may carry a scalar part and is not pure.

## The Four-Vector Representation

The algebra is read as the quadruple of its complex coefficients, in *The Four-Vector Element Representation of Biquaternions*. Each unit is one coordinate place,

$$
e_t \longleftrightarrow (1,0,0,0), \qquad \vec e_x \longleftrightarrow (0,1,0,0), \qquad \vec e_y \longleftrightarrow (0,0,1,0), \qquad \vec e_z \longleftrightarrow (0,0,0,1),
$$

so that an element is its quadruple of coefficients,

$$
\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu \;\longleftrightarrow\; (Q_t, Q_x, Q_y, Q_z).
$$

**No index is raised or lowered anywhere in the series.** On $\mathbb{C}^4$ there is no pairing with which to move one, and the $ict$ convention is what puts the metric into the coefficient — $(ict, \vec x)$ rather than a contraction rule — so that the interval is the sum of squares with no explicit scalar product. The article owns the product in components.

## The 4×4 Matrix Representation

Multiplication is read as a linear map on that quadruple, in *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The four units act by

$$
\mathsf{M}_4(e_t) = I_4 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \qquad
\mathsf{M}_4(\vec e_x) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix},
$$

$$
\mathsf{M}_4(\vec e_y) = \begin{pmatrix} 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{pmatrix}, \qquad
\mathsf{M}_4(\vec e_z) = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix},
$$

and each of the three vector matrices squares to $-I_4$, as $\vec e_k^2 = -e_t$ requires. For a general element, left multiplication by $\tilde{Q}$ is the matrix $\mathsf{M}_4(\tilde{Q})$, and right multiplication is the same construction, giving $\mathsf{M}_4^{R}(e_t) = I_4$ and $\mathsf{M}_4^{R}(\vec e_k) = \eta\,\mathsf{M}_4(\vec e_k)^{\mathsf{T}}\eta$, with $\eta = \operatorname{diag}(-1,+1,+1,+1)$. The two sides are distinguished on purpose and are not interchangeable: $\mathsf{M}_4^{R}(\tilde{Q})$ is not $\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$, and what relates them is the metric, not a relabelling.

The determinant and the trace of the two regular matrices, the relation between $\mathsf{M}_4^{R}$ and $\mathsf{M}_4$, and the volume identity $\det\mathsf{M}_4(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural}^2$ are *The $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*.

## The 2×2 Matrix Representation

The algebra is read as the complex $2 \times 2$ matrices, under the isomorphism

$$
\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C}),
$$

in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and this is the representation every numerical check in the series is performed with. The four unit images are fixed here, once, because every article depends on them agreeing. The three vector units are the Pauli matrices times $-i$:

$$
\mathsf{M}_2(e_t) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\mathsf{M}_2(\vec e_x) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_z) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

with the central scalar mapping to $\mathsf{M}_2(i) = iI_2$. Because $\mathsf{M}_2$ is $\mathbb{C}$-linear, the Hermitian units require no separate choice, $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$.

**The trace is the trace of this image.** The series writes

$$
\operatorname{Tr}(\tilde{Q}) := \operatorname{Tr}\mathsf{M}_2(\tilde{Q}).
$$

On the units $\operatorname{Tr}(e_t) = 2$ and $\operatorname{Tr}(\vec e_k) = 0$, so on a general element $\operatorname{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$. That factor $2$ is not a normalisation but a consequence of $\mathsf{M}_2(e_t) = I_2$: it comes with the four images above, it cannot be divided out, and every pairing in the series is written with it, the Born rule $p = \operatorname{Tr}(\tilde{Q}_1\tilde{\rho})$ among them. An unsubscripted trace means this one; a regular matrix has its own, written with its subscript. The unrestricted identity $\operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2)$ is recorded with its verification in the article just named.

**The determinant is the norm.** The determinant of the image is the biquaternion norm, $\det\mathsf{M}_2(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}$, and it is multiplicative, which is what makes the matrix model compute every norm in the series. The invertibility criterion, the group of units and the unit-norm group are read from it; the derivations are *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

**The assignment is forced, not chosen.** $\vec e_k^2 = -e_t$ requires the factor $i$ and $\vec e_x\vec e_y = \vec e_z$ fixes the sign, so neither the factor nor the sign in the three vector images could have been otherwise. A reviewer must not "correct" the assignment by making the three images real, nor by negating all three. *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* derives both.

**Never conjugate the matrix entries on their own.** Conjugating the entries of $\mathsf{M}_2(\tilde{Q})$ is *not* the image of any involution of the algebra: it negates the images of $\vec e_x$ and $\vec e_z$ while leaving $\mathsf{M}_2(\vec e_y)$, which has real entries, untouched, and so it destroys the sector dictionary. The four conjugations $\natural$, $\bar{\phantom{Q}}$, ${}^{*}$ and $\flat$ are evaluated through the matrix formulas recorded in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, never by conjugating entries.

**The realisation is a convention of presentation, not of content.** The isomorphisms that preserve the subspace dictionary are the $\mathsf{M}_2' = S\mathsf{M}_2 S^{-1}$ with $S$ unitary up to a nonzero complex scalar, and an arbitrary invertible $S$ destroys the dictionary. The practical consequence is that a mistake of translation between the algebra and its matrices is repaired **here** — by correcting the assignment or the explicit factors of $i$ — and never by altering the biquaternion norm, the $ict$ assignment or the sector split.

**A bare $\mathsf{M}_2$ means this isomorphism and nothing else.** A plain $\mathsf{M}_2$, with no subscript, superscript or tilde, is reserved throughout the series for this isomorphism alone. The other uses a reader may meet are marked differently: $\varphi$ is an abstract homomorphism on the mathematics pages and an angle in the Thomas-precession exercise, $\tilde{\Phi} = \varphi\,e_t$ is the central scalar field of the Higgs articles, and $\Phi_{\tilde{U}}$ is the quantum channel of the gates article. None of these is the isomorphism, and a bare $\mathsf{M}_2$ is not any of them.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; all partial derivatives are written explicitly with $\partial$. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm r}$; it never denotes a derivative. The derivative of a field with respect to a coordinate is written $\partial_xv$, $\partial_tv$ or $\partial_\mu v$, and it is why the corpus writes $\partial_uL$ and $\partial_pL$ where a PDE text writes $L_u$ and $L_p$. The rule holds on every object of the series, whether the letter names an element of the algebra, an element-valued field, a kernel or an operator.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.**

**The prime.** No derivative is contracted to a mark on the letter: every derivative is written with an explicit operator and its variable is named where it is used, so that one glyph never has to stand for different variables in different places. The prime is reserved for the derivative with respect to the single argument of a function of one variable, and a second derivative is written with $\partial$, never with a repeated subscript.

**The two derivative operators of the series** are the **gradient** $\nabla$ and the **d'Alembertian** $\Box$, fixed in the subsection below and in no other place; every other derivative is written with $\partial$.

### The Gradient and the d'Alembertian

The series' d'Alembertian is built from the **biquaternionic gradient**

$$
\tilde{\nabla} = e_t\frac{\partial}{\partial Q_t} + \vec e_x\frac{\partial}{\partial Q_x} + \vec e_y\frac{\partial}{\partial Q_y} + \vec e_z\frac{\partial}{\partial Q_z} = \sum_{\mu\in\{t,x,y,z\}} e_\mu\frac{\partial}{\partial Q_\mu}
$$

and its **quaternion conjugate**

$$
\tilde{\nabla}^{\natural} = e_t\frac{\partial}{\partial Q_t} - \vec e_x\frac{\partial}{\partial Q_x} - \vec e_y\frac{\partial}{\partial Q_y} - \vec e_z\frac{\partial}{\partial Q_z},
$$

the involution of the norm. It is this conjugate and no other that the series composes with (*Biquaternion Analysis*, §*The Biquaternionic Gradient*, §*The Quaternion Conjugate of the Gradient* and §*The d'Alembertian*), and the two orders agree:

$$
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \frac{\partial^2}{\partial Q_t^2} + \Delta_Q ,
$$

with $\Delta_Q = \partial^2/\partial Q_x^2 + \partial^2/\partial Q_y^2 + \partial^2/\partial Q_z^2$ the Laplacian in the three vector coordinates, the whole of it **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box\tilde{F} = \sum_\mu(\Box F_\mu)e_\mu$, and it is the norm of the gradient, $\Box = \langle\tilde{\nabla},\tilde{\nabla}\rangle_{\natural}$ (*The Four Forms, the Four Algebraic Norms and the Change of Scalars*). The operator is $\partial^2/\partial Q_t^2 + \Delta_Q$ on the whole algebra; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. On the material sector $\mathbb{M}_-$, where $Q_t = ict$ and $Q_k = q_k$, the derivative $\partial^2/\partial Q_t^2 = -c^{-2}\partial_t^2$ and the same operator reads

$$
\Box\big|_{\mathbb{M}_-} = \Delta - c^{-2}\partial_t^2 = \partial_{ict}^2 + \Delta ,
$$

a plus on the spatial part and a minus on the time part. **The $ict$ substitution — and with it the form $\Box = \partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$ — is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial Q_t^2 + \Delta_Q$. On $\mathbb{M}_-$, where the series does its work, that form is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series.

The operator is one, and every article writes it the same way. **No article of the series defines a second d'Alembertian**, and no mass-term sign is left to a local convention.

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

## The Superscripts

Two superscript tokens run beside the marks of the elements and the marks of the conjugations, and neither is to be read for the other:

| Token | Written on | Meaning |
|---|---|---|
| $^{\mathrm{fop}}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $^{\mathrm{opp}}$ | an algebra name | the opposite algebra, the algebra with the reversed product |

The tilde and the arrow are marks of the **elements**: the tilde the quaternionic factor, the arrow the vector part of a named element and a pure element read on its own. None of them says that a glyph is an operator, and no mark is needed to say it, because on this algebra **an operator is a multiplication by an element**. Every element acts on the algebra, on the left $L_{\tilde Q}$ or on the right $R_{\tilde Q}$, so an operator whose letter is the letter of an element **is** that element and keeps the element's glyph. The Hamiltonian $H$, the number $N$, the momentum $p$, the position $x$, the spin $S$ and the boosts $S_x,S_y,S_z,S_t$ of the chiral article are elements acting by multiplication and are written with **no mark**; so are the structural operators, the left and right multiplications $L_{\tilde Q}$ and $R_{\tilde Q}$, the sandwich $\operatorname{H}_{\tilde Q}$, the derivations, the automorphisms, and the rotation rotor $\tilde u$, an element of $Sp(1)$ and an operator only through its action.

**The mark, and its one use.** The single exception is the **Fock layer**, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the upright superscript $\mathrm{fop}$, set on the glyph and read as part of it:

$$
a^{\mathrm{fop}},\quad b^{\mathrm{fop}},\quad a^{\mathrm{fop}\dagger},\quad b^{\mathrm{fop}\dagger},\quad \psi^{\mathrm{fop}},\quad N^{\mathrm{fop}},\quad H^{\mathrm{fop}},\quad F^{\mathrm{fop}},\quad Ϙ^{\mathrm{fop}},\quad U^{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $p=-i\hbar\nabla$ is written $p$ and never $p^{\mathrm{fop}}$, the quadratures $x$ and $p$ of the oscillator are written $x$ and $p$, the spin $S_k=\tfrac{\hbar}{2}\sigma_k$ is written $S_k$, and the parity, charge-conjugation and time-reversal maps $P$, $C$ and $T$ carry no mark. Where a ladder is meant as an element of the algebra it is written with the element's glyph, the truncated pair $\vec\Upsilon_1,\vec\Upsilon_2$, and the abstract ladder operator keeps the mark, $a^{\mathrm{fop}}$.

**It combines with the dagger, the mark first.** The dagger is the general adjoint (§*The Conjugations and the Adjoint*); the superscript marks the Fock operator. Where both are written on the same glyph, the Fock mark comes first and the adjoint follows, $(a^{\mathrm{fop}})^{\dagger}$, contracted to $a^{\mathrm{fop}\dagger}$. The dagger alone never says that its glyph is an operator, and the superscript alone never says that the Fock operator is self-adjoint; the two are read together, so that $a^{\mathrm{fop}\dagger}$ is the adjoint of the ladder and $N^{\mathrm{fop}}$ is written without an adjoint because it is self-adjoint.

**The opposite algebra carries a different token.** The reversed-product algebra is written with the superscript $\mathrm{opp}$, $\mathbb{B}^{\mathrm{opp}}$, $A^{\mathrm{opp}}$, $M_n(D)^{\mathrm{opp}}$, on an **algebra name**, where the Fock mark is written on a **Fock-operator glyph**. The two tokens are distinct and neither is read for the other: $a^{\mathrm{fop}}$ is never an opposite algebra, and $\mathbb{B}^{\mathrm{opp}}$ is never an operator.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}_{\mathrm{r}}$, because a bare underscore would take the first character alone.

**A subscript is never a partial derivative.** The subscript marks a component or a label, a derivative is written with $\partial$, and the rule is fixed in §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** A coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$; an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the general elements, the units, the roots, the idempotents and the nilpotents alike: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}_{\mathrm{r}}$ and $\tilde U_{\mathrm r}$.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $Q_\pm$ |
| an upright word | $\mathbb{B}_{\mathrm{r}}$, $\tilde U_{\mathrm r}$ |
| a grouped expression | $Q_{n+1}$ |

## Summary

The conventions of the series are one object read in order, from the object itself to the two clauses a field equation inherits.

**The object and its parts.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_k^2 = -e_t$, over complex coefficients. The scalar unit $i$ is central, which is what makes the central phase the algebra's continuous symmetry, and multiplication by it is one map whose restrictions are the global phase and the exchanges and duality rotations of the sectors (§*The Central Map and Its Restrictions*). The conjugations cut the algebra into the remarkable subspaces of §*The Remarkable Subspaces*, each carrying its own real parameters and its slice of the coordinate dictionary, with $q'_t = ct$, $q_t = ct'$, $(q_x,q_y,q_z) = (x,y,z)$ and $(q'_x,q'_y,q'_z) = (x',y',z')$. The elements with no scalar part — the vector subspace — are the **pure elements**, written with the arrow and without the tilde, $\vec{Q}$ (§*Pure Elements and their Coefficients*). The algebra carries four forms, not two — the plain form, the quaternionic form, the Hermitian form and the Krein form — read on the diagonal as the four norms, of which the quaternionic norm is the biquaternion norm. The matrix representation $\mathsf{M}_2$ is fixed by its four basis images, with the Hermitian units following as $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$; the residual freedom is a unitary change of basis of $\mathbb{C}^2$ and nothing further, so the sector dictionary cannot be altered by re-choosing it.

**The presentations, the gradient and the metric levels.** The algebra is written in three presentations — the coefficient quadruple, the $4\times4$ regular matrix and the $2\times2$ image $\mathsf{M}_2$ — each developed in its own article, and it is the trace of $\mathsf{M}_2$ that the series calls the trace. The material coordinate is $\tilde{Q} = ict\,e_t + \vec x$, using the $ict$ convention so that the Minkowski interval is the biquaternion norm, vanishing on the zero-divisor cone. The series d'Alembertian is $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta_Q$, read on the material sector as $\partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$; every article uses this one operator, with the mass equation $\left(\Box - m^2c^2/\hbar^2\right)\psi = 0$. The algebra's real structure is $\flat = -{}^{*}$, and the mass term built on $\flat$ and then retired, with the dispersion that retired it, is recorded in *The Dirac Equation in Biquaternionic Form* and *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*. The three levels of the word *metric* are set out in *The Four Forms, the Four Algebraic Norms and the Change of Scalars*, and the tool is never a reason to change a convention of the framework.

The theme is single. In a framework whose algebra and sector assignment are non-standard, the most likely error is a correction of something that is deliberate. The conventions recorded above are the places where that is most likely to happen.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $ϙ$ | The electric charge, the minuscule of the archaic qoppa; a physical quantity, not an element of the algebra (U+03D9) |
| $Ϙ$ | A total charge, or a charge operator, the majuscule of the archaic qoppa; the chiral charges are $ϙ_L, ϙ_R$ and the charge operator of a chiral module is $Ϙ = ϙ_LP_L + ϙ_RP_R$ (U+03D8; see §*The Elements and their Coefficients*) |
| $\tilde{Q}$ | An element of the algebra. The same symbol serves for the general element and for an element of any of the subspaces, whichever the passage at hand is about; the complex coefficients are $Q_\mu$, the real parameters of a four-dimensional subspace are $q_\mu$ and $q'_\mu$, the prime marking the slot that carries the $i$. |
| $\vec Q$ | The vector part of an element, $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$, and a pure element of the biquaternion layer read on its own, $\mathrm{Sc}(\vec Q) = 0$, the vector subspace $\mathrm{Vect}(\mathbb{B})$ (see §*The Elements and their Coefficients* and §*Pure Elements and their Coefficients*) |
| $\vec q$ | A pure quaternion, an element of the quaternion layer with no scalar part, $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ (see §*Pure Elements and their Coefficients*) |
| $\vec u$ | A unit pure quaternion, the axis of a rotation |
| $\vec U$ | A unit pure biquaternion, of norm one |
| $\vec\Xi$ | A pure root of $1$ of the biquaternion layer |
| $\vec\Upsilon$ | A pure nilpotent of the biquaternion layer |
| $\tilde{P}$ | A four-momentum or four-vector, $\tilde{P} = m\tilde{V}$ (see §*The Elements and their Coefficients*) |
| $\tilde{V}$ | The four-velocity, $\langle\tilde{V}\rangle_{\natural} = -c^{2}$ |
| $\tilde{\Pi}$ | An idempotent, projector or pure state, $\tilde{\Pi}^2 = \tilde{\Pi}$, and the minimal left ideal $\mathbb{B}\tilde{\Pi}$ it generates (see §*The Idempotent Convention*). By the case rule the quaternion layer of the mathematical corpus writes $\tilde{\pi}$ and the tilde-free layers $\Pi$ |
| $\tilde{\nu}$ | A nilpotent of the quaternion or split-quaternion layer, $\tilde{\nu}^2 = 0$ (see §*The Nilpotent Convention*) |
| $\tilde{\Upsilon}$ | A nilpotent of the biquaternion or split-biquaternion layer, the upper-case glyph of the same letter; not a $Y$ |
| $\tilde{\Xi}$ | A root of $1$ of the biquaternion or split-biquaternion layer, $\tilde{\Xi}^2 = 1$ (see §*The Root Convention*) |
| $\tilde{U}$ | A unit element, $\mathrm{Norm}(\tilde{U}) = e_t$ for the norm in view (see §*The Unitary Convention*) |
| $\tilde{u}$ | A unit element of the quaternion or split-quaternion layer, a unit quaternion |
| $\tilde{\xi}$ | A root of $1$ of the quaternion or split-quaternion layer |
| $\tilde{Q}^{\natural}, \bar{\tilde{Q}}, \tilde{Q}^{*}, \tilde{Q}^{\flat}$ | Quaternion (the natural sign), complex, Hermitian and anti-Hermitian conjugation |
| $\tilde{Q}^{\natural} \mapsto \epsilon M^{\mathsf T}\epsilon^{-1}$, $\bar{\tilde{Q}} \mapsto \epsilon\overline{M}\epsilon^{-1}$ | The two conjugations dressed by the antisymmetric form; $\epsilon = \mathsf{M}_2(-\vec e_y)$ |
| $\tilde{Q}^{*} \mapsto M^\dagger$, $\tilde{Q}^\flat \mapsto -M^\dagger$ | The two undressed ones. Entrywise conjugation of $M$ alone is not the image of any involution |
| $\flat = -{}^{*}$ | The anti-Hermitian conjugation, the algebra's real structure |
| $^{\mathrm{fop}}$ | A **Fock operator**, an operator on the Fock space and not an element of the algebra — the ladders $a^{\mathrm{fop}}, b^{\mathrm{fop}}$, the field $\psi^{\mathrm{fop}}$, the number $N^{\mathrm{fop}}$, the Hamiltonian $H^{\mathrm{fop}}$, the phase $U^{\mathrm{fop}}$ (see §*The Superscripts*). No other operator carries the mark. The opposite algebra uses the separate token $A^{\mathrm{opp}}$ |
| $\mathbb{C}_{\mathbb{B}} = \{Q_t e_t\}$ | Centre subspace, fixed points of quaternion conjugation; the centre of $\mathbb{B}$ and the complex time sector; parameters $q_t, q'_t$ with $q_t = ct'$ and $q'_t = ct$ |
| $\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\}$ | The vector subspace, i.e. the complex space sector: anti-fixed points of quaternion conjugation, real dimension six; parameters $q_k, q'_k$ with $(q_k) = (x,y,z)$ and $(q'_k) = (x',y',z')$. The pure elements are these, written $\vec{Q}$ (§*Pure Elements and their Coefficients*). |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, i.e. the real sector (the real half): fixed points of complex conjugation, all four coefficients real |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion subspace, i.e. the imaginary sector (the imaginary half): anti-fixed points of complex conjugation, all four coefficients purely imaginary; not a subalgebra. $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, a split that crosses the $\mathbb{M}_\pm$ split |
| $\mathbb{M}_+ = \{ \tilde{Q} : \tilde{Q}^{*} = \tilde{Q} \}$ | Hermitian subspace, the informational sector; basis $e_t, i\vec e_x, i\vec e_y, i\vec e_z$, parameters $q_t, q'_x, q'_y, q'_z$ (real), with $q_t = ct'$ |
| $\mathbb{M}_- = \{ \tilde{Q} : \tilde{Q}^\flat = \tilde{Q} \}$ | Anti-Hermitian subspace, the material sector; basis $ie_t, \vec e_x, \vec e_y, \vec e_z$, parameters $q'_t, q_x, q_y, q_z$ (real), with $q'_t = ct$ |
| $\tilde{Q} = ict\,e_t + \vec x$ | The material coordinate, $\vec x = x \vec e_x + y \vec e_y + z \vec e_z$ |
| $(ct')\,e_t + i\vec x'$ | The informational coordinate, $\vec x' = x' \vec e_x + y' \vec e_y + z' \vec e_z$; the temporal coefficient $ct'$ is real and the spatial ones imaginary, the mirror of the material coordinate |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2$ | Biquaternion norm, level 1 of the three levels of the word *metric* (§*The Metric: Three Levels* of *The Four Forms, the Four Algebraic Norms and the Change of Scalars*) |
| $\mathrm{Form}(\tilde{Q}_1,\tilde{Q}_2)$, $\mathrm{Norm}(\tilde{Q})=\mathrm{Form}(\tilde{Q},\tilde{Q})$ | The generic form and the generic norm, instantiated one to a general product by the four forms and the four norms (§*The Four Algebraic Norms*, §*The Involutions and the Four Forms*) |
| $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ | The twelve products, the four general products and their symmetric and antisymmetric parts (§*The Twelve Products and Their Names*) |
| $\mathbb{B}_{\mathrm{r}}$, $T = A + Bj$ | The reduced biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ on the basis $1, i, j, ij$, equivalently the tessarines or the double-complex numbers; the same twelve codes are registered on it and four collapse — $\mathrm{SPA} = \mathrm{GPA}$, $\mathrm{SQS} = \mathrm{GQS}$, $\mathrm{APA} = 0$, $\mathrm{AQS} = 0$ — leaving the eight structures GPA, GQA, GPS, GQS, SQA, AQA, SPS, APS (§*The Twelve Products and Their Names*) |
| $J = {}^{\natural}$ | The fundamental symmetry, $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*} = \langle\tilde{Q}_1^{\natural},\tilde{Q}_2\rangle_{*}$, $J^2 = \mathrm{id}$, $\mathbb{C}$-linear |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric, signature $(-,+,+,+)$ (level 2) |
| $g$ | Clifford metric of the $\gamma^\mu$ (level 3); an optional tool, not a framework convention. $\mathrm{diag}(+1,-1,-1,-1)$ throughout — the $\mathbb{M}_+$ form, matching the objects the tool represents |
| $\tilde{\nabla} = \sum_{\mu\in\{t,x,y,z\}} e_\mu\partial/\partial Q_\mu$, $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_k\partial/\partial Q_k$ | Biquaternionic gradient and its quaternion conjugate, the two factors of the d'Alembertian |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta_Q$ | The d'Alembertian, a scalar operator; on the material sector it reads $\partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2$, the series convention |
| $\mathrm{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ | Trace pairing, unrestricted; the case $\tilde{Q}_1\in\mathbb{M}_+$, $\tilde{Q}_2\in\mathbb{M}_+$ is the real one. $\mathrm{Tr}(e_t) = 2$ |
| $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ | The matrix representation, with $\mathsf{M}_2(e_t) = I_2$ and $\mathsf{M}_2(\vec e_k)$ as given above; the Hermitian units follow as $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$. Fixed up to a unitary change of basis, and no further |
| $SL(2,\mathbb{C})$ | Unit-norm biquaternions, the Lorentz group on $\mathbb{M}_-$ |

## Further Reading

- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the original quaternion algebra and its units.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents, minimal left ideals, and the conjugations of a Clifford algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for real structures and real forms on Clifford algebras.
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), companion article, for the relations among the subspaces defined here — their coordinate blocks, intersections, spans, gradings and biquaternion norms.
- *The Four-Vector Element Representation of Biquaternions* (`articles_physics/the-four-vector-element-representation-of-biquaternions.md`), companion article, for the coefficient space and the index that is never raised or lowered.
- *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_physics/the-4x4-matrix-element-representation-of-biquaternions.md`), companion article, for the two regular matrices, the relation between them, and the reduction into the two chiralities.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), companion article, for the isomorphism $\mathsf{M}_2$, the trace and the determinant, and the ideals as columns.