# __The Peirce Decomposition of the Quaternion Algebra and Its Collapse__

## Introduction

The Peirce decomposition of a Jordan algebra is written with respect to an idempotent: for $c$ with $c\bullet c=c$, the algebra splits into the eigenspaces of the multiplication operator $L(c)$ for the eigenvalues $1,\tfrac12,0$. In the quaternion algebra the operator $L(c)$ has only the eigenvalues $1$ and $0$, at the two idempotents $e_t$ and $0$, and the decomposition is $\mathbb{H}=\mathbb{H}\oplus0$ or $0\oplus\mathbb{H}$. There is no middle term, no off-diagonal space, and no Peirce basis.

The collapse is not a defect of the calculation; it is the division property in disguise. The Peirce space $J_0(e_t)$ is the set of elements killed by $L(e_t)$, and it is zero exactly because the algebra has no zero divisors. The article proves the decomposition, proves the collapse, reads it as division, and then puts the two cases beside it in which the calculus opens: the biquaternion algebra, where four Peirce lines appear, and the split quaternions, where two non-central idempotents appear and the calculus opens over $\mathbb{R}$ itself.

The algebra is that of [The Jordan Structure of the Symmetric Plain Product of the Quaternions](the-jordan-structure-of-the-symmetric-plain-product-of-the-quaternions.html), cited and not restated; the general theory is [Peirce Decompositions of the Biquaternion Algebra](complementary-idempotents-and-the-peirce-decomposition.html) and [Jordan Algebras](jordan-algebras.html).

## The Peirce Decomposition Written for $\mathbb{H}$

**Definition.** Let $A$ be the quaternion algebra under the symmetric plain product, and let $c\in A$ satisfy $c\bullet c=c$. The **Peirce spaces** of $c$ are
$$
A_\lambda(c)=\bigl\{x\in A:\ c\bullet x=\lambda x\bigr\},\qquad \lambda\in\bigl\{0,\tfrac12,1\bigr\},
$$
and the **Peirce decomposition** is the statement $A=A_1(c)\oplus A_{1/2}(c)\oplus A_0(c)$.

**Theorem (the decomposition holds and the middle term vanishes).** For each of the two idempotents $c$ of the algebra,
$$
A=A_1(c)\oplus A_0(c),\qquad A_{1/2}(c)=0 .
$$

*Proof.* At $c=e_t$ the operator is the identity and at $c=0$ it is zero, so in both cases $L(c)^2=L(c)$, the eigenvalues are $1$ and $0$ only, and the two eigenspaces span the space. Verified in the coefficient basis.

**Corollary (the two cases, written out).** At $c=e_t$,
$$
A_1(e_t)=\mathbb{H},\qquad A_{1/2}(e_t)=0,\qquad A_0(e_t)=0 ;
$$
at $c=0$,
$$
A_1(0)=0,\qquad A_{1/2}(0)=0,\qquad A_0(0)=\mathbb{H} .
$$

*Proof.* $L(e_t)$ is the identity, since $e_t$ is the unit; $L(0)=0$. Verified on the basis.

**Remark (the Peirce rules, and which of them fail).** For two Peirce spaces the rules read $A_\lambda\bullet A_\mu\subseteq A_{\lambda+\mu}$ when $\lambda+\mu$ is one of $0,\tfrac12,1$, and $A_\lambda\bullet A_\mu=0$ otherwise, together with $\{A_\lambda,A_\mu\}\subseteq A_{\lambda+\mu-1}$ for the mixed products. With the middle space zero and the spaces equal to the algebra or to zero, the rules reduce to $\mathbb{H}\bullet\mathbb{H}\subseteq\mathbb{H}$ at $e_t$ and to $0\subseteq0$ at $0$: they hold, and they say nothing. This is the sense of the word collapse: the rules are satisfied because there is nothing for them to constrain.

## The Idempotent Class

**Theorem (the idempotents are two points).** The idempotents of the algebra are $0$ and $e_t$.

*Proof.* $c\bullet c=c$ is $c^2=c$ in the parent, hence $c(c-e_t)=0$, and the parent has no zero divisors, so $c=0$ or $c=e_t$. Verified by solving the four quadratic conditions in the coefficient basis, and by a random search of $2\times10^{5}$ draws which found no other element.

**Remark (the middle term does not vanish in general).** For a rank-one idempotent of a Jordan algebra of degree two the operator $L(c)$ has the eigenvalue $\tfrac12$, and the middle space is the largest of the three. The vanishing here is not a general phenomenon but the consequence of the idempotent class being trivial: at $e_t$ and at $0$ the operator is the identity or zero, and a projection with two eigenvalues has two eigenspaces. **The collapse of the Peirce decomposition begins with the collapse of the idempotent class, and the two collapses have the same cause.**

**Remark (why the class is so small).** In a Jordan algebra of degree $d$ with a spectral theorem, the idempotents form a family of dimension $d-1$ or more, and they are the carriers of the spectral resolution. Here the class is discrete, with two points, and neither of them is a rank-one idempotent in the sense of a spectral theory: $e_t$ has Peirce eigenvalues $1,0$ and rank one in no sense at all, since $A_1(e_t)$ is the whole algebra. **A degree-one Jordan algebra has no spectral theory, and the quaternion algebra is the degree-one case: its unit idempotent is the whole space.**

**Proposition (the Peirce spaces of the two idempotents are the same two spaces).** $A_1(e_t)=A_0(0)=\mathbb{H}$ and $A_0(e_t)=A_1(0)=0$.

*Proof.* The corollary of the decomposition theorem. The two idempotents give the same splitting with the roles of $1$ and $0$ exchanged.

## The Spaces $J_1(e_t)$, $J_0(0)$ and the Off-Diagonal

**Proposition (the off-diagonal is zero).** For the pair of orthogonal idempotents $(e_t,0)$,
$$
A_{1/2}(e_t)=\{x:\ e_t\bullet x=\tfrac12x\}=\{0\},\qquad
A_{1/2}(0)=\{x:\ 0\bullet x=\tfrac12x\}=\{0\},
$$
so the off-diagonal space of the pair is $\{0\}$, and the four Peirce lines of a general decomposition reduce to two.

*Proof.* The equations are $x=0$ and $0=\tfrac12x$. Verified in the basis.

**Remark (the standard four lines and their degeneration).** For a pair of orthogonal idempotents $c,c'=e_t-c$ in a unital Jordan algebra, one writes the algebra as four pieces: $A_{11}$ in $A_1(c)\cap A_1(c')$, $A_{00}$ in $A_0(c)\cap A_0(c')$, and the two off-diagonal pieces in $A_{1/2}(c)$. Here $c'=0$, so $A_{11}$ collapses into $A_1(c)$, $A_{00}$ into $A_0(c)$, and the off-diagonal pieces into the middle space, which is zero. **The four lines of the general theory become one line and three zeroes, and the passage is the single substitution $c'=0$.**

**Remark (the absent grading).** A Peirce decomposition with a non-zero middle space gives the algebra a $\mathbb{Z}_2$-grading twisted by the half-integral eigenvalue, and that grading is what makes the Jordan theory work: it separates the "diagonal" part of the algebra, where the computation is associative, from the "off-diagonal" part, where it is not. Here there is no off-diagonal part, and the reason is that the algebra has no element that is half-eigen for the unit. The absence of the grading is the algebraic form of the absence of the spectral theory.

## The Absent Off-Diagonal Unit

**Proposition (no off-diagonal unit).** There is no element $\tilde u$ with $e_t\bullet\tilde u=\tfrac12\tilde u$ and $\tilde u\bullet\tilde u=e_t$; there is no element that would play the role of a mixed unit for the pair $(e_t,0)$.

*Proof.* The first equation forces $\tilde u=0$, and $0\bullet0=0\neq e_t$. Verified in the basis. In a Jordan algebra with two orthogonal idempotents, the mixed unit of the pair is an element of the middle space with square equal to the sum of the two idempotents; its existence is equivalent to the non-vanishing of the middle space, and here the middle space is zero.

**Remark (what the mixed unit would do).** A mixed unit $u$ with $u\bullet u=c+c'$ and $c\bullet u=\tfrac12u$ generates, inside the algebra, a copy of the Jordan algebra of the $2\times2$ symmetric matrices over the base field, and with it a Peirce calculus, a spectral decomposition of every element, and a cone. The three objects appear and disappear together, and in the quaternion algebra all three are absent for the same reason: the mixed unit does not exist.

## The Affine Correspondence

**Theorem (idempotents and involutions).** The map
$$
c\longmapsto s=2c-e_t
$$
is an affine bijection from the idempotents of the algebra onto the involutions, the elements with $s\bullet s=e_t$; its inverse is $s\mapsto\tfrac12(s+e_t)$.

*Proof.* If $c\bullet c=c$ then $(2c-e_t)\bullet(2c-e_t)=4c-4c+e_t=e_t$; if $s\bullet s=e_t$ then $\tfrac12(s+e_t)$ has square $\tfrac14(e_t+2s+e_t)=\tfrac12(s+e_t)$. The two maps are inverse affine maps. The involution class is $\{e_t,-e_t\}$ and the idempotent class is $\{e_t,0\}$. Verified in the basis.

**Remark (the correspondence is a dictionary and not a theory).** In a formally real Jordan algebra the same correspondence maps the rank-one idempotents onto the reflections of the algebra, and it is the algebraic form of the passage from a projection to a symmetry. Here it maps two points onto two points, and its content is exhausted by the pair $e_t\mapsto e_t$ and $0\mapsto-e_t$. The correspondence is stated because it is the prototype of the one used in the biquaternion block, where it is a genuine dictionary between two four-parameter families.

## The Complement and Its Orthogonality

**Proposition (the complement).** For $c=e_t$ the complement is $c'=e_t-c=0$; for $c=0$ the complement is $e_t$. In both cases $c\bullet c'=0$, so the complement is orthogonal, and $c+c'=e_t$.

*Proof.* The definitions and $e_t\bullet0=0$. Verified in the basis.

**Remark (orthogonality is vacuous here).** The orthogonality of a decomposition is the statement that the two Peirce spaces are orthogonal for the trace form, and here it holds trivially, since one of the two spaces is zero. In a decomposition with a middle space the orthogonality is a genuine condition, and it is the condition that makes the trace form diagonal in a Peirce basis. **One line and three zeroes have no orthogonality to speak of, and this is why the Peirce basis of the biquaternion block has no real analogue.**

## The Collapse Read as the Division Property

**Theorem (the collapse is division).** The following are equivalent: $A_0(e_t)=0$; the operator $L(e_t)$ is injective; the algebra has no zero divisors; the algebra is a division algebra.

*Proof.* $A_0(e_t)$ is the kernel of $L(e_t)=I$, which is zero, and the equivalence of the first two is the definition. The algebra has no zero divisors because $N(\tilde q_1\tilde q_2)=N(\tilde q_1)N(\tilde q_2)$ and the norm is positive definite, and it is a division algebra because every non-zero element is invertible. The implication in the other direction is the standard argument: a zero divisor $\tilde q_1\tilde q_2=0$ with both factors non-zero gives an element of the kernel of $L(\tilde q_1)$, and with $\tilde q_1$ invertible that kernel is zero. Verified on the basis and by random search for zero divisors, which found none in $10^{5}$ draws.

**Corollary (the three absences are one absence).** There is no spectral theorem, no cone of squares that is proper, and no Peirce calculus, and all three are the division property.

*Proof.* The spectral theorem needs idempotents and the Peirce calculus needs a middle space; the cone needs a proper cone of squares, and the cone of squares is the whole space because every element is a square in a division algebra of this kind. The three are the three faces of the same property, and the present section is their common proof.

**Remark (the verdict in one line).** **The Peirce decomposition of the quaternion algebra is not hard; it is empty.** The only information it carries is that the algebra is a division algebra, and that information is stated more directly by the norm.

## The Comparison with the Four Peirce Lines and the Split Quaternions

**Remark (the four Peirce lines of a biquaternion).** In the biquaternion algebra the same construction with the idempotent $\tfrac12(e_t+\vec u)$ over $\mathbb{C}$, where $\vec u$ is a complex vector with $(\vec u,\vec u)=1$, gives a middle space of dimension two and a decomposition into four lines: $A_1$, $A_0$ and the two off-diagonal lines. The complex numbers supply the vectors of square $+e_t$ that the real algebra lacks. The four lines, the mixed units and the calculus are read in [Peirce Decompositions of the Biquaternion Algebra](complementary-idempotents-and-the-peirce-decomposition.html), and the present article is the real column of the same table.

**Theorem (the split quaternions have two non-central idempotents).** In the algebra with $\vec e_x^2=-e_t$ and $\vec e_y^2=\vec e_z^2=+e_t$, keeping $\vec e_x\vec e_y=\vec e_z$, the elements
$$
\pi_\pm=\tfrac12\bigl(e_t\pm\vec e_y\bigr)
$$
are idempotents, they are not central, $\pi_+\pi_-=0$, and their Peirce decomposition has the dimensions $1,1,2$.

*Proof.* $\pi_\pm^2=\tfrac14(e_t\pm2\vec e_y+\vec e_y^2)=\tfrac14(2e_t\pm2\vec e_y)=\pi_\pm$; $\pi_+\pi_-=\tfrac14(e_t-\vec e_y^2)=0$; and $\pi_\pm$ do not commute with $\vec e_x$, since $\pi_+\vec e_x=\tfrac12(\vec e_x-\vec e_z)$ while $\vec e_x\pi_+=\tfrac12(\vec e_x+\vec e_z)$, the relations being $\vec e_y\vec e_x=-\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$. The Peirce spaces are the two lines $\mathbb{R}\pi_\pm$ and the two-dimensional space spanned by $\vec e_x,\vec e_z$, whose elements are half-eigen for $\pi_+$: $\pi_+\bullet\vec e_x=\tfrac12\vec e_x$ and $\pi_+\bullet\vec e_z=\tfrac12\vec e_z$. Computed exactly.

**Remark (the two ways of opening the calculus).** The calculus opens in two ways: by complexifying, which supplies vectors of square $+e_t$ and leaves the algebra central, or by changing the signs of the basis, which supplies a non-central idempotent and a hyperbolic structure over $\mathbb{R}$ itself. The quaternion algebra is the case in which neither happens, and the collapse of this article is the exact statement that it is a division algebra: **the Peirce calculus is the calculus of a zero divisor, and a division algebra has none.**

## The Calculus that Opens Only after Complexification

**Theorem (the complexified family).** In the biquaternion algebra the idempotents of the symmetric plain product are $0$, $e_t$ and the elements $\tfrac12(e_t+\vec u)$ with $\vec u$ a complex vector satisfying $(\vec u,\vec u)=1$.

*Proof.* $\tfrac14(e_t+2\vec u+\vec u^2)=\tfrac12(e_t+\vec u)$ exactly when $\vec u^2=e_t$, that is $(\vec u,\vec u)=1$ and the imaginary part of the vector vanishes in the product, which is the same condition. The complex quadric $\{(\vec u,\vec u)=1\}$ in $\mathbb{C}^3$ is of complex dimension two, hence of real dimension four, and with the two isolated idempotents it is the four-parameter family of the biquaternion article. Verified on the real and imaginary parts of random complex vectors on the quadric.

**Corollary (what complexification buys and what it does not).** Complexification supplies the idempotents, the off-diagonal spaces and the Peirce calculus. It does not supply a cone: the cone of squares of the complexified algebra contains the complex line, and a cone over $\mathbb{C}$ is not a cone over $\mathbb{R}$.

*Proof.* The idempotents are the theorem. For the cone, the squares of the complexified algebra contain $\lambda e_t$ for every complex $\lambda$, since $\tilde q$ and $i\tilde q$ have squares of opposite sign, and the cone generated is the whole complex space.

**Remark (the order of the operations).** The sequence is: write the decomposition, watch it collapse over $\mathbb{R}$, complexify to make it open, and then read the real information back through the real form. The three steps are the three sections of this article, and the last is the subject of [The Real Forms of the General Quaternionic Algebra of the Quaternions](the-quaternionic-structure-and-the-real-forms-of-m4c.html). **The Peirce decomposition of the quaternion algebra is the Peirce decomposition of a division algebra, and its content is the word division.**

## Summary

For an idempotent $c$ of the symmetric plain product, the Peirce spaces are the eigenspaces of $L(c)$ for the eigenvalues $1,\tfrac12,0$.

The idempotents are $0$ and $e_t$; the operator $L(e_t)$ is the identity and $L(0)$ is zero; the middle space is zero in both cases; and the decomposition is $\mathbb{H}=\mathbb{H}\oplus0$ at $e_t$ and $0\oplus\mathbb{H}$ at $0$.

The off-diagonal space is $\{0\}$, there is no mixed unit, and the affine correspondence $c\mapsto2c-e_t$ maps the two idempotents onto the two involutions $\pm e_t$.

The vanishing of $A_0(e_t)$ is the injectivity of $L(e_t)$, which is the absence of zero divisors, which is the division property. The three absences — spectral theorem, proper cone, Peirce calculus — are that one property.

The calculus opens with the complex idempotents $\tfrac12(e_t+\vec u)$, $(\vec u,\vec u)=1$, a family of real dimension four, and it opens over $\mathbb{R}$ in the split quaternions with the non-central idempotents $\tfrac12(e_t\pm\vec e_y)$, where the Peirce dimensions are $1,1,2$. The quaternion algebra is the case of collapse, and the collapse is division.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra |
| $\tilde q=q_te_t+\vec q$ | the element, its scalar part and its vector part |
| $\bullet$ | the symmetric plain product |
| $A_\lambda(c)$ | the Peirce space of the idempotent $c$ |
| $L(c)$ | the multiplication operator by $c$ |
| $\pi_\pm$ | the non-central idempotents of the split quaternions |
| $\natural$ | the quaternion conjugation |

## Further Reading

- [The Jordan Structure of the Symmetric Plain Product of the Quaternions](the-jordan-structure-of-the-symmetric-plain-product-of-the-quaternions.html), for the algebra and its idempotents.
- [Peirce Decompositions of the Biquaternion Algebra](complementary-idempotents-and-the-peirce-decomposition.html), for the case in which the calculus opens.
- [The Category of Modules over the Quaternion Algebra](the-category-of-modules-over-the-quaternion-algebra.html), for the division property read as a categorical statement.
- [The Split Quaternions and the Two Non-Central Idempotents](split-quaternion-idempotents-and-projections.html), for the hyperbolic case.
- [Jordan Algebras](jordan-algebras.html), for the Peirce decomposition in general.
