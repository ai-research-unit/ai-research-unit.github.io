# __The Four Weights of the Module and the Half Angle__

## Introduction

**The subject.** The Cartan generator of the copy acts on the four-dimensional module with the four weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, each simple. The article computes the ladder, identifies the highest weight vector as the cube of a spinor, computes the raising and lowering coefficients, and reads the half angle: a rotation of angle $\theta$ of the algebra acts on the module as the exponential of half the generator, and the weights are the derivatives of that action. The half-integer character of the weights is the feature that separates this row from the row of the elements.

**The order of the article.** The weights and the ladder come first; the highest weight vector and the coefficients second. The half angle follows, and the reading closes the article.

**It assumes** *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*, *The One-Sided Operators* and *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. **The row of the elements is** where the same generator has the weights $\pm\tfrac12$; here the cube of the module doubles the string.

**The result in one line.** The module has the four simple weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, the ladder has the coefficients $\sqrt3,2,\sqrt3$, and the weights are half-integers because the generator acts on the module as half of the rotation.

**Boundaries.** The label of the module as a whole is *The Slot and the Summand*; the group and its kernel are *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*; the decomposition of the sixteen is *The Spin Decomposition: Four Carriers and the Weight Multiset*.

## The Weights

**Definition.** The **Cartan generator** is $H=i\xi_z$, the operator of left multiplication by $i\vec e_z$ multiplied by $i$, so that $H$ is Hermitian for the trace form. Its **weights** are the eigenvalues of $H$ on the module.

**Theorem.** The generator $H$ has the four eigenvalues
$$
\tfrac32,\quad \tfrac12,\quad -\tfrac12,\quad -\tfrac32,
$$
each with multiplicity one, and the four eigenvectors form a basis of the module.

*Proof.* The generator is the left multiplication by $i\vec e_z$ times $i$; its action on the module, identified with the third symmetric power of the two-dimensional spinor space, is the sum of the three diagonal actions on the three factors, so the eigenvalues are the sums of three values $\pm\tfrac12$, taken with multiplicity, and the sums are the four numbers displayed.

**Corollary.** The module is multiplicity-free, and its four weights are in arithmetic progression of step one, symmetric about zero.

*Proof.* The sums of three signs give the four values, each in exactly one way up to the order of the factors.

**Corollary.** The sum of the four weights is zero, and the sum of their squares is five.

*Proof.* $\tfrac32+\tfrac12-\tfrac12-\tfrac32=0$ and $\tfrac94+\tfrac14+\tfrac14+\tfrac94=5$.

**The reading.** Four weights, four dimensions, no repetition. The module is the simplest carrier of the copy at this row, and its weight string is fixed by the algebra: the generator is a left multiplication, and the module is the algebra.

## The Ladder

**Definition.** The **raising and lowering operators** are $E=\xi_x+i\xi_y$ and $F=\xi_x-i\xi_y$, the complex combinations of the two remaining generators.

**Theorem.** On the weight vectors $v_m$, ordered by increasing weight,
$$
Fv_{-3/2}=\sqrt3\,v_{-1/2},\qquad Fv_{-1/2}=2v_{1/2},\qquad Fv_{1/2}=\sqrt3\,v_{3/2},\qquad Fv_{3/2}=0,
$$
and $E$ is the mirror ladder with the same coefficients.

*Proof.* The coefficients are those of the ladder operators of the spin $	frac32$ representation, which are $\sqrt{j(j+1)-m(m+1)}$; for $j=\tfrac32$ the three values are $\sqrt3$, $2$ and $\sqrt3$.

**Corollary.** The highest weight vector is annihilated by $E$ and generates the module under $F$.

*Proof.* The highest weight vector has weight $\tfrac32$, the maximum, so no raising is possible; the lowering steps reach all four weights.

**Corollary.** The Casimir operator of the copy acts on the module by the scalar $\tfrac{15}{4}$, and the four weights are recovered from it together with $H$.

*Proof.* The Casimir of the spin $j$ representation is $j(j+1)=\tfrac32\cdot\tfrac52=\tfrac{15}{4}$.

**The reading.** The ladder is the whole structure of the module: one vector, three steps, four weights. The coefficients are fixed by the algebra and not by a choice of basis, and their squares $3,4,3$ sum to ten, which is the dimension of the symmetric square.

## The Highest Weight Vector

**Proposition.** Let $s$ be a highest weight spinor of the two-dimensional spinor space $S$. Then $s^{3}$ is the highest weight vector of the module, and its weight is $\tfrac32$.

*Proof.* The symmetric cube of the highest weight vector of $S$ has weight three times $\tfrac12$, and it is annihilated by the raising operator because the latter acts as a derivation on the symmetric algebra.

**Corollary.** The module is generated by a single monomial, and every weight vector is a monomial in the two spinor coordinates.

*Proof.* The symmetric cube has the four monomials $s^{3},s^{2}t,st^{2},t^{3}$, and they are the four weight vectors.

**Corollary.** The vanishing of the raising operator on $s^{3}$ is the statement that there is no weight $\tfrac52$ in the module.

*Proof.* A vector of weight $\tfrac52$ would be a fourth symmetric power, and the module is the third.

**The reading.** The module is the cube of the spinor space, and the highest weight vector is the cube of a spinor. The truncation at the fourth power is the reason the ladder stops, and the stopping is the statement that the module is finite-dimensional.

## The Half Angle

**Theorem.** A rotation of angle $\theta$ of the algebra acts on the module by $\exp(\theta H/2)$, and the weight of a vector is the derivative of its phase at $\theta=0$:
$$
u(\theta)\cdot v_m=e^{\,i m\theta/2}v_m .
$$

*Proof.* The rotor of angle $\theta$ is the exponential of $\tfrac{\theta}{2}\xi_{\vec n}$, and on the module the generator acts with the eigenvalues $2m$; hence the phase of a weight vector is $m\theta$ over two.

**Corollary.** The half angle is forced by the pair of facts: the generator has the eigenvalues $2m$ on the module and the rotation is the exponential of half the generator.

*Proof.* The two statements compose to the displayed phase.

**Corollary.** The weights are half-integers exactly when the module changes sign at $\theta=2\pi$.

*Proof.* The phase at $\theta=2\pi$ is $e^{i\pi m}$, which is $-1$ exactly for a half-integer $m$.

**The reading.** The half angle is not an extra structure: it is the composition of the exponential of the generator with the doubling of the weights on the module. This is why the four weights are half-integers and why the module is the place where the sign after a full turn lives.

## The Separation from the Row of the Elements

**Proposition.** The row of the elements has two weights $\pm\tfrac12$ for the same generator, and the row of the operators has four weights $\pm\tfrac12,\pm\tfrac32$.

*Proof.* The module of the elements is the two-dimensional spinor space, with the weights $\pm\tfrac12$; the module of the operators is its third symmetric power, with the four sums.

**Corollary.** The two rows differ by the number of weights and by the presence of the integer gap, not by the nature of the weights.

*Proof.* Both strings are half-integral and symmetric; the second has a step of one and four terms.

**Corollary.** No computation on the operators is needed to pass from one string to the other: the passage is the symmetric cube.

*Proof.* The weights of the cube are the sums of three weights of the module.

**The reading.** The half angle is shared by the two rows, and the doubling of the string is the only difference. A statement about the spin of this row must therefore name the module, since the weights do not distinguish the rows by their character but only by their number.

## Further Reading

- [The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-the-principal-copy-and-the-kernel.html), for the copy acting on the module.
- [The Minimal Left Ideals and the Module $V_{3/2}$](the-minimal-left-ideals-and-the-module.html), for the module and its weight vectors.
- [The Slot and the Summand: $\tfrac12$ in $\mathbb{B}$ and $\tfrac32$ in the Operators](the-slot-and-the-summand.html), for the labels of the two rows.
- [The Spin Decomposition: Four Carriers and the Weight Multiset](the-spin-decomposition-four-carriers-and-the-weight-multiset.html), for the weights of the sixteen differences.
