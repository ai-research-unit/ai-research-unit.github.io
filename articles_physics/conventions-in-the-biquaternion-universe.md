# __Conventions in the Biquaternion Universe__

## Introduction

A framework built on a non-standard algebra, and on a non-standard choice of which part of it counts as "real", is a framework in which a reader will repeatedly find things that look wrong and are not. Two examples fix the idea. The series takes the **anti**-Hermitian subspace as the material sector, where the more familiar convention would take the Hermitian one. And the series' d'Alembertian carries a sign opposite to the one used in the articles on Weyl spinors. In both cases it is the "correction" that is the error.

This article opens the conventions of the series. It states the conventions of the base: the algebra and its basis, the units, the element and its coefficients, the remarkable subspaces, the conjugations and the common glyphs. The conventions of the products and the forms, of the norms and the pairings, of the special elements, of the representations, of the operators and the calculus, and of the units, the indices and the notation are carried by the six companion articles of the category, in that order. The split follows the dependency order and introduces no new convention: each article states what it needs and cites the one before it, and together they hold what one article held before.

It states conventions only: the proofs, the properties and the physical interpretations of the objects it names belong to the articles cited beside them. It is meant to be read before any other article is edited, and its reader is anyone writing or revising an article of the series, for whom the conventions are load-bearing — a change that looks local, a sign or a factor of $i$, generally propagates into a dozen dependent articles.

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

and this identification is used constantly. It is fixed by a single isomorphism, written $\mathsf{M}_2$; its four basis images, and the rule that neither the factor $i$ nor the sign is a free choice, are stated in *Conventions of the Representations*, §*The 2×2 Matrix Representation*, and the development of the representation — the general element, the remarkable subspaces as matrices, the conjugations, the trace and the determinant — is in the companion article *The Element and Operator Representations*. Its two **Peirce carriers**, the minimal left ideals here, are the algebra's two chiralities; the spinor module and the mass term a field equation builds on that structure are the subject of *The Dirac Equation in Biquaternionic Form*.

## The Base and Its Units

The base is written with the letter $e$, one unit to a direction. The scalar unit is $e_t = 1$ and the three vector units are $\vec e_x, \vec e_y, \vec e_z$; the arrow is the only mark that separates the scalar unit from the vector units. **The three vector units are the quaternion units, the series' replacement for Hamilton's $i, j, k$.** A general element is written in the base,

$$
\tilde Q = Q_t e_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $e_\mu$ the unit of the direction $\mu$ — the arrowless $e_t$ at $\mu = t$ and the arrowed $\vec e_\mu$ at $\mu = x, y, z$. The three vector units close on the scalar unit and on one another,

$$
e_t = 1, \qquad \vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t , \qquad \vec e_x \vec e_y = -\vec e_y \vec e_x = \vec e_z ,
$$

and cyclically, the space index running over $k = x, y, z$. **The notation is the unit along the axis.** A coefficient carries the name of the direction it multiplies, as in $\vec v = v_x\hat x + v_y\hat y + v_z\hat z$ of the vector calculus: $Q_x$ is the coefficient of $\vec e_x$, the label on the unit names the direction and the label on the coefficient names the same direction, so $q_x = x$ reads without ambiguity. **The base letter is $e$ and the unit-element letter is $u$, and the two are never exchanged.** The base units carry $e$, so $e$ is not available for the exponential, which is written $\exp(\cdot)$; a unit element of a layer carries the glyph of the unit element, $\tilde u$ or $\tilde Q$ (§*The Unitary Convention*).

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
| $\mathbb{C}^2$ | Duo-complex numbers | $Q = (Q_{\blacktriangle}, Q_{\blacktriangledown})$ | $Q_{\blacktriangle}$, complex; $Q_{\blacktriangledown}$, complex | — |
| $\mathbb{B}_{\mathrm{r}}$ | Reduced biquaternions | $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ | $Q_{\blacktriangle}$, complex; $Q_{\blacktriangledown}$, complex | — |
| $\mathbb{H}$ | Quaternions | $\tilde q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $q_t$, real | $q_x\vec e_x$, $q_y\vec e_y$, $q_z\vec e_z$, real |
| $\mathbb{B}$ | Biquaternions | $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $Q_t$, complex | $Q_x\vec e_x$, $Q_y\vec e_y$, $Q_z\vec e_z$, complex |

Under this framework, the **vector part** is the part carried by the three vector units $\vec e_x,\vec e_y,\vec e_z$; it exists only in the four quaternionic layers.

**The two part columns.** The fourth column gives the scalar part — the $\mathbb{C}$ scalar part in $\mathbb{B}$ and $\mathbb{B}_{\mathrm{r}}$ — and the fifth the vector part, each coefficient with its nature. In $\mathbb{C}$, $\mathbb{C}^2$ and $\mathbb{B}_{\mathrm{r}}$ there is no vector direction, so both coefficients are scalars of the coefficient field and the vector column is empty.

**The reals come first, written $q$.** The reals have no vector part and carry no tilde and no prime: the generic real element is the lower-case $q$, and it is the glyph every coefficient of the layers is a real parameter of — the $q_\mu$ of the quaternions, and the real part of $Q_\mu = q_\mu + iq'_\mu$ of the biquaternions.

**Several elements of one kind take subscripts.** Where a statement needs more than one element of the same kind, each occurrence takes a number: three generic biquaternions are $\tilde Q_1, \tilde Q_2, \tilde Q_3$, two quaternions are $\tilde q_1, \tilde q_2$, and two complex numbers are $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. The number counts the element and never names a direction; a letter names the direction. **Every element of a numbered statement is numbered**: a bare $\tilde Q$ stands alone, in a statement about one element, and never beside $\tilde Q_1$ or $\tilde Q_2$. The numbers count the elements in the order the statement introduces them, $\tilde Q_1, \tilde Q_2, \tilde Q_3$, and the coefficients follow their element, $Q_{1t}, \vec Q_1$ for $\tilde Q_1$.

**The coefficient index is the label of its unit.** The four slots are labelled $t,x,y,z$, and a coefficient takes the label of the unit it multiplies: $Q_t$ with $e_t$, and $Q_x,Q_y,Q_z$ with $\vec e_x,\vec e_y,\vec e_z$. A sum over the four runs over those labels,

$$
\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu,
$$

with $e_t$ at $\mu=t$ and $\vec e_\mu$ at $\mu=x,y,z$. The same rule reads a quaternion, $\tilde q=\sum_\mu q_\mu e_\mu$. The label names the unit, not the time coordinate: the material time is $t'$ and the informational time is $t$.

**The coefficient prime marks the slot that carries the $i$.** Each complex coefficient is a real part plus $i$ times a real part,

$$
Q_\mu = q_\mu + iq'_\mu, \qquad q_\mu, q'_\mu \in \mathbb{R}, \qquad \mu \in \{t, x, y, z\},
$$

so $q_\mu$ multiplies $e_\mu$ and $q'_\mu$ multiplies $ie_\mu$, the same rule for the four slots:

| Coefficient | Real part | Attached to | Imaginary part | Attached to |
|---|---|---|---|---|
| $Q_t$ | $q_t$ | $e_t$ | $q'_t$ | $ie_t$ |
| $Q_x$ | $q_x$ | $\vec e_x$ | $q'_x$ | $i\vec e_x$ |
| $Q_y$ | $q_y$ | $\vec e_y$ | $q'_y$ | $i\vec e_y$ |
| $Q_z$ | $q_z$ | $\vec e_z$ | $q'_z$ | $i\vec e_z$ |

**The element is a scalar part plus, where the layer has one, a vector part.** The scalar part is carried by $1$ in $\mathbb{C}$ and $\mathbb{B}_{\mathrm{r}}$ and by $e_t$ in $\mathbb{H}$ and $\mathbb{B}$; the vector part exists in the quaternionic layers alone and carries the arrow, $\tilde Q = Q_te_t + \vec Q$ with $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$. In $\mathbb{C}$ the second term $iq'$ is the imaginary part of a single coefficient, and in $\mathbb{B}_{\mathrm{r}}$ the second term $jQ_{\blacktriangledown}$ is its $j$-part, neither being a vector part. The reduced biquaternion layer writes $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$, with complex $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$; the breve tells it from the complex element $Q$ of the same capital, its algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is commutative and has no quaternionic factor, and its second unit is the hyperbolic $j$, $j^{2} = +1$ with $ji = ij$, on the basis $1, i, j, ij$.

**A duo-complex number carries the same two triangles.** The pair $(Q_{\blacktriangle},Q_{\blacktriangledown})$ is a point of $\mathbb{C}^2$, two complex coordinates with no product, and it is the reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ read without the multiplication by $j$, the basis of the algebra over $\mathbb{C}$ being $1,j$. **The ascending triangle is the first coordinate and the descending triangle the second**; the breve is what makes the pair an element of the algebra, and a point is never written with it. The coordinates of two points are numbered before the triangle, $Q_{1\blacktriangle}$ and $Q_{2\blacktriangle}$, and the prime marks the slot that carries the $i$, $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$. **The triangles mark the coordinates and the digits mark the basis**: in the basis $e_1,e_2$ the point is $Q=Q_{\blacktriangle}e_1+Q_{\blacktriangledown}e_2$, the ascending triangle on $e_1$ and the descending triangle on $e_2$. A column of the $2\times2$ representation takes the same pair when it is read as a point of $\mathbb{C}^2$; attached to an element it is the pair of coordinates of that element, and the object it is attached to says which.

**A pure element carries the arrow.** A pure element is one with no scalar part, a vector of its layer, written $\vec q$ or $\vec Q$ without the tilde; the arrow names the vector part of a named element and the element read on its own, the two never stacked (§*The Centre and the Vector Subspace*).

**The forms and the operators are written on the Q family.** Two elements of one statement are $\tilde Q_1$ and $\tilde Q_2$, a third taking the next number. The plain form is $\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2)$, with plain norm $\langle\tilde{Q}\rangle=\langle\tilde{Q},\tilde{Q}\rangle$ and unit $\langle e_t\rangle=1$; the trace pairing $2\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2)$ is its $2\times2$ reading, the commutator bracket $[\tilde{Q}_1,\tilde{Q}_2] = \tilde{Q}_1\tilde{Q}_2 - \tilde{Q}_2\tilde{Q}_1$, the general quaternionic bilinear form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ and the multiplicativity $\langle\tilde{Q}_1\tilde{Q}_2\rangle_{\natural} = \langle\tilde{Q}_1\rangle_{\natural}\,\langle\tilde{Q}_2\rangle_{\natural}$. The argument of an operator, the dummy of an annihilator, the second entry of a bracket and the element a field or a map is applied to carry the same glyph: $L_{\tilde Q_1}(\tilde Q_2) = \tilde Q_1 \bullet \tilde Q_2$, $\{\tilde Q_2 : \tilde Q_1 \star \tilde Q_2 = 0\}$, $[\tilde Q_1, \tilde Q_2]$. **The letter $\tilde P$ is never a generic element**; it is the four-momentum, $\tilde P = m\tilde V$. **In the layers of the biquaternion family the glyph $Q$ belongs to the element and never to an operator**: an operator generated by an element carries the structural capital and the element in the subscript, $L_{\tilde Q}$, and an operator that is not the multiplication by an element takes a letter of its own.

**The letters of the physical quantities.** The glyphs are fixed one to a quantity, so that a reader meets the same letter for the same thing in every article; the tables of §*The Most Common Quaternions and Biquaternions* and §*Summary of Notation* list them all.

**A logarithm carries the glyph of its element and the subscript $\log$.** The logarithm is a solution of the exponential equation in the same algebra, not an object of a new kind, so it carries the glyph of the element and the subscript, and the definition reads $\exp(\tilde Q_{\log}) = \tilde Q$. The glyph is $\tilde Q_{\log}$ in this algebra, $\tilde q_{\log}$ in the quaternion and split-quaternion layers, $\breve Q_{\log}$ in the reduced biquaternions, and $Q_{\log}$ in the complex, split-complex and dual ones. The subscript is a word, so it competes neither with the direction labels, $Q_t$ and $Q_x$, nor with the counts, $Q_1$; a numbered element keeps its number in front of the subscript, $\tilde Q_{1\log}$. The subscript is dropped when the logarithm is written as an operator, $\log\tilde Q$ or $\operatorname{Log}\tilde Q$. The coordinates of a logarithm follow the coefficient rule: in the complex, split-complex and dual layers, $Q_{\log}=q_{\log}+iq'_{\log}$ has real part $q_{\log}$ and imaginary part $q'_{\log}$, with $j$ in place of $i$ in the split-complex case, and the prime marks the imaginary coordinate alone. The logarithm of a real number is the ordinary real logarithm, written $\log q$; the glyph $q_{\log}$ is the real coordinate of $Q_{\log}$, not the logarithm of $q$.

## The Remarkable Subspaces of Biquaternions

The eight real parameters of a general element group into **remarkable subspaces**: the centre, the vector subspace, the two halves of the coefficient split, and the two sectors. Each is cut out by a conjugation:

| Subspace | Defining condition | Dimension over $\mathbb{R}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $\tilde{Q}^{\natural} = \tilde{Q}$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $\bar{\tilde{Q}} = \tilde{Q}$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$, the antiquaternion subspace | $\bar{\tilde{Q}} = -\tilde{Q}$ | $4$ |
| $\mathbb{M}_+$, the Hermitian subspace | $\tilde{Q}^{*} = \tilde{Q}$ | $4$ |
| $\mathbb{M}_-$, the anti-Hermitian subspace | $\tilde{Q}^{\flat} = \tilde{Q}$ | $4$ |

### The Basis, the Parameters and the Coordinates

The dictionary between the parameters and the physical coordinates is fixed once and for all. The four real parts are $(t, x, y, z)$ and the four imaginary parts $(t', x', y', z')$,

$$
q'_t = c\,t', \qquad (q_x, q_y, q_z) = (x, y, z), \qquad q_t = c\,t, \qquad (q'_x, q'_y, q'_z) = (x', y', z'),
$$

so that the four coefficients are $Q_t = c(t+it')$, $Q_x = x+ix'$, $Q_y = y+iy'$, $Q_z = z+iz'$, with $\vec q = x\vec e_x+y\vec e_y+z\vec e_z$ the real spatial vector and $i(x'\vec e_x+y'\vec e_y+z'\vec e_z)$ its imaginary counterpart. Each subspace keeps whichever part of the dictionary its defining condition leaves free.

| Subspace | Algebraic name | Physical name | Basis | Real parameters | Physical coordinates |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | The centre | Complex time sector | $e_t,\ ie_t$ | $q_t,\ q'_t$ | $ct,\ ict'$ |
| $\mathrm{Vect}(\mathbb{B})$ | Vector | Complex space sector | $\vec e_x,\ \vec e_y,\ \vec e_z,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q_x,\ q_y,\ q_z,\ q'_x,\ q'_y,\ q'_z$ | $x,\ y,\ z,\ ix',\ iy',\ iz'$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion | Real sector | $e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $q_t,\ q_x,\ q_y,\ q_z$ | $ct,\ x,\ y,\ z$ |
| $i\mathbb{H}_{\mathbb{B}}$ | Antiquaternion | Imaginary sector | $ie_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q'_t,\ q'_x,\ q'_y,\ q'_z$ | $ict',\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_+$ | Hermitian | Informational sector | $e_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $q_t,\ q'_x,\ q'_y,\ q'_z$ | $ct,\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_-$ | Anti-Hermitian | Material sector | $ie_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $q'_t,\ q_x,\ q_y,\ q_z$ | $ict',\ x,\ y,\ z$ |

Each subspace carries an **algebraic name**, taken from the involution that defines it, and a **physical name**, taken from the role it plays; the companion articles are titled by the physical name.

### The Centre and the Vector Subspace

The algebra is the direct sum

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}),
$$

the centre with the traceless part.

**The centre and the vector subspace carry a glyph each.** The centre is written with the tilde-free coefficient of $e_t$, $Q_te_t$, a complex scalar times the unit; the vector subspace is written $\vec Q$, the pure element, with the arrow and without the tilde.

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

### The Quaternion and Antiquaternion Subspaces

The algebra is the direct sum

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}},
$$

the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, whose elements carry real coefficients throughout, with the antiquaternion subspace $i\mathbb{H}_{\mathbb{B}}$, whose elements carry purely imaginary ones: the two are the **real and imaginary halves** of the algebra. The prime splits the element into the two parts,

$$
\tilde Q = \tilde q + i\tilde q',\qquad
\tilde q = q_t\,e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z \in \mathbb{H}_{\mathbb{B}},\qquad
\tilde q' = q'_t\,e_t + q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z \in \mathbb{H}_{\mathbb{B}}.
$$

The prime marks the second glyph and the split is uniform: $\tilde q$ takes the unprimed parameters and $\tilde q'$ the primed ones.

### The Hermitian and Anti-Hermitian Subspaces

The algebra is the direct sum

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

the Hermitian subspace with the anti-Hermitian one; without qualification, *the sectors* in this series are these two, and the relativistic articles are written in terms of this split. The element splits a second time, across the coefficient slots,

$$
\tilde Q = \tilde Q_{\mathrm H} + \tilde Q_{\mathrm A},\qquad
\tilde Q_{\mathrm H} = q_t\,e_t + i\bigl(q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z\bigr),\qquad
\tilde Q_{\mathrm A} = iq'_t\,e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z.
$$

$\tilde Q_{\mathrm H}$ is the informational part: it takes the real scalar slot with the imaginary vector slots, and $\tilde Q_{\mathrm A}$ is the material part: the imaginary scalar slot with the real vector slots. The primed set therefore holds the material time $q'_t$ and the three informational spaces $q'_k$; the unprimed set holds the informational time $q_t$ and the three material spaces $q_k$.

**The particular case of coordinates.** At the dictionary values the two parts are the informational coordinate and the material coordinate,

$$
\tilde Q_{\mathrm H} = ct\,e_t + i\bigl(x'\vec e_x + y'\vec e_y + z'\vec e_z\bigr),\qquad
\tilde Q_{\mathrm A} = \tilde R = ict'\,e_t + x\vec e_x + y\vec e_y + z\vec e_z,
$$

the informational part carrying the real time $ct$ and the imaginary space $x',y',z'$, the material part the real space $x,y,z$ and the imaginary time $ct'$.

Quantum physics writes the informational coordinate in the letters of an operator rather than of a coordinate: its four real parameters are named $h_t, h_x, h_y, h_z$ in place of $q_t, q'_x, q'_y, q'_z$ — the direction labels, as for the coordinates $Q_\mu$ — and the element is

$$
\tilde Q_{\mathrm H} = \tilde{H} = h_te_t + ih_x\vec e_x + ih_y\vec e_y + ih_z\vec e_z, \qquad h_t, h_x, h_y, h_z \in \mathbb{R},
$$

or, with the vector part assembled,

$$
\tilde Q_{\mathrm H} = \tilde{H} = h_te_t + i\vec h , \qquad \vec h = h_x\vec e_x + h_y\vec e_y + h_z\vec e_z ,
$$

with $h_t = ct$ and $h_k = x'_k$. This is the informational coordinate $ct\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ of the table under the coefficient names of an operator, and its matrix image, under the unit images of *Conventions of the Representations*, §*The 2×2 Matrix Representation* ($\mathsf{M}_2(e_t) = I_2$ and the vector units $-i$ times the Pauli matrices $\sigma_1, \sigma_2, \sigma_3$), is the general Hermitian $2\times2$ matrix $h_tI_2 + h_x\sigma_1 + h_y\sigma_2 + h_z\sigma_3$ of *The Native Qubit and the Defining Module of the Biquaternion Algebra*. The tilde is required, because $H$ without it is the Hamiltonian, and $h$ without a subscript is the Planck constant.

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

**The fourth mark is a sign, not a fourth conjugation.** $\flat=-{}^{*}$ is the negative of the star, it reverses products with a twist, $(\tilde Q_1\tilde Q_2)^{\flat}=-\tilde Q_2^{\flat}\tilde Q_1^{\flat}$, and it is an involution of the underlying real space only, not of the ring. Its fixed space is the material sector $\mathbb{M}_-$, and the sector split is its work in the series. It is retained for that split, for the bilinear pairings built on it, and for the real-form question of Dirac against Majorana fermions. It is not the mass — the retired form $\tilde\nabla\tilde\Psi=m\tilde\Psi^\flat$ conflated the two — and it is not the charge conjugation of the module, the operation defined in *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*.

**The biquaternion norm.** The natural sign carries the algebra's **biquaternion norm**,

$$
\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 ,
$$

used throughout the series and read on the four forms and their norms in *Conventions of the Products and the Forms*, §*The Involutions and the Four Forms* and *Conventions of the Norms and the Pairings*, §*The Four Algebraic Norms and the $*$-Unitary Convention*. It is **multiplicative** and complex-valued in general, and it is not an analytic norm; its unit group and its invertibility reading are *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Group of Units*.

Each of the four marks has a fixed space, and each of these is one of the **remarkable subspaces** of the algebra. Which involution defines which subspace, and which of them are anti-fixed, is recorded with the subspaces themselves, in *The Remarkable Subspaces* above.

## The Most Common Quaternions and Biquaternions

The tilde-marked glyphs a reader meets in every article are collected here, with the role, the formula, the space and the meaning of each, after the section that defines the conjugations; the norms they are read against are fixed in *Conventions of the Norms and the Pairings*. The basis, the central $i$, the charges, the pure elements, the glyphs of the reduced biquaternion layer and the tilde-free relations carry no tilde and are collected in §*Summary of Notation*.

**Scope: tilde glyphs only.** Every catalogued symbol carries a tilde. Four kinds of glyph are outside the scope and are not listed among the allowed uses: a matrix, $I_n$, $\mathsf{M}_2$, $\mathsf{M}_4^{L}$; a pure element written with an arrow, $\vec Q$, $\vec q$, $\vec u$, $\vec U$, $\vec\Xi$, $\vec\Upsilon$, $\vec\pi$; a mark that is not an element; and every glyph of the reduced, tilde-free layers, $\Pi_\pm$, $\Xi_\pm$. The first is fixed by the rule that a matrix carries no tilde, *Conventions of the Representations*, §*General Matrix Conventions*; the others are elements of other layers or of no layer at all. The operator section states the rule that pairs the two marks; it is not a catalogue of arrowed glyphs.

The tilde marks a quaternionic factor. A base glyph counts every numbered and subscripted variant.

**Allowed tilde.** The role is fixed by this article, or by the case-and-mark rule it states, and checked against the corpus. Cite these entries as they stand. The tables are ordered by theme, as the objects are; the letters outside the U family are bound where they are introduced.

The governing rule: **only the Q family is generic, and only an element carries the tilde.** $\tilde Q$ is the biquaternion or split-biquaternion element and $\tilde q$ the quaternion or split-quaternion element; numbered variants are allowed. A generic element of norm one is written $\tilde U$. A letter outside the family names an object, or an element bound where it is introduced. A matrix — the image of an element, an array of biquaternions, or a colour matrix — takes no tilde; a tilde on one is a defect of scope, corrected where it occurs and not catalogued here. A tensor is not an element of the algebra: its components $T^\mu{}_\nu$ and $T^{\mu\nu}$, and the irreducible tensor operators $T^{(k)}_\mu$, carry no tilde, and a free element written $\tilde T$ is the same defect, corrected to the Q family.

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
| $\tilde U$ | $N$-norm-one element | $U_te_t+\vec U$, with $\langle\tilde U\rangle_{\natural}=e_t$ | $\mathbb{B}$ | A unit element in the norm $N$ of the biquaternion layer, $\mathbb{B}^{\times}_1\cong\mathrm{SL}(2,\mathbb{C})$; not a $*$-unitary element, which is a different set. The conjugating element of an inner automorphism, normalised by the central square root of its norm, is this glyph |
| $\tilde u$ | Unit quaternion | $\cos(\theta/2)e_t+\sin(\theta/2)\vec u$, $\vec u$ a unit real vector | $\mathbb{H}_{\mathbb{B}}$, norm one | The rotor of $\mathrm{Sp}(1)\cong\mathrm{SU}(2)$; a pure unit quaternion is $\vec u$ |
| $\tilde U_{\mathrm b}$ | Hermitian positive boost, the frame rotor | $\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | $\mathbb{M}_+$, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$ | The Lorentz boost of rapidity $\psi$ and the boost factor of the polar word; the congruence by it is the boost, and a four-vector element carries its inverse square $\mathcal B=\tilde U_{\mathrm b}^{-2}$, *Conventions of the Norms and the Pairings*, §*The Polar Word and the Three Pairings*. It is not $*$-unitary under ${}^{*}$, $\tilde U_{\mathrm b}^{*}\tilde U_{\mathrm b}\neq e_t$. The label is $\mathrm b$; the longer spelling $\mathrm{boost}$ is not used. Its generator is the pure element $\tfrac12 i\vec u_{\mathrm b}$ |
| $\mathcal B$ | Four-vector boost factor | $\tilde U_{\mathrm b}^{-2}=\cosh\psi\,e_t-i\sinh\psi\,\vec u_{\mathrm b}$ | $\mathbb{M}_+$, $\det=1$ | The factor a four-vector element carries; equal to $e^{\vec U\Theta}$ with $\Theta=-i\psi$. It is not the acting rotor: the word's factor is $\tilde U_{\mathrm b}$ for a transformation and $\mathcal B$ for a four-vector |
| $\tilde u_{\mathrm r}$ | Unit real quaternion rotor | $\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | $\mathbb{H}_{\mathbb{B}}$, norm one | The rotor of the polar word and of every rotation here, the rotating frame included; half-angle $\theta/2$, axis $\vec u_{\mathrm r}$; $*$-unitary under every product |
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

**No hat accents on algebra elements.** The series writes no hatted glyph for an element of the algebra. A hat is not available for a new object, and an existing hatted symbol is rewritten without it: the positive polar factor is $\tilde Q_H$, the $*$-unitary polar factor is $\tilde Q_0=\tilde Q_H^{-1}\tilde Q$, and the normalised amplitude is $\tilde Q_{\mathrm n}=\tilde Q_H/\sqrt{2\langle\tilde Q_H,\tilde Q_H\rangle_{*}}$. The mathematical articles write Tate cohomology and profinite completions as $H^n_{\mathrm{Tate}}(G,M)$ and $G^{\mathrm{pf}}$. The hat on a unit vector, $\hat p$ and $\hat x$, is the direction notation of *Conventions of the Norms and the Pairings*, §*The Four-Momentum* and is unaffected.

### The Gradient and the Operators

| Symbol | Name | Formula | Space | Meaning |
|---|---|---|---|---|
| $\tilde\nabla$ | Biquaternionic gradient | $e_t\,\partial/\partial Q_t+\vec e_x\,\partial/\partial Q_x+\vec e_y\,\partial/\partial Q_y+\vec e_z\,\partial/\partial Q_z$ | Operator, $\mathbb{B}$-valued | Its conjugate $\tilde\nabla^{\natural}=e_t\,\partial/\partial Q_t-\vec e_k\,\partial/\partial Q_k$ is the second factor of $\Box$ |
| $\tilde D$ | Gauge-covariant derivative | $\tilde D=\tilde\nabla+i\kappa\mathcal A$ | Operator, $\mathbb{B}$-valued | The gauge-principle, minimal-coupling, Yang–Mills, instanton and Stueckelberg articles. Its $e_t$ coefficient is $\partial/\partial Q_t+i\kappa\mathcal A_t$, so the operator is read with its scalar part; on the curvature it acts as $\tilde D\tilde F=\tilde\nabla\tilde F+i\kappa[\mathcal A,\tilde F]$, the Yang–Mills current. The component $D_\mu=\partial/\partial Q_\mu+i\kappa\mathcal A_\mu$ carries no tilde |
| $\tilde K_{\mathrm{ret}}$ | Retarded-time gradient coefficient | $\tilde K_{\mathrm{ret}}=\tilde\nabla^{\natural}t'_r=\frac{1}{c\kappa}(-ie_t+\vec u_R)$, $\kappa=1-\vec u_R\cdot\vec\beta$ | $\mathbb{M}_-$, null | The gradient of the retarded time, also called the null retarded gradient: an element, not an operator, and $\tilde\nabla^{\natural}\tilde Q=\tilde K_{\mathrm{ret}}\,d\tilde Q/dt'_r$ for a source depending on $t'_r$ alone. It is a zero divisor, $\langle\tilde K_{\mathrm{ret}}\rangle_{\natural}=0$, so it is null and not $*$-unitary at any $\kappa$. The $\kappa$ here is the retarded denominator, not the coupling of $\tilde D$ |

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
| $\tilde S$ | Spin operators | $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ | $\mathbb{M}_+$ | The vector slots of $\mathbb{M}_+$. The total of several angular momenta is $\tilde S_{\mathrm{tot},k}=\tilde L_k+\tilde S_k$ or a sum of factor spins, never a bare $\tilde S$ |
| $\tilde E$ | Effect of a measurement | $0\le\tilde E\le e_t$, $\tilde E\in\mathbb{M}_+$; $\tilde E_y=\tilde K_y^{*}\tilde K_y$ | $\mathbb{M}_+$ | The outcome of a POVM; a rank-one effect is the idempotent $\tilde\Pi$ |
| $\tilde K_y,\tilde K_l,\tilde K_i,\tilde K_\epsilon,\tilde K_{1,2},\tilde K_0,\tilde K_1,\tilde K_2,\tilde K_k$ | Kraus operator | $\tilde E_y=\tilde K_y^{*}\tilde K_y$; $\Phi(\tilde{Ϛ})=\sum_l\tilde K_l\tilde{Ϛ}\tilde K_l^{*}$ | $\mathbb{B}$ | The Kraus operators of a channel or an instrument: each is an element of $\mathbb{B}$, multiplied on both sides of the state, not an array; its matrix image $\mathsf{M}_2(\tilde K_y)$ carries no tilde. The resolution is $\sum_y\tilde K_y^{*}\tilde K_y=e_t$, and the three rank-one articles write the single operator bare, $\tilde K=\tilde U$. The outcome label is an index, $y$, $l$, $i$, $\epsilon$ or a numbered pair; the count includes the two articles that label the outcomes $\epsilon$ and $(1,2)$ |
| $\tilde K_{\mathrm{mod}}$ | Modular Hamiltonian | $\tilde K_{\mathrm{mod}}=-\log\tilde{Ϛ}$; $\Delta=\exp(-\tilde K_{\mathrm{mod}})$ | $\mathbb{M}_+$ | The modular Hamiltonian of Tomita–Takesaki, with the modular flow $\sigma_{t'}(\tilde Q)=\Delta^{it'}\tilde Q\Delta^{-it'}$. In the finite-dimensional model it is $-\log\tilde{Ϛ}\in\mathbb{M}_+$; the labels $W$, $V$, $\omega$, $L$, $R$ and $\varphi$ name the region, state or side |

**The angular-momentum labels are lower-case Latin, and the total takes the role subscript.** A spin label is $s$, its weight $s_z$, and the operator carries the tilde, $\tilde S_k$. An orbital label is $l$, its weight $l_z$, with $\tilde L_k$. The total of an orbital and a spin part, or of several spins, is $s_{\mathrm{tot}}$, its weight $s_{\mathrm{tot},z}$, and its operator $\tilde S_{\mathrm{tot},k}=\tilde L_k+\tilde S_k$. A coupled pair writes $s_1,s_{1z},s_2,s_{2z}$ and its total $s_{\mathrm{tot}},s_{\mathrm{tot},z}$; the final multiplet of a tensor operator is $s_{\mathrm{fin}}$, with weight $s_{\mathrm{fin},z}$, and its reduced matrix element is $\langle s_{\mathrm{fin}}\|T^{(k)}\|s_{\mathrm{tot}}\rangle$. A representation of spin $s$ is $V_s$, of dimension $2s+1$. The letter $j$ is not used for any of these: it is the hyperbolic unit of the reduced layer, and it never denotes an angular momentum or a weight. The letter $m$ is not used for a weight either: it is the mass, and a magnetic weight is written $s_z$, $l_z$ or $s_{\mathrm{tot},z}$.

**The state takes the stigma, because the majuscule of rho is taken.** The case rule asks a complex element for an upper-case glyph, and the upper-case rho is drawn as $P$ and names the four-momentum $\tilde P$, which the series never writes otherwise. The state therefore takes a capital that names nothing else in the corpus, the **stigma** $Ϛ$ (U+03DA). The glyph is bound to the state and is never generic; the earlier lowercase rho spelling, and the varrho variant with it, are retired, and the corpus uses neither. Bare $\rho$ is not the state: it keeps its other roles, the charge density and the radial coordinate among them. The matrix image takes no tilde, as for every element.

## Summary

The base conventions are one object read in order. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ satisfying $\vec e_k^2=-e_t$, over complex coefficients; the scalar unit $i$ is central, and multiplication by it is one map whose restrictions are read in *Conventions of the Special Elements*. The element is written with its case and its tilde, and its coefficients $Q_\mu=q_\mu+iq'_\mu$ split it into a quaternion part and an antiquaternion part.

The conjugations cut the algebra into the remarkable subspaces, and the subspaces carry the coordinate dictionary and the two sector names, with $q'_t=ct'$, $q_t=ct$, $(q_x,q_y,q_z)=(x,y,z)$ and $(q'_x,q'_y,q'_z)=(x',y',z')$. The pure elements — those with no scalar part — are written with the arrow and without the tilde, $\vec Q$. A duo-complex number is written $Q=(Q_{\blacktriangle},Q_{\blacktriangledown})$, a pair of complex coordinates with no product, and the reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is that pair together with the multiplication by $j$.

The glyphs a reader meets in every article are collected once, with the role, the formula, the space and the meaning of each. The collection is a closed list: no tilde is written on an array, no glyph is invented for an operator, and no letter is reused for a second object of the same layer. The rest of the conventions is in the six companion articles — products and forms, norms and pairings, special elements, representations, operators and calculus, units and notation — each stated after the one it depends on.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde Q = \tilde q + i\tilde q'$ | The element and its split into a quaternion part and an antiquaternion part |
| $\vec Q$ | The vector part of an element, a pure element when read on its own, $\mathrm{Sc}(\vec Q)=0$ |
| $\vec q$ | Position, the pure quaternion $\vec q=x\vec e_x+y\vec e_y+z\vec e_z$ |
| $\mathbb{C}_{\mathbb{B}} = \{Q_t e_t\}$ | Centre subspace, the complex time sector |
| $\mathrm{Vect}(\mathbb{B})$ | The vector subspace, the complex space sector, real dimension six |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | Real-quaternion and antiquaternion subspaces, the real and imaginary halves |
| $\mathbb{M}_+$ | Hermitian subspace, the informational sector |
| $\mathbb{M}_- = \{\tilde Q : \tilde Q^\flat=\tilde Q\}$ | Anti-Hermitian subspace, the material sector; $\flat=-{}^{*}$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | The reduced biquaternion, a duo-complex pair with the multiplication by $j$ |

## Further Reading

- [Conventions of the Products and the Forms](conventions-of-the-products-and-the-forms.html), for the twelve products and the four forms.
- [Conventions of the Norms and the Pairings](conventions-of-the-norms-and-the-pairings.html), for the four norms, the unitary convention, the polar word and the three pairings.
- [Conventions of the Special Elements](conventions-of-the-special-elements.html), for the central map, the root, the idempotent, the nilpotent and spin.
- [Conventions of the Representations](conventions-of-the-representations.html), for the four-vector, the $2\times2$ isomorphism, the $4\times4$ regular representation and the Clifford map.
- [Conventions of the Operators and the Calculus](conventions-of-the-operators-and-the-calculus.html), for the operators and for the derivative marks, the gradient and the d'Alembertian.
- [Conventions of the Units, the Indices and the Notation](conventions-of-the-units-the-indices-and-the-notation.html), for the SI units, the two superscript tokens and the rules of the subscripts.
- [The Biquaternion Space, the Group of Involutions and the Six Subspaces](the-biquaternion-space-the-group-of-involutions-and-the-six-subspaces.html), companion article, for the relations among the subspaces defined here — their coordinate blocks, intersections, spans, gradings and biquaternion norms.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the original quaternion algebra and its units.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents, minimal left ideals and the conjugations of a Clifford algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for real structures and real forms on Clifford algebras.
