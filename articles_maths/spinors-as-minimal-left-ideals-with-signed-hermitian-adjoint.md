# __Spinors as Minimal Left Ideals with Signed Hermitian Adjoint__

## Introduction

A spinor can be taken to be an element of a minimal left ideal $I=\mathrm{Cl}(V,q)\pi$ of the Clifford algebra, the algebra acting on it by left multiplication; this is *Spinors as Minimal Left Ideals with Inner Conjugation*, and it is the description that makes the whole pin group, and not only its even part, act on spinors. The present article reads the same ideal with the signed Hermitian sandwich as the operator, and the Hermitian form as the structure on the ideal.

The ideal is a left ideal, so left multiplication by **every** element of the algebra carries it into itself, and the pin action on it is defined for all of $\mathrm{Pin}(V,q)$. The ideal is not homogeneous, $I=I^0\oplus I^1$ with $I^i=\mathrm{Cl}^i\pi$, and an odd element interchanges the two summands while an even element preserves them, so a spinor of the ideal has a parity decomposition and the odd part of the group swaps the components.

The signed Hermitian sandwich is realised on the ideal by a conjugation of the Clifford multiplication with **two left multiplications**,

$$
\Theta^{\alpha}_x(v)\,\psi=\alpha(x)\,v\,x^{\dagger}\,\psi
=\rho(\alpha(x))\,\rho(v)\,\rho(x^{\dagger})\,\psi
=\rho(\alpha(x))\,\rho(v)\,\rho(x)^{*}\,\psi,
\qquad v\in V,\ \psi\in I,
$$

where the last equality is the adjoint identity $\rho(x)^{*}=\rho(x^{\dagger})$ of *Pin Representations and Hermitian Modules with Signed Hermitian Adjoint*, valid for the Hermitian form of the ideal. So the left factor of the two-sided operator appears as the signed left multiplication $\Lambda^{\alpha}_x$, and the right factor appears as the **adjoint** of the left multiplication by $x$, not as its inverse. This is the Hermitian specificity of the ideal picture: on the slice the adjoint is the inverse and the two factors are $\rho(\alpha(x))$ and $\rho(x)^{-1}$, which is exactly the inverse formulation; off the slice the second factor is the adjoint, and the defect $\rho(x)\rho(x)^{*}=\rho(xx^{\dagger})$ measures the failure of the ideal to be a unitary module under the action of $x$.

The Clifford algebra, its parity grading and the intrinsic involutions are *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*; the idempotents, the minimal left ideals, the bridge to the Chevalley module, the even-multivector picture and the two actions on the ideal are *Spinors as Minimal Left Ideals with Inner Conjugation*, and nothing of that theory is re-derived; the Hermitian form on the ideal and the adjoint of the left action are *The Adjoint of the One-Sided Action with Hermitian Adjoint* and *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*; the Clifford modules and the pin representation are *Pin Representations and Hermitian Modules with Signed Hermitian Adjoint*; the groups are *The Pin and Spin Groups with Signed Hermitian Adjoint*; and the two-sided operator with its one-sided factors is *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint* and *One-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*. The base is a commutative ring $A$ with involution $\sigma$, $F$ the field of scalars of characteristic not two, $q$ non-degenerate on $V$, $B$ its polar form.

## The Ideal as a Pin Module

**Proposition (the left action).** Let $I=\mathrm{Cl}(V,q)\pi$ be a left ideal. For every $a\in\mathrm{Cl}(V,q)$ the left multiplication $L_a$ carries $I$ into itself, $L_a(I)\subseteq I$, and $I$ is a Clifford module. Consequently the assignment

$$
\rho(x)\psi=x\,\psi,\qquad x\in\mathrm{Pin}(V,q),\ \psi\in I,
$$

is the restriction of the algebra action to the group, that is, the pin representation on the Hermitian module $I$.

*Proof.* If $y=b\pi$ then $ay=(ab)\pi\in I$; the action is associative and restricts to the units. The Hermitian form on $I$ is the restriction of the module form, and the self-adjointness axiom holds because it holds on the whole algebra.

**Proposition (faithfulness on the ideal).** If $\mathrm{Cl}(V,q)$ is simple and $I\neq0$ the action on $I$ has trivial kernel, and if $\mathrm{Cl}(V,q)\cong A'\times A'$ with $I$ the minimal ideal of the first factor, the kernel is $\mathrm{Pin}(V,q)\cap(\{1\}\times A')$.

*Proof.* The annihilator of the ideal is a proper two-sided ideal; it vanishes over a simple algebra and over a product the ideal of one factor is annihilated by the other. This is the kernel computation of the pin-representation article read on the ideal.

**Remark.** The left action is why the ideal description is available for the whole pin group; the right action does not preserve a minimal left ideal, and the dual representation is realised on a minimal right ideal instead. The Hermitian form does not change this: it is a form on the ideal as a left module, and the adjoint of a left multiplication is again a left multiplication, by the dagger of the element.

## The Parity of the Ideal

**Proposition (the splitting).** The ideal splits according to the grading,

$$
I=I^0\oplus I^1,\qquad I^i=\mathrm{Cl}^i(V,q)\,\pi,
$$

and left multiplication by an even element preserves the two summands while left multiplication by an odd element interchanges them.

*Proof.* An element of the algebra is the sum of its even and its odd part, giving the splitting; and $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$ gives $L_a(I^j)\subseteq I^{i+j}$ for $a\in\mathrm{Cl}^i$, the exponent read modulo two.

**Corollary (pinors and the halves).** An odd element of $\mathrm{Pin}(V,q)$ maps $I^0$ onto $I^1$ and $I^1$ onto $I^0$; an even element, in particular every element of $\mathrm{Spin}(V,q)$, preserves each summand. On a minimal left ideal the two summands play the role of the two half-spin spaces of the module theory, and the odd part of the group exchanges them.

*Proof.* Immediate from the splitting and the parity of the left multiplication.

**Remark (the Hermitian pairing of the halves).** The Hermitian form of the ideal pairs only elements of the same parity, so $I^0$ and $I^1$ are orthogonal for it; the two summands are orthogonal chiral halves, and the Hermitian form restricts to each of them. This is the ideal-theoretic form of the orthogonality of the chiral summands of a Hermitian Clifford module, recorded in *The Blade Form and the Hermitian Structure with Hermitian Adjoint*.

## The Signed Hermitian Sandwich on the Ideal

**Proposition (the operator realised by left multiplications).** For $x\in\mathrm{Cl}(V,q)$, $v\in V$ and $\psi\in I$,

$$
\Theta^{\alpha}_x(v)\,\psi=\alpha(x)\,v\,x^{\dagger}\,\psi
=\rho(\alpha(x))\,\rho(v)\,\rho(x)^{*}\,\psi .
$$

So the signed Hermitian sandwich is realised on the ideal as the conjugation of the Clifford multiplication by the left multiplication of $\alpha(x)$ and the **adjoint** of the left multiplication of $x$: the left factor is the signed left multiplication $\Lambda^{\alpha}_x$ and the right factor is the dagger right multiplication, read on the ideal as the adjoint operator $\rho(x)^{*}=\rho(x^{\dagger})$. On the unitary slice the adjoint is the inverse and the formula is that of the inverse formulation.

*Proof.* Both sides are the same product of three factors in the algebra, applied to $\psi$; the first factor is $\rho(\alpha(x))=\Lambda^{\alpha}_x$ and the third is $\rho(x^{\dagger})=\rho(x)^{*}$ by the adjoint proposition of the pin-representation article, since the ideal is a Hermitian Clifford module. On the slice $x^{\dagger}=x^{-1}$ and $\rho(x)^{*}=\rho(x)^{-1}$.

**Corollary (the reflection, on and off the slice).** Let $u\in V$ with $q(u)\neq0$ and let $\rho_u$ be the reflection in $u^{\perp}$. Then for all $v\in V$ and $\psi\in I$,

$$
\Theta^{\alpha}_u(v)\,\psi=-q(u)\,\rho_u(v)\,\psi,\qquad
\rho(u)\,\rho(v)\,\rho(u)^{*}\,\psi=-q(u)\,\rho_u(v)\,\psi ,
$$

and on the unitary slice, $q(u)=-1$, both reduce to $\rho_u(v)\psi$; the unsigned sandwich is the negative of this on the slice. So on the ideal the sandwich with a slice-normalised vector is the reflection, and the sign that the two-sided operator removes is $-q(u)$, which is $+1$ exactly on the slice.

*Proof.* The first identity is the previous proposition with $x=u$ and the vector formula $\Theta^{\alpha}_u=-q(u)\rho_u$; the second is the corollary of the pin-representation article.

**Remark (the defect off the slice).** Off the slice the third factor of the operator is the adjoint, and the two-sided operator is not the conjugation by a unit: the element $x$ satisfies $\rho(x)\rho(x)^{*}=\rho(xx^{\dagger})$, which is the identity only when $xx^{\dagger}=1$, that is on the slice. So the ideal conjugation by a general element realises the Hermitian sandwich but not by a unitary operator, and that is the precise sense in which the Hermitian formulation needs the slice to produce unitarily the geometric operators.

## Worked Cases

### The Ideal of the Three-Dimensional Definite Algebra

In $\mathrm{Cl}_{0,3}(\mathbb{R})$ with $e_j^{2}=-1$ and $\sigma=\mathrm{id}$, let $\pi=\tfrac12(1+e_3)$. Then $\pi^{2}=\pi$, $\pi$ is primitive, $e_3\pi=\pi$, and

$$
I=\mathrm{Cl}_{0,3}\,\pi=\mathrm{span}_{\mathbb{R}}\{\pi,\ e_1\pi,\ e_2\pi,\ e_1e_2\pi\},
$$

of real dimension four, with the volume element $\omega=e_1e_2e_3$ acting by $\omega\pi=e_1e_2\pi$ and the splitting $I^0=\mathrm{span}\{\pi,e_1e_2\pi\}$, $I^1=\mathrm{span}\{e_1\pi,e_2\pi\}$. The dagger is $\sigma=\mathrm{id}$ and $\alpha$ on the generators, so $e_1^{\dagger}=-e_1$, $e_2^{\dagger}=-e_2$; the element $e_1$ is on the slice and

$$
\Theta^{\alpha}_{e_1}(v)\psi=e_1\,v\,e_1\psi=\rho_{e_1}(v)\psi
$$

for $v\in V$, the reflection, while $\rho(e_1)\rho(v)\rho(e_1)^{-1}\psi=-e_1ve_1\psi=-\rho_{e_1}(v)\psi$. The odd idempotent-supported element $e_1$ acts on the ideal by interchanging $I^0$ and $I^1$, as in the inverse formulation.

### The Reflection Read on the Ideal

Take $u=e_1$, $v=e_2$, $\psi=\pi$. Then $\rho_{e_1}$ fixes $e_2$, since $B(e_1,e_2)=0$, and

$$
\Theta^{\alpha}_{e_1}(e_2)\pi=e_1e_2e_1\pi,\qquad
\rho(e_1)\rho(e_2)\rho(e_1)^{*}\pi=e_1e_2e_1\pi,
$$

the same three factors: on the slice the adjoint is the inverse and the signed operator is the conjugation. The unsigned sandwich is the negative of this, $-e_1e_2e_1\pi$, and the parity sign is the only difference between the two computations, exactly as in the inverse formulation; the Hermitian reading adds that the third factor is $\rho(e_1)^{*}$ and that this is $\rho(e_1)^{-1}$ on the slice.

### The Volume Element

The volume element $\omega=e_1e_2e_3$ of the odd-dimensional algebra is odd, central and satisfies $\omega^{2}=-1$, so it is on the slice, and its Hermitian sandwich is the signed inner conjugation: $\Theta^{\alpha}_\omega=\mathrm{Ad}^{\alpha}_\omega=-\mathrm{id}$ while $\Theta_\omega=\mathrm{id}$. On the ideal, left multiplication by $\omega$ sends $I^0$ to $I^1$ and $I^1$ to $I^0$, and the signed Hermitian sandwich by $\omega$ acts as $-\mathrm{id}$ on the ideal, separating a spinor from its negative; the unsigned one is invisible. The adjoint of $\rho(\omega)$ is $\rho(\omega)^{*}=\rho(\bar{\omega})=\rho(\omega)$; on an odd number of skew-adjoint generators the two reversals cancel, so $\rho(\omega)$ is self-adjoint, and it is not the inverse, since $\bar{\omega}=\omega$ while $\omega^{-1}=-\omega$: the volume element is **not** on the slice, $\bar{\omega}\omega=\omega^{2}=-1$. The self-adjointness is nevertheless consistent with the sandwich acting as $-\mathrm{id}$, because the sandwich is the two-sided operator and not the one-sided factor.

### The Biquaternion Ideal

For $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ the same construction gives an ideal whose elements are the biquaternion spinors, with the two summands playing the role of the two chiralities and the odd elements of the pin group exchanging them. In the physics corpus the sandwich is written $\tilde Q\,x\,\tilde{Q}^{*}$, which is the Hermitian sandwich of this article read in the biquaternion algebra, and it is an isometry on the slice, the Lorentz group there; the compatibility of the ideal with the Lorentz action is the subject of the applications layer and nothing of it is used here.

## Summary

A **minimal left ideal** $I=\mathrm{Cl}(V,q)\pi$ is a left ideal and hence a Clifford module on which left multiplication by every element of the algebra is defined; the whole **pin group** acts on it by left multiplication, spinors are the elements of $I$, and on a simple algebra the action is faithful, with kernel $\mathrm{Pin}\cap(\{1\}\times A')$ over a product. The ideal is not homogeneous: it splits as $I=I^0\oplus I^1$ with $I^i=\mathrm{Cl}^i\pi$, the even elements preserve the two summands and the odd elements interchange them, and the Hermitian form of the ideal pairs only equal parities, so the two chiral halves are Hermitian-orthogonal. The signed Hermitian sandwich is realised on the ideal by conjugating the Clifford multiplication with two left multiplications,

$$
\Theta^{\alpha}_x(v)\psi=\rho(\alpha(x))\,\rho(v)\,\rho(x)^{*}\psi
=\rho(\alpha(x))\,\rho(v)\,\rho(x^{\dagger})\psi ,
$$

the left factor being the **signed left multiplication** $\Lambda^{\alpha}_x$ and the right factor being the **adjoint** of the left multiplication of $x$, the Hermitian specificity of the picture; on the unitary slice the adjoint is the inverse and the formula coincides with the inverse formulation, off the slice the defect $\rho(xx^{\dagger})$ measures the failure of the conjugation to be by a unitary. For a slice-normalised vector $u$ the sandwich on the ideal is the reflection, $\Theta^{\alpha}_u(v)\psi=\rho_u(v)\psi$, while the unsigned sandwich is its negative; the central volume element of an odd-dimensional algebra acts on the ideal by exchanging the two chiral summands, and the signed Hermitian sandwich by it acts as $-\mathrm{id}$ where the unsigned one is invisible.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $I=\mathrm{Cl}(V,q)\pi$ | Minimal left ideal, the spinor module |
| $\mathrm{Pin}$ acts by $\rho(x)\psi=x\psi$ | Pin action, one-sided, defined for all of $\mathrm{Pin}$ |
| $I=I^0\oplus I^1$, $I^i=\mathrm{Cl}^i\pi$ | Parity splitting; odd elements exchange the summands |
| $\langle I^0,I^1\rangle=0$ | Hermitian orthogonality of the chiral halves |
| $\Theta^{\alpha}_x(v)\psi=\rho(\alpha(x))\rho(v)\rho(x)^{*}\psi$ | Signed Hermitian sandwich on the ideal |
| $\rho(x)^{*}=\rho(x^{\dagger})=\rho(x)^{-1}$ on $U$ | Adjoint is the inverse on the slice |
| $\rho(xx^{\dagger})$, the defect | Failure of the conjugation to be unitary off the slice |
| $\Theta^{\alpha}_u(v)\psi=\rho_u(v)\psi$, $q(u)=-1$ | Reflection on the ideal, on the slice |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for minimal left ideals, idempotents and the spinor spaces.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Hermitian structure of the spinor module and the adjoint of the Clifford action.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the ideal picture and the pin group.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for minimal left ideals, the density theorem and the kernel of the action.
