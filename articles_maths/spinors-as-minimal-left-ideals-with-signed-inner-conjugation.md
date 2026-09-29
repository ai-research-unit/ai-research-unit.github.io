# __Spinors as Minimal Left Ideals with Signed Inner Conjugation__

## Introduction

The spinor module of *Spin Representations and Clifford Modules with Inner Conjugation* is a Clifford module, and by *Spinors as Minimal Left Ideals with Inner Conjugation* it can be taken to be a minimal left ideal $I=\mathrm{Cl}(V,q)\pi$ of the algebra itself: the elements of $I$ are the spinors, and the Clifford algebra acts on them by left multiplication. That description was used there for the even part of the group, because the spin group lies in $\mathrm{Cl}^0$ and its action on a spinor is left multiplication by a rotor. The present article reads the same ideal with the whole Pin group acting on it.

Two things change, and neither requires a new construction. The first is that a minimal left ideal is a left ideal, so left multiplication by **every** element of the algebra carries it into itself; the action of the unit group on $I$ is therefore defined for all of $\mathrm{Pin}(V,q)$ and not only for its even part. The second is that the ideal is not homogeneous: it splits as $I=I^0\oplus I^1$ with $I^{i}=\mathrm{Cl}^{i}\pi$, and an odd element of the algebra interchanges the two summands while an even element preserves them. A spinor of the ideal therefore has a well-defined parity decomposition, and the odd part of Pin acts on it by swapping the two components.

The sign of the two-sided operator is visible here in a form that the algebra-level article does not show. On the ideal, left multiplication by $x$ realises the one-sided action, and the signed inner conjugation is realised by conjugating the Clifford multiplication by the two one-sided actions of $x$ and $\alpha(x)$:

$$
\mathrm{Ad}^{\alpha}_x(v)\,\psi=\alpha(x)\,v\,x^{-1}\psi=\rho(\alpha(x))\,\rho(v)\,\rho(x)^{-1}\psi .
$$

The two factors of the two-sided operator are thus the left multiplication by $\alpha(x)$ and the inverse left multiplication by $x$, and on the ideal their conjugation is exactly the module statement that the odd part returns the negative of the reflection.

The Clifford algebra, the parity grading and the intrinsic involutions are from *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*; the idempotents, the minimal left ideals, the bridge to the Chevalley module, the even-multivector picture and the two actions on the ideal are *Spinors as Minimal Left Ideals with Inner Conjugation*, and nothing of that theory is re-derived; the Clifford modules and the pin representation are *Pin Representations and Clifford Modules with Signed Inner Conjugation*; the groups are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; and the two-sided operator and its one-sided factors are *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* and *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*. The base is a field $F$ of characteristic not $2$, with $q$ non-degenerate on the finite-dimensional space $V$ and $B$ its polar form.

## The Ideal as a Pin Module

**Proposition (the left action).** Let $I=\mathrm{Cl}(V,q)\pi$ be a left ideal. For every $a\in\mathrm{Cl}(V,q)$ the left multiplication $L_a$ carries $I$ into itself, $L_a(I)\subseteq I$, and $I$ is a Clifford module. Consequently the assignment

$$
\rho(x)\psi=x\,\psi,\qquad x\in\mathrm{Pin}(V,q),\ \psi\in I,
$$

is the restriction of the algebra action to the group, that is, the pin representation of *Pin Representations and Clifford Modules with Signed Inner Conjugation*.

*Proof.* If $y=b\pi$ then $ay=(ab)\pi\in I$, since $ab$ is an element of the algebra; the action is associative and restricts to the units. 

**Remark.** The left action is the reason the ideal description is available for the whole Pin group. The right action does not share this property: right multiplication by a rotor does not preserve a minimal left ideal in general, and the dual representation is realised on a minimal right ideal instead; both statements are from *Spinors as Minimal Left Ideals with Inner Conjugation*. So the ideal is the natural home of the *pinor* rather than of a pair of spinors, and no pairing of one-sided operators is needed to define the group action on it.

**Proposition (faithfulness on the ideal).** If $\mathrm{Cl}(V,q)$ is simple and $I\neq0$, the action on $I$ has trivial kernel, and if $\mathrm{Cl}(V,q)\cong A\times A$ with $I$ the minimal ideal of the first factor, the kernel is $\mathrm{Pin}(V,q)\cap(\{1\}\times A)$.

*Proof.* The annihilator of the ideal is a two-sided ideal, proper because $\pi\in I$ and $\pi^{2}=\pi\neq0$, so it vanishes over a simple algebra; over a product, the ideal of one factor is annihilated by the other. This is the kernel computation of *Pin Representations and Clifford Modules with Signed Inner Conjugation*, read on the ideal.

## The Parity of the Ideal

**Proposition (the splitting).** The ideal splits according to the grading,

$$
I=I^0\oplus I^1,\qquad I^{i}=\mathrm{Cl}^{i}(V,q)\,\pi=\{\,a\pi : a\in\mathrm{Cl}^{i}(V,q)\,\},
$$

and left multiplication by an even element preserves the two summands while left multiplication by an odd element interchanges them.

*Proof.* An element of the algebra is the sum of its even and its odd part, giving the splitting; and $\mathrm{Cl}^{i}\mathrm{Cl}^{j}\subseteq\mathrm{Cl}^{i+j}$ gives $L_a(I^{j})\subseteq I^{i+j}$ for $a\in\mathrm{Cl}^{i}$, the exponent read modulo two. 

**Corollary (pinors and the halves).** An odd element of $\mathrm{Pin}(V,q)$ maps $I^0$ onto $I^1$ and $I^1$ onto $I^0$; an even element, in particular every element of $\mathrm{Spin}(V,q)$, preserves each of the two summands. On a minimal left ideal the two summands play the role that the two half-spin spaces $\Delta_\pm$ play on the module of *Spin Representations and Clifford Modules with Inner Conjugation*, and the odd part of the group exchanges them.

**Remark.** The exchange is the ideal-theoretic form of the chirality statement of the pin representation: a spinor of the ideal has two components, the even part $I^0$ and the odd part $I^1$ of the ideal, the spin group acts on each of them separately, and the remaining odd elements of Pin swap them. In an odd-dimensional algebra the two summands have the same dimension, since multiplication by a fixed odd element is a bijection of $I$ carrying one onto the other; in the low-dimensional cases for which the ideal is identified with the even subalgebra, the representative of a spinor is an even multivector and the odd elements move it out of that representative.

## The Signed Conjugation on the Ideal

**Proposition (the operator realised by left multiplications).** For $x\in\mathrm{Cl}(V,q)^{\times}$, $v\in V$ and $\psi\in I$,

$$
\mathrm{Ad}^{\alpha}_x(v)\,\psi=\alpha(x)\,v\,x^{-1}\,\psi=\rho(\alpha(x))\,\rho(v)\,\rho(x)^{-1}\,\psi .
$$

So the signed inner conjugation is realised on the ideal as the conjugation of the Clifford multiplication by the left multiplications of $\alpha(x)$ and $x$: the left factor is the signed left multiplication $\Lambda^{\alpha}_x$ and the right factor is the inverse left multiplication, the two ingredients of *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*.

*Proof.* Both sides are the same product of three factors in the algebra, applied to $\psi$; the first and the third factor are $\rho(\alpha(x))=\Lambda^{\alpha}_x$ and $\rho(x)^{-1}=\rho(x^{-1})$, since $\rho$ is a representation of the group of units. The module is one-sided, so both factors of the two-sided operator act on $\psi$ as left multiplications by elements of the algebra; the inverse right multiplication $R_{x^{-1}}$ of *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* is the right factor on the algebra, and on the ideal its work is done by the left multiplication by $x^{-1}$.

**Corollary (the reflection, with and without the sign).** Let $u\in V$ with $q(u)\neq0$ and let $\rho_u$ be the reflection in $u^{\perp}$. Then for all $v\in V$ and $\psi\in I$,

$$
\rho(\mathrm{Ad}^{\alpha}_u(v))\,\psi=\rho_u(v)\,\psi,\qquad \rho(u)\,\rho(v)\,\rho(u)^{-1}\,\psi=-\rho_u(v)\,\psi .
$$

So on the ideal the sandwich with a vector returns the negative of the reflection, and the signed inner conjugation is what removes the sign; the parity sign $\varepsilon_x=(-1)^{k}$ of *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* is the only difference between the two computations.

*Proof.* The first identity is the previous proposition with $x=u$ and $\mathrm{Ad}^{\alpha}_u=\rho_u$; the second is $\rho(u)\rho(v)\rho(u)^{-1}=\rho(\mathrm{Ad}_u(v))=-\rho(\rho_u(v))$, the corollary of *Pin Representations and Clifford Modules with Signed Inner Conjugation*.

## Worked Cases

### The Ideal of the Three-Dimensional Definite Algebra

In $\mathrm{Cl}_{3,0}(\mathbb{R})$ with $e_j^{2}=+1$, let $\pi=\tfrac12(1+e_3)$. Then $\pi^{2}=\pi$ and $\pi$ is primitive, and the minimal left ideal is

$$
I=\mathrm{Cl}_{3,0}\,\pi=\mathrm{span}_{\mathbb{R}}\{\,\pi,\ e_1\pi,\ e_2\pi,\ e_1e_2\pi\,\},
$$

of real dimension four, with the reductions $e_3\pi=\pi$, $e_1e_3\pi=e_1\pi$, $e_2e_3\pi=e_2\pi$ and $\omega\pi=e_1e_2\pi$ for the volume element $\omega=e_1e_2e_3$. The splitting is $I^0=\mathrm{span}\{\pi,e_1e_2\pi\}$ and $I^1=\mathrm{span}\{e_1\pi,e_2\pi\}$, and the odd element $e_1$ acts by

$$
e_1\pi=e_1\pi\in I^1,\qquad e_1(e_1\pi)=\pi\in I^0,\qquad e_1(e_2\pi)=e_1e_2\pi\in I^0,\qquad e_1(e_1e_2\pi)=e_2\pi\in I^1 ,
$$

so it interchanges the two summands, while the even element $e_1e_2$ acts by $e_1e_2\pi\in I^0$, $e_1e_2(e_1\pi)=-e_2\pi\in I^1$ and preserves them.

### The Reflection Read on the Ideal

In the same algebra take $u=e_1$, $v=e_2$ and $\psi=\pi$. Then $\rho_{e_1}$ fixes $e_2$, since $B(e_1,e_2)=0$, and the two computations are

$$
\mathrm{Ad}^{\alpha}_{e_1}(e_2)\,\pi=-e_1e_2e_1\,\pi=e_2\,\pi,\qquad \rho(e_1)\rho(e_2)\rho(e_1)^{-1}\,\pi=e_1e_2e_1\,\pi=-e_2\,\pi ,
$$

because $e_1e_2e_1=-e_2e_1e_1=-e_2$, and the reflection of $e_2$ in $e_1^{\perp}$ is $e_2$ itself. The two computations differ exactly by the sign: the same three factors, with the left one carrying $\alpha$, give $e_2\pi$, and without it give $-e_2\pi$.

### The Volume Element

The volume element $\omega=e_1e_2e_3$ is odd, central and satisfies $\omega^{2}=-1$, and its action on the ideal is left multiplication by $\omega$, which is the map $\psi\mapsto\omega\psi$ sending $I^{0}$ to $I^{1}$ and $I^{1}$ to $I^{0}$. By the corollary of *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*, $\mathrm{Ad}^{\alpha}_\omega=-\mathrm{id}$ while $\mathrm{Ad}_\omega=\mathrm{id}$, so on the ideal the signed conjugation by $\omega$ acts as $-\mathrm{id}$, that is, it separates a spinor from its negative and is not the identity; the inner conjugation by the same central element is invisible on the ideal.

### The Biquaternion Ideal

For $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ the same construction gives an ideal whose elements are the biquaternion spinors of the applications layer, with the two summands of the splitting playing the role of the two chiralities and the odd elements of $\mathrm{Pin}(1,3)$ exchanging them; the compatibility of the ideal with the Lorentz action is the subject of the applications layer and nothing of it is used here.

## Summary

A **minimal left ideal** $I=\mathrm{Cl}(V,q)\pi$ is a left ideal, hence a Clifford module on which the left multiplication by *every* element of the algebra is defined; the whole **Pin group** therefore acts on it by left multiplication, and the ideal carries the pinor representation, with spinors understood as the elements of $I$. If the algebra is simple and $I\neq0$ the action is faithful, and over a product the kernel is $\mathrm{Pin}\cap(\{1\}\times A)$.

The ideal is not homogeneous: it splits as $I=I^0\oplus I^1$ with $I^{i}=\mathrm{Cl}^{i}\pi$, the even elements of the algebra, hence all of $\mathrm{Spin}$, preserve the two summands, and the odd elements of $\mathrm{Pin}$ interchange them. The two summands are the ideal-theoretic counterparts of the two chiral halves of an even-dimensional Clifford module. The signed inner conjugation is realised on the ideal by conjugating the Clifford multiplication with two left multiplications, $\mathrm{Ad}^{\alpha}_x(v)\psi=\rho(\alpha(x))\rho(v)\rho(x)^{-1}\psi$, so the left factor of the two-sided operator appears as the **signed left multiplication** $\Lambda^{\alpha}_x$ and the right factor as the inverse left multiplication; for a vector the plain sandwich gives $-\rho_u(v)\psi$ and the signed one $\rho_u(v)\psi$, which is the sign that the pin theory needs and that the spin theory, confined to the even part, never meets. The central volume element of an odd-dimensional algebra acts on the ideal by the exchange of the two summands, and the signed conjugation by it acts as $-\mathrm{id}$ where the inner conjugation acts as the identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $I=\mathrm{Cl}(V,q)\pi$ | Minimal left ideal, a Clifford module; $\pi$ a primitive idempotent |
| $\rho(x)\psi=x\psi$ | Left action of the algebra, restricted to Pin |
| $I=I^0\oplus I^1$, $I^{i}=\mathrm{Cl}^{i}\pi$ | The parity splitting of the ideal |
| $\mathrm{Cl}^0$ preserves, $\mathrm{Cl}^1$ interchanges | Even and odd elements on the summands |
| $\mathrm{Ad}^{\alpha}_x(v)\psi=\rho(\alpha(x))\rho(v)\rho(x)^{-1}\psi$ | The signed conjugation on the ideal |
| $\Lambda^{\alpha}_x=\rho(\alpha(x))$, $L_{x^{-1}}=\rho(x)^{-1}$ | The one-sided factors, both as left multiplications on the ideal |
| $\rho(\mathrm{Ad}^{\alpha}_u(v))\psi=\rho_u(v)\psi$ | The reflection on the ideal |
| $\rho(u)\rho(v)\rho(u)^{-1}\psi=-\rho_u(v)\psi$ | The same, without the sign |
| $\mathrm{Ad}^{\alpha}_\omega=-\mathrm{id}$, $\mathrm{Ad}_\omega=\mathrm{id}$ | The central volume element, odd dimension |
| $\ker\rho=\mathrm{Pin}\cap(\{1\}\times A)$ | Kernel over a product of simple algebras |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the realisation of spinors as elements of a minimal left ideal and the parity of the ideal.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford action on an ideal, the chirality splitting and the action of the odd part.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for idempotents, minimal ideals and the pin and spin actions upon them.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the original ideal-theoretic construction of the spinors.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for primitive idempotents, minimal left ideals and the action of an algebra on them.
