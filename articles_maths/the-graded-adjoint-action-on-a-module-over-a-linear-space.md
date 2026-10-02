# __The Graded Adjoint Action on a Module over a Linear Space__

## Introduction

The units of the endomorphism algebra act on it by conjugation, $X \mapsto aXa^{-1}$, and this **adjoint action** is the module-level form of the signed inner sandwich; on a graded module over the graded algebra $E = E_0\oplus E_1$ it is compatible with the gradings when the conjugating element is homogeneous, and the compatibility is the statement that conjugation by an even element preserves the two parts of the module while conjugation by an odd element preserves them up to the parity. This article records the adjoint action, its compatibility with the grading, its form on a graded module, and the sign rule, which belongs to the graded category and is deferred.

*Involutions of a Graded Linear Space* supplies the grading of $E$ and the parity of endomorphisms; *The Graded Action on a Module over a Linear Space* supplies the graded module and the compatible action; *The Signed Sandwich on a Linear Space* supplies the signed inner sandwich $\mathrm{Ad}_a\circ\alpha$, of which the adjoint action is the case $\alpha=\mathrm{id}$. *Superalgebras and Graded Structures* owns the sign rule of the graded commutator, named here and not used.

Throughout, $F$ is a field with $2 \neq 0$, $V = V_0\oplus V_1$ is a graded linear space, $E = \operatorname{End}_F(V) = E_0\oplus E_1$ its graded endomorphism algebra with grade involution $\alpha$, and $M = M_0\oplus M_1$ a graded $E$-module with grade involution $\beta$. No form, norm or topology is used.

## The Adjoint Action

**Definition.** For an invertible $a \in E^{\times}$ the **adjoint action** of $a$ on $E$ is

$$
\mathrm{Ad}_a(X) = a\,X\,a^{-1} .
$$

**Proposition.** $\mathrm{Ad}$ is a homomorphism $E^{\times} \to \operatorname{Aut}(E)$ with kernel the centre $Z(E)^{\times}$, so the group of inner automorphisms of $E$ is $E^{\times}/Z(E)^{\times}$; the adjoint action on a graded module $M$ is defined by the same formula, $\mathrm{Ad}_a(m) = a\,m$, together with its inverse, and it is the case $\alpha=\mathrm{id}$ of the signed inner sandwich $\mathrm{Ad}_a\circ\alpha$ of *The Signed Sandwich on a Linear Space*.

**Proof.** $\mathrm{Ad}_a$ is an automorphism with inverse $\mathrm{Ad}_{a^{-1}}$, and $\mathrm{Ad}_{ab}=\mathrm{Ad}_a\mathrm{Ad}_b$; the kernel is the centraliser of $E$, which is the centre; the identification with the signed inner sandwich at $\alpha=\mathrm{id}$ is the definition.

## Compatibility with the Grading

**Proposition.** For $a$ homogeneous, $\mathrm{Ad}_a$ commutes with the grade involution, $\alpha\,\mathrm{Ad}_a = \mathrm{Ad}_a\,\alpha$; more generally $\mathrm{Ad}_a$ commutes with $\alpha$ if and only if $a^{-1}\alpha(a)$ is central in $E$. Consequently $\mathrm{Ad}_a$ preserves the two parts $E_0,E_1$ of the grading exactly when $a^{-1}\alpha(a)$ is central, and in particular for every homogeneous $a$.

**Proof.** $\alpha\mathrm{Ad}_a\alpha(X) = \alpha(a\alpha(X)a^{-1}) = \alpha(a)X\alpha(a)^{-1} = \mathrm{Ad}_{\alpha(a)}(X)$; so $\alpha\mathrm{Ad}_a\alpha=\mathrm{Ad}_{\alpha(a)}$, which equals $\mathrm{Ad}_a$ exactly when $\mathrm{Ad}_{a^{-1}\alpha(a)}$ is the identity, that is when $a^{-1}\alpha(a)$ is central. If $a$ is homogeneous then $\alpha(a)=\pm a$ and $a^{-1}\alpha(a)=\pm1$ is central. Conjugation preserving the eigenspaces $E_0,E_1$ of $\alpha$ is commutation with $\alpha$.

**Corollary.** For homogeneous $a$ and $X$ the parity of $\mathrm{Ad}_a(X)$ is the parity of $X$: conjugation by a homogeneous element preserves the parity; the adjoint action therefore restricts to $\operatorname{GL}(E_0)\times\operatorname{GL}(E_1)$ on the graded pieces.

**Proof.** The preservation of the two parts is the previous proposition, and the parity of a conjugated element is the parity of the element.

## The Adjoint Action on a Graded Module

**Proposition.** A graded module $M$ over $E$ carries the adjoint action $a\cdot m = a\,m$, and the compatibility with the grading, $E_iM_j\subseteq M_{i+j}$ of *The Graded Action on a Module over a Linear Space*, is equivalent to the identity $\beta(a\cdot m) = (-1)^i\,a\cdot\beta(m)$ for $a$ homogeneous of parity $i$; conjugation by a homogeneous element preserves the parity of the elements it acts on.

**Proof.** The identity is the equivalent form of the compatibility; the parity statement is the same computation as for the algebra.

**Remark (the deferred sign rule).** The adjoint action itself carries no sign; the bracket $[X,Y]=XY-YX$ is the infinitesimal form of the adjoint action of the unit group on $E$, and the **graded** bracket $[X,Y]=XY-(-1)^{|X||Y|}YX$, with the sign governed by the parities, belongs to *Superalgebras and Graded Structures*. It is named here because the graded operator articles refer to it, and it is not defined or used.

## Summary

The units of $E = \operatorname{End}_F(V)$ act on $E$ and on a graded $E$-module $M$ by the adjoint action $\mathrm{Ad}_a(X)=aXa^{-1}$, a homomorphism $E^{\times}\to\operatorname{Aut}(E)$ with kernel the centre, which is the case $\alpha=\mathrm{id}$ of the signed inner sandwich. The adjoint action commutes with the grade involution, and hence preserves the graded parts, exactly when $a^{-1}\alpha(a)$ is central, which holds for every homogeneous $a$; conjugation by a homogeneous element therefore preserves parity. On the graded module the adjoint action satisfies the compatibility identity $\beta(a\cdot m)=(-1)^i a\cdot\beta(m)$ for $a$ of parity $i$. The graded commutator and its sign rule are *Superalgebras and Graded Structures*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=V_0\oplus V_1$, $\alpha$ | the graded space and its grade involution |
| $E=\operatorname{End}_F(V)=E_0\oplus E_1$ | the graded endomorphism algebra |
| $M=M_0\oplus M_1$, $\beta$ | the graded module and its grade involution |
| $\mathrm{Ad}_a(X)=aXa^{-1}$ | the adjoint action |
| $E^{\times}/Z(E)^{\times}$ | the group of inner automorphisms |
| $a^{-1}\alpha(a)\in Z(E)$ | the grading-preservation condition |
| $\beta(a\cdot m)=(-1)^i a\cdot\beta(m)$ | the compatibility on the module |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the adjoint action, the inner automorphisms and graded algebras.
- Pierre Deligne and John W. Morgan, *Notes on Supersymmetry (following Joseph Bernstein)*, in *Quantum Fields and Strings* (American Mathematical Society, 1999), for the graded adjoint action and the sign rule.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the inner automorphisms and the centre of an endomorphism ring.
