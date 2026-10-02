
# __Hermitian Forms and Unitary Geometry__

## Introduction

A Hermitian form over a field with an involution is classified by its isometry class, and the two theorems that make the classification run are the **Witt extension theorem**, that every isometry between two subspaces of a nondegenerate space extends to an isometry of the whole space, and the **Witt cancellation theorem**, that a form may be cancelled from both sides of an isometry. From these two the classification follows in the shape the article presents: every nondegenerate form decomposes into an orthogonal sum of hyperbolic planes and an anisotropic residue, the number of the planes is the **Witt index**, and the residue is determined by the invariants of the field. The forms themselves form the **Witt group**, and the unitary group acts on the isotropic subspaces with the Witt index as the invariant of the orbit.

The article develops the orthogonal sum and the isometries, the two Witt theorems and their proofs by induction, the hyperbolic planes, the Witt index and the decomposition of a form, the classification of the forms over the real, the complex, the finite and the local fields, the Witt group with its ring structure, and the unitary geometry of the isotropic flags. The article is the classification companion of *Unitary Geometry over a Field with Involution*, which owns the definitions, and it is the general companion of *Hermitian Spaces over a Local Field*, which treats the local case with its arithmetic invariants.

The article assumes *Unitary Geometry over a Field with Involution* for the field with an involution, the Hermitian forms, the polarity and the unitary group; *Quadratic Forms and Polarisation* and *Bilinear Forms* of Part II for the forms, the orthogonal sums and the hyperbolic planes; and *Vector Spaces* of Part I for the subspace decompositions. The article owns the Witt theorems and the classification; the local arithmetic is *Hermitian Spaces over a Local Field* and *Hermitian Forms over a Local Field*, and the algebraic theory of the forms is Part II. No distance and no physics is invoked.

## Isometry, Orthogonal Sum and the Witt Theorems

### The Definitions

**Definition.** Let $(V,h)$ and $(V',h')$ be Hermitian spaces over a field $K$ with involution. An **isometry** is a linear isomorphism $T : V \to V'$ with $h'(Tx,Ty) = h(x,y)$ for all $x,y$; the spaces are **isometric** when such a $T$ exists, and the isometry class is the class of the form. The **orthogonal sum** of two Hermitian spaces is the direct sum $V \perp V'$ with the form $h \perp h'$ vanishing between the summands, and a subspace $W \subseteq V$ is **nondegenerate** when the restriction of $h$ to $W$ is nondegenerate, equivalently when $V = W \perp W^\perp$.

**Definition.** A **hyperbolic plane** is the two-dimensional space with the form, in a basis $(e,f)$,

$$
h(e,e) = h(f,f) = 0, \qquad h(e,f) = 1 ,
$$

written $\mathbb{H}$; a vector $x$ is **isotropic** when $h(x,x) = 0$ and **anisotropic** otherwise, and a subspace is **totally isotropic** when the restriction of the form to it vanishes. The **Witt index** of a nondegenerate form is the largest dimension of a totally isotropic subspace.

**Proposition.** A hyperbolic plane contains exactly two isotropic lines, they are the lines of $e$ and $f$, and the form pairs them; the orthogonal complement of an isotropic line in a hyperbolic plane is the other isotropic line, and a nondegenerate form is hyperbolic when it is an orthogonal sum of hyperbolic planes. Every isotropic vector of a nondegenerate space lies in a hyperbolic plane: the Witt index is the number of the planes in the decomposition of the next subsection.

**Proof.** The two isotropic lines are the solutions of $h(x,x) = 0$ in the two-dimensional space, which in the coordinates $(s,t)$ is the equation $2st = 0$ over a field of characteristic not two, giving the two coordinate lines; the form pairs them by $h(e,f) = 1$. If $x$ is isotropic then the nondegeneracy gives a vector $y$ with $h(x,y) \neq 0$, and after the scaling the span of $x$ and $y$ is a hyperbolic plane with $x$ and $y$ as the pair.

**Theorem (Witt extension).** Let $(V,h)$ be a nondegenerate Hermitian space and let $T : W \to W'$ be an isometry between two subspaces. Then $T$ extends to an isometry of $V$, that is, there is an element of the unitary group $U(V,h)$ whose restriction to $W$ is $T$; the restriction of the form to $W$ is then isometric to its restriction to $W'$, and the two subspaces are carried to each other by the unitary group.

**Proof sketch.** The theorem is proved by induction on the dimension of $W$. For a one-dimensional nondegenerate $W$ the form is determined by the value $h(x,x)$ and the extension is the Witt extension of a single vector, which the nondegeneracy provides by an orthogonal reflection; for a degenerate $W$ the induction is applied to the radical and to a complement, the isometry being split along the direct sum. The classical proof and the two lemmas are in *Quadratic Forms and Polarisation* and in the references; the statement is quoted here as the engine of the classification.

**Theorem (Witt cancellation).** Let $(V_1,h_1)$, $(V_2,h_2)$ and $(W,g)$ be nondegenerate Hermitian spaces with $V_1 \perp W$ isometric to $V_2 \perp W$; then $V_1$ is isometric to $V_2$,

$$
V_1 \perp W \ \cong\ V_2 \perp W \quad \Longrightarrow \quad V_1 \cong V_2 .
$$

**Proof sketch.** The isometry of the sums is an isometry between two subspaces of the common space, and the Witt extension theorem applied to the subspace $W$ in the two copies gives the extension to the whole space; the orthogonal complement of $W$ in either sum is $V_1$ or $V_2$, and the extension carries one to the other. The statement is the cancellation theorem of *Quadratic Forms and Polarisation*.

## The Classification

### The Decomposition and the Witt Index

**Theorem (the decomposition).** Let $(V,h)$ be a nondegenerate Hermitian space of dimension $n$ over a field of characteristic not two. Then $V$ decomposes as

$$
V = \mathbb{H}_1 \perp \cdots \perp \mathbb{H}_r \perp V_0 ,
$$

an orthogonal sum of $r$ hyperbolic planes and an **anisotropic** subspace $V_0$ (one containing no isotropic vector), of dimension $n - 2r$; the number $r$ is the Witt index, it is the same for every such decomposition by the Witt cancellation theorem, and the isometry class of the whole space is determined by the number $r$ and the isometry class of the anisotropic residue $V_0$.

**Proof.** If $V$ contains an isotropic vector then the proposition gives a hyperbolic plane $\mathbb{H} \subset V$, and $V = \mathbb{H} \perp \mathbb{H}^\perp$ because the plane is nondegenerate; the induction on the dimension applied to $\mathbb{H}^\perp$ gives the decomposition. The uniqueness of $r$ is the Witt cancellation: two decompositions give $r_1$ and $r_2$ planes and the residues, and cancelling the planes one by one forces the two residues to be isometric and the numbers to be equal. The statement is in *Quadratic Forms and Polarisation*.

**Corollary (the unitary group and the isotropic flags).** The unitary group $U(V,h)$ acts transitively on the totally isotropic subspaces of each dimension $k \leq r$, so the **isotropic Grassmannian** of the $k$-dimensional totally isotropic subspaces is the homogeneous space $U(V,h)/P_k$ of the unitary group modulo the stabiliser $P_k$ of one of them; the Witt index $r$ is the largest $k$ for which the Grassmannian is nonempty, and the maximal totally isotropic subspaces form the single orbit of the maximal parabolic.

**Proof.** Two totally isotropic subspaces of the same dimension are isometric by an isometry sending a basis to a basis, and the Witt extension theorem extends the isometry to the whole space, giving an element of the unitary group carrying one to the other; the stabiliser of a subspace in the unitary group is the subgroup preserving it, and the orbit-stabiliser identification is the standard one. The statement is the geometric form of the Witt theorem, and it is in *Quadratic Forms and Polarisation* and *Unitary Geometry over a Field with Involution*.

### The Classification over the Standard Fields

**Theorem (over $\mathbb{R}$).** A nondegenerate Hermitian form over $\mathbb{R}$ with the trivial involution is a symmetric bilinear form and is classified by its **signature** $(p,q)$ with $p + q = n$, the numbers of the positive and the negative eigenvalues; the Witt index is $\min(p,q)$ and the anisotropic residue is the positive-definite space of dimension $|p-q|$. The Hermitian forms over $\mathbb{C}$ with the complex conjugation are classified by the signature as well, by the spectral theorem for the Hermitian matrices.

**Proof.** Sylvester's law of inertia shows that the form is diagonalisable with the eigenvalues reduced to their signs and the number of the positive ones is an invariant; over $\mathbb{C}$ with the conjugation the same argument applies to the Hermitian matrices by the spectral theorem. The statement is in *Quadratic Forms and Polarisation* and *Self-Adjoint Operators and the Spectral Theorem*.

**Theorem (over $\mathbb{C}$ with the trivial involution and over an algebraically closed field).** Every nondegenerate symmetric bilinear form over an algebraically closed field of characteristic not two is hyperbolic in an even dimension and is the orthogonal sum of a hyperbolic plane and a one-dimensional form in an odd dimension; the classification is by the rank alone, and the Witt index is $\lfloor n/2 \rfloor$.

**Proof.** The Gram–Schmidt argument diagonalises the form, and each diagonal entry is a square in an algebraically closed field, so it may be scaled to $1$; the form $\sum x_i^2$ in dimension $n$ is, after a change of basis $e_i = (u_i + u_{i+1})/2$, the sum of the hyperbolic planes in the even part and one unit vector in the odd part. The statement is in *Quadratic Forms and Polarisation*.

**Theorem (over a finite field and a local field).** Over a finite field of odd characteristic a nondegenerate form is classified by its dimension and its **discriminant**, the Hasse invariant being determined by the two; over a non-Archimedean local field the classification is by the rank, the discriminant and the Hasse invariant, and the invariants determine the Witt index and the anisotropic residue, whose dimension is at most two.

**Proof.** The classification over a finite field is the counting of the isometry classes by the discriminant and the parity of the dimension; the local statement is the local classification theorem with the Witt cancellation, and the anisotropic residue has dimension at most two because every form of dimension three over a local field is isotropic. The statement is in *Quadratic Forms and Polarisation* and in *Hermitian Spaces over a Local Field*.

**Remark (the invariants are not the eigenvalues).** Over a general field the invariant is not the signature, which requires an order, but the class of the form in the Witt group of the next section; the discriminant and the Hasse invariant are the arithmetic shadows of that class, and they are complete over the local and the finite fields but not over a general field. The article records the standard cases and defers the general classification to the Witt group.

## The Witt Group

**Definition.** The **Witt group** $W(K,\sigma)$ of a field with an involution is the Grothendieck group of the isometry classes of the nondegenerate Hermitian forms under the orthogonal sum, modulo the subgroup generated by the hyperbolic forms: two forms are equal in $W(K,\sigma)$ when they become isometric after the addition of hyperbolic planes, and the sum is the orthogonal sum. For the trivial involution the group is written $W(K)$ and called the **Witt group of the quadratic forms**.

**Theorem.** The Witt group is an abelian group under the orthogonal sum, and the tensor product of the forms, $h \otimes h'$ on $V \otimes V'$ with the involution acting on the two factors, makes it a commutative ring with unit the one-dimensional form $h(x,y) = x\bar y$; the classes of the forms of dimension one generate the group over a field, and the hyperbolic forms are exactly the classes of the zero in the quotient.

**Proof.** The orthogonal sum is associative and commutative, the zero form is the unit for the sum up to the hyperbolic classes, and the inverse of a form is its negative, the form with $h$ replaced by $-h$; the tensor product is compatible with the sum and the isometry, so it descends to the quotient, and the one-dimensional form is the multiplicative unit. The statement is the classical ring structure of the Witt group, in *Quadratic Forms and Polarisation*.

**Example (the standard Witt groups).** Over $\mathbb{R}$ the Witt group $W(\mathbb{R})$ is $\mathbb{Z}$, with the class of a form the signature and the hyperbolic forms the kernel; over $\mathbb{C}$ the Witt group is $\mathbb{Z}/2$ generated by the one-dimensional form; over a finite field $\mathbb{F}_q$ of odd characteristic the Witt group is $\mathbb{Z}/2 \oplus \mathbb{Z}/2$ when $q \equiv 1 \pmod 4$ and $\mathbb{Z}/4$ when $q \equiv 3 \pmod 4$, the class being decided by the dimension and the discriminant; and over a local field the group is finite, detected by the discriminant and the Hasse invariant.

**Proof.** The signature is additive under the orthogonal sum and vanishes on the hyperbolic forms, and every form is determined by its signature, giving the isomorphism $W(\mathbb{R}) \cong \mathbb{Z}$; over $\mathbb{C}$ every form is hyperbolic in an even dimension and the one-dimensional form generates the quotient; the finite and the local statements are the classifications of the previous section read in the group. The statement is in *Quadratic Forms and Polarisation*.

**Remark (the fundamental ideal and the higher invariants).** The Witt group carries the **fundamental ideal** of the even-dimensional forms, and the powers of the ideal give the higher invariants, the Arf and the Hasse invariants of the successive quotients; this is the algebraic theory of the quadratic forms of Part II, and the article names it as the source of the finer invariants. The Witt group of a field is the home of the classification of the forms that the present article states geometrically.

## The Unitary Geometry of the Isotropic Flags

**Definition.** Let $(V,h)$ be a nondegenerate Hermitian space of dimension $n$ and Witt index $r$. The **isotropic Grassmannian** $\mathrm{IG}_k(V)$ is the set of the $k$-dimensional totally isotropic subspaces of $V$, for $0 \leq k \leq r$; the **maximal isotropic** subspaces are the elements of $\mathrm{IG}_r(V)$, and the **isotropic flag manifold** is the set of the complete flags $0 \subset W_1 \subset \cdots \subset W_r$ of totally isotropic subspaces.

**Theorem.** The unitary group acts transitively on each isotropic Grassmannian, and the stabiliser of a totally isotropic subspace is a **parabolic** subgroup of the unitary group; the isotropic flag manifold is the quotient of the unitary group by a **Borel** subgroup, and the Weyl group of the unitary group acts on the cohomology of the flag manifold with the Schubert cells indexed by the isotropic flags. The geometry of the isotropic flags is the unitary counterpart of the projective geometry of the flags of *Operators on a Projective Space*.

**Proof.** The transitivity is the corollary of the Witt theorem; the stabilisers are the parabolics by the standard correspondence between the subgroups containing a Borel and the subsets of the simple roots, which is the Lie-theoretic structure of the unitary group, and the Schubert cell decomposition is the Bruhat decomposition of the flag manifold. The statement is in *Linear Algebraic Groups*.

**Remark (the Witt index and the geometry).** The Witt index is the invariant of the unitary geometry that the group alone sees: it is the largest dimension of the totally isotropic figures, it is the number of the hyperbolic planes, and the isotropic flags of dimension up to the index are the figures on which the unitary group acts with the parabolic stabilisers. The classification of the forms and the geometry of the unitary group are two readings of the same invariant, and the article states both.

## Summary

A Hermitian space decomposes as an orthogonal sum of hyperbolic planes and an anisotropic residue, the number $r$ of the planes is the **Witt index**, and the isometry class is determined by $r$ and by the class of the residue. The **Witt extension theorem** extends every isometry between subspaces to an isometry of the whole space, and the **Witt cancellation theorem** cancels a common summand; the two give the uniqueness of the decomposition and the transitivity of the unitary group on the totally isotropic subspaces of each dimension, so the isotropic Grassmannians are the homogeneous spaces $U(V,h)/P_k$ of the unitary group modulo the parabolics. Over the standard fields the classification is by the signature over $\mathbb{R}$ and over $\mathbb{C}$ with the conjugation, by the rank over an algebraically closed field with the trivial involution, and by the dimension and the discriminant, with the Hasse invariant, over the finite and the local fields. The isometry classes form the **Witt group** $W(K,\sigma)$, a commutative ring under the orthogonal sum and the tensor product, with $W(\mathbb{R}) \cong \mathbb{Z}$ and $W(\mathbb{C}) \cong \mathbb{Z}/2$, and the fundamental ideal carries the higher invariants. The unitary geometry of the isotropic flags is the geometric form of the classification.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V \perp V'$ | Orthogonal sum of Hermitian spaces |
| $\mathbb{H}$ | Hyperbolic plane, $h(e,e)=h(f,f)=0$, $h(e,f)=1$ |
| isotropic, anisotropic | $h(x,x)=0$; $h(x,x)\neq0$ for every nonzero $x$ |
| $r$ | Witt index, the largest dimension of a totally isotropic subspace |
| $V = \mathbb{H}_1 \perp \cdots \perp \mathbb{H}_r \perp V_0$ | Witt decomposition |
| $(p,q)$ | Signature over $\mathbb{R}$; Witt index $\min(p,q)$ |
| $W(K,\sigma)$ | Witt group of the Hermitian forms |
| $W(K)$ | Witt group of the quadratic forms (trivial involution) |
| $\mathrm{IG}_k(V)$ | Isotropic Grassmannian of the $k$-dimensional isotropic subspaces |
| $U(V,h)/P_k$ | Orbit of a totally isotropic subspace, $P_k$ a parabolic |
| isotropic flag manifold | Complete flags of isotropic subspaces, $U/B$ |

## Further Reading

- Tsit Yuen Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the Witt theorems, the Witt group and the classification.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the classification over the general fields.
- Jean-Pierre Serre, *A Course in Arithmetic* (Springer, 1973), for the forms over the finite and the local fields and the Hasse invariant.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the unitary groups and the isotropic flags.
- Armand Borel, *Linear Algebraic Groups*, 2nd ed. (Springer, 1991), for the parabolic and the Borel subgroups and the flag manifolds.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the Hermitian forms over a field with involution.
- John Milnor and Dale Husemoller, *Symmetric Bilinear Forms* (Springer, 1973), for the Witt group, the Witt ring and the invariants.
