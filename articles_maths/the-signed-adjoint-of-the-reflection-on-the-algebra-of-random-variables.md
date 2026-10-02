
# __The Signed Adjoint of the Reflection on the Algebra of Random Variables__

## Introduction

A reflection of the algebra of random variables is the signed two-sided operator
$$
r_u(x)=u\,\alpha(x)\,u^{-1},
$$
the inner conjugation by a unit with the grade involution in the middle, and on the commutative algebra it collapses to the grade involution, $r_u=\alpha$ for every unit $u$. This article computes its **adjoint**. With respect to the form of the category, $\langle x,y\rangle=\varphi(xy^*)$, the grade involution is self-adjoint, $\alpha^*=\alpha$, so the reflection is self-adjoint,
$$
r_u^*=r_u=\alpha ,
$$
and it is its own adjoint for every unit. The adjoint operation therefore carries **no information** about the reflection over the commutative algebra: it fixes the single operator $\alpha$ and cannot distinguish the units. The article derives this, computes the adjoint with respect to the **signed pairing** $\{x,y\}=\langle x,\alpha y\rangle$, where the reflection is again an isometry with itself as adjoint, identifies the involutive signed sandwiches among which the reflections form a single point, and states the failure of the correspondence, as against the noncommutative ring where the adjoint of the reflection is $r_{\delta(u)^{-1}}$ and depends on the unit.

The conventions are those of *The Signed Sandwich on the Algebra of Random Variables* and *Reflections as Signed Two-Sided Operators on the Algebra of Random Variables*, earlier in this category: $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the conjugation $\sigma(a)=\bar a$, the state $\varphi(a)=\mathbb E[a]$, the form $\langle x,y\rangle=\varphi(xy^*)$, the grade involution $\alpha$ (an involutive, unitary, self-adjoint automorphism), the grading and the twisted involution $\delta=\sigma\alpha$. The signed sandwiches and their adjoints are *The Signed Adjoint Sandwich on the Algebra of Random Variables*, the preceding article of this category; the signed left multiplication and its adjoint are *The Signed Left Multiplication on the Algebra of Random Variables*, earlier in this category, and *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the later article of this category; the adjoint of the unsigned left multiplication is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, earlier in this category. The noncommutative theory of the reflections and their adjoints is *The Signed Adjoint of the Reflection on a Ring*, in Part I, and the arithmetic counterpart, in which the collapse is as total as here, is *The Signed Adjoint of the Reflection on the Algebra of Arithmetic Functions*, written. No physics is invoked.

Throughout, $\mathcal{A}$ is the algebra of random variables, $\mathcal{H}=L^2(\Omega,\mathbb P)$ with the form $\langle x,y\rangle=\varphi(xy^*)$ is the Hilbert space of the category, $r_u(x)=u\alpha(x)u^{-1}$ is the reflection of the unit $u$, and the signed pairing is $\{x,y\}=\langle x,\alpha y\rangle$. The grade involution satisfies $\alpha^2=\mathrm{id}$, $\alpha^*=\alpha$, $\alpha\sigma=\sigma\alpha$ and $\alpha(\mathcal{A}_{\bar i})=\mathcal{A}_{\bar{1-i}}$.

## The Adjoint of the Reflection

### The form of the category

**Theorem (the reflection and its adjoint).** For every unit $u$ of $\mathcal{A}$,
$$
r_u=\alpha,\qquad r_u^*=r_u=\alpha,\qquad \alpha^*=\alpha,\qquad \alpha^2=\mathrm{id},\qquad \|\alpha x\|=\|x\| ,
$$
so the reflection is an involutive unitary operator and is its own adjoint.

*Proof.* The collapse $r_u=\alpha$ is the commutativity of the product: $u\alpha(x)u^{-1}=\alpha(x)uu^{-1}=\alpha(x)$. In the standard model the grade involution is the composition with a measure-preserving involution $\varphi_0$, $\alpha(x)=x\circ\varphi_0$, and the change of variables under $\varphi_0$ gives the self-adjointness,
$$
\langle\alpha x,y\rangle=\mathbb E[(x\circ\varphi_0)\bar y]=\mathbb E[x\,(\bar y\circ\varphi_0)]=\langle x,\alpha y\rangle ,
$$
and the isometry $\|\alpha x\|^2=\mathbb E[|x\circ\varphi_0|^2]=\mathbb E[|x|^2]$; the involution is $\alpha^2=\mathrm{id}$.

**Theorem (the adjoint of the reflection is the reflection).** The adjoint operation maps the class of the reflections to itself and fixes every element,
$$
r_u^*=r_u\qquad\text{for every unit }u ,
$$
so the class of the reflections, which is the single operator $\alpha$, is pointwise fixed by the adjoint.

*Proof.* The adjoint of $r_u=\alpha$ is $\alpha^*=\alpha=r_u$; the class is the single operator, so the map is the identity on it.

### The signed form

**Definition.** The **signed pairing** of two elements is
$$
\{x,y\}=\langle x,\alpha y\rangle=\varphi\bigl(x\,\alpha(y)^*\bigr),
$$
a Hermitian form equivalent to the form of the category through the grade involution.

**Theorem (the signed adjoint of the reflection).** With respect to the signed pairing the adjoint of the reflection is again the reflection, and the reflection is an isometry:
$$
\{r_ux,y\}=\{x,r_uy\},\qquad \{r_ux,r_uy\}=\{x,y\} .
$$

*Proof.* With $r_u=\alpha$ one has $\{r_ux,y\}=\langle\alpha x,\alpha y\rangle=\langle x,y\rangle$ by the unitarity of $\alpha$, and $\{x,r_uy\}=\langle x,\alpha\alpha y\rangle=\langle x,y\rangle$; the two are equal, and the isometry is the same computation applied twice. The signed pairing is equivalent to the form because $\alpha$ is invertible.

## The Correspondence

### The involutive signed sandwiches

**Theorem (the involutions).** The signed sandwiches that are involutions are the operators $S^\alpha_c=L_c\alpha$ with
$$
c\,\alpha(c)=1 ,
$$
the $\alpha$-cocycles, and they form a group under multiplication; the reflection $\alpha=S^\alpha_1$ is the one with $c=1$, and $-\alpha=S^\alpha_{-1}$ is the companion. Every involution is self-adjoint for the form of the category exactly when it is also $\alpha$-Hermitian, $\alpha(c)=c^*$, which fails for the general cocycle.

*Proof.* The square is $(S^\alpha_c)^2=S^\alpha_{c\alpha(c)}$ by *The Signed Adjoint Sandwich on the Algebra of Random Variables*, the preceding article, so the involution is $c\alpha(c)=1$; the cocycles are closed under multiplication because $\alpha$ is an involution, and the inverse of a cocycle is a cocycle; the self-adjointness is $c=\delta(c)$, that is $\alpha(c)=c^*$, again from the preceding article.

### The failure of the correspondence

**Theorem (the failure).** Over the algebra of random variables the correspondence between a unit and the reflection it defines is the constant map on the unit group: $r_u=\alpha$ for every $u$, its adjoint is $\alpha$, and the group of the reflections is the trivial group generated by $\alpha$. The adjoint operation carries no information about the correspondence.

*Proof.* The collapse is the commutativity; the adjoint is the theorem above; the class of the reflections is a single element, so its group is trivial.

**Corollary (the noncommutative contrast).** In the noncommutative ring of *The Signed Adjoint of the Reflection on a Ring*, in Part I, the adjoint of the reflection $r_u$ is the reflection $r_{\delta(u)^{-1}}$ with $\delta=\sigma\alpha$, which depends on the unit, and the adjoint operation is a nontrivial anti-automorphism of the group of the reflections.

*Proof.* The noncommutative computation reverses the two-sided product with the involution inserted, and the composite $\delta=\sigma\alpha$ produces the inverse of the twisted unit; the commutativity here is exactly what removes the dependence.

## Worked Examples

**Example (the trivial unit).** For $u=1$ the reflection is $r_1=\alpha$, and $r_1^*=\alpha$; the operator is self-adjoint and unitary, with fixed algebra the even part $\mathcal{A}_{\bar0}$ and $(-1)$-eigenspace the odd part $\mathcal{A}_{\bar1}$.

**Example (the two-atom swap).** For $\Omega=\{\omega_-,\omega_+\}$ with the uniform probability and $\alpha(x_-,x_+)=(x_+,x_-)$, the reflection is the swap for every unit: with $u=(u_-,u_+)$, $u^{-1}=(u_-^{-1},u_+^{-1})$, and $u\alpha(x)u^{-1}=(u_-x_+u_-^{-1},u_+x_-u_+^{-1})=(x_+,x_-)=\alpha(x)$. The adjoint is the swap again, and the reflection is a self-adjoint unitary involution, the parity operator of the two atoms.

**Example (the circle reflection).** On $\Omega=\mathbb R/\mathbb Z$ with the Lebesgue measure and $\alpha(x)(\theta)=x(-\theta)$, the reflection is the operator $\alpha$, self-adjoint and unitary, with the even and the odd functions as its eigenalgebras; the signed pairing $\{x,y\}=\int x(\theta)y(-\theta)\,d\theta$ is symmetric, and $\alpha$ is an isometry for it.

**Example (the cocycle companion).** The operator $S^\alpha_{-1}=-\alpha$ is an involution, $(-\alpha)^2=\mathrm{id}$, and it is not the reflection of any unit; it is self-adjoint and unitary, and it is the degenerate companion of the reflection. The example shows that the involutions of the signed theory are the cocycles $c\alpha(c)=1$, of which the reflections supply only the two with constant parameters.

## Failure of the Degenerate Cases

The signed adjoint of the reflection degenerates in four configurations. First, the adjoint of the reflection is the reflection itself, so the adjoint operation is the identity on the class of the reflections and there is no correspondence to compute; the adjoint is trivial precisely because the reflection is a unitary involution. Second, the signed pairing is equivalent to the form of the category through the grade involution, so the signed adjoint and the ordinary adjoint coincide; on the commutative algebra the signed structure adds nothing to the adjoint of the reflection. Third, the class of the reflections is a single operator, so the adjoint operation cannot distinguish the units; the group of the reflections is the trivial group, and the comparison with the ring isolates the commutativity as the cause. Fourth, the involutions $S^\alpha_c$ with nonconstant cocycles are not reflections and are in general not self-adjoint, so the class of the self-adjoint involutions is strictly smaller than the class of the involutions; confusing the two is the standard error of the commutative case.

## Summary

The reflection $r_u(x)=u\alpha(x)u^{-1}$ of the algebra of random variables collapses to the grade involution, $r_u=\alpha$ for every unit $u$, and its adjoint with respect to the form $\langle x,y\rangle=\varphi(xy^*)$ is again $\alpha$, so the reflection is a self-adjoint unitary involution and the adjoint operation fixes the class of the reflections pointwise. With respect to the signed pairing $\{x,y\}=\langle x,\alpha y\rangle$ the reflection is an isometry and its signed adjoint is itself; the signed pairing is equivalent to the form through $\alpha$, so the signed structure adds nothing beyond the identification of the two forms. The involutive signed sandwiches are the $\alpha$-cocycles $c\alpha(c)=1$, among which the reflections form the single point $c=1$ (with the companion $c=-1$), and the self-adjoint involutions are the smaller family of the $\alpha$-Hermitian cocycles. The correspondence between a unit and the reflection fails totally over the commutative algebra, and the noncommutative contrast with the adjoint $r_{\delta(u)^{-1}}$ is *The Signed Adjoint of the Reflection on a Ring*, in Part I. The signed sandwich adjoint is *The Signed Adjoint Sandwich on the Algebra of Random Variables*, the preceding article of this category, and the signed left multiplication adjoint is *The Signed Adjoint of the Left Multiplication on the Algebra of Random Variables*, the later article of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $r_u(x)=u\alpha(x)u^{-1}$ | the reflection of the unit $u$ |
| $r_u=\alpha$ | the collapse on the commutative algebra |
| $r_u^*=r_u=\alpha$ | the adjoint of the reflection |
| $\alpha^*=\alpha$, $\alpha^2=\mathrm{id}$ | the grade involution |
| $\{x,y\}=\langle x,\alpha y\rangle$ | the signed pairing |
| $\{r_ux,y\}=\{x,r_uy\}$ | the signed adjoint of the reflection |
| $S^\alpha_c$, $c\alpha(c)=1$ | the involutive signed sandwiches |
| $-\alpha=S^\alpha_{-1}$ | the companion involution |

## Further Reading

- Jacques Dixmier, *C*-Algebras* (North-Holland, 1977), for the involutions, the automorphisms and the representations.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the adjoints, the unitaries and the involutions.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions, the twisted involutions and the cocycles.
- Sterling K. Berberian, *Baer *-Rings* (Springer, 1972), for the involutions and the isometries of the forms.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd edition, 1982), for the involutions, the reflections and the forms.
