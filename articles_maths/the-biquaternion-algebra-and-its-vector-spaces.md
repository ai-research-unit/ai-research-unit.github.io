# __The Biquaternion Algebra__

## Introduction

The **biquaternion algebra** is the complexification of the quaternion algebra,

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H} ,
$$

the four quaternion units $e_t, \vec e_x, \vec e_y, \vec e_z$ kept and the new scalar imaginary $i$ adjoined as a **central** element. This article fixes the algebra: the construction by the tensor product, the multiplication and its table, the algebra axioms, the multiplication as a scalar extension, the centre and the structure map, the presentation by generators and relations, and the absence of division. The element, its three coordinate systems, the two scalar readings and the complex structure $J$ are *The Element, the Coordinates and the Conjugations*; the matrix model is *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*; the hyperbolic basis of the plain scalar part is filed with the plain product, after the forms.

The multiplication is stated here at the level of the basis, the table and bilinearity. Its scalar–vector form, the four general products, their relations and their comparison are *The Four General Products and Their Relations over the Biquaternion Algebra*. The four conjugations, their group and their fixed spaces are *The Element, the Coordinates and the Conjugations*, *The Group of Involutions* and *The Six Subspaces*; the lattice they form is *The Lattice of the Subspaces*. The algebra read over the real scalars is in *The Element, the Coordinates and the Conjugations*. No form appears here: the forms and their algebraic norms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

This article opens the group *The Algebra and Its Vector Spaces* and the Biquaternions category. It is self-contained up to the quaternion algebra $\mathbb{H}$, whose basis, multiplication and conjugation are assumed.

## The Construction of the Algebra

### The Tensor Product

**Definition.** The **biquaternion algebra** is the tensor product of $\mathbb{R}$-algebras

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H} ,
$$

where $\mathbb{C}$ is read as a commutative $\mathbb{R}$-algebra.

**Theorem.** $\mathbb{B}$ is an associative algebra with unit $1 \otimes 1$ over $\mathbb{R}$, and a $\mathbb{C}$-algebra under the scalar action $A \tilde Q = (A \otimes 1) \tilde Q$. As a $\mathbb{C}$-vector space it has dimension $4$, on the basis

$$
e_t = 1 \otimes 1, \qquad \vec e_x = 1 \otimes \vec e_x, \qquad \vec e_y = 1 \otimes \vec e_y, \qquad \vec e_z = 1 \otimes \vec e_z ,
$$

where each vector unit on the right is the quaternion unit of $\mathbb{H}$ and each on the left is its image in $\mathbb{B}$; the two carry the same letter by the identification that names the biquaternion unit after the quaternion unit it extends.

**Proof.** The tensor product of two associative algebras is associative under $(x \otimes y)(x' \otimes y') = xx' \otimes yy'$, and $1 \otimes 1$ is a two-sided identity. The scalar action is multiplication by the subalgebra $\mathbb{C} \otimes 1 \cong \mathbb{C}$, which is central: $(A \otimes 1)(x \otimes y) = Ax \otimes y = xA \otimes y = (x \otimes y)(A \otimes 1)$, because $\mathbb{C}$ is commutative and $1$ is central in $\mathbb{H}$. The four elements listed are $\mathbb{R}$-linearly independent because the four quaternion units are, and they span over $\mathbb{C}$ because every tensor is a sum of $A \otimes y = (A \otimes 1)(1 \otimes y)$; they are therefore a $\mathbb{C}$-basis.

### The Basis and the Complexification

**Corollary.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the **complexification** of $\mathbb{H}$, of complex dimension $4$ and real dimension $8$. The element $i = i \otimes 1$ is central and satisfies $i^2 = -1$, and it is independent of the four units, which satisfy $\vec e_k^2 = -e_t$. **The scalar imaginary is $i$ and not any $\vec e_k$**, so it can occur only as a coefficient and never as a factor of a product of basis elements; the four units keep their products.

This is the first reading of the name *biquaternion*: one quaternion algebra, read with the complex scalars. The real algebra that carries the same multiplication with the scalars restricted to $\mathbb{R}$ is *The Realification and the Effect of the Change of Scalars*; only the scalar system changes, and the real dimension doubles.

## The Multiplication

### The Rule

**Definition.** The **multiplication** of the algebra is the rule

$$
\cdot \; : \; \mathbb{B} \times \mathbb{B} \longrightarrow \mathbb{B} , \qquad
(\tilde Q_1, \tilde Q_2) \longmapsto \tilde Q_1 \tilde Q_2 = \sum_{\mu\in\{t,x,y,z\}} \sum_{\nu\in\{t,x,y,z\}} Q_{1\mu} Q_{2\nu} \, e_\mu e_\nu ,
$$

the general plain bilinear product of *The Four General Products and Their Relations over the Biquaternion Algebra*. Each of the sixteen products $e_\mu e_\nu$ is a basis element up to sign, so the double sum is a complex combination of $e_t, \dots, \vec e_z$: **the rule is a map into $\mathbb{B}$ and is well defined**. The coordinate rule, with the dot and cross products, is *The Four General Products and Their Relations over the Biquaternion Algebra*, *The Four General Products and Their Relations over the Biquaternion Algebra*.

### The Multiplication Table

A product linear in each argument is fixed by its values on the basis pairs, so the multiplication is fixed by the following sixteen products.

**Proposition.** The products of the basis elements are

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

**Proof.** The entries are the products of the quaternion units, $\vec e_x \vec e_y = \vec e_z$, $\vec e_y \vec e_z = \vec e_x$, $\vec e_z \vec e_x = \vec e_y$ and $\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t$, of *Quaternion Algebra*, with the central imaginary admitted as a coefficient and never as a factor.

The table is **the quaternion table**. Every entry is a basis element up to sign, the diagonal entry $e_t e_t$ is the unit while the three others are $-e_t$, and the three imaginary units anticommute pairwise, $\vec e_\mu \vec e_\nu = -\vec e_\nu \vec e_\mu$ for $\mu \neq \nu$ in $\{x,y,z\}$; the unit commutes with everything, so the antisymmetry is confined to the imaginary block. The scalar imaginary $i$ occurs nowhere among the entries, being central: this is why the multiplication table of a complex algebra is a table of real quaternions.

### Bilinearity and the Determination by the Table

**Proposition.** The multiplication is $\mathbb{C}$-**bilinear**:

$$
(\tilde Q_1 + \tilde Q_2)\tilde Q_3 = \tilde Q_1 \tilde Q_3 + \tilde Q_2 \tilde Q_3 , \qquad
\tilde Q_3(\tilde Q_1 + \tilde Q_2) = \tilde Q_3 \tilde Q_1 + \tilde Q_3 \tilde Q_2 , \qquad
(A \tilde Q_1)\tilde Q_2 = A(\tilde Q_1 \tilde Q_2) = \tilde Q_1(A \tilde Q_2) , \qquad A \in \mathbb{C} .
$$

**Proof.** Every coordinate on the right of the developed form is a sum of terms $Q_{1\mu} Q_{2\nu}$ with a fixed coefficient, hence is additive and homogeneous in the four coordinates of $\tilde Q_1$ alone and in the four coordinates of $\tilde Q_2$ alone; the three identities are that statement read coordinate by coordinate.

**Proposition (determination by the table).** The multiplication is the unique $\mathbb{C}$-bilinear map $\mathbb{B} \times \mathbb{B} \to \mathbb{B}$ sending the pair $(e_\mu, e_\nu)$ to the product $e_\mu e_\nu$ of the table.

**Proof.** A $\mathbb{C}$-bilinear map is determined by its values on the pairs of basis elements, and the double sum of the definition is such a map taking those values.

**Corollary.** Two multiplications on the same space that agree on the sixteen pairs of basis elements agree on every pair.

## The Algebra Axioms

### Associativity

**Proposition.** The multiplication is **associative**: $(\tilde Q_1 \tilde Q_2)\tilde Q_3 = \tilde Q_1(\tilde Q_2 \tilde Q_3)$ for all $\tilde Q_1, \tilde Q_2, \tilde Q_3 \in \mathbb{B}$.

**Proof.** Both sides are $\mathbb{C}$-trilinear in $(\tilde Q_1, \tilde Q_2, \tilde Q_3)$, so it suffices to check the $64$ triples of basis elements. Each product of two basis elements is a basis element up to sign by the table, and the coefficient sign is a central scalar; each of the $64$ triple products is therefore a triple product in the quaternion algebra, and those associate. The two sides agree on the basis triples, hence everywhere.

### The Unit

**Proposition.** The element $e_t$ is a **two-sided identity**: $e_t \tilde Q = \tilde Q e_t = \tilde Q$ for every $\tilde Q$.

**Proof.** By bilinearity it suffices to check $\tilde Q = \vec e_k$, and the first row and the first column of the table give it.

The identity is unique: a two-sided identity $u$ satisfies $u = u u' = u'$ for any other two-sided identity $u'$. It is written $e_t$ and is the unit of the algebra.

### Non-Commutativity

**Proposition.** The multiplication is **not commutative**.

**Proof.** $\vec e_x \vec e_y = \vec e_z$ while $\vec e_y \vec e_x = -\vec e_z$, and the two differ because $\vec e_z$ is a basis element and $\vec e_z \neq -\vec e_z$.

The centre is therefore a proper subspace, and it is the scalar line: §*The Scalars, the Centre and the Structure Map* below proves that and records the statement with the structure map.

### The Algebra Structure

**Theorem.** With the general plain bilinear product as its multiplication, $\mathbb{B}$ is a four-dimensional associative unital non-commutative $\mathbb{C}$-algebra.

**Proof.** By the propositions above the multiplication is a $\mathbb{C}$-bilinear, associative, unital binary operation on the $\mathbb{C}$-vector space $\mathbb{B}$, which is the definition of an algebra over the commutative ring $\mathbb{C}$ in the broad sense of *Algebras: A General Introduction*; the two hypotheses the corpus adds to that sense, associativity and an identity, are the subjects of *Associative Algebras* and *Unital Algebras* and both hold. The dimension is four on the basis $e_t, \vec e_x, \vec e_y, \vec e_z$, and $\vec e_x \vec e_y \neq \vec e_y \vec e_x$.

Every general statement about associative unital algebras is therefore available for $\mathbb{B}$: the two-sided ideals, the centre, the group of units and the opposite algebra. The rest of this article reads off the ones the multiplication alone decides.

## The Multiplication as a Scalar Extension

### The Tensor Product of the Two Multiplications

The underlying space of $\mathbb{B}$ is the tensor product $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ of the two $\mathbb{R}$-algebras $\mathbb{C}$ and $\mathbb{H}$, whose algebra product is $(A \otimes h)(A' \otimes h') = (AA') \otimes (hh')$ of *Tensor Products of Algebras*. Under the identification $1 \otimes e_\mu \mapsto e_\mu$, $i \otimes e_\mu \mapsto ie_\mu$ of the two eight-dimensional real spaces — the one forced by $(i \otimes e_t)(1 \otimes e_\mu) = i \otimes e_\mu$ — this product is the general plain bilinear product: the two agree on the eight real basis elements $e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z$, and two $\mathbb{R}$-bilinear products agreeing on a real basis agree everywhere. **The multiplication is the tensor product of the complex multiplication and the quaternion multiplication.** Associativity is inherited from the two associative factors, and the unit is $1 \otimes 1 = e_t$.

### The Two Factor Embeddings

The two factor embeddings

$$
\mathbb{C} \longrightarrow \mathbb{B}, \quad A \longmapsto A \otimes 1 = Ae_t , \qquad
\mathbb{H} \longrightarrow \mathbb{B}, \quad h \longmapsto 1 \otimes h ,
$$

are unital algebra homomorphisms over $\mathbb{R}$ with commuting images (*Tensor Products of Algebras*); the commuting of the images is the statement that the scalars are central, used in the next section. The second image is the real quaternion subspace $\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_t + \mathbb{R}\vec e_x + \mathbb{R}\vec e_y + \mathbb{R}\vec e_z$, and on it the multiplication is the quaternion product of *Quaternion Algebra*.

## The Scalars, the Centre and the Structure Map

### The Structure Map

The scalars of an algebra enter through the canonical unital ring homomorphism from the base ring into the centre, the map $\eta(r) = r 1_A$ of *Unital Algebras*, whose image is the scalar line. Here it is

$$
\varphi : \mathbb{C} \longrightarrow Z(\mathbb{B}) , \qquad \varphi(A) = Ae_t ,
$$

with image the scalar line $\mathbb{C}e_t = \mathbb{C}_{\mathbb{B}}$, and the scalar action is $A \tilde Q = \varphi(A)\tilde Q$, applied to the four complex coefficients. The image is central, so the action is compatible with the product,

$$
A(\tilde Q_1 \tilde Q_2) = (A \tilde Q_1)\tilde Q_2 = \tilde Q_1(A \tilde Q_2) , \qquad A \in \mathbb{C} ,
$$

which is the bilinearity proposition read as the axiom of an algebra: the first equality is associativity with the scalar written as $Ae_t$, and the second is where centrality enters, because $\tilde Q_1(A \tilde Q_2) = (\tilde Q_1\, Ae_t)\tilde Q_2$ agrees with $(Ae_t\, \tilde Q_1)\tilde Q_2$ exactly when $Ae_t$ commutes with $\tilde Q_1$.

### The Gate: a Central Element of Square $-1$

**The gate, applied here.** A $\mathbb{C}$-algebra structure on a real algebra, whose structure map lands in the centre, is the same thing as a **central element $j$ with $j^2 = -1$**, the scalar action being $(a + ib)\tilde Q = a\tilde Q + bj\tilde Q$. For $\mathbb{B}$ that element is the central imaginary $i$ itself — $j = i$ — and the complex structure it induces on the underlying real space is the real-linear map

$$
J : \mathbb{B} \longrightarrow \mathbb{B} , \qquad J(\tilde Q) = i\tilde Q , \qquad J^2 = -\mathrm{id} ,
$$

the compatibility demanded at the product being exactly the formula above. Centrality is not decoration: the product of $\mathbb{B}$ is $\mathbb{R}$-bilinear in any case, and it is $\mathbb{C}$-bilinear precisely because $i$ is central.

### The Scalars Are the Centre

**Proposition.** The centre of $\mathbb{B}$ is the complex line spanned by $e_t$:

$$
Z(\mathbb{B}) = \mathbb{C} \otimes_{\mathbb{R}} Z(\mathbb{H}) = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{R} = \mathbb{C} = \mathbb{C}_{\mathbb{B}} .
$$

**Proof.** The centre of a tensor product of algebras over a field is the tensor product of their centres, and $Z(\mathbb{C}) = \mathbb{C}$ while $Z(\mathbb{H}) = \mathbb{R}$. In coordinates, $[\tilde Q, \vec e_x] = 2Q_z \vec e_y - 2Q_y \vec e_z$ vanishes exactly when $Q_y = Q_z = 0$, and $[\tilde Q, \vec e_y]$ vanishes exactly when $Q_x = Q_z = 0$, so centrality forces $Q_x = Q_y = Q_z = 0$; conversely every $Q_t e_t$ is central because $i$ commutes with the units.

The scalars cannot be enlarged further, because there is no room in the centre for more; which base rings are admissible, and why the quaternion factor cannot serve, is *The Realification and the Effect of the Change of Scalars*.

**Corollary.** The algebra is **central** over $\mathbb{C}$: the image of the structure map is the whole centre, so no scalar is lost and no non-scalar is admitted as a scalar. The centre is a subalgebra isomorphic to the field $\mathbb{C}$, and it is proper, the algebra being non-commutative.

**Corollary.** The scalars are determined by the multiplication: the centre is an invariant of the algebra, so the field $\mathbb{C}$ acting on $\mathbb{B}$ is recoverable from the product alone.

### Central Simplicity and the Absence of Division

**Proposition.** $\mathbb{B}$ is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$.

*Proof.* Let $I$ be a nonzero two-sided ideal and let $0\neq x\in I$. If $x$ is central, then $x=Q_t e_t$ with $Q_t\neq0$, and $e_t=Q_t^{-1}x\in I$. If $x$ is not central, one of the commutators $[x,\vec e_k]=x\vec e_k-\vec e_k x$ is nonzero, since the centre is the scalar line. The commutator is a nonzero pure element $y=b\vec e_x+c\vec e_y+d\vec e_z$ of $I$. Choose $k$ with $y_k\neq0$; the distinct quaternion units anticommute and $\vec e_k^2=-e_t$, so $y\vec e_k+\vec e_k y=-2y_k e_t$ by the table. Both terms lie in $I$, hence $e_t\in I$ and $I=\mathbb{B}$.

Since the algebra is also central, it is a **central simple** $\mathbb{C}$-algebra, the subject of *Central Simple Algebras and the Brauer Group*.

**Proposition.** $\mathbb{B}$ is **not a division algebra**.

**Proof.** The product

$$
(e_t + i\vec e_x)(e_t - i\vec e_x) = e_t^2 - (i\vec e_x)^2 = e_t - i^2 \vec e_x^2 = e_t - e_t = 0
$$

vanishes with both factors non-zero, so the algebra has zero divisors and is not a division ring.

## Generators and the Presentation

### The Generators

**Proposition.** $\mathbb{B}$ is generated, as a $\mathbb{C}$-algebra with unit, by $\vec e_x$ and $\vec e_y$; more generally by any two of $\vec e_x, \vec e_y, \vec e_z$.

**Proof.** The relations $\vec e_x^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$ of the table give $e_t$ and $\vec e_z$ from $\vec e_x$ and $\vec e_y$, and the four basis elements span the algebra. For the other pairs, $\vec e_x \vec e_z = -\vec e_y$ and $\vec e_y \vec e_z = \vec e_x$ give the third unit from the two chosen ones, and $\vec e_k^2 = -e_t$ gives the identity.

### The Relations and the Presentation

**Proposition.** The generators $\vec e_x, \vec e_y$ satisfy

$$
\vec e_x^2 = \vec e_y^2 = -e_t , \qquad \vec e_x \vec e_y + \vec e_y \vec e_x = 0 ,
$$

and these relations present the algebra: writing $\mathbb{C}\langle E_1, E_2\rangle$ for the free associative $\mathbb{C}$-algebra on two generators,

$$
\mathbb{B} \cong \mathbb{C}\langle E_1, E_2\rangle \big/ \bigl(E_1^2 + 1 , \; E_2^2 + 1 , \; E_1 E_2 + E_2 E_1\bigr) .
$$

**Proof.** The relations hold on the basis by the table, so $E_1 \mapsto \vec e_x$, $E_2 \mapsto \vec e_y$ descends to a homomorphism from the quotient onto $\mathbb{B}$, which is surjective because the two generate. In the quotient every word in $E_1, E_2$ is a $\mathbb{C}$-combination of $1, E_1, E_2, E_1 E_2$: the relation $E_1 E_2 + E_2 E_1 = 0$, read as $E_2 E_1 = -E_1 E_2$, moves every occurrence of $E_1$ to the left of every occurrence of $E_2$, and then $E_1^2 = E_2^2 = -1$ reduces the exponents of the two letters modulo two. The reduced words are $\pm 1, \pm E_1, \pm E_2, \pm E_1 E_2$, so the quotient is at most four-dimensional, and a surjection from a space of dimension at most four onto the four-dimensional algebra $\mathbb{B}$ is an isomorphism (*Quotients of the Tensor Algebra*).

The algebra presented is the **quaternion algebra over $\mathbb{C}$**: the quaternion relations of *Quaternion Algebra*, with the base field enlarged from $\mathbb{R}$ to $\mathbb{C}$. This is the second reading of the name biquaternion, and it agrees with the first, the complexification of §*The Construction of the Algebra*.

The relation that ties $\vec e_z$ to the two generators is not redundant. Were the three imaginary units taken as generators with the pairwise relations $E_j E_k + E_k E_j = 0$ for $j \neq k$ and $E_k^2 = -1$ alone, the element $E_1 E_2$ would remain independent of $1, E_1, E_2, E_3$: the three square relations and the three anticommutations do not force $E_1 E_2$ into the span of the generators, and the algebra presented is eight-dimensional rather than four.

## Summary

The biquaternion algebra is the complexification $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ of the real quaternions: the four-dimensional complex space on $e_t, \vec e_x, \vec e_y, \vec e_z$, with the quaternion multiplication table unchanged and the complex unit $i$ central, so that $i$ is a coefficient and never a factor. With the general plain bilinear product as its multiplication, $\mathbb{B}$ is an associative unital non-commutative $\mathbb{C}$-algebra of dimension four; the product is determined by the sixteen products of the four basis elements.

$$
\boxed{\ \text{With the general plain bilinear product, } \mathbb{B} \text{ is an associative unital non-commutative } \mathbb{C}\text{-algebra of dimension four.}\ }
$$

Its scalars enter through the structure map $\varphi(A) = Ae_t$, whose image is the scalar line and which is central; the centre is the scalar line, so the algebra is central simple. It is not a division algebra, and the witness uses the product alone:

$$
(e_t + i\vec e_x)(e_t - i\vec e_x)=0,\qquad e_t\pm i\vec e_x\neq0 .
$$

Two generators suffice, and the relations $\vec e_x^2 = \vec e_y^2 = -e_t$ and $\vec e_x \vec e_y + \vec e_y \vec e_x = 0$ present the algebra as the quaternion algebra over $\mathbb{C}$.

The algebra is central simple of dimension four. The element, its three coordinate systems and the four conjugations are *The Element, the Coordinates and the Conjugations*; the group they form is *The Group of Involutions*.

| Property | Value for $\mathbb{B}$ |
|---|---|
| Construction | $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| Complex dimension | $4$ (real dimension $8$) |
| Basis, centre | $e_t, \vec e_x, \vec e_y, \vec e_z$, central $i$; $Z(\mathbb{B}) = \mathbb{C}e_t$ |
| Product | associative, unital, $\mathbb{C}$-bilinear; unit $e_t$ |
| Division algebra | no; $(e_t + i\vec e_x)(e_t - i\vec e_x)=0$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra |
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | the biquaternion algebra |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | complex basis; $e_t$ the unit, $\vec e_k$ the quaternion units, $\vec e_k^2 = -e_t$ |
| $i$ | central scalar imaginary, $i^2 = -1$ |
| $J : \tilde Q \mapsto i\tilde Q$ | the real-linear complex structure, $J^2 = -\mathrm{id}$ |
| $\lambda\tilde Q = a\tilde Q + bJ(\tilde Q)$ | the complex action read over $\mathbb{R}$, for $\lambda = a + bi$ |
| $\tilde Q = Q_t e_t + \vec Q = \sum_\mu Q_\mu e_\mu$ | a biquaternion and its scalar–vector split, $\vec Q = \sum_k Q_k \vec e_k$ |
| $Q_\mu = q_\mu + i q'_\mu$ | a complex coefficient, $q_\mu, q'_\mu \in \mathbb{R}$ |
| $\tilde Q = h_1 + ih_2$ | the quaternionic coordinates, $h_1, h_2 \in \mathbb{H}$ |
| $(\vec Q_1, \vec Q_2) = \sum_k Q_{1k} Q_{2k}$ | complex bilinear dot product of the vector parts |
| $\vec Q_1 \times \vec Q_2$ | complex bilinear cross product of the vector parts |
| $\varphi : \mathbb{C} \to Z(\mathbb{B})$, $A \mapsto Ae_t$ | the structure map of the complex algebra |
| $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_t$ | the centre, equal to the scalar line |
| $\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_t + \mathbb{R}\vec e_x + \mathbb{R}\vec e_y + \mathbb{R}\vec e_z$ | the quaternion subspace |
| ${}^{\natural}$, $\bar{\cdot}$ | the natural and the coefficient conjugation |
| ${}^{*} = \bar{\cdot} \circ {}^{\natural} = \natural \circ \bar{\cdot}$ | the Hermitian conjugation |
| ${}^{\flat} = -{}^{*}$ | the anti-Hermitian conjugation, outside the Klein group |
| $\varepsilon = (1,-1,-1,-1)$ | the sign vector of the natural conjugation |
| $h_1, h_2, h_3, h_4$ | the hyperbolic basis of the plain product, $e_t+\vec e_x$, $\tfrac12(e_t-\vec e_x)$, $\vec e_y+i\vec e_z$, $\tfrac12(i\vec e_z-\vec e_y)$ |
| real form of $\mathbb{B}$ | a real subspace $V$ of real dimension $4$ with $\mathbb{B} = V \oplus JV$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion product whose complexification carries the multiplication.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for algebras over a commutative ring, the structure map into the centre and the tensor product of algebras.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the quaternion algebra over a field, its presentations and its behaviour under an extension of scalars.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the presentation of an algebra by generators and relations and for central simplicity.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the scalar–vector form of the multiplication, the four general products and their comparison.
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations, their Cayley table and their orbits.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the subspaces the conjugations single out.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the quaternionic norm, the invertibility criterion and the zero-divisor cone.
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the idempotents, the Peirce decomposition and the matrix model $M_2(\mathbb{C})$.
- [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](m2c-representation-the-matrix-product-and-the-algebra-structure.html), for the matrix model in full.
- [Modules over the Biquaternion Algebra](modules-over-the-biquaternion-algebra.html), for the simple modules, the classification, Schur's lemma, the intertwiners and the Morita equivalence.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
