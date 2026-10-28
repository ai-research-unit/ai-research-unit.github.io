# __The Adjoint Action, the Orbits and the Flag Variety__

## Introduction

The group $GL_5(\mathbb{C})$ acts on its Lie algebra $\mathfrak{gl}_5=M_5(\mathbb{C})$ by conjugation,

$$
g\cdot A=gAg^{-1}.
$$

The orbits are the **conjugacy classes**, classified by the Jordan form. The orbit of an element $A$ has dimension

$$
\dim(GL_5\cdot A)=25-\dim Z(A),
$$

where $Z(A)$ is the centralizer. The **root orbit** is the conjugacy class of the root $H=\sum_k\zeta_kP_k$; its centralizer is the torus $T$, and its dimension is

$$
25-5=20 .
$$

The **rank-one orbit** of the projection $E_{11}$ has centralizer $GL_1\times GL_4$, of dimension $17$, and dimension

$$
25-17=8 .
$$

The **flag variety** $\mathcal{F}=GL_5/B$ has dimension $10$; it is the quotient by the Borel, the stabilizer of the standard full flag. The root orbit is a $10$-dimensional bundle over the flag variety,

$$
20=10+10,
$$

with fibre the unipotent radical $B/T$; the splitting data of the root is exactly the fibre. The Peirce decomposition is the weight decomposition of the adjoint action of the root,

$$
\operatorname{ad}_H(E_{kl})=(\zeta_k-\zeta_l)E_{kl},
$$

and the simple nilpotents $E_{k,k+1}$ are the simple root vectors.

This article develops the adjoint action, the orbit-stabilizer theorem, the root and rank-one orbits, the flag variety and the Peirce decomposition. It states the classification of the semisimple and nilpotent orbits, with the dimension tables, and the closure order. It assumes the root, the frame, the Peirce decomposition and the partial flags; it uses no form and no topology. The Springer resolution is mentioned at the end as the geometric link between the flag variety and the nilpotent cone, but it is not developed.

## The Adjoint Action

### The Action of $GL_5$ and $PGL_5$

**Definition.** The **adjoint action** of $GL_5$ on $\mathfrak{gl}_5$ is

$$
\operatorname{Ad}_g(A)=gAg^{-1}.
$$

The **adjoint action** of the Lie algebra is $\operatorname{ad}_A(B)=[A,B]$.

**Proposition.** $\operatorname{Ad}$ is a group homomorphism $GL_5\to GL(\mathfrak{gl}_5)$, and $\operatorname{ad}$ is its derivative at the identity. The center $\mathbb{C}^\times I$ acts trivially, so the action factors through $PGL_5$.

**Proof.** $\operatorname{Ad}_g\operatorname{Ad}_h(A)=ghAh^{-1}g^{-1}=\operatorname{Ad}_{gh}(A)$; differentiating $g=e^{tX}$ gives $\operatorname{ad}_X$. A scalar matrix commutes with everything, so it acts trivially.

**Corollary.** The orbits in $\mathfrak{gl}_5$ and in $\mathfrak{pgl}_5$ have the same dimensions for non-scalar elements; the scalar matrices are fixed points. The root orbit is the orbit of the image of $H$ in $\mathfrak{pgl}_5$, of dimension $20$.

**Proof.** The center is contained in every stabilizer; the orbit through a non-scalar element is the same in both quotients. The root is non-scalar, and its stabilizer in $PGL_5$ is $T/\mathbb{C}^\times$, of dimension $4$, so the orbit has dimension $24-4=20$.

### The Orbit-Stabilizer Theorem

**Theorem.** For $A\in\mathfrak{gl}_5$,

$$
\dim(GL_5\cdot A)=\dim GL_5-\dim Z(A)=25-\dim Z(A),
$$

where $Z(A)=\{g:gAg^{-1}=A\}$ is the centralizer. For the action of $PGL_5$, the same formula holds with $24$ and the centralizer modulo scalars.

**Proof.** The orbit is the homogeneous space $GL_5/Z(A)$; the dimension of a homogeneous space is the dimension of the group minus the dimension of the stabilizer. The $PGL_5$ case is the same with the center removed.

**Corollary.** The orbit is a locally closed smooth subvariety of $\mathfrak{gl}_5$, of the stated dimension, and its Zariski closure is a union of orbits.

**Proof.** A homogeneous space of an algebraic group is smooth and locally closed; the closure is a union of orbits because the group action preserves the closure.

### The Stabilizers

**Proposition.** The centralizer of a semisimple element with distinct eigenvalue multiplicities $m_1,\dots,m_r$ is $\prod_iGL_{m_i}$, of dimension $\sum_im_i^2$. The centralizer of the root is the torus $T$; the centralizer of the regular nilpotent is the algebra of polynomials in the nilpotent, of dimension $5$.

**Proof.** A matrix commuting with a semisimple element preserves each eigenspace, so the centralizer is the product of the general linear groups of the eigenspaces. The root has five distinct eigenvalues, so the centralizer is the diagonal torus. A regular nilpotent is a single Jordan block; its centralizer is the algebra of polynomials in the block, of dimension $5$.

**Corollary.** The root orbit has dimension $20$; the regular nilpotent orbit has dimension $20$; they are different orbits of the same dimension.

**Proof.** The root centralizer has dimension $5$; the regular nilpotent centralizer has dimension $5$; both orbits have dimension $25-5=20$. The root is semisimple and the regular nilpotent is nilpotent, so the orbits are disjoint.

## The Root Orbit

### Dimension 20

**Theorem.** The root orbit is

$$
\mathcal{O}_{\mathrm{root}}=GL_5\cdot H=\{gHg^{-1}:g\in GL_5\},
$$

of dimension $20$; in $PGL_5$ it is $PGL_5/T$, also of dimension $20$. It is the set of matrices with characteristic polynomial $\prod_k(t-\zeta_k)$ and five distinct eigenvalues.

**Proof.** The conjugates of $H$ have the same characteristic polynomial and the same five distinct eigenvalues. Conversely, two matrices with the same five distinct eigenvalues are diagonalizable with the same diagonal form, hence conjugate. The centralizer is $T$, of dimension $5$, so the orbit has dimension $20$; in $PGL_5$ the stabilizer is $T/\mathbb{C}^\times$, of dimension $4$, and the orbit has dimension $24-4=20$.

**Corollary.** The root orbit is a single conjugacy class, not the whole regular semisimple locus. The regular semisimple locus is the union of all the root orbits with distinct eigenvalues, of dimension $25$.

**Proof.** The orbit fixes the five eigenvalues $\zeta_k$; a different choice of five distinct eigenvalues gives a different orbit. The union over all choices is the open locus of distinct eigenvalues, of dimension $25$.

### The Stabilizer $T$

**Proposition.** The stabilizer of the root is the diagonal torus

$$
T=\left\{\operatorname{diag}(t_0,\dots,t_4):t_k\in\mathbb{C}^\times\right\},
$$

of dimension $5$ in $GL_5$ and $4$ in $PGL_5$. The Lie algebra of the stabilizer is the Cartan subalgebra of diagonal matrices.

**Proof.** $gHg^{-1}=H$ iff $g$ commutes with $H$; since $H$ has distinct eigenvalues, $g$ preserves each eigenspace and is diagonal in the eigenbasis. The scalars are the intersection with the center.

**Corollary.** The root orbit is $GL_5/T\cong PGL_5/T$, of dimension $20$. The tangent space at $H$ is the sum of the off-diagonal lines $A_{kl}$ for $k\ne l$, of dimension $20$.

**Proof.** The tangent space of the orbit is $\mathfrak{gl}_5/\mathfrak{t}$, the quotient by the diagonal; the off-diagonal lines are a complement, of dimension $25-5=20$.

### The Peirce Decomposition

**Theorem.** The adjoint action of $H$ on $\mathfrak{gl}_5$ is diagonal in the Peirce basis:

$$
\operatorname{ad}_H(E_{kl})=(\zeta_k-\zeta_l)E_{kl},
\qquad k,l=0,\dots,4 .
$$

The Peirce lines $A_{kl}$ are the eigenspaces of $\operatorname{ad}_H$ with eigenvalue $\zeta_k-\zeta_l$; the zero eigenspace is the diagonal Cartan, of dimension $5$; the nonzero eigenspaces are the off-diagonal lines, of dimension $20$.

**Proof.** $[H,E_{kl}]=(\zeta_k-\zeta_l)E_{kl}$ because $H$ is diagonal with entries $\zeta_k$. The eigenvalue zero occurs exactly when $k=l$, giving the diagonal; the other $20$ lines are the nonzero weights.

**Corollary.** The Peirce decomposition is the weight decomposition of the adjoint representation of the torus; the simple nilpotents $E_{k,k+1}$ have the simple root weights $\zeta_k-\zeta_{k+1}$. The root orbit is the orbit of the sum of the idempotents, and the Peirce lines are its weight spaces.

**Proof.** The weights of the adjoint representation are the differences of the eigenvalues; the simple roots are the differences of consecutive eigenvalues; the simple nilpotents are the corresponding weight vectors.

**Remark.** **The root orbit and the Peirce decomposition are the same data in two languages.** The orbit is the conjugacy class of $H$; the Peirce decomposition is the eigenspace decomposition of $\operatorname{ad}_H$. The stabilizer $T$ is the torus that acts by the gauge; the weight spaces are the lines $A_{kl}$; the simple nilpotents are the simple root vectors. The flag variety is the quotient by the Borel, which is the semidirect product of $T$ and the unipotent radical generated by the positive root vectors.

## The Rank-One Orbit

### The Projection

**Theorem.** The conjugacy class of the rank-one projection $E_{11}$ is

$$
\mathcal{O}_{1}=\{v\ell:\ell(v)=1\},
$$

the set of rank-one idempotents, of dimension $8$. Its stabilizer is $GL_1\times GL_4$, of dimension $17$.

**Proof.** A conjugate of $E_{11}$ is a rank-one idempotent; conversely every rank-one idempotent is $v\ell$ with $\ell(v)=1$, and it is conjugate to $E_{11}$ because $GL_5$ acts transitively on the pairs (line, hyperplane complement). The pair $(v,\ell)$ with $\ell(v)=1$ has $5+5-1=9$ parameters modulo the scaling $v\mapsto tv$, $\ell\mapsto t^{-1}\ell$, so dimension $8$. The stabilizer of $E_{11}$ is the set of $g$ preserving the image line and the kernel hyperplane and inducing inverse scalars; in block form it is $GL_1\times GL_4$, of dimension $1+16=17$.

**Corollary.** The orbit of the projection is the set of pairs (line, transverse hyperplane), of dimension $8$. It is not the partial flag of type $(1,4)$ (a nested line in a hyperplane, of dimension $7$) and not the Grassmannian $\mathrm{Gr}(1,5)$ (dimension $4$).

**Proof.** The projection $E_{11}$ is determined by its image line $L$, its kernel hyperplane $K$, and the condition $V=L\oplus K$; conversely a transverse pair $(L,K)$ determines the projection onto $L$ along $K$. The pairs with $V=L\oplus K$ form an open subset of $\mathbb{P}^4\times\mathbb{P}^4$, of dimension $4+4=8$. The nested partial flag $L\subset K$ is a different incidence, of dimension $1(4-1)+4(5-4)=7$; the projection uses the transverse complement, not the nested containment.

### The Nilpotent

**Theorem.** The conjugacy class of the rank-one nilpotent $E_{12}$ is the set of nonzero square-zero matrices of rank one, of dimension $8$. Its stabilizer has dimension $17$.

**Proof.** The Jordan type is the partition $[2,1,1,1]$; the centralizer dimension is $\sum_i(\lambda_i')^2$ for the conjugate partition $[4,1]$, which is $16+1=17$; the orbit dimension is $25-17=8$.

**Corollary.** The rank-one projection orbit and the rank-one nilpotent orbit both have dimension $8$, but they are different orbits: one is semisimple (eigenvalues $1,0,0,0,0$), the other nilpotent (all eigenvalues $0$). Their closures meet at the zero matrix.

**Proof.** The projection is semisimple with eigenvalues $1,0,0,0,0$; the nilpotent has all eigenvalues zero. The closures both contain the zero matrix; the orbits are disjoint.

### Dimension 8

**Corollary.** The rank-one orbit is not the minimal orbit: the zero orbit has dimension $0$. It is the orbit of a rank-one matrix, and its dimension is $8$.

**Proof.** The zero matrix is fixed; the rank-one orbit is $8$-dimensional.

## The Flag Variety

### The Borel and the Flag

**Definition.** The **Borel subgroup** $B\subset GL_5$ is the group of upper triangular matrices; the **flag variety** is $\mathcal{F}=GL_5/B$.

**Theorem.** $\mathcal{F}$ is the set of full flags of $\mathbb{C}^5$, of dimension $10$. The stabilizer of the standard flag is $B$, and the tangent space at the standard flag is $\mathfrak{gl}_5/\mathfrak{b}$, isomorphic to the strictly lower triangular matrices, of dimension $10$.

**Proof.** The standard flag is preserved exactly by the upper triangular matrices; the quotient $GL_5/B$ is the set of flags. The dimension is $25-15=10$; the tangent space is the quotient by the Borel, of dimension $10$.

**Corollary.** The flag variety is the orbit of the standard Borel subalgebra $\mathfrak{b}$ under the adjoint action on the Grassmannian of $15$-dimensional subspaces of $\mathfrak{gl}_5$; the stabilizer is $B$, and the orbit has dimension $10$.

**Proof.** The conjugates of $\mathfrak{b}$ are the Borel subalgebras; the stabilizer of $\mathfrak{b}$ is $B$; the orbit is $GL_5/B$.

### The Map from the Root Orbit

**Theorem.** The map

$$
\pi:GL_5/T\longrightarrow GL_5/B,\qquad gT\longmapsto gB
$$

is a fibration with fibre $B/T\cong U$, the unipotent radical of $B$, of dimension $10$. The root orbit is a $10$-dimensional bundle over the flag variety:

$$
20=10+10 .
$$

**Proof.** The map is well defined because $T\subset B$; the fibre over the standard flag is $B/T$, the upper triangular matrices modulo the diagonal, which is the unipotent radical $U$ of dimension $10$. The dimensions are $20$, $10$ and $10$.

**Corollary.** The root orbit is **not** the flag variety: it is the total space of the splitting bundle, and the fibre records the five lines, while the flag records only their partial sums.

**Proof.** The fibre $U$ is nontrivial; a unipotent matrix changes the splitting without changing the flag. The dimensions differ: $20$ versus $10$.

### The Partial Flags

**Proposition.** The partial flag of type $(d_1,\dots,d_s)$ is $GL_5/P$ for the parabolic $P$; its dimension is $\sum_i d_i(d_{i+1}-d_i)$ with $d_{s+1}=5$. The rank-two partial flag $\mathrm{Gr}(2,5)$ has dimension $6$; the root orbit maps to it with fibre dimension $14$.

**Proof.** The dimension formula is the partial-flag formula; the parabolic of the two-plane has dimension $19$ in $GL_5$, the torus $T$ has dimension $5$, the fibre $P/T$ has dimension $14$, and the base has dimension $6$; $6+14=20$.

**Corollary.** The flag variety is the finest quotient of the root orbit; the partial flags are the coarser quotients. The root orbit is the space of splittings; the flag varieties are the spaces of chains.

**Proof.** The quotients correspond to the parabolics containing $B$; the finest is the Borel, the coarsest is $GL_5$; the dimensions decrease as the parabolic grows.

## The Orbit Classification

### The Semisimple Orbits

**Theorem.** The semisimple orbits are classified by the eigenvalue multiplicities $(m_1,\dots,m_r)$, a partition of $5$. The orbit of the partition has dimension $25-\sum_im_i^2$. The list is

| Partition | Dimension |
|---|---|
| $(1,1,1,1,1)$ | $20$ |
| $(2,1,1,1)$ | $18$ |
| $(2,2,1)$ | $16$ |
| $(3,1,1)$ | $14$ |
| $(3,2)$ | $12$ |
| $(4,1)$ | $8$ |
| $(5)$ | $0$ |

**Proof.** The centralizer is $\prod_iGL_{m_i}$, of dimension $\sum m_i^2$; the orbit dimension is $25-\sum m_i^2$. Evaluate for the seven partitions.

**Corollary.** The root orbit is the orbit $(1^5)$, of dimension $20$. The orbit of the rank-one projection is the orbit $(4,1)$, of dimension $8$.

**Proof.** The root has five distinct eigenvalues; the projection has eigenvalues $1,0,0,0,0$, of multiplicities $4$ and $1$.

### The Nilpotent Orbits

**Theorem.** The nilpotent orbits are classified by the partitions of $5$ (the Jordan type). The orbit of the partition $\lambda$ has dimension

$$
\dim=25-\sum_i(\lambda_i')^2,
$$

where $\lambda'$ is the conjugate partition. The list is

| Partition | Conjugate | Dimension |
|---|---|---|
| $(5)$ | $(1,1,1,1,1)$ | $20$ |
| $(4,1)$ | $(2,1,1,1)$ | $18$ |
| $(3,2)$ | $(2,2,1)$ | $16$ |
| $(3,1,1)$ | $(3,1,1)$ | $14$ |
| $(2,2,1)$ | $(3,2)$ | $12$ |
| $(2,1,1,1)$ | $(4,1)$ | $8$ |
| $(1,1,1,1,1)$ | $(5)$ | $0$ |

**Proof.** The centralizer of a nilpotent Jordan type $\lambda$ has dimension $\sum_i(\lambda_i')^2$; the orbit dimension is $25$ minus this. Evaluate for the seven partitions.

**Corollary.** The rank-one nilpotent orbit is the partition $(2,1,1,1)$, of dimension $8$. The regular nilpotent orbit is the partition $(5)$, of dimension $20$, the same dimension as the root orbit but a different orbit.

**Proof.** The rank-one nilpotent has one block of size $2$ and three fixed vectors, the partition $(2,1,1,1)$; the regular nilpotent has a single block of size $5$, the partition $(5)$.

### The Closure Order

**Proposition.** The closure order of the nilpotent orbits is the dominance order on the partitions: the orbit of $\lambda$ is in the closure of the orbit of $\mu$ iff $\lambda\le\mu$ in the dominance order. The zero orbit is the unique closed orbit; the regular orbit is the unique open dense nilpotent orbit.

**Proof.** The dominance order theorem for nilpotent orbits of $\mathfrak{gl}_n$; the zero orbit is the smallest and closed; the regular orbit is the largest and dense in the nilpotent cone.

**Corollary.** The nilpotent cone is the union of the nilpotent orbits; it is irreducible, of dimension $20$, and its unique dense orbit is the regular one. The root orbit is not in the nilpotent cone.

**Proof.** The nilpotent cone is the zero set of the invariant polynomials, irreducible of dimension $n^2-n=20$; the regular nilpotent orbit is open dense. The root is semisimple, not nilpotent.

**Remark.** **The semisimple and nilpotent dimension lists agree after conjugation of the partition.** The semisimple orbit of $\lambda$ and the nilpotent orbit of $\lambda'$ have the same dimension $25-\sum\lambda_i^2$; this is the numerical duality visible in the two tables. The orbits themselves are different: one is semisimple, the other nilpotent. The flag variety is the common geometric object: the Springer resolution $T^*\mathcal{F}\to\mathcal{N}$ maps the cotangent bundle of the flag variety to the nilpotent cone, and the fibres are the Springer fibres, related to the orbital varieties and the Peirce decomposition.

## Summary

The adjoint action of $GL_5$ on $\mathfrak{gl}_5$ has orbits the conjugacy classes; the orbit of $A$ has dimension $25-\dim Z(A)$. The root orbit $GL_5/T\cong PGL_5/T$ has dimension $20$; the rank-one projection orbit has dimension $8$; the rank-one nilpotent orbit has dimension $8$; the flag variety $GL_5/B$ has dimension $10$.

$$
\boxed{\ \dim\mathcal{O}_{\mathrm{root}}=20,\quad \dim\mathcal{O}_{1}=8,\quad \dim\mathcal{F}=10,\quad 20=10+10.\ }
$$

The root orbit is a $10$-dimensional bundle over the flag variety with fibre the unipotent radical $B/T$. The Peirce decomposition is the weight decomposition of $\operatorname{ad}_H$; the simple nilpotents are the simple root vectors. The semisimple orbits have dimensions $20,18,16,14,12,8,0$; the nilpotent orbits have the same list, paired by conjugation of the partition. The nilpotent cone is irreducible of dimension $20$, with the regular orbit dense; the flag variety and the Springer resolution link the nilpotent cone to the flag geometry.

| Object | Dimension | Stabilizer |
|---|---|---|
| Root orbit $PGL_5/T$ | $20$ | $T$, dimension $4$ |
| Rank-one projection orbit | $8$ | $GL_1\times GL_4$, dimension $17$ |
| Rank-one nilpotent orbit | $8$ | Dimension $17$ |
| Regular nilpotent orbit | $20$ | Dimension $5$ |
| Flag variety $GL_5/B$ | $10$ | $B$, dimension $15$ |
| Root orbit fibre over flag | $10$ | $B/T=U$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Ad}_g(A)=gAg^{-1}$ | The adjoint action |
| $\operatorname{ad}_A(B)=[A,B]$ | The Lie algebra adjoint action |
| $Z(A)$ | The centralizer of $A$ |
| $\mathcal{O}_{\mathrm{root}}$ | The root orbit, dimension $20$ |
| $\mathcal{O}_1$ | The rank-one orbit, dimension $8$ |
| $\mathcal{F}=GL_5/B$ | The flag variety, dimension $10$ |
| $T$ | The diagonal torus, the root stabilizer |
| $B$ | The Borel subgroup of upper triangular matrices |
| $U=B/T$ | The unipotent radical, dimension $10$ |

## Further Reading

- James E. Humphreys, *Conjugacy Classes in Semisimple Algebraic Groups* (American Mathematical Society, 1995), for the semisimple and nilpotent orbits, the centralizers and the closure order.
- David Collingwood and William McGovern, *Nilpotent Orbits in Semisimple Lie Algebras* (Van Nostrand Reinhold, 1993), for the nilpotent orbit classification, the dimensions and the Springer resolution.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the flag variety, the Borel and parabolic subgroups and the Bruhat decomposition.
- [The Root](roots-of-unity-and-the-lagrange-idempotents-of-m5c.html), for the root, its stabilizer and the orbit.
- [The Peirce Decomposition](the-peirce-decomposition-of-m5c.html), for the weight decomposition of the adjoint action.
- [The Partial Flags](the-partial-flags-of-m5c.html), for the flag varieties and their dimensions.
- [The Quintic and the Spectral Strata](the-quintic-and-the-spectral-strata-of-m5c.html), for the semisimple orbit dimensions and the discriminant.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m5c.html), for the simple root vectors and the gauge.
