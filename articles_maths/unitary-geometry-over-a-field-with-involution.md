
# __Unitary Geometry over a Field with Involution__

## Introduction

A field with an involution is a field together with an order-two automorphism, the conjugation of the field, and the geometry built on it is **unitary geometry**: the vector space over the field carries the **Hermitian forms**, the forms that are sesquilinear and equal to their own conjugate transpose, and the operators that preserve such a form form the **unitary group**. The article develops the structure in the **involution on the elements** layer of this Part: the field involution is the datum, the Hermitian forms are the figures it cuts out, and the unitary group is the operator group of the geometry. The two specialisations are the fields with the trivial involution, where the Hermitian forms are the symmetric bilinear forms and the unitary geometry is the orthogonal geometry, and the fields of a quadratic extension, where the conjugation is nontrivial and the Hermitian geometry is genuinely new.

The article develops the fields with an involution and the two kinds of conjugating structure, the Hermitian forms and their matrices, the unitary, special unitary and general unitary groups with their exact sequences and dimensions, the unitary geometry of the projective space with the Hermitian polarity and the Hermitian quadric, and the examples of the finite fields, the complex numbers and the local fields. The classification of the Hermitian forms is the subject of *Hermitian Forms and Unitary Geometry*, and the local case is *Hermitian Spaces over a Local Field* and *Hermitian Forms over a Local Field*; the article states the definitions and the group, and it cites the classification.

The article assumes *Field Extensions* of Part I for the fields, their automorphisms and the quadratic extensions; *Vector Spaces* and *Bilinear Forms* of Parts I and II for the sesquilinear forms, their matrices and their radicals; *Quadratic Forms and Polarisation* of Part II for the Witt theory, named as the source of the classification; and *Projective Geometry* and *Operators on a Projective Space* of this Part for the projective reading. The article owns the field-with-involution structure and the unitary group. No distance and no physics is invoked.

## Fields with Involution

### Definition and the Two Kinds

**Definition.** An **involution** of a field $K$ is an automorphism $\sigma$ with $\sigma^2 = \mathrm{id}$, and the **fixed field** is

$$
K_0 = K^\sigma = \{x \in K : \sigma(x) = x\} .
$$

The involution is **trivial** when $\sigma = \mathrm{id}$; otherwise $K/K_0$ is a Galois extension of degree two when $K_0$ is the whole fixed field, and the involution is the nontrivial element of the Galois group. The coefficient conjugation is written with a bar, $\bar{x} = \sigma(x)$, and the elements of $K_0$ are the **fixed** or **scalar** elements of the geometry.

**Proposition.** Let $\sigma$ be a nontrivial involution of a field $K$ and let $K_0$ be its fixed field; then $K/K_0$ is a quadratic extension, $K = K_0(\theta)$ for an element $\theta$ with $\sigma(\theta) = -\theta$, and the **norm** $N(x) = x\bar{x}$ and the **trace** $\operatorname{Tr}(x) = x + \bar{x}$ are the two maps from $K$ to $K_0$; the norm is multiplicative and the trace is additive, and an element is fixed exactly when it equals its conjugate.

**Proof.** The fixed field of an automorphism of order two has index two by the artin–Schreier argument, and the extension is Galois of degree two; the element $x - \bar{x}$ is negated by $\sigma$, so any $x$ with $x \neq \bar{x}$ generates $K$ over $K_0$ and is a candidate for $\theta$; the norm and the trace lie in the fixed field by inspection, and the multiplicativity and the additivity are the definitions. The statement is in *Field Extensions*.

**Example (the standard involutions).** On the complex field $\mathbb{C}$ the involution is the complex conjugation with the fixed field $\mathbb{R}$; on a finite field $\mathbb{F}_{q^2}$ the involution is the Frobenius $x \mapsto x^q$ with the fixed field $\mathbb{F}_q$; on the field $\mathbb{Q}(\sqrt{d})$ of a squarefree integer $d$ the involution sends $\sqrt{d}$ to $-\sqrt{d}$ with the fixed field $\mathbb{Q}$; on the real numbers and on any field with the trivial involution the only involution is the identity.

**Remark.** The two cases that the article distinguishes are the **trivial** involution, in which the geometry is the orthogonal geometry of Part II and the unitary group is the orthogonal group, and the **nontrivial** involution, in which the geometry is the Hermitian geometry. A field of characteristic two with the trivial involution is the degenerate case in which the symmetric forms and the Hermitian forms differ, and the article keeps the characteristic not two unless it says otherwise.

## Hermitian Forms

### Definition and Matrices

**Definition.** Let $V$ be a vector space over a field $K$ with involution $\sigma$. A **Hermitian form** is a map $h : V \times V \to K$ that is **sesquilinear**, linear in the first variable and conjugate-linear in the second,

$$
h(x + x', y) = h(x,y) + h(x',y), \quad h(\lambda x, y) = \lambda\, h(x,y), \quad h(x, \lambda y) = \bar{\lambda}\, h(x,y) ,
$$

and **Hermitian**, $h(x,y) = \overline{h(y,x)}$; it is **symmetric** when $\sigma = \mathrm{id}$ and the Hermitian condition is the symmetry, and **alternating** when $h(x,x) = 0$ throughout, a case that occurs only in characteristic two for the nontrivial involution.

**Proposition.** In a basis of $V$ a Hermitian form is represented by a matrix $H$ with

$$
h(x,y) = x^{*}\, H\, y , \qquad H^{*} = H , \qquad (H^{*})_{ij} = \overline{H_{ji}} ,
$$

where $x$ and $y$ are the coordinate columns and the star is the conjugate transpose; the Hermitian matrices form a $K_0$-subspace of $M_n(K)$, of dimension $n^2$ over $K_0$ when $K/K_0$ is quadratic and of dimension $\frac{n(n+1)}{2}$ when $\sigma = \mathrm{id}$, and the form is **nondegenerate** exactly when $H$ is invertible.

**Proof.** The sesquilinearity is the linearity in the coordinates and the conjugate-linearity in the second factor, so the form is $x^{*}Hy$; the Hermitian condition is $H^{*} = H$ because the conjugate transpose of the scalar $x^{*}Hy$ is $y^{*}H^{*}x$; the dimension over $K_0$ follows from the number of the independent entries, which is $n^2$ for each entry subject to $H_{ij} = \overline{H_{ji}}$ and $\frac{n(n+1)}{2}$ for the symmetric case; the form is nondegenerate exactly when the map $y \mapsto h(\cdot,y)$ is an isomorphism, which is the invertibility of $H$.

**Definition.** The **radical** of a Hermitian form $h$ is the subspace

$$
\operatorname{rad}(h) = \{x \in V : h(x,y) = 0 \ \text{for all } y \in V\} ,
$$

and the form is nondegenerate when the radical is zero; the **trace form** on $K$ itself is the Hermitian form $h(x,y) = x\bar{y}$ of rank one, the form of the extension, and its norm is the quadratic form $x\bar{x}$.

**Proposition.** The radical is the kernel of the adjoint map $V \to V^{*}$, $y \mapsto h(\cdot,y)$, and the form is nondegenerate exactly when the map is an isomorphism; a nondegenerate Hermitian form defines a **polarity** of the projective space, sending a subspace $W$ to its orthogonal complement $W^\perp = \{y : h(W,y) = 0\}$, which is an inclusion-reversing involution on the lattice of subspaces.

**Proof.** The radical is the kernel of the adjoint map by definition, and the isomorphism is the nondegeneracy; the orthogonality is an inclusion-reversing map of the lattice, and it is an involution because the form is Hermitian and nondegenerate, $W^{\perp\perp} = W$ by the dimension count $\dim W + \dim W^\perp = \dim V$. The statement is the standard polarity of a Hermitian form, in *Bilinear Forms* and *Projective Geometry*.

## The Unitary Group

### Definition and the Exact Sequences

**Definition.** Let $(V,h)$ be a Hermitian space. The **unitary group** is

$$
U(V,h) = \{T \in GL(V) : h(Tx, Ty) = h(x,y) \ \text{for all } x, y\} ,
$$

the group of the isometries of the form; the **general unitary group** is the group of the **similitudes**,

$$
GU(V,h) = \{T \in GL(V) : h(Tx,Ty) = \lambda(T)\, h(x,y),\ \lambda(T) \in K_0^\times\} ,
$$

and the **special unitary group** $SU(V,h) = U(V,h) \cap SL(V)$ is the subgroup of determinant one; over a real field the groups are the compact groups of the classical theory.

**Theorem.** The unitary group is a subgroup of $GL(V)$ defined by the polynomial equations $T^{*}HT = H$ in a basis, and the general unitary group sits in the exact sequence

$$
1 \longrightarrow U(V,h) \longrightarrow GU(V,h) \xrightarrow{\ \lambda\ } K_0^\times ,
$$

with $\lambda$ the similarity factor, a homomorphism whose kernel is the unitary group and whose image contains the squares of $K_0$ and the norms $N(K^\times)$; the determinant of an element of the unitary group lies in $K_0$ with norm one in the nontrivial case, so the special unitary group $SU(V,h)$ has index the group of the determinants of norm one, and the dimension of the unitary group over $K_0$ is $n^2$ in the quadratic case and $\frac{n(n-1)}{2}$ in the symmetric case.

**Proof.** The isometry condition in coordinates is $T^{*}HT = H$, which is the displayed matrix equation; the similarity factor is a homomorphism to $K_0^\times$ because the form is Hermitian and the factor is fixed by the involution, and the kernel is the unitary group. The determinant statement follows because $\det(T^{*}HT) = \overline{\det T}\det H \det T = \det H$ forces $N(\det T) = 1$ in the nontrivial case while the trivial case has no condition beyond the determinant being a square class; the dimension counts are those of the ambient matrix space minus the conditions, computed as in the previous section.

**Example (the classical unitary groups).** Over $\mathbb{C}$ with the complex conjugation and the form $\sum |x_i|^2$ the unitary group is the compact group $U(n)$, of real dimension $n^2$, and the special unitary group $SU(n)$ has dimension $n^2 - 1$; over $\mathbb{R}$ with the trivial involution and the form $\sum x_i^2$ the unitary group is the orthogonal group $O(n)$ and the special one is $SO(n)$, of dimension $\frac{n(n-1)}{2}$. The two families are the two extreme instances of the field with an involution, and the unitary geometry of this article interpolates between them.

### The Geometries of the Unitary Group

**Definition.** The **unitary geometry** is the projective space $\mathbb{P}(V)$ together with the nondegenerate Hermitian form $h$; the **Hermitian quadric** is the set of the isotropic points

$$
Q = \{[x] : h(x,x) = 0\} ,
$$

and the **unitary group** $U(V,h)$ is the operator group of the geometry, the group of the projective operators preserving the quadric and the polarity.

**Theorem.** The projective operators preserving the Hermitian quadric are exactly the projectivities induced by the general unitary group modulo the scalars, so the operator group of the unitary geometry is $GU(V,h)/K_0^\times$ acting on $\mathbb{P}(V)$; the group acts transitively on the isotropic points and preserves the polarity, and the geometry of the isotropic points is the homogeneous space of the group modulo the stabiliser of one of them.

**Proof.** A projectivity preserving the quadric preserves the polarity induced by the form and hence the form up to a scalar, which is the similarity condition; conversely a similarity preserves the quadric and the polarity. The transitivity on the isotropic points is the Witt extension theorem for the Hermitian forms, which is stated in *Hermitian Forms and Unitary Geometry*; the stabiliser of a point is the subgroup fixing a vector, and the orbit statement follows.

## The Two Kinds of Involution

**Definition.** The article distinguishes the **trivial involution**, with $K_0 = K$, from the **nontrivial involutions**, with $K_0 \subsetneq K$ of index two; in the trivial case the Hermitian forms are the symmetric bilinear forms, the unitary group is the orthogonal group, and the geometry is the orthogonal geometry of *Orthogonal Geometry and the Involution*; in the nontrivial case the Hermitian geometry is genuinely different, the isotropic cone is not a cone of a bilinear form, and the group is the unitary group of the classical theory.

**Proposition.** For a nontrivial involution the map $q(x) = h(x,x)$ is a quadratic form over $K_0$ only after the restriction of the scalars, $h(x,x) \in K_0$, and the Hermitian forms of rank $n$ correspond to the quadratic forms over $K_0$ of a special type; for the trivial involution the two notions coincide and the Hermitian form is the polar form of the quadratic form $q(x) = h(x,x)$.

**Proof.** In the nontrivial case $h(x,x) = \overline{h(x,x)}$ is fixed by the involution, so it lies in $K_0$; the polarisation of the resulting quadratic form over $K_0$ gives back the Hermitian form, and the two are in bijection; in the trivial case the situation is the classical one of a quadratic form and its polar bilinear form. The statement is the standard descent of the Hermitian forms to the fixed field, in *Quadratic Forms and Polarisation*.

**Remark (the two involutions of the corpus).** The involution of the present article sits on the **elements** of the field, and the adjoint of an operator that it induces sits on the **operators**; the two are different structures, and the article in the operator layer that pairs them is *The Adjoint under a Hermitian Pairing*. The unitary group is the group of the operators that are isometric for the pairing, while the involution on the elements alone does not produce the adjoint without the choice of the pairing; this is the distinction the conventions of the corpus record, and it is the reason the unitary geometry is placed in the `*` Theory layer and the adjoint in the `*` Operator Theory layer.

## Summary

A field with an involution $(K,\sigma)$ has a fixed field $K_0$, equal to $K$ for the trivial involution or of index two in the nontrivial case, with the norm $N(x) = x\bar{x}$ and the trace $x + \bar{x}$ landing in $K_0$. A Hermitian form is a sesquilinear form with $h(x,y) = \overline{h(y,x)}$, represented in a basis by a matrix with $H^{*} = H$, nondegenerate when $H$ is invertible, with the radical as the kernel of the adjoint map and with the polarity $W \mapsto W^\perp$ on the lattice of the subspaces. The unitary group $U(V,h)$ is the isometry group of the form, the general unitary group $GU$ is the group of the similitudes with the factor $\lambda \in K_0^\times$, and the special unitary group $SU$ is the determinant-one subgroup; over $\mathbb{C}$ and $\mathbb{R}$ the groups are the classical $U(n)$, $SU(n)$, $O(n)$ and $SO(n)$ with the dimensions $n^2$, $n^2-1$ and $\frac{n(n-1)}{2}$. The unitary geometry is the projective space with the Hermitian quadric of the isotropic points, and its operator group is the general unitary group modulo the scalars; the trivial involution recovers the orthogonal geometry, and the classification of the forms and the Witt theorem are *Hermitian Forms and Unitary Geometry* and, over a local field, *Hermitian Spaces over a Local Field*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(K,\sigma)$ | Field with involution |
| $\bar{x} = \sigma(x)$ | Conjugation of a coefficient |
| $K_0 = K^\sigma$ | Fixed field |
| $N(x) = x\bar{x}$, $\operatorname{Tr}(x) = x + \bar{x}$ | Norm and trace to $K_0$ |
| $h(x,y) = \overline{h(y,x)}$ | Hermitian form |
| $H^{*} = H$, $(H^{*})_{ij} = \overline{H_{ji}}$ | Hermitian matrix condition |
| $\operatorname{rad}(h)$ | Radical of the form |
| $W^\perp = \{y : h(W,y) = 0\}$ | Orthogonal complement, the polarity |
| $U(V,h)$ | Unitary group (isometries) |
| $GU(V,h)$, $SU(V,h)$ | General unitary (similitudes) and special unitary groups |
| $Q = \{[x] : h(x,x) = 0\}$ | Hermitian quadric of the isotropic points |
| $GU/K_0^\times$ | Operator group of the unitary geometry |

## Further Reading

- Nathan Jacobson, *Lectures in Abstract Algebra*, vol. 1 (Van Nostrand, 1951), for the fields with involution and the Hermitian forms.
- Tsit Yuen Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the Hermitian and the sesquilinear forms and the Witt theory.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the general theory of the forms over a field with involution.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the unitary and the orthogonal groups of a form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the algebras with involution and the unitary groups.
