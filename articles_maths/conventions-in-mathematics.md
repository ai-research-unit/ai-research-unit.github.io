# __Conventions in Mathematics__

## Introduction

This article gathers the conventions the mathematical articles assume: the symbols, the arithmetic conventions, the shape of a generic element and its coefficients, the marks reserved for the conjugations of an algebra with an involution, the glyphs and marks of the operators, the convention of the form and the norm, the working conventions of the corpus itself — the menu, the groups inside a category, the article files and the skeleton — and the typographic rules of the source.

They are stated once, here, so that no other article need repeat them. This article states conventions only: the proofs and the properties of the objects it names belong to the articles cited beside them. How the articles are organised into the six parts and their categories is the subject of the companion article *Introduction to Mathematics*; this one is the reference for the elements, the marks, the glyphs and the layout.

## Groups, Rings and Operations

A group is written multiplicatively by default, with unit $e$ and inverse $x^{-1}$, and additively when it is the underlying group of a ring, with zero $0$ and inverse $-x$. A ring is a triple $(R, +, \cdot)$; a ring need not be commutative and need not have a unit, and the article that introduces it says which conventions it adopts. A field is a commutative ring with $1 \neq 0$ in which every nonzero element is invertible. A module is written with its scalars on the left unless the article says otherwise, and the side matters as soon as the ring is non-commutative. Products are written by juxtaposition: $ab$ for the product in a group or an algebra, $fv$ for the action of a scalar on a vector. The **symmetrised (Jordan) product** is written with a bullet, $x \bullet y = \tfrac{1}{2}(xy + yx)$, and the circle $\circ$ is kept for the **composition of maps**, as in $\mathrm{H}_{\tilde Q}\circ\mathrm{H}_{\sqrt{\mu}\,\tilde J}$.

## The Base and Its Units

The base is written with the letter $e$, one unit to a direction. The scalar unit is $e_t = 1$ and the three vector units are $\vec e_x, \vec e_y, \vec e_z$; the arrow is the only mark that separates the scalar unit from the vector units. **The three vector units are the quaternion units, the corpus's replacement for Hamilton's $i, j, k$.** A general element is written in the base,

$$
\tilde Q = Q_t e_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $e_\mu$ the unit of the direction $\mu$. In the quaternion layers the three vector units square to the negative of the scalar unit, $\vec e_k^2 = -e_t$; the split-quaternion layer keeps $\vec e_x^2 = -e_t$ and takes $\vec e_y^2 = \vec e_z^2 = +e_t$ (§*The Conjugations*). **The notation is the unit along the axis.** A coefficient carries the name of the direction it multiplies: $Q_x$ is the coefficient of $\vec e_x$, the label on the unit names the direction and the label on the coefficient names the same direction, so the coefficient and the unit read without ambiguity. **The base letter is $e$ and the unit-element letter is $u$, and the two are never exchanged.** The base units carry $e$, so $e$ is not available for the exponential, which is written $\exp(\cdot)$; a unit element of a layer carries the glyph of the unit element, $\tilde u$ or $\tilde U$ (§*The Unitary Convention*).

**The replacement of Hamilton's $i, j, k$ by the base rests on three reasons:**

- **The letters $i$ and $j$ are already taken.** Hamilton's $i, j, k$ collides with the complex $i$, kept for the central imaginary, and with the hyperbolic unit $j$, so a vector unit written with either letter would be misread.
- **The base names the four directions.** The labels $t, x, y, z$ name the four directions of the base and carry no physical meaning; $e_\mu$ is the unit along the direction $\mu$.
- **The base spends no digit.** The labels carry no digit, so every digit stays free to count the generic objects: $Q_1, Q_2$, $\tilde Q_1, \tilde Q_2$ and $\tilde q_1, \tilde q_2$.

## The Elements and their Coefficients

The case and the tilde of the glyph are fixed first, and the element is written after. A generic element is written so that the glyph alone identifies its algebra, two features being read together: the **case** separates a real scalar from a complex one, and a **tilde** marks the quaternionic factor. **The generic element of a layer of the algebra belongs to the Q family and to no other letter**: $\tilde q$ is the quaternion or split-quaternion element, $\tilde Q$ the biquaternion or split-biquaternion one, in every layer of the quaternion family. A letter outside the family is never a generic element of the algebra: it names an object, or an element bound at the point of use.

| System | Name | Generic element | Scalar part | Vector part |
|---|---|---|---|---|
| $\mathbf{2}$ | Booleans | $\alpha, \beta, \dots$ | — | — |
| $\mathbb{N}$ | Naturals | $n, m, \dots$ | — | — |
| $\mathbb{Z}$ | Integers | $n, m, \dots$ | — | — |
| $\mathbb{Q}$ | Rationals | $q, q_1, q_2, \dots$ | $q$, real | — |
| $\mathbb{R}$ | Reals | $q, q_1, q_2$ | $q$, real | — |
| $\mathbb{C}$ | Complex numbers | $Q = q + iq'$ | $q$, real; $q'$, real | — |
| $\mathbb{D}$ | Split-complex numbers | $Q = q + jq'$ | $q$, real; $q'$, real | — |
| $\mathbb{D}'$ | Dual numbers | $Q = q + \varepsilon q'$ | $q$, real; $q'$, real | — |
| $\mathbb{B}_{\mathrm{r}}$ | Reduced biquaternions | $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ | $Q_{\blacktriangle}$, complex; $Q_{\blacktriangledown}$, complex | — |
| $\mathbb{H}$ | Quaternions | $\tilde q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $q_t$, real | $q_x\vec e_x$, $q_y\vec e_y$, $q_z\vec e_z$, real |
| $\mathbb{H}_{\mathrm{s}}$ | Split-quaternions | $\tilde q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $q_t$, real | $q_x\vec e_x$, $q_y\vec e_y$, $q_z\vec e_z$, real |
| $\mathbb{B}$ | Biquaternions | $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $Q_t$, complex | $Q_x\vec e_x$, $Q_y\vec e_y$, $Q_z\vec e_z$, complex |
| $\mathbb{H}_{\mathbb{D}}$ | Split-biquaternions | $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $Q_t$, split-complex | $Q_x\vec e_x$, $Q_y\vec e_y$, $Q_z\vec e_z$, split-complex |

Under this framework, the **vector part** is the part carried by the three vector units $\vec e_x,\vec e_y,\vec e_z$; it exists only in the four quaternionic layers.

**The two part columns.** The fourth column gives the scalar part — the $\mathbb{C}$ scalar part in $\mathbb{B}$ and $\mathbb{B}_{\mathrm{r}}$, the split scalar part in $\mathbb{H}_{\mathbb{D}}$ — and the fifth the vector part, each coefficient with its nature. In $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{B}_{\mathrm{r}}$ there is no vector direction, so both coefficients are scalars of the coefficient field and the vector column is empty.

**Several elements of one kind take subscripts.** Where a statement needs more than one element of the same kind, each occurrence takes a number: three generic biquaternions are $\tilde Q_1, \tilde Q_2, \tilde Q_3$, two quaternions are $\tilde q_1, \tilde q_2$, and two complex numbers are $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. The number counts the element and never names a direction; a letter names the direction. **The unnumbered glyph is the single generic element**: a bare $\tilde Q$ stands alone, or leads the pair $\tilde Q, \tilde Q_2$; two numbered elements are $\tilde Q_1, \tilde Q_2$, and a third takes the next number. The numbers count the elements in the order the statement introduces them, $\tilde Q_1, \tilde Q_2, \tilde Q_3$, and the coefficients follow their element, $Q_{1t}, \vec Q_1$ for $\tilde Q_1$.

**The four coordinates are labelled $t, x, y, z$.** So that a sum over the coordinates of a quaternion, a split-quaternion, a biquaternion or a split-biquaternion shows at once which unit each term carries, the coefficients take the labels of the directions in place of the numbers: $Q_t$ with $e_t$, and $Q_x, Q_y, Q_z$ with $\vec e_x, \vec e_y, \vec e_z$. A sum over the four therefore runs over those labels,

$$
\tilde Q = \sum_{\mu \in \{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $\mu$ the label and $e_\mu$ the unit it carries — the arrowless $e_t$ at $\mu = t$ and the arrowed $\vec e_\mu$ at $\mu = x, y, z$. The same rule reads a quaternion, $\tilde q = \sum_{\mu} q_\mu e_\mu$, and a four-vector of the algebra, and the primed coefficients follow the same labels, $Q_\mu = q_\mu + iq'_\mu$: the label marks the direction and the prime marks the slot that carries the $i$.

**A complex element carries a majuscule**, $Q$, the case naming the scalar sector: an upper-case glyph has a scalar sector larger than the reals, a lower-case one has the reals. **The second coordinate of a complex element carries a prime**, $Q = q + iq'$, with $j$ in place of $i$ for the split-complex numbers and $\varepsilon$ for the dual numbers; a second and a third complex element are $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. **The four quaternionic elements carry a tilde**: lower case for the quaternions and the split-quaternions, $\tilde q$, and upper case for the biquaternions and the split-biquaternions, $\tilde Q$. The reduced biquaternion element carries **no tilde but the breve**: its algebra has no quaternionic factor, being the commutative two-parameter system over the complex scalars, and it is written $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$, the ascending triangle for the coefficient of $1$ and the descending triangle for the coefficient of $j$, with the two complex coordinates $Q_{\blacktriangle} = q_{\blacktriangle} + iq'_{\blacktriangle}$ and $Q_{\blacktriangledown} = q_{\blacktriangledown} + iq'_{\blacktriangledown}$, the second unit $j$ being the hyperbolic unit of the corpus, $j^{2} = +1$ and $ji = ij$, so that the basis is $1, i, j, ij$. And **the arithmetic systems and the reals carry a letter that is theirs alone**: $\alpha, \beta$ the Booleans, $n, m$ the naturals and the integers, and $q, q_1, q_2$ the rationals and the reals — a letter, no prime, no tilde, no coefficient sector, since these elements are not written as linear combinations. Finally, **the element is a scalar part plus, where the layer has one, a vector part**: the scalar part is carried by the unit — $1$ in the commutative two-parameter systems, $e_t$ in the quaternionic ones — and the vector part, in the quaternionic layers alone, by the remaining basis directions, carrying the arrow, $\vec q$ or $\vec Q$, so that $\tilde Q = Q_te_t + \vec Q$ is written in the coefficients according to the system; in the commutative two-parameter systems the second term is an imaginary, hyperbolic or dual part and not a vector part; in the quaternionic layers the two are the fixed and the anti-fixed spaces of the intrinsic conjugate, and the arithmetic systems, which are not written as linear combinations, have no vector part. **A pure element carries the arrow.** A pure element is one with no scalar part, a vector of its layer, and it is written with the arrow of the vector part: $\vec q$ and $\vec Q$ are the pure elements of the quaternion and of the biquaternion layers, standing by themselves (§*Pure Elements and their Coefficients*). The arrow names the vector part of a named element, $\vec Q$ in $\tilde Q = Q_te_t + \vec Q$, and it names the same object when the element is read on its own; the arrow and the tilde are never stacked.

For the biquaternions, whose basis is $e_t, \vec e_x, \vec e_y, \vec e_z$ with $e_t = 1$ the unit,

$$
\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z, \qquad Q_\mu = q_\mu + iq'_\mu,
$$

where the four coefficients $Q_\mu$ are complex, and each of them splits into a real part $q_\mu$ and an imaginary part $q'_\mu$. **The two parts of a coefficient share its letter**, the imaginary part carrying a prime. The shape is the same in the quaternion systems; only the coefficient sector changes, and the table above gives the element and the coefficients of each system. The unit $e_t$ is the identity in the two quaternion systems, and the real and the imaginary part of a coefficient may be read off only where the scalar sector is larger than the reals, which is the case in $\mathbb{C}$ and $\mathbb{B}$ and not in $\mathbb{R}$ or $\mathbb{H}$.

The case and the tilde are read independently, and the glyph of a generic element is the two together: $q$ is real, $Q$ complex, split-complex or dual, $\breve Q$ reduced biquaternion — upper case, with the breve, no tilde, and two complex coordinates — $\tilde q$ quaternion or split-quaternion, $\tilde Q$ biquaternion or split-biquaternion.

**A matrix carries no tilde, and neither does an array of elements.** The tilde marks the element, never the array that holds it: $\mathsf{M}_2(\tilde Q)$ keeps the tilde inside the argument, $I_n$ and $\mathsf{M}_4$ carry none, and an array of biquaternions, $\mathsf{Q}=(\tilde Q_{\lambda\rho})\in\mathbb{B}^{n\times m}$, carries none either, its entries carrying theirs. A tilde on a matrix or on an array is forbidden: it is a defect, not a variant. A matrix of a model takes a letter of its own and never a glyph of the Q family: the matrix of an element is written $\mathsf{M}_2(\tilde Q)$, and a matrix parameter is written $A$, $B$ or $M$, the letter $Q$ staying with the element.

**The generic element of the biquaternion algebra is written $\tilde{Q}$, and only the Q family is generic there.** No letter outside the family, at any case, with any subscript, in any article, stands for an arbitrary element of the algebra: a letter outside the family names a specific object, or an element bound where it is introduced. A statement that holds for every element is written with $\tilde Q$; a statement that needs two writes them $\tilde Q_1$ and $\tilde Q_2$, and a third takes the next number. The trace pairing is $\operatorname{Tr}(\tilde Q_1\tilde Q_2) = 2\operatorname{Sc}(\tilde Q_1\tilde Q_2)$, the commutator bracket $[\tilde Q_1, \tilde Q_2] = \tilde Q_1\tilde Q_2 - \tilde Q_2\tilde Q_1$, the general plain bilinear form $\langle\tilde Q_1, \tilde Q_2\rangle$ and the multiplicativity $\langle\tilde Q_1\tilde Q_2\rangle_{\natural} = \langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, inherited from *Idempotents of the General Plain Algebra* and its companions, which write the generic element $\tilde Q$ beside the idempotent $\tilde\Pi$. The argument of an operator, the dummy of an annihilator, the second entry of a bracket and the element a map is applied to carry the same glyph: $L_{\tilde Q_1}(\tilde Q_2) = \tilde Q_1 \bullet \tilde Q_2$, $\{\tilde Q_2 : \tilde Q_1 \star \tilde Q_2 = 0\}$, $[\tilde Q_1, \tilde Q_2]$. The letters $X$, $Y$, $Z$ and $W$ name no element of the algebra: $X$ is kept for the universal cover $X^{\mathrm{cov}}$ and the left-invariant field, and $Y$, $Z$, $W$ are free of any element role. **In the layers of the biquaternion family the glyph $Q$ belongs to the element and never to an operator.** An operator generated by an element carries the structural capital and the element's own glyph in the subscript, $L_{\tilde Q}$, $R_{\tilde Q}$, $\Theta_{\tilde Q}$; an operator that is not the multiplication by an element takes the matrix letter $A$, with $T$ for its argument, so that a sandwich reads $H_A(T)=ATA^{\dagger}$. A bare $Q$ is never written for such an operator.

Where the constructions that share a glyph must be told apart — the complex from the split-complex and the dual, the quaternion from the split-quaternion, the biquaternion from the split-biquaternion — the glyph is qualified by a subscript, as in $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{H}_{\mathbb{D}}$.

**The letters of the mathematical quantities.** The glyphs of the elements are kept for the algebra, and a quantity that would borrow one is written with a letter of its own. The **quadratic form** takes the Fraktur $\mathfrak{Q}$ — Fraktur is already the script of a distinguished object here, as in $\mathfrak{a}$, $\mathfrak{p}$ and $\mathfrak{k}$, and the letter is free of every other use — so that the plain $q$ and $Q$ stay with the elements; its polarisation is written with the bracket $\langle\cdot,\cdot\rangle$, with $\mathfrak{Q}(v)=\langle v,v\rangle$, so that no letter is spent on it. The **null quadric** takes the calligraphic $\mathcal{Q}$, as in $\mathcal{Q}^{n+1}$, and the **signature indices** take $n$ and $m$, as in $\mathrm{Cl}_{n,m}$ and $O(n,m)$; the table of §*Notational Conventions* lists the three with the other quantities, and where a quantity is itself an element of the algebra it carries the glyph of an element.

**A logarithm carries the glyph of its element and the subscript $\log$.** The logarithm is not a new kind of object: it is a solution of the exponential equation in the same algebra, so it carries the glyph of that algebra and the subscript, and the definition reads $\exp(Q_{\log}) = Q$. The glyph is $Q_{\log}$ for a complex, split-complex or dual element, $\tilde q_{\log}$ for a quaternion or split-quaternion, $\tilde Q_{\log}$ for a biquaternion or split-biquaternion, and $\breve Q_{\log}$ for a reduced biquaternion. The subscript is a word, not a letter, so it competes neither with the direction labels, $Q_t$ and $Q_x$, nor with the counts, $Q_1$; a numbered element keeps its number in front of the subscript, $\tilde Q_{1\log}$ and $\breve Q_{2\log}$, as its coefficients keep theirs. The subscript is dropped when the logarithm is written as an operator, $\log Q$ or $\operatorname{Log}Q$, because an operator carries no subscript. **The coordinates of a logarithm follow the coefficient rule**: the element $Q_{\log}=q_{\log}+iq'_{\log}$ has real part $q_{\log}$ and imaginary part $q'_{\log}$, with $j$ in place of $i$ in the split-complex case. The prime marks the imaginary coordinate and nothing else. The logarithm of a real number is the ordinary real logarithm and takes no glyph of an algebra, so it is written $\log q$; the glyph $q_{\log}$ is the real coordinate of $Q_{\log}$, not the logarithm of $q$.

## Pure Elements and their Coefficients

A **pure element** is an element with no scalar part. The notion belongs to the four quaternionic layers alone. In these layers the scalar part is carried by $e_t$, so a pure element is one whose $e_t$-coefficient vanishes and which is carried by the three vector directions alone. The pure elements are exactly the elements of the **vector subspace** $\mathrm{Vect}$, the anti-fixed space of the intrinsic conjugate,

$$
\vec q^{\natural} = -\vec q, \qquad \vec Q^{\natural} = -\vec Q,
$$

so a pure real quaternion is a vector of $\mathbb{R}^{3}$ and a pure biquaternion an element of a complex vector space of real dimension six. **The layers $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{B}_{\mathrm{r}}$ have no vector part**, so they have no pure element: their element is a scalar part beside an imaginary, hyperbolic or dual part — in $\mathbb{B}_{\mathrm{r}}$, the $j$-part $jQ_{\blacktriangledown}$ — and that second part is not a vector of anything.

**The glyph drops the tilde and carries the arrow.** The tilde marks the quaternionic factor of an element that is read with its scalar part beside its vector part; a pure element is read on its vector part alone, so it is written with the arrow and without the tilde, $\vec q$ in the quaternion and split-quaternion layers and $\vec Q$ in the biquaternion and split-biquaternion ones. The case is unchanged, and the arrow is the only mark: the vector part of a named element and a pure element standing by itself are one object, written with the one glyph, so a pure element is never written with a tilde.

**The arrow is reserved for pure elements.** Three rules follow from this. First, **the arrow marks a pure element and nothing else**: an element with a nonzero scalar part is never written with an arrow, whatever its magnitude or its role. Second, **a unit element carries the arrow only if it is pure**: the unit pure quaternion $\vec u$ and the unit pure biquaternion $\vec U$ carry it, whereas a unit element that has a scalar part — a rotor $\tilde q$ of unit norm, say — carries no arrow, its unit length being carried by the construction that names it. Third, **a unit in the direction of an element takes that element as a subscript**, written $\vec u_{e}$ as in $\vec u_B$ for the unit along the field $B$; the subscript names the element whose direction is taken, and the arrow on $\vec u$ records that the unit is pure.

| System | Name | Pure element | Pure unit element | Scalar part | Coefficients |
|---|---|---|---|---|---|
| $\mathbb{H}$ | Quaternions | $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $\vec u$ | $q_t = 0$ | Real, $q_\mu$ |
| $\mathbb{H}_{\mathrm{s}}$ | Split-quaternions | $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $\vec u$ | $q_t = 0$ | Real, $q_\mu$ |
| $\mathbb{B}$ | Biquaternions | $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $\vec U$ | $Q_t = 0$ | Complex, $Q_\mu = q_\mu + iq'_\mu$ |
| $\mathbb{H}_{\mathbb{D}}$ | Split-biquaternions | $\vec Q = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $\vec U$ | $Q_t = 0$ | Split-complex, $Q_\mu = q_\mu + jq'_\mu$ |

Three rules are read off the table. **A pure element is the vector part of an element read on its own.** For $\tilde q = q_te_t + \vec q$ the vector part $\vec q$ is a pure quaternion, and for $\tilde Q = Q_te_t + \vec Q$ the vector part $\vec Q$ is a pure biquaternion; the vector part of a named element and a pure element standing by itself are one object, and the arrow names both. **A pure element is anti-fixed by the intrinsic conjugate**, $\vec q^{\natural} = -\vec q$, having no scalar part to be fixed; the quaternionic layers are the only ones where this splitting leaves three directions to be pure in. **The arrow marks purity, not magnitude.** A pure element is of arbitrary magnitude; a unit pure element — a unit pure quaternion $\vec u$ — carries no second mark, its unit length being carried by the construction.

**The pure glyphs.** The arrow is laid on the glyph of a special element on the same case rule that governs the layer: the pure root is $\vec\Xi$ in the biquaternion and split-biquaternion layers and $\vec\xi$ in the quaternion and split-quaternion ones, and the pure nilpotent is $\vec\Upsilon$ in the biquaternion and split-biquaternion layers and $\vec\nu$ in the quaternion and split-quaternion ones.

**The arrow has priority over the tilde.** Where an element is pure, the arrow is written whatever else the element is, and the tilde of a special glyph is dropped: a pure root is $\vec\Xi$ and a pure nilpotent is $\vec\Upsilon$ (or $\vec\xi$ and $\vec\nu$ in the quaternion layers), never $\tilde\Xi$ or $\tilde\Upsilon$. The tilde belongs to the general element, read with its scalar part beside its vector part, and a pure element has no scalar part to be read against; purity therefore decides the mark. The special conventions that write the root $\tilde\Xi$ or the nilpotent $\tilde\Upsilon$ name the **general** element of that class, which need not be pure, and an element that is at once special and pure is written with the arrow and only the arrow.

A pure glyph is given from the quaternions to the biquaternions only. The layers with no quaternionic factor have no vector subspace, hence no pure element and no arrow: their second term is an imaginary, hyperbolic, dual or $j$-part carried by one coefficient — real in $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$, complex in $\mathbb{B}_{\mathrm{r}}$ — and written $Q = q + iq'$, with $j$ or $\varepsilon$ in place of $i$, in the three two-dimensional layers.

## The Conjugations

The biquaternion algebra carries three natural involutions, and the anti-Hermitian sign derived from them, all of them used in the series:

| Map | Mark | What it is |
|---|---|---|
| Complex conjugation | $\bar{\cdot}$ | The involution of the base, extended to the element |
| Quaternion conjugation | ${}^{\natural}$ | The intrinsic conjugate: it fixes the scalars and negates the vectors |
| Hermitian conjugation | ${}^{*}$ | The involution of the algebra, $\bar{\cdot}\circ{}^{\natural}$ |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | The negative of the star |

Outside the quaternionic layers there is no vector part. In $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$ the imaginary, hyperbolic and dual units are the coefficient sector itself, conjugated by the bar, so the natural sign is the identity and the star is the bar, $*=\bar{\cdot}$. $\mathbb{B}_{\mathrm{r}}$ is commutative and has no vector part as well, but its second line is not the coefficient sector: the coefficients are complex and the bar leaves $j$ fixed, so the bar and the identity do not exhaust the involutions, the natural sign has no sense and is not written. The intrinsic conjugation of the layer is the **tessarine sign** ${}_{\mathrm{ts}}$, $\breve Q_{\mathrm{ts}}=Q_{\blacktriangle}-jQ_{\blacktriangledown}$, $\mathbb{C}$-linear and of square one, and the star is its composite with the bar, ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$, $\breve Q^{*}=\bar Q_{\blacktriangle}-j\bar Q_{\blacktriangledown}$.

Which of the marks has a sense depends on the system, since a mark degenerates wherever the structure it conjugates is absent. The examples below fix it system by system.

**The complex numbers $\mathbb{C}$.** Only the bar has a sense, the algebra carrying a single non-trivial involution:

$$
\bar Q = q - iq' .
$$

**The split-complex numbers $\mathbb{D}$.** Only the bar has a sense:

$$
\bar Q = q - jq' , \qquad j^2 = +1 .
$$

**The quaternions $\mathbb{H}$ and the split-quaternions $\mathbb{H}_{\mathrm{s}}$.** Only the natural sign has a sense, the coefficients being real and the conjugation intrinsic to the quaternion factor, and the same formula is read on the two sets of units:

$$
\tilde q^{\natural} = q_te_t - q_x\vec e_x - q_y\vec e_y - q_z\vec e_z , \qquad \vec e_k^2 = -e_t \ (\mathbb{H}) , \qquad \vec e_x^2 = -e_t , \ \vec e_y^2 = \vec e_z^2 = +e_t \ (\mathbb{H}_{\mathrm{s}}) .
$$

**The biquaternions $\mathbb{B}$ and the split-biquaternions.** All four have a sense, the bar conjugating the coefficient, complex in $\mathbb{B}$ and split-complex in the split-biquaternions:

$$
\bar{\tilde Q} = \bar Q_te_t + \bar Q_x\vec e_x + \bar Q_y\vec e_y + \bar Q_z\vec e_z , \qquad \tilde Q^{\natural} = Q_te_t - Q_x\vec e_x - Q_y\vec e_y - Q_z\vec e_z ,
$$

$$
\tilde Q^{*} = \overline{\tilde Q^{\natural}} = \bar Q_te_t - \bar Q_x\vec e_x - \bar Q_y\vec e_y - \bar Q_z\vec e_z , \qquad \tilde Q^{\flat} = -\tilde Q^{*} .
$$

**The reduced biquaternions $\mathbb{B}_{\mathrm{r}}$.** The coefficients are complex, so the bar has a sense; the layer has no vector part, so the quaternion conjugation has none, and the intrinsic conjugation is the tessarine sign:

$$
\breve Q_{\mathrm{ts}} = Q_{\blacktriangle} - jQ_{\blacktriangledown} , \qquad \breve Q^{*} = \overline{\breve Q_{\mathrm{ts}}} = \bar Q_{\blacktriangle} - j\bar Q_{\blacktriangledown} , \qquad \breve Q_{\mathrm{ts}}\breve Q = Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2} .
$$

The maps of the layer are the bar, the tessarine sign, the star that is their composite, and the derived anti-Hermitian sign; the natural sign is not written on it.

## The Special Elements: Root, Idempotent and Nilpotent

**The special glyphs are notational.** A root $\tilde\Xi$, an idempotent $\tilde\Pi$ or a nilpotent $\tilde\nu$ is not a different kind of object from a generic $\tilde Q$: the glyph records what the element is known to be, at the point of use.

### The Root Convention

The roots carry a symbol of their own, beside the idempotent $\tilde\Pi$ (§*The Idempotent Convention*) and the nilpotent $\tilde\nu$ (§*The Nilpotent Convention*): the **xi**, in the two cases.

A **root of $1$** of the algebra is an element $\tilde\Xi$ with $\tilde\Xi^2 = 1$. More generally a **root of a central value** $\lambda$ is an element with $\tilde\Xi^2 = \lambda e_t$; the roots of the three central values $-1, 0, +1$ are determined in *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general problem is *Square Roots of a General Element in the Biquaternion Algebra*.

**The square is read in a named product**, the algebra product unless the statement names another, as for the nilpotents: the class is relative to the product, and the roots of a value are read product by product in *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The case rule splits the glyph, as it does for the elements, the idempotents and the nilpotents.** The roots of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde\Xi$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde\xi$; those of the complex, split-complex and dual layers carry the plain capital, $\Xi$; and those of the reduced biquaternion layer carry the same plain capital, $\Xi$, no tilde being written where there is no quaternionic factor.

**The coordinates carry the letter of the root**: in $\mathbb{B}$ the root is $\tilde\Xi = \Xi_te_t + \Xi_x\vec e_x + \Xi_y\vec e_y + \Xi_z\vec e_z$ with $\Xi_\mu = \xi_\mu + i\xi'_\mu$, its scalar part $\Xi_t$ and its vector part $\vec\Xi = \vec\xi + i\vec\xi'$; in $\mathbb{H}$ it is $\tilde\xi = \xi_te_t + \xi_x\vec e_x + \xi_y\vec e_y + \xi_z\vec e_z$ with real $\xi_\mu$.

**It is allowed to add subscripts when several roots are used.** **The subscript of a root is numeric when it counts and a role label when it names.** Where more than one occurs the roots are numbered, $\tilde\Xi_1, \tilde\Xi_2$, as for the nilpotents and for the idempotent pairs other than the complete sign pair of §*The Idempotent Convention*; where a root plays a named role, it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The root glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\Xi$ | A root of $1$ of the complex, split-complex or dual layer, where no tilde is written |
| $\Xi_\pm$ | A root of $1$ of the reduced biquaternion layer, where no tilde is written |
| $\tilde\xi$ | A root of $1$ of the quaternion or split-quaternion layer |
| $\tilde\Xi$ | A root of $1$ of the biquaternion or split-biquaternion layer |

### The Idempotent Convention

The convention of *The Elements and their Coefficients* fixes the case and the tilde of a generic element. The idempotents carry a symbol of their own, and the corpus uses it throughout.

An **idempotent** of the algebra is an element $\tilde\Pi$ with $\tilde\Pi^2 = \tilde\Pi$, and a **projector** is an idempotent operator, $p^2 = p$, that is an idempotent of the morphism space, not an element of the algebra; the two are different objects, and an idempotent element corresponds to a projector when its multiplication operator is idempotent. An idempotent fixed by the star, $\tilde\Pi^{*} = \tilde\Pi$, is a **Hermitian idempotent**, and the rank-one Hermitian idempotents of $\mathbb{M}_+$, the Hermitian subspace, are the **pure states**.

**The case rule splits the glyph, as it does for the elements.** The idempotents of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde\Pi$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde\pi$; those of the complex, split-complex, dual and reduced biquaternion layers carry the plain capital, $\Pi$, no tilde being written where there is no quaternionic factor. The same splitting of the identity is written $\tilde\pi_{1,2}$ in $\mathbb{H}_{\mathrm{s}}$ (*Split-Quaternion Idempotents and Projections*), while the split-complex layer $\mathbb{D}$ (*Square Roots of One and the Idempotents of the Split-Complex Algebra*) and the reduced biquaternion layer $\mathbb{B}_{\mathrm{r}}$ write the complete pair with the signs, $\Pi_\pm$, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$; the idempotents of the split-biquaternion layer are the $\tilde\Pi_{1,2}$ of *Split-Biquaternion Idempotents and Projections*, and the layer fixes the glyph.

The involution here is the star on the elements, as *The Conjugations* fixes it, and *Conventions in the Biquaternion Universe* writes the same involution with the same star, $\tilde\Pi^{*} = \tilde\Pi$: the two corpora agree on the mark, and it is the dagger that is confined to the operators.

**The coordinates carry the letter of the idempotent**: in $\mathbb{B}$ the idempotent is $\tilde\Pi = \Pi_te_t + \Pi_x\vec e_x + \Pi_y\vec e_y + \Pi_z\vec e_z$ with $\Pi_\mu = \pi_\mu + i\pi'_\mu$, its scalar part $\Pi_t$ and its vector part $\vec\Pi = \vec\pi + i\vec\pi'$; in $\mathbb{H}$ it is $\tilde\pi = \pi_te_t + \pi_x\vec e_x + \pi_y\vec e_y + \pi_z\vec e_z$ with real $\pi_\mu$.

**It is allowed to add subscripts when several idempotents are used.** **The subscript of an idempotent is numeric when it counts and a role label when it names, but for the two members of a complete sign pair.** A pair is $\tilde\Pi_1, \tilde\Pi_2$; a second pair occurring in the same statement takes the next numbers, $\tilde\Pi_3, \tilde\Pi_4$; and a family indexed by a direction is written with its argument, $\tilde\Pi_\pm(\tilde\Xi)$. When a pair is **complete**, $\tilde\Pi_+ + \tilde\Pi_- = e_t$, its two members may be written $\tilde\Pi_+$ and $\tilde\Pi_-$, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$. A pair that is not complete may be numbered, labelled or signed as the statement requires. A role label is written in upright roman, as for a unit element. The split-complex and reduced biquaternion layers write their complete pair with the signs throughout, $\Pi_\pm$. The Peirce indices of the reduced biquaternion layer are the same signs, $\mathbb{B}_{\sigma\tau}=\{\breve Q:\Pi_\sigma \breve Q\Pi_\tau=\breve Q\}$ with $\sigma,\tau\in\{+,-\}$, the two signs a pair read on the left and on the right, so that a corner such as $\mathbb{B}_{++}$ is never a coordinate and never a doubled label. The coordinates of the element in that pair are the **idempotent coordinates**, written with the sign of the member, $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, so that $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$; the sign marks a coordinate of the idempotent pair and the triangle a basis coordinate, so that a numbered element is read the same way, $Q_{1+}$ and $Q_{1-}$ for the idempotent coordinates of $\breve Q_{1}$ and $Q_{1\blacktriangle}$ and $Q_{1\blacktriangledown}$ for its basis coordinates.

A non-zero idempotent $\tilde\Pi$ generates the **minimal left ideal** $\mathbb{B}\tilde\Pi$; the standard pair, the classification of the idempotents, the polarisation identity, the Peirce decomposition, the matrix units and the projective geometry of the pure states are those of *Idempotents of the General Plain Algebra* and its companions.

The idempotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\Pi$ | An idempotent of the complex, split-complex or dual layer, where no tilde is written |
| $\Pi_\pm$ | A complete sign pair of idempotents of the split-complex or reduced biquaternion layer, where no tilde is written |
| $\tilde\pi$ | An idempotent of the quaternion or split-quaternion layer |
| $\tilde\Pi$ | An idempotent or a pure state of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde\Pi$ it generates |

### The Nilpotent Convention

The nilpotents carry a symbol of their own, beside the idempotent $\tilde\Pi$ (§*The Idempotent Convention*): the lower-case $\tilde\nu$ of the quaternion and split-quaternion layers and the upper-case $\tilde\Upsilon$ of the biquaternion and split-biquaternion layers, as the case rule requires. **The capital is an upsilon and not a $Y$.**

A **nilpotent** of the algebra is an element $\tilde\nu$ whose square vanishes,

$$
\tilde\nu^2 = 0 .
$$

**The square is read in a named product**, the algebra product unless the statement names another: the corpus writes nilpotents in the four general products of *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* as well, and the class is relative to the product — an element square-zero in the plain product need not be square-zero in the general plain sesquilinear one, and in the plain antisymmetric block every central element is square-zero, the unit among them. **No nilpotent is a Hermitian idempotent**, a Hermitian nilpotent being zero, so no nilpotent is a pure state; it is nevertheless the partner of the idempotent in a minimal left ideal — for the standard pair $\mathbb{B}\vec\Upsilon_2 = \mathbb{B}\tilde\Pi_1$ — and its products with its star are Hermitian idempotents of that ideal.

**The coordinates carry the letter of the nilpotent**: in $\mathbb{B}$ the nilpotent is $\tilde\Upsilon = \Upsilon_te_t + \Upsilon_x\vec e_x + \Upsilon_y\vec e_y + \Upsilon_z\vec e_z$ with $\Upsilon_\mu = \nu_\mu + i\nu'_\mu$, its scalar part $\Upsilon_t$ and its vector part $\vec\Upsilon = \vec\nu + i\vec\nu'$; in $\mathbb{H}$ it is $\tilde\nu = \nu_te_t + \nu_x\vec e_x + \nu_y\vec e_y + \nu_z\vec e_z$ with real $\nu_\mu$.

**It is allowed to add subscripts when several nilpotents are used.** **The subscript of a nilpotent is numeric when it counts and a role label when it names**, as for the idempotents apart from their complete sign pair: where more than one occurs a pair is $\tilde\nu_1, \tilde\nu_2$, a second pair in the same statement takes the next numbers, and where a nilpotent plays a named role it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The nilpotents have no classification of the idempotent kind. The square-zero set is not one family, and which set it is depends on the product: the elements of zero norm under the general quaternionic product, the pure isotropic vectors under the associative one. The standard units and the instances are those of *Nilpotents of the General Quaternionic Algebra*, *Idempotents of the General Plain Algebra* and *Ideals and Peirce Decompositions of the Biquaternion Algebra*. The standard pair of nilpotents is the two off-diagonal Peirce units of the last of these, $\vec\Upsilon_1$ and $\vec\Upsilon_2$, exchanged by the star.

The nilpotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\Upsilon$ | A nilpotent of the complex, split-complex or dual layer, where no tilde is written |
| $\tilde\nu$ | A nilpotent of the quaternion or split-quaternion layer |
| $\tilde\Upsilon$ | A nilpotent of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde\Upsilon$ it generates |
| $\vec\Upsilon$, $\vec\nu$ | A pure nilpotent, written with the arrow and without the tilde by the priority rule of §*Pure Elements and their Coefficients* |

**The standard pair carries the arrow, not the tilde.** The two off-diagonal Peirce units are pure, $\vec\Upsilon_1 = \tfrac12(i\vec e_x - \vec e_y)$ and $\vec\Upsilon_2 = \tfrac12(i\vec e_x + \vec e_y)$, with no scalar part, so by §*Pure Elements and their Coefficients* the arrow takes priority over the tilde and the tilde is dropped; the pair is written $\vec\Upsilon_1, \vec\Upsilon_2$ and never $\tilde\Upsilon_1, \tilde\Upsilon_2$. The tilde is kept for the general nilpotent $\tilde\Upsilon$, which may carry a scalar part and is not pure.

## The Twelve Products and Their Names

The algebra carries **four general products** — one to each of the four choices of the two slots, the first factor read as it stands or through ${}^{\natural}$ and the second as it stands or through ${}^{*}$ — and each of the four splits into a **symmetric part** and an **antisymmetric part**, so that the complex space carries **twelve products** in all. The names are these, with the three-letter code the band articles write them by:

| The general product | Its symmetric part | Its antisymmetric part |
|---|---|---|
| The general plain bilinear product ($\mathrm{GPA}$) | The symmetric plain bilinear product ($\mathrm{SPA}$) | The antisymmetric plain bilinear product ($\mathrm{APA}$) |
| The general quaternionic bilinear product ($\mathrm{GQA}$) | The symmetric quaternionic bilinear product ($\mathrm{SQA}$) | The antisymmetric quaternionic bilinear product ($\mathrm{AQA}$) |
| The general plain sesquilinear product ($\mathrm{GPS}$) | The symmetric plain sesquilinear product ($\mathrm{SPS}$) | The antisymmetric plain sesquilinear product ($\mathrm{APS}$) |
| The general quaternionic sesquilinear product ($\mathrm{GQS}$) | The symmetric quaternionic sesquilinear product ($\mathrm{SQS}$) | The antisymmetric quaternionic sesquilinear product ($\mathrm{AQS}$) |

**The code is read letter by letter.** The first letter says which of the three operations of a row — $\mathrm G$ the general product, $\mathrm S$ its symmetric part, $\mathrm A$ its antisymmetric part; the second says which of the two products — $\mathrm P$ the plain one, whose first slot is read as it stands, and $\mathrm Q$ the one whose first slot carries the intrinsic conjugation, ${}^{\natural}$ in the quaternionic layers and ${}_{\mathrm{ts}}$ in $\mathbb{B}_{\mathrm{r}}$; and the third says the family — $\mathrm A$ the **algebra** over $\mathbb{C}$, whose three products are $\mathbb{C}$-bilinear, and $\mathrm S$ the **sesqualgebra** over $(\mathbb{C},\bar{\cdot})$, whose three products are sesquilinear. The four general products are the multiplications of the four general structures; the eight parts are the symmetric and antisymmetric products beside them; and the twelve codes together name the twelve algebraic structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The same code on the reduced biquaternion space.** The construction is not special to $\mathbb{B}$. On the commutative algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C}$ — the reduced biquaternions, equivalently the tessarines or the double-complex numbers — the same four general products exist, $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$, and each splits into a symmetric and an antisymmetric part by the two exchanges. Because the algebra is **commutative**, four of the twelve codes name no new operation there: $\mathrm{SPA} = \mathrm{GPA}$ and $\mathrm{SQS} = \mathrm{GQS}$, while $\mathrm{APA} = 0$ and $\mathrm{AQS} = 0$. The space therefore carries **eight distinct algebraic structures** — $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ and the four live halves $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ — and the twelve slots, the four that collapse and the eight that remain are *The Four Products, Their Forms and Their Algebraic Norms* and *The Specificities of the Algebra of the Reduced Biquaternions*. The letter $\mathrm Q$ keeps its sense there — the first slot read through ${}_{\mathrm{ts}}$, the tessarine conjugation $j\mapsto-j$ (and $ij\mapsto-ij$) — as in the band above.

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

The products themselves — their coordinates, their laws, their units and their images — are *Symmetric and Antisymmetric Decomposition of the Four General Products*, and the grid of the four general products is *The Four General Products and Their Relations over the Biquaternion Algebra*.

## The Form Convention, the Norm Convention and the Unitary Convention

The corpus writes a **generic form** and a **generic norm**, the norm being the form read at its two equal arguments:

$$
\mathrm{Form}(\tilde Q_1,\tilde Q_2) , \qquad \mathrm{Norm}(\tilde Q) = \mathrm{Form}(\tilde Q,\tilde Q) .
$$

**One bracket, two arities.** A **bracket** names a **form** when it carries two arguments and its **algebraic norm** when it carries one, the single argument standing for the two equal ones. Each form is built from its own conjugation in the first argument and its own in the second, and the bracket's subscript records the two. Written out, the **plain form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2) , \qquad \langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle ,
$$

the **quaternionic form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2) , \qquad \langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural} ,
$$

the **Hermitian form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}) , \qquad \langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*} ,
$$

and the **Krein form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*}) , \qquad \langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*} .
$$

**The bracket carries the mark that is not the identity in the layer**, and the four brackets collapse two-and-two wherever one mark degenerates. The cases are worked layer by layer in §*The Six Layer Tables*, below.

The distinction is one of **notation, not of substance**: the pair is the form and the norm of the statement at hand. The two definitions — the form of an operation as its scalar part read in two arguments, bilinear or sesquilinear by its second slot, and the algebraic norm as that form at its two equal arguments — and the four brackets, $\langle\cdot,\cdot\rangle$ the plain, $\langle\cdot,\cdot\rangle_{*}$ the Hermitian, $\langle\cdot,\cdot\rangle_{\natural}$ the quaternionic and $\langle\cdot,\cdot\rangle_{\natural*}$ the Krein, are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

**The four names stand on the four norms, and the form is the norm read in two slots.** One name runs over the three levels of the product, the form and the norm: the **plain** bracket is the scalar part of the plain bilinear product, the **quaternionic** bracket that of the quaternionic bilinear product, the **Hermitian** bracket that of the plain sesquilinear product, and the **Krein** bracket that of the quaternionic sesquilinear product. Read on one argument the four are the **plain norm**, the **Hermitian norm**, the **quaternionic norm** and the **Krein norm**. The four products, their forms and their norms go together, one to a row:

| Product | Form | Norm |
|---|---|---|
| the general plain bilinear | $\langle\tilde Q_1,\tilde Q_2\rangle$ | the plain norm $\langle\tilde Q\rangle$ |
| the general quaternionic bilinear | $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | the quaternionic norm $\langle\tilde Q\rangle_{\natural}$ |
| the general plain sesquilinear | $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | the Hermitian norm $\langle\tilde Q\rangle_{*}$ |
| the general quaternionic sesquilinear | $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | the Krein norm $\langle\tilde Q\rangle_{\natural*}$ |

**The names are read in the layer where the map they mark exists.** In $\mathbb{B}_{\mathrm{r}}$ the **quaternionic** name becomes the **tessarine** and the **Krein** name the **tessarine-Hermitian**, their brackets carrying ${}_{\mathrm{ts}}$ and ${}_{\mathrm{ts}*}$; the plain and the Hermitian keep their names.

### The Six Layer Tables

**The four formulas are written on the biquaternion glyph, whose two marks are independent; when one mark degenerates the brackets collapse two-and-two, and in the reduced biquaternions no mark degenerates and the four remain distinct.** Each table below gives only the brackets that survive on the layer, with the norm they carry.

**One table per layer.** Each table reads the brackets that survive on the layer's own glyph. The **algebraic norm** is the diagonal of the form, the **realified signature** is that of the real quadratic form with the positive directions counted first, and the **role** records what the bracket does: the definite bracket carries the topology and the multiplicative one the invertibility criterion.

**The complex numbers $\mathbb{C}$**, $Q=q+iq'$.

| bracket | form | algebraic norm | realified signature | role |
|---|---|---|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | plain, also quaternionic | $\langle Q\rangle=Q^2\in\mathbb{C}$, $\operatorname{Re}\langle Q\rangle=q^2-q'^2$ | $(1,1)$ | anisotropic; real part indefinite |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | Hermitian, also Krein | $\langle Q\rangle_{*}=Q\bar Q=q^2+q'^2$ | $(2,0)$ | definite; multiplicative; topology |

In $\mathbb{C}$ the star bracket is definite and multiplicative at once. The plain norm is complex and anisotropic, $\langle Q\rangle=0$ only at $Q=0$; its real part is indefinite. The natural sign being the identity, the quaternionic bracket is the plain one and the Krein bracket the Hermitian one.

**The split-complex numbers $\mathbb{D}$**, $Q=q+jq'$, $j^2=+1$.

| bracket | form | algebraic norm | realified signature | role |
|---|---|---|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | plain, also quaternionic | $\langle Q\rangle=Q^2\in\mathbb{D}$, $\operatorname{Re}\langle Q\rangle=q^2+q'^2$ | $(2,0)$ | definite; topology; not multiplicative |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | Hermitian, also Krein | $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2$ | $(1,1)$ | multiplicative; invertibility; null cone |

The two brackets exchange their signatures with the sign of the square of the coefficient unit: $i^2=-1$ makes the real part of the plain norm indefinite and the star norm definite, while $j^2=+1$ does the reverse. Definite and multiplicative are split across the two brackets, and no single bracket is both, since $(1+j)(1-j)=0$ with $1\pm j\neq0$. The topological norm is therefore $\sqrt{\operatorname{Re}\langle Q\rangle}$, with no modulus sign, and the scale of the polar factor is $\sqrt{\lvert\langle Q\rangle_{*}\rvert}$, which is multiplicative on the units and is not a norm. Over the dual numbers $\mathbb{D}'$ the square of the coefficient unit vanishes and both brackets realify to the rank-one form $q^2$; the algebraic norm is degenerate, and the topology is the Euclidean form $q^2+q'^2$ of the coefficient plane, which is not one of the brackets.

**The modulus of an element is a square root of its algebraic norm**: $\sqrt{\langle Q\rangle_{*}}$ over $\mathbb{C}$ and $\mathbb{D}'$, and $\sqrt{\lvert\langle Q\rangle_{*}\rvert}$ over the indefinite $\mathbb{D}$; the modulus is written only through the algebraic norm.

**The reduced biquaternions $\mathbb{B}_{\mathrm{r}}$**, $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$; the marks are the bar and the tessarine sign ${}_{\mathrm{ts}}$, and ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$.

| bracket | form | algebraic norm | value | role |
|---|---|---|---|---|
| $\langle\breve Q_1,\breve Q_2\rangle=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | plain | $\langle\breve Q\rangle=Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2$ | complex | — |
| $\langle\breve Q_1,\breve Q_2\rangle_{\mathrm{ts}}=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | tessarine | $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | complex | multiplicative; invertibility; zero divisors |
| $\langle\breve Q_1,\breve Q_2\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | Hermitian | $\langle\breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^2-\lvert Q_{\blacktriangledown}\rvert^2$ | real, $(2,2)$ | indefinite |
| $\langle\breve Q_1,\breve Q_2\rangle_{\mathrm{ts}*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | tessarine-Hermitian | $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^2+\lvert Q_{\blacktriangledown}\rvert^2$ | real, $(4,0)$ | definite; topology |

The tessarine bracket carries the algebra and the tessarine-Hermitian bracket carries the topology. The norm $\langle\breve Q\rangle_{\mathrm{ts}}$ is the **reduced norm** of the layer: multiplicative, vanishing exactly on the zero divisors and at $0$, so $\breve Q$ is invertible if and only if that norm is non-zero, with $\breve Q^{-1}=\breve Q_{\mathrm{ts}}/\langle\breve Q\rangle_{\mathrm{ts}}$. The fourth bracket is definite, so it is not a Krein form. The plain and the tessarine norms are complex-valued.

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

**The biquaternions $\mathbb{B}$**, $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the marks $\bar{\cdot}$ and ${}^{\natural}$ are independent, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

| bracket | form | algebraic norm | value | realified signature | role |
|---|---|---|---|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | plain | $Q_t^2-Q_x^2-Q_y^2-Q_z^2$ | $\mathbb{C}$ | $(4,4)$ | complex cone |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ | quaternionic | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | $\mathbb{C}$ | $(4,4)$ | multiplicative; zero-divisor cone |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | Hermitian | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ | $\mathbb{R}$ | $(8,0)$ | definite; topology |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$ | Krein | $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$ | $\mathbb{R}$ | $(2,6)$ | indefinite |

The quaternionic norm is the determinant in the $2\times2$ image and is the multiplicative one, vanishing exactly on the zero-divisor cone; the Hermitian norm is the definite one and carries the topology; the plain and the Krein norms are the remaining two, complex and indefinite respectively. The signature column is that of the realified form on the eight real parameters; on the material sector the restrictions are those stated above. The split-biquaternion layer $\mathbb{H}_{\mathbb{D}}$ keeps the same four brackets, its coefficients being split-complex instead of complex, so the two bilinear norms take split-complex values and the two sesquilinear ones stay real.

**The one-line rule.** Write the bracket with the intrinsic conjugation of the layer: the star in $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$, where the natural sign is the identity; the natural sign in $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$, where the bar is the identity; the tessarine sign in $\mathbb{B}_{\mathrm{r}}$; and both marks, all four brackets, in $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$.

### The Unitary Convention

A unit element carries its own glyph, the **$u$** in the two cases, beside the root $\tilde\Xi$, the idempotent $\tilde\Pi$ and the nilpotent $\tilde\nu$: the letter $u$ is reserved for a unit element, and a general element is $\tilde q$ or $\tilde Q$. **The exponential is written $\exp(\cdot)$**, never $e^{\cdot}$, the letter $e$ being the base $e_t,\vec e_x,\vec e_y,\vec e_z$. A unit element is an element of norm one, and the norm is the one in view: the glyph is the generic norm read at the central value $e_t$, so it names no set until the norm is named, and the four norms of the biquaternion layer give four level sets:

| Norm | the condition $\mathrm{Norm}(\tilde U)=e_t$ | the norm-one elements |
|---|---|---|
| $\langle\tilde Q\rangle$ | $Q_t^2-Q_x^2-Q_y^2-Q_z^2=e_t$ | the complex hyperboloid of the plain norm |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2=e_t$ | $\mathbb{B}^{\times}_1$, the norm-one units |
| $\langle\tilde Q\rangle_{*}$ | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2=1$ | the unit sphere of the Hermitian norm |
| $\langle\tilde Q\rangle_{\natural*}$ | $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2=1$ | the indefinite level set of the Krein norm |

The two bilinear norms are complex-valued, so their condition is $=e_t$; the two sesquilinear norms are real-valued, so theirs is $=1$. In the quaternion layer the level set is $Sp(1)=\{\tilde u\in\mathbb{H}:\tilde u\tilde u^{\natural}=e_t\}=S^{3}=\mathrm{SU}(2)$, and **the rotors are these elements**: an orientation rotor, of norm $e_t$, is a unit real quaternion and is written $\tilde u$.

**The group condition is narrower than the norm-one condition.** Where the sesquilinear form is preserved, $\tilde U^{*}\tilde U=e_t$, the norm-one elements that do so form the **unitary group**, written without the tilde of an element,

$$
\mathrm{U}(\mathbb{B})=\{\tilde U:\tilde U^{*}\tilde U=e_t\}\cong \mathrm{U}(2)=S^{1}\cdot S^{3},\qquad S^{1}\cap S^{3}=\{\pm e_t\},
$$

of real dimension $4$. The name **unitary** is the name of that group; the glyph $\tilde U$ is the wider norm-one element. The norm and the group condition exist only where their involution does: the bar alone over $\mathbb{C}$ and the split-complex numbers, the natural sign alone over $\mathbb{H}$ and the split-quaternions, the bar, the tessarine sign and the star over $\mathbb{B}_{\mathrm{r}}$, and all four marks over $\mathbb{B}$ and the split-biquaternions.

**The case rule splits the glyph**, as for the elements: $\tilde U$ in the biquaternion and split-biquaternion layers, $\tilde u$ in the quaternion and split-quaternion ones, $U$ in the complex, split-complex, dual and reduced biquaternion ones. The pure case carries the arrow, $\vec u$ and $\vec U$.

**The coordinates carry the letter of the unit element**: in $\mathbb{B}$ it is $\tilde U = U_te_t + U_x\vec e_x + U_y\vec e_y + U_z\vec e_z$ with $U_\mu = u_\mu + iu'_\mu$ and vector part $\vec U = \vec u + i\vec u'$; in $\mathbb{H}$ it is $\tilde u = u_te_t + u_x\vec e_x + u_y\vec e_y + u_z\vec e_z$ with real $u_\mu$. **A coordinate carries the label of its direction**, as the base does: the scalar coordinate is $U_t$ and the vector coordinates are $U_x, U_y, U_z$, and likewise $u_t, u_x, u_y, u_z$ for the quaternion-layer element $\tilde u$; a role label is written in the upright roman where the statement names a role. **It is allowed to add subscripts when several unit elements are used**, $\tilde U_1, \tilde U_2$.

### The Letters $U$ and $u$ Outside the Layers

The reservation above is **local to the layers of the biquaternion family** — the complex, split-complex, dual and reduced biquaternion layers, the quaternion, split-quaternion, biquaternion and split-biquaternion layers, and the operator articles built on them. Inside them the glyphs $u$, $\tilde u$, $\vec u$, $U$, $\tilde U$ and $\vec U$ name unit elements and nothing else.

Outside them the letter keeps a single shape for a single meaning, and the font carries the distinctions the layers do not need. The **unitary group** and the **universal enveloping algebra** are upright roman, $\mathrm{U}(n)$, $\mathrm{U}(H)$, $\mathrm{U}(\mathbb B)$, $\mathrm{U}(\mathfrak g)$; the **group of units** of a ring is the sans-serif $\mathsf{U}(R)$, which the corpus more usually writes $R^{\times}$; a **family of sets** — an open cover, a filter, a uniformity — is the script $\mathcal U$; and the **up quark** and the **atomic mass unit** are the upright roman $\mathrm u$. The italic letters $U$ and $u$ are reserved: outside the layers they never name an open set, a flow or evolution operator, a horocycle, a Jordan quadratic representation, a dual element, an internal energy or an unknown function.

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

- A glyph read with its scalar part, four components: the tilde. The biquaternionic gradient $\tilde\nabla$ of §*The Gradient* is the algebraic example, and the canonical momentum $\tilde p=p_te_t+\vec p$ is the physical one.
- A pure glyph, three components: the arrow. The momentum operator $\vec p=-i\hbar\nabla=\vec e_kp_k$ is the physical example, and $\nabla=\vec e_k\,\partial/\partial Q_k$ is the fixed spatial gradient, which carries no second mark (§*The Gradient*).

The gradient decides the case cleanly: $\tilde\nabla$ is not pure, because its $e_t$ term carries $\partial/\partial Q_t$, while $\nabla$ is pure. The case follows the layer: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$; where the letter already names another object of the layer, a subscript or the explicit form $-i\hbar\vec\nabla$ fixes the operator.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the natural sign for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves; the tilde states a glyph read with its scalar part, which the adjoint also preserves. Where the adjoint in view is the formal algebraic one of the definite form, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$ and $\tilde\nabla^{\dagger}=\tilde\nabla^{*}=\tilde\nabla^{\natural}$. The identification is formal: the $L^2$ adjoint of a derivative carries the sign of the integration by parts, and it is not the dagger of this convention.

**An operator written as an array carries no tilde.** The element rule above governs an operator that acts on the algebra by multiplication, because such an operator is the element. An operator written as a linear map on a coordinate column, or as a matrix in the $2\times2$ image, is an array: it carries no tilde, its elements keep theirs inside the argument, $\mathsf{M}_2(\tilde Q)$, and its adjoint is the dagger and not the star. A Kraus operator, where the physics corpus uses one, is written in the element reading, $\tilde K_l\in\mathbb{B}$, because it multiplies the state on both sides; its matrix image $\mathsf{M}_2(\tilde K_l)$ carries no tilde.

**The Fock exception.** A Fock operator is not an element of the algebra; its superscript $\mathrm{fop}$ and the order of the two marks are fixed in §*The Superscripts*.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm r}$; it never denotes a derivative. The derivative with respect to a coordinate is written $\partial/\partial Q_\mu$, and in a fixed direction $\partial/\partial Q_t$, $\partial/\partial Q_x$, $\partial/\partial Q_y$ or $\partial/\partial Q_z$; a coordinate is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception, neither on a free index nor on any other. A derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the Lagrangian derivative puts the function in the numerator, $\partial L/\partial w$, so that where a PDE text writes $L_u$ and $L_p$ the calculus-of-variations and partial-differential-equation articles write $\partial L/\partial w$ and $\partial L/\partial p$; the second derivative has the same shape, $\partial^2 L/\partial w^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the operand is a compound expression rather than a single letter. The derivative $\partial/\partial Q_t$ is the derivative along the fourth coordinate: on the material sector, where $Q_t=iq'_t$, it equals $-i\,\partial/\partial q'_t$, and $q'_t$ is a real coefficient and not one of the coordinates, so the derivative with respect to it is written out as $\partial/\partial q'_t$.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.**

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dt}$ for the parameter $t$, $\frac{d}{d\tau}$ for the parameter $\tau$, $\frac{d}{dt_r}$ for the parameter $t_r$; inline, the same derivative is written $dq/dt$. The partial derivative is written $\frac{\partial}{\partial t}$ or, inline, $\partial/\partial t$. A higher derivative is written $\frac{d^2}{dt^2}$, $\frac{\partial^2}{\partial t^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{dx}{dt}\right)^2$, never as $\frac{dx^2}{dt}$.

**The prime marks the imaginary coordinate, and nothing else.** A prime marks the imaginary coordinate of a complex number: the second coefficient of a complex, split-complex or dual element, $Q = q + iq'$ in the complex case, and of a biquaternion coefficient, $Q_\mu = q_\mu + iq'_\mu$. It never marks a derivative: a function of one variable is differentiated as $df/dx$, a second derivative as $d^2f/dx^2$, and the value at a point as $\frac{df}{dx}(a)$; a derivative with respect to a coordinate is written $\partial/\partial Q_\mu$ (§*Conventions for Derivation*). No further use of the prime is admitted.

**Labels that are not derivatives.** The second Lorentz label is written $\bar l$, and a spinor index of the conjugate representation is written $\bar\alpha$; the bar on an index marks the conjugate spinor. The conjugate matrix is $\bar\Pi$. These are labels, not derivatives.

**The scope mark.** In geometric calculus the factor differentiated is marked with an underline, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$, not with a dot.

### The Gradient

**The two derivative operators of the corpus** are the **biquaternionic gradient** $\tilde\nabla$ and the **d'Alembertian** $\Box$; each carries a glyph of its own and is fixed here and in no other place, and every other partial derivative is written with $\partial$.

The coordinate derivative is written $\partial/\partial Q_\mu$ and is defined by

$$
\frac{\partial}{\partial Q_\mu}:=\frac{\partial}{\partial q_\mu}+\frac{\partial}{\partial(iq'_\mu)},\qquad Q_\mu=q_\mu+iq'_\mu,
$$

the $i$ being glued to the primed coordinate: the derivative is taken with respect to the product $iq'_\mu$, not with respect to $q'_\mu$ with the $i$ pulled out in front. It is the formal derivative on the complex coordinate; with $Q_\mu$ and $\bar Q_\mu$ read as independent, its unhalved normalization gives $\partial Q_\mu/\partial Q_\mu=2$ and $\partial Q_\mu/\partial\bar Q_\mu=0$. On a real sector, where the fields depend on the tangential coordinate alone, the normal derivative is absent; on the material sector, with $Q_t=iq'_t$, the symbol is read with the tangential derivative alone, $\partial/\partial Q_t=-i\,\partial/\partial q'_t$. The conjugate derivative is

$$
\frac{\partial}{\partial\bar Q_\mu}:=\frac{\partial}{\partial q_\mu}-\frac{\partial}{\partial(iq'_\mu)},
$$

with $\partial\bar Q_\mu/\partial\bar Q_\mu=2$. The **biquaternionic gradient** is the element-valued operator

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},
$$

whose tilde marks its scalar part beside its vector part (*Conventions in the Biquaternion Universe*, §*The Gradient*; *Biquaternion Analysis*), with its quaternion conjugate $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\,\partial/\partial Q_\mu$ and $\varepsilon=(1,-1,-1,-1)$. Write $\nabla=\sum_k\vec e_k\,\partial/\partial Q_k$ for the spatial gradient, with divergence $\nabla\cdot\vec Q_{\mathrm f}$ and curl $\nabla\times\vec Q_{\mathrm f}$ of the element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and $\Delta_Q=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$ for the Laplacian in the three vector coordinates; on the material sector it is the physical $\Delta=\partial^2/\partial q_x^2+\partial^2/\partial q_y^2+\partial^2/\partial q_z^2$, where $Q_k=q_k$.

**The conjugates of the gradient.** The gradient is an operator, and the marks are read on its units at fixed coordinate: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial Q_\mu$ is real; the unhalved derivative defined above is complex, and on an element-valued field the star is coefficientwise, carried through the derivative by $\partial/\partial\bar Q_\mu$ rather than by $\partial/\partial Q_\mu$. Read on the units, the quaternion conjugation reverses the three spatial units, and so does the Hermitian conjugation, so the two act on the gradient alike,

$$
\tilde\nabla^{*}=\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad \overline{\tilde\nabla}=\tilde\nabla .
$$

**The forms stay four, the norms are two.** The four forms keep their four conventions, named above in this section, each conjugating its own slot: the quaternionic form conjugates the first argument and the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm and the Krein norm with the plain bilinear norm. The four subsections below carry the four forms, and their norms are the two operators $\Box$ and $\partial^2/\partial Q_t^2-\Delta_Q$.

**On the material sector $\mathbb{M}_-$**, where $Q_t=iq'_t$ and $Q_k=q_k$, the derivative along the fourth coordinate reads $\partial/\partial Q_t=-i\,\partial/\partial q'_t$.

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four of §*The Twelve Products and Their Names*. On the gradient, with the element-valued field $\tilde Q_{\mathrm f}$ of §*The Gradient*, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j\vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit,

$$
\tilde\nabla\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$, with $\tilde J=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **On the material sector** the same product is read with $\partial/\partial Q_t=-i\,\partial/\partial q'_t$, the space part being unchanged.

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

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$. **On the material sector** it is $-i\frac{\partial Q_{\mathrm{f}t}}{\partial q'_t}-\nabla\cdot\vec Q_{\mathrm f}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla\rangle=\langle\tilde\nabla,\tilde\nabla\rangle=\mathrm{Sc}(\tilde\nabla\tilde\nabla)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

the cross terms cancelling. **On the material sector** it is $-\frac{\partial^2}{\partial (q'_t)^2}-\Delta$, which is not the series' d'Alembertian; on this sector the d'Alembertian is $\Delta-\frac{\partial^2}{\partial (q'_t)^2}$ (§*The Quaternionic Bilinear Product, Its Form and Its Norm*).

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four of §*The Twelve Products and Their Names*; on the gradient it is $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**On the material sector** the same substitution $\partial/\partial Q_t=-i\,\partial/\partial q'_t$ applies.

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

a scalar, the **contraction** of the derivative with the field in the signature of the material sector. It differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed. **On the material sector** it is $-i\frac{\partial Q_{\mathrm{f}t}}{\partial q'_t}+\nabla\cdot\vec Q_{\mathrm f}$.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal arguments, and the two orders of the product agree:

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\langle\tilde\nabla,\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, an operator on the whole algebra, one and the same before any sector is named (*The Four Forms, the Four Algebraic Norms and the Change of Scalars*). The coordinates $Q_\mu$ are those of the algebra and are complex in general; the operator is $\partial^2/\partial Q_t^2+\Delta_Q$ whatever the sector, and it is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box\tilde Q_{\mathrm f}=\sum_\mu(\Box Q_{\mathrm{f}\mu})e_\mu$. It is the identity above, and not the relation $Q_t=iq'_t$, that fixes it, and **no article of the series defines a second d'Alembertian**; no mass-term sign is left to a local convention.

**The special case of the material sector.** On $\mathbb{M}_-$ the coordinates are $Q_t=iq'_t$ and $Q_k=q_k$, and the relation $Q_t=iq'_t$ flips the sign of the second derivative in $q'_t$, $\partial^2/\partial Q_t^2=-\partial^2/\partial (q'_t)^2$, so the same operator reads

$$
\Box\big|_{\mathbb{M}_-}=\frac{\partial^2}{\partial Q_t^2}+\Delta=\Delta-\frac{\partial^2}{\partial (q'_t)^2},
$$

a plus on the vector part and a minus on the fourth coordinate. On $\mathbb{M}_-$, where the series does its work, this reading is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series. **The relation $Q_t=iq'_t$ is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial Q_t^2+\Delta_Q$; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. The operator is one, and every article writes it the same way.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four of §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is central and is the Hermitian form itself,

$$
\tilde\nabla\bullet_{*}\tilde Q_{\mathrm f}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})\,e_t=\Bigl[\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t ,
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

in which the conjugate stands on the first factor and no absolute value is taken; the two derivatives in $Q_t$ are imaginary on the material sector, so that scalar part is $-\lvert\partial\phi/\partial q'_t\rvert^2+\lvert\nabla\phi\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L_{\mathrm{kin}}=-\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\Bigl|\frac{\partial\phi}{\partial q'_t}\Bigr|^2-\lvert\nabla\phi\rvert^2 ,
$$

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the material sector** the form itself is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial q'_t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q=\Box ,
$$

so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four on the biquaternion layer**, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert_E$; positivity is a property of the elements, the norm of this subsection being the operator $\Box$. **On the material sector** it is the same operator, $\Box|_{\mathbb{M}_-}=\Delta-\partial^2/\partial (q'_t)^2$.

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

a scalar, the **contraction** of the conjugate derivative with the conjugated field in the signature of the material sector. **On the material sector** it is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial q'_t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form, and on the elements it is the form of signature $(1,3)$ whose diagonal is $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$: Hermitian, indefinite — positive where $\lvert Q_t\rvert^2>\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ and negative where the opposite inequality holds — so it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these subsections. **On the material sector**, in the real coefficient $q'_t$ of $Q_t=iq'_t$, it is $-\frac{\partial^2}{\partial (q'_t)^2}-\Delta$.

**A contraction is a form, never an index.** The metric of the series is the sign vector $\varepsilon$ inside the product, so no index is raised and none is lowered. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla\rangle_{\natural}=\Box$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the metric being the sign vector inside the product.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}_{\mathrm{r}}$, because a bare underscore would take the first character alone.

**A subscript is never a partial derivative.** The subscript marks a component or a label, a partial derivative is written with $\partial$, and the rule is fixed in §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the units, the roots, the idempotents and the nilpotents as well as the general elements: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}_{\mathrm{r}}$ and $\tilde U_{\mathrm r}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$. In the reduced biquaternion layer the sign belongs to the idempotent pair and to its coordinates, $\Pi_\pm$, $Q_{+}$ and $Q_{-}$, the two basis coordinates carrying the triangles, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and a numbered element putting its number first in either case, $Q_{1+}$ and $Q_{1\blacktriangle}$; the element they build is $\breve Q$. The sign is read with the glyph, and no identity is implied between the pairs: $\tilde Q_\pm$ names the two quaternionic components of a split-biquaternion, $\vec Q_\pm$ their vector parts, and $Q_\pm$ the idempotent coordinates of $\breve Q$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $\tilde\Pi_\pm$ |
| an upright word | $\mathbb{B}_{\mathrm{r}}$, $\tilde U_{\mathrm r}$ |
| a grouped expression | $Q_{n+1}$ |

The decorations that may stand in the subscript slot are these: all 451 distinct glyphs of the KaTeX 0.16.9 symbol table, one entry per glyph, with a single command written where several commands draw the same glyph. An entry that takes an argument is shown on $n$, and an entry that is text is written inside \text.

**Binary operators.** ${}_{\pm}$, ${}_{\times}$, ${}_{\div}$, ${}_{\dagger}$, ${}_{\ddagger}$, ${}_{\mp}$, ${}_{\dotplus}$, ${}_{\setminus}$, ${}_{\ast}$, ${}_{\circ}$,
${}_{\bullet}$, ${}_{\land}$, ${}_{\lor}$, ${}_{\cap}$, ${}_{\cup}$, ${}_{\wr}$, ${}_{\uplus}$, ${}_{\sqcap}$, ${}_{\sqcup}$, ${}_{\oplus}$,
${}_{\ominus}$, ${}_{\otimes}$, ${}_{\oslash}$, ${}_{\odot}$, ${}_{\circledcirc}$, ${}_{\circledast}$, ${}_{\circleddash}$, ${}_{\boxplus}$, ${}_{\boxminus}$, ${}_{\boxtimes}$,
${}_{\boxdot}$, ${}_{\intercal}$, ${}_{\veebar}$, ${}_{\barwedge}$, ${}_{\diamond}$, ${}_{\cdot}$, ${}_{\star}$, ${}_{\divideontimes}$, ${}_{\ltimes}$, ${}_{\rtimes}$,
${}_{\leftthreetimes}$, ${}_{\rightthreetimes}$, ${}_{\curlyvee}$, ${}_{\curlywedge}$, ${}_{\Cap}$, ${}_{\Cup}$, ${}_{\lessdot}$, ${}_{\gtrdot}$, ${}_{\triangleright}$, ${}_{\bigtriangledown}$,
${}_{\triangleleft}$, ${}_{\bigcirc}$, ${}_{\amalg}$, ${}_{\doublebarwedge}$

**Relations.** ${}_{\lt}$, ${}_{\gt}$, ${}_{\in}$, ${}_{\ni}$, ${}_{\backepsilon}$, ${}_{\propto}$, ${}_{\mid}$, ${}_{\nmid}$, ${}_{\parallel}$, ${}_{\nparallel}$,
${}_{\therefore}$, ${}_{\because}$, ${}_{\sim}$, ${}_{\backsim}$, ${}_{\nsim}$, ${}_{\eqsim}$, ${}_{\simeq}$, ${}_{\cong}$, ${}_{\ncong}$, ${}_{\approx}$,
${}_{\approxeq}$, ${}_{\asymp}$, ${}_{\Bumpeq}$, ${}_{\bumpeq}$, ${}_{\doteq}$, ${}_{\Doteq}$, ${}_{\fallingdotseq}$, ${}_{\risingdotseq}$, ${}_{\eqcirc}$, ${}_{\circeq}$,
${}_{\triangleq}$, ${}_{\equiv}$, ${}_{\le}$, ${}_{\ge}$, ${}_{\leqq}$, ${}_{\geqq}$, ${}_{\lneqq}$, ${}_{\gneqq}$, ${}_{\ll}$, ${}_{\gg}$,
${}_{\between}$, ${}_{\nless}$, ${}_{\ngtr}$, ${}_{\nleq}$, ${}_{\ngeq}$, ${}_{\lesssim}$, ${}_{\gtrsim}$, ${}_{\lessgtr}$, ${}_{\gtrless}$, ${}_{\prec}$,
${}_{\succ}$, ${}_{\preccurlyeq}$, ${}_{\succcurlyeq}$, ${}_{\precsim}$, ${}_{\succsim}$, ${}_{\nprec}$, ${}_{\nsucc}$, ${}_{\subset}$, ${}_{\supset}$, ${}_{\subseteq}$,
${}_{\supseteq}$, ${}_{\nsubseteq}$, ${}_{\nsupseteq}$, ${}_{\subsetneq}$, ${}_{\supsetneq}$, ${}_{\sqsubset}$, ${}_{\sqsupset}$, ${}_{\sqsubseteq}$, ${}_{\sqsupseteq}$, ${}_{\vdash}$,
${}_{\dashv}$, ${}_{\perp}$, ${}_{\vDash}$, ${}_{\Vdash}$, ${}_{\Vvdash}$, ${}_{\nvdash}$, ${}_{\nvDash}$, ${}_{\nVdash}$, ${}_{\nVDash}$, ${}_{\vartriangleleft}$,
${}_{\vartriangleright}$, ${}_{\trianglelefteq}$, ${}_{\trianglerighteq}$, ${}_{\origof}$, ${}_{\imageof}$, ${}_{\multimap}$, ${}_{\Join}$, ${}_{\backsimeq}$, ${}_{\Subset}$, ${}_{\Supset}$,
${}_{\pitchfork}$, ${}_{\lll}$, ${}_{\ggg}$, ${}_{\lesseqgtr}$, ${}_{\gtreqless}$, ${}_{\curlyeqprec}$, ${}_{\curlyeqsucc}$, ${}_{\npreceq}$, ${}_{\nsucceq}$, ${}_{\lnsim}$,
${}_{\gnsim}$, ${}_{\precnsim}$, ${}_{\succnsim}$, ${}_{\ntriangleleft}$, ${}_{\ntriangleright}$, ${}_{\ntrianglelefteq}$, ${}_{\ntrianglerighteq}$, ${}_{\frown}$, ${}_{\smile}$, ${}_{\vartriangle}$,
${}_{\blacktriangleright}$, ${}_{\blacktriangleleft}$, ${}_{\leqslant}$, ${}_{\geqslant}$, ${}_{\lessapprox}$, ${}_{\gtrapprox}$, ${}_{\lneq}$, ${}_{\gneq}$, ${}_{\lnapprox}$, ${}_{\gnapprox}$,
${}_{\lesseqqgtr}$, ${}_{\gtreqqless}$, ${}_{\eqslantless}$, ${}_{\eqslantgtr}$, ${}_{\preceq}$, ${}_{\succeq}$, ${}_{\precneqq}$, ${}_{\succneqq}$, ${}_{\precapprox}$, ${}_{\succapprox}$,
${}_{\precnapprox}$, ${}_{\succnapprox}$, ${}_{\subseteqq}$, ${}_{\supseteqq}$, ${}_{\subsetneqq}$, ${}_{\supsetneqq}$, ${}_{\nshortmid}$, ${}_{\nshortparallel}$, ${}_{\lvertneqq}$, ${}_{\gvertneqq}$,
${}_{\ngeqq}$, ${}_{\ngeqslant}$, ${}_{\nleqslant}$, ${}_{\nleqq}$, ${}_{\nsubseteqq}$, ${}_{\varsubsetneqq}$, ${}_{\nsupseteqq}$, ${}_{\varsupsetneqq}$, ${}_{\varsubsetneq}$, ${}_{\varsupsetneq}$,
${}_{\not}$

**Arrows.** ${}_{\gets}$, ${}_{\uparrow}$, ${}_{\to}$, ${}_{\downarrow}$, ${}_{\leftrightarrow}$, ${}_{\updownarrow}$, ${}_{\nwarrow}$, ${}_{\nearrow}$, ${}_{\searrow}$, ${}_{\swarrow}$,
${}_{\nleftarrow}$, ${}_{\nrightarrow}$, ${}_{\twoheadleftarrow}$, ${}_{\twoheadrightarrow}$, ${}_{\leftarrowtail}$, ${}_{\rightarrowtail}$, ${}_{\mapsto}$, ${}_{\hookleftarrow}$, ${}_{\hookrightarrow}$, ${}_{\looparrowleft}$,
${}_{\looparrowright}$, ${}_{\leftrightsquigarrow}$, ${}_{\nleftrightarrow}$, ${}_{\Lsh}$, ${}_{\Rsh}$, ${}_{\curvearrowleft}$, ${}_{\curvearrowright}$, ${}_{\circlearrowleft}$, ${}_{\circlearrowright}$, ${}_{\leftharpoonup}$,
${}_{\leftharpoondown}$, ${}_{\restriction}$, ${}_{\upharpoonleft}$, ${}_{\rightharpoonup}$, ${}_{\rightharpoondown}$, ${}_{\downharpoonright}$, ${}_{\downharpoonleft}$, ${}_{\rightleftarrows}$, ${}_{\leftrightarrows}$, ${}_{\leftleftarrows}$,
${}_{\upuparrows}$, ${}_{\rightrightarrows}$, ${}_{\downdownarrows}$, ${}_{\leftrightharpoons}$, ${}_{\rightleftharpoons}$, ${}_{\nLeftarrow}$, ${}_{\nLeftrightarrow}$, ${}_{\nRightarrow}$, ${}_{\Leftarrow}$, ${}_{\Uparrow}$,
${}_{\Rightarrow}$, ${}_{\Downarrow}$, ${}_{\Leftrightarrow}$, ${}_{\Updownarrow}$, ${}_{\Lleftarrow}$, ${}_{\Rrightarrow}$, ${}_{\leadsto}$, ${}_{\dashleftarrow}$, ${}_{\dashrightarrow}$, ${}_{\longleftarrow}$,
${}_{\longrightarrow}$, ${}_{\longleftrightarrow}$, ${}_{\Longleftarrow}$, ${}_{\Longrightarrow}$, ${}_{\Longleftrightarrow}$, ${}_{\longmapsto}$

**Large operators.** ${}_{\prod}$, ${}_{\coprod}$, ${}_{\sum}$, ${}_{\int}$, ${}_{\iint}$, ${}_{\iiint}$, ${}_{\oint}$, ${}_{\oiint}$, ${}_{\oiiint}$, ${}_{\bigwedge}$,
${}_{\bigvee}$, ${}_{\bigcap}$, ${}_{\bigcup}$, ${}_{\bigodot}$, ${}_{\bigoplus}$, ${}_{\bigotimes}$, ${}_{\biguplus}$, ${}_{\bigsqcup}$

**Symbols.** ${}_{\text{\textdollar}}$, ${}_{\text{\textasciicircum}}$, ${}_{\text{\textbar}}$, ${}_{\text{\textasciitilde}}$, ${}_{\pounds}$, ${}_{\yen}$, ${}_{\neg}$, ${}_{\circledR}$, ${}_{\degree}$, ${}_{\wp}$,
${}_{\mho}$, ${}_{\Game}$, ${}_{\forall}$, ${}_{\complement}$, ${}_{\partial}$, ${}_{\exists}$, ${}_{\nexists}$, ${}_{\emptyset}$, ${}_{\nabla}$, ${}_{\surd}$,
${}_{\infty}$, ${}_{\angle}$, ${}_{\measuredangle}$, ${}_{\sphericalangle}$, ${}_{\top}$, ${}_{\varvdots}$, ${}_{\circledS}$, ${}_{\diagup}$, ${}_{\diagdown}$, ${}_{\blacksquare}$,
${}_{\Box}$, ${}_{\blacktriangle}$, ${}_{\blacktriangledown}$, ${}_{\Diamond}$, ${}_{\bigstar}$, ${}_{\spadesuit}$, ${}_{\heartsuit}$, ${}_{\diamondsuit}$, ${}_{\clubsuit}$, ${}_{\flat}$,
${}_{\natural}$, ${}_{\sharp}$, ${}_{\checkmark}$, ${}_{\maltese}$, ${}_{\blacklozenge}$

**Letters.** ${}_{\text{\AE}}$, ${}_{\text{\O}}$, ${}_{\text{\ss}}$, ${}_{\text{\ae}}$, ${}_{\eth}$, ${}_{\text{\o}}$, ${}_{\text{\i}}$, ${}_{\text{\OE}}$, ${}_{\text{\oe}}$, ${}_{\text{\j}}$,
${}_{\Gamma}$, ${}_{\Delta}$, ${}_{\Theta}$, ${}_{\Lambda}$, ${}_{\Xi}$, ${}_{\Pi}$, ${}_{\Sigma}$, ${}_{\Upsilon}$, ${}_{\Phi}$, ${}_{\Psi}$,
${}_{\Omega}$, ${}_{\alpha}$, ${}_{\beta}$, ${}_{\gamma}$, ${}_{\delta}$, ${}_{\varepsilon}$, ${}_{\zeta}$, ${}_{\eta}$, ${}_{\theta}$, ${}_{\iota}$,
${}_{\kappa}$, ${}_{\lambda}$, ${}_{\mu}$, ${}_{\nu}$, ${}_{\xi}$, ${}_{\omicron}$, ${}_{\pi}$, ${}_{\rho}$, ${}_{\varsigma}$, ${}_{\sigma}$,
${}_{\tau}$, ${}_{\upsilon}$, ${}_{\varphi}$, ${}_{\chi}$, ${}_{\psi}$, ${}_{\omega}$, ${}_{\vartheta}$, ${}_{\phi}$, ${}_{\varpi}$, ${}_{\digamma}$,
${}_{\varkappa}$, ${}_{\varrho}$, ${}_{\epsilon}$, ${}_{\hbar}$, ${}_{\Im}$, ${}_{\ell}$, ${}_{\Re}$, ${}_{\Finv}$, ${}_{\aleph}$, ${}_{\beth}$,
${}_{\gimel}$, ${}_{\daleth}$, ${}_{\imath}$, ${}_{\jmath}$

**Delimiters.** ${}_{\lparen}$, ${}_{\rparen}$, ${}_{\lceil}$, ${}_{\rceil}$, ${}_{\lfloor}$, ${}_{\rfloor}$, ${}_{\lmoustache}$, ${}_{\rmoustache}$, ${}_{\ulcorner}$, ${}_{\urcorner}$,
${}_{\llcorner}$, ${}_{\lrcorner}$, ${}_{\langle}$, ${}_{\rangle}$, ${}_{\lgroup}$, ${}_{\rgroup}$

**Ellipses.** ${}_{\ldots}$, ${}_{\cdots}$, ${}_{\ddots}$

**Punctuation.** ${}_{\#}$, ${}_{\%}$, ${}_{\&}$, ${}_{\ldotp}$, ${}_{\lbrack}$, ${}_{\backslash}$, ${}_{\rbrack}$, ${}_{\_}$, ${}_{\{}$, ${}_{\}}$,
${}_{\S}$, ${}_{\P}$, ${}_{\text{\textendash}}$, ${}_{\text{\textemdash}}$, ${}_{\text{\textquoteleft}}$, ${}_{\text{\textquoteright}}$, ${}_{\text{\textquotedblleft}}$, ${}_{\text{\textquotedblright}}$, ${}_{\prime}$, ${}_{\backprime}$

**Accents.** ${}_{\ddot{n}}$, ${}_{\c{n}}$, ${}_{\^{n}}$, ${}_{\v{n}}$, ${}_{\={n}}$, ${}_{\'{n}}$, ${}_{\`{n}}$, ${}_{\u{n}}$, ${}_{\.{n}}$, ${}_{\r{n}}$,
${}_{\~{n}}$, ${}_{\H{n}}$, ${}_{\vec{n}}$

**Spacing.** The command ${}_{\ }$ draws no mark; it sets a space.

Beyond the table the slot takes any expression: an upright word, ${}_{\mathrm{ret}}$; a text string, ${}_{\text{word}}$; a nested index, ${}_{i_1}$; and the compound ${}_{\natural*}$ that the biquaternion articles use.

## The Superscripts

Two superscript tokens run beside the marks of the elements and the marks of the conjugations, on the glyphs of elements and algebras, and neither is to be read for the other:

| Token | Written on | Meaning |
|---|---|---|
| $^{\mathrm{fop}}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $^{\mathrm{opp}}$ | an algebra name | the opposite algebra, the algebra with the reversed product |

Two further upright superscripts belong to objects outside the algebra — $\mathrm{fn}$ on a function and $\mathrm{spin}$ on a group element — and are recorded in §*Notational Conventions*.

**The mark, and its one use.** The marks of the elements say what a glyph **is**, not that it is an **operator** (§*The Operators*). The single exception is the **Fock layer** of the physical corpus, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the upright superscript $\mathrm{fop}$, set on the glyph:

$$
a^{\mathrm{fop}},\quad b^{\mathrm{fop}},\quad a^{\mathrm{fop}\dagger},\quad \psi^{\mathrm{fop}},\quad N^{\mathrm{fop}},\quad H^{\mathrm{fop}},\quad F^{\mathrm{fop}},\quad Q^{\mathrm{fop}},\quad U^{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p$, the position $x$, the spin $S$ and the parity, charge-conjugation and reversal maps $P$, $C$ and $T$ carry no superscript, because each keeps the glyph of its element or is a map with a glyph of its own.

**It combines with the dagger, the mark first.** The dagger is the general adjoint (§*The Operators*). Where both marks fall on one glyph the Fock mark comes first and the adjoint follows, $(a^{\mathrm{fop}})^{\dagger}$, contracted to $a^{\mathrm{fop}\dagger}$; the dagger alone never marks a glyph as an operator, and the superscript alone never asserts self-adjointness.

**The opposite algebra carries a different token.** The **opposite algebra**, whose multiplication is reversed, $a\cdot b=ba$, carries the superscript $\mathrm{opp}$ — $A^{\mathrm{opp}}$, $\mathbb{B}^{\mathrm{opp}}$, $M_n(D)^{\mathrm{opp}}$ — and it is the **algebra name** that takes the mark; the Fock token $\mathrm{fop}$ marks a Fock-operator glyph. The two meanings are separated by the token itself and not by context.

## Conventions of the Corpus Itself

The corpus has a small number of working conventions that are not mathematical.

**The menus.** Every article is registered in exactly one menu: `maths.md` for the mathematical corpus and `physics.md` for the physics corpus. An entry has the form of a link to the article followed by a comment that lists the contents of the article in outline. The mathematical menu opens with the two articles that describe the corpus rather than belonging to one of them — *Introduction to Mathematics* and this one — placed outside the parts. An entry that begins with `+` is a **planned** article, one that is registered in the menu and not yet written; an entry without the marker has its article on disk.

**The groups inside a category.** A category of Parts I to IV lists its articles in four groups, each of which adds one thing to the group before it. The group `- Theory` holds the structure itself, read with the product of its elements. The group `- Operator Theory` holds the operators on that structure — the left and right multiplications, the derivations, the automorphisms, the actions and the sandwich — and adds an operator layer and nothing else. The group `- * Theory` holds the same structure read with an involution on its **elements**. The group `- * Operator Theory` holds the operators built from the **involution**, of which the adjoint is the archetype.

**The two involutions.** The star names the involutive layer in both groups, and the layer of the elements and the layer of the operators are two structures and not one: the involution of `- * Theory` sits on the elements and the adjoint of `- * Operator Theory` sits on the operators. They need not coincide: an involution on the elements does not by itself produce an adjoint on the operators, and two adjoints of the same structure may differ — the transpose and the Hermitian adjoint of a matrix are both adjoints, taken with respect to different pairings. When the two do agree the representation is a `*`-representation, and the agreement is proved in the article, never assumed by the menu.

**The order and the fill rule.** The four groups are placed in the order above, and the group `- Applications`, which holds the concrete instances of the structure, closes the category. The groups `- Operator Theory` and `- * Operator Theory` are present in a category whenever it has an operator layer, and the group `- * Theory` is present in every category of Parts I to IV, whether or not it yet holds an article.

**The category names and numbers.** The menu numbers its categories, and an article elsewhere in the corpus may address one by number rather than by name: *category n* means the n-th category of the mathematical menu, read in order. This article refers to categories by **name** throughout, because the names are the stable thing and the numbers shift whenever a category is inserted or split. A reader who meets a bare number in another article can resolve it in the menu.

**The article files.** The corpus is split into two collections, each with its own folder: a mathematical article is a file `articles_maths/<slug>.md` and a physical article is a file `articles_physics/<slug>.md`, where the slug is the title in lower case with hyphens in place of spaces and punctuation. The folder and the menu agree — an article lies in the folder whose menu lists it, and no article lies in both.

**The article skeleton.** Every article opens with its title as the first heading, followed by an *Introduction* that states what the article does and what it assumes, then the thematic sections, and closes with three sections in this order: *Summary*, *Summary of Notation*, and *Further Reading*. The introduction states the article's boundaries — what it deliberately does not cover, and where the reader will find it. This article is the one exception: its notation is merged into the Summary and its table closes the article.

**Cross-references and boundaries.** A concept is introduced once, in the category that owns it, and referred to afterwards rather than restated. Articles do not duplicate the content of other articles; they cite them. Every article that touches a structure belonging to a later part states the deferral explicitly, which is the mechanism by which Rule 1 is enforced.

**The word "interval".** Two different objects share the word, and the corpus keeps them apart. In the mathematical corpus an **interval** is an order-theoretic or lattice object: a convex subset of a linearly ordered set, the interval $[a,b]=\{x:a\le x\le b\}$ of a lattice or of a poset of effects, defined by the order and not by a form. In the physical corpus the **interval** is the value of the quadratic form, $\langle\tilde Q\rangle_{\natural}=-\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ on the material sector, defined by the form and not by an order. A statement about the sign of the interval is therefore never a statement about a lattice interval, and a lattice interval is never the line element; where the two senses could meet, the corpus writes *the form value* or *the quadratic form* for the physical one.

## LaTeX and Typesetting

The articles are rendered with KaTeX on the page, and the following rules are observed in the source.

- Inline mathematics is written between single dollars, and display mathematics between double dollars on lines of their own.
- Inline mathematics never spans a line break. If a formula is too long, it is displayed.
- Display mathematics inside a list is indented four spaces.
- A prime may follow a subscript as well as precede it: the forms `q'_t` and `q_t'` are both admitted, and an article keeps one order throughout.
- Tables are Markdown tables. A LaTeX array is never used for a table.
- Every heading that introduces a comparison or a classification is a real `###` heading, and the objects are defined before they are tabulated.
- **Bold marks the result.** In a Remark that states a verdict, the clause carrying the outcome is
  set in bold, `**...**`, the object of the sentence staying in plain roman: *the subspace **is a
  commutative Jordan algebra over $\mathbb{R}$ of degree two***. A statement already displayed as a
  Theorem, a Proposition or a Proof is not bolded; the convention applies to the prose of a Remark and
  to the lead sentence of a section that states an outcome.
- The third derivative is written `d^3/dt^3`, and the macro `\slashed` is available. The characters `|`, `{`, `}`, `<` and `>` inside mathematics need no escaping.
- A malformed formula is rendered in red on the page rather than reported as an error, so mathematics is checked by eye and not by the absence of a warning.

## Summary

The conventions are of two kinds: the mathematical notation, and the working conventions of the corpus. The notation is collected in a single table, at §*Notational Conventions* at the end of the article, which lists the glyphs of this article and of the articles that cite it.

A generic element of a number system is written as a linear combination of the basis with its coefficients in
the scalar sector of the system, the biquaternion element being $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$
with $Q_\mu = q_\mu + iq'_\mu$. The generic element of a system carries a letter of its own: $\alpha, \beta$ for the Booleans, $n, m$ for the naturals and the integers, $q, q_1, q_2$ for the rationals and the reals, with a rational in lowest terms written $r/s$ so that $q$ is never a numerator or a denominator, $Q = q + iq'$ for the commutative two-parameter systems, and $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ for the reduced biquaternions, whose two coordinates are complex and whose second unit is the hyperbolic $j$. The notation is fixed here above all for the conjugations, which is where the corpus has the most marks to keep apart, and for the number systems, whose glyphs carry two bits each. An algebra with a degree-2 form carries an intrinsic conjugate, the map that negates its vectors and fixes its scalars; it is written with a **natural sign**. The involution of the base extends to the coefficients and is written with a **bar**. Their composite is the Hermitian anti-automorphism, written with a **star**; its negative is the **anti-Hermitian** conjugation, written **flat**; and the **dagger** is the adjoint of an operator, written on operators and never on the elements. The star and the bar commute, $^{*} = \bar{\cdot}\circ{}^{\natural} = {}^{\natural}\circ\bar{\cdot}$, the flat is $\flat = -{}^{*}$, and $\{\mathrm{id}, \bar{\cdot}, {}^{\natural}, {}^{*}\}$ is a Klein four-group while the flat stands outside it. The corpus writes a **form** with two arguments and its **algebraic norm** with one, the generic pair $\mathrm{Form}(\tilde Q_1,\tilde Q_2)$ and $\mathrm{Norm}(\tilde Q)=\mathrm{Form}(\tilde Q,\tilde Q)$. On a base whose involution is the identity the bar is the identity map and the star coincides with the natural sign.

On the number systems the **case** records whether the commuting scalar sector is larger than the reals and the **tilde** records the presence of the quaternionic factor, and the two are read independently: $q$ is real, $Q$ complex or split-complex or dual, $\breve Q$ reduced biquaternion — upper case, with the breve and no tilde, with two complex coordinates — $\tilde q$ quaternion or split-quaternion, $\tilde Q$ biquaternion or split-biquaternion. A **pure element** — one with no scalar part — drops the tilde and carries the arrow, $\vec q$ in the quaternion and split-quaternion layers and $\vec Q$ in the biquaternion and split-biquaternion ones. The **idempotents**, the **nilpotents** and the **roots** carry symbols of their own, split by the same case rule: $\tilde\Pi$ is an idempotent or a pure state of the biquaternion and split-biquaternion layers, and the minimal left ideal it generates, $\tilde\pi$ the same in the quaternion and split-quaternion layers, $\Pi$ in the complex, split-complex, dual and reduced biquaternion layers, where no tilde is written; $\tilde\nu$ is a nilpotent of the quaternion or split-quaternion layer, $\tilde\Upsilon$ a nilpotent of the biquaternion or split-biquaternion layer, and $\Upsilon$ the same in the complex, split-complex, dual and reduced biquaternion layers; $\tilde\Xi$ is a root of $1$ of the biquaternion and split-biquaternion layers, $\tilde\xi$ the same in the quaternion and split-quaternion layers, and $\Xi$ the same in the complex, split-complex, dual and reduced biquaternion layers; while $\tilde Q$ is the generic element of a statement that holds for every element. The upper-case tilde carries four roles — the idempotent, the nilpotent, the root and the generic element — and the split is deliberate.

The working conventions are the corpus's own. Every article is registered in exactly one menu, with a comment that outlines it, and a leading `+` marks a planned article. The four groups of a category — Theory, Operator Theory, `*` Theory and `*` Operator Theory — each add one thing to the group before, the star naming the involutive layer on the elements and then on the operators, so that the last group holds the operators built from the involution, and the group `Applications` closes the category. A concept is introduced once, in the category that owns it, and is cited afterwards rather than restated; every deferral to a later part is stated explicitly, which is how the ordering rule of *Introduction to Mathematics* is enforced. Each article opens with its title and an Introduction and closes with Summary, Summary of Notation and Further Reading; in this article the notation is merged into the Summary and its table is placed at the end.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853). The original formulation, and the source of the quaternion conjugation and its notation.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
- James Cockle, "On a new imaginary in algebra", *Philosophical Magazine* **34** (1849) 37–47. The tessarines, the commutative algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ that the corpus records as the reduced biquaternions, and the earliest occurrence of the hyperbolic versor.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022. The reduced biquaternion algebra of the engineering literature, its idempotent decomposition, its ring-valued norm and its transform.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution, the first and the second kind, and the classification of their involutions.
- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for a notation fixed once and used without variation.
- Donald E. Knuth, *The TeXbook* (Addison-Wesley, 1984). The typographic conventions the source of the corpus follows.

## Notational Conventions

The conventions below are those used throughout the corpus.

| Symbol | Meaning |
|---|---|
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ | The naturals, integers, rationals, reals and complex numbers |
| $\mathbb{D}$ | The split-complex numbers, $\mathbb{R}[x]/(x^2-1)$ |
| $\mathbb{D}'$ | The dual numbers, $\mathbb{R}[x]/(x^2)$ |
| $\mathbb{B}_{\mathrm{r}}$ | The reduced biquaternions, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \oplus \mathbb{C}$, equivalently the tessarines or the double-complex numbers; its intrinsic conjugation is the tessarine sign ${}_{\mathrm{ts}}$, and the natural sign is not written on the layer |
| $\mathbb{H}$ | The real quaternions |
| $\mathbb{H}_{\mathrm{s}}$ | The split-quaternions, $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ |
| $\mathbb{B}$ | The biquaternions, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\mathbb{H}_{\mathbb{D}}$ | The split-biquaternions, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| Lower case, upper case | The scalar sector is the reals, or larger than the reals |
| Tilde | The presence of the quaternionic factor |
| Arrow | The vector part of a named element and a pure element standing by itself — $\vec q$ or $\vec Q$ (§*Pure Elements and their Coefficients*) |
| $\alpha, \beta$; $q, q_1, q_2$ | The generic elements of the Booleans, and of the rationals and the reals |
| $r/s$ | A rational written as a fraction, with numerator $r \in \mathbb{Z}$ and denominator $s \in \mathbb{N}_{\geq 1}$; in lowest terms $\gcd(r,s) = 1$; the letter $q$ is never a numerator or a denominator |
| $n$, $m$ | The generic elements of the naturals and the integers, and the signature indices, the counts of positive and negative directions of a real form, as in $\mathrm{Cl}_{n,m}$ and $O(n,m)$ |
| $Q = q + iq'$ | The generic element of a commutative two-parameter system, with $j$ or $\varepsilon$ in place of $i$, and the imaginary coefficient carrying a prime; where several occur they are numbered $Q_1, Q_2, \dots$ |
| $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ | The generic element of the reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}$, upper case, with the breve and no tilde, its two coordinates $Q_{\blacktriangle} = q_{\blacktriangle} + iq'_{\blacktriangle}$ and $Q_{\blacktriangledown} = q_{\blacktriangledown} + iq'_{\blacktriangledown}$ complex and its second unit the hyperbolic $j$, $j^{2} = +1$ and $ji = ij$, on the basis $1, i, j, ij$ |
| $\tilde q$ | The generic element of the quaternion or split-quaternion layer |
| $\tilde Q$ | The generic element of the biquaternion or split-biquaternion layer, and the generic element of a statement that holds for every element; in a statement with several they are numbered $\tilde Q_1, \tilde Q_2, \dots$ |
| $Q_{\log}$ | A logarithm of $Q$, a solution of $\exp(Q_{\log}) = Q$: $Q_{\log}$ in the complex, split-complex and dual algebras, $\tilde q_{\log}$ in the quaternion and split-quaternion layers, $\tilde Q_{\log}$ in the biquaternion and split-biquaternion layers, $\breve Q_{\log}$ in the reduced biquaternion algebra |
| $\vec q$ | A pure element of the quaternion or split-quaternion layer, an element with no scalar part |
| $\vec Q$ | A pure element of the biquaternion or split-biquaternion layer |
| $G$; $R$; $k$, $F$; $V$; $M$; $A$ | A group; a ring; a field; a vector space; a module; an algebra |
| $\mathrm{G}, \mathrm{H}, \mathrm{SL}_n$ | Lie algebras |
| $\mathrm{M}, \mathrm{P}$ | Ideals and prime ideals |
| $\operatorname{Sym}(X), \operatorname{Aut}(X)$ | The symmetric group of a set; the automorphism group of a structure |
| $\operatorname{End}(V), \operatorname{Der}(A), \operatorname{Inn}(A), \operatorname{Out}(A)$ | Endomorphisms, derivations, inner and outer automorphisms |
| $GL, SL, PGL, O, SO, U, SU, Sp$ | The classical groups |
| $T(V), S(V), \Lambda(V), Cl(V,\mathfrak{Q})$ | Tensor, symmetric, exterior and Clifford algebras |
| $V^{\otimes n}, S^n V, \Lambda^n V$ | Tensor, symmetric and exterior powers |
| $\langle v,w\rangle, \mathfrak{Q}(v), \lVert x\rVert$ | Bilinear form, quadratic form, norm |
| $\mathfrak{Q}$ | The quadratic form of a quadratic space, in Fraktur so that the plain $q$ and $Q$ stay with the elements |
| $\mathcal{Q}$ | The Lie or null quadric, in calligraphic, as in $\mathcal{Q}^{n+1}$ |
| $\bullet$ | The symmetrised (Jordan) product, $x \bullet y = \tfrac{1}{2}(xy + yx)$, and, with the slot subscripts ${}_{*}$, ${}_{\natural}$ and ${}_{\natural*}$, the four **symmetric products** of §*The Twelve Products and Their Names*; the circle $\circ$ is reserved for the composition of maps |
| $\wedge$ | The antisymmetrised product, $x \wedge y = \tfrac{1}{2}(xy - yx)$, and, with the same subscripts, the four **antisymmetric products** of §*The Twelve Products and Their Names*. On differential forms the same glyph is the exterior product, $\alpha\wedge\beta$, a different use |
| $\bar{\cdot}, {}^{\natural}, {}_{\mathrm{ts}}, {}^{*}, {}^{\flat}, {}^{\dagger}$ | The conjugations of an algebra with an involution — the bar, the natural sign ${}^{\natural}$, the tessarine sign ${}_{\mathrm{ts}}$ of $\mathbb{B}_{\mathrm{r}}$, the star, the anti-Hermitian sign — and the adjoint of an operator; §*The Conjugations* and §*The Operators* fix their meanings |
| $\tilde\Pi$, $\tilde\pi$, $\Pi$, $\Pi_\pm$ | An idempotent or a pure state, and the minimal left ideal it generates; the biquaternion layer writes $\tilde\Pi$, the quaternion layer $\tilde\pi$, and the tilde-free layers $\Pi$, the split-complex and reduced biquaternion ones writing the sign pair $\Pi_\pm$ (§*The Idempotent Convention*) |
| $\tilde\Xi$, $\tilde\xi$, $\Xi$ | A root of $1$: the biquaternion layer writes $\tilde\Xi$, the quaternion layer $\tilde\xi$, and the tilde-free layers $\Xi$ (§*The Root Convention*) |
| $\tilde\nu$ | A nilpotent of the quaternion or split-quaternion layer |
| $\tilde\Upsilon$ | A nilpotent of the biquaternion or split-biquaternion layer |
| $\Upsilon$ | A nilpotent of the complex, split-complex or dual layer, where no tilde is written |
| $\vec\Xi$, $\vec\Upsilon$ | A pure root of $1$ and a pure nilpotent of the biquaternion or split-biquaternion layer; $\vec\xi$ and $\vec\nu$ in the quaternion and split-quaternion layers |
| $\tilde u$, $\vec u$ | A unit element of the quaternion or split-quaternion layer, and its pure case, the axis of a rotation |
| $\tilde U$, $\vec U$ | A unit element of the biquaternion or split-biquaternion layer, $\mathrm{Norm}(\tilde U)=e_t$, and its pure case, of norm one |
| $U$ | A unit element of the complex, split-complex, dual or reduced biquaternion layer |
| $F^{\mathrm{fn}}, G^{\mathrm{fn}}, H^{\mathrm{fn}}$ | A function from a domain into the algebra, $F^{\mathrm{fn}} : \Omega \to \mathbb{B}$; the tilde marks a value and is never put on a map, since a function is not an element |
| $\tilde\nabla$ | The biquaternionic gradient, $\tilde\nabla = \sum_{\mu\in\{t,x,y,z\}} e_\mu \partial/\partial Q_\mu$; it keeps the tilde because its symbol is an algebra unit and not a letter |
| $g^{\mathrm{spin}}$ | An element of the group $\mathrm{Spin}(n)$ or $\mathrm{Pin}(n)$ on a principal bundle; not an element of the algebra |
| $^{\mathrm{fop}}$ | A **Fock operator**, an operator on the Fock space and not an element of the algebra — $a^{\mathrm{fop}}$, $N^{\mathrm{fop}}$, $H^{\mathrm{fop}}$, $U^{\mathrm{fop}}$. No other operator carries the mark. The opposite algebra uses the separate token $A^{\mathrm{opp}}$ |
| $\mathrm{Form}(\tilde Q_1,\tilde Q_2)$, $\mathrm{Norm}(\tilde Q)=\mathrm{Form}(\tilde Q,\tilde Q)$ | The generic form and the generic norm (§*The Form Convention, the Norm Convention and the Unitary Convention*) |
| $\langle\tilde Q_1,\tilde Q_2\rangle$, $\langle\tilde Q\rangle$ | The generic bracket, the form in two arguments and the norm in one; the subscript records the pair of slots — plain, $*$ Hermitian, $\natural$ quaternionic, $\natural*$ Krein, and, in $\mathbb{B}_{\mathrm{r}}$, ${}_{\mathrm{ts}}$ tessarine and ${}_{\mathrm{ts}*}$ tessarine-Hermitian |
| `- Theory`, `- Operator Theory`, `- * Theory`, `- * Operator Theory` | The four groups of a category, in that order |
| `- Applications` | The group that closes a category with the concrete instances of its structure |
| `+` | A planned article, registered in the menu and not yet written |
| `articles_maths/<slug>.md` | The file of a mathematical article; the slug is the title in lower case with hyphens |
| Introduction, thematic sections, Summary, Summary of Notation, Further Reading | The skeleton of every article |
