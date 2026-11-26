# __The Conjugation Labels at $n=4$: Integers $0,1,2,3$ from the Kernel__

## Introduction

**The subject.** The copy acts on the algebra by conjugation and the algebra decomposes into four integer-labelled carriers, while the copy acts on the module by the spin representation and the module has the half-integer label $\tfrac32$. The article proves both statements from one computation: the kernel of the conjugation action is $\{\pm\mathrm I\}$, so the conjugation action is an action of $SO(3)$, and the labels of an action of $SO(3)$ are integers.

**The order of the article.** The first section identifies the kernel. The second shows that the quotient is $SO(3)$ and that the algebra is an honest representation of it. The third proves that the labels are integers, once from the group and once from the weights. The fourth treats the odd orders, where the module descends as well. The fifth draws the boundary.

**It assumes** *The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$* for the copy, and *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$*. The row at order two is *The Conjugation Labels Are Integer*.

**The result in one line.** $\ker\Phi=\{\pm\mathrm I\}$, the conjugation action factors through $SO(3)$, and every label of an $SO(3)$-module is an integer, so the carriers have the labels $0,1,2,3$.

**Boundaries.** The article uses the weights of the module without recomputing them, and it does not treat the spin group beyond the kernel; the double cover is the subject of the article on the spin group.

## The Kernel

**Theorem.** $\ker\Phi=\{\pm\mathrm I\}$, where $\Phi_q(X)=\rho(q)X\rho(q)^{-1}$.

*Proof.* If $\Phi_q$ is the identity then $\rho(q)$ commutes with every matrix, hence is a scalar $\lambda\mathrm I$. The eigenvalues of $\rho(q)$ are $\lambda^{2j},\lambda^{2j-2},\dots,\lambda^{-2j}$; all equal forces $\lambda^{2j}=\lambda^{2j-2}$, that is $\lambda^{2}=1$, so $\lambda=\pm1$. The scalars in the image of $\rho$ are therefore $\pm\mathrm I$, and $\rho(-1)=(-1)^{2j}\mathrm I=-\mathrm I$ at $2j=3$, so the kernel is exactly $\{\pm\mathrm I\}$.

**Corollary.** The kernel is the centre of the copy, and it has two elements.

*Proof.* The centre of $SU(2)$ is $\{\pm\mathrm I\}$, and both elements act trivially by conjugation because a scalar commutes with everything.

**Corollary.** $\Phi$ is not faithful, and $\rho$ is faithful at $n=4$ because $\rho(-1)=-\mathrm I\neq\mathrm I$.

*Proof.* The kernel of $\Phi$ is nontrivial and contains the kernel of $\rho$; $\rho(-1)=-\mathrm I$.

**The reading.** The loss of faithfulness is exactly the loss of the sign of a spinor: the copy and its quotient by $\pm1$ act alike on the algebra, and the module distinguishes them.

## The Quotient

**Proposition.** $SU(2)/\{\pm\mathrm I\}\cong SO(3)$, and the conjugation action of the copy on the algebra factors through this quotient.

*Proof.* The adjoint representation of $SU(2)$ on its Lie algebra is the conjugation action on the three-dimensional space of traceless anti-Hermitian matrices; its kernel is $\{\pm\mathrm I\}$ and its image is $SO(3)$, by the double cover of the rotation group.

**Corollary.** The algebra is a representation of $SO(3)$, and its four carriers are the $SO(3)$-modules of labels $0,1,2,3$.

*Proof.* The action factors through the quotient, and the carriers are the isotypic pieces.

**Corollary.** Two elements of the copy differing by sign act identically on the algebra.

*Proof.* The factorisation.

## The Labels Are Integers

**Proposition.** Every irreducible representation of $SO(3)$ has an integer label.

*Proof.* The representations of $SO(3)$ are the representations of $SU(2)$ on which $-\mathrm I$ acts trivially; on $V_j$ the element $-\mathrm I$ acts by $(-1)^{2j}$, so the representation descends exactly when $2j$ is even, that is when $j$ is an integer.

**Corollary.** The carriers' labels are integers, and the module's label $\tfrac32$ is not.

*Proof.* The carriers are $SO(3)$-modules, hence have integer labels; $\tfrac32$ is not an integer.

**Corollary.** The algebra has no carrier of label $\tfrac32$, and the total dimension is $1+3+5+7=16$.

*Proof.* The labels are $0,\dots,2j$ and the dimensions add.

**The second proof from weights.** The algebra's weights are differences of the module's weights, the module's weights are congruent to $\tfrac12$ modulo one, so the differences are integers; a module with integer weights has an integer label.

*Proof.* The weights of $V_{3/2}$ are $\pm\tfrac32,\pm\tfrac12$, and the difference of two of them is an integer.

**The reading.** The two proofs are the group-theoretic and the weight-theoretic face of one fact: the conjugation action sees only the quotient by the sign, and the sign is what makes a label half-integral.

## The Odd Orders

**Proposition.** At odd $n$ the module's label is an integer, $-\mathrm I$ acts trivially on the module, and the module descends to $SO(3)$; the kernel of $\Phi$ is still $\{\pm\mathrm I\}$.

*Proof.* $2j=n-1$ is even, so $\rho(-\mathrm I)=(-1)^{2j}\mathrm I=\mathrm I$ and the representation descends; the computation of the theorem does not use the parity of $2j$ and gives $\{\pm\mathrm I\}$ at every order.

**Corollary.** At odd order the module is one of the carriers and the sign of a spinor is not seen; at even order the module is not a carrier and the sign is seen on the module only.

*Proof.* The integer label at odd order makes the module a carrier; at even order the label is a half-integer and the module is not a carrier.

**Corollary.** The phrase "the conjugation labels stay integer" is a statement about the quotient and not about the order; what changes with the order is whether the module descends.

*Proof.* The theorem holds at every order, and the descent depends on the parity of $2j$.

## The Boundary

**Against the spin group article.** That article proves the double cover and computes $\operatorname{Sym}^3$; this one uses the kernel to explain the integrality of the labels. The two computations agree on $\{\pm\mathrm I\}$.

**Against the half-integer article.** That article follows the half-integer into the weights; this one explains why the algebra's labels are integers in the first place.

**Against the odd order.** The statements at odd order are made separately, because the module's descent changes and the labels do not.

## The Two Values of the Indicator

**The trichotomy.** An irreducible representation of the copy is of real, complex or quaternionic type according to the value $+1$, $0$ or $-1$ of the indicator; the module of half-integer label is quaternionic and the carriers of integer label are real, and no carrier of this algebra is of complex type.

**The sign rule.** The indicator is $(-1)^{2j}$, so the two cases alternate with the parity of twice the label; the module has twice the label equal to an odd integer and the carriers have it even, which is the whole content of the rule.

**The consequence for the forms.** A real type carrier has an invariant symmetric bilinear form and a real structure; a quaternionic module has an invariant alternating form and an anti-linear map with square $-1$; the forms of the carriers and of the module are therefore different in kind, not only in value.

**The reading.** The integrality of the labels is the arithmetic shadow of the trichotomy, and it decides which invariant forms exist at each order.

## Summary

The kernel of the conjugation action of the copy on the algebra is $\{\pm\mathrm I\}$: an element acting trivially must act by a scalar, and the eigenvalues of that scalar on the module force it to be $\pm1$. The quotient is $SO(3)$, and the algebra is an $SO(3)$-module.

Every irreducible $SO(3)$-module has an integer label, because the modules of $SU(2)$ descend exactly when $-\mathrm I$ acts trivially, which is the case of even $2j$. Hence the carriers have the labels $0,1,2,3$, of total dimension sixteen, and the module's label $\tfrac32$ is not a carrier label.

At odd orders the module descends as well and is a carrier; the kernel remains $\{\pm\mathrm I\}$ and the integrality of the labels is unchanged.


**The place in the corpus.** The integrality of the labels is the reason the algebra has invariant symmetric bilinear forms on every carrier and the module has none, and it is the same sign rule that decides the quaternionic structure of the module and the real structure of the carriers; the argument is a single evaluation of the centre of the copy on the highest weight.
## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi_q(X)=\rho(q)X\rho(q)^{-1}$ | the conjugation action |
| $\ker\Phi=\{\pm\mathrm I\}$ | the kernel |
| $SU(2)/\{\pm\mathrm I\}\cong SO(3)$ | the quotient |
| $(-1)^{2j}$ | the sign by which $-\mathrm I$ acts on $V_j$ |
| $0,1,2,3$ | the integer labels of the carriers |

## Further Reading

- [The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-at-n-4-the-principal-copy-and-its-kernel.html), for the copy.
- [Four Integer Labels and One Half-Integer Module: $\tfrac32$ Is a Weight, Not a Label](four-integer-labels-and-one-half-integer-module.html), for the half-integer.
- [No Half-Integer Summand at $n=4$: Four Requirements Fail Together](no-half-integer-summand-at-n-4.html), for the obstruction.
- [The Conjugation Labels Are Integer](the-conjugation-labels-are-integer.html), for the row at order two.
- [The Slot and the Summand at $n=4$](the-slot-and-the-summand-at-n-4.html), for the vocabulary.
