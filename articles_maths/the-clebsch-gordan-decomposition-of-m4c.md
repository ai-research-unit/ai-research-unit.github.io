# __The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$__

## Introduction

**The subject.** The algebra of order four is the tensor square of its own spin module, and the tensor square of the module of label $\tfrac32$ decomposes into four irreducible pieces of labels $3,2,1,0$. The article proves the identification, computes the four summands with their dimensions, and expresses the projectors as polynomials in the Casimir.

**The order of the article.** The first section identifies the algebra with $V\otimes V^{*}$ and then with $V\otimes V$. The second applies the Clebsch–Gordan rule and counts dimensions. The third checks the result on weights. The fourth records the Casimir spectrum and the projectors. The fifth states the general rule at order $n$ and draws the boundary with the articles on the individual carriers.

**It assumes** *The Four Weights of the Module and the Half Angle at $n=4$* for the weight basis and *The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$* for the copy. The row at order two is *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*.

**The result in one line.** $M_4(\mathbb{C})\cong V_{3/2}\otimes V_{3/2}\cong V_3\oplus V_2\oplus V_1\oplus V_0$ with dimensions $7+5+3+1=16$, each summand occurring once.

**Boundaries.** The article proves the decomposition and computes the Casimir; it does not describe the individual carriers in detail, which is the business of the four articles on $V_3,V_2,V_1,V_0$. It does not treat the product of two carriers, which is not a carrier and is the subject of *The Truncated Rule*.

## The Algebra as a Tensor Square

**Proposition.** For every finite-dimensional $V$ there is a canonical isomorphism $\operatorname{End}(V)\cong V\otimes V^{*}$, and under it the conjugation action of $G$ on $\operatorname{End}(V)$ becomes the action on $V\otimes V^{*}$.

*Proof.* The map sends $u\otimes\lambda$ to the operator $x\mapsto\lambda(x)u$; it is bilinear and has the right dimension. Conjugation by $\rho(g)$ sends $\lambda(x)u$ to $(\lambda\circ\rho(g)^{-1})(x)\,\rho(g)u$, which is the tensor action.

**Corollary.** At $n=4$ one has $M_4(\mathbb{C})\cong V\otimes V^{*}$ with $V=V_{3/2}$.

*Proof.* $V$ is the defining module of the copy and $\operatorname{End}(V)=M_4(\mathbb{C})$.

**Proposition.** $V^{*}\cong V$ as modules of the copy, through the invariant Hermitian form, so that $M_4(\mathbb{C})\cong V\otimes V$.

*Proof.* The module carries a positive definite invariant form, since the copy is compact and the module is irreducible; the form identifies $V$ with its dual and is invariant, hence equivariant.

**Corollary.** The conjugation action on the algebra is the tensor product of the module with itself.

*Proof.* The two propositions composed.

## The Rule

**Theorem.** $V_{3/2}\otimes V_{3/2}\cong V_3\oplus V_2\oplus V_1\oplus V_0$, each summand occurring exactly once, with complex dimensions $7,5,3,1$.

*Proof.* The Clebsch–Gordan rule for $SU(2)$ states that $V_j\otimes V_k=\bigoplus_{m=|j-k|}^{j+k}V_m$ with each $m$ occurring once. With $j=k=\tfrac32$ the labels run over $3,2,1,0$. The dimensions are $2m+1$ for $m=3,2,1,0$, and their sum is $7+5+3+1=16=\dim M_4(\mathbb{C})$, which checks the count.

**Corollary.** The algebra splits into four irreducible invariant subspaces of complex dimensions $7,5,3,1$ and real dimensions $14,10,6,2$.

*Proof.* The theorem, and the real dimension of a complex space of dimension $d$ is $2d$.

**Corollary.** The traceless part is $V_3\oplus V_2\oplus V_1$, of dimension $15$, and the centre is $V_0$.

*Proof.* The trace is invariant and vanishes on the three summands of dimension $7,5,3$; the scalars are the one-dimensional invariant subspace on which the trace does not vanish.

**Corollary.** The four labels are $0,1,2,3$: three integers below the label of the module and one equal to nothing in the module.

*Proof.* The labels displayed in the theorem; the module has label $\tfrac32$, which is not among them.

## The Check on Weights

**Proposition.** The weights of $V\otimes V$ are the sixteen sums $m+m'$ of two weights of $V$, and their multiset is

$$
3,\;2,\;1,\;0,\;0,\;-1,\;-2,\;-3
$$

together with $2,\;1,\;0,\;-1,\;-2$ and $1,\;0,\;-1$ and $0$.

*Proof.* The weights of $V$ are $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$; the sums of two of them are $3$ (once), $2$ (twice), $1$ (three times), $0$ (four times), and symmetrically. Reading the multiset $3,2,2,1,1,1,0,0,0,0,-1,-1,-1,-2,-2,-3$ as the strings $3,2,1,0,-1,-2,-3$; $2,1,0,-1,-2$; $1,0,-1$; $0$ gives the four carriers.

**Corollary.** The multiset of weights of the algebra is $0^{4},\pm1^{3},\pm2^{2},\pm3$, and the four strings read from the top are exactly the four labels $3,2,1,0$.

*Proof.* The proposition, counted by multiplicity.

**Corollary.** The decomposition is visible in the weights alone: the highest weight $3$ occurs once, so exactly one summand of label $3$ is present; after removing its string the next highest weight $2$ occurs twice, one of which belongs to the same summand, and so on.

*Proof.* The strings of $V_3,V_2,V_1,V_0$ contain $3$ once, $2$ once, $1$ once, $0$ once at their tops, and the remaining copies are accounted for by the lower members.

## The Casimir and the Projectors

**Definition.** The **Casimir element** of the copy acting on the algebra is $C=-\sum_{i}\operatorname{ad}_{J_i}^{2}$, where $J_1,J_2,J_3$ are the three Hermitian generators.

**Proposition.** $C$ acts on the summand of label $k$ by the scalar $k(k+1)$, so its spectrum on the algebra is $0,2,6,12$ with multiplicities $1,3,5,7$, computed to a residual of order $10^{-15}$.

*Proof.* The Casimir of $\mathfrak{su}_2$ acts on the irreducible module of highest weight $k$ by $k(k+1)$; the multiplicities are the dimensions $2k+1$. The numerical diagonalisation of the sixteen-by-sixteen matrix $C$ gives the four eigenvalues with the stated multiplicities.

**Corollary.** The four summands are the eigenspaces of $C$, and each is the range of the Lagrange projector

$$
\Pi_k=\prod_{l\neq k}\frac{C-l(l+1)}{k(k+1)-l(l+1)},\qquad k=0,1,2,3,
$$

which is idempotent, Hermitian, and of trace $2k+1$.

*Proof.* A polynomial in $C$ acts on the eigenspace of eigenvalue $k(k+1)$ by the value at that point; the Lagrange polynomial with value one there and zero at the other three eigenvalues gives the projector. The trace is the dimension of the range.

**Corollary.** The four projectors sum to the identity and are mutually orthogonal, and their traces sum to $1+3+5+7=16$.

*Proof.* The Lagrange polynomials sum to one on the spectrum, and the ranges are the eigenspaces.

**The numerical check.** Applying $\Pi_k$ to a random element of the algebra and then applying the Casimir reproduces the element multiplied by $k(k+1)$ to a residual of order $10^{-15}$, and the composition $\Pi_k\Pi_l$ vanishes for $k\neq l$ to the same order.

*Proof.* The two matrices are polynomials in one matrix, so they commute and act diagonally in the same basis.

## The General Rule

**Proposition.** At order $n$ the module is $V_{(n-1)/2}$ and the algebra is $\bigoplus_{k=0}^{n-1}V_k$, with $\sum_{k=0}^{n-1}(2k+1)=n^{2}$.

*Proof.* The tensor square of $V_j$ with $2j=n-1$ decomposes into the labels $0,1,\dots,2j=n-1$, and the dimensions sum to $n^{2}$, which is the dimension of the algebra.

**Corollary.** At $n=2$ the decomposition is $V_1\oplus V_0$ of dimensions $3+1=4$; at $n=3$ it is $V_2\oplus V_1\oplus V_0$ of dimensions $5+3+1=9$; at $n=4$ it is the four summands of the theorem.

*Proof.* The proposition at the three orders.

**Corollary.** The number of summands is $n$ and the labels are $0,\dots,n-1$; the module's label is $\tfrac{n-1}{2}$, which is a summand label exactly when $n$ is odd.

*Proof.* The labels displayed; $\tfrac{n-1}{2}$ is an integer exactly for odd $n$.

## The Boundary

**Against the carriers.** The four summands are the four carriers, and each has its own article: *The Spin-Three Carrier*, *Introduction to the Spin-Two Carrier*, *The Spin-One Carrier* and *The Spin-Zero Carrier*. The present article proves that the list is complete and that each occurs once.

**Against the product of carriers.** The product of two summands is not a summand; it is a subspace whose projection on the summands is computed in *The Truncated Rule: the Product of Two Carriers Is Not a Carrier*. The decomposition is a decomposition of the space and not of the algebra as an algebra.

**Against the module.** The module has label $\tfrac32$ and appears in the algebra only as a minimal left ideal, not as a summand, as *Where the Half-Integers Go in $M_4(\mathbb{C})$* explains.

## Summary

The algebra is $\operatorname{End}(V)\cong V\otimes V^{*}\cong V\otimes V$ with $V=V_{3/2}$, and the Clebsch–Gordan rule for the tensor square of the label $\tfrac32$ gives $V_3\oplus V_2\oplus V_1\oplus V_0$ with dimensions $7+5+3+1=16$, each summand once. The traceless part is the sum of the first three, of dimension fifteen, and the centre is the last.

The weights of the algebra are the sixteen sums of two weights of the module, with multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$, and the four strings read from the top are the four labels. The Casimir acts by $k(k+1)$, with spectrum $0,2,6,12$ and multiplicities $1,3,5,7$; the projectors are the Lagrange polynomials in the Casimir, and they are idempotent, Hermitian, orthogonal and of traces $1,3,5,7$.

At order $n$ the decomposition is $\bigoplus_{k=0}^{n-1}V_k$ with $\sum(2k+1)=n^{2}$, and the module's label is a summand label exactly when $n$ is odd.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=V_{3/2}$ | the module, complex dimension four |
| $V_k$ | the carrier of label $k$, dimension $2k+1$ |
| $C=-\sum_i\operatorname{ad}_{J_i}^{2}$ | the Casimir of the conjugation action |
| $\Pi_k$ | the projector onto the carrier of label $k$ |
| $0^{4},\pm1^{3},\pm2^{2},\pm3$ | the weight multiset of the algebra |
| $n^{2}$ | the sum of the dimensions |

## Further Reading

- [The Spin Decomposition of $M_4(\mathbb{C})$: Four Carriers and the Weight Multiset](the-spin-decomposition-of-m4c.html), for the weight strings.
- [The Four Weights of the Module and the Half Angle at $n=4$](the-four-weights-of-the-module-and-the-half-angle-at-n-4.html), for the weights of the module.
- [The Truncated Rule: the Product of Two Carriers Is Not a Carrier](the-truncated-rule-the-product-of-two-carriers-at-n-4.html), for the product.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the row at order two.
- [Where the Half-Integers Go in $M_4(\mathbb{C})$](where-the-half-integers-go-in-m4c.html), for the label $\tfrac32$.
