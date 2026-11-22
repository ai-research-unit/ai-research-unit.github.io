# __Why the Conjugation Labels Are Integer: the Kernel $\{\pm\mathrm I\}$__

## Introduction

**The subject.** The conjugation action of the copy on the operator algebra has the four labels $3,2,1,0$, all integers, while the left action of the same copy on the same space has no such labels at all. The article explains the integrality: it is the statement that the labels of a conjugation representation are differences of weights of the module, and it has three consequences, the grading of the algebra, the triviality of the sign, and the reality of the conjugation module.

**The order of the article.** The two actions come first; the differences second. The grading follows, then the triviality of the sign, and the reality closes the article.

**It assumes** *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*, *Operators Acting on Two Sides* and *The Four Weights of the Module and the Half Angle*. **The row of the elements is** where the same argument gives the integer labels $1,0$ of the conjugation action on the algebra, and the pattern is the same.

**The result in one line.** Under conjugation the weights are the differences of the weights of the module, hence integers, so the conjugation labels are $3,2,1,0$, the algebra is graded by integers, and the conjugation action carries no sign after a full turn.

**Boundaries.** The conjugation action as a whole is *The Conjugation Action, the Orbits and the Flag Variety*; the decomposition into carriers is *The Clebsch–Gordan Decomposition of the Operators*; the sign is *From the Spin Group to the Spin of a Single Rotor*.

## The Two Actions

**Definition.** The **left action** of the copy on the operator space is $O\mapsto\xi O$; the **conjugation action** is $O\mapsto\xi O-O\xi$, the commutator.

**Proposition.** The left action is the tensor product of the defining module with the trivial action, and the conjugation action is the difference of the two factors:
$$
\xi\cdot_{\mathrm{left}}O=\xi O,\qquad \xi\cdot_{\mathrm{conj}}O=\xi O-O\xi .
$$

*Proof.* The two formulas are the definitions, and the second is the difference of the left and right multiplications.

**Corollary.** The weights of the left action are the weights of the module, each repeated four times, and the weights of the conjugation action are the differences of two weights.

*Proof.* The first action moves only the left factor, the second moves both with opposite signs.

**Corollary.** The left action has half-integer weights and the conjugation action has integer weights, on the same space.

*Proof.* The weights of the module are half-integers, and the differences of half-integers are integers.

**The reading.** The same space carries two actions with different weight characters. The integrality of the second is not a property of the space but of the action: it is the difference that removes the halves.

## The Differences

**Theorem.** If the module has the weights $m_1,\dots,m_r$, then the conjugation action has the weights $m_i-m_j$, and its highest weight is the difference of the highest and the lowest weight of the module.

*Proof.* The commutator acts on the operator $T_{a,b}$ by $\xi a\otimes b-a\otimes \xi b$, which is the difference of the two diagonal actions; the weights are the differences.

**Corollary.** The highest conjugation label is $3$, the difference $\tfrac32-(-\tfrac32)$.

*Proof.* The highest and lowest weights of the module.

**Corollary.** Every conjugation label is an integer, and the labels are the integers from zero to the highest in this case.

*Proof.* The differences of the four half-integers are the half-integer steps of one taken twice, giving integers.

**The reading.** The integrality is a subtraction, and the subtraction is the commutator. A conjugation label counts how many steps of weight separate two states of the module, and a step is one unit, so the count is an integer.

## The Grading

**Proposition.** The algebra of the operators is graded by the integers, the grade of an operator being its weight under the conjugation action.

*Proof.* The commutator with the Cartan element is a derivation, so the product of two homogeneous operators of grades $p$ and $q$ has grade $p+q$; the weights are integers, and the grading follows.

**Corollary.** The algebra has no component of half-integer grade, and its graded pieces have the dimensions of the multiplicities of the differences.

*Proof.* The weights are the differences, and their multiplicities are $4,3,2,1$.

**Corollary.** The left action does not define a grading of the algebra, since its weights are half-integers and the product of two homogeneous elements has half-integer grade not matching the sum of the grades of the modules.

*Proof.* The left action is not a derivation; the left multiplication does not satisfy the Leibniz rule with respect to the weight.

**The reading.** The grading is the algebraic form of the integrality, and it exists only for the action that is a derivation. This is why the conjugation labels are the ones that appear in the algebra's own structure.

## The Triviality of the Sign

**Theorem.** The conjugation action of the rotor of angle $2\pi$ is the identity, and therefore the conjugation representation descends to the rotation group.

*Proof.* The rotor of angle $2\pi$ is the central element $-1$, and the commutator with a central element vanishes.

**Corollary.** No element of the algebra changes sign after a full turn under the conjugation action, while every element of the module does.

*Proof.* The commutator with $-1$ is zero; the left action of $-1$ is minus the identity.

**Corollary.** The conjugation representation has integer labels and the left representation half-integer ones, and the two differ by the kernel of the action.

*Proof.* The kernel of the conjugation action contains $-1$, and the kernel of the left action is trivial.

**The reading.** The integrality and the triviality of the sign are the same statement: a representation with integer labels is a representation of the rotation group, and one with half-integer labels is a representation of the double cover. The algebra is on the first side, its module on the second.

## The Reality of the Conjugation Module

**Proposition.** The conjugation module is real in the sense that its carriers admit real structures, and this is again the integrality of the labels.

*Proof.* The sign of the square of the anti-linear intertwiner of a carrier is $(-1)^{2k}$, which is positive for an integer $k$; hence each carrier admits a real structure.

**Corollary.** The conjugation action can be described without complex numbers, and the left action cannot.

*Proof.* The first has a real form on each carrier; the second has only a quaternionic structure.

**Corollary.** The algebra of the operators is a real object for the conjugation action and a quaternionic one for the left action, on the same underlying space.

*Proof.* The two statements about the types of the carriers and of the module.

**The reading.** Three consequences, one cause: the labels are integers because they are differences, the differences make the sign trivial, and the integer labels make the carriers real. The integrality of the conjugation labels is the reason the algebra can be studied over the reals.

## Further Reading

- [The Conjugation Action, the Orbits and the Flag Variety](the-adjoint-action-the-orbits-and-the-flag-variety.html), for the conjugation action.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the two actions compared.
- [The Quaternionic Structure of the Module: Why $V_{3/2}$ Admits Real Forms](the-quaternionic-structure-of-the-module-and-the-real-forms.html), for the reality of the carriers.
- [The Clebsch–Gordan Decomposition of the Operators](the-clebsch-gordan-decomposition-of-the-operators.html), for the integer labels.
