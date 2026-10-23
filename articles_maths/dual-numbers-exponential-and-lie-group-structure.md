
# __Dual-Numbers Exponential and Lie Group Structure__

## Introduction

This article develops the Lie theory of the dual-number algebra: the Lie algebra structure on $\mathbb{D}'$ itself, the exponential map, the group of units as a Lie group, the parabolic one-parameter subgroup, and the quotient of the unit group by the scalars. It follows *Dual-Numbers Algebra* for the algebra and its abelian Lie bracket, *Dual-Numbers Norm and Invertibility* for the unit group, *Dual-Numbers Automorphisms and Derivations* for the derivation algebra, and *Shears and Parabolic Rotations* for the shear. The comparison throughout is with the split complex algebra, whose unit group is the two-component quotient $\mathbb{R}^\times$; here the unit group is the much smaller group $\mathbb{R}^\times \times \mathbb{R}$.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the exponential is a formal series when $R$ is a commutative $\mathbb{Q}$-algebra and an analytic series over the geometric specialisation $R = \mathbb{R}$, and then the algebra is written $\mathbb{D}'$. A general dual number is

$$
Q = q + \varepsilon q', \qquad q, q' \in R,
$$

with $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$, norm $\langle Q\rangle = q^2$, maximal ideal $\mathrm{M} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$, and unit group $(\mathbb{D}')^\times = \{q \neq 0\}$.

## The Lie Algebra Structure

### The Lie Bracket

**Definition.** The **Lie bracket** on $\mathbb{D}'_R$ is the commutator

$$
[Q_1, Q_2] = Q_1Q_2 - Q_2Q_1.
$$

**Theorem.** $\mathbb{D}'_R$ is a **commutative** algebra, so its Lie bracket vanishes identically:

$$
[Q_1, Q_2] = 0 \qquad \text{for all } Q_1, Q_2 \in \mathbb{D}'_R.
$$

Hence the Lie algebra $\mathrm{G} = \mathbb{D}'_R$ is **abelian**.

**Proof.** $Q_1Q_2 = Q_2Q_1$ for all $Q_1, Q_2$ because multiplication of dual numbers is commutative.

### Nilpotence

**Definition.** A Lie algebra $\mathrm{G}$ is **nilpotent of class $c$** if the descending central series $\mathrm{G}^1 = \mathrm{G}$, $\mathrm{G}^{k+1} = [\mathrm{G}, \mathrm{G}^k]$ reaches $0$ at step $c + 1$, and $\mathrm{G}$ is **abelian** when $[\mathrm{G}, \mathrm{G}] = 0$.

**Proposition.** $\mathrm{G} = \mathbb{D}'_R$ is a nilpotent Lie algebra of class $1$; equivalently, its derived subalgebra is zero, $[\mathrm{G}, \mathrm{G}] = 0$.

**Proof.** The derived subalgebra is spanned by brackets $[Q_1,Q_2]$, all of which vanish; the series is $\mathrm{G} \supset 0$.

So the dual-number Lie algebra is the abelian two-dimensional real Lie algebra, the simplest nilpotent example. Its enveloping algebra is the polynomial algebra on two commuting generators, and its only Lie structure is the underlying vector space.

### The Lie Algebra of a Commutative Associative Algebra

**Remark.** For any associative algebra $A$ the commutator makes $A$ a Lie algebra, and the Jacobi identity is a consequence of associativity. When $A$ is commutative the bracket vanishes, so the Lie algebra records no more than the $R$-module structure. The interesting Lie theory of $\mathbb{D}'$ therefore lives not in $\mathbb{D}'$ itself but in its derivation algebra $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$ and in the Lie group structure of the unit group, which are treated below.

## The Exponential

### Definition and Convergence

**Definition.** Let $R$ be a commutative $\mathbb{Q}$-algebra, so that $k!$ is invertible for every $k$. The **exponential** of $Q \in \mathbb{D}'_R$ is the formal series

$$
\exp(Q) = \sum_{k \geq 0} \frac{Q^k}{k!}.
$$

Over $R = \mathbb{R}$ the series converges for every $Q$, in the topology of $\mathbb{D}' \cong \mathbb{R}^2$.

### Closed Form

**Theorem.** For every $Q = q + \varepsilon q'$,

$$
\boxed{\; \exp(q + \varepsilon q') = \exp(q)\bigl(1 + \varepsilon q'\bigr) = \exp(q) + \exp(q)\varepsilon q' \;}.
$$

**Proof.** By the binomial expansion and $\varepsilon^2 = 0$, $(q + \varepsilon q')^k = q^k + k q^{k-1}\varepsilon q'$ for $k \geq 1$. Summing,

$$
\exp(q + \varepsilon q') = \sum_{k \geq 0}\frac{q^k}{k!} + \varepsilon \sum_{k \geq 1}\frac{k q^{k-1}q'}{k!} = \exp(q) + \varepsilon\, q' \sum_{k \geq 1}\frac{q^{k-1}}{(k-1)!} = \exp(q) + \exp(q)\varepsilon q',
$$

the two series being the exponential of $q$.

**Corollary.** $\exp(\varepsilon) = 1 + \varepsilon$ and $\exp(s\varepsilon) = 1 + s\varepsilon$ for every $s$; the exponential of a purely infinitesimal element is a shear.

### Worked Values

**Example.** $\exp(2 + 3\varepsilon) = e^{2}(1 + 3\varepsilon)$; numerically $e^{2} = 7.389056\ldots$, so the real part is $7.389056\ldots$ and the infinitesimal part is $3e^{2} = 22.167168\ldots$.

**Example.** The dual logarithm inverts the exponential on the shear group $1 + \mathrm{M}$, where it is $\log(1 + s\varepsilon) = s\varepsilon$; thus $\log(1 + 5\varepsilon) = 5\varepsilon$ and $\log(1 - \varepsilon) = -\varepsilon$.

### The Group Homomorphism Property

**Theorem.** The exponential is a homomorphism from the additive group $(\mathbb{D}'_R, +)$ to the multiplicative group $(\mathbb{D}'_R)^\times$:

$$
\exp(Q_1 + Q_2) = \exp(Q_1)\exp(Q_2).
$$

**Proof.** The exponential is the usual exponential of the commutative associative algebra $\mathbb{D}'_R$, and for commuting $Q_1, Q_2$ the identity $\exp(Q_1+Q_2) = \exp(Q_1)\exp(Q_2)$ follows by the binomial theorem. Alternatively, $\exp(q_1 + \varepsilon q'_1)\exp(q_2 + \varepsilon q'_2) = \exp(q_1)(1 + \varepsilon q'_1)\exp(q_2)(1 + \varepsilon q'_2) = \exp(q_1+q_2)(1 + (q'_1+q'_2)\varepsilon) = \exp((q_1+q_2) + \varepsilon(q'_1+q'_2))$, matching $Q_1 + Q_2$.

So $\exp$ is a homomorphism of groups, and the image is a subgroup of the unit group.

## The Group of Units

### The Lie Group

**Theorem.** The group of units

$$
(\mathbb{D}'_R)^\times = \{q + \varepsilon q' : q \in R^\times\}
$$

is a group under multiplication, with $(q + \varepsilon q')^{-1} = q^{-1} - q^{-2}\varepsilon q'$. Over $R = \mathbb{R}$ it is a two-dimensional abelian Lie group with the following structure:

$$
\boxed{\; (\mathbb{D}')^\times \cong \mathbb{R}^\times \times (\mathbb{R}, +) \;},
$$

the isomorphism being $q + \varepsilon q' \leftrightarrow (q,\, q'/q)$.

**Proof.** The group axioms and the inverse formula are from *Dual-Numbers Norm and Invertibility*; the isomorphism is the direct-product decomposition of *Shears and Parabolic Rotations*, where the second factor is the shear group $1 + \mathrm{M}$.

### Connected Components

**Proposition.** Over $R = \mathbb{R}$ the unit group has exactly two connected components, $\{q > 0\}$ and $\{q < 0\}$, each contractible; the identity component is

$$
(\mathbb{D}')^\times_0 = \{q > 0\} \cong \mathbb{R}_{>0} \times \mathbb{R}.
$$

**Proof.** The sign of $q$ is a continuous surjective homomorphism $(\mathbb{D}')^\times \to \{\pm 1\}$; the two fibres are half-planes, hence connected and contractible.

### Surjectivity of the Exponential onto the Identity Component

**Theorem.** Over $R = \mathbb{R}$ the exponential

$$
\exp : \mathrm{G} = \mathbb{D}' \longrightarrow (\mathbb{D}')^\times
$$

is injective, with image exactly the identity component $(\mathbb{D}')^\times_0 = \{q > 0\}$. It is therefore a bijection, and in fact a diffeomorphism, onto the identity component.

**Proof.** $\exp(q + \varepsilon q') = \exp(q)(1 + \varepsilon q')$ has real part $\exp(q) > 0$, so the image is contained in $\{q > 0\}$. Conversely, for $Q_1 = q_1 + \varepsilon q'_1$ with $q_1 > 0$ set $q = \log q_1$ and $q' = q'_1/q_1$; then $\exp(q + \varepsilon q') = q_1(1 + \varepsilon q'_1/q_1) = q_1 + \varepsilon q'_1$, so the image is $\{q > 0\}$. For injectivity, $\exp(q + \varepsilon q') = 1$ forces $\exp(q) = 1$, hence $q = 0$, and then $\exp(q)q' = q' = 0$. The map is smooth with the explicit smooth inverse $q_1 + \varepsilon q'_1 \mapsto \log q_1 + (q'_1/q_1)\varepsilon$ on $\{q_1 > 0\}$, so it is a diffeomorphism.

**Remark.** The kernel of the exponential is trivial. This is the sharpest contrast with the complex and matrix cases, where the exponential has a nontrivial kernel: on $\mathbb{C}$ the kernel is $2\pi i\mathbb{Z}$, and on $GL_2(\mathbb{C})$ the exponential is surjective but not injective, with kernel the matrices having eigenvalues in $2\pi i\mathbb{Z}$. Here the exponential is a global diffeomorphism from the abelian Lie algebra onto the identity component, the maximal simply connected abelian case.

## The Parabolic One-Parameter Subgroup

### Definition

**Definition.** The **parabolic one-parameter subgroup** of $(\mathbb{D}')^\times$ is

$$
G = \{1 + s\varepsilon : s \in \mathbb{R}\} = 1 + \mathrm{M}.
$$

### Identification with the Additive Line

**Theorem.** The maps

$$
(\mathbb{R}, +) \longrightarrow G, \qquad s \longmapsto 1 + s\varepsilon, \qquad G \longrightarrow \mathrm{M}, \qquad 1 + s\varepsilon \longmapsto s\varepsilon
$$

are inverse isomorphisms of groups, where $\mathrm{M}$ carries the additive group structure. In particular $G \cong (\mathbb{R},+)$ is a connected, simply connected, one-dimensional abelian Lie group, and it is exactly the image of the exponential of the maximal ideal, $G = \exp(\mathrm{M})$.

**Proof.** $(1 + s\varepsilon)(1 + t\varepsilon) = 1 + (s+t)\varepsilon$ because $\varepsilon^2 = 0$, so the first map is a homomorphism; it is bijective with the displayed inverse; and $\exp(s\varepsilon) = 1 + s\varepsilon$, so $G = \exp(\mathrm{M})$.

### The Unipotent Character

**Proposition.** Every element of $G$ is **unipotent**: it differs from the identity by a nilpotent, $(1 + s\varepsilon) - 1 = s\varepsilon$ with $(s\varepsilon)^2 = 0$. The subgroup $G$ is the unique one-parameter subgroup of $(\mathbb{D}')^\times$ generated by a nilpotent element of the algebra, and it is the image of the algebra's own nilpotent direction.

**Proof.** $(1 + s\varepsilon) - 1 = s\varepsilon$ and $(s\varepsilon)^2 = s^2\varepsilon^2 = 0$, so the displacement from the identity is nilpotent of index two, which is the algebraic form of unipotence; in particular $1 + s\varepsilon$ has no eigenvalue different from $1$ as a linear map of the algebra. The generator is the nilpotent $\varepsilon$, whose exponential is polynomial.

## The Group of Units Modulo Scaling

### The Quotient

**Theorem.** The central scalars embed as $\mathbb{R}^\times \hookrightarrow (\mathbb{D}')^\times$, $q \mapsto q$, and

$$
\boxed{\; (\mathbb{D}')^\times / \mathbb{R}^\times \;\cong\; 1 + \mathrm{M} \;\cong\; (\mathbb{R}, +) \;},
$$

the isomorphism being the class of $q + \varepsilon q'$ mapped to $1 + (q'/q)\varepsilon$, equivalently to the parabolic angle $s = q'/q$.

**Proof.** Every unit is $q(1 + \varepsilon q'/q)$, and multiplying by the scalar $q$ is exactly the quotient by the subgroup $\mathbb{R}^\times$; two units have the same class exactly when their shear parameters agree.

**Corollary.** The quotient is connected, contractible and one-dimensional; it is the space of shears, and it is the same object as the parabolic one-parameter subgroup $G$.

## Comparison with the Split Complex Case

### The Split Complex Case

For the split complex algebra $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$, the unit group is $\mathbb{D}^\times \cong \mathbb{R}^\times \times \mathbb{R}^\times$, of real dimension two and with four contractible components; the exponential from the abelian Lie algebra $\mathbb{R}^2$ is a bijection onto the identity component, exactly as in the dual case. The quotient is

$$
\mathbb{D}^\times/\mathbb{R}^\times \cong \mathbb{R}^\times,
$$

obtained by the ratio of the two idempotent components, and it has two components—unlike the connected quotient $(\mathbb{D}')^\times/\mathbb{R}^\times \cong \mathbb{R}$. The difference is the degeneracy of the norm: the split complex form has two independent directions, so the quotient retains a hyperbola-like two-component structure, while the dual form has one, so the quotient collapses to a line.

### The Table

| | $\mathbb{D}'$ | $\mathbb{D}$ |
|---|---|---|
| Lie algebra | $\mathbb{R}^2$, abelian | $\mathbb{R}^2$, abelian |
| Unit group | $\mathbb{R}^\times\times\mathbb{R}$, two components | $\mathbb{R}^\times\times\mathbb{R}^\times$, four components |
| Exponential | bijection onto identity component | bijection onto identity component |
| Kernel of $\exp$ | $0$ | $0$ |
| Unit group $/$ scalars | $\mathbb{R}$, connected | $\mathbb{R}^\times$, two components |

The dual row is the two-dimensional row with the collapse of the quotient: the parabolic case replaces the hyperbolic two-component quotient of the split complex numbers by a single contractible line, while sharing with it the property that the exponential is a global diffeomorphism.

## Summary

The dual-number algebra $\mathbb{D}'$ is an abelian two-dimensional real Lie algebra, nilpotent of class one, with vanishing bracket. The exponential has the closed form $\exp(q + \varepsilon q') = \exp(q)(1 + \varepsilon q')$ and is a group homomorphism from $(\mathbb{D}',+)$ to the unit group. The unit group is $(\mathbb{D}')^\times \cong \mathbb{R}^\times \times \mathbb{R}$: a two-dimensional abelian Lie group with two contractible components, and the exponential is a diffeomorphism from the Lie algebra onto the identity component $\{q > 0\}$, with trivial kernel. The parabolic one-parameter subgroup $G = 1 + \mathrm{M} = \{1 + s\varepsilon\}$ is isomorphic to the additive line $(\mathbb{R},+)$, is the image of the exponential of the maximal ideal, and consists of unipotent elements; the quotient of the unit group by the central scalars is $(\mathbb{D}')^\times/\mathbb{R}^\times \cong 1 + \mathrm{M} \cong \mathbb{R}$. The comparison with the split complex case shows the same exponential behaviour but a two-component quotient $\mathbb{R}^\times$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $Q = q + \varepsilon q'$ | General dual number |
| $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$ | Real and infinitesimal parts |
| $[Q_1,Q_2] = Q_1Q_2 - Q_2Q_1$ | Lie bracket, identically zero |
| $\mathrm{G} = \mathbb{D}'$ | Abelian Lie algebra of the dual numbers |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal, the nilpotent direction |
| $\exp(q + \varepsilon q') = \exp(q)(1 + \varepsilon q')$ | Exponential |
| $(\mathbb{D}')^\times = \{q \neq 0\}$ | Group of units |
| $G = 1 + \mathrm{M}$ | Parabolic one-parameter subgroup $\cong (\mathbb{R},+)$ |
| $(\mathbb{D}')^\times/\mathbb{R}^\times \cong \mathbb{R}$ | Unit group modulo scaling |
| $\partial_\varepsilon$ | Derivation generator, $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$ |

## Further Reading

- Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen* (Teubner, Leipzig, 1888–1893), for one-parameter groups, their infinitesimal generators, and the exponential map.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, New York, 1978), for the exponential map of a Lie group and the structure of abelian and nilpotent Lie groups.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Graduate Texts in Mathematics 222, Springer, New York, 2nd ed. 2015), for the matrix exponential, its kernel, and its surjectivity on matrix groups.
- Erdal Inönü and Eugene P. Wigner, "On the contraction of groups and their representations", *Proceedings of the National Academy of Sciences of the USA* **39** (1953) 510–524, for the contraction of the elliptic and hyperbolic groups to the parabolic one-parameter group.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, London, 2012), for the parabolic one-parameter subgroup and its unipotent structure.
