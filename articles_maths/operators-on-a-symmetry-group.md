
# __Operators on a Symmetry Group__

## Introduction

A **symmetry group** is a group of isometries of a space that carries a chosen distance or form, and the choice is what makes the group and its operators geometric: the same abstract group is the symmetry group of many forms, and a different form gives different motions, different orbits and different operators. This article opens the operator layer of *Geometry on Groups*. It treats the operators that the action of a symmetry group $G$ on its space $X$ produces — the action operators, the left and the right multiplications of the group on itself, the two-sided sandwich, and the operators that commute with the action — and it does no more. The involution on the **elements** of $G$, together with the spaces its fixed subgroup defines, is the subject of the group `- * Theory` of this category; the **adjoint** of an operator, which that involution defines, is the subject of the group `- * Operator Theory`. Neither is used here: an operator is introduced, composed and classified, and no form on the elements and no adjoint is taken.

The base is a set $X$ with a chosen distance, or a linear space $V$ with a chosen quadratic or Hermitian form; the space $X$ is a smooth manifold when the regular action is used, and the group is a Lie group then. The isometries of the form and the group they form are *Isometries and Orthogonal Transformations*; the realisation of a figure's symmetry group inside the Euclidean isometry group, and the finiteness or discreteness of that group, are *Symmetry, Point and Crystallographic Groups*; the orbit–stabiliser theorem and the decomposition of a $G$-set into orbits are *Group Actions and Structure*; the automorphism group of a structure and the hierarchy of its symmetry groups are *Transformation Groups*; and a linear action of a group is a module over its group algebra, treated in *Representations of Groups* and *Modules over an Algebra*. None of that theory is re-derived.

The article has six sections: the space, the form and the symmetry group; the action operators; the left and right multiplications and the sandwich; the equivariant operators; the operator layer the group generates; and the worked cases. The operators are collected in the closing *Summary of Notation*.

## The Space, the Form and the Symmetry Group

### The Chosen Form and Its Isometries

Let $X$ be a set with a chosen distance $d$, or a finite-dimensional space $V$ over a field of characteristic not $2$ with a chosen non-degenerate quadratic form $Q$ and its polar form $B$. A **symmetry of $X$** is a bijection preserving the chosen structure: a distance-preserving bijection when $X$ is metric, or a linear isomorphism $T$ with $Q(Tv) = Q(v)$ when $X = V$ is a quadratic space. The symmetries of the chosen form form a group under composition, the **isometry group** $\operatorname{Isom}(X)$ of the chosen structure; for a quadratic space it is the orthogonal group $\operatorname{O}(V, Q)$, a subgroup of the general linear group, and the reflections generate it, by the theorem of Cartan–Dieudonné. These are the objects of *Isometries and Orthogonal Transformations* and of *The Rotation Group and Orientation*, and are cited rather than restated.

### The Symmetry Group

**Definition.** A **symmetry group** of $X$ is a subgroup $G \leq \operatorname{Isom}(X)$ of the isometry group of the chosen structure. Its elements are the **motions** available for $X$; when $X$ is a figure $F$ inside a larger space and the chosen structure is the ambient one, the maximal such subgroup is $\operatorname{Sym}(F) = \{\varphi \in \operatorname{Isom}(X) : \varphi(F) = F\}$, the symmetry group of the figure, whose finite and discrete instances are *Symmetry, Point and Crystallographic Groups*.

A symmetry group is therefore not a datum of $X$ alone. The Euclidean plane with its form $x^2+y^2$ has the symmetry group $O(2)$ and no hyperbolic rotation; the plane with the form $x^2-y^2$ has the symmetry group $O(1,1)$ and no Euclidean rotation. This dependence on the chosen form is the boundary test of the part, and it is what makes every statement below a statement of geometry rather than of group theory.

### The Action

**Definition.** A symmetry group $G$ **acts** on $X$ by the evaluation map

$$
G \times X \longrightarrow X, \qquad (a, x) \longmapsto a \cdot x = a(x),
$$

with $e \cdot x = x$ and $(ab)\cdot x = a \cdot (b \cdot x)$; the action is **effective** when the assignment $a \mapsto (x \mapsto a\cdot x)$ is injective, and it is by definition by isometries of the chosen form. The **orbit** of $x$ is $G \cdot x = \{a \cdot x : a \in G\}$, the **stabiliser** is $G_x = \{a \in G : a \cdot x = x\}$, and the orbit–stabiliser theorem, *Group Actions and Structure*, identifies the orbit with the coset space $G/G_x$ as a $G$-set. The orbits are the figures of the geometry that the chosen form and the subgroup $G$ jointly single out: the circles of the Euclidean plane under $SO(2)$, the hyperbolas of the hyperbolic plane under the hyperbolic rotations, the spheres of $\mathbb{R}^n$ under $O(n)$.

**Remark.** When $G$ is the whole isometry group the action is transitive on each connected component of $X$; when $G$ is a proper subgroup the orbit decomposition is finer, and the refinement is the geometric content of the choice of $G$ inside $\operatorname{Isom}(X)$.

## The Action Operators

### The Operator of an Element

**Definition.** Let $\mathcal{F}(X)$ be the space of functions on $X$ (the smooth functions when $X$ is a manifold, the linear functions when $X = V$ is a quadratic space). The **action operator** of $a \in G$ is the linear map

$$
\pi(a) : \mathcal{F}(X) \longrightarrow \mathcal{F}(X), \qquad
\bigl(\pi(a)f\bigr)(x) = f\bigl(a^{-1}\cdot x\bigr).
$$

The inverse in the argument is what makes the assignment a left action: for $a, b$ and $f$,

$$
\pi(a)\pi(b)f(x) = \pi(b)f(a^{-1}\cdot x) = f\bigl(b^{-1}\cdot a^{-1}\cdot x\bigr) = f\bigl((ab)^{-1}\cdot x\bigr) = \pi(ab)f(x).
$$

**Proposition.** The assignment $\pi : G \to GL(\mathcal{F}(X))$ is a group homomorphism, $\pi(e) = \mathrm{id}$ and $\pi(a)^{-1} = \pi(a^{-1})$; the space $\mathcal{F}(X)$ is a module over the group algebra of $G$ through it, and the representation $\pi$ is the **permutation representation** of the action on functions. When $G$ is effective the representation is faithful on $\mathcal{F}(X)$ when the functions separate the points of $X$.

**Proof.** The composition rule is the computation above; that $\pi(e) = \mathrm{id}$ is $e \cdot x = x$; and the inverse is read off from $\pi(a)\pi(a^{-1}) = \pi(e)$. The module statement is the definition of the group algebra acting through a representation, *Representations of Groups*.

### Fixed Functions and Invariants

**Definition.** A function $f$ is **invariant** under the action when $\pi(a)f = f$ for every $a \in G$, equivalently when $f$ is constant on every orbit. The invariant functions form the subspace

$$
\mathcal{F}(X)^G = \{f : f(a \cdot x) = f(x)\ \text{for all } a \in G,\ x \in X\},
$$

the **fixed space** of the representation, and the functions invariant under the isometry group of a form are the invariants of the form: on a quadratic space $\operatorname{O}(V,Q)$-invariant polynomials are the polynomials in $Q$, by the first fundamental theorem of invariant theory, so the invariant functions of a quadratic space are exactly the functions of $Q$.

**Proposition.** The fixed space $\mathcal{F}(X)^G$ is the common kernel of the operators $\pi(a) - \mathrm{id}$, and it is a subalgebra of $\mathcal{F}(X)$ when $G$ is effective and $\mathcal{F}$ is closed under products.

## Left and Right Multiplication and the Sandwich

### The Group as a Space

The simplest space on which a symmetry group acts is the group itself. When $X = G$ with the chosen structure that the identification $G \leq \operatorname{Isom}(X)$ supplies, the action becomes the left multiplication, and it is accompanied by the right multiplication, which commutes with it.

**Definition.** The **left translation operator** and the **right translation operator** by $a \in G$ on $\mathcal{F}(G)$ are

$$
L_a f(x) = f(a^{-1}x), \qquad R_a f(x) = f(xa),
$$

so that $L_a$ is the action operator of the left action of $G$ on itself and $R_b$ is the action operator of the right action. They satisfy

$$
L_a L_b = L_{ab}, \qquad R_a R_b = R_{ab}, \qquad L_a R_b = R_b L_a,
$$

and each family is a representation of $G$ on $\mathcal{F}(G)$; the two representations commute.

**Proof.** The composition rules are immediate from the definitions, and the commutation is the associativity of the product: $L_a R_b f(x) = R_b f(a^{-1}x) = f(a^{-1}xb) = L_a f(xb) = R_b L_a f(x)$.

**Remark.** The two-sidedness matters. When $G$ is non-abelian, $L_a$ and $R_a$ differ, and the difference is the inner conjugation of the next subsection; when $G$ is abelian the two coincide, and the regular action degenerates. The left and the right multiplication are the elementary operators, and every operator built from the group is a composite of them.

### The Sandwich

**Definition.** The **sandwich** by the pair $(a, b) \in G \times G$ is the two-sided operator

$$
\Psi_{a,b} : \mathcal{F}(G) \longrightarrow \mathcal{F}(G), \qquad
\Psi_{a,b} f(x) = f(a\,x\,b),
$$

the pullback of the map $x \mapsto axb$. In terms of the one-sided operators,

$$
\Psi_{a,b} = L_{a^{-1}} R_b = R_b L_{a^{-1}} .
$$

**Proposition.** The sandwiches compose by

$$
\Psi_{a,b} \circ \Psi_{c,d} = \Psi_{c a,\, b d},
$$

they satisfy $\Psi_{a,b}^{-1} = \Psi_{a^{-1}, b^{-1}}$, and the assignment $(a, b) \mapsto \Psi_{a,b}$ is a homomorphism $G \times G^{\mathrm{op}} \to GL(\mathcal{F}(G))$. The sandwich with $b = a^{-1}$ is the **inner conjugation** $\Psi_{a, a^{-1}} f(x) = f(a\,x\,a^{-1})$.

**Proof.** For the composition, $\Psi_{a,b}\bigl(\Psi_{c,d}f\bigr)(x) = \Psi_{c,d}f(axb) = f(c\,a x b\,d) = \Psi_{ca,bd}f(x)$; the inverse is the sandwich with the inverses, and the composition law is that of the direct product with the opposite group in the second factor.

**Remark (the inner conjugation).** The conjugation action $a \mapsto (x \mapsto axa^{-1})$ is the orbit map of the action of $G$ on itself by conjugation, and its orbits are the conjugacy classes of *Group Actions and Structure*. Its kernel is the centre $Z(G)$, so the inner automorphisms are $G/Z(G)$; this is the operator that the group-theoretic conjugation contributes to the layer, and it is taken up in the negative form of the signed operators of the group `- * Operator Theory` of this category.

## Equivariant Operators

### The Commutant of the Action

**Definition.** Let $\mathcal{H}$ be a module over the group algebra of $G$, that is, a space with a linear action $\pi$. An operator $T : \mathcal{H} \to \mathcal{H}$ is **equivariant** (or an **intertwiner** of the action with itself) when

$$
T \pi(a) = \pi(a) T \qquad \text{for every } a \in G .
$$

The equivariant operators form the **commutant** $\operatorname{End}_G(\mathcal{H})$, a subalgebra of $\operatorname{End}(\mathcal{H})$ under composition, and it is the set of operators of the action that the action cannot tell apart.

**Proposition.** The commutant is a unital subalgebra of $\operatorname{End}(\mathcal{H})$, closed under inversion of its invertible members; it contains the identity and every scalar multiple of the identity, so $\operatorname{End}_G(\mathcal{H}) \supseteq k\cdot\mathrm{id}$ when the action is over the field $k$.

**Proof.** If $S$ and $T$ commute with every $\pi(a)$ then so do $S + T$, $ST$ and $T^{-1}$ for invertible $T$; the identity commutes with everything.

### Schur's Lemma and the Irreducible Case

**Theorem (Schur).** Let $\mathcal{H}$ be an irreducible module over the group algebra of $G$ over an algebraically closed field $k$. Then every equivariant operator is a scalar, $\operatorname{End}_G(\mathcal{H}) = k \cdot \mathrm{id}$; consequently two irreducible modules are either isomorphic or have no nonzero intertwiner between them.

**Proof.** An equivariant endomorphism of an irreducible module has kernel and image that are submodules, hence each is $0$ or the whole; so a nonzero endomorphism is invertible, and over an algebraically closed field an operator commuting with an irreducible action has an eigenvalue and the corresponding eigenspace is a nonzero submodule, hence the whole space, so the operator is that scalar. For the second statement, the kernel of an intertwiner is a submodule and the image is a submodule, and irreducibility forces the two alternatives.

**Remark.** The classification of the equivariant operators is therefore the classification of the module: an irreducible module has only scalars, a sum of isotypic components has as many operators as the component ring, and a general module has the matrix algebra of its multiplicity spaces. The geometric reading is exact: the operators of a space that commute with its symmetry group are precisely the operators that the symmetry cannot detect, and they are the invariants of the action on the operator layer.

### The Equivariant Operators of a Space

**Definition.** An operator $T$ on the chosen space $X$ is a **symmetry-preserving operator** when it commutes with every symmetry of the form, $T \in \operatorname{End}_G(\mathcal{F}(X))$. The group generated by the action operators and the sandwiche is contained in $\operatorname{End}_G(\mathcal{F}(X))$ when the group is abelian, and in general the action operators themselves are equivariant under the action by conjugation only.

**Example.** On the Euclidean plane the Laplacian commutes with $O(2)$, so it is a symmetry-preserving operator; the radial derivative commutes with $SO(2)$ but not with the reflections, so it is equivariant for the rotations alone. The operators equivariant for a subgroup are the operators equivariant for the larger group exactly when the larger group is generated by the smaller together with operators that already commute with them.

## The Operator Layer the Group Generates

### The Generated Algebra

**Definition.** The **operator layer** of the symmetry group $G$ is the smallest subalgebra of $\operatorname{End}(\mathcal{F}(G))$ containing the identity and the one-sided operators $L_a$, $R_b$ for $a, b \in G$; equivalently, it is the algebra generated by the image of the group algebra under the left and right regular representations.

**Proposition.** The operator layer contains every sandwich $\Psi_{a,b}$, because $\Psi_{a,b} = L_{a^{-1}}R_b$, and it contains the inner conjugation $\Psi_{a,a^{-1}}$; it is spanned by the sandwiches when the group is finite, since a word in the generators is a composite of sandwiches and reduces to one by the composition law.

**Proof.** The first statements are the definitions and the composition law of the sandwiches. For the spanning, expanding a word by $L_a = \Psi_{a,e}$ and $R_b = \Psi_{e,b^{-1}}$ and using the composition law $\Psi_{a,b}\Psi_{c,d} = \Psi_{ca,bd}$ reduces every word to a single sandwich; the span over the field of the group is the layer.

### The Two-Sided Operators

The sandwiches are the two-sided operators of the layer, the one-sided operators are the degenerate cases with one parameter trivial, and the inner conjugation is the diagonal. They are the complete list of the operators that carry the group's own product to itself, in the following sense.

**Proposition.** A linear operator $T : kG \to kG$ on the group algebra is a sandwich, $T = \Psi_{a,b}$, exactly when $T$ is the pullback of a group automorphism of the form $x \mapsto axb$ for fixed $a, b$; in particular the invertible operators of the layer that are multiplicative on the group algebra are the composites of a left and a right multiplication.

**Proof.** The pullback of $x \mapsto axb$ is a sandwich, and conversely a sandwich carries the product of two elements to the product of their images, so it is multiplicative on the group algebra; an operator multiplicative on the group algebra and sending $e$ to $e$ is a group automorphism, and the automorphisms of the shape $x \mapsto axb$ are exactly the composites of the left and right translations, the inner ones when $b = a^{-1}$.

## Worked Cases

**Example (the circle and its rotations).** Let $X = S^1$ with the Euclidean form and $G = SO(2) = \{R(\theta)\}$. The action on $L^2(S^1)$ has the Fourier characters $f_m(x) = e^{imx}$ as eigenfunctions, $L_{R(\theta)}f_m = e^{-im\theta}f_m$, so the action operators are diagonal in the character basis and the commutant of the action on each isotypic component is the scalars. The subgroups of $SO(2)$ are the cyclic and the dense subgroups, and the commutant of a dense one is trivial, which is the operator form of the fact that a dense subgroup has no invariant functions but the constants.

**Example (the finite symmetry group of a polygon).** Let $X$ be the regular $n$-gon and $G = D_n$ its dihedral symmetry group of order $2n$, *Symmetry, Point and Crystallographic Groups*. The action on the $n$ vertices is the standard permutation action, and the equivariant operators are the $D_n$-stable linear maps of the vertex space: the circulant matrices commuting with the rotation form the cyclic algebra, and the reflection reduces the commutant to the symmetric circulants. The orbit–stabiliser count gives the invariant functions of the vertex set, one dimension for each orbit of the group on the vertex set.

**Example (the Euclidean group and its translations).** Let $X = \mathbb{R}^n$ and $G = E(n) = \mathbb{R}^n \rtimes O(n)$, the Euclidean isometry group of *Symmetry, Point and Crystallographic Groups*. A translation $T_b$ has the single action operator with $L_{T_b}f(x) = f(x-b)$, and the translations alone form the abelian normal subgroup; the sandwich by two translations is a single translation, $\Psi_{T_b,T_c} = L_{T_{-(b+c)}}$, so the layer of the translation subgroup is the commutative algebra generated by the shift operators, whose characters are the exponentials $e^{i\langle\xi,x\rangle}$.

## Summary

A symmetry group $G$ is a subgroup of the isometry group of a space $X$ carrying a chosen distance or form, and the choice of the form is what makes the group and its operators geometric. The action $G \times X \to X$ by isometries gives the action operators $\pi(a)f(x) = f(a^{-1}\cdot x)$, a representation of $G$ on the functions, whose fixed space is the invariant functions, constant on the orbits. On the group itself the left and the right multiplications $L_a f(x) = f(a^{-1}x)$ and $R_a f(x) = f(xa)$ are two commuting representations, and the two-sided sandwich $\Psi_{a,b}f(x) = f(axb) = L_{a^{-1}}R_b f(x)$ composes by $\Psi_{a,b}\Psi_{c,d} = \Psi_{ca,bd}$ and has inverse $\Psi_{a^{-1},b^{-1}}$; the inner conjugation $\Psi_{a,a^{-1}}$ has kernel the centre. The operators equivariant for the action are the commutant of the representation, a unital subalgebra; for an irreducible module over an algebraically closed field Schur's lemma makes the commutant the scalars, and the equivariant operators of a space are exactly the operators the symmetry cannot detect. The layer generated by the group is spanned by the sandwiches, and the multiplicative invertible members of the layer are the composites of a left and a right multiplication.

The involution on the elements of $G$, the spaces its fixed subgroup defines, and the adjoint of an operator defined by that involution are not part of this article: the first is the group `- * Theory` of this category and the second the group `- * Operator Theory`. The convolution and translation operators of the group are the two following articles of the present group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$ | a space with a chosen distance, or a quadratic space |
| $Q$, $B$ | the chosen quadratic form and its polar form |
| $\operatorname{Isom}(X)$ | the isometry group of the chosen structure |
| $G \leq \operatorname{Isom}(X)$ | the symmetry group; a subgroup of the isometries |
| $\operatorname{Sym}(F)$ | the symmetry group of a figure $F$ |
| $a \cdot x$ | the action of $a \in G$ on $x \in X$ |
| $G\cdot x$, $G_x$ | orbit and stabiliser of $x$ |
| $\mathcal{F}(X)$, $\mathcal{F}(X)^G$ | functions on $X$; the invariant functions |
| $\pi(a)$ | the action operator, $\pi(a)f(x) = f(a^{-1}\cdot x)$ |
| $L_a$, $R_b$ | left and right translation operators |
| $\Psi_{a,b} = L_{a^{-1}}R_b$ | the two-sided sandwich, $\Psi_{a,b}f(x) = f(axb)$ |
| $\operatorname{End}_G(\mathcal{H})$ | the commutant; the equivariant operators |
| $kG$ | the group algebra acting through the representation |
| $E(n) = \mathbb{R}^n \rtimes O(n)$ | the Euclidean isometry group |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for group actions on spaces, invariant operators and the two-sided calculus on a group.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume I* (Interscience, 1963), for the isometry group of a Riemannian manifold and the equivariant operators.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the isometry groups of the classical forms and their generation by reflections.
- Sergei Lang, *Algebra* (Springer, third edition, 2002), for group actions, the orbit–stabiliser theorem and the group algebra.
- Hermann Weyl, *The Classical Groups: Their Invariants and Representations* (Princeton, 1939), for the invariants of the classical groups and the operators the symmetry cannot detect.
