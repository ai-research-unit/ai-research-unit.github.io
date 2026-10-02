
# __Symmetric Pairs of a Lie Algebra__

## Introduction

A **symmetric pair** is a pair $(\mathrm{G},\mathrm{K})$ consisting of a Lie algebra $\mathrm{G}$ and the fixed subalgebra $\mathrm{K}=\mathrm{G}^{\theta}$ of an involution $\theta$; equivalently it is a Lie algebra with a decomposition

$$
\mathrm{G}=\mathrm{K}\oplus\mathrm{P},\qquad
[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K},\qquad
[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P},\qquad
[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K},
$$

where $\mathrm{K}$ is the $+1$-eigenspace and $\mathrm{P}$ the $-1$-eigenspace of the involution. The quotient $\mathrm{G}/\mathrm{K}$, read through the identification with $\mathrm{P}$, is the **infinitesimal symmetric space** of the pair, and its structure is governed by the bracket $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$, which plays the role of the curvature. This article, the eighth and last entry of the `- * Theory` group of the category, defines symmetric pairs, derives the decomposition and the curvature identity, describes the infinitesimal symmetric space, and states the **classification** of the symmetric pairs of a semisimple Lie algebra by the involutions up to conjugacy, equivalently by the real forms and the Satake and Vogan diagrams. The Cartan involution and the Cartan decomposition are *The Cartan Involution and the Cartan Decomposition*; the real forms are *Real Forms of a Complex Lie Algebra*; the graded structure is *Graded Lie Algebras with an Involution*; the group theory and the global symmetric spaces belong to later Parts and are named only.

The base is a field $K$ of characteristic not two; the Lie algebra is $\mathrm{G}$ and the involution $\theta$; the article uses the eigenspace decomposition and the bracket only, and takes no topological or geometric reading.

## Symmetric Pairs and the Decomposition

**Definition.** A **symmetric pair** is a pair $(\mathrm{G},\mathrm{K})$ with $\mathrm{G}$ a Lie algebra and $\mathrm{K}$ the fixed subalgebra of an involution $\theta$ of $\mathrm{G}$; a **morphism** of symmetric pairs is a Lie homomorphism carrying one involution to the other, and an **isomorphism** is a bijective morphism.

**Proposition.** A pair $(\mathrm{G},\mathrm{K})$ is symmetric if and only if there is a direct decomposition $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$ with the three bracket relations displayed above; the involution is then $+1$ on $\mathrm{K}$ and $-1$ on $\mathrm{P}$, and it is unique for the decomposition.

**Proof.** An involution gives the decomposition by its eigenspaces and the bracket relations by applying $\theta$ to the bracket; conversely a decomposition with the bracket relations defines the map which is $+1$ on $\mathrm{K}$ and $-1$ on $\mathrm{P}$, and the bracket relations are exactly the statement that this map is an automorphism of order two. $\square$

**Corollary.** A symmetric pair is the same thing as a Lie algebra with an involution, that is a Lie algebra with a $\mathbb{Z}/2$-grading whose grade involution is an automorphism of the algebra; the pair is the graded object of *Graded Lie Algebras with an Involution* in the $\mathbb{Z}/2$ case.

## The Curvature and the Infinitesimal Symmetric Space

**Definition.** For a symmetric pair $(\mathrm{G},\mathrm{K})$ with decomposition $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$, the **curvature** is the $\mathrm{K}$-valued graded bilinear map on $\mathrm{P}$ given by the bracket,

$$
\mathrm{R}(x,y)=[x,y]\in\mathrm{K}\qquad (x,y\in\mathrm{P}).
$$

**Theorem.** The curvature satisfies, for $x,y,z\in\mathrm{P}$,

$$
\mathrm{R}(x,y)=-\mathrm{R}(y,x),\qquad
\mathrm{R}(x,y)z+\mathrm{R}(y,z)x+\mathrm{R}(z,x)y=0 ,
$$

the second identity being the projection to $\mathrm{P}$ of the Jacobi identity of $\mathrm{G}$.

**Proof.** The antisymmetry is that of the bracket; the Jacobi identity $[[x,y],z]+[[y,z],x]+[[z,x],y]=0$ has $[x,y],[y,z],[z,x]\in\mathrm{K}$, and since $[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}$ the three summands lie in $\mathrm{P}$ and their sum is zero. $\square$

**Corollary.** The pair $(\mathrm{K},\mathrm{P},\mathrm{R})$ is an **infinitesimal symmetric space**: a Lie algebra $\mathrm{K}$ acting on $\mathrm{P}$ and a $\mathrm{K}$-invariant curvature satisfying the Bianchi identity, obtained from the bracket; the symmetry of the space is the involution, acting as $-1$ on the tangent space $\mathrm{P}$.

**Proposition.** The $\mathrm{K}$-module $\mathrm{P}$ is the tangent module of the infinitesimal symmetric space, and the decomposition is a "symmetric" one in the sense that the involution reverses the tangent directions while preserving $\mathrm{K}$; the group analogue, where $(\mathrm{G},\mathrm{K})$ is a pair of Lie groups, gives the symmetric space $\mathrm{G}/\mathrm{K}$, whose theory belongs to Part II and is named only.

**Proof.** The identification $\mathrm{G}/\mathrm{K}\cong\mathrm{P}$ is the linear isomorphism of the previous article, and the action of $\mathrm{K}$ is the adjoint one; the statement about the involution is the definitions. $\square$

## Classification

**Proposition.** The symmetric pairs of a fixed Lie algebra $\mathrm{G}$ correspond to the involutions of $\mathrm{G}$ up to conjugation by automorphisms: two pairs $(\mathrm{G},\mathrm{K})$ and $(\mathrm{G},\mathrm{K}')$ are isomorphic when the involutions are conjugate, and then $\mathrm{K}'$ is the image of $\mathrm{K}$.

**Proof.** An isomorphism of the pairs carries the involution to the involution, hence conjugates them; conversely a conjugating automorphism carries the fixed subalgebra to the fixed subalgebra by uniqueness of the involution for the decomposition. $\square$

**Theorem (classification).** Let $\mathrm{G}$ be a complex semisimple Lie algebra. The conjugacy classes of involutions of $\mathrm{G}$ are classified by the **Satake** and **Vogan diagrams**, which record the action of the involution on a system of simple roots of a stable Cartan subalgebra, equivalently by the real forms of $\mathrm{G}$; the pair is described by the **rank** of the symmetric pair, the number of black nodes plus the number of pairs of white nodes joined by an arrow.

**Proof.** This is the standard classification of involutions of a complex semisimple Lie algebra, via the restriction to a stable Cartan subalgebra, the induced action on the roots and the associated diagram; it is the same classification as that of the real forms of *Real Forms of a Complex Lie Algebra*, and it is quoted from the theory of *Root Systems and Classification*. $\square$

**Corollary.** The symmetric pairs of the complex semisimple $\mathrm{G}$ are in bijection with the real forms of $\mathrm{G}$ and with the diagrams; the compact real form corresponds to the involution with all nodes black and the split real form to the involution with all nodes white.

**Proposition (index).** The **index** of a symmetric pair, the difference $\dim\mathrm{K}-\dim\mathrm{P}$ up to the fixed part of a Cartan subalgebra, is determined by the diagram, and the pair is **irreducible** when the diagram is connected; the index and the rank are the two invariants read off the diagram.

**Proof.** The dimension of $\mathrm{K}$ is the number of roots fixed by the involution plus the dimension of the fixed part of the Cartan subalgebra, and the dimension of $\mathrm{P}$ is the number of roots moved; both are read off the diagram operations. $\square$

## Worked Cases

For $\mathrm{G}=\mathrm{sl}(2,\mathbb{C})$ the involutions correspond to the two real forms $\mathrm{su}(2)$ and $\mathrm{sl}(2,\mathbb{R})$; the diagrams are the single black node and the single white node, and the pairs are $(\mathrm{sl}(2,\mathbb{C}),\mathrm{su}(2))$ with $\dim\mathrm{K}=3$, $\dim\mathrm{P}=0$ and $(\mathrm{sl}(2,\mathbb{C}),\mathrm{sl}(2,\mathbb{R}))$ with $\dim\mathrm{K}=1$, $\dim\mathrm{P}=2$.

For $\mathrm{G}=\mathrm{sl}(3,\mathbb{C})$ the three involutions correspond to $\mathrm{su}(3)$, $\mathrm{sl}(3,\mathbb{R})$ and $\mathrm{su}(2,1)$; the pairs have $\dim\mathrm{K}=8,\dim\mathrm{P}=0$; $\dim\mathrm{K}=5,\dim\mathrm{P}=3$; and $\dim\mathrm{K}=4,\dim\mathrm{P}=4$ respectively, and the diagrams are those of *Real Forms of a Complex Lie Algebra*.

**Verified.** The bracket relations of a symmetric pair were checked on $\mathrm{sl}(2,\mathbb{R})$ with the involution $x\mapsto-x^{t}$, the curvature identity was verified on the basis, and the dimensions were computed for the two $A_1$ pairs and the three $A_2$ pairs.

## Summary

A **symmetric pair** $(\mathrm{G},\mathrm{K})$ is a Lie algebra with an involution $\theta$ and the fixed subalgebra $\mathrm{K}=\mathrm{G}^{\theta}$, equivalently a decomposition $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$ with $[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K}$, $[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}$, $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$; it is the $\mathbb{Z}/2$-graded object whose grade involution is the symmetry. The bracket on $\mathrm{P}$ is the **curvature** $\mathrm{R}(x,y)=[x,y]\in\mathrm{K}$, antisymmetric and satisfying the Bianchi identity, and $(\mathrm{K},\mathrm{P},\mathrm{R})$ is the **infinitesimal symmetric space** with tangent module $\mathrm{P}$ and the involution acting as $-1$ on the tangent directions. Isomorphism classes of symmetric pairs are conjugacy classes of involutions, and over $\mathbb{C}$ they are classified by the Satake and Vogan diagrams, equivalently by the real forms, with the rank and the index read off the diagram; the compact and split real forms correspond to the all-black and all-white diagrams. For $\mathrm{sl}(2,\mathbb{C})$ there are two pairs and for $\mathrm{sl}(3,\mathbb{C})$ three, matching the real forms. The group-level symmetric spaces belong to Part II and are named only; the operator layer belongs to the `- * Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{G}$ | a Lie algebra with an involution |
| $\theta$ | the involution |
| $\mathrm{K}=\mathrm{G}^{\theta}$ | the fixed subalgebra |
| $\mathrm{P}$ | the anti-fixed complement, the tangent module |
| $\mathrm{R}(x,y)=[x,y]$ | the curvature |
| $(\mathrm{K},\mathrm{P},\mathrm{R})$ | the infinitesimal symmetric space |
| Satake diagram | the decorated diagram classifying the involution |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for symmetric pairs and symmetric spaces.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction*, Progress in Mathematics 140 (Birkhäuser, 2nd ed. 2002), for the classification of involutions and Vogan diagrams.
- Ottmar Loos, *Symmetric Spaces I: General Theory*, Mathematics Lecture Note Series (Benjamin, 1969), for the infinitesimal theory of symmetric spaces.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4–6 (Springer, 2002), for involutions, symmetric pairs and the associated graded structures.
