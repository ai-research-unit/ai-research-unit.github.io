
# __The Graded Adjoint Action on a Module over a Symmetry Group__

## Introduction

A graded module over a graded symmetry group is a vector space split into even and odd parts on which the group acts by an action compatible with the two gradings; the **adjoint action** on its endomorphisms is the conjugation $T \mapsto \rho(g)T\rho(g)^{-1}$, and the **adjoint** of a graded operator is defined with a sign: on a graded algebra the operator involution satisfies

$$
(S T)^{*} = (-1)^{\lvert S\rvert\,\lvert T\rvert}\, T^{*}S^{*},
$$

the **sign rule** of the graded adjoint. The sign is the Koszul sign that appears wherever two odd objects are exchanged, and it is the whole difference between the adjoint action on a graded module and its ungraded shadow. The parity of the adjoint is tied to the parity of the operator — the adjoint of an even operator is even, of an odd operator is odd — and the adjoint action of the group is compatible with the grading precisely when the invariant form on the module is graded and the group acts by graded isometries.

The article treats the graded module and the graded action, the graded invariant form and the adjoint of an operator on it, the adjoint action with the sign rule, and the worked cases. The graded module, the graded action and the Koszul sign are *The Graded Action on a Module over a Symmetry Group*, the operator whose adjoint is computed; the adjoint of a single operator and the operator involution are *The Adjoint of a Symmetry Operator* and *Unitary Operators of a Symmetry Group*, the first articles of this group; the graded algebras, the sign rule and the supertrace are *Superalgebras and Graded Structures*, *Involutive Graded Algebras* and *Superalgebras and Graded Structures*; the exterior algebra and the Clifford module are *The Exterior Algebra* and *Pin Representations and Clifford Modules with Signed Inner Conjugation*; the modules over a group are *Modules over an Algebra* and *Representations of Groups*. The closing article of the parallel category, on the adjoint action in the complex-vector-space setting, is treated in *Geometry on Linear Spaces*, written in parallel. The grade involution $\alpha$ is the parity of the grading and not the involution of the group `- * Theory`; the two-structures theorem, whether an involution on the elements agrees with the adjoint on the operators, is *The Adjoint of a Symmetry Operator* and is cited only.

The article has four sections: the graded module and the graded action; the graded form and the adjoint; the adjoint action and the sign rule; and the worked cases. Throughout, $G$ is a graded group with central sign element $z$ and grade involution $\alpha$, $M = M_0\oplus M_1$ a graded module over $G$ with a **graded form** — a bilinear form $B$ with $B(M_i, M_j) = 0$ for $i \neq j$, non-degenerate on each part, and symmetric or antisymmetric on each part in the graded sense $B(x,y) = (-1)^{\lvert x\rvert\lvert y\rvert}B(y,x)$ — and $\operatorname{End}(M) = \operatorname{End}(M)_0\oplus\operatorname{End}(M)_1$ the graded endomorphism algebra.

## The Graded Module and the Graded Action

### The Graded Module

**Definition.** A **graded module** over the graded group $G$ is a graded vector space $M = M_0\oplus M_1$ with an action $\rho : G \to GL(M)$ such that a homogeneous $g$ of parity $\lvert g\rvert$ carries $M_i$ to $M_{i+\lvert g\rvert}$,
$$
\rho(g)(M_i) \subseteq M_{i+\lvert g\rvert},
$$
so that even elements act by parity-preserving operators and odd elements by parity-reversing isomorphisms; the action is the **graded action** of *The Graded Action on a Module over a Symmetry Group*.

**Proposition.** A graded action decomposes as $\rho = \rho_0\oplus\rho_1$ with $\rho_0 : G_0 \to GL(M_0)\times GL(M_1)$ and $\rho_1 : G_1 \to \mathrm{Iso}(M_0,M_1)$; the endomorphism algebra is graded, $\operatorname{End}(M)_i = \{T : T(M_j)\subseteq M_{j+i}\}$, and the graded commutator
$$
[T, S\} = TS - (-1)^{\lvert T\rvert\lvert S\rvert}ST
$$
makes $\operatorname{End}(M)$ a graded Lie algebra, the **sign** $(-1)^{\lvert T\rvert\lvert S\rvert}$ being the Koszul sign.

**Proof.** The decomposition is the definition of a graded action on each homogeneous point; the parity of a composition is the sum of the parities, $\lvert TS\rvert = \lvert T\rvert+\lvert S\rvert$, so $\operatorname{End}(M)$ is graded, and the graded commutator is graded-antisymmetric and satisfies the graded Jacobi identity, *Superalgebras and Graded Structures*.

### The Geometric Modules

**Example (the exterior algebra).** Let $V$ be a quadratic space and $M = \Lambda V = \bigoplus_k\Lambda^k V$ with the grading by parity of degree; the orthogonal group acts by $g\cdot(v_1\wedge\cdots\wedge v_k) = (gv_1)\wedge\cdots\wedge(gv_k)$, a graded action with $G_0 = SO(V,q)$ acting on each part and $G_1$ (an odd isometry, an element of $O(V,q)$ of determinant $-1$) exchanging them. The module is the basic geometric graded module.

**Example (the Clifford module).** Let $S$ be a Clifford module of a quadratic space; the pin group acts by Clifford multiplication, and an odd element of the group acts by a parity-reversing operator, so $S$ is a graded module over $\mathrm{Pin}(V,q)$; this is *Pin Representations and Clifford Modules with Signed Inner Conjugation*.

## The Graded Form and the Adjoint

### The Graded Form

**Definition.** A **graded form** on $M$ is a bilinear form $B$ with $B(M_i,M_j) = 0$ for $i \neq j$, non-degenerate on each part, and of graded symmetry $B(x,y) = (-1)^{\lvert x\rvert\lvert y\rvert}B(y,x)$; it is **invariant** under the graded action when $B(\rho(g)x,\rho(g)y) = B(x,y)$ for all $g$.

**Proposition.** The **graded adjoint** of $T \in \operatorname{End}(M)$ with respect to a graded form is the unique operator $T^{*}$ with $B(Tx, y) = (-1)^{\lvert T\rvert\lvert x\rvert}B(x, T^{*}y)$ for homogeneous $x$, and it satisfies
$$
(T^{*})^{*} = T, \qquad (T + S)^{*} = T^{*} + S^{*}, \qquad (ST)^{*} = (-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*},
$$
the **sign rule** of the graded adjoint; the parity of the adjoint is the parity of the operator, $\lvert T^{*}\rvert = \lvert T\rvert$.

**Proof.** The defining relation and non-degeneracy give existence and uniqueness; the involution and additivity are the same as in the ungraded case; the product rule acquires the Koszul sign because in the pairing $B(STx, y)$ the operator $S$ of parity $\lvert S\rvert$ must be moved past $T^{*}$ of parity $\lvert T\rvert$, each crossing contributing $(-1)^{\lvert S\rvert\lvert T\rvert}$. The parity statement is that $T^{*}$ carries $M_j$ to $M_{j+\lvert T\rvert}$ if and only if $T$ does. This is the graded `*`-algebra theory of *Involutive Graded Algebras*.

### Invariance and the Unitary Operators

**Proposition.** If the graded form is invariant under the graded action, then every $\rho(g)$ is a graded isometry and its graded adjoint is its inverse, $\rho(g)^{*} = \rho(g)^{-1}$, with the parity of the inverse equal to the parity of $g$; the graded adjoint of an even element is even, and of an odd element is odd. The graded isometries form the **graded unitary group** of the module, $U(M,B) = \{T : T^{*}T = \operatorname{id}\}$ in the graded sense.

**Proof.** The invariance $B(\rho(g)x,\rho(g)y) = B(x,y)$ gives $\rho(g)^{*}\rho(g) = \operatorname{id}$ with the sign convention of the graded adjoint, hence $\rho(g)^{*} = \rho(g)^{-1}$; the parity statement is that the inverse of a homogeneous element has the same parity, and the defining relation of the graded form forces the adjoint to have the parity of the operator.

## The Adjoint Action and the Sign Rule

### The Adjoint Action

**Definition.** The **adjoint action** of $G$ on the graded endomorphism algebra is the conjugation

$$
\operatorname{Ad}_g : \operatorname{End}(M) \longrightarrow \operatorname{End}(M), \qquad \operatorname{Ad}_g(T) = \rho(g)\,T\,\rho(g)^{-1},
$$

restricted to the graded endomorphisms; it is a graded representation of $G$ on $\operatorname{End}(M)$, the parity of $\operatorname{Ad}_g(T)$ being the parity of $T$.

**Proposition.** The adjoint action preserves the grading, $\operatorname{Ad}_g(\operatorname{End}(M)_i)\subseteq\operatorname{End}(M)_i$; it preserves the graded commutator, $\operatorname{Ad}_g[T,S\} = [\operatorname{Ad}_gT, \operatorname{Ad}_gS\}$; and it preserves the **supertrace** $\operatorname{str}(T) = \operatorname{tr}(T|_{M_0}) - \operatorname{tr}(T|_{M_1})$, so that the module carries the invariant graded trace form $\langle S, T\rangle = \operatorname{str}(S^{*}T)$.

**Proof.** The parity of $\rho(g)T\rho(g)^{-1}$ is $\lvert g\rvert + \lvert T\rvert + \lvert g\rvert = \lvert T\rvert$ since the parities are in $\mathbb{Z}/2$; the commutator is preserved because conjugation is an algebra automorphism and the Koszul sign is a function of the parities, which are preserved; the supertrace is invariant under the adjoint action because $\operatorname{str}(TS) = (-1)^{\lvert T\rvert\lvert S\rvert}\operatorname{str}(ST)$, the graded trace property, which gives $\operatorname{str}(\rho(g)T\rho(g)^{-1}) = \operatorname{str}(T)$ by the cyclicity with the sign. This is *Superalgebras and Graded Structures*.

### The Sign Rule in the Adjoint Action

**Theorem (the sign rule and the adjoint action).** For an even element $g$ the adjoint action is a graded algebra automorphism of $\operatorname{End}(M)$ preserving the involution $^{*}$ and the supertrace; hence it is a graded isometry of the invariant graded trace form and its graded adjoint is the adjoint action of the inverse,

$$
\bigl(\operatorname{Ad}_g\bigr)^{*} = \operatorname{Ad}_{g^{-1}} \qquad (g \text{ even}),
$$

with respect to $\langle S, T\rangle = \operatorname{str}(S^{*}T)$. For an odd element $g$ the adjoint action still preserves the grading and the graded commutator but carries the extra Koszul sign $(-1)^{\lvert S\rvert\lvert g\rvert} = (-1)^{\lvert S\rvert}$ on a homogeneous $S$; the sign is the graded correction that the exchange of two odd objects requires, and it is the same Koszul sign as in the product rule $(ST)^{*} = (-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}$.

**Proof.** For even $g$ the sign $(-1)^{\lvert S\rvert\lvert g\rvert}$ is $1$, so $\operatorname{Ad}_g(S^{*}) = (\operatorname{Ad}_g S)^{*}$; the supertrace is invariant under the adjoint action by the graded trace property, so $\operatorname{Ad}_g$ is an isometry of $\langle\cdot,\cdot\rangle$ and its graded adjoint is its inverse $\operatorname{Ad}_{g^{-1}}$. For odd $g$ the sign $(-1)^{\lvert S\rvert\lvert g\rvert} = (-1)^{\lvert S\rvert}$ is $1$ on the even endomorphisms and $-1$ on the odd ones, which is the displayed correction; the product rule is the proposition on the graded adjoint.

**Remark.** The sign rule is not an accident of the convention: it is the Koszul sign that makes the graded adjoint an involution, $(T^{*})^{*} = T$, and it is the same sign that appears in the graded commutator and in the supertrace. The graded adjoint action is compatible with the grading because it preserves it, and it is compatible with the involution because the sign rule is exactly the correction that the exchange of two odd operators requires.

### The Two-Structures Boundary

**Proposition.** As in the ungraded case, the adjoint on the operators and an involution $\sigma$ on the elements of $\rho(G)$ are two structures; the identity $\rho(\sigma(g)) = \rho(g)^{*}$ (with the graded adjoint) is the equation $\rho(g\sigma(g)) = \operatorname{id}$ of *The Adjoint of a Symmetry Operator* and is not assumed. The **grade involution** $\alpha$ of the group is a parity and not such a $\sigma$; the sign rule of the graded adjoint is a statement about the operators alone.

**Proof.** The criterion and the abelian obstruction are proved for the ungraded case and apply verbatim to the graded case with the graded adjoint, since the criterion compares $\rho(\sigma(g))$ with $\rho(g)^{-1}$, and the graded adjoint of a graded isometry is also its inverse. The grade involution is a parity by the definition of the grading.

## Worked Cases

**Example (the exterior algebra of a quadratic space).** Let $M = \Lambda V$ with the grading by degree parity and the graded form induced by the quadratic form on $V$ and the determinant pairing on the top degree; the orthogonal group acts by graded isometries, the adjoint action on $\operatorname{End}(\Lambda V)$ is the conjugation with the Koszul sign, and the adjoint of the exterior multiplication by a vector is the interior multiplication, with the sign rule $(\epsilon_v)^{*} = \iota_v$ up to sign. The example is the standard graded module of the geometry.

**Example (the Clifford module).** Let $M = S$ be a Clifford module and $G = \mathrm{Pin}(V,q)$; an even element acts by a parity-preserving operator and an odd element by a parity-reversing one, the graded form is the Clifford inner product, and the adjoint of the Clifford multiplication by a vector $u$ is the multiplication by $u^{*}$, with the sign rule carrying the reality condition of *The Signed Adjoint of the Left Multiplication on a Symmetry Group*.

**Example (the supersymmetric module).** Let $M = M_0\oplus M_1$ with $\dim M_0 = \dim M_1$ and the graded form the pairing of the two parts; the adjoint action of the group is the graded conjugation, its adjoint is the conjugation by the inverse, and the supertrace vanishes on the odd part, $\operatorname{str}(T) = 0$ for $T$ odd. The example shows the supertrace and the sign rule in the simplest supersymmetric case.

**Example (the trivial grading).** Let $M_1 = 0$; then the graded action is an ordinary action, the graded form is an ordinary invariant form, and the sign rule is vacuous, $(-1)^{\lvert S\rvert\lvert T\rvert} = 1$; the adjoint action is the ordinary conjugation and the article reduces to the ungraded theory. The example is the check that the sign is the only new ingredient.

## Summary

A graded module $M = M_0\oplus M_1$ over a graded group carries a graded action, even elements acting by parity-preserving and odd elements by parity-reversing operators; the graded form is invariant under a graded isometry, and the **graded adjoint** of an operator satisfies $(ST)^{*} = (-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}$ with the Koszul sign, has the parity of the operator, and inverts a graded isometry. The adjoint action $\operatorname{Ad}_g(T) = \rho(g)T\rho(g)^{-1}$ preserves the grading, the graded commutator $[T,S\} = TS - (-1)^{\lvert T\rvert\lvert S\rvert}ST$ and the supertrace, so the module carries the invariant graded trace form $\langle S,T\rangle = \operatorname{str}(S^{*}T)$; its own adjoint is the adjoint action of the inverse for an even element, with the sign rule carried into the operator involution. The grade involution is a parity and not the involution of the group `- * Theory`, and the agreement of an involution on the elements with the adjoint on the operators is the two-structures criterion of *The Adjoint of a Symmetry Operator*, never assumed. The exterior algebra of a quadratic space, the Clifford module of the pin group and the supersymmetric module are the geometric instances, and the trivial grading recovers the ungraded theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M = M_0\oplus M_1$ | the graded module; even and odd parts |
| $\rho(g)(M_i)\subseteq M_{i+\lvert g\rvert}$ | the graded action |
| $\lvert T\rvert$ | the parity of a graded endomorphism |
| $[T,S\} = TS - (-1)^{\lvert T\rvert\lvert S\rvert}ST$ | the graded commutator; the Koszul sign |
| $B(x,y) = (-1)^{\lvert x\rvert\lvert y\rvert}B(y,x)$ | the graded symmetry of the form |
| $T^{*}$ with $(ST)^{*} = (-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}$ | the graded adjoint; the sign rule |
| $U(M,B)$ | the graded unitary group of the module |
| $\operatorname{Ad}_g(T) = \rho(g)T\rho(g)^{-1}$ | the adjoint action on the endomorphisms |
| $(\operatorname{Ad}_g)^{*} = \operatorname{Ad}_{g^{-1}}$ | the adjoint of the adjoint action (for $g$ even) |
| $\operatorname{str}(T) = \operatorname{tr}(T|_{M_0}) - \operatorname{tr}(T|_{M_1})$ | the supertrace; the graded trace form |

## Further Reading

- Pierre Deligne and John W. Morgan, *Notes on Supersymmetry (following Joseph Bernstein)*, in *Quantum Fields and Strings: A Course for Mathematicians* (American Mathematical Society, 1999), for the sign rule, the graded adjoint and the supertrace.
- Yuri I. Manin, *Gauge Field Theory and Complex Geometry* (Springer, second edition, 1997), for the graded modules, the Koszul sign and the graded Lie algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the graded modules of the Clifford algebra and the pin action.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the graded Lie algebras and the graded commutator.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint of a bounded operator, in the ungraded comparison.
