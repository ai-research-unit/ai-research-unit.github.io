# __The Quintic and the Spectral Strata of $M_5(\mathbb{C})$__

## Introduction

The characteristic polynomial of $A\in M_5(\mathbb{C})$ is

$$
\chi_A(t)=\det(tI-A)=t^5-c_1t^4+c_2t^3-c_3t^2+c_4t-c_5,
$$

with $c_1=\operatorname{tr}A$, $c_5=\det A$, and $c_k$ the sum of the principal $k\times k$ minors. Its roots are the eigenvalues, and their multiplicity pattern is the **spectral type** of $A$. The **spectral strata** are the locally closed subsets of matrices with a fixed multiplicity pattern:

$$
1+1+1+1+1,\quad 2+1+1+1,\quad 2+2+1,\quad 3+1+1,\quad 3+2,\quad 4+1,\quad 5 .
$$

The first is the **regular semisimple** stratum, the open stratum of matrices with five distinct eigenvalues; the last is the scalar stratum, the unique closed stratum. The root orbit of *Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$* is the conjugacy class of a fixed root, of dimension $20$, inside the regular semisimple locus.

The **discriminant** $\Delta$ is the polynomial in the coefficients whose vanishing is the condition of a repeated root. Its zero locus is the **singular set** of the characteristic polynomial map, a hypersurface of codimension $1$; its complement is the regular semisimple locus. The orbit strata have dimensions $20,18,16,14,12,8,0$ and codimensions $5,7,9,11,13,17,25$ in $M_5$; the discriminant locus is the union of all the strata with a repeated root, including the non-semisimple matrices, and it has dimension $24$.

The **quintic** enters because the eigenvalues of a $5\times5$ matrix are the roots of a quintic. A general quintic has no solution in radicals: the Galois group of the general quintic is $S_5$, which is not solvable (Abel–Ruffini, Galois). The eigenvalues exist by the fundamental theorem of algebra, and the Lagrange projectors exist at a simple spectrum, but neither fact produces a radical formula for the roots. The projectors are algebraic functions of the coefficients, not generally radical functions.

The article assumes the matrix algebra and the root. It uses no form and no topology. The determinant and the discriminant are treated as polynomials; the singular set $\det=0$ of *The Forms, the Norms and the Singular Set of $M_5(\mathbb{C})$* is a different locus, and it is not the discriminant.

## The Characteristic Polynomial

### The Coefficients

**Definition.** The **characteristic polynomial** of $A$ is $\chi_A(t)=\det(tI-A)$. Its coefficients are the elementary symmetric functions of the eigenvalues:

$$
\chi_A(t)=\prod_{k=1}^{5}(t-\lambda_k)
=t^5-e_1t^4+e_2t^3-e_3t^2+e_4t-e_5,
$$

where $e_k$ is the $k$-th elementary symmetric function of the eigenvalues $\lambda_1,\dots,\lambda_5$.

**Proposition (Vieta).** The coefficients are

$$
e_1=\sum_k\lambda_k=\operatorname{tr}A,\qquad
e_5=\prod_k\lambda_k=\det A,
$$

and $e_k$ is the sum of the principal $k\times k$ minors of $A$.

**Proof.** The coefficient of $t^{5-k}$ in $\det(tI-A)$ is $(-1)^k$ times the sum of the principal $k\times k$ minors, by the Laplace expansion; the eigenvalues are the roots, and the elementary symmetric functions are the coefficients by Vieta. The trace is the sum of the eigenvalues and the determinant their product.

**Corollary.** The characteristic polynomial is a polynomial map

$$
\chi:M_5(\mathbb{C})\longrightarrow\mathbb{C}^5,\qquad A\longmapsto(c_1,\dots,c_5),
$$

whose fibres are the sets of matrices with a fixed characteristic polynomial. The map is surjective: every monic quintic is the characteristic polynomial of its companion matrix.

**Proof.** The companion matrix of $t^5-c_1t^4+c_2t^3-c_3t^2+c_4t-c_5$ has the displayed polynomial as its characteristic polynomial, by the standard computation of the companion matrix.

### The Companion Matrix

**Definition.** The **companion matrix** of the monic quintic

$$
t^5+a_4t^4+a_3t^3+a_2t^2+a_1t+a_0
$$

is

$$
C=\begin{pmatrix}
0&0&0&0&-a_0\\
1&0&0&0&-a_1\\
0&1&0&0&-a_2\\
0&0&1&0&-a_3\\
0&0&0&1&-a_4
\end{pmatrix}.
$$

**Proposition.** $\chi_C(t)=t^5+a_4t^4+a_3t^3+a_2t^2+a_1t+a_0$.

**Proof.** Expand $\det(tI-C)$ along the first column, or use the standard companion-matrix identity. The matrix has the cyclic vector $e_1$, and its minimal polynomial is the displayed quintic.

**Corollary.** Every monic quintic arises as the characteristic polynomial of a $5\times5$ matrix, and the eigenvalues of $C$ are the roots of the quintic. The spectral theory of $M_5$ is therefore the spectral theory of quintics.

**Proof.** The characteristic polynomial of $C$ is the quintic; the eigenvalues are its roots.

## The Discriminant

### The Definition

**Definition.** The **discriminant** of the monic quintic is

$$
\Delta=\prod_{1\le i<j\le5}(\lambda_i-\lambda_j)^2,
$$

a symmetric polynomial in the roots, hence a polynomial in the coefficients $c_1,\dots,c_5$.

**Proposition.** $\Delta=0$ if and only if the quintic has a repeated root. The discriminant is a polynomial in the coefficients of total degree $2\cdot5-2=8$ (it is isobaric of weight $20$ when the coefficient of $t^{5-k}$ is given weight $k$).

**Proof.** The product vanishes exactly when two roots coincide. The degree statement is the standard isobaric degree of the discriminant: in the roots it is homogeneous of degree $5\cdot4=20$; in the coefficients $c_k$ of weight $k$ it has weight $20$, and its total degree is at most $2\cdot5-2=8$. The formula is classical; see the references.

**Corollary.** The discriminant is the **singular set** of the characteristic polynomial map: over $\Delta\ne0$ the five roots are distinct and the fibre is the conjugacy class of the companion matrix; over $\Delta=0$ two roots merge and the fibre degenerates.

**Proof.** The roots are distinct exactly when $\Delta\ne0$; the fibre over a polynomial with distinct roots is the set of matrices similar to the companion matrix, a single conjugacy class.

### The Regular Semisimple Locus

**Definition.** The **regular semisimple locus** of $M_5$ is the open set

$$
M_5^{\mathrm{rs}}=\{A:\Delta(\chi_A)\ne0\},
$$

the matrices with five distinct eigenvalues. Its complement is the **discriminant locus** $\{A:\Delta(\chi_A)=0\}$.

**Proposition.** $M_5^{\mathrm{rs}}$ is a nonempty Zariski open subset of $M_5$, of dimension $25$. The discriminant locus is a hypersurface, of dimension $24$.

**Proof.** The discriminant is a nonzero polynomial on $M_5$ (the diagonal matrix with distinct eigenvalues has $\Delta\ne0$), so its nonvanishing locus is a nonempty Zariski open set; a nonzero polynomial vanishes on a hypersurface, of codimension $1$. The dimension of $M_5$ is $25$.

**Corollary.** The regular semisimple locus is dense in $M_5$; every matrix is a limit of matrices with distinct eigenvalues. The discriminant locus is the complement, and it contains every matrix with a repeated eigenvalue, semisimple or not.

**Proof.** A nonempty Zariski open subset of an irreducible variety is dense; the discriminant vanishes on every matrix with a repeated eigenvalue by definition.

**Remark.** **The regular semisimple locus is not the root orbit.** The locus is the union of all conjugacy classes of matrices with distinct eigenvalues, of dimension $25$; the root orbit of a fixed root $H$ is one conjugacy class inside it, of dimension $20$. The root set $PGL_5/T$ of the earlier articles is the orbit of the fixed root, not the whole open locus. The distinction is the difference between "some five distinct eigenvalues" and "the five eigenvalues $\zeta_1,\dots,\zeta_5$".

## The Spectral Strata

### The Multiplicity Partitions

**Definition.** The **spectral type** of $A$ is the partition of $5$ given by the multiplicities of its distinct eigenvalues. The **semisimple spectral stratum** of a partition $\lambda=(m_1,\dots,m_r)$ is the conjugacy class of a diagonal matrix with distinct eigenvalues of multiplicities $m_1,\dots,m_r$.

**Proposition.** The semisimple spectral strata are the partitions

$$
(1,1,1,1,1),\quad(2,1,1,1),\quad(2,2,1),\quad(3,1,1),\quad(3,2),\quad(4,1),\quad(5),
$$

and every semisimple matrix lies in exactly one of them.

**Proof.** The multiplicities of the distinct eigenvalues sum to $5$; the partitions of $5$ are the listed seven. A semisimple matrix is diagonalizable, and its conjugacy class is determined by the eigenvalues and their multiplicities.

### Dimensions and Codimensions

**Theorem.** The semisimple spectral stratum of the partition $(m_1,\dots,m_r)$ has dimension

$$
\dim=25-\sum_{i=1}^{r}m_i^2,
$$

in $M_5$ and in $PGL_5$. Its codimension in $M_5$ is $\sum_i m_i^2$, and its codimension in $PGL_5$ is $\sum_i m_i^2-1$.

**Proof.** The centraliser of a diagonal matrix with distinct eigenvalues on blocks of sizes $m_i$ is $\prod_iGL_{m_i}$, of dimension $\sum_i m_i^2$. The conjugacy class has dimension $\dim GL_5-\sum_i m_i^2=25-\sum_i m_i^2$. In $PGL_5$ the centraliser is the image of the product modulo scalars, of dimension $\sum_i m_i^2-1$, and the orbit has dimension $24-(\sum_i m_i^2-1)=25-\sum_i m_i^2$; the two dimensions agree.

**Corollary.** The dimensions and the codimensions in $M_5$ are

| Partition | Dimension | Codimension in $M_5$ |
|---|---|---|
| $(1,1,1,1,1)$ | $20$ | $5$ |
| $(2,1,1,1)$ | $18$ | $7$ |
| $(2,2,1)$ | $16$ | $9$ |
| $(3,1,1)$ | $14$ | $11$ |
| $(3,2)$ | $12$ | $13$ |
| $(4,1)$ | $8$ | $17$ |
| $(5)$ | $0$ | $25$ |

**Proof.** Evaluate $25-\sum m_i^2$: for $1^5$, $25-5=20$; for $2,1,1,1$, $25-7=18$; for $2,2,1$, $25-9=16$; for $3,1,1$, $25-11=14$; for $3,2$, $25-13=12$; for $4,1$, $25-17=8$; for $5$, $25-25=0$. The codimension in $M_5$ is $25-\dim=\sum m_i^2$; in $PGL_5$ it is one less.

### The Closure Order

**Proposition.** The closure of the stratum of $\lambda$ contains the stratum of $\mu$ if and only if $\lambda$ is a coarsening of $\mu$ (equivalently, $\mu$ refines $\lambda$). In particular the regular stratum $(1,1,1,1,1)$ is open and dense, and the scalar stratum $(5)$ is the unique closed stratum.

**Proof.** A diagonal matrix with eigenvalue multiplicities $\mu$ can be deformed to one with multiplicities $\lambda$ by letting groups of eigenvalues coalesce; the multiplicities can only merge under a limit, never split. The regular stratum is open because the discriminant is nonzero; the scalar stratum is a single point, hence closed.

**Corollary.** The semisimple spectral strata form a stratification of the semisimple locus, with the refinement order. The root orbit $(1^5)$ is the open stratum; the strata $(2,1,1,1)$ and the others lie in its closure.

**Proof.** The closure order is the refinement order of partitions; the open stratum is the finest partition, and every other partition is a coarsening of it.

**Remark.** **The discriminant locus is larger than the union of the non-regular semisimple orbits.** The largest semisimple non-regular orbit has dimension $18$ (the orbit $(2,1,1,1)$), and the union of the semisimple strata with a repeated eigenvalue has dimension $22$ (the orbit plus the four eigenvalue parameters); the discriminant locus also contains the non-semisimple matrices, and it is the hypersurface of dimension $24$. The semisimple strata are the smooth pieces of the **semisimple** part; the full discriminant is their closure plus the non-semisimple orbits.

## The Quintic

### The General Quintic

**Theorem (Abel–Ruffini, Galois).** A general quintic

$$
t^5+a_4t^4+a_3t^3+a_2t^2+a_1t+a_0=0
$$

has no solution in radicals. Its Galois group over the field of rational functions of the coefficients is $S_5$, which is not solvable.

**Proof.** The Galois group of the general quintic is $S_5$; a solvable Galois group is necessary for solvability by radicals; $S_5$ has the non-abelian simple subgroup $A_5$, so it is not solvable. The theorem is the Abel–Ruffini theorem; the Galois-theoretic form is due to Galois.

**Corollary.** The eigenvalues of a general $5\times5$ matrix are not radical functions of the matrix entries: no expression built from the entries by $+,-,\times,\div$ and $k$-th roots gives the eigenvalues for all matrices.

**Proof.** The eigenvalues of the companion matrix are the roots of the quintic; a radical formula for the eigenvalues of all matrices would give a radical solution of the general quintic.

### The Lagrange Projectors

**Theorem.** Let $H$ be a matrix with simple spectrum $\zeta_1,\dots,\zeta_5$. The Lagrange projectors

$$
P_k=\prod_{l\ne k}\frac{H-\zeta_lI}{\zeta_k-\zeta_l},\qquad k=1,\dots,5,
$$

are well defined, idempotent, orthogonal and complete:

$$
P_k^2=P_k,\qquad P_kP_l=\delta_{kl}P_k,\qquad \sum_kP_k=I,\qquad H=\sum_k\zeta_kP_k .
$$

**Proof.** The polynomial $\prod_{l\ne k}(t-\zeta_l)/(\zeta_k-\zeta_l)$ is the Lagrange interpolating polynomial for the function that is $1$ at $\zeta_k$ and $0$ at the other $\zeta_l$. Evaluated at $H$, it gives the spectral projector onto the $\zeta_k$-eigenspace; the identities follow from the polynomial identities at the five distinct points.

**Corollary.** The projectors exist for every simple spectrum, independently of the solvability of the quintic. They are polynomial in $H$ of degree $4$, with coefficients that are rational functions of the eigenvalues; their entries are algebraic functions of the entries of $H$, not generally radical functions.

**Proof.** The Lagrange polynomial has degree $4$ and coefficients rational in the $\zeta_k$; substituting $H$ gives a polynomial of degree $4$ in $H$. The eigenvalues are algebraic functions of the entries (the roots of the characteristic polynomial), and the projectors are rational functions of $H$ and the eigenvalues; the composition is algebraic, not generally radical.

**Remark.** **The existence of the projectors is not a radical solution of the quintic.** The projectors are the spectral decomposition of a matrix whose eigenvalues are given; they presuppose the roots. The theorem that they exist at a simple spectrum is a theorem of linear algebra, valid for every matrix with distinct eigenvalues, and it says nothing about expressing the roots in radicals. The Galois obstruction is to the radical expression of the eigenvalues, not to the spectral decomposition.

### The Galois Action

**Proposition.** The Galois group of the characteristic polynomial acts on the five eigenvalues, hence on the five Lagrange projectors, by permutation. For a general quintic the action is the full symmetric group $S_5$.

**Proof.** An automorphism of the splitting field permutes the roots and hence the projectors $P_k$, which are labelled by the roots. For a general quintic the Galois group is $S_5$.

**Corollary.** The projectors are permuted transitively by the Galois group of a general quintic; no single projector is defined over the field of coefficients. The **set** of five projectors is Galois-invariant, but the individual projector is not.

**Proof.** $S_5$ acts transitively on the five roots; the projectors are labelled by the roots; a projector fixed by the whole group would correspond to a root fixed by the whole group, which does not exist for a general quintic.

## The Spectral Strata of $M_5$

### The Characteristic Map

**Proposition.** The characteristic map $\chi:M_5\to\mathbb{C}^5$ is surjective, and its fibre over a polynomial with distinct roots is the conjugacy class of the companion matrix, of dimension $20$. The fibre over a polynomial with a repeated root is larger, and the discriminant locus is the preimage of the discriminant hypersurface in $\mathbb{C}^5$.

**Proof.** Surjectivity is the companion matrix. Over a polynomial with distinct roots, every matrix with that characteristic polynomial is diagonalizable with the five distinct eigenvalues, hence conjugate to the diagonal matrix, hence to the companion matrix; the conjugacy class has dimension $20$. Over a repeated root, the fibre contains matrices with different Jordan types and has larger dimension.

**Corollary.** The regular semisimple locus is the preimage of the complement of the discriminant; its dimension is $25$, and the discriminant locus has dimension $24$.

**Proof.** The complement of the discriminant is open in $\mathbb{C}^5$, and its preimage is open in $M_5$; the discriminant hypersurface has codimension $1$, and its preimage has codimension $1$ because the characteristic map is dominant.

### The Strata in the Algebra

**Proposition.** The semisimple spectral stratum of the partition $(m_1,\dots,m_r)$ is the union of the conjugacy classes of diagonal matrices with those multiplicities; its dimension is $25-\sum m_i^2$. The **spectral stratum** of the characteristic polynomial with the same multiplicity pattern is the preimage of the corresponding coefficient stratum, of dimension $25-(5-r)=20+r$.

**Proof.** The orbit dimension is the centraliser computation. The coefficient stratum of a polynomial with $r$ distinct roots has codimension $5-r$ in $\mathbb{C}^5$ (each merging of two roots imposes one condition); its preimage under the dominant characteristic map has the same codimension, hence dimension $25-(5-r)=20+r$.

**Corollary.** The two stratifications are different:

| Partition | Orbit dimension | Characteristic-stratum dimension |
|---|---|---|
| $(1,1,1,1,1)$ | $20$ | $25$ |
| $(2,1,1,1)$ | $18$ | $24$ |
| $(2,2,1)$ | $16$ | $23$ |
| $(3,1,1)$ | $14$ | $23$ |
| $(3,2)$ | $12$ | $22$ |
| $(4,1)$ | $8$ | $22$ |
| $(5)$ | $0$ | $21$ |

**Proof.** The orbit dimensions are $25-\sum m_i^2$; the characteristic-stratum dimensions are $20+r$, with $r$ the number of parts. Evaluate for the seven partitions.

**Remark.** **The root orbit is the orbit stratum $(1^5)$, of dimension $20$; the regular semisimple locus is the characteristic stratum $(1^5)$, of dimension $25$.** The first is the conjugacy class of the fixed root; the second is the open set of all matrices with distinct eigenvalues. The article uses the orbit strata for the spectral types and the characteristic strata for the discriminant; the two tables are not the same, and the difference is the dimension of the eigenvalue parameters.

## Summary

The characteristic polynomial of $A\in M_5(\mathbb{C})$ is a monic quintic, with the coefficients $c_1=\operatorname{tr}A$, $c_5=\det A$ and $c_k$ the principal minors. The discriminant $\Delta=\prod_{i<j}(\lambda_i-\lambda_j)^2$ vanishes exactly on the matrices with a repeated eigenvalue; its zero locus is the discriminant hypersurface of dimension $24$, and its complement is the regular semisimple locus of dimension $25$.

$$
\boxed{\ \text{The spectral types are }1^5,\,2\,1^3,\,2^2\,1,\,3\,1^2,\,3\,2,\,4\,1,\,5;\quad \text{the root orbit }1^5\text{ has dimension }20.\ }
$$

The semisimple orbit strata have dimensions $20,18,16,14,12,8,0$ and codimensions in $M_5$ $5,7,9,11,13,17,25$; the characteristic strata have dimensions $25,24,23,23,22,22,21$. The root orbit is the orbit of the fixed root; the regular semisimple locus is the open characteristic stratum.

A general quintic has no radical solution: its Galois group is $S_5$, not solvable. The eigenvalues exist by the fundamental theorem of algebra; the Lagrange projectors exist at a simple spectrum and are polynomial in $H$; neither fact gives a radical formula for the roots. The Galois group permutes the five projectors, and for a general quintic the action is transitive.

| Object | Value |
|---|---|
| Characteristic polynomial | Monic quintic, $\chi_A(t)=\det(tI-A)$ |
| Trace | $c_1=\sum\lambda_k$ |
| Determinant | $c_5=\prod\lambda_k$ |
| Discriminant | $\Delta=\prod_{i<j}(\lambda_i-\lambda_j)^2$ |
| Regular semisimple locus | $\Delta\ne0$, dimension $25$ |
| Discriminant locus | $\Delta=0$, dimension $24$ |
| Root orbit | $1^5$, dimension $20$ |
| General quintic | No radical solution, Galois group $S_5$ |
| Lagrange projectors | Exist at a simple spectrum, polynomial in $H$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\chi_A(t)$ | The characteristic polynomial |
| $c_k$ | The coefficient of $t^{5-k}$, up to sign |
| $\lambda_1,\dots,\lambda_5$ | The eigenvalues |
| $\Delta$ | The discriminant |
| $M_5^{\mathrm{rs}}$ | The regular semisimple locus, $\Delta\ne0$ |
| $(m_1,\dots,m_r)$ | A spectral type, a partition of $5$ |
| $P_k$ | The Lagrange projector of the eigenvalue $\zeta_k$ |
| $C$ | The companion matrix of a quintic |

## Further Reading

- Israel M. Gelfand, Mikhail M. Kapranov and Andrei V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants* (Birkhäuser, 1994), for the discriminant, its degree and the stratification of the polynomial space.
- Jean-Pierre Serre, *Topics in Galois Theory* (Jones and Bartlett, 1992), for the inverse Galois problem, the group $S_5$ and the general quintic.
- Ian Stewart, *Galois Theory* (Chapman and Hall, fourth edition, 2015), for the Abel–Ruffini theorem and the solvability of the quintic.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the characteristic polynomial, the principal minors, the companion matrix and the discriminant.
- [Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m5c.html), for the root, its simple spectrum and the projectors.
- [The Element, the Coordinates and the Trace of $M_5(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m5c.html), for the characteristic polynomial, the trace and the Jordan decomposition.
- [The Forms, the Norms and the Singular Set of $M_5(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m5c.html), for the singular set $\det=0$ and its difference from the discriminant.
- [The Topology of $M_5(\mathbb{C})$](the-topology-of-m5c.html), for the topology of the discriminant complement and the strata.
