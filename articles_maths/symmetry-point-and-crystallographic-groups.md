
# __Symmetry, Point and Crystallographic Groups__

## Introduction

A **symmetry** of a figure in Euclidean space is an isometry of the space that carries the figure to itself, and the symmetries of a figure form a group under composition. The group is the precise algebraic expression of the regularity of the figure, and the classification of the possible symmetry groups is the classification of the possible regularities: finite **point groups** for a bounded figure, and **crystallographic groups** for a figure that repeats periodically in space. The two theories are the two halves of the same problem, the subgroup structure of the Euclidean isometry group $E(n) = \mathbb{R}^n \rtimes O(n)$: a bounded figure has a finite symmetry group, which fixes a point and is therefore a finite subgroup of the orthogonal group, while a periodic figure has a symmetry group that is discrete and has compact fundamental domain, and Bieberbach's theorems reduce its study to a finite group acting on a lattice.

The subject is the meeting point of three strands of the corpus. The **distance** of Part II is what an isometry preserves, so the whole theory is a geometry of Part II and belongs to this category; the **orthogonal group** and its finite subgroups are the object of *The Rotation Group and Orientation* and *The Unitary and Symplectic Groups*, together with the classical groups as the continuous families of symmetry; and the **lattice** is the arithmetic object of *Lattices and the Quaternion Lattice* and of the theory of quadratic forms, which supplies the lattices that the crystallographic groups translate by. The classification itself is finite and classical: there are $2$ crystallographic groups on the line, $7$ frieze groups in the plane, $17$ wallpaper groups, $230$ space groups in three dimensions and $4894$ in four, and the crystallographic restriction — the only rotations compatible with a lattice are those of order $1, 2, 3, 4, 6$ — is what makes the classification finite in each dimension.

This article defines the isometry group of Euclidean space and its structure as a semidirect product; it treats the symmetry group of a figure and proves that a finite symmetry group fixes a point and is conjugate to a finite subgroup of $O(n)$; it classifies the finite subgroups of $O(2)$ and of $SO(3)$, with the dihedral and polyhedral families, their orders and their isomorphism types; it defines the lattices, the point group and the crystallographic group, and proves the crystallographic restriction; it states the Bieberbach theorems and draws their consequences for the classification and for the flat manifolds; it records the classical counts of the frieze, wallpaper and space groups and of the Bravais lattices; and it closes with the classical groups as the continuous analogue of the point groups.

The article assumes *Euclidean Geometry* for the Euclidean space, the distance, the isometries and the congruence of figures; *The Rotation Group and Orientation* and *The Unitary and Symplectic Groups* for $O(n)$, $SO(n)$ and the classical families; *Groups* and the finite group theory of Part I for the cyclic, dihedral, symmetric and alternating groups; *Lattices and the Quaternion Lattice* for the free $\mathbb{Z}$-modules and the rank; and *Topological Groups* and *Lie Groups* for a group topology and the discreteness of a subgroup. The article does not develop the structure theory of the discrete subgroups of a Lie group, the lattices in a general Lie group, their cohomology, or the rigidity and arithmetic properties: those are the subject of *Lattices in Lie Groups* and of the rest of the Topology on Groups category, written in parallel, and the crystallographic group is treated here as a subgroup of the Euclidean isometry group of Part II rather than as a lattice in a general group. The invariant measure and the averaging over a compact group, which a proof of the existence of an invariant point may use, are Part III's; the elementary proof given here uses only a finite average in a vector space. No physics is invoked.

## The Isometry Group of Euclidean Space

**Definition.** The **Euclidean isometry group** $E(n)$ is the group of all distance-preserving bijections of $\mathbb{R}^n$ with the Euclidean distance, under composition; an element is written $x \mapsto Ax + b$ with $A \in O(n)$ and $b \in \mathbb{R}^n$, and the map $(A, b) \mapsto (x \mapsto Ax + b)$ is a group isomorphism

$$
E(n) \cong \mathbb{R}^n \rtimes O(n), \qquad (A, b)(A', b') = (AA', Ab' + b),
$$

the **affine group** of Euclidean space, with the translations $\mathbb{R}^n$ as a normal subgroup and $O(n)$ the stabiliser of the origin; the **linear part** $\ell(A,b) = A$ is a homomorphism $E(n) \to O(n)$ with kernel the translations.

**Proposition.** Every isometry of $\mathbb{R}^n$ is of the form $x \mapsto Ax + b$ with $A \in O(n)$. An isometry preserves the distance, the segments, the lines, the angles and the balls, and it is the composite of a translation and an orthogonal transformation; the orientation-preserving isometries are those with $\det A = 1$, and they form the normal subgroup $\mathbb{R}^n \rtimes SO(n)$ of index $2$.

**Proof sketch.** An isometry fixes the origin after composition with a translation; an origin-fixing isometry preserves the norm, hence the inner product by the polarisation identity, hence is orthogonal. $\square$

**Definition.** The **translation subgroup** of a subgroup $\Gamma \leq E(n)$ is $\Gamma \cap \mathbb{R}^n$, the set of the elements with trivial linear part. A subgroup $\Gamma$ is **discrete** if every point of $E(n)$ has a neighbourhood meeting $\Gamma$ in finitely many points, equivalently if the identity is isolated in the relative topology; and $\Gamma$ is **cocompact** if the quotient $\mathbb{R}^n/\Gamma$ is compact.

**Example.** The group $E(1) \cong \mathbb{R} \rtimes \{\pm 1\}$ consists of the maps $x \mapsto \pm x + b$; a cyclic group of translations, the infinite dihedral group generated by a reflection and a translation, and the finite groups of order $2$ generated by a reflection are the symmetry groups of the bounded and periodic figures on the line. In the plane $E(2) \cong \mathbb{R}^2 \rtimes O(2)$ contains the rotations about arbitrary centres, the reflections in arbitrary lines, the translations and the glide reflections.

## Symmetry Groups of Figures

**Definition.** Let $F \subseteq \mathbb{R}^n$ be a figure. Its **symmetry group** is

$$
\operatorname{Sym}(F) = \{\varphi \in E(n) : \varphi(F) = F\},
$$

a subgroup of $E(n)$; its elements are the symmetries of $F$, and $\operatorname{Sym}(F)$ acts on $F$.

**Theorem.** If $F$ is bounded and nonempty then $\operatorname{Sym}(F)$ is finite, and it fixes a point: there is $c \in \mathbb{R}^n$ with $\varphi(c) = c$ for every $\varphi \in \operatorname{Sym}(F)$. Consequently every finite subgroup of $E(n)$ is conjugate to a subgroup of $O(n)$, and the finite subgroups of $E(n)$ are exactly the conjugates of the finite subgroups of $O(n)$.

**Proof.** If $F$ is bounded, its diameter $D < \infty$ is attained by a pair of points, and the group acts faithfully on the finite set of the pairs at distance $D$; the group is therefore finite. For the fixed point, choose $x \in \mathbb{R}^n$ and let

$$
c = \frac{1}{|\operatorname{Sym}(F)|}\sum_{\varphi} \varphi(x);
$$

then for $\psi$ in the group, $\psi(c) = \frac{1}{|\Gamma|}\sum_\varphi \psi\varphi(x) = c$, since $\varphi \mapsto \psi\varphi$ permutes the group. The fixed point gives a translate of the group into $O(n)$ by conjugating with the translation $x \mapsto x - c$. $\square$

**Example (the symmetry of the regular polygon).** The symmetry group of the regular $n$-gon, $n \geq 3$, is the **dihedral group** $D_n$ of order $2n$, generated by the rotation through $2\pi/n$ and a reflection in an axis through the centre; its rotation subgroup is cyclic of order $n$. For $n = 3, 4, 6$ the group is that of an equilateral triangle, a square and a regular hexagon. The symmetry group of the circle is the full $O(2)$, infinite and continuous, which shows that the finiteness of a bounded figure's group depends on the figure and not on the boundedness alone.

**Example (the Platonic solids).** The symmetry group of the regular tetrahedron is $T_d$ of order $24$, of the cube and the regular octahedron $O_h$ of order $48$, and of the regular dodecahedron and the regular icosahedron $I_h$ of order $120$; the corresponding rotation groups are $T$, $O$, $I$ of orders $12$, $24$, $60$, and the full group is obtained from the rotation group by adjoining the reflections, the inversion being present in $O_h$ and $I_h$ but not in $T_d$. These groups are the symmetry groups of the Platonic solids, and they reappear in the section below on the finite subgroups of $SO(3)$.

## Point Groups

### Finite Subgroups of $O(2)$

**Theorem.** A finite subgroup of $O(2)$ is one of the following.

**(a)** A **cyclic group** $C_n$ of order $n$, the rotation group generated by the rotation through $2\pi/n$, for $n \geq 1$; it consists of the rotations and contains no reflection.

**(b)** A **dihedral group** $D_n$ of order $2n$, generated by the rotation through $2\pi/n$ and one reflection, for $n \geq 2$; it contains $n$ rotations and $n$ reflections, and as an abstract group it is the semidirect product $C_n \rtimes C_2$.

These are the two **rosette groups**, and every finite subgroup of $O(2)$ is of one of the two types.

**Proof sketch.** The determinant is a homomorphism $O(2) \to \{\pm 1\}$; the rotation part of a finite subgroup is cyclic, generated by a rotation of minimal angle, and if a reflection is present, the conjugate of every rotation by that reflection is the inverse rotation, so the subgroup is determined by its order and the type. $\square$

### Finite Subgroups of $SO(3)$

**Theorem (the polyhedral classification).** A finite subgroup of $SO(3)$ other than the trivial group is one of the following.

**(a)** The **cyclic group** $C_n$ of order $n$, the rotations about a fixed axis.

**(b)** The **dihedral group** $D_n$ of order $2n$, the rotation group of a regular $n$-gonal prism, for $n \geq 2$.

**(c)** The **tetrahedral group** $T \cong A_4$ of order $12$, the rotation group of the regular tetrahedron.

**(d)** The **octahedral group** $O \cong S_4$ of order $24$, the rotation group of the cube and of the regular octahedron.

**(e)** The **icosahedral group** $I \cong A_5$ of order $60$, the rotation group of the regular dodecahedron and of the regular icosahedron.

**Proof sketch.** Let $G \leq SO(3)$ be finite and nontrivial. Each non-identity element is a rotation about an axis, and a finite group of rotations acts on the set of the poles — the points where an axis meets the unit sphere — with the orbits of size $|G|/|\text{stabiliser}|$. Counting incidences between the group elements and the pairs of poles gives the equation

$$
2 - \frac{2}{|G|} = \sum_{\text{orbits}} \left(1 - \frac{1}{m_i}\right),
$$

where $m_i$ is the order of the stabiliser of a pole in the $i$-th orbit. Since the left side is less than $2$, the number of orbits is $2$ or $3$; the case of $2$ orbits gives (a) or (b) according to the orders, and the case of $3$ gives the solutions $(2,2,m)$ with $m$ arbitrary, leading to the dihedral family, and the accidental solutions $(2,3,3)$, $(2,3,4)$, $(2,3,5)$, of orders $12$, $24$, $60$, which are (c), (d), (e). $\square$

**Remark (the double covers).** The preimage of a finite subgroup of $SO(3)$ under the double cover $SU(2) \to SO(3)$, or equivalently under $Sp(1) \to SO(3)$ inside the unit quaternions, is a finite subgroup of $Sp(1)$ of twice the order: the binary cyclic, binary dihedral and **binary polyhedral** groups $2T$, $2O$, $2I$ of orders $24$, $48$, $120$. These are the finite subgroups listed in *The Rotation and Reflection Groups in the Biquaternion Algebra*, where the $8$ Lipschitz and $24$ Hurwitz units and the binary tetrahedral group are computed, and the double cover is the source of the spin structures of the corpus.

### The Point Groups in Two and Three Dimensions

**Definition.** A **point group** is a finite subgroup of $O(n)$; it is a **crystallographic point group** if it is the point group of a crystallographic group in the sense of the section below on the crystallographic groups, that is, if it preserves a lattice.

**Theorem.** In two dimensions there are exactly $10$ crystallographic point groups: the cyclic $C_1, C_2, C_3, C_4, C_6$, the dihedral $D_1, D_2, D_3, D_4, D_6$ in the notation of the rosette groups, where $D_1$ means the reflection group of order $2$; the cyclic groups of other orders and the dihedral groups of other orders are point groups but not crystallographic point groups. In three dimensions there are exactly $32$ crystallographic point groups.

**Proof sketch.** The crystallographic restriction of §the crystallographic groups restricts the orders of the rotations that preserve a lattice to $1, 2, 3, 4, 6$, and a case check over the two-dimensional Bravais lattices gives the $10$ groups; in three dimensions the same restriction with the possible axes and their relative angles gives the $32$ groups, a classical enumeration. $\square$

**Example (the icosahedral exception).** The icosahedral group $I$ of order $60$ and the dihedral group $D_5$ of order $10$ are point groups but not crystallographic point groups: the fivefold rotation cannot preserve a lattice, and the icosahedral symmetry is realised in a quasicrystal only by an aperiodic structure with no lattice of translations. This is the phenomenon that makes the crystallographic restriction a genuine restriction rather than a technicality.

## Lattices and Crystallographic Groups

**Definition.** A **lattice** in $\mathbb{R}^n$ is a subgroup $L \leq \mathbb{R}^n$ generated by $n$ linearly independent vectors $b_1, \ldots, b_n$,

$$
L = \Bigl\{\sum_{i} m_i b_i : m_i \in \mathbb{Z}\Bigr\} ;
$$

the vectors $b_i$ are a **basis**, the integer matrix of the change of basis between two bases has determinant $\pm 1$, and the lattice is discrete, of rank $n$, with $\mathbb{R}^n / L$ a torus. The **point group** of a lattice is its symmetry group $\operatorname{Sym}(L) \leq O(n)$, the finite subgroup of the orthogonal transformations preserving $L$.

**Definition.** A **crystallographic group** in dimension $n$ is a subgroup $\Gamma \leq E(n)$ that is discrete as a subgroup of $E(n)$ and cocompact, that is, the quotient $\mathbb{R}^n/\Gamma$ is compact. Its **translation subgroup** is $T_\Gamma = \Gamma \cap \mathbb{R}^n$, its **point group** is the image $P = \ell(\Gamma) \leq O(n)$ of $\Gamma$ under the linear-part homomorphism, and the sequence

$$
1 \to T_\Gamma \to \Gamma \to P \to 1
$$

is exact; the quotient is the point group. A crystallographic group is **torsion-free** if it contains no element of finite order other than the identity; the torsion-free crystallographic groups are the fundamental groups of the compact flat manifolds, and $T_\Gamma = \Gamma$ exactly when $\Gamma$ is a pure lattice of translations. The two conditions are not the same: the Klein bottle group is torsion-free with point group of order two and translation subgroup of index two.

**Theorem (Bieberbach's first two theorems).** For a crystallographic group $\Gamma \leq E(n)$, the translation subgroup $T_\Gamma$ is a lattice of rank $n$ in $\mathbb{R}^n$, and the point group $P$ is finite. Moreover $P$ acts faithfully on $T_\Gamma$, and the group $\Gamma$ is a finite extension of the lattice $T_\Gamma$.

**Proof sketch.** The discreteness of $\Gamma$, read on the compact quotient, forces the linear parts of the elements to form a discrete subgroup of the compact group $O(n)$, hence to be finite; the translations among the elements are then shown to generate a lattice of full rank by bounding the set of the translations modulo $T_\Gamma$, using the fact that a bounded region of $\mathbb{R}^n$ meets $\Gamma$ in finitely many points, and the extension statement follows from the exact sequence. $\square$

**Theorem (Bieberbach's third theorem).** Two crystallographic groups in dimension $n$ are isomorphic as abstract groups if and only if they are conjugate in the affine group $\operatorname{Aff}(n) = \mathbb{R}^n \rtimes GL(n, \mathbb{R})$; in particular the crystallographic groups in each dimension are finitely many up to conjugacy, hence in finitely many isomorphism classes.

**Theorem (the crystallographic restriction).** Let $\Gamma \leq E(n)$ be a crystallographic group and let $A \in P \leq O(n)$ be the linear part of an element of finite order $k$; then

$$
2\cos(2\pi/k) \in \mathbb{Z}, \qquad \text{hence } k \in \{1, 2, 3, 4, 6\}.
$$

**Proof.** Choose a basis of the lattice $T_\Gamma$ and write $A$ as a matrix with integer entries; the trace of an integer matrix is an integer, and the eigenvalues of the orthogonal transformation $A$ on the invariant plane of the rotation are $e^{\pm 2\pi i/k}$, so $\operatorname{tr} A = 1 + 2\cos(2\pi/k)$ in dimension three and $2\cos(2\pi/k)$ in dimension two; in either case $2\cos(2\pi/k)$ is an integer. Since $-2 \leq 2\cos(2\pi/k) \leq 2$, the integer is one of $-2, -1, 0, 1, 2$, giving $k \in \{2, 3, 4, 6\}$ and, adding $k = 1$, the five possibilities. $\square$

**Corollary.** A fivefold, sevenfold or higher rotation cannot preserve a lattice; the only rotational symmetries of a periodic plane figure or of a crystal in three dimensions have orders $2$, $3$, $4$ and $6$.

**Example (the tiling and the torus).** The group generated by the translations by the standard basis of $\mathbb{Z}^n$ and the reflections in the coordinate hyperplanes is crystallographic with point group $(\mathbb{Z}/2)^n$ and quotient the $n$-torus with the orbifold structure of the cube; the corresponding wallpaper group is $pmm$ and the space group $Pmmm$ in the standard notation, the point group being the group of order $2^n$ generated by the reflections and not the larger group $4mm$ of $p4m$. The torsion-free groups give the compact flat manifolds: for $n = 2$ the only two are the torus and the Klein bottle, and for $n = 3$ there are exactly ten.

## The Classical Counts

**Theorem (the classification).** Up to conjugacy in the affine group there are

| Dimension | Crystallographic groups | Bravais lattices | Crystallographic point groups |
|---|---|---|---|
| $1$ | $2$ | $1$ | $2$ |
| $2$ | $17$ | $5$ | $10$ |
| $3$ | $230$ | $14$ | $32$ |
| $4$ | $4894$ | $64$ | $227$ |

The two groups in dimension one are the infinite cyclic group of the translations and the infinite dihedral group; the $17$ in dimension two are the **wallpaper groups**, classified by Fedorov and by Pólya; the $230$ in dimension three are the **space groups**, classified by Fedorov, Schoenflies and Barlow; the $7$ groups of the frieze, the symmetry groups of a band pattern that are discrete in one direction and bounded in the other, are a subfamily of the wallpaper groups of the strip. The point groups count is $10$ and $32$ in dimensions two and three, and the Bravais lattices $5$ and $14$, the number of the lattices up to the equivalence of the holohedral point groups.

**Remark (the naming of the wallpaper groups).** Each wallpaper group carries the standard four-symbol name of the crystallographic notation, encoding the lattice and the glide and reflection elements; each space group carries the international short symbol of the Hermann–Mauguin system, and the correspondence between the $230$ symbols is the content of the tables of crystallography. The classification is finite because the crystallographic restriction bounds the rotational orders and the lattice theory bounds the shapes, and the enumeration is a case check that no longer needs the geometry once the two bounds are known.

**Remark (the orbifold quotient).** The quotient $\mathbb{R}^n/\Gamma$ is a compact flat **orbifold**, with the singularities at the fixed points of the elements of finite order; when $\Gamma$ is torsion-free the quotient is a compact flat Riemannian manifold, of the kind studied in *Riemannian Geometry*, and the correspondence between the torsion-free crystallographic groups and the compact flat manifolds is a consequence of Bieberbach's theorems. The flat manifolds are rigid in the sense of the theorem, and the classification of the torsion-free crystallographic groups in dimension three gives the ten flat three-manifolds, of which the torus and the Klein bottle in dimension two are the models.

## The Classical Groups as Continuous Symmetry

**Definition.** The **classical groups** $O(n)$, $U(n)$ and $Sp(2n)$ are the groups of the linear transformations preserving, respectively, a positive definite symmetric form, a positive definite Hermitian form and a nondegenerate alternating form; they are the continuous analogues of the point groups, the point groups being their finite subgroups that preserve a lattice.

**Theorem (the pattern).** The classification of the finite subgroups of $SO(3)$ is the finite counterpart of the classification of the compact connected groups: $SO(3)$ contains the circle $SO(2)$ as a maximal connected subgroup, the dihedral and polyhedral groups are its finite subgroups, and the passage from the finite to the continuous case replaces the enumeration by the classification of the forms, the definite symmetric forms giving $O(n)$ and $SO(n)$, the Hermitian forms $U(n)$ and $SU(n)$, and the alternating forms $Sp(2n)$. The sphere $S^{n-1}$ is the homogeneous space $O(n)/O(n-1)$ of *Homogeneous Spaces*, and the finite symmetry groups of a figure in the sphere are the finite subgroups of the stabiliser of a point.

**Proof sketch.** The classification of the finite subgroups is the case check of the polyhedral theorem; the continuous statement is the determination of the forms fixed by a compact group, and the transitive action on the sphere is the orbit-stabiliser theorem applied to the unit vector. $\square$

**Example (the symmetry of the icosahedron and the exceptional groups).** The icosahedral group $I \cong A_5$ is the finite group of the regular icosahedron, and the corresponding continuous family $H_3$ of the Coxeter classification is the noncrystallographic exception among the finite reflection groups; its failure to preserve a lattice is the crystallographic restriction again. The finite subgroups of $Sp(1) \cong SU(2)$ of orders $24$, $48$ and $120$ are the binary polyhedral groups, and the finite subgroups of $SO(4)$ obtained from the two-sided action include the symmetry groups of the regular polytopes in four dimensions.

## Summary

The isometry group of Euclidean space is the semidirect product $E(n) = \mathbb{R}^n \rtimes O(n)$, whose elements are the maps $x \mapsto Ax + b$; the symmetry group of a figure is the subgroup of $E(n)$ preserving it. A bounded figure has a finite symmetry group, which fixes a point, so the finite subgroups of $E(n)$ are the conjugates of the finite subgroups of $O(n)$. The finite subgroups of $O(2)$ are the cyclic and dihedral groups, the rosette groups; those of $SO(3)$ are the cyclic, dihedral, tetrahedral, octahedral and icosahedral groups of orders $n$, $2n$, $12$, $24$, $60$, isomorphic to $C_n$, $D_n$, $A_4$, $S_4$, $A_5$; their double covers in $Sp(1)$ are the binary polyhedral groups of orders $24$, $48$, $120$.

A lattice in $\mathbb{R}^n$ is a discrete subgroup of full rank; a crystallographic group is a discrete cocompact subgroup $\Gamma \leq E(n)$, its translation subgroup is a lattice, its point group the finite linear part, and the sequence $1 \to T_\Gamma \to \Gamma \to P \to 1$ is exact. Bieberbach's theorems state that the translation subgroup is a lattice of rank $n$, that the point group is finite, that the isomorphism class determines the conjugacy class in the affine group, and that there are finitely many such groups in each dimension. The crystallographic restriction, proved by the integrality of the trace, allows only the rotation orders $1, 2, 3, 4, 6$; consequently there are $2$, $17$, $230$ and $4894$ crystallographic groups in dimensions $1$ to $4$, with $17$ wallpaper groups, $230$ space groups, $10$ and $32$ crystallographic point groups and $5$ and $14$ Bravais lattices in dimensions two and three. The quotient $\mathbb{R}^n/\Gamma$ is a compact flat orbifold, a flat manifold when $\Gamma$ is torsion-free. The classical groups $O(n)$, $U(n)$ and $Sp(2n)$ are the continuous symmetry groups of the forms, of which the point groups are the finite lattice-preserving subgroups; the general theory of the discrete subgroups of a Lie group is the neighbouring subject of *Lattices in Lie Groups*, written in parallel, and the crystallographic group is treated here as a subgroup of the Euclidean isometry group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E(n) = \mathbb{R}^n \rtimes O(n)$ | Euclidean isometry group; $x \mapsto Ax + b$ |
| $\ell(A,b) = A$ | Linear part; homomorphism onto $O(n)$ |
| $\operatorname{Sym}(F)$ | Symmetry group of the figure $F$ |
| $C_n$, $D_n$ | Cyclic and dihedral groups; rosette and point groups |
| $T$, $O$, $I$ | Tetrahedral, octahedral, icosahedral rotation groups; orders $12$, $24$, $60$ |
| $T_d$, $O_h$, $I_h$ | Full symmetry groups of the Platonic solids; orders $24$, $48$, $120$ |
| $2T$, $2O$, $2I$ | Binary polyhedral groups in $Sp(1)$; orders $24$, $48$, $120$ |
| $L$, $b_1,\ldots,b_n$ | Lattice in $\mathbb{R}^n$; a basis |
| $\Gamma \leq E(n)$ | Crystallographic group; discrete and cocompact |
| $T_\Gamma = \Gamma \cap \mathbb{R}^n$ | Translation subgroup; a lattice of rank $n$ |
| $P = \ell(\Gamma)$ | Point group; finite subgroup of $O(n)$ |
| $2\cos(2\pi/k) \in \mathbb{Z}$ | Crystallographic restriction; $k \in \{1,2,3,4,6\}$ |
| $\mathbb{R}^n/\Gamma$ | Compact flat orbifold; flat manifold if $\Gamma$ is torsion-free |
| $O(n)$, $U(n)$, $Sp(2n)$ | Classical groups; continuous symmetry of the forms |

## Further Reading

- Ludwig Bieberbach, "Über die Bewegungsgruppen der Euklidischen Räume I, II", *Mathematische Annalen* 70 (1911), 297–336, and 72 (1912), 400–412, for the three theorems on the crystallographic groups.
- J. J. Burckhardt, *Die Bewegungsgruppen der Kristallographie* (Birkhäuser, 2nd edition, 1966), for the classification of the crystallographic groups and the counting.
- Harold S. M. Coxeter, *Regular Polytopes* (Dover, 3rd edition, 1973), for the finite subgroups of the orthogonal groups and the polyhedral symmetry.
- John Conway, Olaf Delgado Friedrichs, Daniel H. Huson and William P. Thurston, "On three-dimensional space groups", *Beiträge zur Algebra und Geometrie* 42 (2001), 475–507, for the modern treatment of the $230$ space groups and the orbifold enumeration.
- Ludwig Bieberbach and Issai Schur, "Über die Minkowskische Reduktionstheorie der positiven quadratischen Formen", *Mathematische Annalen* 87 (1922), 1–13, for the Bravais lattices and the reduction theory.
- A. L. Onishchik and E. B. Vinberg, *Lie Groups and Algebraic Groups* (Springer, 1990), for the classical groups and the discrete subgroups of the Euclidean and affine groups.
- Barry Simon, *Representations of Finite and Compact Groups* (American Mathematical Society, 1996), for the parallel between the finite point groups and the compact classical groups.
