# __The Geometry of the Idempotents__

## Introduction

An **idempotent** is a matrix $P$ with $P^2=P$. The idempotents of $M_5(\mathbb{C})$ are the projections, and their geometry is the geometry of the subspaces of $\mathbb{C}^5$:

- the rank-one idempotents form an **affine bundle of rank $4$ over $\mathbb{P}^4$**, of dimension $8$;
- the rank-$p$ idempotents form the homogeneous space
  $$
  PGL_5/P(GL_p\times GL_{5-p}),
  $$
  of dimension $2p(5-p)$, a fibre bundle over the Grassmannian $\operatorname{Gr}(p,5)$ whose fibre is the contractible affine space of complements;
- the full flag variety $GL_5/B$ has dimension $10$;
- the partial flags and their incidence relations organize the nested subspaces;
- the gauge torus is the diagonal fibre of the frame bundle $GL_5\to GL_5/B$.

The rank-one case is the model. A rank-one idempotent is $P=v\ell$ with $\ell(v)=1$; the image is the line $[v]\in\mathbb{P}^4$, and the fibre over $[v]$ is the affine space of linear functionals $\ell$ with $\ell(v)=1$, of dimension $4$. The total space has dimension $4+4=8$. The idempotent is determined by the pair (line, transverse hyperplane), not by a nested flag: the kernel is a complement of the image, not a hyperplane containing it.

The rank-$p$ case is the same picture with a $p$-plane: the idempotent is the projection onto a $p$-plane $L$ along a complementary $(5-p)$-plane $K$. The base is the Grassmannian $\operatorname{Gr}(p,5)$ of $L$, of dimension $p(5-p)$; the fibre over $L$ is the affine space of complements $K$, also of dimension $p(5-p)$; the total is $2p(5-p)$.

The article computes the dimensions, proves the bundle structure, describes the rank stratification and the Peirce decomposition, and relates the idempotents to the full and partial flag varieties. It assumes the rank-one idempotents, the Peirce decomposition and the orbits of *Roots of Unity and the Lagrange Idempotents*, *The Peirce Decomposition* and *The Adjoint Action, the Orbits and the Flag Variety*.

## The Idempotents of Rank One

### The Affine Bundle over $\mathbb{P}^4$

**Theorem.** The rank-one idempotents of $M_5(\mathbb{C})$ form an affine bundle of rank $4$ over $\mathbb{P}^4$, of total dimension $8$.

**Proof.** A rank-one idempotent is $P=v\ell$ with $v\ne0$, $\ell\ne0$ and $\ell(v)=1$. The map $\pi:P\mapsto[v]$ sends $P$ to its image line. The fibre over $[v]$ is $\{\ell\in(\mathbb{C}^5)^*:\ell(v)=1\}$, an affine space of dimension $4$ (the affine hyperplane in the dual cut out by $\ell(v)=1$). The structure group is the affine group of the fibre; the total dimension is $4+4=8$.

**Corollary.** The rank-one idempotents are the pairs (line, transverse hyperplane) with $\ell(v)=1$, modulo the scaling $v\mapsto tv$, $\ell\mapsto t^{-1}\ell$; the dimension is $5+5-1-1=8$.

**Proof.** The pair $(v,\ell)$ has $5+5=10$ parameters; the scaling has one parameter; the normalization $\ell(v)=1$ removes one; total $8$. The kernel of $P$ is $\ker\ell$, a hyperplane transverse to the line.

**Corollary.** The rank-one idempotent with image $[e_1]$ and kernel $\{x_1=0\}$ is $E_{11}$; a general rank-one idempotent over $[v]$ is $v\ell$ with $\ell(v)=1$.

**Proof.** $E_{11}=e_1e_1^*$; the general formula is the outer product.

### The Dimension

**Proposition.** The affine bundle of rank-one idempotents has base $\mathbb{P}^4$ of dimension $4$ and fibre of dimension $4$; the total dimension is $8$. The projection is a submersion; the fibres are affine spaces, hence contractible.

**Proof.** The map $\pi$ is surjective; in a local trivialization over the affine chart $v_1\ne0$, the fibre is the affine hyperplane $\ell(v)=1$, which is an affine space. The rank of the differential is $4$; the fibre dimension is $4$.

**Corollary.** The rank-one idempotents are an affine bundle, not a vector bundle: there is no zero section, because the zero matrix has rank $0$.

**Proof.** The zero matrix is the unique idempotent of rank $0$; it is not in the rank-one stratum. The fibres are affine spaces without a distinguished origin.

**Corollary.** The rank-one idempotents are the orbit of $E_{11}$ under $GL_5$, of dimension $8$; the stabilizer is the block diagonal $GL_1\times GL_4$ of dimension $17$.

**Proof.** The orbit-stabilizer theorem: $25-17=8$. The stabilizer preserves the image line and the kernel hyperplane.

### The Explicit Projections

**Proposition.** In a basis adapted to the decomposition $\mathbb{C}^5=L\oplus K$, a rank-one idempotent with image $L$ and kernel $K$ is

$$
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},
$$

in the block form $1+4$. The general rank-one idempotent is conjugate to this matrix.

**Proof.** The projection onto $L$ along $K$ is the identity on $L$ and zero on $K$; the block matrix is the display. Every rank-one idempotent has a one-dimensional image and a four-dimensional kernel, so it is conjugate to $E_{11}$.

**Corollary.** The rank-one idempotents are the matrices $v\ell$ with $\ell(v)=1$; the trace is $1$, the determinant is $0$, and the spectrum is $\{1,0,0,0,0\}$.

**Proof.** The trace of $v\ell$ is $\ell(v)=1$; the eigenvalues are $1$ and $0$ with multiplicities $1$ and $4$; the determinant is $0$.

## The Idempotents of Rank $p$

### The Homogeneous Space

**Theorem.** The idempotents of rank $p$ form the homogeneous space

$$
PGL_5/P(GL_p\times GL_{5-p}),
$$

of dimension $2p(5-p)$, where $P(GL_p\times GL_{5-p})$ is the image in $PGL_5$ of the block diagonal subgroup $GL_p\times GL_{5-p}$.

**Proof.** The group $GL_5$ acts transitively on the rank-$p$ idempotents by conjugation; the stabilizer of $P=\operatorname{diag}(I_p,0)$ is the block diagonal $GL_p\times GL_{5-p}$. The dimension is

$$
25-\left(p^2+(5-p)^2\right)=2p(5-p),
$$

and the center acts trivially, so the same dimension holds for $PGL_5$.

**Corollary.** The dimensions are $p=0,1,2,3,4,5$: $0,8,12,12,8,0$. The top rank is $p=2$ or $3$, of dimension $12$; the rank-one and rank-four strata have dimension $8$; the zero and identity are points.

**Proof.** Evaluate $2p(5-p)$ at the six values.

**Corollary.** The rank-$p$ idempotent is determined by the pair (image $p$-plane $L$, kernel $(5-p)$-plane $K$) with $V=L\oplus K$; the pair is transverse, not nested.

**Proof.** The projection onto $L$ along $K$ has image $L$ and kernel $K$; conversely the pair determines the projection. The direct sum condition is the transversality.

### The Fibre Bundle over $\operatorname{Gr}(p,5)$

**Theorem.** The rank-$p$ idempotents form a fibre bundle over the Grassmannian $\operatorname{Gr}(p,5)$ with fibre the affine space of complements to $L$, of dimension $p(5-p)$.

**Proof.** The map $\pi:P\mapsto\operatorname{im}P$ sends the idempotent to its image $p$-plane. The fibre over $L$ is the set of $(5-p)$-planes $K$ with $V=L\oplus K$, which is an affine space of dimension $p(5-p)$: the space of linear maps $\operatorname{Hom}(\mathbb{C}^5/L,L)\cong\operatorname{Hom}(\mathbb{C}^{5-p},\mathbb{C}^p)$, dimension $p(5-p)$. The base has dimension $p(5-p)$; the total is $2p(5-p)$.

**Corollary.** The fibre is contractible; the bundle is affine, not vector; the total space has the homotopy type of the Grassmannian.

**Proof.** An affine space is contractible; the bundle is a fibre bundle with contractible fibre, so the total space deformation retracts onto the base.

**Corollary.** For $p=1$, the base is $\mathbb{P}^4$ and the fibre is the affine space of hyperplane complements, dimension $4$; the total is $8$. For $p=2$, the base is $\operatorname{Gr}(2,5)$, dimension $6$, and the fibre has dimension $6$; the total is $12$.

**Proof.** The dimensions $p(5-p)$: $4$ for $p=1$, $6$ for $p=2$; the totals are $8$ and $12$.

### The Contractible Fibre

**Proposition.** The complement of a $p$-plane $L$ in $\mathbb{C}^5$ is the affine space $\operatorname{Hom}(\mathbb{C}^5/L,L)$, which is contractible; the bundle of complements is the affine bundle associated with the tautological quotient and subbundles.

**Proof.** A complement $K$ is the graph of a linear map $\mathbb{C}^5/L\to L$; the graph is a $(5-p)$-plane transverse to $L$; every complement arises uniquely from such a map. The space of maps is a vector space, hence contractible.

**Corollary.** The idempotents of rank $p$ are the sections of the affine bundle; the zero section would be a canonical complement, which does not exist without a choice of Hermitian metric.

**Proof.** A canonical complement would be the orthogonal complement, which requires a metric; without a metric, there is no zero section.

**Remark.** **The idempotents are the transverse pairs, not the nested flags.** The image and the kernel are complementary, not nested; the nested partial flag $L\subset K$ is a different homogeneous space, of dimension $p(5-p)$ for the Grassmannian, not $2p(5-p)$. The affine bundle of complements is the geometric content of the idempotent.

## The Rank Stratification

### The Orbits

**Theorem.** The idempotent variety is the disjoint union of the $GL_5$-orbits $\mathcal{I}_p$ of rank $p$, for $p=0,\dots,5$. Each orbit is smooth of dimension $2p(5-p)$.

**Proof.** The rank is invariant under conjugation; the orbit of $\operatorname{diag}(I_p,0)$ is the set of rank-$p$ idempotents; the homogeneous space is smooth; the dimension is the orbit-stabilizer computation.

**Corollary.** The top-dimensional orbits are $p=2$ and $p=3$, of dimension $12$; the rank-one and rank-four orbits have dimension $8$; the zero and identity are the fixed points.

**Proof.** The dimensions $2p(5-p)$; the maximum at $p=2,3$; the endpoints.

### The Rank Is Locally Constant

**Proposition.** On the idempotent variety, the rank equals the trace: $\operatorname{rank}P=\operatorname{tr}P$ for $P^2=P$. The trace is continuous, so the rank is locally constant; each orbit $\mathcal{I}_p$ is open and closed in the idempotent variety.

**Proof.** The eigenvalues of an idempotent are $0$ and $1$; the trace is the number of $1$s, which is the rank. The trace is a continuous function, and an integer-valued continuous function is locally constant. The preimage of the value $p$ is open and closed.

**Corollary.** The idempotent variety is the disjoint union of the six smooth orbits $\mathcal{I}_0,\dots,\mathcal{I}_5$, of dimensions $0,8,12,12,8,0$; it is smooth but disconnected, and it is not irreducible.

**Proof.** Each orbit is a homogeneous space, hence smooth; the rank is locally constant, so the orbits are the connected components (each orbit is connected because $GL_5(\mathbb{C})$ is connected); the dimensions are $2p(5-p)$.

**Corollary.** The closure of $\mathcal{I}_p$ in $M_5$ may contain non-idempotent matrices of rank at most $p$ (for $p\ge2$), but it contains no idempotent of a different rank. The idempotent variety itself has no closure inclusions between different ranks.

**Proof.** A sequence $P_n\in\mathcal{I}_p$ has trace $p$, so its limit has trace $p$; the limit can be non-idempotent and of lower rank, but if it were idempotent its rank would be $\operatorname{tr}P=p$. The idempotent variety is closed, because $P^2=P$ is polynomial; hence no idempotent of a different rank lies in the closure.

### The Peirce Decomposition

**Theorem.** Relative to an idempotent $P$ of rank $p$, the algebra decomposes as

$$
M_5=P M_5 P\oplus P M_5(1-P)\oplus(1-P)M_5P\oplus(1-P)M_5(1-P),
$$

of dimensions $p^2$, $p(5-p)$, $p(5-p)$, $(5-p)^2$. The off-diagonal summands form the tangent space to the orbit of $P$, of dimension $2p(5-p)$; the diagonal summands form the stabilizer, of dimension $p^2+(5-p)^2$.

**Proof.** The four corners are the Peirce spaces; the multiplication table is the block multiplication. The tangent space to the conjugation orbit is $\{[X,P]:X\in\mathfrak{gl}_5\}$, which is the off-diagonal part; the stabilizer is the block diagonal part.

**Corollary.** The Peirce decomposition is the infinitesimal form of the affine bundle: the off-diagonal corners are the directions of the image and kernel, the diagonal corners the gauge directions.

**Proof.** The tangent directions change the image or the kernel; the stabilizer directions preserve the decomposition.

**Remark.** **The geometry of the idempotents is the geometry of the Peirce decomposition.** The idempotent is the projection onto the $1$-eigenspace along the $0$-eigenspace; the four corners are the four Peirce spaces; the orbit is the off-diagonal part; the stabilizer is the diagonal part. The rank stratification is the stratification by the dimension of the $1$-eigenspace.

## The Full Flag Variety

### The Flags

**Definition.** A **full flag** in $\mathbb{C}^5$ is a chain

$$
0\subset V_1\subset V_2\subset V_3\subset V_4\subset\mathbb{C}^5,
\qquad \dim V_k=k .
$$

The **full flag variety** $\mathcal{F}=GL_5/B$ is the set of full flags, where $B$ is the Borel subgroup of upper triangular matrices.

**Proposition.** $GL_5$ acts transitively on the full flags; the stabilizer of the standard flag is $B$; the flag variety is the homogeneous space $GL_5/B$.

**Proof.** A flag is the span of a basis $v_1,\dots,v_5$ with $V_k=\langle v_1,\dots,v_k\rangle$; $GL_5$ acts transitively on the bases and hence on the flags; the stabilizer of the standard flag is the group of upper triangular matrices.

**Corollary.** The flag variety is compact and projective; it is the quotient of $GL_5$ by the Borel.

**Proof.** The flag variety is a closed subvariety of a product of Grassmannians, hence projective; it is compact because $GL_5/B$ is the image of the compact unitary group $U(5)$ (the Iwasawa decomposition).

### The Dimension

**Theorem.** The full flag variety has dimension $10$:

$$
\dim GL_5/B=25-15=10 .
$$

**Proof.** The Borel $B$ has dimension $15$ (five diagonal plus ten upper-triangular entries); the quotient has dimension $25-15=10$.

**Corollary.** The dimension is also $\binom{5}{2}=10$, the number of positive roots; the flag variety is the model for the root system $A_4$.

**Proof.** $\binom{5}{2}=10$; the positive roots of $A_4$ are the ten pairs $i<j$.

**Corollary.** The full flag variety is the bundle over $\mathbb{P}^4$ with fibre $\mathbb{P}^3$, then over $\mathbb{P}^2$, and so on; the dimensions add $4+3+2+1=10$.

**Proof.** The projection to $V_1$ has fibre the flags of $\mathbb{C}^5/V_1\cong\mathbb{C}^4$; inductively the dimensions add $4+3+2+1$.

### The Borel

**Theorem.** The Borel $B=T\ltimes U$ is the stabilizer of the standard flag; the torus $T$ is the diagonal, the unipotent $U$ the upper triangular with unit diagonal. The dimensions are $5$, $10$ and $15$.

**Proof.** The upper triangular matrices preserve the standard flag; the diagonal and the unipotent parts are the semidirect product.

**Corollary.** The flag variety is the quotient of $GL_5$ by the Borel; the fibre of the frame bundle over the flag variety is $B$.

**Proof.** The frame bundle $GL_5\to GL_5/B$ has fibre $B$; the frame is a basis adapted to the flag.

## The Partial Flags and the Incidence

### The Nested Partial Flags

**Definition.** A **partial flag of type** $(d_1,\dots,d_s)$ is a chain $V_{d_1}\subset\cdots\subset V_{d_s}$ with $\dim V_{d_i}=d_i$. The **parabolic** $P$ stabilizing a partial flag is the group of block upper triangular matrices; the partial flag variety is $GL_5/P$.

**Theorem.** The dimension of the partial flag variety of type $(d_1,\dots,d_s)$ is

$$
\sum_{i=0}^{s}d_i(d_{i+1}-d_i),
\qquad d_0=0,\quad d_{s+1}=5 .
$$

**Proof.** The dimension is the sum of the dimensions of the Grassmannians of the successive quotients: $d_i(d_{i+1}-d_i)$ for each step. The sum telescopes to $\dim GL_5-\dim P$.

**Corollary.** The full flag has type $(1,2,3,4)$, dimension $1\cdot1+2\cdot1+3\cdot1+4\cdot1=10$. The Grassmannian $\operatorname{Gr}(p,5)$ has type $(p)$, dimension $p(5-p)$.

**Proof.** Evaluate the formula for the two types.

**Corollary.** The nested partial flags are not the idempotents: the nested partial flag of type $(p,5-p)$ has dimension $p(5-p)$ for the $p$-plane alone, while the rank-$p$ idempotents have dimension $2p(5-p)$. The idempotent needs the transverse kernel as well.

**Proof.** The formula gives $p(5-p)$ for the nested flag; the idempotent adds the complement, of dimension $p(5-p)$.

### The Transverse Pairs

**Theorem.** The rank-$p$ idempotents are the transverse pairs $(L,K)$ with $\dim L=p$, $\dim K=5-p$, $L\oplus K=\mathbb{C}^5$; they form the homogeneous space $GL_5/(GL_p\times GL_{5-p})$ of dimension $2p(5-p)$.

**Proof.** The pair determines the projection; the stabilizer is the block diagonal; the dimension is $2p(5-p)$.

**Corollary.** The transverse pair is not a nested partial flag; the incidence "L\subset K" is a different variety, of dimension $p(5-p)$; the transverse incidence "L\oplus K=V" is open in $\operatorname{Gr}(p,5)\times\operatorname{Gr}(5-p,5)$.

**Proof.** The nested incidence is the closed condition $L\subset K$; the transverse condition is the open condition $L\cap K=0$; the dimensions differ.

**Corollary.** The idempotent variety maps to the product of Grassmannians by $P\mapsto(\operatorname{im}P,\ker P)$; the image is the open set of transverse pairs; the map is an isomorphism onto its image.

**Proof.** The projection is determined by the transverse pair; the map is bijective onto the open set of transverse pairs.

### The Incidence Relations

**Proposition.** The incidence relations between the image and the kernel of the idempotents are the transverse incidence; the nested incidence appears in the flag variety, not in the idempotent variety.

**Proof.** The image and kernel of a projection are complementary; a nested flag has $V_p\subset V_{p+1}$, which is not the idempotent condition.

**Corollary.** The idempotents of rank $p$ are the open subset of $\operatorname{Gr}(p,5)\times\operatorname{Gr}(5-p,5)$ where the two subspaces are transverse; the closure contains the incident pairs.

**Proof.** The transverse condition is open; the boundary is the incident locus, where the subspaces meet nontrivially.

**Remark.** **The geometry of the idempotents is the geometry of the transverse pairs, and the geometry of the flags is the geometry of the nested chains.** The two are related by the incidence but are not the same. The idempotent of rank $p$ is the projection onto the first subspace along the second; the nested flag is the chain of subspaces. The affine bundle of complements is the difference.

## The Gauge and the Frame Bundle

### The Frame Bundle

**Definition.** A **frame** of $\mathbb{C}^5$ is a basis $(v_1,\dots,v_5)$; the **frame bundle** is $\mathcal{F}=GL_5$, with the projection to the flag variety sending a basis to the flag it spans.

**Theorem.** The frame bundle $GL_5\to GL_5/B$ has fibre the Borel $B=T\ltimes U$; the structure group is $B$; the frame bundle is a principal $B$-bundle.

**Proof.** The fibre over the standard flag is the set of bases adapted to the flag, which is the Borel: the diagonal rescalings and the upper triangular changes.

**Corollary.** The diagonal torus $T$ is the gauge group of the frame; the unipotent $U$ is the group of triangular changes of the frame.

**Proof.** The diagonal changes rescale the basis vectors; the unipotent changes add higher vectors to lower ones; the semidirect product is the Borel.

### The Gauge Fibre

**Theorem.** The gauge torus $T\cong(\mathbb{C}^\times)^5$ acts on the frames by rescaling the basis vectors. The centre $\mathbb{C}^\times$ acts trivially on the flag and on the projection; the effective gauge group is $T/\mathbb{C}^\times\cong(\mathbb{C}^\times)^4$, of dimension $4$.

**Proof.** The rescaling $v_k\mapsto t_kv_k$ changes the frame but not the flag if the $t_k$ are nonzero; the common scaling of all $v_k$ changes nothing in the flag or the projection. The four ratios $t_k/t_{k+1}$ are the gauge parameters.

**Corollary.** The four gauge parameters are the simple-root directions of the torus; the composites are the products; there is no fifth independent scalar.

**Proof.** The torus has dimension $5$; the centre has dimension $1$; the quotient has dimension $4$. The simple roots are the four ratios.

**Corollary.** The gauge is the fibre of the frame bundle modulo the centre; the frame bundle is the $T$-bundle over the flag variety with the four-parameter gauge fibre.

**Proof.** The frame bundle has fibre $B$; the diagonal part is $T$; the centre acts trivially on the flag; the effective gauge is $T/\mathbb{C}^\times$.

**Remark.** **The gauge is the diagonal fibre of the frame bundle.** The frame bundle $GL_5\to GL_5/B$ has the Borel as fibre; the diagonal torus is the gauge, the unipotent is the triangular change. The four parameters are the ratios of the diagonal scalings; they rescale the simple nilpotents and fix the root. The geometry of the idempotents and the flags is the geometry of the frames modulo the gauge.

## Summary

The idempotents of rank one form an affine bundle of rank $4$ over $\mathbb{P}^4$, of dimension $8$. The idempotents of rank $p$ form the homogeneous space

$$
PGL_5/P(GL_p\times GL_{5-p}),
$$

of dimension $2p(5-p)$; they are the transverse pairs $(L,K)$ with $L\oplus K=\mathbb{C}^5$, and they fibre over $\operatorname{Gr}(p,5)$ with the contractible affine fibre of complements.

$$
\boxed{\ \dim\mathcal{I}_p=2p(5-p);\quad \dim GL_5/B=10;\quad \dim\operatorname{Gr}(p,5)=p(5-p);\quad \text{gauge}=(\mathbb{C}^\times)^4.\ }
$$

The full flag variety $GL_5/B$ has dimension $10$; the nested partial flags have dimension $\sum d_i(d_{i+1}-d_i)$; the idempotents are the transverse pairs, not the nested flags. The Peirce decomposition splits the algebra into the four corners; the off-diagonal corners are the tangent space to the orbit, the diagonal corners the stabilizer. The gauge torus is the diagonal fibre of the frame bundle, of dimension $4$ modulo the centre.

| Object | Dimension |
|---|---|
| Rank-one idempotents | $8$ (affine bundle over $\mathbb{P}^4$) |
| Rank-$p$ idempotents | $2p(5-p)$ |
| $\operatorname{Gr}(p,5)$ | $p(5-p)$ |
| Full flag variety | $10$ |
| Partial flag $(d_1,\dots,d_s)$ | $\sum d_i(d_{i+1}-d_i)$ |
| Gauge torus | $4$ (effective) |
| Borel $B$ | $15$ |
| Unipotent $U$ | $10$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{I}_p$ | The rank-$p$ idempotents |
| $\operatorname{Gr}(p,5)$ | The Grassmannian of $p$-planes |
| $GL_5/B$ | The full flag variety |
| $P(GL_p\times GL_{5-p})$ | The block diagonal stabilizer |
| $T$ | The diagonal torus |
| $U$ | The unipotent group |
| $B=T\ltimes U$ | The Borel |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the flag varieties, the Grassmannians and the incidence relations.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the geometry of the Grassmannians and the flag varieties.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the homogeneous spaces and the frame bundles.
- [The Peirce Decomposition](the-peirce-decomposition-of-m5c.html), for the four corners and the multiplication table.
- [The Adjoint Action, the Orbits and the Flag Variety](the-adjoint-action-the-orbits-and-the-flag-variety-of-m5c.html), for the orbits and the flag variety.
- [The Partial Flags](the-partial-flags-of-m5c.html), for the nested partial flags and their dimensions.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m5c.html), for the gauge and the frame.
