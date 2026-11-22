# __Which Spin Lives in Which Reading__

## Introduction

**The subject.** The number $\tfrac32$ and the number $3$ both occur in the theory of the operators, and they are not the same number attached to two names: $\tfrac32$ is the label of the module, a weight that a vector of the space can have, and $3$ is the label of the largest carrier, a difference of two such weights. The article separates the two readings, lists what each one measures, and gives the rule that decides which one a given statement uses.

**The order of the article.** The two readings come first; the labels and their meaning second. The passage between the readings follows, then the mistaken uses, and the reading closes the article.

**It assumes** *The Slot and the Summand: $\tfrac12$ in $\mathbb{B}$ and $\tfrac32$ in the Operators*, *Why the Conjugation Labels Are Integer* and *The Four Carrier Lists*. **The row of the elements is** where the two numbers are $\tfrac12$ and $1$, and the same separation applies.

**The result in one line.** The label $\tfrac32$ measures the module under the left action, the label $3$ measures the largest carrier under the conjugation action, and the two differ by a factor two, the square of the module.

**Boundaries.** The labels of the two rows are *The Slot and the Summand*; the integrality of the second reading is *Why the Conjugation Labels Are Integer*; the four lists are *The Four Carrier Lists*.

## The Two Readings

**Definition.** A **module label** is the highest weight of a module of the copy; a **carrier label** is the highest weight of an invariant subspace of the conjugation action.

**Proposition.** The module labels of the theory are $\tfrac12$ and $\tfrac32$; the carrier labels are $0,1,2,3$ in the operator algebra and $0,1$ in the algebra.

*Proof.* The module strings and the conjugation strings, as computed in the two rows.

**Corollary.** The module labels are half-integers and the carrier labels are integers, in both rows.

*Proof.* The second reading subtracts two weights of the first.

**Corollary.** A statement using a module label is a statement about the left action, and a statement using a carrier label is a statement about the commutator.

*Proof.* The two actions and their weights.

**The reading.** Two numbers, two actions. The article's rule is that the label alone does not say which reading is meant, and that the action must be named.

## What the Module Label Measures

**Proposition.** The module label $\tfrac32$ measures the dimension four of the module, the number of weights, the sign after a full turn, and the quaternionic type.

*Proof.* The dimension is $2j+1=4$; the number of weights is the same; the sign is $(-1)^{2j}=-1$; the type is quaternionic because the label is half-integer.

**Corollary.** The module label is the number that appears in the half angle, since a rotation of angle $\theta$ acts on the module by $\exp(\theta H/2)$.

*Proof.* The half angle and the weight.

**Corollary.** The module label is not visible in the weights of the operator space, and it is visible in every statement about phases.

*Proof.* The differences are integers, and the phases are half-integer.

**The reading.** The module label is the projective label: it measures how far the module is from being a representation of the rotation group. It is the label of the object that carries a sign.

## What the Carrier Label Measures

**Proposition.** The carrier label $3$ measures the dimension seven of the largest carrier, the eigenvalue $12$ of the Casimir, the highest weight of the space, and the reality of the carrier.

*Proof.* The dimension is $2k+1=7$; the Casimir is $k(k+1)=12$; the highest weight is the largest difference of the module weights; the type is real because the label is an integer.

**Corollary.** The carrier label is visible in the weights of the operator space, since it is one of them.

*Proof.* The highest weight of the space is $3$, the largest difference.

**Corollary.** The carrier label is the integral label: it measures an invariant subspace and not a phase.

*Proof.* The carrier is an eigenspace of the Casimir of the conjugation action.

**The reading.** The carrier label is the algebraic label: it measures a subspace of the algebra, and it is visible to the algebra's own operators. It appears in dimensions and in Casimir eigenvalues and never in a phase.

## The Passage

**Theorem.** The passage from the module label to the carrier label is the doubling: the square of a module of label $j$ has the carrier labels $0,1,\dots,2j$.

*Proof.* The differences of the weights of a module of label $j$ are the integers from $-2j$ to $2j$, and the carriers run from zero to $2j$.

**Corollary.** The passage from the module label $\tfrac32$ gives the carrier labels up to $3$, and the passage from the module label $\tfrac12$ gives the labels up to $1$.

*Proof.* Twice $\tfrac32$ is three and twice $\tfrac12$ is one.

**Corollary.** No passage returns from the carrier label to the module label, since the doubling loses the half.

*Proof.* Two modules of labels $j$ and $j+\tfrac12$ would give different carrier labels, but one module gives one list and the list does not encode the half.

**The reading.** The passage is the tensor square read on the labels, and it is one-way. A statement about carriers cannot be lifted to a statement about the module without extra data, and the extra data is the half-integer.

## The Mistaken Uses

**Proposition.** The two common mistakes are to attribute the carrier label to the module and to attribute the module label to a carrier.

*Proof.* The first mistake gives a module of dimension seven instead of four; the second gives a carrier of dimension four instead of seven.

**Corollary.** Both mistakes are detected by the dimension count: $2\cdot\tfrac32+1=4$ and $2\cdot3+1=7$.

*Proof.* The formula for the dimension of a module in terms of its label.

**Corollary.** The two labels coincide only at zero, where the module and the carrier are the scalars.

*Proof.* $j=2j$ only for $j=0$.

**The reading.** The dimension is the quickest test, and it decides the reading. A number quoted without its action is a number half understood, and the article's rule is to always name the action.

## The Test Case of the Algebra Itself

**Proposition.** On the algebra of dimension four the same two readings give the module label $\tfrac12$ and the carrier label $1$, and the ratio is again three.

*Proof.* The algebra is the square of the slot: it is the tensor square of the two-dimensional spinor, whose weights are $\pm\tfrac12$, so as a module over the copy it is two copies of the slot; and under the conjugation the square splits as the triplet and the singlet, of labels $1$ and $0$.

**Corollary.** The half-integer belongs to the module in both rows and the integer to the carriers in both rows, and the displacement from the module string to the carrier string is the same multiplication by three.

*Proof.* The strings are $\pm\tfrac12$ against $0,\pm1$ in the algebra and $\pm\tfrac32,\pm\tfrac12$ against $0,\pm1,\pm2,\pm3$ in the operators, and in both cases the largest carrier label is three times the largest module label.

**Corollary.** A statement that confuses the two readings is detected by its number alone, without any computation on the space.

*Proof.* A label of the form $\tfrac12$ with an odd numerator can only be a module label, since the carrier labels are integers in both rows.

**The reading.** The algebra is the smallest case in which the two readings can be compared, and it shows that the separation of the two labels is not a feature of dimension sixteen. The half-integer records a module, the integer records an invariant subspace, and the factor three is the multiplication of the label by the cube.

## Further Reading

- [The Slot and the Summand: $\tfrac12$ in $\mathbb{B}$ and $\tfrac32$ in the Operators](the-slot-and-the-summand.html), for the module labels of the two rows.
- [Why the Conjugation Labels Are Integer](why-the-conjugation-labels-are-integer.html), for the carrier labels.
- [The Four Carrier Lists](the-four-carrier-lists-of-one-algebra.html), for the actions and their decompositions.
- [The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-the-principal-copy-and-the-kernel.html), for the copy that carries both labels.
