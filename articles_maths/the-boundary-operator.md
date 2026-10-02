# __The Boundary Operator__

## Introduction

A chain complex is a graded module together with an operator that lowers the degree by one and squares to zero, and the homology of the complex is the graded module of the cycles modulo the boundaries. The operator is the **boundary operator** $\partial$, and the whole of the homology theory of this Part is the study of it: the singular complex of a space, the simplicial complex of a triangulation and the cellular complex of a CW complex are all complexes in this sense, and their homologies are all the homology of the same operator applied to different graded modules. This article isolates the operator. It states the square-zero property and the homology it defines, reads the functoriality of the construction as the statement that the chain maps are exactly the operators intertwining the boundaries, derives the connecting homomorphism of a short exact sequence as the operator built from $\partial$ by the snake lemma, identifies the coboundary $\delta$ as the adjoint of $\partial$ under the evaluation pairing, and records the two derivation laws by which $\partial$ acts on the cap product and $\delta$ on the cup product.

The article is the operator layer of *Simplicial and Singular Homology*, which constructs the singular and the simplicial complexes and proves that their boundary operators square to zero; the explicit boundary formulas, the face relations and the computations are there and are not repeated. The construction of the connecting homomorphism, the snake lemma and the algebra of modules entering and leaving an exact sequence are those of *Exact Sequences*; the general theory of chain complexes over a ring, of resolutions, of derived functors and of the spectral sequence of a filtered complex is the planned *Homological Algebra* of Part I, written in parallel, and is cited only for the statements it supplies. The cup and cap products and the pairing between cohomology and homology are those of *Cup and Cap Products* and *Cohomology and the Universal Coefficient Theorem*; the transfer and the suspension, which are further operators built on the same complex, are the subjects of *The Transfer Map* and *The Suspension Operator* of this category.

Nothing analytic and nothing geometric is used. The article is the algebra of a single square-zero operator on a graded module; the topological complexes are named as the instances that give the operator its content, and no distance, no norm, no limit and no measure occurs. The classes of this article are not to be confused with the boundary operator of a triangulation read concretely, which is the sibling article *The Boundary Operator of a Simplicial Complex*, nor with the differential of a spectral sequence, which is a family of boundary operators on the pages of a filtration and belongs to *The Leray–Serre Spectral Sequence*.

## The Operator and Its Square Zero

### The Definition

**Definition.** A **graded module** over a ring $R$ is a family $C_* = (C_n)_{n \in \mathbb{Z}}$ of $R$-modules; a **boundary operator** on it is a family of $R$-linear maps $\partial_n : C_n \to C_{n-1}$ with

$$
\partial_{n-1} \circ \partial_n = 0
$$

for every $n$. The pair $(C_*,\partial)$ is a **chain complex**; an element of $C_n$ is an $n$-**chain**, a chain $c$ with $\partial c = 0$ is a **cycle**, and a chain of the form $\partial c'$ is a **boundary**.

Since $\partial$ lowers the degree, the two subspaces of $C_n$ with which the theory works are

$$
Z_n = \ker \partial_n, \qquad B_n = \operatorname{im}\partial_{n+1},
$$

the cycles and the boundaries; the square-zero property is exactly the inclusion $B_n \subseteq Z_n$, so the quotient makes sense.

**Definition.** The **homology** of the complex is the graded module

$$
H_n(C_*,\partial) = Z_n / B_n = \frac{\ker \partial_n}{\operatorname{im}\partial_{n+1}} .
$$

A complex is **acyclic**, or a **resolution**, when $H_n = 0$ for $n \neq 0$; it is **exact in degree $n$** when $H_n = 0$.

The homology measures the failure of the operator to be as injective and as surjective as a boundary operator of acyclic provenance would be: it vanishes exactly when the complex is exact, and it is the obstruction to splitting the complex into its own cycles.

### The Augmentation and the Reduced Complex

**Definition.** An **augmentation** of a complex of non-negative degree is an $R$-linear map $\varepsilon : C_0 \to R$ with $\varepsilon \partial_1 = 0$; the **reduced complex** is obtained by replacing $C_0$ by $\ker\varepsilon$ and restricting $\partial_1$, and its homology is the **reduced homology** $\tilde H_*$.

The augmentation is a map of complexes to the complex concentrated in degree zero, so it is an operator of the same kind as $\partial$, and the reduced complex is the kernel of that operator. The singular complex of a non-empty space carries the augmentation $\varepsilon(\sigma) = 1$ and the reduced complex of *Simplicial and Singular Homology* is this construction.

### The Coboundary as the Dual Operator

**Definition.** Let $C^* = (C^n)$ be a graded module and let $\delta^n : C^n \to C^{n+1}$ be $R$-linear with $\delta^{n+1}\delta^n = 0$; then $(C^*,\delta)$ is a **cochain complex**, its elements in degree $n$ are **cochains**, and its **cohomology** is

$$
H^n(C^*,\delta) = \frac{\ker\delta^n}{\operatorname{im}\delta^{n-1}} .
$$

The operator $\delta$ is the **coboundary**.

A cochain complex is the same thing as a chain complex with the grading reversed: writing $D_n = C^{-n}$ and $\partial_n = \delta^{-n}$ turns $\delta\delta = 0$ into $\partial\partial=0$. The two are distinguished only by the convention that homology is written with lower indices and cohomology with upper indices, and by the functorial variance: a chain map preserves the degree, while a cochain map does too, and it is the source and target that determine in which direction an induced map runs.

## Chain Maps and the Functoriality

### The Operators Intertwining the Boundary

**Definition.** A **chain map** $f : (C_*,\partial) \to (D_*,\partial)$ is a family of $R$-linear maps $f_n : C_n \to D_n$ with $f_{n-1}\partial_n = \partial_n f_n$, that is an operator commuting with the boundary. A **chain homotopy** between two chain maps $f$ and $g$ is a family $P_n : C_n \to D_{n+1}$ with

$$
\partial_{n+1} P_n + P_{n-1}\partial_n = g_n - f_n .
$$

**Theorem.** A chain map carries cycles to cycles and boundaries to boundaries, and hence induces $H_n(f) : H_n(C_*) \to H_n(D_*)$; the assignments $(C_*,\partial) \mapsto H_n(C_*,\partial)$, $f \mapsto H_n(f)$ are functorial. Chain-homotopic maps induce the same map on homology.

*Proof.* If $\partial c = 0$ then $\partial(fc) = f\partial c = 0$, so $fc$ is a cycle; if $c = \partial c'$ then $fc = f\partial c' = \partial f c'$, so $fc$ is a boundary. The induced map is therefore well defined on classes; $(g \circ f)_n = g_n \circ f_n$ and $(\mathrm{id})_n = \mathrm{id}$ give functoriality. For the last statement, the displayed identity applied to a cycle $c$ gives $g c - f c = \partial P c$, a boundary, so the two classes agree. $\square$

The theorem is the exact content of the phrase that homology is a functor on the homotopy category of complexes: the objects are the complexes, the morphisms are the chain maps modulo chain homotopy, and the functor is homology.

**Proposition (the boundary is determined by its values on generators).** If a graded module is free with a basis and $\partial$ is defined on the basis with $\partial^2 = 0$, then $\partial$ extends uniquely to an $R$-linear boundary operator, and the homology is computed from the matrix of $\partial$ in the basis. In particular a boundary operator on a finitely generated free complex is a matrix operator, and its rank and nullity are the data from which the homology is read.

*Proof.* The extension is the universal property of a free module, and the square-zero condition is checked on the basis because both sides are $R$-linear. The matrix description and the rank-nullity computation of $H_n = \ker\partial_n/\operatorname{im}\partial_{n+1}$ are then linear algebra. $\square$

This is the operator under which the concrete computations of *The Boundary Operator of a Simplicial Complex* are performed, and the incidence matrices of a triangulation are its matrix expression.

### The Euler Characteristic and the Lefschetz Number

**Definition.** For a finite complex of finitely generated free modules over a field, the **Euler characteristic** is

$$
\chi = \sum_{n} (-1)^n \dim_R H_n = \sum_{n} (-1)^n \dim_R C_n ,
$$

the second expression being the alternating sum of the ranks of the chain modules.

The equality of the two expressions is the statement that the alternating sum of the dimensions is additive along an exact sequence, applied to the short exact sequences $0 \to Z_n \to C_n \to B_{n-1}\to 0$ and $0 \to B_n \to Z_n \to H_n \to 0$; it is the operator-level form of the Euler–Poincaré formula and the prototype of the Lefschetz fixed-point formula, in which a chain map that commutes with $\partial$ replaces the zero operator and the traces of its restrictions replace the dimensions.

## The Boundary of an Exact Sequence

### The Connecting Homomorphism

**Theorem.** Let $0 \to A_* \xrightarrow{i} B_* \xrightarrow{j} C_* \to 0$ be a short exact sequence of chain complexes and chain maps. Then there is a boundary operator

$$
\Delta : H_n(C_*) \longrightarrow H_{n-1}(A_*),
$$

the **connecting homomorphism**, natural in maps of short exact sequences, and the resulting triangle

$$
H_n(A_*) \xrightarrow{\ i_*\ } H_n(B_*) \xrightarrow{\ j_*\ } H_n(C_*) \xrightarrow{\ \Delta\ } H_{n-1}(A_*) \xrightarrow{\ i_*\ } H_{n-1}(B_*) \to \cdots
$$

is exact. The map $\Delta$ satisfies $\Delta j_* = 0$ and $i_* \Delta = 0$, and it is the composite of the inverse of $j$ on a lift, an application of $\partial$, and the inverse of $i$ — the **snake** of the diagram.

*Proof.* This is the snake lemma of *Exact Sequences*, applied to the $3\times 3$ diagram whose two rows of complexes and two columns are the two adjacent degrees of the short exact sequence; the connecting map is built from $\partial_B$ by the chase, and the naturality is that of the chase. $\square$

The connecting homomorphism is thus an operator *constructed from* the boundary operator of the middle complex and the inverses of the two maps of the sequence; it is the reason an exact sequence of complexes produces an exact sequence of homology modules, and it is the pattern that every long exact sequence of this Part follows.

**Corollary (the boundary of a pair).** For a pair $(X,A)$ of spaces, the connecting homomorphism $\partial : H_n(X,A;R) \to H_{n-1}(A;R)$ of the long exact sequence of *Simplicial and Singular Homology* is the connecting homomorphism of the short exact sequence $0 \to C_*(A) \to C_*(X) \to C_*(X,A) \to 0$ of complexes. The same statement holds for the relative complex of a pair of chain complexes and for every quotient by a subcomplex.

*Proof.* The relative complex is the quotient of the ambient complex by the subcomplex of the subspace, so the sequence of complexes is short exact; apply the theorem. $\square$

## The Coboundary as the Adjoint

### The Evaluation Pairing

**Definition.** Let $C_*$ be a complex of free $R$-modules and let $C^* = \operatorname{Hom}_R(C_*,R)$ be its dual cochain complex with $\delta = \partial^*$, that is $(\delta \alpha)(c) = \alpha(\partial c)$ on cochains. The **evaluation pairing** is

$$
\langle \alpha, c \rangle = \alpha(c) \in R, \qquad \alpha \in C^n, \ c \in C_n .
$$

**Theorem.** The coboundary is the adjoint of the boundary under the evaluation pairing,

$$
\langle \delta \alpha, c \rangle = \langle \alpha, \partial c \rangle ,
$$

so that $\delta = \partial^*$; consequently $\delta^2 = 0$ because $\partial^2 = 0$, and the pairing descends to cohomology and homology,

$$
\langle-,-\rangle : H^n(C^*) \times H_n(C_*) \longrightarrow R ,
$$

because a cocycle pairs with a boundary to zero and a coboundary pairs with a cycle to zero. A chain map $f : C_* \to D_*$ has a dual $f^* : D^* \to C^*$ with $\langle f^*\alpha, c\rangle = \langle \alpha, f c\rangle$; the dual is a cochain map, and dualising is contravariant.

*Proof.* The first identity is the definition of $\delta$; the bilinearity of the pairing together with the two vanishing statements — $\langle\delta\alpha, c\rangle = \langle\alpha,\partial c\rangle = 0$ for a cycle $c$ and a cocycle $\alpha$ — shows that the pairing of classes is well defined. The dual statements are the definition of the transpose and the associativity of composition. $\square$

The theorem is the operator-layer form of the universal coefficient theorem: it says that passage to the dual exchanges the boundary and the coboundary and reverses the direction of the operators, and it is the reason the cohomology of a complex is computed from the same matrix as the homology, transposed.

### The Leibniz Rule for the Cap Product

**Theorem.** The boundary operator is a graded derivation for the cap product of *Cup and Cap Products*: for a cochain $\varphi$ of degree $k$ and a chain $c$ of degree $n$,

$$
\partial(c \frown \varphi) = (-1)^{k}\bigl((\partial c) \frown \varphi - c \frown \delta\varphi\bigr),
$$

so that on classes the cap product makes $H_*(X;R)$ a graded module over the graded ring $H^*(X;R)$, with the boundary measuring the failure of the two terms on the right to cancel. The dual statement, the Leibniz rule $\delta(\varphi \smile \psi) = (\delta\varphi)\smile\psi + (-1)^{|\varphi|}\varphi\smile(\delta\psi)$, makes the coboundary a graded derivation for the cup product; its operator form is the subject of *The Cup Product as an Operator*.

*Proof.* Both are the cochain-level identities of *Cup and Cap Products*, where the sign is forced by the convention for the evaluation of a cochain on a chain; the first is the boundary rule for the cap product, the second the Leibniz rule for the cup product. $\square$

**Remark (the derivation and the product operators).** The two rules say that $\partial$ and $\delta$ are derivations of the products that the complexes carry, and they are exactly the identities needed for the products to pass to homology and cohomology. An operator that is a derivation of a product is the operator-layer form of the product's compatibility with the boundary; in the differential graded algebra of the cochains the operator $\delta$ is the differential, the product is the cup product, and the Leibniz rule is the defining relation of the differential graded structure.

## The Boundary in the Topological Complexes

### The Instances

The abstract operator of this article is realised by the following complexes, whose boundary operators are constructed and whose square-zero property is proved in the articles named.

1. **The singular complex.** $C_n(X;R)$ is free on the singular $n$-simplices, $\partial_n$ is the alternating sum of the face maps, and $\partial^2 = 0$ is the simplicial identity $\partial\partial=0$ of *Simplicial and Singular Homology*; the homology is the singular homology $H_n(X;R)$, and the augmentation is $\varepsilon(\sigma)=1$.
2. **The simplicial complex.** For a triangulation, $C_n$ is free on the oriented $n$-simplices and $\partial_n$ is given by the incidence numbers; the homology is the simplicial homology, and the concrete operator, its matrices and its computations are the subject of *The Boundary Operator of a Simplicial Complex*.
3. **The cellular complex.** For a CW complex the cellular chain group $C_n$ is free on the $n$-cells and the boundary is the degree of the attaching maps; the homology agrees with the singular homology, and the construction is that of *CW Complexes and Cellular Approximation*.
4. **The de Rham complex.** The differential forms of a smooth manifold form a cochain complex under the exterior derivative, with $\delta = d$ and $d^2 = 0$; the complex, its product and its cohomology belong to the analysis and geometry of Part III, and the operator is named there and not used here.
5. **The Koszul and tensor complexes.** The exterior algebra with its differential $\partial(e_{i_1}\wedge\cdots\wedge e_{i_p}) = \sum_k (-1)^{k+1} a_{i_k} e_{i_1}\wedge\cdots\widehat{e_{i_k}}\cdots\wedge e_{i_p}$ is a complex used in the algebra of Part I; it is a boundary operator of the same kind, and the general theory is the planned *Homological Algebra*.

### Naturality of the Instances

The boundary operators of the instances are natural for the maps of the appropriate kind, and the naturality is what makes the operator a functor. A continuous map induces a chain map of the singular complexes; a simplicial map induces a chain map of the simplicial complexes; an attaching map together with a cellular map induces the cellular chain map; and in each case the induced map intertwines the boundary. The identification of the homologies of the instances is the content of *Simplicial and Singular Homology*, and it is the statement that the different graded modules carry the same operator.

## Summary

A **chain complex** is a graded module with a degree-lowering endomorphism $\partial$ satisfying $\partial^2 = 0$; its cycles and boundaries are $Z_n = \ker\partial_n$ and $B_n = \operatorname{im}\partial_{n+1}$, the square-zero property is the inclusion $B_n \subseteq Z_n$, and the homology is $H_n = Z_n/B_n$. An **augmentation** $\varepsilon$ with $\varepsilon\partial = 0$ defines the reduced complex and the reduced homology, and the **coboundary** $\delta$ of the dual complex is the same operator with the grading reversed. The **chain maps** are exactly the operators commuting with $\partial$; they carry cycles to cycles and boundaries to boundaries and induce maps on homology functorially, and a chain homotopy $\partial P + P\partial = g - f$ gives the equality of the induced maps, so that homology is a functor on the homotopy category of complexes. The connecting homomorphism of a short exact sequence of complexes is the operator built from $\partial$ by the snake lemma, and it is the source of every long exact sequence of this Part, in particular that of a pair. The coboundary is the adjoint of the boundary under the evaluation pairing, $\langle\delta\alpha, c\rangle = \langle\alpha,\partial c\rangle$, so dualising exchanges the two and reverses the operators; the boundary is a graded derivation for the cap product and the coboundary for the cup product, with the signs of *Cup and Cap Products*. The singular, simplicial, cellular, de Rham and Koszul complexes are the instances, and the general theory of the operator over a ring is the planned *Homological Algebra* of Part I; no analysis and no geometry was used here beyond the naming of the instances.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C_*$, $C_n$ | Graded module and its degree-$n$ part |
| $\partial$, $\partial_n$ | Boundary operator, of degree $-1$, with $\partial^2 = 0$ |
| $Z_n = \ker\partial_n$, $B_n = \operatorname{im}\partial_{n+1}$ | Cycles and boundaries |
| $H_n = Z_n/B_n$ | Homology of the complex |
| $\varepsilon : C_0 \to R$ | Augmentation, $\varepsilon\partial_1 = 0$; reduced complex and $\tilde H_*$ |
| $C^*$, $\delta$ | Dual cochain complex and coboundary; $H^n$ |
| chain map $f$, $H_n(f)$ | Operator commuting with $\partial$ and its induced map |
| $P$, $\partial P + P\partial = g - f$ | Chain homotopy; equality of induced maps |
| $\Delta$ | Connecting homomorphism of a short exact sequence of complexes |
| $0 \to C_*(A) \to C_*(X) \to C_*(X,A) \to 0$ | The pair sequence; its connecting map is $\partial$ |
| $\langle\alpha,c\rangle = \alpha(c)$ | Evaluation pairing; $\delta = \partial^*$, adjointness |
| $\frown$, $\smile$ | Cap and cup products; $\partial$ and $\delta$ are derivations |
| $\chi = \sum (-1)^n\dim H_n$ | Euler characteristic, equal to $\sum(-1)^n\dim C_n$ |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the singular and cellular boundary operators, the square-zero identity and the long exact sequences.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for the simplicial boundary operator, its incidence matrices and the Euler–Poincaré formula.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for chain complexes, chain maps, the snake lemma and the connecting homomorphism over a general ring.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the derived-functor and spectral-sequence context of a square-zero operator.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the chain complex as the primitive object of homological algebra and the adjointness of the two differentials.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the de Rham complex and the two differentials of a double complex, named here and treated in Part III.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the Euler characteristic and the Lefschetz number as alternating traces of a chain operator.
