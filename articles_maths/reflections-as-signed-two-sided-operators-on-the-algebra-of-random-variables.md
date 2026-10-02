
# __Reflections as Signed Two-Sided Operators on the Algebra of Random Variables__

## Introduction

A reflection of the algebra of random variables is the inner conjugation by a unit with the grade involution inserted in the middle, $r_u(x)=u\,\alpha(x)\,u^{-1}$, the two-sided operator obtained by conjugating the grade involution by $u$. Over a noncommutative algebra the reflections form a group that carries the conjugacy of the units, and the correspondence between a unit and the reflection it defines is the interesting part of the theory. Over the algebra of random variables the product is commutative, so $u\,\alpha(x)\,u^{-1}=\alpha(x)$ for every unit, and the whole family collapses onto the single map $\alpha$; the correspondence between a unit and an involution becomes the constant map with the unit group as its domain, and its failure is total rather than partial. This article states the collapse, records the properties of the surviving operator $\alpha$ — it is the involutive, unitary, self-adjoint automorphism that defines the grading — and identifies the involutive signed two-sided operators that remain.

The operator conventions are those fixed in *The Signed Sandwich on the Algebra of Random Variables*, the preceding article: $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the conjugation $\sigma(x)=\bar x$, the state $\varphi(x)=\mathbb E[x]$, the form of the category $\langle x,y\rangle=\varphi(xy^*)$, the grade involution $\alpha$, and the twisted involution $\delta=\sigma\alpha$. The noncommutative theory of the reflections, where the correspondence is injective up to the central units, is *Reflections as Signed Two-Sided Operators on a Ring*, in Part I; the arithmetic counterpart, in which the convolution leaves the collapse as total as here, is *Reflections as Signed Two-Sided Operators on the Algebra of Arithmetic Functions*, written. The involution on the elements is *The Involution on the Algebra of Random Variables*, later in this category, and the signed left multiplication whose involutions are computed here is *The Signed Left Multiplication on the Algebra of Random Variables*, later in this category. No physics is invoked.

Throughout, $\mathcal{A}$ is the algebra of random variables as fixed in the preceding article, $\mathcal{A}^\times$ is its group of units, the units being the bounded random variables bounded away from zero, and $\alpha$ is the grade involution. The grading is $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$, the inner conjugation by $u$ is $\operatorname{conj}_u(x)=uxu^{-1}$, and the signed left multiplication is $S^\alpha_c=L_c\alpha$.

## The Reflection of a Unit

### Definition

**Definition.** For $u\in\mathcal{A}^\times$ the **reflection** is the signed two-sided operator
$$
r_u:\mathcal{A}\to\mathcal{A},\qquad r_u(x)=u\,\alpha(x)\,u^{-1},
$$
where $u^{-1}$ is the pointwise reciprocal of the unit.

### The collapse

**Theorem.** For every unit $u$,
$$
r_u=\alpha .
$$
Consequently the reflection is independent of the unit, the map $u\mapsto r_u$ is constant on $\mathcal{A}^\times$, and the inner conjugation
$$
\operatorname{conj}_u(x)=u\,x\,u^{-1}=x
$$
is the identity for every unit: the group of inner automorphisms of the graded algebra is trivial. The two operators commute, $\operatorname{conj}_u\circ\alpha=\alpha\circ\operatorname{conj}_u=\alpha$.

*Proof.* The product is commutative, so $u\,\alpha(x)\,u^{-1}=\alpha(x)\,u\,u^{-1}=\alpha(x)$; the inner conjugation collapses for the same reason, $uxu^{-1}=xuu^{-1}=x$. The commutation with $\alpha$ is immediate from $\operatorname{conj}_u=\mathrm{id}$.

### Properties of the reflection

**Theorem.** The operator $\alpha$ is an involutive, unitary, self-adjoint algebra automorphism of $\mathcal{A}$:
$$
\alpha^2=\mathrm{id},\qquad \alpha(xy)=\alpha(x)\alpha(y),\qquad \alpha(1)=1,\qquad \alpha^*=\alpha,\qquad \alpha^*\alpha=\alpha\alpha^*=\mathrm{id},
$$
it commutes with the conjugation, $\alpha\sigma=\sigma\alpha$, it reverses the grading, $\alpha(\mathcal{A}_{\bar i})=\mathcal{A}_{\bar{1-i}}$, and it is self-adjoint for the form of the category. Its fixed algebra is the even part, $\mathcal{A}^\alpha=\mathcal{A}_{\bar0}$, and its $(-1)$-eigenspace is the odd part, $\mathcal{A}_{\bar1}$.

*Proof.* The involution, the multiplicativity and the unitality are the definition of a grade involution; the unitarity is $\alpha^*\alpha=\alpha^2=\mathrm{id}$; the self-adjointness is the change of variables $\langle\alpha x,y\rangle=\mathbb E[(x\circ\varphi_0)\bar y]=\mathbb E[x(\bar y\circ\varphi_0)]=\langle x,\alpha y\rangle$ under the measure-preserving $\varphi_0$; the eigenspace description is the definition of the grading, and the fixed algebra is an algebra because an automorphism preserves the product.

## The Correspondence with the Involutions

### The involutive signed sandwiches

**Theorem.** Write $S^\alpha_c=L_c\alpha$, the signed left multiplication by $c$, so that $L_c\alpha=\alpha L_{\alpha(c)}$. Then $S^\alpha_c$ is an involution if and only if
$$
c\,\alpha(c)=1 ,
$$
and the involutive signed sandwiches are exactly the maps $S^\alpha_c$ with $c$ a unit of $\mathcal{A}$ satisfying this equation. Each such $S^\alpha_c$ is unitary exactly when also $|c|=1$.

*Proof.* $\bigl(S^\alpha_c\bigr)^2=L_c\alpha L_c\alpha=L_cL_{\alpha(c)}=L_{c\alpha(c)}$, which is the identity exactly when $c\alpha(c)=1$; the unitarity is the condition $|c|=1$ of the preceding article.

**Corollary (the correspondence).** The **reflection** $r_u$ corresponds to the unit $u$ through the composite of the inner conjugation and the grade involution, $\alpha\circ\operatorname{conj}_u$, but the correspondence is not injective: the fibre of the map $u\mapsto r_u$ is the whole unit group $\mathcal{A}^\times$ and its image is the single element $\alpha$. Equivalently the reflections are the operators $r_u=u\alpha(\cdot)u^{-1}$ with $u$ a unit, and all of them are $\alpha$.

*Proof.* The first statement is the definition of the reflection, $r_u=\alpha\operatorname{conj}_u$; the collapse makes the composite $\alpha$ for every $u$, giving the fibre and the image.

### The comparison with the noncommutative theory

**Remark.** In the noncommutative ring of *Reflections as Signed Two-Sided Operators on a Ring*, in Part I, the map $u\mapsto r_u$ has the whole unit group as its domain and its fibres are the cosets of the central units, the reflection group is a genuine quotient, and the correspondence with the involutions carries information. The commutativity of $\mathcal{A}$ destroys this information completely: the unit group is as large as possible, the inner automorphism group is trivial, and the image is a single point.

## The Degenerate Failure

**Theorem (failure in the commutative case).** Over the commutative algebra $\mathcal{A}$ the following hold. The signed inner automorphism group is trivial, since $\operatorname{conj}_u=\mathrm{id}$ for every unit. The reflection group is generated by $\alpha$ and is $\mathbb{Z}/2\mathbb{Z}$. The correspondence between the elements acting by an involution and the involutions is many-to-one without exception, and it carries the whole unit group to one map. No two-sided operator of the form $x\mapsto u\,\alpha(x)\,u^{-1}$ distinguishes the units. The involutive signed sandwiches, by contrast, are the $S^\alpha_c$ with $c\,\alpha(c)=1$, a family large enough to be parametrised by the $\alpha$-cocycles of $\mathcal{A}^\times$, and this family, not the reflections, is where the involutions of the signed theory live.

*Proof.* Every assertion about the reflections is the computation $u\alpha(x)u^{-1}=\alpha(x)$; the inner automorphism group is trivial because $uxu^{-1}=x$. The description of the involutions is the theorem above: $(S^\alpha_c)^2=L_{c\alpha(c)}$, and the equation $c\alpha(c)=1$ defines the $\alpha$-cocycles, the units $c$ whose $\alpha$-norm is the identity. The contrast is the reason the two notions, reflection and involutive signed two-sided operator, must be kept apart in the commutative case.

## Worked Examples

**Example (the swap on two atoms).** Let $\Omega=\{\omega_-,\omega_+\}$ with $\mathbb P(\omega_\pm)=\frac12$ and let $\varphi_0$ interchange the points, so that $\alpha(x_-,x_+)=(x_+,x_-)$ and the unit group is $\{(u_-,u_+):u_\pm\ne0\}$. The reflection of the unit $u$ is $(x_-,x_+)\mapsto(u_+x_+u_+^{-1},u_-x_-u_-^{-1})=(x_+,x_-)=\alpha(x)$, for every unit. The involutive signed sandwiches are the $S^\alpha_c$ with $c_+c_-=1$, that is $c=(c_-,1/c_-)$, a two-parameter family of order-two maps.

**Example (the reflection of the circle).** Let $\Omega=\mathbb R/\mathbb Z$ with the Lebesgue measure and $\varphi_0(\theta)=-\theta$; the group of units contains every nonvanishing continuous function, and each one defines the same reflection $\alpha$. The operator $\alpha$ fixes the cosines and negates the sines, and its fixed algebra is the algebra of the even functions.

**Example (the trivial grading).** For $\alpha=\mathrm{id}$ the reflection is the identity, the unit group acts trivially and the signed theory reduces to the theory of the invertible elements; this is the boundary of the family at which every reflection is the identity.

## Failure of the Degenerate Cases

The reflection degenerates in four configurations. First, the reflection is independent of the unit, so the notion of a reflection carries no information about the element that defines it; the striking contrast is with the noncommutative case, where the reflection group is the quotient of the unit group by the central units. Second, the fixed algebra of the reflection is the even part of the grading and can be as large as the whole algebra when $\alpha=\mathrm{id}$, in which case the reflection is the identity and the grading is trivial. Third, the involutive signed sandwiches need not be reflections: the equation $c\alpha(c)=1$ has the large solution set of the $\alpha$-cocycles, and the only one of these that is a reflection is $c=1$ giving $\alpha$ itself; the two notions separate. Fourth, when the algebra is reduced to a single point, $\mathcal{A}=\mathbb{C}$, the grade involution is the identity, the unit group is $\mathbb{C}^\times$, and every construction collapses to the scalars; the degenerate case is total and is the reason the noncommutative theory is the informative one.

## Summary

The reflection of a unit $u$ of the algebra of random variables is the signed two-sided operator $r_u(x)=u\,\alpha(x)\,u^{-1}$, and over the commutative algebra it collapses to the grade involution, $r_u=\alpha$ for every unit; the inner conjugation is the identity and the group of inner automorphisms is trivial. The surviving operator $\alpha$ is the involutive, unitary, self-adjoint automorphism that defines the grading, with fixed algebra the even part and $(-1)$-eigenspace the odd part, and it commutes with the conjugation. The correspondence between a unit and the reflection it defines is the constant map on the unit group, its failure total; the involutions of the signed theory are not the reflections but the signed left multiplications $S^\alpha_c$ with $c\,\alpha(c)=1$, the $\alpha$-cocycles, among which the reflections supply only $\alpha$. The conventions are those of *The Signed Sandwich on the Algebra of Random Variables*, the preceding article; the noncommutative theory is *Reflections as Signed Two-Sided Operators on a Ring*, in Part I; and the signed left multiplication is the next article of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A}^\times$ | the units, the bounded random variables bounded away from zero |
| $r_u(x)=u\,\alpha(x)\,u^{-1}$ | the reflection of the unit $u$ |
| $r_u=\alpha$ | the collapse in the commutative algebra |
| $\operatorname{conj}_u=\mathrm{id}$ | the triviality of the inner automorphisms |
| $\alpha^2=\mathrm{id}$, $\alpha^*=\alpha$ | the properties of the grade involution |
| $\mathcal{A}^\alpha=\mathcal{A}_{\bar0}$ | fixed algebra of the reflection, the even part |
| $S^\alpha_c=L_c\alpha$ | the signed left multiplication |
| $c\,\alpha(c)=1$ | the involutive signed sandwiches, the $\alpha$-cocycles |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the automorphism groups of a commutative involutive algebra.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the inner automorphisms, the conjugacy and the modular automorphism group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the involutions of an algebra with involution and their conjugacy classes.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the conjugation by units, the central units and the reflection groups.
