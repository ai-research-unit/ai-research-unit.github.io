# __Introduction to the Spin-Two Carrier: the Alternating Square__

## Introduction

**The subject.** The carrier of label two is the five-dimensional summand of the operator space that lies in the alternating square of the module. The article defines it without a frame, fixes its weight string, proves that it is of real type with five real dimensions, and explains why the label suggests symmetric tensors while the space is alternating.

**The order of the article.** The module and its alternating square come first; the weight string and the irreducibility follow. The reality type is settled next, then the relation between the label and the symmetry of the tensor, and the two readings close the article.

**It assumes** *The Clebsch–Gordan Decomposition of the Biquaternion Algebra* and *From the Spin to the Carriers and the Closures*. **The row of the elements is** where the two squares of a four-dimensional module are counted; there the alternating square is a line and the symmetric square is the traceless part of the algebra.

**The result in one line.** The carrier is
$$
V_2=\Lambda^{2}\mathcal M\big/\mathbb{C}\omega ,
$$
of complex dimension five and real dimension five, with weight string $2,1,0,-1,-2$, and it is the only one of the four carriers whose dimension is not one less than a power of two.

**Boundaries.** The form on the carrier is *The Spin-Two Carrier and the Trace Form*; its rank stratification is *The Spin-Two Carrier and the Rank Strata*; the two halves of the operator space, of which this carrier is one summand of the alternating half, are *The Symmetric and Antisymmetric Parts of the Operator Space*.

## The Module and Its Alternating Square

**Definition.** The **module** of the operator row is the carrier of the copy in which the sixteen is a square,
$$
\mathcal M=V_{3/2}=\operatorname{Sym}^{3}S,
$$
where $S$ is a minimal left ideal of the algebra, of complex dimension two. It has complex dimension four, and its weights at a Cartan generator of the copy are $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$.

The sixteen is the endomorphism space of this module, and as a module of the copy it is the square $\mathcal M\otimes\mathcal M$, the dual being identified with the module by the invariant form that the quaternionic structure supplies. The two squares of the module are the symmetric and the alternating part of that tensor square,
$$
\operatorname{Sym}^{2}\mathcal M=\operatorname{span}\{u\odot v\},\qquad
\Lambda^{2}\mathcal M=\operatorname{span}\{u\wedge v\},
$$
of complex dimensions ten and six.

**Proposition.** The weights of the Cartan generator on $\Lambda^{2}\mathcal M$ are
$$
2,\ 1,\ 0,\ 0,\ -1,\ -2 ,
$$
counted with multiplicity, so the alternating square carries the trivial label once.

*Proof.* The weights of an alternating product are the sums of two distinct weights of the module. The six unordered pairs of distinct weights give $\tfrac32+\tfrac12=2$, $\tfrac32-\tfrac12=1$, $\tfrac32-\tfrac32=0$, $\tfrac12-\tfrac12=0$, $\tfrac12-\tfrac32=-1$ and $-\tfrac12-\tfrac32=-2$. The value zero occurs twice, from the two pairs of opposite weights.

**Corollary.** The alternating square splits as $V_2\oplus V_0$, where $V_0$ is the line of the invariant alternating form $\omega$ of the module, and $V_2$ is the carrier of label two.

*Proof.* The summand of label zero has dimension one and is spanned by the highest vector of weight zero that is killed by the raising operator; that vector is the form $\omega$, which is invariant because the copy preserves it. Removing the line leaves the five weights $2,1,0,-1,-2$, simple and spaced by one.

**The reading.** One of the six dimensions of the alternating square is the form that the module carries by virtue of being quaternionic; the carrier is the traceless part that remains.

## The Weight String

**Proposition.** The five weight vectors of $V_2$ form a simple string spaced by one, so the carrier is irreducible, its highest weight is two, and its complex dimension is five.

*Proof.* The string is $2,1,0,-1,-2$ by the proposition above, with no repetition; consecutive values differ by one. A module whose string is simple and spaced by one is irreducible and has the largest value as its highest weight, since the ladder operators shift the weight by one and the string has no room for a second summand.

**Corollary.** The Casimir is the scalar six on the carrier, and the ladder coefficients are $\sqrt4,\sqrt6,\sqrt6,\sqrt4$ in the normalisation in which the weight vectors are of unit length.

*Proof.* On a carrier of label $k$ the Casimir is $k(k+1)$, and the coefficient at the step from $m$ to $m\pm1$ is the square root of $k(k+1)-m(m\pm1)$, which for $k=2$ gives the four values displayed.

**Corollary.** The carrier is the middle summand of the addition rule
$$
\tfrac32\otimes\tfrac32=V_3\oplus V_2\oplus V_1\oplus V_0,
$$
of dimensions $7+5+3+1=16$, and it is the only summand of dimension five.

*Proof.* The rule is the Clebsch–Gordan series for the copy, and the dimensions are $2k+1$ for $k=3,2,1,0$.

**The reading.** The string determines the carrier, and nothing in the description refers to the choice of the spinor space $S$. The carrier is attached to the operator row and not to a frame.

## The Reality of the Carrier

**Proposition.** The carrier is of real type. There is an antilinear involution $J_2$ of $V_2$ commuting with the copy and satisfying $J_2^{2}=+\mathrm I$, its fixed space has real dimension five, and on that space the invariant symmetric form of the carrier is real.

*Proof.* The Frobenius–Schur indicator of the carrier of label $k$ is $(-1)^{2k}$, which is $+1$ for $k=2$. An irreducible carrier with indicator $+1$ carries an invariant antilinear involution with square $+1$ and an invariant symmetric bilinear form, and the fixed space of such an involution is a real form of real dimension equal to the complex dimension.

**Corollary.** The carrier carries no invariant alternating form, and the module does.

*Proof.* An invariant alternating form on an irreducible carrier exists only when the carrier is self-dual with a skew pairing, which happens exactly for the half-integer labels. The module has label $\tfrac32$ and indicator $-1$; it is quaternionic, of real dimension eight, and it carries the form $\omega$ that the alternating square was built from.

**The reading.** The real dimension of the carrier equals its complex dimension, while the module doubles at every step and carries an alternating form instead of a symmetric one.

## The Label and the Symmetry of the Tensor

**Proposition.** The two squares of the module carry different labels:
$$
\operatorname{Sym}^{2}\mathcal M=V_3\oplus V_1,\qquad
\Lambda^{2}\mathcal M=V_2\oplus V_0,
$$
of dimensions $10=7+3$ and $6=5+1$.

*Proof.* The exchange of the two factors of $\mathcal M\otimes\mathcal M$ is an involution, and its fixed and negated parts are the two squares. The summands of the addition rule have labels $0,1,2,3$, and the exchange acts on the summand of label $k$ by the sign $(-1)^{k}$, as the parity of the number of factors shows. The even labels therefore lie in the symmetric square and the odd ones in the alternating square.

**Corollary.** The label two does not mean that the carrier consists of symmetric tensors of rank two; it means that the carrier has highest weight two, and the space in which it lives is the alternating square.

*Proof.* A symmetric tensor of rank two lives in $\operatorname{Sym}^{2}\mathcal M$, whose summands have labels three and one. The carrier of label two is a summand of $\Lambda^{2}\mathcal M$, and its elements are alternating tensors with the invariant form removed.

**The reading.** The analogy with traceless symmetric tensors is an analogy of labels only: the number two names the highest weight, and the tensor that carries it is alternating. The correction decides which square contains the carrier and therefore which form it inherits.

## The Two Readings

**Proposition.** The carrier occurs once in the principal reading of the sixteen and once in the conjugation reading.

*Proof.* In the principal reading the sixteen is $\tfrac32\otimes\tfrac32$ and the carrier is the summand of label two, which occurs once. In the conjugation reading the sixteen is the tensor square of the algebra read as $V_1\oplus V_0$, and
$$
(V_1\oplus V_0)\otimes(V_1\oplus V_0)=V_2\oplus 3V_1\oplus 2V_0,
$$
so the quintet occurs once there as well, as the top piece of $V_1\otimes V_1$.

**Corollary.** The two readings agree on the carrier and disagree on the multiplicities of the two lower labels.

*Proof.* The principal reading gives each of the four labels once, of dimensions $7+5+3+1$; the conjugation reading gives the quintet once, the triplet three times and the singlet twice, of dimensions $5+9+2$. Both sums are sixteen, and the labels of dimension one and three are the ones that repeat.

## The Middle Carrier

**Proposition.** The dimension five is the only carrier dimension of the row that is not one less than a power of two.

*Proof.* The four dimensions are $1,3,5,7$, and $1=2-1$, $3=4-1$, $7=8-1$, while $5$ is not of the form $2^{k}-1$ for any integer $k$.

**The reading.** The quintet is the middle carrier, and it is the one where the two descriptions of the row, by label and by tensor construction, are furthest apart. It is a summand of the alternating square, it carries the label two, and its dimension is the only one of the four that is not a Mersenne number.

## Further Reading

- [The Spin-Three Carrier and the Rank Strata](the-spin-three-carrier-and-the-rank-strata.html), for the carrier above it in the chain.
- [The Spin-Two Carrier and the Trace Form](the-spin-two-carrier-and-the-trace-form.html), for the invariant form on the quintet.
- [The Spin-Two Carrier and the Rank Strata](the-spin-two-carrier-and-the-rank-strata.html), for the ranks realised inside it.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the addition rule.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the two squares of the sixteen.
