
# __Hermitian Spaces over a Local Field__

## Introduction

A local field is a field complete in a nontrivial absolute value and locally compact, and over such a field a Hermitian space carries a geometry that combines the unitary geometry of an involution with the topology of the field: the unitary group is a locally compact group, the lattices over the ring of integers form the vertices of a building, and the invariants of the form — the rank, the discriminant and the Hasse invariant — organise the isotropic subspaces and the compact subgroups. The article develops the local Hermitian space in the **involution on the elements** layer of this Part, with the classification read geometrically: the invariants of the form are the invariants of the building and of the isotropic flags, and the unitary group is the group of the geometry. The arithmetic of the forms is *Hermitian Forms over a Local Field*, and the article owns the geometric reading over the local field.

The article develops the local fields with an involution, the Hermitian spaces and their invariants, the unitary group as a locally compact group with its maximal compact subgroups, the lattice theory over the ring of integers and the Bruhat–Tits building whose apartments are the maximal split subspaces, and the isotropic flags as the homogeneous spaces of the unitary group. The classification theorem of the local forms is stated and read geometrically; its proof and the local class field theory of the Hasse invariant are *Hermitian Forms over a Local Field* and *Local Fields*.

The article assumes *Unitary Geometry over a Field with Involution* and *Hermitian Forms and Unitary Geometry* for the Hermitian forms, the Witt theorem and the classification over a general field; *Local Fields* and *Hermitian Forms over a Local Field* for the local classification and the Hasse invariant; and *Buildings and Tits Systems* and *Bruhat–Tits Theory* for the buildings, the lattices and the maximal compact subgroups, earlier in the corpus. The article owns the geometric reading of the local Hermitian space. No distance beyond the local absolute value and no physics is invoked.

## Local Fields with an Involution

### The Local Fields

**Definition.** A **local field** is a field $K$ with a nontrivial absolute value $|\cdot|$ for which $K$ is complete and locally compact; the local fields are the real numbers $\mathbb{R}$, the complex numbers $\mathbb{C}$, the finite extensions of the $p$-adic numbers $\mathbb{Q}_p$, and the finite extensions of the Laurent series field $\mathbb{F}_p((t))$. A local field is **Archimedean** when it is $\mathbb{R}$ or $\mathbb{C}$ and **non-Archimedean** otherwise; a non-Archimedean local field has the **ring of integers**

$$
\mathcal{O}_K = \{x \in K : |x| \leq 1\} ,
$$

a discrete valuation ring with the unique maximal ideal $\mathfrak{p} = \{x : |x| < 1\}$ and the finite residue field $k = \mathcal{O}_K/\mathfrak{p}$.

**Theorem.** A local field carries only the identity involution, except when it is a quadratic extension $K/K_0$ of a local field $K_0$, in which case the nontrivial element of the Galois group is an involution; consequently the local Hermitian geometry is either the orthogonal geometry of the trivial involution or the unitary geometry of a quadratic extension, and the two cases behave differently over the Archimedean and the non-Archimedean fields.

**Proof.** The automorphisms of a local field are continuous by the uniqueness of the topology, and the Galois theory of a quadratic extension gives the nontrivial involution; the real and the complex fields have the identity and, for $\mathbb{C}/\mathbb{R}$, the complex conjugation. The statement is in *Local Fields* and *Involutive Local Fields*.

### The Norm and the Discriminant

**Definition.** For a quadratic extension $K/K_0$ with the conjugation $c$ the **norm** is $N(x) = x\,c(x)$ and the **trace** is $\operatorname{Tr}(x) = x + c(x)$, both landing in $K_0$; the group $N(K^\times)$ is an open subgroup of $K_0^\times$ of finite index, and the quotient $K_0^\times/N(K^\times)$ is the group of the **norm classes** of the extension.

**Theorem.** For a nondegenerate Hermitian form $H$ over a non-Archimedean local field with an involution, the **discriminant** is the class

$$
\operatorname{disc}(H) = \det(H) \in K_0^\times / N(K^\times)
$$

and the **Hasse invariant** is the sign $s(H) \in \{\pm 1\}$; two nondegenerate Hermitian forms are isometric if and only if they have the same rank, the same discriminant and the same Hasse invariant, and every compatible triple is realised. Over the real field the two invariants are replaced by the **signature** $(p,q)$, and over the complex field with the conjugation the form is classified by the signature as well.

**Proof.** The local classification is the decomposition into orthogonal hyperbolic planes and an anisotropic residue of rank at most two, and the residue is determined by the discriminant and the Hasse invariant; the Hilbert symbol of the extension gives the Hasse invariant and the norm class. The theorem and the proof are *Hermitian Forms over a Local Field*, and the article records the invariants as the data of the geometry.

## Hermitian Spaces over a Local Field

### The Space and the Invariants

**Definition.** A **Hermitian space over the local field** $(K,c)$ is a finite-dimensional $K$-vector space $V$ with a nondegenerate Hermitian form $h$; the **rank** is the dimension $n$, the **Witt index** $r$ is the largest dimension of a totally isotropic subspace, and the **residue** is the anisotropic part of the Witt decomposition $V = \mathbb{H}_1 \perp \cdots \perp \mathbb{H}_r \perp V_0$ with $\dim V_0 = n - 2r$. The space is **hyperbolic** when $n = 2r$ and **anisotropic** when $r = 0$.

**Theorem.** Over a non-Archimedean local field the anisotropic residue has dimension at most two, so the space is determined by the rank $n$, the discriminant, the Hasse invariant and the Witt index $r = \lfloor (n - \dim V_0)/2 \rfloor$ with $\dim V_0 \in \{0, 1, 2\}$; the Hasse invariant decides the existence of an isotropic vector, and the space is hyperbolic exactly when $n$ is even, the discriminant is trivial and the Hasse invariant has the split value.

**Proof.** The residue of dimension at most two is the local classification; the existence of an isotropic vector is decided by the Hasse invariant because the only anisotropic forms of rank at least three fail to exist over a non-Archimedean local field, and the hyperbolic condition is the vanishing of the residue. The statement is in *Hermitian Forms over a Local Field* and *Quadratic Forms and Polarisation*.

**Example (the Archimedean signatures).** Over $\mathbb{R}$ with the trivial involution and the form of signature $(p,q)$ the Witt index is $\min(p,q)$ and the residue is the definite space of dimension $|p-q|$; over $\mathbb{C}$ with the conjugation the form of signature $(p,q)$ behaves the same way, and the unitary group of the standard form is the compact group $U(p,q)$ of the next section. The Archimedean case is the one in which the residue may have any dimension and the metric is not discrete.

### The Isotropic Subspaces

**Theorem.** Let $(V,h)$ be a Hermitian space over the local field with Witt index $r$. The isotropic Grassmannians $\mathrm{IG}_k(V)$ for $0 \leq k \leq r$ are nonempty, the unitary group acts transitively on each, and the maximal totally isotropic subspace is unique up to the action of the unitary group with the dimension $r$; the flags of the isotropic subspaces form the homogeneous spaces $U(V,h)/P_k$ of the unitary group modulo the parabolics. Over a non-Archimedean local field the flags are the chambers and the maximal isotropic subspaces are the ends of the building of the next section.

**Proof.** The transitivity is the Witt extension theorem, valid over any field, applied to the local case; the stabilisers are the parabolics by the standard correspondence, and over the non-Archimedean field the parabolics are the stabilisers of the facets of the building. The statement is in *Hermitian Forms and Unitary Geometry* and *Bruhat–Tits Theory*.

## The Unitary Group over a Local Field

### The Locally Compact Group

**Definition.** The **unitary group** $U(V,h)$ of a Hermitian space over the local field $(K,c)$ is the group of the $K$-linear isometries of the form; it carries the topology of the convergence of the matrix entries, and it is a locally compact group, a real or complex Lie group in the Archimedean case, and a totally disconnected locally compact group in the non-Archimedean case.

**Theorem.** The unitary group over a local field is locally compact and unimodular, it acts properly on the space, and its **maximal compact subgroups** are the stabilisers of a lattice in the non-Archimedean case: a lattice $L \subseteq V$ is an $\mathcal{O}_K$-submodule of full rank, its stabiliser in $U(V,h)$ is open and compact, and it is maximal compact exactly when the lattice is **self-dual** for the form up to the discriminant; the group is compact exactly when the space is anisotropic.

**Proof.** The group is the zero set of the polynomial equations of the isometries, hence closed in $GL_n(K)$ and locally compact; the modular function is trivial because the group is unimodular as the isometry group of a form; the stabiliser of a lattice is open and compact by the discreteness of the lattice and the compactness of the associated Grassmannian, and the compactness of the whole group in the anisotropic case is the finiteness of the number of lattice classes. The statement is in *Bruhat–Tits Theory* and in the theory of the arithmetic groups.

### The Rank and the Compact Quotient

**Definition.** The **rank** of the unitary group over a non-Archimedean local field is the Witt index $r$ of the form, the dimension of the maximal split torus, or equivalently the largest dimension of a totally isotropic subspace; the **amenable radical** is the subgroup generated by the unipotent radicals of the parabolics, and the reductive quotient is the anisotropic unitary group of the residue.

**Theorem.** The maximal split torus of the unitary group has dimension the Witt index, its Weyl group is the hyperoctahedral group of the isotropic flags, and the quotient of the group by the amenable radical and the parabolic is compact; the group is anisotropic exactly when the Witt index is zero, in which case it is compact and the geometry has no isotropic figure.

**Proof.** The split torus acts by the scalars on the hyperbolic planes of the Witt decomposition, giving a torus of dimension $r$; the Weyl group permutes the planes and reverses the two isotropic lines of each, giving the hyperoctahedral group; the compactness of the quotient is the standard property of the parabolic decomposition of a reductive group over a local field, in *Bruhat–Tits Theory* and *Linear Algebraic Groups*.

## Lattices and the Bruhat–Tits Building

### The Lattices

**Definition.** Let $(V,h)$ be a Hermitian space over a non-Archimedean local field. A **lattice** is a free $\mathcal{O}_K$-submodule $L \subseteq V$ with $L \otimes_{\mathcal{O}_K} K = V$; two lattices are **homothetic** when one is a scalar multiple of the other, and the **building** of the space is the flag complex whose vertices are the homothety classes of the lattices and whose simplices are the chains of the classes with the inclusions.

**Theorem.** The Bruhat–Tits building of the unitary group is a simplicial complex of dimension $r - 1$, it is the union of the **apartments** corresponding to the maximal split tori, each apartment is a Coxeter complex of type $B_r$ or $C_r$, and the group acts on the building by simplicial automorphisms, transitively on the chambers and on the pairs of a chamber and an apartment; the building is the geometry of the parabolic subgroups, and the boundary strata are the isotropic flags.

**Proof.** The building of a reductive group over a non-Archimedean field is the flag complex of its parahoric subgroups, which for the unitary group are the stabilisers of the lattice chains; the apartments are the fixed complexes of the maximal split tori and their types are the root systems of the group; the transitivity is the Bruhat–Tits theorem. The statement is in *Buildings and Tits Systems* and *Bruhat–Tits Theory*.

### The Geometry of the Building

**Theorem.** The Bruhat–Tits building is a CAT(0) metric space, and the fixed point theorem of Bruhat–Tits holds: every bounded group of automorphisms of the building has a fixed point, so a compact subgroup of the unitary group fixes a facet of the building and lies in a parahoric subgroup. The building is homotopy equivalent to a wedge of spheres of dimension $r-1$, and the Wang and the Solomon–Tits theorems describe the finite parahoric subgroups as the stabilisers of the facets.

**Proof.** The metric of the building is the Euclidean metric on the apartments grafted along the faces, and the Bruhat–Tits fixed point theorem is the standard one; the homotopy type is that of the building of the reductive group, computed from the apartments and the Coxeter complex, and the parahoric subgroups are the stabilisers of the facets. The statement is in *Bruhat–Tits Theory* and *Buildings and Tits Systems*.

**Remark (the local Hermitian geometry).** The building is the geometry of the local Hermitian space at the level of the lattices, and the isotropic flags of the space are its boundary strata; the invariants of the form — the rank, the discriminant and the Hasse invariant — determine the rank of the building, the apartments and the compact subgroups. The present article reads the local Hermitian space geometrically, and the arithmetic of the local duality is *Hermitian Forms over a Local Field*.

## Summary

A Hermitian space over a local field $(K,c)$ is classified non-Archimedeanly by the rank, the discriminant $\operatorname{disc}(H) = \det(H) \in K_0^\times/N(K^\times)$ and the Hasse invariant $s(H) \in \{\pm 1\}$, the anisotropic residue having dimension at most two, and Archimedeanly by the signature $(p,q)$; the Witt index $r$ is the largest dimension of a totally isotropic subspace, and the unitary group acts transitively on the isotropic Grassmannians and the isotropic flags. The unitary group is a locally compact unimodular group, with the maximal compact subgroups the stabilisers of the self-dual lattices in the non-Archimedean case and the anisotropic groups compact; its rank is the Witt index, and the quotient by the amenable radical and the parabolic is compact. The lattices over the ring of integers organise the **Bruhat–Tits building**, a CAT(0) simplicial complex of dimension $r-1$ union of the apartments of the maximal split tori, on which the group acts transitively on the chambers, and the fixed point theorem relates the compact subgroups to the parahoric stabilisers. The boundary strata of the building are the isotropic flags, and the invariants of the form are the invariants of the geometry.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(K,c)$ | Local field with an involution |
| $\vert x\vert$ | Absolute value of the local field |
| $\mathcal{O}_K$, $\mathfrak{p}$ | Ring of integers and its maximal ideal |
| $N(x) = x\,c(x)$, $\operatorname{Tr}(x) = x + c(x)$ | Norm and trace to $K_0$ |
| $n$, $r$ | Rank (dimension) and Witt index |
| $V = \mathbb{H}_1 \perp \cdots \perp \mathbb{H}_r \perp V_0$ | Witt decomposition, $\dim V_0 \in \{0,1,2\}$ |
| $\operatorname{disc}(H) = \det(H)$ | Discriminant in $K_0^\times/N(K^\times)$ |
| $s(H) \in \{\pm 1\}$ | Hasse invariant |
| $(p,q)$ | Signature in the Archimedean case |
| $U(V,h)$ | Unitary group, a locally compact group |
| lattice $L$ | Full-rank $\mathcal{O}_K$-submodule |
| building | Flag complex of the homothety classes of the lattices |
| apartment | Subcomplex of a maximal split torus, a Coxeter complex |
| CAT(0) | Nonpositive-curvature metric property of the building |

## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the local fields, the norms and the Hasse invariant.
- Tsit Yuen Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the local classification and the Witt theory.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the Hermitian forms over the local fields.
- François Bruhat and Jacques Tits, "Groupes réductifs sur un corps local I", *Publications Mathématiques de l'IHÉS* **41** (1972), 5–251, for the buildings, the lattices and the parahoric subgroups.
- Kenneth S. Brown, *Buildings* (Springer, 1989), for the buildings, the apartments and the fixed point theorem.
- Jean-Pierre Serre, *Trees* (Springer, 1980), for the building of $SL_2$ and the lattice theory.
- Armand Borel, *Linear Algebraic Groups*, 2nd ed. (Springer, 1991), for the parabolics, the maximal split tori and the rank.
