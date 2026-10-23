# __The Symmetrised Quaternionic Product and the Hermitian Subspace__

## Introduction

The **symmetrised quaternionic product** is the commutative companion of the general quaternionic bilinear product $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$ of *Introduction to the General Quaternionic Algebra*:

$$
\tilde q_1 \bullet \tilde q_2 = \tfrac12\bigl(\tilde q_1 \star \tilde q_2 + \tilde q_2 \star \tilde q_1\bigr) .
$$

It is the symmetrisation of the general quaternionic product, and the commutative scalar-valued rule it defines is not a structure of this category: this article collects what the category keeps of it, the hermitian subspace and the trace form, and cites nothing further.

The reading is short because of one property: the symmetrisation of the quaternionic product is not only commutative but **central-valued**, its value being a real multiple of $e_t$. The symmetrised product is therefore the quaternion form of the space, the Euclidean inner product of $\mathbb{R}^4$, read as a product. It has no unit, it is not associative, and it fails the Jordan identity; and the two subspaces that the conjugation singles out — the scalar line and the vector subspace — are its two natural blocks, because over $\mathbb{R}$ there is **one** nontrivial involution and not two, so there are two eigenspaces and not four.

## The Symmetrised Product

**Definition.** The **symmetrised quaternionic product** of $\tilde q_1,\tilde q_2 \in \mathbb{H}$ is $\tilde q_1 \bullet \tilde q_2 = \tfrac12(\tilde q_1 \star \tilde q_2 + \tilde q_2 \star \tilde q_1)$.

**Theorem (the central value).** For all $\tilde q_1,\tilde q_2 \in \mathbb{H}$,

$$
\boxed{\;\tilde q_1 \bullet \tilde q_2 = \beta(\tilde q_1,\tilde q_2)\,e_t , \qquad \beta(\tilde q_1,\tilde q_2) = q_{1t}q_{2t} + \vec q_1 \cdot \vec q_2\;}.
$$

The product is $\mathbb{R}$-bilinear, commutative, and its values lie in the scalar line.

*Proof.* The two summands are $\tilde q_1^{\natural}\tilde q_2$ and $\tilde q_2^{\natural}\tilde q_1$, of vector parts $q_{1t}\vec q_2 - q_{2t}\vec q_1 - \vec q_1 \times \vec q_2$ and $q_{2t}\vec q_1 - q_{1t}\vec q_2 - \vec q_2 \times \vec q_1$; the cross products are opposite by antisymmetry and cancel in the half-sum, the two copies of $q_{1t}\vec q_2 - q_{2t}\vec q_1$ cancel too, and the scalar parts add to $2\beta(\tilde q_1,\tilde q_2)$.

**Corollary (the quaternion form).** The symmetrised product is the quaternion form of the space read as a product: $\beta$ is the symmetric bilinear form whose diagonal is the quaternionic bilinear algebraic norm, $\beta(\tilde q,\tilde q) = \langle\tilde q\rangle_{\natural}$ (*The 2 Forms over the Quaternioid $\mathbb{R}$ Space*). It is positive definite and non-degenerate.

**Proposition (no unit, not associative, not Jordan).** The symmetrised product has no unit: $e_t \bullet \tilde q = q_te_t$, which differs from $\tilde q$ as soon as the vector part is nonzero. It is not associative: at $(\tilde q_1,\tilde q_2,\tilde q_3) = (\vec e_x,\vec e_x,e_t)$ the two readings are $(\tilde q_1 \bullet \tilde q_2) \bullet \tilde q_3 = e_t \bullet e_t = e_t$ and $\tilde q_1 \bullet (\tilde q_2 \bullet \tilde q_3) = \vec e_x \bullet 0 = 0$. It fails the Jordan identity; at $\tilde q_1 = \tilde q_2 = \vec e_x$ the two sides of

$$
(\tilde q_1 \bullet \tilde q_2) \bullet \tilde q_1^{\bullet 2} = \tilde q_1 \bullet \bigl(\tilde q_2 \bullet \tilde q_1^{\bullet 2}\bigr) , \qquad \tilde q_1^{\bullet 2} = \tilde q_1 \bullet \tilde q_1 ,
$$

are $(\vec e_x \bullet \vec e_x) \bullet e_t = e_t \bullet e_t = e_t$ on the left and $\vec e_x \bullet (\vec e_x \bullet e_t) = \vec e_x \bullet 0 = 0$ on the right.

*Proof.* The unit statement is the definition of the product at $e_t$. In the associativity example $\vec e_x \bullet \vec e_x = \langle \vec e_x\rangle_{\natural}e_t = e_t$ and $\vec e_x \bullet e_t = \beta(\vec e_x,e_t)e_t = 0$. The Jordan computation uses again $\vec e_x^{\bullet 2} = e_t$, so the left side is $e_t \bullet e_t = e_t$ and the right side is $\vec e_x \bullet 0 = 0$. The failure of the Jordan identity forbids every Jordan-theoretic statement for the symmetrisation, and it is the failure that the ternary product of the preceding article linearises (*The Associator and the Ternary Product of the Quaternionic Product*).

## The Hermitian Subspace

**Definition.** The **Hermitian subspace** and the **anti-Hermitian subspace** of the conjugation ${}^{\natural}$ are

$$
\mathbb{M}_+ = \{\tilde q \in \mathbb{H} : \tilde q^{\natural} = \tilde q\} , \qquad \mathbb{M}_- = \{\tilde q \in \mathbb{H} : \tilde q^{\natural} = -\tilde q\} .
$$

**Theorem (the two subspaces).** $\mathbb{M}_+$ is the scalar line $\mathbb{R}e_t$, of real dimension one; $\mathbb{M}_-$ is the vector subspace $\mathrm{Vect}(\vec e_x,\vec e_y,\vec e_z)$, of real dimension three. They are the two eigenspaces of the conjugation and they give the splitting

$$
\boxed{\;\mathbb{H} = \mathbb{M}_+ \oplus \mathbb{M}_- , \qquad \tilde q = q_te_t + \vec q\;},
$$

the scalar part being Hermitian and the vector part anti-Hermitian.

*Proof.* The conjugation acts by $q_te_t + \vec q \mapsto q_te_t - \vec q$, so its fixed subspace is the scalar line and its negated one the vector subspace; an involution of a real vector space splits the space into its two eigenspaces.

Over $\mathbb{R}$ the scalar sector has **no** nontrivial involution — the bar is the identity by the conventions of the corpus — so ${}^{\natural}$ is the only involution at hand, it has two eigenspaces, and the four-subspace lattice collapses to two. The subspace and its companion are therefore the scalar line and the vector subspace, and no other.

## Positivity on the Hermitian Subspace

**Theorem (positivity).** The symmetrised product is positive definite: $\tilde q \bullet \tilde q = \langle\tilde q\rangle_{\natural}e_t$, which is a non-negative multiple of $e_t$ vanishing only at $\tilde q = 0$. On the Hermitian subspace it reads $\tilde q_1 \bullet \tilde q_2 = q_{1t}q_{2t}e_t$, positive definite there; on the anti-Hermitian subspace it reads $\tilde q_1 \bullet \tilde q_2 = (\vec q_1 \cdot \vec q_2)e_t$, also positive definite there. The two subspaces are orthogonal for the form, $\beta(\mathbb{M}_+,\mathbb{M}_-) = 0$.

*Proof.* On the scalar line $\vec q_1 = \vec q_2 = 0$, so $\beta = q_{1t}q_{2t}$; on the vector subspace $q_{1t} = q_{2t} = 0$, so $\beta = \vec q_1 \cdot \vec q_2$; the mixed value has $q_{1t} = 0$ or $q_{2t} = 0$ together with the corresponding vector part zero, so it vanishes.

Definiteness removes the indefinite companion, but it does not remove the zero divisors of the symmetrisation, which lie in the orthogonal pairs: $\tilde q_1 \bullet \tilde q_2 = \beta(\tilde q_1,\tilde q_2)e_t$ vanishes exactly on the pairs with $\beta(\tilde q_1,\tilde q_2) = 0$, and those pairs are abundant, $\vec e_x \bullet \vec e_y = 0$ for two orthogonal pure elements and $e_t \bullet \vec e_x = 0$ for a scalar and a vector. What definiteness removes is the zero divisor **against itself**: $\tilde q \bullet \tilde q = \langle\tilde q\rangle_{\natural}e_t$ never vanishes for $\tilde q \neq 0$, so the symmetrisation is anisotropic even though it has zero divisors. The contrast with the quaternionic product is exact: $\star$ has no zero divisor at all, while its symmetrisation has all the orthogonal pairs (*The Specificities of the General Quaternionic Algebra*, above this article in this category).

## Summary

The symmetrised quaternionic product $\tilde q_1 \bullet \tilde q_2 = \tfrac12(\tilde q_1 \star \tilde q_2 + \tilde q_2 \star \tilde q_1)$ is central-valued, $\beta(\tilde q_1,\tilde q_2)e_t$, $\mathbb{R}$-bilinear and commutative; it is the quaternion form of the space read as a product, it has no unit, it is not associative, and it fails the Jordan identity at $\tilde q_1 = \tilde q_2 = \vec e_x$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde q_1 \bullet \tilde q_2 = \tfrac12(\tilde q_1 \star \tilde q_2 + \tilde q_2 \star \tilde q_1)$ | the symmetrised quaternionic product |
| $\beta(\tilde q_1,\tilde q_2) = q_{1t}q_{2t} + \vec q_1 \cdot \vec q_2$ | the quaternion form, the central coefficient |
| $\mathbb{M}_+ = \{\tilde q : \tilde q^{\natural} = \tilde q\}$ | the Hermitian subspace, the scalar line $\mathbb{R}e_t$ |
| $\mathbb{M}_- = \{\tilde q : \tilde q^{\natural} = -\tilde q\}$ | the anti-Hermitian subspace, the vector subspace |
| $\langle\tilde q\rangle_{\natural} = \beta(\tilde q,\tilde q)$ | the quaternionic bilinear algebraic norm |
| $\tilde q^{\bullet 2} = \tilde q \bullet \tilde q$ | the square in the symmetrised product |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the symmetrisation of a bilinear product, the Jordan identity and the subspaces of an involution.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan triple identity and the quadratic representation.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the eigenspaces of an involution and the forms attached to them.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Euclidean inner product as a quaternion product.
