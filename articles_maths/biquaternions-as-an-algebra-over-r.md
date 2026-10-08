# __Biquaternions as an Algebra over $\mathbb{R}$__

## Introduction

The underlying $\mathbb{R}$-vector space of the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is eight-dimensional, with the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ of *Biquaternions as a Vector Space over $\mathbb{R}$*. The general plain bilinear product of *The Four Biquaternion Complex Products* is $\mathbb{R}$-bilinear as well as $\mathbb{C}$-bilinear, so the same rule that makes that space a $\mathbb{C}$-algebra also makes it an $\mathbb{R}$-algebra, of twice the dimension. This article takes that product as the multiplication of the **real algebra** and reads off the structure the real scalars produce.

The axioms are the same as over $\mathbb{C}$ and what they produce is finer. The product is $\mathbb{R}$-bilinear, associative and unital, so the space is an associative unital $\mathbb{R}$-algebra; the sixty-four products of the eight basis elements fix the multiplication; and the algebra is then read off. What the smaller scalar system exposes is the subject of the middle of the article: the central imaginary $i$ is an element of the real algebra rather than a scalar, so the real algebra carries the complex structure of $\mathbb{B}$ as an operator; the four conjugations are all ordinary $\mathbb{R}$-linear maps; and the signs of the squares of the eight basis elements separate the quaternion directions from the complex and split-complex ones.

Two boundaries are stated at once. The product is not defined here: its coordinate rule and its scalar–vector form are *Introduction to the General Plain Algebra of Biquaternions*. The reading of the same product with the complex scalars is *Introduction to the General Plain Algebra of Biquaternions*, where the structure map, the centre and central simplicity are developed, and the complex algebra cited here is that article's; the real scalars are used here and the complex material is cited, not repeated. The elements, the basis, the conjugations and the six distinguished subspaces are *Biquaternions as a Vector Space over $\mathbb{C}$*.

The general theory is *Algebras: A General Introduction*, associativity is *Associative Algebras*, the identity is *Unital Algebras*, the restriction and the extension of scalars are *Change of Rings* and *Extension of Scalars*, the split complex numbers are *Split-Complex Algebra*, the quaternions are *Quaternion Algebra*, the real form is *Real Forms and the Descent of an Algebra*, the group of conjugations is *The Group of Involutions*, and the simplicity is *Biquaternion Ideals and Peirce Decomposition*.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is read here with the real scalars, on the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$. A general element is $\tilde Q = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, equivalently $\tilde Q = \sum_\mu q_\mu e_\mu + \sum_\mu q'_\mu\,(ie_\mu)$ with real $q_\mu,q'_\mu$; the scalar imaginary $i$ is the central element $ie_0$ of square $-e_0$, and $(\mathbf P,\mathbf Q) = \sum_k P_kQ_k$ is the complex bilinear dot product of the vector parts.

## The Multiplication as a Binary Operation

### The Rule

**Definition.** The **multiplication** of the real algebra is the rule

$$
\cdot \; : \; \mathbb{B} \times \mathbb{B} \longrightarrow \mathbb{B} , \qquad
(\tilde P,\tilde Q) \longmapsto \tilde P\tilde Q = \sum_{\mu=0}^{3}\sum_{\nu=0}^{3} P_\mu Q_\nu \, e_\mu e_\nu ,
$$

the general plain bilinear product. Each of the sixteen products $e_\mu e_\nu$ is a basis element up to sign and $i^2 = -e_0$ with $i$ central, so the double sum is an $\mathbb{R}$-linear combination of $e_0,\dots,e_3,ie_0,\dots,ie_3$: the rule is a map into $\mathbb{B}$ and is well defined.

On the eight real coordinates it is the complex coordinate rule read apart. Writing $P_\mu = p_\mu + ip'_\mu$ and $Q_\nu = q_\nu + iq'_\nu$,

$$
\tilde P\tilde Q = \sum_{\mu=0}^{3} R_\mu e_\mu , \qquad
\begin{aligned}
R_0 &= P_0Q_0 - P_1Q_1 - P_2Q_2 - P_3Q_3 , \\
R_1 &= P_0Q_1 + P_1Q_0 + P_2Q_3 - P_3Q_2 , \\
R_2 &= P_0Q_2 - P_1Q_3 + P_2Q_0 + P_3Q_1 , \\
R_3 &= P_0Q_3 + P_1Q_2 - P_2Q_1 + P_3Q_0 ,
\end{aligned}
$$

with each $R_\mu$ complex and each of its two real parts a real bilinear expression in the eight coordinates of $\tilde P$ and $\tilde Q$.

### The Multiplication Table

An $\mathbb{R}$-bilinear product is fixed by its values on the pairs of basis elements, so the multiplication is fixed by the following sixty-four products. They are arranged in four blocks: the products of the four quaternion units, the two mixed blocks where exactly one factor carries $i$, and the block where both do.

**Proposition.** The products of the eight basis elements are

| | $e_0$ | $e_1$ | $e_2$ | $e_3$ | $ie_0$ | $ie_1$ | $ie_2$ | $ie_3$ |
|---|---|---|---|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ | $ie_0$ | $ie_1$ | $ie_2$ | $ie_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ | $ie_1$ | $-ie_0$ | $ie_3$ | $-ie_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ | $ie_2$ | $-ie_3$ | $-ie_0$ | $ie_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ | $ie_3$ | $ie_2$ | $-ie_1$ | $-ie_0$ |
| $ie_0$ | $ie_0$ | $ie_1$ | $ie_2$ | $ie_3$ | $-e_0$ | $-e_1$ | $-e_2$ | $-e_3$ |
| $ie_1$ | $ie_1$ | $-ie_0$ | $ie_3$ | $-ie_2$ | $-e_1$ | $e_0$ | $-e_3$ | $e_2$ |
| $ie_2$ | $ie_2$ | $-ie_3$ | $-ie_0$ | $ie_1$ | $-e_2$ | $e_3$ | $e_0$ | $-e_1$ |
| $ie_3$ | $ie_3$ | $ie_2$ | $-ie_1$ | $-ie_0$ | $-e_3$ | $-e_2$ | $e_1$ | $e_0$ |

**Proof.** The upper left block is the product of the quaternion units, $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$ and $e_1^2 = e_2^2 = e_3^2 = -e_0$, of *Quaternion Algebra*. The two mixed blocks are that table multiplied by $i$: $e_\mu(ie_\nu) = i(e_\mu e_\nu) = (ie_\mu)e_\nu$ because $i$ is central. The lower right block is the table with every entry negated, $(ie_\mu)(ie_\nu) = i^2(e_\mu e_\nu) = -e_\mu e_\nu$, since $i^2 = -e_0$. Every entry is therefore a basis element up to sign.

The table is not the quaternion table, because the real basis is not closed at the four quaternion units: $i$ is now an element rather than a scalar, and the products $ie_\mu$ have to be listed. The block structure is the visible trace of that, and so is the diagonal: $e_0$ has square $e_0$, the three units $e_1,e_2,e_3$ have square $-e_0$, the element $ie_0$ has square $-e_0$, and the three elements $ie_1,ie_2,ie_3$ have square $+e_0$. The last four signs are the subject of §*The Two Kinds of Imaginary Unit*.

### Bilinearity and the Determination by the Table

**Proposition.** The multiplication is $\mathbb{R}$-**bilinear**:

$$
(\tilde P + \tilde Q)\tilde R = \tilde P\tilde R + \tilde Q\tilde R , \qquad
\tilde R(\tilde P + \tilde Q) = \tilde R\tilde P + \tilde R\tilde Q , \qquad
(r\tilde P)\tilde Q = r(\tilde P\tilde Q) = \tilde P(r\tilde Q) , \qquad r \in \mathbb{R} .
$$

**Proof.** Every coordinate on the right of the developed form is a sum of terms $p_\mu q_\nu$, $p_\mu q'_\nu$, $p'_\mu q_\nu$ or $p'_\mu q'_\nu$ with a fixed coefficient, hence is additive and homogeneous in the eight coordinates of $\tilde P$ alone and in the eight coordinates of $\tilde Q$ alone. The three identities are that statement read coordinate by coordinate.

**Proposition (determination by the table).** The multiplication is the unique $\mathbb{R}$-bilinear map $\mathbb{B} \times \mathbb{B} \to \mathbb{B}$ sending the pair $(b_i,b_j)$ of basis elements to the product $b_ib_j$ of the table.

**Proof.** An $\mathbb{R}$-bilinear map is determined by its values on the pairs of basis elements, and the double sum of the definition is such a map and takes those values.

**Corollary.** Two multiplications on the same real space that agree on the sixty-four pairs of basis elements agree on every pair.

## The Algebra Axioms

### Associativity

**Proposition.** The multiplication is **associative**: $(\tilde P\tilde Q)\tilde R = \tilde P(\tilde Q\tilde R)$ for all $\tilde P,\tilde Q,\tilde R \in \mathbb{B}$.

**Proof.** Both sides are $\mathbb{R}$-trilinear in $(\tilde P,\tilde Q,\tilde R)$, being built from the multiplication by bilinearity, so it suffices to check the $8^3 = 512$ triples of basis elements. A basis element is $\varepsilon e_\mu$ with $\varepsilon \in \{1,i\}$, every product of two of them is a basis element up to sign by the table, and the coefficient sign is a central scalar; each triple product is therefore a quaternion triple product with central scalars, and those associate. The two sides agree on the basis triples, hence everywhere.

### The Unit

**Proposition.** The element $e_0$ is a **two-sided identity**: $e_0\tilde Q = \tilde Q e_0 = \tilde Q$ for every $\tilde Q$.

**Proof.** By bilinearity it suffices to check $\tilde Q = b_k$ for the eight basis elements, and the first row and the first column of the table give it.

The identity is unique: a two-sided identity $u$ satisfies $u = uu' = u'$ for any other two-sided identity $u'$. It is written $e_0$ or $1$.

### Non-Commutativity

**Proposition.** The multiplication is **not commutative**.

**Proof.** $e_1e_2 = e_3$ while $e_2e_1 = -e_3$, and $e_3 \neq -e_3$.

### The Algebra Structure

**Theorem.** With the general plain bilinear product as its multiplication, $\mathbb{B}$ is an eight-dimensional associative unital non-commutative $\mathbb{R}$-algebra.

**Proof.** By the propositions above the multiplication is an $\mathbb{R}$-bilinear, associative, unital binary operation on the eight-dimensional $\mathbb{R}$-vector space $\mathbb{B}$, which is the definition of an algebra over the commutative ring $\mathbb{R}$ in the broad sense of *Algebras: A General Introduction*; the two hypotheses the corpus adds to that sense, associativity and an identity, hold (*Associative Algebras*, *Unital Algebras*). The dimension is eight on the stated basis, and $e_1e_2 \neq e_2e_1$.

Every general statement about associative unital algebras is therefore available for $\mathbb{B}$ over $\mathbb{R}$ as it is over $\mathbb{C}$: the two-sided ideals, the centre, the group of units, the modules and the opposite algebra. The rest of this article reads off the ones that the real scalars decide.

## The Two Kinds of Imaginary Unit

### The Squares of the Eight Basis Elements

The eight basis elements fall into four classes by their squares:

| element | square | reason |
|---|---|---|
| $e_0$ | $+e_0$ | the unit |
| $e_1,e_2,e_3$ | $-e_0$ | the quaternion units |
| $ie_0$ | $-e_0$ | $i^2e_0^2 = (-1)(+e_0)$ |
| $ie_1,ie_2,ie_3$ | $+e_0$ | $i^2e_k^2 = (-1)(-e_0)$ |

The four elements $ie_0,ie_1,ie_2,ie_3$ are therefore **not** a second set of quaternion units. The element $ie_0$ is a second square root of $-e_0$, and because it is central it generates a field, not a split ring. The three elements $ie_1,ie_2,ie_3$ square to $+e_0$, and each of them generates a copy of the split complex numbers. The real algebra displays the two kinds of imaginary direction side by side, and the real scalars are the only reading in which the two are visible: over $\mathbb{C}$ the element $i$ is a scalar, and the relations $(ie_k)^2 = +e_0$ dissolve into $i^2e_k^2 = e_0$ by pulling the scalars out of the product.

### The Split-Complex Planes

**Proposition.** For each $k = 1,2,3$ the plane $\operatorname{span}_\mathbb{R}\{e_0, ie_k\}$ is closed under the product and is isomorphic, as a real algebra, to the split complex numbers $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$:

$$
(a e_0 + b\, ie_k)(c e_0 + d\, ie_k) = (ac + bd)e_0 + (ad + bc)\, ie_k .
$$

**Proof.** All products lie in the plane by the relations $e_0^2 = e_0$ and $(ie_k)^2 = e_0$, and the multiplication is commutative on the plane because $ie_k$ commutes with itself and with $e_0$; the rule displayed is the product of $\mathbb{D}$ under the correspondence $ie_k \leftrightarrow x$, with $x^2 = 1$.

**Corollary.** The elements $\tilde\Pi_\pm = \tfrac12(e_0 \pm ie_k)$ are orthogonal idempotents, $\tilde\Pi_+ + \tilde\Pi_- = e_0$ and $\tilde\Pi_+\tilde\Pi_- = 0$, and the plane is $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ by the idempotent decomposition of *Split-Complex Algebra*. The conjugate pair $ae_0 \pm b\,ie_k$ has product $(a^2 - b^2)e_0$, a null line when $a = \pm b$.

### The Centre Is a Field

**Proposition.** The centre of $\mathbb{B}$ is the plane $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$, and it is a field:

$$
(a e_0 + b\, ie_0)(a e_0 - b\, ie_0) = (a^2 + b^2)e_0 , \qquad a,b \in \mathbb{R} .
$$

**Proof.** The centre is $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$ by *Introduction to the General Plain Algebra of Biquaternions*, §*The Scalars Are the Centre*, where the centrality criterion $[\tilde Q,e_1] = [\tilde Q,e_2] = 0 \iff Q_1 = Q_2 = Q_3 = 0$ is proved. On the centre $(ie_0)^2 = -e_0$, so the displayed product is $a^2e_0 - b^2(ie_0)^2 = (a^2+b^2)e_0$, which vanishes only at $a = b = 0$.

**Corollary.** The centre is a field of real dimension two, and it is not one of the split-complex planes: its generator squares to $-e_0$, while $(ie_k)^2 = +e_0$ for $k = 1,2,3$. The real algebra is therefore **not** split at its centre, and no scalar of the real algebra is a zero divisor.

## The Conjugations Are Ordinary Linear Maps

### All Four Are $\mathbb{R}$-Linear

The four conjugations of *Biquaternions as a Vector Space over $\mathbb{C}$* are

$$
\natural(\tilde Q) = Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3 , \qquad
\bar{\tilde Q} = \bar Q_0e_0 + \bar Q_1e_1 + \bar Q_2e_2 + \bar Q_3e_3 ,
$$

$$
\tilde Q^{*} = \natural(\bar{\tilde Q}) = \bar{\tilde Q^{\natural}} , \qquad
\tilde Q^{\flat} = -\tilde Q^{*} .
$$

**Proposition.** All four are $\mathbb{R}$-**linear** maps of the real algebra, and $\natural$ is an algebra anti-automorphism while $\bar{\cdot}$ is an algebra automorphism.

**Proof.** Each of the four fixes or negates real scalars and acts on the eight real coordinates by a fixed real permutation with signs, so each is additive and homogeneous over $\mathbb{R}$. The anti-automorphism and automorphism properties are those of *The Group of Involutions*.

### The Two That Change Character over $\mathbb{C}$

Over $\mathbb{C}$ the map $\natural$ fixes the coefficients and so is $\mathbb{C}$-linear, while $\bar{\cdot}$ and ${}^{*} = \bar{\cdot} \circ \natural$ conjugate them and are only $\mathbb{C}$-antilinear; the real reading draws no distinction between the two notions, since the conjugate of a real scalar is itself. This is the simplest of the two readings of the four maps, and the one in which each of them is an ordinary linear operator: the natural conjugation is a reflection, the complex conjugation is a reflection of a different kind, and the star and the flat map are the composites.

The algebra structure of the four is nonetheless the same in both readings: $\natural$ is a $\mathbb{C}$-linear anti-automorphism of the complex algebra and an $\mathbb{R}$-linear anti-automorphism of the real one, and $\bar{\cdot}$ is an automorphism of the underlying real algebra that is conjugate-linear over $\mathbb{C}$. It is therefore not a $\mathbb{C}$-algebra automorphism.

## The Complex Structure and the Change of Scalars

### The Central Element as a Complex Structure

The element $i = ie_0$ is central of square $-e_0$, so the map

$$
J : \mathbb{B} \longrightarrow \mathbb{B} , \qquad J(\tilde Q) = i\tilde Q , \qquad J^2 = -\mathrm{id} ,
$$

is a real-linear map with no nonzero fixed vector, and it makes the underlying real space a complex vector space of dimension four — the complex structure of *Biquaternions as a Vector Space over $\mathbb{R}$*. Because $i$ is central, $J$ is not merely linear but an **algebra automorphism** of the real algebra, $J(\tilde P\tilde Q) = J(\tilde P)\tilde Q = \tilde P J(\tilde Q)$, so the complex structure is compatible with the multiplication; and every $\mathbb{C}$-linear map of the complex algebra is $\mathbb{R}$-linear, so the two scalar systems are compatible as *Extension of Scalars* requires.

### Restriction of Scalars

The two algebra structures of the same set are related by one operation. The complex algebra is $\mathbb{B}$ on the four basis elements $e_0,e_1,e_2,e_3$ with $\mathbb{C}$-bilinear product, and the real algebra here is its **restriction of scalars** $R_{\mathbb{C}/\mathbb{R}}\mathbb{B}$ (*Change of Rings*): the same addition, the same product, the same elements, with the field of scalars taken from $\mathbb{C}$ down to $\mathbb{R}$. The dimension doubles and nothing else changes,

$$
\dim_\mathbb{R} \mathbb{B} = 2 \dim_\mathbb{C} \mathbb{B} = 8 ,
$$

so every $\mathbb{C}$-linear statement is an $\mathbb{R}$-linear statement and the real reading is the weaker one. The real algebra is the object in which the product is defined before any scalar is chosen; over $\mathbb{C}$ the element $i$ has been promoted to a scalar and the basis shrinks from eight to four.

### The Complexification Is Not the Complex Algebra

The extension of scalars runs the other way and does **not** return the complex algebra. For the complex algebra is four-dimensional over $\mathbb{C}$, whereas the extension $\mathbb{C} \otimes_\mathbb{R} \mathbb{B}$ of the real algebra has complex dimension eight:

$$
\dim_\mathbb{C}(\mathbb{C} \otimes_\mathbb{R} \mathbb{B}) = \dim_\mathbb{R}\mathbb{B} = 8 \neq 4 = \dim_\mathbb{C}\mathbb{B} .
$$

The complex algebra is instead the extension of scalars of the quaternion algebra, $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ (*Introduction to the General Plain Algebra of Biquaternions*, §*The Tensor Product*), of complex dimension four. The pair of algebras is therefore linked by restriction of scalars in one direction only, and an extension of the real algebra is a larger algebra, not the complex one.

## The Admissible Bases: $\mathbb{R}$, $\mathbb{C}$ and Not $\mathbb{H}$

### The Criterion

An algebra structure over a commutative ring $R$ on a ring $A$ is a unital ring homomorphism $R \to Z(A)$ into the centre of $A$ (*Algebras: A General Introduction*). The base ring therefore has to map into the centre, and the image has to be central, so that the product is $R$-bilinear. The centre decides which rings can serve, and for $\mathbb{B}$ it is the complex line $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$ of §*The Centre Is a Field*.

### The Table

| base ring | is $\mathbb{B}$ an algebra over it? | reason |
|---|---|---|
| $\mathbb{R}$ | yes | $\mathbb{R} \subset \mathbb{C} = Z(\mathbb{B})$, so the image is central |
| $\mathbb{C}$ | yes | $A \mapsto Ae_0$ lands on $Z(\mathbb{B}) = \mathbb{C}$ |
| $\mathbb{H}$ | no | $\mathbb{H}$ is non-commutative and simple, so no unital homomorphism $\mathbb{H} \to \mathbb{C}$ exists |
| $\mathbb{B}$ | no | the same obstruction, with the identity map in place of the embedding of $\mathbb{H}$ |

The first two rows are the two readings of the same product developed in this article and in *Introduction to the General Plain Algebra of Biquaternions*; the last two are the excluded candidates.

### Why the Quaternions Fail

The canonical embedding

$$
\psi : \mathbb{H} \longrightarrow \mathbb{B} , \qquad \psi(h) = 1 \otimes h ,
$$

is an injective unital ring homomorphism, with image the quaternion subspace $\mathbb{H}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2,e_3\}$. It is a homomorphism into the algebra but not into its centre: $\psi(e_2) = e_2$ fails to commute with $e_1$, since $e_1e_2 = -e_2e_1$. No other map can repair this, because no unital homomorphism $\mathbb{H} \to \mathbb{C}$ exists at all: such a map would be injective, $\mathbb{H}$ being simple, and its image would lie in a commutative ring, which $\mathbb{H}$ cannot. There is therefore no map $\mathbb{H} \to Z(\mathbb{B})$ to serve as a structure map, and $\mathbb{B}$ is a ring over $\mathbb{H}$ as a bimodule only, which is *Biquaternions as a Bimodule over $\mathbb{H}$*. The same argument applies with $\mathbb{B}$ in place of $\mathbb{H}$: the identity map has image all of $\mathbb{B}$, which is not central.

### The Natural Base

Two rings therefore admit $\mathbb{B}$ as an algebra and they sit one inside the other. The centre of the real algebra is itself a copy of the complex numbers, so the algebra is **central** as a $\mathbb{C}$-algebra and merely simple as an $\mathbb{R}$-algebra: over $\mathbb{R}$ the base ring is a proper subfield of the centre, and over $\mathbb{C}$ the base ring is the centre. The finer reading is the complex one, and the coarser is the restriction of the finer:

$$
\boxed{\ \text{The same product makes } \mathbb{B} \text{ an associative unital } \mathbb{R}\text{-algebra of dimension eight and a } \mathbb{C}\text{-algebra of dimension four.}\ }
$$

## The Real Form and the Subalgebras

### The Quaternion Subalgebra and Its Imaginary

The quaternion subspace $\mathbb{H}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2,e_3\}$ is closed under the product and carries the quaternion product, so it is a **real** subalgebra, closed under real scalars only and not a $\mathbb{C}$-subalgebra. Its imaginary $i\mathbb{H}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{ie_0,ie_1,ie_2,ie_3\}$ is neither a $\mathbb{C}$-subspace nor a subalgebra, since $i\,(ie_1) = -e_1$ and $(ie_1)^2 = e_0$ both leave it. The two halves of the real decomposition

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}
$$

thus differ in kind: one is a subalgebra, the other is not. Both statements are the real-space form of material proved in *Introduction to the General Plain Algebra of Biquaternions*, §*The Quaternion Subalgebra and Its Imaginary*, and they are repeated here only because the real scalars are the reading in which the signs $-e_0$ and $+e_0$ are visible.

Since $\mathbb{C} \otimes_\mathbb{R} \mathbb{H}_{\mathbb{B}} \cong \mathbb{B}$, the quaternion subalgebra is a **real form** of $\mathbb{B}$ — a real algebra whose extension of scalars is the complex algebra — the subject of *Real Forms and the Descent of an Algebra*.

### The Subalgebra Generated by One Element

**Proposition.** The real subalgebra $\mathbb{R}[\tilde Q] = \operatorname{span}_\mathbb{R}\{e_0,\tilde Q,\tilde Q^2,\dots\}$ generated by one element is commutative, and it is contained in the complex plane $\mathbb{C}[\tilde Q] = \mathbb{C}e_0 \oplus \mathbb{C}\tilde Q$ read with the real scalars: for every $\tilde Q$,

$$
\tilde Q^2 = \bigl(Q_0^2 - (\mathbf Q,\mathbf Q)\bigr)e_0 + 2Q_0\mathbf Q \in \mathbb{C}e_0 + \mathbb{C}\tilde Q , \qquad
\mathbb{R}[\tilde Q] \subseteq \operatorname{span}_\mathbb{R}\{e_0,\tilde Q,ie_0,i\tilde Q\} .
$$

**Proof.** The displayed square writes $\tilde Q^2$ as $ae_0 + b\tilde Q$ with $a = Q_0^2-(\mathbf Q,\mathbf Q)$ and $b = 2Q_0$ complex, so every power of $\tilde Q$ lies in $\operatorname{span}_\mathbb{R}\{e_0,\tilde Q,ie_0,i\tilde Q\}$; that span is four-dimensional in general, and the algebra is commutative because it is generated by one element.

It is therefore at most four-dimensional over $\mathbb{R}$, and generically exactly four — but it can be strictly smaller than the complex plane, which the complex reading does not see. For $\tilde Q = e_1$ the powers are $e_0, e_1, -e_0, -e_1$, so

$$
\mathbb{R}[e_1] = \operatorname{span}_\mathbb{R}\{e_0,e_1\} \cong \mathbb{C} , \qquad \dim_\mathbb{R}\mathbb{R}[e_1] = 2 ,
$$

whereas $\mathbb{C}[e_1] = \mathbb{C}e_0 \oplus \mathbb{C}e_1$ has real dimension four. The classification of the complex plane — $\mathbb{C} \oplus \mathbb{C}$ when $(\mathbf Q,\mathbf Q) \neq 0$, the dual numbers $\mathbb{C}[t]/(t^2)$ when $(\mathbf Q,\mathbf Q) = 0$ — is *Introduction to the General Plain Algebra of Biquaternions*, §*The Subalgebra Generated by One Element*, and is not repeated here.

## Summary

The general plain bilinear product, read on the underlying real space of $\mathbb{B}$, is $\mathbb{R}$-bilinear, associative and unital. It is fixed by the sixty-four products of the eight basis elements $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, and the table is organised in four blocks: the quaternion table, that table multiplied by $i$ in the two mixed blocks, and the table negated.

$$
\boxed{\ \text{With the general plain bilinear product, } \mathbb{B} \text{ is an associative unital non-commutative } \mathbb{R}\text{-algebra of dimension eight.}\ }
$$

What the real scalars expose is the sign pattern of the eight squares and its consequences. The element $ie_0$ is a second square root of $-e_0$ and is central, so the centre $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$ is a field; the elements $ie_1,ie_2,ie_3$ square to $+e_0$, so each plane $\operatorname{span}_\mathbb{R}\{e_0,ie_k\}$ is a copy of the split complex numbers with idempotents $\tfrac12(e_0 \pm ie_k)$; the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is a real subalgebra and a real form, while its imaginary $i\mathbb{H}_{\mathbb{B}}$ is not a subalgebra; and the central element $i$ is a complex structure $J$ on the whole algebra, an algebra automorphism with $J^2 = -\mathrm{id}$.

The real algebra is the restriction of scalars of the complex algebra of *Introduction to the General Plain Algebra of Biquaternions*, related to it by $\dim_\mathbb{R}\mathbb{B} = 2\dim_\mathbb{C}\mathbb{B} = 8$; its extension of scalars is a larger algebra of complex dimension eight, and the complex algebra is the extension of scalars of $\mathbb{H}$ instead. The centre decides the admissible bases: $\mathbb{R}$ and $\mathbb{C}$ qualify and $\mathbb{H}$ and $\mathbb{B}$ do not, since the base ring must map into the complex centre and no unital homomorphism $\mathbb{H} \to \mathbb{C}$ exists. Finally, over $\mathbb{R}$ all four products are bilinear, and the axioms alone select the general plain bilinear product as the multiplication.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | the biquaternion algebra, read here with the real scalars |
| $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$ | the real basis; $e_0$ the unit, $e_k$ the quaternion units, $i$ central |
| $\tilde Q = \sum_\mu Q_\mu e_\mu$ | a biquaternion, $Q_\mu = q_\mu + iq'_\mu$ complex |
| $(\mathbf P,\mathbf Q) = \sum_k P_kQ_k$ | complex bilinear dot product of the vector parts |
| $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$ | the centre, a field, equal to the complex line |
| $\mathbb{H}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2,e_3\}$ | the quaternion subspace, a real subalgebra and a real form |
| $i\mathbb{H}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{ie_0,ie_1,ie_2,ie_3\}$ | its imaginary, not a subalgebra and not a $\mathbb{C}$-subspace |
| $\operatorname{span}_\mathbb{R}\{e_0, ie_k\}$, $k = 1,2,3$ | the split-complex planes, $\cong \mathbb{D} = \mathbb{R}[x]/(x^2-1)$ |
| $J : \tilde Q \mapsto i\tilde Q$ | the central element as a complex structure, $J^2 = -\mathrm{id}$ |
| $R_{\mathbb{C}/\mathbb{R}}\mathbb{B}$ | the complex algebra with the scalars restricted to $\mathbb{R}$ |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*} = \bar{\cdot}\circ\natural$, ${}^{\flat} = -{}^{*}$ | the four conjugations, all $\mathbb{R}$-linear |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion product whose relation to the central imaginary fixes the table.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for algebras over a commutative ring, the structure map into the centre and the tensor product of algebras.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the centre of a tensor product and the impossibility of a unital homomorphism from a simple non-commutative ring into a commutative one.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the restriction and the extension of scalars and the real forms of a complex algebra.
- *Introduction to the General Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-biquaternions.md`), for the same product read with the complex scalars, the structure map and the centre.
