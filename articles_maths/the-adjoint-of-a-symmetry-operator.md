
# __The Adjoint of a Symmetry Operator__

## Introduction

An operator on a space with a chosen form has an **adjoint**: the operator that moves the form from one side of it to the other, defined by $h(Tu, v) = h(u, T^{*}v)$. When the operator is a **symmetry** — an isometry of the chosen form, an element of a symmetry group acting on the space — the adjoint is its inverse, and the symmetry operators are exactly the **unitary** operators of the form. The passage $T \mapsto T^{*}$ is itself an involution, on the operators rather than on the elements, and it is the archetype of the group `- * Operator Theory` of this category: the operators are read together with the involution the form defines on them.

The article treats the invariant form, the adjoint of an operator on it, the unitarity of the symmetry operators, and the two involutions — the involution $\sigma$ on the **elements** of the group and the adjoint $T \mapsto T^{*}$ on the **operators** — which are different structures and coincide only when the representation is a `*`-representation. The algebra of the adjoint, the involutive algebras and the unitary elements in the algebraic setting are *The Adjoint in an Involutive Algebra*, *Unitary Operators of an Involutive Algebra*, *Involutions of the Endomorphism Algebra* and *Involutions of the Operator Layer*, in Part I, and the topological case is *Involutions of the Bounded Operators*; the representation theory and the invariant form are *Representations of Groups*, *The Left and Right Regular Representation* and *Noncommutative Harmonic Analysis*; the operators of the symmetry group, the left and right multiplications and the sandwich, are *Operators on a Symmetry Group* and *The Symmetry Operators of a Space*, the first articles of this category; the involution on the elements is the group `- * Theory`, the previous group. The adjoint in the complex-vector-space setting is *The Adjoint of a Hermitian Operator* and *The Adjoint of the Left Multiplication on a Complex Vector Space*, in *Geometry on Linear Spaces*, written in parallel.

The article has four sections: the invariant form and the adjoint; the adjoint of a symmetry operator; the involution on the operators and the two involutions; and the worked cases. Throughout, $V$ is a finite-dimensional space over a field $F$ of characteristic not $2$ with a chosen non-degenerate form $h$ — quadratic, symmetric bilinear or Hermitian — which is **invariant** under a symmetry group $G$ in the sense that $h(gu, gv) = h(u, v)$ for all $g \in G$; $T \in \operatorname{End}(V)$ is a linear operator, and $T^{*}$ its adjoint with respect to $h$.

## The Invariant Form and the Adjoint of an Operator

### The Invariant Form

**Definition.** A form $h$ on $V$ is **invariant** under the symmetry group $G \leq GL(V)$ when $h(gu, gv) = h(u, v)$ for all $g \in G$ and all $u, v$; equivalently, when $G$ is a subgroup of the isometry group $\operatorname{Isom}(V,h)$ of the form.

**Proposition.** If $h$ and $h'$ are two invariant forms under a group $G$ acting irreducibly on $V$, then $h' = \lambda h$ for a scalar $\lambda$ when the two have the same symmetry type, by Schur's lemma; more generally the invariant forms are the fixed points of the $G$-action on the space of forms, and the space of invariant forms is determined by the irreducible constituents of $V$. For a symmetric space the invariant form is the metric, unique up to scale on each irreducible factor, *Riemannian Symmetric Spaces and the Involution*.

**Proof.** The invariance of $h'$ is the statement that the map $V \to \overline{V}^{*}$ it defines is an intertwiner; two intertwiners between irreducible modules differ by a scalar, the standard form of Schur's lemma, *Representations of Groups*. The general statement is the decomposition into isotypic components.

**Remark.** The choice of the form is what makes the theory geometric: the same linear group is the isometry group of many forms, and the adjoint it defines depends on the form. This is the boundary test of the part, read on the operators.

### The Adjoint of an Operator

**Definition.** The **adjoint** of $T \in \operatorname{End}(V)$ with respect to $h$ is the unique operator $T^{*}$ with

$$
h(Tu, v) = h(u, T^{*}v) \qquad \text{for all } u, v \in V,
$$

which exists and is unique because $h$ is non-degenerate.

**Proposition.** The adjoint is a conjugate-linear involution of $\operatorname{End}(V)$ and an anti-automorphism,

$$
(T + S)^{*} = T^{*} + S^{*}, \qquad (\lambda T)^{*} = \overline{\lambda}\, T^{*}, \qquad (ST)^{*} = T^{*}S^{*}, \qquad (T^{*})^{*} = T, \qquad \operatorname{id}^{*} = \operatorname{id},
$$

so $\operatorname{End}(V)$ is an **involutive algebra** (a `*`-algebra) over $F$; the **Hermitian** operators are those with $T^{*} = T$, the **unitary** those with $T^{*}T = \operatorname{id}$, the **normal** those with $T^{*}T = TT^{*}$.

**Proof.** Uniqueness is the non-degeneracy; the identities are the defining relation applied to $uv$ and to the products of three vectors, the anti-automorphism being $(ST)^{*} = T^{*}S^{*}$ because $h(STu,v) = h(Tu, S^{*}v) = h(u, T^{*}S^{*}v)$. This is the algebraic theory of *The Adjoint in an Involutive Algebra* and *Involutions of the Endomorphism Algebra*.

## The Adjoint of a Symmetry Operator

### Symmetries Are Unitary

**Theorem.** For $g \in G$ a symmetry operator the adjoint with respect to the invariant form is the inverse,

$$
g^{*} = g^{-1}, \qquad g^{*}g = gg^{*} = \operatorname{id},
$$

so every element of the symmetry group is a unitary operator of the form; conversely a unitary operator of the form is an isometry, and the group of unitary operators is the isometry group of $h$.

**Proof.** The invariance of the form under $g$ is $h(gu, gv) = h(u,v)$, that is $h(u, g^{*}gv) = h(u,v)$ for all $u,v$, hence $g^{*}g = \operatorname{id}$ by non-degeneracy; then $g^{*} = g^{-1}$. Conversely a unitary operator satisfies $h(Tu,Tv) = h(u,T^{*}Tv) = h(u,v)$, so it is an isometry, and the set of unitary operators is exactly the isometry group, *Isometries and Orthogonal Transformations* and *The Unitary and Symplectic Groups*.

**Corollary.** For the orthogonal group of a quadratic form the adjoint is the transpose-adjoint, $T^{*} = J^{-1}T^{\mathrm{tr}}J$, and for the unitary group of a Hermitian form it is the conjugate transpose, $T^{*} = J^{-1}T^{\dagger}J$; in both cases the symmetry operators are the operators with $T^{*}T = \operatorname{id}$.

**Proof.** The matrix formula of the adjoint in a basis in which the form has the matrix $J$, read in the two cases.

### The Invariant Form and the Lie Algebra

**Proposition.** The Lie algebra of the symmetry group is the space of operators skew-adjoint with respect to the invariant form,

$$
\mathrm{Lie}(G) = \{X \in \operatorname{End}(V) : X^{*} = -X\},
$$

so the one-parameter groups of symmetries are the exponentials of the skew-adjoint operators; the Hermitian operators are the $i$ times the skew-adjoint ones in the complex case, and the flow of a skew-adjoint operator preserves the form.

**Proof.** Differentiate $h(e^{tX}u, e^{tX}v) = h(u,v)$ at $t = 0$: $h(Xu,v) + h(u,Xv) = 0$, i.e., $X^{*} = -X$; conversely the exponential of a skew-adjoint operator is unitary, the standard Lie-correspondence, *Lie Groups*.

**Remark.** The realisation of the symmetry group inside the unitary operators of the form is a **representation** of $G$ by operators, and the statement $g^{*} = g^{-1}$ holds **for the elements of the group**, without reference to any involution on the group. The two structures are distinguished in the next section.

## The Involution on the Operators and the Two Involutions

### The Operator Involution

**Definition.** The **operator involution** on $\operatorname{End}(V)$ is the map $T \mapsto T^{*}$; the operators it fixes are the Hermitian ones, and the operators it inverts are the skew-adjoint ones, so the involution on the operators is the same structure as the involution on the elements of the group `- * Theory`, transported to the algebra of operators.

**Proposition.** The operator involution is an involutive anti-automorphism of the algebra $\operatorname{End}(V)$, it makes the algebra a `*`-algebra, and its interaction with a subalgebra is what the unitary group of the form is defined by:

$$
U(V,h) = \{T : T^{*}T = \operatorname{id}\} = \{T : T^{*} = T^{-1}\}.
$$

**Proof.** The anti-automorphism and the involution are the proposition of the previous section; the characterisation of the unitary group is the definition.

### The Two Involutions

**Theorem (the two structures do not coincide).** Let $\rho$ be a representation of the symmetry group $G$ by isometries of the invariant form $h$, so that $\rho(g)^{*} = \rho(g)^{-1}$ for every $g$, and let $\sigma$ be an involution of the **elements** of $G$. Then the identity

$$
\rho(\sigma(g)) = \rho(g)^{*} \qquad \text{for all } g \in G
$$

holds if and only if

$$
\rho\bigl(g\,\sigma(g)\bigr) = \operatorname{id} \qquad \text{for all } g \in G,
$$

because $\rho(\sigma(g)) = \rho(g)^{-1}$ is equivalent to $\rho(g)\rho(\sigma(g)) = \operatorname{id}$; the representation is then a **`*`-representation** for the involution $\sigma$. The condition depends on the representation and on the involution together, and it is **not** a consequence of the definitions: the involution on the elements and the adjoint on the operators are two structures, and the identity is an additional property that is proved for the representations that have it and is never assumed.

**Proof.** The adjoint of an isometry is its inverse, $\rho(g)^{*} = \rho(g)^{-1}$, by the unitarity theorem above, so the identity is the equation $\rho(\sigma(g)) = \rho(g)^{-1}$, which by multiplicativity is $\rho(g)\rho(\sigma(g)) = \rho(g\sigma(g)) = \operatorname{id}$. This is the general criterion. The theory of the algebras with an involution and of the `*`-representations is *The Adjoint in an Involutive Algebra*, *Unitary Operators of an Involutive Algebra* and *The Adjoint Representation and the Involution*.

**Corollary (the abelian case and the obstruction).** If the image $\rho(G)$ is abelian and the involution is the inversion on it, $\sigma(g)g \in \ker\rho$, the identity holds; conversely, when $\sigma$ is an automorphism, the identity forces $\rho(G)$ to be abelian: it gives $\rho(\sigma(gh)) = \rho(gh)^{-1} = \rho(h)^{-1}\rho(g)^{-1}$ and also $\rho(\sigma(g)\sigma(h)) = \rho(g)^{-1}\rho(h)^{-1}$, so the two orders of the inverses agree and the image is abelian. Hence for a nonabelian symmetry group the involution on the elements and the adjoint on the operators are genuinely different structures, and no faithful `*`-representation exists for an automorphic $\sigma$; the familiar coincidences occur for abelian images.

**Proof.** The first statement is the criterion with $\sigma(g) = g^{-1}$ on the image; the second is the computation displayed: $\sigma$ an automorphism gives $\rho(\sigma(gh)) = \rho(\sigma(g)\sigma(h)) = \rho(g)^{-1}\rho(h)^{-1}$ and the homomorphism property gives $\rho(\sigma(gh)) = \rho(gh)^{-1} = \rho(h)^{-1}\rho(g)^{-1}$, so $\rho(h)^{-1}\rho(g)^{-1} = \rho(g)^{-1}\rho(h)^{-1}$ for all $g, h$, which is the commutativity of $\rho(G)$.

**Remark.** This is the distinction the general brief makes: **the involution on the elements and the adjoint on the operators are two structures, not one.** The group `- * Theory` read the involution $\sigma$ on the elements; this group reads the adjoint on the operators; and the two agree only in a `*`-representation, which is proved case by case.

## Worked Cases

**Example (the orthogonal group).** Let $h = Q$ be a quadratic form of signature $(p,q)$ and $G = O(p,q)$; the adjoint is $T^{*} = J^{-1}T^{\mathrm{tr}}J$, the symmetry operators satisfy $g^{*} = g^{-1}$, and the operator involution is the transpose-adjoint of *The Orthogonal Group and the Involutive Automorphism*. The Cartan involution $\theta(g) = JgJ^{-1}$ of the elements is **not** the adjoint in general: for the defining representation, $\theta(g)$ is the identity on the block-diagonal $K$ and $-1$ on $\mathfrak{p}$, while $g^{*} = g^{-1}$; the two coincide only for the elements with $JgJ^{-1} = g^{-1}$, which is a proper subset unless the group is abelian.

**Example (the unitary group).** Let $h$ be a Hermitian form of signature $(p,q)$ and $G = U(p,q)$; the adjoint is the conjugate transpose $T^{*} = J^{-1}T^{\dagger}J$, and the symmetry operators satisfy $g^{*} = g^{-1}$. The Cartan involution $\theta(g) = JgJ^{-1}$ of the elements does **not** satisfy $\rho(\theta(g)) = \rho(g)^{*}$ in the defining representation: the condition is $JgJ^{-1} = g^{-1}$, which holds only for the elements of order two that commute with $J$, and it fails for a rotation of the definite part through an angle other than $0$ or $\pi$. The defining representation of a nonabelian unitary group is therefore not a `*`-representation for the Cartan involution, which is the generic behaviour of the theorem.

**Example (the symmetric group of a figure).** Let $F$ be a figure in a Euclidean space and $G = \operatorname{Sym}(F)$ its symmetry group, a subgroup of $O(n)$; the invariant form is the Euclidean one, the adjoint is the transpose, and every symmetry satisfies $g^{*} = g^{-1}$. The operator involution inverts the rotations and fixes the reflections, so the reflections are Hermitian ($g^{*} = g$) as well as unitary, while a rotation through an angle other than $0$ or $\pi$ is unitary and not Hermitian; the picture is the finite case of the general theory.

**Example (the failing case).** Let $G = G_1\times G_2$ with $G_1$ and $G_2$ simple, let $\sigma(g_1,g_2) = (g_2,g_1)$ be the exchange involution of the elements, and let $\rho$ be the representation on $V_1$ where $G_2$ acts trivially; then $\rho(\sigma(g)) = \rho(g_2)$ does not depend on $g_1$, while $\rho(g)^{*}$ does, so the identity fails and the representation is not a `*`-representation for this involution. The example shows that the equality of the two structures is a genuine restriction.

## Summary

A form $h$ invariant under a symmetry group $G$ defines the adjoint $T^{*}$ of an operator by $h(Tu,v) = h(u,T^{*}v)$; the adjoint is a conjugate-linear involutive anti-automorphism, so the operator algebra is a `*`-algebra, and the Hermitian, unitary and normal operators are defined by $T^{*} = T$, $T^{*}T = \operatorname{id}$ and $T^{*}T = TT^{*}$. Every symmetry operator is unitary, $g^{*} = g^{-1}$, and the unitary operators of the form are exactly the isometries, so the symmetry group is a subgroup of the unitary group $U(V,h)$ and its Lie algebra consists of the skew-adjoint operators; for the orthogonal group the adjoint is the transpose-adjoint and for the unitary group the conjugate transpose. The involution $T \mapsto T^{*}$ on the operators and the involution $\sigma$ on the elements of the group are two different structures: the identity $\rho(\sigma(g)) = \rho(g)^{*}$ holds exactly when $\rho(g\sigma(g)) = \operatorname{id}$ for all $g$, so it holds for an abelian image with the inversion and, when $\sigma$ is an automorphism, it forces the image to be abelian; it is proved for the representations that have it and never assumed. The adjoint of the standard operators of the group is the subject of the following articles of this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h$ | the invariant form, quadratic, bilinear or Hermitian |
| $G$ | the symmetry group, a subgroup of the isometry group of $h$ |
| $T^{*}$ | the adjoint of $T$, $h(Tu,v) = h(u,T^{*}v)$ |
| $T^{*} = T$, $T^{*}T = \operatorname{id}$ | Hermitian and unitary operators |
| $g^{*} = g^{-1}$ | every symmetry operator is unitary |
| $\{X : X^{*} = -X\}$ | the Lie algebra of the symmetry group |
| $U(V,h)$ | the unitary group of the form; $\{T : T^{*}T = \operatorname{id}\}$ |
| $T \mapsto T^{*}$ | the operator involution; a `*`-algebra structure |
| $\sigma(g) = (g^{*})^{-1}$ | the Cartan involution manufactured from the form |
| $\rho(\sigma(g)) = \rho(g)^{*}$ | the `*`-representation identity; proved, not assumed |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the invariant form, the adjoint of an isometry and the symmetric spaces.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for unitary representations, the adjoint with respect to an invariant form and the `*`-representations.
- Sterling K. Berberian, *Baer `*`-Rings* (Springer, 1972), for the algebraic theory of the adjoint and the unitary elements in an involutive ring.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint of a bounded operator, the self-adjoint and the unitary operators.
- Israel M. Gel'fand and Mark A. Naimark, *Unitäre Darstellungen der klassischen Gruppen* (Akademie-Verlag, 1957), for the unitary representations and the invariant forms of the classical groups.
