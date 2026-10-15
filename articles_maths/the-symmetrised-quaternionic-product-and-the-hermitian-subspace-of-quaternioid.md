# __The Symmetrised Quaternionic Product and the Hermitian Subspace__

## Introduction

The **symmetrised quaternionic product** is the commutative companion of the general quaternionic bilinear product $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ of *Introduction to the General Quaternionic Algebra of Quaternions*:

$$
\tilde p \bullet \tilde q = \tfrac12\bigl(\tilde p \star \tilde q + \tilde q \star \tilde p\bigr) .
$$

It is the multiplication of the symmetric quaternionic algebra of the chapter, and this article does **not** develop that block: the commutative scalar-valued algebra, its zero divisors, its specificities and its matrix models are the articles of *Quaternions as a Symmetric Quaternionic Algebra (SQA) over $\mathbb{R}$*, all below this article in this category, and the introduction of the block is *Introduction to the Symmetric Quaternionic Algebra of Quaternions*, below this article in this category.

The reading is short because of one property: the symmetrisation of the quaternionic product is not only commutative but **central-valued**, its value being a real multiple of $e_0$. The symmetrised product is therefore the quaternion form of the space, the Euclidean inner product of $\mathbb{R}^4$, read as a product. It has no unit, it is not associative, and it fails the Jordan identity; and the two subspaces that the conjugation singles out — the scalar line and the vector subspace — are its two natural blocks, because over $\mathbb{R}$ there is **one** nontrivial involution and not two, so there are two eigenspaces and not four.

## The Symmetrised Product

**Definition.** The **symmetrised quaternionic product** of $\tilde p,\tilde q \in \mathbb{H}$ is $\tilde p \bullet \tilde q = \tfrac12(\tilde p \star \tilde q + \tilde q \star \tilde p)$.

**Theorem (the central value).** For all $\tilde p,\tilde q \in \mathbb{H}$,

$$
\tilde p \bullet \tilde q = \beta(\tilde p,\tilde q)\,e_0 , \qquad \beta(\tilde p,\tilde q) = p_0q_0 + \vec p \cdot \vec q .
$$

The product is $\mathbb{R}$-bilinear, commutative, and its values lie in the scalar line.

*Proof.* The two summands are $\tilde p^{\natural}\tilde q$ and $\tilde q^{\natural}\tilde p$, of vector parts $p_0\vec q - q_0\vec p - \vec p \times \vec q$ and $q_0\vec p - p_0\vec q - \vec q \times \vec p$; the cross products are opposite by antisymmetry and cancel in the half-sum, the two copies of $p_0\vec q - q_0\vec p$ cancel too, and the scalar parts add to $2\beta(\tilde p,\tilde q)$.

**Corollary (the quaternion form).** The symmetrised product is the quaternion form of the space read as a product: $\beta$ is the symmetric bilinear form whose diagonal is the quaternionic bilinear algebraic norm, $\beta(\tilde p,\tilde p) = N(\tilde p)$ (*The 2 Forms over the Quaternion $\mathbb{R}$ Space*). It is positive definite and non-degenerate.

**Proposition (no unit, not associative, not Jordan).** The symmetrised product has no unit: $e_0 \bullet \tilde q = q_0e_0$, which differs from $\tilde q$ as soon as the vector part is nonzero. It is not associative: at $(\tilde p,\tilde q,\tilde r) = (e_1,e_1,e_0)$ the two readings are $(\tilde p \bullet \tilde q) \bullet \tilde r = e_0 \bullet e_0 = e_0$ and $\tilde p \bullet (\tilde q \bullet \tilde r) = e_1 \bullet 0 = 0$. It fails the Jordan identity; at $x = y = e_1$ the two sides of

$$
(x \bullet y) \bullet x^{\bullet 2} = x \bullet \bigl(y \bullet x^{\bullet 2}\bigr) , \qquad x^{\bullet 2} = x \bullet x ,
$$

are $(e_1 \bullet e_1) \bullet e_0 = e_0 \bullet e_0 = e_0$ on the left and $e_1 \bullet (e_1 \bullet e_0) = e_1 \bullet 0 = 0$ on the right.

*Proof.* The unit statement is the definition of the product at $e_0$. In the associativity example $e_1 \bullet e_1 = N(e_1)e_0 = e_0$ and $e_1 \bullet e_0 = \beta(e_1,e_0)e_0 = 0$. The Jordan computation uses again $e_1^{\bullet 2} = e_0$, so the left side is $e_0 \bullet e_0 = e_0$ and the right side is $e_1 \bullet 0 = 0$. The failure of the Jordan identity forbids every Jordan-theoretic statement for the symmetrisation, and it is the failure that the ternary product of the preceding article linearises (*The Associator and the Ternary Product of the Quaternionic Product*).

## The Hermitian Subspace

**Definition.** The **Hermitian subspace** and the **anti-Hermitian subspace** of the conjugation ${}^{\natural}$ are

$$
\mathbb{M}_+ = \{\tilde p \in \mathbb{H} : \tilde p^{\natural} = \tilde p\} , \qquad \mathbb{M}_- = \{\tilde p \in \mathbb{H} : \tilde p^{\natural} = -\tilde p\} .
$$

**Theorem (the two subspaces).** $\mathbb{M}_+$ is the scalar line $\mathbb{R}e_0$, of real dimension one; $\mathbb{M}_-$ is the vector subspace $\mathrm{Vect}(e_1,e_2,e_3)$, of real dimension three. They are the two eigenspaces of the conjugation and they give the splitting

$$
\mathbb{H} = \mathbb{M}_+ \oplus \mathbb{M}_- , \qquad \tilde p = p_0e_0 + \vec p ,
$$

the scalar part being Hermitian and the vector part anti-Hermitian.

*Proof.* The conjugation acts by $p_0e_0 + \vec p \mapsto p_0e_0 - \vec p$, so its fixed subspace is the scalar line and its negated one the vector subspace; an involution of a real vector space splits the space into its two eigenspaces.

Over $\mathbb{R}$ the scalar sector has **no** nontrivial involution — the bar is the identity by the conventions of the corpus — so ${}^{\natural}$ is the only involution at hand, it has two eigenspaces, and the four-subspace lattice collapses to two. The subspace and its companion are therefore the scalar line and the vector subspace, and no other.

## Positivity on the Hermitian Subspace

**Theorem (positivity).** The symmetrised product is positive definite: $\tilde p \bullet \tilde p = N(\tilde p)e_0$, which is a non-negative multiple of $e_0$ vanishing only at $\tilde p = 0$. On the Hermitian subspace it reads $\tilde p \bullet \tilde q = p_0q_0e_0$, positive definite there; on the anti-Hermitian subspace it reads $\tilde p \bullet \tilde q = (\vec p \cdot \vec q)e_0$, also positive definite there. The two subspaces are orthogonal for the form, $\beta(\mathbb{M}_+,\mathbb{M}_-) = 0$.

*Proof.* On the scalar line $\vec p = \vec q = 0$, so $\beta = p_0q_0$; on the vector subspace $p_0 = q_0 = 0$, so $\beta = \vec p \cdot \vec q$; the mixed value has $p_0 = 0$ or $q_0 = 0$ together with the corresponding vector part zero, so it vanishes.

Definiteness removes the indefinite companion, but it does not remove the zero divisors of the symmetrisation, which lie in the orthogonal pairs: $\tilde p \bullet \tilde q = \beta(\tilde p,\tilde q)e_0$ vanishes exactly on the pairs with $\beta(\tilde p,\tilde q) = 0$, and those pairs are abundant, $e_1 \bullet e_2 = 0$ for two orthogonal pure elements and $e_0 \bullet e_1 = 0$ for a scalar and a vector. What definiteness removes is the zero divisor **against itself**: $\tilde p \bullet \tilde p = N(\tilde p)e_0$ never vanishes for $\tilde p \neq 0$, so the symmetrisation is anisotropic even though it has zero divisors. The contrast with the quaternionic product is exact: $\star$ has no zero divisor at all, while its symmetrisation has all the orthogonal pairs (*The Specificities of the General Quaternionic Algebra*, above this article in this category).

## Summary

The symmetrised quaternionic product $\tilde p \bullet \tilde q = \tfrac12(\tilde p \star \tilde q + \tilde q \star \tilde p)$ is central-valued, $\beta(\tilde p,\tilde q)e_0$, $\mathbb{R}$-bilinear and commutative; it is the quaternion form of the space read as a product, it has no unit, it is not associative, and it fails the Jordan identity at $x = y = e_1$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p \bullet \tilde q = \tfrac12(\tilde p \star \tilde q + \tilde q \star \tilde p)$ | the symmetrised quaternionic product |
| $\beta(\tilde p,\tilde q) = p_0q_0 + \vec p \cdot \vec q$ | the quaternion form, the central coefficient |
| $\mathbb{M}_+ = \{\tilde p : \tilde p^{\natural} = \tilde p\}$ | the Hermitian subspace, the scalar line $\mathbb{R}e_0$ |
| $\mathbb{M}_- = \{\tilde p : \tilde p^{\natural} = -\tilde p\}$ | the anti-Hermitian subspace, the vector subspace |
| $N(\tilde p) = \beta(\tilde p,\tilde p)$ | the quaternionic bilinear algebraic norm |
| $x^{\bullet 2} = x \bullet x$ | the square in the symmetrised product |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the symmetrisation of a bilinear product, the Jordan identity and the subspaces of an involution.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan triple identity and the quadratic representation.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the eigenspaces of an involution and the forms attached to them.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Euclidean inner product as a quaternion product.
