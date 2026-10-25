# __Conventions in the Biquaternion Universe__

## Introduction

A framework built on a non-standard algebra, and on a non-standard choice of which part of it counts as "real", is a framework in which a reader will repeatedly find things that look wrong and are not. Two examples fix the idea. The series takes the **anti**-Hermitian subspace as the material sector, where the more familiar convention would take the Hermitian one. And the series' d'Alembertian carries a sign opposite to the one used in the articles on Weyl spinors. In both cases it is the "correction" that is the error.

This article states the conventions of the series, one to a section, and records the reason each was chosen. It states conventions only: the proofs, the properties and the physical readings of the objects it names belong to the articles cited beside them. It is meant to be read before any other article is edited, and its reader is anyone writing or revising an article of the series, for whom the conventions are load-bearing — a change that looks local, a sign or a factor of $i$, generally propagates into a dozen dependent articles.

The article is ordered as a dictionary of a single object, each section stated after the one it depends on. First the object and its writing: the algebra and its basis, then the element and its coefficients. Then its parts: the four involutions, the remarkable subspaces they cut out, and the coordinate dictionary and the sector names those subspaces carry. Then what is done with the object: the twelve products, the four forms that are their scalar parts and the four norms read on the diagonal, named by the generic Form and the generic Norm, and the restrictions of the central map, which the norms and the forms make precise. Then the three distinguished elements — the root, the idempotent and the nilpotent — whose glyphs the series writes. Then the three presentations of the same object, the four-vector, the 4×4 regular and the 2×2 element representation with its trace. Last the conventions a field equation inherits, the gradient and its d'Alembertian, the physical units, the two superscript tokens, and the rules of the subscripts, closed by the summary and the summary of notation.

The word *metric* is used at three levels in the series — the biquaternion norm, the two real sectors with their $ict'$ metric, and the Clifford tool — and the distinction between them is set out in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, together with the one-way rule that the Clifford tool is a translation of the algebra and never a reason to change it.

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
\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t, \qquad \vec e_x \vec e_y = -\vec e_y \vec e_x = \vec e_z,
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

The split is also a split of **roles**, and the two roles belong to the two **factors** of the tensor product and cannot be exchanged. The central unit $i$ is the scalar imaginary: it is what enters the phase $\exp(iS/\hbar)$, and it multiplies a whole element from inside the centre. The three units $\vec e_x,\vec e_y,\vec e_z$ are the vector directions: they are the relativistic and rotational structure, and they enter through the quaternion factor. A central scalar and a vector direction are different kinds of object — one commutes with everything, the other rotates — so no product of the four general products may read $i$ through the quaternion direction or a unit through the scalar one. The mirror statement, that the two conjugations act on the two factors separately, is the subject of *The Four General Products: Composition, Probability, Causality, Gauge*.

As a complex algebra $\mathbb{B}$ is isomorphic to the full matrix algebra,

$$
\boxed{\;\mathbb{B} \cong M_2(\mathbb{C})\;},
$$

and this identification is used constantly. It is fixed by a single isomorphism, written $\mathsf{M}_2$; its four basis images, and the rule that neither the factor $i$ nor the sign is a free choice, are stated in §*The 2×2 Matrix Representation* below, and the development of the representation — the general element, the remarkable subspaces as matrices, the conjugations, the trace and the determinant — is in the companion article *The Element and Operator Representations*. Its two **minimal left ideals** are the algebra's two chiralities; the spinor module and the mass term a field equation builds on that structure are the subject of *The Dirac Equation in Biquaternionic Form*.

## The Base and Its Units

The base is written with the letter $e$, one unit to a direction. The scalar unit is $e_t = 1$ and the three vector units are $\vec e_x, \vec e_y, \vec e_z$; the arrow is the only mark that separates the scalar unit from the vector units. **The three vector units are the quaternion units, the series' replacement for Hamilton's $i, j, k$.** A general element is written in the base,

$$
\tilde Q = Q_t e_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $e_\mu$ the unit of the direction $\mu$ — the arrowless $e_t$ at $\mu = t$ and the arrowed $\vec e_\mu$ at $\mu = x, y, z$. The three vector units close on the scalar unit and on one another,

$$
e_t = 1, \qquad \vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t , \qquad \vec e_x \vec e_y = -\vec e_y \vec e_x = \vec e_z ,
$$

and cyclically, the space index running over $k = x, y, z$. **The notation is the unit along the axis.** A coefficient carries the name of the direction it multiplies, as in $\vec v = v_x\hat x + v_y\hat y + v_z\hat z$ of the vector calculus: $Q_x$ is the coefficient of $\vec e_x$, the label on the unit names the direction and the label on the coefficient names the same direction, so $q_x = x$ reads without ambiguity. **The base letter is $e$ and the unit-element letter is $u$, and the two are never exchanged.** The base units carry $e$, so $e$ is not available for the exponential, which is written $\exp(\cdot)$; a unit element of a layer carries the glyph of the unit element, $\tilde u$ or $\tilde U$ (§*The Unitary Convention*).

**The replacement of Hamilton's $i, j, k$ by the base rests on three reasons:**

- **The letters $i$ and $j$ are already taken.** Hamilton's $i, j, k$ collides with the complex $i$, kept for the central imaginary, and with the hyperbolic unit $j$, so a vector unit written with either letter would be misread.
- **The base names the directions of spacetime.** The labels $t, x, y, z$ name the four directions of spacetime, so the base states the physics directly, and $e_\mu$ remains an acceptable notation in mathematics, the unit along the axis $\mu$.
- **The base spends no digit.** The labels carry no digit, so every digit stays free to count the generic objects: $Q_1, Q_2$, $\tilde Q_1, \tilde Q_2$ and $\tilde q_1, \tilde q_2$.

## The Elements and their Coefficients

The case and the tilde of the glyph are fixed first, and the element is written after. A generic element is written so that the glyph alone identifies its algebra, two features being read together: the **case** separates a real scalar from a complex one, and a **tilde** marks the quaternionic factor. **The generic element belongs to the Q family and to no other letter**: $\tilde q$ is the quaternion or split-quaternion element, $\tilde Q$ the biquaternion or split-biquaternion one, in every layer of the quaternion family. A letter outside the family is never generic: it names an object, or an element bound at the point of use.

| System | Name | Generic element | Scalar part | Vector part |
|---|---|---|---|---|
| $\mathbb{R}$ | Reals | $q$ | $q$, real | — |
| $\mathbb{C}$ | Complex numbers | $Q = q + iq'$ | $q$, real; $q'$, real | — |
| $\mathbb{B}_{\mathrm{r}}$ | Reduced biquaternions | $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ | $Q_{\blacktriangle}$, complex; $Q_{\blacktriangledown}$, complex | — |
| $\mathbb{H}$ | Quaternions | $\tilde q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $q_t$, real | $q_x\vec e_x$, $q_y\vec e_y$, $q_z\vec e_z$, real |
| $\mathbb{B}$ | Biquaternions | $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $Q_t$, complex | $Q_x\vec e_x$, $Q_y\vec e_y$, $Q_z\vec e_z$, complex |

Under this framework, the **vector part** is the part carried by the three vector units $\vec e_x,\vec e_y,\vec e_z$; it exists only in the four quaternionic layers.

**The two part columns.** The fourth column gives the scalar part — the $\mathbb{C}$ scalar part in $\mathbb{B}$ and $\mathbb{B}_{\mathrm{r}}$ — and the fifth the vector part, each coefficient with its nature. In $\mathbb{C}$ and $\mathbb{B}_{\mathrm{r}}$ there is no vector direction, so both coefficients are scalars of the coefficient field and the vector column is empty.

**The reals come first, written $q$.** The reals have no vector part and carry no tilde and no prime: the generic real element is the lower-case $q$, and it is the glyph every coefficient of the layers is a real parameter of — the $q_\mu$ of the quaternions, and the real part of $Q_\mu = q_\mu + iq'_\mu$ of the biquaternions.

**Several elements of one kind take subscripts.** Where a statement needs more than one element of the same kind, each occurrence takes a number: three generic biquaternions are $\tilde Q_1, \tilde Q_2, \tilde Q_3$, two quaternions are $\tilde q_1, \tilde q_2$, and two complex numbers are $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. The number counts the element and never names a direction; a letter names the direction. **Every element of a numbered statement is numbered**: a bare $\tilde Q$ stands alone, in a statement about one element, and never beside $\tilde Q_1$ or $\tilde Q_2$. The numbers count the elements in the order the statement introduces them, $\tilde Q_1, \tilde Q_2, \tilde Q_3$, and the coefficients follow their element, $Q_{1t}, \vec Q_1$ for $\tilde Q_1$.

**The four coefficient slots are labelled $t, x, y, z$; the material coordinate is $(t', x, y, z)$.** So that a sum over the coefficients of a quaternion or of a biquaternion shows at once which unit each term carries, the coefficients take the labels of the units in place of the numbers: $Q_t$ with $e_t$, and $Q_x, Q_y, Q_z$ with $\vec e_x, \vec e_y, \vec e_z$. A sum over the four therefore runs over those labels,

$$
\tilde Q = \sum_{\mu \in \{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $\mu$ the label and $e_\mu$ the unit it carries — the arrowless $e_t$ at $\mu = t$ and the arrowed $\vec e_\mu$ at $\mu = x, y, z$. The same rule reads a quaternion, $\tilde q = \sum_{\mu} q_\mu e_\mu$, and a four-vector of the algebra, and the primed coefficients follow the same labels, $Q_\mu = q_\mu + iq'_\mu$: the label marks the direction and the prime marks the slot that carries the $i$. The slot label names the unit, not the time coordinate: the material time is $t'$, the imaginary part of $Q_t$, and the informational time is $t$, its real part.

**A complex element carries a majuscule**, $Q$, the case naming the scalar sector: an upper-case glyph has a scalar sector larger than the reals, a lower-case one has the reals. **The second coordinate of a complex element carries a prime**, $Q = q + iq'$; a second and a third are $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. And **the quaternionic elements carry a tilde**: lower case for the quaternions, $\tilde q$, and upper case for the biquaternions, $\tilde Q$; **the reduced biquaternion element carries no tilde but the breve**, $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$, the ascending triangle for the coefficient of $1$ and the descending triangle for the coefficient of $j$, the breve telling it from the complex element $Q$ of the same capital, its algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ being commutative and having no quaternionic factor, its second unit being the hyperbolic $j$, $j^{2} = +1$ and $ji = ij$, so that the basis is $1, i, j, ij$. Finally, **the element is a scalar part plus, where the layer has one, a vector part**: the scalar part is carried by the unit — $1$ in $\mathbb{C}$ and $\mathbb{B}_{\mathrm{r}}$, $e_t$ in $\mathbb{H}$ and $\mathbb{B}$ — and the vector part, in $\mathbb{H}$ and $\mathbb{B}$ alone, by the remaining basis directions, carrying the arrow, $\vec q$ or $\vec Q$, so that $\tilde Q = Q_te_t + \vec Q$ with $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ and $Q_\mu = q_\mu + iq'_\mu$. In $\mathbb{C}$ the second term $iq'$ is the imaginary part of a single coefficient, and in $\mathbb{B}_{\mathrm{r}}$ the second term $jQ_{\blacktriangledown}$ is its $j$-part, neither being a vector part. **A pure element carries the arrow.** A pure element is one with no scalar part, a vector of its layer, and it is written with the arrow of the vector part: $\vec q$ and $\vec Q$ are the pure elements of the quaternion and of the biquaternion layers, standing by themselves (§*Pure Elements and their Coefficients*). The arrow names the vector part of a named element, $\vec{Q}$ in $\tilde{Q} = Q_te_t + \vec{Q}$, and it names the same object when the element is read on its own; the arrow and the tilde are never stacked.

**The generic element is $\tilde{Q}$, and only the Q family is generic.** No letter outside the family, at any case, with any subscript, in any article, stands for an arbitrary element: a letter outside the family names a specific object, or an element bound where it is introduced. A statement that holds for every element is written with $\tilde{Q}$; a statement that needs two writes them $\tilde{Q}_1$ and $\tilde{Q}_2$, and a third takes the next number. The plain form is $\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2)$, with plain norm $\langle\tilde{Q}\rangle=\langle\tilde{Q},\tilde{Q}\rangle$ and unit $\langle e_t\rangle=1$; the trace pairing $2\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2)$ is its $2\times2$ reading, the commutator bracket $[\tilde{Q}_1,\tilde{Q}_2] = \tilde{Q}_1\tilde{Q}_2 - \tilde{Q}_2\tilde{Q}_1$, the general quaternionic bilinear form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ and the multiplicativity $\langle\tilde{Q}_1\tilde{Q}_2\rangle_{\natural} = \langle\tilde{Q}_1\rangle_{\natural}\,\langle\tilde{Q}_2\rangle_{\natural}$. The argument of an operator, the dummy of an annihilator, the second entry of a bracket and the element a field or a map is applied to carry the same glyph: $L_{\tilde Q_1}(\tilde Q_2) = \tilde Q_1 \bullet \tilde Q_2$, $\{\tilde Q_2 : \tilde Q_1 \star \tilde Q_2 = 0\}$, $[\tilde Q_1, \tilde Q_2]$. **The letter $\tilde P$ is never a generic element**; it is the four-momentum, $\tilde P = m\tilde V$. **In the layers of the biquaternion family the glyph $Q$ belongs to the element and never to an operator**: an operator generated by an element carries the structural capital and the element in the subscript, $L_{\tilde Q}$, and an operator that is not the multiplication by an element takes a letter of its own.

**The letters of the physical quantities.** The glyphs are fixed one to a quantity, so that a reader meets the same letter for the same thing in every article; the tables of §*The Most Common Quaternions and Biquaternions* and §*Summary of Notation* list them all.

**What the coefficient prime marks.** The coefficient prime belongs to the **coefficients of complex numbers**, and it marks their imaginary parts. The four coefficients of a general element are complex, and writing each as a real part plus $i$ times a real part,

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

The primed parameter is the one attached to $ie_\mu$, so **the coefficient prime marks the imaginary part, the slot that carries the $i$**. Read as physical coordinates, the four real parts are $(t, x, y, z)$ and the four imaginary parts are $(t', x', y', z')$: $Q_t = c(t+it')$, $Q_x = x+ix'$, $Q_y = y+iy'$, $Q_z = z+iz'$. The material sector takes the imaginary time and the real space, $(t', x, y, z)$; the informational sector takes the real time and the imaginary space, $(t, x', y', z')$. Grouped by the algebra's real-and-imaginary split, the four unprimed parameters are the coordinates of the quaternion subspace and the four primed ones those of the antiquaternion subspace,

$$
q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z \in \mathbb{H}_{\mathbb{B}}, \qquad iq'_te_t + iq'_x\vec e_x + iq'_y\vec e_y + iq'_z\vec e_z \in i\mathbb{H}_{\mathbb{B}} .
$$

**The three-and-one pattern.** The two subspaces of the coefficient split are uniform: $\mathbb{H}_{\mathbb{B}}$ is carried entirely by unprimed parameters, $i\mathbb{H}_{\mathbb{B}}$ entirely by primed ones. Each of the two sectors, by contrast, is mixed, because each takes its scalar slot from one side of that split and its three vector slots from the other. The informational sector is $q_te_t + iq'_k\vec e_k$ — unprimed scalar, primed vectors — and the material sector is $iq'_te_t + q_k\vec e_k$ — primed scalar, unprimed vectors. Read by parameter, the primed set $\{q'_t, q'_x, q'_y, q'_z\}$ is therefore one material slot (the material time $q'_t$) and three informational ones (the informational space $q'_k$), rather than four belonging to a single sector; that mixed ownership is the same statement as the crossing of the two decompositions.

**A logarithm carries the glyph of its element and the subscript $\log$.** The logarithm is a solution of the exponential equation in the same algebra, not an object of a new kind, so it carries the glyph of the element and the subscript, and the definition reads $\exp(\tilde Q_{\log}) = \tilde Q$. The glyph is $\tilde Q_{\log}$ in this algebra, $\tilde q_{\log}$ in the quaternion and split-quaternion layers, $\breve Q_{\log}$ in the reduced biquaternions, and $Q_{\log}$ in the complex, split-complex and dual ones. The subscript is a word, so it competes neither with the direction labels, $Q_t$ and $Q_x$, nor with the counts, $Q_1$; a numbered element keeps its number in front of the subscript, $\tilde Q_{1\log}$. The subscript is dropped when the logarithm is written as an operator, $\log\tilde Q$ or $\operatorname{Log}\tilde Q$. The coordinates of a logarithm follow the coefficient rule: in the complex, split-complex and dual layers, $Q_{\log}=q_{\log}+iq'_{\log}$ has real part $q_{\log}$ and imaginary part $q'_{\log}$, with $j$ in place of $i$ in the split-complex case, and the prime marks the imaginary coordinate alone. The logarithm of a real number is the ordinary real logarithm, written $\log q$; the glyph $q_{\log}$ is the real coordinate of $Q_{\log}$, not the logarithm of $q$.

## Pure Elements and their Coefficients

A **pure element** is an element with no scalar part. The notion belongs to $\mathbb{H}$ and $\mathbb{B}$ alone: $\mathbb{C}$ and $\mathbb{B}_{\mathrm{r}}$ have no vector part, their second term being an imaginary or $j$-part carried by a single coefficient. In $\mathbb{B}$ the scalar part is carried by $e_t$, so a pure element is one whose $e_t$-coefficient vanishes, $\mathrm{Sc}(\tilde{Q}) = Q_t = 0$, and which is carried by the three vector directions alone. The pure elements are exactly the elements of the **vector subspace** $\mathrm{Vect}(\mathbb{B})$, the anti-fixed space of quaternion conjugation,

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

A pure glyph is given from the quaternions to the biquaternions only, the layers this convention reaches; the commutative layers carry their imaginary part in a single coefficient, $Q = q + iq'$.

## The Most Common Quaternions and Biquaternions

The tilde-marked glyphs a reader meets in every article are collected here, with the role, the formula, the space and the meaning of each, before the sections that define the conjugations and the norms. The basis, the central $i$, the charges, the pure elements, the glyphs of the reduced biquaternion layer and the tilde-free relations carry no tilde and are collected in §*Summary of Notation*.

**Scope: tilde glyphs only.** Every catalogued symbol carries a tilde. Four kinds of glyph are outside the scope and are not listed among the allowed uses: a matrix, $I_n$, $\mathsf{M}_2$, $\mathsf{M}_4$; a pure element written with an arrow, $\vec Q$, $\vec q$, $\vec u$, $\vec U$, $\vec\Xi$, $\vec\Upsilon$, $\vec\pi$; a mark that is not an element; and every glyph of the reduced, tilde-free layers, $\Pi_\pm$, $\Xi_\pm$. The first is fixed by the rule that a matrix carries no tilde, §*General Matrix Conventions*; the others are elements of other layers or of no layer at all. The operator section states the rule that pairs the two marks; it is not a catalogue of arrowed glyphs.

The tilde marks a quaternionic factor. A base glyph counts every numbered and subscripted variant.

**Allowed tilde.** The role is fixed by this article, or by the case-and-mark rule it states, and checked against the corpus. Cite these entries as they stand. The tables are ordered by theme, as the objects are; the letters outside the U family are bound where they are introduced.

The governing rule: **only the Q family is generic, and only an element carries the tilde.** $\tilde Q$ is the biquaternion or split-biquaternion element and $\tilde q$ the quaternion or split-quaternion element; numbered variants are allowed. A generic element that is unitary is written $\tilde U$. A letter outside the family names an object, or an element bound where it is introduced. A matrix — the image of an element, an array of biquaternions, or a colour matrix — takes no tilde; a tilde on one is a defect of scope, corrected where it occurs and not catalogued here. A tensor is not an element of the algebra: its components $T^\mu{}_\nu$ and $T^{\mu\nu}$, and the irreducible tensor operators $T^{(k)}_\mu$, carry no tilde, and a free element written $\tilde T$ is the same defect, corrected to the Q family.

### The Layer Glyphs

| Symbol | Name | Formula | Space | Meaning |
|---|---|---|---|---|
| $\tilde Q$ | General element of the algebra | $Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, $Q_\mu\in\mathbb{C}$ | $\mathbb{B}$ | The only generic glyph; a second and a third are $\tilde Q_1,\tilde Q_2$ |
| $\tilde q$ | General element of the quaternion layer | $q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, $q_\mu\in\mathbb{R}$ | $\mathbb{H}_{\mathbb{B}}$ | The only generic glyph of that layer; a second is $\tilde q_1$ |
| $\tilde\Pi$ | Idempotent; a Hermitian idempotent is a pure state | $\Pi_te_t+\vec\Pi$, with $\tilde\Pi^2=\tilde\Pi$ | $\mathbb{B}$; $\mathbb{M}_+$ when $\tilde\Pi^{*}=\tilde\Pi$ | A Hermitian idempotent is a pure state; $\mathbb{B}\tilde\Pi$ is the minimal left ideal, the state module. The retarded pure state of the moving-charge exercise is $\tilde\Pi(\vec u_R)=\tfrac12(e_t+i\vec u_R)$ |
| $\tilde\pi$ | Idempotent of the quaternion and split-quaternion layers; canonical momentum | $\tilde\pi_{1,2}=\tfrac12(1\pm\vec e_y)$; $\tilde\pi=\pi^0e_t+\vec\pi$ | The quaternion and split-quaternion layers; $\mathbb{B}$ for the canonical momentum | The idempotent pair of the two layers; the canonical momentum of the canonical-quantization, Landau-level and quantum-gravity articles, with the scalar part constrained or central. It is never the Goldstone field, which is the pure element $\vec\pi$ |
| $\tilde\Xi$ | Root of a central value | $\Xi_te_t+\vec\Xi$, with $\tilde\Xi^2=\lambda e_t$, $\lambda$ central | $\mathbb{B}$; $\mathbb{M}_+$ for the roots $i\vec e_k$; $\mathbb{C}_{\mathbb{B}}$ for $\pm i$ | For a root of $1$ the idempotents are $\tfrac12(e_t\pm\tilde\Xi)$ |
| $\tilde\xi$ | Root of $1$ of the quaternion layer | $\xi_te_t+\vec\xi$, with $\tilde\xi^2=e_t$ | $\mathbb{H}_{\mathbb{B}}$; the split-quaternion layer writes the same glyph | The tilde-free layers write $\Xi$ |
| $\tilde\nu$ | Nilpotent of the quaternion layer | $\nu_te_t+\vec\nu$, with $\tilde\nu^2=0$ | The null cone, in neither sector | The biquaternion layer writes $\tilde\Upsilon$ |
| $\tilde\Upsilon$ | Nilpotent of the biquaternion layer | $\Upsilon_te_t+\vec\Upsilon$, with $\tilde\Upsilon^2=0$ | The null cone, in neither sector | The quaternion layer writes $\tilde\nu$ |
| $\tilde U$ | Norm-one element | $U_te_t+\vec U$, with $\mathrm{Norm}(\tilde U)=e_t$; $\tilde U^{*}\tilde U=e_t$ in the unitary case | $\mathbb{B}$ | A unit element; a rotor when unitary. The unitary group is $\mathrm{U}(\mathbb{B})\cong\mathrm{U}(2)$. The conjugating element of an inner automorphism, normalised by the central square root of its norm, is this glyph |
| $\tilde u$ | Unit quaternion | $\cos(\theta/2)e_t+\sin(\theta/2)\vec u$, $\vec u$ a unit real vector | $\mathbb{H}_{\mathbb{B}}$, norm one | The rotor of $\mathrm{Sp}(1)\cong\mathrm{SU}(2)$; a pure unit quaternion is $\vec u$ |
| $\tilde U_{\mathrm b}$ | Hermitian positive boost, the frame rotor | $\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | $\mathbb{M}_+$, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$ | The Lorentz boost of rapidity $\psi$ and the boost factor of the polar word; the congruence by it is the boost, and a four-vector element carries its inverse square $\mathcal B=\tilde U_{\mathrm b}^{-2}$, §*The Polar Word and the Three Pairings*. It is not unitary under ${}^{*}$, $\tilde U_{\mathrm b}^{*}\tilde U_{\mathrm b}\neq e_t$. The label is $\mathrm b$; the longer spelling $\mathrm{boost}$ is not used. Its generator is the pure element $\tfrac12 i\vec u_{\mathrm b}$ |
| $\mathcal B$ | Four-vector boost factor | $\tilde U_{\mathrm b}^{-2}=\cosh\psi\,e_t-i\sinh\psi\,\vec u_{\mathrm b}$ | $\mathbb{M}_+$, $\det=1$ | The factor a four-vector element carries; equal to $e^{\vec U\Theta}$ with $\Theta=-i\psi$. It is not the acting rotor: the word's factor is $\tilde U_{\mathrm b}$ for a transformation and $\mathcal B$ for a four-vector |
| $\tilde u_{\mathrm r}$ | Unit real quaternion rotor | $\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | $\mathbb{H}_{\mathbb{B}}$, norm one | The rotor of the polar word and of every rotation here, the rotating frame included; half-angle $\theta/2$, axis $\vec u_{\mathrm r}$; unitary under every product |
| $\tilde U_{\mathrm L}$ | Unit-norm biquaternion, the product of the two factors above | $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}$, with $\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t$ | $\mathbb{B}$, norm one; $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$ | The product of the boost and the rotor, in that order; it is a Lorentz transformation. The series fixes this order, the factors do not commute, and the decomposition is unique when the boost is positive definite. The opposite polar order is recorded in the note below the table |
| $\tilde u_H$ | Evolution rotor | $\exp(-i\tilde H_Rt'/\hbar)=\exp(-\frac{\Omega t'}{2}\vec u_R)$ | $\mathbb{H}_{\mathbb{B}}$, norm one | The same rotor for the evolution inside that frame: axis $\vec u_R$, angle $\Omega t'$ |
| $\tilde U_{\mathrm{int}}$ | Bound unit element: the Thomas interval rotor | $\tilde U_{\mathrm{int}}=\tilde U_{\vec v+d\vec v}\tilde U_{\vec v}^{-1}$ | $\mathbb{B}$, norm one | The unit-norm biquaternion that carries the rest frame at $t'$ to the rest frame at $t'+dt'$. It takes the glyph of the U family because it is of norm one; the role label $\mathrm{int}$ fixes it |

**The two polar orders.** The table fixes the word with the Hermitian positive boost on the left, $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$. The opposite word is equally valid and is used where the right polar decomposition is the natural one:
$$
\tilde U_{\mathrm L}=\tilde u_{\mathrm r}B_{\mathrm{right}},
\qquad
B_{\mathrm{right}}=\sqrt{\tilde U_{\mathrm L}^{*}\tilde U_{\mathrm L}}=\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\neq\tilde U_{\mathrm b}.
$$
The two words are the left and the right polar decompositions of the same rotor. They share the rotation factor $\tilde u_{\mathrm r}$ and the Wigner angle; they differ in the boost, which has the same rapidity magnitude and the axis $\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$. Only the rotation factor and the Wigner angle are independent of the word, so a statement about "the boost factor" must name the word. The symbols $\tilde U_{\mathrm b}$ and $B_{\mathrm{right}}$ are not interchangeable when the rotation axis is not parallel to the boost axis.

### The Gradient and the Operators

| Symbol | Name | Formula | Space | Meaning |
|---|---|---|---|---|
| $\tilde\nabla$ | Biquaternionic gradient | $e_t\,\partial/\partial Q_t+\vec e_x\,\partial/\partial Q_x+\vec e_y\,\partial/\partial Q_y+\vec e_z\,\partial/\partial Q_z$ | Operator, $\mathbb{B}$-valued | Its conjugate $\tilde\nabla^{\natural}=e_t\,\partial/\partial Q_t-\vec e_k\,\partial/\partial Q_k$ is the second factor of $\Box$ |
| $\tilde D$ | Gauge-covariant derivative | $\tilde D=\tilde\nabla+i\kappa\mathcal A$ | Operator, $\mathbb{B}$-valued | The gauge-principle, minimal-coupling, Yang–Mills, instanton and Stueckelberg articles. Its $e_t$ coefficient is $\partial/\partial Q_t+i\kappa\mathcal A_t$, so the operator is read with its scalar part; on the curvature it acts as $\tilde D\tilde F=\tilde\nabla\tilde F+i\kappa[\mathcal A,\tilde F]$, the Yang–Mills current. The component $D_\mu=\partial/\partial Q_\mu+i\kappa\mathcal A_\mu$ carries no tilde |
| $\tilde K_{\mathrm{ret}}$ | Retarded-time gradient coefficient | $\tilde K_{\mathrm{ret}}=\tilde\nabla^{\natural}t'_r=\frac{1}{c\kappa}(-ie_t+\vec u_R)$, $\kappa=1-\vec u_R\cdot\vec\beta$ | $\mathbb{M}_-$, null | The gradient of the retarded time, also called the null retarded gradient: an element, not an operator, and $\tilde\nabla^{\natural}\tilde Q=\tilde K_{\mathrm{ret}}\,d\tilde Q/dt'_r$ for a source depending on $t'_r$ alone. It is a zero divisor, $\langle\tilde K_{\mathrm{ret}}\rangle_{\natural}=0$, so it is null and not unitary at any $\kappa$. The $\kappa$ here is the retarded denominator, not the coupling of $\tilde D$ |

### The Four-Vectors and the Currents

| Symbol | Name | Formula | Space | Meaning |
|---|---|---|---|---|
| $\tilde P$ | Four-momentum | $i(E/c)e_t+\vec p$ | $\mathbb{M}_-$ | $\tilde P=m\tilde V$; the letter is never generic |
| $\tilde p$ | Canonical momentum quaternion | $\tilde p=p_te_t+\vec p$, $\tilde p=\partial L/\partial(d\tilde q/dt')$ | $\mathbb{H}_{\mathbb{B}}$ | Real quaternion with four components, scalar $p_t$ and vector $\vec p$; the Legendre conjugate of $\tilde q$. The maths articles bind it at the definition of a multiplication, $L_{\tilde p}(\tilde q_3)=\tilde p^{\natural}\tilde q_3$ for $\tilde p\in\mathbb{H}$; the letter is never generic |
| $\tilde V$ | Four-velocity | $\gamma(ic\,e_t+\vec v)$ | $\mathbb{M}_-$ | $\langle\tilde V\rangle_{\natural}=-c^2$ |
| $\tilde K_{\mathrm f}$ | Four-force | $\tilde K_{\mathrm f}=d\tilde P/d\tau=-ϙ\sqrt{\mu}\,P_{\mathbb{M}_-}(\tilde V\tilde F)$ | $\mathbb{M}_-$ | The proper-time derivative of the four-momentum; the Lorentz-force article projects it onto the material sector, $P_{\mathbb{M}_-}(\tilde Q)=\tfrac12(\tilde Q-\tilde Q^{*})$. The label $a$ numbers a particle, as in $\tilde K_{\mathrm f,a}$ |
| $\tilde R$ | Material four-position | $\tilde R=ict'\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$ | $\mathbb{M}_-$ | The position of a world line; the translation displacement of the causality article is $\tilde R_{\mathrm d}$ and of the Poincaré and conformal articles is $\tilde R_0$. Its vector part is pure, $\vec r=x\vec e_x+y\vec e_y+z\vec e_z$, and carries the arrow without the tilde; the rotor equation $d\vec r/dt'=\vec\omega_T\times\vec r$ is written on it. The corpus still writes the four-position $\tilde Q$; the second point of a convolution is $\tilde R_2$ |
| $\tilde{\mathcal L}$ | Future null four-vector of a pure state | $\tilde{\mathcal L}=i\tilde\Pi(u)\in\mathbb{M}_-$ | $\mathbb{M}_-$ | $\langle\tilde{\mathcal L}\rangle_{\natural}=0$; the scalar part $i/2$ is complex, so the majuscule, §*The Elements and their Coefficients*. The retarded instance of the moving-charge exercise is $\tilde{\mathcal L}_{\mathrm{ret}}=\tilde{\mathcal L}(\vec u_R)$, whose null factor is $-2\tilde{\mathcal L}_{\mathrm{ret}}=-ie_t+\vec u_R$ |
| $\tilde J$ | Four-current; the Maxwell source; also the Noether current of a continuous symmetry; the programme's combined electro–gravimagnetic source | $J^\nu e_\nu=ic\rho\,e_t+\vec J$, $\langle\tilde\nabla,\tilde J\rangle_{\natural}=0$ | $\mathbb{M}_-$ for the Maxwell current; the programme's normalisation adds an $\mathbb{M}_+$ magnetic source and is in neither sector when that source is nonzero | $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J)=0$; enters Maxwell as $\sqrt{\mu}\,\tilde J$, so $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$; the spatial part $\vec J$ is the current density. The axial current is $\tilde J_5$. The electro-gravimagnetic programme writes the same glyph in its own normalisation, $\tilde J=i\rho+\vec J$ with $\rho=\rho_E/\sqrt{\epsilon}-i\rho_H/\sqrt{\mu}$ and $\vec J=\sqrt{\mu}\,\vec j_E-i\sqrt{\epsilon}\,\vec j_H$; in terms of the Maxwell current $\tilde J=ic\rho_Ee_t+\vec j_E$, the programme's current is $\sqrt{\mu}\,\tilde J+\frac{\rho_H}{\sqrt{\mu}}e_t-i\sqrt{\epsilon}\,\vec j_H$, and the added piece is the magnetic source, an element of $\mathbb{M}_+$. The lowercase form of the letter is not used |
| $\tilde A$ | Electromagnetic four-potential, abelian gauge connection | $\tilde A=i\phi/c\,e_t+\vec A\in\mathbb{M}_-$ | $\mathbb{M}_-$ | The potential of the minimal-coupling, hydrogen, Klein–Gordon, Hopf, quadrupole and self-dual articles; the tension biquaternion of the electro-gravimagnetic programme. In *The Stueckelberg Mechanism* the gauge-invariant combination $\tilde A_{\mathrm u}=\tilde A-\tilde\nabla\chi$ is the connection in the unitary gauge, with $\tilde A_{\mathrm u}$ carrying this glyph |
| $\tilde W$ | Energy–momentum four-vector of the electromagnetic field | $\tilde W=\tfrac12\tilde F\tilde F^{*}=W e_t+\tfrac{i}{c}\vec S_{\mathrm P}$, with $W=\tfrac12(\epsilon\vec E^2+\mu\vec H^2)$ and $\vec S_{\mathrm P}=\vec E\times\vec H$ | $\mathbb{M}_+$ | The energy–momentum density: the time row of the stress–energy tensor, $T^0{}_0=-W$ and $T^0{}_k=S_{\mathrm{P}k}/c$. It is a four-vector, and one of the two entries of this table in $\mathbb{M}_+$: the Hermitian form carries the central $i$, and $-i\tilde W=-iW e_t+\vec S_{\mathrm P}/c$ is the $\mathbb{M}_-$ four-vector. It carries the energy density and the flux, not the stress |
| $\tilde\Sigma$ | Energy–momentum biquaternion | $\tilde\Sigma=\tfrac12\tilde F\tilde F^{*}=W\,e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ for the electromagnetic field, the same object as $\tilde W$; $\tilde\Sigma=\tfrac12\tilde J_{\mathrm{eg}}\circ\tilde J_{\mathrm{eg}}^{*}$ for the programme's charge–current field, with $\tilde\Sigma_\Lambda=\Lambda\Lambda^{*}$ and $\tilde\Sigma_{\mathrm O}=\tfrac12\mathrm{O}\,\mathrm{O}^{*}$ for light and the photon cloud | $\mathbb{M}_+$ | The energy–momentum element of the electro-gravimagnetic programme: the scalar part is the energy density and the vector part the flux. The capital is required by the case rule: the vector part is $i\vec S_{\mathrm P}/c$, imaginary, so the element is a biquaternion and not a real quaternion; the letter is also the source's, bound in the four programme articles. In the electromagnetic case it is the same object as $\tilde W$, the corpus's glyph for it |
| $\tilde Q_{\mathrm d}$ | Gauge parameter of the linearized diffeomorphism | $\delta\tilde E_\mu\mapsto\delta\tilde E_\mu-\partial\tilde Q_{\mathrm d}/\partial Q_\mu$; $\xi_\nu=\langle\tilde Q_{\mathrm d},\varepsilon_\nu\rangle_{\natural}$ | $\mathbb{M}_-$ | The image of the diffeomorphism vector, one element of $\mathbb{M}_-$ whose four components remove four of the ten, $16=10+6\to6$. A parameter, not a connection, and written $\tilde Q_{\mathrm d}$, not $\tilde\Delta$; the central scalar $\Gamma$ of $\tilde A\mapsto\tilde A-\tilde\nabla\Gamma$ is the abelian case |

### The Fields

| Symbol | Name | Formula | Space | Meaning |
|---|---|---|---|---|
| $\tilde F$ | Field strength | $i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, scalar part zero | $\mathrm{Vect}(\mathbb{B})$ | The one fixed field: it enters $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$ and is never a generic field. A generic element-valued field is the Q family, written $\tilde Q_{\mathrm f}$ in the derivation articles, the $\mathrm f$ naming the field and not counting the element. One bound use remains outside the field strength: *Fueter Theory for Quaternions* writes the Fueter–Sce construction $\tilde F=\Delta^{(n-1)/2}f^{\mathrm{ax}}_0$, a function bound at its definition. The dual in the tensor articles is $F^{\mathrm{dual}}$, tilde-free |
| $\tilde{\mathcal F}$ | Power–force biquaternion | $\tilde{\mathcal F}=i\tilde J\circ\tilde F_2$, with $\tilde J=i\rho+\vec J$ in the programme's normalisation | $\mathbb{B}$; neither sector in general | The scalar part is a power density and the vector part a force density, per unit volume: the density counterpart of the per-particle four-force $\tilde K$, and not $\tilde K$ itself. The scalar part is complex, which is why the glyph is a majuscule. The field strength of the other field of the mutual pair is $\tilde F_2$, the second of the pair, the first being $\tilde F_1=\tilde F$; the same numeral marks the field in the transformed frame, $\tilde F_2=\tilde U^{\natural}\tilde F\tilde U$, when an article contrasts the two frames. The numeral is a field label, not a derivative and not the dual $-i\tilde F$. The three gauge articles write the same glyph for the field strength or the non-abelian curvature, a second role |
| $\tilde\Psi$ | Dirac field | $\tilde\Psi_L+\tilde\Psi_R$ | $\mathbb{B}$ | An algebra-valued spinor field, with $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$ |
| $\tilde\Phi$ | Algebra-valued scalar field | $\tilde\Phi=\varphi e_t$ in the central case; a general element of $\mathbb{B}$ otherwise | $\mathbb{B}$; $\mathbb{C}_{\mathbb{B}}$ when central | A field whose value at each point is an element of the algebra keeps the element tilde, §*Summary of Notation* below. Central in the Higgs, axion and effective-potential articles, where $\varphi$ is complex and hence the majuscule; general in the Klein–Gordon and functional-integral articles; an $\mathbb{M}_-$-valued field in the integer-spin article; the photon biquaternion of the electro-gravimagnetic programme. The fluctuation about the central field is $\delta\tilde\Phi$; the classical field of the functional articles is $\tilde\Phi_{\mathrm{cl}}=\delta W/\delta\tilde J$, with sector parts $\tilde\Phi_{\mathrm{cl},\pm}$, and the sector parts of the field are $\tilde\Phi_\pm=\tfrac12(\tilde\Phi\pm\tilde\Phi^{\flat})$ |
| $\tilde G$ | Source of the biwave equation | $\tilde\nabla\tilde\Phi=\tilde G$ | $\mathbb{B}$ | A general element of $\mathbb{B}$ read with its scalar part, so it keeps the tilde of a general element; not the same object as $\tilde{G}_{\tilde\nabla}$ |
| $\tilde{G}_{\tilde{\nabla}}$ | Biquaternionic Green's function of the first-order operator | $\tilde{G}_{\tilde{\nabla}}=\tilde\nabla^{\natural}G_\Box$ | $\mathbb{M}_-$ | The kernel that inverts $\tilde\nabla$, with $\tilde\nabla\tilde{G}_{\tilde\nabla}=-\delta^{(4)}$; its scalar part is imaginary and its vector part real. The subscript names the operator inverted, as $G_\Box$ names $\Box$; the numeral $\tilde G_1$ is not used, since there is no second kernel and $G_1$ is the boost generator of *The Unruh Effect in Biquaternionic Form*. The scalar kernel $G_\Box$ and the scalar amplitudes $G(\omega,\vec p)$, $G_F(\omega,\vec p)$ take no tilde |
| $\tilde Q_{\mathrm{amp}}$ | Constant amplitude of the central-phase plane wave | $\tilde\Phi_{\tilde P}(\tilde R)=\tilde Q_{\mathrm{amp}}\exp\!\big(i\operatorname{Sc}(\tilde P^{\natural}\tilde R)\big)$ | $\mathbb{B}$ | The external-leg amplitude of *The LSZ Reduction Formula in Biquaternionic Form*, bound where it is introduced; a general element with a complex scalar part, hence the majuscule. It replaced the earlier $\tilde w$ |

### The Observables, the States and the Quantum Objects

| Symbol | Name | Formula | Space | Meaning |
|---|---|---|---|---|
| $\tilde{Ϛ}$ | State (density) element | $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$, $\lvert\vec r\rvert\le1$ | $\mathbb{M}_+$ | The state of the Bloch ball: Hermitian, positive, $2\,\mathrm{Sc}(\tilde{Ϛ})=1$, read in the $2\times2$ image as $\mathrm{Tr}(\tilde{Ϛ})=1$. The glyph is the upper-case stigma, U+03DA, because the majuscule of rho is the four-momentum $\tilde P$; the rho and varrho spellings are not used. Its matrix image $\mathsf{M}_2(\tilde{Ϛ})$ carries no tilde |
| $\tilde H$ | General Hermitian observable | $h_te_t+ih_k\vec e_k$, $h_t,h_k\in\mathbb{R}$ | $\mathbb{M}_+$ | The Born pairing is $2\langle\tilde{Ϛ},\tilde H\rangle_{*}=2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})=2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H)$, read at normalisation in the $2\times2$ image as $\operatorname{Tr}(\tilde{Ϛ}\tilde H)$; the tilde belongs to this object only |
| $\tilde S$ | Spin operators | $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ | $\mathbb{M}_+$ | The vector slots of $\mathbb{M}_+$, with the total spin $\tilde S$ of a composite |
| $\tilde E$ | Effect of a measurement | $0\le\tilde E\le e_t$, $\tilde E\in\mathbb{M}_+$; $\tilde E_y=\tilde K_y^{*}\tilde K_y$ | $\mathbb{M}_+$ | The outcome of a POVM; a rank-one effect is the idempotent $\tilde\Pi$ |
| $\tilde K_y,\tilde K_l,\tilde K_i,\tilde K_\epsilon,\tilde K_{1,2},\tilde K_0,\tilde K_1,\tilde K_2,\tilde K_k$ | Kraus operator | $\tilde E_y=\tilde K_y^{*}\tilde K_y$; $\Phi(\tilde{Ϛ})=\sum_l\tilde K_l\tilde{Ϛ}\tilde K_l^{*}$ | $\mathbb{B}$ | The Kraus operators of a channel or an instrument: each is an element of $\mathbb{B}$, multiplied on both sides of the state, not an array; its matrix image $\mathsf{M}_2(\tilde K_y)$ carries no tilde. The resolution is $\sum_y\tilde K_y^{*}\tilde K_y=e_t$, and the three rank-one articles write the single operator bare, $\tilde K=\tilde U$. The outcome label is an index, $y$, $l$, $i$, $\epsilon$ or a numbered pair; the count includes the two articles that label the outcomes $\epsilon$ and $(1,2)$ |
| $\tilde K_{\mathrm{mod}}$ | Modular Hamiltonian | $\tilde K_{\mathrm{mod}}=-\log\tilde{Ϛ}$; $\Delta=\exp(-\tilde K_{\mathrm{mod}})$ | $\mathbb{M}_+$ | The modular Hamiltonian of Tomita–Takesaki, with the modular flow $\sigma_{t'}(\tilde Q)=\Delta^{it'}\tilde Q\Delta^{-it'}$. In the finite-dimensional model it is $-\log\tilde{Ϛ}\in\mathbb{M}_+$; the labels $W$, $V$, $\omega$, $L$, $R$ and $\varphi$ name the region, state or side |

**The state takes the stigma, because the majuscule of rho is taken.** The case rule asks a complex element for an upper-case glyph, and the upper-case rho is drawn as $P$ and names the four-momentum $\tilde P$, which the series never writes otherwise. The state therefore takes a capital that names nothing else in the corpus, the **stigma** $Ϛ$ (U+03DA). The glyph is bound to the state and is never generic; the earlier lowercase rho spelling, and the varrho variant with it, are retired, and the corpus uses neither. Bare $\rho$ is not the state: it keeps its other roles, the charge density and the radial coordinate among them. The matrix image takes no tilde, as for every element.

## The Conjugations

The biquaternion algebra carries three natural involutions and the anti-Hermitian sign derived from them, all of them used in the series:

| Map | Mark | What it is |
|---|---|---|
| Complex conjugation | $\bar{\cdot}$ | The involution of the base, extended to the element |
| Quaternion conjugation | ${}^{\natural}$ | The intrinsic conjugate: it fixes the scalars and negates the vectors |
| Hermitian conjugation | ${}^{*}$ | The involution of the algebra, $\bar{\cdot}\circ{}^{\natural}$ |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | The negative of the star |

Which of the marks has a sense depends on the system, since a mark degenerates wherever the structure it conjugates is absent. The examples below fix it system by system.

**The complex numbers $\mathbb{C}$.** Only the bar has a sense, the algebra carrying a single non-trivial involution:

$$
\bar Q = q - iq' .
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

**The fourth mark is a sign, not a fourth conjugation.** $\flat=-{}^{*}$ is the negative of the star, it reverses products with a twist, $(\tilde Q_1\tilde Q_2)^{\flat}=-\tilde Q_2^{\flat}\tilde Q_1^{\flat}$, and it is an involution of the underlying real space only, not of the ring. Its fixed space is the material sector $\mathbb{M}_-$, and the sector split is its work in the series. It is retained for that split, for the bilinear pairings built on it, and for the real-form question of Dirac against Majorana fermions. It is not the mass — the retired form $\tilde\nabla\tilde\Psi=m\tilde\Psi^\flat$ conflated the two — and it is not the charge conjugation of the module, which is the conjugate-linear pseudoautomorphism $\Pi A^{*}\Pi^{-1}$ owned by *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*.

**The biquaternion norm.** The natural sign carries the algebra's **biquaternion norm**,

$$
\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 ,
$$

used throughout the series and read on the four forms and their norms in §*The Involutions and the Four Forms* and §*The Four Algebraic Norms and the Unitary Convention* below. It is **multiplicative** and complex-valued in general, and it is not an analytic norm; its unit group and its invertibility reading are *N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Group of Units*.

Each of the four marks has a fixed space, and each of these is one of the **remarkable subspaces** of the algebra. Which involution defines which subspace, and which of them are anti-fixed, is recorded with the subspaces themselves, in *The Remarkable Subspaces* below.

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

The last row is the one the mark $\flat$ exists for. $\mathbb{M}_-$ is fixed by $\flat=-{}^{*}$ and not by ${}^{*}$, and the minus sign is what selects the anti-Hermitian half; it cuts out this subspace alone, and it is a sign derived from the star rather than an independent involution. The choice of that half as "real" is flagged in §*The Coordinate Dictionary and the Sector Names*.

The basis of each, the coefficients it takes and the physical coordinates those carry are the table of §*The Coordinate Dictionary and the Sector Names*.

**Compact and non-compact directions.** A direction is **compact** when the one-parameter group it generates is a circle and **non-compact** when it is a hyperbola. The three real vector units $\vec e_x,\vec e_y,\vec e_z$ generate the compact directions, the three imaginary units $i\vec e_x,i\vec e_y,i\vec e_z$ the non-compact ones, and the complex vector subspace carries both. The Lie algebra this gives is *The Physical Interpretation of the 12 Products*.

The subspaces are treated one by one in the owner articles: $\mathbb{C}_{\mathbb{B}}$ in *The Biquaternion Space, the Group of Involutions and the Six Subspaces*, §*The Complex Time Sector $\mathbb{C}_{\mathbb{B}}$*; $\mathrm{Vect}(\mathbb{B})$ in §*The Complex Space Sector $\mathrm{Vect}(\mathbb{B})$*; $\mathbb{H}_{\mathbb{B}}$ in §*The Real Sector $\mathbb{H}_{\mathbb{B}}$*; $i\mathbb{H}_{\mathbb{B}}$ in §*The Imaginary Sector $i\mathbb{H}_{\mathbb{B}}$*; and the two sectors in *The Informational Sector: States, Observables and Probability* and *The Material Sector: Four-Vectors, Interval and Lorentz Action*.

## The Coordinate Dictionary and the Sector Names

The dictionary between the parameters and the physical coordinates is fixed once and for all,

$$
q'_t = c\,t', \qquad (q_x, q_y, q_z) = (x, y, z), \qquad q_t = c\,t, \qquad (q'_x, q'_y, q'_z) = (x', y', z'),
$$

with $\vec q = x \vec e_x + y \vec e_y + z \vec e_z$ the real spatial vector and $i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z) = i x' \vec e_x + i y' \vec e_y + i z' \vec e_z$ its imaginary counterpart. The **material coordinate** $\tilde{R} = ict'\,e_t + \vec q$ and the **informational coordinate** $\tilde{Q} = ct\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ are the two ends of it, and each subspace keeps whichever part of the dictionary its defining condition leaves free.

| Subspace | Algebraic name | Physical name | Basis | Real parameters | Physical coordinates |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | The centre | Complex time sector | $e_t,\ ie_t$ | $q_t,\ q'_t$ | $ct,\ ict'$ |
| $\mathrm{Vect}(\mathbb{B})$ | Vector | Complex space sector | $\vec e_x,\ \vec e_y,\ \vec e_z,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q_x,\ q_y,\ q_z,\ q'_x,\ q'_y,\ q'_z$ | $x,\ y,\ z,\ ix',\ iy',\ iz'$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion | Real sector | $e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $q_t,\ q_x,\ q_y,\ q_z$ | $ct,\ x,\ y,\ z$ |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion | Imaginary sector | $ie_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q'_t,\ q'_x,\ q'_y,\ q'_z$ | $ict',\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_+$ | Hermitian | Informational sector | $e_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q_t,\ q'_x,\ q'_y,\ q'_z$ | $ct,\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_-$ | Anti-Hermitian | Material sector | $ie_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $q'_t,\ q_x,\ q_y,\ q_z$ | $ict',\ x,\ y,\ z$ |

Each subspace carries an **algebraic name**, taken from the involution that defines it, and a **physical name**, taken from the role it plays; the companion articles are titled by the physical name.

**The informational coordinate under operator names.** Quantum physics writes the informational coordinate in the letters of an operator rather than of a coordinate: its four real parameters are named $h_t, h_x, h_y, h_z$ in place of $q_t, q'_x, q'_y, q'_z$ — the direction labels, as for the coordinates $Q_\mu$ — and the element is

$$
\tilde{H} = h_te_t + ih_x\vec e_x + ih_y\vec e_y + ih_z\vec e_z, \qquad h_t, h_x, h_y, h_z \in \mathbb{R},
$$

or, with the vector part assembled,

$$
\tilde{H} = h_te_t + i\vec h , \qquad \vec h = h_x\vec e_x + h_y\vec e_y + h_z\vec e_z ,
$$

with $h_t = ct$ and $h_k = x'_k$. This is the informational coordinate $ct\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ of the table under the coefficient names of an operator, and its matrix image, under the unit images of §*The 2×2 Matrix Representation* ($\mathsf{M}_2(e_t) = I_2$ and the vector units $-i$ times the Pauli matrices $\sigma_1, \sigma_2, \sigma_3$), is the general Hermitian $2\times2$ matrix $h_tI_2 + h_x\sigma_1 + h_y\sigma_2 + h_z\sigma_3$ of *The Native Qubit and the Defining Module of the Biquaternion Algebra*. The tilde is required, because $H$ without it is the Hamiltonian, and $h$ without a subscript is the Planck constant.

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

**The code is read letter by letter.** The first letter says which of the three operations of a row — $\mathrm G$ the general product, $\mathrm S$ its symmetric part, $\mathrm A$ its antisymmetric part; the second says which of the two products — $\mathrm P$ the plain one, whose first slot is read as it stands, and $\mathrm Q$ the quaternionic one, whose first slot carries ${}^{\natural}$; and the third says the family — $\mathrm A$ the **algebra** over $\mathbb{C}$, whose three products are $\mathbb{C}$-bilinear, and $\mathrm S$ the **sesqualgebra** over $(\mathbb{C},\bar{\cdot})$, whose three products are sesquilinear. The four general products are the multiplications of the four general structures of the band; the eight parts are the symmetric and antisymmetric products beside them; and the twelve codes together name the twelve algebraic structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The definitions.** Write the two elements $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ and $\tilde Q_2=Q_{2t}e_t+\vec Q_2$, with $\vec Q_1=(Q_{1x},Q_{1y},Q_{1z})$ and $\vec Q_2=(Q_{2x},Q_{2y},Q_{2z})$; $(\vec Q_1,\vec Q_2)$ is the Euclidean inner product, $\vec Q_1\times\vec Q_2$ the cross product in the units $\vec e_x,\vec e_y,\vec e_z$, and $\overline{\vec Q_2}$ the coefficientwise conjugation. Every product is the sum of a scalar part, a multiple of $e_t$, and a vector part.

**The four general products**, one to each choice of the two slots.

**The general plain bilinear product**, the multiplication of the algebra, associative, with $e_t$ a unit on both sides:

$$
\tilde Q_1\tilde Q_2=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2 .
$$

**The general plain sesquilinear product**, the second factor read through ${}^{*}$, not associative, with $e_t$ a unit on the right only:

$$
\tilde Q_1\tilde Q_2^{*}=\bigl[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2} .
$$

**The general quaternionic bilinear product**, the first factor read through ${}^{\natural}$, not associative, with $e_t$ a unit on the left only:

$$
\tilde Q_1^{\natural}\tilde Q_2=\bigl[Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 .
$$

**The general quaternionic sesquilinear product**, both slots read through a conjugation, not associative, with a unit on neither side:

$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2} .
$$

**The four symmetric parts**, written with the **full dot** $\bullet$, the four half-sums under the exchange that keeps the class of the product — the interchange for the two bilinear products, the conjugate transpose for the two sesquilinear ones. The subscript names the slots as it does for the forms: none for the plain bilinear product, ${}_{\natural}$ for the quaternionic bilinear, ${}_{*}$ for the plain sesquilinear and ${}_{\natural*}$ for the quaternionic sesquilinear.

**The symmetric plain bilinear product**, the half-sum of the two orders, the **Jordan product** $\tilde Q_1\bullet\tilde Q_2$, written $\star$ in the symmetric-plain band of the physics corpus:

$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr)=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1 .
$$

**The symmetric plain sesquilinear product**, the half-sum under the conjugate transpose, the **Hermitian form** $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$, central-valued:

$$
\tilde Q_1\bullet_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\bigl[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr] .
$$

**The symmetric quaternionic bilinear product**, the half-sum of the two orders, the **quaternion form** $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, central-valued:

$$
\tilde Q_1\bullet_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1\bigr)=\bigl[Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr] .
$$

**The symmetric quaternionic sesquilinear product**, the half-sum under the conjugate transpose:

$$
\tilde Q_1\bullet_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1 .
$$

**The four antisymmetric parts**, written with the **wedge** $\wedge$, the four half-differences under the same exchange; all four have zero scalar part and lie in the vector subspace.

**The antisymmetric plain bilinear product**, the half-difference of the two orders, the **outer product** $\tilde Q_1\wedge\tilde Q_2$:

$$
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr)=\vec Q_1\times\vec Q_2 .
$$

**The antisymmetric plain sesquilinear product**, the half-difference under the conjugate transpose, the vector part $\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$:

$$
\tilde Q_1\wedge_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)=\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2} .
$$

**The antisymmetric quaternionic bilinear product**, the half-difference of the two orders:

$$
\tilde Q_1\wedge_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr)=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 .
$$

**The antisymmetric quaternionic sesquilinear product**, the half-difference under the conjugate transpose, the cross product $\vec Q_1\times\overline{\vec Q_2}$:

$$
\tilde Q_1\wedge_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\vec Q_1\times\overline{\vec Q_2} .
$$

**The reconstruction.** The dot and the wedge rebuild the four general products, so the eight parts carry the whole content of the twelve, one identity to a slot:

$$
\tilde Q_1\tilde Q_2=\tilde Q_1\bullet\tilde Q_2+\tilde Q_1\wedge\tilde Q_2,\qquad
\tilde Q_1\tilde Q_2^{*}=\tilde Q_1\bullet_{*}\tilde Q_2+\tilde Q_1\wedge_{*}\tilde Q_2,\qquad
\tilde Q_1^{\natural}\tilde Q_2=\tilde Q_1\bullet_{\natural}\tilde Q_2+\tilde Q_1\wedge_{\natural}\tilde Q_2,\qquad
\tilde Q_1^{\natural}\tilde Q_2^{*}=\tilde Q_1\bullet_{\natural*}\tilde Q_2+\tilde Q_1\wedge_{\natural*}\tilde Q_2 .
$$

**The two antisymmetrisations are not one.** The eight parts above come from the exchange that keeps the class of the product; the **bare interchange** of the two arguments gives a second antisymmetrisation and different objects — the symmetrised sesquilinear product and the **sesquilinear commutator**,

$$
[\tilde Q_1,\tilde Q_2]_\varsigma=\tilde Q_1\tilde Q_2^{*}-\tilde Q_2\tilde Q_1^{*},
$$

whose values lie in the skew-Hermitian part. **The full dot $\bullet$ and the wedge $\wedge$ are reserved for the exchange that keeps the class of the product, so neither names the objects of this paragraph.** The two are not the same operation (*Symmetric and Antisymmetric Decomposition of the Four General Products*; *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternion*), and the current of a scalar field is the commutator, $\tilde J=i[\tilde\Phi^{*}(\tilde\nabla\tilde\Phi)-(\tilde\nabla\tilde\Phi^{*})\tilde\Phi]$.

The products themselves — their coordinates, their laws, their units and their images — are *Symmetric and Antisymmetric Decomposition of the Four General Products*, and the grid of the four general products is *The Four General Products: Composition, Probability, Causality, Gauge*.

**The same code on the reduced biquaternion space.** The construction is not special to $\mathbb{B}$. On the commutative algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C}$ — the reduced biquaternions, equivalently the tessarines or the double-complex numbers — the same four general products exist, $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$, and each splits into a symmetric and an antisymmetric part by the two exchanges. Because the algebra is **commutative**, four of the twelve codes name no new operation there: $\mathrm{SPA} = \mathrm{GPA}$ and $\mathrm{SQS} = \mathrm{GQS}$, while $\mathrm{APA} = 0$ and $\mathrm{AQS} = 0$. The space therefore carries **eight distinct algebraic structures** — $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ and the four live halves $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ — and the twelve slots, the four that collapse and the eight that remain are *The Four Products, Their Forms and Their Algebraic Norms* and *The Specificities of the General Plain Algebra of the Reduced Biquaternions* of the mathematical corpus. The letter $\mathrm Q$ keeps its sense there — the first slot read through ${}_{\mathrm{ts}}$, the tessarine conjugation $j\mapsto-j$ (and $ij\mapsto-ij$) — as in the band above.

## The Involutions and the Four Forms

The algebra carries the identity and three conjugations, four maps in all, and on it there are four forms, each applying one map to each of its two arguments, so the two lists are one list read twice. One rule ties the two lists together, and that rule is what lets the series say which form is the metric and which is the inner product without having to choose.

**The setting.** $\mathbb{B}$ is a $\mathbb{C}$-algebra whose centre is $\mathbb{C}$, so every complex scalar is central, $\lambda\tilde{Q} = \tilde{Q}\lambda$ for all $\lambda \in \mathbb{C}$, which is the property that makes "$\mathbb{C}$-bilinear" well defined on $\mathbb{B}$; the scalar part $\mathrm{Sc}(\tilde{Q}) = Q_t$ is $\mathbb{C}$-linear. The centre is treated in *The Biquaternion Space, the Group of Involutions and the Six Subspaces*, §*The Complex Time Sector $\mathbb{C}_{\mathbb{B}}$*, and the forms of the algebra in *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* and its mathematical twin *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and, on the side of positivity, in *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

**The four maps.** The tensor product $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is built from two rings that each carry two involutions, the identity and the conjugation, so it carries $2\times 2 = 4$, together with the derived anti-Hermitian sign:

| Map | Mark | Action | As a ring map | Over $\mathbb{C}$ |
|---|---|---|---|---|
| Identity | — | $\tilde{Q} \mapsto \tilde{Q}$ | Automorphism | $\mathbb{C}$-**linear** |
| Complex conjugation | $\bar{\cdot}$ | $Q_\mu \mapsto \bar{Q}_\mu$ | **Automorphism**: conjugation on the scalars, identity on the quaternion factor | $\mathbb{C}$-**antilinear** |
| Quaternion conjugation | ${}^{\natural}$ | $Q_te_t - Q_x\vec e_x - Q_y\vec e_y - Q_z\vec e_z$ | **Anti-automorphism**: identity on the scalars, conjugation on the quaternion factor | $\mathbb{C}$-**linear** |
| Hermitian conjugation | ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ | $\bar{Q}_te_t - \bar{Q}_x\vec e_x - \bar{Q}_y\vec e_y - \bar{Q}_z\vec e_z$ | **Anti-automorphism** | $\mathbb{C}$-**antilinear** |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | $-\tilde{Q}^{*}$ | **Neither** | $\mathbb{C}$-**antilinear** |

The fourth column is what the two questions separate. The bar acts on the scalars and on nothing else, so it is an order-two automorphism, $\mathbb{C}$-antilinear and **not** an anti-automorphism. The quaternion conjugation and the Hermitian conjugation are the two genuine **involutions of the ring**, $(\tilde{Q}_1\tilde{Q}_2)^{\natural} = \tilde{Q}_2^{\natural}\tilde{Q}_1^{\natural}$ and $(\tilde{Q}_1\tilde{Q}_2)^{*} = \tilde{Q}_2^{*}\tilde{Q}_1^{*}$, the quaternion conjugation being the one that touches only the quaternion factor. The anti-Hermitian sign is neither: it reverses with a twist, $(\tilde{Q}_1\tilde{Q}_2)^{\flat} = -\tilde{Q}_2^{\flat}\tilde{Q}_1^{\flat}$, so it is an involution of the underlying real vector space and nothing more. It is a derived sign and not a fifth map: it is minus the star, its fixed space is the material sector alone, and a text that counts it as a fifth map will misread the lattice. The four maps, the sign they derive, their fixed and anti-fixed spaces, and the lattice they form are *Comparison of the Remarkable Subspaces*.

**The generic form.** The series writes a **generic form** $\mathrm{Form}(\tilde{Q}_1,\tilde{Q}_2)$, the form of the statement at hand, of which the four below are the instances; the matching generic norm is stated with the norms in §*The Four Algebraic Norms and the Unitary Convention*.

**The four forms, written out.** Each conjugation applied to the first argument and each to the second gives one form. The four are written with the single bracket $\langle\cdot,\cdot\rangle$, whose subscript records the pair of conjugations — nothing when the identity sits in both, ${}^{\natural}$ when the quaternion conjugation sits in the first, ${}^{*}$ when the Hermitian conjugation sits in the second, and $\natural*$ when both sit.

The **plain form** applies the identity to both arguments:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2) = Q_{1t}Q_{2t} - Q_{1x}Q_{2x} - Q_{1y}Q_{2y} - Q_{1z}Q_{2z},
$$

$\mathbb{C}$-**bilinear** in both arguments; on $\mathbb{M}_-$ it is $-c^2{t'}^2-x^2-y^2-z^2$, signature $(0,4)$.

The **quaternionic form** applies the quaternion conjugation to the first argument and the identity to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural} = \mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2) = Q_{1t}Q_{2t} + Q_{1x}Q_{2x} + Q_{1y}Q_{2y} + Q_{1z}Q_{2z},
$$

$\mathbb{C}$-**bilinear** in both arguments; on $\mathbb{M}_-$ it is $-c^2{t'}^2+x^2+y^2+z^2$, signature $(3,1)$.

The **Hermitian form** applies the identity to the first argument and the Hermitian conjugation to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*}) = Q_{1t}\bar{Q}_{2t} + Q_{1x}\bar{Q}_{2x} + Q_{1y}\bar{Q}_{2y} + Q_{1z}\bar{Q}_{2z},
$$

$\mathbb{C}$-**sesquilinear**, linear in the first argument and antilinear in the second; on $\mathbb{M}_-$ it is $c^2{t'}^2+x^2+y^2+z^2$, signature $(4,0)$.

The **Krein form** applies the quaternion conjugation to the first argument and the Hermitian conjugation to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*} = \mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2^{*}) = Q_{1t}\bar{Q}_{2t} - Q_{1x}\bar{Q}_{2x} - Q_{1y}\bar{Q}_{2y} - Q_{1z}\bar{Q}_{2z},
$$

$\mathbb{C}$-**sesquilinear**, linear in the first argument and antilinear in the second; on $\mathbb{M}_-$ it is $c^2{t'}^2-x^2-y^2-z^2$, signature $(1,3)$.

Each form is the scalar part of its own product. The Hermitian form is the pairing that carries probability; the plain form is its restriction to $\mathbb{M}_+$ and the primary computational form on the sector; the other two are read by choosing the conjugation of a slot, and the trace is a reading of the Hermitian form in the $2\times2$ image.

**The four formulas are written on the biquaternion glyph, whose two marks are independent; when one mark degenerates the brackets collapse two-and-two, and in the reduced biquaternions no mark degenerates and the four remain distinct.** Each table below gives only the brackets that survive on the layer, with the norm they carry.

**One table per lower layer.** Each table reads the brackets that survive on the layer's own glyph. The **algebraic norm** is the diagonal of the form, the **signature** is that of the real quadratic form with the positive directions counted first, and the **role** records what the bracket does: the definite bracket carries the topology and the multiplicative one the invertibility criterion.

**The complex numbers $\mathbb{C}$**, $Q=q+iq'$.

| bracket | form | algebraic norm | signature | role |
|---|---|---|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | plain, also quaternionic | $\langle Q\rangle=Q^2\in\mathbb{C}$, $\operatorname{Re}\langle Q\rangle=q^2-q'^2$ | $(1,1)$ | anisotropic; real part indefinite |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | Hermitian, also Krein | $\langle Q\rangle_{*}=Q\bar Q=q^2+q'^2$ | $(2,0)$ | definite; multiplicative; topology |

In $\mathbb{C}$ the star bracket is definite and multiplicative at once. The plain norm is complex and anisotropic; its real part is indefinite. The modulus is $\sqrt{\langle Q\rangle_{*}}$. The natural sign being the identity, the quaternionic bracket is the plain one and the Krein bracket the Hermitian one.

**The split-complex numbers $\mathbb{D}$**, $Q=q+jq'$, $j^2=+1$.

| bracket | form | algebraic norm | signature | role |
|---|---|---|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | plain, also quaternionic | $\langle Q\rangle=Q^2\in\mathbb{D}$, $\operatorname{Re}\langle Q\rangle=q^2+q'^2$ | $(2,0)$ | definite; topology; not multiplicative |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | Hermitian, also Krein | $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2$ | $(1,1)$ | multiplicative; invertibility; null cone |

The two brackets exchange their signatures with the sign of the square of the coefficient unit: $i^2=-1$ makes the real part of the plain norm indefinite and the star norm definite, while $j^2=+1$ does the reverse. Definite and multiplicative are split across the two brackets, and no single bracket is both, since $(1+j)(1-j)=0$ with $1\pm j\neq0$. The topological norm is $\sqrt{\operatorname{Re}\langle Q\rangle}$, with no modulus sign; the scale of the polar factor is $\sqrt{\lvert\langle Q\rangle_{*}\rvert}$ and is not a norm. Over the dual numbers $\mathbb{D}'$ both brackets realify to the rank-one form $q^2$; the algebraic norm is degenerate, and the topology is the Euclidean form $q^2+q'^2$ of the coefficient plane, which is not one of the brackets.

**The reduced biquaternions $\mathbb{B}_{\mathrm{r}}$**, $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with complex $Q_{\blacktriangle},Q_{\blacktriangledown}$; the marks are the bar and the tessarine sign ${}_{\mathrm{ts}}$, and ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$.

| bracket | form | algebraic norm | value | role |
|---|---|---|---|---|
| $\langle\breve Q_1,\breve Q_2\rangle=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | plain | $\langle\breve Q\rangle=Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2$ | complex | — |
| $\langle\breve Q_1,\breve Q_2\rangle_{\mathrm{ts}}=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | tessarine | $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | complex | multiplicative; invertibility; zero divisors |
| $\langle\breve Q_1,\breve Q_2\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | Hermitian | $\langle\breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^2-\lvert Q_{\blacktriangledown}\rvert^2$ | real, $(2,2)$ | indefinite |
| $\langle\breve Q_1,\breve Q_2\rangle_{\mathrm{ts}*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | tessarine-Hermitian | $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^2+\lvert Q_{\blacktriangledown}\rvert^2$ | real, $(4,0)$ | definite; topology |

The tessarine bracket carries the algebra and the tessarine-Hermitian bracket carries the topology. The tessarine norm is the **reduced norm**, multiplicative and vanishing exactly on the zero divisors, so it decides invertibility. The fourth bracket is definite, so it is not a Krein form.

**The quaternions $\mathbb{H}$**, $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ with real coefficients and $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$.

| bracket | form | algebraic norm | signature | role |
|---|---|---|---|---|
| $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ | plain, also Krein | $q_t^2-q_x^2-q_y^2-q_z^2$ | $(1,3)$ | indefinite; not multiplicative |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)$ | quaternionic, also Hermitian | $q_t^2+q_x^2+q_y^2+q_z^2$ | $(4,0)$ | definite; multiplicative; topology |

The coefficients are real and the only non-trivial involution is the natural sign, so the Hermitian form is the quaternionic one and the Krein form the plain one. The quaternionic form is definite and its norm is multiplicative, the usual quaternion norm $q_t^2+q_x^2+q_y^2+q_z^2$; the plain form is indefinite and its norm is not multiplicative.

**The split-quaternions $\mathbb{H}_{\mathrm{s}}$**, the same glyph over the units $\vec e_x^2=-e_t$ and $\vec e_y^2=\vec e_z^2=+e_t$.

| bracket | form | algebraic norm | signature | role |
|---|---|---|---|---|
| $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ | plain, also Krein | $q_t^2-q_x^2+q_y^2+q_z^2$ | $(3,1)$ | indefinite; not multiplicative |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)$ | quaternionic, also Hermitian | $q_t^2+q_x^2-q_y^2-q_z^2$ | $(2,2)$ | multiplicative; indefinite; zero divisors |

The collapse of the names is the same. The quaternionic norm is the split-quaternion norm $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+q_x^2-q_y^2-q_z^2$: multiplicative, indefinite, and vanishing exactly on the zero divisors, so it decides invertibility. The plain form is $\mathrm{Sc}(\tilde q^2)$ and is indefinite as well, so neither form is definite. No positive-definite form can be multiplicative here: $1+\vec e_y$ and $1-\vec e_y$ are non-zero and their product is $1-\vec e_y^2=0$, so a multiplicative form vanishes on one of them. The topology is therefore the Euclidean form of the coefficient space, $q_t^2+q_x^2+q_y^2+q_z^2$, which is positive definite but not multiplicative.

**The biquaternion layer.** The four brackets and their norms on $\mathbb{B}$ are the table of §*The Four Algebraic Norms and the Unitary Convention*, below.

**The Hermitian form, its norm, the unit, the normalisation and the weight.** The order is fixed once for the series. The form is

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*}) = \sum_\mu Q_{1\mu}\bar Q_{2\mu},
$$

its diagonal is the Hermitian norm,

$$
\langle\tilde{Q}\rangle_{*} = \langle\tilde{Q},\tilde{Q}\rangle_{*} = \sum_\mu\lvert Q_\mu\rvert^{2},
$$

and the unit is normalised by it, $\langle e_t\rangle_{*} = 1$. The form is positive definite on the whole algebra. Its restriction to $\mathbb{M}_+$ is the plain form,
$$
\langle\tilde{H}_1,\tilde{H}_2\rangle = \mathrm{Sc}(\tilde{H}_1\tilde{H}_2),
$$
of signature $(4,0)$ there, and its restriction to $\mathbb{M}_-$ is minus the plain form, of signature $(0,4)$. A state is normalised by the form against the unit,

$$
\langle\tilde{Ϛ},e_t\rangle_{*} = \tfrac12\langle e_t\rangle_{*},
\qquad \langle e_t\rangle_{*}=1 .
$$

and the Born weight of an observable is the normalised Hermitian form,

$$
p=\frac{\langle\tilde{Ϛ},\tilde H\rangle_{*}}{\langle\tilde{Ϛ},e_t\rangle_{*}}
 =\frac{\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})}{\mathrm{Sc}(\tilde{Ϛ})}
 =h_t+\vec r\cdot\vec h .
$$

The star is the Hermitian conjugation, and it is what makes the pairing positive definite on the whole algebra. On $\mathbb{M}_+$ it is inert, since both arguments are Hermitian, and the weight is positive there by the sector's own definiteness. The weight is written with the star on $\mathbb{M}_+$ and on $\mathbb{B}$ alike. On $\mathbb{M}_+$ both arguments are Hermitian, so $\tilde H^{*}=\tilde H$ and the star acts as the identity on them, but it is not omitted: it names the form that is positive definite everywhere. The same weight is therefore also $\mathrm{Sc}(\tilde{Ϛ}\tilde H)/\mathrm{Sc}(\tilde{Ϛ})$, the plain scalar. The plain form is the restriction of the Hermitian form to the sector, not a second definition of the weight. The Hermitian norm is the only one of the four that is positive definite on the whole algebra; the plain form is definite only on a sector, with opposite signs on the two. For a state $\tilde{Ϛ}\ge0$ and an effect $0\le\tilde H\le e_t$ the weight lies in $[0,1]$, manifestly non-negative because the form is positive definite on the whole algebra. The trace is the final reading, at normalisation: the unstarred trace is real, because $(AB)^{\dagger}=BA$ for Hermitian $A,B$ gives $\overline{\mathrm{tr}(AB)}=\mathrm{tr}(AB)$; it is non-negative here because $\mathrm{tr}(AB)=\mathrm{tr}(A^{1/2}BA^{1/2})\ge0$ for the positive state and effect. The weight is therefore also $p=\operatorname{Tr}(\tilde{Ϛ}\tilde H)/\operatorname{Tr}(\tilde{Ϛ})\in[0,1]$.

The scalar part is then a reading of the form against the unit, $\mathrm{Sc}(\tilde Q)=\langle\tilde Q,e_t\rangle_{*}$, and the trace is the reading in the $2\times2$ image, once and last,

$$
2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*}),
\qquad 2\,\mathrm{Sc}(\tilde Q)=\operatorname{Tr}(\tilde Q).
$$

The factor $2$ is the dimension of that image, not a property of the form. The order of the readings is fixed once for the series — form with star, scalar with star, plain scalar on $\mathbb{M}_+$, trace at normalisation last — and is explained in *The Born Rule from the Hermitian Form — Derivation and Comparison*. The Hermitian norm is not the normalising functional: on a state it reads $\langle\tilde{Ϛ}\rangle_{*}=\tfrac14(1+|\vec r|^2)$, which varies from $\tfrac14$ to $\tfrac12$ across the Bloch ball.

**In the $2\times2$ image.** The four forms are the traces of their products up to that factor,

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

**Where the four are proved and named.** The classification of the four, their Gram matrices, their signatures, their isometry groups, their Witt classes, and their reading as Hermitian forms over the algebra with respect to their own involutions are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, with its twin *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*.

**What is forced and what is chosen.** The two bilinear forms are $\mathbb{C}$-bilinear in both slots and the two sesquilinear forms are linear in the first slot and sesquilinear in the second. That is not a choice but a consequence of the $\mathbb{C}$-linearity of the natural sign together with the centrality of $\mathbb{C}$ in $\mathbb{B}$; its verification is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. Multiplication by $i$ reverses the sign of the two bilinear forms and leaves the two sesquilinear forms unchanged, since the centrality of $i$ puts either a factor $i^2 = -1$ on both slots or on neither.

## The Four Algebraic Norms and the Unitary Convention

**The definition of a norm.** The norm of a form is that form read at its two equal arguments,

$$
\mathrm{Norm}(\tilde{Q}) = \mathrm{Form}(\tilde{Q},\tilde{Q}) ,
$$

and the convention is one of **notation, not of substance**: the pair is the form and the norm of the statement at hand, and the four forms above and the four norms below are its instances.

**Bars around a complex element are the ordinary complex modulus.** For $Q=q+iq'$,

$$
\lvert Q\rvert=\sqrt{Q\bar Q}=\sqrt{q^2+q'^2},
$$

a real and non-negative number. The bars are the modulus and not a bracket of the layer: the algebraic norms keep their bracket, $\langle Q\rangle=Q^2$ and $\langle Q\rangle_{*}=Q\bar Q$. The same bars apply to a complex coefficient of a biquaternion, $\lvert Q_\mu\rvert=\sqrt{q_\mu^2+q'_\mu^2}$; over $\mathbb{C}$ the square of the modulus is the Hermitian norm, $\lvert Q\rvert^2=\langle Q\rangle_{*}$.

**The four algebraic norms.** Each pair gives one norm, the diagonal of its form. **One bracket, two arities:** the bracket names the form when it carries two arguments and the algebraic norm when it carries one, so the plain bracket is the form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ and the norm $\langle\tilde{Q}\rangle = \langle\tilde{Q},\tilde{Q}\rangle$, and the same holds for the Hermitian, the quaternionic and the Krein. Read with one argument, the value lies in $\mathbb{C}$ for the two bilinear norms and in $\mathbb{R}$ for the two sesquilinear norms, because a sesquilinear form has a real diagonal. The four names are those of the four forms with *norm* in place of *form*:

| bracket | form | letter | algebraic norm | value | realified signature | role |
|---|---|---|---|---|---|---|
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle=\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ | plain | $P$ | $Q_t^2-Q_x^2-Q_y^2-Q_z^2$ | $\mathbb{C}$ | $(4,4)$ | complex cone |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}=\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$ | quaternionic | $N$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | $\mathbb{C}$ | $(4,4)$ | multiplicative; zero-divisor cone |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$ | Hermitian | $H$ | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ | $\mathbb{R}$ | $(8,0)$ | definite; topology |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}=\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2^{*})$ | Krein | $K$ | $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$ | $\mathbb{R}$ | $(2,6)$ | indefinite |

**One letter, two arities.** The four also carry one letter each, $P$ for the plain, $N$ for the quaternionic, $H$ for the Hermitian and $K$ for the Krein, the letter naming the form with two arguments and the algebraic norm with one: $P(\tilde{Q}_1,\tilde{Q}_2)$ is the plain form and $P(\tilde{Q})$ the plain norm, and the same holds for the other three. The plain norm is written $P$ and not $B$, because $B$ is the complex modulus of the vector part, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$. The letters and the four qualified notions of a regular and a degenerate biquaternion are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*.

The quaternionic norm is the determinant in the $2\times2$ image and is the multiplicative one, vanishing exactly on the zero-divisor cone; the Hermitian norm is the definite one and carries the topology. The signature column is that of the realified form on the eight real parameters; on the material sector the restrictions are those stated above. Read on one argument the four are the plain norm, the Hermitian norm, the quaternionic norm and the Krein norm. The other sense of the word, the **topological norm**, is the square root of the definite one, $\lVert\tilde{Q}\rVert_E = \bigl(\langle\tilde{Q}\rangle_{*}\bigr)^{1/2}$, and it is *The Norm Defined by a Form*. The four products, their forms and their norms go together, one to a row:

| Product | Form | Letter | Norm |
|---|---|---|---|
| the general plain bilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | $P$ | the plain norm $\langle\tilde{Q}\rangle$ |
| the general quaternionic bilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | $N$ | the quaternionic norm $\langle\tilde{Q}\rangle_{\natural}$ |
| the general plain sesquilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | $H$ | the Hermitian norm $\langle\tilde{Q}\rangle_{*}$ |
| the general quaternionic sesquilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}$ | $K$ | the Krein norm $\langle\tilde{Q}\rangle_{\natural*}$ |

**The qualified regular and the qualified degenerate.** For a letter $\Phi$ of the four, a biquaternion is **$\Phi$-regular** when $\Phi(\tilde{Q})\neq0$ and **$\Phi$-degenerate** when $\Phi(\tilde{Q})=0$. Only $N$ decides invertibility: $\{N=0\}$ is the origin together with the zero divisors, so $N$-regular is the unit group and $N$-degenerate the non-units. $P$-degenerate and $K$-degenerate contain units, $P(e_t+\vec e_x)=K(e_t+\vec e_x)=0$ with $N(e_t+\vec e_x)=2$, and $H$-degenerate is the origin alone. The unqualified *regular* is the spectral one, $B^{2}\neq0$, of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, so the letter is never omitted.

### The Unitary Convention

A unit element carries its own glyph, the **$u$** in the two cases, beside the root $\tilde\Xi$, the idempotent $\tilde\Pi$ and the nilpotent $\tilde\nu$, as in the mathematical corpus (§*The Unitary Convention* of *Conventions in Mathematics*): the letter $u$ is reserved for a unit element, and a general element is $\tilde q$ or $\tilde Q$. **The exponential is written $\exp(\cdot)$**, never $e^{\cdot}$, the letter $e$ being the base $e_t,\vec e_x,\vec e_y,\vec e_z$. A unit element is an element of norm one, and the norm is the one in view: the glyph is the generic norm read at the central value $e_t$, so it names no set until the norm is named, and the four norms of the biquaternion layer give four level sets:

| Letter | Norm | the condition $\mathrm{Norm}(\tilde U)=e_t$ | the norm-one elements |
|---|---|---|---|
| $P$ | $\langle\tilde Q\rangle$ | $Q_t^2-Q_x^2-Q_y^2-Q_z^2=e_t$ | the complex hyperboloid of the plain norm |
| $N$ | $\langle\tilde Q\rangle_{\natural}$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2=e_t$ | $\mathbb{B}^{\times}_1$, the norm-one units |
| $H$ | $\langle\tilde Q\rangle_{*}$ | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2=1$ | the unit sphere of the Hermitian norm |
| $K$ | $\langle\tilde Q\rangle_{\natural*}$ | $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2=1$ | the indefinite level set of the Krein norm |

The two bilinear norms are complex-valued, so their condition is $=e_t$; the two sesquilinear norms are real-valued, so theirs is $=1$. In the quaternion layer the level set is $Sp(1)=\{\tilde u\in\mathbb{H}:\tilde u\tilde u^{\natural}=e_t\}=S^{3}=\mathrm{SU}(2)$, and **the rotors are these elements**: an orientation rotor, of norm $e_t$, is a unit real quaternion and is written $\tilde u$.

**The group condition is narrower than the norm-one condition.** Where the sesquilinear form is preserved, $\tilde U^{*}\tilde U=e_t$, the norm-one elements that do so form the **unitary group**, written without the tilde of an element,

$$
\mathrm{U}(\mathbb{B})=\{\tilde U:\tilde U^{*}\tilde U=e_t\}\cong \mathrm{U}(2)=S^{1}\cdot S^{3},\qquad S^{1}\cap S^{3}=\{\pm e_t\},
$$

of real dimension $4$. The name **unitary** is the name of that group; the glyph $\tilde U$ is the wider norm-one element. The norm and the group condition exist only where their involution does: the bar alone over $\mathbb{C}$ and the split-complex numbers, the natural sign alone over $\mathbb{H}$ and the split-quaternions, all four marks over $\mathbb{B}$ and the split-biquaternions.

**The case rule splits the glyph**, as for the elements: $\tilde U$ in the biquaternion and split-biquaternion layers, $\tilde u$ in the quaternion and split-quaternion ones, $U$ in the complex, split-complex, dual and reduced biquaternion ones. The pure case carries the arrow, $\vec u$ and $\vec U$.

**The coordinates carry the letter of the unit element**: in $\mathbb{B}$ it is $\tilde U = U_te_t + U_x\vec e_x + U_y\vec e_y + U_z\vec e_z$ with $U_\mu = u_\mu + iu'_\mu$ and vector part $\vec U = \vec u + i\vec u'$; in $\mathbb{H}$ it is $\tilde u = u_te_t + u_x\vec e_x + u_y\vec e_y + u_z\vec e_z$ with real $u_\mu$. **A coordinate carries the label of its direction**, as the base does: the scalar coordinate is $U_t$ and the vector coordinates are $U_x, U_y, U_z$, and likewise $u_t, u_x, u_y, u_z$ for the quaternion-layer element $\tilde u$; a role label is written in the upright roman where the statement names a role. **It is allowed to add subscripts when several unit elements are used**, $\tilde U_1, \tilde U_2$.

**The letter $u$ names a unit element and nothing else.** A velocity, a speed, a Lorentz factor and a rapidity are never written $u$ or $U$: the letter of a motion is $v$, and the four-velocity is the element $\tilde V$. A unitary group is written $\mathrm{U}(1)$, $SU(2)$, $SU(3)$, and its Lie algebra in the upright roman, $\mathrm{u}(1)$, $\mathrm{su}(2)$, $\mathrm{su}(3)$.

**The boost is a unit element, not a letter.** The boost of rapidity $\psi$ along the unit $\vec u_{\mathrm b}$ is
$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b},
$$
a Hermitian element of norm one; it carries the glyph $\tilde U$ of every unit element. It is the **frame rotor**; the four-vector factor $\mathcal B=\tilde U_{\mathrm b}^{-2}$ is a different object, and §*The Polar Word and the Three Pairings* separates the four objects called a boost. Where an infinitesimal generator is needed it is read from the exponential as the pure element $\tfrac12 i\vec u_{\mathrm b}$, and the Lorentz brackets are written on the pure elements $\tfrac12\vec e_k$ and $\tfrac12 i\vec e_k$. No letter $K$ is introduced for the Lorentz boost.

## The Polar Word and the Three Pairings

The series writes one polar word and reads it in three bracketings. The word, its factors and the three readings are fixed here once: the polar-decomposition articles of the *Biquaternions* category prove the statements and the physics articles interpret them, but all of them use these symbols with these meanings.

### The Word and Its Factors

**The domain.** The word exists on the complement of the zero-divisor cone, $\langle\tilde Q\rangle_{\natural}\neq0$, and on no larger set. The existence and uniqueness are those of *Modulus–Unit Polar Decomposition of Biquaternions*.

**The word.** Every element off the cone is the ordered product

$$
\tilde Q=r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad r>0,\qquad \alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}],\qquad \psi_w\ge0,\qquad \theta\in[0,2\pi],
$$

with the factors of the table. The order is forced: the scale and the phase are central, the Hermitian positive boost stands on the left of the real rotor, and the rotor is what remains after the Hermitian part is divided out.

| # | factor | glyph | range | type | action on the algebra |
| --- | --- | --- | --- | --- | --- |
| 1 | scale | $r$ | $r>0$ | real central scalar | dilation by $r^2$ |
| 2 | central phase | $\exp(i\alpha)$ | $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | central unit | scalar multiplication |
| 3 | boost | $\tilde U_{\mathrm b}(\psi_w)=\cosh\frac{\psi_w}{2}e_t+i\sinh\frac{\psi_w}{2}\vec u_{\mathrm b}$ | $\psi_w\ge0$, $\vec u_{\mathrm b}$ a unit real vector | Hermitian positive, $\det=1$ | congruence $X\mapsto\tilde U_{\mathrm b}(\psi_w)X\tilde U_{\mathrm b}(\psi_w)^{*}$ |
| 4 | rotor | $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\vec u_{\mathrm r}$ a unit real vector | real unit quaternion | conjugation $X\mapsto\tilde u_{\mathrm r}X\tilde u_{\mathrm r}^{-1}$ |

**The word is not the exponential.** The four factors are a section of the word map, not of the exponential map; the two coincide only when the exponents commute. The defect is the Baker–Campbell–Hausdorff term, and it is recorded in *The Exponential Word and Its Boundary*.

### The Two Norms of the Word

The modulus is the square root of the **quaternionic** norm, and it is not the square root of the Hermitian norm. The two norms measure different things, and the corpus uses both.

| bracket | name | value | role in the word |
| --- | --- | --- | --- |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | quaternionic norm | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$, complex | the modulus, $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ on the principal branch; multiplicative; vanishing is the cone |
| $\langle\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})$ | Hermitian norm | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$, real and non-negative | the total size; it carries the topology and never enters the existence condition of the word |

**Two warnings.** First, a square root of the Hermitian norm is the **topological norm**, not the polar modulus: the polar modulus is complex and the topological norm is real, so the two are not interchangeable. Second, the polar articles write $E^2=\sum_\mu\lvert Q_\mu\rvert^2$ for the Hermitian norm. That $E$ is not the physical energy: for a four-momentum it is $m^2c^2\cosh 2\psi$ in the notation below, not $m^2c^4\cosh^2\psi$. A formula that needs the energy takes it from the four-momentum, not from this $E^2$.

### The Four Objects Called a Boost

Four different objects carry the word *boost*, and the factor of two between them is the most common error in the corpus. They are separated here once. The kinematic rapidity is $\psi$; the word's parameter is $\psi_w$.

| object | glyph | formula | exponent angle | what it is |
| --- | --- | --- | --- | --- |
| frame rotor | $\tilde U_{\mathrm b}(\psi)$ | $\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | $\psi/2$ | the Lorentz rotor; its congruence is the boost of rapidity $\psi$; linear in the spinor |
| four-vector factor | $\mathcal B=\tilde U_{\mathrm b}(\psi)^{-2}$ | $\cosh\psi\,e_t-i\sinh\psi\,\vec u_{\mathrm b}$ | $-\psi$ | the inverse square of the frame rotor; the factor a four-vector element carries |
| generator | $\tfrac12 i\psi\vec u_{\mathrm b}$ | — | — | the Hermitian element whose exponential is $\tilde U_{\mathrm b}(\psi)$ |
| rapidities | $\psi,\ \psi_w$ | real, $\psi\ge0$ | — | $\psi$ kinematic; $\psi_w=2\psi$ for a four-vector element, whose word axis is opposite the frame axis |

The fourth factor of the word, $\tilde u_{\mathrm r}$, is a rotation and not a boost. The word *boost* alone is not a name: a statement must say whether it means the frame rotor, the four-vector factor, the generator or a rapidity. In the word table the letter $\vec u_{\mathrm b}$ names the axis of the word's factor; for a transformation it coincides with the frame axis, and for a four-vector it is opposite it.

**Linear and bilinear.** The frame rotor acts on a spinor by left multiplication, $\chi\mapsto\tilde U_{\mathrm b}(\psi)\chi$, and on a four-vector by the congruence $X\mapsto\tilde U_{\mathrm b}(\psi)X\tilde U_{\mathrm b}(\psi)^{*}$. A four-vector is bilinear in the spinor, so the factor that the four-vector element itself carries is the inverse square, $\mathcal B=\tilde U_{\mathrm b}(\psi)^{-2}=e^{-i\psi\vec u_{\mathrm b}}$: the same boost, read twice. The word stores the boost in the frame rotor and deposits it twice in the four-vector; its parameter is $\psi_w=2\psi$.

### The Four-Momentum

Let $\tilde P=i(E/c)e_t+\vec p$ with $E=mc^2\cosh\psi$ and $\vec p=mc\sinh\psi\,\hat p$, so that $\psi$ is the kinematic rapidity. Then

$$
\tilde P=imc\,\mathcal B,\qquad \mathcal B=e^{-i\psi\hat p},\qquad \Rho=imc,\qquad \Theta=-i\psi,\qquad \vec U=\hat p,
$$

with $B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}=\lvert\vec p\rvert$, and the eigenvalues are

$$
\lambda_\pm=Q_t\pm iB=imc\,e^{\pm\psi}=\Rho\,e^{\pm i\Theta}.
$$

The word's parameter here is $\psi_w=2\psi$, and the third factor of the word is $\mathcal B$, whose axis is $-\hat p$. The frame rotor $\tilde U_{\mathrm b}(\psi)$ has the axis $+\hat p$.

**Three errors to avoid.** Writing $\Theta=+i\psi$ swaps the two eigenvalues. Writing $\psi$ for the word parameter when the element is a four-vector halves the word's rapidity, because $\psi_w=2\psi$. Taking the frame rotor $\tilde U_{\mathrm b}(\psi)$ for the four-vector factor gives $imc\,\tilde U_{\mathrm b}(\psi)$, a four-vector of rapidity $\psi/2$. The Hamilton axis $\vec U=\vec Q/B$ points along the momentum; the word's axis in $\mathcal B$ points opposite it, because $\mathcal B=e^{-i\psi\hat p}$ is a boost of rapidity $\psi$ about $-\hat p$.

### The Trace and the Normalised State

The trace is the trace of the $2\times2$ image and nothing else,

$$
\operatorname{Tr}\tilde Q=\operatorname{Tr}\mathsf M_2(\tilde Q)=2\,\mathrm{Sc}\,\tilde Q=2Q_t.
$$

The factor $2$ is forced by $\mathsf M_2(e_t)=I_2$ and cannot be divided out. It cancels in every ratio, and the Born weight is a ratio:

$$
p=\frac{\langle\tilde{Ϛ},\tilde H\rangle_{*}}{\langle\tilde{Ϛ},e_t\rangle_{*}}=\frac{\operatorname{Tr}(\tilde{Ϛ}\tilde H)}{\operatorname{Tr}\tilde{Ϛ}},
\qquad \operatorname{Tr}\tilde{Ϛ}=1\iff\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12 .
$$

A normalised state therefore has trace one; the factor $2$ belongs in the definition of the trace and cancels in the probability. Dropping it from the trace or inserting it in the ratio are the two opposite mistakes.

### The Domains of the Three Pairings

The three pairings are three bracketings of the same word, and their domains differ. The table records the condition for the **factorisation** and the condition for the **construction**, which are not the same statement.

| pairing | factorisation | factorisation exists | construction exists | witness of failure |
| --- | --- | --- | --- | --- |
| word | $r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ | same | any element of the cone |
| quaternion | $\tilde q\,e^{i\tilde\Psi}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ | $\tilde q_r\neq0$ (on this domain) | $i\vec e_x+i\vec e_y$: $\langle\tilde Q\rangle_{\natural}=-2$ but $\tilde q_r=0$ |
| Hamilton | $\Rho\,e^{\vec U\Theta}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ | same | $e_t+\vec e_x+i\vec e_y$: $\langle\tilde Q\rangle_{\natural}=1$ but $\langle\vec Q,\vec Q\rangle_{\natural}=0$ |
| Cartan | $\tilde H\tilde U$ | $\langle\tilde Q\rangle_{\natural}\neq0$ | same | $e_t+i\vec e_x$: on the cone; the generalized form gives a partial isometry |

**The domains are not nested.** The quaternion construction fails at $\tilde q_r=0$; the Hamilton pairing fails when the vector part is null; the Cartan pairing is the widest and is total off the cone. The generalized polar decomposition extends the Cartan pairing to the cone with a partial isometry, and it is *The Generalized Polar Decomposition of a Biquaternion*.

**The tangent equation on the domain of the word.** The equation $\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i$ fails to have a real solution in exactly one case, when $\tilde q_r^{-1}\tilde q_i$ is a unit pure quaternion. That case forces $\langle\tilde Q\rangle_{\natural}=0$: writing $\tilde q_i=\tilde q_rT$ with $T$ a unit pure quaternion makes the real inner product of $\tilde q_r$ and $\tilde q_i$ vanish and their norms equal, so the difference of the squared norms and the cross term both vanish. On the complement of the cone, therefore, the construction exists exactly when $\tilde q_r\neq0$. The condition $\tilde q_r\neq0$ alone is not sufficient on the whole algebra: $e_t+i\vec e_x$ has $\tilde q_r=e_t$ and lies on the cone, where the word does not exist. The article's "exactly" is correct on the word's domain; its claim that the set $\{\tilde q_r\neq0\}$ lies inside that domain is not.

## The Central Map and Its Restrictions

The scalar imaginary $i$ is central, so multiplication by it is **one** $\mathbb{C}$-linear map of the algebra, and the movements the series reads in four places are its restrictions to the subspaces. The generator satisfies $(ie_t)^2=-e_t$, so its powers close on four values and the group $\exp(i\theta)e_t$ of the centre interpolates between them. The remarkable subspaces carry the restrictions.

| Subspace | $i\,\cdot$ | The name |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the complex time sector | Itself | The global phase |
| $\mathrm{Vect}(\mathbb{B})$, the complex space sector | Itself | The duality rotation |
| $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ | Each other | The Wick rotation |
| $\mathbb{M}_-$ and $\mathbb{M}_+$ | Each other | The material–informational exchange |

The rule that ties the names is a rule about the generator and not about the subspaces: the map is central, so it acts the same way in every subspace, and it is a scalar that acts through the centre and never through the quaternion directions; a non-central generator would give one rotation per carrier. It is a rotation and not a projection, a collapse or a measurement — a loss of information is a non-invertible map and belongs to *The Operators: One-Sided, Two-Sided, Sandwich*.

**The relation to the Wick rotation.** The coordinate continuation $t' \mapsto -i\tau$ of *Interpretation of the Wick Rotation in the Biquaternion Universe*, and the two senses in which the series uses the phrase *Wick rotation* — the exchange of the real and imaginary sectors, on the whole element, and the continuation of the time coordinate, a relabeling of one coordinate — are set out there. The two share one generator and one temporal sign flip, and they are not the same map.

The phase gate of the gate articles is a rotation about $\vec e_z$, a non-central generator, and it must not be identified with the central rotation.

## The Special Elements: Root, Idempotent and Nilpotent

**The special glyphs are notational.** A root $\tilde\Xi$, an idempotent $\tilde\Pi$ or a nilpotent $\tilde\nu$ is not a different kind of object from a generic $\tilde Q$: the glyph records what the element is known to be, at the point of use.

### The Root Convention

The roots carry a symbol of their own, beside the idempotent $\tilde{\Pi}$ (§*The Idempotent Convention*) and the nilpotent $\tilde{\nu}$ (§*The Nilpotent Convention*): the **xi**, in the two cases.

A **root of $1$** of the algebra is an element $\tilde{\Xi}$ with $\tilde{\Xi}^2 = 1$. More generally a **root of a central value** $\lambda$ is an element with $\tilde{\Xi}^2 = \lambda e_t$. The roots of the three central values $-1, 0, +1$ are those of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general root is that of *Square Roots of a General Element in the Biquaternion Algebra*; the roots the series uses are the roots of $1$.

**The square is read in a named product**, the algebra product unless the statement names another, as for the nilpotents (§*The Nilpotent Convention*), and the class is relative to the product; the roots of a value in the four general products are those of *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The case rule splits the glyph, as it does for the elements, the idempotents and the nilpotents.** The roots of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde{\Xi}$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde{\xi}$; those of the complex, split-complex and dual layers carry the plain capital, $\Xi$; and those of the reduced biquaternion layer carry the same plain capital, $\Xi$, no tilde being written where there is no quaternionic factor. The layer fixes the glyph.

**The coordinates carry the letter of the root**: in $\mathbb{B}$ the root is $\tilde{\Xi} = \Xi_te_t + \Xi_x\vec e_x + \Xi_y\vec e_y + \Xi_z\vec e_z$ with $\Xi_\mu = \xi_\mu + i\xi'_\mu$, its scalar part $\Xi_t$ and its vector part $\vec\Xi = \vec\xi + i\vec\xi'$; in $\mathbb{H}$ it is $\tilde\xi = \xi_te_t + \xi_x\vec e_x + \xi_y\vec e_y + \xi_z\vec e_z$ with real $\xi_\mu$.

**It is allowed to add subscripts when several roots are used.** **The subscript of a root is numeric when it counts and a role label when it names.** Where more than one occurs the roots are numbered, $\tilde\Xi_1, \tilde\Xi_2$, as for the nilpotents and for the idempotent pairs other than the complete sign pair of §*The Idempotent Convention*; where a root plays a named role, it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The root glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\Xi$ | A root of $1$ of the complex, split-complex or dual layer, where no tilde is written |
| $\Xi_\pm$ | A root of $1$ of the reduced biquaternion layer, where no tilde is written |
| $\tilde{\xi}$ | A root of $1$ of the quaternion or split-quaternion layer |
| $\tilde{\Xi}$ | A root of $1$ of the biquaternion or split-biquaternion layer |

### The Idempotent Convention

The convention of *The Elements and their Coefficients* fixes the case and the tilde of a generic element. The idempotents carry a symbol of their own, and the series uses it throughout.

An **idempotent** of the algebra is an element $\tilde{\Pi}$ with $\tilde{\Pi}^2 = \tilde{\Pi}$; a **projector** is an idempotent operator, $p^2 = p$, that is an idempotent of the morphism space, not an element of the algebra, and an idempotent element corresponds to a projector when its multiplication operator is idempotent. An idempotent fixed by the star, $\tilde{\Pi}^{*} = \tilde{\Pi}$, is a **Hermitian idempotent**, and the rank-one Hermitian idempotents of $\mathbb{M}_+$ are the **pure states** of the informational sector.

**The case rule splits the glyph, as it does in the mathematical corpus.** The idempotents of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde{\Pi}$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde{\pi}$; those of the complex, split-complex, dual and reduced biquaternion layers carry the plain capital, $\Pi$, no tilde being written where there is no quaternionic factor. The series works in $\mathbb{B}$ and writes $\tilde{\Pi}$ throughout; the other glyphs are the mathematical corpus's, and the layer fixes the glyph.

A non-zero idempotent $\tilde{\Pi}$ generates the **minimal left ideal** $\mathbb{B}\tilde{\Pi}$, which is the state module of the companion articles; the standard pair, the classification of the idempotents, the polarisation identity, the Peirce decomposition, the matrix units and the projective geometry of the pure states are those of *Square Roots of One and the Idempotents of the Biquaternion Algebra* and its companions in the mathematical corpus.

**The coordinates carry the letter of the idempotent**: in $\mathbb{B}$ the idempotent is $\tilde{\Pi} = \Pi_te_t + \Pi_x\vec e_x + \Pi_y\vec e_y + \Pi_z\vec e_z$ with $\Pi_\mu = \pi_\mu + i\pi'_\mu$, its scalar part $\Pi_t$ and its vector part $\vec\Pi = \vec\pi + i\vec\pi'$; in $\mathbb{H}$ it is $\tilde\pi = \pi_te_t + \pi_x\vec e_x + \pi_y\vec e_y + \pi_z\vec e_z$ with real $\pi_\mu$.

**It is allowed to add subscripts when several idempotents are used.** **The subscript of an idempotent is numeric when it counts and a role label when it names, but for the two members of a complete sign pair.** A pair is $\tilde{\Pi}_1, \tilde{\Pi}_2$; a second pair in the same statement takes the next numbers, $\tilde{\Pi}_3, \tilde{\Pi}_4$; and a family indexed by a direction is written with its argument, $\tilde{\Pi}_{1,2}(\vec u)$. When a pair is **complete**, $\tilde{\Pi}_+ + \tilde{\Pi}_- = e_t$, its two members may be written $\tilde{\Pi}_+$ and $\tilde{\Pi}_-$: the subscript $+$ names the member attached to $+1$ and the subscript $-$ the member attached to $-1$. A pair that is not complete may be numbered, labelled or signed as the statement requires. A role label is written in upright roman, as for a unit element.

The idempotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\Pi$ | An idempotent of the complex, split-complex or dual layer, in the mathematical corpus |
| $\Pi_\pm$ | An idempotent of the reduced biquaternion layer, in the mathematical corpus |
| $\tilde{\pi}$ | An idempotent of the quaternion or split-quaternion layer, in the mathematical corpus |
| $\tilde{\Pi}$ | An idempotent or a pure state of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde{\Pi}$ it generates |

### The Nilpotent Convention

The nilpotents carry a symbol of their own, beside the idempotent $\tilde{\Pi}$ (§*The Idempotent Convention*): the lower-case $\tilde{\nu}$ of the quaternion and split-quaternion layers and the upper-case $\tilde{\Upsilon}$ of the biquaternion and split-biquaternion layers. **The capital is an upsilon and not a $Y$.**

A **nilpotent** of the algebra is an element $\tilde{\nu}$ whose square vanishes,

$$
\tilde{\nu}^2 = 0 .
$$

**The square is read in a named product**, the algebra product unless the statement names another, as in the mathematical corpus (§*The Nilpotent Convention* of *Conventions in Mathematics*), and the class is relative to the product. A nilpotent is never a Hermitian idempotent, a Hermitian nilpotent being zero, and it is never a state; the nilpotent is the partner of the idempotent in a minimal left ideal, $\mathbb{B}\vec{\Upsilon}_2 = \mathbb{B}\tilde{\Pi}_1$.

**The coordinates carry the letter of the nilpotent**: in $\mathbb{B}$ the nilpotent is $\tilde{\Upsilon} = \Upsilon_te_t + \Upsilon_x\vec e_x + \Upsilon_y\vec e_y + \Upsilon_z\vec e_z$ with $\Upsilon_\mu = \nu_\mu + i\nu'_\mu$, its scalar part $\Upsilon_t$ and its vector part $\vec\Upsilon = \vec\nu + i\vec\nu'$; in $\mathbb{H}$ it is $\tilde\nu = \nu_te_t + \nu_x\vec e_x + \nu_y\vec e_y + \nu_z\vec e_z$ with real $\nu_\mu$.

**It is allowed to add subscripts when several nilpotents are used.** **The subscript of a nilpotent is numeric when it counts and a role label when it names**, as for the idempotents apart from their complete sign pair: where more than one occurs a pair is $\tilde{\nu}_1, \tilde{\nu}_2$, a second pair in the same statement takes the next numbers, and where a nilpotent plays a named role it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The nilpotents have no classification of the idempotent kind and no sphere of pure states; which set the square-zero elements form depends on the product. The nilpotents of a state module are those of *The Biquaternion Vacuum as a Minimal Idempotent*, and the spin-down state of *Spin-1/2 Quantum Physics in Biquaternionic Form* is a nilpotent of the ideal of that vacuum.

The nilpotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\Upsilon$ | A nilpotent of the complex, split-complex or dual layer, where no tilde is written |
| $\tilde{\nu}$ | A nilpotent of the quaternion or split-quaternion layer |
| $\tilde{\Upsilon}$ | A nilpotent of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde{\Upsilon}$ it generates |
| $\vec{\Upsilon}$, $\vec{\nu}$ | A pure nilpotent, written with the arrow and without the tilde by the priority rule of §*Pure Elements and their Coefficients* |

The standard pair of nilpotents is $\vec{\Upsilon}_1$ and $\vec{\Upsilon}_2$, the off-diagonal Peirce units of *Ideals and Peirce Decompositions of the Biquaternion Algebra* exchanged by the star. The truncated ladder of *The Biquaternion Vacuum as a Minimal Idempotent* and of the Fock, vacuum and matrix-representation articles is this pair: those articles write it $\vec{\Upsilon}_1$ and $\vec{\Upsilon}_2$ wherever the algebra element is meant, and keep the ladder letters for the abstract operators.

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

**No index is raised or lowered anywhere in the series.** On $\mathbb{C}^4$ there is no pairing with which to move one, and the $ict'$ convention is what puts the metric into the coefficient — $(ict', \vec q)$ rather than a contraction rule — so that the interval is the sum of squares with no explicit scalar product. The article owns the product in components.

## The Matrix Representations

The algebra is read in matrices in two ways, and the two answer different questions. The **4×4 reading** is the regular representation: multiplication by an element becomes a linear map on the coefficient quadruple, and the matrices are operators on that quadruple. The **2×2 reading** is the isomorphism $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$: the elements themselves become complex matrices. They are different representations, not two sizes of one: the $4\times4$ matrices act on $\mathbb{C}^4$ and the $2\times2$ matrices on $\mathbb{C}^2$.

### General Matrix Conventions

**A matrix carries no tilde, and the ban is absolute.** The tilde marks an element of the algebra, not its image. The identity is $I_n$, with $\mathsf{M}_2(e_t)=I_2$ and $\mathsf{M}_4(e_t)=I_4$, and the image of an element is written $\mathsf{M}_2(\tilde Q)$ or $\mathsf{M}_4(\tilde Q)$, with the tilde inside the argument. **An array of biquaternions carries no tilde either.** A matrix whose entries are biquaternions is written $\mathsf{Q}=(\tilde Q_{\lambda\rho})\in\mathbb{B}^{n\times m}$: the tildes sit on the entries, and the array that holds them has none, whatever its size and whatever its entries. The identity matrix never takes a tilde; nor do the regular matrices $\mathsf{M}_4$ and $\mathsf{M}_4^{R}$, whose subscript gives the size and whose superscript, where present, gives the side of the multiplication. The same ban covers a matrix of biquaternions and a colour matrix.

**The ban is on the array, not on its argument.** The writings $\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_4(\tilde Q)$ are correct because the tilde stays inside the argument. A tilde on the array — $\tilde I_n$, $\tilde{\mathsf{M}}_2$, $\tilde{\mathcal Q}$, or $\tilde Q$ where the matrix $\mathsf{M}_2(\tilde Q)$ is meant — is forbidden and is a defect to be rewritten, not a variant to be read: no object is behind it, and the element it would name is already named by the argument.

**The letter $M$ belongs to matrices.** It names a matrix and nothing else: the images $\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_4(\tilde Q)$, the matrix algebras $M_2(\mathbb{C})$ and $M_4(\mathbb{C})$, and an entrywise matrix in a proof. No element of the algebra is written $M$, with or without a tilde.

### The 4×4 Matrix Representation

Multiplication is read as a linear map on the coefficient quadruple, in *The Element and Operator Representations*. The four units act by

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

### The 2×2 Matrix Representation

The algebra is read as the complex $2 \times 2$ matrices, under the isomorphism

$$
\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C}),
$$

in *The Element and Operator Representations*, and this is the representation every numerical check in the series is performed with. The four unit images are fixed here, once, because every article depends on them agreeing. The three vector units are the Pauli matrices times $-i$:

$$
\mathsf{M}_2(e_t) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\mathsf{M}_2(\vec e_x) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_z) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

with the central scalar mapping to $\mathsf{M}_2(i) = iI_2$. Because $\mathsf{M}_2$ is $\mathbb{C}$-linear, the Hermitian units require no separate choice, $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$.

**The trace is the trace of this image.** The Hermitian form above is defined on the algebra and needs no matrix. The trace is defined only here, on the image, and it is a reading of the Hermitian form in this presentation, not a second pairing. The series writes

$$
\operatorname{Tr}(\tilde{Q}) := \operatorname{Tr}\mathsf{M}_2(\tilde{Q}).
$$

On the units $\operatorname{Tr}(e_t) = 2$ and $\operatorname{Tr}(\vec e_k) = 0$, so on a general element $2\,\mathrm{Sc}(\tilde{Q}) = \operatorname{Tr}(\tilde{Q})$. That factor $2$ is not a normalisation but a consequence of $\mathsf{M}_2(e_t) = I_2$: it comes with the four images above and cannot be divided out. The probability pairing is written in the Hermitian form and read in the trace where the $2\times2$ image is used, the Born rule among them,

$$
2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*}),\qquad 2\,\mathrm{Sc}(\tilde Q)=\operatorname{Tr}(\tilde Q),
$$

and this is the only place in the section where the trace appears. An unsubscripted trace means this one; a regular matrix has its own, written with its subscript. The identity $2\,\operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2) = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2)$ is the same reading applied to the plain form, not a probability statement. The same element in the regular $4\times4$ representation has trace $4\,\mathrm{Sc}(\tilde{Q})$, twice the trace of the $2\times2$ image: the factor belongs to the presentation, not to the element.

**The determinant is the norm.** The determinant of the image is the biquaternion norm, $\det\mathsf{M}_2(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}$, and it is multiplicative, which is what makes the matrix model compute every norm in the series. The invertibility criterion, the group of units and the unit-norm group are read from it; the derivations are *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

**The assignment is forced, not chosen.** $\vec e_k^2 = -e_t$ requires the factor $i$ and $\vec e_x \vec e_y = \vec e_z$ fixes the sign, so neither the factor nor the sign in the three vector images could have been otherwise. A reviewer must not "correct" the assignment by making the three images real, nor by negating all three. *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* derives both.

**Never conjugate the matrix entries on their own.** Conjugating the entries of $\mathsf{M}_2(\tilde{Q})$ is *not* the image of any involution of the algebra: it negates the images of $\vec e_x$ and $\vec e_z$ while leaving $\mathsf{M}_2(\vec e_y)$, which has real entries, untouched, and so it destroys the sector dictionary. The four conjugations $\natural$, $\bar{\phantom{Q}}$, ${}^{*}$ and $\flat$ are evaluated through the matrix formulas recorded in *The Element and Operator Representations*, never by conjugating entries.

**The realisation is a convention of presentation, not of content.** The isomorphisms that preserve the subspace dictionary are the $\mathsf{M}_{2,\mathrm{S}} = S\mathsf{M}_2 S^{-1}$ with $S$ unitary up to a nonzero complex scalar, and an arbitrary invertible $S$ destroys the dictionary. The practical consequence is that a mistake of translation between the algebra and its matrices is repaired **here** — by correcting the assignment or the explicit factors of $i$ — and never by altering the biquaternion norm, the $ict'$ assignment or the sector split.

**A bare $\mathsf{M}_2$ means this isomorphism and nothing else.** A plain $\mathsf{M}_2$, with no subscript, superscript or tilde, is reserved throughout the series for this isomorphism alone. The other uses a reader may meet are marked differently: $\varphi$ is an abstract homomorphism on the mathematics pages and an angle in the Thomas-precession exercise, $\tilde{\Phi} = \varphi\,e_t$ is the central scalar field of the Higgs articles, and $\Phi_{\tilde{U}}$ is the quantum channel of the gates article. None of these is the isomorphism, and a bare $\mathsf{M}_2$ is not any of them.

## The Operators

**An operator acting by multiplication is the element it multiplies by.** Every element acts on the algebra, on the left $L_{\tilde Q}$ or on the right $R_{\tilde Q}$, and an operator whose letter is the letter of an element **is** that element. The glyph of the operator is therefore the glyph of its element, and the marks are read on it as on the element: the tilde marks the quaternionic element read with its scalar part, the arrow the pure element read on its vector part alone. Neither mark says that a glyph is an operator, and no mark is added to say it.

**The named operators.** The structural operators take an upright capital letter and carry the element in the subscript, where it keeps its own mark:

| Operator | Glyph |
|---|---|
| left multiplication | $L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2$ |
| right multiplication | $R_{\tilde Q_1}(\tilde Q_2)=\tilde Q_2\tilde Q_1$ |
| two-sided | $L_{\tilde Q_4}R_{\tilde Q_1}(\tilde Q_2)=\tilde Q_4\tilde Q_2\tilde Q_1$ |
| sandwich | $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=\operatorname{H}_{\tilde Q}$ |
| inner derivation | $\operatorname{ad}_{\tilde Q_4}(\tilde Q_1)=[\tilde Q_4,\tilde Q_1]$ |
| automorphism | $\operatorname{Ad}_{\tilde Q_4}$ |

The tilde sits in the subscript because it belongs to the element, not to the operator: $L_{\tilde Q}$ is an operator, $\tilde Q$ is the element that generates it.

**The two marks on a glyph that is also an operator.** An operator read through its element follows the element rule in full.

- A glyph read with its scalar part, four components: the tilde. The canonical momentum $\tilde p=p_te_t+\vec p$, the Legendre conjugate of $\tilde q$; the biquaternionic gradient $\tilde\nabla$ of §*The Gradient*; the gauge-covariant derivative $\tilde D$.
- A pure glyph, three components: the arrow. The momentum operator $\vec p=-i\hbar\nabla=\vec e_kp_k$.

The gradient decides the case cleanly: $\tilde\nabla$ is not pure, because its $e_t$ term carries $\partial/\partial Q_t$, while $\nabla=\vec e_k\,\partial/\partial Q_k$ is pure and keeps the fixed glyph of §*The Gradient*, which carries no second mark.

**The case follows the layer.** The arrow does not change the case: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$. Where the letter already names another object of the layer, a subscript fixes the operator, $\vec P_{\mathrm{op}}$, or the explicit form $-i\hbar\vec\nabla$ is used. The three-momentum and the momentum operator share $\vec p$, as an eigenvalue and its operator do.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the natural sign for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves, so $\vec p^{\dagger}$ is again a pure operator; the tilde states a glyph read with its scalar part, which the adjoint also preserves, so $\tilde\nabla$ keeps its tilde. Where the adjoint in view is the one of the definite form and the operator carries no derivative, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$. A derivative separates them: its dagger is the adjoint and carries the integration by parts, its star conjugates the units alone (§*The Gradient*); the series writes $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ for the star.

**A Kraus operator is an element, not an array.** The Kraus operators of a channel or an instrument multiply the state on both sides, $\Phi(\tilde{Ϛ})=\sum_l\tilde K_l\tilde{Ϛ}\tilde K_l^{*}$, so each $\tilde K_l$ is an element of $\mathbb{B}$ and carries the tilde of the element. It is not a matrix, and the ban on a tilde on an array does not apply to it. Where the same operator is read as an array, that array is its image $\mathsf{M}_2(\tilde K_l)$, which carries no tilde, and its adjoint is the dagger, $\mathsf{M}_2(\tilde K_l)^{\dagger}=\mathsf{M}_2(\tilde K_l^{*})$; the corpus does not use that reading, and the star on the element is not a matrix adjoint.

**The Fock exception.** A Fock operator is not an element of the algebra; its superscript $\mathrm{fop}$ and the order of the two marks are fixed in §*The Superscripts*.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm r}$; it never denotes a derivative. The derivative with respect to a coordinate is written $\partial/\partial Q_\mu$, and in a fixed direction $\partial/\partial Q_t$, $\partial/\partial Q_x$, $\partial/\partial Q_y$ or $\partial/\partial Q_z$; a coordinate is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception, neither on a free index nor on any other.

**The coordinate derivative is unhalved.** It is defined by

$$
\frac{\partial}{\partial Q_\mu}:=\frac{\partial}{\partial q_\mu}+\frac{\partial}{\partial(iq'_\mu)},\qquad Q_\mu=q_\mu+iq'_\mu,
$$

the $i$ being glued to the primed coordinate: the derivative is taken with respect to the product $iq'_\mu$, not with respect to $q'_\mu$ with the $i$ pulled out in front. It is the formal derivative on the complex coordinate; with $Q_\mu$ and $\bar Q_\mu$ read as independent, its unhalved normalization gives $\partial Q_\mu/\partial Q_\mu=2$ and $\partial Q_\mu/\partial\bar Q_\mu=0$. On a real sector, where the fields depend on the tangential coordinate alone, the normal derivative is absent; on the material sector, with $Q_t=ict'$, the symbol is read with the tangential derivative alone, $\partial/\partial Q_t=-(i/c)\,\partial/\partial t'$, the reading that reproduces the kinetic term of §*The Hermitian Product, Its Form and Its Norm*; a derivative carrying a numerical factor would rescale that term. The conjugate derivative is

$$
\frac{\partial}{\partial\bar Q_\mu}:=\frac{\partial}{\partial q_\mu}-\frac{\partial}{\partial(iq'_\mu)},
$$

with $\partial\bar Q_\mu/\partial\bar Q_\mu=2$.

A derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the Lagrangian derivative puts the function in the numerator, $\partial L/\partial u$, so that where a PDE text writes $L_u$ and $L_p$ the corpus writes $\partial L/\partial u$ and $\partial L/\partial p$; the second derivative has the same shape, $\partial^2 L/\partial u^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the operand is a compound expression rather than a single letter. The time derivative $\partial/\partial Q_t$ is the imaginary-time derivative, and the material time derivative is written out as $\partial/\partial t'$. The rule holds on every object of the series, whether the letter names an element of the algebra, an element-valued field, a kernel or an operator.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.**

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dt'}$ for time, $\frac{d}{d\tau}$ for proper time, $\frac{d}{dt'_r}$ for retarded time; inline, the same derivative is written $dq/dt'$. The partial derivative is written $\frac{\partial}{\partial t'}$ or, inline, $\partial/\partial t'$. A higher derivative is written $\frac{d^2}{d{t'}^2}$, $\frac{\partial^2}{\partial {t'}^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{dx}{dt'}\right)^2$, never as $\frac{dx^2}{dt'}$.

**The prime marks the imaginary part, and nothing else.** The prime belongs to a coefficient: it marks the imaginary part of a complex number, $q'_\mu$ of $Q_\mu = q_\mu + iq'_\mu$, the part that carries the $i$. It is not a derivative mark, and it is not a label of an element, a field or a coupling. A derivative is written with $d$ or $\partial$ and its variable named: a function of one variable is differentiated as $df/dx$, never as $f'$, and a second derivative as $d^2f/dx^2$ or $\partial^2f/\partial x^2$, never with a repeated prime or a repeated subscript. The complex time is $Q_t = c(t+it')$: its real part $ct$ is the informational time and its imaginary part $ct'$ the material time, with $q_t = ct$ and $q'_t = ct'$. The prime on $t'$ marks the coefficient that carries the $i$, exactly as the primes on $x',y',z'$ mark the imaginary spatial coefficients.

**The prime is not a frame, source or field label.** The primed spatial coordinates $x',y',z'$ are the imaginary parts of the spatial coefficients, $Q_x=x+ix'$, $Q_y=y+iy'$, $Q_z=z+iz'$, with $(q'_x,q'_y,q'_z)=(x',y',z')$; the prime names the coordinate that carries the $i$. The primed time $t'$ is the imaginary part of $Q_t=c(t+it')$, with $q'_t=ct'$; the unprimed time $t$ is its real part, with $q_t=ct$. Outside these uses the prime is not written. A transformed frame is named by a subscript, never by $x'$ or $t'$; a source point, a second point and an integration variable take a numeric or role subscript, never a prime; an element, field, connection, curvature, current, state, coupling, group or map that is transformed or distinguished takes a numeric or role subscript, never a prime; and a derivative is written $df/dx$, never $f'$. The glyph $x'$ cannot be both the imaginary coordinate and a source or boosted coordinate: where both are needed, the source point or the frame takes the subscript.

**Labels that are not derivatives.** The second Lorentz label is written $\bar l$, and a spinor index of the conjugate representation is written $\bar\alpha$; the bar on an index marks the conjugate spinor. The conjugate matrix is $\bar\Pi$. These are labels, not derivatives.

**The scope mark.** In geometric calculus the factor differentiated is marked with an underline, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$, not with a dot.

**The two derivative operators of the series** are the **biquaternionic gradient** $\tilde\nabla$ and the **d'Alembertian** $\Box$; every other partial derivative is written with $\partial$.

### The Gradient

The coordinate derivative is written $\partial/\partial Q_\mu$ and is defined by $\partial/\partial Q_\mu:=\partial/\partial q_\mu+\partial/\partial(iq'_\mu)$, with $Q_\mu=q_\mu+iq'_\mu$, as fixed in §*Conventions for Derivation*. The **biquaternionic gradient** is the element-valued operator

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu}=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z},
$$

whose tilde marks its scalar part beside its vector part, with its **quaternion conjugate**, the involution of the norm,

$$
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu}
=e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z},
\qquad \varepsilon=(1,-1,-1,-1).
$$

It is this conjugate and no other that the series composes with (*Biquaternion Analysis*, §*The Biquaternionic Gradient*, §*The Quaternion Conjugate of the Gradient*). Write $\nabla=\sum_k\vec e_k\,\partial/\partial Q_k$ for the spatial gradient, with divergence $\nabla\cdot\vec Q_{\mathrm f}$ and curl $\nabla\times\vec Q_{\mathrm f}$, and $\Delta_Q=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$ for the Laplacian in the three vector coordinates.

**The conjugates of the gradient.** The gradient is an operator, and the marks are read on its units at fixed coordinate: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial Q_\mu$ is real; the unhalved derivative of §*Conventions for Derivation* is complex, and on an element-valued field the star is coefficientwise, carried through the derivative by $\partial/\partial\bar Q_\mu$ rather than by $\partial/\partial Q_\mu$. Read on the units, the quaternion conjugation reverses the three spatial units, and so does the Hermitian conjugation, so the two act on the gradient alike,

$$
\tilde\nabla^{*}=\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad \overline{\tilde\nabla}=\tilde\nabla .
$$

**The forms stay four, the norms are two.** The four forms of §*The Involutions and the Four Forms* remain four distinct conventions here, because each conjugates its own slot: the quaternionic form conjugates the first argument and the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm, $\langle\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{\natural}$, and the Krein norm with the plain bilinear norm, $\langle\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle$. The four subsections below carry the four forms, and their norms are the two operators $\Box$ and $\partial^2/\partial Q_t^2-\Delta_Q$.

**On the material sector $\mathbb{M}_-$**, where $Q_t=ict'$ and $Q_k=q_k$, the time derivative reads $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t'$, the Laplacian is the physical $\Delta$, and the gradient is

$$
\tilde\nabla\big|_{\mathbb{M}_-}=-\frac{i}{c}\,e_t\frac{\partial}{\partial t'}+\sum_k\vec e_k\frac{\partial}{\partial Q_k}.
$$

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four of §*The Twelve Products and Their Names*. On the gradient, with an element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j \vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit,

$$
\tilde\nabla\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$, with $\tilde J=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **On the material sector** the same product is read with $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t'$, the space part being unchanged.

**The symmetric and antisymmetric parts.** Read with two arguments, the product splits as in §*The Twelve Products and Their Names*. The half-sum keeps the form as its scalar part,

$$
\tilde\nabla\bullet\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-(\nabla,\vec Q_{\mathrm f})\Bigr]e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+Q_{\mathrm{f}t}\nabla=\Bigl[\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr]e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t} ,
$$

and the half-difference is the curl,

$$
\tilde\nabla\wedge\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}\tilde\nabla\bigr)=\tfrac12\bigl(\nabla\times\vec Q_{\mathrm f}+\nabla\times\vec Q_{\mathrm f}\bigr)=\nabla\times\vec Q_{\mathrm f} ,
$$

a pure vector, so the plain form carries the whole scalar content of the product. Throughout these four subsections the pair $(\nabla,\vec X)$ is read as the divergence $\nabla\cdot\vec X$ and $X\nabla$ as the gradient $\nabla X$, the derivative acting on the coefficient it multiplies, and the coordinate formulas substituted are those of §*The Twelve Products and Their Names*.

**The form.** The **plain form** is the scalar part of the product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial}{\partial Q_\mu}Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f} ,
$$

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$. **On the material sector** it is $-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial t'}-\nabla\cdot\vec Q_{\mathrm f}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla\rangle=\langle\tilde\nabla,\tilde\nabla\rangle=\mathrm{Sc}(\tilde\nabla\tilde\nabla)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

the cross terms cancelling. **On the material sector** it is $-c^{-2}\frac{\partial^2}{\partial {t'}^2}-\Delta$, which is neither the wave operator $\partial^2/\partial {t'}^2-c^2\Delta$ nor the series' d'Alembertian; on this sector the d'Alembertian is $\Delta-c^{-2}\partial^2/\partial {t'}^2$ (§*The Quaternionic Bilinear Product, Its Form and Its Norm*).

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four of §*The Twelve Products and Their Names*; on the gradient it is $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**On the material sector** the same substitution $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t'$ applies.

**The symmetric and antisymmetric parts.** The half-sum is central and is the quaternionic form itself,

$$
\tilde\nabla\bullet_{\natural}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}^{\natural}\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+(\nabla,\vec Q_{\mathrm f})\Bigr]e_t=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t ,
$$

and the half-difference is the vector part of the product,

$$
\tilde\nabla\wedge_{\natural}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}^{\natural}\tilde\nabla\bigr)=\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-Q_{\mathrm{f}t}\nabla-\nabla\times\vec Q_{\mathrm f}=\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**The form.** The **quaternionic form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde Q_{\mathrm f})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial Q_\mu}Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f} ,
$$

a scalar, the **contraction** of the derivative with the field in the $ict'$ metric. It differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed. **On the material sector** it is $-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial t'}+\nabla\cdot\vec Q_{\mathrm f}$.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal arguments, and the two orders of the product agree:

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\langle\tilde\nabla,\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, an operator on the whole algebra, one and the same before any sector is named (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*). The coordinates $Q_\mu$ are those of the algebra and are complex in general; the operator is $\partial^2/\partial Q_t^2+\Delta_Q$ whatever the sector, and it is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box\tilde Q_{\mathrm f}=\sum_\mu(\Box Q_{\mathrm{f}\mu})e_\mu$. It is the identity above, and not the $ict'$ substitution, that fixes it, and **no article of the series defines a second d'Alembertian**; no mass-term sign is left to a local convention.

**The special case of the material sector.** On $\mathbb{M}_-$ the coordinates are the material ones, $Q_t=ict'$ and $Q_k=q_k$, and the $ict'$ substitution flips the sign of the time second derivative, $\partial^2/\partial Q_t^2=-c^{-2}\,\partial^2/\partial {t'}^2$, so the same operator reads

$$
\Box\big|_{\mathbb{M}_-}=\frac{\partial^2}{\partial Q_t^2}+\Delta=\Delta-c^{-2}\,\frac{\partial^2}{\partial {t'}^2},
$$

a plus on the spatial part and a minus on the time part. On $\mathbb{M}_-$, where the series does its work, this reading is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series. **The $ict'$ substitution is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial Q_t^2+\Delta_Q$; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. The operator is one, and every article writes it the same way.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four of §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is central and is the Hermitian form itself,

$$
\tilde\nabla\bullet_{*}\tilde Q_{\mathrm f}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=\Bigl[\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t ,
$$

and the half-difference is the vector part,

$$
\tilde\nabla\wedge_{*}\tilde Q_{\mathrm f}=\mathrm{Vect}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\bar Q_{\mathrm{f}t}\nabla-\nabla\times\overline{\vec Q_{\mathrm f}}=-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The form.** The **Hermitian form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial Q_\mu}\bar Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}} ,
$$

a scalar, the **contraction** of the derivative with the **conjugated** field in the sign vector $\varepsilon$. Taken on the scalar field it gives the **kinetic density**, the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial\Phi^{*}}{\partial Q_\mu}\frac{\partial\Phi}{\partial Q_\mu} ,
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two time derivatives are imaginary on the material sector, so that scalar part is $-c^{-2}\lvert\partial\phi/\partial t'\rvert^2+\lvert\nabla\phi\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L_{\mathrm{kin}}=-\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\frac{1}{c^2}\Bigl|\frac{\partial\phi}{\partial t'}\Bigr|^2-\lvert\nabla\phi\rvert^2 ,
$$

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the material sector** the form itself is $-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial t'}+\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q=\Box ,
$$

so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four**, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert_E$; positivity is a property of the elements, the norm of this subsection being the operator $\Box$. **On the material sector** it is the same operator, $\Box|_{\mathbb{M}_-}=\Delta-c^{-2}\,\partial^2/\partial {t'}^2$.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four of §*The Twelve Products and Their Names*; it is the conjugate derivative applied to the conjugated field, $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}$, the companion of the quaternionic bilinear product in the second slot,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}-\nabla\bar Q_{\mathrm{f}t}+\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is

$$
\tilde\nabla\bullet_{\natural*}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}+\tilde Q_{\mathrm f}^{*}\tilde\nabla^{\natural}\bigr)=\Bigl[\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}-\bar Q_{\mathrm{f}t}\nabla=\Bigl[\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr]e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}-\nabla\bar Q_{\mathrm{f}t} ,
$$

whose scalar part is the Krein form, and the half-difference is the curl of the conjugated field,

$$
\tilde\nabla\wedge_{\natural*}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}-\tilde Q_{\mathrm f}^{*}\tilde\nabla^{\natural}\bigr)=\tfrac12\bigl(\nabla\times\overline{\vec Q_{\mathrm f}}+\nabla\times\overline{\vec Q_{\mathrm f}}\bigr)=\nabla\times\overline{\vec Q_{\mathrm f}} ,
$$

a pure vector.

**The form.** The **Krein form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial}{\partial Q_\mu}\bar Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}} ,
$$

a scalar, the **contraction** of the conjugate derivative with the conjugated field in the $ict'$ metric. **On the material sector** it is $-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial t'}-\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form, and on the elements it is the form of signature $(1,3)$ whose diagonal is $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$: Hermitian, and negative on a nonzero element, so it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these subsections. **On the material sector** it is $-c^{-2}\frac{\partial^2}{\partial {t'}^2}-\Delta$.

**A contraction is a form, never an index.** The metric of the series is the sign vector $\varepsilon$ inside the product, so no index is raised and none is lowered. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla\rangle_{\natural}=\Box$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the metric being the sign vector inside the product.

## Physical Units

**A unit element is not a physical unit.** The base $e_t,\vec e_x,\vec e_y,\vec e_z$ of §*The Base and Its Units* is algebraic: its structure constants are $0$ or $\pm1$, and the biquaternion norm is a sum of four squares of coefficients. No element of $\mathbb{B}$ carries a metre, a second or a kilogram. A physical unit enters only where an element is **identified** with a physical quantity, and that identification is a convention of the article that makes it, not a property of the algebra. The phrase *unit element* names a basis element and *physical unit* names a convention of measurement; the two are never exchanged.

**The series uses the SI.** Length is measured in metres, time in seconds, mass in kilograms, temperature in kelvin and charge in coulomb. The derived units follow from these, and the ones the articles use are collected here.

| Quantity | Symbol | Unit |
|---|---|---|
| Length | $x,y,z$; $ict'$ in the length coordinate | metre ($\mathrm{m}$) |
| Time | $t'$ in the time coordinate | second ($\mathrm{s}$) |
| Mass | $m$ | kilogram ($\mathrm{kg}$) |
| Temperature | $T$ | kelvin ($\mathrm{K}$) |
| Electric charge | $ϙ$ | coulomb ($\mathrm{C}$) |
| Speed | $c$, $c_0$ | $\mathrm{m\,s^{-1}}$ |
| Momentum | $\vec p$ | $\mathrm{kg\,m\,s^{-1}}$ |
| Energy | $E$ | joule ($\mathrm{J}$) |
| Action, angular momentum, spin | $S$, $S_0$, $I_\mu$, $\theta$, $\vec L$, $\tilde S_3$ | joule-second ($\mathrm{J\,s}$) |
| Metric coefficient, time writing | $g_{tt}=-c^2$ | $\mathrm{m^2\,s^{-2}}$ |
| Inverse length | $\mu=mc/\hbar$ | $\mathrm{m^{-1}}$ |
| Inverse temperature | $\beta=\hbar/(k_BT)$ | second ($\mathrm{s}$) |
| Planck constants | $h$, $\hbar$ | joule-second ($\mathrm{J\,s}$) |
| Boltzmann constant | $k_B$ | $\mathrm{J\,K^{-1}}$ |
| Gravitational constant | $G$ | $\mathrm{m^3\,kg^{-1}\,s^{-2}}$ |
| Permittivity and permeability | $\epsilon$, $\mu$ | $\mathrm{F\,m^{-1}}$, $\mathrm{H\,m^{-1}}$ |

**The coefficients of one element share one unit.** The biquaternion norm is a sum of four squares of the coefficients of a single element, so the four terms are commensurable only if the four coefficients carry the same unit. The requirement is per element and not across elements: the coefficients of a four-displacement are lengths and its norm a length squared, the coefficients of a four-velocity are speeds and its norm a speed squared, and the temporal slot of a four-potential carries $\phi/c$ rather than $\phi$ so that its four components share the unit of the vector potential. The unit is the unit of the quantity the element represents, and it is supplied by the identification.

**The two writings of the temporal slot.** In the length coordinate the material position is $\tilde R = ict'\,e_t+\vec q$, with time measured in metres; this is the corpus's default. In the time coordinate the temporal component is $it'$, time stays in seconds, and the conversion is carried by the metric coefficient $g_{tt}=-c^2$. The quadratic form is one and the same, $\langle\tilde R\rangle_{\natural}=-c^2{t'}^2+x^2+y^2+z^2$; the two differ only in where the factor $c$ is written, and an article that uses the second states it where the temporal slot is read.

**Dimensionless and dimensionful.** A pure number — the fine-structure constant $\alpha$, the ratio $g=2$, the phase $S/\hbar$, the trace normalisation $2$ — carries no unit and no conversion. A dimensionful constant is a unit conversion and is written with its unit. No dimensionful constant is derived by the algebra: $c$, $\hbar$, $k_B$, $G$, $m$ and $ϙ$ are inserted at the places where the structure requires a scale. The metrology says the same thing from the other side. Since the 2019 revision the SI fixes $c$, $h$, the elementary charge and $k_B$ by definition and realises the units from them, while a dimensionless constant such as $\alpha$ has to be measured. An article that sets a constant to one — $c=1$, $\hbar=1$ or $G=1$ — says so locally, and the constant returns wherever a dimensional statement is at issue.

**A caution on $\mu$.** The letter $\mu$ names the permeability in $c=1/\sqrt{\epsilon\mu}$ and the inverse Compton length in $\mu=mc/\hbar$, and it is the direction label in $e_\mu$ and $Q_\mu$. The corpus distinguishes the uses by context; an article should not use two of them in one expression.

## The Superscripts

Two superscript tokens run beside the marks of the elements and the marks of the conjugations, and neither is to be read for the other:

| Token | Written on | Meaning |
|---|---|---|
| $^{\mathrm{fop}}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $^{\mathrm{opp}}$ | an algebra name | the opposite algebra, the algebra with the reversed product |

**The mark, and its one use.** The marks of the elements say what a glyph **is**, not that it is an **operator** (§*The Operators*). The single exception is the **Fock layer**, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the upright superscript $\mathrm{fop}$, set on the glyph and read as part of it:

$$
a^{\mathrm{fop}},\quad b^{\mathrm{fop}},\quad a^{\mathrm{fop}\dagger},\quad b^{\mathrm{fop}\dagger},\quad \psi^{\mathrm{fop}},\quad N^{\mathrm{fop}},\quad H^{\mathrm{fop}},\quad F^{\mathrm{fop}},\quad Ϙ^{\mathrm{fop}},\quad U^{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p=-i\hbar\nabla$ keeps its element glyph and never takes the Fock mark, the quadratures $x$ and $p$ of the oscillator are written $x$ and $p$, the spin $S_k=\tfrac{\hbar}{2}\sigma_k$ is written $S_k$, and the parity, charge-conjugation and time-reversal maps $P$, $C$ and $T$ carry no mark. Where a ladder is meant as an element of the algebra it is written with the element's glyph, the truncated pair $\vec\Upsilon_1,\vec\Upsilon_2$, and the abstract ladder operator keeps the mark, $a^{\mathrm{fop}}$.

**It combines with the dagger, the mark first.** The dagger is the general adjoint (§*The Operators*); the superscript marks the Fock operator. Where both are written on the same glyph, the Fock mark comes first and the adjoint follows, $(a^{\mathrm{fop}})^{\dagger}$, contracted to $a^{\mathrm{fop}\dagger}$. The dagger alone never says that its glyph is an operator, and the superscript alone never says that the Fock operator is self-adjoint; the two are read together, so that $a^{\mathrm{fop}\dagger}$ is the adjoint of the ladder and $N^{\mathrm{fop}}$ is written without an adjoint because it is self-adjoint.

**The opposite algebra carries a different token.** The reversed-product algebra is written with the superscript $\mathrm{opp}$, $\mathbb{B}^{\mathrm{opp}}$, $A^{\mathrm{opp}}$, $M_n(D)^{\mathrm{opp}}$, on an **algebra name**, where the Fock mark is written on a **Fock-operator glyph**. The two tokens are distinct and neither is read for the other: $a^{\mathrm{fop}}$ is never an opposite algebra, and $\mathbb{B}^{\mathrm{opp}}$ is never an operator.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}_{\mathrm{r}}$, because a bare underscore would take the first character alone.

**A subscript is never a partial derivative.** The subscript marks a component or a label, a partial derivative is written with $\partial$, and the rule is fixed in §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the general elements, the units, the roots, the idempotents and the nilpotents alike: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}_{\mathrm{r}}$ and $\tilde U_{\mathrm r}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$. In the reduced biquaternion layer the sign belongs to the idempotent pair and to its coordinates, $\Pi_\pm$, $Q_{+}$ and $Q_{-}$, the two basis coordinates carrying the triangles, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and a numbered element putting its number first in either case, $Q_{1+}$ and $Q_{1\blacktriangle}$; the element they build is $\breve Q$. The sign is read with the glyph: $\tilde Q_\pm$ names an element of the sector $\mathbb{M}_\pm$, while $Q_\pm$ names the idempotent coordinates of $\breve Q$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $\tilde\Pi_\pm$ |
| an upright word | $\mathbb{B}_{\mathrm{r}}$, $\tilde U_{\mathrm r}$ |
| a grouped expression | $Q_{n+1}$ |

## Summary

The conventions of the series are one object read in order, from the object itself to the two clauses a field equation inherits.

**The object and its parts.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_k^2 = -e_t$, over complex coefficients. The scalar unit $i$ is central, which is what makes the central phase the algebra's continuous symmetry, and multiplication by it is one map whose restrictions are the global phase and the exchanges and duality rotations of the sectors (§*The Central Map and Its Restrictions*). The conjugations cut the algebra into the remarkable subspaces of §*The Remarkable Subspaces*, each carrying its own real parameters and its slice of the coordinate dictionary, with $q'_t = ct'$, $q_t = ct$, $(q_x,q_y,q_z) = (x,y,z)$ and $(q'_x,q'_y,q'_z) = (x',y',z')$. The elements with no scalar part — the vector subspace — are the **pure elements**, written with the arrow and without the tilde, $\vec{Q}$ (§*Pure Elements and their Coefficients*). The algebra carries four forms, not two — the plain form, the quaternionic form, the Hermitian form and the Krein form — read on the diagonal as the four norms, of which the quaternionic norm is the biquaternion norm. The matrix representation $\mathsf{M}_2$ is fixed by its four basis images, with the Hermitian units following as $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$; the residual freedom is a unitary change of basis of $\mathbb{C}^2$ and nothing further, so the sector dictionary cannot be altered by re-choosing it.

**The presentations, the gradient and the metric levels.** The algebra is written in three presentations — the coefficient quadruple, the $4\times4$ regular matrix and the $2\times2$ image $\mathsf{M}_2$ — each developed in its own article, and it is the trace of $\mathsf{M}_2$ that the series calls the trace. The material coordinate is $\tilde{R} = ict'\,e_t + \vec q$, using the $ict'$ convention so that the Minkowski interval is the biquaternion norm, vanishing on the zero-divisor cone. The series d'Alembertian is $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta_Q$, read on the material sector as $\partial^2/\partial Q_t^2 + \Delta = \Delta - c^{-2}\,\partial^2/\partial {t'}^2$; every article uses this one operator, with the mass equation $\left(\Box - m^2c^2/\hbar^2\right)\psi = 0$. The algebra's real structure is $\flat = -{}^{*}$ — a sign derived from the star, not an independent involution, and fixed on the material sector — and the mass term built on $\flat$ and then retired, with the dispersion that retired it, is recorded in *The Dirac Equation in Biquaternionic Form* and *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*. Physical units are the SI, and the two writings of the temporal slot — $ict'$ in metres and $it'$ with $g_{tt} = -c^2$ — are stated where an article uses the second. The three levels of the word *metric* are set out in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, and the tool is never a reason to change a convention of the framework.

The theme is single. In a framework whose algebra and sector assignment are non-standard, the most likely error is a correction of something that is deliberate. The conventions recorded above are the places where that is most likely to happen.

## Summary of Notation

The tilde-marked element glyphs are collected in §*The Most Common Quaternions and Biquaternions*; the table below holds the structures and the physical quantities built on the algebra.

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde Q_{\log}$ | A logarithm of $\tilde Q$, a solution of $\exp(\tilde Q_{\log}) = \tilde Q$ (see §*The Elements and their Coefficients*); the quaternion layers write $\tilde q_{\log}$, the reduced biquaternion layer $\breve Q_{\log}$, and the complex, split-complex and dual layers $Q_{\log}$ |
| $\vec Q$ | The vector part of an element, $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$, and a pure element of the biquaternion layer read on its own, $\mathrm{Sc}(\vec Q) = 0$, the vector subspace $\mathrm{Vect}(\mathbb{B})$ (see §*The Elements and their Coefficients* and §*Pure Elements and their Coefficients*) |
| $\vec q$ | **Position; pure quaternion.** The spatial part of the material coordinate: the vector part of the full generic element $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$, read at the material values, $\tilde R = ict'\,e_t + \vec q$; as an element of the quaternion layer with no scalar part, $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ (see §*Pure Elements and their Coefficients*) |
| $\vec u$ | A unit pure quaternion, the axis of a rotation |
| $\vec U$ | A unit pure biquaternion, of norm one |
| $\vec\Xi$ | A pure root of $1$ of the biquaternion layer |
| $\vec\Upsilon$ | A pure nilpotent of the biquaternion layer |
| $\Pi_\pm$ | An idempotent of the reduced biquaternion layer, the plain glyph of the mathematical corpus |
| $\Xi_\pm$ | A root of $1$ of the reduced biquaternion layer, the plain glyph of the mathematical corpus |
| $\flat = -{}^{*}$ | The anti-Hermitian conjugation, the algebra's real structure: a sign derived from the star, not an independent involution; its fixed space is $\mathbb{M}_-$, the material sector |
| $ϙ$ | The electric charge, the minuscule of the archaic qoppa; a physical quantity, not an element of the algebra (U+03D9) |
| $Ϙ$ | A total charge, or a charge operator, the majuscule of the archaic qoppa; the chiral charges are $ϙ_L, ϙ_R$ and the charge operator of a chiral module is $Ϙ = ϙ_LP_L + ϙ_RP_R$ (U+03D8) |
| $m$ | **Mass.** The rest mass, as in the mass equation $(\Box - m^2c^2/\hbar^2)\psi = 0$; not the signature index $m$ below, which occurs only inside $\mathrm{Cl}_{n,m}$ and $O(n,m)$ |
| $\pi$ | **The circle constant.** The number; not the idempotent, which is written $\tilde\Pi$ |
| $\hbar$ | **Reduced Planck constant.** Turns the action into the phase $\exp(iS/\hbar)$, and the mass into a wavenumber |
| $c$ | **Speed of light.** Enters through the material time, $\tilde R = ict'\,e_t + \vec q$ |
| $E$ | **Energy.** The energy of a particle or of a normal mode |
| $\vec p$ | **Three-momentum.** The three-momentum $\vec p$; the four-momentum $\tilde P = m\tilde V$ is an element of the algebra, collected in §*The Most Common Quaternions and Biquaternions* |
| $\phi$, $\vec A$ | **Scalar and vector potential.** The electromagnetic potential of the minimal-coupling articles |
| $\vec N$ | **Riemann–Silberstein vector.** The complex field vector $\vec N = \vec E + ic\vec B$ of the electromagnetic articles; its letter is not that of a velocity, and a velocity is never written $\vec N$ |
| $S$ | **Action.** The exponent of the central phase and the classical action of the stationary-phase articles |
| $g_{\mathrm W}$, $g_{\mathrm Y}$ | **Gauge couplings.** The weak coupling $g_{\mathrm W}$ of $SU(2)_L$ and the hypercharge coupling $g_{\mathrm Y}$ of $U(1)_Y$, the hypercharge field being $B_\mu$; not the Clifford metric $g_{\mu\nu}$ below; the framework's own coupling is $\kappa$ |
| $\kappa$ | **Framework coupling.** $\kappa = ϙ/\hbar$, the coefficient of the biquaternionic covariant derivative |
| $\theta_W$ | **Weak mixing angle.** The rotation that separates the photon from the $Z$ |
| $k_B$, $\beta$ | **Boltzmann constant and inverse temperature.** $\beta = \hbar/(k_BT)$, the corpus convention with $\hbar$ retained |
| $\mathfrak{Z}$ | **Atomic number, nuclear charge number.** The number of elementary charges of the nucleus, the nuclear charge being $\mathfrak{Z}ϙ$; the plain $Z$ is the $Z$ boson, $\mathbb{Z}$ the integers and $\mathcal{Z}$ the light-cone set |
| $\mathcal{Q}_{lm}$, $\mathcal{Q}_{ij}$ | **Multipole moments, quadrupole.** The charge moments of the multipole articles, spherical and Cartesian; not the generic element $\tilde Q$ |
| $\mathcal{Q}$ | **Heat; supercharge, BRST charge.** The heat of the thermodynamic articles, as in $\mathcal{Q} = T\,\Delta S$; and the odd generator of the supersymmetry and BRST articles, with $\{\mathcal{Q},\mathcal{Q}^\dagger\} = H$ and $\mathcal{Q}^2 = 0$. Two physical uses of the one calligraphic glyph, read by context |
| $\xi$, $\eta_{\mathrm{can}}$ | **Canonical coordinates.** The old and the new canonical variables of a transformation, and the transformation function $\langle \xi\vert \eta\rangle$; not the metric $\eta$ below |
| $k$ | **Mode momentum.** The integration momentum of a mode expansion, $\int d^3k$ |
| $k^\mu$, $\vec k$ | **Exchange momentum, momentum transfer.** The momentum carried by an exchanged boson at a vertex, or transferred in a scattering; the letter of a mode momentum, and never $q$, which belongs to the elements |
| $\zeta$ | **Quadratic Zeeman coupling.** The spin-1 coupling of the quadratic Zeeman term, $\zeta \propto B^2$ |
| $n$, $m$ | **Signature indices.** The counts of positive and negative directions, as in $\mathrm{Cl}_{n,m}$ and $O(n,m)$; the $m$ of a signature is an index, not the mass |
| $(ct)\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ | The informational coordinate, $x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z$; the temporal coefficient $ct$ is real and the spatial ones imaginary, the mirror of the material coordinate |
| $\mathbb{C}_{\mathbb{B}} = \{Q_t e_t\}$ | Centre subspace, fixed points of quaternion conjugation; the centre of $\mathbb{B}$ and the complex time sector; parameters $q_t, q'_t$ with $q_t = ct$ and $q'_t = ct'$ |
| $\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\}$ | The vector subspace, i.e. the complex space sector: anti-fixed points of quaternion conjugation, real dimension six; parameters $q_k, q'_k$ with $(q_k) = (x,y,z)$ and $(q'_k) = (x',y',z')$. The pure elements are these, written $\vec{Q}$ (§*Pure Elements and their Coefficients*). |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, i.e. the real sector (the real half): fixed points of complex conjugation, all four coefficients real |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion subspace, i.e. the imaginary sector (the imaginary half): anti-fixed points of complex conjugation, all four coefficients purely imaginary; not a subalgebra. $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, a split that crosses the $\mathbb{M}_\pm$ split |
| $\mathbb{M}_+ = \{ \tilde{Q} : \tilde{Q}^{*} = \tilde{Q} \}$ | Hermitian subspace, the informational sector; basis $e_t, i\vec e_x, i\vec e_y, i\vec e_z$, parameters $q_t, q'_x, q'_y, q'_z$ (real), with $q_t = ct$ |
| $\mathbb{M}_- = \{ \tilde{Q} : \tilde{Q}^\flat = \tilde{Q} \}$ | Anti-Hermitian subspace, the material sector; basis $ie_t, \vec e_x, \vec e_y, \vec e_z$, parameters $q'_t, q_x, q_y, q_z$ (real), with $q'_t = ct'$ |
| $N(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2$ | Biquaternion norm, written $N$, level 1 of the three levels of the word *metric* (§*The Metric: Three Levels* of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*) |
| $\mathrm{Form}(\tilde{Q}_1,\tilde{Q}_2)$, $\mathrm{Norm}(\tilde{Q})=\mathrm{Form}(\tilde{Q},\tilde{Q})$ | The generic form and the generic norm, instantiated one to a general product by the four forms and the four norms (§*The Four Algebraic Norms and the Unitary Convention*, §*The Involutions and the Four Forms*) |
| $P(\tilde{Q})$, $N(\tilde{Q})$, $H(\tilde{Q})$, $K(\tilde{Q})$ | The four algebraic norms in letters, the diagonals of the plain, the quaternionic, the Hermitian and the Krein form; each letter names the form with two arguments and the norm with one (§*The Four Algebraic Norms and the Unitary Convention*) |
| $\Phi$-regular, $\Phi$-degenerate | $\Phi(\tilde{Q})\neq0$ and $\Phi(\tilde{Q})=0$ for $\Phi\in\{P,N,H,K\}$; only the $N$ pair is the unit partition, and *regular* unqualified is spectral, $B^{2}\neq0$ (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*) |
| $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ | The twelve products, the four general products and their symmetric and antisymmetric parts (§*The Twelve Products and Their Names*) |
| $\tilde Q_1\bullet\tilde Q_2$ | The **symmetric product**, the half-sum $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$, the Jordan product for the plain slot; the subscripts ${}_{*}$, ${}_{\natural}$ and ${}_{\natural*}$ name the sesquilinear, quaternionic and quaternionic-sesquilinear slots (§*The Twelve Products and Their Names*) |
| $\tilde Q_1\wedge\tilde Q_2$ | The **antisymmetric product**, the half-difference $\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)$, the outer product for the plain slot, with the same subscripts. On differential forms the same glyph is the exterior product, $\alpha\wedge\beta$, a different use (§*The Twelve Products and Their Names*) |
| $\mathbb{B}_{\mathrm{r}}$, $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ | The reduced biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ on the basis $1, i, j, ij$, equivalently the tessarines or the double-complex numbers; its intrinsic conjugation is the tessarine sign ${}_{\mathrm{ts}}$, and the natural sign is not written on the layer; its two complex coordinates are $Q_{\blacktriangle} = q_{\blacktriangle} + iq'_{\blacktriangle}$ and $Q_{\blacktriangledown} = q_{\blacktriangledown} + iq'_{\blacktriangledown}$; the same twelve codes are registered on it and four collapse — $\mathrm{SPA} = \mathrm{GPA}$, $\mathrm{SQS} = \mathrm{GQS}$, $\mathrm{APA} = 0$, $\mathrm{AQS} = 0$ — leaving the eight structures GPA, GQA, GPS, GQS, SQA, AQA, SPS, APS (§*The Twelve Products and Their Names*) |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict'$-coordinate metric, signature $(-,+,+,+)$ (level 2) |
| $g_{\mu\nu}$, matrix $g$ | **Clifford metric** of the $\gamma^\mu$ (level 3), not the gauge coupling $g$ above; an optional tool, not a framework convention. The matrix is $(g_{\mu\nu}) = \mathrm{diag}(+1,-1,-1,-1)$ throughout — the $\mathbb{M}_+$ form, matching the objects the tool represents |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta_Q$ | The d'Alembertian, a scalar operator; on the material sector it reads $\partial^2/\partial Q_t^2 + \Delta = \Delta - c^{-2}\,\partial^2/\partial {t'}^2$, the series convention |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$, $\langle e_t\rangle_{*}=1$ | The Hermitian form, its norm and the unit: the probability pairing. A state is $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12$; the Born weight is $\langle\tilde{Ϛ},\tilde H\rangle_{*}/\langle\tilde{Ϛ},e_t\rangle_{*}$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle$ | The plain form and the plain norm: the restriction of the Hermitian form to $\mathbb{M}_+$ |
| $2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*})$, $2\,\mathrm{Sc}(\tilde Q)=\operatorname{Tr}(\tilde Q)$ | Trace reading of the Hermitian form in the $2\times2$ image, once and last |
| $\Rho,\Theta,\vec U,B,\psi,\psi_w$ | The Hamilton data of the polar word: $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ the complex modulus, $\Theta$ the complex angle, $\vec U$ the Hamilton axis, $B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}$ the length of the vector part; $\psi$ the kinematic rapidity and $\psi_w=2\psi$ the word parameter of a four-vector. A four-momentum reads $\Rho=imc$, $\Theta=-i\psi$, $\vec U=\hat p$, and its eigenvalues are $\Rho e^{\pm i\Theta}=imc\,e^{\pm\psi}$ |
| $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ | The matrix representation, with $\mathsf{M}_2(e_t) = I_2$ and $\mathsf{M}_2(\vec e_k)$ as given above; the Hermitian units follow as $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$. Fixed up to a unitary change of basis, and no further |
| $SL(2,\mathbb{C})$ | Unit-norm biquaternions, the Lorentz group on $\mathbb{M}_-$ |

## Further Reading

- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the original quaternion algebra and its units.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents, minimal left ideals, and the conjugations of a Clifford algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for real structures and real forms on Clifford algebras.
- [The Biquaternion Space, the Group of Involutions and the Six Subspaces](the-biquaternion-space-the-group-of-involutions-and-the-six-subspaces.html), companion article, for the relations among the subspaces defined here — their coordinate blocks, intersections, spans, gradings and biquaternion norms.
- [The Element and Operator Representations](the-element-and-operator-representations.html), companion article, for the coefficient space, the 2×2 and 4×4 matrix images, the determinant and the two chiralities.
