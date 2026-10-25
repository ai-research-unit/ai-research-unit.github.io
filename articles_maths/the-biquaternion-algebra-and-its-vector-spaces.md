# __The Biquaternion Algebra and Its Vector Spaces__

## Introduction

The **biquaternion algebra** is the complexification of the quaternion algebra,

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H} ,
$$

the four quaternion units $e_t, \vec e_x, \vec e_y, \vec e_z$ kept and the new scalar imaginary $i$ adjoined as a **central** element. This article fixes the algebra and the two vector spaces it carries: the construction by the tensor product, the element and its three coordinate systems, the multiplication and its table, the algebra axioms, the multiplication as a scalar extension, the centre and the structure map, the presentation by generators and relations, and the hyperbolic basis of the plain product. It then reads the same set over the two scalar systems, the complex space of dimension four and the real space of dimension eight, and the complex structure $J$ that carries the difference between them.

The multiplication is stated here at the level of the basis, the table and bilinearity. Its scalar–vector form, the four general products, their relations and their comparison are *The Four General Products and Their Relations over the Biquaternion Algebra*. The group of the four conjugations, their fixed spaces and the remarkable subspaces are *The Group of Involutions*, *Introduction to the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*. The algebra read over the real scalars is *The Realification and the Effect of the Change of Scalars*, and the two ring-based readings are *Modules over the Quaternion Algebra* and *Modules over the Biquaternion Algebra*. No form appears here: the forms and their algebraic norms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

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
e_t = 1 \otimes 1, \qquad \vec e_x = 1 \otimes \mathbf{i}, \qquad \vec e_y = 1 \otimes \mathbf{j}, \qquad \vec e_z = 1 \otimes \mathbf{k} ,
$$

where $1, \mathbf{i}, \mathbf{j}, \mathbf{k}$ are the quaternion units.

**Proof.** The tensor product of two associative algebras is associative under $(x \otimes y)(x' \otimes y') = xx' \otimes yy'$, and $1 \otimes 1$ is a two-sided identity. The scalar action is multiplication by the subalgebra $\mathbb{C} \otimes 1 \cong \mathbb{C}$, which is central: $(A \otimes 1)(x \otimes y) = Ax \otimes y = xA \otimes y = (x \otimes y)(A \otimes 1)$, because $\mathbb{C}$ is commutative and $1$ is central in $\mathbb{H}$. The four elements listed are $\mathbb{R}$-linearly independent because $1, \mathbf{i}, \mathbf{j}, \mathbf{k}$ are, and they span over $\mathbb{C}$ because every tensor is a sum of $A \otimes y = (A \otimes 1)(1 \otimes y)$; they are therefore a $\mathbb{C}$-basis.

### The Basis and the Complexification

**Corollary.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the **complexification** of $\mathbb{H}$, of complex dimension $4$ and real dimension $8$. The element $i = i \otimes 1$ is central and satisfies $i^2 = -1$, and it is independent of the four units, which satisfy $\vec e_k^2 = -e_t$. **The scalar imaginary is $i$ and not any $\vec e_k$**, so it can occur only as a coefficient and never as a factor of a product of basis elements; the four units keep their products.

This is the first reading of the name *biquaternion*: one quaternion algebra, read with the complex scalars. The real algebra that carries the same multiplication with the scalars restricted to $\mathbb{R}$ is *The Realification and the Effect of the Change of Scalars*; only the scalar system changes, and the real dimension doubles.


## The Element and Its Coordinates

### The General Element

A general element of $\mathbb{B}$ is

$$
\tilde Q = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu = Q_t e_t + \vec Q , \qquad Q_\mu = q_\mu + i q'_\mu \in \mathbb{C} ,
$$

the **$\mathbb{C}$ scalar part** $Q_t e_t$ and the **$\mathbb{C}$ vector part** $\vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$. The four complex coefficients are eight real ones, $q_\mu$ the coefficient of $e_\mu$ and $q'_\mu$ the coefficient of $ie_\mu$. The element is also read as a pair of real quaternions, $\tilde Q = h_1 + i h_2$ with $h_1 = \sum_\mu q_\mu e_\mu$ and $h_2 = \sum_\mu q'_\mu e_\mu$, the three coordinate systems being the subject of §*The Coordinate Systems*, below.

### The Coordinate Systems

The same element is written in three coordinate systems, and all three are used below.

**Real coordinates.** Splitting each complex coefficient as $Q_\mu = q_\mu + iq'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$ gives a list of eight real numbers on the real basis:

$$
\tilde{Q} = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z + q'_t(ie_t) + q'_x(i\vec e_x) + q'_y(i\vec e_y) + q'_z(i\vec e_z).
$$

**Complex coordinates.** Collecting the eight real numbers into four complex ones gives the developed form, four complex coordinates $(Q_t, Q_x, Q_y, Q_z)$ on the complex basis $\{e_t, \vec e_x, \vec e_y, \vec e_z\}$.

**Quaternionic coordinates.** Collecting them by the scalar imaginary instead gives

$$
\tilde{Q} = h_1 + ih_2, \qquad h_1 = \sum_{\mu\in\{t,x,y,z\}} q_\mu e_\mu \in \mathbb{H}, \qquad h_2 = \sum_{\mu\in\{t,x,y,z\}} q'_\mu e_\mu \in \mathbb{H},
$$

a real quaternion plus $i$ times another real quaternion. The decomposition is unique, so in this view an element is a **pair of quaternions**.

| coordinates | basis | count | scalars |
|---|---|---|---|
| real | $e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ | $8$ | $\mathbb{R}$ |
| complex | $e_t, \vec e_x, \vec e_y, \vec e_z$ | $4$ | $\mathbb{C}$ |
| quaternionic | $e_t, ie_t$ | $2$ | $\mathbb{H}$ |

The three rows count the same element against three scalar systems, and all three are used below. The first row is the coordinate list of the real reading, developed in §*The Real Scalars*; the eight real coordinates and the four complex ones differ only in how the eight real numbers are gathered.


### The Scalar–Vector Split and the Two Products of Vector Parts

Writing $\vec Q_1 = \sum_k Q_{1k} \vec e_k$ and $\vec Q_2 = \sum_k Q_{2k} \vec e_k$, the two bilinear products of the vector parts are

$$
(\vec Q_1, \vec Q_2) = \sum_k Q_{1k} Q_{2k} , \qquad
\vec Q_1 \times \vec Q_2 = (Q_{1y} Q_{2z} - Q_{1z} Q_{2y})\vec e_x + (Q_{1z} Q_{2x} - Q_{1x} Q_{2z})\vec e_y + (Q_{1x} Q_{2y} - Q_{1y} Q_{2x})\vec e_z .
$$

The first is the complex bilinear **dot product**, a scalar; the second is the complex bilinear **cross product**, a vector part, alternating, $(\vec Q_2, \vec Q_1) = (\vec Q_1, \vec Q_2)$ and $\vec Q_2 \times \vec Q_1 = -\vec Q_1 \times \vec Q_2$. The two are the ingredients of the scalar–vector form of the multiplication, and they are those of *Quaternion Algebra*, read with complex coefficients.


## The Multiplication

### The Rule

**Definition.** The **multiplication** of the algebra is the rule

$$
\cdot \; : \; \mathbb{B} \times \mathbb{B} \longrightarrow \mathbb{B} , \qquad
(\tilde Q_1, \tilde Q_2) \longmapsto \tilde Q_1 \tilde Q_2 = \sum_{\mu\in\{t,x,y,z\}} \sum_{\nu\in\{t,x,y,z\}} Q_{1\mu} Q_{2\nu} \, e_\mu e_\nu ,
$$

the general plain bilinear product of *The Four General Products and Their Relations over the Biquaternion Algebra*. Each of the sixteen products $e_\mu e_\nu$ is a basis element up to sign, so the double sum is a complex combination of $e_t, \dots, \vec e_z$: **the rule is a map into $\mathbb{B}$ and is well defined**. The coordinate rule, with the dot and cross products, is *The Four General Products and Their Relations over the Biquaternion Algebra*, §*The General Plain Bilinear Product*.

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


## Left Alternativity and the Isolation among the Twelve

**The plain product is the only left-alternative one of the twelve structures on the space, and left alternativity is the exact threshold of the associative theory read in this article.**

A product $\circ$ is **left-alternative** when

$$
\tilde Q_1\circ(\tilde Q_1\circ\tilde Q_2)=(\tilde Q_1\circ\tilde Q_1)\circ\tilde Q_2\qquad\text{for all }\tilde Q_1,\tilde Q_2,
$$

equivalently when the multiplication operators satisfy $L^{\circ}_{\tilde Q_1}L^{\circ}_{\tilde Q_1}=L^{\circ}_{\tilde Q_1\circ\tilde Q_1}$ at every element. In a left-alternative structure an idempotent gives a projector, $L_{\tilde\Pi}^{2}=L_{\tilde\Pi}$, and a square-zero element a square-zero operator, $L_{\tilde\Upsilon}^{2}=0$; the projector splits the space, and the square-zero operator produces the flag $\{0\}\subseteq\operatorname{im}L_{\tilde\Upsilon}\subseteq\ker L_{\tilde\Upsilon}\subseteq\mathbb{B}$.

**Theorem (the isolation).** Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the general plain product is the only left-alternative one.

*Proof.* The twelve come from the plain product by twisting the first slot with ${}^{\natural}$, twisting the second with ${}^{*}$, or (anti)symmetrising. Each destroys the law: the first twist demands $\tilde Q_1^{\natural}\tilde Q_1^{\natural}=\tilde Q_1^{\natural}\tilde Q_1$ for every $\tilde Q_1$, false at $\vec e_x$; the second equates a linear with a conjugate-linear operator; the (anti)symmetrisations add cross terms of a left and a right multiplication. The plain product itself is associative, hence left-alternative.

| family | structures | left-alternative |
|---|---|---|
| plain | the algebra | **yes** |
| symmetrised plain | SPA, APA | no |
| first slot ${}^{\natural}$ | GQA | no |
| from GQA | SQA, AQA | no |
| second slot ${}^{*}$ | GPS, GQS | no |
| from the sesquilinear | SPS, APS, SQS, AQS | no |

The claim is about the law and not about single elements. Other structures contain an idempotent here and a square-zero element there, but no other structure carries the law, so the well-behaved elements of the others do not form a theory. The nearest case is the general quaternionic product, whose operator is a plain one with a conjugated index, $L^{\circ}_{\tilde Q_1}=L_{\tilde Q_1^{\natural}}$; it inherits the projector calculus only at the elements whose conjugate is an idempotent.

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

**Proposition.** $\mathbb{B}$ is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$. This is *Ideals and Peirce Decompositions of the Biquaternion Algebra*, cited and not repeated. Since the algebra is also central, it is a **central simple** $\mathbb{C}$-algebra, the subject of *Central Simple Algebras and the Brauer Group*.

**Proposition.** $\mathbb{B}$ is **not a division algebra**.

**Proof.** The product

$$
(e_t + i\vec e_x)(e_t - i\vec e_x) = e_t^2 - (i\vec e_x)^2 = e_t - i^2 \vec e_x^2 = e_t - e_t = 0
$$

vanishes with both factors non-zero, so the algebra has zero divisors and is not a division ring. Equivalently the element $e_t + i\vec e_x$ is not a unit, the product of an element with its natural conjugate being scalar and vanishing exactly on the non-units; the group of units and the invertibility criterion are *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*, and the zero divisors themselves are classified in *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*.


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


## The Conjugations and the Classification

**Definition.** The **natural**, the **coefficient** and the **Hermitian** conjugations of $\tilde Q=Q_te_t+\vec Q$ are

$$
\tilde Q^{\natural}=Q_te_t-\vec Q , \qquad
(\overline{\tilde Q})_\mu=\bar Q_\mu , \qquad
\tilde Q^{*}=\bar Q_te_t-\overline{\vec Q} ,
$$

with $\tilde Q^{\flat}=-\tilde Q^{*}$ the **anti-Hermitian** one. They are involutions, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and $\{\mathrm{id},\natural,\bar{\cdot},{}^{*}\}\cong\mathbb{Z}_2\times\mathbb{Z}_2$; the group, its table, its orbits and the six fixed and anti-fixed subspaces are *The Group of Involutions*.

**Remark (the algebra is a matrix algebra).** Central simplicity and complex dimension four give $\mathbb{B}\cong M_2(\mathbb{C})$, the quaternionic norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ being the determinant of the model. The model is read in *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and the quaternionic norm, invertibility and the zero divisors in *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*.

## The Real Scalars

**Definition.** The **real reading** of $\mathbb{B}$ is the same additive group over the subfield $\mathbb{R}$ of $\mathbb{C}$, obtained by restriction of scalars: the elements are unchanged and the scalar domain is cut from $\mathbb{C}$ down to the subfield $\mathbb{R}$. The general element is written in the eight real coordinates of §*The Coordinate Systems*, on the real basis

$$
e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z.
$$

Every element is a unique real combination of those eight, so the real dimension is the complex dimension doubled, $\dim_\mathbb{R}\mathbb{B} = 2\dim_\mathbb{C}\mathbb{B} = 8$, as recorded in §*The Coordinate Systems*.

**Remark.** No complex number is used as a scalar in this reading: the scalars are real, and the complex reading is the stronger structure rather than a different set. Every polynomial identity over $\mathbb{R}$ extends to $\mathbb{C}$ by scalar extension, and the real reading keeps the additive group, the basis and the product while dropping the complex scalars alone.


## The Complex Structure

The difference between the two readings is carried by one operator. Multiplication by the central imaginary,

$$
J : \tilde{Q} \mapsto i\tilde{Q}, \qquad J^2 = -\mathrm{id},
$$

is real-linear, and it is the **complex structure** of the real space, already met in §*The Scalars, the Centre and the Structure Map*. It carries the whole gap between the readings: for $\lambda = a + bi$, the centrality of the scalars gives

$$
\boxed{\;
\lambda\tilde{Q} = a\tilde{Q} + bJ(\tilde{Q})
\;},
$$

so the complex action is the real action together with $J$, and the real space together with $J$ is the complex space.

**Proposition (linearity is the commutator with $J$).** A real-linear map $T$ of $\mathbb{B}$ is $\mathbb{C}$-linear exactly when it commutes with $J$, and antilinear exactly when it anticommutes with it:

$$
\boxed{\;
T(\lambda\tilde{Q}) = \lambda T(\tilde{Q}) \text{ for all } \lambda \iff TJ = JT, \qquad T(\lambda\tilde{Q}) = \bar{\lambda} T(\tilde{Q}) \text{ for all } \lambda \iff TJ = -JT
\;}.
$$

**Proof.** Let $T$ be real-linear. Then $T(J\tilde{Q}) = T(i\tilde{Q})$ and $J(T\tilde{Q}) = iT(\tilde{Q})$, so the identity $T(i\tilde{Q}) = iT(\tilde{Q})$ is exactly $TJ = JT$; real-linearity then gives $T(\lambda\tilde{Q}) = T(a\tilde{Q} + bJ\tilde{Q}) = aT(\tilde{Q}) + bJT(\tilde{Q}) = \lambda T(\tilde{Q})$ for every $\lambda = a + bi$, and conversely $TJ = JT$ gives $T(i\tilde{Q}) = iT(\tilde{Q})$ and hence the same identity. The antilinear case is the same computation with the sign reversed, $T(i\tilde{Q}) = -iT(\tilde{Q})$, which is $TJ = -JT$.

### Linear and Antilinear Maps

The four conjugations of §*The Conjugations and the Classification* are all real-linear, and the proposition separates them into two classes: ${}^{\natural}$ commutes with $J$ and is $\mathbb{C}$-linear, while $\bar{\cdot}$, ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and $\flat = -{}^{*}$ anticommute with $J$ and are antilinear. The line between the two kinds of map is thus the commutation with one operator.

The real reading sees more linear maps than the complex one:

$$
\boxed{\;
\operatorname{End}_\mathbb{R}(\mathbb{B}) \cong M_8(\mathbb{R}), \qquad \operatorname{End}_\mathbb{C}(\mathbb{B}) \cong M_4(\mathbb{C})
\;},
$$

of real dimensions $64$ and $32$. The $\mathbb{C}$-linear maps are the real-linear ones commuting with $J$, a subspace of half the dimension; a real-linear map that anticommutes with $J$ is antilinear, an ordinary linear map of the real space that is not a complex-linear operator. The conjugations are the natural examples.

### The Real Form

A real subspace of $\mathbb{B}$ of real dimension four need not be closed under $J$; when it meets its image under $J$ only at zero, the two together fill $\mathbb{B}$ and the subspace is a **real form**.

**Proposition.** Let $V$ be a real subspace of $\mathbb{B}$ of real dimension four. Then $V \cap JV = 0$ if and only if $\mathbb{B} = V \oplus JV$, and in that case the complex reading is recovered from $V$ by extension of scalars, $\mathbb{C}\otimes_\mathbb{R}V\cong\mathbb{B}$.

**Proof.** If $\mathbb{B} = V \oplus JV$, then $V \cap JV = 0$ by the directness of the sum. Conversely let $V \cap JV = 0$. If $v + Jw = 0$ with $v, w \in V$, then $v = -Jw$ lies in $V \cap JV$, so $v = 0$ and $Jw = 0$, hence $w = 0$; the map $V \oplus JV \to \mathbb{B}$, $v + Jw \mapsto v + Jw$, is therefore injective, and since both sides have real dimension eight it is an isomorphism, $\mathbb{B} = V \oplus JV$. The map $\mathbb{C}\otimes_\mathbb{R}V \to \mathbb{B}$, $z \otimes v \mapsto zv$, is then $\mathbb{C}$-linear and surjective, because its image contains $V$ and $JV$, hence all of $\mathbb{B}$, and both spaces have complex dimension four, so it is an isomorphism.

**Example.** The elements with real coefficients, spanned by $e_t, \vec e_x, \vec e_y, \vec e_z$, form a real form; its image under $J$ is the subspace of elements with purely imaginary coefficients, the two meet at zero and their sum is $\mathbb{B}$. Real forms are not unique, and the choice of one is data beyond the real reading.

**Remark (the two real spaces, of dimensions eight and four).** The two dimensions must not be confused. The restriction of scalars of the complex reading is the eight-dimensional space above, whose extension of scalars back to $\mathbb{C}$ has complex dimension eight; the extension of scalars of a real form is the four-dimensional complex space $\mathbb{B}$ itself. What returns the complex reading from the eight-dimensional space is the operator $J$, not a scalar extension. The version of this caution for the algebra and its base rings, where $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$, is *The Realification and the Effect of the Change of Scalars*.

**Remark (the remarkable subspaces in the real reading).** The remarkable subspaces are real subspaces, and the complex structure sorts them: the centre and the vector subspace are carried to themselves by $J$ and are the only two that are complex subspaces, of complex dimensions one and three, while the other four are real forms, exchanged in two pairs by $J$. The remarkable subspaces are defined in *Introduction to the Remarkable Subspaces*, and the action of the central imaginary unit upon them is *Comparison of the Remarkable Subspaces*.

### What the View Adds

The real reading sees more subspaces than the complex one, since every complex subspace is a real subspace and the converse fails, and it makes the antilinear maps visible as ordinary linear maps. It drops the complex scalars, so the complex structure becomes an extra operator $J$ whenever the complex action is meant. The product stays $\mathbb{R}$-bilinear, so the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra* are read over $\mathbb{R}$ unchanged; the two ring-based readings, the $\mathbb{H}$-bimodule and the module over $\mathbb{B}$ itself, are *Modules over the Quaternion Algebra* and *Modules over the Biquaternion Algebra*.


## The Hyperbolic Basis of the Plain Product

The plain product $\tilde Q_1\tilde Q_2$ has the scalar part

$$
\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\sum_\mu\varepsilon_\mu Q_{1,\mu}Q_{2,\mu},\qquad \varepsilon=(1,-1,-1,-1),
$$

where $\mathrm{Sc}$ is the coefficient of $e_t$. That scalar part records which pairs the product carries onto the scalar line. The four elements

$$
h_1=e_t+\vec e_x,\qquad h_2=\tfrac12(e_t-\vec e_x),\qquad h_3=\vec e_y+i\vec e_z,\qquad h_4=\tfrac12(i\vec e_z-\vec e_y)
$$

are a basis of the vector space in which this scalar part takes its simplest values.

**Theorem (the hyperbolic basis).** The four elements $h_1,\dots,h_4$ are a $\mathbb{C}$-basis of $\mathbb{B}$, the scalar part of each square vanishes,

$$
\mathrm{Sc}(h_1^2)=\mathrm{Sc}(h_2^2)=\mathrm{Sc}(h_3^2)=\mathrm{Sc}(h_4^2)=0,
$$

and among the sixteen scalar parts $\mathrm{Sc}(h_ih_j)$ the only non-zero ones are

$$
\boxed{\;\mathrm{Sc}(h_1h_2)=\mathrm{Sc}(h_3h_4)=1\;}.
$$

The vector space is therefore the direct sum of the two planes $\operatorname{span}\{e_t,\vec e_x\}$ and $\operatorname{span}\{\vec e_y,\vec e_z\}$, and on them the scalar part of the plain product is hyperbolic: inside each plane it vanishes on the diagonal and equals $1$ on the pair $h_1,h_2$ — respectively $h_3,h_4$ — and between the two planes it vanishes identically. The basis is **hyperbolic**, and the index is $1+1=2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$.

*Proof.* From $\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\sum_\mu\varepsilon_\mu Q_{1,\mu}Q_{2,\mu}$ with $\varepsilon=(1,-1,-1,-1)$: inside the first plane $\varepsilon_t=1$ and $\varepsilon_x=-1$, so $\mathrm{Sc}(h_1^2)=1-1=0$, $\mathrm{Sc}(h_2^2)=\tfrac14(1-1)=0$ and $\mathrm{Sc}(h_1h_2)=\tfrac12(1+1)=1$; inside the second $\varepsilon_y=\varepsilon_z=-1$ and $\mathrm{Sc}(\vec e_y\vec e_z)=\mathrm{Sc}(\vec e_z\vec e_y)=0$, so $\mathrm{Sc}(h_3^2)=-1+1=0$, $\mathrm{Sc}(h_4^2)=\tfrac14(1-1)=0$ and $\mathrm{Sc}(h_3h_4)=\tfrac12(1+1)=1$; and the cross scalar parts vanish because a product of an element supported on $e_t,\vec e_x$ with one supported on $\vec e_y,\vec e_z$ is supported on $\vec e_y,\vec e_z$, hence has no scalar part. The four elements are a basis: $e_t=\tfrac12(h_1+2h_2)$ and $\vec e_x=\tfrac12(h_1-2h_2)$ recover the first plane, and $\vec e_y=\tfrac12(h_3-2h_4)$ and $\vec e_z=\tfrac1{2i}(h_3+2h_4)$ the second. The index over $\mathbb{C}$ is the number of hyperbolic planes, hence $1+1=2$; over $\mathbb{R}$, on the eight real coordinates, the same count is $4$.

**Remark (the maximal planes).** The index $2$ is the largest complex dimension of a subspace on which the scalar part of every product vanishes. Two such planes are $\operatorname{span}_{\mathbb{C}}\{e_t+\vec e_x,\,\vec e_y+i\vec e_z\}$ and $\operatorname{span}_{\mathbb{C}}\{e_t-\vec e_x,\,\vec e_y-i\vec e_z\}$, each of complex dimension $2$, distinct, and meeting in the origin.


## Summary

The biquaternion algebra is the complexification $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ of the real quaternions: the four-dimensional complex space on $e_t, \vec e_x, \vec e_y, \vec e_z$, with the quaternion multiplication table unchanged and the complex unit $i$ central, so that $i$ is a coefficient and never a factor. With the general plain bilinear product as its multiplication, $\mathbb{B}$ is an associative unital non-commutative $\mathbb{C}$-algebra of dimension four; the product is determined by the sixteen products of the four basis elements. In the hyperbolic basis $h_1=e_t+\vec e_x$, $h_2=\tfrac12(e_t-\vec e_x)$, $h_3=\vec e_y+i\vec e_z$, $h_4=\tfrac12(i\vec e_z-\vec e_y)$ the scalar part of the plain product vanishes on every square and pairs only $h_1$ with $h_2$ and $h_3$ with $h_4$, with the value $1$.

$$
\boxed{\ \text{With the general plain bilinear product, } \mathbb{B} \text{ is an associative unital non-commutative } \mathbb{C}\text{-algebra of dimension four.}\ }
$$

Its scalars enter through the structure map $\varphi(A) = Ae_t$, whose image is the scalar line and which is central; the centre is the scalar line, so the algebra is central simple; and it is not a division algebra, the product of $e_t + i\vec e_x$ and $e_t - i\vec e_x$ being zero. Two generators suffice, and the relations $\vec e_x^2 = \vec e_y^2 = -e_t$ and $\vec e_x \vec e_y + \vec e_y \vec e_x = 0$ present the algebra as the quaternion algebra over $\mathbb{C}$.

The algebra is central simple of dimension four, so $\mathbb{B} \cong M_2(\mathbb{C})$, and the quaternionic norm is the determinant of the model; the matrix model and the norm are *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*. The four conjugations — the identity, the natural $\natural$, the coefficient conjugation $\bar{\cdot}$, the Hermitian ${}^{*}$, with the anti-Hermitian $\flat = -{}^{*}$ beside them — have the natural one as the unique $\mathbb{C}$-linear one, form the Klein four-group on the first four, and their fixed and anti-fixed spaces are the six remarkable subspaces. The subalgebra generated by one element is the plane spanned by $e_t$ and that element, a product of two copies of $\mathbb{C}$ when $(\vec Q, \vec Q) \neq 0$ and the dual numbers when $(\vec Q, \vec Q) = 0$.

The same set carries two scalar readings. Over $\mathbb{C}$ it is the space of dimension four on $e_t, \vec e_x, \vec e_y, \vec e_z$. Over $\mathbb{R}$, by restriction of scalars, it is the same additive group with real dimension eight on the basis $e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z$. The same element is written in three coordinate systems: eight real coordinates, four complex coordinates, or two quaternionic coordinates as a pair of real quaternions, $\tilde Q = h_1 + ih_2$.

The gap between the two readings is one operator: $J : \tilde Q \mapsto i\tilde Q$ is real-linear with $J^2 = -\mathrm{id}$, and the complex action is the real action together with $J$. A real-linear map is $\mathbb{C}$-linear exactly when it commutes with $J$ and antilinear exactly when it anticommutes; ${}^{\natural}$ commutes and the other three conjugations anticommute. Hence $\operatorname{End}_\mathbb{R}(\mathbb{B}) \cong M_8(\mathbb{R})$ against $\operatorname{End}_\mathbb{C}(\mathbb{B}) \cong M_4(\mathbb{C})$, of real dimensions $64$ and $32$. A real form is a real subspace $V$ of real dimension four meeting $JV$ only at zero; then $\mathbb{B} = V \oplus JV$ and $\mathbb{C}\otimes_\mathbb{R}V \cong \mathbb{B}$, so the complex reading is recovered from $V$ by extension of scalars. The centre and the vector subspace are the only remarkable subspaces closed under $J$; the other four are real forms exchanged in pairs.

| Property | Value for $\mathbb{B}$ |
|---|---|
| Construction | $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| Complex dimension | $4$ (real dimension $8$) |
| Basis, centre | $e_t, \vec e_x, \vec e_y, \vec e_z$, central $i$; $Z(\mathbb{B}) = \mathbb{C}e_t$ |
| Product | associative, unital, $\mathbb{C}$-bilinear; unit $e_t$ |
| Conjugations | $\{\mathrm{id}, \natural, \bar{\cdot}, {}^{*}\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, with $\flat = -{}^{*}$ outside |
| Division algebra | no; $e_t + i\vec e_x$ is a zero divisor |

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
| $\operatorname{End}_\mathbb{R}(\mathbb{B})$, $\operatorname{End}_\mathbb{C}(\mathbb{B})$ | the real-linear and the $\mathbb{C}$-linear self-maps, $\cong M_8(\mathbb{R})$ and $M_4(\mathbb{C})$ |
| real form of $\mathbb{B}$ | a real subspace $V$ of real dimension $4$ with $\mathbb{B} = V \oplus JV$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion product whose complexification carries the multiplication.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for algebras over a commutative ring, the structure map into the centre and the tensor product of algebras.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the quaternion algebra over a field, its presentations and its behaviour under an extension of scalars.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the presentation of an algebra by generators and relations and for central simplicity.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the scalar–vector form of the multiplication, the four general products and their comparison.
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations, their Cayley table and their orbits.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the subspaces the conjugations single out.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the quaternionic norm, the invertibility criterion and the zero-divisor cone.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the simplicity of $\mathbb{B}$ and the matrix model $M_2(\mathbb{C})$.
- [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html), for the matrix model in full.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
