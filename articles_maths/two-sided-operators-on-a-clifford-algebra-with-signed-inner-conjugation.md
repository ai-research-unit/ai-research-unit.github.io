# __Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation__

## Introduction

The family of two-sided operators of *Two-Sided Operators on a Clifford Algebra* is indexed by a pair: an automorphism $\theta$ of the Clifford algebra that acts on the left factor and an anti-automorphism $c$ that acts on the right one, the operator attached to $x$ being $\Phi^{\theta,c}_x(y)=\theta(x)\,y\,c(x)$. The present article singles out the member in which the right factor is the inverse and the left factor carries the grade involution,

$$
x\,y\,x^{-1}\ \longmapsto\ \alpha(x)\,y\,x^{-1},
$$

the **signed inner conjugation**. The name records the input that the inner conjugation cannot supply: the grade involution is the sign character of the algebra, equal to $-1$ on the odd part, and it is that minus which makes an odd element reproduce the reflection $\rho_u$ instead of its negative.

The reason a separate name and a separate article are needed is that the even part of the algebra and the odd part behave differently, and the difference is exactly the sign. On an even element the factors $\alpha(x)$ and $x$ coincide and the signed inner conjugation is the inner conjugation, an algebra automorphism; on an odd element the two differ by $-1$, so the signed inner conjugation is the inner conjugation composed with the sign, a map that is multiplicative only up to that sign, yet still bijective, still preserving the parity grading, and on the space of vectors the one that returns the reflection. The inner conjugation and the signed inner conjugation therefore agree on $\mathrm{Cl}^0$ and differ on $\mathrm{Cl}^1$, and only the signed one has the kernel and the action on $V$ on which the pin and spin groups are built.

The Clifford algebra, its parity grading and the three intrinsic involutions $\alpha$, $r$ and $x^{\natural}=\alpha(x^{r})$ are from *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*. The general two-sided family, its five members, its value at the unit, its parity and its composition law are *Two-Sided Operators on a Clifford Algebra*, and nothing of that general theory is re-derived here. The restriction to the quadratic space, the Clifford group $\Gamma(V,q)$ and the groups cut out of it by the Clifford norm are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the one-sided factors of the operator are *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*, and its role on a module is *Pin Representations and Clifford Modules with Signed Inner Conjugation*; and the reason the signed member is not a second independent structure, with the cancellation of two odd signs and the graded decomposition of the algebra, is *The Grading of the Clifford Algebra with Signed Inner Conjugation*. The base is a field $F$ of characteristic not $2$, with $q$ a non-degenerate quadratic form on the finite-dimensional space $V$ and $B$ its polar form.

## The Operator and the Parity Sign

**Definition.** Let $x\in\mathrm{Cl}(V,q)^{\times}$ be a unit. The **signed inner conjugation** by $x$ is the $F$-linear map

$$
\mathrm{Ad}^{\alpha}_x:\mathrm{Cl}(V,q)\longrightarrow\mathrm{Cl}(V,q),\qquad \mathrm{Ad}^{\alpha}_x(y)=\alpha(x)\,y\,x^{-1}.
$$

It is the two-sided operator of *Two-Sided Operators on a Clifford Algebra* attached to the pair $\theta=\alpha$, $c=(\ )^{-1}$, and it is defined on the unit group alone, because the right factor is the inverse.

**Proposition (the parity sign).** Let $x$ be homogeneous of degree $k$ and let $\varepsilon_x=(-1)^{k}$, so that $\alpha(x)=\varepsilon_x\,x$. Then

$$
\mathrm{Ad}^{\alpha}_x=\varepsilon_x\,\mathrm{Ad}_x,
$$

where $\mathrm{Ad}_x(y)=x\,y\,x^{-1}$ is the inner conjugation. In particular $\mathrm{Ad}^{\alpha}_x=\mathrm{Ad}_x$ when $x$ is even, and $\mathrm{Ad}^{\alpha}_x=-\mathrm{Ad}_x$ when $x$ is odd.

*Proof.* The grade involution multiplies the degree-$k$ part by $(-1)^k$, so $\alpha(x)=\varepsilon_x x$; substituting into the definition gives $\mathrm{Ad}^{\alpha}_x(y)=\varepsilon_x x\,y\,x^{-1}$, and $\varepsilon_x$ is central because it is a scalar.

**Proposition (value at the unit and parity).** For every unit $x$ one has $\mathrm{Ad}^{\alpha}_x(1)=\varepsilon_x$, that is $+1$ on the even part and $-1$ on the odd part, and $\mathrm{Ad}^{\alpha}_x$ preserves the parity grading, $\mathrm{Ad}^{\alpha}_x(\mathrm{Cl}^i)\subseteq\mathrm{Cl}^i$.

*Proof.* The value at the unit is $\alpha(x)x^{-1}=\varepsilon_x x\,x^{-1}=\varepsilon_x$. For the grading, each of the maps $\alpha$ and $\mathrm{Ad}_x$ preserves the degree modulo two, and a scalar multiple does not change that.

**Remark.** The value at the unit is the whole difference. On the even part of the algebra the inner conjugation and the signed inner conjugation are the same automorphism, which is why a rotation, carried by an even element, is described by either of them; on the odd part they differ by the sign $-1$, and it is the odd part that carries the reflections.

## The Automorphism and Its Sign

**Proposition (bijectivity and composition).** The map $\mathrm{Ad}^{\alpha}_x$ is an $F$-linear bijection of the algebra with inverse $\mathrm{Ad}^{\alpha}_{x^{-1}}$, and

$$
\mathrm{Ad}^{\alpha}_x\circ\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz},\qquad x,z\in\mathrm{Cl}(V,q)^{\times}.
$$

So $x\mapsto\mathrm{Ad}^{\alpha}_x$ is a homomorphism from the unit group to the group of $F$-linear bijections of $\mathrm{Cl}(V,q)$, with image isomorphic to $\mathrm{Cl}(V,q)^{\times}/F^{\times}$.

*Proof.* For the composition, $\mathrm{Ad}^{\alpha}_x\bigl(\mathrm{Ad}^{\alpha}_z(y)\bigr)=\alpha(x)\bigl(\alpha(z)\,y\,z^{-1}\bigr)x^{-1}=\alpha(xz)\,y\,(xz)^{-1}$. Taking $z=x^{-1}$ gives the inverse. The kernel is computed in the next section.

**Proposition (multiplicativity, with the sign).** Let $x$ be homogeneous of degree $k$ and $\varepsilon_x=(-1)^{k}$. Then for all $y,z$,

$$
\mathrm{Ad}^{\alpha}_x(yz)=\varepsilon_x\,\mathrm{Ad}^{\alpha}_x(y)\,\mathrm{Ad}^{\alpha}_x(z).
$$

In particular $\mathrm{Ad}^{\alpha}_x$ is an **algebra automorphism** when $x$ is even, and when $x$ is odd it is a bijection that is multiplicative only up to the global sign $-1$.

*Proof.* By the parity-sign proposition, $\mathrm{Ad}^{\alpha}_x=\varepsilon_x\mathrm{Ad}_x$, and $\mathrm{Ad}_x$ is conjugation by $x$, an algebra automorphism. Hence $\mathrm{Ad}^{\alpha}_x(yz)=\varepsilon_x\mathrm{Ad}_x(y)\mathrm{Ad}_x(z)$; substituting $\mathrm{Ad}_x=\varepsilon_x\mathrm{Ad}^{\alpha}_x$ in each factor and using $\varepsilon_x^{3}=\varepsilon_x$ gives the claim.

**Proposition (compatibility with the grade involution).** The signed inner conjugation commutes with the grade involution,

$$
\mathrm{Ad}^{\alpha}_x\circ\alpha=\alpha\circ\mathrm{Ad}^{\alpha}_x .
$$

*Proof.* Both sides are $\varepsilon_x\,\alpha\circ\mathrm{Ad}_x$: the grade involution commutes with conjugation by $x$, and it is a scalar on each homogeneous component, so it commutes with the scalar $\varepsilon_x$ as well.

**Remark.** The two propositions together say precisely what kind of object the signed inner conjugation is: an automorphism of the algebra on the even part, and a twisted automorphism on the odd part. It is not an inner automorphism in the ordinary sense when $x$ is odd, since $\mathrm{Ad}^{\alpha}_x=-\mathrm{Ad}_x$ and $-\mathrm{Ad}_x$ is not multiplicative; it is what the geometric layer needs, because the reflection formula carries the same minus.

## The Kernel and the Centre

The inner conjugation and the signed inner conjugation have different kernels, and that difference is the second place where the minus is load-bearing.

**Proposition.** The kernel of the inner conjugation on the unit group is the group of units of the centre,

$$
\ker\mathrm{Ad}=\{\,x\in\mathrm{Cl}(V,q)^{\times} : xy=yx\ \text{for all } y\,\}=Z\bigl(\mathrm{Cl}(V,q)\bigr)^{\times},
$$

which is $F^{\times}\cdot1$ when $\dim V$ is even and $F^{\times}\cdot1\cup F^{\times}\omega$ when $\dim V$ is odd, where $\omega$ is the volume element.

*Proof.* $\mathrm{Ad}_x=\mathrm{id}$ says $xy=yx$ for every $y$. The centre of a Clifford algebra of a non-degenerate form is $F$ in even dimension and $F\oplus F\omega$ with $\omega$ odd in odd dimension; a central element of odd dimension is a unit because $\omega^{2}=\pm1$, a nonzero scalar.

**Proposition.** The kernel of the signed inner conjugation on the unit group is the group of nonzero scalars,

$$
\ker\mathrm{Ad}^{\alpha}=F^{\times}\cdot1 ,
$$

in every dimension.

*Proof.* The equation $\mathrm{Ad}^{\alpha}_x=\mathrm{id}$ at $y=1$ reads $\alpha(x)=x$, so $x$ is even; on the even part $\mathrm{Ad}^{\alpha}_x=\mathrm{Ad}_x$, whose kernel is the even part of the centre, and the even part of the centre is $F\cdot1$ in both parities of the dimension.

**Corollary (the volume element).** Let $\dim V$ be odd and let $\omega$ be the volume element. Then $\omega$ is central, so $\mathrm{Ad}_{\omega}=\mathrm{id}$, while

$$
\mathrm{Ad}^{\alpha}_{\omega}=-\mathrm{id}.
$$

*Proof.* The volume element is odd and central in odd dimension, so $\mathrm{Ad}_\omega=\mathrm{id}$, and the parity-sign proposition gives $\mathrm{Ad}^{\alpha}_\omega=-\mathrm{Ad}_\omega$.

**Remark (why the exact sequences need the signed form).** The corollary is the sharp statement that the inner conjugation is the wrong operator for the pin group. The element $\omega$ of an odd-dimensional Clifford algebra is a unit of norm $N(\omega)=\omega\bar\omega=\pm1$, so it lies in $\mathrm{Pin}(V,q)$; under $\mathrm{Ad}$ it acts trivially on $V$ and belongs to the kernel of $\mathrm{Pin}\to O(V,q)$, so that kernel is strictly larger than $\{\pm1\}$ and the exact sequence fails. Under $\mathrm{Ad}^{\alpha}$ the same element acts as $-\mathrm{id}$, hence nontrivially, and the kernel is the scalars; intersected with the norm-one condition of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* it is $\{\pm1\}$, which is the double cover. The minus in the left factor is therefore not a convention: it is what makes the kernel of the action on the quadratic space the two elements that the covering group requires.

## The Action on the Quadratic Space

**Proposition.** Let $u\in V$ with $q(u)\neq0$ and let $\rho_u(v)=v-2B(v,u)q(u)^{-1}u$ be the reflection in $u^{\perp}$. Then

$$
\mathrm{Ad}^{\alpha}_u(v)=\rho_u(v),\qquad \mathrm{Ad}_u(v)=-\rho_u(v),\qquad v\in V .
$$

*Proof.* For a vector $u$ one has $\alpha(u)=-u$, so $\mathrm{Ad}^{\alpha}_u=-u\,v\,u^{-1}$ and $\mathrm{Ad}_u=u\,v\,u^{-1}$; from the fundamental relation, $uvu=2B(u,v)u-q(u)v$, hence $-uvu^{-1}=\rho_u(v)$ and the other equality is its negative.

**Proposition.** For $x\in\mathrm{Cl}(V,q)^{\times}$ the condition $\mathrm{Ad}^{\alpha}_x(V)\subseteq V$ holds exactly when $\mathrm{Ad}_x(V)\subseteq V$, and characterizes the Clifford group $\Gamma(V,q)$; on $\Gamma$ the map $\mathrm{Ad}^{\alpha}$ is a surjection onto $O(V,q)$ with kernel $F^{\times}$, and on an even element it is a rotation while on a vector it is a reflection.

*Proof.* The two conditions are equivalent because the two maps differ by the central scalar $\varepsilon_x$, which carries $V$ to itself. The rest is the theory of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, quoted here.

**Remark.** The equivalence of the two conditions shows that the Clifford group does not depend on which member is used to define it; what the member changes is the map, and hence which isometry is attached to which element. With $\mathrm{Ad}$ an odd element $u$ is sent to $-\rho_u$, that is to the reflection composed with $-\mathrm{id}$, and with the rotations of the even part this still fills out $O(V,q)$; with $\mathrm{Ad}^{\alpha}$ the same element is sent to the reflection itself. The two maps agree on the even part and differ by the sign on the odd part, and it is the signed map that matches the classical sandwich formula $v\mapsto-u\,v\,u^{-1}$.

## Worked Cases

### The Sign on the Odd Part

In $\mathrm{Cl}_{0,3}(\mathbb{R})$ with $e_j^{2}=-1$, let $x=e_1$. Then $x$ is odd, $\varepsilon_x=-1$, $x^{-1}=-e_1$ and $\alpha(x)=-e_1$, so $\mathrm{Ad}^{\alpha}_{e_1}=-\mathrm{Ad}_{e_1}$ and

| operator | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|
| $\mathrm{Ad}_{e_1}$ | $e_1$ | $-e_2$ | $-e_3$ |
| $\mathrm{Ad}^{\alpha}_{e_1}$ | $-e_1$ | $e_2$ | $e_3$ |

The second row is the reflection $\rho_{e_1}$ and the first its negative, and the values at the unit are $+1$ and $-1$ respectively.

### The Volume Element

In the same algebra the volume element $\omega=e_1e_2e_3$ is odd, central and satisfies $\omega^{2}=1$, so it is a unit and $\alpha(\omega)=-\omega$. Hence

$$
\mathrm{Ad}_{\omega}=\mathrm{id},\qquad \mathrm{Ad}^{\alpha}_{\omega}=-\mathrm{id},\qquad N(\omega)=\omega\bar\omega=\omega^{2}=1 .
$$

So $\omega\in\mathrm{Pin}(V,q)$, it is invisible to the inner conjugation, and the signed inner conjugation separates it from the identity. This is the worked form of the corollary above.

### An Even Element

The element $R=e_1e_2$ is even, so the two operators coincide. With $R^{-1}=-e_1e_2$,

$$
\mathrm{Ad}^{\alpha}_R(e_1)=-e_1,\qquad \mathrm{Ad}^{\alpha}_R(e_2)=-e_2,\qquad \mathrm{Ad}^{\alpha}_R(e_3)=e_3 ,
$$

which is the half-turn of the plane $\mathrm{span}(e_1,e_2)$: the rotation carried by the rotor, with no sign to correct.

### A Split Signature

In $\mathrm{Cl}_{1,1}(\mathbb{R})\cong M_2(\mathbb{R})$ with $e_1^{2}=1$ and $e_2^{2}=-1$, take $x=e_1+e_2$, an odd element with $x^{2}=0$. Then $x$ is not a unit and no member of the family is defined at $x$; the isotropic vector $e_1+e_2$ is exactly the element that the reflection formula cannot use, since $q(e_1+e_2)=0$. The example isolates the invertibility hypothesis, which is the only hypothesis that the two inverse members share.

## Summary

The **signed inner conjugation** is the two-sided operator $\mathrm{Ad}^{\alpha}_x(y)=\alpha(x)\,y\,x^{-1}$, the member of the family of *Two-Sided Operators on a Clifford Algebra* whose left factor carries the grade involution and whose right factor is the inverse. Its whole behaviour is governed by the parity sign: with $\varepsilon_x=(-1)^{k}$ on the degree-$k$ part,

$$
\mathrm{Ad}^{\alpha}_x=\varepsilon_x\,\mathrm{Ad}_x ,
$$

so it is the inner conjugation on the even part and minus the inner conjugation on the odd part. It is an $F$-linear bijection with $\mathrm{Ad}^{\alpha}_x\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz}$, it commutes with the grade involution, it preserves the parity grading, and it is an algebra automorphism for even $x$ and a map that is multiplicative only up to the global sign for odd $x$.

Its kernel is $F^{\times}\cdot1$ in every dimension, strictly smaller than the kernel $Z(\mathrm{Cl})^{\times}$ of the inner conjugation in odd dimension: the central volume element $\omega$ satisfies $\mathrm{Ad}_\omega=\mathrm{id}$ but $\mathrm{Ad}^{\alpha}_\omega=-\mathrm{id}$, and it is a unit of norm $1$. On the quadratic space the signed form is the one that returns the reflection, $\mathrm{Ad}^{\alpha}_u=\rho_u$ while $\mathrm{Ad}_u=-\rho_u$, so an odd element acts on $V$ by the reflection itself and not by its negative. The two members define the same Clifford group, since they differ by a central scalar, but only the signed one gives $\mathrm{Pin}(V,q)\to O(V,q)$ the kernel $\{\pm1\}$ on which the double cover rests.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | Grade involution, the sign character, $\alpha(x)=(-1)^kx$ on the degree-$k$ part |
| $\varepsilon_x=(-1)^{k}$ | Parity sign of a homogeneous element, $\alpha(x)=\varepsilon_xx$ |
| $\mathrm{Ad}_x(y)=x\,y\,x^{-1}$ | Inner conjugation, defined on the units |
| $\mathrm{Ad}^{\alpha}_x(y)=\alpha(x)\,y\,x^{-1}$ | Signed inner conjugation, the operator of this article |
| $\mathrm{Ad}^{\alpha}_x=\varepsilon_x\mathrm{Ad}_x$ | The parity sign, the spine of the article |
| $\mathrm{Ad}^{\alpha}_x(\mathrm{Cl}^i)\subseteq\mathrm{Cl}^i$ | Preservation of the parity grading |
| $\mathrm{Ad}^{\alpha}_x\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz}$ | Composition law; image $\cong\mathrm{Cl}^{\times}/F^{\times}$ |
| $\mathrm{Ad}^{\alpha}_x(yz)=\varepsilon_x\mathrm{Ad}^{\alpha}_x(y)\mathrm{Ad}^{\alpha}_x(z)$ | Multiplicativity with the sign |
| $\ker\mathrm{Ad}^{\alpha}=F^{\times}$, $\ker\mathrm{Ad}=Z(\mathrm{Cl})^{\times}$ | The two kernels |
| $\mathrm{Ad}^{\alpha}_\omega=-\mathrm{id}$, $\mathrm{Ad}_\omega=\mathrm{id}$ | The volume element, odd dimension |
| $\mathrm{Ad}^{\alpha}_u=\rho_u$, $\mathrm{Ad}_u=-\rho_u$ | The reflection and its negative on a vector $u$ |
| $\Gamma(V,q)$ | Clifford group, the units with $\mathrm{Ad}^{\alpha}_x(V)\subseteq V$ |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the two conjugation actions on vectors and the sign that distinguishes them.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the twisted conjugation $\alpha(x)vx^{-1}$, the Lipschitz group and the action of the pin and spin groups on the quadratic space.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grade involution, the centre of a Clifford algebra and the two kernels.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the original construction of the twisted action and the reflection formula.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the intrinsic involutions of a Clifford algebra and the role of the volume element.
