# __The Three Rows: $\mathbb{B}$, $M_2(\mathbb{C})$ and $M_4(\mathbb{C})$__

## Introduction

**The subject.** The corpus treats three algebras in the same way: the biquaternions, the two-by-two complex matrices and the four-by-four complex matrices. The article places the three rows side by side, states which numbers change and which stay the same, and explains why the middle row is not a separate theory but the same one as the first, read over the complex numbers.

**The order of the article.** The first section fixes the three algebras and their dimensions. The second compares their modules and labels. The third compares their decompositions and kernels. The fourth states the law that generates one row from the next. The fifth draws the boundary.

**It assumes** *The Biquaternions as a Clifford Algebra* and *The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$*.

**The result in one line.** The biquaternions are the real algebra $M_2(\mathbb{C})$, of real dimension eight and complex dimension four, and $M_4(\mathbb{C})$ is the same construction with the module doubled twice: complex dimensions $4\to16$ and $2\to4$.

**Boundaries.** The article compares the rows; the detailed articles for each row remain the reference for the single cases.

## The Three Algebras

**Proposition.** $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ is isomorphic to $M_2(\mathbb{C})$ as a real algebra, of real dimension eight and complex dimension four, and $M_4(\mathbb{C})$ has complex dimension sixteen and real dimension thirty-two.

*Proof.* The quaternions form a four-dimensional real algebra and their complexification is the matrix algebra of two-by-two complex matrices, of complex dimension four and real dimension eight; the algebra of four-by-four complex matrices has $16$ complex and $32$ real dimensions.

**Corollary.** The three rows have real dimensions $8$, $8$ and $32$, so the first two coincide as algebras and the third is the next case.

*Proof.* The proposition.

**Corollary.** Each algebra is simple over its own field, so each has no nontrivial two-sided ideals.

*Proof.* A full matrix algebra is simple, and the biquaternions are a full matrix algebra over the complex numbers.

**The reading.** There are two algebras and three rows: the biquaternion row and the two-by-two row are the same algebra read over different fields.

## The Modules and the Labels

**Proposition.** The module is $V_{1/2}$ of dimension two for the row of order two and $V_{3/2}$ of dimension four for the row of order four; the label is $(n-1)/2$ in both cases.

*Proof.* The module is the space of column vectors, of dimension $n$, and the copy acts on it as the symmetric power $\operatorname{Sym}^{n-1}$ of the two-dimensional representation, whose label is $(n-1)/2$.

**Corollary.** The labels of the algebra are the integers $0$ to $n-1$, and the module carries the half-integer label.

*Proof.* The tensor square of the module with its dual decomposes into the integer labels; the module itself carries the half-integer label.

**Corollary.** At order two the algebra carries the labels zero and one, of dimensions $1$ and $3$; at order four it carries zero to three, of dimensions $1,3,5,7$.

*Proof.* The dimensions $2k+1$ for the label $k$.

**The reading.** The row of order two has a module of dimension two and one nontrivial carrier; the row of order four has a module of dimension four and three nontrivial carriers.

## The Decompositions and the Kernels

**Proposition.** In both rows the algebra decomposes into the carriers with multiplicity one, and the kernel of the map from the copy to the special unitary group is $\{\pm\mathrm I\}$.

*Proof.* The tensor square of the module with its dual is multiplicity-free in both cases; the representation $\operatorname{Sym}^{n-1}$ of the two-dimensional module is faithful up to the sign, so the kernel is the centre of the copy.

**Corollary.** In both rows every summand label is an integer while the module label is half-integral.

*Proof.* The decomposition of the tensor square.

**Corollary.** The quaternionic structure of the module holds in both rows, and the real forms of the carriers exist in both rows because their labels are integers.

*Proof.* The indicator of the module is $(-1)^{n-1}$, which is $-1$ for $n=2$ and $n=4$, and the indicator of an integer label is $+1$.

**The reading.** The two rows share the same structural facts: multiplicity-free decomposition, integer carriers, half-integer module, two-element kernel.

## The Law of the Rows

**Proposition.** The passage from the row of order two to the row of order four squares the complex dimension of the algebra, $4\to16$, doubles the dimension of the module, $2\to4$, and multiplies the number of carriers by three, $2\to4$ counting the scalars.

*Proof.* The dimension of the algebra is $n^{2}$ and that of the module is $n$.

**Corollary.** The real dimension grows from eight to thirty-two, a factor of four, while the complex dimension grows by a factor of four as well.

*Proof.* The dimensions displayed.

**Corollary.** The next row would have module of dimension six, algebra of dimension thirty-six, label five halves and four nontrivial carriers.

*Proof.* The law with $n=6$.

**The reading.** The rows form a sequence indexed by the dimension of the module, and each row is generated by the same three ingredients: the module, the copy and the tensor square.

## The Boundary

**Against the biquaternion articles.** Those articles treat the row of order two in detail, including the quaternionic real structure.

**Against the spin group article.** That article treats the copy, the symmetric power and the kernel at order four.

**Against the law of the module.** The general statement of the sequence is the subject of *The Law of the Module and the Chain of Carriers at Every $n$*.

## A Final Observation

**The invariants that do not change.** In both rows the algebra is simple, the decomposition is multiplicity-free, the module is quaternionic and the kernel is the centre; the numbers change and the structure does not, which is the reason a single set of proofs serves two rows.

**The row of order six.** The next case would have a module of dimension six, a quaternionic structure again because six minus one is odd, and an algebra of dimension thirty-six with the carriers of labels zero to five.

## The Same Proof Twice

**The transfer of the proofs.** Every proof in the row of order four that uses only the Clebsch–Gordan rule, the multiplicity-free decomposition and the sign rule transfers to the row of order two without change, because none of them uses the value of the dimension; the proofs that use the number four, such as the count of the ranks, do not transfer.

**The two kinds of statement.** A statement is structural when it names the module, the copy and the carriers; it is numerical when it names a dimension, a rank or a signature. The structural statements hold in both rows, and the numerical ones must be recomputed.

**The example.** The statement that every carrier label is an integer is structural and holds in both rows; the statement that the left multiplication by a matrix of rank three has rank twelve is numerical and holds only at order four.

**The reading.** The three rows are one theory with numerical parameters, and the comparison is the separation of the statements that survive the change of the parameter from those that do not.

## Summary

The biquaternions and the two-by-two complex matrices are the same algebra read over two fields, of dimensions eight real and four complex; the four-by-four complex matrices are the next case, of dimensions thirty-two real and sixteen complex. The module has dimension $n$ and label $(n-1)/2$, and the algebra decomposes into the integer carriers with multiplicity one in both rows.

The kernel of the map to the special unitary group is the centre in both rows, and the module is quaternionic in both, while the carriers are real type because their labels are integers.


**The place in the corpus.** The comparison fixes the vocabulary of the sequence: module, copy, carriers, kernel, real form. Every later article that speaks of the row of order four is speaking of the same five objects with the numbers of that row, and the row of order two is the smallest instance in which they all occur.
## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\cong M_2(\mathbb{C})$ | the biquaternion row |
| $M_4(\mathbb{C})$ | the row of order four |
| $4\to16$, $2\to4$ | the growth of the dimensions |
| $0,1$ and $0,1,2,3$ | the carrier labels |

## Further Reading

- [The Biquaternions as a Clifford Algebra](the-biquaternions-as-a-clifford-algebra.html), for the first row.
- [The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-at-n-4-the-principal-copy-and-its-kernel.html), for the third row.
- [The Law of the Module and the Chain of Carriers at Every $n$](the-law-of-the-module-and-the-chain-of-carriers.html), for the general statement.
- [The Four Carrier Lists of One Algebra at $n=4$](the-four-carrier-lists-of-one-algebra-at-n-4.html), for the readings.
- [The Spin Zero Carrier of the Biquaternion Algebra](the-spin-zero-carrier-of-m4c.html), for the scalar carrier at order two.
