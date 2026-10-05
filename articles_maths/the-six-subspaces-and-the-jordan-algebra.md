# __The Six Subspaces and the Jordan Algebra__

## Introduction

The product of the biquaternion algebra splits into a symmetric and an antisymmetric part, and the symmetric part is the **symmetrized product**

$$
\tilde{P} \circ \tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P}) .
$$

Because the ambient algebra is associative, the symmetrized product satisfies the Jordan identity identically, so every subspace closed under it is a Jordan algebra in its own right. This article records, for each ordered pair of the six distinguished subspaces, the real span of the symmetrized products of an element of the first by an element of the second, and identifies which of the six are Jordan subalgebras. The full product is the subject of *The Six Subspaces and the Products*, and the antisymmetric half is the subject of *The Six Subspaces and the Lie Algebra*.

The six subspaces are those of *Introduction to the Six Subspaces*. As in the product article, an entry is written $\mathbb{B}$ when the span is the whole algebra.

| $\circ$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| $\mathbb{M}_+$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
| $\mathbb{M}_-$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |

The symmetrized table is tighter than the product table: exactly five of its thirty-six cells differ, and all five involve the vector subspace or the two Hermitian subspaces. The product of the vector subspace with itself spans the whole algebra, while its symmetrized product collapses to the centre; the product of two Hermitian elements, and the product of two anti-Hermitian elements, spans a seven-dimensional subspace each, while their symmetrized products are Hermitian; and the product of a Hermitian by an anti-Hermitian element spans a seven-dimensional subspace, while its symmetrized product is anti-Hermitian. In particular every entry of the symmetrized table is either one of the six subspaces or the whole algebra.

**Theorem.** Exactly three of the six subspaces are closed under the symmetrized product, namely the centre, the quaternion subspace and the Hermitian subspace:

$$
\mathbb{C}_{\mathbb{B}} \circ \mathbb{C}_{\mathbb{B}} = \mathbb{C}_{\mathbb{B}} , \qquad \mathbb{H}_{\mathbb{B}} \circ \mathbb{H}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}} , \qquad \mathbb{M}_+ \circ \mathbb{M}_+ = \mathbb{M}_+ .
$$

**Proof.** The three equalities are read from the diagonal of the table. The other three diagonal entries are not the subspace itself: $\mathrm{Vect}(\mathbb{B}) \circ \mathrm{Vect}(\mathbb{B}) = \mathbb{C}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}} \circ i\mathbb{H}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_- \circ \mathbb{M}_- = \mathbb{M}_+$. The three closed subspaces are therefore the only Jordan subalgebras among the six, and each inherits the Jordan identity from the ambient associative algebra.

The table also shows a gradation by the Hermitian decomposition. Writing $\mathbb{M}_+$ for the even and $\mathbb{M}_-$ for the odd part, two elements of the same part have a symmetrized product in $\mathbb{M}_+$ and two of opposite parts one in $\mathbb{M}_-$: the symmetrized product is $\mathbb{Z}/2$-graded with even part $\mathbb{M}_+$. The same gradation governs the full product, where it shows up as the real or purely imaginary scalar part, and is recorded in *The Six Subspaces and the Products*.

## The Centre Subspace

Central elements commute with every element, so the symmetrized product of a central element with anything is the ordinary product:

$$
(Ae_0) \circ \tilde{Q} = A\tilde{Q} .
$$

The row of the centre is therefore the row of the product table: $\mathbb{C}_{\mathbb{B}} \circ \mathbb{C}_{\mathbb{B}} = \mathbb{C}_{\mathbb{B}}$ and $\mathbb{C}_{\mathbb{B}} \circ \mathrm{Vect}(\mathbb{B}) = \mathrm{Vect}(\mathbb{B})$, while the symmetrized product with any of the other four spans $\mathbb{B}$.

The centre is a Jordan subalgebra for the trivial reason that it is a commutative associative subalgebra, so its symmetrized product is its product; it is a field. It is one of the three closed subspaces of the theorem above, and it is the smallest of them.

## The Vector Subspace

The symmetrized product of two pure vectors is the scalar–vector formula with the cross product cancelled by antisymmetry:

$$
\mathbf{P} \circ \mathbf{Q} = -(\mathbf{P},\mathbf{Q})e_0 .
$$

The **square** of a pure vector is therefore a scalar, $\mathbf{P} \circ \mathbf{P} = \mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$, and the subspace spanned is the centre alone:

$$
\mathrm{Vect}(\mathbb{B}) \circ \mathrm{Vect}(\mathbb{B}) = \mathbb{C}_{\mathbb{B}} .
$$

This is the sharpest contrast between the two parts of the product in the whole table: the same two elements that span the algebra under the product have their symmetrized product confined to the two-dimensional centre. The vector subspace is not a Jordan subalgebra, and the vanishing of $\mathbf{P} \circ \mathbf{P}$ is the algebraic fact behind the square-zero elements of the vector subspace, which are exactly its nonzero non-units in *The Six Subspaces and the Units*.

The symmetrized product with a central element stays in the vector subspace, and with each of the other four spans the algebra.

## The Quaternion Subspace

The quaternion subspace is closed under the symmetrized product, since it is closed under the product itself:

$$
\mathbb{H}_{\mathbb{B}} \circ \mathbb{H}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}} .
$$

It is a Jordan subalgebra, and the second of the three. Its symmetrized product is not its product: the quaternion subspace is not commutative, so $\tilde{P} \circ \tilde{Q}$ and $\tilde{P}\tilde{Q}$ differ by the commutator whenever the two elements do not commute. The Jordan structure obtained is the symmetrization of the real quaternion algebra, whose properties are those of *Biquaternion Jordan Algebras* restricted to real coefficients.

With the anti-quaternion subspace the symmetrized product stays in the anti-quaternion subspace, and with the centre, the vector subspace and the two Hermitian subspaces it spans the algebra.

## The Anti-Quaternion Subspace

The anti-quaternion subspace is not closed under the symmetrized product:

$$
i\mathbb{H}_{\mathbb{B}} \circ i\mathbb{H}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}} .
$$

The witness is the generator: $(ie_0) \circ (ie_0) = (ie_0)^2 = -e_0$, which is in the quaternion subspace. With the quaternion subspace the symmetrized product stays in the anti-quaternion subspace, so the quaternion decomposition is $\mathbb{Z}/2$-graded for the symmetrized product exactly as it is for the product:

$$
\mathbb{H}_{\mathbb{B}} \circ \mathbb{H}_{\mathbb{B}} \subseteq \mathbb{H}_{\mathbb{B}} , \qquad \mathbb{H}_{\mathbb{B}} \circ i\mathbb{H}_{\mathbb{B}} \subseteq i\mathbb{H}_{\mathbb{B}} , \qquad i\mathbb{H}_{\mathbb{B}} \circ \mathbb{H}_{\mathbb{B}} \subseteq i\mathbb{H}_{\mathbb{B}} , \qquad i\mathbb{H}_{\mathbb{B}} \circ i\mathbb{H}_{\mathbb{B}} \subseteq \mathbb{H}_{\mathbb{B}} .
$$

With the centre, the vector subspace and the two Hermitian subspaces the symmetrized product spans the algebra.

## The Hermitian Subspace

Write a Hermitian element as $a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector. As in *The Six Subspaces and the Products*, the product of two of them is $(a_0b_0 + (\mathbf{p},\mathbf{r}))e_0 - \mathbf{p} \times \mathbf{r} + i(a_0\mathbf{r} + b_0\mathbf{p})$, and the cross product is the antisymmetric part, so it cancels in the symmetrization:

$$
(a_0e_0 + i\mathbf{p}) \circ (b_0e_0 + i\mathbf{r}) = (a_0b_0 + (\mathbf{p},\mathbf{r}))e_0 + i(a_0\mathbf{r} + b_0\mathbf{p}) .
$$

Both terms of the result lie in the Hermitian subspace, the first in the block $A_1$ and the second in $B_2$:

$$
\mathbb{M}_+ \circ \mathbb{M}_+ = \mathbb{M}_+ .
$$

The Hermitian subspace is therefore a Jordan subalgebra, the third of the three, and the only one among the four four-dimensional subspaces. Its symmetrized product is the **Jordan product** of the algebra, and its scalar part $a_0b_0 + (\mathbf{p},\mathbf{r})$ is the restriction to $\mathbb{M}_+$ of the scalar pairing $\operatorname{Sc}(\tilde{P}\tilde{Q})$. The Hermitian subspace is closed under the commutator only into its complement; the product of a Hermitian by an anti-Hermitian element, symmetrized, stays in the anti-Hermitian subspace:

$$
\mathbb{M}_+ \circ \mathbb{M}_- = \mathbb{M}_- .
$$

With the centre, the vector subspace and the two quaternion subspaces the symmetrized product spans the algebra.

## The Anti-Hermitian Subspace

Write an anti-Hermitian element as $ib'_0e_0 + \mathbf{q}$ with $b'_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector. The symmetrized product of two of them keeps the scalar part and cancels the cross product in the vector part:

$$
(ib'_0e_0 + \mathbf{q}) \circ (ic'_0e_0 + \mathbf{r}) = (-b'_0c'_0 - (\mathbf{q},\mathbf{r}))e_0 + i(b'_0\mathbf{r} + c'_0\mathbf{q}) .
$$

The scalar part is real and the vector part imaginary, so the result is Hermitian and not anti-Hermitian:

$$
\mathbb{M}_- \circ \mathbb{M}_- = \mathbb{M}_+ .
$$

The anti-Hermitian subspace is therefore not a Jordan subalgebra, and the symmetrized product of two anti-Hermitian elements is always Hermitian. This is the sign reversal that distinguishes the two sectors: $\mathbb{M}_+$ is closed and $\mathbb{M}_-$ is not, although the two are exchanged by multiplication by the central imaginary unit. With a Hermitian element the symmetrized product stays in $\mathbb{M}_-$, and with the centre, the vector subspace and the two quaternion subspaces it spans the algebra.

## Summary

The symmetrized product $\tilde{P} \circ \tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P})$ restricted to the six subspaces is tabulated above, and it is tighter than the product. Exactly three of the six are closed under it and are therefore Jordan subalgebras: the centre, the quaternion subspace and the Hermitian subspace; the three witnesses of failure are $\mathrm{Vect}(\mathbb{B}) \circ \mathrm{Vect}(\mathbb{B}) = \mathbb{C}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}} \circ i\mathbb{H}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_- \circ \mathbb{M}_- = \mathbb{M}_+$. The symmetrized product of two pure vectors is always a scalar, the cross product of the product formula cancelling by antisymmetry, so the same two elements that span the algebra under the product have their symmetrized product confined to the centre. The Hermitian subspace is the natural home of the product, and its symmetrized product is the Jordan product, with scalar part the restriction of the scalar pairing of the algebra; the anti-Hermitian subspace is not closed, and the symmetrized product of two of its elements is Hermitian. The symmetrized product is $\mathbb{Z}/2$-graded by the Hermitian decomposition, with even part $\mathbb{M}_+$. The Jordan structure of the whole algebra, the Jordan identity, the trace form and the Peirce decomposition are *Biquaternion Jordan Algebras*; the antisymmetric half of the product is the subject of *The Six Subspaces and the Lie Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde{P} \circ \tilde{Q}$ | the symmetrized product $\tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P})$ |
| $(\mathbf{P},\mathbf{Q})$ | the complex dot product |
| $\operatorname{Sc}(\tilde{Q})$ | the scalar part, the coefficient of $e_0$ |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *The Six Subspaces and the Products* (`articles_maths/the-six-subspaces-and-the-products.md`), for the full product and the two parts into which it splits
- *Decomposition of the Biquaternion Complex Products* (`articles_maths/decomposition-of-the-biquaternion-complex-products.md`), for the symmetrized product in its original setting
- *Biquaternion Jordan Algebras* (`articles_maths/biquaternion-jordan-algebras.md`), for the Jordan identity, the trace form and the Jordan structure of the whole algebra
- *The Six Subspaces and the Idempotents and Projections* (`articles_maths/the-six-subspaces-and-the-idempotents-and-projections.md`), for the idempotents, which occur in exactly the Hermitian subspace and are the reason it is the nontrivial Jordan subalgebra among the six
