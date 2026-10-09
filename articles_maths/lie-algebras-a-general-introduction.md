# __Lie Algebras: A General Introduction__

## Introduction

This article introduces Lie algebras. The treatment is introductory and purely mathematical. The goal is to explain what a Lie algebra is, why it is a natural construction, and how it relates to the associative algebras studied in the preceding articles.

We assume familiarity with modules and linear maps. No prior knowledge of Lie algebras is required.

In the preceding articles, an **algebra** was defined as a module over a commutative ring $R$ equipped with a bilinear product. No further assumptions were made. We then studied **associative algebras**, in which the product satisfies $(uv)w = u(vw)$. In this article, we study a different specialization: algebras whose product is antisymmetric and satisfies an identity called the **Jacobi identity**. These are called **Lie algebras**.

This article treats the general theory over a **commutative ring**. The companion article *Structure of Lie Algebras* gives the classification of the Lie algebras the corpus meets.

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

A **Lie algebra** over a commutative ring $R$ is an $R$-module $\mathrm{G}$ equipped with a bilinear, antisymmetric product $[\cdot, \cdot]$ satisfying the Jacobi identity.

The product $[\cdot, \cdot]$ is called the **Lie bracket**. The elements of $\mathrm{G}$ are called **Lie algebra elements**, or simply **elements** when the context is clear.

**Key difference from the field case.** Over a field, every Lie algebra is a vector space, so it has a well-defined dimension. Over a general commutative ring, a Lie algebra is a module, which need not be free. When the module is free of rank $n$, we say that the Lie algebra has **rank** $n$. The classical structure theory assumes the module is free and finitely generated.

### Why the Jacobi Identity?

The Jacobi identity is not arbitrary. It has several equivalent formulations, each of which reveals a different aspect of its meaning.

**Formulation 1: The sum of cyclic permutations.** The identity as stated above:

$$
[u, [v, w]] + [v, [w, u]] + [w, [u, v]] = 0.
$$

**Formulation 2: The adjoint action is a derivation.** For each $u \in \mathrm{G}$, define the **adjoint action** $\mathrm{ad}_u : \mathrm{G} \to \mathrm{G}$ by

$$
\mathrm{ad}_u(v) = [u, v].
$$

The Jacobi identity is equivalent to

$$
\mathrm{ad}_u([v, w]) = [\mathrm{ad}_u(v), w] + [v, \mathrm{ad}_u(w)].
$$

In words: the adjoint action $\mathrm{ad}_u$ is a **derivation** of the bracket. This is the precise sense in which the Jacobi identity replaces associativity: it says that the bracket behaves like a derivative with respect to itself.

**Formulation 3: The bracket is a representation.** The map $u \mapsto \mathrm{ad}_u$ is a **representation** of $\mathrm{G}$ on itself: it is linear, and it satisfies

$$
\mathrm{ad}_{[u, v]} = [\mathrm{ad}_u, \mathrm{ad}_v],
$$

where the bracket on the right is the commutator of linear maps. This is the **adjoint representation** of $\mathrm{G}$.

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

This construction applies in particular to every associative algebra: an associative algebra is a Lie algebra with the commutator bracket. The Clifford algebras are the central instance — they are associative and carry a form — and the Lie algebras they yield, the bivectors together with the orthogonal Lie algebra $\mathrm{SO}(V,Q)$ and the rotations these generate, belong to Part II and to Part IV, where the form and the distance are available, and are named only.

The converse is not true: not every Lie algebra arises from an associative algebra in this way. The cross product on $\mathbb{R}^3$ is an example of a Lie algebra that does not arise from an associative algebra. So the class of Lie algebras is strictly larger than the class of Lie algebras that come from associative algebras.

---

## Part IV: Basic Properties

### Subalgebras and Ideals

A **Lie subalgebra** of a Lie algebra $\mathrm{G}$ is a submodule $\mathrm{H} \subseteq \mathrm{G}$ such that

$$
[u, v] \in \mathrm{H}
$$

for all $u, v \in \mathrm{H}$. In other words, $\mathrm{H}$ is closed under the bracket.

A **Lie ideal** of $\mathrm{G}$ is a submodule $\mathrm{I} \subseteq \mathrm{G}$ such that

$$
[u, v] \in \mathrm{I}
$$

for all $u \in \mathrm{G}$ and $v \in \mathrm{I}$. In other words, $\mathrm{I}$ is closed under bracketing with any element of $\mathrm{G}$.

Every ideal is a subalgebra, but not every subalgebra is an ideal. The distinction is the same as in ring theory.

### Homomorphisms

A **Lie algebra homomorphism** from a Lie algebra $\mathrm{G}$ to a Lie algebra $\mathrm{H}$ is an $R$-linear map $\varphi : \mathrm{G} \to \mathrm{H}$ that preserves the bracket:

$$
\varphi([u, v]) = [\varphi(u), \varphi(v)]
$$

for all $u, v \in \mathrm{G}$.

An **isomorphism** is a bijective homomorphism. If there is an isomorphism from $\mathrm{G}$ to $\mathrm{H}$, we say that $\mathrm{G}$ and $\mathrm{H}$ are **isomorphic**, written $\mathrm{G} \cong \mathrm{H}$.

The kernel of a homomorphism is an ideal, and every ideal is the kernel of some homomorphism (the quotient map). This is the content of the first isomorphism theorem for Lie algebras.

### Quotients

Let $\mathrm{G}$ be a Lie algebra and let $\mathrm{I}$ be an ideal of $\mathrm{G}$. The **quotient Lie algebra** $\mathrm{G}/\mathrm{I}$ is the set of cosets $\{u + \mathrm{I} : u \in \mathrm{G}\}$ with addition, scalar multiplication, and bracket defined by

$$
(u + \mathrm{I}) + (v + \mathrm{I}) = (u + v) + \mathrm{I},
$$

$$
r(u + \mathrm{I}) = (r u) + \mathrm{I},
$$

$$
[u + \mathrm{I}, v + \mathrm{I}] = [u, v] + \mathrm{I}.
$$

These operations are well-defined precisely because $\mathrm{I}$ is an ideal.

---

## Part V: The Structure of Lie Algebras

### The Center

The **center** of a Lie algebra $\mathrm{G}$ is the set of elements that bracket to zero with every element of $\mathrm{G}$:

$$
Z(\mathrm{G}) = \{z \in \mathrm{G} : [z, v] = 0 \text{ for all } v \in \mathrm{G}\}.
$$

The center is always an abelian ideal of $\mathrm{G}$.

### The Derived Subalgebra

The **derived subalgebra** of a Lie algebra $\mathrm{G}$ is the submodule spanned by all brackets:

$$
[\mathrm{G}, \mathrm{G}] = \mathrm{span}\{[u, v] : u, v \in \mathrm{G}\}.
$$

The derived subalgebra is always an ideal of $\mathrm{G}$. It measures how far $\mathrm{G}$ is from being abelian: $\mathrm{G}$ is abelian if and only if $[\mathrm{G}, \mathrm{G}] = 0$.

### Solvable and Nilpotent Lie Algebras

A Lie algebra $\mathrm{G}$ is **solvable** if the sequence

$$
\mathrm{G}^{(0)} = \mathrm{G}, \qquad \mathrm{G}^{(k+1)} = [\mathrm{G}^{(k)}, \mathrm{G}^{(k)}],
$$

eventually reaches zero.

A Lie algebra $\mathrm{G}$ is **nilpotent** if the sequence

$$
\mathrm{G}_0 = \mathrm{G}, \qquad \mathrm{G}_{k+1} = [\mathrm{G}, \mathrm{G}_k],
$$

eventually reaches zero.

Every nilpotent Lie algebra is solvable, but not every solvable Lie algebra is nilpotent.

**Key difference from the field case.** The notions of solvable and nilpotent Lie algebras are defined over any commutative ring, but the classical structure theory (Levi decomposition, classification of semisimple Lie algebras) requires the base ring to be a field of characteristic zero. Over a general commutative ring, the theory is more subtle.

### Simple Lie Algebras

A Lie algebra $\mathrm{G}$ is **simple** if it is non-abelian and has no nontrivial ideals.

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

A **representation** of a Lie algebra $\mathrm{G}$ on an $R$-module $V$ is a Lie algebra homomorphism

$$
\rho : \mathrm{G} \to \mathrm{GL}(V),
$$

where $\mathrm{GL}(V)$ is the Lie algebra of $R$-linear endomorphisms of $V$ with the commutator bracket.

In other words, it is an $R$-linear map that preserves the bracket:

$$
\rho([u, v]) = [\rho(u), \rho(v)] = \rho(u)\rho(v) - \rho(v)\rho(u).
$$

The module $V$ is called the **representation space**. The representation is **faithful** if $\rho$ is injective.

### Examples

**The trivial representation.** The map $\rho(u) = 0$ for all $u \in \mathrm{G}$.

**The adjoint representation.** The map $\mathrm{ad} : \mathrm{G} \to \mathrm{GL}(\mathrm{G})$ defined by $\mathrm{ad}_u(v) = [u, v]$.

**The standard representation of $\mathrm{SL}(n, R)$.** The natural action of $\mathrm{SL}(n, R)$ on $R^n$ by matrix multiplication.

### Why Representations Matter

Representations are the way Lie algebras act on other mathematical objects.

The classification of representations of a given Lie algebra is one of the central problems of representation theory. For simple Lie algebras over a field of characteristic zero, the finite-dimensional representations are classified by their **highest weights**.

---

## Part VII: Lie Algebras and Lie Groups

### The Relationship

Lie algebras are the infinitesimal versions of **Lie groups**. A Lie group is a group that is also a smooth manifold, with the group operations being smooth maps.

Every Lie group $G$ has an associated Lie algebra $\mathrm{G}$, which is the tangent space to $G$ at the identity element. The bracket on $\mathrm{G}$ is derived from the group commutator. The Lie algebra captures the local structure of the group.

### Why This Matters

The Lie algebra is often easier to study than the Lie group. It is a linear object (a module with a bracket), while the group is a nonlinear object (a manifold with a group structure). Many questions about Lie groups can be reduced to questions about their Lie algebras.

This is the reason Lie algebras were introduced in the first place. Sophus Lie, in the late nineteenth century, found that the local structure of continuous groups of symmetries could be captured by a linear object: the Lie algebra.

---

## Summary

**A Lie algebra** is a module over a commutative ring equipped with a bilinear, antisymmetric product satisfying the Jacobi identity.

**The Jacobi identity** is the replacement for associativity. It says that the adjoint action is a derivation, and it makes the adjoint representation a representation.

**Every associative algebra is a Lie algebra** when equipped with the commutator bracket. This applies in particular to the matrix algebras, the endomorphism algebras and the enveloping algebras; the Clifford algebras are the instance that belongs to Part II.

**The structure theory** of Lie algebras includes subalgebras, ideals, the center, the derived subalgebra, solvable and nilpotent Lie algebras, and simple Lie algebras.

**Representations** of Lie algebras are homomorphisms into $\mathrm{GL}(V)$. They are the way Lie algebras act on other mathematical objects.

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

