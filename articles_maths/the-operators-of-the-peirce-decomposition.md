# __The Operators of the Peirce Decomposition__

## Introduction

**The subject.** An idempotent of the algebra splits it into four pieces, $e\mathbb{B}e$, $e\mathbb{B}f$, $f\mathbb{B}e$ and $f\mathbb{B}f$ with $f=1-e$, and an operator is then a rule carrying each piece into each piece. The article reads the sixteen-dimensional operator space in that splitting. The four pieces are one-dimensional for a primitive idempotent, so the sixteen blocks of the operator space are sixteen lines, and a two-sided operator is a sum of sixteen pieces whose coefficients are the four coordinates of each parameter in the Peirce frame. The operators preserving one piece form a subalgebra of dimension thirteen, and the family of idempotents over which the whole picture moves is two-dimensional.

**The order of the article.** The Peirce splitting comes first, then the blocks of the operator space, then the two-sided operator in those blocks. The preserving subalgebra follows, and the variety of idempotents closes the article.

**It assumes** *The Peirce Decomposition of the Biquaternion Algebra*, *The Square Roots of One and the Idempotents of the Biquaternion Algebra* and *Operators Acting on Two Sides*. **The row of the elements is** where the four Peirce components are computed; here they are the four pieces that an operator carries into one another.

**The result in one line.** A primitive idempotent gives four one-dimensional Peirce components, the operator space becomes sixteen one-dimensional blocks, and a two-sided operator acts on the blocks by the four coordinates of each parameter.

**Boundaries.** The two-sided operators outside the Peirce frame are *The Two-Sided Operators and the Segre Cone*; the adjoint action on the blocks is *The Adjoint Action, the Orbits and the Flag Variety*; the idempotents themselves are *The Square Roots of One and the Idempotents of the Biquaternion Algebra*.

## The Peirce Splitting

**Definition.** For an idempotent $e$ put $f=1-e$ and
$$
\mathbb{B}=e\mathbb{B}e\oplus e\mathbb{B}f\oplus f\mathbb{B}e\oplus f\mathbb{B}f .
$$

**Theorem.** The four Peirce components are subalgebras or bimodules as follows: $e\mathbb{B}e$ and $f\mathbb{B}f$ are algebras with identities $e$ and $f$, and the two off-diagonal components are bimodules over them. For a primitive idempotent each of the four has complex dimension one.

*Proof.* The multiplication respects the four pieces because $e$ and $f$ are orthogonal idempotents summing to the identity, so a product of an element of $e\mathbb{B}f$ with an element of $f\mathbb{B}e$ lands in $e\mathbb{B}e$. For the dimensions, a primitive idempotent of this algebra is a projection onto a line along a complementary line, so each of the four pieces is a line.

**Corollary.** The algebra is the sum of four lines in the Peirce frame of a primitive idempotent, and the multiplication of two elements is read on the four coordinates of each.

*Proof.* The splitting, and the dimensions.

**The reading.** The Peirce frame is a set of four lines depending on a choice of idempotent, and the algebra is read in it as a four-by-four rule with no free space. The frame is not canonical, and the question of how it varies is taken up at the end.

## The Blocks of the Operator Space

**Definition.** For two Peirce components $P_i$ and $P_j$ let $\operatorname{End}_{ij}$ be the set of the operators carrying $P_j$ into $P_i$ and vanishing on the other three components.

**Theorem.** The operator space splits as the direct sum of the sixteen spaces $\operatorname{End}_{ij}$, each of complex dimension one, and the product of an element of $\operatorname{End}_{ij}$ with one of $\operatorname{End}_{kl}$ is zero unless $j=k$, in which case it lies in $\operatorname{End}_{il}$.

*Proof.* Every operator is determined by its sixteen restrictions, one for each ordered pair of the four lines; each restriction is a linear map of a line into a line, hence a scalar; the product rule is the composition of the restrictions.

**Corollary.** The operator algebra is the algebra of the four-by-four rules on the four lines, and its dimension sixteen is the square of the four.

*Proof.* The splitting and the product rule.

**Corollary.** The sixteen basis operators $T_{e_\mu,e_\nu}$ are not the sixteen blocks in general, and the two bases are related by the four coordinates of the Peirce frame.

*Proof.* The Peirce frame is a second basis of the algebra, and the change of basis carries the products of the units to the blocks.

**The reading.** In the Peirce frame the operator space is a square of lines: four lines in, four lines out, one scalar for each pair. This is the block reading of the sixteen, and it depends on the idempotent, unlike the basis of the products of the units.

## The Two-Sided Operator in the Blocks

**Definition.** For an element $a$ written in the Peirce frame as $\sum a_{ij}$ with $a_{ij}\in P_i$, the four coordinates $a_{ij}$ are its **Peirce coordinates**.

**Theorem.** The product operator $T_{a,b}$ has the block entries
$$
(T_{a,b})_{ij}=a_{ik}\,b_{kj}
$$
summed over the intermediate line $k$, and each block entry is the corresponding scalar product of the Peirce coordinates.

*Proof.* Apply the operator to an element of the $j$-th line: the product $aXb$ picks the $k$-th coordinate of $X$ through $b$, and the $i$-th through $a$, so the block is the sum displayed.

**Corollary.** A two-sided operator is decomposable in the blocks exactly when its four-by-four table of entries is the product of two coordinate tables, that is, when the table has rank one.

*Proof.* The entries of the table are the products of the coordinates of the two parameters summed over one index, which is the statement that the table is a product of a column table and a row table.

**Corollary.** The Peirce coordinates of a product vanish in a block exactly when every intermediate coordinate product vanishes.

*Proof.* The sum displayed.

**The reading.** The block form of a two-sided operator is the multiplication of two four-by-four tables of scalars, and the length-one condition is the rank-one condition on that table. The Peirce frame makes the tensor structure of the products look like the multiplication of tables, and it is the only frame in which the block rule is that simple.

## The Preserving Subalgebra

**Definition.** For one of the four lines, the **parabolic** of the frame is the set of the operators carrying that line into itself.

**Theorem.** The parabolic is a subalgebra of complex dimension thirteen, and it contains the sixteen-block algebra of the two complementary pieces.

*Proof.* The condition is the vanishing of the three blocks that carry the line into the other three: three one-dimensional conditions, hence $16-3=13$. A product of two such operators carries the line into itself, so the set is closed under multiplication and contains the identity.

**Corollary.** The parabolic is the stabiliser of a line of the algebra, and the four parabolics of a frame meet in the diagonal algebra of the four lines.

*Proof.* The four conditions together say that every line is carried into itself, which is the diagonal.

**Corollary.** The two-sided operators lying in a parabolic are those whose parameters keep the line inside the corresponding left ideal.

*Proof.* The image of a two-sided operator is contained in the left ideal generated by the left parameter, and the condition of preserving the line is a condition on both parameters.

**The reading.** The parabolic is the operator form of a partial flag: it fixes one line and lets the other three move. Its dimension thirteen is the dimension sixteen minus the three blocks that would move the line, and the four parabolics of a frame form the corners of the block picture.

## The Variety of Idempotents

**Theorem.** The primitive idempotents of the algebra form a complex variety of dimension two: an idempotent is the projection onto a line along a complementary line, and the pairs of a line and a distinct complementary line form a two-dimensional family.

*Proof.* A primitive idempotent has a one-dimensional image and a one-dimensional kernel, and the two determine it; the condition that the image and the kernel meet only at the origin is open, so the family has dimension $1+1=2$.

**Corollary.** The Peirce decomposition varies with the idempotent, and the sixteen blocks are a frame that moves over a two-dimensional parameter space.

*Proof.* The frame is built from the idempotent, and the idempotents form the variety described.

**Corollary.** Two frames are conjugate by a unit exactly when the corresponding idempotents are conjugate, so the frames form one orbit under the group of the units.

*Proof.* The units act transitively on the primitive idempotents, and the conjugacy carries the Peirce frame of one to that of the other.

**The reading.** The block picture is not canonical: it is a chart on a two-dimensional family of frames, and the frames are all conjugate. This is why the Peirce decomposition is a tool and not a structure: it makes the multiplication transparent at the cost of a choice, and the choice is parametrised by the idempotents.

## Further Reading

- [The Square Roots of One and the Idempotents of the Biquaternion Algebra](the-square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the idempotents themselves.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the products read in the blocks.
- [The Adjoint Action, the Orbits and the Flag Variety](the-adjoint-action-the-orbits-and-the-flag-variety.html), for the action that moves the frame.
- [The Two-Sided Operators and the Segre Cone](the-two-sided-operators-and-the-segre-cone.html), for the rank-one condition on the block table.
