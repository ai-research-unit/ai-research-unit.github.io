# __Introduction to the General Plain Algebra of Biquaternions__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four general products, defined side by side in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Read as a multiplication, only one of the four makes that space an associative unital algebra: the **general plain bilinear product** $\tilde P \tilde Q$; the $\natural$-product is $\mathbb{C}$-bilinear as well but lacks associativity, and the two sesquilinear products are not $\mathbb{C}$-bilinear at all. This article takes the general plain bilinear product as the multiplication and builds the algebra it defines, then reads off the structure the axioms give it.

The construction is short and the consequences long. The product is $\mathbb{C}$-bilinear, associative and unital, so the space becomes an associative unital $\mathbb{C}$-algebra; a bilinear product is determined by its values on a basis, so the four basis elements carry all of it; and once the algebra is in place, its scalar structure, its centre, its generators and its presentation by relations are read off in turn.

Two boundaries are stated at once. The product is not defined here: the coordinate rule and the four names are *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and what the four rules are to one another is *Relations Between the Four General Products* and *Comparison Between the Four General Products*. And the question of which base rings $\mathbb{B}$ admits, together with the reading of the same product with the real scalars, is *Biquaternions as an Algebra over $\mathbb{R}$*, where the two admissible bases and the failure of the quaternions are treated; the centre of $\mathbb{B}$ and the centrality criterion are §*The Scalars Are the Centre* below. What this article adds is the algebra as the product makes it.

The elements, the basis and the conjugations are *Biquaternions as a Vector Space over $\mathbb{C}$*. The general theory is *Algebras: A General Introduction*, associativity is *Associative Algebras*, the identity is *Unital Algebras*, the tensor product is *Tensor Products of Algebras*, the presentation of an algebra by generators and relations is *Quotients of the Tensor Algebra*, and the anti-automorphism as an isomorphism onto the opposite algebra is *Opposite Algebras and Anti-Isomorphisms*. On the biquaternion side, the two-sided ideals and the simplicity of $\mathbb{B}$ are *Biquaternion Ideals and Peirce Decomposition*, the units and the invertibility criterion are *Introduction to the Six Subspaces*, the zero divisors are *Biquaternion Zero Divisors*, the square of one element is *Biquaternion Square Roots of a General Element*, and the matrix model of the algebra is *Biquaternion 2×2 Matrix Element Representation*.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$, $i^2 = -1$; a general element is $\tilde Q = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. Throughout, a biquaternion is written $\tilde Q = Q_0e_0 + \mathbf Q$ with $\mathbf Q = \sum_{k=1}^{3} Q_ke_k$, and $(\mathbf P,\mathbf Q) = \sum_k P_kQ_k$ is the complex bilinear dot product of the vector parts.

## The Multiplication as a Binary Operation

### The Rule

**Definition.** The **multiplication** of the algebra is the rule

$$
\cdot \; : \; \mathbb{B} \times \mathbb{B} \longrightarrow \mathbb{B} , \qquad
(\tilde P,\tilde Q) \longmapsto \tilde P\tilde Q = \sum_{\mu=0}^{3}\sum_{\nu=0}^{3} P_\mu Q_\nu \, e_\mu e_\nu ,
$$

the general plain bilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Each of the sixteen products $e_\mu e_\nu$ is a basis element up to sign, so the double sum is a complex combination of $e_0,\dots,e_3$: the rule is a map into $\mathbb{B}$ and is well defined. On the four coordinates it reads

$$
\tilde P\tilde Q = \bigl(P_0Q_0 - P_1Q_1 - P_2Q_2 - P_3Q_3\bigr)
+ \bigl(P_0Q_1 + P_1Q_0 + P_2Q_3 - P_3Q_2\bigr)e_1
+ \bigl(P_0Q_2 - P_1Q_3 + P_2Q_0 + P_3Q_1\bigr)e_2
+ \bigl(P_0Q_3 + P_1Q_2 - P_2Q_1 + P_3Q_0\bigr)e_3 .
$$

### The Scalar–Vector Form

Collecting the scalar part and the vector part of the two elements, the same product reads

$$
\tilde P\tilde Q = \bigl(P_0Q_0 - (\mathbf P,\mathbf Q)\bigr) + P_0\mathbf Q + Q_0\mathbf P + \mathbf P\times\mathbf Q ,
$$

where $(\mathbf P,\mathbf Q)$ and $\mathbf P\times\mathbf Q$ are the complex bilinear dot and cross products of the vector parts and the display is the one of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Its scalar part is $\mathrm{Sc}(\tilde P\tilde Q) = \sum_{\mu=0}^{3}\varepsilon_\mu P_\mu Q_\mu$ with $\varepsilon = (1,-1,-1,-1)$, and its vector part is the one displayed.

### The Multiplication Table

A product that is linear in each argument is fixed by its values on the basis pairs, so the multiplication is fixed by the following sixteen products.

**Proposition.** The products of the basis elements are

| | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

**Proof.** The entries are read from the coordinate rule; equivalently they are the products of the quaternion units, $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$ and $e_1^2 = e_2^2 = e_3^2 = -e_0$, of *Quaternion Algebra*, with the central imaginary admitted as a coefficient and never as a factor.

The table is the quaternion table. Every entry is a basis element up to sign, the diagonal entry $e_0e_0$ is the unit while the three others are $-e_0$, and the three imaginary units anticommute pairwise, $e_je_k = -e_ke_j$ for $j \neq k$ in $\{1,2,3\}$ (the unit commutes with everything, so the antisymmetry is confined to the imaginary block). The scalar imaginary $i$ occurs nowhere among the entries: it is central, so it can only be a coefficient, and this is why the table of a complex algebra is a table of real quaternions.

### Bilinearity and the Determination by the Table

**Proposition.** The multiplication is $\mathbb{C}$-**bilinear**:

$$
(\tilde P + \tilde Q)\tilde R = \tilde P\tilde R + \tilde Q\tilde R , \qquad
\tilde R(\tilde P + \tilde Q) = \tilde R\tilde P + \tilde R\tilde Q , \qquad
(A\tilde P)\tilde Q = A(\tilde P\tilde Q) = \tilde P(A\tilde Q) , \qquad A \in \mathbb{C} .
$$

**Proof.** Every coordinate on the right of the developed form is a sum of terms $P_\mu Q_\nu$ with a fixed coefficient, hence is additive and homogeneous in the four coordinates of $\tilde P$ alone and in the four coordinates of $\tilde Q$ alone. The three identities are that statement read coordinate by coordinate.

**Proposition (determination by the table).** The multiplication is the unique $\mathbb{C}$-bilinear map $\mathbb{B} \times \mathbb{B} \to \mathbb{B}$ sending the pair $(e_\mu,e_\nu)$ to the product $e_\mu e_\nu$ of the table.

**Proof.** A $\mathbb{C}$-bilinear map is determined by its values on the pairs of basis elements, and the double sum of the definition is such a map and takes those values.

**Corollary.** Two multiplications on the same space that agree on the sixteen pairs of basis elements agree on every pair.

## The Algebra Axioms

### Associativity

**Proposition.** The multiplication is **associative**: $(\tilde P\tilde Q)\tilde R = \tilde P(\tilde Q\tilde R)$ for all $\tilde P,\tilde Q,\tilde R \in \mathbb{B}$.

**Proof.** Both sides are $\mathbb{C}$-trilinear in $(\tilde P,\tilde Q,\tilde R)$, being built from the multiplication by bilinearity, so it suffices to check the 64 triples of basis elements. The basis elements are the four quaternion basis elements $e_0,e_1,e_2,e_3$ of *Quaternion Algebra*, every product of two of them is a basis element up to sign by the table, and the coefficient sign is a central scalar; each of the 64 triple products is therefore a triple product in the quaternion algebra, and those associate. The two sides agree on the basis triples, hence everywhere.

### The Unit

**Proposition.** The element $e_0$ is a **two-sided identity**: $e_0\tilde Q = \tilde Q e_0 = \tilde Q$ for every $\tilde Q$.

**Proof.** By bilinearity it suffices to check $\tilde Q = e_k$, and the first row and the first column of the table give it.

The identity is unique: a two-sided identity $u$ satisfies $u = uu' = u'$ for any other two-sided identity $u'$. It is written $e_0$ and is the unit of the algebra.

### Non-Commutativity

**Proposition.** The multiplication is **not commutative**.

**Proof.** $e_1e_2 = e_3$ while $e_2e_1 = -e_3$, and the two differ because $e_3$ is a basis element and $e_3 \neq -e_3$.

The centre is therefore a proper subspace, and it is the scalar line: §*The Scalars Are the Centre* below proves that and records the statement with the structure map.

### The Algebra Structure

**Theorem.** With the general plain bilinear product as its multiplication, $\mathbb{B}$ is a four-dimensional associative unital non-commutative $\mathbb{C}$-algebra.

**Proof.** By the propositions above the multiplication is a $\mathbb{C}$-bilinear, associative, unital binary operation on the $\mathbb{C}$-vector space $\mathbb{B}$, which is the definition of an algebra over the commutative ring $\mathbb{C}$ in the broad sense of *Algebras: A General Introduction*; the two hypotheses the corpus adds to that sense, associativity and an identity, are the subjects of *Associative Algebras* and *Unital Algebras* and both hold. The dimension is four on the basis $e_0,e_1,e_2,e_3$ (*Biquaternions as a Vector Space over $\mathbb{C}$*), and $e_1e_2 \neq e_2e_1$.

Every general statement about associative unital algebras is therefore available for $\mathbb{B}$: the two-sided ideals, the centre, the group of units, the modules and the opposite algebra. The rest of this article reads off the ones that the multiplication alone decides.

## The Multiplication as a Scalar Extension

### The Tensor Product

The underlying space of $\mathbb{B}$ is the tensor product $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ of the two $\mathbb{R}$-algebras $\mathbb{C}$ and $\mathbb{H}$, and the product on a tensor product of algebras (*Tensor Products of Algebras*) is

$$
(A \otimes h)(A' \otimes h') = (AA') \otimes (hh') , \qquad A,A' \in \mathbb{C}, \quad h,h' \in \mathbb{H} .
$$

Under the identification $1 \otimes e_k \mapsto e_k$, $i \otimes e_k \mapsto ie_k$ of the two eight-dimensional real spaces — the one forced by $(i\otimes e_0)(1\otimes e_k) = i\otimes e_k$ — this product is the general plain bilinear product: the two agree on the eight real basis elements $e_0,\dots,e_3,ie_0,\dots,ie_3$, and two $\mathbb{R}$-bilinear products agreeing on a real basis agree everywhere. **The multiplication is the tensor product of the complex multiplication and the quaternion multiplication.** Associativity is inherited from the two associative factors, and the unit is $1 \otimes 1 = e_0$.

### The Two Factor Embeddings

The two factor embeddings

$$
\mathbb{C} \longrightarrow \mathbb{B}, \quad A \longmapsto A \otimes 1 = Ae_0 , \qquad
\mathbb{H} \longrightarrow \mathbb{B}, \quad h \longmapsto 1 \otimes h ,
$$

are unital algebra homomorphisms over $\mathbb{R}$ and have commuting images (*Tensor Products of Algebras*); the commuting of the images is the statement that the scalars are central, which is the centrality used in the next section. The second image is the real quaternion subspace $\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_0 + \mathbb{R}e_1 + \mathbb{R}e_2 + \mathbb{R}e_3$, and on it the multiplication is the quaternion product of *Quaternion Algebra*.

The multiplication is thus the $\mathbb{C}$-bilinear extension of the quaternion product, and $\mathbb{B}$ is the **complexification** of $\mathbb{H}$: one quaternion algebra, read with the complex scalars. This is the sense in which the name is exact. The real algebra of *Biquaternions as an Algebra over $\mathbb{R}$* carries the same multiplication as the complex algebra here; only the scalar system changes, and with it the dimension, which doubles.

## The Scalars, the Centre and the Structure Map

### The Structure Map

The scalars of an algebra enter through the canonical unital ring homomorphism from the base ring into the centre, the map $\eta(r) = r1_A$ of *Unital Algebras*, whose image is the scalar line. Here it is

$$
\varphi : \mathbb{C} \longrightarrow Z(\mathbb{B}) , \qquad \varphi(A) = Ae_0 ,
$$

with image the scalar line $\mathbb{C}e_0 = \mathbb{C}_{\mathbb{B}}$, and the scalar action is $A\tilde Q = \varphi(A)\tilde Q$, applied to the four complex coefficients. The image is central, so the action is compatible with the product,

$$
A(\tilde P\tilde Q) = (A\tilde P)\tilde Q = \tilde P(A\tilde Q) , \qquad A \in \mathbb{C} ,
$$

which is the bilinearity proposition read as the axiom of an algebra: the first equality is associativity with the scalar written as $Ae_0$, and the second is where centrality enters, because $\tilde P(A\tilde Q) = (\tilde P\,Ae_0)\tilde Q$ agrees with $(Ae_0\,\tilde P)\tilde Q$ exactly when $Ae_0$ commutes with $\tilde P$.

### The Gate: a Central Element of Square $-1$

**The gate, applied here.** The complex structure of the multiplication is carried by one element. **The gate** is the elementary form of the structure map: a $\mathbb{C}$-algebra structure on a real algebra, compatible with its real structure, is the same thing as a central element $j$ with $j^2 = -1$, the scalar action being $(a+ib)\tilde Q = a\tilde Q + bj\tilde Q$. For $\mathbb{B}$ that element is the central imaginary $i$ itself — the element $j = i$ — and the complex structure it induces on the underlying real space is the real-linear map

$$
J : \mathbb{B} \longrightarrow \mathbb{B} , \qquad J(\tilde Q) = i\tilde Q , \qquad J^2 = -\mathrm{id} ,
$$

and the compatibility demanded at the product is exactly the formula above. Centrality is not decoration: the product of $\mathbb{B}$ is $\mathbb{R}$-bilinear in any case, and it is $\mathbb{C}$-bilinear precisely because $i$ is central.

### The Scalars Are the Centre

**Proposition.** The centre of $\mathbb{B}$ is the complex line spanned by $e_0$ and $ie_0$:

$$
Z(\mathbb{B}) = \mathbb{C} \otimes_{\mathbb{R}} Z(\mathbb{H}) = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{R} = \mathbb{C} = \mathbb{C}_{\mathbb{B}} .
$$

**Proof.** The centre of a tensor product of algebras over a field is the tensor product of their centres, and $Z(\mathbb{C}) = \mathbb{C}$ while $Z(\mathbb{H}) = \mathbb{R}$. In coordinates, $[\tilde Q,e_1] = 2Q_3e_2 - 2Q_2e_3$ vanishes exactly when $Q_2 = Q_3 = 0$, and $[\tilde Q,e_2]$ vanishes exactly when $Q_1 = Q_3 = 0$, so centrality forces $Q_1 = Q_2 = Q_3 = 0$; conversely every $Q_0e_0$ is central because $i$ commutes with the units.

The scalars cannot be enlarged further, because there is no room in the centre for more; which base rings are admissible, and why the quaternion factor cannot serve, is *Biquaternions as an Algebra over $\mathbb{R}$*, §*The Admissible Bases: $\mathbb{R}$, $\mathbb{C}$ and Not $\mathbb{H}$*.

**Corollary.** The algebra is **central** over $\mathbb{C}$: the image of the structure map is the whole centre, so no scalar is lost and no non-scalar is admitted as a scalar. The centre is a subalgebra isomorphic to the field $\mathbb{C}$, and it is proper, the algebra being non-commutative.

**Corollary.** The scalars are determined by the multiplication: the centre is an invariant of the algebra, so the field $\mathbb{C}$ acting on $\mathbb{B}$ is recoverable from the product alone.

### Central Simplicity and the Absence of Division

**Proposition.** $\mathbb{B}$ is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$. This is *Biquaternion Ideals and Peirce Decomposition*, cited and not repeated. Since the algebra is also central, it is a **central simple** $\mathbb{C}$-algebra, the subject of *Central Simple Algebras and the Brauer Group*.

Being central simple of dimension four over the algebraically closed field $\mathbb{C}$, the algebra admits a model as the full algebra of $2 \times 2$ matrices over $\mathbb{C}$, which is *Biquaternion 2×2 Matrix Element Representation*, and the module theory that model carries is *Modules over the General Plain Algebra of Biquaternions*. Nothing of the model is used here.

**Proposition.** $\mathbb{B}$ is **not a division algebra**.

**Proof.** The product

$$
(e_0 + ie_1)(e_0 - ie_1) = e_0^2 - (ie_1)^2 = e_0 - i^2e_1^2 = e_0 - e_0 = 0
$$

vanishes with both factors non-zero, so the algebra has zero divisors and is not a division ring. Equivalently the element $e_0+ie_1$ is not a unit, the product of an element with its natural conjugate being scalar and vanishing exactly on the non-units; the group of units and the invertibility criterion are *Introduction to the Six Subspaces*, and the zero divisors themselves are classified in *Biquaternion Zero Divisors*.

## Generators and the Presentation

### The Generators

**Proposition.** $\mathbb{B}$ is generated, as a $\mathbb{C}$-algebra with unit, by $e_1$ and $e_2$; more generally by any two of $e_1,e_2,e_3$.

**Proof.** The relations $e_1^2 = -e_0$ and $e_1e_2 = e_3$ of the table give $e_0$ and $e_3$ from $e_1$ and $e_2$, and the four basis elements span the algebra. For the other pairs, $e_1e_3 = -e_2$ and $e_2e_3 = e_1$ give the third unit from the two chosen ones, and $e_k^2 = -e_0$ gives the identity.

### The Relations and the Presentation

**Proposition.** The generators $e_1,e_2$ satisfy

$$
e_1^2 = e_2^2 = -e_0 , \qquad e_1e_2 + e_2e_1 = 0 ,
$$

and these relations present the algebra: writing $\mathbb{C}\langle E_1,E_2\rangle$ for the free associative $\mathbb{C}$-algebra on two generators,

$$
\mathbb{B} \cong \mathbb{C}\langle E_1,E_2\rangle \big/ \bigl(E_1^2 + 1 , \; E_2^2 + 1 , \; E_1E_2 + E_2E_1\bigr) .
$$

**Proof.** The relations hold on the basis by the table, so $E_1 \mapsto e_1$, $E_2 \mapsto e_2$ descends to a homomorphism from the quotient onto $\mathbb{B}$, which is surjective because the two generate. In the quotient every word in $E_1,E_2$ is a $\mathbb{C}$-combination of $1, E_1, E_2, E_1E_2$: the relation $E_1E_2 + E_2E_1 = 0$, read as $E_2E_1 = -E_1E_2$, moves every occurrence of $E_1$ to the left of every occurrence of $E_2$, and then $E_1^2 = E_2^2 = -1$ reduces the exponents of the two letters modulo two. The reduced words are $\pm 1, \pm E_1, \pm E_2, \pm E_1E_2$, so the quotient is at most four-dimensional, and a surjection from a space of dimension at most four onto the four-dimensional algebra $\mathbb{B}$ is an isomorphism (*Quotients of the Tensor Algebra*, for algebras presented by generators and relations).

The algebra presented is the **quaternion algebra over $\mathbb{C}$**: the quaternion relations of *Quaternion Algebra*, with the base field enlarged from $\mathbb{R}$ to $\mathbb{C}$. This is the second reading of the name biquaternion, and it agrees with the first, the complexification of the previous section.

The relation that ties $e_3$ to the two generators is not redundant. Were the three imaginary units taken as generators with the pairwise relations $E_jE_k + E_kE_j = 0$ for $j \neq k$ and $E_k^2 = -1$ alone, the element $E_1E_2$ would remain independent of $1, E_1, E_2, E_3$: the three square relations and the three anticommutations do not force $E_1E_2$ into the span of the generators, and the algebra presented is eight-dimensional rather than four.

## The Subalgebras and the Real Form

### The Scalar Line

The centre $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ is a $\mathbb{C}$-subalgebra of $\mathbb{B}$, isomorphic to the field $\mathbb{C}$ and proper. It is the only scalar line the algebra has, by the preceding section, and it sits in every unital subalgebra, since a unital subalgebra contains the identity and hence every $\mathbb{C}$-multiple of it (*Unital Algebras*). A subalgebra need not be unital: the line $\mathbb{C}(e_1 + ie_2)$ is a subalgebra of $\mathbb{B}$ in which the product vanishes identically, because $(e_1 + ie_2)^2 = 0$.

### The Quaternion Subalgebra and Its Imaginary

The quaternion subspace $\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_0 + \mathbb{R}e_1 + \mathbb{R}e_2 + \mathbb{R}e_3$ is closed under the product, each of the sixteen products of the table lying in $\{\pm e_0, \pm e_1, \pm e_2, \pm e_3\}$, so it is a real subalgebra of $\mathbb{B}$, and on it the multiplication is the quaternion product. It is not a $\mathbb{C}$-subalgebra, being closed under real scalars only. Since $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ as real vector spaces (*Biquaternions as a Vector Space over $\mathbb{C}$*), the subalgebra is a **real form** of $\mathbb{B}$: the real algebra whose complexification is $\mathbb{B}$ (*Real Forms and the Descent of an Algebra*).

The real subspace $i\mathbb{H}_{\mathbb{B}} = \mathbb{R}(ie_0) + \mathbb{R}(ie_1) + \mathbb{R}(ie_2) + \mathbb{R}(ie_3)$ is a real subspace but not a $\mathbb{C}$-subspace, since $i\,(ie_1) = -e_1 \notin i\mathbb{H}_{\mathbb{B}}$, and it is **not** a subalgebra: the element $ie_1$ squares to

$$
(ie_1)^2 = i^2e_1^2 = (-1)(-e_0) = e_0 ,
$$

which lies outside $i\mathbb{H}_{\mathbb{B}}$. The two halves of the quaternion decomposition differ in this: one is a subalgebra and one is not.

### The Subalgebra Generated by One Element

The subalgebra $\mathbb{C}[\tilde Q] = \mathbb{C}e_0 + \mathbb{C}\tilde Q + \mathbb{C}\tilde Q^2 + \cdots$ generated by one element is commutative and at most two-dimensional:

$$
\tilde Q^2 = \bigl(Q_0^2 - (\mathbf Q,\mathbf Q)\bigr) + 2Q_0\mathbf Q \in \mathbb{C}e_0 + \mathbb{C}\tilde Q ,
$$

the developed square being that of *Biquaternion Square Roots of a General Element*. So $\mathbb{C}[\tilde Q] = \mathbb{C}e_0$ for central $\tilde Q$, and $\mathbb{C}[\tilde Q] = \mathbb{C}e_0 \oplus \mathbb{C}\tilde Q$ otherwise. In the second case the element $\tilde Q - Q_0e_0$ has square $-(\mathbf Q,\mathbf Q)e_0$, and the plane is read off from it: when $(\mathbf Q,\mathbf Q) \neq 0$ it is the algebra $\mathbb{C} \oplus \mathbb{C}$ of two copies of the field with coordinatewise multiplication, and when $(\mathbf Q,\mathbf Q) = 0$ it is the algebra of dual numbers $\mathbb{C}[t]/(t^2)$.

## The Other Three Products

The comparison of the four general products settles which of them is a multiplication. The two sesquilinear products are conjugate-linear in their second argument, so neither can be the multiplication of a $\mathbb{C}$-algebra; the $\natural$-product is $\mathbb{C}$-bilinear, but it is not associative and it has an identity on the left only, so it is a bilinear product that is not the multiplication of an associative unital algebra (*Comparison Between the Four General Products*). **Exactly one of the four general products is the multiplication of an associative unital $\mathbb{C}$-algebra, and it is the general plain bilinear product.**

The four are not unrelated, and the algebra determines all of them. Each is the multiplication with a conjugation applied in one or both slots:

$$
\tilde P^{\natural}\tilde Q = \natural(\tilde P)\,\tilde Q , \qquad
\tilde P\tilde Q^{*} = \tilde P\,\natural(\bar{\tilde Q}) , \qquad
\tilde P^{\natural}\tilde Q^{*} = \natural(\tilde P)\,\natural(\bar{\tilde Q}) ,
$$

where the complex conjugation $\bar{\cdot}$ conjugates the coefficients, ${}^{\natural}$ negates the vector units, the two commute, and $\tilde Q^{*} = \natural(\bar{\tilde Q}) = \bar{\tilde Q^{\natural}}$. The map ${}^{\natural}$ is a $\mathbb{C}$-linear anti-automorphism of $\mathbb{B}$, and $\bar{\cdot}$ is an automorphism of its underlying real algebra that is conjugate-linear over $\mathbb{C}$ (*The Group of Involutions*). Each of the three products is therefore the multiplication with one of these maps inserted in one or both slots, and this is the source of the properties the comparison tabulates: the reversed order in which the left multiplications of the $\natural$-product compose, and the conjugate-linearity of the two sesquilinear products in their second argument.

## Summary

The general plain bilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, read as a multiplication on the underlying $\mathbb{C}$-vector space of $\mathbb{B}$, is $\mathbb{C}$-bilinear, associative and unital. It is determined by the sixteen products of the four basis elements, and the table is the quaternion table with the central imaginary allowed as a coefficient.

$$
\boxed{\ \text{With the general plain bilinear product, } \mathbb{B} \text{ is an associative unital non-commutative } \mathbb{C}\text{-algebra of dimension four.}\ }
$$

Its scalars enter through the structure map $\varphi(A) = Ae_0$, whose image is the scalar line and which is central; the algebra is the complexification of $\mathbb{H}$ by the tensor product of algebras; its centre is the scalar line, so it is central, simple and hence central simple; and it is not a division algebra, the product of $e_0 + ie_1$ and $e_0 - ie_1$ being zero. Two generators suffice, and the relations $e_1^2 = e_2^2 = -e_0$ and $e_1e_2 + e_2e_1 = 0$ present the algebra as the quaternion algebra over $\mathbb{C}$.

The real quaternion subspace is a real subalgebra and a real form; its imaginary $i\mathbb{H}_{\mathbb{B}}$ is not a subalgebra and not a $\mathbb{C}$-subspace; and the subalgebra generated by one element is the plane spanned by $e_0$ and that element, a product of two copies of $\mathbb{C}$ when $(\mathbf Q,\mathbf Q) \neq 0$ and the dual numbers when $(\mathbf Q,\mathbf Q) = 0$. The other three of the four general products are the multiplication with a conjugation in one or both slots, which is why the comparison finds only one multiplication among them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | the biquaternion algebra, read here with the complex scalars |
| $e_0, e_1, e_2, e_3$ | complex basis; $e_0$ the unit, $e_k$ the quaternion units |
| $i$ | central scalar imaginary, $i^2 = -1$ |
| $\tilde Q = Q_0e_0 + \mathbf Q$ | a biquaternion and its scalar–vector split, $\mathbf Q = \sum_k Q_ke_k$ |
| $(\mathbf P,\mathbf Q) = \sum_k P_kQ_k$ | complex bilinear dot product of the vector parts |
| $\varphi : \mathbb{C} \to Z(\mathbb{B})$, $A \mapsto Ae_0$ | the structure map of the complex algebra |
| $i$, $J : \tilde Q \mapsto i\tilde Q$ | the central element of square $-1$, and the complex structure it defines |
| $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ | the centre, equal to the scalar line |
| $\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_0 + \mathbb{R}e_1 + \mathbb{R}e_2 + \mathbb{R}e_3$ | the quaternion subspace, a real subalgebra and a real form |
| ${}^{\natural}$, $\bar{\cdot}$ | the natural and the complex conjugation |
| ${}^{*} = \bar{\cdot} \circ {}^{\natural} = \natural \circ \bar{\cdot}$ | the Hermitian conjugation |
| $\tilde Q\tilde Q^{\natural} = \sum_\mu Q_\mu^2$ | the product of an element with its natural conjugate, central and scalar |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion product whose complexification carries the multiplication.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for algebras over a commutative ring, the structure map into the centre and the tensor product of algebras.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the quaternion algebra over a field, its presentations and its behaviour under an extension of scalars.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the presentation of an algebra by generators and relations and for central simplicity.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the product, its coordinate rule and its scalar–vector form.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table that decides which of the four general products is a multiplication.
