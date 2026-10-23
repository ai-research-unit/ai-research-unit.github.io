# __Introduction to the Biquaternion Algebra__

## Introduction

The **biquaternion algebra** is the complexification of the quaternion algebra,

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H} ,
$$

the four quaternion units $e_t, \vec e_x, \vec e_y, \vec e_z$ kept and the new scalar imaginary $i$ adjoined as a **central** element. It is the object the Biquaternions category is built on, and this article is its opening: it fixes the element, the basis and the multiplication of $\mathbb{B}$, records the four conjugations the complex scalars make available, and reads off the algebra the multiplication defines. It opens the group *The Algebra and Its Vector Spaces*, and it is the article the other two assume.

The construction is short and the consequences long. The multiplication $\tilde Q_1 \tilde Q_2$ is $\mathbb{C}$-bilinear, associative and unital, so the complex vector space $\mathbb{B}$ becomes an associative unital $\mathbb{C}$-algebra; a bilinear map is determined by its values on a basis, so the sixteen products of the basis elements carry the whole multiplication, and the table is the quaternion table with the central imaginary admitted only as a coefficient. Once the algebra is in place its scalar structure, its centre, its generators, its presentation by relations, its conjugations and its matrix model are read off in turn. The algebra is central and simple of complex dimension four, hence isomorphic to the matrix algebra $M_2(\mathbb{C})$, and it is not a division algebra: the element $e_t + i\vec e_x$ is a zero divisor.

## The Construction of the Algebra

### The Tensor Product

**Definition.** The **biquaternion algebra** is the tensor product of $\mathbb{R}$-algebras

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H} ,
$$

where $\mathbb{C}$ is read as a commutative $\mathbb{R}$-algebra.

**Theorem.** $\mathbb{B}$ is an associative algebra with unit $1 \otimes 1$ over $\mathbb{R}$, and a $\mathbb{C}$-algebra under the scalar action $A \tilde Q = (A \otimes 1) \tilde Q$. As a $\mathbb{C}$-vector space it has dimension $4$, on the basis

$$
e_t = 1 \otimes 1, \qquad \vec e_x = 1 \otimes \mathbf{i}, \qquad \vec e_y = 1 \otimes \mathbf{j}, \qquad \vec e_z = 1 \otimes \mathbf{k} ,
$$

where $1, \mathbf{i}, \mathbf{j}, \mathbf{k}$ are the quaternion units.

**Proof.** The tensor product of two associative algebras is associative under $(x \otimes y)(x' \otimes y') = xx' \otimes yy'$, and $1 \otimes 1$ is a two-sided identity. The scalar action is multiplication by the subalgebra $\mathbb{C} \otimes 1 \cong \mathbb{C}$, which is central: $(A \otimes 1)(x \otimes y) = Ax \otimes y = xA \otimes y = (x \otimes y)(A \otimes 1)$, because $\mathbb{C}$ is commutative and $1$ is central in $\mathbb{H}$. The four elements listed are $\mathbb{R}$-linearly independent because $1, \mathbf{i}, \mathbf{j}, \mathbf{k}$ are, and they span over $\mathbb{C}$ because every tensor is a sum of $A \otimes y = (A \otimes 1)(1 \otimes y)$; they are therefore a $\mathbb{C}$-basis.

### The Basis and the Complexification

**Corollary.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the **complexification** of $\mathbb{H}$, of complex dimension $4$ and real dimension $8$. The element $i = i \otimes 1$ is central and satisfies $i^2 = -1$, and it is independent of the four units, which satisfy $\vec e_k^2 = -e_t$. **The scalar imaginary is $i$ and not any $\vec e_k$**, so it can occur only as a coefficient and never as a factor of a product of basis elements; the four units keep their products.

This is the first reading of the name *biquaternion*: one quaternion algebra, read with the complex scalars. The real algebra that carries the same multiplication with the scalars restricted to $\mathbb{R}$ is *The Realification and the Effect of the Change of Scalars*; only the scalar system changes, and the dimension halves.

## The Element and Its Coordinates

### The General Element

A general element of $\mathbb{B}$ is

$$
\tilde Q = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu = Q_t e_t + \vec Q , \qquad Q_\mu = q_\mu + i q'_\mu \in \mathbb{C} ,
$$

the **$\mathbb{C}$ scalar part** $Q_t e_t$ and the **$\mathbb{C}$ vector part** $\vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$. The four complex coefficients are eight real ones, $q_\mu$ the coefficient of $e_\mu$ and $q'_\mu$ the coefficient of $ie_\mu$. The element is also read as a pair of real quaternions, $\tilde Q = h_1 + i h_2$ with $h_1 = \sum_\mu q_\mu e_\mu$ and $h_2 = \sum_\mu q'_\mu e_\mu$, the three coordinate systems being the subject of *The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$*.

### The Scalar–Vector Split and the Two Products of Vector Parts

Writing $\vec Q_1 = \sum_k Q_{1k} \vec e_k$ and $\vec Q_2 = \sum_k Q_{2k} \vec e_k$, the two bilinear products of the vector parts are

$$
(\vec Q_1, \vec Q_2) = \sum_{k=1}^{3} Q_{1k} Q_{2k} , \qquad
\vec Q_1 \times \vec Q_2 = (Q_{1,2} Q_{2z} - Q_{1,3} Q_{2y})\vec e_x + (Q_{1,3} Q_{2x} - Q_{1,1} Q_{2z})\vec e_y + (Q_{1,1} Q_{2y} - Q_{1,2} Q_{2x})\vec e_z .
$$

The first is the complex bilinear **dot product**, a scalar; the second is the complex bilinear **cross product**, a vector part, alternating, $(\vec Q_2, \vec Q_1) = (\vec Q_1, \vec Q_2)$ and $\vec Q_2 \times \vec Q_1 = -\vec Q_1 \times \vec Q_2$. The two are the ingredients of the scalar–vector form of the multiplication, and they are those of *Quaternion Algebra*, read with complex coefficients.

## The Multiplication

### The Rule

**Definition.** The **multiplication** of the algebra is the rule

$$
\cdot \; : \; \mathbb{B} \times \mathbb{B} \longrightarrow \mathbb{B} , \qquad
(\tilde Q_1, \tilde Q_2) \longmapsto \tilde Q_1 \tilde Q_2 = \sum_{\mu\in\{t,x,y,z\}} \sum_{\nu\in\{t,x,y,z\}} Q_{1\mu} Q_{2\nu} \, e_\mu e_\nu ,
$$

the general plain bilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Each of the sixteen products $e_\mu e_\nu$ is a basis element up to sign, so the double sum is a complex combination of $e_t, \dots, \vec e_z$: **the rule is a map into $\mathbb{B}$ and is well defined**. On the four coordinates it reads

$$
\boxed{\;
\tilde Q_1 \tilde Q_2 = (Q_{1,0} Q_{2t} - Q_{1,1} Q_{2x} - Q_{1,2} Q_{2y} - Q_{1,3} Q_{2z})
+ (Q_{1,0} Q_{2x} + Q_{1,1} Q_{2t} + Q_{1,2} Q_{2z} - Q_{1,3} Q_{2y})\, \vec e_x
+ (Q_{1,0} Q_{2y} - Q_{1,1} Q_{2z} + Q_{1,2} Q_{2t} + Q_{1,3} Q_{2x})\, \vec e_y
+ (Q_{1,0} Q_{2z} + Q_{1,1} Q_{2y} - Q_{1,2} Q_{2x} + Q_{1,3} Q_{2t})\, \vec e_z
\;}
$$.

### The Scalar–Vector Form

Collecting the scalar and the vector parts of the two elements, the same product reads

$$
\tilde Q_1 \tilde Q_2 = \bigl(Q_{1,0} Q_{2t} - (\vec Q_1, \vec Q_2)\bigr) + Q_{1,0} \vec Q_2 + Q_{2t} \vec Q_1 + \vec Q_1 \times \vec Q_2 ,
$$

the display being the one of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Its scalar part is $\mathrm{Sc}(\tilde Q_1 \tilde Q_2) = \sum_{\mu\in\{t,x,y,z\}} \varepsilon_\mu Q_{1\mu} Q_{2\mu}$ with $\varepsilon = (1, -1, -1, -1)$.

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

The centre is therefore a proper subspace, and it is the scalar line: §*The Scalars Are the Centre* below proves that and records the statement with the structure map.

### The Algebra Structure

**Theorem.** With the general plain bilinear product as its multiplication, $\mathbb{B}$ is a four-dimensional associative unital non-commutative $\mathbb{C}$-algebra.

**Proof.** By the propositions above the multiplication is a $\mathbb{C}$-bilinear, associative, unital binary operation on the $\mathbb{C}$-vector space $\mathbb{B}$, which is the definition of an algebra over the commutative ring $\mathbb{C}$ in the broad sense of *Algebras: A General Introduction*; the two hypotheses the corpus adds to that sense, associativity and an identity, are the subjects of *Associative Algebras* and *Unital Algebras* and both hold. The dimension is four on the basis $e_t, \vec e_x, \vec e_y, \vec e_z$, and $\vec e_x \vec e_y \neq \vec e_y \vec e_x$.

Every general statement about associative unital algebras is therefore available for $\mathbb{B}$: the two-sided ideals, the centre, the group of units, the modules and the opposite algebra. The rest of this article reads off the ones the multiplication alone decides.

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

**Proposition.** $\mathbb{B}$ is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$. This is *Ideals and Peirce Decomposition of the Biquaternion Algebra*, cited and not repeated. Since the algebra is also central, it is a **central simple** $\mathbb{C}$-algebra, the subject of *Central Simple Algebras and the Brauer Group*.

**Proposition.** $\mathbb{B}$ is **not a division algebra**.

**Proof.** The product

$$
(e_t + i\vec e_x)(e_t - i\vec e_x) = e_t^2 - (i\vec e_x)^2 = e_t - i^2 \vec e_x^2 = e_t - e_t = 0
$$

vanishes with both factors non-zero, so the algebra has zero divisors and is not a division ring. Equivalently the element $e_t + i\vec e_x$ is not a unit, the product of an element with its natural conjugate being scalar and vanishing exactly on the non-units; the group of units and the invertibility criterion are *Norm and Invertibility in the General Quaternionic Algebra*, and the zero divisors themselves are classified in *Zero Divisors of the Biquaternion Algebra*.

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

## The Conjugations

### The Four Conjugations

**Definition.** The **natural** conjugation, the **coefficient** conjugation and the **Hermitian** conjugation of $\tilde Q = Q_t e_t + \vec Q$ are

$$
\tilde Q^{\natural} = Q_t e_t - \vec Q , \qquad
(\overline{\tilde Q})_\mu = \bar Q_\mu , \qquad
\tilde Q^{*} = \bar Q_t e_t - \overline{\vec Q} = \overline{\tilde Q^{\natural}} ,
$$

and the **anti-Hermitian** conjugation is the negative of the Hermitian one,

$$
\tilde Q^{\flat} = -\tilde Q^{*} .
$$

**Proposition.** The natural, the coefficient and the Hermitian conjugations are involutions; the natural and the Hermitian ones are anti-automorphisms, $(\tilde Q_1 \tilde Q_2)^{\natural} = \tilde Q_2^{\natural} \tilde Q_1^{\natural}$ and $(\tilde Q_1 \tilde Q_2)^{*} = \tilde Q_2^{*} \tilde Q_1^{*}$, while the coefficient conjugation is an automorphism, $\overline{(\tilde Q_1 \tilde Q_2)} = \overline{\tilde Q_1}\, \overline{\tilde Q_2}$. The natural conjugation fixes the scalar part and negates the vector part; the star does the same with the coefficients conjugated.

**Proof.** On a basis element $e_\mu$ one has $e_\mu^{\natural} = \varepsilon_\mu e_\mu$ and $\overline{e_\mu} = e_\mu$, the $e_\mu$ being real; the coefficient rules extend $\mathbb{C}$-linearly for the natural conjugation, $\mathbb{C}$-antilinearly for the coefficient and Hermitian ones, and $\mathbb{R}$-linearly for all. On a product of two basis elements $e_\mu e_\nu = \pm e_{\mu\nu}$ the three sign patterns agree with the anti-automorphism rules, and the identities extend by bilinearity. The sign vector of the natural conjugation is $\varepsilon = (1,-1,-1,-1)$.

**Proposition (linearity).** The natural conjugation is $\mathbb{C}$-**linear**, the coefficient and Hermitian conjugations are $\mathbb{C}$-**antilinear**, and all are $\mathbb{R}$-linear.

**Proof.** The natural conjugation touches the quaternion factor and leaves the complex scalars alone, so $\natural(\lambda \tilde Q) = \lambda \tilde Q^{\natural}$ for every $\lambda \in \mathbb{C}$; the coefficient conjugation conjugates a complex coefficient, and the star does so too, so both are antilinear. Conjugating a complex coefficient is $\mathbb{R}$-linear, so all are.

### The Group of the Conjugations

**Proposition.** The identity, the natural, the coefficient and the Hermitian conjugations commute and satisfy

$$
{}^{*} = \bar{\cdot} \circ {}^{\natural} = {}^{\natural} \circ \bar{\cdot} , \qquad
\{\mathrm{id}, \natural, \bar{\cdot}, {}^{*}\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2 ,
$$

the **Klein four-group**, in which the composition of two non-identity elements is the third. The anti-Hermitian conjugation is the Hermitian one times the central sign, $\flat = -{}^{*}$, of square the identity, and it lies **outside** the group: it is a conjugate-linear involution of the space, with the same two fixed spaces as the star and the signs exchanged, but it is not an algebra anti-automorphism. The Cayley table and the composition with the reversal included are *The Group of Involutions*.

**Proof.** The commutation and ${}^{*} = \bar{\cdot} \circ {}^{\natural}$ are the definitions read together, and the three non-identity involutions have pairwise products the third. The map $\flat$ satisfies $\flat^2 = \mathrm{id}$ but not the anti-automorphism rule: $(\tilde Q_1 \tilde Q_2)^{\flat} = -\tilde Q_2^{*}\tilde Q_1^{*}$ while $\tilde Q_1^{\flat} \tilde Q_2^{\flat} = \tilde Q_1^{*}\tilde Q_2^{*}$, so it is not an algebra anti-automorphism and does not join the group.

### The Fixed Spaces and the Remarkable Subspaces

The fixed and anti-fixed spaces of the four conjugations are the six **remarkable subspaces**. The natural conjugation fixes the **centre** $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_t$ and anti-fixes the **vector subspace** $\mathrm{Vect}(\mathbb{B})$, complementary, of real dimensions two and six. The coefficient conjugation fixes the **quaternion subspace** $\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_t + \mathbb{R}\vec e_x + \mathbb{R}\vec e_y + \mathbb{R}\vec e_z$ and anti-fixes the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$, complementary, of dimensions four and four. The Hermitian conjugation fixes the **Hermitian subspace** $\mathbb{M}_+$ and anti-fixes the **anti-Hermitian subspace** $\mathbb{M}_-$; the anti-Hermitian conjugation reproduces exactly these two spaces with the signs exchanged, so it adds no new subspace. The four conjugations therefore produce six remarkable subspaces and not eight. They are defined one to a section in *Introduction to the Remarkable Subspaces* and compared in *Comparison of the Remarkable Subspaces*.

## The Classification and the Matrix Model

### Central Simplicity and Dimension

The algebra is central simple of complex dimension four. Since the base field $\mathbb{C}$ is algebraically closed, the classification of finite-dimensional central simple algebras applies: such an algebra is a full matrix algebra $M_n(\mathbb{C})$ over the field, and the dimension $n^2$ fixes $n$. Here $n = 2$. The theorem is the Artin–Wedderburn theorem, and the general theory is *Central Simple Algebras and the Brauer Group*.

### The Matrix Model

**Theorem.** As a $\mathbb{C}$-algebra, $\mathbb{B}$ is isomorphic to the algebra of $2 \times 2$ complex matrices,

$$
\boxed{\;
\mathbb{B} \;\cong\; M_2(\mathbb{C})
\;}
$$,

under the assignment

$$
e_t \longmapsto \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
\vec e_x \longmapsto \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \quad
\vec e_y \longmapsto \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}, \quad
\vec e_z \longmapsto \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}, \quad
i \longmapsto i\,\mathrm{I}_2 .
$$

**Proof.** The four matrices satisfy the products of the table — $u_x^2 = u_y^2 = u_z^2 = -\mathrm{I}_2$, $u_x u_y = u_z$, $u_y u_z = u_x$ and $u_z u_x = u_y$ — and $i\mathrm{I}_2$ is central with square $-\mathrm{I}_2$; a $\mathbb{C}$-bilinear map is determined by its values on a basis, so the assignment is a well-defined unital $\mathbb{C}$-algebra homomorphism. It is injective because its kernel is a two-sided ideal other than the whole algebra, the domain being simple, and both sides have complex dimension $4$, so it is also surjective.

The model is used in full in *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, in *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* and in *Introduction to Biquaternion Element Representations*; nothing of it beyond the classification and the determinant is used here.

### The Reduced Norm and Invertibility

The product of an element with its natural conjugate is central and scalar:

$$
\tilde Q \tilde Q^{\natural} = \tilde Q^{\natural} \tilde Q = \Bigl(\sum_{\mu\in\{t,x,y,z\}} Q_\mu^2\Bigr) e_t .
$$

The scalar $\sum_\mu Q_\mu^2$ is the **reduced norm** $\langle\tilde Q\rangle_{\natural}$, and it is the determinant in the matrix model,

$$
\boxed{\;
\langle\tilde Q\rangle_{\natural} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu^2 = \det\bigl(\rho(\tilde Q)\bigr) , \qquad
\rho(\tilde Q) = \begin{pmatrix} Q_t + iQ_3 & Q_x + iQ_2 \\ -Q_x + iQ_2 & Q_t - iQ_3 \end{pmatrix}
\;}
$$.

**Theorem.** The reduced norm is multiplicative, $\langle\tilde Q_1 \tilde Q_2\rangle_{\natural} = \langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, and an element $\tilde Q$ is invertible if and only if $\langle\tilde Q\rangle_{\natural} \neq 0$; then $\tilde Q^{-1} = \tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$. A nonzero element is a zero divisor exactly when $\langle\tilde Q\rangle_{\natural} = 0$.

**Proof.** The determinant is multiplicative, and the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ transfers both statements: a matrix is invertible exactly when its determinant is nonzero, and a nonzero matrix of zero determinant is a zero divisor. The inverse formula is the natural-conjugate product divided by its scalar value.

**Corollary.** The reduced norm vanishes on the **zero-divisor cone** $\mathcal N = \{\tilde Q \neq 0 : \langle\tilde Q\rangle_{\natural} = 0\}$, and the invertible elements form the group of units $\mathbb{B}^{\times} = \{\tilde Q : \langle\tilde Q\rangle_{\natural} \neq 0\}$, of structure *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone*.

The reduced norm is the algebraic norm of the **general quaternionic product** $\tilde Q_1^{\natural}\tilde Q_2$ and not of the plain product: the algebraic norm of the plain product is $\langle\tilde Q\rangle = \sum_\mu \varepsilon_\mu Q_\mu^2$, a different function on the same space, and the units of the plain product are read from the norm of the other. The separation, and the names of the two, are *Norm and Invertibility in the Biquaternion Algebra* and *Norm and Invertibility in the General Quaternionic Algebra*.

## The Subalgebra Generated by One Element

The subalgebra $\mathbb{C}[\tilde Q] = \mathbb{C}e_t + \mathbb{C}\tilde Q + \mathbb{C}\tilde Q^2 + \cdots$ generated by one element is commutative and at most two-dimensional:

$$
\tilde Q^2 = \bigl(Q_t^2 - (\vec Q, \vec Q)\bigr) + 2Q_t\vec Q \in \mathbb{C}e_t + \mathbb{C}\tilde Q ,
$$

the developed square being that of *Square Roots of a General Element in the Biquaternion Algebra*. So $\mathbb{C}[\tilde Q] = \mathbb{C}e_t$ for central $\tilde Q$, and $\mathbb{C}[\tilde Q] = \mathbb{C}e_t \oplus \mathbb{C}\tilde Q$ otherwise. In the second case the element $\tilde Q - Q_t e_t$ has square $-(\vec Q, \vec Q)e_t$, and the plane is read off from it: when $(\vec Q, \vec Q) \neq 0$ it is the algebra $\mathbb{C} \oplus \mathbb{C}$ of two copies of the field with coordinatewise multiplication, and when $(\vec Q, \vec Q) = 0$ it is the algebra of dual numbers $\mathbb{C}[t]/(t^2)$.

A unital subalgebra contains the identity $e_t$ and hence every $\mathbb{C}$-multiple of it, so it contains the centre $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_t$, the only scalar line the algebra has; a subalgebra need not be unital, and the line $\mathbb{C}(\vec e_x + i\vec e_y)$ is one, its product vanishing identically because $(\vec e_x + i\vec e_y)^2 = 0$. The real subalgebras of $\mathbb{B}$, among them the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and its imaginary $i\mathbb{H}_{\mathbb{B}}$, are read with the real scalars in *The Realification and the Effect of the Change of Scalars*.

## Summary

The biquaternion algebra is the complexification $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ of the real quaternions: the four-dimensional complex space on $e_t, \vec e_x, \vec e_y, \vec e_z$, with the quaternion multiplication table unchanged and the complex unit $i$ central, so that $i$ is a coefficient and never a factor. The general plain bilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, read as a multiplication, is $\mathbb{C}$-bilinear, associative and unital; it is determined by the sixteen products of the four basis elements.

$$
\boxed{\ \text{With the general plain bilinear product, } \mathbb{B} \text{ is an associative unital non-commutative } \mathbb{C}\text{-algebra of dimension four.}\ }
$$

Its scalars enter through the structure map $\varphi(A) = Ae_t$, whose image is the scalar line and which is central; the algebra is the complexification of $\mathbb{H}$ by the tensor product of algebras; its centre is the scalar line, so it is central and simple, hence central simple; and it is not a division algebra, the product of $e_t + i\vec e_x$ and $e_t - i\vec e_x$ being zero. Two generators suffice, and the relations $\vec e_x^2 = \vec e_y^2 = -e_t$ and $\vec e_x \vec e_y + \vec e_y \vec e_x = 0$ present the algebra as the quaternion algebra over $\mathbb{C}$.

Central simplicity and dimension four force the classification: $\mathbb{B} \cong M_2(\mathbb{C})$. The reduced norm $\langle\tilde Q\rangle_{\natural} = \sum_\mu Q_\mu^2$, the determinant in the model, is multiplicative and decides both invertibility and the zero divisors: $\tilde Q$ is invertible exactly when $\langle\tilde Q\rangle_{\natural} \neq 0$. The four conjugations — the identity, the natural $\natural$, the coefficient conjugation $\bar{\cdot}$, the Hermitian ${}^{*}$, with the anti-Hermitian $\flat = -{}^{*}$ beside them — carry the natural one as the unique $\mathbb{C}$-linear one and give the Klein four-group on the first four, and their fixed spaces are the six remarkable subspaces. The subalgebra generated by one element is the plane spanned by $e_t$ and that element, a product of two copies of $\mathbb{C}$ when $(\vec Q, \vec Q) \neq 0$ and the dual numbers when $(\vec Q, \vec Q) = 0$.

| Property | Value for $\mathbb{B}$ |
|---|---|
| Construction | $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| Complex dimension | $4$ (real dimension $8$) |
| Basis, centre | $e_t, \vec e_x, \vec e_y, \vec e_z$, central $i$; $Z(\mathbb{B}) = \mathbb{C}e_t$ |
| Product | associative, unital, $\mathbb{C}$-bilinear; unit $e_t$ |
| Conjugations | $\{\mathrm{id}, \natural, \bar{\cdot}, {}^{*}\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, with $\flat = -{}^{*}$ outside |
| Classification | $\mathbb{B} \cong M_2(\mathbb{C})$, central simple of degree $2$ |
| Division algebra | no; with $e_t + i\vec e_x$ a zero divisor |
| Reduced norm | $\langle\tilde Q\rangle_{\natural} = \sum_\mu Q_\mu^2$, multiplicative, $\det$ in $M_2(\mathbb{C})$ |
| Invertibility | $\langle\tilde Q\rangle_{\natural} \neq 0$; zero divisor iff $\langle\tilde Q\rangle_{\natural} = 0$, $\tilde Q \neq 0$ |
| General products | four: $\tilde Q_1 \tilde Q_2$, $\tilde Q_1 \tilde Q_2^{*}$, $\tilde Q_1^{\natural} \tilde Q_2$, $\tilde Q_1^{\natural} \tilde Q_2^{*}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | the biquaternion algebra, read here with the complex scalars |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | complex basis; $e_t$ the unit, $\vec e_k$ the quaternion units |
| $i$ | central scalar imaginary, $i^2 = -1$ |
| $\tilde Q = Q_t e_t + \vec Q$ | a biquaternion and its scalar–vector split, $\vec Q = \sum_k Q_k \vec e_k$ |
| $\tilde Q_1, \tilde Q_2$ | two biquaternions, numbered when both occur |
| $Q_\mu = q_\mu + i q'_\mu$ | a complex coefficient, $q_\mu, q'_\mu \in \mathbb{R}$ |
| $(\vec Q_1, \vec Q_2) = \sum_k Q_{1k} Q_{2k}$ | complex bilinear dot product of the vector parts |
| $\vec Q_1 \times \vec Q_2$ | complex bilinear cross product of the vector parts |
| $\varphi : \mathbb{C} \to Z(\mathbb{B})$, $A \mapsto Ae_t$ | the structure map of the complex algebra |
| $i$, $J : \tilde Q \mapsto i\tilde Q$ | the central element of square $-1$, and the complex structure it defines |
| $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_t$ | the centre, equal to the scalar line |
| $\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_t + \mathbb{R}\vec e_x + \mathbb{R}\vec e_y + \mathbb{R}\vec e_z$ | the quaternion subspace, the image of the second factor embedding |
| ${}^{\natural}$, $\bar{\cdot}$ | the natural and the coefficient conjugation |
| ${}^{*} = \bar{\cdot} \circ {}^{\natural} = \natural \circ \bar{\cdot}$ | the Hermitian conjugation |
| ${}^{\flat} = -{}^{*}$ | the anti-Hermitian conjugation, outside the Klein group |
| $\varepsilon = (1,-1,-1,-1)$ | the sign vector of the natural conjugation |
| $\tilde Q \tilde Q^{\natural} = \bigl(\sum_\mu Q_\mu^2\bigr)e_t$ | the product of an element with its natural conjugate, central and scalar |
| $\langle\tilde Q\rangle_{\natural} = \sum_\mu Q_\mu^2$ | the reduced norm; $\det$ of the $2 \times 2$ model |
| $\rho$ | the isomorphism $\mathbb{B} \to M_2(\mathbb{C})$ |
| $\mathcal N$ | the zero-divisor cone, $\{\tilde Q \neq 0 : \langle\tilde Q\rangle_{\natural} = 0\}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion product whose complexification carries the multiplication.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for algebras over a commutative ring, the structure map into the centre and the tensor product of algebras.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the quaternion algebra over a field, its presentations and its behaviour under an extension of scalars.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the presentation of an algebra by generators and relations and for central simplicity.
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the four scalar parts of the four general products, their Gram matrices and their isometry groups.
- [The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space](the-4-algebraic-norms-over-the-biquaternion-c-space.html), for the four diagonals of the four forms and the separation of the algebraic and the topological sense of the norm.
- [The Four General Products of the Biquaternion $\mathbb{C}$ Space](the-four-general-products-of-the-biquaternion-c-space.html), for the product, its coordinate rule and its scalar–vector form.
- [The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$](the-biquaternion-algebra-as-a-vector-space-over-c-and-r.html), for the element, the basis, the three coordinate systems and the conjugation formulas.
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations, their Cayley table and their orbits.
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html), for the reduced norm, the invertibility criterion and the zero-divisor cone.
- [Ideals and Peirce Decomposition of the Biquaternion Algebra](ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html), for the simplicity of $\mathbb{B}$ and the matrix model $M_2(\mathbb{C})$.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the subspaces the conjugations single out.
- [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html), for the matrix model in full.
- [Quaternion Algebra](quaternion-algebra.html), for the real quaternions $\mathbb{H}$, their basis, their multiplication and their conjugation, of which $\mathbb{B}$ is the complexification.
