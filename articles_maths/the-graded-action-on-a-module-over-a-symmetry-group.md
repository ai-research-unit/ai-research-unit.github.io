
# __The Graded Action on a Module over a Symmetry Group__

## Introduction

A linear action of a symmetry group is a **module** over the group: a linear space on which the group acts by linear operators, equivalently a module over the group algebra, the representations of *Representations of Groups* and *Modules over an Algebra*. When the group is **graded** — even and odd elements, grade involution $\alpha$ — and the module is **graded** — even and odd parts, $M = M_0\oplus M_1$ — the action has to be compatible with the two gradings: the **graded action** is the action in which an element of parity $|g|$ carries $M_i$ to $M_{i+|g|}$. Even elements preserve the parity of a vector, odd elements reverse it, and the compatibility of the action with the graded structure maps imposes a **sign rule**, the Koszul sign $(-1)^{|m||n|}$ in every place where two odd objects are exchanged.

The geometric origin of the graded module is the space of tensors and forms of a space with a form. On the exterior algebra $\Lambda V$ of a quadratic space the orthogonal group acts linearly, and a symmetry preserves the degree of a form and hence its parity: the natural action is graded. On the module of spinors the pin group acts by Clifford multiplication, and an odd element of the group acts by a parity-reversing operator. The grading is not an extra structure imposed on the geometry; it is the parity of the degree of the form, and the sign rule is the Koszul sign of the exterior algebra read as an equivariance.

The article has five sections: modules over a symmetry group; the graded module and the graded action; the sign rule; the fixed submodule; and the worked cases. The group algebra of a graded group, its grading and its parity are *Superalgebras and Graded Structures* and *Involutive Graded Algebras*; the exterior algebra and its Koszul sign are *The Exterior Algebra*; the Clifford module and the pin action are *Pin Representations and Clifford Modules with Signed Inner Conjugation*; the modules over a group are *Representations of Groups* and *Modules over an Algebra*. None of that is re-derived. The grading and the grade involution are those of *The Signed Sandwich on a Symmetry Group* and *The Signed Left Multiplication on a Symmetry Group*, the previous articles of this group; no adjoint is taken, and the adjoint action on the endomorphism module is the group `- * Operator Theory`.

Throughout, $k$ is a field, $G$ a graded group with central sign element $z$ and grade involution $\alpha$, and $M = M_0\oplus M_1$ a graded $k$-vector space.

## Modules over a Symmetry Group

### The Linear Action

**Definition.** A **module over the symmetry group** $G$ (a $G$-module, or a linear representation) is a $k$-vector space $M$ with a linear action $\rho : G \to GL(M)$, $g \mapsto \rho(g)$, satisfying $\rho(e) = \mathrm{id}$ and $\rho(gh) = \rho(g)\rho(h)$; equivalently, a module over the group algebra $kG$ in the sense of *Modules over an Algebra*. A **submodule** is a subspace stable under every $\rho(g)$; the module is **irreducible** when it has no proper nonzero submodule.

**Proposition.** The assignment of a $G$-module is the same thing as a representation of $G$; the space of module maps between two $G$-modules is the space of intertwiners $\operatorname{Hom}_G(M,N)$, and the endomorphism ring $\operatorname{End}_G(M)$ of a free module of finite rank is a matrix ring over the division ring of the irreducible constituents, by Schur's lemma and the Jordan–Hölder theory.

**Proof.** The dictionary between an action and a representation is the definition; the endomorphism statement is the module-theoretic form of Schur's lemma, *Representations of Groups*.

### The Geometric Modules

**Example (the functions).** The action operators of *Operators on a Symmetry Group* make the space $\mathcal{F}(X)$ of functions on the space $X$ a module over the symmetry group, the permutation representation of the action.

**Example (the exterior algebra of a quadratic space).** Let $V$ be a quadratic space over $k$, let $G \leq O(V,q)$ act on $V$, and let $M = \Lambda V = \bigoplus_k \Lambda^k V$; the action of $G$ extends uniquely to the exterior algebra by the universal property, $g\cdot(v_1\wedge\cdots\wedge v_k) = (gv_1)\wedge\cdots\wedge(gv_k)$, and it preserves each degree. This is the basic geometric module, and its grading by parity of degree is the grading of the next section.

**Example (the Clifford module).** Let $V$ be a quadratic space and let $S$ be a Clifford module, a module over $\mathrm{Cl}(V,q)$; the pin group $\mathrm{Pin}(V,q) \leq \Gamma(V,q)$ acts on $S$ by the restrictions of the algebra elements, and the action of an odd element is not the action of a linear map of the algebra but its composition with the parity. This is *Pin Representations and Clifford Modules with Signed Inner Conjugation*.

## The Graded Module and the Graded Action

### The Grading

**Definition.** A **graded module** over the graded group $G$ is a graded $k$-vector space $M = M_0\oplus M_1$ with an action $\rho : G \to GL(M)$ such that

$$
\rho(g)\bigl(M_i\bigr) \subseteq M_{i + |g|}, \qquad g \in G\ \text{homogeneous}, \quad i \in \mathbb{Z}/2 ,
$$

where $|g| = 0$ for even $g$ and $|g| = 1$ for odd $g$. Equivalently, $M$ is a module over the group algebra $kG$ that is graded and whose multiplication respects the grading, the group algebra being a graded algebra by the parity of its basis elements. The action is the **graded action**.

**Proposition.** A graded action decomposes as

$$
\rho = \rho_0 \oplus \rho_1, \qquad \rho_0 : G_0 \to GL(M_0)\times GL(M_1), \qquad \rho_1 : G_1 \to \mathrm{Iso}(M_0, M_1),
$$

so that the even subgroup acts by parity-preserving operators on each part and the odd coset acts by parity-reversing isomorphisms. When $G_1 = \varnothing$, the grading is trivial and a graded action is an ordinary action preserving each part.

**Proof.** A homogeneous $g$ of parity zero satisfies $\rho(g)M_i \subseteq M_i$, so its restriction to each part is an isomorphism; a homogeneous $g$ of parity one satisfies $\rho(g)M_i \subseteq M_{i+1}$, so it exchanges the two parts and restricts to an isomorphism $M_0 \to M_1$ with inverse the restriction of $\rho(g^{-1})$, which has the same parity because $g^{-1}$ is odd. The decomposition over $G_0\sqcup G_1$ assembles the two cases.

### Compatibility with the Grade Involution

**Proposition.** For a graded action the action twisted by the grade involution is

$$
\rho\circ\alpha : g \longmapsto \rho\bigl(\alpha(g)\bigr) = \rho\bigl(\varepsilon(g)\bigr)\,\rho(g),
$$

equal to $\rho(g)$ on the even part and to $\rho(z)\rho(g)$ on the odd part; when the central sign element acts on the module by the parity operator, $\rho(z) = \Pi$, this reads

$$
\rho\bigl(\alpha(g)\bigr) = \Pi^{\,|g|}\,\rho(g), \qquad g \in G,
$$

so that the twist by the grade involution is the identity on the even coset and the parity operator on the odd one. The map $\rho\circ\alpha$ is again a graded action, with the same even part and the opposite odd part, and it is the module-level **parity-reversed action**.

**Proof.** By the definition of α, $\alpha(g) = \varepsilon(g)g$ with $\varepsilon(g) \in \{e,z\}$, so $\rho(\alpha(g)) = \rho(\varepsilon(g))\rho(g)$, and $\rho(\varepsilon(g))$ is $\rho(e) = \mathrm{id}$ on the even coset and $\rho(z)$ on the odd one. If $\rho(z) = \Pi$ then $\rho(\alpha(g)) = \Pi^{|g|}\rho(g)$, which is the displayed form. Multiplicativity and the parity condition for $\rho\circ\alpha$ are inherited from $\rho$ and $\alpha$, so it is a graded action.

**Remark.** The identity is the module form of the parity sign of *The Signed Sandwich on a Symmetry Group*: the central sign element $z$ of the group acts on the module by the parity operator, $\rho(z) = \Pi$, and the grade involution of the group and the parity of the module are then the same sign read on the two sides. The twisted action $\rho\circ\alpha$ is what the signed operators of the preceding articles induce on a module.

## The Sign Rule

### The Koszul Sign

**Definition.** The **sign rule** of the graded action is the Koszul sign $(-1)^{|m||n|}$ in the exchange of two homogeneous vectors: the **flip** of the tensor product is

$$
\tau : M\otimes M \longrightarrow M\otimes M, \qquad \tau(m\otimes n) = (-1)^{|m||n|}\, n\otimes m ,
$$

and the sign rule is the requirement that $\tau$ be equivariant for the diagonal action,

$$
\tau\,\rho(g)\otimes\rho(g) = \rho(g)\otimes\rho(g)\,\tau, \qquad g \in G .
$$

**Proposition.** The flip is equivariant for the diagonal action of a graded group on the tensor square, with the Koszul sign, and no smaller sign works: the diagonal action is $g\cdot(m\otimes n) = (g\cdot m)\otimes(g\cdot n)$ and the parity of a tensor is the sum $|m\otimes n| = |m|+|n|$, so the exchange contributes $(-1)^{|m||n|}$ on both sides.

**Proof.** Evaluate both sides on $m\otimes n$ with $g$ homogeneous. The left side is $\tau((gm)\otimes(gn)) = (-1)^{|gm||gn|}(gn)\otimes(gm) = (-1)^{(|g|+|m|)(|g|+|n|)}g\cdot(n\otimes m)$. The right side is $g\cdot\tau(m\otimes n) = (-1)^{|m||n|}g\cdot(n\otimes m)$. The two exponents are congruent modulo two, because $(|g|+|m|)(|g|+|n|) - |m||n| = |g|(|g|+|m|+|n|) \equiv 0$, using $|g|^2 = |g|$; so the two sides agree.

### The Graded Leibniz Rule

**Proposition (the graded derivation).** Let $M$ be a graded algebra and let $G$ act by algebra automorphisms of parity $|g|$, $\rho(g)(mn) = \rho(g)(m)\,\rho(g)(n)$. Then every element acts as an automorphism of parity $|g|$, and the associativity of the action is the parity-respecting composition. If instead an element $D$ of parity $|D|$ acts as a **graded derivation**, it obeys the graded Leibniz rule

$$
D(mn) = (Dm)\,n + (-1)^{|D||m|}\,m\,(Dn),
$$

and the rule is the sign rule of the odd part of the action.

**Proof.** The automorphism statement is the multiplicativity of $\rho(g)$ and the parity condition $\rho(g)(M_i)\subseteq M_{i+|g|}$; the Leibniz rule is the definition of a graded derivation of parity $|D|$, and it is what the odd elements of a graded action on an algebra become when the action is written infinitesimally. In parity zero the rule is the ordinary product rule, and the only novelty is the sign on the odd part.

**Remark.** The sign rule is not an extra axiom of the graded action; it is the parity $(-1)^{|m||n|}$ of the ambient graded structure, and the action respects it because the action respects the grading. The two examples that show it are the exterior algebra, whose wedge product is graded-commutative by exactly this sign, and the endomorphism module, whose supercommutator $[T,U] = TU - (-1)^{|T||U|}UT$ is the associative bracket of *Superalgebras and Graded Structures*.

## The Fixed Submodule

**Definition.** The **fixed submodule** of a $G$-module $M$ is $M^G = \{m : \rho(g)m = m\ \text{for all } g \in G\}$, the largest submodule on which $G$ acts trivially; the **coinvariants** are $M_G = M/\langle m - \rho(g)m : g \in G, m \in M\rangle$.

**Proposition.** The fixed space of the **even** subgroup $G_0$ is graded, $M^{G_0} = M_0^{G_0}\oplus M_1^{G_0}$, because the even elements preserve the parity. The full fixed space $M^G$ is graded when the odd part of $G$ is empty or acts without fixed vectors; when an odd element $g$ fixes a vector $m$, the odd part $m_1$ is determined by the even part through $m_1 = \rho(g)m_0$ and $m_0 = \rho(g)m_1$, so a fixed vector of an odd element need not be homogeneous, and the fixed space is then not the sum of its even and odd parts.

**Proof.** For even $g$ the condition $\rho(g)M_i\subseteq M_i$ makes the fixed-space equation hold on each parity separately; for odd $g$ one has $\rho(g)M_0\subseteq M_1$ and $\rho(g)M_1\subseteq M_0$, so if $m = m_0+m_1$ is fixed then $\rho(g)m_0 = m_1$ and $\rho(g)m_1 = m_0$, which is consistent and gives a non-homogeneous solution whenever $m_0$ is a nonzero vector with $\rho(g)^2 m_0 = m_0$.

**Example (the invariants of the exterior algebra).** For the action of $O(V,q)$ on $\Lambda V$, the even subgroup — the rotations — preserves the degree, and its fixed space is the span of the volume element in each degree where a nonzero invariant form exists, namely $k$ in degree $0$ and $k\omega$ in degree $n$ for odd $n$; the full fixed space of $O(V,q)$ is $k\cdot 1$ in even dimension and $k\cdot 1\oplus k\cdot\omega$ in odd dimension, by the first fundamental theorem of the orthogonal group, quoted. The example shows the generic behaviour: the even part contributes a graded fixed space, and the odd part removes the invariants that the reflections move.

## Worked Cases

**Example (the exterior algebra).** Let $V$ be a quadratic space over $k$ of characteristic not $2$, $G = O(V,q)$, and $M = \Lambda V$ with the induced action. The module is graded by the parity of the degree, even elements of $G$ preserve each $\Lambda^k V$ and the parity, odd elements — the reflections — exchange the even and the odd degrees; the sign rule is the Koszul rule $\alpha\wedge\beta = (-1)^{|\alpha||\beta|}\beta\wedge\alpha$ of *The Exterior Algebra*, and it is equivariant for the action. The fixed submodule is $k$ in even-dimensional $V$ and $k\oplus k\omega$ in odd dimension, $\omega$ the volume element.

**Example (the Clifford module).** Let $S$ be a Clifford module over $V$ and let $G = \mathrm{Pin}(V,q)$ act through the algebra. An even element of the pin group acts by a linear map preserving the parity of the spinor decomposition, and an odd element acts by a parity-reversing map; the grade involution of the group acts by the parity operator of $S$, and this is the module form of the signed inner conjugation. The action is the graded action of *Pin Representations and Clifford Modules with Signed Inner Conjugation*.

**Example (the group algebra over itself).** Let $M = kG$ with the left regular action. The module is graded by the parity of the group elements, $kG = (kG)_0\oplus(kG)_1$; the left multiplication by an even element preserves the parity and by an odd element reverses it; the fixed submodule under the left action is the span of the elements $\sum_{a\in G} a$ for finite $G$, and the sign rule is the graded multiplication of the group algebra. The **adjoint** action on the same module is the subject of *The Graded Adjoint Action on a Module over a Symmetry Group* in the group `- * Operator Theory`.

## Summary

A module over a symmetry group is a linear space with a linear action, equivalently a module over the group algebra; the geometric instances are the functions of the space, the exterior algebra of a quadratic space and the Clifford module. When the group is graded and the module is graded, the **graded action** is the action with $\rho(g)M_i \subseteq M_{i+|g|}$: even elements preserve the parity and odd elements reverse it, and the decomposition $\rho = \rho_0\oplus\rho_1$ separates the parity-preserving part of the even subgroup from the parity-reversing isomorphisms of the odd coset. The grade involution twists the action to $\rho(\alpha(g)) = \rho(\varepsilon(g))\rho(g) = \Pi^{\,|g|}\rho(g)$, the identity on the even coset and the parity operator on the odd one; the central sign element acts as the parity operator. The **sign rule** is the Koszul sign $(-1)^{|m||n|}$, appearing in the equivariance of the flip $\tau(m\otimes n) = (-1)^{|m||n|}n\otimes m$ for the diagonal action and in the graded Leibniz rule $D(mn) = (Dm)n + (-1)^{|D||m|}m(Dn)$ of an odd derivation; it is the parity of the graded structure and not an independent axiom. The fixed space of the even subgroup is graded; a fixed vector of an odd element need not be homogeneous, its two parities being exchanged by the element, and the fixed submodule of the full group is graded exactly when the odd part moves no invariant. No adjoint is taken; the adjoint action on the endomorphism module is the group `- * Operator Theory`.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M = M_0\oplus M_1$ | a graded module; even and odd parts |
| $\rho : G \to GL(M)$ | the action; the graded action when $\rho(g)M_i\subseteq M_{i+|g|}$ |
| $|g|$, $|m|$ | the parity of a homogeneous element |
| $kG$ | the group algebra, a graded algebra |
| $\Pi$ | the parity operator, $+1$ on $M_0$ and $-1$ on $M_1$ |
| $\rho(\alpha(g)) = \Pi^{\,|g|}\rho(g)$ | the action twisted by the grade involution |
| $\tau(m\otimes n) = (-1)^{|m||n|}n\otimes m$ | the Koszul flip; the sign rule |
| $D(mn) = (Dm)n + (-1)^{|D||m|}m(Dn)$ | the graded Leibniz rule |
| $M^G$, $M_G$ | fixed submodule and coinvariants |
| $\Lambda V$ | the exterior algebra, the basic geometric graded module |

## Further Reading

- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for graded modules, the Koszul sign rule and the graded tensor product.
- Werner Greub, *Multilinear Algebra* (Springer, second edition, 1978), for the exterior algebra, its Koszul sign and the action of the orthogonal group.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for modules over the group algebra and the intertwiners.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the Clifford module, the pin action and the parity of the action.
- Joseph Bernstein, Israel Gel'fand and Sergei Gel'fand, in *Representation Theory of Algebraic Groups*, for the graded and super representations that the parity-preserving and parity-reversing operators define.
