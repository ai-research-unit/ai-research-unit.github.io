# __The Minimal Left Ideals and the Module $V_{3/2}$__

## Introduction

**The subject.** A minimal left ideal of the operator algebra is the set of the operators with image inside a fixed line of the module, and each of them is a copy of the module itself, of complex dimension four. The article parametrises the family of these ideals, shows that the copy acts on the family transitively, computes the stabiliser, checks the weight string of one ideal, and reads the identity $\Lambda^{3}V_{3/2}\cong V_{3/2}$ that makes the third exterior power return the module.

**The order of the article.** The ideals and their parametrisation come first; the action of the copy and the stabiliser second. The weight string follows, then the exterior power, and the pairing closes the article.

**It assumes** *The Left Ideals and the Image of a Left Multiplication*, *The Four Weights of the Module and the Half Angle* and *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*. **The row of the elements is** where the minimal left ideals are the lines of a plane; here they are the lines of a three-dimensional projective space, and each ideal is a four-dimensional module.

**The result in one line.** The minimal left ideals are parametrised by the lines of the module, form one orbit of the copy, each is a copy of $V_{3/2}$ with the weight string $\pm\tfrac32,\pm\tfrac12$, and $\Lambda^{3}V_{3/2}\cong V_{3/2}$.

**Boundaries.** The left ideals of the algebra itself are *The Left Ideals and the Image of a Left Multiplication*; the weights are *The Four Weights of the Module and the Half Angle*; the spinor spaces built on the ideals are *Introduction to the Spin-$\tfrac32$ Bispinor Spaces*.

## The Ideals

**Definition.** For a line $\ell$ of the module let $I_\ell$ be the set of the operators whose image is contained in $\ell$.

**Theorem.** Each $I_\ell$ is a minimal left ideal of the operator algebra, of complex dimension four, and every minimal left ideal is of this form.

*Proof.* The set $I_\ell$ is closed under left multiplication by any operator, it is a left ideal, and its dimension is four because an operator with image in a line is determined by the four values on a basis, all landing in that line. It is minimal because a nonzero element of it has image exactly $\ell$ and generates the whole ideal under left multiplication. Conversely a minimal left ideal consists of the operators of rank one with a fixed image line.

**Corollary.** The ideals of the operator algebra are parametrised by the lines of the module, that is, by a projective three-space.

*Proof.* The map $\ell\mapsto I_\ell$ is injective, since distinct lines give distinct ideals, and surjective by the theorem.

**Corollary.** The ideals of the algebra itself are parametrised by the lines of a plane, and each is of complex dimension two.

*Proof.* The same construction with the algebra as a module of dimension two: the lines form a projective line, and each ideal is a copy of the two-dimensional spinor space.

**The reading.** The family of minimal left ideals is a projective space whose points are the spinor spaces, and the passage from the algebra to its operator algebra doubles the dimension of the module and raises the dimension of the family from one to three.

## The Action of the Copy

**Theorem.** The copy acts on the family of ideals by its action on the lines of the module, and the action is transitive.

*Proof.* An element of the copy is an operator, and left multiplication by it carries $I_\ell$ to $I_{g\ell}$ where $g$ is the corresponding linear map of the module; the transitivity is that of the defining action on the lines.

**Corollary.** The family of ideals is a single orbit of the group of the copy, and the orbit map is the projection of the group onto the projective space.

*Proof.* The transitivity, and the identification of the stabiliser as the subgroup preserving a line.

**Corollary.** The stabiliser of one ideal is a parabolic subgroup, of dimension the dimension of the group minus three.

*Proof.* The orbit has dimension three and the orbit-stabiliser count gives the dimension of the stabiliser.

**The reading.** The ideals are the points of one orbit, and the freedom in the choice of an ideal is exactly the freedom in the choice of a line. This is why every construction built on an ideal has to be checked for independence of the line.

## The Weight String

**Theorem.** Each minimal left ideal, as a module for the Cartan generator, has the weight string
$$
\tfrac32,\quad\tfrac12,\quad-\tfrac12,\quad-\tfrac32,
$$
one vector of each weight.

*Proof.* The ideal is isomorphic to the module, since the operator carrying a fixed nonzero element of $\ell$ to itself and the rest to zero is an idempotent whose image is the ideal, and the module is $V_{3/2}$; the weights are those of the module.

**Corollary.** The ideal is multiplicity-free and its four weights sum to zero.

*Proof.* The string of the module.

**Corollary.** The two extreme weights of an ideal are the highest and the lowest weight of the module, and the two middle ones are interchanged by the reflection of the string.

*Proof.* The order of the weights and the symmetry of the string.

**The reading.** Every ideal carries the same string: the choice of the ideal changes the embedding in the operator algebra and not the module structure. A spinor of the operators is therefore a vector of a fixed four-dimensional weight space, wherever the ideal sits.

## The Third Exterior Power

**Theorem.** The third exterior power of the module is isomorphic to the module,
$$
\Lambda^{3}V_{3/2}\cong V_{3/2}\otimes\Lambda^{4}V_{3/2}\cong V_{3/2},
$$
the last isomorphism by a volume form.

*Proof.* The weights of the third exterior power are the sums of three distinct weights of the module, namely $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, which is the same string; the two modules therefore have the same weights and, being simple, are isomorphic.

**Corollary.** The duality of the module with its exterior cube is canonical once a volume form is chosen, and the choice is a scalar.

*Proof.* The isomorphism is the contraction with the volume form.

**Corollary.** The second exterior power is the dual of the module twisted by the volume, and its weights are the negatives of the weights of the module.

*Proof.* $\Lambda^{2}V\cong V^{*}\otimes\Lambda^{4}V$, and the weights of the dual are the negatives.

**The reading.** The third exterior power returns the module because the module has four weights and three of them sum to a weight of the module. The arithmetic of the string is the whole content of the identity, and it is the same arithmetic that makes the module self-dual.

## The Pairing

**Definition.** For a left ideal $I_\ell$ and a right ideal $J_r$ built on a line $r$, the **pairing** is the trace of the product, $\langle S,T\rangle=\operatorname{tr}(ST)$, for $S\in I_\ell$ and $T\in J_r$.

**Proposition.** The pairing is nonzero exactly when the two lines are not orthogonal, and it is a perfect pairing between the two ideals in that case.

*Proof.* The product $ST$ has image in $\ell$ and factors through the quotient by the orthogonal of $r$; the trace sees the diagonal part, which is nonzero exactly when the two lines meet the same functional.

**Corollary.** The pairing of an ideal with its own right partner is nondegenerate, and it is the restriction of the trace form of the operator algebra.

*Proof.* The trace form is nondegenerate on the whole algebra, and the two ideals are complementary in the appropriate sense.

**Corollary.** The weight vectors of the two ideals pair according to the sum of their weights, and the pairing vanishes unless the sums of the two weights is zero.

*Proof.* The trace of a product of two weight vectors is nonzero only when the total weight is zero, since the trace is invariant under the Cartan generator.

**The reading.** The pairing is the trace form read on the two ideals, and it is the operator form of the spinor pairing. It vanishes by weight, and this is what makes the four-dimensional module self-dual: the highest weight pairs with the lowest.

## Further Reading

- [The Left Ideals and the Image of a Left Multiplication](the-left-ideals-and-the-image-of-a-left-multiplication.html), for the ideals of the algebra.
- [The Four Weights of the Module and the Half Angle](the-four-weights-of-the-module-and-the-half-angle.html), for the weight string.
- [The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-the-principal-copy-and-the-kernel.html), for the action of the copy.
- [Introduction to the Spin-$\tfrac32$ Bispinor Spaces](introduction-to-the-spin-three-halves-bispinor-spaces.html), for the spinors built on the ideals.
