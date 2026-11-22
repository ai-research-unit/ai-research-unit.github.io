# __The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$__

## Introduction

**The subject.** The operator space is the tensor square of the module, and the tensor square of the highest weight $\tfrac32$ decomposes into four summands of labels three, two, one and zero. The article proves the rule, computes the dimensions, identifies the highest weight of each summand, checks the multiplicity one, and reads the four summands as the four carriers of the space. It also compares the rule with the rule of the row of the elements.

**The order of the article.** The tensor square and the rule come first; the highest weights and the dimensions second. The multiplicity one follows, then the four carriers, and the comparison closes the article.

**It assumes** *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*, *The Four Weights of the Module and the Half Angle* and *The Spin Decomposition: Four Carriers and the Weight Multiset*. **The row of the elements is** where the rule is $\tfrac12\otimes\tfrac12=V_1\oplus V_0$; here the same rule is applied to the doubled label and produces four summands.

**The result in one line.** $\tfrac32\otimes\tfrac32=V_3\oplus V_2\oplus V_1\oplus V_0$ with dimensions $7+5+3+1=16$, each summand occurring once, so the decomposition is canonical.

**Boundaries.** The weight multiset of the sixteen is *The Spin Decomposition: Four Carriers and the Weight Multiset*; the products of the carriers are *The Truncated Rule: the Product of Two Carriers Is Not a Carrier*; the squares of the module are *The Parity Rule*.

## The Tensor Square

**Theorem.** The operator algebra, as a module for the copy by left multiplication on the first factor and right multiplication on the second, is the tensor square of the module:
$$
\operatorname{End}(\mathbb{B})=\mathbb{B}\otimes\mathbb{B}^{*}\cong V_{3/2}\otimes V_{3/2},
$$
the last isomorphism by the self-duality of the module.

*Proof.* The operators are the linear maps of the module into itself, and the space of linear maps is the tensor product of the module with its dual; the module is self-dual, so the dual is the module again.

**Corollary.** The dimension of the operator space is the square of the dimension of the module, $16=4\cdot4$.

*Proof.* The tensor product of two four-dimensional spaces.

**Corollary.** The weights of the operator space are the sums of a weight and the negative of a weight of the module, that is, the sixteen differences.

*Proof.* The weight of a tensor product is the sum of the weights of the factors, and the dual carries the negative weights.

**The reading.** The operator space is the square of the module, and its weights are the differences of the weights of the module. Everything below follows from that single identification.

## The Rule

**Theorem.** The tensor square decomposes as
$$
V_{3/2}\otimes V_{3/2}=V_3\oplus V_2\oplus V_1\oplus V_0,
$$
where $V_k$ is the simple module of label $k$, and the four summands have complex dimensions $7,5,3,1$.

*Proof.* The Clebsch–Gordan rule for the tensor square of the highest weight $j$ reads $V_j\otimes V_j=\bigoplus_{k=0}^{2j}V_k$, each summand once; with $j=\tfrac32$ the labels are $3,2,1,0$. The dimension of $V_k$ is $2k+1$, giving $7,5,3,1$.

**Corollary.** The dimensions sum to sixteen, and the count is the check of the rule at this row.

*Proof.* $7+5+3+1=16$, the dimension of the tensor square.

**Corollary.** No further summand occurs, since a fifth simple module would raise the dimension above sixteen.

*Proof.* The smallest unused label would contribute at least one dimension, and the sum is already exact.

**The reading.** The rule is the addition of the weights: each summand of label $k$ has a highest weight $k$, obtained by adding two weights of the module. The four labels are all the integers from zero to three, and this is the arithmetic of the doubled string.

## The Highest Weights

**Proposition.** The highest weight of $V_k$ in the tensor square is the product of the highest weight vector of the module with the lowest weight vector, of total weight $k$, or the sum of two weights adding to $k$.

*Proof.* The highest weight of the tensor square is $\tfrac32+\tfrac32=3$, and the lowering steps produce the weights $2,1,0$ for the other summands, each realised by a pair of a weight and the negative of a weight.

**Corollary.** The four highest weight vectors are $s^{3}\otimes t^{3}$, $s^{3}\otimes s^{2}t$, $s^{3}\otimes st^{2}$ and $s^{3}\otimes s^{3}$ up to the choice of pairing.

*Proof.* The monomials of the module have the weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, and the pairings displayed give the four highest weights.

**Corollary.** The highest weight vector of each summand is annihilated by the raising operator of the diagonal copy.

*Proof.* A vector of highest weight is annihilated by the raising part of the diagonal copy by definition.

**The reading.** The four highest weights are read on four products of monomials, and their weights are three, two, one, zero. The lowest weight of the module, $t^{3}$, plays the role of the dual and is what makes the differences appear.

## The Multiplicity One

**Theorem.** Each summand occurs exactly once in the tensor square, so the decomposition is canonical and no choice of a projector is needed.

*Proof.* The Clebsch–Gordan rule for the square of one module gives each label at most once; the dimension count then forces exactness.

**Corollary.** The four summands are the eigenspaces of the Casimir operator with the four distinct eigenvalues $12,6,2,0$.

*Proof.* The Casimir acts on $V_k$ by $k(k+1)$, giving $12,6,2,0$; distinct eigenvalues give the eigenspaces directly.

**Corollary.** A canonical projector onto $V_k$ is the Lagrange interpolation of the Casimir at the value $k(k+1)$.

*Proof.* The interpolation polynomial in the Casimir is the identity on the eigenspace of that eigenvalue and zero on the other three.

**The reading.** Multiplicity one is what makes the decomposition usable: the summands are the eigenspaces of one operator, and the projectors are polynomials in it. No frame and no choice of basis enters.

## The Four Carriers and the Comparison

**Proposition.** The four summands are the carriers of the operator space: the top $V_3$ of dimension seven, then $V_2$ of dimension five, $V_1$ of dimension three and $V_0$ of dimension one.

*Proof.* The decomposition of the theorem, and the dimensions.

**Corollary.** The carrier $V_0$ is the scalars, and $V_1$ is the three-dimensional space of the traceless part of the diagonal action.

*Proof.* The label zero is the trivial module, spanned by the identity; the label one is the adjoint module of the copy.

**Corollary.** The rule of the row of the elements is $\tfrac12\otimes\tfrac12=V_1\oplus V_0$, with dimensions $3+1=4$, and the passage to the operators replaces each label $k$ by $2k$.

*Proof.* The same Clebsch–Gordan rule at $j=\tfrac12$, and the doubling of the label from the module to the tensor square of the module.

**The reading.** One rule, two rows, and the difference is the label of the module. The four carriers of the operators are the four terms of one sum, and the terms are distinguished by the Casimir alone.

## Further Reading

- [The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-the-principal-copy-and-the-kernel.html), for the module and the copy.
- [The Spin Decomposition: Four Carriers and the Weight Multiset](the-spin-decomposition-four-carriers-and-the-weight-multiset.html), for the weights of the sixteen.
- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module.html), for the split of the four carriers into the two squares.
- [The Truncated Rule: the Product of Two Carriers Is Not a Carrier](the-truncated-rule-the-product-of-two-carriers-is-not-a-carrier.html), for the failure of the carriers to be closed under the product.
