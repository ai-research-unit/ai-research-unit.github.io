# __The Extraspecial Group of the Two-Sided Operators__

## Introduction

**The subject.** Inside the group of the units of the operator algebra sits a finite subgroup of order eight: the four sign units of the algebra and their negatives, acting by conjugation. That group is the quaternion group, it is extraspecial, and its action on the sixteen lines of the operator space is by the four sign characters. The article computes the group, its presentation, its commutator form, the two types of extraspecial group of that order, and the orbits of its action. It is the finite shadow of the continuous unit group, and every discrete feature of the operator space that survives the passage to a finite group is visible here.

**The order of the article.** The group and its presentation come first; the extraspecial structure and the commutator form second. The two types follow, then the action and its orbits, and the comparison with the continuous group closes the article.

**It assumes** *The One-Sided Operators*, *The Operators of the Peirce Decomposition* and *The Square Roots of One and the Idempotents of the Biquaternion Algebra*. **The row of the elements is** where the eight sign units act on a four-dimensional space; here they act on the sixteen operators, and the action is by signs alone.

**The result in one line.** The eight sign units form the quaternion group of order eight, extraspecial with centre $\{\pm\mathrm{I}\}$ and quotient of order four carrying a nondegenerate alternating commutator form; it acts on the sixteen lines of the operator space by four sign characters, with four classes of four lines.

**Boundaries.** The continuous group of the units is *The One-Sided Operators*; the Peirce blocks on which the group acts are *The Operators of the Peirce Decomposition*; the full adjoint action is *The Adjoint Action, the Orbits and the Flag Variety*.

## The Group

**Definition.** Let $\Gamma$ be the set of the eight elements
$$
\Gamma=\{\pm e_t,\ \pm i\vec e_x,\ \pm i\vec e_y,\ \pm i\vec e_z\},
$$
acting on the operator algebra by conjugation, $O\mapsto L_\gamma OL_\gamma^{-1}$.

**Proposition.** $\Gamma$ is a group under multiplication, isomorphic to the quaternion group of order eight. Its centre is $\{\pm e_t\}$ and its quotient by the centre is the Klein four group.

*Proof.* The four elements $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ multiply by the quaternion rules, with $i\vec e_x\cdot i\vec e_x=-e_t$ and the three imaginary units anticommuting pairwise; the set is closed under multiplication and under inverses. The centre consists of the two scalars, since each imaginary unit anticommutes with the other two, and the four cosets form a group of exponent two.

**Corollary.** The conjugation action of $\Gamma$ has the kernel $\{\pm e_t\}$, so the effective group is of order four.

*Proof.* Conjugation by $\gamma$ and by $-\gamma$ is the same map, since the two sign changes cancel.

**The reading.** The four sign units are the units of the real quaternion subalgebra, and their action by conjugation is the action of the rotations of the three-dimensional space of the vector part. The group is finite, of order eight, and the two signs act identically on the operators: the first sign of a double cover.

## The Extraspecial Structure

**Definition.** A finite $2$-group is **extraspecial** when its centre is of order two and its quotient by the centre is abelian with a nondegenerate alternating commutator form.

**Theorem.** $\Gamma$ is extraspecial of order eight, its centre is $\{\pm e_t\}$, and the commutator form on the quotient is the alternating form of the Klein four group with values in the centre.

*Proof.* The centre has order two by the proposition. The commutator of two imaginary units is twice their product, hence a central element, and it vanishes exactly when the two units are equal up to sign; the form is therefore alternating and nondegenerate on the quotient of order four.

**Corollary.** The commutator form pairs the three imaginary axes, and the three pairings are the three products of the units.

*Proof.* The commutator of $i\vec e_x$ and $i\vec e_y$ is $-2\vec e_x\vec e_y$, a nonzero central element, and the same for the other two pairs.

**The reading.** The commutator of two units of the algebra is a central element, and the central element is the area of the parallelogram they span. This is why the quotient is only of order four: the three-dimensional space of the imaginary units has three pairings, and the form records all three.

## The Two Types

**Proposition.** There are exactly two extraspecial groups of order eight, the quaternion group and the dihedral group, and they are distinguished by the number of involutions: one for the quaternion group and five for the dihedral group.

*Proof.* The centre and the quotient are fixed, and the two possible values of the square of a lifting of a nonzero class of the quotient give the two groups; the involutions are the central element together with the lifts with square the identity, of which there are none in the quaternion case and four in the dihedral case.

**Corollary.** The group of the sign units is of the quaternion type, and no operator construction of this row produces the dihedral type.

*Proof.* Each of the four imaginary units has square $-e_t$, so no lift of a nonzero class is an involution.

**Corollary.** At order thirty-two the same dichotomy recurs, and the invariant that separates the two types is the number of elements of each order, equivalently the value of the Arf invariant of the commutator form.

*Proof.* The two extraspecial groups of order thirty-two have different order statistics, and the invariant is the Arf invariant of the quadratic refinement of the commutator form.

**The reading.** The quaternion type is forced by the algebra: the imaginary units square to minus the identity, and this single fact excludes the dihedral type at every order. The discrete structure of the operator space is therefore of the minus type throughout, and the minus type is the one attached to the quaternion units.

## The Action and the Orbits

**Theorem.** The conjugation action of $\Gamma$ preserves each of the sixteen lines of the operator space and multiplies the line of $T_{e_\mu,e_\nu}$ by the product of two sign characters,
$$
\gamma\,T_{e_\mu,e_\nu}\,\gamma^{-1}=\chi_\mu(\gamma)\,\chi_\nu(\gamma)\,T_{e_\mu,e_\nu}.
$$

*Proof.* Conjugation by an imaginary unit sends each of $e_t$ and the unit on its own axis to itself and the other two units to their negatives; the same holds for the conjugation of the operators, which acts on the two indices separately.

**Corollary.** The sixteen lines fall into four classes of four, according to the pair of characters, and the classes have dimensions four each.

*Proof.* Each index has one of four sign characters, so the pairs fall into sixteen combinations which the two-dimensional character group identifies in classes of four.

**Corollary.** The orbits of the action on the projective operator space are the four classes, and the action on each orbit is through the Klein four group.

*Proof.* The character of a line is constant on a class, and the effective group is the Klein four group.

**The reading.** The finite group does not move the sixteen lines: it multiplies them by signs. The discreteness of the operator space is therefore carried by characters and not by permutations, and the four classes are the finest partition that the finite group sees.

## The Continuous Shadow

**Proposition.** The group of the units of the operator algebra is connected of complex dimension sixteen, and $\Gamma$ is a finite subgroup of it.

*Proof.* The units are the operators of nonzero determinant, an open dense set; the finite group consists of the eight operators of the form $L_\gamma$ composed with the conjugation.

**Corollary.** The orbits of the continuous group are open sets of dimension sixteen, while the orbits of the finite group are the four classes.

*Proof.* The unit group of the operator algebra acts transitively on the operators of a given Jordan type, and its orbits are the similarity classes.

**Corollary.** The finite group detects the sign characters and the continuous group detects the spectrum; the two readings are independent.

*Proof.* The characters are constant on the continuous orbits up to scalar, and the spectrum is invariant under the finite group.

**The reading.** The finite group is a shadow of the continuous one: it keeps the signs and loses the magnitudes. What survives is a group of order eight of the minus type, acting by four characters on sixteen lines, and this is the whole discrete skeleton of the operator space.

## Further Reading

- [The One-Sided Operators](the-one-sided-operators-of-the-biquaternion-algebra.html), for the continuous group of the units.
- [The Operators of the Peirce Decomposition](the-operators-of-the-peirce-decomposition.html), for the blocks on which the group acts.
- [The Square Roots of One and the Idempotents of the Biquaternion Algebra](the-square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the sign units.
- [The Adjoint Action, the Orbits and the Flag Variety](the-adjoint-action-the-orbits-and-the-flag-variety.html), for the continuous orbits.
