# __The Boundary Operator of a Simplex__

## Introduction

The simplest combinatorial object of algebraic topology is a simplex with an ordering of its vertices, and the simplest operator on it is the **boundary**: the alternating sum of its faces. This article introduces the standard simplex, the oriented simplices built from its vertices, the free module they generate in each degree, and the boundary operator on that module; it proves the one identity that makes the construction work, the **square-zero property** $\partial\partial = 0$, and it records the structure that the identity creates, a **chain complex**. The boundary operator is the archetype of a differential: a degree-lowering operator whose square vanishes, and every chain complex in the corpus is a graded module with such an operator.

The article is pure algebra on a combinatorial carrier: the oriented simplices are formal symbols, the chain module is a free module, and the boundary is defined by a signed sum. The topological content that the simplex carries — the realization of a simplicial complex, the singular chains of a space, and the homology of a chain complex — belongs to the algebraic topology of this Part and is named here with the deferral that the reader is about to meet it. The companion article for the topological uses is *Simplicial and Singular Homology*, which attaches a chain complex to a space and takes the homology of the chain complexes introduced here.

Coefficients are taken in a commutative ring $R$ with identity $1 \neq 0$, so that the chain groups are $R$-modules and the default $R = \mathbb{Z}$ gives abelian groups. The algebra of modules and free modules is that of Part I. Nothing analytic and nothing geometric is used: no distance is chosen, the simplex is a combinatorial object, and no length, area or angle is read from it.

## Oriented Simplices and the Chain Module

### Vertices, Simplices and Orientation

**Definition.** Let $v_{0}, v_{1}, \ldots, v_{n}$ be $n+1$ points in general position in $\mathbb{R}^{n}$, called the **vertices** of a **standard $n$-simplex**, and let

$$
\Delta_{n} = \Bigl\{\, \sum_{i=0}^{n} t_{i} v_{i} : t_{i} \geq 0,\ \sum_{i=0}^{n} t_{i} = 1 \,\Bigr\}
$$

be the simplex they span. An **oriented $n$-simplex** is the ordered list $[v_{0}, v_{1}, \ldots, v_{n}]$, subject to the relation that an even permutation of the vertices gives the same oriented simplex and an odd permutation gives the negative, so that

$$
[v_{\pi(0)}, \ldots, v_{\pi(n)}] = \operatorname{sgn}(\pi)\,[v_{0}, \ldots, v_{n}]
$$

for every permutation $\pi$. An oriented simplex in which two vertices are equal is declared to be zero.

The orientation is the only data beyond the unordered set of vertices: two orderings either agree or differ by a sign, and the sign is a sign of a permutation. For $n = 0$ an oriented simplex is a single vertex $[v_{0}]$, with no sign to change; for $n = 1$ the relation is $[v_{0}, v_{1}] = -[v_{1}, v_{0}]$.

### The Chain Module

**Definition.** For $n \geq 0$ the **chain module** $C_{n}$ is the free $R$-module on the oriented $n$-simplices of the ambient simplex, with the relations of the orientation imposed: reversing an ordering negates the generator.

An element of $C_{n}$ is a finite formal sum $\sum_{j} r_{j} \sigma_{j}$ with $r_{j} \in R$ and $\sigma_{j}$ an oriented $n$-simplex, and the module is graded by the degree $n$. The collection $(C_{n})_{n \geq 0}$ is a **graded module**, written $C_{*}$.

The generators are the oriented simplices, and the relations are the sign relations. In the language of operators, $C_{n}$ is the carrier of the operator that the next section defines, and the whole article is the study of that one operator on this carrier.

## The Boundary Operator

### The Alternating Sum

**Definition.** The **boundary operator** $\partial_{n} : C_{n} \to C_{n-1}$ is defined on an oriented simplex by

$$
\partial_{n}[v_{0}, \ldots, v_{n}] = \sum_{i=0}^{n} (-1)^{i}\,[v_{0}, \ldots, \hat{v}_{i}, \ldots, v_{n}],
$$

where the hat omits the vertex it covers and the remaining vertices keep their order; for $n = 0$ one sets $\partial_{0} = 0$. The formula is extended $R$-linearly to all of $C_{n}$, so that

$$
\partial_{n}\Bigl(\sum_{j} r_{j}\sigma_{j}\Bigr) = \sum_{j} r_{j}\,\partial_{n}\sigma_{j}.
$$

The sign $(-1)^{i}$ alternates with the position of the omitted vertex; the resulting sum is a **chain**, an element of $C_{n-1}$. The operator $\partial_{n}$ lowers the degree by one.

**Example (degrees one and two).** For the $1$-simplex,

$$
\partial_{1}[v_{0}, v_{1}] = [v_{1}] - [v_{0}],
$$

the difference of the two ends under the orientation. For the $2$-simplex,

$$
\partial_{2}[v_{0}, v_{1}, v_{2}] = [v_{1}, v_{2}] - [v_{0}, v_{2}] + [v_{0}, v_{1}],
$$

the three faces with alternating signs; the middle term is $[v_{0}, v_{2}] = -[v_{2}, v_{0}]$, so the three faces carry the signs of the orientation of the boundary.

### The Face Maps

**Definition.** For $i = 0, \ldots, n$ the **face map** $\delta^{i}$ replaces the oriented $n$-simplex by its $i$-th face,

$$
\delta^{i}[v_{0}, \ldots, v_{n}] = [v_{0}, \ldots, \hat{v}_{i}, \ldots, v_{n}],
$$

and is the identity on zero; it is extended linearly. The boundary is then

$$
\partial_{n} = \sum_{i=0}^{n} (-1)^{i}\,\delta^{i}.
$$

The face maps satisfy the **simplicial identities**

$$
\delta^{j}\delta^{i} = \delta^{i}\delta^{j-1} \qquad (i < j),
$$

read as maps from degree $n$ to degree $n-2$: the composition of the omission of the $i$-th vertex with that of the $j$-th is the same as the omission of the $(j-1)$-st vertex with that of the $i$-th when the first omission is performed second.

**Proof.** Both sides omit the vertices in positions $i$ and $j$ of the original ordering and keep the remaining vertices in their original order; the only difference is the order in which the two omissions are performed, which does not change the result.

The identities are the combinatorial engine of the square-zero property: the double omission of two vertices can be performed in either order, and the two orders carry signs that cancel.

### Linearity and Naturality

**Proposition.** The boundary operator is $R$-linear and degree-lowering; it is natural for maps of the oriented simplices, in the sense that a map that relabels the vertices and preserves the order commutes with $\partial$, and a map that reverses the order anti-commutes with it.

**Proof.** Linearity is the definition, and the degree statement is that $\partial_{n}$ maps $C_{n}$ to $C_{n-1}$. For the reordering statement, a relabelling by a permutation $\pi$ multiplies the oriented simplex by the sign of the restriction of $\pi$ to the remaining vertices, and the alternating sum of the faces transforms with the same sign; an odd permutation changes the sign of the whole sum.

## The Square-Zero Property

### The Statement

**Theorem.** For every $n \geq 1$,

$$
\partial_{n-1} \circ \partial_{n} = 0 .
$$

Equivalently, every boundary is a cycle: the image of $\partial_{n}$ is contained in the kernel of $\partial_{n-1}$.

**Proof.** It suffices to compute on an oriented simplex $[v_{0}, \ldots, v_{n}]$. Write the outer $\partial_{n-1}$ with summation index $j$ and the inner $\partial_{n}$ with summation index $i$, so that the composite is $\sum_{j}\sum_{i} (-1)^{j+i}\delta^{j}\delta^{i}$, where $\delta^{j}$ acts on the $(n-1)$-simplex produced by $\delta^{i}$. A pair of indices with $i < j$ contributes through the term $(j, i)$; the simplicial identity gives $\delta^{j}\delta^{i} = \delta^{i}\delta^{j-1}$, so the same face map occurs in the term $(i, j-1)$ of the double sum. The signs are $(-1)^{j+i}$ and $(-1)^{i+j-1}$, which are opposite, so the two terms cancel. Every term is paired this way, and the total is zero.

### The Cancellation in Low Degrees

**Example (degree two).** On the $2$-simplex,

$$
\partial_{1}\partial_{2}[v_{0}, v_{1}, v_{2}] = \partial_{1}\bigl([v_{1},v_{2}] - [v_{0},v_{2}] + [v_{0},v_{1}]\bigr) = ([v_{2}] - [v_{1}]) - ([v_{2}] - [v_{0}]) + ([v_{1}] - [v_{0}]) = 0,
$$

the six terms cancelling in three opposite pairs. This is the cancellation of the proof in the first nontrivial degree.

**Example (degree three).** On the $3$-simplex, $\partial_{3}$ is the alternating sum of its four $2$-faces, and each of those contributes three $1$-faces; the twelve terms cancel in six pairs, by the same sign computation. The number of terms of $\partial^{2}$ on an $n$-simplex is $(n+1)n$, and they cancel in $\tfrac{n(n+1)}{2}$ pairs.

**Remark.** The square-zero property is the statement that $\operatorname{im}\partial_{n} \subseteq \ker\partial_{n-1}$, and the failure of the inclusion to be an equality is the whole of homology: the quotient $\ker\partial_{n} / \operatorname{im}\partial_{n+1}$ is the $n$-th homology of the chain complex, the subject of *Simplicial and Singular Homology*. The boundary operator introduced here is the operator whose image and kernel that quotient compares.

## The Chain Complex

### The Complex

**Definition.** A **chain complex** over $R$ is a graded $R$-module $C_{*}$ with operators $\partial_{n} : C_{n} \to C_{n-1}$ satisfying $\partial_{n-1}\partial_{n} = 0$ for all $n$. The operators are its **differentials**, and the complex is written

$$
\cdots \longrightarrow C_{n+1} \xrightarrow{\ \partial_{n+1}\ } C_{n} \xrightarrow{\ \partial_{n}\ } C_{n-1} \longrightarrow \cdots \longrightarrow C_{0} \longrightarrow 0 .
$$

**Theorem.** Let $\Delta_{n}$ be the standard $n$-simplex, let $C_{n}$ be the free $R$-module on its oriented $n$-simplices, and let $\partial_{n}$ be the alternating sum of the faces. Then $(C_{*}, \partial_{*})$ is a chain complex. It is the **simplicial chain complex of the simplex**, and the boundary operator of a simplex is the operator that starts it.

**Proof.** The square-zero property is the previous theorem; the rest is the definition of the chain module and of the boundary.

The complex of the standard simplex is finite: $C_{n} = 0$ for $n$ greater than the dimension of the ambient simplex, and the complex is a finite sequence of free modules. The boundary operators satisfy the single relation $\partial\partial = 0$, so the complex is determined by the alternating sum on the top simplex together with the face maps.

### Cycles and Boundaries

**Definition.** A chain $c \in C_{n}$ with $\partial_{n} c = 0$ is a **cycle**, and a chain of the form $\partial_{n+1} d$ is a **boundary**. The square-zero property says that every boundary is a cycle, so that

$$
B_{n} = \operatorname{im}\partial_{n+1} \subseteq Z_{n} = \ker\partial_{n},
$$

and the quotient $H_{n} = Z_{n} / B_{n}$ is the **homology** of the complex in degree $n$.

**Example (the simplex has trivial reduced homology).** For the standard $n$-simplex with $n \geq 1$ and coefficients in a ring, the homology of its simplicial chain complex is $H_{0} \cong R$ and $H_{k} = 0$ for $k \geq 1$; the simplex is contractible, and the computation belongs to *Simplicial and Singular Homology*, where it is made with the boundary operators introduced here. The vanishing is the statement that on a simplex every cycle of positive degree is a boundary, which is the failure of the inclusion $B_{n} \subseteq Z_{n}$ to be strict in that case.

### The Boundary of a Boundary

**Corollary.** The boundary operator applied twice is the zero operator on every chain, $\partial_{n-1}\partial_{n} = 0$, so the operator $\partial$ is a differential of degree $-1$; and a linear operator $d$ of degree $-1$ on a graded module is a differential exactly when $d^{2} = 0$.

**Proof.** The first statement is the square-zero property; the second is the definition of a chain complex, and the equivalence is the same square-zero condition read for a general graded module.

## The Operator Point of View

The boundary is an operator of a kind that recurs throughout the corpus: it lowers a degree, and its square vanishes. Three consequences of the point of view are worth recording, because later articles use them.

**Theorem.** The boundary operator is not injective and not surjective in general; its kernel is the module of cycles, its image the module of boundaries, and its failure to be an isomorphism in each degree is measured by the homology. The operator is determined by its values on the oriented simplices, and these are constrained only by the orientation relation and the square-zero property.

**Proof.** The kernel and the image are the cycle and boundary modules by definition; the failure of injectivity is that a boundary need not be zero, and the failure of surjectivity is that not every chain is a boundary. The last statement is that a linear map on a free module is determined by its values on a basis, and the values are the alternating sum of the faces.

**Remark.** The **coboundary** of a cochain complex raises the degree and satisfies the same square-zero property; it is the transpose of the boundary and is the operator of the cohomology of *Cohomology and the Universal Coefficient Theorem*. It is named here to fix the vocabulary and is not developed.

**Remark.** The boundary operator on simplices is the oldest example of a differential, and the chain complex it starts is the simplest nontrivial one. The higher structure — the product on cohomology, the exact sequences, the spectral sequences — is built on top of the square-zero property, and none of it is available until the complex exists. This is why the operator is introduced before the homology: the operator is the definition, and the homology is the invariant.

## Summary

An oriented $n$-simplex is an ordered list of $n+1$ vertices, taken modulo even permutations, and the chain module $C_{n}$ is the free $R$-module on the oriented $n$-simplices with the orientation relations imposed. The boundary operator $\partial_{n} : C_{n} \to C_{n-1}$ is the alternating sum of the faces, $\partial_{n}[v_{0},\ldots,v_{n}] = \sum_{i}(-1)^{i}[v_{0},\ldots,\hat v_{i},\ldots,v_{n}]$, extended linearly; it lowers the degree, and it satisfies the square-zero property $\partial_{n-1}\partial_{n} = 0$, proved by the cancellation of the two orders in which a pair of vertices is omitted. A graded module with a degree-lowering operator squaring to zero is a chain complex, so the boundary operator starts the simplicial chain complex of the simplex; its kernel is the module of cycles and its image the module of boundaries, and the inclusion of the boundaries in the cycles is the homology, which is the subject of the algebraic topology of this Part. The boundary is the archetype of a differential, and the square-zero property is the relation that makes the complex a complex.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | A commutative ring with $1 \neq 0$; the coefficient ring |
| $\Delta_{n}$ | The standard $n$-simplex on vertices $v_{0}, \ldots, v_{n}$ |
| $[v_{0}, \ldots, v_{n}]$ | Oriented $n$-simplex; even permutations give it, odd ones its negative |
| $\hat{v}_{i}$ | The vertex omitted from the list |
| $C_{n}$ | Free $R$-module on the oriented $n$-simplices; the chain module |
| $C_{*}$ | The graded module $(C_{n})_{n \geq 0}$ |
| $\partial_{n}$ | Boundary, $\sum_{i}(-1)^{i}\delta^{i}$, a map $C_{n} \to C_{n-1}$ |
| $\delta^{i}$ | The $i$-th face map |
| $\delta^{j}\delta^{i} = \delta^{i}\delta^{j-1}$ | The simplicial identities, for $i < j$ |
| $\partial_{n-1}\partial_{n} = 0$ | The square-zero property; $\partial$ is a differential |
| $Z_{n} = \ker\partial_{n}$, $B_{n} = \operatorname{im}\partial_{n+1}$ | Cycles, boundaries |
| $H_{n} = Z_{n}/B_{n}$ | Homology of the complex; introduced in *Simplicial and Singular Homology* |
| chain complex | A graded module with a degree-lowering operator squaring to zero |

## Further Reading

- Samuel Eilenberg and Norman Steenrod, *Foundations of Algebraic Topology* (Princeton University Press, 1952), for the simplicial chain complex, the boundary operator and the square-zero property.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the boundary operator, the simplicial chain complex and the computation of the homology of a simplex.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for oriented simplices, the face maps and the simplicial identities.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for chain complexes, differentials and the algebraic theory of the square-zero operator.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for complexes over a ring, the differential, and the homology of a complex.
- Saunders Mac Lane, *Homology* (Springer, 1963; reprinted 1995), for the simplicial identities and the construction of the chain complex from a simplicial object.
