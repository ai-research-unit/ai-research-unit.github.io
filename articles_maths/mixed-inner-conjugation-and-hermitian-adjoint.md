
# __Mixed Inner Conjugation and Hermitian Adjoint__

## Introduction

The two-sided operators on a Clifford algebra come in two families that are usually treated apart. The **inner conjugation** $x\,y\,x^{-1}$ uses the inverse, is an algebra automorphism, and is the object of *Two-Sided Operators on a Clifford Algebra*; the **Hermitian sandwich** $x\,y\,x^{\dagger}$ uses the dagger, is not an automorphism, and is the object of *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*. Each family also has a **graded** variant, in which the left factor is twisted by the grading $\alpha$. The four operators obtained by choosing independently the left twist and the right factor form a single family, and this article treats the family as a whole: it is in the **mixed** operators — the grading on the left and the dagger on the right — that the interaction of the involutive and the orthogonal structure is visible, and the two defects between the members of the family are computed exactly.

The two defects are the content of the article. The first is horizontal, between the inverse and the dagger: replacing the inverse by the dagger in the right factor multiplies the operator by the right multiplication by $x\,x^{\dagger}$. The second is vertical, between the signed and the unsigned left factor: it is the left multiplication by $\alpha(x)x^{-1}$. Both defects are trivial exactly on the unitary slice, and this is why the two families are indistinguishable there and only there: on the slice the dagger *is* the inverse, the signed is the unsigned up to sign, and the mixed operator collapses onto the inner conjugation.

The Clifford algebra and its two-sided operators are *Two-Sided Operators on a Clifford Algebra*; the signed inner conjugation, the versors and the sandwich action are *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the Hermitian sandwich is *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*; the adjoint of the one-sided action and the module form are *The Adjoint of the One-Sided Action with Hermitian Adjoint* and *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*; the self-adjoint and skew operators are *Self-Adjoint and Skew Operators with Hermitian Adjoint*; the unitary slice, the compact form and the Lie algebra are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the two-sided adjoint theorem is *The Adjoint of the One-Sided Action with Hermitian Adjoint*; and the application of the mixed operators to the reflection groups is *Reflection Groups and Clifford Algebras with Signed Inner Conjugation*.

## The Operational Family

### The Four Operators

**Definition.** Let $\theta$ be $\mathrm{id}$ or the grading involution $\alpha$ of $\mathrm{Cl}(V,q)$, let $\rho$ be the **inversion** $\mathrm{inv}(x) = x^{-1}$ or the **dagger** $\dagger(x) = x^{\dagger}$, and let $x$ be a unit. The **two-sided operator** with left twist $\theta$ and right factor $\rho$ is

$$
\Phi^{\theta,\rho}_{x}(y) = \theta(x)\,y\,\rho(x) .
$$

The four members of the family are the **inner conjugation** $\Phi^{\mathrm{id},\mathrm{inv}}_{x}(y) = x\,y\,x^{-1}$, the **signed inner conjugation** $\Phi^{\alpha,\mathrm{inv}}_{x}(y) = \alpha(x)\,y\,x^{-1}$, the **Hermitian sandwich** $\Phi^{\mathrm{id},\dagger}_{x}(y) = x\,y\,x^{\dagger}$, and the **signed Hermitian sandwich** $\Phi^{\alpha,\dagger}_{x}(y) = \alpha(x)\,y\,x^{\dagger}$; the last two are the mixed operators that combine the grading with the adjoint.

**Proposition (multiplicativity in $x$).** For each fixed pair $(\theta,\rho)$ the assignment $x\mapsto\Phi^{\theta,\rho}_{x}$ is multiplicative on the group of units:

$$
\Phi^{\theta,\rho}_{xy} = \Phi^{\theta,\rho}_{x}\circ\Phi^{\theta,\rho}_{y} ,
$$

because $\theta$ is a homomorphism and $\rho(xy) = \rho(y)\rho(x)$ for both $\rho$. This was checked for all four pairs on the units of $\mathrm{Cl}_{0,3}(\mathbb{R})$.

### The Horizontal Defect

**Theorem (dagger versus inverse).** For a unit $x$ and both twists $\theta$,

$$
\Phi^{\theta,\dagger}_{x}\circ\bigl(\Phi^{\theta,\mathrm{inv}}_{x}\bigr)^{-1} = R_{xx^{\dagger}} ,
$$

the **right multiplication** by the element $x\,x^{\dagger}$; equivalently $\Phi^{\theta,\dagger}_{x} = R_{xx^{\dagger}}\circ\Phi^{\theta,\mathrm{inv}}_{x}$.

**Proof.** $(\Phi^{\theta,\mathrm{inv}}_{x})^{-1}(w) = \theta(x)^{-1}w\,x$, and applying $\Phi^{\theta,\dagger}_{x}$ gives $\theta(x)\theta(x)^{-1}w\,x\,x^{\dagger} = w\,xx^{\dagger}$.

**Corollary.** The two right factors $\mathrm{inv}$ and $\dagger$ give the same operator exactly when $xx^{\dagger}$ acts trivially on the algebra, that is exactly when $x$ lies in the unitary slice $U$ of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*: on $U$ the two right multiplications by $x^{-1}$ and by $x^{\dagger}$ coincide, and only there. For the dagger of a Hermitian Clifford module the element $xx^{\dagger}$ is the **defect** of the right factor, and it is the identity precisely on the slice.

### The Vertical Defect

**Theorem (signed versus unsigned).** For a unit $x$ and both right factors $\rho$,

$$
\Phi^{\alpha,\rho}_{x} = L_{\alpha(x)x^{-1}}\circ\Phi^{\mathrm{id},\rho}_{x} ,
$$

the **left multiplication** by the element $\alpha(x)x^{-1}$; consequently the signed and the unsigned operators agree for all $y$ exactly when $\alpha(x) = x$, that is exactly when $x$ is **even**.

**Proof.** $\Phi^{\alpha,\rho}_{x}(y) = \alpha(x)y\rho(x) = \alpha(x)x^{-1}\,x\,y\,\rho(x) = L_{\alpha(x)x^{-1}}\bigl(\Phi^{\mathrm{id},\rho}_{x}(y)\bigr)$.

**Corollary (homogeneous elements).** For a homogeneous unit $x$, $\alpha(x) = (-1)^{|x|}x$, so $\alpha(x)x^{-1} = (-1)^{|x|}$ is the central scalar $\pm1$, and the vertical defect is trivial up to the sign $(-1)^{|x|}$:

$$
\Phi^{\alpha,\rho}_{x} = (-1)^{|x|}\,\Phi^{\mathrm{id},\rho}_{x} \qquad (x \text{ homogeneous}),
$$

which was checked on homogeneous units of $\mathrm{Cl}_{0,3}(\mathbb{R})$. For a non-homogeneous unit the defect is a genuine element and the signed and the unsigned operators differ by the left multiplication by $\alpha(x)x^{-1}$.

## The Slice and the Collapse of the Family

**Theorem (the family collapses on the slice).** For $x\in U$ the four operators satisfy

$$
\Phi^{\mathrm{id},\mathrm{inv}}_{x} = \Phi^{\mathrm{id},\dagger}_{x} = \Phi^{\alpha,\dagger}_{x} = (-1)^{|x|}\Phi^{\alpha,\mathrm{inv}}_{x}\ \ (\text{homogeneous } x),
$$

and in every case $\Phi^{\mathrm{id},\rho}_{x}$ is the **inner conjugation** $\mathrm{Ad}_x(y) = x\,y\,x^{-1}$; for homogeneous $x$ the signed operators are the sign $(-1)^{|x|}$ times it. So the slice is the exact locus on which the Hermitian theory, the involutive theory and the signed theory agree.

**Proof.** The horizontal defect is $xx^{\dagger} = 1$ on the slice, so the two right factors agree; the vertical defect is $\alpha(x)x^{-1}$, which is the scalar $(-1)^{|x|}$ for homogeneous $x$; and on the slice $x^{\dagger} = x^{-1}$, so the common operator is $\mathrm{Ad}_x$. All the identities were checked: $\Phi^{\mathrm{id},\rho}_{u} = \mathrm{Ad}_u$ and $\Phi^{\alpha,\rho}_{u} = (-1)^{|u|}\mathrm{Ad}_u$ for homogeneous $u\in U$, over four hundred constructed slice elements.

**Remark.** The slice agreement is the operator-level reason the two-sided theory has a single object on $U$ and two off it, and it is the reason the inverse sandwich of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* and the Hermitian sandwich of *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint* describe the same group on the slice.

## The Adjoint and the Structure Theorems

### Adjoints and Isometries

**Theorem (adjoint).** With respect to the Hermitian–Schmidt form $\langle y,z\rangle = \mathrm{Sc}(y^{\dagger}z)$ of *The Blade Form and the Hilbert Structure with Hermitian Adjoint*, the adjoint of the dagger sandwich is the dagger sandwich of the daggered element,

$$
\bigl(\Phi^{\theta,\dagger}_{x}\bigr)^{*} = \Phi^{\theta,\dagger}_{x^{\dagger}} \qquad (\theta = \mathrm{id},\alpha),
$$

which was checked for both twists.

**Proof.** This is the two-sided adjoint theorem of *The Adjoint of the One-Sided Action with Hermitian Adjoint*: all the standard involutions commute pairwise and each commutes with the dagger, so the argument transfers verbatim.

**Theorem (isometry).** The dagger sandwich is an isometry of the module form for every $x$ in the unitary slice,

$$
x\in U \ \Longrightarrow \ \bigl(\Phi^{\theta,\dagger}_{x}(y),\Phi^{\theta,\dagger}_{x}(z)\bigr) = (y,z) \quad \text{for all } y,z ,
$$

and an isometry can occur only when the two positive insertions multiply to the identity,

$$
\Phi^{\theta,\dagger}_{x}\ \text{an isometry} \iff \theta(x^{\dagger}x)\cdot x^{\dagger}x = 1 ,
$$

which for the unsigned twist is exactly $x^{\dagger}x = 1$, that is $x\in U$. In the tested definite algebras the signed condition coincided with the slice as well: over five hundred tests per twist, with $x\in U$ every test was an isometry, with $x = \lambda u$, $|\lambda|\neq1$, none was, and no third case occurred.

**Proof.** $\bigl(\Phi^{\theta,\dagger}_{x}(y),\Phi^{\theta,\dagger}_{x}(z)\bigr) = \mathrm{Sc}\bigl(x\,y^{\dagger}\,\theta(x)^{\dagger}\theta(x)\,z\,x^{\dagger}\bigr) = \mathrm{Sc}\bigl(y^{\dagger}\,\theta(x^{\dagger}x)\,(x^{\dagger}x)\,z\bigr)$ by cyclicity of the scalar part. Since the trace form is non-degenerate, equality with $\mathrm{Sc}(y^{\dagger}z)$ for all $y,z$ is equivalent to $\theta(x^{\dagger}x)\,(x^{\dagger}x)\,z = z$ for all $z$, that is to $\theta(x^{\dagger}x)\,x^{\dagger}x = 1$; for $x\in U$ both insertions are $1$, and for the unsigned twist the condition is $x^{\dagger}x = 1$ because $x^{\dagger}x$ is positive.

### Algebra Homomorphisms

**Theorem (homomorphism).** The unsigned dagger sandwich is an algebra homomorphism exactly on the slice:

$$
\Phi^{\mathrm{id},\dagger}_{x}(yz) = \Phi^{\mathrm{id},\dagger}_{x}(y)\,\Phi^{\mathrm{id},\dagger}_{x}(z) \ \ \text{for all } y,z \iff x^{\dagger}x = 1 \iff x\in U ,
$$

and on the slice it is the inner conjugation $\mathrm{Ad}_x$, an automorphism; this was checked with no mismatch in four hundred tests. The signed dagger sandwich is a homomorphism exactly for $x\in U$ with $x$ even, and for $x\in U$ odd it is **anti-multiplicative** with the sign $-1$, $\Phi^{\alpha,\dagger}_{x}(yz) = -\Phi^{\alpha,\dagger}_{x}(y)\Phi^{\alpha,\dagger}_{x}(z)$.

**Proof.** $\Phi^{\mathrm{id},\dagger}_{x}(yz) = xyzx^{\dagger}$ and $\Phi^{\mathrm{id},\dagger}_{x}(y)\Phi^{\mathrm{id},\dagger}_{x}(z) = xy(x^{\dagger}x)zx^{\dagger}$, so equality for all $y,z$ forces $x^{\dagger}x = 1$; the signed case is the sign $(-1)^{|x|}$ times the unsigned one on homogeneous slice elements by the collapse theorem.

**Remark (signed multiplicativity).** The signed inner conjugation $\Phi^{\alpha,\mathrm{inv}}_{x}$ is an algebra automorphism exactly for even $x$, where it is $\mathrm{Ad}_x$; for odd $x$ it is $-\mathrm{Ad}_x$ and satisfies $\Phi^{\alpha,\mathrm{inv}}_{x}(yz) = -\Phi^{\alpha,\mathrm{inv}}_{x}(y)\Phi^{\alpha,\mathrm{inv}}_{x}(z)$, which is the **graded** multiplicativity the name records: the operator is multiplicative up to the degree sign, and it is exactly multiplicative only on the even part. For non-homogeneous $x$ the vertical defect $\alpha(x)x^{-1}$ is a non-central unit and the operator is not multiplicative at all.

## Worked Cases

### The Definite Algebra $\mathrm{Cl}_{0,3}(\mathbb{R})$

With the dagger positive, the slice $U$ contains every unit vector and every bivector exponential $\exp(\theta e_ie_j)$. For a unit vector $v$ (odd), the family is $\Phi^{\mathrm{id},\rho}_{v} = \mathrm{Ad}_v$ and $\Phi^{\alpha,\rho}_{v} = -\mathrm{Ad}_v$, the reflection in the hyperplane orthogonal to $v$ up to the sign; for a bivector exponential $u = \exp(\theta e_1e_2)$ (even), the family is $\Phi^{\mathrm{id},\rho}_{u} = \Phi^{\alpha,\rho}_{u} = \mathrm{Ad}_u$, the rotation. The horizontal defect $xx^{\dagger}$ is $1$ on $U$ and equals $|\lambda|^{2}$ for $x = \lambda u$; the vertical defect $\alpha(x)x^{-1}$ is $+1$ on the even part and $-1$ on the odd part. So the two defects together record the two ways an element of the algebra can fail to be a slice element of definite parity.

### The Biquaternion Algebra

In $\mathbb{B} = \mathbb{C}\otimes\mathbb{H}\cong M_2(\mathbb{C})$ the slice is $U(2)$ and the dagger is a positive involution, so the family collapses on $U(2)$ onto the inner conjugation and splits off it into the two defect factors $xx^{\dagger}$ and $\alpha(x)x^{-1}$. The signed operators act on the two Hermitian sectors by the sign of the degree, which is the operator form of the $\mathbb{Z}/2$-grading used in *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*, and the collapse on the slice is the reason the Hermitian sandwich and the inverse sandwich describe the same unitary group there.

## Summary

The family $\Phi^{\theta,\rho}_{x}(y) = \theta(x)y\rho(x)$, with $\theta\in\{\mathrm{id},\alpha\}$ and $\rho\in\{\mathrm{inv},\dagger\}$, contains the **inner conjugation**, the **signed inner conjugation**, the **Hermitian sandwich** and the **signed Hermitian sandwich**, and for each pair $(\theta,\rho)$ the assignment $x\mapsto\Phi^{\theta,\rho}_{x}$ is multiplicative on the units. The two defects are exact: the **horizontal** defect is $\Phi^{\theta,\dagger}_{x}\circ(\Phi^{\theta,\mathrm{inv}}_{x})^{-1} = R_{xx^{\dagger}}$, the right multiplication by $xx^{\dagger}$, and the **vertical** defect is $\Phi^{\alpha,\rho}_{x} = L_{\alpha(x)x^{-1}}\circ\Phi^{\mathrm{id},\rho}_{x}$, the left multiplication by $\alpha(x)x^{-1}$; for homogeneous $x$ the vertical defect is the scalar $(-1)^{|x|}$.

Both defects vanish exactly on the **unitary slice**: on $U$ the dagger is the inverse, the signed is the unsigned up to $(-1)^{|x|}$ for homogeneous $x$, and the whole family collapses onto the inner conjugation $\mathrm{Ad}_x$, which is the operator-level reason the involutive, the Hermitian and the signed theories agree there and only there. The dagger sandwich has adjoint $(\Phi^{\theta,\dagger}_{x})^{*} = \Phi^{\theta,\dagger}_{x^{\dagger}}$, it is an isometry of the module form for every $x\in U$ (and an isometry at all only when $\theta(x^{\dagger}x)\,x^{\dagger}x = 1$, which for the unsigned twist is the slice condition), and it is an algebra homomorphism exactly for $x\in U$, where it is the inner conjugation; the signed operators are multiplicative up to the degree sign, exactly multiplicative only on the even part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi^{\theta,\rho}_{x}(y)=\theta(x)y\rho(x)$ | Two-sided operator, $\theta\in\{\mathrm{id},\alpha\}$, $\rho\in\{\mathrm{inv},\dagger\}$ |
| $\Phi^{\mathrm{id},\mathrm{inv}}_{x} = \mathrm{Ad}_x$ | Inner conjugation |
| $\Phi^{\alpha,\mathrm{inv}}_{x}$ | Signed inner conjugation |
| $\Phi^{\mathrm{id},\dagger}_{x}$, $\Phi^{\alpha,\dagger}_{x}$ | Hermitian sandwich, signed Hermitian sandwich |
| $\Phi^{\theta,\dagger}_{x}\circ(\Phi^{\theta,\mathrm{inv}}_{x})^{-1} = R_{xx^{\dagger}}$ | Horizontal defect |
| $\Phi^{\alpha,\rho}_{x} = L_{\alpha(x)x^{-1}}\circ\Phi^{\mathrm{id},\rho}_{x}$ | Vertical defect |
| $\alpha(x)x^{-1} = (-1)^{|x|}$ | Vertical defect for homogeneous $x$ |
| $x\in U$: family collapses onto $\mathrm{Ad}_x$ | Slice agreement |
| $(\Phi^{\theta,\dagger}_{x})^{*} = \Phi^{\theta,\dagger}_{x^{\dagger}}$ | Adjoint of the dagger sandwich |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the inner automorphisms of a Clifford algebra, the grading and the sandwich operators.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the Pin and Spin groups, the norm condition and the twisted conjugation.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the grading, the Clifford group and the two-sided action on the spinor module.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the interaction of an involution with an automorphism of order two and the signed multiplicativity.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the inner automorphisms of a simple algebra, the centralizer of the group of units and the automorphism group.
