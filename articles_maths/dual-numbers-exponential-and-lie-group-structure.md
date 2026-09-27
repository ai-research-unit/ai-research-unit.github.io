
# __Dual-Numbers Exponential and Lie Group Structure__

## Introduction

This article develops the Lie theory of the dual-number algebra: the Lie algebra structure on $\mathbb{D}'$ itself, the exponential map, the group of units as a Lie group, the parabolic one-parameter subgroup, and the quotient of the unit group by the scalars. It follows *Dual-Numbers Algebra* for the algebra and its abelian Lie bracket, *Dual-Numbers Norm and Invertibility* for the unit group, *Dual-Numbers Automorphisms and Derivations* for the derivation algebra, and *Shears and Parabolic Rotations* for the shear. The structural model is *Biquaternion Lie Algebra and Lie Group Structure*, where the unit group is $GL_2(\mathbb{C})$; here it is the much smaller group $\mathbb{R}^\times \times \mathbb{R}$.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the exponential is a formal series when $R$ is a commutative $\mathbb{Q}$-algebra and an analytic series over the geometric specialisation $R = \mathbb{R}$, and then the algebra is written $\mathbb{D}'$. A general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in R,
$$

with $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$, norm form $N(Z) = a^2$, maximal ideal $\mathfrak{m} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$, and unit group $(\mathbb{D}')^\times = \{a \neq 0\}$.

## The Lie Algebra Structure

### The Lie Bracket

**Definition.** The **Lie bracket** on $\mathbb{D}'_R$ is the commutator

$$
[Z, W] = ZW - WZ.
$$

**Theorem.** $\mathbb{D}'_R$ is a **commutative** algebra, so its Lie bracket vanishes identically:

$$
[Z, W] = 0 \qquad \text{for all } Z, W \in \mathbb{D}'_R.
$$

Hence the Lie algebra $\mathfrak{g} = \mathbb{D}'_R$ is **abelian**.

**Proof.** $ZW = WZ$ for all $Z, W$ because multiplication of dual numbers is commutative. $\square$

### Nilpotence

**Definition.** A Lie algebra $\mathfrak{g}$ is **nilpotent of class $c$** if the descending central series $\mathfrak{g}^1 = \mathfrak{g}$, $\mathfrak{g}^{k+1} = [\mathfrak{g}, \mathfrak{g}^k]$ reaches $0$ at step $c + 1$, and $\mathfrak{g}$ is **abelian** when $[\mathfrak{g}, \mathfrak{g}] = 0$.

**Proposition.** $\mathfrak{g} = \mathbb{D}'_R$ is a nilpotent Lie algebra of class $1$; equivalently, its derived subalgebra is zero, $[\mathfrak{g}, \mathfrak{g}] = 0$.

**Proof.** The derived subalgebra is spanned by brackets $[Z,W]$, all of which vanish; the series is $\mathfrak{g} \supset 0$. $\square$

So the dual-number Lie algebra is the abelian two-dimensional real Lie algebra, the simplest nilpotent example. Its enveloping algebra is the polynomial algebra on two commuting generators, and its only Lie structure is the underlying vector space.

### The Lie Algebra of a Commutative Associative Algebra

**Remark.** For any associative algebra $A$ the commutator makes $A$ a Lie algebra, and the Jacobi identity is a consequence of associativity. When $A$ is commutative the bracket vanishes, so the Lie algebra records no more than the $R$-module structure. The interesting Lie theory of $\mathbb{D}'$ therefore lives not in $\mathbb{D}'$ itself but in its derivation algebra $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$ and in the Lie group structure of the unit group, which are treated below.

## The Exponential

### Definition and Convergence

**Definition.** Let $R$ be a commutative $\mathbb{Q}$-algebra, so that $k!$ is invertible for every $k$. The **exponential** of $Z \in \mathbb{D}'_R$ is the formal series

$$
\exp(Z) = \sum_{k \geq 0} \frac{Z^k}{k!}.
$$

Over $R = \mathbb{R}$ the series converges for every $Z$, in the topology of $\mathbb{D}' \cong \mathbb{R}^2$.

### Closed Form

**Theorem.** For every $Z = a + \varepsilon b$,

$$
\exp(a + \varepsilon b) = e^{a}\bigl(1 + \varepsilon b\bigr) = e^{a} + e^{a}\varepsilon b.
$$

**Proof.** By the binomial expansion and $\varepsilon^2 = 0$, $(a + \varepsilon b)^k = a^k + k a^{k-1}\varepsilon b$ for $k \geq 1$. Summing,

$$
\exp(a + \varepsilon b) = \sum_{k \geq 0}\frac{a^k}{k!} + \varepsilon \sum_{k \geq 1}\frac{k a^{k-1}b}{k!} = e^{a} + \varepsilon\, b \sum_{k \geq 1}\frac{a^{k-1}}{(k-1)!} = e^{a} + e^{a}\varepsilon b,
$$

the two series being the exponential of $a$. $\square$

**Corollary.** $\exp(\varepsilon) = 1 + \varepsilon$ and $\exp(s\varepsilon) = 1 + s\varepsilon$ for every $s$; the exponential of a purely infinitesimal element is a shear.

### The Group Homomorphism Property

**Theorem.** The exponential is a homomorphism from the additive group $(\mathbb{D}'_R, +)$ to the multiplicative group $(\mathbb{D}'_R)^\times$:

$$
\exp(Z + W) = \exp(Z)\exp(W).
$$

**Proof.** The exponential is the usual exponential of the commutative associative algebra $\mathbb{D}'_R$, and for commuting $Z, W$ the identity $\exp(Z+W) = \exp(Z)\exp(W)$ follows by the binomial theorem. Alternatively, $\exp(a + \varepsilon b)\exp(c + \varepsilon d) = e^a(1 + \varepsilon b)e^c(1 + \varepsilon d) = e^{a+c}(1 + (b+d)\varepsilon) = \exp((a+c) + (b+d)\varepsilon)$, matching $Z + W$. $\square$

So $\exp$ is a homomorphism of groups, and the image is a subgroup of the unit group.

## The Group of Units

### The Lie Group

**Theorem.** The group of units

$$
(\mathbb{D}'_R)^\times = \{a + \varepsilon b : a \in R^\times\}
$$

is a group under multiplication, with $(a + \varepsilon b)^{-1} = a^{-1} - a^{-2}\varepsilon b$. Over $R = \mathbb{R}$ it is a two-dimensional abelian Lie group with the following structure:

$$
(\mathbb{D}')^\times \cong \mathbb{R}^\times \times (\mathbb{R}, +),
$$

the isomorphism being $a + \varepsilon b \leftrightarrow (a,\, b/a)$.

**Proof.** The group axioms and the inverse formula are from *Dual-Numbers Norm and Invertibility*; the isomorphism is the direct-product decomposition of *Shears and Parabolic Rotations*, where the second factor is the shear group $1 + \mathfrak{m}$. $\square$

### Connected Components

**Proposition.** Over $R = \mathbb{R}$ the unit group has exactly two connected components, $\{a > 0\}$ and $\{a < 0\}$, each contractible; the identity component is

$$
(\mathbb{D}')^\times_0 = \{a > 0\} \cong \mathbb{R}_{>0} \times \mathbb{R}.
$$

**Proof.** The sign of $a$ is a continuous surjective homomorphism $(\mathbb{D}')^\times \to \{\pm 1\}$; the two fibres are half-planes, hence connected and contractible. $\square$

### Surjectivity of the Exponential onto the Identity Component

**Theorem.** Over $R = \mathbb{R}$ the exponential

$$
\exp : \mathfrak{g} = \mathbb{D}' \longrightarrow (\mathbb{D}')^\times
$$

is injective, with image exactly the identity component $(\mathbb{D}')^\times_0 = \{a > 0\}$. It is therefore a bijection, and in fact a diffeomorphism, onto the identity component.

**Proof.** $\exp(a + \varepsilon b) = e^{a}(1 + \varepsilon b)$ has real part $e^{a} > 0$, so the image is contained in $\{a > 0\}$. Conversely, for $c + \varepsilon d$ with $c > 0$ set $a = \log c$ and $b = d/c$; then $\exp(a + \varepsilon b) = c(1 + \varepsilon d/c) = c + \varepsilon d$, so the image is $\{a > 0\}$. For injectivity, $\exp(a + \varepsilon b) = 1$ forces $e^{a} = 1$, hence $a = 0$, and then $e^{a}b = b = 0$. The map is smooth with the explicit smooth inverse $c + \varepsilon d \mapsto \log c + (d/c)\varepsilon$ on $\{c > 0\}$, so it is a diffeomorphism. $\square$

**Remark.** The kernel of the exponential is trivial. This is the sharpest contrast with the complex and matrix cases, where the exponential has a nontrivial kernel: on $\mathbb{C}$ the kernel is $2\pi i\mathbb{Z}$, and on $GL_2(\mathbb{C})$ the exponential is surjective but not injective, with kernel the matrices having eigenvalues in $2\pi i\mathbb{Z}$. Here the exponential is a global diffeomorphism from the abelian Lie algebra onto the identity component, the maximal simply connected abelian case.

## The Parabolic One-Parameter Subgroup

### Definition

**Definition.** The **parabolic one-parameter subgroup** of $(\mathbb{D}')^\times$ is

$$
G = \{1 + s\varepsilon : s \in \mathbb{R}\} = 1 + \mathfrak{m}.
$$

### Identification with the Additive Line

**Theorem.** The maps

$$
(\mathbb{R}, +) \longrightarrow G, \qquad s \longmapsto 1 + s\varepsilon, \qquad G \longrightarrow \mathfrak{m}, \qquad 1 + s\varepsilon \longmapsto s\varepsilon
$$

are inverse isomorphisms of groups, where $\mathfrak{m}$ carries the additive group structure. In particular $G \cong (\mathbb{R},+)$ is a connected, simply connected, one-dimensional abelian Lie group, and it is exactly the image of the exponential of the maximal ideal, $G = \exp(\mathfrak{m})$.

**Proof.** $(1 + s\varepsilon)(1 + t\varepsilon) = 1 + (s+t)\varepsilon$ because $\varepsilon^2 = 0$, so the first map is a homomorphism; it is bijective with the displayed inverse; and $\exp(s\varepsilon) = 1 + s\varepsilon$, so $G = \exp(\mathfrak{m})$. $\square$

### The Unipotent Character

**Proposition.** Every element of $G$ is **unipotent**: it differs from the identity by a nilpotent, $(1 + s\varepsilon) - 1 = s\varepsilon$ with $(s\varepsilon)^2 = 0$. The subgroup $G$ is the unique one-parameter subgroup of $(\mathbb{D}')^\times$ generated by a nilpotent element of the algebra, and it is the image of the algebra's own nilpotent direction.

**Proof.** $(1 + s\varepsilon) - 1 = s\varepsilon$ and $(s\varepsilon)^2 = s^2\varepsilon^2 = 0$, so the displacement from the identity is nilpotent of index two, which is the algebraic form of unipotence; in particular $1 + s\varepsilon$ has no eigenvalue different from $1$ as a linear map of the algebra. The generator is the nilpotent $\varepsilon$, whose exponential is polynomial. $\square$

## The Group of Units Modulo Scaling

### The Quotient

**Theorem.** The central scalars embed as $\mathbb{R}^\times \hookrightarrow (\mathbb{D}')^\times$, $a \mapsto a$, and

$$
(\mathbb{D}')^\times / \mathbb{R}^\times \;\cong\; 1 + \mathfrak{m} \;\cong\; (\mathbb{R}, +),
$$

the isomorphism being the class of $a + \varepsilon b$ mapped to $1 + (b/a)\varepsilon$, equivalently to the parabolic angle $s = b/a$.

**Proof.** Every unit is $a(1 + \varepsilon b/a)$, and multiplying by the scalar $a$ is exactly the quotient by the subgroup $\mathbb{R}^\times$; two units have the same class exactly when their shear parameters agree. $\square$

**Corollary.** The quotient is connected, contractible and one-dimensional; it is the space of shears, and it is the same object as the parabolic one-parameter subgroup $G$.

## Comparison with the Split Complex and Biquaternion Cases

### The Split Complex Case

For the split complex algebra $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$, the unit group is $\mathbb{D}^\times \cong \mathbb{R}^\times \times \mathbb{R}^\times$, of real dimension two and with four contractible components; the exponential from the abelian Lie algebra $\mathbb{R}^2$ is a bijection onto the identity component, exactly as in the dual case. The quotient is

$$
\mathbb{D}^\times/\mathbb{R}^\times \cong \mathbb{R}^\times,
$$

obtained by the ratio of the two idempotent components, and it has two components—unlike the connected quotient $(\mathbb{D}')^\times/\mathbb{R}^\times \cong \mathbb{R}$. The difference is the degeneracy of the norm form: the split complex form has two independent directions, so the quotient retains a hyperbola-like two-component structure, while the dual form has one, so the quotient collapses to a line.

### The Biquaternion Case

For the biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ the unit group is $GL_2(\mathbb{C})$, of real dimension eight, connected. The exponential of $\mathfrak{gl}(2,\mathbb{C})$ is surjective onto $GL_2(\mathbb{C})$ but not injective, with kernel the matrices whose eigenvalue differences lie in $2\pi i\mathbb{Z}$; the exponential is not a diffeomorphism, and there is no global logarithm. The quotient by the scalars is

$$
GL_2(\mathbb{C})/\mathbb{C}^\times = PGL(2,\mathbb{C}) = PSL(2,\mathbb{C}),
$$

the automorphism group of *Biquaternion Automorphisms and Derivations*, connected of real dimension six.

### The Table

| | $\mathbb{D}'$ | $\mathbb{D}$ | $\mathbb{B}$ |
|---|---|---|---|
| Lie algebra | $\mathbb{R}^2$, abelian | $\mathbb{R}^2$, abelian | $\mathfrak{gl}(2,\mathbb{C})$ |
| Unit group | $\mathbb{R}^\times\times\mathbb{R}$, two components | $\mathbb{R}^\times\times\mathbb{R}^\times$, four components | $GL_2(\mathbb{C})$, connected |
| Exponential | bijection onto identity component | bijection onto identity component | surjective, not injective |
| Kernel of $\exp$ | $0$ | $0$ | eigenvalue gaps in $2\pi i\mathbb{Z}$ |
| Unit group $/$ scalars | $\mathbb{R}$, connected | $\mathbb{R}^\times$, two components | $PGL(2,\mathbb{C})$, connected |

The dual row is the two-dimensional row with the collapse of the quotient: the parabolic case replaces the hyperbolic two-component quotient of the split complex numbers by a single contractible line, while sharing with it the property that the exponential is a global diffeomorphism.

## Summary

The dual-number algebra $\mathbb{D}'$ is an abelian two-dimensional real Lie algebra, nilpotent of class one, with vanishing bracket. The exponential has the closed form $\exp(a + \varepsilon b) = e^{a}(1 + \varepsilon b)$ and is a group homomorphism from $(\mathbb{D}',+)$ to the unit group. The unit group is $(\mathbb{D}')^\times \cong \mathbb{R}^\times \times \mathbb{R}$: a two-dimensional abelian Lie group with two contractible components, and the exponential is a diffeomorphism from the Lie algebra onto the identity component $\{a > 0\}$, with trivial kernel. The parabolic one-parameter subgroup $G = 1 + \mathfrak{m} = \{1 + s\varepsilon\}$ is isomorphic to the additive line $(\mathbb{R},+)$, is the image of the exponential of the maximal ideal, and consists of unipotent elements; the quotient of the unit group by the central scalars is $(\mathbb{D}')^\times/\mathbb{R}^\times \cong 1 + \mathfrak{m} \cong \mathbb{R}$. The comparison with the split complex case shows the same exponential behaviour but a two-component quotient $\mathbb{R}^\times$; the comparison with the biquaternion case shows a connected unit group $GL_2(\mathbb{C})$ on which the exponential is surjective but not injective.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $[Z,W] = ZW - WZ$ | Lie bracket, identically zero |
| $\mathfrak{g} = \mathbb{D}'$ | Abelian Lie algebra of the dual numbers |
| $\mathfrak{m} = (\varepsilon)$ | Maximal ideal, the nilpotent direction |
| $\exp(a + \varepsilon b) = e^{a}(1 + \varepsilon b)$ | Exponential |
| $(\mathbb{D}')^\times = \{a \neq 0\}$ | Group of units |
| $G = 1 + \mathfrak{m}$ | Parabolic one-parameter subgroup $\cong (\mathbb{R},+)$ |
| $(\mathbb{D}')^\times/\mathbb{R}^\times \cong \mathbb{R}$ | Unit group modulo scaling |
| $\partial_\varepsilon$ | Derivation generator, $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$ |
| $\mathbb{B} \cong M_2(\mathbb{C})$ | Biquaternion algebra, the comparison model |

## Further Reading

- Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen* (Teubner, Leipzig, 1888–1893), for one-parameter groups, their infinitesimal generators, and the exponential map.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, New York, 1978), for the exponential map of a Lie group and the structure of abelian and nilpotent Lie groups.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Graduate Texts in Mathematics 222, Springer, New York, 2nd ed. 2015), for the matrix exponential, its kernel, and its surjectivity on matrix groups.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the groups of units of the low-dimensional real algebras.
- Erdal Inönü and Eugene P. Wigner, "On the contraction of groups and their representations", *Proceedings of the National Academy of Sciences of the USA* **39** (1953) 510–524, for the contraction of the elliptic and hyperbolic groups to the parabolic one-parameter group.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, London, 2012), for the parabolic one-parameter subgroup and its unipotent structure.
