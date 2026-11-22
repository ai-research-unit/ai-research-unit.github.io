# __The Slot and the Summand: $\tfrac12$ in $\mathbb{B}$ and $\tfrac32$ in the Operators__

## Introduction

**The subject.** The algebra has a module of label $\tfrac12$ and the operator algebra has a module of label $\tfrac32$. The two labels are the same object read at two levels: the operator module is the third symmetric power of the algebra module, and the label is the sum of three copies of $\tfrac12$. The article names the two readings, the slot and the summand, computes their dimensions, and shows that the doubling is an exact rule with no free parameter.

**The order of the article.** The two labels come first; the slot second. The summand follows, then the doubling, and the reading closes the article.

**It assumes** *The Four Weights of the Module and the Half Angle*, *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$* and *The Minimal Left Ideals and the Module $V_{3/2}$*. **The row of the elements is** the slot; the row of the operators is the summand.

**The result in one line.** The algebra is a slot of half-integer label $\tfrac12$ and dimension two, the operator algebra is a summand of label $\tfrac32$ and dimension four, and the passage is the symmetric cube, which multiplies the label by three.

**Boundaries.** The weights are *The Four Weights of the Module and the Half Angle*; the decomposition of the operator space is *The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$*; the identity of the two labels is also read in *From the Spin Decomposition to the Weight Strings*.

## The Two Labels

**Definition.** The **label** of a simple module of the copy is the highest weight of its weight string; the module of the algebra has label $\tfrac12$ and the module of the operators has label $\tfrac32$.

*Proof.* The weight strings are $\tfrac12,-\tfrac12$ and $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$.

**Corollary.** The two labels differ by one unit, and the dimensions differ by a factor two.

*Proof.* $\tfrac32-\tfrac12=1$ and $4/2=2$.

**Corollary.** The two labels are both half-integer, so both modules are quaternionic.

*Proof.* The type is decided by the parity of twice the label, and both are odd.

**The reading.** Two labels, one half-integer each, and a difference of one. The article explains where the one comes from and why it cannot be anything else.

## The Slot

**Proposition.** The algebra is a slot: its module is the two-dimensional spinor space, the label is $\tfrac12$, and the slot is the pair (label, dimension) $=(\tfrac12,2)$.

*Proof.* The algebra is four-dimensional over the reals and two-dimensional over the complex numbers; the copy acts on it by left multiplication, and the weights are $\pm\tfrac12$.

**Corollary.** The slot is the smallest non-trivial module of the group, and it is the module on which the sign after a full turn is visible.

*Proof.* The weights are half-integers, so the rotor of angle $2\pi$ acts as $-1$.

**Corollary.** The slot is quaternionic and has real dimension four.

*Proof.* The complex dimension two and the negative square of the intertwiner.

**The reading.** The slot is the elementary object: one label, one dimension, one sign. Every other module of the theory is built from it by symmetric powers and tensor products, and the operator module is the first non-trivial power.

## The Summand

**Proposition.** The operator algebra is a summand: its module is the four-dimensional space of the operators, the label is $\tfrac32$, and the summand is $(\tfrac32,4)$.

*Proof.* The module of the operators is the algebra as a left module, of complex dimension four; the weights are the four half-integers from $\tfrac32$ down.

**Corollary.** The summand is the third symmetric power of the slot, $\tfrac32=3\cdot\tfrac12$.

*Proof.* The weights of the symmetric cube are the sums of three weights of the slot, the largest being three times $\tfrac12$.

**Corollary.** The summand is quaternionic, with real dimension eight.

*Proof.* The label is half-integer.

**The reading.** The summand is the slot cubed, and the cube is the reason for the label $\tfrac32$. Nothing in the definition of the operator algebra mentions the copy; the label appears only when the copy is chosen, and then it appears as three times the slot.

## The Doubling

**Theorem.** The passage from the slot to the summand multiplies the label by three and the dimension by two, and no other passage preserves both the half-integer character and the symmetry of the strings.

*Proof.* The symmetric cube of a module of label $j$ has label $3j$; with $j=\tfrac12$ the label is $\tfrac32$. The dimension of the cube of a two-dimensional module is four. Any other power would give a label $kj$ with a different $k$, and the half-integer character would require $k$ odd.

**Corollary.** The next symmetric power, the fourth, would have label two and would be integral, so the string of the operator module stops at the cube because the algebra does.

*Proof.* The symmetric cube is the module of the operators, and there is no fourth symmetric power in the theory.

**Corollary.** The tensor square of the summand has the four integer labels, which is the spin decomposition of the operator space.

*Proof.* Twice $\tfrac32$ is three, and the series runs from zero to three.

**The reading.** The two operations, symmetric cube and tensor square, are the two passages of the theory: cube from the algebra to its operators, square from the operators to their algebra. The first doubles the label's denominator, the second removes it.

## The Square and the Cube

**Proposition.** The algebra is the square of the slot and the module of the operators is its cube, and the two are different modules although both have dimension four.

*Proof.* The tensor square of a two-dimensional space has dimension four and splits as the triplet and the singlet; the third symmetric power of a two-dimensional space has dimension four and is irreducible, of label $\tfrac32$.

**Corollary.** The square of the slot contains the singlet, and the cube does not.

*Proof.* The square of the slot contains the alternating square of two slot vectors, which is one-dimensional and invariant; the cube has top weight $\tfrac32$ and every weight of it is half-integral, so no invariant line occurs in it.

**Corollary.** A statement about the algebra and a statement about the operators cannot be transferred by dimension alone, since the two spaces have the same dimension and different module structure.

*Proof.* The two decompositions $3+1$ and $4$.

**The reading.** The two spaces are twins of dimension four with different symmetry. The algebra keeps a singlet because it is a square, and the operators have none because they are a cube. This is the reason the operators carry the half-integer label and the algebra does not.

## The Reading

**One object, two names.** The slot and the summand are the same module at two levels of one construction; the names record which level a statement belongs to. A statement about a spinor is a statement about the slot; a statement about an operator is a statement about the summand.

**One arithmetic.** The labels $\tfrac12$ and $\tfrac32$ differ by the number of factors in the cube, and the difference is the only thing the two rows do not share.

**One warning.** The label of the operator module is not the label of the algebra, and a formula that uses one where the other belongs will be off by a factor three in the exponent of a phase. The half angle is the place where the error shows first.

**One check.** The two dimensions, two and four, satisfy the binomial count of the symmetric cube, $\binom{2+3-1}{3}=4$, and the two labels satisfy the addition of three halves. The two identities are one identity read on dimensions and on weights.

## Further Reading

- [The Four Weights of the Module and the Half Angle](the-four-weights-of-the-module-and-the-half-angle.html), for the two strings.
- [The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-the-principal-copy-and-the-kernel.html), for the symmetric cube.
- [The Minimal Left Ideals and the Module $V_{3/2}$](the-minimal-left-ideals-and-the-module.html), for the module of the operators as a left ideal.
- [The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$](the-clebsch-gordan-decomposition-of-the-biquaternion-operators.html), for the square of the summand.
