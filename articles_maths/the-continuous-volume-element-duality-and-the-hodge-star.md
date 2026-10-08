# __The Continuous Volume Element, Duality and the Hodge Star__

## Introduction

The top grade of the Clifford algebra of a non-degenerate quadratic form on an $n$-dimensional space is one-dimensional, and an element that spans it is a **volume element**; multiplication by it is a bijection from each grade to the complementary grade, and normalised by its inverse it is the **Hodge star**. The algebraic theory of that operation is in Part I: the square of the star is a scalar determined by the form, the star is an involution when that scalar is $+1$ and a complex structure when it is $-1$, the self-dual and anti-self-dual parts appear where it is an involution, the cross product of three-dimensional space is the star of an outer product, and in the biquaternion algebra the star is multiplication by $-i$. This article reads the same object with a topology, and it is the topology that the article owns: the continuity of the volume element as a function of the orthogonal frame, the homeomorphism property of the complement map and of the star, the **duality pairing** between a grade and its complement, and the topological nature of the two cases of the square.

Three facts are the substance of the article. The first is that the volume element depends continuously on the frame that defines it, that the set of volume elements is the open set of units of the one-dimensional top grade, and that the assignment of the star to the volume element is continuous there; the star is thus not a single operator but a continuous family of operators over a two-component parameter, the two components being the two orientations, and the sign reversal $\omega\mapsto-\omega$ changes the star by a sign. The second is the duality pairing $\mathrm{Cl}_{k}\times\mathrm{Cl}_{n-k}\to F$, $(x,y)\mapsto\langle xy\rangle_{n}$, which is continuous and non-degenerate and therefore exhibits each grade as the continuous dual of its complement, in the finite-dimensional case where the two have the same dimension; the pairing is the reason the word duality belongs in the title, and it is the topological form of the complement map. The third is that the two cases $\star^{2}=\pm1$ are topological statements about the algebra: in the involutive case the projections $\tfrac12(\mathrm{id}\pm\star)$ are continuous and split the grade as a topological direct sum of its self-dual and its anti-self-dual part, and in the complex case the star is a continuous complex structure, so the grade is a topological complex vector space with the star as multiplication by $i$.

The article treats the volume element and its continuity, the complement map and the duality pairing, the star and the topological reading of its square, the real and the complex structures, the cross product, and the failure of the whole construction in infinite dimension, where there is no top grade. The grade decomposition and the filtration are *The Continuous Grade Decomposition and the Filtration*; the algebraic statements are *The Volume Element, Duality and the Hodge Star*, *The Hodge Star and the Real Structure of the Exterior Algebra* and *The Clifford Algebra Representation*; the function-theoretic Hodge star — the differential forms of a manifold, the codifferential, the Laplacian, harmonic forms and the Hodge theorem — is not read here at all, since it belongs to Analysis and to Geometry, and the article says so. The Euclidean form, the norm of a blade and the isometry property of the star belong to the Hermitian layer, *The Blade Form and the Hermitian Structure with Hermitian Adjoint* and *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*, and are named and deferred. Throughout, $F$ is a topological field of characteristic not $2$ or $0$ as the antisymmetrisation requires, $V$ is a finite-dimensional space of dimension $n$, $q$ is a non-degenerate quadratic form and the volume element is that of an orthogonal basis of *The Volume Element, Duality and the Hodge Star*, §*The Complement Map*.

## The Volume Element and its Continuity

### The Volume Element of a Frame

**Definition.** Let $e_{1},\dots,e_{n}$ be an orthogonal basis of $V$ and put

$$
\omega = e_{1}e_{2}\cdots e_{n}, \qquad \omega^{2} = (-1)^{n(n-1)/2}\prod_{i}q(e_{i}) ,
$$

the **volume element**, also called the pseudoscalar, as in *The Volume Element, Duality and the Hodge Star*, §*The Complement Map*. It is a unit of the algebra because $\omega^{2}\neq0$ for a non-degenerate form, with $\omega^{-1}=\omega/\omega^{2}$, and it spans the top grade $\mathrm{Cl}_{n}(V,q)$.

**Proposition (the volume element depends continuously on the frame).** Let $\mathrm{Fr}(V)$ be the set of orthogonal frames, a subset of $V^{n}$ carrying the product topology, and let $\Phi : \mathrm{Fr}(V)\to\mathrm{Cl}(V,q)$ be the map $(e_{1},\dots,e_{n})\mapsto e_{1}\cdots e_{n}$. Then $\Phi$ is continuous.

*Proof.* The product of the algebra is bilinear, and a multilinear map on a finite product of finite-dimensional spaces is continuous; the composite of the $n$-fold product map with the inclusion of the frame is therefore continuous. The set of orthogonal frames is the preimage of the closed set where the polar form vanishes off the diagonal and is nonzero on the diagonal, hence a closed condition intersected with the open condition of linear independence; its exact topology does not matter for the continuity of $\Phi$, which holds on all of $V^{n}$. $\square$

**Proposition (the volume elements form an open set).** The set $U$ of volume elements of the algebra, that is, the set of units of the top grade, is open in the one-dimensional space $\mathrm{Cl}_{n}(V,q)$ and equals $\mathrm{Cl}_{n}(V,q)\setminus\{0\}$; over $\mathbb{R}$ it has two connected components, $\{\lambda\omega : \lambda>0\}$ and $\{\lambda\omega : \lambda<0\}$, which are the two orientations of $V$. The assignment $\omega\mapsto\star_{\omega}$, $\star_{\omega}(A)=A\omega^{-1}$, is continuous on $U$.

*Proof.* The regular representation $x\mapsto L_{x}$ is an injective linear map of the algebra into $\operatorname{End}(\mathrm{Cl}(V,q))$, since $L_{x}=0$ implies $x=L_{x}(1)=0$; the units of the algebra are the preimage of the open set of invertible endomorphisms, hence open, and their intersection with the top grade is $\mathrm{Cl}_{n}\setminus\{0\}$ because every nonzero element of a one-dimensional space is a unit when the ambient algebra is unital and finite-dimensional. The one-dimensional real space minus the origin has two components, and the star is the composite of the continuous inverse and the continuous left multiplication, hence continuous in the pair $(\omega,A)$ and in particular in $\omega$ for fixed $A$. $\square$

**Remark (the star changes sign with the orientation).** Reversing the orientation of the frame replaces $\omega$ by $-\omega$ and hence $\star$ by $-\star$; the star is therefore not a function of the form alone but a section of a two-fold covering over the space of orientations, and the sign of the star is exactly the orientation. This is the topological form of the statement of *The Volume Element, Duality and the Hodge Star*, §*The Hodge Star* that the map depends on the orientation.

## The Complement Map and the Duality Pairing

### The Complement Map

**Definition.** For $A\in\mathrm{Cl}(V,q)$ the **right complement** is $A\omega$ and the **left complement** is $\omega A$, as in *The Volume Element, Duality and the Hodge Star*, §*The Complement Map*.

**Theorem (the complement map is a homeomorphism).** Let $A$ have grade $k$. Then $A\omega$ and $\omega A$ have grade $n-k$, and the maps $A\mapsto A\omega$ and $A\mapsto\omega A$ are continuous linear isomorphisms $\mathrm{Cl}_{k}(V,q)\to\mathrm{Cl}_{n-k}(V,q)$ whose inverses are continuous.

*Proof.* The algebraic statement, that multiplication by $\omega$ lowers the grade to its complement and is a bijection, is the theorem of *The Volume Element, Duality and the Hodge Star*, §*The Complement Map*. Continuity: the algebra is finite-dimensional over a topological field, so every linear map on it is continuous, and a linear isomorphism between spaces of the same finite dimension has a linear inverse, which is likewise continuous. $\square$

### The Duality Pairing

**Definition.** The **duality pairing** of the grades $k$ and $n-k$ is

$$
\beta_{k} : \mathrm{Cl}_{k}(V,q)\times\mathrm{Cl}_{n-k}(V,q)\to F, \qquad \beta_{k}(x,y)\,\omega = \langle xy\rangle_{n} ,
$$

where $\langle\cdot\rangle_{n}$ is the grade projection onto the top grade of *The Continuous Grade Decomposition and the Filtration*, §*The Grade Projections*, and the top grade is identified with $F$ through the chosen volume element; the pairing depends on the choice of $\omega$ by the same sign as the orientation.

**Theorem.** The pairing $\beta_{k}$ is bilinear and continuous, and it is non-degenerate; consequently the induced map $x\mapsto\beta_{k}(x,-)$ is a continuous linear isomorphism $\mathrm{Cl}_{k}(V,q)\to(\mathrm{Cl}_{n-k}(V,q))^{*}$ of the grade onto the dual of its complement.

*Proof.* Bilinearity is the bilinearity of the product and the linearity of the grade projection. Continuity is automatic in finite dimension, the pairing being bilinear on a finite product of finite-dimensional spaces. For non-degeneracy, let $x\neq0$ in grade $k$ and choose a basis blade $e_{I}$ with nonzero coefficient in $x$; then $\beta_{k}(e_{I},e_{J})=\pm1$ for $J$ the complementary index set, since $e_{I}e_{J}=\pm\omega$ with a sign that is $\pm1$ for an orthogonal basis, by the computation of *The Volume Element, Duality and the Hodge Star*, §*The Complement Map*. Hence $\beta_{k}(x,e_{J})\neq0$ for that $J$, so $x$ is not annihilated; the same argument on the other side, using $\omega$ central up to sign, shows that a nonzero $y$ in grade $n-k$ is not annihilated either. A bilinear form on finite-dimensional spaces of equal dimension is non-degenerate if and only if the induced map to the dual is injective, hence bijective, and the inverse is linear and therefore continuous. $\square$

**Corollary (the duality of the exterior algebra).** Under the symbol map of *The Continuous Grade Decomposition and the Filtration*, §*The Symbol Map and the Two Topologies*, the duality pairing is the wedge pairing $\Lambda^{k}V\times\Lambda^{n-k}V\to\Lambda^{n}V\cong F$ of *The Exterior Algebra*, §*The Wedge Product*, up to the signs of the normalisation; the pairing is therefore continuous in both readings.

*Proof.* The symbol map is an isomorphism of graded vector spaces carrying the Clifford product to the wedge product on the grades, and the top-grade component is the top-degree component; the signs are those recorded in *The Volume Element, Duality and the Hodge Star*, §*The Hodge Star*, and the continuity is that of the finite-dimensional case. $\square$

## The Hodge Star and the Topology of its Square

### The Star

**Definition.** The **Hodge star** of the volume element $\omega$ is the linear map

$$
\star : \mathrm{Cl}(V,q)\to\mathrm{Cl}(V,q), \qquad \star A = A\omega^{-1} ,
$$

homogeneous of degree $-2k$ on the grade $k$ in the sense that it maps $\mathrm{Cl}_{k}$ to $\mathrm{Cl}_{n-k}$, as in *The Volume Element, Duality and the Hodge Star*, §*The Hodge Star*; it is continuous, being linear on a finite-dimensional space, and it is a homeomorphism with inverse $\star^{-1}$ of the same form for $\omega^{-1}$.

**Theorem (the square).** On the grade $\mathrm{Cl}_{k}(V,q)$ one has $\star\star=(\omega^{2})^{-1}\mathrm{id}$, a scalar; when $\omega^{2}=1$ the star is an involution on the algebra, when $\omega^{2}=-1$ it is a complex structure, and in general it is a scalar multiple of one of the two on each grade.

*Proof.* The computation $\star\star A=A\omega^{-2}=(\omega^{2})^{-1}A$ is that of *The Volume Element, Duality and the Hodge Star*, §*The Hodge Star*, and the scalar commutes with $A$ because $\omega^{2}$ is central. The two cases are then the definitions of an involution and of a complex structure, and in the remaining cases $(\omega^{2})^{-1}$ is a scalar which is neither $1$ nor $-1$ and the star has square an arbitrary scalar, so no order-two statement is available. $\square$

### The Two Cases as Topological Decompositions

**Theorem (the involutive case).** Let $\omega^{2}=1$, so that $\star$ is an involution. Then the spectral projections $\tfrac12(\mathrm{id}\pm\star)$ are continuous linear maps and

$$
\mathrm{Cl}_{k}(V,q) = \mathrm{Cl}_{k}^{+}\oplus\mathrm{Cl}_{k}^{-}, \qquad \mathrm{Cl}_{k}^{\pm}=\{x : \star x=\pm x\} ,
$$

is a topological direct sum of the self-dual and the anti-self-dual parts; the two are interchanged by an orientation-reversing isometry and preserved by an orientation-preserving one.

*Proof.* A linear involution on a vector space over a field of characteristic not $2$ is diagonalisable with eigenvalues $\pm1$ and its spectral projections are $\tfrac12(\mathrm{id}\pm\star)$, which are continuous because $\star$ is; a direct sum split by continuous projections is topological, and the eigenspaces are closed. The action of an isometry is the algebraic statement of *The Hodge Star and the Real Structure of the Exterior Algebra*, §*The Real Structure*, transported along the symbol isomorphism, which is continuous. $\square$

**Theorem (the complex case).** Let $\omega^{2}=-1$, so that $\star$ is a complex structure. Then the grade $\mathrm{Cl}_{k}(V,q)$ is a topological complex vector space with $i$ acting as $\star$, the action $\mathbb{C}\times\mathrm{Cl}_{k}\to\mathrm{Cl}_{k}$, $(a+ib,x)\mapsto ax+b\star x$, is continuous, the complex dimension is $\tfrac{1}{2}\dim\mathrm{Cl}_{k}$ when the dimension is even, and $\star$ is complex-linear.

*Proof.* The algebraic statements are *The Hodge Star and the Real Structure of the Exterior Algebra*, §*The Complex Structure*: an operator with square $-1$ defines a module structure over $F[i]$ with $i$ acting as the operator, and the minimal polynomial divides $T^{2}+1$, halving the dimension. The continuity of the scalar action is the continuity of the two operations that define it, the multiplication by the scalar and the operator $\star$. $\square$

**Corollary (the middle degrees).** For $n$ even and $k=n/2$ the sign $\star^{2}=(-1)^{n^{2}/4}$ separates the two cases: for $n\equiv0\pmod4$ the middle grade splits as a topological direct sum of two self-dual parts of equal dimension, and for $n\equiv2\pmod4$ it is a topological complex vector space. In particular the six-dimensional space of bivectors of $\mathrm{Cl}_{4,0}$ is the topological direct sum of two three-dimensional parts, and the middle grade of $\mathrm{Cl}_{0,6}$ is a complex space of complex dimension ten.

*Proof.* The sign is computed in *The Hodge Star and the Real Structure of the Exterior Algebra*, §*The Middle Degree*, and the topological statements are the two theorems above read at $k=n/2$; the dimensions are those of the same article. $\square$

**Remark (the star as an isometry).** The statement that the star preserves the scalar form of the algebra is a statement about the **Hermitian** layer, where the blade form and its positivity make the words *isometry* and *norm* meaningful; it is owned by *The Blade Form and the Hermitian Structure with Hermitian Adjoint* and by *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*, and it is not read here. What is read here is what needs no positivity: the continuity, the homeomorphism property and the two order-two cases.

## The Cross Product and the Exterior Reading

**Definition.** The **cross product** on a three-dimensional space is $a\times b=\star(a\wedge b)=a\wedge b\,\omega^{-1}$, as in *The Volume Element, Duality and the Hodge Star*, §*The Cross Product in Three Dimensions*.

**Proposition.** The cross product is a continuous bilinear map $V\times V\to V$; the induced map $\Lambda^{2}V\to V$ is a homeomorphism; and the scalar triple product $a\cdot(b\times c)=(a\wedge b\wedge c)\omega^{-1}$ is a continuous trilinear form.

*Proof.* The cross product is bilinear and $V$ is finite-dimensional, so it is continuous; the induced map from the bivectors to the vectors is the star restricted to $\Lambda^{2}$ composed with the identification of bivectors with the vectors of a three-dimensional space, both linear isomorphisms between finite-dimensional spaces, hence homeomorphisms. The triple product is a composite of continuous multilinear maps. The algebraic identities, including the Lagrange identity $q(a\times b)=q(a)q(b)-B(a,b)^{2}$, are those of the Part I article and are polynomial identities, hence continuous. $\square$

**Remark (the exterior Hodge star is continuous).** The Hodge star of the exterior algebra of *The Hodge Star and the Real Structure of the Exterior Algebra* is the present star read through the symbol isomorphism; since the symbol map is a homeomorphism in finite dimension, by *The Continuous Grade Decomposition and the Filtration*, §*The Symbol Map and the Two Topologies*, every continuity statement proved here transfers to the exterior reading, and conversely. The function-theoretic star of differential forms on a manifold is not this operation and is not read in this corpus at this layer: the exterior derivative, the codifferential and the Laplacian are Analysis, and the Hodge theorem is Geometry.

## The Failure in Infinite Dimension

**Remark.** The construction of this article has no analogue in infinite dimension, and the reason is the absence of the object it starts from: there is no top grade, no one-dimensional space $\mathrm{Cl}_{n}$ and no volume element, so there is no complement map, no star and no duality pairing between a grade and its complement. What replaces them in the infinite-dimensional theory is the duality between the algebra and its dual taken with respect to the form and the canonical anticommutation relations of the completion, which is the subject of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation* and of *The Completion of a Clifford Algebra*; the pairing there is between the algebra and the dual of the completion and is not the finite-dimensional complement map. The infinite-dimensional objects of this category therefore carry the grade decomposition and the filtration but not the star, and this article is the finite-dimensional one.

## Examples

### The Definite Cases

**Example ($\mathrm{Cl}_{4,0}$).** Let $V=\mathbb{R}^{4}$ with the positive definite form and $\omega=e_{1}e_{2}e_{3}e_{4}$, of square $+1$, so that $\star$ is an involution. The grade $\mathrm{Cl}_{2}$ of dimension six is the topological direct sum of the self-dual and the anti-self-dual parts, of dimension three each, by the continuous projections $\tfrac12(\mathrm{id}\pm\star)$; the volume elements are the nonzero multiples of $\omega$, an open set with two components, and the two components give the star and its negative. The duality pairing exhibits $\mathrm{Cl}_{2}$ as its own dual, of the same dimension, and the form $\beta_{2}$ is symmetric, since the grade two is the middle one.

**Example ($\mathrm{Cl}_{3,0}$ and the biquaternion case).** Let $V=\mathbb{R}^{3}$ with the positive definite form and $\omega=e_{1}e_{2}e_{3}$, of square $-1$, so that $\star$ is a complex structure and each grade is a topological complex vector space. On the vectors, the star carries $e_{1}$ to $-e_{2}e_{3}$ and the identification of the bivectors with the vectors makes $\star$ the cross product up to the sign; on the algebra $\mathrm{Cl}_{3,0}\cong M_{2}(\mathbb{C})$ the volume element is central of square $-1$ and is identified with the imaginary unit $i$ of *The Clifford Algebra Representation*, so that the star is multiplication by $-i$ as in the Part I article. The topological content is that this identification is a homeomorphism of the algebra onto the complex matrix algebra, and that the complex structure it defines on each grade is continuous.

### The Indefinite Case and the Duality Pairing

**Example ($\mathrm{Cl}_{1,1}$).** Let $V=\mathbb{R}^{2}$ with $q(e_{1})=1$, $q(e_{2})=-1$ and $\omega=e_{1}e_{2}$, of square $+1$. The star is an involution exchanging the two coordinate directions, and the top grade with the scalars; its eigenspaces in the algebra are of dimension two each, and the projections $\tfrac12(\mathrm{id}\pm\star)$ are the two idempotents $\tfrac12(1\pm\omega)$ of the algebra, which are the two primitive idempotents of the matrix algebra $M_{2}(\mathbb{R})$ under the identification $\mathrm{Cl}_{1,1}\cong M_{2}(\mathbb{R})$ of *The Low-Dimensional Classification*. The example is the smallest indefinite case and shows that the sign of $\omega^{2}$, not the definiteness of the form, decides which of the two order-two cases holds.

**Example (the duality in three dimensions).** On $\mathbb{R}^{3}$ with the positive definite form, the pairing $\beta_{1}$ of vectors with bivectors is non-degenerate and the star identifies $\mathrm{Cl}_{1}$ with $\mathrm{Cl}_{2}$; the induced identification of the vectors with their dual is the one that gives the scalar triple product, and the cross product is the composite of the wedge product with the star. All the maps are continuous and finite-dimensional, and the example is the classical one of the duality of three-dimensional space read in the layer.

## Summary

A **volume element** is a nonzero element of the one-dimensional top grade of the Clifford algebra of a non-degenerate form; it depends **continuously** on the orthogonal frame that defines it, the set of volume elements is the open set of units of the top grade, with two components over $\mathbb{R}$ corresponding to the two **orientations**, and the assignment of the **Hodge star** $\star A=A\omega^{-1}$ to the volume element is continuous. The star is a continuous linear **homeomorphism** of the algebra, and on a grade of a volume element with $\omega^{2}=\pm1$ it is an involution or a complex structure according to the sign.

The **complement map** $A\mapsto A\omega$ is a homeomorphism from each grade onto its complement, and its bilinear form is the **duality pairing** $\beta_{k}$ with $\beta_{k}(x,y)\omega=\langle xy\rangle_{n}$; the pairing is continuous and non-degenerate, so each grade is the continuous dual of its complement, and under the symbol map it is the wedge pairing of the exterior algebra. In the **involutive case** $\omega^{2}=1$ the continuous projections $\tfrac12(\mathrm{id}\pm\star)$ split the grade as a **topological direct sum** of the self-dual and anti-self-dual parts, interchanged by an orientation-reversing isometry; in the **complex case** $\omega^{2}=-1$ the star endows the grade with the structure of a **topological complex vector space**, of half the real dimension. For the middle degree the parity of $n/2$ decides which case holds: $n\equiv0\pmod4$ gives the splitting, $n\equiv2\pmod4$ the complex structure.

The **cross product** of three-dimensional space is the star of the outer product, a continuous bilinear map with a homeomorphic induced map from the bivectors to the vectors, and the **scalar triple product** is continuous and trilinear. What the article does not own is as important as what it does: the isometry property of the star needs the **positivity** of the Hermitian layer and is owned by *The Blade Form and the Hermitian Structure with Hermitian Adjoint*; the differential-form star, the codifferential and the Laplacian are **Analysis**; the Hodge theorem is **Geometry**; and in infinite dimension there is **no volume element**, no star and no complement map, the role of the duality passing to the pairing with the completion in *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\omega=e_{1}\cdots e_{n}$, $\omega^{2}=(-1)^{n(n-1)/2}\prod q(e_{i})$ | the volume element and its square |
| $\mathrm{Cl}_{n}(V,q)\setminus\{0\}$ | the volume elements, open, two components over $\mathbb{R}$ |
| $A\omega$, $\omega A$ | the right and the left complement, homeomorphisms $\mathrm{Cl}_{k}\to\mathrm{Cl}_{n-k}$ |
| $\beta_{k}(x,y)\omega=\langle xy\rangle_{n}$ | the duality pairing, continuous and non-degenerate |
| $\star A=A\omega^{-1}$ | the Hodge star, a continuous homeomorphism |
| $\star^{2}=(\omega^{2})^{-1}\mathrm{id}$ | the square of the star |
| $\mathrm{Cl}_{k}^{\pm}$, $\tfrac12(\mathrm{id}\pm\star)$ | the self-dual parts and their continuous projections |
| $\star^{2}=-1$ | the complex structure on a grade |
| $a\times b=\star(a\wedge b)$ | the cross product |
| $\beta_{1}$, $\mathrm{Cl}_{1}\cong\mathrm{Cl}_{2}^{*}$ | the duality of three-dimensional space |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the volume element, the complement map and the duality of the grades.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the Hodge star in the Clifford normalisation and its square.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the self-dual and anti-self-dual splitting in four dimensions.
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the continuity of a multilinear map on a finite-dimensional product and the homeomorphism property of a linear isomorphism.
- Nicolas Bourbaki, *Topological Vector Spaces* (Springer, 1987), for the topological direct sum and the continuous projections of an involutive operator.
- Warner Greub, Stephen Halperin and Ray Vanstone, *Connections, Curvature, and Cohomology*, Vol. I (Academic Press, 1972), for the differential-form Hodge star, named here and deferred to Analysis and Geometry.
