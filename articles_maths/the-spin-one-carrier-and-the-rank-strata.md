# __The Spin-One Carrier and the Rank Strata__

## Introduction

**The subject.** An element of the triplet acts on the module of the operators, and the rank of that action separates the triplet into two strata: the regular elements, of rank four, and the nilpotent cone, of rank three away from the origin. This article proves the separation, computes the dimensions of the two strata, compares the result with the spectral stratification and with the ranks of the whole operator space, and reads the vanishing of the trace as the balance of the two halves of the weight string.

**The order of the article.** *The Rank of an Element* fixes the action; *Four off the Cone, Three on It* proves the theorem; *The Two Strata* gives the dimensions; *The Coincidence with the Spectral Strata* compares the two separations; *The Higher Ranks* places the triplet in the whole space; *The Trace and the Sum of the Ranks* reads the constraint.

**It assumes** *The Spin-One Carrier: the Adjoint Triplet*, *The Spin-One Carrier and the Spectral Strata* and *The Four Ranks of the Two-Sided Operators*. **The row of the elements is** where an element acts on the algebra by left multiplication with rank zero or four.

**The result in one line.** On the triplet the rank of the action on the module is four at a regular element, three at a non-zero element of the cone, and zero at the origin.

**Boundaries.** The spectrum is *The Spin-One Carrier and the Spectral Strata*; the form is *The Spin-One Carrier and the Trace Form*; the rank strata of the operator carrier are *The Spin-$\tfrac32$ Bispinors and the Rank Strata*.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$; the generators of the triplet are $J_k=\tfrac12(L_{\vec e_k}-R_{\vec e_k})$; the module of the operators is $V=V_{3/2}$ of complex dimension four; the star is $\natural$; and $\operatorname{tr}$ is the trace of an operator on the module.

## The Rank of an Element

**Definition.** An element $X$ of the triplet is an operator on the module $V$; its **rank** is the dimension of its image, $\operatorname{rank}X=\dim XV$, and its **kernel** is the space of vectors it annihilates.

**Proposition.** The rank is invariant under the action of the group of the copy, and it is unchanged under multiplication of the element by a non-zero scalar.

*Proof.* The group acts by conjugation, which preserves the dimension of the image, and a scalar multiple has the same kernel and the same image.

**Corollary.** $\operatorname{rank}X=4-\dim\ker X$, and the kernel of a semisimple element is the sum of its zero-weight spaces.

*Proof.* The rank and the nullity of an operator on a four-dimensional space add to four, and the kernel of a semisimple element is the zero-weight space.

**The reading.** The rank is the first invariant of the element as an operator, and it is available without a choice of basis: it is the codimension of the kernel, and the kernel is read from the weights.

## Four off the Cone, Three on It

**Theorem.** An element of the triplet is either semisimple with four distinct eigenvalues on the module, or nilpotent; in the first case its rank is four, in the second its rank is three unless it is zero.

*Proof.* The triplet is the Lie algebra of the copy, and every element of that algebra is semisimple or nilpotent, the two cases being distinguished by the invariant form: the regular elements are those on which the form does not vanish. A semisimple element acts on the module with the four weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ scaled by its own value, and the four are distinct, so the kernel is zero and the rank is four. A non-zero nilpotent is the raising operator in some axis frame: it annihilates the highest weight line and carries the three other weight lines to non-zero vectors, so its kernel is one-dimensional and its rank is three.

**Corollary.** The rank of an element of the triplet is never one or two.

*Proof.* The two cases exhaust the elements, and their ranks are four, three and zero.

**The reading.** The exclusion of the intermediate ranks is a property of the triplet and not of the module: the operator space has elements of every rank, the triplet only of the two adjacent to the top.

## The Two Strata

**Theorem.** The triplet is the disjoint union of the regular set $\{c\neq0\}$, of complex dimension three, and the cone $\{c=0\}$, of complex dimension two; the origin lies in the cone and is the only element of rank zero.

$$
\dim\{c\neq0\}=3,\qquad \dim\{c=0\}=2,\qquad \operatorname{rank}=\begin{cases}4,& c\neq0,\\ 3,& c=0,\ X\neq0,\\ 0,& X=0.\end{cases}
$$

*Proof.* The invariant form is a non-zero quadratic form on a three-dimensional space, so its non-vanishing set is open and dense, of dimension three, and its zero locus is a cone of dimension two; the rank values are the theorem above.

**Corollary.** The regular stratum is connected, and the cone is connected with the origin as its vertex.

*Proof.* The complement of a cone in three dimensions has one piece for a form of rank three, and a cone is connected through its vertex.

**The reading.** Two strata of dimensions three and two, the smaller one carrying the vertex; the drop is the codimension one of a cone.

## The Coincidence with the Spectral Strata

**Proposition.** The spectral stratification has two strata, the regular set and the cone, and the rank stratification has three, the regular set, the interior of the cone and the vertex. The rank is therefore the finer of the two by exactly one stratum.

$$
\{c\neq0\}\ \big|\ \{c=0\}\setminus\{0\}\ \big|\ \{0\}\qquad\text{against}\qquad \{c\neq0\}\ \big|\ \{c=0\}.
$$

*Proof.* The spectrum of the adjoint action is $\lambda,0,-\lambda$ with $\lambda^2=c(X)$, so it is zero for every element of the cone and non-zero off it; it cannot separate the vertex from the rest of the cone. The rank is four on the regular set, three on the cone away from the vertex, and zero at the vertex.

**Corollary.** On the interior of the cone the two stratifications agree, and at the vertex the rank separates what the spectrum cannot.

*Proof.* Both stratifications put the interior of the cone in one piece, and only the rank has a piece consisting of the vertex alone.

**The reading.** The direction of the refinement is the opposite of the one at the row of the bispinors, and the reason is visible in the display: the adjoint action of a nilpotent annihilates the triplet, so the spectrum of the carrier is blind to the vertex. At the row of the bispinors the operator of the zero element is zero and the operator of a degenerate element is not, so there the spectrum is the finer of the two.

## The Higher Ranks

**Proposition.** The operator space contains elements of every rank from zero to four, and the triplet contributes only the ranks three, four and zero. The ranks one and two are contributed by the carriers of higher label.

*Proof.* A rank-one operator exists in the operator space and is not an element of the triplet, since every element of the triplet has rank at least three; the rank is therefore attained outside the triplet, and the operator space is the sum of the four carriers.

**Corollary.** The triplet is the carrier on which the rank is farthest from zero, and the low ranks appear only when the higher carriers are present.

*Proof.* The minimum rank of a non-zero element of the triplet is three, and the other carriers lower the minimum.

**The reading.** The rank measures how far an element is from the cone, and the higher carriers are where the low ranks live. The triplet is the carrier on which the rank stays closest to the dimension of the module.

## The Trace and the Sum of the Ranks

**Proposition.** Every element of the triplet is traceless on the module, and on the regular part the vanishing of the trace is the equality of the two halves of the weight string: two weights above zero and two below, each half of rank two.

*Proof.* An element of the triplet is a commutator, $X=\tfrac12(L_a-R_a)$, and the trace of a commutator is zero. A regular element has the four weights $\pm\tfrac32$ and $\pm\tfrac12$ scaled by its value, so two are positive and two negative, and the sum of the positive ones equals the sum of the negative ones.

**Corollary.** The rank four of a regular element is the sum $2+2$ of the ranks of the two halves of the string, and the vanishing of the trace is the balance of those two numbers.

*Proof.* The positive weights number two and the negative weights number two, so each half has rank two and the total is four.

**The reading.** The trace is the difference of the two halves and the rank is their sum, so the pair (rank, trace) is the pair (sum, difference) of two equal numbers at this row, and the trace vanishes.

## Further Reading

- [The Spin-One Carrier and the Spectral Strata](the-spin-one-carrier-and-the-spectral-strata.html), for the finer stratification and its discriminant
- [The Spin-One Carrier: the Adjoint Triplet](the-spin-one-carrier-the-adjoint-triplet.html), for the generators and the brackets
- [The Four Ranks of the Two-Sided Operators](the-four-ranks-of-the-two-sided-operators.html), for the rank of a two-sided operator at the row of the elements
- [The Spin-One Carrier and the Trace Form](the-spin-one-carrier-and-the-trace-form.html), for the invariant form that distinguishes the cone
- [The Spin-$\tfrac32$ Bispinors and the Rank Strata](the-spin-three-halves-bispinors-and-the-rank-strata.html), for the rank of the operator named by a bispinor
