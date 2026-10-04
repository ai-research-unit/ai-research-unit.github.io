# __The Six Subspaces and the Lie Algebra__

## Introduction

The biquaternion algebra is associative, and its product splits into a symmetric and an antisymmetric part. The antisymmetric part is the **commutator**

$$
[\tilde{P},\tilde{Q}] = \tilde{P}\tilde{Q} - \tilde{Q}\tilde{P} , \qquad \tilde{P}\tilde{Q} = \tilde{P} \circ \tilde{Q} + \tfrac{1}{2}[\tilde{P},\tilde{Q}] .
$$

The commutator is bilinear, alternating and satisfies the Jacobi identity, so the algebra is a Lie algebra under it; the Jacobi identity is inherited from the associativity of the product and is not proved again here. This article records, for each ordered pair of the six distinguished subspaces, the real span of all brackets of an element of the first with an element of the second, and identifies the Lie subalgebras among the six. The symmetric half is *The Six Subspaces and the Jordan Algebra*, and the full product is *The Six Subspaces and the Products*.

The six subspaces are those of *Introduction to the Six Subspaces*. The blocks $B_1 = \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ and $B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ are the two vector blocks of *Comparison of the Six Subspaces*.

Everything follows from one computation. Because the scalar and vector parts multiply according to the scalar–vector formula and the scalar part of a product is symmetric in the two factors, the commutator kills the scalar parts:

$$
[\tilde{P},\tilde{Q}] = 2\,\mathbf{P} \times \mathbf{Q} ,
$$

where $\mathbf{P}$ and $\mathbf{Q}$ are the vector parts. **The commutator of two elements is twice the complex cross product of their vector parts, and is therefore a pure vector.** Three consequences follow at once. First $[\mathbb{B},\mathbb{B}] = \mathrm{Vect}(\mathbb{B})$, since the cross products of complex vectors span the whole of the vector subspace. Second the centre of the Lie algebra is $\mathbb{C}_{\mathbb{B}}$, since the vector part of an element that brackets to zero with every element must vanish. Third, the Lie algebra is the direct sum

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})
$$

of the two-dimensional abelian Lie algebra $\mathbb{C}_{\mathbb{B}}$ and the six-dimensional Lie algebra $\mathrm{Vect}(\mathbb{B})$, since $\mathbb{C}_{\mathbb{B}}$ is central, $\mathrm{Vect}(\mathbb{B})$ is a Lie subalgebra, and the two meet in the origin.

The vector part of each of the six is one of the four blocks, or zero, or all of them:

| subspace | vector part |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $0$ |
| $\mathrm{Vect}(\mathbb{B})$ | $B_1 \oplus B_2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $B_1$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $B_2$ |
| $\mathbb{M}_+$ | $B_2$ |
| $\mathbb{M}_-$ | $B_1$ |

The cross product of two complex vectors in the blocks $B_1, B_2$ lands according to

$$
B_1 \times B_1 = B_1 , \qquad B_1 \times B_2 = B_2 , \qquad B_2 \times B_1 = B_2 , \qquad B_2 \times B_2 = B_1 ,
$$

the last because $i^2 = -1$. Combining the two tables gives the whole bracket, tabulated below by the real span. The entry is written $0$ when the bracket vanishes.

| $[\cdot,\cdot]$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $\mathrm{Vect}(\mathbb{B})$ | $0$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathrm{Vect}(\mathbb{B})$ |
| $\mathbb{H}_{\mathbb{B}}$ | $0$ | $\mathrm{Vect}(\mathbb{B})$ | $B_1$ | $B_2$ | $B_2$ | $B_1$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $0$ | $\mathrm{Vect}(\mathbb{B})$ | $B_2$ | $B_1$ | $B_1$ | $B_2$ |
| $\mathbb{M}_+$ | $0$ | $\mathrm{Vect}(\mathbb{B})$ | $B_2$ | $B_1$ | $B_1$ | $B_2$ |
| $\mathbb{M}_-$ | $0$ | $\mathrm{Vect}(\mathbb{B})$ | $B_1$ | $B_2$ | $B_2$ | $B_1$ |

Two features of the table are worth naming. It is **antisymmetric**: the entry in the row of $U$ and the column of $V$ equals the entry in the row of $V$ and the column of $U$, which is the alternating property of the bracket. And **it is blind to the distinction between $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_-$ on the one hand and between $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ on the other**: those two pairs share the same rows and the same columns, precisely because the bracket reads only the vector part, which is $B_1$ for both members of the first pair and $B_2$ for both members of the second. The commutator of two elements of the algebra therefore carries less information about the six than the product does.

**Theorem.** Exactly three of the six distinguished subspaces are Lie subalgebras, namely the centre, the vector subspace and the anti-Hermitian subspace:

$$
[\mathbb{C}_{\mathbb{B}},\mathbb{C}_{\mathbb{B}}] = 0 , \qquad [\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})] = \mathrm{Vect}(\mathbb{B}) , \qquad [\mathbb{M}_-,\mathbb{M}_-] = B_1 \subseteq \mathbb{M}_- .
$$

**Proof.** The three are read from the diagonal of the table. The other three diagonal entries leave the subspace: $[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}] = B_1$, $[i\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}}] = B_1$ and $[\mathbb{M}_+,\mathbb{M}_+] = B_1$, and $B_1$ is contained in $\mathbb{H}_{\mathbb{B}}$ and in $\mathbb{M}_-$ but in neither $i\mathbb{H}_{\mathbb{B}}$ nor $\mathbb{M}_+$, while it is contained in the vector subspace. The centre and the vector subspace are therefore Lie subalgebras, and the anti-Hermitian subspace is one because $B_1$ lies inside it; the quaternion, anti-quaternion and Hermitian subspaces are not.

## The Centre Subspace

A central element brackets to zero with everything, because it commutes with everything:

$$
[\mathbb{C}_{\mathbb{B}}, \mathbb{B}] = 0 .
$$

The centre of the Lie algebra is exactly $\mathbb{C}_{\mathbb{B}}$: an element brackets to zero with every element only if its vector part vanishes, and every central element does. The associative centre and the Lie centre are therefore the same subspace, and it is one of the six. The centre is an abelian Lie subalgebra, and it is the first of the three.

## The Vector Subspace

The bracket of two pure vectors is twice their cross product,

$$
[\mathbf{P},\mathbf{Q}] = 2\,\mathbf{P} \times \mathbf{Q} ,
$$

so the vector subspace is closed under it and the cross products span the whole subspace:

$$
[\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})] = \mathrm{Vect}(\mathbb{B}) .
$$

The vector subspace is the **derived subalgebra** of the algebra, $[\mathbb{B},\mathbb{B}] = \mathrm{Vect}(\mathbb{B})$, and it is **perfect**, being equal to its own derived subalgebra. It is the largest of the three Lie subalgebras of the theorem and the only one that is not commutative. With the centre the bracket vanishes, and with each of the other four it is again the whole vector subspace: the vector subspace brackets onto itself with everything outside the centre, so the whole bracket of the algebra is carried by it.

## The Quaternion Subspace

The bracket of two real quaternions is twice the real cross product of their vector parts:

$$
[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}] = B_1 .
$$

The quaternion subspace is therefore not a Lie subalgebra; its bracket lands in the real vector triple $B_1$, which is a Lie subalgebra of the vector subspace, being closed under the cross product as the cross product of real vectors. With the anti-quaternion subspace the bracket is the imaginary vector triple,

$$
[\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}] = B_2 ,
$$

and with the two Hermitian subspaces it is $B_2$ with $\mathbb{M}_+$ and $B_1$ with $\mathbb{M}_-$. With the centre it vanishes and with the vector subspace it is the vector subspace. The row of the quaternion subspace is the same as the row of the anti-Hermitian subspace, since both have vector part $B_1$.

## The Anti-Quaternion Subspace

The anti-quaternion subspace is not a Lie subalgebra either, and the bracket of two of its elements lands in the *other* vector block:

$$
[i\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}] = B_1 .
$$

The reason is the sign $i^2 = -1$: the vector part of an element of $i\mathbb{H}_{\mathbb{B}}$ lies in $B_2$, and the cross product of two vectors of $B_2$ lies in $B_1$. An element and its partner therefore have their bracket in the real vector triple, even though neither has any real vector part. With the quaternion subspace the bracket is $B_2$, with the anti-Hermitian subspace also $B_2$, with the Hermitian subspace $B_1$, with the centre it vanishes, and with the vector subspace it is the vector subspace. The row of the anti-quaternion subspace is the same as the row of the Hermitian subspace, since both have vector part $B_2$.

## The Hermitian Subspace

The vector part of a Hermitian element is imaginary, so the bracket of two Hermitian elements is twice the cross product of two vectors of $B_2$:

$$
[\mathbb{M}_+,\mathbb{M}_+] = B_1 .
$$

The Hermitian subspace is therefore not a Lie subalgebra: the bracket of two Hermitian elements is a **real** pure vector, and in particular a real element, whereas the Hermitian elements with a real vector part are the anti-Hermitian ones. The bracket pairs the two sectors the other way round, and

$$
[\mathbb{M}_+,\mathbb{M}_-] = B_2 \subseteq \mathbb{M}_+ ,
$$

so the bracket of a Hermitian with an anti-Hermitian element is an imaginary pure vector and does lie in the Hermitian subspace. With the centre the bracket vanishes and with the vector subspace it is the vector subspace.

## The Anti-Hermitian Subspace

The vector part of an anti-Hermitian element is real, so the bracket of two of them stays in the real vector triple:

$$
[\mathbb{M}_-,\mathbb{M}_-] = B_1 \subseteq \mathbb{M}_- .
$$

The anti-Hermitian subspace is a Lie subalgebra, the third of the three. Its derived subalgebra is $B_1$, the real vector triple, and the central imaginary unit spans its centre, since $[\mathbb{C}_{\mathbb{B}},\mathbb{B}] = 0$ and an element of $\mathbb{M}_-$ with vanishing vector part is a multiple of $ie_0$. The Lie algebra is therefore the direct sum

$$
\mathbb{M}_- = \mathbb{R}(ie_0) \oplus B_1
$$

of a one-dimensional abelian Lie algebra and the real vector triple. With the Hermitian subspace the bracket is $B_2$, with the quaternion and anti-quaternion subspaces it is $B_1$ and $B_2$ respectively, with the centre it vanishes and with the vector subspace it is the vector subspace.

## Summary

The commutator of two biquaternions is twice the complex cross product of their vector parts, and is always a pure vector. Hence the derived subalgebra of the algebra is the vector subspace, $[\mathbb{B},\mathbb{B}] = \mathrm{Vect}(\mathbb{B})$; the centre of the Lie algebra is the centre of the algebra, the two-dimensional abelian $\mathbb{C}_{\mathbb{B}}$; and the algebra is the direct sum $\mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ of the abelian centre and the six-dimensional vector subspace as Lie algebras. Exactly three of the six distinguished subspaces are Lie subalgebras: the centre, the vector subspace and the anti-Hermitian subspace, the last because the bracket of two of its elements is a real pure vector, which lies inside it. The vector subspace is perfect, being equal to its own derived subalgebra. The quaternion, anti-quaternion and Hermitian subspaces are not closed: each has bracket with itself the real vector triple $B_1$. Because the bracket sees only the vector parts, and the vector parts of the six are the four blocks $0$, $B_1$, $B_2$ and $B_1 \oplus B_2$, the bracket cannot tell the quaternion subspace from the anti-Hermitian one, nor the anti-quaternion subspace from the Hermitian one: the table is two-to-one on those two pairs. The symmetric half of the product is *The Six Subspaces and the Jordan Algebra*; the Lie theory of the whole algebra — its ideals, its derivations and its relation to the classical Lie algebras — is the business of the Lie theory articles.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $B_1, B_2$ | the real and imaginary vector triples $\operatorname{span}\{e_1,e_2,e_3\}$, $\operatorname{span}\{ie_1,ie_2,ie_3\}$ |
| $[\tilde{P},\tilde{Q}]$ | the commutator $\tilde{P}\tilde{Q} - \tilde{Q}\tilde{P}$ |
| $\mathbf{P} \times \mathbf{Q}$ | the complex cross product of the vector parts |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the blocks and the intersections
- *The Six Subspaces and the Products* (`articles_maths/the-six-subspaces-and-the-products.md`), for the full product and the two halves into which it splits
- *The Six Subspaces and the Jordan Algebra* (`articles_maths/the-six-subspaces-and-the-jordan-algebra.md`), for the symmetric half of the product
- *Biquaternion Lie Algebra* (`articles_maths/biquaternion-lie-algebra.md`), for the Jacobi identity, the derived series and the Lie structure of the whole algebra
