# __The Quaternionic Product on the Quaternion Subspace__

## Introduction

The general quaternionic bilinear product $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ of *Introduction to the General Quaternionic Algebra of Quaternions* is defined on the whole four-dimensional real space $\mathbb{H}$, and the involution ${}^{\natural}$ splits that space into its two eigenspaces: the Hermitian one, which is the scalar line $S = \mathbb{R}e_0$, and the anti-Hermitian one, which is the vector subspace $V = \mathrm{Vect}(e_1,e_2,e_3)$ (*The Symmetrised Quaternionic Product and the Hermitian Subspace*). This article reads the product on those two **companion pieces**, identifies the restriction on $V$ with a product already known on the same space, records which piece is invariant and which is not, and compares the restriction with the one that the plain product gives on the same pieces.

The outcome is short. On the scalar line the quaternionic product is the plain product of the scalars. On the vector subspace it is the **negative** of the plain product of the two pure quaternions: the pure part of the restriction is the negative of the cross product, and the scalar part is the Euclidean pairing. The scalar line is invariant; the vector subspace is **not**, and it is invariant exactly on the orthogonal pairs. The two pieces act on one another by scaling. The restriction to $V$ is the negative of the plain restriction to $V$, and the two differ by a sign and by nothing else.

Over $\mathbb{R}$ the whole space is already the quaternion space, so its role is played by the largest proper subspace the involution singles out, the vector subspace $V$, of real dimension three; the four-dimensional complex subspace of that chapter has no analogue here, and the contrast is the last section of the article.

## The Two Companion Pieces

**Definition.** The **scalar line** and the **vector subspace** of $\mathbb{H}$ are

$$
S = \mathbb{R}e_0 = \{\tilde p : \tilde p^{\natural} = \tilde p\} , \qquad V = \mathrm{Vect}(e_1,e_2,e_3) = \mathbb{R}^3 = \{\tilde p : \tilde p^{\natural} = -\tilde p\} .
$$

They are the two eigenspaces of the conjugation, of real dimensions one and three, and $\mathbb{H} = S \oplus V$ with the decomposition $\tilde p = p_0e_0 + \vec p$.

**Proposition (the mixed products).** The scalar line acts on the vector subspace by scaling, on both sides:

$$
(p_0e_0) \star \vec q = p_0\vec q , \qquad \vec p \star (q_0e_0) = -q_0\vec p .
$$

*Proof.* $e_0^{\natural} = e_0$ and $\vec q^{\natural} = -\vec q$, so $(p_0e_0)^{\natural}\vec q = p_0\vec q$ and $\vec p^{\natural}(q_0e_0) = -q_0\vec p$.

**Corollary.** Both mixed products lie again in $V$, with the scalar coefficient on the left and the negated scalar coefficient on the right; the scalar line therefore acts on $V$ by the two opposite scalings, and the asymmetry is the same conjugation that makes the unit one-sided.

## The Restriction to the Vector Subspace

**Theorem (the restriction).** For pure elements $\vec p, \vec q \in V$,

$$
\vec p \star \vec q = \vec p^{\natural}\vec q = -\vec p\vec q = \bigl(\vec p \cdot \vec q\bigr)e_0 - \vec p \times \vec q .
$$

The restriction of the quaternionic product to the vector subspace is therefore the **negative of the plain product** of the two pure quaternions; its value lies in $S \oplus V$, its scalar part is the Euclidean pairing, and its pure part is the negative of the cross product.

*Proof.* For a pure element $\vec p^{\natural} = -\vec p$, so $\vec p \star \vec q = -\vec p\vec q$; the plain product of two pure quaternions is $\vec p\vec q = -\,\vec p \cdot \vec q + \vec p \times \vec q$, and the sign is reversed.

**Corollary (the identification).** The restriction is the difference of the two plain companion operations on $V$: the scalar part is the symmetrised plain product, $\tfrac12(\vec p\vec q + \vec q\vec p) = \vec p \cdot \vec q$, and the pure part is the antisymmetrised one, $\tfrac12(\vec p\vec q - \vec q\vec p) = \vec p \times \vec q$. The quaternionic product on $V$ is thus the symmetrised product minus the antisymmetrised one, the plain product read with the conjugation inserted in the first slot, and the insertion of the conjugation on a pure first factor is exactly a negation.

**Example.** At $\vec p = \vec q = e_1$ the value is $e_0$; at $\vec p = e_1$, $\vec q = e_2$ the value is $-e_3$; at $\vec p = e_1$, $\vec q = -e_1$ the value is $e_0$. The first and the third values are in the scalar line, the second in the vector subspace, and the reading is the Euclidean pairing and the negative cross product of the two vectors.

## The Invariance

**Theorem (which piece is invariant).** The scalar line $S$ is invariant under the quaternionic product, and on it the product is the plain multiplication of the scalars: $(p_0e_0) \star (q_0e_0) = p_0q_0e_0$. The vector subspace $V$ is **not** invariant: for pure $\vec p, \vec q \neq 0$ the value $\vec p \star \vec q$ lies in $V$ exactly when $\vec p \cdot \vec q = 0$, and then it is $-\vec p \times \vec q$. The mixed products lie in $V$.

*Proof.* The scalar line statement is the mixed product at two scalars. The vector statement is the restriction theorem: the scalar part of $\vec p \star \vec q$ is $\vec p \cdot \vec q$, which vanishes exactly on the orthogonal pairs; in that case the value is the pure element $-\vec p \times \vec q$, also nonzero on non-parallel pairs.

**Corollary.** The product mixes the two pieces in one direction only: $S \star S \subseteq S$, $S \star V \subseteq V$, $V \star S \subseteq V$, while $V \star V$ meets both pieces. The scalar line is the unique proper invariant subspace, of dimension one; the vector subspace is a three-dimensional piece stable under the mixing but not closed.

*Proof.* The three inclusions are the two propositions above; the failure of closure of $V$ is the exact condition $\vec p \cdot \vec q = 0$.

**Remark.** The scalar line is invariant for the symmetrised product as well, and the vector subspace is not closed for it either, the value being the scalar $\vec p \cdot \vec q e_0$ (*The Symmetrised Quaternionic Product and the Hermitian Subspace*). The failure of closure of $V$ is thus common to the two companion operations, and it is the algebraic reason the corpus gives only two remarkable subspaces and not more.

## The Comparison with the Plain Product

**Proposition.** The restriction of the plain product to the two pieces is the negative of the restriction of the quaternionic product, on both pieces read together: on $S$ the two agree, $(p_0e_0)(q_0e_0) = p_0q_0e_0$, while on $V$ they differ by the sign of the conjugate, $\vec p\vec q = -\vec p \star \vec q$. In particular the plain pure part of the restriction is $+\vec p \times \vec q$ against the $-\vec p \times \vec q$ of the quaternionic product, and the plain scalar part is $-\vec p \cdot \vec q$ against $+\vec p \cdot \vec q$.

*Proof.* The plain product of two pure quaternions is $\vec p\vec q = -\,\vec p \cdot \vec q + \vec p \times \vec q$, and the quaternionic one is its negative by the restriction theorem.

**Remark.** The pattern of invariance is the same for the two products on the scalar line and the same on the vector subspace, and only the signs differ; the two products are exchanged by the conjugation, $\vec q \star \vec p = (\vec p \star \vec q)^{\natural}$, and on a pair of pure elements the conjugation is the negation, which is the whole of the comparison. The general comparison of the two products, with the whole table of their laws, is *Comparison Between the Two General Products*.

## Summary

The conjugation splits $\mathbb{H}$ into the scalar line $S$ and the vector subspace $V$, the two companion pieces of the block. On $S$ the quaternionic product is the plain product of the scalars and $S$ is invariant; on $V$ it is the negative of the plain product of pure quaternions, $\vec p \star \vec q = -\vec p\vec q = (\vec p \cdot \vec q)e_0 - \vec p \times \vec q$, so that the value is the Euclidean pairing in the scalar line and the negative cross product in the vector subspace; $V$ is therefore not invariant, and it is invariant exactly on the orthogonal pairs. The mixed products lie in $V$ and act by the two opposite scalings. Compared with the plain product on the same pieces the only difference is a sign, the two products being exchanged by the conjugation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H} = S \oplus V$ | the splitting into the two eigenspaces of the conjugation |
| $S = \mathbb{R}e_0$ | the scalar line, the Hermitian subspace, dimension one |
| $V = \mathrm{Vect}(e_1,e_2,e_3)$ | the vector subspace, the anti-Hermitian subspace, dimension three |
| $\vec p \star \vec q = -\vec p\vec q$ | the restriction to the vector subspace |
| $\vec p \cdot \vec q$ | the Euclidean pairing, the scalar part of the restriction |
| $\vec p \times \vec q$ | the cross product, the negative of the pure part |
| $\tilde p\tilde q$ | the plain product, whose restriction to $V$ is the negative |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the subalgebra generated by a subspace and the invariance of a piece under a product.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the symmetric and antisymmetric parts of a bilinear product and their readings on a subspace.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the pure quaternions, the cross product and the Euclidean pairing.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the eigenspaces of an involution and the products they carry.
