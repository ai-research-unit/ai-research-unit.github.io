# __The Cayley–Dickson Construction of the Biquaternion Algebra__

## Introduction

**A note on the order of the corpus.** This article is not the preferred construction of the algebra, and it is kept for the questions only it can answer. It reads the ladder in three layers, and two of the three spend a vector unit on a field: the first rung makes $\vec e_z$ the imaginary unit of $\mathbb{C}$, the second makes $\vec e_x$ the adjoined unit and computes $\vec e_y=\vec e_z\vec e_x$, and the third adds the central scalar $i$ to a construction that already carries a direction. Three units that the algebra treats alike therefore enter in three different roles, and the central scalar enters last, as a layer on top of a construction that ranks what it should not rank. Nothing here is wrong: the stack is complete, and it is the only route that shows why the third layer is a scalar extension and not a fourth rung.

**The preferred route.** It is *The Axis-Free Construction of the Biquaternion Algebra*, before this article in this category. It declares the four units and the central $i$ in one act, with three equal squares, one rule of anticommutation and a central scalar that appears in no entry of the table; it derives the same sixteen products, proves associativity inside the coefficient display, and derives the tensor product $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ as a theorem rather than taking it as a definition. The two articles prove different things about one object. What this article supplies and that one cannot is the reason for the signs and the reason the stack stops where it does.

The biquaternion algebra is the complexification of the quaternion algebra, and this article builds it as a stack of three layers. The first two are the rungs of the Cayley–Dickson doubling that carry the real numbers to the quaternions: the unit $\vec e_z$ adjoined to $\mathbb{R}$ gives $\mathbb{C}$, and the unit $\vec e_x$ adjoined to $\mathbb{C}$ under the twisting rule gives $\mathbb{H}$. The third layer is the scalar imaginary $i$, adjoined to $\mathbb{H}$ as a central element.

The article asks one question about the third layer and answers it: whether it is a fourth rung of the same ladder. It is not. The Cayley–Dickson double of an associative algebra is associative exactly when that algebra is commutative, so no double of $\mathbb{H}$ is associative, while $\mathbb{B}$ is associative. The move that produces $\mathbb{B}$ is the **scalar extension**: it adjoins a central element, which *Introduction to the Algebra of Biquaternions* calls the gate, and it leaves the four units of $\mathbb{H}$, their squares and their products untouched.

The rest follows from reading the third layer against the first two. It keeps the multiplication table, the associativity and the non-commutativity of the quaternion layer, it changes the centre from the real line to the complex line, and it destroys the division property. The mechanism of the last is short: every unit direction of the quaternion layer, multiplied by $i$, has square $+e_t$, so the layer carries the idempotents $\tfrac12(e_t\pm i\vec u)$ and the zero divisors $(e_t+i\vec e_x)(e_t-i\vec e_x)$.

**The boundaries.** The full Cayley–Dickson construction of $\mathbb{H}$, with the nine derivations of Hamilton's rules and the argument that fixes the twist, is *The Cayley–Dickson Construction of the Quaternion Algebra*, in the Quaternion Algebra category. The algebra $\mathbb{B}$, its table, its axioms and the proof that it is not a division algebra are *Introduction to the Algebra of Biquaternions*, above this article in this category. The element, its three coordinate systems and the four conjugations are *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*; the algebraic norms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the zero divisors and the unit criterion are *Zero Divisors and Invertibles in the Biquaternion Algebra*; the general doubling and its associativity criterion are *Quadratic Forms over Algebras and Norms*; the tensor product is *Tensor Products of Algebras*.

**What the construction uses.** One unit for the first rung, $\vec e_z$; one unit for the second, $\vec e_x$; one scalar for the third, $i$. The third direction of the vector subspace, $\vec e_y$, is computed and not adjoined, $\vec e_y=\vec e_z\vec e_x$. The letters j and k are not used at any layer: the three directions keep the letters $x$, $y$ and $z$, and the remaining letter is the scalar $i$.

## The Units of the Three Layers

Each layer is a real algebra, and the table records what was adjoined to obtain it.

| Layer | Algebra | Adjoined | Real dimension | Centre |
|---|---|---|---|---|
| 0 | $\mathbb{R}$ | — | 1 | $\mathbb{R}$ |
| 1 | $\mathbb{C}=\mathbb{R}[\vec e_z]$ | $\vec e_z$ | 2 | $\mathbb{C}$ |
| 2 | $\mathbb{H}=\mathbb{C}\oplus\mathbb{C}\vec e_x$ | $\vec e_x$ | 4 | $\mathbb{R}e_t$ |
| 3 | $\mathbb{B}=\mathbb{H}\oplus i\mathbb{H}$ | $i$ | 8 | $\mathbb{C}e_t$ |

**The glyphs.** The generic element of the second layer is written $\tilde q$ and the generic element of the third is written $\tilde Q$. The two are told apart by the case of the letter, because the third layer is the second read with complex coefficients: $\tilde Q=\tilde q+i\tilde q'$ with $\tilde q$ and $\tilde q'$ in $\mathbb{H}$. The vector part of $\tilde Q$ is $\vec Q$, and a coefficient is written $Q_\mu=q_\mu+iq'_\mu$ with $q_\mu$ and $q'_\mu$ real. The prime marks the imaginary part throughout.

**The arrows.** The three vector units carry the arrow and the two scalar units do not, at every layer: $\vec e_x,\vec e_y,\vec e_z$ name directions, while $e_t$ and $i$ are scalars. The arrow is a statement about the grade of an invertible element and not about its layer. The two scalars differ in a respect that the rest of this article is about: $e_t$ is the unit of the algebra and $i$ is a scalar of the coefficient field.

## Rung One: The Complex Algebra

**The square.** The first rung adjoins one unit with the square $\vec e_z^2=-e_t$.

**The algebra.** The span $\mathbb{R}[\vec e_z]=\{u+v\vec e_z\}$ is closed under the product, associative, commutative and two-dimensional, so it is the complex algebra. Its generic element is $w=u+v\vec e_z$ with $u$ and $v$ real.

**The product.** Expanding and using the square gives

$$
(u+v\vec e_z)(u'+v'\vec e_z)=(uu'-vv')+(uv'+vu')\vec e_z .
$$

**The conjugation of the rung.** The map $\bar w=u-v\vec e_z$ reverses the sign of the one imaginary direction, it is an involution, and it reverses the order of a product because the algebra is commutative. Its product with the element is the squared norm of the layer,

$$
w\bar w=u^2+v^2 ,
$$

a real number, zero only at $w=0$. This is the first rung; the derivation is §*The Base Algebra* of *The Cayley–Dickson Construction of the Quaternion Algebra*.

## Rung Two: The Quaternion Algebra

**The two rules.** The second rung adjoins the unit $\vec e_x$ with two rules and no others: its square, and the twisting rule that says how it passes a base element,

$$
\vec e_x^2=-e_t,\qquad \vec e_xw=\bar w\,\vec e_x\quad\text{for every }w\in\mathbb{C} .
$$

**The space.** The four elements $1,\vec e_z,\vec e_x,\vec e_z\vec e_x$ are linearly independent over $\mathbb{R}$, and every element is written uniquely as

$$
\tilde q=w_1+w_2\vec e_x,\qquad w_1,w_2\in\mathbb{C} .
$$

The four units are $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_y:=\vec e_z\vec e_x$.

**The product.** Applying the twist twice, and using that the base is commutative, gives

$$
(w_1+w_2\vec e_x)(w_3+w_4\vec e_x)=\bigl(w_1w_3-\bar w_4w_2\bigr)+\bigl(w_4w_1+w_2\bar w_3\bigr)\vec e_x .
$$

**The nine derivations.** The two rules produce the whole table of the layer, and each entry is one application of them.

| Rule | Derivation |
|---|---|
| $\vec e_z^2=-e_t$ | the square of the base unit, rung one |
| $\vec e_x^2=-e_t$ | the square of the new unit, by definition |
| $\vec e_x\vec e_z=-\vec e_z\vec e_x$ | the twist at $w=\vec e_z$, whose conjugate is $-\vec e_z$ |
| $\vec e_y^2=-e_t$ | $(\vec e_z\vec e_x)(\vec e_z\vec e_x)=\vec e_z(\vec e_x\vec e_z)\vec e_x=\vec e_z(-\vec e_z\vec e_x)\vec e_x=-\vec e_z^2\vec e_x^2=-e_t$, by the twist and then associativity |
| $\vec e_z\vec e_x=\vec e_y$ | the definition of the third direction |
| $\vec e_x\vec e_y=\vec e_z$ | $\vec e_x(\vec e_z\vec e_x)=-\vec e_z\vec e_x^2=\vec e_z$, by the twist and the square |
| $\vec e_y\vec e_x=-\vec e_z$ | $(\vec e_z\vec e_x)\vec e_x=\vec e_z\vec e_x^2=-\vec e_z$, by the square |
| $\vec e_y\vec e_z=\vec e_x$ | $(\vec e_z\vec e_x)\vec e_z=-\vec e_z^2\vec e_x=\vec e_x$, by the twist and the square |
| $\vec e_z\vec e_y=-\vec e_x$ | $\vec e_z(\vec e_z\vec e_x)=\vec e_z^2\vec e_x=-\vec e_x$, by the square |

**The table.** The nine rules collected are the multiplication table of the quaternion algebra.

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

**The cyclic triple.** The three directions multiply in the cycle $\vec e_z\vec e_x=\vec e_y$, $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, and the product of the three in that order is $\vec e_z\vec e_x\vec e_y=-e_t$, because the first two give $\vec e_y$ and $\vec e_y^2=-e_t$. The reversed order gives $+e_t$, and the difference is the whole of the non-commutativity of the layer.

**The ladder so far.** Two rungs, two units, and one rule besides the squares: the twist. The real dimension has doubled twice.

## The Third Layer

**The element adjoined.** The third layer adjoins one element $i$ with two properties,

$$
i^2=-e_t,\qquad i\,\tilde q=\tilde q\,i\quad\text{for every }\tilde q\in\mathbb{H} .
$$

The first is the square; the second says that $i$ is **central**, and it is the property that separates this layer from the two rungs below it. A central element of square $-e_t$ is what *Introduction to the Algebra of Biquaternions* calls a gate: it is the same datum as a complex algebra structure on a real algebra, with the scalar action $(a+ib)\tilde Q=a\tilde Q+b\,i\tilde Q$. Multiplication by $i$, the map $J(\tilde Q)=i\tilde Q$, is therefore the complex structure of the algebra, and it is the one of *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*.

**The space.** Every element of the layer is written uniquely as

$$
\tilde Q=\tilde q+i\tilde q',\qquad \tilde q,\tilde q'\in\mathbb{H} ,
$$

and the eight elements $e_t,\vec e_x,\vec e_y,\vec e_z,i,i\vec e_x,i\vec e_y,i\vec e_z$ are a real basis. The real dimension is eight and the complex dimension, with $i$ as the scalar, is four. The algebra is the tensor product $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ of the complex algebra and the quaternion algebra, by *Tensor Products of Algebras* and by §*The Tensor Product of the Two Multiplications* of *Introduction to the Algebra of Biquaternions*.

**The product rule.** For two elements,

$$
(\tilde q_1+i\tilde q_1')(\tilde q_2+i\tilde q_2')=\bigl(\tilde q_1\tilde q_2-\tilde q_1'\tilde q_2'\bigr)+i\bigl(\tilde q_1\tilde q_2'+\tilde q_1'\tilde q_2\bigr).
$$

*Proof.* Expand the four products. The term $\tilde q_1\tilde q_2$ is the first summand. The term $i\tilde q_1'\,i\tilde q_2'$ carries $i^2=-e_t$ and contributes $-\tilde q_1'\tilde q_2'$ to the real half. The two mixed terms are $\tilde q_1\,i\tilde q_2'$ and $i\tilde q_1'\,\tilde q_2$, and in each the central $i$ passes to the front without changing the order of the two quaternions, so they contribute $i\tilde q_1\tilde q_2'$ and $i\tilde q_1'\tilde q_2$. The four terms collected are the display.

**The table does not change.** The sixteen products of $e_t,\vec e_x,\vec e_y,\vec e_z$ are those of §*Rung Two: The Quaternion Algebra*, unchanged, because $i$ is never a factor of a product of two units: it is central, so it moves to the front of every term. This is why the table of a complex quaternion algebra is a table of real quaternions.

**The scalar-vector split.** The element splits as $\tilde Q=Q_te_t+\vec Q$ with the complex scalar $Q_t$ and the complex vector part $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, as in *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*. The two halves are recovered from the element by

$$
\tilde q=\tfrac12\bigl(\tilde Q+\bar{\tilde Q}\bigr),\qquad \tilde q'=\tfrac{1}{2i}\bigl(\tilde Q-\bar{\tilde Q}\bigr),
$$

where the bar is the coefficient conjugation of §*Conjugation, the Norm and the Inverse*.

## Why the Third Layer Is Not a Rung

The third layer doubles the real dimension, as each rung did, so it looks like an instance of the same rule. It is not, and the difference is worth stating exactly.

**The doubling rule.** For an algebra $A$ with an involution $\sigma$, the **double** is $A\oplus A$ with the product

$$
(a,b)(c,d)=\bigl(ac-\sigma(d)b,\;da+b\sigma(c)\bigr),
$$

whose new unit is $(0,e_t)$, of square $(-e_t,0)$.

**The two natural readings of the quaternion layer.** The quaternion algebra carries the conjugation $\natural$, which reverses the order of a product, and the identity, which preserves it; these are the two involutions the construction uses, and the two choices give two different doubles. Neither of them is $\mathbb{B}$.

**With the conjugation.** The choice $\sigma=\natural$ is the standard one, and the double is of real dimension eight. It is not associative, by the criterion proved below, and it is a division algebra. The construction and the loss of associativity are worked in *Quadratic Forms over Algebras and Norms*, §*The Cayley–Dickson Doubling*.

**With the identity.** The choice $\sigma=\mathrm{id}$ removes the conjugations from the rule, and the product becomes

$$
(a,b)(c,d)=\bigl(ac-db,\;da+bc\bigr).
$$

The layer's product, written in the same letters, is $(ac-bd,\,ad+bc)$. Subtracting it from the double leaves the two commutators and nothing else:

$$
\bigl(ac-db,\;da+bc\bigr)-\bigl(ac-bd,\;ad+bc\bigr)=\bigl([b,d],\,[d,a]\bigr).
$$

*Proof.* In the first slot $ac-db$ and $ac-bd$ differ by $bd-db=[b,d]$; in the second $da+bc$ and $ad+bc$ differ by $da-ad=[d,a]$.

**The consequence of the identity reading.** The two products agree on a pair of elements exactly when the imaginary half of the second factor commutes with the imaginary half of the first and with its real half. The quaternion algebra is not commutative, so they do not agree, and the double with the identity involution is a third algebra of real dimension eight. Its new unit is central, as in $\mathbb{B}$, and it is not $\mathbb{B}$: the difference is exactly the pair of commutators.

**The criterion.** The double of an associative algebra is associative exactly when that algebra is commutative, by *Quadratic Forms over Algebras and Norms*, §*The Cayley–Dickson Doubling*. The quaternion algebra is associative and not commutative, so **no Cayley–Dickson double of $\mathbb{H}$ is associative**, whichever involution is used. The algebra $\mathbb{B}$ is associative by §*What the Layer Keeps*. Therefore $\mathbb{B}$ is not a Cayley–Dickson double of $\mathbb{H}$: the third layer is not a rung of the ladder that produced the first two.

**What the layer is.** It is the scalar extension, the adjunction of a central element of square $-e_t$ to an algebra whose product is kept. The difference from a rung is read on the centre, and the table of §*What the Layer Keeps* shows it: a rung above the first never enlarges the centre, and the scalar extension always does.

## What the Layer Keeps

**The table and the subalgebra.** The sixteen products of the four units are unchanged, and an element with $\tilde q'=0$ multiplies as in $\mathbb{H}$. The quaternion layer is therefore a real subalgebra of $\mathbb{B}$, of real dimension four, and it is the fixed set of the coefficient conjugation.

**Associativity.** The layer is associative. Each factor of the tensor product is associative and the product of tensors is associative term by term; in coordinates, each of the eight basis elements multiplies by the table of $\mathbb{H}$ with the central $i$ carried as a coefficient, so the signs of a triple product collect exactly as in $\mathbb{H}$. The associativity is inherited from the tensor product and not from a doubling rule, which is the whole point of §*Why the Third Layer Is Not a Rung*.

**Non-commutativity.** $\vec e_x\vec e_y=\vec e_z$ while $\vec e_y\vec e_x=-\vec e_z$, and the two differ because $\vec e_z$ is a basis element. The layer is not commutative.

**The centre.** The centre of the layer is the complex line of the scalar multiples of the unit,

$$
Z(\mathbb{B})=\{Q_te_t\}=\mathbb{C}e_t=\mathbb{B}_{C} ,
$$

of real dimension two. *Proof.* The commutator $[X,Y]=XY-YX$ with a vector unit reads $[\tilde Q,\vec e_x]=2Q_z\vec e_y-2Q_y\vec e_z$, which vanishes exactly when $Q_y=Q_z=0$, and the two other commutators are its cyclic permutations. So centrality forces the three vector coefficients to vanish, and conversely every $Q_te_t$ is central because $i$ commutes with the four units. This is §*The Scalars Are the Centre* of *Introduction to the Algebra of Biquaternions*, read in the coordinates of the construction.

**The centre across the layers.** The centre grows at the first rung, shrinks at the second and grows again at the third.

| Layer | Centre | Real dimension |
|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | 1 |
| $\mathbb{C}$ | $\mathbb{C}$ | 2 |
| $\mathbb{H}$ | $\mathbb{R}e_t$ | 1 |
| $\mathbb{B}$ | $\mathbb{C}e_t$ | 2 |

**Why a rung does not enlarge the centre.** Beyond the first rung, the unit adjoined is not central: the twist makes $\vec e_x$ anticommute with $\vec e_z$, and the same twist inside the double makes the new unit of a rung above $\mathbb{H}$ non-central. What a later rung does to the centre is to carry the previous scalar direction into the vector subspace: $\vec e_z$ is a scalar at rung one and a direction at rung two. The scalar extension does the opposite. It adjoins an identity that is central by construction, so the centre grows by one real dimension and the vector subspace does not move, and that is the structural difference between the two moves.

## What the Layer Loses

**The square of a direction changes sign.** Every unit direction of the quaternion layer, multiplied by $i$, has square $+e_t$:

$$
(i\vec u)^2=i^2\vec u^2=(-e_t)(-e_t)=e_t ,
$$

for every $\vec u$ in the vector subspace with $\vec u^2=-e_t$, the three coordinate directions included.

**The idempotents.** For every such $\vec u$ the two elements

$$
\Pi_\pm=\tfrac12\bigl(e_t\pm i\vec u\bigr)
$$

are idempotent and orthogonal,

$$
\Pi_\pm^2=\tfrac14\bigl(e_t\pm2i\vec u+(i\vec u)^2\bigr)=\tfrac12\bigl(e_t\pm i\vec u\bigr)=\Pi_\pm,\qquad \Pi_+\Pi_-=\tfrac14\bigl(e_t-(i\vec u)^2\bigr)=0 .
$$

Neither vanishes, because $i\vec u$ has no real part and is not a real multiple of $e_t$. The layer therefore carries a continuum of orthogonal idempotent pairs, one pair to each unit direction, indexed by the sphere of directions modulo the sign.

**The zero divisors.** Each pair gives a product of two non-zero elements that vanishes:

$$
(e_t+i\vec e_x)(e_t-i\vec e_x)=e_t^2-(i\vec e_x)^2=e_t-e_t=0 .
$$

This is the witness of §*Central Simplicity and the Absence of Division* of *Introduction to the Algebra of Biquaternions*, and the two accounts agree.

**The division property is gone.** In $\mathbb{H}$ the only idempotents are $0$ and $e_t$, because $x^2=x$ gives $x(x-e_t)=0$ and the algebra has no zero divisors. In $\mathbb{B}$ every $\Pi_+$ of the family is a non-zero idempotent which is not the unit, so no such element is invertible, and the algebra is not a division algebra. The layer has kept the table and the associativity of $\mathbb{H}$ and has lost the property that made the table a division table.

**Why the loss is unavoidable.** The square of $i$ and the square of a direction are both $-e_t$, and the two signs multiply to $+e_t$ for every direction. A central element of square $-e_t$ adjoined to an algebra that already has a direction of square $-e_t$ produces $+e_t$ squares automatically, and with them the idempotents. The loss is not a defect of the construction; it is the construction.

## The Three Two-Dimensional Subalgebras

The layer contains three copies of a two-dimensional real algebra, and they are three different subalgebras.

| Subalgebra | Unit | Square of the unit | Central | Role |
|---|---|---|---|---|
| $\mathbb{R}[\vec e_z]$ | $\vec e_z$ | $-e_t$ | no | the first rung, inside the vector subspace |
| $\mathbb{R}[i]$ | $i$ | $-e_t$ | yes | the scalar field, the centre |
| $\mathbb{R}[i\vec e_z]$ | $i\vec e_z$ | $+e_t$ | no | the split line |

**Two copies of the complex algebra.** The first rung $\mathbb{R}[\vec e_z]$ and the coefficient field $\mathbb{R}[i]$ are both isomorphic to $\mathbb{C}$ and they are different subalgebras of $\mathbb{B}$. The first is contained in the vector subspace and is not central, since $\vec e_z\vec e_x=-\vec e_x\vec e_z$; the second is the centre. Their intersection is $\mathbb{R}e_t$. The first rung of the ladder therefore survives inside the third layer as a non-central copy, and the scalar of the third layer is a second copy, central.

**The split line.** The third subalgebra has a unit of square $+e_t$ and is the split-complex algebra of *Split-Complex Algebra*. It is the one that carries the idempotents of §*What the Layer Loses*, since $\tfrac12(e_t\pm i\vec e_z)$ are its two idempotents, and it is not central either, since $i\vec e_z$ inherits the non-centrality of $\vec e_z$ from the central factor $i$.

**The reading.** A biquaternion is read over three scalar systems at once, and the three lines say which: the complex line of the rung, the complex line of the scalars, and the split line of the idempotents. The sign $+e_t$ of the third is the inertia of the loss of §*What the Layer Loses*; the sign $-e_t$ of the first two is the inertia of the two rungs.

## Conjugation, the Norm and the Inverse

**The three maps.** The layer carries the quaternion conjugation $\natural$, the coefficient conjugation $\bar{\cdot}$, and their composite ${}^{*}=\bar{\cdot}\circ\natural=\natural\circ\bar{\cdot}$,

$$
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z,\qquad
\bar{\tilde Q}=\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z,
$$

$$
\tilde Q^{*}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z .
$$

**What each does.** All three are involutions. The conjugation $\natural$ is $\mathbb{C}$-linear, it fixes the scalar $i$ and the scalar line, and it reverses the three directions. The coefficient conjugation is conjugate-linear, it fixes the quaternion layer and it sends $i$ to $-i$. The star is conjugate-linear, and its fixed space is the Hermitian subspace of *Subspaces and Decompositions of the Biquaternion Algebra*, of real basis $e_t,i\vec e_x,i\vec e_y,i\vec e_z$.

**Which ones reverse the order.** The conjugation and the star reverse the order of a product, $(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}$ and $(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}$, and the coefficient conjugation does not: it is an automorphism, $\overline{\tilde Q_1\tilde Q_2}=\bar{\tilde Q_1}\,\bar{\tilde Q_2}$. The reason is that it conjugates the scalar field alone and fixes the quaternion factor, and a field is commutative. The composite of the star and the conjugation is the coefficient conjugation, an automorphism and not an anti-automorphism, and this is the identity $\bar{\cdot}={}^{\natural}{}^{*}$ of *The Group of Involutions of the Biquaternion Algebra*.

**The norm.** For every element,

$$
\tilde Q\tilde Q^{\natural}=N(\tilde Q)\,e_t,\qquad N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2\in\mathbb{C} .
$$

*Proof.* Expand $\sum_{\mu,\nu}Q_\mu Q_\nu\,e_\mu e_\nu^{\natural}$ over the sixteen pairs, with $e_t^{\natural}=e_t$ and $\vec e_k^{\natural}=-\vec e_k$. A pair with $\mu\neq\nu$ contributes $Q_\mu Q_\nu\,e_\mu e_\nu$ and its reverse contributes $-Q_\nu Q_\mu\,e_\nu e_\mu$, and the second is the negative of the first because $e_\nu e_\mu=-e_\mu e_\nu$ and the coefficients commute: the twelve off-diagonal pairs cancel in six pairs. What remains is the diagonal, $Q_t^2e_t$ from the scalar unit and $Q_k^2\vec e_k\vec e_k^{\natural}=-Q_k^2\vec e_k^2=+Q_k^2e_t$ from each of the three directions.

**The norm is complex.** In $\mathbb{H}$ the norm is a sum of four real squares and vanishes only at the origin. In $\mathbb{B}$ the squares are complex and the sum vanishes on non-zero elements:

$$
N(e_t+i\vec e_x)=1+i^2=0 .
$$

Its real part is $\sum_k q_k^2-\sum_k(q'_k)^2$, a form of inertia $(4,4)$ on the eight real coordinates, and its imaginary part is $2\sum_k q_kq'_k$. The norm of the layer is therefore not definite, and the identity $\tilde Q\tilde Q^{\natural}=Ne_t$ no longer forces $\tilde Q=0$.

**Multiplicativity.** The norm is multiplicative, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, by *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. In the coordinates of the construction it is the reduced norm of the layer, and its multiplicativity is the four-square identity of the quaternion rung read over $\mathbb{C}$.

**The inverse.** If $N(\tilde Q)\neq0$ then

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)} ,
$$

two-sided, because $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_t$ by the same computation on the other side. If $N(\tilde Q)=0$ and $\tilde Q\neq0$, then $\tilde Q\tilde Q^{\natural}=0$ with $\tilde Q^{\natural}\neq0$, so $\tilde Q$ is a zero divisor. Hence **an element is invertible exactly when its norm is non-zero**, which is the criterion of *Zero Divisors and Invertibles in the Biquaternion Algebra*, and the vanishing set of the norm is the set of the zero divisors of the layer.

## The Place of the Layer

**The ladder.** Three steps, of which two are rungs and one is a layer.

| Step | Move | Algebra | Real dimension | Associative | Division |
|---|---|---|---|---|---|
| 1 | adjoin $\vec e_z$ | $\mathbb{C}$ | 2 | yes | yes |
| 2 | adjoin $\vec e_x$, twisted | $\mathbb{H}$ | 4 | yes | yes |
| 3 | adjoin $i$, central | $\mathbb{B}$ | 8 | yes | no |

**What a rung at the third step would give.** A rung there is the double of $\mathbb{H}$ by an involution, and it agrees with the layer in two respects: the real dimension, eight, and the square of the adjoined element, $-e_t$. It differs in the rest: its product is not the product of the layer, the difference being the pair of commutators of §*Why the Third Layer Is Not a Rung*, and it is not associative. The third step therefore admits two moves, and only one of them keeps associativity; the layer is that one, and its price is the division property.

**The place of the layer.** The finite-dimensional associative division algebras over $\mathbb{R}$ are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, and by the theorem of Frobenius the list is complete. The layer neither continues that list nor pretends to: it keeps associativity and gives up division. Read the other way, it is the smallest enlargement of $\mathbb{H}$ that makes the algebra a complex algebra, and the enlargement costs the division property and nothing else.

**What the doubling cannot do.** No Cayley–Dickson double of $\mathbb{H}$ is associative, so the ladder cannot be climbed past the quaternions while keeping associativity. The layer is the only move available above $\mathbb{H}$ that keeps it, and it is a change of scalars rather than a change of units. The two operations act on different data: a rung adjoins a direction, and the layer adjoins a scalar.

## Summary

1. The biquaternion algebra is built as a stack of three layers: $\mathbb{R}\to\mathbb{C}$ by the unit $\vec e_z$, $\mathbb{C}\to\mathbb{H}$ by the unit $\vec e_x$ under the twisting rule, and $\mathbb{H}\to\mathbb{B}$ by the central scalar $i$.
2. The first two layers are the Cayley–Dickson rungs, and the third direction $\vec e_y$ is computed, $\vec e_y=\vec e_z\vec e_x$, not adjoined.
3. The third layer is not a rung. The double of an associative algebra is associative only when the algebra is commutative, and $\mathbb{H}$ is not, so no double of $\mathbb{H}$ is associative while $\mathbb{B}$ is.
4. The third layer is the scalar extension, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the adjunction of a central element of square $-e_t$ that the companion article calls the gate.
5. The product rule is $(\tilde q_1+i\tilde q_1')(\tilde q_2+i\tilde q_2')=(\tilde q_1\tilde q_2-\tilde q_1'\tilde q_2')+i(\tilde q_1\tilde q_2'+\tilde q_1'\tilde q_2)$, and the table of the four units is unchanged because $i$ is never a factor.
6. The layer keeps the table, the associativity and the non-commutativity of $\mathbb{H}$, and it changes the centre from $\mathbb{R}e_t$ to $\mathbb{C}e_t$, of real dimension two.
7. The layer destroys the division property: $(i\vec u)^2=+e_t$ for every invertible element direction, so the idempotents $\tfrac12(e_t\pm i\vec u)$ exist and $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$.
8. The layer contains three two-dimensional subalgebras: the non-central copy of $\mathbb{C}$ of the first rung, the central copy $\mathbb{R}[i]$ of the scalars, and the split line $\mathbb{R}[i\vec e_z]$ of the idempotents.
9. The norm is the complex number $N=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, with $\tilde Q\tilde Q^{\natural}=Ne_t$; it is multiplicative and not definite, and an element is invertible exactly when its norm is non-zero.
10. At the third step only the layer keeps associativity: a rung above $\mathbb{H}$ is not associative, whichever involution it uses, while $\mathbb{B}$ is associative and is not a division algebra.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $e_t$ | the scalar unit, $e_t=1$ | this article |
| $\vec e_x,\vec e_y,\vec e_z$ | the three directions, each of square $-e_t$ | this article, rung two |
| $i$ | the central scalar imaginary, $i^2=-e_t$ | this article, the third layer |
| $w=u+v\vec e_z$ | the generic element of the base $\mathbb{C}$ | this article, rung one |
| $\tilde q$ | the generic element of $\mathbb{H}$, $w_1+w_2\vec e_x$ | this article, rung two |
| $\tilde Q=\tilde q+i\tilde q'$ | the generic element of $\mathbb{B}$ | *Introduction to the Algebra of Biquaternions* |
| $Q_\mu=q_\mu+iq'_\mu$ | a complex coefficient and its two real parts | *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra* |
| $\vec Q$ | the vector part, $Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra* |
| $\natural$ | the quaternion conjugation, $\mathbb{C}$-linear | *The Group of Involutions of the Biquaternion Algebra* |
| $\bar{\cdot}$ | the coefficient conjugation, $i\mapsto-i$ | *The Group of Involutions of the Biquaternion Algebra* |
| ${}^{*}$ | the composite $\bar{\cdot}\circ\natural$, the Hermitian conjugation | *The Group of Involutions of the Biquaternion Algebra* |
| $N(\tilde Q)$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$, the scalar of $\tilde Q\tilde Q^{\natural}$ | *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* |
| $\Pi_\pm$ | $\tfrac12(e_t\pm i\vec u)$, the idempotents of the layer | this article |
| $J$ | the complex structure $\tilde Q\mapsto i\tilde Q$ | *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra* |

## Further Reading

- Leonard E. Dickson, *On Quaternions and Their Generalization and the History of the Eight Square Theorem* (Annals of Mathematics, 1919), for the doubling as a construction and its sign choices.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Dover, 1995), for the doubling rule and its associativity criterion.
- Eduard Study, *Geometrie der Dynamen* (Leipzig, 1903), for the complex quaternion algebra in its classical use in kinematics, where the scalar imaginary is kept apart from the quaternion units as this article keeps it.
