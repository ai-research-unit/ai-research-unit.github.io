# __What a Half-Integer Summand Would Require__

## Introduction

**The subject.** The four carriers have the integer labels $3,2,1,0$, and it is natural to ask what a fifth carrier of label $\tfrac52$ would require. The article answers by listing the three requirements it would have to satisfy, the weight, the eigenvalue of the Casimir, and the type, and shows that each of the three fails, and that they fail for one reason: the operator space is a square of a half-integer module.

**The order of the article.** The requirement on the weights comes first; the requirement on the Casimir second. The requirement on the type follows, then the single reason, and the reading closes the article.

**It assumes** *The Clebsch–Gordan Decomposition of the Operators*, *Why the Conjugation Labels Are Integer* and *The Spin Decomposition: Four Carriers and the Weight Multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$*. **The row of the elements is** where the same question asks for a carrier of label $\tfrac32$ in a four-dimensional algebra, and the same three requirements fail.

**The result in one line.** A carrier of label $\tfrac52$ would need a weight $\tfrac52$ in the operator space, the Casimir eigenvalue $\tfrac{35}{4}$, and a quaternionic type; the largest weight is $3$, the eigenvalues are $12,6,2,0$, and the space is a square, so all three fail.

**Boundaries.** The existing carriers are *The Clebsch–Gordan Decomposition of the Operators*; the weights are *The Spin Decomposition*; the types are *The Quaternionic Structure of the Module*.

## The Weight Requirement

**Proposition.** A carrier of label $L$ requires a weight $L$ in the space, and a weight $L$ in the operator space is a difference $m-m'$ of two weights of the module.

*Proof.* The label is the highest weight of the carrier, and the weights of the space are the differences.

**Corollary.** The label $\tfrac52$ would require a difference of two weights of the module equal to $\tfrac52$, and the largest difference is $3$.

*Proof.* The four weights are $\pm\tfrac32,\pm\tfrac12$, and the largest difference is $\tfrac32-(-\tfrac32)=3$.

**Corollary.** No difference equals $\tfrac52$, since the differences are integers and $\tfrac52$ is not.

*Proof.* The differences of half-integers are integers.

**The reading.** The first requirement fails twice: the value $\tfrac52$ is not integral and it exceeds the largest difference. The failure is not a matter of dimension but of the arithmetic of the weight string.

## The Casimir Requirement

**Theorem.** A carrier of label $L$ is an eigenspace of the Casimir with the eigenvalue $L(L+1)$; for $L=\tfrac52$ the eigenvalue would be $\tfrac{35}{4}$.

*Proof.* The Casimir of the simple module of label $L$ is $L(L+1)$, and $\tfrac52\cdot\tfrac72=\tfrac{35}{4}$.

**Corollary.** The four eigenvalues present are $12,6,2,0$, and none equals $\tfrac{35}{4}$.

*Proof.* The four labels are $3,2,1,0$, and their Casimir values are computed by the same formula.

**Corollary.** The four eigenvalues are distinct and exhaust the spectrum of the Casimir, so a fifth eigenspace cannot be added without changing the space.

*Proof.* The sum of the dimensions of the four eigenspaces is sixteen, the dimension of the space.

**The reading.** The second requirement fails on the spectrum. The Casimir is a single operator, and its eigenvalues on the space are four numbers; the value $\tfrac{35}{4}$ is not among them, so no eigenspace of that label exists.

## The Type Requirement

**Proposition.** A carrier of half-integer label is quaternionic and has a real dimension twice its complex dimension; a carrier of label $\tfrac52$ would have complex dimension six and real dimension twelve.

*Proof.* The sign of the square of the anti-linear intertwiner is negative for a half-integer label, so the real structure doubles the dimension; the dimension of the carrier is $2\cdot\tfrac52+1=6$.

**Corollary.** The presence of such a carrier would force the real dimension of the operator space to be an even number not equal to sixteen.

*Proof.* Twelve real dimensions for one carrier, and the remaining carriers would contribute integers of the same kind.

**Corollary.** The real dimension of the operator algebra is sixteen, the square of the real dimension of the module, so the count excludes the half-integer carrier.

*Proof.* The operator algebra is the real algebra of the linear maps of a four-real-dimensional space, and its real dimension is the square of the dimension.

**The reading.** The third requirement fails on the type: a half-integer carrier is quaternionic, and a quaternionic carrier of dimension six would need twelve real dimensions in a space whose real dimension is sixteen and whose other carriers are real of dimensions seven, five, three and one. The sums do not close.

## The Single Reason

**Theorem.** All three failures have one cause: the operator space is the tensor square of a module of half-integer label, and the square of a half-integer label is an integer.

*Proof.* The weights of the square are differences and hence integral; the Casimir series of a tensor square of label $j$ runs over the integers from zero to $2j$; and the type of an integer label is real.

**Corollary.** A half-integer summand would require a module of half-integer label whose square has a half-integer label, which is impossible.

*Proof.* Twice a half-integer is an integer.

**Corollary.** The obstruction is not removed by enlarging the space, since any tensor square of a half-integer module has integer labels.

*Proof.* The argument uses only the doubling of the label.

**The reading.** The three requirements are three faces of one arithmetic fact. A reader who tries to add a half-integer carrier by hand will find that the weight, the Casimir and the type all refuse at once, and the refusal is the parity of the label.

**The dimensional echo.** The four carriers exhaust sixteen dimensions, and any fifth would have to be paid for out of the sixteen; the smallest half-integer carrier, of label $\tfrac12$, would need two complex dimensions and a quaternionic doubling to four real ones, leaving twelve to the rest. The count alone does not forbid it, which is why the weight argument is the decisive one.

## The Selection Rule

**Proposition.** A coefficient $\langle\tfrac32,m_1;\tfrac32,m_2\vert J,M\rangle$ vanishes unless $m_1+m_2=M$.

*Proof.* A state of weight $M$ is a sum of products of weight $M$ and of no others.

**Corollary.** No half-integer label occurs, because the products of the module have integer weights and a label is the weight of a product.

*Proof.* The weights of the module are $\pm\tfrac32$ and $\pm\tfrac12$, so every sum $m_1+m_2$ is an integer; a label of the square is such a sum, so it is an integer.

**The reading.** The requirement fails at the count of the weights, before any Casimir is computed: the selection rule forbids the coefficient, and the multiset of the square forbids the half-integer weight that a half-integer label would need.

## The Reading

**What would be needed.** A module whose tensor square has a half-integer label, that is, a module with a quarter-integer weight, or an odd number of factors with a residual half shift. Neither exists among the modules of this copy.

**What fails first.** The weight, because it is the cheapest test: one subtraction of two half-integers and the answer is an integer.

**What the failure teaches.** The integer labels of the operator space are not a choice of the theory; they are forced by the doubling. The half-integer label of the module is the last place where the half-integers can live, and every attempt to put them elsewhere is stopped by the same parity.

## Further Reading

- [The Clebsch–Gordan Decomposition of the Operators](the-clebsch-gordan-decomposition-of-the-operators.html), for the four labels present.
- [Why the Conjugation Labels Are Integer](why-the-conjugation-labels-are-integer.html), for the integrality of the differences.
- [The Spin Decomposition: Four Carriers and the Weight Multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$](the-spin-decomposition-four-carriers-and-the-weight-multiset.html), for the largest weight.
- [The Quaternionic Structure of the Module: Why $V_{3/2}$ Admits Real Forms](the-quaternionic-structure-of-the-module-and-the-real-forms.html), for the type of a half-integer carrier.
