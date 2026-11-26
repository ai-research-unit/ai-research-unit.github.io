# __The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$__

## Introduction

**The subject.** Three operators of the sixteen satisfy the brackets of the angular momentum algebra, and they generate a copy of $\mathfrak{su}(2)$ inside $\operatorname{End}(\mathbb{B})$. The algebra, read as a module for that copy, is the third symmetric power of a two-dimensional spinor space, and the group of the copy is the spin group of the module. The article constructs the copy without a frame, identifies the module, computes the kernel of its action, and shows that the construction does not depend on the choice of the spinor space.

**The order of the article.** The copy and its brackets come first; the module and its identification second. The group and the kernel follow, then the independence of the construction, and the reading closes the article.

**It assumes** *The One-Sided Operators*, *The Minimal Left Ideals and the Module $V_{3/2}$* and *The Four Weights of the Module and the Half Angle*. **The row of the elements is** where a copy acts on a two-dimensional spinor space; here the same copy acts on a four-dimensional module, the third symmetric power.

**The result in one line.** The three operators $L_{i\vec e_x},L_{i\vec e_y},L_{i\vec e_z}$ generate a copy of $\mathfrak{su}(2)$, the algebra is $\operatorname{Sym}^{3}S$ for a two-dimensional spinor space $S$, the group of the copy is $\mathrm{SU}(2)$ acting on the module with kernel $\{\pm\mathrm I\}$, and it acts on the algebra through the quotient.

**Boundaries.** The weights of the module are *The Four Weights of the Module and the Half Angle*; the minimal left ideals are *The Minimal Left Ideals and the Module $V_{3/2}$*; the integer labels of the algebra are *The Conjugation Labels Are Integer*.

## The Copy

**Definition.** Put $\xi_x=L_{i\vec e_x}$, $\xi_y=L_{i\vec e_y}$, $\xi_z=L_{i\vec e_z}$, the operators of left multiplication by the three imaginary units, and let $\mathfrak{g}$ be their complex span.

**Theorem.** The three operators satisfy
$$
[\xi_x,\xi_y]=-2\xi_z,\qquad [\xi_y,\xi_z]=-2\xi_x,\qquad [\xi_z,\xi_x]=-2\xi_y,
$$
so that $\mathfrak{g}$ is a copy of $\mathfrak{sl}_2(\mathbb{C})$ inside the operator algebra, and the real span of $i\xi_x,i\xi_y,i\xi_z$ is a copy of $\mathfrak{su}(2)$.

*Proof.* The left multiplications satisfy $[L_a,L_b]=L_{[a,b]}$ because they are a representation of the algebra, and the commutator of the imaginary units is twice the third one: $[i\vec e_x,i\vec e_y]=-2\vec e_x\vec e_y=-2 i\vec e_z$ after multiplication by $i$. The reality statement follows from the anti-Hermitian character of the three operators.

**Corollary.** The copy acts on the algebra by operators of trace zero, and its three generators are anti-Hermitian for the trace form.

*Proof.* Each $\xi$ is a left multiplication by a purely imaginary element, hence anti-Hermitian; the trace of a commutator is zero.

**The reading.** The copy is reached without any frame: the three imaginary units are canonical up to the rotation of the vector part, and the three left multiplications inherit that freedom. Every statement below is invariant under the rotation, and the copy is determined by the algebra alone.

## The Module

**Theorem.** Let $S$ be a minimal left ideal of the algebra, of complex dimension two. Then the algebra, as a module for the copy by left multiplication, is isomorphic to the third symmetric power,
$$
\mathbb{B}\cong\operatorname{Sym}^{3}S,
$$
and the isomorphism is canonical up to the choice of $S$.

*Proof.* The minimal left ideal $S$ is a copy of the two-dimensional spinor space, and left multiplication by the algebra on itself is, in the identification of the algebra with the endomorphisms of $S$ promoted to the symmetric cube, the natural action on $\operatorname{Sym}^{3}S$. The dimensions agree, $4=\binom{3+1}{3}$, and the highest weight of the module is $\tfrac32$, which is the third symmetric power of the defining two-dimensional module.

**Corollary.** The module is multiplicity-free, with the four weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ occurring once each.

*Proof.* The symmetric cube of a two-dimensional module has a basis of monomials of degree three, and the weights are the sums of three weights of $S$, each equal to $\pm\tfrac12$.

**Corollary.** The sixteen operators, as a module for the copy by left multiplication, decompose as $\tfrac32\otimes\tfrac32$, with four summands of dimensions seven, five, three and one.

*Proof.* The operator algebra is the tensor square of the module, and the Clebsch–Gordan rule for the tensor square of the highest weight $\tfrac32$ gives the four summands.

**The reading.** The module is four-dimensional and its label is $\tfrac32$; the operators add the second factor and produce the four integer labels. The passage from the elements to the operators is the passage from $S$ to $\operatorname{Sym}^{3}S$ and then to its tensor square.

## The Group and the Kernel

**Definition.** The **spin group** of the module is the group of the copy, the exponentials of the real Lie algebra $\mathfrak{su}(2)$, acting on the algebra by left multiplication.

**Theorem.** The group is isomorphic to $\mathrm{SU}(2)$, its action on the module has kernel $\{\pm\mathrm I\}$, and its action on the algebra by conjugation has trivial kernel.

*Proof.* The exponentials of $\mathfrak{su}(2)$ form $\mathrm{SU}(2)$. The element $-\mathrm I$ is the exponential of a full turn and acts as minus the identity on every module of half-integer label, in particular on $\operatorname{Sym}^{3}S$; it is the only element acting trivially up to sign. On the algebra, the action is by conjugation, and $-\mathrm I$ conjugates every operator to itself, so it acts trivially on the algebra.

**Corollary.** The action on the module factors through $\mathrm{SO}(3)$, and the action on the algebra factors through the same quotient; the two actions differ only by the kernel.

*Proof.* The kernel of the module action is $\{\pm\mathrm I\}$, and the quotient by it is the rotation group.

**Corollary.** The group of the copy is a double cover of the rotation group of the vector part, and the cover is non-trivial because the module changes sign after a full turn.

*Proof.* The two elements $\pm\mathrm I$ map to the identity rotation, and the module distinguishes them.

**The reading.** The kernel is the whole difference between the two readings. The algebra cannot see the sign, because conjugation by a scalar is the identity; the module sees it, because left multiplication by minus one is minus the identity. Every integer label of the algebra and every half-integer label of the module follows from this single fact.

## The Independence of the Choice

**Theorem.** Any two minimal left ideals of the algebra are conjugate by a unit, and the isomorphism $\mathbb{B}\cong\operatorname{Sym}^{3}S$ does not depend on the choice of $S$ up to that conjugacy.

*Proof.* Two minimal left ideals are the images of two primitive idempotents, and the unit group acts transitively on the primitive idempotents; conjugating one idempotent to the other carries its ideal to the other ideal, and the two isomorphisms differ by the conjugacy.

**Corollary.** The copy, the module and the group are attached to the algebra and not to a choice of spinor space.

*Proof.* The copy is spanned by the three left multiplications, which are defined without a choice; the module is the algebra itself; and the group is the group of the copy.

**Corollary.** The family of minimal left ideals is a projective space, and every member of the family gives the same four weights.

*Proof.* The ideals are parametrised by the lines of the module, and the weights are those of the module, independent of the line.

**The reading.** The construction has one free choice, the spinor space, and the choice is a point of a projective space. The copy, the weights, the group and the kernel do not depend on it, and this is what makes the spin of the operators a property of the algebra rather than of a frame.

## Further Reading

- [The Minimal Left Ideals and the Module $V_{3/2}$](the-minimal-left-ideals-and-the-module.html), for the spinor spaces.
- [The Four Weights of the Module and the Half Angle](the-four-weights-of-the-module-and-the-half-angle.html), for the weights.
- [The Clebsch–Gordan Decomposition of the Operators](the-clebsch-gordan-decomposition-of-the-operators.html), for the decomposition of the sixteen.
- [The One-Sided Operators](the-one-sided-operators-of-the-biquaternion-algebra.html), for the left multiplications generating the copy.
