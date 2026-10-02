# __The Boundary Operator of a Simplicial Complex__

## Introduction

A simplicial complex is a combinatorial object, a set of simplices closed under faces, and its homology is computed by a boundary operator that is read off the incidences of the simplices. The operator is completely explicit: on an oriented simplex it is the alternating sum of the oriented facets, so that it is a matrix of signs against the facet relation, and the identity $\partial\partial=0$ is a cancellation of the terms in pairs. This article treats that operator as an operator: it writes the boundary as the incidence matrix of the complex, computes the cycles and boundaries as the kernel and the image of a sequence of matrices, obtains the homology and the Euler characteristic from their ranks, and reads the coboundary operator of the dual complex as the transpose of the same matrix. The simplicial complex is the one instance of the boundary operator of *The Boundary Operator* in which everything can be exhibited and counted, and the counting is the reason the whole homology of the corpus is computable on a finite triangulation.

The article develops the operator in four stages. It recalls the oriented simplices and the chain modules of *Simplicial and Singular Homology* and states the boundary as a matrix; it proves the square-zero identity at the level of the incidence numbers; it treats the kernel and the image of the operator, with the rank formula for the homology, the Euler characteristic and the Smith normal form; and it treats the dual complex, whose coboundary is the transpose matrix, together with the naturality of the operator under a simplicial map and the Hopf trace formula. The invariance of the result — the agreement of the simplicial homology with the singular homology, so that the operator computes a topological invariant — is the theorem of *Simplicial and Singular Homology* and is cited; the general operator of a chain complex over a ring is that of *The Boundary Operator*; and the Smith normal form and the structure of the finitely generated modules over a principal ideal domain are those of the algebra of Part I.

Nothing analytic and nothing geometric is used. The article is finite linear algebra over a ring: incidence numbers, matrices, kernels and images, alternating sums of ranks. No distance, no norm and no measure is chosen, and the geometric realisation of the complex is used only to name the space whose homology is computed; the topology enters through the cited agreement with the singular theory. Throughout, $K$ is a simplicial complex, finite when ranks are counted, $|K|$ is its underlying space, $R$ is a commutative ring with identity $1 \neq 0$ and, when the Smith normal form is invoked, a principal ideal domain with the integers as the case of reference. The chain modules, the oriented simplices, the boundary of an oriented simplex and the agreement of the simplicial with the singular homology are those of *Simplicial and Singular Homology*, whose notation is used; the operator $\partial$ and its square-zero property are those of *The Boundary Operator*, and the concrete computations below are their simplicial realisation.

## Oriented Simplices and the Chain Modules

### Oriented Simplices

**Definition.** An $n$-simplex of $K$ with vertices $v_0,\dots,v_n$ is written $[v_0,\dots,v_n]$, and an **orientation** is an equivalence class of orderings of its vertices under even permutations; the oriented simplex is written with a chosen ordering, and a permutation acts by

$$
[v_{\pi(0)},\dots,v_{\pi(n)}] = \operatorname{sgn}(\pi)\,[v_0,\dots,v_n].
$$

The **facets** of $\sigma=[v_0,\dots,v_n]$ are the simplices $[v_0,\dots,\widehat{v_i},\dots,v_n]$ obtained by omitting one vertex, with the induced ordering; for each facet the incidence with $\sigma$ is the sign in the face formula below.

The orientation is a choice only up to sign: reversing it negates the generator of the chain module in which the simplex appears, and no total order of the vertices of $K$ is needed. When a total order is fixed, every simplex carries the induced orientation, and the signs of the boundary formula become the signs of the positions of the omitted vertices.

### The Chain Modules

**Definition.** For $n \geq 0$ the **simplicial $n$-chains** are the free $R$-module

$$
C_n(K;R) = \bigoplus_{\sigma \in K_n} R\cdot[\sigma],
$$

on the oriented $n$-simplices $K_n$ of $K$, subject to the relation $[v_{\pi(0)},\dots,v_{\pi(n)}] = \operatorname{sgn}(\pi)[v_0,\dots,v_n]$; the **augmentation** is $\varepsilon : C_0(K;R) \to R$, $\varepsilon[v] = 1$, and the **reduced** chain modules are the kernel of $\varepsilon$ in degree zero and the ordinary modules above. The modules are zero in negative degree and free of rank the number of $n$-simplices in the finite case.

## The Boundary Operator

### The Face Formula and the Incidence Number

**Definition.** The **boundary operator** of the simplicial complex is the $R$-linear map

$$
\partial_n : C_n(K;R) \longrightarrow C_{n-1}(K;R), \qquad
\partial_n[v_0,\dots,v_n] = \sum_{i=0}^{n}(-1)^i\,[v_0,\dots,\widehat{v_i},\dots,v_n],
$$

for $n \geq 1$, and $\partial_0 = 0$; the **incidence number** of a facet $\tau$ of an $n$-simplex $\sigma$ is the coefficient of $[\tau]$ in $\partial_n[\sigma]$, equal to $\pm 1$ and written $[\sigma:\tau]$.

**Proposition.** The incidence number is well defined independently of the orientations chosen for $\sigma$ and $\tau$: reversing the orientation of $\sigma$ or of $\tau$ changes both sides by the same sign.

*Proof.* Reversing the orientation of $\sigma$ negates $\partial_n[\sigma]$ and hence every coefficient; reversing the orientation of a facet negates that one generator, and the coefficient of that generator changes sign together with the generator. A transposition of two vertices of $\sigma$ reverses the orientation of all the facets except the two omitted by the transposition, and the formula is compatible. $\square$

So the boundary is a matrix of incidence signs against the facet relation, and the matrix depends on the orientations only through the convention that a simplex and its reverse are negatives.

### The Boundary Matrix

**Definition.** Order the $n$-simplices of a finite $K$ and the $(n-1)$-simplices, and let $A_n$ be the $|K_{n-1}| \times |K_n|$ matrix with entries

$$
(A_n)_{\tau,\sigma} = [\sigma:\tau] \in \{0,\pm1\},
$$

the **$n$-th incidence matrix** of $K$. Then $\partial_n$ is the operator whose matrix is $A_n$, and the chain complex is the sequence of matrices

$$
\cdots \xrightarrow{\ A_{n+1}\ } C_n(K;R) \xrightarrow{\ A_n\ } C_{n-1}(K;R) \xrightarrow{\ A_{n-1}\ } \cdots .
$$

**Theorem (the square is zero).** For every $n$,

$$
\partial_{n-1}\partial_n = 0, \qquad \text{equivalently} \qquad A_{n-1}A_n = 0 ,
$$

the second as a matrix identity over $R$.

*Proof.* The terms of $\partial\partial[v_0,\dots,v_n]$ are indexed by ordered pairs of omitted vertices $i < j$; omitting $v_i$ then $v_j$ gives sign $(-1)^i(-1)^j$ and omitting $v_j$ then $v_i$ gives sign $(-1)^{j-1}(-1)^i$, and the two terms are the same oriented simplex with opposite signs, so they cancel; this is the computation of *Simplicial and Singular Homology*, and it is exactly the statement that the products of the incidence matrices vanish. $\square$

The square-zero property has the operator content that the boundary is **nilpotent of index two**, so the complex has an intrinsic chain of subspaces $C_n \supseteq Z_n \supseteq B_n \supseteq 0$; a square-zero operator is the simplest instance of the contractibility criterion of the cone of *The Suspension Operator*, and every complex of this Part is built from such operators.

## Cycles, Boundaries and the Homology

### The Kernel and the Image

**Definition.** The **cycles** and the **boundaries** of the simplicial complex are

$$
Z_n = \ker\partial_n \subseteq C_n(K;R), \qquad B_n = \operatorname{im}\partial_{n+1} \subseteq Z_n,
$$

the second inclusion being the square-zero identity, and the **simplicial homology** is

$$
H_n^\Delta(K;R) = Z_n / B_n = \ker\partial_n\big/\operatorname{im}\partial_{n+1}.
$$

The homology is the object that the operator defines; equivalently, it is the homology of the matrix sequence $(A_n)$ in the sense of *The Boundary Operator*. A cycle that is not a boundary is a nonzero class; a complex is acyclic in degree $n$ when the matrices have full rank in the appropriate sense, $H_n = 0$.

### The Rank Formula and the Euler Characteristic

**Theorem.** Over a field $F$ the dimensions are

$$
\dim_F H_n^\Delta(K;F) = \dim_F C_n - \operatorname{rank}A_n - \operatorname{rank}A_{n+1},
$$

and the **Euler characteristic** obeys

$$
\chi(K) = \sum_n (-1)^n \dim_F C_n(K;F) = \sum_n (-1)^n \dim_F H_n^\Delta(K;F).
$$

*Proof.* The rank-nullity theorem applied to $\partial_n$ gives $\dim\ker\partial_n = \dim C_n - \operatorname{rank}A_n$, and the rank-nullity theorem applied to $\partial_{n+1}$ restricted to its image gives $\dim H_n = \dim\ker\partial_n - \operatorname{rank}A_{n+1}$; substituting gives the first formula. The alternating sum of the dimensions is invariant under passing between the two short exact sequences $0\to Z_n\to C_n\to B_{n-1}\to 0$ and $0 \to B_n \to Z_n \to H_n \to 0$, the ranks telescoping, which is the Euler–Poincaré formula. $\square$

The first formula is the operator form of the computation: the Betti numbers of a finite complex are the differences of the dimensions and the ranks of the incidence matrices, so the boundary operator computes the homology by pure linear algebra.

### The Smith Normal Form and the Torsion

**Theorem.** Let $R$ be a principal ideal domain and let $K$ be finite. Then the homology is the direct sum of a free part and a torsion part,

$$
H_n^\Delta(K;R) \;\cong\; R^{\beta_n} \oplus \bigoplus_{j} R/(d^{(n)}_j), \qquad d^{(n)}_1 \mid d^{(n)}_2 \mid \cdots ,
$$

where the **Betti number** is

$$
\beta_n = \operatorname{rank}C_n - \operatorname{rank}A_n - \operatorname{rank}A_{n+1},
$$

and the invariant factors $d^{(n)}_j$ are the non-unit invariant factors of the Smith normal form of $A_{n+1}$. The free part is the rank over the field of fractions, the torsion is generated by the elementary divisors greater than one, and the whole computation is the Smith normal form of the two boundary matrices at each degree.

*Proof.* The structure theorem for finitely generated modules over a principal ideal domain applied to the cokernel of the restriction of $\partial_{n+1}$ into $Z_n$; the Smith normal form diagonalises $A_{n+1}$ by invertible row and column operations, and the kernel and cokernel are read from the diagonal, the rank formula being the rank-nullity over the fraction field. $\square$

The torsion of the homology is thus a property of the incidence matrix of the next degree: a non-unit invariant factor of $\partial_{n+1}$ produces a cyclic summand of $H_n$. For the projective plane with its minimal triangulation the boundary matrix of degree two has determinant $\pm 2$, and the resulting $H_1 \cong \mathbb{Z}/2$ is the standard instance.

## The Coboundary and the Dual Complex

### The Dual Modules

**Definition.** The **simplicial cochain module** is the dual

$$
C^n(K;R) = \operatorname{Hom}_R\bigl(C_n(K;R),\, R\bigr),
$$

with the dual basis $[\sigma]^*$ of a simplex, and the **coboundary** is the adjoint of the boundary,

$$
\delta^{n-1} : C^{n-1}(K;R) \longrightarrow C^n(K;R), \qquad \langle \delta\alpha, c\rangle = \langle \alpha, \partial c\rangle ,
$$

in the notation of *The Boundary Operator*; the **simplicial cohomology** is $H^n_\Delta(K;R) = \ker\delta^n/\operatorname{im}\delta^{n-1}$.

**Theorem.** The matrix of $\delta^{n-1}$ in the dual bases is the transpose of the matrix of $\partial_n$,

$$
(\delta^{n-1})_{\sigma,\tau} = (A_n)_{\tau,\sigma} = [\sigma:\tau],
$$

and $\delta\delta = 0$ because $A_n A_{n-1}$ is the transpose of $A_{n-1}A_n = 0$; hence the cochain complex is the transpose of the chain complex, and the cohomology is computed by the same matrices with the maps transposed.

*Proof.* The evaluation pairing identifies a cochain with its coordinates, and the identity $\langle\delta\alpha,c\rangle=\langle\alpha,\partial c\rangle$ reads as the transpose relation of the matrices. The square-zero identity is the transpose of the chain one. $\square$

So the dual operator of the simplicial complex is the transpose matrix, and the passage between homology and cohomology is the passage between a matrix and its transpose: the kernel of the transpose computes the cocycles, and the universal coefficient theorem of *Cohomology and the Universal Coefficient Theorem* relates the two graded modules. This is the operator-layer form of the duality between chains and cochains, and it is why the simplicial cohomology of a finite complex is read from the incidence matrices already used for the homology.

## Naturality and the Simplicial Maps

### Simplicial Maps and the Chain Map

**Definition.** A **simplicial map** $\phi : K \to L$ sends simplices of $K$ to simplices of $L$ and vertices to vertices, and is determined by its values on the vertices; it induces, on an oriented simplex, the map

$$
\phi_n[v_0,\dots,v_n] = [\phi(v_0),\dots,\phi(v_n)],
$$

read as zero when the images are not distinct and with the orientation induced by the ordering otherwise, extended $R$-linearly.

**Theorem.** A simplicial map is a chain map of the simplicial complexes, $\phi_{n-1}\partial_n = \partial_n\phi_n$; the assignment is functorial, and it induces maps $H_n^\Delta(\phi) : H_n^\Delta(K;R) \to H_n^\Delta(L;R)$. The chain map is compatible with the operators of *The Boundary Operator*: it intertwines the boundaries, the augmentations and, by duality, the coboundaries.

*Proof.* Both sides evaluated on a simplex are the alternating sum of the images of its facets, and the images of the facets are the facets of the image; the functoriality is that $(\psi\circ\phi)_n = \psi_n\circ\phi_n$ for simplicial maps. The induced map on homology is that of any chain map. $\square$

### The Hopf Trace Formula

**Theorem.** Let $\phi : K \to K$ be a simplicial map of a finite complex and let $\phi_n$ be its chain map. Then the **Lefschetz number**

$$
L(\phi) = \sum_n (-1)^n \operatorname{tr}(\phi_n) = \sum_n (-1)^n \operatorname{tr}\bigl(H_n^\Delta(\phi)\bigr)
$$

depends only on the induced maps on homology, the equality being the **Hopf trace formula**.

*Proof.* The alternating sum of the traces is invariant under passing between the two short exact sequences $0\to Z_n\to C_n\to B_{n-1}\to 0$ and $0\to B_n\to Z_n\to H_n\to 0$ of $\phi$-stable spaces, the same telescoping as in the Euler characteristic; it is the operator form of the additivity of the trace over an exact sequence. $\square$

The Lefschetz number is thus an invariant of the homology of the simplicial map and not of the chain level, and it is the boundary-operator form of the fixed-point index. The topological fixed-point theorem that reads from $L(\phi)\neq 0$ the existence of a fixed point of the geometric realisation, and the degree theory on which it rests, are the subject of *Degree Theory and the Brouwer Fixed Point Theorem*, where the Lefschetz number is a degree and the sign of the permutation of the fixed simplices is the local index.

## Examples

**Example (the boundary of a triangle).** Let $K$ be the three edges of a $2$-simplex. Then $C_1$ is free of rank three and $C_0$ of rank three, and the cycle $[v_0v_1]+[v_1v_2]+[v_2v_0]$ has zero boundary while the boundaries of $C_1$ are generated by the differences $[v_i]-[v_0]$; hence $H_1^\Delta\cong R$ and $H_0^\Delta\cong R$, the homology of a circle, as recorded in *Simplicial and Singular Homology*.

**Example (the sphere and the suspension).** For the boundary of an $(n+1)$-simplex, the simplicial complex is $S^n$; the incidence matrices have ranks $|K_n|$ in the middle and the homology is $R$ in degrees $0$ and $n$. The suspension of *The Suspension Operator* is realised simplicially by the join with a two-point complex, and the suspension operator is the shift of the simplicial complex that adds the two cone vertices.

**Example (the minimal triangulation of the torus).** The minimal triangulation of the torus has $7$ vertices, $21$ edges and $14$ triangles, so the alternating sum of the ranks is $7-21+14=0$; the incidence matrices have maximal possible ranks compatible with that sum, and the homology is $H_0\cong R$, $H_1\cong R^2$, $H_2\cong R$, the free ranks exhibiting the Betti numbers of the surface and no torsion, as the orientability requires.

**Example (the projective plane).** For the minimal triangulation of $\mathbb{RP}^2$, with $6$ vertices, $15$ edges and $10$ triangles, the alternating sum is $6-15+10=1=\chi$; over $\mathbb{Z}$ the second incidence matrix has Smith normal form with one invariant factor $2$, and the homology is $H_0\cong\mathbb{Z}$, $H_1\cong\mathbb{Z}/2$, $H_2 = 0$. The torsion is read from the matrix, and it is the obstruction to the orientability that the top homology would otherwise express.

## Summary

The boundary operator of a simplicial complex sends an oriented simplex to the alternating sum of its oriented facets, with incidence numbers $\pm1$; assembled over the oriented simplices it is the incidence matrix $A_n$ of the complex, and the square-zero identity $\partial\partial=0$ is the matrix identity $A_{n-1}A_n=0$ obtained by cancelling the two orderings of an omitted pair of vertices. The cycles and boundaries are $Z_n=\ker A_n$ and $B_n=\operatorname{im}A_{n+1}$, the homology is $Z_n/B_n$, and over a field the Betti numbers are the rank differences $\dim C_n - \operatorname{rank}A_n - \operatorname{rank}A_{n+1}$, with the Euler characteristic the alternating sum, over a principal ideal domain the Smith normal form of the incidence matrix adds the torsion, the invariant factors of $\partial_{n+1}$ producing the cyclic summands. The coboundary of the dual complex is the transpose of the boundary matrix, and the cohomology is the cohomology of the transpose. A simplicial map is a chain map intertwining the operators, functorially, and the Hopf trace formula reads the alternating trace of a simplicial self-map from its induced maps on homology. The operator is the concrete instance of the operator of *The Boundary Operator*, the agreement of its homology with the singular homology is the invariance theorem of *Simplicial and Singular Homology*, and the whole computation is finite linear algebra over a ring; nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$, $K_n$, $|K|$ | Simplicial complex, its $n$-simplices, its underlying space |
| $[v_0,\dots,v_n]$ | Oriented simplex; reversing the orientation negates it |
| $C_n(K;R)$ | Free module on the oriented $n$-simplices |
| $\partial_n$ | Boundary operator, $[v_0,\dots,v_n]\mapsto\sum_i(-1)^i[\dots\widehat{v_i}\dots]$ |
| $[\sigma:\tau]$ | Incidence number of a facet, equal to $\pm1$ |
| $A_n$ | $n$-th incidence matrix, $(A_n)_{\tau,\sigma}=[\sigma:\tau]$ |
| $A_{n-1}A_n = 0$ | Square-zero identity; the boundary is nilpotent |
| $Z_n$, $B_n$, $H_n^\Delta(K;R)$ | Cycles, boundaries, simplicial homology |
| $\chi = \sum(-1)^n\dim C_n$ | Euler characteristic; equals $\sum(-1)^n\dim H_n$ |
| $\beta_n = \dim C_n - \operatorname{rank}A_n - \operatorname{rank}A_{n+1}$ | Betti number; over a field |
| $R/(d^{(n)}_j)$ | Torsion summands from the Smith normal form of $A_{n+1}$ |
| $C^n(K;R)$, $\delta$, $H^n_\Delta(K;R)$ | Cochains, coboundary (the transpose), cohomology |
| $\phi_n$, $L(\phi)=\sum(-1)^n\operatorname{tr}(\phi_n)$ | Chain map of a simplicial map; Lefschetz number |

## Further Reading

- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for simplicial complexes, oriented chains, the incidence matrices and the computation of simplicial homology and cohomology.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for simplicial and $\Delta$-complexes, the boundary formula and the agreement with the singular theory.
- Edwin H. Spanier, *Algebraic Topology* (McGraw–Hill, 1966), for the simplicial chain complex, the incidence numbers and the homology over a general ring.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the Smith normal form, the structure theorem over a principal ideal domain and the computation of the homology of a matrix.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the chain complex of a simplicial complex, the differential graded structure and the Hopf trace formula.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the Lefschetz number as the alternating trace and for the fixed-point theorem it yields.
