# __The Truncated Rule: the Product of Two Carriers Is Not a Carrier__

## Introduction

**The subject.** The four carriers are the invariant subspaces of the operator space, and the operator space is also an algebra. The article asks what the product of two carriers is, and answers that it is never a carrier except in the trivial cases: the product falls into a sum of carriers, and the sum is the truncation of a Clebsch–Gordan series to the four labels that exist. The scalars are the only carrier closed under the product.

**The order of the article.** The product rule and its table come first; the failure of closure second. The truncation follows, then the scalars, and the filtered reading closes the article.

**It assumes** *The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$*, *The Two-Sided Operators and the Segre Cone* and *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*. **The row of the elements is** where the carriers are the two summands of a four-dimensional algebra and the product rule is the rule of the quaternion units; here there are four carriers and no closure.

**The result in one line.** $V_iV_j\subseteq\bigoplus_{k=|i-j|}^{\min(i+j,3)}V_k$, the sum has more than one term except when one label is zero, and only $V_0$ is a subalgebra.

**Boundaries.** The decomposition is *The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$*; the two squares are *The Parity Rule*; the algebra structure of the operators is *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*.

## The Product Rule

**Theorem.** For two carriers,
$$
V_i\,V_j\subseteq\bigoplus_{k=|i-j|}^{\min(i+j,3)}V_k .
$$

*Proof.* The product of two operators is the composition, which in the identification of the operator space with the tensor square contracts one factor; the labels that can occur in the product are those of the Clebsch–Gordan series of $i\otimes j$, namely $|i-j|,\dots,i+j$, and only the labels present in the space, that is those at most three, survive.

**Corollary.** The series is truncated at the top: the terms of label greater than three are absent from the space and their content is redistributed by the projection onto the four carriers.

*Proof.* The space has no carrier above three, so the higher terms of the series have nowhere to go.

**Corollary.** The product of two carriers is a carrier only when the interval $[|i-j|,\min(i+j,3)]$ is a single point, which happens exactly when one of the labels is zero.

*Proof.* The interval has one element exactly when $|i-j|=\min(i+j,3)$; with non-negative labels this forces one label to vanish.

**The reading.** The product rule is the Clebsch–Gordan rule read on the algebra, and the truncation is the statement that the operator space is finite. The four carriers are the terms of one sum, and the product of two terms is a sum of terms, not a term.

## The Table

**Proposition.** The sixteen products $V_iV_j$ are contained in the following sums, with the labels read on the rows and on the columns:
$$
\begin{array}{c|cccc}
 & V_0 & V_1 & V_2 & V_3\\ \hline
V_0 & V_0 & V_1 & V_2 & V_3\\
V_1 & V_1 & V_0\oplus V_1\oplus V_2 & V_1\oplus V_2\oplus V_3 & V_2\oplus V_3\\
V_2 & V_2 & V_1\oplus V_2\oplus V_3 & V_0\oplus V_1\oplus V_2\oplus V_3 & V_1\oplus V_2\oplus V_3\\
V_3 & V_3 & V_2\oplus V_3 & V_1\oplus V_2\oplus V_3 & V_0\oplus V_1\oplus V_2\oplus V_3
\end{array}
$$

*Proof.* The rule of the theorem applied to each pair, the interval being truncated at three.

**Corollary.** The table is symmetric, since the product of two subspaces does not depend on the order of the factors.

*Proof.* The entries are computed from the unordered pair of labels.

**Corollary.** The diagonal entries are the sums of carriers of both parities, except the first, which is a single carrier.

*Proof.* The intervals for $i=j=1,2,3$ contain zero and an odd label.

**The reading.** The table is the algebra structure at the level of the carriers: sixteen entries, four of them single carriers, twelve of them sums. The entries of the first row and the first column are single because the scalars act on each carrier without moving it.

## The Failure of Closure

**Theorem.** No carrier except the scalars is closed under the product, and no sum of two carriers except $V_0\oplus V_1$ is closed under the product.

*Proof.* For the square of $V_1$ the rule gives $V_0\oplus V_1\oplus V_2$, which contains the carrier $V_2$ outside $V_1$; the same for labels two and three, whose squares contain a carrier of the other parity. For a sum $V_i\oplus V_j$ with $j\ge1$, the square of $V_j$ contains a carrier outside the sum, unless $j=1$ and the sum contains zero and one, in which case the product lands in the sum.

**Corollary.** The sum $V_0\oplus V_1$ is a subalgebra, of dimension four, and it is the only subalgebra of the form a sum of carriers with more than one term.

*Proof.* The entry for $V_1V_1$ is contained in the sum, and every other pair of labels in the sum is contained in it as well.

**Corollary.** The scalars are a subalgebra, and the carrier $V_1$ is not, although the square of a generator of $V_1$ stays inside $V_0\oplus V_1\oplus V_2$.

*Proof.* The square of a generator of the copy is a combination of a scalar, a generator and a component of label two.

**The reading.** Being a carrier is a property of the action; being a subalgebra is a property of the product. The two lists agree only at the scalars and at the four-dimensional sum, and this is the whole content of the failure.

## The Truncation and the Filter

**Proposition.** The truncation defines a filtration of the operator algebra, the subspaces $F_k=V_0\oplus\dots\oplus V_k$ being nested and closed under the product up to the top.

*Proof.* The product of an element of $F_i$ with one of $F_j$ lands in the carriers up to $i+j$, truncated at three, so $F_iF_j\subseteq F_{\min(i+j,3)}$.

**Corollary.** The filtration has the four steps $F_0\subset F_1\subset F_2\subset F_3$ of dimensions $1,4,9,16$, and the associated graded pieces are the four carriers.

*Proof.* The dimensions of the sums, and the definition of the filtration.

**Corollary.** The scalars are the only piece of the filtration that is a two-sided ideal in the associated graded sense, and the top piece is the whole algebra.

*Proof.* The product rule, read on the graded pieces.

**The reading.** The truncation is not an accident of the table: it is a filtration, and the filtration is the algebraic shadow of the truncation of the Clebsch–Gordan series. The carriers are the graded pieces, and the product lowers the degree at most to the sum, never above the top.

## Further Reading

- [The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$](the-clebsch-gordan-decomposition-of-the-biquaternion-operators.html), for the four carriers.
- [$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation](end-b-as-an-algebra-the-regular-representation.html), for the product that is truncated.
- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module.html), for the other decomposition of the sixteen.
- [The Copy Acting on Sixteen Dimensions](the-copy-acting-on-sixteen-dimensions.html), for the action and the loss of the algebra structure.
