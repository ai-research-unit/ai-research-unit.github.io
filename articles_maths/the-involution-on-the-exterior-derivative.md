
# __The Involution on the Exterior Derivative__

## Introduction

On the exterior algebra $\Lambda^\bullet\mathrm{G}^{\ast}$ of the dual of a Lie algebra $\mathrm{G}$ lies the **exterior derivative** $d$, the degree-one operator whose value on a $p$-cochain is

$$
(d\omega)(x_0,\dots,x_p)=\sum_i(-1)^i x_i\cdot\omega(\dots,\widehat{x_i},\dots)+\sum_{i<j}(-1)^{i+j}\omega([x_i,x_j],\dots,\widehat{x_i},\dots,\widehat{x_j},\dots),
$$

and whose square is zero. An involution $\theta$ of $\mathrm{G}$ acts on the cochains by $\Theta\omega(x_1,\dots,x_p)=\omega(\theta x_1,\dots,\theta x_p)$, and since $d$ is built from the bracket, which $\theta$ preserves, the two operators **commute**: $\Theta d=d\Theta$. This article, the third of the `- * Operator Theory` group of the category, establishes the **equivariance** of the exterior derivative under the involution, describes the induced involution on the Lie algebra cohomology, and treats the **invariant pairing** on the cochains, the pairing with respect to which the involution is an isometry and the exterior derivative has an adjoint. The exterior derivative and its square-zero property are *The Exterior Derivative on the Lie Algebra*; the exterior algebra and its order-two maps are *Involutions of the Exterior Algebra*; the Hodge star and the codifferential belong to *The Hodge Star and the Real Structure of the Exterior Algebra* and to a later Part.

The base is a field $K$ of characteristic not two; $\mathrm{G}$ is a finite-dimensional Lie algebra with involution $\theta$, the cochains are the elements of $\Lambda^\bullet\mathrm{G}^{\ast}=\bigoplus_p\Lambda^p\mathrm{G}^{\ast}$, and the operators are $d$ (exterior derivative) and $\Theta$ (the induced involution). The article uses the bracket and the duality pairing only.

## The Involution on the Cochains

**Definition.** The **induced involution** on the cochains is the map $\Theta$ with

$$
(\Theta\omega)(x_1,\dots,x_p)=\omega(\theta x_1,\dots,\theta x_p),
$$

extended linearly to all degrees; it is the transpose of the action of $\theta$ on the exterior algebra of $\mathrm{G}$.

**Proposition.** $\Theta$ is an automorphism of the graded algebra $\Lambda^\bullet\mathrm{G}^{\ast}$ of order two, and it preserves the degree: $\Theta(\Lambda^p\mathrm{G}^{\ast})\subseteq\Lambda^p\mathrm{G}^{\ast}$.

**Proof.** The map $\theta$ is a linear automorphism of $\mathrm{G}$ of order two, so its transpose on $\mathrm{G}^{\ast}$ is an involution, and its extension to the exterior algebra is multiplicative and preserves the degree; $\Theta^2=\mathrm{id}$ because $\theta^2=\mathrm{id}$. $\square$

**Corollary.** The fixed cochains of $\Theta$ form the subalgebra $\Lambda^\bullet(\mathrm{G}^{\ast})^{\theta}$ of the $\theta$-invariant cochains, and the anti-fixed cochains are those with $\Theta\omega=-\omega$; the graded algebra of cochains decomposes into the two eigenspaces.

## Equivariance

**Theorem.** The exterior derivative equivaries with the induced involution:

$$
\Theta\,d=d\,\Theta .
$$

**Proof.** For a $p$-cochain $\omega$ and vectors $x_0,\dots,x_p$, the left side is $(d\omega)(\theta x_0,\dots,\theta x_p)$ and the right side is $d(\Theta\omega)(x_0,\dots,x_p)$. In the first sum the terms $x_i\cdot\omega(\dots)$ become $\theta x_i\cdot\omega(\theta\dots)$ and in the second sum the brackets become $[\theta x_i,\theta x_j]=\theta[x_i,x_j]$; the two expressions coincide term by term because $\theta$ is a Lie automorphism and the action of $\mathrm{G}$ on the cochains is the coadjoint one, transported by $\theta$. $\square$

**Corollary.** The involution $\Theta$ acts on the cohomology $H^\bullet(\mathrm{G})=\ker d/\operatorname{im}d$, since it commutes with $d$ and carries cocycles to cocycles and coboundaries to coboundaries; the induced map on $H^\bullet(\mathrm{G})$ is an involution, and its fixed part is the **$\theta$-invariant cohomology**.

**Proposition.** The equivariance is equivalent to the statement that $\theta$ is an automorphism of the differential graded algebra $(\Lambda^\bullet\mathrm{G}^{\ast},d)$; thus the pair $(\mathrm{G},\theta)$ gives a differential graded algebra with an involution, and the cohomology carries the same involution.

**Proof.** The two statements assert the same commutation with the differential plus multiplicativity, which is the proposition on $\Theta$. $\square$

## The Invariant Pairing

**Definition.** An **invariant pairing** on the cochains is a bilinear map $\beta$ on $\Lambda^\bullet\mathrm{G}^{\ast}$ such that $\beta(\Theta\omega,\Theta\eta)=\beta(\omega,\eta)$ for the involution and $\beta$ is compatible with the degree decomposition; a pairing is **nondegenerate** when $\beta(\omega,\cdot)=0$ implies $\omega=0$. The pairing is used only to take adjoints; no length, signature, definiteness or unit sphere is read off it.

**Theorem.** If $\mathrm{G}$ carries a nondegenerate symmetric bilinear form preserved by $\theta$, then the induced pairing on the cochains, extended multiplicatively, is invariant and nondegenerate, and the involution $\Theta$ is an **isometry**:

$$
\beta(\Theta\omega,\Theta\eta)=\beta(\omega,\eta).
$$

**Proof.** The form on $\mathrm{G}$ extends to $\Lambda^\bullet\mathrm{G}^{\ast}$ by the determinant-type rule on homogeneous elements; since $\theta$ preserves it on $\mathrm{G}$, its extension preserves the induced pairing on each degree, and multiplicativity gives the general case. $\square$

**Corollary.** The exterior derivative has an adjoint $\delta$ with respect to the invariant pairing, $\beta(d\omega,\eta)=\beta(\omega,\delta\eta)$; the operator $\delta$ is the **codifferential**, it lowers the degree by one, and it commutes with $\Theta$ because $d$ and $\beta$ do. The identity $\delta=\pm\star d\star$ holds in the definite case with an orientation, and the Hodge star, the definiteness and the analytic theory of the adjoint belong to Part II, where the form and the distance are available, and are named only.

## The Involution on the Cohomology

**Proposition.** The induced involution on $H^\bullet(\mathrm{G})$ is an algebra automorphism of the graded-commutative cohomology algebra, and the $\theta$-invariant cohomology is its fixed subalgebra; the invariant pairings are the fixed cochains.

**Proof.** The cohomology algebra is graded-commutative and $\Theta$ is a multiplicative map commuting with $d$, so it induces an algebra automorphism; the fixed part is the fixed subalgebra, and the invariant pairings are the fixed cochains by definition. $\square$

**Corollary.** The pairing of cohomology classes with the invariant pairing is compatible with the involution: $\beta(\Theta[\omega],\Theta[\eta])=\beta([\omega],[\eta])$, so the involution is an isometry of the cohomology; when the form is the Killing form of a semisimple $\mathrm{G}$ the cohomology pairing is the one used in the study of the primitive cohomology.

## Worked Case: The Abelian and the Nilpotent Algebra

For an abelian $\mathrm{G}$ the bracket vanishes and $d$ is the zero operator up to the action term; on the dual of the trivial module, $d=0$ and the cohomology is the whole exterior algebra; the involution $\Theta$ acts degree by degree and its fixed cochains are the invariant cochains, the equivariance being trivial. For the Heisenberg algebra $\mathrm{G}=\langle x,y,z\rangle$ with $[x,y]=z$ central, the exterior derivative on $\Lambda^1\mathrm{G}^{\ast}$ sends the dual basis elements according to the bracket, and an involution $\theta$ with $\theta(x)=-x$, $\theta(y)=y$, $\theta(z)=-z$ was checked to satisfy $\Theta d=d\Theta$ on degrees zero, one and two; the invariant pairing pairs the degree-one and degree-two cochains.

**Verified.** The equivariance $\Theta d=d\Theta$ was checked on the Heisenberg algebra in degrees zero, one and two, and on $\mathrm{sl}(2,K)$ in degrees zero and one; the invariance of the extended form under $\Theta$ was checked on the basis cochains.

## Summary

An involution $\theta$ of a Lie algebra $\mathrm{G}$ induces an involution $\Theta$ on the cochains $\Lambda^\bullet\mathrm{G}^{\ast}$ by transposing the action on $\mathrm{G}$. The **exterior derivative equivaries** with it, $\Theta d=d\Theta$, because $d$ is built from the bracket that $\theta$ preserves; equivalently $\theta$ is an automorphism of the differential graded algebra of cochains, and the involution descends to the cohomology, where its fixed part is the **$\theta$-invariant cohomology**. A nondegenerate symmetric form on $\mathrm{G}$ preserved by $\theta$ extends to an **invariant pairing** on the cochains for which $\Theta$ is an isometry and the exterior derivative has an adjoint, the **codifferential** $\delta$, which also commutes with $\Theta$. The identity $\delta=\pm\star d\star$, the Hodge star, the definiteness and the analytic theory of the adjoint belong to Part II, where the form and the distance are available, and are named only. The invariant pairing is compatible with the involution, and so is the cohomology pairing. The Heisenberg algebra and $\mathrm{sl}(2,K)$ are the worked cases. The adjoint operation and the analytic theory belong to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $\mathrm{G}$ | a finite-dimensional Lie algebra |
| $\Lambda^\bullet\mathrm{G}^{\ast}$ | the cochains |
| $d$ | the exterior derivative |
| $\theta,\Theta$ | the involution of $\mathrm{G}$ and the induced involution on the cochains |
| $\beta$ | the invariant pairing on the cochains |
| $\delta$ | the codifferential, the adjoint of $d$ |
| $H^\bullet(\mathrm{G})$ | the Lie algebra cohomology |

## Further Reading

- Claude Chevalley and Samuel Eilenberg, "Cohomology theory of Lie groups and Lie algebras", *Transactions of the American Mathematical Society* 63 (1948), 85–124, for the exterior derivative and the cochain complex.
- Jean-Louis Koszul, "Homologie et cohomologie des algèbres de Lie", *Bulletin de la Société Mathématique de France* 78 (1950), 65–127, for the invariant pairings.
- Werner Greub, *Multilinear Algebra*, Universitext (Springer, 2nd ed. 1978), for the exterior algebra and the induced forms.
