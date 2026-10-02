
# __Real Structures on a Projective Space__

## Introduction

A **real structure** on a projective space over a field with an involution is an involution of the space that conjugates the scalars, and its **real points** are the points it fixes; the structure is the descent datum by which the projective geometry over the larger field is read as the projective geometry over the fixed field. The article develops the structure in the **involution on the elements** layer of this Part: the projective space over a field with an involution carries the antilinear involutions, the real structure is one of them, the real points are its fixed locus, and the fixed descent is the real form of the space. The two signs of the antilinear involution give the two kinds of structure: the involution of the first kind, whose square is the identity and whose fixed locus is a real projective space, and the involution of the second kind, whose square is $-1$ and which has no real point.

The article develops the antilinear maps and the real structures on a vector space, the induced involution on the projective space and the identification of the real points with the projectivisation of the fixed real form, the two kinds of structure with the empty and the nonempty real locus, the classification of the real structures by the Galois cohomology, and the relation of the real structure to the operator group, where the fixed subgroup of the involution is a real form of the projective group and gives the real Möbius and the real orthogonal and unitary groups.

The article assumes *Field Extensions* of Part I for the field with an involution and the Galois theory of the quadratic extension; *Real Forms and the Descent of an Algebra* of Part I and *The Involution on a Complex Vector Space*, later in this Part, for the descent and the antilinear involutions; *Projective Geometry* and *Operators on a Projective Space* of this Part for the projective space and the operator group; and *Vector Spaces* of Part I for the real forms of a vector space. The real structures on a complex manifold and the Galois descent of the varieties are *Real Structures on a Complex Manifold* and *Real Structures on Varieties and Galois Descent*, later in this Part and in Part II, and the article names them as forward references. No distance and no physics is invoked.

## Antilinear Maps and Real Structures

### The Antilinear Maps

**Definition.** Let $L/K$ be a quadratic extension of fields with the nontrivial Galois element written as a bar, $x \mapsto \bar{x}$, and let $V$ be an $L$-vector space. A map $\sigma : V \to V$ is **antilinear** when it is additive and $\sigma(\lambda x) = \bar{\lambda}\,\sigma(x)$ for every $\lambda \in L$; an antilinear involution is an antilinear map with $\sigma^2 = \mathrm{id}$ up to a scalar, and it is of the **first kind** when $\sigma^2 = \mathrm{id}$ and of the **second kind** when $\sigma^2 = -\mathrm{id}$.

**Definition.** A **real structure** on $V$ is an antilinear involution of the first kind,

$$
\sigma : V \to V, \qquad \sigma(\lambda x) = \bar{\lambda}\,\sigma(x), \qquad \sigma^2 = \mathrm{id} ;
$$

the **real form** of $V$ is the fixed space

$$
V^{\sigma} = \{x \in V : \sigma(x) = x\} ,
$$

a vector space over the fixed field $K$, and the pair $(V,\sigma)$ is the **descent datum** of the $K$-vector space $V^\sigma$ over $L$.

**Proposition.** Let $\sigma$ be a real structure on $V$. Then $V^\sigma$ is a $K$-subspace of $V$ with

$$
V = V^\sigma \otimes_K L , \qquad \dim_K V^\sigma = \dim_L V ,
$$

the inclusion and the scalar extension giving the isomorphism; the assignment $W \mapsto W^\sigma$ is an equivalence between the real structures on the $L$-spaces and the $K$-spaces, the inverse sending a $K$-space $U$ to $U \otimes_K L$ with the involution $u \otimes \lambda \mapsto u \otimes \bar{\lambda}$; and every $x \in V$ is written uniquely as $x = y + i z$ with $y, z \in V^\sigma$ when $L = K(i)$ is a quadratic extension with the element $i$ of square in $K$.

**Proof.** A vector of $V$ fixed by $\sigma$ is determined by its coordinates in a basis, and the fixed space is a $K$-subspace because $\sigma$ is additive and $K$-linear on the fixed scalars; the $L$-span of $V^\sigma$ is $V$ because $x + \sigma(x)$ and $(x - \sigma(x))/i$ lie in $V^\sigma$ and reconstruct $x$, and the decomposition is unique; the equivalence with the $K$-spaces is the standard Galois descent. The statement is in *Real Forms and the Descent of an Algebra* and in the Galois theory of *Field Extensions*.

**Remark (the second kind).** When $\sigma^2 = -1$ the fixed space is zero over $K$, and the structure is not a descent to a real form but a **quaternionic structure**: the pair $(V,\sigma)$ is a module over the division algebra of the elements $a + b\sigma$, which is a quaternion algebra over $K$; the antilinear involution of the second kind corresponds to the quaternionic structure of the space, and it has no fixed vector in the projective space. The two kinds are separated by the sign of the square of the involution, and the article treats both.

## The Involution on the Projective Space

### The Induced Involution

**Definition.** Let $V$ be an $L$-vector space with a real structure $\sigma$. The **induced involution** on the projective space is the map

$$
[\sigma] : \mathbb{P}(V) \longrightarrow \mathbb{P}(V), \qquad [\sigma]([v]) = [\sigma(v)] ,
$$

which is well defined because $\sigma(\lambda v) = \bar{\lambda}\sigma(v)$ represents the same point as $\sigma(v)$; it is an involution of the first kind on $\mathbb{P}(V)$ when $\sigma^2 = \mathrm{id}$, and an involution of the second kind without fixed points when $\sigma^2 = -\mathrm{id}$. The induced involution is **antiholomorphic** in the complex case, and it is the **real structure** of the projective space.

**Proposition.** The induced involution is well defined, it satisfies $[\sigma]^2 = \mathrm{id}$ in the first kind, and it preserves the incidence and the projective subspaces, carrying a subspace $\mathbb{P}(W)$ to $\mathbb{P}(\sigma(W))$; the real structures on $V$ and on $\mathbb{P}(V)$ are in bijection up to the scalars, and the induced involution determines the real structure of $V$ up to a scalar.

**Proof.** The well-definedness is the computation $[\sigma(\lambda v)] = [\bar\lambda \sigma(v)] = [\sigma(v)]$; the incidence is preserved because $\sigma$ is additive and semilinear, carrying the linear subspaces to the linear subspaces; the bijection is the statement that the antilinear maps of $V$ differing by a scalar induce the same projective map, and the inverse is the choice of a lift. The statement is the projective form of the descent, in *Projective Geometry*.

### The Real Points

**Theorem.** Let $\sigma$ be a real structure on $V$ of the first kind. Then the fixed points of the induced involution are exactly the projectivisation of the real form,

$$
\mathbb{P}(V)^{[\sigma]} = \mathbb{P}(V^{\sigma}) ,
$$

and the fixed locus is a projective space over the fixed field $K$ of the same dimension as $\mathbb{P}(V)$; for $L = \mathbb{C}$ and $K = \mathbb{R}$ the real points of $\mathbb{P}^n(\mathbb{C})$ with the standard structure are the real projective space $\mathbb{P}^n(\mathbb{R})$.

**Proof.** A point $[v]$ is fixed by $[\sigma]$ exactly when $\sigma(v) = \lambda v$ for a scalar; applying $\sigma$ again gives $v = \bar\lambda \lambda v$, so $|\lambda| = 1$ in the complex case, and rescaling $v$ by a square root of $\lambda$ makes $\sigma(v) = v$, so the fixed points are the points of the real form; the converse is immediate. The statement is the standard real locus of the conjugation, in *Projective Geometry* and *Real Structures on Varieties and Galois Descent*.

**Theorem (the second kind has no real points).** Let $\sigma$ be an antilinear involution of the second kind, $\sigma^2 = -\mathrm{id}$. Then the induced involution has no fixed point in $\mathbb{P}(V)$: a point with $[\sigma]([v]) = [v]$ would give $\sigma(v) = \lambda v$ and $\sigma^2(v) = \bar\lambda \lambda v = -v$, forcing $|\lambda|^2 = -1$ and $\lambda$ in the field of the appropriate sign, with no solution over the real or the complex field. The real locus of the projective space with a quaternionic structure is empty.

**Proof.** The eigenvalue equation of the antilinear map is $\sigma(v) = \lambda v$; the square gives $\sigma^2(v) = \bar\lambda\lambda v = |\lambda|^2 v$, and the second kind demands $|\lambda|^2 = -1$, which has no solution over $\mathbb{R}$ or $\mathbb{C}$; hence no eigenvector and no fixed projective point. The statement is the standard absence of the real points for the quaternionic structure, in *Real Structures on Varieties and Galois Descent*.

## The Classification of the Real Structures

**Definition.** Two real structures $\sigma$ and $\sigma'$ on $V$ are **equivalent** when there is a linear automorphism $A \in GL(V)$ with $\sigma' = A\sigma A^{-1}$, and the real structures on $\mathbb{P}(V)$ are equivalent when the corresponding involutions of the projective space are conjugate by an element of the projective group $PGL(V)$; the equivalence classes are the **real forms** of the projective space.

**Theorem.** Let $L/K$ be a quadratic extension and $V$ an $L$-vector space of dimension $n+1$. Then the real structures of the first kind on $\mathbb{P}(V)$ form a single equivalence class under $PGL(V)$, and the real structures of the second kind form a single class when they exist; the two classes are distinguished by the existence of the real points, and the stabiliser of a real structure is the projective group of the real form, a real form of $PGL(V)$.

**Proof.** Two real forms of $V$ of the same dimension are isomorphic as $K$-vector spaces, and an isomorphism extends to an $L$-linear automorphism carrying one real structure to the other, so the first-kind structures are conjugate; for the second kind the same argument applies to the quaternion modules. The stabiliser is the group of the $K$-linear automorphisms of the real form, which is the fixed subgroup of the involution on $PGL(V)$, and it is a real form in the sense of the Galois descent. The statement is the Galois descent of the projective group, in *Real Forms and the Descent of an Algebra*.

**Remark (the Galois cohomology).** The real forms of the projective space are the elements of the first Galois cohomology set $H^1(\operatorname{Gal}(L/K), PGL_{n+1}(L))$, and the theorem above is the statement that the two kinds of structure correspond to the two classes of the cohomology for the quadratic extension; the real forms of the classical groups are the same computation for the other groups, and they are *Real Forms of a Complex Lie Group and the Cartan Involution* of Part III and the theory of the classical groups. The article keeps the projective case and names the general theory.

## The Fixed Subgroup and the Operator Group

**Definition.** Let $\sigma$ be a real structure on $V$ of the first kind and let $[\sigma]$ be the induced involution on $\mathbb{P}(V)$. The **fixed subgroup** of the operator group is

$$
PGL(V)^{[\sigma]} = \{g \in PGL(V) : [\sigma]\,g\,[\sigma] = g\} ,
$$

the group of the projectivities commuting with the real structure; it is the projective group of the real form $V^\sigma$, and its elements are the real projectivities of the real projective space.

**Proposition.** The fixed subgroup of the involution $[\sigma]$ on $PGL(V)$ is the projective general linear group of the real form, $PGL(V^\sigma) = PGL_{n+1}(K)$, and the real structures on the operator group are the fixed subgroups of the antilinear involutions; for $L = \mathbb{C}$ and $K = \mathbb{R}$ the real Möbius group $PSL(2,\mathbb{R})$ of *The Involution on the Möbius Operators*, later in this Part, is the fixed subgroup of the complex conjugation acting on $PSL(2,\mathbb{C})$.

**Proof.** A projectivity commuting with $[\sigma]$ is induced by a linear map $A$ with $A\sigma = \sigma A$ up to a scalar, hence by a map preserving the real form and $K$-linear on it; conversely a real projectivity extends complex-linearly and commutes with the conjugation. The two-dimensional instance is the fixed subgroup of the complex conjugation on $PSL(2,\mathbb{C})$, which is $PSL(2,\mathbb{R})$. The statement is in *Real Forms and the Descent of an Algebra* and, for the two-dimensional instance, in *The Involution on the Möbius Operators*, later in this Part.

**Remark (the real geometry).** The fixed points of the real structure are the real points of the projective space, and the fixed subgroup is the operator group of the real points; the geometry of the real points is the real projective geometry, and the complex geometry is recovered by the scalar extension. This is the descent of the geometry along the involution, and it is the geometric form of the descent of the vector space; the article is the projective instance of the general descent of *Real Structures on Varieties and Galois Descent*.

## Summary

A real structure on an $L$-vector space $V$ over a quadratic extension is an antilinear involution $\sigma$, of the first kind when $\sigma^2 = \mathrm{id}$ and of the second kind when $\sigma^2 = -\mathrm{id}$; the fixed space $V^\sigma$ is a $K$-vector space with $V = V^\sigma \otimes_K L$, and the assignment is the Galois descent. The induced involution $[\sigma]([v]) = [\sigma(v)]$ is well defined on the projective space, it preserves the incidence, and its fixed locus is exactly the projectivisation of the real form, $\mathbb{P}(V)^{[\sigma]} = \mathbb{P}(V^\sigma)$; for $\mathbb{C}$ and $\mathbb{R}$ the standard structure has the real projective space $\mathbb{P}^n(\mathbb{R})$ as its real points, while the involution of the second kind, the quaternionic structure, has no real point. The real structures of the first kind form a single equivalence class under the projective group, the stabiliser of one of them is a real form of the projective group, and the classes are the elements of the Galois cohomology of the projective group. The fixed subgroup of the involution on $PGL(V)$ is the projective group of the real form, of which the real Möbius group $PSL(2,\mathbb{R})$ and the real projective groups are the instances, and the descent is the projective case of the general real structure on a variety.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L/K$ | Quadratic extension, bar the nontrivial Galois element |
| $\sigma(\lambda x) = \bar\lambda\sigma(x)$ | Antilinear map |
| $\sigma^2 = \mathrm{id}$ | Real structure of the first kind |
| $\sigma^2 = -\mathrm{id}$ | Involution of the second kind, quaternionic structure |
| $V^\sigma$ | Real form, the fixed $K$-subspace |
| $V = V^\sigma \otimes_K L$ | Descent datum |
| $[\sigma]([v]) = [\sigma(v)]$ | Induced involution on $\mathbb{P}(V)$ |
| $\mathbb{P}(V)^{[\sigma]} = \mathbb{P}(V^\sigma)$ | Real points |
| $\mathbb{P}^n(\mathbb{R})$ | Real points of the standard structure on $\mathbb{P}^n(\mathbb{C})$ |
| $PGL(V)^{[\sigma]} = PGL(V^\sigma)$ | Fixed subgroup, the real projective group |
| $H^1(\operatorname{Gal}(L/K), PGL(V))$ | Galois cohomology classifying the real forms |

## Further Reading

- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the descent and the cohomology of the forms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the algebras with involution and the real forms.
- C. T. C. Wall, "On the classification of Hermitian forms", *Compositio Mathematica* **23** (1971), 315–321, for the Hermitian forms and the descent.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the Galois descent and the real forms of the varieties.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the real forms of the classical groups and the projective groups.
- Armand Borel and Jacques Tits, "Groupes réductifs", *Publications Mathématiques de l'IHÉS* **27** (1965), 55–151, for the forms of the algebraic groups and the descent.
