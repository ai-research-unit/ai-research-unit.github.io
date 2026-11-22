# __The Spin-One Carrier and the Spectral Strata__

## Introduction

**The subject.** An element of the triplet acts on the triplet by the bracket, and the spectrum of that action has three values that sum to zero. This article computes the spectrum, proves that the characteristic polynomial is even, describes the two spectral strata, places the triplet spectrum inside the spectrum of the whole operator space, and passes to the group.

**The order of the article.** *The Spectrum on the Triplet* proves the shape $(\lambda,0,-\lambda)$. *Three Values or One* describes the strata. *The Discriminant* computes the polynomial that cuts them and shows that it is even. *The Part Inside the Big Spectrum* places the triplet inside the sixteen eigenvalues. *The Trace and the Constraint* reads the vanishing of the trace. *Passage to the Group* exponentiates.

**It assumes** *The Spin-One Carrier: the Adjoint Triplet*, *The Spin-One Carrier and the Trace Form* and *The Spectrum of a Biquaternion*. **The row of the elements is** where the same bracket is the commutator of the algebra and the spectrum is the pair of values of an element.

**The result in one line.** The adjoint action of an element of the triplet has the spectrum $\lambda,0,-\lambda$, and the only degeneracy is $\lambda=0$, the nilpotent cone.

**Boundaries.** The rank strata are *The Spin-One Carrier and the Rank Strata*; the spectrum of an element of the operator carrier is *The Spin-$\tfrac32$ Bispinors and the Spectral Strata*; the spectrum of an element of the whole operator space is *The Fierz–Kofink Identities and the Classification of Spinors*.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$; the generators of the triplet are $J_k$ and an element is $X=\sum x_kJ_k$; the module of the operators is $V=V_{3/2}$; the star is $\natural$; the trace form is $\langle S,T\rangle=\operatorname{tr}(S^{\natural}T)$; and $\operatorname{tr}$ and $\det$ are read from the spectrum.

## The Spectrum on the Triplet

**Definition.** For $X$ in the triplet the **adjoint action** on the triplet is $\operatorname{ad}_X(S)=[X,S]$, and the **spectrum of the carrier** is the spectrum of that operator on the three-dimensional space $V_1$.

**Proposition.** The characteristic polynomial of $\operatorname{ad}_X$ on the triplet is

$$
\chi_X(t)=t^3-c(X)\,t,
$$

where $c(X)$ is a fixed non-zero multiple of the invariant form of $X$; the spectrum is $\lambda,0,-\lambda$ with $\lambda^2=c(X)$, and the three values sum to zero.

*Proof.* The adjoint action of the triplet on itself is the bracket, which is antisymmetric for the invariant form; an antisymmetric operator in three dimensions has a kernel containing the element itself, and its remaining two eigenvalues are opposite because the trace vanishes. The product of the two non-zero roots is the constant term, which is the invariant form up to a fixed factor, computed once on a generator.

**Corollary.** Every element of the triplet has zero as an eigenvalue of its adjoint action, and the eigenvector is the element itself.

*Proof.* The bracket of an element with itself vanishes, so the element is in the kernel.

**The reading.** Three values summing to zero is the spectral form of the constraint that the triplet is three-dimensional and traceless. A generator has $c=-1$ in the normalisation of the previous article, so its spectrum is $i,0,-i$; a nilpotent element has $c=0$ and the spectrum collapses to zero three times.

## Three Values or One

**Theorem.** The triplet is the disjoint union of two spectral strata: the set where $c(X)\neq0$, on which the spectrum has three distinct values, and the set where $c(X)=0$, on which it has one value, zero, three times.

$$
V_1=\{c\neq0\}\ \sqcup\ \{c=0\},\qquad \operatorname{spec}=\begin{cases}\lambda,0,-\lambda,& c\neq0,\\ 0,0,0,& c=0.\end{cases}
$$

*Proof.* The two roots $\pm\lambda$ are distinct exactly when $\lambda\neq0$, which is $c\neq0$; at $c=0$ both vanish and the third value already vanishes.

**Corollary.** The stratum $\{c\neq0\}$ is open and dense in the triplet, and $\{c=0\}$ is a cone of dimension two.

*Proof.* A non-zero quadratic form does not vanish on an open dense set, and its zero locus in three dimensions is a cone of dimension two.

**The reading.** Only one coincidence can occur, and it is the coincidence of all three values. The absence of a middle case, two distinct values with one of them double, is a property of the antisymmetric action: the spectrum of an antisymmetric operator is closed under negation with equal multiplicities, so a repeated non-zero value would force its negative to occur as often, which the count of three forbids.

**Remark.** The copy can remove no coincidence of the carrier spectrum, because the parameter $c$ is invariant: a coincidence of the regular part does not occur at all, and the coincidence of the cone is carried by every element of the orbit and cannot be removed by the action. It can be removed by a perturbation of the element out of the cone, and this is the sense in which the degeneracy of the cone is stable along the orbit and unstable in the space.

## The Discriminant

**Definition.** The **discriminant** of the carrier spectrum is the discriminant of the cubic $t^3-c(X)t$.

**Proposition.** $\operatorname{disc}=4c(X)^3$, it is a function of the invariant form alone, and it is even in $X$: the discriminant of $-X$ equals the discriminant of $X$.

*Proof.* For a cubic $t^3+pt$ the discriminant is $-4p^3$, so with $p=-c$ it is $4c^3$. The invariant form is quadratic in the coefficients of $X$, so $c^3$ is homogeneous of degree six and unchanged under $X\mapsto-X$.

**Corollary.** The two strata are the vanishing and the non-vanishing of the discriminant, and the character of the spectrum does not distinguish $X$ from $-X$.

*Proof.* The discriminant vanishes exactly on the cone and is non-zero elsewhere; being even, it cannot separate an element from its opposite.

**The reading.** Evenness is the statement that the spectrum of $-X$ is the negative of the spectrum of $X$: the multiset $\lambda,0,-\lambda$ is invariant under the flip of the sign of $\lambda$. The discriminant sees the multiset and not the ordering, and this is why it is even.

## The Part Inside the Big Spectrum

**Proposition.** For a Cartan element of the triplet the spectrum of its adjoint action on the whole operator space is the nine integers from $-3$ to $3$, with multiplicities $1,2,3,4,3,2,1$, and the spectrum on the triplet is the part $1,0,-1$.

*Proof.* The operator space is the tensor square of the module with its dual, whose weights are the differences of the four weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$; the differences are the integers from $-3$ to $3$, with multiplicity four at zero and decreasing multiplicities at the ends. The triplet contributes the weights $1,0,-1$, the three values of its own string.

**Corollary.** The spectrum of the carrier is the innermost part of the spectrum of the space, and the outer values belong to the carriers of higher label.

*Proof.* The weights $\pm2$ occur in the carriers of label two and three, and $\pm3$ only in the carrier of label three; the values $0,\pm1$ are the ones the triplet can carry.

**The reading.** The carrier spectrum is a shadow of the big spectrum, and the shadow is the part nearest zero. The outer values need the larger carriers, which is the spectral form of the statement that the triplet is the smallest carrier.

## The Trace and the Constraint

**Proposition.** The trace of the adjoint action on the triplet vanishes for every element, and this vanishing is the constraint that the three values sum to zero.

*Proof.* The adjoint action is a commutator, so its trace vanishes identically; the sum of the eigenvalues of an operator is its trace.

**Corollary.** The spectrum of the carrier has one free parameter, the invariant $c$, and the constraint reduces the three values to one number.

*Proof.* Three values summing to zero and symmetric under the flip are $\lambda,0,-\lambda$, determined by $\lambda$ alone.

**The reading.** The constraint is not an extra condition on the element; it is a property of the action. Every adjoint action is traceless because it is a commutator, and on a three-dimensional space this leaves exactly the shape $\lambda,0,-\lambda$.

## Passage to the Group

**Proposition.** For the group element $\exp(X)$ the action on the triplet has eigenvalues $1,e^{\lambda},e^{-\lambda}$, and the trace of the group action is $1+2\cosh\lambda$.

*Proof.* The exponential of an operator has the exponentials of its eigenvalues as eigenvalues, and the eigenvalues of the adjoint action are $\lambda,0,-\lambda$, so the group action has $e^{\lambda},1,e^{-\lambda}$.

**Corollary.** On the cone the group action has all eigenvalues equal to one and is not the identity unless $X=0$; off the cone the eigenvalues are distinct.

*Proof.* At $\lambda=0$ the three eigenvalues are all one, and the group element is unipotent: it differs from the identity by the exponential of a non-zero nilpotent action.

**The reading.** The two strata have different group-theoretic meanings: the regular part of the triplet exponentiates to elements with three distinct eigenvalues, and the nilpotent cone exponentiates to unipotent elements. The spectral stratification of the algebra and the orbit stratification of the group agree under the exponential.

## Further Reading

- [The Spin-One Carrier: the Adjoint Triplet](the-spin-one-carrier-the-adjoint-triplet.html), for the brackets whose spectrum is computed here
- [The Spin-One Carrier and the Trace Form](the-spin-one-carrier-and-the-trace-form.html), for the invariant form that the parameter of the spectrum is
- [The Spin-One Carrier and the Rank Strata](the-spin-one-carrier-and-the-rank-strata.html), for the same two strata read through the rank
- [The Spectrum of a Biquaternion](the-spectrum-of-a-biquaternion.html), for the pair of values of an element and its coincidences
- [The Fierz–Kofink Identities and the Classification of Spinors](the-fierz-kofink-identities-and-the-classification-of-spinors-of-the-operators.html), for the five classes of the whole operator space
