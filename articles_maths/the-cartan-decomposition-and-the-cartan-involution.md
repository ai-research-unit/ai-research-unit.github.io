
# __The Cartan Decomposition and the Cartan Involution__

## Introduction

On a real semisimple Lie algebra the Cartan involution is the involution that makes the twisted Killing form positive definite, and the decomposition of the algebra into its $+1$ and its $-1$ eigenspaces is the **Cartan decomposition**. The two pieces are not symmetric: the fixed part is a subalgebra, the complement is a module over it, and the bracket of two complement elements falls back into the fixed part. Globally the decomposition exponentiates to the polar decomposition of the group, the fixed part integrates to a **maximal compact subgroup**, and the quotient is the symmetric space of the group. The decomposition is the algebraic skeleton on which the real structure theory, the representation theory and the analysis of the group are built.

This article treats the Cartan decomposition and the Cartan involution and the maximal compact subgroup they produce. It is the third article of the `- * Theory` group of the category; the real forms and the existence of the Cartan involution for a semisimple algebra are from *Real Forms of a Complex Lie Group and the Cartan Involution*, the analytic consequences are *Unitary Representations of a Lie Group*, and the Hermitian case is *Hermitian Lie Groups and the Bounded Domain*.

The article assumes the real and the complex Lie group, the exponential map and its differential from *Lie Groups* and *The Lie Algebra and the Exponential Map*, the semisimple structure and the Killing form from *Structure of Lie Algebras*, the involution and its fixed and anti-fixed parts from *Involutive Groups* and *Graded Lie Algebras with an Involution*, and the polar decomposition of a real Lie algebra from *Real Forms of a Complex Lie Group and the Cartan Involution*. The Riemannian geometry of the symmetric space — its metric, its geodesics and its curvature as objects of study — belongs to Part IV, and the present article uses the homogeneous space only through the involution that defines it; the harmonic analysis on the symmetric space belongs to *The Convolution Operator on a Symmetric Space* and to the later articles of the category.

## The Involution and Its Eigenspaces

### The Cartan Involution

**Definition.** Let $\mathrm{G}$ be a real semisimple Lie algebra with Killing form $B$. A **Cartan involution** of $\mathrm{G}$ is an involutive automorphism $\theta$ such that the twisted form

$$
B_\theta(X,Y) = -B(X,\theta Y)
$$

is positive definite. The existence and the conjugacy of the Cartan involutions, and the fact that the compact real form is the fixed algebra of a Cartan involution of the complexification, are established in *Real Forms of a Complex Lie Group and the Cartan Involution*.

**Definition.** The **Cartan decomposition** attached to $\theta$ is the decomposition into the eigenspaces

$$
\mathrm{G} = \mathrm{K}\oplus\mathrm{P}, \qquad \mathrm{K} = \{X : \theta X = X\}, \qquad \mathrm{P} = \{X : \theta X = -X\} .
$$

Its elements are written $X = X_{\mathrm{K}} + X_{\mathrm{P}}$ with the two components in the two pieces.

### The Bracket Relations

**Proposition.** The decomposition satisfies

$$
[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K}, \qquad [\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}, \qquad [\mathrm{P},\mathrm{P}]\subseteq\mathrm{K} .
$$

*Proof.* The involution $\theta$ is an automorphism, so $\theta[X,Y] = [\theta X,\theta Y]$; taking $X,Y$ in the eigenpieces with signs $\epsilon,\delta\in\{+1,-1\}$ gives $\theta[X,Y] = \epsilon\delta[X,Y]$, so the bracket lies in the eigenspace of the sign $\epsilon\delta$. In particular $\mathrm{K}$ is a subalgebra, $\mathrm{P}$ is a $\mathrm{K}$-module, and the sum is a $\mathbb{Z}/2$-grading of the Lie algebra in the sense of *Graded Lie Algebras with an Involution*.

**Proposition.** The two pieces are orthogonal for the Killing form and for the twisted form, and the restrictions satisfy

$$
B_\theta(X,Y) = \begin{cases} -B(X,Y), & X,Y\in\mathrm{K},\\ B(X,Y), & X,Y\in\mathrm{P},\\ 0, & X\in\mathrm{K},\ Y\in\mathrm{P}, \end{cases}
$$

so that $-B$ is positive definite on $\mathrm{K}$ and $B$ is positive definite on $\mathrm{P}$.

*Proof.* The decomposition into eigenspaces of an involution that is an automorphism is orthogonal for the invariant form $B$, because $B(X,Y) = B(\theta X,\theta Y) = \epsilon\delta\,B(X,Y)$; the displayed case distinction follows, and the definiteness is the positivity of $B_\theta$ together with the signs.

### The Killing Form on the Pieces

**Corollary.** The restriction of the Killing form to $\mathrm{K}$ is negative definite and to $\mathrm{P}$ is positive definite, and the involution $\theta$ is symmetric with respect to $B$: $B(\theta X,Y) = B(X,\theta Y)$. The signature of $B$ is therefore $(\dim\mathrm{P},\dim\mathrm{K})$.

*Proof.* The definiteness is the case distinction above with $B_\theta$ positive; the symmetry of $\theta$ with respect to $B$ is the invariance of $B$ under the automorphism $\theta$, and the signature counts the positive and the negative directions.

## The Structure of the Decomposition

### The Decomposition Determines the Involution

**Theorem.** Let $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ be a direct sum decomposition of a real semisimple Lie algebra such that $\mathrm{K}$ is a subalgebra, $[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}$, $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$, and $\mathrm{K}$ and $\mathrm{P}$ are orthogonal under $B$ with $B$ negative definite on $\mathrm{K}$ and positive definite on $\mathrm{P}$. Then the linear map $\theta$ equal to $+\mathrm{id}$ on $\mathrm{K}$ and $-\mathrm{id}$ on $\mathrm{P}$ is a Cartan involution, and the given decomposition is its Cartan decomposition.

*Proof.* The map $\theta$ is an automorphism because the bracket relations have exactly the signs needed, $\theta[X,Y] = [\theta X,\theta Y]$ on homogeneous pairs; it is involutive by construction; and $B_\theta(X,Y) = -B(X,\theta Y)$ is positive definite because on $\mathrm{K}$ it is $-B$ and on $\mathrm{P}$ it is $B$, with the two pieces orthogonal by hypothesis. Hence $\theta$ is a Cartan involution and the decomposition is its eigenspace decomposition.

### The Compact Type and the Non-Compact Type

**Definition.** The subalgebra $\mathrm{K}$ is of **compact type** — its Killing form is negative definite, so it is a compact Lie algebra in the sense of *Structure of Lie Algebras* — and a nonzero element of $\mathrm{P}$ is of **non-compact type**. An element $X\in\mathrm{G}$ is **elliptic** when $\operatorname{ad}_X$ is semisimple with purely imaginary eigenvalues, **hyperbolic** when $\operatorname{ad}_X$ is semisimple with real eigenvalues, and **nilpotent** when $\operatorname{ad}_X$ is nilpotent. Every element has a component in $\mathrm{K}$ that is elliptic and a component in $\mathrm{P}$ that is hyperbolic or zero.

*Proof.* On $\mathrm{K}$ the form $B$ is negative definite, so $\operatorname{ad}_X$ for $X\in\mathrm{K}$ is skew with respect to $B_\theta$, hence diagonalisable over $\mathbb{C}$ with purely imaginary eigenvalues; on $\mathrm{P}$ it is self-adjoint with respect to the positive form, hence diagonalisable with real eigenvalues. The decomposition of an element into its two components separates the two types, and the nilpotent case occurs when the hyperbolic component vanishes.

**Corollary (the maximal compact subalgebra).** The subalgebra $\mathrm{K}$ is a maximal compactly embedded subalgebra of $\mathrm{G}$: it is compact, it is contained in no larger compactly embedded subalgebra, and every compactly embedded subalgebra is conjugate to a subalgebra of $\mathrm{K}$.

*Proof.* The compactness is the negative definiteness of the Killing form on $\mathrm{K}$; a larger compactly embedded subalgebra would contain an element of $\mathrm{P}$, whose adjoint is self-adjoint with a nonzero real eigenvalue, contradicting the compactness; the conjugacy is the conjugacy of the Cartan involutions.

## The Maximal Compact Subgroup

### The Fixed Subgroup

**Definition.** Let $G$ be a connected Lie group with Lie algebra $\mathrm{G}$ and let $\theta$ be a Cartan involution of $\mathrm{G}$. The **fixed subgroup** is the closed subgroup

$$
K = \{g\in G : \Theta(g) = g\}
$$

where $\Theta$ is the automorphism of $G$ integrating $\theta$; when $G$ is simply connected the automorphism exists and is unique, and in general it exists on a covering group. Its Lie algebra is $\mathrm{K}$.

**Theorem (the maximal compact subgroup).** The subgroup $K$ is a maximal compact subgroup of $G$: it is compact, it is contained in no larger compact subgroup, and every compact subgroup of $G$ is conjugate to a subgroup of $K$. All maximal compact subgroups of $G$ are conjugate, and the quotient $G/K$ is connected when $G$ is connected.

*Proof.* The compactness of $K$ follows from that of the algebra $\mathrm{K}$ and the closedness of the fixed set of an automorphism; a larger compact subgroup would have a compact Lie algebra strictly containing $\mathrm{K}$, contradicting the maximality of $\mathrm{K}$; the conjugacy of the compact subgroups is the conjugacy of the maximal compactly embedded subalgebras of $\mathrm{G}$, transferable to the group because the adjoint map has the compact subgroups as its fibres up to the centre. The connectedness of $G/K$ is the connectedness of $G$ and the surjectivity of the quotient map.

### The Polar Decomposition

**Theorem (the Cartan decomposition of the group).** Let $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ be the Cartan decomposition. The map

$$
\mathrm{K}\times\mathrm{P} \longrightarrow G, \qquad (X,Y) \longmapsto \exp X\,\exp Y ,
$$

is a diffeomorphism onto $G$; equivalently every $g\in G$ has a unique expression $g = k\exp Y$ with $k\in K$ and $Y\in\mathrm{P}$, and the map $Y\mapsto\exp Y$ is a diffeomorphism from $\mathrm{P}$ onto the image.

*Proof.* The differential of the map at the identity is the identity because $\mathrm{K}\cap\mathrm{P} = 0$, so it is a local diffeomorphism; the exponential restricted to $\mathrm{P}$ is injective because $B$ is positive definite on $\mathrm{P}$ and the flow of a hyperbolic element is unbounded; the surjectivity follows from the polar decomposition of the linear group and the closedness of the image, which is the standard argument of the Cartan decomposition. The detailed proof is in the references.

**Corollary.** The group $G$ is homotopy equivalent to $K$, the quotient $G/K$ is diffeomorphic to the vector space $\mathrm{P}$, and $\exp : \mathrm{P}\to G/K$ is a diffeomorphism; in particular $G$ has the homotopy type of its maximal compact subgroup and $G/K$ is contractible.

*Proof.* The polar decomposition exhibits $G$ as the product of the compact $K$ with the contractible space $\exp\mathrm{P}$; the quotient identifies with $\mathrm{P}$, which is a vector space, and the fibration $K\to G\to G/K$ gives the homotopy equivalence.

## The Symmetric Space

**Definition.** The **symmetric space** attached to the pair $(\mathrm{G},\theta)$ is the quotient $G/K$ with the base point $o = eK$; the involution $\Theta$ descends to the map $gK\mapsto\Theta(g)K$, which fixes $o$, and the tangent space at $o$ identifies with $\mathrm{P}$.

**Theorem.** The map $s_o : gK\mapsto\Theta(g)K$ is an involutive diffeomorphism with isolated fixed point $o$, and for every $p\in G/K$ the conjugate $s_p = g s_o g^{-1}$ with $p = go$ is an involutive diffeomorphism with isolated fixed point $p$; the family $(s_p)$ is the geodesic symmetry of the space, and the curvature at the base point is $R(X,Y)Z = -[[X,Y],Z]$ for $X,Y,Z\in\mathrm{P}$.

*Proof.* The conjugate maps are well defined because $K$ is the fixed subgroup, and each has the single fixed point $p$ because the differential of $s_p$ at $p$ is $-\mathrm{id}$ on $\mathrm{P}$; the curvature is computed from the Maurer--Cartan equation and the bracket relations of the Cartan decomposition, the components of $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$ producing the double bracket. The development of the geometry — the exponential coordinates, the restricted root system, the Weyl group and the boundary — belongs to Part IV.

**Remark (the boundary with geometry).** The symmetric space is introduced here only as the homogeneous space $G/K$ with the involution that defines it, because the article is about the decomposition of the algebra and the compact subgroup it determines. The metric, the geodesics and the curvature as objects of study, and the compactifications and the boundary theory, are Part IV.

## Examples

### The Rank-One Algebra

Let $\mathrm{G} = \mathrm{sl}_2(\mathbb{R})$ with the Cartan involution $\theta(X) = -X^{t}$, the negative transpose. Then $\mathrm{K} = \mathrm{so}(2)$ is one-dimensional, spanned by $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, and $\mathrm{P}$ consists of the traceless symmetric matrices, a two-dimensional space of non-compact type; the maximal compact subgroup is $SO(2)$ and the symmetric space is the hyperbolic plane up to the connected component, whose geometry belongs to Part IV.

### The Orthogonal Algebras

Let $\mathrm{G} = \mathrm{so}(p,q)$ with the involution $\theta(X) = -X^{t}$ for the standard form of signature $(p,q)$. Then $\mathrm{K} = \mathrm{so}(p)\oplus\mathrm{so}(q)$ and $\mathrm{P}$ is the space of the off-diagonal blocks; $\dim\mathrm{K} = \frac{p(p-1)}{2} + \frac{q(q-1)}{2}$ and $\dim\mathrm{P} = pq$, and the symmetric space is the Grassmannian of the $p$-planes of a fixed parity, whose geometry is Part IV.

### The Compact Case

If $\mathrm{G}$ is compact, the Killing form is negative definite and the identity is a Cartan involution; then $\mathrm{K} = \mathrm{G}$, $\mathrm{P} = 0$, and $G/K$ is a point. This is the boundary case of the decomposition, and it is the one in which the analysis of the group is the Peter--Weyl theory of *Unitary Representations of a Lie Group* with no symmetric space present.

### The Complex Case

Let $\mathrm{G}$ be a complex semisimple Lie algebra regarded as a real Lie algebra with its real form $\mathrm{G}^{\mathbb{R}}$. The Cartan involution is the conjugation $\theta(X) = -X$ with respect to a compact real form; the decomposition $\mathrm{G}^{\mathbb{R}} = \mathrm{G}_u\oplus i\mathrm{G}_u$ has $\mathrm{K} = \mathrm{G}_u$ and $\mathrm{P} = i\mathrm{G}_u$, the maximal compact subgroup is the compact form, and the symmetric space is the space of the conjugacy classes, developed in the Hermitian theory of *Hermitian Lie Groups and the Bounded Domain*.

## Summary

A **Cartan involution** of a real semisimple Lie algebra is an involutive automorphism $\theta$ for which the twisted Killing form $B_\theta(X,Y) = -B(X,\theta Y)$ is positive definite; it exists and is unique up to conjugation by an inner automorphism. Its eigenspaces give the **Cartan decomposition** $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$, with $\mathrm{K}$ a subalgebra, $\mathrm{P}$ a $\mathrm{K}$-module, $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$, the two pieces orthogonal under $B$, and $B$ negative definite on $\mathrm{K}$ and positive definite on $\mathrm{P}$; the converse holds, a decomposition with these properties determines its involution. The subalgebra $\mathrm{K}$ is of compact type and maximal compactly embedded, its elements are elliptic and the elements of $\mathrm{P}$ are hyperbolic or zero. Globally the fixed subgroup $K$ is a **maximal compact subgroup**, every compact subgroup is conjugate into it, and the Cartan decomposition exponentiates to the polar decomposition $G = K\exp\mathrm{P}$, a diffeomorphism; hence $G$ is homotopy equivalent to $K$ and $G/K$ is diffeomorphic to the vector space $\mathrm{P}$. The quotient $G/K$ is the symmetric space of the pair, with the geodesic symmetries induced by $\theta$ and curvature $R(X,Y)Z = -[[X,Y],Z]$ on $\mathrm{P}$; its geometry and its compactifications are Part IV, and its harmonic analysis is the later articles of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B$ | the Killing form |
| $\theta$ | the Cartan involution |
| $B_\theta(X,Y) = -B(X,\theta Y)$ | the twisted form, positive definite |
| $\mathrm{G} = \mathrm{K}\oplus\mathrm{P}$ | the Cartan decomposition |
| $\mathrm{K}$ | the fixed subalgebra, of compact type, maximal compactly embedded |
| $\mathrm{P}$ | the complement, of non-compact type, a $\mathrm{K}$-module |
| $[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K}$, $[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}$, $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$ | the bracket relations |
| $K = G^{\Theta}$ | the maximal compact subgroup |
| $G = K\exp\mathrm{P}$ | the polar decomposition, a diffeomorphism |
| $G/K$ | the symmetric space |
| $R(X,Y)Z = -[[X,Y],Z]$ | the curvature at the base point |
| elliptic, hyperbolic, nilpotent | the types of an element |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the Cartan decomposition, the polar decomposition and the symmetric space.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the Cartan involution, the maximal compact subgroup and the structure of the real algebras.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume II (Wiley, 1969), for the symmetric spaces, the geodesic symmetries and the curvature.
- Ottmar Loos, *Symmetric Spaces*, Volume I (Benjamin, 1969), for the algebraic theory of the symmetric spaces and the Cartan decomposition.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the maximal compact subgroups, the polar decomposition and the compactly embedded subalgebras.
