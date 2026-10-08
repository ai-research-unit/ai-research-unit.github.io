# __The Continuous Symplectic Form and the Poisson Bracket__

## Introduction

Among the bilinear forms of the degree-2 layer, the alternating ones are those with $\omega(v,v)=0$, and the object of this article is the alternating form read with a topology, together with the bracket it induces on a commutative algebra. The algebraic theory is complete in Part I: the alternating forms have even rank, they all acquire a symplectic basis after a change of basis, the non-degenerate ones on a finite-dimensional space are all isometric, and the group preserving one is the symplectic group, contained in the special linear group because the Pfaffian forces the determinant to be one. What the topology adds is the reading of these objects as continuous forms on a topological module, the openness of the non-degenerate locus, the closedness of the symplectic group in the space of linear maps, and the continuity of the Poisson bracket and of the derivations it produces.

Two facts organise the article. The first is the contraction $\omega^{\flat} : V\to V^{*}$, $v\mapsto \omega(v,-)$, which converts the form into an operator: the form is non-degenerate exactly when the contraction is injective, the radical is its kernel and is closed when the form is continuous, and in finite dimension the contraction is a homeomorphism. The second is that the decomposition of the bilinear forms into their symmetric and their alternating parts is a **topological** decomposition when the space of forms carries its operator norm, so the layer of this article and the layer of *The Continuous Quadratic Form and the Polar Form* are complementary direct summands of one object, split by the continuous symmetrisation and antisymmetrisation maps. The Poisson bracket is then read on the other side: a continuous bracket on a commutative topological algebra is a bracket for which the Hamiltonian derivations are continuous and the Poisson centre is closed.

The article defines the continuous alternating form, proves the contraction theorem and the topological splitting of the bilinear forms, treats the non-degenerate locus, the Pfaffian and the symplectic group, constructs the canonical form on a module and its dual, and reads the Poisson bracket topologically. It owns no quadratic form of its own — that is *The Continuous Quadratic Form and the Polar Form* — and no Clifford algebra. The closedness of a symplectic form, the Darboux theorem and the Lagrangian geometry are not treated here: the first is a statement about the exterior derivative and belongs to Analysis, the others to Geometry. The algebraic theory is *Bilinear Forms*, §*Alternating Forms*, *Symplectic Forms and Poisson Brackets* and *Exterior Powers*; the symplectic reflection algebras and the rational Cherednik algebras of the same Part I category are algebraic objects with no separate topological layer, and their transcendental realisations are deferred to Analysis. Throughout, $F$ is a topological field of characteristic not $2$, $V$ a topological $F$-module with a continuous scalar action, and $\omega$ a continuous alternating bilinear form.

## The Continuous Alternating Form

### Definition and the Contraction

**Definition.** Let $F$ be a topological field and $V$ a topological $F$-module. A **continuous alternating form** is a bilinear map $\omega : V\times V\to F$ that is continuous and satisfies $\omega(v,v)=0$ for every $v$. The **contraction** of $\omega$ is the map

$$
\omega^{\flat} : V\to V^{*}, \qquad \omega^{\flat}(v)(w) = \omega(v,w),
$$

into the algebraic dual of *Bilinear Forms*, §*Rank and the Radical*; when $V$ carries a norm and the form is continuous, the image lies in the continuous dual $V'$. The **radical** is $\operatorname{rad}(\omega)=\{v : \omega(v,w)=0 \text{ for every } w\}$.

The definition is the algebraic one of *Bilinear Forms*, §*Alternating Forms*, with the continuity added. Alternation is stated through $\omega(v,v)=0$ rather than through skew-symmetry, since the two agree in characteristic not $2$ and the first is the condition available over every base, as *Exterior Powers* records. The contraction is the form read in one slot, and it is the device that makes the topology of the form a statement about an operator.

**Proposition (the contraction is continuous).** Let $\omega$ be a continuous alternating form. Then $\omega^{\flat}$ is a continuous linear map $V\to V^{*}$ when $V^{*}$ carries the topology of uniform convergence on the unit ball of $V$, and $\ker\omega^{\flat}=\operatorname{rad}(\omega)$; the radical is closed. In particular $\omega$ is non-degenerate if and only if $\omega^{\flat}$ is injective.

*Proof.* The linearity of $\omega^{\flat}$ in $v$ is the bilinearity of $\omega$, and its continuity is the continuity of $\omega$: if $v_{n}\to v$ then $\omega(v_{n},w)\to\omega(v,w)$ uniformly over $\lVert w\rVert\le1$, since $\lvert\omega(v_{n},w)-\omega(v,w)\rvert=\lvert\omega(v_{n}-v,w)\rvert\le\lVert\omega\rVert\lVert v_{n}-v\rVert$, and the bound is uniform in $w$ by the operator norm. The kernel is the radical by the definition of the two, and the radical is closed because it is the intersection of the closed kernels of the continuous maps $v\mapsto\omega(v,w)$. $\square$

**Remark (finite dimension).** When $V$ is finite-dimensional and Hausdorff over a complete valued field, $\omega^{\flat}$ is a continuous linear map between spaces of the same finite dimension, so injective, surjective and homeomorphic are equivalent, and a non-degenerate form is exactly one whose contraction is an isomorphism $V\to V^{*}$. In infinite dimension the three separate: an injective contraction need not be onto and its image need not be closed, and a non-degenerate continuous form can fail to be an isomorphism onto the dual. The strong and the weak topologies of the dual enter here, and the dual-pairing statements are owned by the article on the duality of topological linear spaces; the layer itself keeps only the injectivity.

### The Topological Splitting of the Bilinear Forms

**Definition.** The **transpose** of a bilinear form $B$ is $B^{\intercal}(x,y)=B(y,x)$, as in *Bilinear Forms*, §*Bilinear Forms*; $B$ is **symmetric** when $B^{\intercal}=B$ and **alternating** when $B+B^{\intercal}=0$ and $B(x,x)=0$. The **symmetrisation** and the **antisymmetrisation** are

$$
B^{\mathrm{s}} = \tfrac{1}{2}(B+B^{\intercal}), \qquad B^{\mathrm{a}} = \tfrac{1}{2}(B-B^{\intercal}) .
$$

**Theorem (topological splitting).** Let $V$ be a normed space over $\mathbb{R}$ and let $\operatorname{Bil}(V)$ carry the operator norm. The symmetrisation and the antisymmetrisation are continuous linear projections, they commute, and

$$
\operatorname{Bil}(V) = \operatorname{Sym}(V)\oplus\operatorname{Alt}(V)
$$

is a topological direct sum, the norm of each projection being $1$. The polar forms of the quadratic forms are exactly the symmetric summand, and the summand of the alternating forms is the object of this article.

*Proof.* The maps are linear in $B$ and $\lVert B^{\mathrm{s}}\rVert\le\tfrac12(\lVert B\rVert+\lVert B^{\intercal}\rVert)=\lVert B\rVert$ because transposition preserves the operator norm, and $\lVert B^{\mathrm{a}}\rVert\le\lVert B\rVert$ likewise. The identities $(B^{\mathrm{s}})^{\mathrm{s}}=B^{\mathrm{s}}$, $(B^{\mathrm{a}})^{\mathrm{a}}=B^{\mathrm{a}}$ and $B^{\mathrm{s}}+B^{\mathrm{a}}=B$ hold algebraically, and the two projections annihilate each other's image; the images are closed, the symmetric forms being the fixed locus of the continuous involution $B\mapsto B^{\intercal}$, and a direct sum of two closed subspaces split by continuous projections is topological. $\square$

**Corollary (an alternating form is never a polar form).** An alternating form on a space of characteristic not $2$ is the polar form of a quadratic form only if it is zero.

*Proof.* The polar form of a quadratic form is symmetric, by the symmetry of the identity $B(x,y)=\tfrac12(q(x+y)-q(x)-q(y))$, and a form that is both symmetric and alternating satisfies $B=-B^{\intercal}=-B$, hence $2B=0$ and $B=0$ because $2$ is invertible. $\square$

The corollary is the reason the two articles of the category are disjoint in their content and not merely distinct in their emphasis: the layer of this article is the second summand of the degree-2 forms, and the symplectic structure on a vector space is not the quadratic structure on the same space.

## The Non-Degenerate Locus

### Rank and the Openness of the Symplectic Forms

**Definition.** The **rank** of a bilinear form $B$ on a module of finite rank is the rank of its Gram matrix, equivalently the codimension of its radical; it is even for an alternating form, by *Bilinear Forms*, §*Alternating Forms*.

**Theorem.** Let $V=F^{2n}$ and let $\operatorname{Alt}(V)$ be the space of alternating forms with the operator norm. The rank is lower semicontinuous: for each $k$ the set $\{\operatorname{rank}\ge k\}$ is open. Consequently the set of **symplectic forms**, that is, of non-degenerate alternating forms, is open in $\operatorname{Alt}(V)$, and over $F=\mathbb{R}$ it has exactly two connected components.

*Proof.* The rank is at least $k$ exactly when some $k\times k$ minor of the Gram matrix is nonzero; each minor is a continuous function of the entries, so each set $\{\text{minor}\neq0\}$ is open, and $\{\operatorname{rank}\ge k\}$ is their union over the finitely many choices of rows and columns, hence open. For an alternating form of rank $2n$ the Gram matrix is invertible, so the non-degenerate forms are the open set $\{\operatorname{rank}\ge 2n\}$. The **Pfaffian** $\operatorname{Pf}$ of *Symplectic Forms and Poisson Brackets*, §*The Pfaffian and the Volume Form* is a polynomial in the entries and satisfies $\operatorname{Pf}(\Omega)^{2}=\det\Omega$, so on the non-degenerate locus it is a continuous function with no zeros; over $\mathbb{R}$ its sign cannot change, and the two signs give two open and closed pieces. The symplectic group acts transitively on $\{\operatorname{Pf}=1\}$, because it acts transitively on symplectic bases, so each piece is connected and there are no more than two components. $\square$

**Remark.** The sign of the Pfaffian is an orientation of the space, and the two components are the two orientations; the statement is the alternating counterpart of the local constancy of the signature in *The Continuous Quadratic Form and the Polar Form*, §*The Space of Continuous Forms*. It is the topological input to the symplectic entry of *The Topological Witt Group and the Brauer–Wall Group*, where the forms modulo hyperbolic ones are considered.

## The Symplectic Group

### The Group as a Closed Subgroup

**Definition.** The **symplectic group** of a symplectic space $(V,\omega)$ is $\mathrm{Sp}(V,\omega)=\{T\in GL(V) : \omega(Tx,Ty)=\omega(x,y)\text{ for all }x,y\}$, as in *Symplectic Forms and Poisson Brackets*, §*The Symplectic Group*.

**Proposition.** Let $\omega$ be a continuous alternating form on a topological module $V$ and let $\mathrm{Sp}(V,\omega)$ carry the topology induced from the space of continuous linear maps with the operator norm. Then $\mathrm{Sp}(V,\omega)$ is a closed subgroup of $GL(V)$, the group of invertible elements of the topological algebra $\operatorname{End}(V)$, and it is a topological group for the induced operations.

*Proof.* For each pair $(x,y)$ the map $T\mapsto\omega(Tx,Ty)-\omega(x,y)$ is continuous, being a composite of the evaluation and the continuous form, so the set where it vanishes is closed; intersecting over a set of pairs that spans $V\times V$ exhibits the set of all linear $T$ preserving $\omega$ as an intersection of closed sets, and the group is its intersection with the closed set $GL(V)$ of invertible elements of the topological algebra $\operatorname{End}(V)$. The multiplication and the inversion of a topological group of operators are continuous, so the induced operations make the set a topological group. $\square$

**Corollary (the relation to the special linear group).** A symplectic transformation has determinant one, and $\mathrm{Sp}(V,\omega)\subseteq \mathrm{SL}(V)$ is a closed subgroup; in finite dimension over a complete valued field $\mathrm{Sp}(V,\omega)$ is a closed subset of the finite-dimensional space of matrices, hence locally compact.

*Proof.* The determinant of a symplectic matrix is one by the Pfaffian identity $\operatorname{Pf}(\Omega)^{2}=\det\Omega$ and the invariance $\operatorname{Pf}(T^{\intercal}\Omega T)=\det(T)\operatorname{Pf}(\Omega)$, which is the algebraic statement of *Symplectic Forms and Poisson Brackets*. Since $\det$ is continuous, $\mathrm{SL}(V)$ is closed, and the symplectic group is a closed subgroup of it; a closed subset of a finite-dimensional Hausdorff vector space is locally compact. $\square$

**Remark (the action and the two-fold covers).** The action $\mathrm{Sp}(V,\omega)\times V\to V$ is continuous, being the restriction of the continuous evaluation of operators. The group is connected in the classical cases, and its simply-connected covering group, the metaplectic group, is a topological double cover; the covering-theoretic treatment is the one of *The Topological Orthogonal Group and the Spin Group*, §*The Two-Fold Covering by Pin and Spin*, read for the symplectic form, and the present article keeps only the closedness, since the covering belongs with the groups and their topology. The measure-theoretic statements about the metaplectic representation are Analysis and are not read here.

## The Canonical Form on a Module and its Dual

### The Hyperbolic Module

**Theorem.** Let $M$ be a normed space over $\mathbb{R}$ and let $M'$ be its continuous dual with the dual norm. The form

$$
\omega\bigl((x,f),(y,g)\bigr) = g(x) - f(y)
$$

on $M\oplus M'$ is continuous, alternating, and non-degenerate.

*Proof.* Continuity: $\lvert g(x)-f(y)\rvert\le\lVert g\rVert\lVert x\rVert+\lVert f\rVert\lVert y\rVert$, which is a continuous function of the pair. Alternation is immediate by inserting $(x,f)$ twice. Non-degeneracy: if $(x,f)$ pairs to zero with every $(y,g)$, then taking $g=0$ gives $f(y)=0$ for every $y$, so $f=0$, and taking $y=0$ gives $g(x)=0$ for every $g\in M'$; by the Hahn–Banach separation theorem a vector annihilated by every continuous functional is zero, so $x=0$. $\square$

**Remark.** The module $M\oplus M'$ with this form is the topological form of the **hyperbolic plane** of *Bilinear Forms*, §*Alternating Forms*, read with a dual in place of a second copy of the same space. In finite dimension $M'$ is the dual of the same dimension as $M$, the form is the standard symplectic form of *Symplectic Forms and Poisson Brackets*, §*The Standard Symplectic Form* in the symplectic basis $e_{i},f_{i}$, and the module is $\mathbb{R}^{2n}$ itself. The construction is the reason the symplectic forms of a free module of finite rank are classified by the dimension alone, the completion of the module adding nothing to the classification of the form.

## The Continuous Poisson Bracket

### The Bracket and the Hamiltonian Derivations

**Definition.** Let $A$ be a commutative topological $F$-algebra with a continuous product. A **continuous Poisson bracket** on $A$ is a bilinear, alternating, continuous map $\{\cdot,\cdot\} : A\times A\to A$ that is a derivation in each argument, $\{f,gh\}=\{f,g\}h+g\{f,h\}$ and $\{fg,h\}=f\{g,h\}+\{f,h\}g$, and satisfies the Jacobi identity; the algebraic definition is *Symplectic Forms and Poisson Brackets*, §*The Poisson Bracket*. The **Poisson centre** is $Z=\{f : \{f,g\}=0 \text{ for every } g\}$, and the **Hamiltonian derivation** of $f$ is $X_{f}(g)=\{f,g\}$.

**Proposition.** Let $\{\cdot,\cdot\}$ be a continuous Poisson bracket on $A$. Then each Hamiltonian derivation $X_{f}$ is a continuous derivation of $A$, the map $X : A\to\operatorname{Der}(A)$, $f\mapsto X_{f}$, is linear and continuous for the topology of pointwise convergence on $\operatorname{Der}(A)$, its kernel is the Poisson centre, and

$$
X_{\{f,g\}} = [X_{f},X_{g}] .
$$

*Proof.* The derivation property is the algebraic one, and continuity is the continuity of the bracket in its second variable with $f$ fixed. Linearity of $X$ is the bilinearity of the bracket, and continuity is the pointwise continuity of $g\mapsto\{f,g\}$ uniformly over $f$ in a bounded set. The kernel is the centre by the definition of both. The displayed identity is the Jacobi identity, as in *Symplectic Forms and Poisson Brackets*, §*The Poisson Bracket*, and it holds in the topological algebra because it is a polynomial identity. $\square$

**Corollary.** Endow $A$ with the bracket. Then $A$ is a topological Lie algebra, $X$ is a continuous homomorphism of Lie algebras onto the ideal of Hamiltonian derivations, and both the Poisson centre and the closure of the image of $X$ are Lie subalgebras.

*Proof.* The bracket is bilinear, alternating and continuous and satisfies Jacobi, which is the definition of a topological Lie algebra. The map $X$ is a homomorphism by the proposition, its kernel is the centre, so its image is isomorphic as a Lie algebra to $A/Z$; an ideal, and the closure of a Lie subalgebra of a topological Lie algebra is a Lie subalgebra, by the continuity of the bracket. $\square$

**Remark (the bracket of a symplectic form).** When $A$ is the algebra of polynomial functions on a symplectic space and the bracket is defined from $\omega$ by the inverse of the contraction, the derivations $X_{f}$ are the Hamiltonian vector fields and the construction is the one of *Symplectic Forms and Poisson Brackets*, §*The Poisson Bracket*. The topological content added here is the continuity of the bracket and of the Hamiltonian map; the integration of the vector fields, which is where the trajectories appear, is Analysis and is not read.

## Examples

### The Standard Real and Complex Cases

**Example.** Let $V=\mathbb{R}^{2n}$ with the Euclidean topology and $\omega$ the standard symplectic form $\sum_{i}x_{i}\wedge y_{i}$ of *Symplectic Forms and Poisson Brackets*, §*The Standard Symplectic Form*. The form is continuous, its Gram matrix $\Omega = \begin{pmatrix}0&I\\-I&0\end{pmatrix}$ is invertible, so $\omega^{\flat}$ is a homeomorphism onto the algebraic dual; the symplectic group $\mathrm{Sp}_{2n}(\mathbb{R})$ is a closed subgroup of $M_{2n}(\mathbb{R})$, hence locally compact, and it is contained in $\mathrm{SL}_{2n}(\mathbb{R})$ by the Pfaffian. The set of non-degenerate alternating forms on $\mathbb{R}^{2n}$ has two components, distinguished by the sign of the Pfaffian, and the level set $\{\operatorname{Pf}=1\}$ is a single orbit under the group.

**Example (the complex case).** Let $V=\mathbb{C}^{n}$ with its Euclidean topology, read as a real vector space of dimension $2n$, and let $\omega$ be the imaginary part of the standard Hermitian form. The form is continuous and alternating, and it is non-degenerate; the structure is the Hermitian one read on its imaginary part, and the Hermitian form itself belongs to *Topology on Sesqualgebras with a degree-2 form*, where the conjugate slot is available. The reading here uses only the alternating form, which is why it lives in the present category.

### The Degenerate and the Exterior Cases

**Example (the rank-two degenerations).** Let $V=\mathbb{R}^{4}$ and let $\omega$ be the alternating form $\omega = e_{1}\wedge f_{1}$ in the standard coordinates, that is, the form of rank two. Its contraction has a two-dimensional kernel and two-dimensional image; the form is neither zero nor non-degenerate, the set of its rank is the stratum $\{\operatorname{rank}=2\}$, which is neither open nor closed, and the radical is the closed subspace spanned by $e_{2},f_{2}$. The decomposition $V=H\perp H^{\perp}$ of *Bilinear Forms*, §*Alternating Forms* is a topological direct sum, $H$ the non-degenerate plane and $H^{\perp}$ the radical, since both are closed and the sum is direct.

**Example (the zero form and the exterior algebra).** Let $\omega=0$. The contraction is zero, the radical is all of $V$, and the alternating form is the polar form of no quadratic form except the zero one, by the corollary above; the object is the degenerate end of the layer, and the symplectic group is all of $GL(V)$, since the invariance condition is vacuous. It is the alternating counterpart of the collapse of *Topological Clifford Algebras*, §*The Collapse and the Boundary* at the zero form.

## Summary

A **continuous alternating form** is an alternating bilinear form that is also a continuous map, and its **contraction** $\omega^{\flat}(v)=\omega(v,-)$ is a continuous linear map to the dual whose kernel is the radical; the form is non-degenerate exactly when the contraction is injective, and in finite dimension this is equivalent to its being a homeomorphism. The **radical** is closed in a Hausdorff module. The bilinear forms split as a **topological direct sum** of the symmetric and the alternating ones, by continuous projections of norm one, so the quadratic layer and the symplectic layer are complementary pieces of one object and an alternating form is the polar form of a quadratic form only when it is zero.

The **rank** is lower semicontinuous and the **symplectic forms** are open; over $\mathbb{R}$ the sign of the **Pfaffian** splits them into exactly two connected components, the two orientations, each a single orbit of the symplectic group. The **symplectic group** is closed in the invertible continuous linear maps, is contained in the special linear group, and is locally compact in finite dimension over a complete valued field; the metaplectic double cover is named and deferred to *The Topological Orthogonal Group and the Spin Group*. The **canonical form** $g(x)-f(y)$ on a module and its continuous dual is continuous, alternating and non-degenerate, and it is the topological form of the hyperbolic plane.

A **continuous Poisson bracket** on a commutative topological algebra is a continuous alternating derivation bracket satisfying Jacobi; the **Hamiltonian derivations** $X_{f}$ are continuous, the map $f\mapsto X_{f}$ is a continuous homomorphism of Lie algebras with the **Poisson centre** as kernel, and the closure of its image is a Lie subalgebra. The closedness of a symplectic form, the Darboux theorem, the Lagrangian Grassmannian as a geometric object and the metaplectic representation are not owned here: the first is Analysis, the others Geometry.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\omega$ | a continuous alternating bilinear form |
| $\omega^{\flat}:V\to V^{*}$ | the contraction, continuous, of kernel the radical |
| $\operatorname{rad}(\omega)$ | the radical, closed in a Hausdorff module |
| $B^{\mathrm{s}}$, $B^{\mathrm{a}}$ | the symmetrisation and the antisymmetrisation, continuous projections of norm one |
| $\operatorname{Sym}(V)\oplus\operatorname{Alt}(V)$ | the topological splitting of the bilinear forms |
| rank, $\operatorname{Pf}(\Omega)$ | the lower semicontinuous rank; the Pfaffian, with $\operatorname{Pf}^{2}=\det$ |
| $\mathrm{Sp}(V,\omega)$, $\mathrm{SL}(V)$ | the closed symplectic group, contained in the special linear group |
| $M\oplus M'$ | the hyperbolic module, with $\omega=g(x)-f(y)$ |
| $\{\cdot,\cdot\}$, $X_{f}$, $Z$ | the continuous Poisson bracket, the Hamiltonian derivation, the Poisson centre |

## Further Reading

- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the dual norm, the evaluation pairing and the Hahn–Banach separation theorem.
- Nicolas Bourbaki, *Topological Vector Spaces* (Springer, 1987), for the topology of a space of bilinear maps and the topological direct sum.
- Sergei Tabachnikov, *Geometry and Billiards* (American Mathematical Society, 2005), for the linear symplectic structure and the symplectic group.
- Maurice A. de Gosson, *Symplectic Geometry and Quantum Mechanics* (Birkhäuser, 2006), for the metaplectic group as a two-fold covering of the symplectic group, noted here and deferred.
- Izu Vaisman, *Lectures on the Geometry of Poisson Manifolds* (Birkhäuser, 1994), for the Hamiltonian derivations and the Poisson centre.
- Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd edition (Oxford University Press, 2017), for the Darboux theorem and the symplectic geometry that this article does not own.
