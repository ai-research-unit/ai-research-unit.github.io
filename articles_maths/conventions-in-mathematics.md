# __Conventions in Mathematics__

## Introduction

This article is the first of the seven conventions articles of the mathematical corpus, and the one that fixes the base: the base and its units, the shape of a generic element and its coefficients, the remarkable subspaces and the conjugations. It assumes nothing beyond the vocabulary of a set, a group and a ring, which it recalls only where a convention depends on it.

It states conventions only. The proofs and the properties of the objects it names belong to the articles cited beside them. A convention recorded here is not a claim that the alternative is wrong: several of these choices are freely made where either choice would be defensible, and what is not free is *consistency*, since every later article inherits them.

The six companion articles carry the rest, in dependency order: *Conventions of the Twelve Products and the Four Forms*, *Conventions of the Norms and the Unitary Convention*, *Conventions of the Special Elements and the Peirce Decomposition*, *Conventions of the Matrix Models*, *Conventions of the Operators and the Differential Calculus*, and *Conventions of the Indices, the Notation and the Corpus*. The first fixes the twelve products and the four forms, the second the norms and the unitary convention, the third the glyphs of the root, the idempotent and the nilpotent with the Peirce decomposition they generate, the fourth the two matrix models, the fifth the operators and the calculus, and the sixth the indices, the working conventions of the corpus and the typography.

The order is the order of dependence. The base is read first; the products come before the forms, the forms before the norms; the special elements follow the base and precede the representations, whose canonical frame is their Peirce frame; the calculus follows the products and the forms; and the indices come last because they index the six. The table at the end of the article is the index of the glyphs of the whole series.

## Groups, Rings and Operations

A group is written multiplicatively by default, with unit $e$ and inverse $x^{-1}$, and additively when it is the underlying group of a ring, with zero $0$ and inverse $-x$. A ring is a triple $(R, +, \cdot)$; a ring need not be commutative and need not have a unit, and the article that introduces it says which conventions it adopts. A field is a commutative ring with $1 \neq 0$ in which every nonzero element is invertible. A module is written with its scalars on the left unless the article says otherwise, and the side matters as soon as the ring is non-commutative. Products are written by juxtaposition: $ab$ for the product in a group or an algebra, $fv$ for the action of a scalar on a vector. The **symmetrised (Jordan) product** is written with a bullet, $x \bullet y = \tfrac{1}{2}(xy + yx)$, and the circle $\circ$ is kept for the **composition of maps**, as in $\mathrm{H}_{\tilde Q}\circ\mathrm{H}_{\sqrt{\mu}\,\tilde J}$.

## The Base and Its Units

The base is written with the letter $e$, one unit to a direction. The scalar unit is $e_t = 1$ and the three vector units are $\vec e_x, \vec e_y, \vec e_z$; the arrow is the only mark that separates the scalar unit from the vector units. **The three vector units are the quaternion units, the corpus's replacement for Hamilton's $i, j, k$.** A general element is written in the base,

$$
\tilde Q = Q_t e_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $e_\mu$ the unit of the direction $\mu$. In the quaternion layers the three vector units square to the negative of the scalar unit, $\vec e_k^2 = -e_t$; the split-quaternion layer keeps $\vec e_x^2 = -e_t$ and takes $\vec e_y^2 = \vec e_z^2 = +e_t$ (§*The Conjugations*). **The notation is the unit along the axis.** A coefficient carries the name of the direction it multiplies: $Q_x$ is the coefficient of $\vec e_x$, the label on the unit names the direction and the label on the coefficient names the same direction, so the coefficient and the unit read without ambiguity. **The base letter is $e$ and the unit-element letter is $u$, and the two are never exchanged.** The base units carry $e$, so $e$ is not available for the exponential, which is written $\exp(\cdot)$; a unit element of a layer carries the glyph of the unit element, $\tilde u$ or $\tilde Q$ (*Conventions of the Norms and the Unitary Convention*, §*The Unitary Convention*).

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
| $\mathbb{C}^2$ | Duo-complex numbers | $Q = (Q_{\blacktriangle}, Q_{\blacktriangledown})$ | $Q_{\blacktriangle}$, complex; $Q_{\blacktriangledown}$, complex | — |
| $\mathbb{B}_{\mathrm{r}}$ | Reduced biquaternions | $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ | $Q_{\blacktriangle}$, complex; $Q_{\blacktriangledown}$, complex | — |
| $\mathbb{H}$ | Quaternions | $\tilde q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $q_t$, real | $q_x\vec e_x$, $q_y\vec e_y$, $q_z\vec e_z$, real |
| $\mathbb{H}_{\mathrm{s}}$ | Split-quaternions | $\tilde q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ | $q_t$, real | $q_x\vec e_x$, $q_y\vec e_y$, $q_z\vec e_z$, real |
| $\mathbb{B}$ | Biquaternions | $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $Q_t$, complex | $Q_x\vec e_x$, $Q_y\vec e_y$, $Q_z\vec e_z$, complex |
| $\mathbb{H}_{\mathbb{D}}$ | Split-biquaternions | $\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ | $Q_t$, split-complex | $Q_x\vec e_x$, $Q_y\vec e_y$, $Q_z\vec e_z$, split-complex |

Under this framework, the **vector part** is the part carried by the three vector units $\vec e_x,\vec e_y,\vec e_z$; it exists only in the four quaternionic layers.

**The two part columns.** The fourth column gives the scalar part — the $\mathbb{C}$ scalar part in $\mathbb{B}$ and $\mathbb{B}_{\mathrm{r}}$, the split scalar part in $\mathbb{H}_{\mathbb{D}}$ — and the fifth the vector part, each coefficient with its nature. In $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{C}^2$ and $\mathbb{B}_{\mathrm{r}}$ there is no vector direction, so both coefficients are scalars of the coefficient field and the vector column is empty. **The row of $\mathbb{C}^2$ is the one space of the table**: its fourth column records the two complex coordinates of a point, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, each a scalar of the coefficient field, and its fifth column is empty because the space has no vector directions. **The two coordinates are the coefficients of the two basis vectors**, $e_1$ and $e_2$: the split is by basis vector, neither slot is distinguished, and the entry gives the nature of the two coefficients, which is $\mathbb{C}$, as it does for $\mathbb{B}_{\mathrm{r}}$.

**Several elements of one kind take subscripts.** Where a statement needs more than one element of the same kind, each occurrence takes a number: three generic biquaternions are $\tilde Q_1, \tilde Q_2, \tilde Q_3$, two quaternions are $\tilde q_1, \tilde q_2$, and two complex numbers are $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. The number counts the element and never names a direction; a letter names the direction. **The unnumbered glyph is the single generic element**: a bare $\tilde Q$ stands alone, or leads the pair $\tilde Q, \tilde Q_2$; two numbered elements are $\tilde Q_1, \tilde Q_2$, and a third takes the next number. The numbers count the elements in the order the statement introduces them, $\tilde Q_1, \tilde Q_2, \tilde Q_3$, and the coefficients follow their element, $Q_{1t}, \vec Q_1$ for $\tilde Q_1$.

**The four coordinates are labelled $t, x, y, z$.** So that a sum over the coordinates of a quaternion, a split-quaternion, a biquaternion or a split-biquaternion shows at once which unit each term carries, the coefficients take the labels of the directions in place of the numbers: $Q_t$ with $e_t$, and $Q_x, Q_y, Q_z$ with $\vec e_x, \vec e_y, \vec e_z$. A sum over the four therefore runs over those labels,

$$
\tilde Q = \sum_{\mu \in \{t,x,y,z\}} Q_\mu e_\mu ,
$$

with $\mu$ the label and $e_\mu$ the unit it carries — the arrowless $e_t$ at $\mu = t$ and the arrowed $\vec e_\mu$ at $\mu = x, y, z$. The same rule reads a quaternion, $\tilde q = \sum_{\mu} q_\mu e_\mu$, and a four-vector of the algebra, and the primed coefficients follow the same labels, $Q_\mu = q_\mu + iq'_\mu$: the label marks the direction and the prime marks the slot that carries the $i$.

**A complex element carries a majuscule**, $Q$, the case naming the scalar sector: an upper-case glyph has a scalar sector larger than the reals, a lower-case one has the reals. **The second coordinate of a complex element carries a prime**, $Q = q + iq'$, with $j$ in place of $i$ for the split-complex numbers and $\varepsilon$ for the dual numbers; a second and a third complex element are $Q_1 = q_1 + iq'_1$ and $Q_2 = q_2 + iq'_2$. **The four quaternionic elements carry a tilde**: lower case for the quaternions and the split-quaternions, $\tilde q$, and upper case for the biquaternions and the split-biquaternions, $\tilde Q$. The reduced biquaternion element carries **no tilde but the breve**: its algebra has no quaternionic factor, being the commutative two-parameter system over the complex scalars, and it is written $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$, the ascending triangle for the coefficient of $1$ and the descending triangle for the coefficient of $j$, with the two complex coordinates $Q_{\blacktriangle} = q_{\blacktriangle} + iq'_{\blacktriangle}$ and $Q_{\blacktriangledown} = q_{\blacktriangledown} + iq'_{\blacktriangledown}$, the second unit $j$ being the hyperbolic unit of the corpus, $j^{2} = +1$ and $ji = ij$, so that the basis is $1, i, j, ij$. And **the arithmetic systems and the reals carry a letter that is theirs alone**: $\alpha, \beta$ the Booleans, $n, m$ the naturals and the integers, and $q, q_1, q_2$ the rationals and the reals — a letter, no prime, no tilde, no coefficient sector, since these elements are not written as linear combinations. Finally, **the element is a scalar part plus, where the layer has one, a vector part**: the scalar part is carried by the unit — $1$ in the commutative two-parameter systems, $e_t$ in the quaternionic ones — and the vector part, in the quaternionic layers alone, by the remaining basis directions, carrying the arrow, $\vec q$ or $\vec Q$, so that $\tilde Q = Q_te_t + \vec Q$ is written in the coefficients according to the system; in the commutative two-parameter systems the second term is an imaginary, hyperbolic or dual part and not a vector part; in the quaternionic layers the two are the fixed and the anti-fixed spaces of the intrinsic conjugate, and the arithmetic systems, which are not written as linear combinations, have no vector part. **A pure element carries the arrow.** A pure element is one with no scalar part, a vector of its layer, and it is written with the arrow of the vector part: $\vec q$ and $\vec Q$ are the pure elements of the quaternion and of the biquaternion layers, standing by themselves (§*The Centre and the Vector Subspace*). The arrow names the vector part of a named element, $\vec Q$ in $\tilde Q = Q_te_t + \vec Q$, and it names the same object when the element is read on its own; the arrow and the tilde are never stacked.

For the biquaternions, whose basis is $e_t, \vec e_x, \vec e_y, \vec e_z$ with $e_t = 1$ the unit,

$$
\tilde Q = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z, \qquad Q_\mu = q_\mu + iq'_\mu,
$$

where the four coefficients $Q_\mu$ are complex, and each of them splits into a real part $q_\mu$ and an imaginary part $q'_\mu$. **The two parts of a coefficient share its letter**, the imaginary part carrying a prime. The shape is the same in the quaternion systems; only the coefficient sector changes, and the table above gives the element and the coefficients of each system. The unit $e_t$ is the identity in the two quaternion systems, and the real and the imaginary part of a coefficient may be read off only where the scalar sector is larger than the reals, which is the case in $\mathbb{C}$ and $\mathbb{B}$ and not in $\mathbb{R}$ or $\mathbb{H}$.

The case and the tilde are read independently, and the glyph of a generic element is the two together: $q$ is real, $Q$ complex, split-complex or dual, $\breve Q$ reduced biquaternion — upper case, with the breve, no tilde, and two complex coordinates — $\tilde q$ quaternion or split-quaternion, $\tilde Q$ biquaternion or split-biquaternion.

**A matrix carries no tilde, and neither does an array of elements.** The tilde marks the element, never the array that holds it: $\mathsf{M}_2(\tilde Q)$ keeps the tilde inside the argument, $I_n$, $\mathsf{M}_4^{L}$ and $\mathsf{M}_4^{R}$ carry none, and an array of biquaternions, $\mathsf{Q}=(\tilde Q_{\lambda\rho})\in\mathbb{B}^{n\times m}$, carries none either, its entries carrying theirs. A tilde on a matrix or on an array is forbidden: it is a defect, not a variant. A matrix of a model takes a letter of its own and never a glyph of the Q family: the matrix of an element is written $\mathsf{M}_2(\tilde Q)$ or $\mathsf{M}_4^{L}(\tilde Q)$, and a matrix parameter is written $A$, $B$ or $M$, the letter $Q$ staying with the element.

**The generic element of the biquaternion algebra is written $\tilde{Q}$, and only the Q family is generic there.** No letter outside the family, at any case, with any subscript, in any article, stands for an arbitrary element of the algebra: a letter outside the family names a specific object, or an element bound where it is introduced. A statement that holds for every element is written with $\tilde Q$; a statement that needs two writes them $\tilde Q_1$ and $\tilde Q_2$, and a third takes the next number. The trace pairing is $\operatorname{Tr}(\tilde Q_1\tilde Q_2) = 2\operatorname{Sc}(\tilde Q_1\tilde Q_2)$, the commutator bracket $[\tilde Q_1, \tilde Q_2] = \tilde Q_1\tilde Q_2 - \tilde Q_2\tilde Q_1$, the general plain bilinear form $\langle\tilde Q_1, \tilde Q_2\rangle$ and the multiplicativity $\langle\tilde Q_1\tilde Q_2\rangle_{\natural} = \langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, inherited from *Idempotents of the General Plain Algebra* and its companions, which write the generic element $\tilde Q$ beside the idempotent $\tilde\Pi$. The argument of an operator, the dummy of an annihilator, the second entry of a bracket and the element a map is applied to carry the same glyph: $L_{\tilde Q_1}(\tilde Q_2) = \tilde Q_1 \bullet \tilde Q_2$, $\{\tilde Q_2 : \tilde Q_1 \star \tilde Q_2 = 0\}$, $[\tilde Q_1, \tilde Q_2]$. The letters $X$, $Y$, $Z$ and $W$ name no element of the algebra: $X$ is kept for the universal cover $X^{\mathrm{cov}}$ and the left-invariant field, and $Y$, $Z$, $W$ are free of any element role. **In the layers of the biquaternion family the glyph $Q$ belongs to the element and never to an operator.** An operator generated by an element carries the structural capital and the element's own glyph in the subscript, $L_{\tilde Q}$, $R_{\tilde Q}$, $\Theta_{\tilde Q}$; an operator that is not the multiplication by an element takes the matrix letter $A$, with $T$ for its argument, so that a sandwich reads $H_A(T)=ATA^{\dagger}$. A bare $Q$ is never written for such an operator.

Where the constructions that share a glyph must be told apart — the complex from the split-complex and the dual, the quaternion from the split-quaternion, the biquaternion from the split-biquaternion — the glyph is qualified by a subscript, as in $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{H}_{\mathbb{D}}$.

**The letters of the mathematical quantities.** The glyphs of the elements are kept for the algebra, and a quantity that would borrow one is written with a letter of its own. The **quadratic form** takes the Fraktur $\mathfrak{Q}$ — Fraktur is already the script of a distinguished object here, as in $\mathfrak{a}$, $\mathfrak{p}$ and $\mathfrak{k}$, and the letter is free of every other use — so that the plain $q$ and $Q$ stay with the elements; its polarisation is written with the bracket $\langle\cdot,\cdot\rangle$, with $\mathfrak{Q}(v)=\langle v,v\rangle$, so that no letter is spent on it. The **null quadric** takes the calligraphic $\mathcal{Q}$, as in $\mathcal{Q}^{n+1}$, and the **signature indices** take $n$ and $m$, as in $\mathrm{Cl}_{n,m}$ and $O(n,m)$; the table of §*Summary of Notation* lists the three with the other quantities, and where a quantity is itself an element of the algebra it carries the glyph of an element.

**A logarithm carries the glyph of its element and the subscript $\log$.** The logarithm is not a new kind of object: it is a solution of the exponential equation in the same algebra, so it carries the glyph of that algebra and the subscript, and the definition reads $\exp(Q_{\log}) = Q$. The glyph is $Q_{\log}$ for a complex, split-complex or dual element, $\tilde q_{\log}$ for a quaternion or split-quaternion, $\tilde Q_{\log}$ for a biquaternion or split-biquaternion, and $\breve Q_{\log}$ for a reduced biquaternion. The subscript is a word, not a letter, so it competes neither with the direction labels, $Q_t$ and $Q_x$, nor with the counts, $Q_1$; a numbered element keeps its number in front of the subscript, $\tilde Q_{1\log}$ and $\breve Q_{2\log}$, as its coefficients keep theirs. The subscript is dropped when the logarithm is written as an operator, $\log Q$ or $\operatorname{Log}Q$, because an operator carries no subscript. **The coordinates of a logarithm follow the coefficient rule**: the element $Q_{\log}=q_{\log}+iq'_{\log}$ has real part $q_{\log}$ and imaginary part $q'_{\log}$, with $j$ in place of $i$ in the split-complex case. The prime marks the imaginary coordinate and nothing else. The logarithm of a real number is the ordinary real logarithm and takes no glyph of an algebra, so it is written $\log q$; the glyph $q_{\log}$ is the real coordinate of $Q_{\log}$, not the logarithm of $q$.

### The Points of the Duo-Complex Numbers

**A point of $\mathbb{C}^2$ is written $Q$, and its two coordinates carry the triangles.** In coordinates,
$$
Q=(Q_{\blacktriangle},Q_{\blacktriangledown}),\qquad Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle},\qquad Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown},
$$
with the four real parameters $q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown}$, the prime marking the slot that carries the $i$ as in every complex coefficient. **The ascending triangle marks the first coordinate and the descending triangle the second**, and the order is part of the notation. The case rule is that of the Q family: the scalar sector is $\mathbb{C}$, larger than the reals, so the glyph is upper case.

**The triangles mark the coordinates and the digits mark the basis.** In the standard basis $e_1,e_2$ the point is
$$
Q=Q_{\blacktriangle}e_1+Q_{\blacktriangledown}e_2,
$$
so the ascending triangle is the coefficient of $e_1$ and the descending triangle the coefficient of $e_2$. A triangle is never written on a basis vector, and the pair is read in the standard basis unless the article names another.

**The reduced biquaternion is the same pair with a product.** The points of $\mathbb{C}^2$ and the elements of $\mathbb{B}_{\mathrm{r}}$ are the same set of pairs, and the triangles name the same two slots in the two objects: the ascending triangle is the slot that the space writes $e_1$ and the algebra writes $1$, and the descending triangle the slot that the space writes $e_2$ and the algebra writes $j$, the basis of the algebra over $\mathbb{C}$ being $1,j$. **The breve is the whole difference.** The element $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is the point $Q$ together with the multiplication by $j$, $j^2=+1$ and $ji=ij$; the point carries no product, and no product of two points is written. The dictionary between the two is therefore coefficient by coefficient, and the one capital $Q$ serves both.

**Several points are numbered before the triangle.** Two points are $Q_1=(Q_{1\blacktriangle},Q_{1\blacktriangledown})$ and $Q_2=(Q_{2\blacktriangle},Q_{2\blacktriangledown})$, with $Q_{1\blacktriangle}=q_{1\blacktriangle}+iq'_{1\blacktriangle}$; the number counts the point and the triangle names the slot, as the number counts an element and the letter names a direction.

**The operations are componentwise, and a form takes two points as two arguments.** The sum and the scalar multiple are
$$
Q_1+Q_2=(Q_{1\blacktriangle}+Q_{2\blacktriangle},\,Q_{1\blacktriangledown}+Q_{2\blacktriangledown}),\qquad \lambda Q=(\lambda Q_{\blacktriangle},\,\lambda Q_{\blacktriangledown}),
$$
and a form on two points is written with two arguments, $H(Q_1,Q_2)$, as *Conventions of the Twelve Products and the Four Forms*, §*The Form Convention* requires.

**A point of the space is not written $z$.** The articles of the Duo-Complex Numbers category write a point as $Q$ and do not use $z$ for it, in agreement with *Several Complex Variables*, which writes a point of $\mathbb{C}^n$ as $Q$. The glyph of the point and the glyph of the complex element are the same, and the pair tells them apart: a bare $Q$ with no triangle is the complex number $Q=q+iq'$, and a point is always written as the pair.

## The Remarkable Subspaces of Biquaternions

The eight real parameters of a general element group into **remarkable subspaces**: the centre, the vector subspace, the quaternion and antiquaternion halves, and the Hermitian and anti-Hermitian halves. Each is cut out by a conjugation:

| Subspace | Defining condition | Dimension over $\mathbb{R}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $\tilde{Q}^{\natural} = \tilde{Q}$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $\bar{\tilde{Q}} = \tilde{Q}$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$, the antiquaternion subspace | $\bar{\tilde{Q}} = -\tilde{Q}$ | $4$ |
| $\mathbb{M}_+$, the Hermitian subspace | $\tilde{Q}^{*} = \tilde{Q}$ | $4$ |
| $\mathbb{M}_-$, the anti-Hermitian subspace | $\tilde{Q}^{\flat} = \tilde{Q}$ | $4$ |

The four marks are those of §*The Conjugations*. The first pair is the split of the scalar direction $e_t$ from the three vector directions; the second pair, the split by the coefficient conjugation; the third, the split by the star.

### The Centre and the Vector Subspace

The algebra is the direct sum

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}),
$$

the centre with the traceless part.

**The centre and the vector subspace carry a glyph each.** The centre is written with the tilde-free coefficient of $e_t$, $Q_te_t$, a complex scalar times the unit; the vector subspace is written $\vec Q$, the pure element, with the arrow and without the tilde.

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

the Hermitian subspace with the anti-Hermitian one. The element splits across the coefficient slots,

$$
\tilde Q = \tilde Q_{\mathrm H} + \tilde Q_{\mathrm A},\qquad
\tilde Q_{\mathrm H} = q_t\,e_t + i\bigl(q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z\bigr),\qquad
\tilde Q_{\mathrm A} = iq'_t\,e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z.
$$

$\tilde Q_{\mathrm H}$ takes the real scalar slot with the imaginary vector slots, and $\tilde Q_{\mathrm A}$ the imaginary scalar slot with the real vector slots. The two letters label the parts of one element and not two fields, so no label passes into the coefficients.

## The Conjugations

The biquaternion algebra carries three involutions — coefficient, natural and Hermitian — and the reversal $\flat=-{}^{*}$ beside them. The three give the six subspaces; $\flat$ repeats the two of ${}^{*}$ with the signs exchanged. All four are used in the series:

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

## Summary

The base is written with the letter $e$, one unit to a direction: the scalar unit $e_t=1$ and the three vector units $\vec e_x,\vec e_y,\vec e_z$. A generic element is $\tilde Q=\sum_{\mu}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu$, a coefficient carrying the name of the direction it multiplies and an element a number. The **case** records whether the scalar sector is larger than the reals and the **tilde** the presence of the quaternionic factor, and the two are read independently: $q$ is real, $Q$ complex, split-complex or dual, $\breve Q$ reduced biquaternion, $\tilde q$ quaternion or split-quaternion, $\tilde Q$ biquaternion or split-biquaternion. A matrix and an array carry no tilde.

The biquaternion algebra splits into the centre $\mathbb{C}_{\mathbb{B}}$ and the vector subspace $\mathrm{Vect}(\mathbb{B})$, the fixed and anti-fixed spaces of the intrinsic conjugate; into the quaternion and antiquaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, the real and imaginary halves; and into the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$, the fixed and anti-fixed spaces of the star. A pure element carries the arrow and no tilde, and the arrow takes priority where the two marks could fall on one glyph.

The biquaternion algebra carries three involutions — the coefficient bar, the natural sign ${}^{\natural}$ and the star ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ — and the reversal ${}^{\flat}=-{}^{*}$ beside them. Which of the marks has a sense depends on the layer, since a mark degenerates wherever the structure it conjugates is absent: the complex, split-complex and dual layers keep the bar, the quaternion and split-quaternion layers the natural sign, and the reduced biquaternion layer the bar, the tessarine sign and the star.

This article is the reference for the element, the subspaces and the marks. The products and forms, the norms, the special elements, the representations, the calculus and the indices are the subjects of the six companions, and the table below is the index of the glyphs they share.

## Summary of Notation

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
| $\mathbb{B}_L$, $M_4(\mathbb{C})_{\mathbb{B},L}$ | The image of the left regular representation, a four-dimensional subalgebra of $M_4(\mathbb{C})$; the right copy $\mathbb{B}_R=M_4(\mathbb{C})_{\mathbb{B},R}$ is its commutant |
| $\mathsf{M}_4^{L}(\tilde Q)$, $\mathsf{M}_4^{R}(\tilde Q)$ | The matrices of left and right multiplication by $\tilde Q$ in the basis the article names |
| $\mathbb{H}_{\mathbb{D}}$ | The split-biquaternions, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| Lower case, upper case | The scalar sector is the reals, or larger than the reals |
| Tilde | The presence of the quaternionic factor |
| Arrow | The vector part of a named element and a pure element standing by itself — $\vec q$ or $\vec Q$ (§*The Centre and the Vector Subspace*) |
| $\alpha, \beta$; $q, q_1, q_2$ | The generic elements of the Booleans, and of the rationals and the reals |
| $r/s$ | A rational written as a fraction, with numerator $r \in \mathbb{Z}$ and denominator $s \in \mathbb{N}_{\geq 1}$; in lowest terms $\gcd(r,s) = 1$; the letter $q$ is never a numerator or a denominator |
| $n$, $m$ | The generic elements of the naturals and the integers, and the signature indices, the counts of positive and negative directions of a real form, as in $\mathrm{Cl}_{n,m}$ and $O(n,m)$ |
| $Q = (Q_{\blacktriangle}, Q_{\blacktriangledown})$ | A duo-complex number, a point of $\mathbb{C}^2$: the ascending triangle is the first coordinate and the descending triangle the second, each complex, $Q_{\blacktriangle} = q_{\blacktriangle} + iq'_{\blacktriangle}$ and $Q_{\blacktriangledown} = q_{\blacktriangledown} + iq'_{\blacktriangledown}$; the same pair with the multiplication by $j$ is the reduced biquaternion $\breve Q$ |
| $Q = q + iq'$ | The generic element of a commutative two-parameter system, with $j$ or $\varepsilon$ in place of $i$, and the imaginary coefficient carrying a prime; where several occur they are numbered $Q_1, Q_2, \dots$ |
| $\breve Q = Q_{\blacktriangle} + jQ_{\blacktriangledown}$ | The generic element of the reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}$, upper case, with the breve and no tilde, its two coordinates $Q_{\blacktriangle} = q_{\blacktriangle} + iq'_{\blacktriangle}$ and $Q_{\blacktriangledown} = q_{\blacktriangledown} + iq'_{\blacktriangledown}$ complex and its second unit the hyperbolic $j$, $j^{2} = +1$ and $ji = ij$, on the basis $1, i, j, ij$ |
| $\tilde q$ | The generic element of the quaternion or split-quaternion layer |
| $\tilde Q$ | The generic element of the biquaternion or split-biquaternion layer, and the generic element of a statement that holds for every element; in a statement with several they are numbered $\tilde Q_1, \tilde Q_2, \dots$ |
| $Q_{\log}$ | A logarithm of $Q$, a solution of $\exp(Q_{\log}) = Q$: $Q_{\log}$ in the complex, split-complex and dual algebras, $\tilde q_{\log}$ in the quaternion and split-quaternion layers, $\tilde Q_{\log}$ in the biquaternion and split-biquaternion layers, $\breve Q_{\log}$ in the reduced biquaternion algebra |
| $\vec q$ | A pure element of the quaternion or split-quaternion layer, an element with no scalar part |
| $\vec Q$ | A pure element of the biquaternion or split-biquaternion layer |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | The centre and the vector subspace of the biquaternion algebra, the fixed and anti-fixed spaces of the intrinsic conjugate (§*The Remarkable Subspaces of Biquaternions*) |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | The quaternion and antiquaternion subspaces, the real and imaginary halves of the biquaternion algebra |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | The Hermitian and anti-Hermitian subspaces, the fixed and anti-fixed spaces of the star |
| $\tilde Q_{\mathrm H}$, $\tilde Q_{\mathrm A}$ | The Hermitian and anti-Hermitian parts of an element, $\tilde Q=\tilde Q_{\mathrm H}+\tilde Q_{\mathrm A}$ (§*The Hermitian and Anti-Hermitian Subspaces*) |
| $G$; $R$; $k$, $F$; $V$; $M$; $A$ | A group; a ring; a field; a vector space; a module; an algebra |
| $\mathrm{G}, \mathrm{H}, \mathrm{SL}_n$ | Lie algebras |
| $\mathrm{M}, \mathrm{P}$ | Ideals and prime ideals |
| $\operatorname{Sym}(X), \operatorname{Aut}(X)$ | The symmetric group of a set; the automorphism group of a structure |
| $\operatorname{End}(V), \operatorname{Der}(A), \operatorname{Inn}(A), \operatorname{Out}(A)$ | Endomorphisms, derivations, inner and outer automorphisms |
| $GL, SL, PGL, O, SO, U, SU, Sp$ | The classical groups |
| $T(V), S(V), \Lambda(V), Cl(V,\mathfrak{Q})$ | Tensor, symmetric, exterior and Clifford algebras |
| $V^{\otimes n}, S^n V, \Lambda^n V$ | Tensor, symmetric and exterior powers |
| $\langle v,w\rangle, \mathfrak{Q}(v), \lVert x\rVert$ | Bilinear form, quadratic form, norm |
| $P$, $N$, $H$, $K$ | The letters of the four forms and algebraic norms of the biquaternion layer — plain, quaternionic, Hermitian and Krein — each naming the form with two arguments and the norm with one; $P$ and not $B$, which is the complex modulus of the vector part and the right annihilator (*Conventions of the Twelve Products and the Four Forms*, §*The Form Convention*) |
| $\Phi$-regular, $\Phi$-degenerate | $\Phi(\tilde Q)\neq0$ and $\Phi(\tilde Q)=0$ for $\Phi\in\{P,N,H,K\}$; only the $N$ pair is the partition into units and non-units, and *regular* unqualified is spectral, $B^{2}\neq0$ (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*) |
| $\mathfrak{Q}$ | The quadratic form of a quadratic space, in Fraktur so that the plain $q$ and $Q$ stay with the elements |
| $\mathcal{Q}$ | The Lie or null quadric, in calligraphic, as in $\mathcal{Q}^{n+1}$ |
| $\bullet$ | The symmetrised (Jordan) product, $x \bullet y = \tfrac{1}{2}(xy + yx)$, and, with the slot subscripts ${}_{*}$, ${}_{\natural}$ and ${}_{\natural*}$, the four **symmetric products** of *Conventions of the Twelve Products and the Four Forms*, §*The Twelve Products and Their Names*; the circle $\circ$ is reserved for the composition of maps |
| $\wedge$ | The antisymmetrised product, $x \wedge y = \tfrac{1}{2}(xy - yx)$, and, with the same subscripts, the four **antisymmetric products** of *Conventions of the Twelve Products and the Four Forms*, §*The Twelve Products and Their Names*. On differential forms the same glyph is the exterior product, $\alpha\wedge\beta$, a different use |
| $\bar{\cdot}, {}^{\natural}, {}_{\mathrm{ts}}, {}^{*}, {}^{\flat}, {}^{\dagger}$ | The conjugations of an algebra with an involution — the bar, the natural sign ${}^{\natural}$, the tessarine sign ${}_{\mathrm{ts}}$ of $\mathbb{B}_{\mathrm{r}}$, the star, the anti-Hermitian sign — and the adjoint of an operator; §*The Conjugations* and *Conventions of the Operators and the Differential Calculus*, §*The Operators*, fix their meanings |
| $\tilde\Pi$, $\tilde\pi$, $\Pi$, $\Pi_\pm$ | An idempotent or a pure state, and the minimal left ideal it generates; the biquaternion layer writes $\tilde\Pi$, the quaternion layer $\tilde\pi$, and the tilde-free layers $\Pi$, the split-complex and reduced biquaternion ones writing the sign pair $\Pi_\pm$ (*Conventions of the Special Elements and the Peirce Decomposition*, §*The Idempotent Convention*) |
| $\tilde\Xi$, $\tilde\xi$, $\Xi$ | A root of $1$: the biquaternion layer writes $\tilde\Xi$, the quaternion layer $\tilde\xi$, and the tilde-free layers $\Xi$ (*Conventions of the Special Elements and the Peirce Decomposition*, §*The Root Convention*) |
| $\tilde\nu$ | A nilpotent of the quaternion or split-quaternion layer |
| $\tilde\Upsilon$ | A nilpotent of the biquaternion or split-biquaternion layer |
| $\Upsilon$ | A nilpotent of the complex, split-complex or dual layer, where no tilde is written |
| $\vec\Xi$, $\vec\Upsilon$ | A pure root of $1$ and a pure nilpotent of the biquaternion or split-biquaternion layer; $\vec\xi$ and $\vec\nu$ in the quaternion and split-quaternion layers |
| $\tilde u$, $\vec u$ | A unit element of the quaternion or split-quaternion layer, and its pure case, the axis of a rotation |
| $\tilde U$, $\vec U$ | A unit element of the biquaternion or split-biquaternion layer, $\langle\tilde U\rangle_{\natural}=e_t$ (the $N$-norm), and its pure case, of norm one |
| $U$ | A unit element of the complex, split-complex, dual or reduced biquaternion layer |
| $F^{\mathrm{fn}}, G^{\mathrm{fn}}, H^{\mathrm{fn}}$ | A function from a domain into the algebra, $F^{\mathrm{fn}} : \Omega \to \mathbb{B}$; the tilde marks a value and is never put on a map, since a function is not an element |
| $\tilde\nabla$ | The biquaternionic gradient, $\tilde\nabla = \sum_{\mu\in\{t,x,y,z\}} e_\mu \partial/\partial Q_\mu$; it keeps the tilde because its symbol is an algebra unit and not a letter |
| $g^{\mathrm{spin}}$ | An element of the group $\mathrm{Spin}(n)$ or $\mathrm{Pin}(n)$ on a principal bundle; not an element of the algebra |
| $^{\mathrm{fop}}$ | A **Fock operator**, an operator on the Fock space and not an element of the algebra — $a^{\mathrm{fop}}$, $N^{\mathrm{fop}}$, $H^{\mathrm{fop}}$, $U^{\mathrm{fop}}$. No other operator carries the mark. The opposite algebra uses the separate token $A^{\mathrm{opp}}$ |
| $\mathrm{Form}(\tilde Q_1,\tilde Q_2)$, $\mathrm{Norm}(\tilde Q)=\mathrm{Form}(\tilde Q,\tilde Q)$ | The generic form and the generic norm (*Conventions of the Twelve Products and the Four Forms*, §*The Form Convention*) |
| $\langle\tilde Q_1,\tilde Q_2\rangle$, $\langle\tilde Q\rangle$ | The generic bracket, the form in two arguments and the norm in one; the subscript records the pair of slots — plain, $*$ Hermitian, $\natural$ quaternionic, $\natural*$ Krein, and, in $\mathbb{B}_{\mathrm{r}}$, ${}_{\mathrm{ts}}$ tessarine and ${}_{\mathrm{ts}*}$ tessarine-Hermitian |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853). The original formulation, and the source of the quaternion conjugation and its notation.
- James Cockle, "On a new imaginary in algebra", *Philosophical Magazine* **34** (1849) 37–47. The tessarines, the commutative algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ that the corpus records as the reduced biquaternions, and the earliest occurrence of the hyperbolic versor.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022. The reduced biquaternion algebra of the engineering literature, its idempotent decomposition, its ring-valued norm and its transform.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution, the first and the second kind, and the classification of their involutions.
- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for a notation fixed once and used without variation.
