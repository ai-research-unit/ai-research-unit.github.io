# __Biquaternion Algebra__

## Introduction

This article is the algebraic foundation of the physics series. It defines the biquaternion algebra, its four conjugations, its six distinguished real subspaces, its three decompositions and its three quadratic forms, and it gives each structure its physical reading as it is introduced.

The algebra is the same algebra as the one set down in *Biquaternion Algebra* in the mathematics corpus, and the conventions are the same. What is added here is the interpretation. The article is written for a reader who wants the algebraic skeleton and the physical reading on the same page, rather than the skeleton first and the reading several articles later.

The physical content enters through one identification and one only: the eight real parameters of an element are read as coordinates of spacetime. That dictionary is fixed in *Conventions in the Biquaternion Universe* and is repeated in the section **Developed Form** below. Everything else that is called physical in this article is a restatement of that dictionary in algebraic language.

The algebra is stated and its properties are proved. The physical reading is an **identification**, not a derivation, and it is flagged as such wherever it occurs: the series does not claim that the algebra forces the interpretation.

The six distinguished subspaces each have their own article in the **Focus on Subspaces** group of the series, where the basis and dimension, the algebra and module structure, the biquaternion norm, the matrix image and the intersections are worked out in full. The present article uses them throughout and points to the article concerned at each step.

## Biquaternions

### Definition

The **biquaternion algebra** is the complexification of the quaternion algebra:

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}.
$$

### Two Views: Over $\mathbb{C}$ and Over $\mathbb{R}$

The algebra can be viewed in two equivalent ways, depending on which scalars are allowed.

**As a $\mathbb{C}$-algebra.** The tensor product $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is naturally a module over $\mathbb{C}$, with the complex scalars acting on the first factor. In this view, $\mathbb{B}$ is a **four-dimensional algebra over $\mathbb{C}$**: its complex basis is $\{e_0, e_1, e_2, e_3\}$, multiplication is $\mathbb{C}$-bilinear, and the algebra is associative and unital with unit $e_0$. Its center is $\mathbb{C}$, and it is isomorphic to the algebra $M_2(\mathbb{C})$ of $2\times2$ complex matrices.

**As an $\mathbb{R}$-algebra.** Forgetting the $\mathbb{C}$-module structure, the same set $\mathbb{B}$ is a **real vector space of dimension $8$**, with real basis $\{e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3\}$. The multiplication is $\mathbb{R}$-bilinear, and the scalar imaginary $i$ is now an element of the algebra, central but not a scalar.

The two views are related by a change of base ring, from the quaternion algebra $\mathbb{H}$ to the $\mathbb{C}$-algebra $\mathbb{B}$ by extension of scalars from $\mathbb{R}$ to $\mathbb{C}$, and back by restriction of scalars. The dimension relation is

$$
\dim_{\mathbb{R}} \mathbb{B} = 2 \cdot \dim_{\mathbb{C}} \mathbb{B},
$$

because each complex dimension contributes two real dimensions, the real and imaginary parts of its coefficient.

**Which view the physics uses.** Both, for different purposes, and it is worth being explicit about which is in force.

- The **real view** is the one in which the physics is written. The six distinguished subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ are **real** subspaces of this eight-dimensional space, the coordinate dictionary of the series is a dictionary between real parameters and physical coordinates, and the two signatures carried by the biquaternion norm are real forms on two of those subspaces. A statement about a signature is a statement over $\mathbb{R}$ and cannot be read off the complex view.

- The **complex view** is the view in which the complex scalars act as scalars, so the algebra is four-dimensional over $\mathbb{C}$ and therefore as small as it can be.

In this article both views are used, and the field is named whenever it matters. "Four-dimensional" means over $\mathbb{C}$; "eight-dimensional" means over $\mathbb{R}$.

### Developed Form

A general biquaternion is written in developed form as

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly,

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C}.
$$

We write

$$
\tilde{Q} = Q_0 + \mathbf{Q}, \qquad \mathbf{Q} = \sum_{k=1}^{3} Q_k e_k,
$$

where $Q_0$ is the **complex scalar part** and $\mathbf{Q}$ is the **complex vector part**. The tilde signals that $\tilde{Q}$ is an element of the algebra $\mathbb{B}$, not a four-vector.

Each complex coefficient is written in terms of its real and imaginary parts:

$$
Q_0 = q_0 + i q'_0, \qquad Q_k = q_k + i q'_k, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The scalar imaginary satisfies $i^2 = -1$ and commutes with every quaternion unit, $i e_k = e_k i$.

**The physical coordinates.** The eight real parameters are read as the coordinates of spacetime by the dictionary

$$
q'_0 = c\,t, \qquad (q_1, q_2, q_3) = (x, y, z), \qquad q_0 = c\,t', \qquad (q'_1, q'_2, q'_3) = (x', y', z'),
$$

with

$$
\mathbf{x} = x e_1 + y e_2 + z e_3, \qquad i\mathbf{x}' = i x' e_1 + i y' e_2 + i z' e_3 .
$$

Two elements of the algebra carry the two ends of the dictionary, and they are the two elements the physics works with:

$$
\tilde{Q} = ict\,e_0 + \mathbf{x} \quad\text{(the \textbf{material coordinate})},
\qquad
\tilde{Q} = ct'\,e_0 + i\mathbf{x}' \quad\text{(the \textbf{informational coordinate})}.
$$

The four coordinates $ct, x, y, z$ and the four coordinates $ct', x', y', z'$ are **the same eight parameters in a different grouping**, not two independent sets: the unprimed coordinates are the imaginary parts of the coefficients and the primed coordinates are the real parts. The material coordinate is the four-position of relativistic physics, written with the time coordinate $ict$ so that the Minkowski interval is carried by the biquaternion norm of the algebra; the informational coordinate is the same object read on the other sector. Primes always mark the informational end of the dictionary. **No index is raised or lowered anywhere in the series**, and no metric is used to move one: the $ict$ convention is what replaces that operation.

### The Algebra Structure

The algebra $\mathbb{B}$ is associative, non-commutative and unital, in both views. It is **not a division algebra**: it has zero divisors, and the study of them is the subject of *Biquaternion Zero Divisors*. In the physics of the series the zero divisors are not a pathology; they are the light cone, and the physical reading is worked out in *The Light Cone as the Biquaternion Zero Divisor Cone*.

The **center** is $\mathbb{C}$ in both views, with a subtlety worth naming. As a $\mathbb{C}$-algebra, the center is the scalar copy of $\mathbb{C}$ spanned by $e_0$: an element is central exactly when it commutes with every quaternion unit, and those are the $\tilde{Q} = Q_0 e_0$ with $Q_0 \in \mathbb{C}$. As an $\mathbb{R}$-algebra, the same center is a real vector space of dimension 2, spanned by $e_0$ and $ie_0$. It is the complex time sector of the series, and it carries both time coordinates of the dictionary and no spatial direction.

### Multiplication

The product of two biquaternions is defined by extending the quaternion product complex-linearly. In developed form,

$$
\tilde{Q} \circ \tilde{R} = \sum_{\mu=0}^{3} \sum_{\nu=0}^{3} Q_\mu R_\nu \, e_\mu e_\nu ,
$$

where the products $e_\mu e_\nu$ are those of the quaternion algebra, extended complex-linearly. In scalar-vector notation,

$$
\tilde{Q} \circ \tilde{R} = Q_0 R_0 - (\mathbf{Q}, \mathbf{R}) + Q_0 \mathbf{R} + R_0 \mathbf{Q} + [\mathbf{Q}, \mathbf{R}],
$$

where

$$
(\mathbf{Q}, \mathbf{R}) = \sum_{k=1}^{3} Q_k R_k , \qquad [\mathbf{Q}, \mathbf{R}] = \sum_{j,k,l=1}^{3} \epsilon_{jkl} Q_j R_k e_l
$$

are the **complex bilinear dot product** and the **complex bilinear cross product**, reducing to the ordinary ones when the coefficients are real.

The formula has the same shape as the quaternion product: scalar part, vector part, dot product, cross product. The only change is that the coefficients are complex.

**Physical face of the non-commutativity.** The cross-product term is where the non-commutativity lives, and it is the term the physics cannot do without: for two four-vectors in the material sector it is the term that produces, on composition of two boosts, the rotation the series calls the Wigner rotation and, followed along a worldline, the Thomas precession. The commutation of two generators, and with it the failure of two boosts to commute, is worked out in *Biquaternion Rotations and Lorentz Transformations*; the polar counterpart is in *The Polar Element Representation of Biquaternions*. In algebraic terms the point is only this: the product is not commutative, and the defect is a cross product in the vector part.

### Conjugations

There are **four** natural conjugations on $\mathbb{B}$. The first three come from the quaternion conjugation $\bar{\cdot}$ and the complex conjugation ${}^*$; the fourth is the negative of the Hermitian conjugation.

**Quaternion conjugation** $\bar{\tilde{Q}}$:

$$
\bar{\tilde{Q}} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3 .
$$

**Complex conjugation** $\tilde{Q}^*$:

$$
\tilde{Q}^* = Q_0^* e_0 + Q_1^* e_1 + Q_2^* e_2 + Q_3^* e_3 .
$$

**Hermitian conjugation** $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$:

$$
\tilde{Q}^\dagger = Q_0^* e_0 - Q_1^* e_1 - Q_2^* e_2 - Q_3^* e_3 .
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^\dagger$:

$$
\tilde{Q}^\flat = -Q_0^* e_0 + Q_1^* e_1 + Q_2^* e_2 + Q_3^* e_3 .
$$

Each conjugation is an involution: applying it twice returns the biquaternion. Each therefore splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and each of the two is a real vector subspace of $\mathbb{B}$.

**What each conjugation is for.** The four are not four interchangeable operations; each is the defining operation of one piece of the physics.

| conjugation | fixes | negates | physical role |
|---|---|---|---|
| $\bar{\cdot}$ | $\mathbb{C}_{\mathbb{B}}$ (complex time) | $\mathrm{Vect}(\mathbb{B})$ (complex space) | separates the time coordinates from the spatial ones |
| ${}^{*}$ | $\mathbb{H}_{\mathbb{B}}$ (real sector) | $i\mathbb{H}_{\mathbb{B}}$ (imaginary sector) | separates the real coefficients from the coefficients that carry $i$ |
| ${}^{\dagger}$ | $\mathbb{M}_+$ (informational) | $\mathbb{M}_-$ (material) | separates the informational sector from the material one |
| ${}^{\flat} = -{}^{\dagger}$ | $\mathbb{M}_-$ (material) | $\mathbb{M}_+$ (informational) | the defining involution of the material sector |

The last two lines are the same involution with the two eigenspaces exchanged, and that is why the fourth conjugation adds no subspace: the pair $\dagger,\flat$ produces the two sectors, but it produces them once.

### The Group of Conjugations

The quaternion conjugation and the complex conjugation are commuting involutions. They generate the Klein four-group

$$
\{\mathrm{id}, \bar{\cdot}, {}^{*}, {}^{\dagger}\} \cong \mathbb{Z}/2 \times \mathbb{Z}/2,
\qquad\text{with}\qquad
\tilde{Q}^\dagger = \bar{\tilde{Q}}^{*} = \tilde{Q}^{*\bar{}} .
$$

So Hermitian conjugation is the composition of the two commuting generators, and there is no fourth independent involution of this kind.

The anti-Hermitian conjugation is defined by $\tilde{Q}^\flat = -\tilde{Q}^\dagger$. It is an involution, since $(\tilde{Q}^\flat)^\flat = \tilde{Q}$, but it is **not** an algebra anti-automorphism, and it is not a member of the Klein group above. Composing it with $\dagger$ gives

$$
(\tilde{Q}^\dagger)^\flat = -\tilde{Q}, \qquad (\tilde{Q}^\flat)^\dagger = -\tilde{Q},
$$

so $\flat$ is $\dagger$ together with the central sign $-1$. Under a product it behaves as

$$
(\tilde{Q}\tilde{R})^\flat = -\tilde{R}^\flat \tilde{Q}^\flat ,
$$

an anti-automorphism only up to the sign. This is the algebraic reason the material sector is not a subalgebra: the involution that defines it is the one that does not respect the product.

## The Six Subspaces

The three commuting involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\dagger}$ each split $\mathbb{B}$ into a fixed space and an anti-fixed space. The **six** subspaces so obtained are the distinguished real subspaces of the algebra: four of dimension 4, together with the two-dimensional **center** and the six-dimensional **vector subspace**. The fourth conjugation produces no further subspace, as explained above.

The table gives each subspace under its **algebraic** name, from the property that defines it, and its **physical** name, from the role it plays in the series; the physical interpretation is a column of the same table because in this series it is part of the definition of the object.

| subspace | physical interpretation | defining condition | real basis | $\dim_{\mathbb{R}}$ | physical coordinates |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | complex time sector | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_0,\ ie_0$ | $2$ | $ct',\ ict$ |
| $\mathrm{Vect}(\mathbb{B})$ (vector) | complex space sector | $\bar{\tilde{Q}} = -\tilde{Q}$ | $e_1,\ e_2,\ e_3,\ ie_1,\ ie_2,\ ie_3$ | $6$ | $x,\ y,\ z,\ ix',\ iy',\ iz'$ |
| $\mathbb{H}_{\mathbb{B}}$ (quaternion) | real sector | $\tilde{Q}^{*} = \tilde{Q}$ | $e_0,\ e_1,\ e_2,\ e_3$ | $4$ | $ct',\ x,\ y,\ z$ |
| $i\mathbb{H}_{\mathbb{B}}$ (anti-quaternion) | imaginary sector | $\tilde{Q}^{*} = -\tilde{Q}$ | $ie_0,\ ie_1,\ ie_2,\ ie_3$ | $4$ | $ict,\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_+$ (Hermitian) | informational sector | $\tilde{Q}^{\dagger} = \tilde{Q}$ | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $4$ | $ct',\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_-$ (anti-Hermitian) | material sector | $\tilde{Q}^{\flat} = \tilde{Q}$ | $ie_0,\ e_1,\ e_2,\ e_3$ | $4$ | $ict,\ x,\ y,\ z$ |

Each of the six has its own article in the **Focus on Subspaces** group of the series:

| subspace | article |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | *The Center Subspace $\mathbb{C}_{\mathbb{B}}$ as the Complex Time Sector* |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | *The Vector Subspace $\mathrm{Vect}(\mathbb{B})$ as the Complex Space Sector* |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | *The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$ as the Real Sector* |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | *The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$ as the Imaginary Sector* |
| $\mathbb{M}_+$, the Hermitian subspace | *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* |
| $\mathbb{M}_-$, the anti-Hermitian subspace | *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* |

The relations between them are collected in *Relations Between Subspaces*, and the four conjugations themselves in *The Biquaternion Involution Lattice: Hermitian, Anti-Hermitian and Reversal*. What the present article uses of the six, again and again, is the following:

- $\mathbb{C}_{\mathbb{B}}$ is the set of central elements, a copy of $\mathbb{C}$ embedded as the scalar part, $\{\lambda e_0 : \lambda \in \mathbb{C}\}$; physically the complex time sector, carrying both $ct'$ and $ict$ and no direction in space;
- $\mathrm{Vect}(\mathbb{B})$ is the kernel of the scalar-part functional, equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$; physically the complex space sector, the three coordinates $x,y,z$ and their imaginary counterparts $ix',iy',iz'$;
- $\mathbb{H}_{\mathbb{B}}$ is the set of elements with real coefficients, a copy of the real quaternion algebra; physically the **real sector**, whose four parameters are the real coordinates $ct',x,y,z$, and the home of the rotation rotors;
- $i\mathbb{H}_{\mathbb{B}}$ is the set of products $i\tilde{P}$ with $\tilde{P} \in \mathbb{H}_{\mathbb{B}}$, a two-sided module over $\mathbb{H}_{\mathbb{B}}$ but not a subalgebra; physically the **imaginary sector**, whose parameters are $ict, ix', iy', iz'$, so that the material time coordinate is one of them;
- $\mathbb{M}_+$ is the set of elements with real scalar part and purely imaginary vector part; physically the **informational sector**;
- $\mathbb{M}_-$ is the set of elements with purely imaginary scalar part and real vector part; physically the **material sector**, which is where the four-position $ict\,e_0 + \mathbf{x}$ lives.

The two coordinates of the dictionary sit in the sectors, not in the blocks of the other groupings:

$$
ict\,e_0 + \mathbf{x} \in \mathbb{M}_- \quad\text{(material)},
\qquad
ct'\,e_0 + i\mathbf{x}' \in \mathbb{M}_+ \quad\text{(informational)} .
$$

Both are **split** by the quaternion decomposition and by the centre/vector decomposition: the material coordinate has its scalar part in $i\mathbb{H}_{\mathbb{B}}$ and its vector part in $\mathbb{H}_{\mathbb{B}}$, and the informational coordinate the other way round. This is why the physics is organised by the two sectors and not by the real and imaginary sectors: the sectors are the subspaces inside which a four-position sits whole.

### The Six Together

Of the six subspaces, exactly two are subalgebras: the centre $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$ and the real sector $\mathbb{H}_{\mathbb{B}} \cong \mathbb{H}$. Both are division algebras. The vector subspace is closed under neither multiplication nor left multiplication by $\mathbb{H}_{\mathbb{B}}$; the imaginary sector is an $\mathbb{H}_{\mathbb{B}}$-module but not a subalgebra; and the two sectors $\mathbb{M}_\pm$ are neither.

**Why the two physical sectors are not subalgebras.** The witnesses are one line each. In $\mathbb{M}_+$,

$$
(e_0 + ie_1)(e_0 + ie_2) = e_0 + ie_1 + ie_2 - e_3 ,
$$

which has a real vector part $-e_3$, so the product has left the informational sector. In $\mathbb{M}_-$,

$$
(ie_0)(ie_0) = -e_0 ,
$$

which has a real scalar part, so the product has left the material sector. The physical consequence is the one the series uses everywhere: the product of two four-vectors is not a four-vector, and it is the **biquaternion norm** and the **inner product**, not the algebra product, that carry the metric and the contractions of four-vectors. Multiplication in the algebra is reserved for the rotors and for the operators built from them.

The six subspaces are pairwise distinct, and their dimensions $2,6,4,4,4,4$ sum to more than $8$, so they necessarily overlap; how they do so is the subject of *Relations Between Subspaces*.

## The Quaternion Decomposition

The complex conjugation is an involution, and the two subspaces just defined are its eigenspaces: $\mathbb{H}_{\mathbb{B}}$ with eigenvalue $+1$, $i\mathbb{H}_{\mathbb{B}}$ with eigenvalue $-1$. Both have real dimension 4, and they are independent, so $\mathbb{B}$ splits as a direct sum.

Every biquaternion can be written uniquely as

$$
\tilde{Q} = \tilde{Q}_r + i \tilde{Q}_i ,
$$

where $\tilde{Q}_r$ and $\tilde{Q}_i$ are **ordinary quaternions** embedded in $\mathbb{B}$, with real coefficients. The two components are

$$
\tilde{Q}_r = \frac{1}{2}\left(\tilde{Q} + \tilde{Q}^{*}\right), \qquad \tilde{Q}_i = \frac{1}{2i}\left(\tilde{Q} - \tilde{Q}^{*}\right),
$$

both fixed by complex conjugation, with sum $\tilde{Q}_r + i\tilde{Q}_i = \tilde{Q}$. This is the direct sum

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}} .
$$

This is the **quaternion decomposition**. It expresses $\tilde{Q}$ as a quaternion plus the scalar imaginary times another quaternion, and it is the natural decomposition when $\mathbb{B}$ is thought of as the complexification of $\mathbb{H}$: the first summand is the "real part" of the complexification and the second the "imaginary part". Physically it is the split into the **real sector** and the **imaginary sector**, that is, into the parameters that carry no $i$ and the parameters that carry one; the material time coordinate $ict$ belongs to the second summand, which is why no four-position lies inside a single summand of this decomposition.

## The Hermitian Decomposition

The Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ are the two eigenspaces of the Hermitian conjugation. Every biquaternion decomposes uniquely as

$$
\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_- , \qquad \tilde{Q}_+ \in \mathbb{M}_+, \quad \tilde{Q}_- \in \mathbb{M}_- ,
$$

with the components obtained from the conjugation,

$$
\tilde{Q}_+ = \frac{1}{2}\left(\tilde{Q} + \tilde{Q}^{\dagger}\right), \qquad \tilde{Q}_- = \frac{1}{2}\left(\tilde{Q} - \tilde{Q}^{\dagger}\right),
$$

giving the direct sum

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_- .
$$

Both summands are real vector spaces of dimension 4, and their direct sum is the full eight-dimensional algebra.

**This is the decomposition the physics is organised by.** The two summands are the informational sector and the material sector, and each of them holds a four-position whole: the informational coordinate $ct'\,e_0 + i\mathbf{x}'$ lies in $\mathbb{M}_+$ and the material coordinate $ict\,e_0 + \mathbf{x}$ lies in $\mathbb{M}_-$. The decomposition is a vector-space decomposition and not an algebra decomposition: $\mathbb{M}_+$ and $\mathbb{M}_-$ are not subalgebras, as the witnesses above show, so the split is a split of the objects and not of the products.

## The Center and Vector Decomposition

The quaternion conjugation is the third commuting involution. Its eigenspaces are the centre $\mathbb{C}_{\mathbb{B}}$ (eigenvalue $+1$) and the vector subspace $\mathrm{Vect}(\mathbb{B})$ (eigenvalue $-1$), of real dimensions 2 and 6. Every biquaternion therefore decomposes uniquely as

$$
\tilde{Q} = \tilde{Q}_{\mathrm{c}} + \tilde{Q}_{\mathrm{v}} , \qquad
\tilde{Q}_{\mathrm{c}} = Q_0 e_0 \in \mathbb{C}_{\mathbb{B}} , \qquad
\tilde{Q}_{\mathrm{v}} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3 \in \mathrm{Vect}(\mathbb{B}) ,
$$

with

$$
\tilde{Q}_{\mathrm{c}} = \frac{1}{2}\left(\tilde{Q} + \bar{\tilde{Q}}\right), \qquad \tilde{Q}_{\mathrm{v}} = \frac{1}{2}\left(\tilde{Q} - \bar{\tilde{Q}}\right),
$$

giving

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}) .
$$

This is the decomposition into centre and derived subspace, and it is the one whose summands have unequal dimension: 2 and 6. Physically it is the split into the **complex time sector** and the **complex space sector**, that is, into what is purely scalar and what has a direction in space; a four-position contributes to both summands, its time coordinate to the first and its spatial vector to the second.

## Relation Between the Three Decompositions

The three decompositions

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}}, \qquad
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-, \qquad
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})
$$

are the eigenspace decompositions of the three pairwise commuting involutions ${}^{*}$, $\dagger$ and $\bar{\cdot}$. They are the only decompositions of this kind: each is determined by one of the three, and $\flat = -\dagger$ reproduces the eigenspaces of $\dagger$ with the signs exchanged and gives nothing new. That is why there are six subspaces rather than four or eight.

**The four coordinate blocks.** Because the involutions commute, the four-dimensional subspaces are built from four common pieces:

$$
A_1 = \mathbb{R} e_0, \qquad A_2 = \mathbb{R}(ie_0), \qquad
B_1 = \operatorname{span}_{\mathbb{R}}\{e_1, e_2, e_3\}, \qquad
B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1, ie_2, ie_3\} .
$$

These are the two **scalar blocks** $A_1, A_2$ of dimension 1 and the two **vector blocks** $B_1, B_2$ of dimension 3. In the dictionary, $A_1$ carries $ct'$, $A_2$ carries $ict$, $B_1$ carries $x,y,z$ and $B_2$ carries $ix',iy',iz'$. Every one of the six subspaces is a sum of blocks:

| subspace | blocks | $\dim_{\mathbb{R}}$ | physical coordinates |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $A_1 \oplus A_2$ | $2$ | $ct',\ ict$ |
| $\mathrm{Vect}(\mathbb{B})$ | $B_1 \oplus B_2$ | $6$ | $x,\ y,\ z,\ ix',\ iy',\ iz'$ |
| $\mathbb{H}_{\mathbb{B}}$ | $A_1 \oplus B_1$ | $4$ | $ct',\ x,\ y,\ z$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $A_2 \oplus B_2$ | $4$ | $ict,\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_+$ | $A_1 \oplus B_2$ | $4$ | $ct',\ ix',\ iy',\ iz'$ |
| $\mathbb{M}_-$ | $A_2 \oplus B_1$ | $4$ | $ict,\ x,\ y,\ z$ |

Each of the four four-dimensional subspaces takes one scalar block and one vector block, the four ways of choosing one from each column; the centre takes both scalar blocks and the vector subspace both vector blocks. **The real sector and the material sector are the two subspaces that take the real coordinates**, $A_1$ and $B_1$ between them, and the imaginary sector and the informational sector are the two that take the coordinates carrying $i$. The material coordinate $ict\,e_0 + \mathbf{x}$ takes $A_2$ from one and $B_1$ from the other, which is why it is in $\mathbb{M}_-$ and in neither $\mathbb{H}_{\mathbb{B}}$ nor $i\mathbb{H}_{\mathbb{B}}$ whole.

**The three pairings.** The three decompositions are exactly the three ways of splitting the four blocks into two complementary pairs: $\{A_1,B_1\}$ against $\{A_2,B_2\}$ gives the quaternion decomposition; $\{A_1,B_2\}$ against $\{A_2,B_1\}$ gives the sector decomposition; and $\{A_1,A_2\}$ against $\{B_1,B_2\}$ gives the centre/vector decomposition. There are exactly three such pairings of a four-element set into two pairs, so there are exactly three decompositions and no fourth.

**Intersections.** Two distinct subspaces meet in the blocks they share, so their intersection has dimension $0$, $1$ or $3$, and never $2$ or $4$:

$$
\mathbb{H}_{\mathbb{B}}\cap \mathbb{M}_+=A_1,\qquad
\mathbb{H}_{\mathbb{B}}\cap \mathbb{M}_-=B_1,\qquad
i\mathbb{H}_{\mathbb{B}}\cap \mathbb{M}_+=B_2,\qquad
i\mathbb{H}_{\mathbb{B}}\cap \mathbb{M}_-=A_2 ,
$$

$$
\mathbb{C}_{\mathbb{B}}\cap \mathbb{H}_{\mathbb{B}}=A_1,\qquad
\mathbb{C}_{\mathbb{B}}\cap i\mathbb{H}_{\mathbb{B}}=A_2,\qquad
\mathrm{Vect}(\mathbb{B})\cap \mathbb{H}_{\mathbb{B}}=B_1,\qquad
\mathrm{Vect}(\mathbb{B})\cap i\mathbb{H}_{\mathbb{B}}=B_2 ,
$$

$$
\mathbb{C}_{\mathbb{B}}\cap \mathbb{M}_+=A_1,\qquad
\mathbb{C}_{\mathbb{B}}\cap \mathbb{M}_-=A_2,\qquad
\mathrm{Vect}(\mathbb{B})\cap \mathbb{M}_+=B_2,\qquad
\mathrm{Vect}(\mathbb{B})\cap \mathbb{M}_-=B_1 .
$$

The only pairs of distinct subspaces that meet in $\{0\}$ are the three complementary pairs:

$$
\mathbb{M}_+ \cap \mathbb{M}_- = 0, \qquad
\mathbb{H}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} = 0, \qquad
\mathbb{C}_{\mathbb{B}} \cap \mathrm{Vect}(\mathbb{B}) = 0 .
$$

Every pair that is not one of these three shares blocks, hence meets in dimension 1 or 3. In physical terms, the two sectors meet in nothing, and each of them meets the centre in one time coordinate and the vector subspace in one vector block.

**Action of the conjugations.** The quaternion conjugation commutes with both ${}^{*}$ and $\dagger$, so it preserves each of the six subspaces, acting as $+1$ on the scalar blocks and $-1$ on the vector blocks. Multiplication by the central scalar $i$ interchanges the two summands in every decomposition:

$$
i\,\mathbb{H}_{\mathbb{B}}=i\mathbb{H}_{\mathbb{B}},\qquad i\,(i\mathbb{H}_{\mathbb{B}})=\mathbb{H}_{\mathbb{B}},
\qquad
i\,\mathbb{M}_+=\mathbb{M}_-,\qquad i\,\mathbb{M}_-=\mathbb{M}_+,
\qquad
i\,\mathbb{C}_{\mathbb{B}}=\mathbb{C}_{\mathbb{B}},\qquad i\,\mathrm{Vect}(\mathbb{B})=\mathrm{Vect}(\mathbb{B}) .
$$

The complex conjugation fixes $\mathbb{H}_{\mathbb{B}}$ and negates $i\mathbb{H}_{\mathbb{B}}$, while the Hermitian conjugation fixes $\mathbb{M}_+$ and negates $\mathbb{M}_-$. In particular it is **multiplication by $i$, not quaternion conjugation, that swaps the two sectors**; the centre and the vector subspace are each stable under it.

This is the algebraic statement of a physical one. Multiplication by $i$ carries the informational coordinate to a material coordinate,

$$
i\left(ct'\,e_0 + i\mathbf{x}'\right) = ict'\,e_0 - \mathbf{x}' ,
$$

which is $ict\,e_0 + \mathbf{x}$ with $ct = ct'$ and $\mathbf{x} = -\mathbf{x}'$: the same time and the reversed spatial vector. The passage between the two descriptions of the four-position in the series is therefore the central multiplication by $i$, an algebra operation and not a change of coordinates.

## Quadratic Forms and Inner Product

### The Biquaternion Norm

The **biquaternion norm** of a biquaternion is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2 ,
$$

a complex number in general, central, **multiplicative**,

$$
N(\tilde{Q} \circ \tilde{R}) = N(\tilde{Q})\,N(\tilde{R}) ,
$$

not positive-definite, and capable of vanishing for a nonzero $\tilde{Q}$. The elements on which it vanishes and the structure of the zero divisors are the subject of *Biquaternion Zero Divisors*.

**Physical reading: the biquaternion norm is the metric.** The series calls $N$ the **level-1 form**, and it is the form the whole framework is built on. On the material coordinate it is the Minkowski interval:

$$
N\!\left(ict\,e_0 + \mathbf{x}\right) = (ict)^2 + x^2 + y^2 + z^2 = -c^2t^2 + \mathbf{x}^2 .
$$

This is why the time coordinate is written $ict$: the single algebraic operation $N$ then reproduces the metric of relativistic physics with no $i$ inserted by hand and no sign chosen by hand. On the informational coordinate the same form gives the opposite signature:

$$
N\!\left(ct'\,e_0 + i\mathbf{x}'\right) = c^2t'^2 - \mathbf{x}'^2 .
$$

The vanishing of the biquaternion norm is the light cone: $N(ict\,e_0 + x e_1) = 0$ exactly when $x = \pm ct$, and the null material coordinates are the zero divisors of the algebra. The two signatures are worked out in **The Two Real Restrictions** below, and the physics of the zero divisors in *The Light Cone as the Biquaternion Zero Divisor Cone* and *Zero Divisors as a Physical Locus in Biquaternionic Form*.

**Why multiplicativity matters.** Because $N$ is multiplicative, an element of unit norm — a **rotor** — preserves the interval of every element it acts on. This is the single algebraic fact behind the rotor calculus of the series: the Lorentz transformations are the unit-norm elements acting on the material sector, and the four-position, the four-velocity and the four-momentum are all carried by the same action. The biquaternion norm is thus not a side object but the invariant of the theory.

### The Hermitian Form

The **Hermitian form** of a biquaternion is

$$
\tilde{Q} \tilde{Q}^\dagger =
\left( \sum_{\mu=0}^{3} |Q_\mu|^2 \right) e_0
+ \left( Q_0^* \mathbf{Q} - Q_0 \mathbf{Q}^* - [\mathbf{Q}, \mathbf{Q}^*] \right),
$$

where $\mathbf{Q}^{*}$ is the coefficient-wise conjugate of the vector part and $[\mathbf{Q},\mathbf{Q}^{*}]$ the complex bilinear cross product of the multiplication formula. In terms of the real and imaginary coefficient vectors, $\mathbf{q} = \sum_k q_k e_k$ and $\mathbf{q}' = \sum_k q'_k e_k$, with $[\mathbf{q},\mathbf{q}']$ the ordinary cross product,

$$
\tilde{Q} \tilde{Q}^\dagger =
\left( \sum_{\mu=0}^{3} |Q_\mu|^2 \right) e_0
+ 2i\left( q_0 \mathbf{q}' - q'_0 \mathbf{q} + [\mathbf{q}, \mathbf{q}'] \right),
$$

using $[\mathbf{Q},\mathbf{Q}^{*}] = -2i[\mathbf{q},\mathbf{q}']$ and $Q_0^{*}\mathbf{Q} - Q_0\mathbf{Q}^{*} = 2i(q_0\mathbf{q}' - q'_0\mathbf{q})$.

So the vector terms are not free: they are the vector part of the product, built from $\mathbf{Q}$, $\mathbf{Q}^{*}$ and $Q_0$. The result is generally a **biquaternion**, not a scalar, and it is Hermitian: $\tilde{Q}\tilde{Q}^\dagger$ is fixed by $\dagger$, hence lies in the informational sector $\mathbb{M}_+$. Its scalar part is

$$
\mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^\dagger\right) = \sum_{\mu=0}^{3} |Q_\mu|^2 = \sum_{\mu=0}^{3} \left(q_\mu^2 + q'^2_\mu\right),
$$

non-negative, vanishing only for $\tilde{Q} = 0$. Its vector part vanishes exactly when the four coefficients are real multiples of one complex number, $Q_\mu = \lambda r_\mu$ with $\lambda \in \mathbb{C}$ and $r_\mu \in \mathbb{R}$; equivalently, when every ratio $Q_\mu/Q_\nu$ of nonzero coefficients is real. For example, $\tilde{Q} = e_0 + ie_1$ has coefficients $Q_0 = 1$ and $Q_1 = i$, not real multiples of one another, so

$$
\tilde{Q}^\dagger = e_0 + ie_1, \qquad \tilde{Q}\tilde{Q}^\dagger = (e_0 + ie_1)^2 = 2e_0 + 2ie_1 ,
$$

with a nonzero vector part. Note that for this element the **biquaternion norm** vanishes instead, $N(\tilde{Q}) = 1 + i^2 = 0$: the two forms are different objects, and an element can be a zero divisor of the biquaternion norm and a perfectly ordinary element for the Hermitian form.

The corresponding **Euclidean norm** on the underlying real space is

$$
\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}\!\left(\tilde{Q}\tilde{Q}^\dagger\right)} = \sqrt{\sum_{\mu=0}^{3} |Q_\mu|^2} ,
$$

positive-definite, subadditive and homogeneous of degree one, and **not** multiplicative with respect to the algebra product.

**Physical reading.** The scalar part is the squared length of the element in the underlying eight-dimensional real space, which is what makes the algebra a normed space and the operator theory of the series well defined. The Hermitian form itself is an element of the informational sector, which is its name in the series: it is the form whose scalar part is the probabilistic norm of a state and whose vector part is the residue that a purely scalar reading of that norm would discard.

### The Inner Product

The **inner product** of two biquaternions is the complex scalar

$$
\langle \tilde{P}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} P_\mu^* Q_\mu
= \sum_{\mu=0}^{3} \left(p_\mu q_\mu + p'_\mu q'_\mu\right) + i \sum_{\mu=0}^{3} \left(p_\mu q'_\mu - p'_\mu q_\mu\right).
$$

It is generally **complex**, not real. It is linear in the second argument and anti-linear in the first,

$$
\langle \lambda \tilde{P}, \tilde{Q} \rangle = \lambda^* \langle \tilde{P}, \tilde{Q} \rangle, \qquad
\langle \tilde{P}, \lambda \tilde{Q} \rangle = \lambda \langle \tilde{P}, \tilde{Q} \rangle , \qquad \lambda \in \mathbb{C} ,
$$

and Hermitian in the sense that

$$
\langle \tilde{P}, \tilde{Q} \rangle^* = \langle \tilde{Q}, \tilde{P} \rangle .
$$

On the diagonal it is real and non-negative,

$$
\langle \tilde{Q}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} |Q_\mu|^2 = \mathrm{Sc}\!\left(\tilde{Q}\tilde{Q}^\dagger\right),
$$

vanishing only for $\tilde{Q} = 0$.

**Physical reading.** The real part of the inner product is the Euclidean pairing of the two elements, the same quantity that makes $\mathbb{B}$ a Hilbert space of real dimension 8, and the diagonal value is the squared norm. The **imaginary part** is a relative phase, the quantity that a pair of states carries and a single state does not; the series reads the interference of two informational states, and Pancharatnam's phase for a pair of polarisations, from exactly this term: see *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*.

### Relation Between the Three Forms

The three quadratic objects are distinct and each is used for a different job:

- **Biquaternion norm:** $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. Complex in general, central, multiplicative, capable of vanishing for nonzero $\tilde{Q}$. It controls the multiplicative structure: the rotors are its unit elements, and it carries the metric of the material sector.
- **Hermitian form:** $\tilde{Q}\tilde{Q}^\dagger$, an element of the informational sector whose scalar part is $\sum_\mu |Q_\mu|^2$ and whose vector part is generally nonzero. Not multiplicative. It carries the positive-definite norm used by the operator and informational side of the series.
- **Inner product:** $\langle \tilde{P},\tilde{Q}\rangle = \sum_\mu P_\mu^* Q_\mu$, complex in general, Hermitian, linear in the second argument. Its diagonal value equals the scalar part of the Hermitian form, and its imaginary part carries the relative phase of a pair.

The biquaternion norm controls the multiplicative structure, the scalar part of the Hermitian form (equivalently the diagonal of the inner product) controls the topological structure — continuity, completeness, the Euclidean topology — and the full inner product adds the phase.

### The Two Real Restrictions

On the **real sector** $\mathbb{H}_{\mathbb{B}}$, where the coefficients are real, the biquaternion norm is the sum of four squares and is positive-definite:

$$
N\!\left(q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3\right) = q_0^2 + q_1^2 + q_2^2 + q_3^2 ,
$$

the Euclidean form of the quaternion algebra, which is why the real sector is the home of the rotation rotors and carries no light cone. On the **imaginary sector** $i\mathbb{H}_{\mathbb{B}}$ the same form is the negative of a sum of four squares and is negative-definite, with no zero divisors either.

The two **sectors** are where the form becomes indefinite, and they are the two cases the physics uses:

| subspace | basis | biquaternion norm | signature |
|---|---|---|---|
| $\mathbb{H}_{\mathbb{B}}$ (real) | $e_0, e_1, e_2, e_3$ | $q_0^2 + \mathbf{q}^2$ | $(+,+,+,+)$ |
| $i\mathbb{H}_{\mathbb{B}}$ (imaginary) | $ie_0, ie_1, ie_2, ie_3$ | $-(q'^2_0 + \mathbf{q}'^2)$ | $(-,-,-,-)$ |
| $\mathbb{M}_-$ (material) | $ie_0, e_1, e_2, e_3$ | $-c^2t^2 + \mathbf{x}^2$ | $(-,+,+,+)$ |
| $\mathbb{M}_+$ (informational) | $e_0, ie_1, ie_2, ie_3$ | $c^2t'^2 - \mathbf{x}'^2$ | $(+,-,-,-)$ |

The material signature is the $ict$ metric of the series, $-c^2t^2 + \mathbf{x}^2$, and it is the signature of spacetime. The informational signature is its negative, which is not a second spacetime but the same form read on the other end of the dictionary. The two are exchanged by multiplication by $i$, exactly as the two sectors are. Only the two indefinite subspaces carry null elements, $N(\tilde{Q}) = 0$ with $\tilde{Q} \neq 0$; the light cone is the null cone of the material restriction.

## Summary

The biquaternion algebra is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and central scalar imaginary $i$. It is associative, non-commutative and not a division algebra.

It carries four natural conjugations, $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger}$ and $\flat = -\dagger$, of which the first three are commuting involutions and form the Klein four-group together with the identity. The **six** distinguished real subspaces are the eigenspaces of those three involutions:

- the **center** $\mathbb{C}_{\mathbb{B}} = \{Q_0 e_0\}$, of dimension 2, fixed by $\bar{\cdot}$, a subalgebra isomorphic to $\mathbb{C}$; the complex time sector, carrying $ct'$ and $ict$;
- the **vector subspace** $\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : Q_0 = 0\}$, of dimension 6, the anti-fixed space of $\bar{\cdot}$, the kernel of the scalar part and the derived subspace $[\mathbb{B},\mathbb{B}]$; the complex space sector, carrying $x,y,z$ and $ix',iy',iz'$;
- the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, of dimension 4, fixed by ${}^{*}$, the subalgebra isomorphic to $\mathbb{H}$; the real sector, carrying $ct',x,y,z$;
- the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$, of dimension 4, the anti-fixed space of ${}^{*}$, an $\mathbb{H}_{\mathbb{B}}$-module but not a subalgebra; the imaginary sector, carrying $ict,ix',iy',iz'$;
- the **Hermitian subspace** $\mathbb{M}_+$, of dimension 4, fixed by $\dagger$; the informational sector, carrying $ct',ix',iy',iz'$;
- the **anti-Hermitian subspace** $\mathbb{M}_-$, of dimension 4, fixed by $\flat$; the material sector, carrying $ict,x,y,z$.

The three involutions give three direct-sum decompositions, $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ and $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, which are the three pairings of the four coordinate blocks $\mathbb{R}e_0$, $\mathbb{R}(ie_0)$, $\operatorname{span}_\mathbb{R}\{e_1,e_2,e_3\}$, $\operatorname{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$; there is no fourth. Each of the four four-dimensional subspaces is one scalar block plus one vector block, and two distinct subspaces meet in dimension $0$, $1$ or $3$, the dimension $0$ occurring exactly for the three complementary pairs. Multiplication by the central $i$ swaps the two sectors and preserves the centre and the vector subspace.

On the algebra sit three quadratic objects, kept apart throughout: the **biquaternion norm** $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$, multiplicative and capable of vanishing for nonzero $\tilde{Q}$, which is the level-1 form and reproduces the Minkowski interval on the material coordinate and the opposite signature on the informational one; the **Hermitian form** $\tilde{Q}\tilde{Q}^\dagger$, an element of the informational sector whose scalar part is $\sum_\mu |Q_\mu|^2$; and the complex **inner product** $\langle \tilde{P},\tilde{Q}\rangle = \sum_\mu P_\mu^* Q_\mu$, whose diagonal value is that scalar part and whose imaginary part carries the relative phase of a pair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0 = 1$ | Identity |
| $e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$, commutes with $e_k$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| $Q_0$ | Complex scalar part |
| $\mathbf{Q}$ | Complex vector part |
| $c\,t = q'_0$, $(x,y,z) = (q_1,q_2,q_3)$ | Material coordinates |
| $c\,t' = q_0$, $(x',y',z') = (q'_1,q'_2,q'_3)$ | Informational coordinates |
| $\mathbf{x} = x e_1 + y e_2 + z e_3$ | Real spatial vector |
| $i\mathbf{x}' = i x' e_1 + i y' e_2 + i z' e_3$ | Imaginary spatial vector |
| $ict\,e_0 + \mathbf{x}$ | Material coordinate (four-position) |
| $c\,t'\,e_0 + i\mathbf{x}'$ | Informational coordinate |
| $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$ | Quaternion conjugate |
| $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$ | Complex conjugate |
| $\tilde{Q}^\dagger = Q_0^* e_0 - \mathbf{Q}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\bar{\tilde{Q}}^{*} = -\tilde{Q}^\dagger$ | Anti-Hermitian conjugate |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Biquaternion norm, the level-1 form |
| $\mathrm{Sc}(\tilde{Q}\tilde{Q}^\dagger) = \sum_\mu |Q_\mu|^2$ | Scalar part of the Hermitian form |
| $\langle \tilde{P},\tilde{Q}\rangle = \sum_\mu P_\mu^* Q_\mu$ | Inner product |
| $\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}(\tilde{Q}\tilde{Q}^\dagger)}$ | Euclidean norm |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, fixed-point set of $\bar{\cdot}$: complex time sector, basis $e_0, ie_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | Vector subspace, anti-fixed set of $\bar{\cdot}$: complex space sector, basis $e_1,e_2,e_3,ie_1,ie_2,ie_3$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace, fixed-point set of ${}^{*}$: real sector, basis $e_0,e_1,e_2,e_3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | Anti-quaternion subspace, anti-fixed set of ${}^{*}$: imaginary sector, basis $ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{M}_+$ | Hermitian subspace: informational sector, basis $e_0,ie_1,ie_2,ie_3$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace: material sector, basis $ie_0,e_1,e_2,e_3$ |
| $A_1,A_2,B_1,B_2$ | The four coordinate blocks $\mathbb{R}e_0$ ($ct'$), $\mathbb{R}(ie_0)$ ($ict$), $\operatorname{span}_\mathbb{R}\{e_1,e_2,e_3\}$ ($x,y,z$), $\operatorname{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$ ($ix',iy',iz'$) |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
