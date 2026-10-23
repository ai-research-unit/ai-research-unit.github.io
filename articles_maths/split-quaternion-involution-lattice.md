
# __Split-Quaternion Involution Lattice__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ carries three involutions — the conjugation ${}^{\natural}$, the principal involution $\alpha$ and the reversal $\rho$ — and the companion article *Split-Quaternion Subspaces and the Involutions* treats them one at a time. This article treats them as a **group**: it computes the group they generate, its composition table, the way the group acts on the algebra, the lattice of fixed spaces it produces, and the orbits and stabilisers of that action. It closes with the comparison to the involution lattice of $\mathbb{B}$.

The group is the Klein four-group, and the lattice of fixed spaces is a three-element refinement of the coordinate-block decomposition of *Split-Quaternion Relations Between Subspaces*. The article is self-contained in its algebra but relies on the individual articles for the definitions of the subspaces.

$$
\alpha : (\vec e_x, \vec e_y, \vec e_z) \mapsto (-\vec e_x, -\vec e_y, \vec e_z), \qquad \rho : (\vec e_x, \vec e_y, \vec e_z) \mapsto (\vec e_x, \vec e_y, -\vec e_z).
$$

The scalar and vector subspaces and the split-complex planes are $S, V, \mathbb{D}_2, \mathbb{D}_3$ of *Split-Quaternion Relations Between Subspaces*. All three involutions fix $\mathbb{R}$ pointwise and are $\mathbb{R}$-linear.

## The Three Involutions

Each involution is a linear map $T : \mathbb{H}_{\mathrm{s}} \to \mathbb{H}_{\mathrm{s}}$ with $T^2 = \operatorname{id}$, and each has a definite relationship to the product.

| involution | definition on generators | type |
|---|---|---|
| conjugation ${}^{\natural}$ | $\vec e_k \mapsto -\vec e_k$ | anti-automorphism |
| principal $\alpha$ | $\vec e_x,\vec e_y \mapsto -\vec e_x,-\vec e_y$; $\vec e_z \mapsto \vec e_z$ | automorphism |
| reversal $\rho$ | $\vec e_x,\vec e_y \mapsto \vec e_x,\vec e_y$; $\vec e_z \mapsto -\vec e_z$ | anti-automorphism |

### (Anti)linearity

All three are $\mathbb{R}$-linear and fix the real scalars; none is $\mathbb{C}$-linear, because $\mathbb{H}_{\mathrm{s}}$ is an $\mathbb{R}$-algebra with no central imaginary unit to be conjugated. In the language of involutions of an algebra, ${}^{\natural}$ is a **conjugation** (an anti-automorphism of order two with fixed field $\mathbb{R}$, here the full scalar line since the centre is $\mathbb{R}$), whereas $\alpha$ is a **grade-type automorphism** and $\rho$ is the **reversal** or **principal anti-automorphism**.

### (Anti)automorphism properties

**Proposition.** For all $\tilde q_1, \tilde q_2 \in \mathbb{H}_{\mathrm{s}}$,

$$
\alpha(\tilde q_1 \tilde q_2) = \alpha(\tilde q_1)\alpha(\tilde q_2), \qquad \rho(\tilde q_1 \tilde q_2) = \rho(\tilde q_2)\rho(\tilde q_1), \qquad (\tilde q_1 \tilde q_2)^{\natural} = \tilde q_2^{\natural}\,\tilde q_1^{\natural}.
$$

**Proof.** It suffices to check the generators, using $\vec e_z = \vec e_x \vec e_y$. For $\alpha$: $\alpha(\vec e_x)\alpha(\vec e_y) = (-\vec e_x)(-\vec e_y) = \vec e_x \vec e_y = \vec e_z = \alpha(\vec e_z)$, and the squares are preserved. For $\rho$: $\rho(\vec e_y)\rho(\vec e_x) = \vec e_y \vec e_x = -\vec e_z = \rho(\vec e_z)$. For the conjugation: $\vec e_y^{\natural}\vec e_x^{\natural} = (-\vec e_y)(-\vec e_x) = \vec e_y \vec e_x = -\vec e_z = \vec e_z^{\natural}$.

## The Group They Generate

### Two Composition Rules

The three involutions satisfy

$$
\boxed{\;
{}^{\natural} = \alpha \circ \rho = \rho \circ \alpha
\;},
$$

so that any two of them determine the third. Equivalent forms are ${}^{\natural}\,\alpha = \alpha\,{}^{\natural} = \rho$ and ${}^{\natural}\,\rho = \rho\,{}^{\natural} = \alpha$. In particular $\alpha$ and $\rho$ commute, every product of two distinct involutions is the third, and every square is the identity.

**Theorem.** The set $G = \{\operatorname{id}, \alpha, \rho, {}^{\natural}\}$ is closed under composition and is a group, isomorphic to the **Klein four-group** $\mathbb{Z}/2 \times \mathbb{Z}/2$. Every non-identity element is an involution.

**Proof.** Closure follows from the rules above: the product of two distinct involutions is the third, and the square of each is the identity; the identity is included. Associativity is inherited from the composition of functions. Hence $G$ is a group of order $4$ in which every element has order $2$, which is $\mathbb{Z}/2 \times \mathbb{Z}/2$.

### Composition Table

The composition $g \circ h$ of the rows on the columns is

| $\circ$ | $\operatorname{id}$ | ${}^{\natural}$ | $\alpha$ | $\rho$ |
|---|---|---|---|---|
| $\operatorname{id}$ | $\operatorname{id}$ | ${}^{\natural}$ | $\alpha$ | $\rho$ |
| ${}^{\natural}$ | ${}^{\natural}$ | $\operatorname{id}$ | $\rho$ | $\alpha$ |
| $\alpha$ | $\alpha$ | $\rho$ | $\operatorname{id}$ | ${}^{\natural}$ |
| $\rho$ | $\rho$ | $\alpha$ | ${}^{\natural}$ | $\operatorname{id}$ |

The table is symmetric, which is the commutativity of $G$; the off-diagonal entries $2 \times 2$ blocks exhibit the rule that the product of two distinct involutions is the third. Note that ${}^{\natural}$ is the product $\alpha\rho$, so the group is generated by the two algebra maps $\alpha$ and $\rho$, and ${}^{\natural}$ is not an independent generator.

### Permutation of the Involutions

Since $G$ is abelian, conjugation inside $G$ fixes each element, so the three involutions are permuted trivially by the group itself. The full automorphism group $\operatorname{Aut}(G) \cong S_3$ acts on the set $\{{}^{\natural}, \alpha, \rho\}$ by the six permutations of the three elements, but only the identity permutation is induced by conjugation within $G$; the other permutations arise, when they do, from conjugation by a unit of the algebra, that is from the inner automorphism group $\operatorname{Isom}^{+}$, and the outer automorphisms of the algebra $M_2(\mathbb{R})$ are not realised as such. The relevant structure here is therefore the fixed-space lattice of $G$ and not a nontrivial action on $G$.

## The Lattice of Fixed Spaces

### Fixed and Anti-Fixed Spaces

For an involution $T$ the algebra splits as $\operatorname{Fix}(T) \oplus \operatorname{Anti}(T)$, where $\operatorname{Fix}(T)$ is the $+1$ eigenspace and $\operatorname{Anti}(T)$ the $-1$ eigenspace. For the three involutions,

| $T$ | $\operatorname{Fix}(T)$ | $\dim$ | $\operatorname{Anti}(T)$ | $\dim$ |
|---|---|---|---|---|
| ${}^{\natural}$ | $S = \operatorname{span}\{1\}$ | $1$ | $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | $3$ |
| $\alpha$ | $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$ | $2$ | $\operatorname{span}\{\vec e_x,\vec e_y\}$ | $2$ |
| $\rho$ | $\operatorname{span}\{1,\vec e_x,\vec e_y\}$ | $3$ | $\mathbb{R} \vec e_z$ | $1$ |

### The Eigenspace Lattice

Because $G$ is abelian, every element of $G$ preserves the eigenspaces of every other element, so the eigenspaces are nested with respect to the common decomposition and form a lattice under inclusion:

$$
\boxed{\;
\{0\} \;\subset\; S \;\subset\; \operatorname{span}\{\vec e_x,\vec e_y\} \;\subset\; \operatorname{span}\{1,\vec e_x,\vec e_y\} \;\subset\; \mathbb{H}_{\mathrm{s}}
\;},
$$

the eigenspaces of dimension $2$ being the two $\pm1$ eigenspaces of the single involution $\alpha$, namely $\mathbb{D}_3$ and $\operatorname{span}\{\vec e_x,\vec e_y\}$, and the eigenspaces of dimension $3$ being $V$ and $\operatorname{span}\{1,\vec e_x,\vec e_y\}$. The eigenspaces of the three involutions, their intersections and their common refinement, in terms of the coordinate blocks $\langle 1\rangle, \langle \vec e_x\rangle, \langle \vec e_y\rangle, \langle \vec e_z\rangle$ of *Split-Quaternion Relations Between Subspaces*, are:

| subspace | blocks | dimension | eigenspace of |
|---|---|---|---|
| $\{0\}$ | — | $0$ | — |
| $S$ | $\langle 1\rangle$ | $1$ | $+1$ for ${}^{\natural}, \alpha, \rho$ |
| $\mathbb{R} \vec e_z$ | $\langle \vec e_z\rangle$ | $1$ | $-1$ for ${}^{\natural}, \rho$; $+1$ for $\alpha$ |
| $\mathbb{R} \vec e_x$ | $\langle \vec e_x\rangle$ | $1$ | $-1$ for ${}^{\natural}, \alpha$; $+1$ for $\rho$ |
| $\mathbb{R} \vec e_y$ | $\langle \vec e_y\rangle$ | $1$ | $-1$ for ${}^{\natural}, \alpha$; $+1$ for $\rho$ |
| $\mathbb{D}_3$ | $\langle 1\rangle\oplus\langle \vec e_z\rangle$ | $2$ | $+1$ for $\alpha$ |
| $\operatorname{span}\{\vec e_x,\vec e_y\}$ | $\langle \vec e_x\rangle\oplus\langle \vec e_y\rangle$ | $2$ | $-1$ for ${}^{\natural}, \alpha$; $+1$ for $\rho$ |
| $\operatorname{span}\{1,\vec e_x,\vec e_y\}$ | $\langle 1\rangle\oplus\langle \vec e_x\rangle\oplus\langle \vec e_y\rangle$ | $3$ | $+1$ for $\rho$ |
| $V$ | $\langle \vec e_x\rangle\oplus\langle \vec e_y\rangle\oplus\langle \vec e_z\rangle$ | $3$ | $-1$ for ${}^{\natural}$ |
| $\mathbb{H}_{\mathrm{s}}$ | all four | $4$ | — |

The lattice is the refinement of the coordinate-block decomposition by the eigenspace data of the three involutions. The subspaces listed are the eigenspaces of the involutions, their intersections and their common refinement; the wider family of subspaces fixed by $G$ as a **set** is larger, since $\alpha$ acts as $-1$ on $\operatorname{span}\{\vec e_x,\vec e_y\}$ and a sign change fixes every line of that plane, so that every line of $\operatorname{span}\{\vec e_x,\vec e_y\}$ is also $G$-invariant. Within the eigenspace lattice a subspace is fixed pointwise by some nonzero element of $G$ exactly when its blocks all carry the same sign under that element.

## The Orbits and the Orbit–Stabiliser Count

The group $G$ acts on $\mathbb{H}_{\mathrm{s}}$ by the four sign patterns tabulated above, and the orbit–stabiliser theorem reads $|G| = |\operatorname{Orb}(\tilde q)| \cdot |\operatorname{Stab}(\tilde q)|$ with $|G| = 4$.

**Theorem.** The orbit of a general element consists of the four elements

$$
\boxed{\;
\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \quad \tilde{q}^{\natural}, \quad \alpha(\tilde q), \quad \rho(\tilde q)
\;},
$$

with $\tilde q$ repeated exactly when $G$ does not act freely at $\tilde q$. The possible orbit sizes and stabilisers are:

| orbit size | stabiliser | condition on $\tilde q$ |
|---|---|---|
| $4$ | $\{\operatorname{id}\}$ | $(q_x,q_y) \neq (0,0)$ and $q_z \neq 0$ |
| $2$ | $\{\operatorname{id}, \rho\}$ | $q_z = 0$, $(q_x,q_y) \neq (0,0)$ |
| $2$ | $\{\operatorname{id}, \alpha\}$ | $q_x = q_y = 0$, $q_z \neq 0$ |
| $1$ | $G$ | $q_x = q_y = q_z = 0$, i.e. $\tilde q \in S$ |

**Proof.** For generic $\tilde q$ with $q_x,q_y,q_z \neq 0$, the four images are distinct, so $|\operatorname{Orb}(\tilde q)| = 4$ and the stabiliser is trivial. If $q_z = 0$ but $(q_x,q_y) \neq (0,0)$, the images of $\tilde q$ and $\rho(\tilde q)$ coincide, since $\rho$ fixes $\vec e_x$ and $\vec e_y$, and $\tilde{q}^{\natural}, \alpha(\tilde q)$ coincide for the same reason; the orbit has size $2$ and the stabiliser is $\{\operatorname{id},\rho\}$. If $q_x = q_y = 0$ and $q_z \neq 0$, then $\alpha$ fixes $\tilde q$ while ${}^{\natural}$ and $\rho$ coincide, giving size $2$ and stabiliser $\{\operatorname{id},\alpha\}$. If $\tilde q \in S$ then every element of $G$ fixes $\tilde q$, giving the singleton orbit and stabiliser $G$.

The count is exact because $G$ acts in the $(q_x,q_y,q_z)$-coordinates through the subgroup

$$
H = \{\, (0,0,0),\, (1,1,1),\, (1,1,0),\, (0,0,1) \,\} \subset (\mathbb{Z}/2)^3,
$$

of order $4$, where $1$ means a sign flip; equivalently ${}^{\natural}, \alpha, \rho$ flip the sign patterns $(q_x,q_y,q_z)$, $(q_x,q_y)$, $(q_z)$. The orbit of $(q_x,q_y,q_z)$ has size $|H| / |\operatorname{Stab}|$, and the stabiliser is the subgroup of $H$ generated by the sign flips of the vanishing coordinates of $(q_x,q_y,q_z)$, which is the content of the table.

## The Reduction of the Labelled Spaces

Each of the four blocks and each of the distinguished subspaces carries a **triple sign pattern** $({}^{\natural}, \alpha, \rho)$:

| space | ${}^{\natural}$ | $\alpha$ | $\rho$ |
|---|---|---|---|
| $\langle 1\rangle$ | $+$ | $+$ | $+$ |
| $\langle \vec e_x\rangle$ | $-$ | $-$ | $+$ |
| $\langle \vec e_y\rangle$ | $-$ | $-$ | $+$ |
| $\langle \vec e_z\rangle$ | $-$ | $+$ | $-$ |
| $S$ | $+$ | $+$ | $+$ |
| $\mathbb{R} \vec e_z$ | $-$ | $+$ | $-$ |
| $\operatorname{span}\{\vec e_x,\vec e_y\}$ | $-$ | $-$ | $+$ |
| $\mathbb{D}_3$ | mixed on $\{1,\vec e_z\}$ | $+$ | mixed |
| $V$ | $-$ | mixed on $\{\vec e_x,\vec e_y,\vec e_z\}$ | mixed |

The two lines $\langle \vec e_x\rangle$ and $\langle \vec e_y\rangle$ carry the same triple pattern and are therefore not separated by $G$; this is the lattice-theoretic reason for the unsplittable plane of *Split-Quaternion Subspaces and the Involutions*. Only the line $\langle \vec e_z\rangle$ carries a distinct pattern, $(-,+,-)$.

## The Relation to the Involution Lattice of $\mathbb{B}$

The biquaternion article *The Group of Involutions* treats four involutions — the conjugation ${}^{\natural}$, the complex conjugation $\bar{\cdot}$, the Hermitian conjugation ${}^{*} = \bar{\cdot}{}^{\natural}$ and the anti-Hermitian one $\flat = -{}^{*}$ — which generate a larger group, and *Comparison of the Remarkable Subspaces* treats the richer lattice they produce, because $\mathbb{B}$ has eight real coordinates and four involutions. The split-quaternion lattice differs in two structural ways. First, three involutions generate the Klein four-group, so the composition table is the simplest of all nontrivial groups and the whole group is determined by any two of the involutions. Second, the eigenspace lattice has a **maximum chain** of length four, $\{0\} \subset S \subset \operatorname{span}\{\vec e_x,\vec e_y\} \subset \operatorname{span}\{1,\vec e_x,\vec e_y\} \subset \mathbb{H}_{\mathrm{s}}$, and the vector subspace $V$ lies outside it; the lattice has two incomparable three-dimensional elements $V$ and $\operatorname{span}\{1,\vec e_x,\vec e_y\}$ rather than a single maximal proper subspace as a chain would give. Nothing biquaternion-specific — the two commuting complex structures, the Hermitian pairing — is invoked here.

## Examples

**Example (an element of each orbit size).** The element $\tilde q = 5 + 2\vec e_x + 3\vec e_y + 4\vec e_z$ has orbit size $4$ with trivial stabiliser; the element $\tilde q = 5 + 2\vec e_x + 3\vec e_y$ has orbit $\{\tilde q, \tilde{q}^{\natural}\}$ of size $2$ with stabiliser $\{\operatorname{id},\rho\}$; the element $\tilde q = 5 + 4\vec e_z$ has orbit size $2$ with stabiliser $\{\operatorname{id},\alpha\}$; and the scalar $\tilde q = 5$ has orbit size $1$ with stabiliser $G$.

**Example (the stabiliser of a vector).** For $\vec e_z$ the images are $\vec e_z^{\natural} = -\vec e_z$, $\alpha(\vec e_z) = \vec e_z$, $\rho(\vec e_z) = -\vec e_z$, so the orbit is $\{\vec e_z, -\vec e_z\}$ of size $2$ and the stabiliser is $\{\operatorname{id}, \alpha\}$. For the vector $\vec e_x + \vec e_y$ the images are ${}^{\natural}(\vec e_x+\vec e_y) = -\vec e_x-\vec e_y$, $\alpha(\vec e_x+\vec e_y) = -\vec e_x-\vec e_y$, $\rho(\vec e_x+\vec e_y) = \vec e_x+\vec e_y$, so the stabiliser is $\{\operatorname{id}, \rho\}$. The vector $\vec e_x + \vec e_z$, by contrast, has the four images $\vec e_x+\vec e_z$, $-\vec e_x-\vec e_z$, $-\vec e_x+\vec e_z$, $\vec e_x-\vec e_z$, all distinct, so its stabiliser is trivial.

**Example (an element with mixed pattern).** For $\tilde q = 2 + \vec e_x + \vec e_z$, the images are $\tilde{q}^{\natural} = 2 - \vec e_x - \vec e_z$, $\alpha(\tilde q) = 2 - \vec e_x + \vec e_z$, $\rho(\tilde q) = 2 + \vec e_x - \vec e_z$, all distinct, so the orbit has size $4$ and the stabiliser is trivial; the sign pattern of $\tilde q$ itself is not a single triple because $\tilde q$ is a mixed element, only its coordinates carry triples.

**Example (composition verified on an element).** For $\tilde q = 1 + \vec e_y$: $\alpha(\rho(\tilde q)) = \alpha(1 - \vec e_y) = 1 - \vec e_y = \tilde{q}^{\natural}$, and $\rho(\alpha(\tilde q)) = \rho(1 - \vec e_y) = 1 - \vec e_y = \tilde{q}^{\natural}$, confirming ${}^{\natural} = \alpha\rho = \rho\alpha$.

## Summary

The split-quaternion algebra carries three $\mathbb{R}$-linear involutions — the conjugation ${}^{\natural}$ (an anti-automorphism), the principal involution $\alpha$ (an automorphism) and the reversal $\rho$ (an anti-automorphism) — related by ${}^{\natural} = \alpha\rho = \rho\alpha$. Together they form the Klein four-group $G \cong \mathbb{Z}/2\times\mathbb{Z}/2$, whose composition table is the one above; ${}^{\natural}$ is the product of the other two, so $\alpha$ and $\rho$ generate.

The fixed spaces of the three involutions are $S = \operatorname{span}\{1\}$, $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$ and $\operatorname{span}\{1,\vec e_x,\vec e_y\}$, with anti-fixed spaces $V$, $\operatorname{span}\{\vec e_x,\vec e_y\}$ and $\mathbb{R} \vec e_z$. The lattice of eigenspaces is the coordinate-block decomposition refined by the sign data, with the maximum chain $\{0\} \subset S \subset \operatorname{span}\{\vec e_x,\vec e_y\} \subset \operatorname{span}\{1,\vec e_x,\vec e_y\} \subset \mathbb{H}_{\mathrm{s}}$. The group acts on the algebra by four sign patterns; the orbit–stabiliser theorem gives orbit sizes $1, 2$ or $4$ with the stabilisers tabulated, the generic orbit having size $4$ and trivial stabiliser and the scalar orbit being a fixed point. The lines $\langle \vec e_x\rangle$ and $\langle \vec e_y\rangle$ carry the same triple sign pattern and are not separated by the involution group. This lattice is the split-quaternion analogue of the biquaternion involution lattice, with three involutions in place of four and a Klein four-group in place of the larger group.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| ${}^{\natural}, \alpha, \rho$ | conjugation, principal involution, reversal | *Split-Quaternion Subspaces and the Involutions* |
| $G = \{\operatorname{id},\alpha,\rho,{}^{\natural}\}$ | the Klein four-group generated by the involutions | this article |
| $\operatorname{Fix}(T)$, $\operatorname{Anti}(T)$ | the $+1$ and $-1$ eigenspaces of an involution $T$ | this article |
| $S, V, \mathbb{D}_2, \mathbb{D}_3$ | the distinguished subspaces | *Split-Quaternion Relations Between Subspaces* |
| $\langle 1\rangle,\langle \vec e_x\rangle,\langle \vec e_y\rangle,\langle \vec e_z\rangle$ | the four coordinate blocks | *Split-Quaternion Relations Between Subspaces* |
| $({}^{\natural},\alpha,\rho)$, $(-,+,-)$ … | triple sign patterns | this article |
| $\operatorname{Orb}(\tilde q)$, $\operatorname{Stab}(\tilde q)$ | orbit and stabiliser under $G$ | this article |
| $\operatorname{Aut}(G) \cong S_3$ | the automorphisms of the Klein four-group | this article |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the general theory of involutions, their groups and their fixed fields.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the involution group generated by the conjugation, reversal and grade involutions of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the composition rules of the involutions of the low-dimensional Clifford algebras and the lattice of their fixed spaces.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the involutions of the coquaternions and their fixed subspaces.
