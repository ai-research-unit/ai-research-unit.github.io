# __Lie Algebras: A General Introduction__

## Introduction

This article introduces Lie algebras. The treatment is introductory and purely mathematical. The goal is to explain what a Lie algebra is, why it is a natural construction, and how it relates to the associative algebras studied in the preceding articles.

We assume familiarity with modules and linear maps. No prior knowledge of Lie algebras is required.

In the preceding articles, an **algebra** was defined as a module over a commutative ring $R$ equipped with a bilinear product. No further assumptions were made. We then studied **associative algebras**, in which the product satisfies $(uv)w = u(vw)$. In this article, we study a different specialization: algebras whose product is antisymmetric and satisfies an identity called the **Jacobi identity**. These are called **Lie algebras**.

This article treats the general theory over a **commutative ring**. A separate article, *Lie Algebras: Categorization*, gives a classification organized by ring.

A word on the base structure. The classical theory of Lie algebras assumes that the scalars form a field. But many of the constructions and theorems carry over to the more general setting where the scalars form a **commutative ring**. This is the setting we adopt here. The main differences from the field case are:

- Modules over a commutative ring need not be free, whereas vector spaces over a field always are.
- The classical structure theory (solvable, nilpotent, simple Lie algebras) is cleanest over fields of characteristic zero, and requires care over general commutative rings.
- The classification of simple Lie algebras by Dynkin diagrams requires the base ring to be a field of characteristic zero.

We indicate where these differences matter.

---

## Part I: Why Lie Algebras?

### The Failure of Associativity

In the preceding articles, we studied associative algebras. But not every algebra of interest is associative. Two important examples are:

**The cross product on $\mathbb{R}^3$.** For $u, v \in \mathbb{R}^3$, the cross product $u \times v$ is bilinear and antisymmetric, but it is not associative:

$$
(u \times v) \times w \neq u \times (v \times w).
$$

**The commutator on matrices.** For $A, B \in M_n(R)$, the commutator $[A, B] = AB - BA$ is bilinear and antisymmetric, but it is not associative:

$$
[[A, B], C] \neq [A, [B, C]].
$$

These two examples share a common structure. Both are bilinear, antisymmetric, and satisfy a certain identity that replaces associativity. That identity is the **Jacobi identity**. Algebras with this structure are called **Lie algebras**.

### The Motivating Question

The question that motivates Lie algebras is:

> What structure do the cross product and the commutator share, and what can we do with it?

The answer is that they are both Lie brackets. A Lie algebra is a module equipped with a bilinear, antisymmetric product satisfying the Jacobi identity. The cross product and the commutator are two examples; there are many others.

---

## Part II: The Definition

### Bilinear and Antisymmetric Products

Let $M$ be a module over a commutative ring $R$. A **bilinear product** on $M$ is a function

$$
[\cdot, \cdot] : M \times M \to M
$$

that is linear in each argument separately:

$$
[u + v, w] = [u, w] + [v, w], \qquad [r u, v] = r [u, v],
$$

$$
[u, v + w] = [u, v] + [u, w], \qquad [u, r v] = r [u, v].
$$

The product is **antisymmetric** if

$$
[u, v] = -[v, u]
$$

for all $u, v \in M$. In particular, taking $u = v$, we get

$$
[u, u] = 0
$$

for all $u \in M$, provided that $2$ is not a zero divisor in $R$. Over a general commutative ring, the antisymmetry condition $[u, v] = -[v, u]$ implies $[u, u] = 0$ only if $2$ is invertible or at least not a zero divisor. We assume this throughout.

### The Jacobi Identity

The product satisfies the **Jacobi identity** if

$$
[u, [v, w]] + [v, [w, u]] + [w, [u, v]] = 0
$$

for all $u, v, w \in M$.

The Jacobi identity is the replacement for associativity. It says that the failure of the bracket to be associative is controlled: the three nested brackets sum to zero.

### The Definition

A **Lie algebra** over a commutative ring $R$ is an $R$-module $\mathfrak{g}$ equipped with a bilinear, antisymmetric product $[\cdot, \cdot]$ satisfying the Jacobi identity.

The product $[\cdot, \cdot]$ is called the **Lie bracket**. The elements of $\mathfrak{g}$ are called **Lie algebra elements**, or simply **elements** when the context is clear.

**Key difference from the field case.** Over a field, every Lie algebra is a vector space, so it has a well-defined dimension. Over a general commutative ring, a Lie algebra is a module, which need not be free. When the module is free of rank $n$, we say that the Lie algebra has **rank** $n$. The classical structure theory assumes the module is free and finitely generated.

### Why the Jacobi Identity?

The Jacobi identity is not arbitrary. It has several equivalent formulations, each of which reveals a different aspect of its meaning.

**Formulation 1: The sum of cyclic permutations.** The identity as stated above:

$$
[u, [v, w]] + [v, [w, u]] + [w, [u, v]] = 0.
$$

**Formulation 2: The adjoint action is a derivation.** For each $u \in \mathfrak{g}$, define the **adjoint action** $\mathrm{ad}_u : \mathfrak{g} \to \mathfrak{g}$ by

$$
\mathrm{ad}_u(v) = [u, v].
$$

The Jacobi identity is equivalent to

$$
\mathrm{ad}_u([v, w]) = [\mathrm{ad}_u(v), w] + [v, \mathrm{ad}_u(w)].
$$

In words: the adjoint action $\mathrm{ad}_u$ is a **derivation** of the bracket. This is the precise sense in which the Jacobi identity replaces associativity: it says that the bracket behaves like a derivative with respect to itself.

**Formulation 3: The bracket is a representation.** The map $u \mapsto \mathrm{ad}_u$ is a **representation** of $\mathfrak{g}$ on itself: it is linear, and it satisfies

$$
\mathrm{ad}_{[u, v]} = [\mathrm{ad}_u, \mathrm{ad}_v],
$$

where the bracket on the right is the commutator of linear maps. This is the **adjoint representation** of $\mathfrak{g}$.

The Jacobi identity is what makes the adjoint action a derivation, and it is what makes the adjoint representation a representation. Without it, the bracket would not have these properties, and the theory would be much poorer.

---

## Part III: The Relationship with Associative Algebras

### The Commutator Bracket

Every associative algebra is a Lie algebra when equipped with the commutator bracket. This is a general fact, and it is worth stating explicitly.

Let $A$ be an associative algebra over a commutative ring $R$, with product written $xy$. Define

$$
[x, y] = xy - yx.
$$

This bracket is bilinear, antisymmetric, and satisfies the Jacobi identity. So $A$, equipped with this bracket, is a Lie algebra.

This construction applies in particular to the Clifford algebras studied in the other articles. Every Clifford algebra is an associative algebra, hence a Lie algebra with the commutator bracket. This is the reason the theory of Lie algebras and the theory of Clifford algebras are connected.

The converse is not true: not every Lie algebra arises from an associative algebra in this way. The cross product on $\mathbb{R}^3$ is an example of a Lie algebra that does not arise from an associative algebra. So the class of Lie algebras is strictly larger than the class of Lie algebras that come from associative algebras.

### The Subspace of Bivectors

Inside a Clifford algebra, the subspace of bivectors forms a Lie subalgebra under the commutator bracket. This Lie subalgebra is isomorphic to the orthogonal Lie algebra $\mathfrak{so}(V, Q)$.

This is the algebraic origin of the relationship between Clifford algebras and orthogonal groups. The bivectors generate the rotations, and the commutator bracket on the bivectors is the Lie bracket of the orthogonal Lie algebra.

---

## Part IV: Basic Properties

### Subalgebras and Ideals

A **Lie subalgebra** of a Lie algebra $\mathfrak{g}$ is a submodule $\mathfrak{h} \subseteq \mathfrak{g}$ such that

$$
[u, v] \in \mathfrak{h}
$$

for all $u, v \in \mathfrak{h}$. In other words, $\mathfrak{h}$ is closed under the bracket.

A **Lie ideal** of $\mathfrak{g}$ is a submodule $\mathfrak{i} \subseteq \mathfrak{g}$ such that

$$
[u, v] \in \mathfrak{i}
$$

for all $u \in \mathfrak{g}$ and $v \in \mathfrak{i}$. In other words, $\mathfrak{i}$ is closed under bracketing with any element of $\mathfrak{g}$.

Every ideal is a subalgebra, but not every subalgebra is an ideal. The distinction is the same as in ring theory.

### Homomorphisms

A **Lie algebra homomorphism** from a Lie algebra $\mathfrak{g}$ to a Lie algebra $\mathfrak{h}$ is an $R$-linear map $\varphi : \mathfrak{g} \to \mathfrak{h}$ that preserves the bracket:

$$
\varphi([u, v]) = [\varphi(u), \varphi(v)]
$$

for all $u, v \in \mathfrak{g}$.

An **isomorphism** is a bijective homomorphism. If there is an isomorphism from $\mathfrak{g}$ to $\mathfrak{h}$, we say that $\mathfrak{g}$ and $\mathfrak{h}$ are **isomorphic**, written $\mathfrak{g} \cong \mathfrak{h}$.

The kernel of a homomorphism is an ideal, and every ideal is the kernel of some homomorphism (the quotient map). This is the content of the first isomorphism theorem for Lie algebras.

### Quotients

Let $\mathfrak{g}$ be a Lie algebra and let $\mathfrak{i}$ be an ideal of $\mathfrak{g}$. The **quotient Lie algebra** $\mathfrak{g}/\mathfrak{i}$ is the set of cosets $\{u + \mathfrak{i} : u \in \mathfrak{g}\}$ with addition, scalar multiplication, and bracket defined by

$$
(u + \mathfrak{i}) + (v + \mathfrak{i}) = (u + v) + \mathfrak{i},
$$

$$
r(u + \mathfrak{i}) = (r u) + \mathfrak{i},
$$

$$
[u + \mathfrak{i}, v + \mathfrak{i}] = [u, v] + \mathfrak{i}.
$$

These operations are well-defined precisely because $\mathfrak{i}$ is an ideal.

---

## Part V: The Structure of Lie Algebras

### The Center

The **center** of a Lie algebra $\mathfrak{g}$ is the set of elements that bracket to zero with every element of $\mathfrak{g}$:

$$
Z(\mathfrak{g}) = \{z \in \mathfrak{g} : [z, v] = 0 \text{ for all } v \in \mathfrak{g}\}.
$$

The center is always an abelian ideal of $\mathfrak{g}$.

### The Derived Subalgebra

The **derived subalgebra** of a Lie algebra $\mathfrak{g}$ is the submodule spanned by all brackets:

$$
[\mathfrak{g}, \mathfrak{g}] = \mathrm{span}\{[u, v] : u, v \in \mathfrak{g}\}.
$$

The derived subalgebra is always an ideal of $\mathfrak{g}$. It measures how far $\mathfrak{g}$ is from being abelian: $\mathfrak{g}$ is abelian if and only if $[\mathfrak{g}, \mathfrak{g}] = 0$.

### Solvable and Nilpotent Lie Algebras

A Lie algebra $\mathfrak{g}$ is **solvable** if the sequence

$$
\mathfrak{g}^{(0)} = \mathfrak{g}, \qquad \mathfrak{g}^{(k+1)} = [\mathfrak{g}^{(k)}, \mathfrak{g}^{(k)}],
$$

eventually reaches zero.

A Lie algebra $\mathfrak{g}$ is **nilpotent** if the sequence

$$
\mathfrak{g}_0 = \mathfrak{g}, \qquad \mathfrak{g}_{k+1} = [\mathfrak{g}, \mathfrak{g}_k],
$$

eventually reaches zero.

Every nilpotent Lie algebra is solvable, but not every solvable Lie algebra is nilpotent.

**Key difference from the field case.** The notions of solvable and nilpotent Lie algebras are defined over any commutative ring, but the classical structure theory (Levi decomposition, classification of semisimple Lie algebras) requires the base ring to be a field of characteristic zero. Over a general commutative ring, the theory is more subtle.

### Simple Lie Algebras

A Lie algebra $\mathfrak{g}$ is **simple** if it is non-abelian and has no nontrivial ideals.

Simple Lie algebras are the building blocks of the theory. Every finite-dimensional Lie algebra over a field of characteristic zero is a semidirect product of a solvable Lie algebra and a semisimple Lie algebra, and every semisimple Lie algebra is a direct sum of simple Lie algebras. This is the **Levi decomposition**.

### The Classification of Simple Lie Algebras

Over the complex numbers, the simple Lie algebras are classified by their **root systems**, which are encoded in combinatorial objects called **Dynkin diagrams**. The classification was achieved by Killing and Cartan in the late nineteenth century. The simple Lie algebras fall into four infinite families

$$
A_n, \quad B_n, \quad C_n, \quad D_n,
$$

and five exceptional algebras

$$
G_2, \quad F_4, \quad E_6, \quad E_7, \quad E_8.
$$

This classification is one of the great achievements of nineteenth-century mathematics, and it is the foundation of much of modern representation theory.

**Key difference from the field case.** This classification requires the base ring to be a field of characteristic zero. Over a general commutative ring, the classification does not apply, and the theory of Lie algebras is more complicated.

---

## Part VI: Representations

### The Definition

A **representation** of a Lie algebra $\mathfrak{g}$ on an $R$-module $V$ is a Lie algebra homomorphism

$$
\rho : \mathfrak{g} \to \mathfrak{gl}(V),
$$

where $\mathfrak{gl}(V)$ is the Lie algebra of $R$-linear endomorphisms of $V$ with the commutator bracket.

In other words, it is an $R$-linear map that preserves the bracket:

$$
\rho([u, v]) = [\rho(u), \rho(v)] = \rho(u)\rho(v) - \rho(v)\rho(u).
$$

The module $V$ is called the **representation space**. The representation is **faithful** if $\rho$ is injective.

### Examples

**The trivial representation.** The map $\rho(u) = 0$ for all $u \in \mathfrak{g}$.

**The adjoint representation.** The map $\mathrm{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ defined by $\mathrm{ad}_u(v) = [u, v]$.

**The standard representation of $\mathfrak{sl}(n, R)$.** The natural action of $\mathfrak{sl}(n, R)$ on $R^n$ by matrix multiplication.

### Why Representations Matter

Representations are the way Lie algebras act on other mathematical objects.

The classification of representations of a given Lie algebra is one of the central problems of representation theory. For simple Lie algebras over a field of characteristic zero, the finite-dimensional representations are classified by their **highest weights**.

---

## Part VII: Lie Algebras and Lie Groups

### The Relationship

Lie algebras are the infinitesimal versions of **Lie groups**. A Lie group is a group that is also a smooth manifold, with the group operations being smooth maps.

Every Lie group $G$ has an associated Lie algebra $\mathfrak{g}$, which is the tangent space to $G$ at the identity element. The bracket on $\mathfrak{g}$ is derived from the group commutator. The Lie algebra captures the local structure of the group.

### Why This Matters

The Lie algebra is often easier to study than the Lie group. It is a linear object (a module with a bracket), while the group is a nonlinear object (a manifold with a group structure). Many questions about Lie groups can be reduced to questions about their Lie algebras.

This is the reason Lie algebras were introduced in the first place. Sophus Lie, in the late nineteenth century, found that the local structure of continuous groups of symmetries could be captured by a linear object: the Lie algebra.

---

## Summary

**A Lie algebra** is a module over a commutative ring equipped with a bilinear, antisymmetric product satisfying the Jacobi identity.

**The Jacobi identity** is the replacement for associativity. It says that the adjoint action is a derivation, and it makes the adjoint representation a representation.

**Every associative algebra is a Lie algebra** when equipped with the commutator bracket. This applies in particular to the Clifford algebras.

**The structure theory** of Lie algebras includes subalgebras, ideals, the center, the derived subalgebra, solvable and nilpotent Lie algebras, and simple Lie algebras.

**Representations** of Lie algebras are homomorphisms into $\mathfrak{gl}(V)$. They are the way Lie algebras act on other mathematical objects.

**Lie algebras** are the infinitesimal versions of Lie groups.

**Key differences from the field case.**

- Over a field, every Lie algebra is a vector space, so it has a well-defined dimension. Over a general commutative ring, a Lie algebra is a module, which need not be free.
- The classical structure theory (Levi decomposition, classification of semisimple Lie algebras) requires the base ring to be a field of characteristic zero.
- The classification of simple Lie algebras by Dynkin diagrams requires the base ring to be a field of characteristic zero.

The classification of these Lie algebras is organized by ring.



---

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972).
- Nathan Jacobson, *Lie Algebras* (Dover, 1979).
- Karin Erdmann and Mark J. Wildon, *Introduction to Lie Algebras* (Springer, 2006).
- Brian Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015).
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 1987).
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).

