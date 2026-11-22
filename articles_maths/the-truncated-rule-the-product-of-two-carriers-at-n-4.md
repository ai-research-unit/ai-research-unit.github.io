# __The Truncated Rule: the Product of Two Carriers Is Not a Carrier__

## Introduction

**The subject.** Each carrier is a subspace of the algebra, and two carriers can be multiplied element by element. The product is again an invariant subspace, because conjugation is an automorphism, but it is not a carrier: it is a sum of several, and the sum is cut off at label $3$.

**The order of the article.** The first section proves that the product of two invariant subspaces is invariant, and explains why this does not make it a carrier. The second states the truncation: the Clebsch–Gordan sum stops at $2j=3$ because the algebra has no carrier above $3$. The third works out the products of the four carriers with themselves and with each other. The fourth proves that no carrier except the centre is closed under multiplication. The fifth draws the boundary with the ideals.

**It assumes** *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the four summands, and *The Spin Decomposition of $M_4(\mathbb{C})$* for the labels. The row at order two is *The Truncated Rule: the Product of Two Carriers*.

**The result in one line.** $V_kV_l$ is a sum of carriers with labels between $|k-l|$ and $k+l$, truncated at $3$, and it is strictly smaller than that truncated sum in general; the only carrier closed under multiplication is $V_0$.

**Boundaries.** The article treats the product of two carriers as a subspace; it does not treat the product of an arbitrary pair of elements, which is the algebra multiplication itself, and it does not treat one-sided multiplication by the whole algebra, which is the theory of ideals.

## The Product Is Invariant

**Definition.** For two subspaces $U,W$ of the algebra let $UW$ be the span of the products $uw$ with $u\in U$ and $w\in W$.

**Proposition.** If $U$ and $W$ are invariant under the conjugation action of the copy, then $UW$ is invariant.

*Proof.* For $q$ in the copy, $\Phi_q(uw)=\Phi_q(u)\Phi_q(w)$, since $\Phi_q$ is an algebra automorphism. The right side lies in $UW$ because $\Phi_q(u)\in U$ and $\Phi_q(w)\in W$. Hence the whole span is carried into itself.

**Corollary.** The product of two carriers is a sum of carriers.

*Proof.* It is invariant and the algebra is the direct sum of its four irreducible invariant subspaces.

**The point of the article.** Invariance is not irreducibility. The product of two carriers is invariant, and it is a carrier only when the sum of labels happens to have one term; in every other case it splits, and the article computes the splitting.

*Proof.* A direct sum of two nonzero carriers is not irreducible.

## The Truncation

**Proposition.** If $U\subseteq V_k$ and $W\subseteq V_l$, then $UW\subseteq\bigoplus_{m\le k+l}V_m$, and since the only labels present are $0,1,2,3$, the sum is truncated at $3$.

*Proof.* The product map $V_k\otimes V_l\to M_4(\mathbb{C})$ is equivariant, so its image is a quotient of the tensor product; by Clebsch–Gordan the tensor product is the sum of the $V_m$ with $|k-l|\le m\le k+l$, and only those $m\le3$ can appear as summands of the algebra.

**Corollary.** $V_kV_l\subseteq\bigoplus_{m=|k-l|}^{\min(k+l,3)}V_m$.

*Proof.* The proposition, together with the lower bound $|k-l|$ of the Clebsch–Gordan rule.

**Corollary.** The truncated sum is $\bigoplus_{m\le3}V_m$, which is the whole algebra, so the truncation gives no information when $k+l\ge3$; it does give information when $k+l\le3$.

*Proof.* The algebra is the sum of the four carriers, and the four labels are $0,1,2,3$.

**The strict inequality.** The product can be strictly smaller than the truncated sum: $V_1V_3$ has dimension twelve, while the truncated sum $V_2\oplus V_3$ has dimension $5+7=12$ and the untruncated sum would add $V_4$, which does not exist; and $V_2V_2$ has dimension eleven, while the truncated sum $V_0\oplus V_1\oplus V_2\oplus V_3$ has dimension sixteen.

*Proof.* The dimensions are computed by projecting the span of the products onto the four carriers; the residuals of the projection are of order $10^{-15}$.

## The Products Computed

**Proposition.** The products of the carriers are, up to equality of the spans,

$$
V_0V_0=V_0,\qquad V_0V_k=V_k,\qquad V_1V_1=V_0\oplus V_1\oplus V_2,
$$

$$
V_1V_2=V_1\oplus V_2\oplus V_3,\qquad V_1V_3=V_2\oplus V_3,
$$

$$
V_2V_2=V_0\oplus V_1\oplus V_3,\qquad V_2V_3=V_1\oplus V_2\oplus V_3,\qquad V_3V_3=M_4(\mathbb{C}).
$$

*Proof.* Each product is invariant, so it is the sum of the carriers on which its projections do not vanish; computing the rank of the projection of a spanning set of products onto each carrier gives the dimensions $1,3,5,7$ for the carriers that occur and zero for those that do not. The five identity products are read off from the same computation.

**Corollary.** The dimensions are $1$, $3$, $5$, $7$, $9$, $12$, $11$, $15$ and $16$ for the products displayed in the order written.

*Proof.* The dimensions of the summands: $V_1V_1$ has $1+3+5=9$, $V_1V_2$ has $3+5+7=15$, $V_1V_3$ has $5+7=12$, $V_2V_2$ has $1+3+7=11$, $V_2V_3$ has $3+5+7=15$, $V_3V_3$ has $16$.

**Corollary.** The four cases named in the menu are $V_3^{2}=M_4(\mathbb{C})$, of dimension sixteen; $V_2V_1=V_1\oplus V_2\oplus V_3$, of dimension fifteen; $V_0^{2}=V_0$, of dimension one; and $V_0V_k=V_k$.

*Proof.* The proposition.

**The reading of $V_2V_2$.** The product of the middle carrier with itself contains the centre, the triplet and the top carrier, and misses the middle carrier: the label $2$ does not appear in the product of two labels $2$.

*Proof.* The projection of $V_2V_2$ onto $V_2$ vanishes to the stated order.

## No Carrier Is a Subalgebra

**Proposition.** $V_0$ is closed under multiplication; $V_1$, $V_2$ and $V_3$ are not.

*Proof.* $V_0$ consists of the scalars, and the product of two scalars is a scalar. For $V_1$: it contains the raising operator $J_+$, and $J_+^{2}$ has weight $2$, so it is not in $V_1$, whose weights are $1,0,-1$. For $V_2$: $V_2V_2$ contains $V_0$ and $V_3$, so it is not contained in $V_2$. For $V_3$: $V_3V_3$ is the whole algebra, which contains $V_0$.

**Corollary.** None of the four carriers except the centre is a subalgebra, and the algebra is not the direct sum of its carriers as an algebra.

*Proof.* The proposition, and a direct sum of subalgebras would be closed under multiplication.

**Corollary.** The product with the centre is the only associative case: $V_0V_k=V_k$ and $V_kV_0=V_k$ for every $k$.

*Proof.* The scalars commute with everything, and the product of a scalar with an element of $V_k$ stays in $V_k$.

**The reading.** A carrier is an invariant subspace and not an ideal and not a subalgebra. The three notions coincide only for the scalars, and the coincidence is the reason the centre is the one carrier that behaves like a piece of the algebra.

## The Boundary

**Against the ideals.** A minimal left ideal $M_4P$ is closed under multiplication by the whole algebra on the left, which is a stronger property than closure under its own products. The carriers are closed under the action of the copy and not under multiplication by the algebra, so the two families of subspaces are different in kind.

**Against the Clebsch–Gordan article.** That article decomposes the space; this one multiplies in it. The tensor rule gives the candidates for the product, and the computation shows which candidates occur.

**Against the modules.** The product of two carriers is a subspace of the algebra, and its dimension is at most sixteen. The product of two modules is not defined inside the algebra, since the module is not a subalgebra; the tensor square is the algebra itself.

## Summary

The product of two invariant subspaces is invariant, because conjugation is an automorphism, so the product of two carriers is a sum of carriers. The Clebsch–Gordan labels of the product run from $|k-l|$ to $k+l$ and are truncated at $3$, the top label of the algebra.

The products are $V_0V_k=V_k$, $V_1^{2}=V_0\oplus V_1\oplus V_2$, $V_1V_2=V_1\oplus V_2\oplus V_3$, $V_1V_3=V_2\oplus V_3$, $V_2^{2}=V_0\oplus V_1\oplus V_3$, $V_2V_3=V_1\oplus V_2\oplus V_3$ and $V_3^{2}=M_4(\mathbb{C})$, with dimensions $9,15,12,11,15,16$. The product can be strictly smaller than the truncated sum, as $V_2^{2}$ shows.

$V_0$ is the only carrier closed under multiplication; $V_1$ fails because $J_+^{2}$ has weight $2$, $V_2$ fails because its square contains the scalars and the top carrier, and $V_3$ fails because its square is the whole algebra. The product with the centre is the only associative case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UW$ | the span of the products $uw$ |
| $V_k$ | the carrier of label $k$ |
| $V_0=\mathbb{C}\mathrm I$ | the centre |
| $J_+$ | the raising operator, of weight $1$ |
| $2j=3$ | the top label, at which the rule truncates |

## Further Reading

- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the four summands.
- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module-at-n-4.html), for the squares of the module.
- [The Minimal Left Ideals of $M_4(\mathbb{C})$ and the Module $V_{3/2}$](the-minimal-left-ideals-of-m4c.html), for the ideals.
- [The Truncated Rule: the Product of Two Carriers](the-truncated-rule-the-product-of-two-carriers.html), for the row at order two.
- [The Spin-Zero Carrier of $M_4(\mathbb{C})$: the Scalars](the-spin-zero-carrier-of-m4c.html), for the carrier that is a subalgebra.
