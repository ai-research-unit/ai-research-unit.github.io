
# __Triality and Spin(8)__

## Introduction

For every $n$ the vector representation of the orthogonal group and the two half-spinor representations of the spin group are three representations of three different groups, related by the covering $\mathrm{Spin}(n)\to SO(n)$. At $n=8$ the three representations are all of the same dimension, eight, and the relation among them becomes a symmetry: an automorphism of the spin group of order three permutes them. This is **triality**, the outer automorphism of $\mathrm{Spin}(8)$, and it is the one structural accident of the spin groups that is not a coincidence of Dynkin diagrams with another classical type: the diagram $D_4$ is its own mirror in three ways at once, and its automorphism group is the symmetric group on three letters.

This article describes the three eight-dimensional representations, the trilinear form that couples them, the octonionic construction in which the symmetry is visible, the fixed-point subgroup under the automorphism, and the reason the accident is confined to eight dimensions. The last point matters for the rest of the corpus: triality is the origin of many of the exceptional structures attached to the octonions, and it is the reason the octonionic plane and the exceptional groups appear where they do.

The Clifford algebra, the $k$-vectors, the volume element and reversion are from *The Clifford Algebra* and *Clifford Algebras in Finite Dimensions*; the spinor module as a minimal left ideal, the chiral splitting and the reality of the spinor module are from *Spinors as Minimal Left Ideals* and *Real Spinors and Reality Conditions*; the spinor modules, their weights and the branching rule are from *Spin Representations and Clifford Modules* and *Spin Representations of the Orthogonal Lie Algebra*; the low-dimensional table and the algebra $\mathrm{Cl}_{8,0}\cong M_{16}(\mathbb{R})$ are from *Clifford Algebras in Finite Dimensions* and *The Low-Dimensional Spin Groups and the Exceptional Isomorphisms*; the root systems, the Dynkin diagrams and their automorphisms are from *Root Systems and Classification*; the octonions and their automorphism group are from *Octonion Algebra*, *Octonion Representations* and *Octonions and the Exceptional Lie Groups*. Nothing owned by those entries is re-derived.

## The Three Representations of Dimension Eight

### The Vector and the Two Half-Spinors

**Theorem.** For $n=8$ the vector representation of $SO(8)$ is of dimension eight, and the two half-spinor modules $S^+$ and $S^-$ of $\mathrm{Spin}(8)$ are of dimension eight each:

$$
\dim 8_v=\dim 8_s=\dim 8_c=8 .
$$

**Proof.** The vector representation has dimension $n=8$ by definition, and the half-spinor modules have dimension $2^{m-1}$ for $n=2m$ with $m=4$, by *Spin Representations of the Orthogonal Lie Algebra*, that is $2^3=8$. $\square$

### Why the Coincidence Is Unique

**Theorem.** If $n=2m$ is even and $n\neq8$ then the vector representation and the two half-spinor representations have pairwise different dimensions.

**Proof.** Read the pair of dimensions $(\dim 8_v,\dim 8_s)=(2m,2^{m-1})$ off the formula. For $m=1,2,3$ the pairs are $(2,1)$, $(4,2)$ and $(6,4)$, so the three dimensions are pairwise different; for $m=4$ the pair is $(8,8)$ and all three dimensions coincide; for $m\ge5$ the half-spinor dimension exceeds the vector dimension, $2^{m-1}>2m$, which follows by induction from $2^4=16>10$. $\square$

**Remark.** The case $n=4$ deserves a word, since there the two half-spinor modules together have dimension $4$, equal to the dimension of the vector module. The coincidence is between the whole spinor module and the vector module, not among the three modules: the half-spinor modules have dimension two each. It is what underlies the accident $D_2\cong A_1\times A_1$ of *The Low-Dimensional Spin Groups and the Exceptional Isomorphisms*, and it produces a symmetry of a different kind, not a triality.

**Corollary.** The coincidence of dimensions that makes triality possible occurs for $n=8$ alone among the even dimensions.

**Proof.** Immediate from the theorem. $\square$

### The Distinct Modules Are Not Equivalent

**Theorem.** As representations of $\mathrm{Spin}(8)$ the three modules $8_v$, $8_s$ and $8_c$ are pairwise non-isomorphic; they are permuted by an automorphism of the group.

**Proof.** The vector module is not isomorphic to either half-spinor module because the centre $\{\pm1\}$ of the spin group acts trivially on the vector module, the vector module being a representation of the quotient $SO(8)$, and by $-1$ on the half-spinor modules, as in *Spin Representations of the Orthogonal Lie Algebra*. The two half-spinor modules are not isomorphic to each other because the volume element acts on them with the two opposite eigenvalues. That an automorphism of the group permutes them is the theorem of the next section. $\square$

## The Trilinear Form

**Theorem.** There is a nonzero trilinear form, invariant under $\mathrm{Spin}(8)$,

$$
\Phi:8_v\otimes 8_s\otimes 8_c\longrightarrow\mathbb{R},
$$

and it is unique up to a nonzero scalar; in the Clifford algebra it is given by

$$
\Phi(v,\psi,\phi)=\langle\,\gamma(v)\psi,\phi\,\rangle
$$

for the pairing $\langle\cdot,\cdot\rangle$ of the spinor module with its dual, with the identifications of the three modules with their duals that the invariant forms provide.

**Proof.** For an invariant trilinear form it suffices to give an invariant map $8_v\otimes8_s\to 8_c$, and the composition of the Clifford action with the invariant pairing is such a map: the Clifford action is $\mathrm{Spin}(8)$-equivariant, and the pairing is invariant. Uniqueness is Schur's lemma: the module $8_c$ occurs in $8_v\otimes8_s$ with multiplicity one, so the space of invariant maps is one-dimensional, and the map displayed is nonzero. $\square$

**Corollary.** The trilinear form is symmetric under the simultaneous permutation of the three modules, and the three modules can be interchanged without altering it.

**Proof.** The symmetry is a statement about the permutation of the three factors; in the octonionic model below it becomes the symmetry of the real part of a product of three octonions, which is preserved by cyclic permutation. $\square$

**Remark.** The trilinear form is the invariant that couples a vector to the two half-spinors, and it is the reason the three representations are spoken of as a triple rather than as three separate modules. It is the analogue, at the level of the three representations, of the bilinear pairing of a module with its dual, and it exists precisely because the three modules have the same dimension.

## The Triality Automorphism

### The Statement

**Theorem (triality).** There is an outer automorphism

$$
\tau:\mathrm{Spin}(8)\longrightarrow\mathrm{Spin}(8),\qquad \tau^3=1,
$$

whose induced permutation of the three eight-dimensional representations is a three-cycle, and the group of outer automorphisms of $\mathrm{Spin}(8)$, and of its Lie algebra $\mathfrak{so}(8)$, is the symmetric group $S_3$:

$$
\mathrm{Out}(\mathrm{Spin}(8))\cong S_3,\qquad \mathrm{Out}(\mathfrak{so}(8,\mathbb{C}))\cong S_3 .
$$

**Proof.** The automorphisms of a Dynkin diagram are the permutations of the nodes that preserve it, so the outer automorphism group of a simple Lie algebra is the automorphism group of its diagram, by *Root Systems and Classification*; the diagram $D_4$ has a central node joined to three end nodes, whose automorphism group is $S_3$, and the corresponding statement for the group holds because the outer automorphisms of the group and of the algebra agree for a simply connected semisimple group. The three-cycle is the cycle of the three end nodes, and the three eight-dimensional representations correspond to the three nodes. $\square$

### The Fixed-Point Subgroup

**Theorem.** The fixed-point subgroup of the triality automorphism of order three is the exceptional group $G_2$:

$$
\mathrm{Spin}(8)^{\tau}\cong G_2 ,
$$

of dimension $14$, and it is the automorphism group of the octonions.

**Proof.** The fixed-point subgroup of a diagram automorphism is the group whose diagram is obtained by folding the diagram along the automorphism; the folding of $D_4$ along the three-cycle glues the three end nodes into one and leaves the central node, producing the diagram of $G_2$. The identification with the automorphism group of the octonions is in *Octonions and the Exceptional Lie Groups*. $\square$

**Corollary.** The group $G_2$ lies in $\mathrm{Spin}(7)$, which lies in $\mathrm{Spin}(8)$, so the chain of the octonionic geometry runs
$$
\mathrm{Spin}(8)\supset\mathrm{Spin}(7)\supset G_2,\qquad \mathrm{Spin}(7)/G_2=S^7,
$$
$\mathrm{Spin}(7)$ being the isotropy in $\mathrm{Spin}(8)$ of a nonzero spinor and $G_2$ the isotropy in $\mathrm{Spin}(7)$ of a unit octonion; the isotropy in $G_2$ of a unit imaginary octonion is $SU(3)$.

**Proof.** The dimensions $28>21>14$ already forbid the reversed order. $G_2$ fixes the real unit $1$ of the octonions and acts faithfully on the imaginary part, so it lies in $SO(7)$; it is simply connected, hence it lifts to $\mathrm{Spin}(7)\subseteq\mathrm{Spin}(8)$. The transitivity of $\mathrm{Spin}(7)$ on the unit sphere of the octonions with stabiliser $G_2$, and the stabiliser $SU(3)$ of a unit imaginary octonion in $G_2$, are the classical statements of *Octonion Geometry* and *Octonions and the Exceptional Lie Groups*; the isotropy of a nonzero spinor in $\mathrm{Spin}(8)$ is $\mathrm{Spin}(7)$, which is the spinor description of the same subgroup. $\square$

## The Octonionic Model

### The Three Products

**Theorem (the octonionic model of triality, quoted).** Let $\mathbb{O}$ be the octonions with conjugation $x\mapsto\bar x$ and inner product $\langle x,y\rangle=\mathrm{Re}(x\bar y)$. Then the trilinear form of triality is the real part of a product of three octonions,

$$
\Phi(x,y,z)=\langle xy,z\rangle=\mathrm{Re}\bigl((xy)\bar z\bigr),
$$

which is invariant under cyclic permutation of its three arguments; and the three legs of the form are the three products

$$
m_1(x,y)=xy,\qquad m_2(x,y)=\bar xy,\qquad m_3(x,y)=x\bar y,
$$

which are carried into one another by conjugating one of the two arguments.

**Proof.** The symmetry of $\mathrm{Re}\bigl((xy)z\bigr)$ under cyclic permutation is the classical identity of a composition algebra, and it follows from the alternative laws recorded in *Octonion Algebra*; the identification of the three legs with the three products, and the realisation of $8_v$ and of the two half-spinor modules on the octonions through them, is the classical octonionic construction of triality, recorded in the literature cited below. The Clifford-algebraic part of the statement is the theorem of the previous section. $\square$

**Remark (the boundary of what this article proves).** The article proves the Clifford-algebraic content: the three modules, their equal dimension, their non-isomorphism, the invariant trilinear form and the automorphism. The realisation of the three modules on the octonions, and the identification of the isotropy of the model with $\mathrm{Spin}(8)$ acting through the three legs, is quoted from the literature and developed in *Octonion Representations*, *Octonion Geometry* and *Octonions and Exceptional Geometry*, where the planes, the lines and the exceptional groups of the octonionic projective plane are treated.

### Alternativity Without Associativity

**Theorem.** The octonion product $m_1(x,y)=xy$ is alternative and not associative:

$$
(xx)y=x(xy),\qquad (xy)y=x(yy),\qquad (xy)z\neq x(yz)\ \text{in general}.
$$

The other two legs satisfy $m_2(x,y)=m_1(\bar x,y)$ and $m_3(x,y)=m_1(x,\bar y)$, each being obtained from the octonion product by conjugating an argument, and the alternative identities written for $m_1$ do not hold for them: for a unit imaginary $x$ one has $m_2(x,m_2(x,y))=-y$ against $m_2(m_2(x,x),y)=y$, and similarly for $m_3$.

**Proof.** The alternative laws are the defining identities of the octonions and the failure of associativity is their complement, both recorded in *Octonion Algebra*; the two relations between the legs are the definition of $m_2$ and $m_3$. For the failure, take $x$ unit imaginary, so that $\bar x=-x$ and $x^2=-1$: then $m_2(x,x)=\bar xx=1$, so $m_2(m_2(x,x),y)=y$, while $m_2(x,m_2(x,y))=\bar x(\bar xy)=x(xy)=(xx)y=-y$ by the alternative law for $m_1$. $\square$

**Remark.** Triality is the statement that the three legs are interchangeable, so the failure of associativity of the octonion product is not a defect to be repaired but the freedom that the symmetry permutes. In a setting in which the vector and the two half-spinors carry the three roles, the absence of a preferred one of the three legs is the absence of a preferred one of the three representations. The alternative laws are the part of the structure that is not symmetric among the legs, and they belong to the product $m_1$ alone: the two conjugated legs are not alternative, as the theorem records.

## Consequences and Boundaries

**Theorem.** The triality automorphism permutes the vector representation and the two half-spinor representations, and therefore:

1. it permutes the two chiralities of the spinor module, so that chirality is not an invariant of the group but of the choice of a leg;
2. it carries the vector representation of $SO(8)$ to a representation that does not descend to $SO(8)$, namely to a half-spinor representation;
3. it acts on the centre $\{\pm1\}$ trivially.

**Proof.** The first two items follow from the description of the permutation as a three-cycle; the third holds because the centre is the kernel of the action on the vector module and is carried to the kernel of the action on a half-spinor module, which is again $\{\pm1\}$, so the permutation of the modules acts trivially on the kernel. $\square$

**Remark (why there is no triality elsewhere).** The construction needs three modules of a common dimension and a diagram with a threefold symmetry. The diagram $D_4$ is the only Dynkin diagram of a simple Lie algebra with an automorphism of order three, and dimension eight is the only dimension in which the vector and the two half-spinor modules coincide, by the earlier theorem. Triality is therefore an accident of one dimension, and no analogous symmetry exists for $\mathrm{Spin}(n)$ with $n\neq8$.

## Summary

For $n=8$ the vector representation of $SO(8)$ and the two half-spinor representations of $\mathrm{Spin}(8)$, of dimension $2^{3}=8$ each, have the same dimension,

$$
\dim 8_v=\dim 8_s=\dim 8_c=8,
$$

and that coincidence of dimensions holds for $n=8$ alone among the even dimensions. The three modules are pairwise non-isomorphic, the centre of the spin group acting trivially on the vector module and by $-1$ on the two half-spinors, and the volume element separating the two half-spinors by the sign of its eigenvalue. There is a unique invariant trilinear form $\Phi:8_v\otimes8_s\otimes8_c\to\mathbb{R}$, the Clifford action composed with the invariant pairing, and it is the coupling of the three modules.

The Dynkin diagram of $D_4$ has a central node joined to three end nodes, so its automorphism group is $S_3$; consequently $\mathrm{Out}(\mathrm{Spin}(8))\cong S_3$ and there is an outer automorphism $\tau$ of order three that permutes the three eight-dimensional representations cyclically. The fixed-point subgroup of $\tau$ is the exceptional group $G_2$ of dimension $14$, obtained by folding the diagram, and the resulting chain is $\mathrm{Spin}(8)\supset\mathrm{Spin}(7)\supset G_2$, with $\mathrm{Spin}(7)$ the isotropy of a nonzero spinor and $G_2$ the isotropy of a unit octonion, so that $\mathrm{Spin}(7)/G_2$ is the unit sphere of the octonions. In the octonionic model the three legs are the three products $xy$, $\bar xy$ and $x\bar y$, the trilinear form is the real part of a product of three octonions, and the failure of associativity is exactly the freedom that triality permutes, while the alternative laws hold for the octonion product alone. The permutation carries a half-spinor to the vector module, so chirality is a matter of the choice of a leg, and it acts trivially on the centre of the spin group. Triality is confined to dimension eight: no other Dynkin diagram of a simple Lie algebra has an automorphism of order three, and no other dimension has the three modules of equal dimension.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $8_v$ | Vector representation of $SO(8)$ |
| $8_s$, $8_c$ | The two half-spinor representations of $\mathrm{Spin}(8)$ |
| $\Phi(v,\psi,\phi)=\langle\gamma(v)\psi,\phi\rangle$ | The triality trilinear form |
| $\tau$ | Triality automorphism, $\tau^3=1$ |
| $\mathrm{Out}(\mathrm{Spin}(8))\cong S_3$ | Outer automorphism group |
| $D_4$ | The Dynkin diagram whose three legs are permuted |
| $G_2=\mathrm{Spin}(8)^{\tau}$ | The fixed-point subgroup, of dimension $14$ |
| $\mathrm{Spin}(8)\supset\mathrm{Spin}(7)\supset G_2$ | Folding of the diagram, isotropy of a spinor and of a unit octonion |
| $\mathbb{O}$, $\bar x$, $\langle x,y\rangle$ | Octonions, conjugation and the inner product |
| $xy$, $\bar xy$, $x\bar y$ | The three legs of the trilinear form |

## Further Reading

- John Conway and Derek Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the octonionic construction of triality and the identification of the fixed-point subgroup.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the three eight-dimensional representations and the trilinear form.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spin representations in dimension eight and their symmetry.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the triality automorphism of $D_4$ and the permutation of the three representations.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6* (Springer, 2002), for the automorphisms of the Dynkin diagrams and the folding that produces $G_2$.
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000), for the octonionic models of triality and the exceptional groups.
