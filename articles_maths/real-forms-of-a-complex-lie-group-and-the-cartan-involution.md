
# __Real Forms of a Complex Lie Group and the Cartan Involution__

## Introduction

A complex Lie group has many real Lie groups with the same complexification, and the passage from the complex object to its real forms is governed by an anti-linear involution, the **conjugation**. On a real form of a complex semisimple group there is a second involution, the **Cartan involution**, characterised by the positivity of the twisted Killing form; its fixed subgroup is a maximal compact subgroup, and the quotient is the symmetric space of the group. The classification of the real forms is the classification of the conjugations, equivalently of the Cartan involutions, and it is the first place at which an involution on the elements organises an entire structure theory.

This article treats real forms of a complex Lie group and the Cartan involution, with the classification and the symmetric space they determine. It is the first article of the `- * Theory` group of the category; the structure of a complex Lie group is from *Lie Groups* and *Real Forms of a Complex Lie Algebra*, the symmetric decomposition and the maximal compact subgroup are *The Cartan Decomposition and the Cartan Involution* below, and the analytic consequences are *Unitary Representations of a Lie Group* and *Hermitian Lie Groups and the Bounded Domain*.

The article assumes the real and the complex Lie group, the complexification of a real Lie algebra and the relation between a Lie group and its algebra from *Lie Groups* and *The Lie Correspondence and the Adjoint Representation*, the semisimple structure, the Killing form and the root data from *Structure of Lie Algebras* and *Root Systems and Classification*, and the elementary theory of involutions from *Involutive Groups* and *Graded Lie Algebras with an Involution*. The symmetric space is treated here as the homogeneous space $G/K$ with the involution that defines it; its curvature, its geodesics and its metric as objects belong to the geometry of Part IV, and its harmonic analysis to the later articles of this category.

## Complexifications and Real Forms

### The Complexification

**Definition.** Let $\mathrm{G}$ be a real Lie algebra. Its **complexification** is $\mathrm{G}_{\mathbb{C}} = \mathrm{G}\otimes_{\mathbb{R}}\mathbb{C}$, with the bracket extended by complex bilinearity; it is a complex Lie algebra with $\dim_{\mathbb{C}}\mathrm{G}_{\mathbb{C}} = \dim_{\mathbb{R}}\mathrm{G}$, and the map $X\mapsto X\otimes1$ is an isomorphism $\mathrm{G}\to\mathrm{G}_{\mathbb{C}}$ of real Lie algebras onto a real subspace.

**Definition.** Let $G$ be a real Lie group and $\mathrm{G}$ its Lie algebra. A **complexification** of $G$ is a complex Lie group $G_{\mathbb{C}}$ with a homomorphism $G \to G_{\mathbb{C}}$ whose differential identifies $\mathrm{G}_{\mathbb{C}}$ with $\mathrm{G}\otimes_{\mathbb{R}}\mathbb{C}$. A complexification exists locally always and globally when $G$ is simply connected, and it is unique up to isomorphism in the simply connected case.

**Definition.** Let $\mathrm{G}_{\mathbb{C}}$ be a complex Lie algebra. A **real form** of $\mathrm{G}_{\mathbb{C}}$ is a real Lie subalgebra $\mathrm{G}$ with $\mathrm{G}_{\mathbb{C}} = \mathrm{G}\oplus i\mathrm{G}$ as real vector spaces, equivalently $\mathrm{G}_{\mathbb{C}} = \mathrm{G}\otimes_{\mathbb{R}}\mathbb{C}$. A real form of a complex Lie group $G_{\mathbb{C}}$ is a real Lie subgroup $G$ whose Lie algebra is a real form and such that the multiplication $G\times G\to G_{\mathbb{C}}$ complexifies to an isomorphism of a neighbourhood.

### The Conjugation

**Definition.** Let $\mathrm{G}_{\mathbb{C}}$ be a complex Lie algebra. A **conjugation** is an anti-linear involutive automorphism $\sigma$, that is a map with $\sigma(\lambda X + \mu Y) = \bar\lambda\,\sigma(X) + \bar\mu\,\sigma(Y)$, $\sigma([X,Y]) = [\sigma X, \sigma Y]$ and $\sigma^2 = \mathrm{id}$.

**Theorem (real forms and conjugations).** The assignment $\sigma \mapsto \mathrm{G}^{\sigma} = \{X : \sigma X = X\}$ is a bijection from the conjugations of $\mathrm{G}_{\mathbb{C}}$ onto the real forms of $\mathrm{G}_{\mathbb{C}}$, with inverse $\mathrm{G}\mapsto \sigma$, where $\sigma$ is the anti-linear extension of the identity of $\mathrm{G}$ by complex conjugation on the scalar.

*Proof.* If $\sigma$ is a conjugation, then $\mathrm{G}^{\sigma}$ is a real subspace closed under the bracket, and every $Z \in \mathrm{G}_{\mathbb{C}}$ is $X + iY$ with $X = \frac12(Z + \sigma Z)$ and $Y = \frac{1}{2i}(Z - \sigma Z)$ in $\mathrm{G}^{\sigma}$, so $\mathrm{G}_{\mathbb{C}} = \mathrm{G}^{\sigma}\oplus i\mathrm{G}^{\sigma}$. Conversely, a real form $\mathrm{G}$ with $\mathrm{G}_{\mathbb{C}} = \mathrm{G}\oplus i\mathrm{G}$ determines the anti-linear map fixing $\mathrm{G}$ pointwise and negating $i\mathrm{G}$, which is involutive, additive and multiplicative for the bracket by linearity.

**Corollary.** Two real forms $\mathrm{G}$ and $\mathrm{G}'$ are **equivalent** — conjugate by an automorphism of $\mathrm{G}_{\mathbb{C}}$ — exactly when their conjugations are conjugate by an automorphism of $\mathrm{G}_{\mathbb{C}}$; the classification of the real forms is therefore the classification of the conjugations up to conjugacy.

*Proof.* An automorphism $\varphi$ of $\mathrm{G}_{\mathbb{C}}$ carries the conjugation $\sigma$ to $\varphi\sigma\varphi^{-1}$, whose fixed algebra is $\varphi(\mathrm{G}^{\sigma})$; the correspondence is bijective.

## The Cartan Involution

### The Twisted Form

**Definition.** Let $\mathrm{G}$ be a real semisimple Lie algebra and $B$ its Killing form. An **involution** is an automorphism $\theta$ of $\mathrm{G}$ with $\theta^2 = \mathrm{id}$. It is a **Cartan involution** when the **twisted form**

$$
B_\theta(X,Y) = -B(X,\theta Y)
$$

is positive definite.

**Definition.** The **Cartan decomposition** is the eigenspace decomposition

$$
\mathrm{G} = \mathrm{K}\oplus\mathrm{P}, \qquad \mathrm{K} = \{X : \theta X = X\}, \quad \mathrm{P} = \{X : \theta X = -X\} .
$$

Its structure — the bracket relations, the maximal compact subgroup and the global decomposition of the group — is the subject of *The Cartan Decomposition and the Cartan Involution*, and the present article uses the definition and the existence.

**Theorem (existence and conjugacy).** Every real semisimple Lie algebra has a Cartan involution, and any two Cartan involutions are conjugate by an inner automorphism. The fixed algebra $\mathrm{K}$ is a maximal compactly embedded subalgebra, and the form $B_\theta$ is invariant under $\theta$ and positive definite on $\mathrm{G}$.

*Proof (sketch).* The existence is proved by writing the automorphism group as the fixed set of a Cartan involution of a larger algebra and using the polar decomposition; the conjugacy is the statement that the positive definite forms of the type $B_\theta$ form a single orbit under the adjoint action, which is the convexity of the space of such forms; the positivity on $\mathrm{G}$ is the definition, and the compactness of $\mathrm{K}$ follows from the negative definiteness of $B$ on $\mathrm{K}$.

**Corollary.** On a compact real form $\mathrm{K}$ the Killing form is negative definite, and the identity is a Cartan involution; conversely a semisimple algebra with negative definite Killing form is compact and the identity is its Cartan involution.

*Proof.* The form $B_\theta$ for $\theta = \mathrm{id}$ is $-B$, which is positive definite exactly when $B$ is negative definite; the characterisation of compactness by the negative definiteness of the Killing form is that of *Structure of Lie Algebras*.

### The Compact Real Form

**Theorem (the compact form is unique).** A complex semisimple Lie algebra has exactly one real form up to conjugacy whose Killing form is negative definite, the **compact real form**; every real form $\mathrm{G}$ has a Cartan involution $\theta$, and the subalgebra $\mathrm{K}\oplus i\mathrm{P}$ of $\mathrm{G}_{\mathbb{C}}$ is a compact real form.

*Proof.* The algebra $\mathrm{K}\oplus i\mathrm{P}$ is closed under the bracket because $[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}$ and $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$, and on it $B$ is negative definite: on $\mathrm{K}$ it is so by the compactness of $\mathrm{K}$ and on $i\mathrm{P}$ it is the negative of the positive form $B_\theta$. Uniqueness is the conjugacy of the Cartan involutions.

## The Classification

### The Classification of the Real Forms

**Theorem (classification).** Let $\mathrm{G}_{\mathbb{C}}$ be a complex semisimple Lie algebra and $\mathrm{G}_u$ its compact real form. The real forms of $\mathrm{G}_{\mathbb{C}}$ are in bijection with the conjugacy classes of involutions of $\mathrm{G}_u$, under the assignment $\mathrm{G} = \{X \in \mathrm{G}_u : \theta(\bar X) = X\}$ to a Cartan involution $\theta$ read on $\mathrm{G}_u$.

*Proof.* A real form $\mathrm{G}$ has a Cartan involution $\theta$ and a compact form $\mathrm{K}\oplus i\mathrm{P} = \mathrm{G}_u$; the involution $\theta$ extends to a complex-linear involution of $\mathrm{G}_{\mathbb{C}}$ commuting with the conjugation, hence restricts to an involution of $\mathrm{G}_u$; conversely an involution $\theta$ of $\mathrm{G}_u$ extended complex-linearly and composed with the conjugation of $\mathrm{G}_u$ produces an anti-linear involution whose fixed algebra is the real form. The two assignments are inverse, and conjugacy corresponds to conjugacy.

**Corollary (the classification is finite).** There are finitely many real forms of a complex semisimple Lie algebra, one for each conjugacy class of involutions of the compact form, and the classification is read in the root data as the **Satake diagrams**, the Dynkin diagram with the vertices fixed by the involution and the arrows recording the restricted root data.

*Proof.* An involution of a compact semisimple algebra is determined by its restriction to a maximal torus and its action on the roots; the fixed subalgebra and the restricted root system are the data of the Satake diagram, and the combinatorial classification of the diagrams is that of *Root Systems and Classification*.

### The Symmetric Space

**Definition.** Let $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ be the Cartan decomposition. The **symmetric space** attached to $\mathrm{G}$ is the homogeneous space $G/K$, where $K$ is the connected subgroup with algebra $\mathrm{K}$ and $G$ is a corresponding Lie group; it is a Riemannian symmetric space when the form $B_\theta$ is transported to the tangent space $T_{eK}G/K \cong \mathrm{P}$.

**Theorem.** The symmetric space $G/K$ has an involutive geodesic symmetry at each point, the curvature tensor at the base point is $R(X,Y)Z = -[[X,Y],Z]$ for $X,Y,Z\in\mathrm{P}$, and the isotropy representation of $K$ on $\mathrm{P}$ is the adjoint action.

*Proof.* The involution $\theta$ of $G$ defined by the Cartan involution of the algebra fixes $K$ and induces the geodesic symmetry $gK\mapsto \theta(g)K$; the curvature is computed from the Cartan decomposition and the Maurer--Cartan equation, the components of the bracket of two elements of $\mathrm{P}$ lying in $\mathrm{K}$ and the double commutator being the standard expression. The geometric development — the exponential coordinates, the Weyl group and the restricted root system — belongs to Part IV, and the operator-theoretic counterpart is *The Convolution Operator on a Symmetric Space* of the analysis on groups.

### The Satake Diagram

**Definition.** Let $\mathrm{G}$ be a real form of the complex semisimple algebra $\mathrm{G}_{\mathbb{C}}$ with Cartan involution $\theta$ and let $\mathrm{G}_{\mathbb{C}} = \mathrm{K}_{\mathbb{C}}\oplus\mathrm{P}_{\mathbb{C}}$ be the decomposition of the complexification by $\theta$. The **Satake diagram** of $\mathrm{G}$ is the Dynkin diagram of $\mathrm{G}_{\mathbb{C}}$ together with the data: a node is **black** when the corresponding root is annihilated by the complexified Cartan subalgebra of $\mathrm{K}$, and two nodes are joined by an arrow when the corresponding roots are exchanged by the involution of the diagram induced by $\theta$.

**Theorem.** Two real forms of $\mathrm{G}_{\mathbb{C}}$ are isomorphic if and only if their Satake diagrams coincide after the symmetries of the diagram, and the real form is determined by its Satake diagram; the number of the white nodes is the restricted rank of the real form, that is the dimension of a maximal abelian subspace of $\mathrm{P}$.

*Proof.* The Satake diagram records the conjugacy class of the conjugation and therefore the real form; the reconstruction of the form from the diagram is the standard construction in which the black nodes generate the compact part and the arrows encode the involution on the roots. The rank statement is the identification of the restricted roots with the roots on the white nodes.

### The Split and the Quasi-Split Forms

**Definition.** A real form is **split** when it has a Cartan subalgebra contained in $\mathrm{P}$, equivalently when no root is compact and the restricted rank is maximal; it is **quasi-split** when the only compact simple factor of $\mathrm{K}$ is the centre of the complexification, equivalently when all the black nodes of the Satake diagram are isolated; and it is **compact** when all the nodes are black, equivalently when $\mathrm{P} = 0$ and the form is compact.

**Theorem.** Every complex semisimple algebra has a unique split real form up to isomorphism, and the compact form is the other extreme; the intermediate real forms are interpolated by the Satake diagrams, the split form having all nodes white and the compact form all nodes black.

*Proof.* The uniqueness of the split form is the classification of the real forms with a maximal non-compact Cartan subalgebra; the interpolation statement is read from the diagram, and the compact form is determined by the negative definiteness of the Killing form.

### The Involutions of the Compact Form

**Theorem.** Let $\mathrm{K}$ be the compact real form of $\mathrm{G}_{\mathbb{C}}$. Then the real forms of $\mathrm{G}_{\mathbb{C}}$ are in bijection with the conjugacy classes of the involutions of $\mathrm{K}$, the real form of an involution $\tau$ being the fixed algebra of the conjugation $\sigma$ on $\mathrm{G}_{\mathbb{C}}$ that is $+\mathrm{id}$ on $\mathrm{K}^{\tau}$ and $-\mathrm{id}$ on the orthogonal complement of $\mathrm{K}^{\tau}$ in $\mathrm{K}$ extended by the antilinearity; the maximal compact subalgebra of the real form is $\mathrm{K}^{\tau}$.

*Proof.* An involution of the compact form extends to a conjugation of the complexification, and two involutions give isomorphic real forms exactly when they are conjugate; the maximal compact subalgebra is the fixed set, which is compactly embedded by the compactness of $\mathrm{K}$. The proof is in the references.

## Examples

### The Algebra of Rank One

For $\mathrm{G}_{\mathbb{C}} = \mathrm{sl}_2(\mathbb{C})$ the real forms are $\mathrm{su}(2)$ (compact, the Killing form negative definite), $\mathrm{sl}_2(\mathbb{R})$ (the form $\mathrm{K}\oplus\mathrm{P}$ with $\mathrm{K} = \mathrm{so}(2)$ and $\mathrm{P}$ two-dimensional), and $\mathrm{su}(1,1)\cong\mathrm{sl}_2(\mathbb{R})$; the Cartan involution of $\mathrm{sl}_2(\mathbb{R})$ is $\theta(X) = -X^t$ on the traceless matrices, whose fixed set is $\mathrm{so}(2)$ and whose symmetric space is the hyperbolic plane of Part IV.

### The Orthogonal Algebras

For $\mathrm{G}_{\mathbb{C}} = \mathrm{so}(n,\mathbb{C})$ the real forms are $\mathrm{so}(p,q)$ with $p+q = n$, up to the order of the two numbers; the Cartan involution is $\theta(X) = -X^t$ with respect to the standard nondegenerate form of signature $(p,q)$, the fixed algebra is $\mathrm{so}(p)\oplus\mathrm{so}(q)$ and the symmetric space is the Grassmannian of the $p$-planes of definite parity, the geometry of which belongs to Part IV.

### The Compact Forms

A compact real form has no non-trivial symmetric space of the type above: the Cartan involution is the identity, $\mathrm{P} = 0$, and $G/K$ is a point; the compact case is the boundary case of the classification, and its representation theory is *Unitary Representations of a Lie Group*.

## Summary

A real form of a complex Lie algebra $\mathrm{G}_{\mathbb{C}}$ is a real subalgebra $\mathrm{G}$ with $\mathrm{G}_{\mathbb{C}} = \mathrm{G}\oplus i\mathrm{G}$, and the real forms are in bijection with the anti-linear involutions, the conjugations, by $\mathrm{G} = \mathrm{G}^{\sigma}$; equivalently they are classified up to equivalence by the conjugacy classes of the conjugations. A real semisimple algebra carries a **Cartan involution** $\theta$, an automorphism of order two for which the twisted Killing form $B_\theta(X,Y) = -B(X,\theta Y)$ is positive definite; any two Cartan involutions are conjugate by an inner automorphism, the fixed algebra $\mathrm{K}$ is a maximal compactly embedded subalgebra, and $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ is the Cartan decomposition. The compact real form is the unique one with negative definite Killing form, and the general real form is obtained from it by an involution of the compact form; the classification is the finite list of conjugacy classes of such involutions, read as the Satake diagrams. The pair $(\mathrm{G},\theta)$ determines the symmetric space $G/K$, whose geodesic symmetries are the involutions and whose curvature at the base point is the double bracket on $\mathrm{P}$; the geometric development of the symmetric space belongs to Part IV and its harmonic analysis to the later articles of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{G}_{\mathbb{C}} = \mathrm{G}\otimes_{\mathbb{R}}\mathbb{C}$ | the complexification of a real Lie algebra |
| $\sigma$ | a conjugation, an anti-linear involutive automorphism |
| $\mathrm{G}^{\sigma} = \{X : \sigma X = X\}$ | the real form fixed by a conjugation |
| $B$ | the Killing form |
| $\theta$ | a Cartan involution, an automorphism with $\theta^2 = \mathrm{id}$ |
| $B_\theta(X,Y) = -B(X,\theta Y)$ | the twisted form, positive definite |
| $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ | the Cartan decomposition |
| $\mathrm{K}$ | the fixed algebra, a maximal compactly embedded subalgebra |
| $\mathrm{G}_u = \mathrm{K}\oplus i\mathrm{P}$ | the compact real form of $\mathrm{G}_{\mathbb{C}}$ |
| Satake diagram | the root datum of a real form |
| $G/K$ | the symmetric space, with curvature $R(X,Y)Z = -[[X,Y],Z]$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the Cartan involution, the real forms and the symmetric space.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the classification of the real forms, the Cartan involution and the Satake diagrams.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume II (Wiley, 1969), for the symmetric spaces and their curvature.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the structure of real semisimple Lie algebras and the Cartan involution.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4--6 (Springer, 2002), for the root data, the involutions and the classification.
