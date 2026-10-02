# __J-Self-Adjoint and J-Unitary Operators__

## Introduction

On a Krein space $K$ with fundamental symmetry $J$, form $[x,y] = \langle Jx,y\rangle$ and Hilbert adjoint $*$, the adjoint for the indefinite form — written $\dagger$ and called the **$J$-adjoint** — is $T^{\dagger} = JT^{*}J$. It is the unique operator satisfying $[Tx,y] = [x,T^{\dagger}y]$ for all vectors, it is involutive, and it reverses products, $ (ST)^{\dagger} = T^{\dagger}S^{\dagger}$. An operator is **$J$-self-adjoint** when $T^{\dagger} = T$, **$J$-unitary** when $T^{\dagger}T = TT^{\dagger} = 1$, and **$J$-normal** when $T^{\dagger}T = TT^{\dagger}$; these are the indefinite counterparts of self-adjointness, unitarity and normality, and the whole theory of the group rests on the translation between them and their Hilbert analogues.

The translation is simple and useful: $T$ is $J$-self-adjoint exactly when $JT$ is Hilbert-self-adjoint; $T$ is $J$-isometric exactly when it preserves the indefinite form, $[Tx,Ty] = [x,y]$; and $T$ is a $J$-projection exactly when it is a Hilbert projection commuting with $J$. What is not simple is the spectral consequence: a $J$-self-adjoint operator need not have real spectrum, and the failure is the entrance to the spectral theory of *Spectral Theory on Krein Spaces*. The $J$-positive cone, $\{T = T^{\dagger} : [Tx,x]\geq0\}$, is strictly larger than the Hilbert positive cone and contains $J$ itself, so positivity in the indefinite sense is a genuinely weaker notion.

This article fixes the $J$-adjoint, $J$-self-adjointness, $J$-isometry and $J$-unitarity, $J$-projections and $J$-normality, the $J$-positive cone, and the failure of the real spectrum in general.

The Krein space, the fundamental symmetry and the form are *Krein Spaces* and *The Fundamental Symmetry*; the $J$-positive cone and the order are *Krein Algebras* and *The J-Positive Cone and the J-Order*; the spectral theory is *Spectral Theory on Krein Spaces*; the boundedness of $J$ and the topology of $K$ are *Indefinite Inner Product Spaces*. Those are cited. The space is $K$ with form $[\cdot,\cdot]$, fundamental symmetry $J$, Hilbert adjoint $*$ and indefinite adjoint $\dagger$.

## The Indefinite Adjoint

**Definition.** The **$J$-adjoint** of a bounded operator $T$ is $T^{\dagger} = JT^{*}J$.

**Proposition (characterisation and calculus).** $T^{\dagger}$ is the unique bounded operator with

$$
[Tx,y] = [x,T^{\dagger}y] \qquad \text{for all } x, y\in K ;
$$

it satisfies $(T^{\dagger})^{\dagger} = T$, $(ST)^{\dagger} = T^{\dagger}S^{\dagger}$, $(\alpha T + \beta S)^{\dagger} = \bar\alpha T^{\dagger} + \bar\beta S^{\dagger}$, and $\|T^{\dagger}\| = \|T\|$ for the Hilbert norm.

**Proof.** $[Tx,y] = \langle JTx,y\rangle = \langle x,T^{*}Jy\rangle = \langle x,J(JT^{*}J)y\rangle = [x,T^{\dagger}y]$; uniqueness follows because the form is nondegenerate; the calculus is the corresponding calculus of the Hilbert adjoint conjugated by $J$.

**Proposition (the $J$-adjoint is a Hilbert adjoint in disguise).** $T$ is $J$-self-adjoint if and only if $JT$ is Hilbert-self-adjoint; $T$ is $J$-isometric if and only if $T$ preserves the form, $T^{*}JT = J$, and for a bounded $T$ on a Krein space this is already equivalent to $T$ being $J$-unitary.

**Proof.** $T^{\dagger} = JT^{*}J$, so $T$ is $J$-self-adjoint, $T = JT^{*}J$, exactly when $JT = J^{2}T^{*}J = T^{*}J$; and $(JT)^{*} = T^{*}J^{*} = T^{*}J$, so the condition is $JT = (JT)^{*}$, that is, $JT$ Hilbert-self-adjoint. For the second statement, the form is preserved, $[Tx,Ty] = [x,y]$ for all $x,y$, exactly when $T^{\dagger}T = 1$, by nondegeneracy; and $T^{\dagger}T = JT^{*}JT = 1$ is equivalent, after multiplication on the left by $J$, to $T^{*}JT = J$. A bounded operator on a Banach space that has a one-sided inverse is invertible, so $T^{\dagger}T = 1$ also gives $TT^{\dagger} = 1$, and a $J$-isometry is $J$-unitary.

**Remark (the adjoint depends on $J$).** The indefinite adjoint is not intrinsic to the topology of the Krein space: changing the fundamental symmetry changes the form and with it the adjoint. This is the first place where the choice of $J$ is visible at the level of operators, and it is the reason the whole theory of the group is a theory of the pair (Krein space, fundamental symmetry).

## J-Self-Adjointness

**Definition.** $T$ is **$J$-self-adjoint** when $T^{\dagger} = T$; it is **$J$-skew-adjoint** when $T^{\dagger} = -T$; and every $T$ decomposes as $T = \frac{1}{2}(T + T^{\dagger}) + \frac{1}{2}(T - T^{\dagger})$ into a $J$-self-adjoint and a $J$-skew-adjoint part.

**Proposition (the real space of $J$-self-adjoint operators).** The $J$-self-adjoint operators form a real vector space, closed under the $J$-adjoint; they are exactly the operators $T$ with $JT$ Hilbert-self-adjoint; and $T^{\dagger}T$ is $J$-self-adjoint for every $T$.

**Proof.** $T^{\dagger} = T$ is a real-linear condition; the identification with $JT = (JT)^{*}$ is the previous proposition; and $(T^{\dagger}T)^{\dagger} = T^{\dagger}(T^{\dagger})^{\dagger} = T^{\dagger}T$.

**Proposition (the quadratic form is real but not sign definite).** If $T$ is $J$-self-adjoint then $[Tx,x]$ is real for every $x$, and the numerical range of $T$ is symmetric with respect to the real axis; but $[Tx,x]$ need not have a constant sign, and the range can contain both signs.

**Proof.** $[Tx,x] = \overline{[x,Tx]} = \overline{[T^{\dagger}x,x]} = \overline{[Tx,x]}$ by $J$-self-adjointness; the indefiniteness is that of the form itself, since $T = J$ is $J$-self-adjoint with $[Jx,x] = \langle x,x\rangle>0$ for $x\neq0$ while $T = -J$ is also $J$-self-adjoint with $[-Jx,x]<0$.

## J-Isometry, J-Unitarity, J-Projection, J-Normality

**Definition.** $T$ is **$J$-isometric** when $T^{\dagger}T = 1$, **$J$-unitary** when $T^{\dagger}T = TT^{\dagger} = 1$, **$J$-normal** when $T^{\dagger}T = TT^{\dagger}$, and a **$J$-projection** when $P^{2} = P = P^{\dagger}$.

**Theorem (isometry is form preservation).** $T$ is $J$-isometric if and only if $[Tx,Ty] = [x,y]$ for all $x, y$; $T$ is $J$-unitary if and only if it is $J$-isometric and surjective. The $J$-unitary operators form a group, the **$J$-unitary group** $\mathcal{U}_{J}(K)$, and the $J$-isometric operators are the isometries of the form.

**Proof.** $[Tx,Ty] = [x,T^{\dagger}Ty]$, so preservation of the form is $T^{\dagger}T = 1$; surjectivity of a $J$-isometry gives an inverse which is $J$-isometric by the same identity applied to the inverse, and the group axioms follow from the composition rules.

**Theorem ($J$-projections are the projections commuting with $J$).** An operator $P$ is a $J$-projection if and only if $P$ is an orthogonal projection with $PJ = JP$.

**Proof.** If $P = P^{2} = P^{\dagger}$ then $JP^{*}J = P$ and $P$ is an idempotent; from $JP^{*}J = P$ one gets $JP^{*} = PJ$ and $P^{*}J = JP$, whence $P^{*} = P$ and then $PJ = JP$; conversely an orthogonal projection commuting with $J$ satisfies $P^{\dagger} = JP^{*}J = JPJ = P$.

**Proposition (normality).** $T$ is $J$-normal when $T^{\dagger}T = TT^{\dagger}$, that is when $JT^{*}JT = TJT^{*}J$. The $J$-self-adjoint and the $J$-unitary operators are $J$-normal; the class is closed under the $J$-adjoint; and an invertible $J$-normal operator has $T^{\dagger}T^{-1}$ $J$-unitary.

**Proof.** The inclusions are the definitions; for the invertible case, $(T^{\dagger}T^{-1})^{\dagger}(T^{\dagger}T^{-1}) = (T^{\dagger})^{-1}T^{\dagger\dagger}T^{\dagger}T^{-1} = (T^{\dagger})^{-1}TT^{\dagger}T^{-1} = (T^{\dagger})^{-1}T^{\dagger}TT^{-1} = 1$ using $TT^{\dagger} = T^{\dagger}T$, and the reverse product is analogous, so the operator is $J$-unitary.

**Remark (what normality is not).** $J$-normality is not the same as the Hilbert normality of $JT$: the two conditions are $JT^{*}JT = TJT^{*}J$ and $T^{*}T = JTT^{*}J$, and neither implies the other. This is a first sign that the indefinite theory keeps the formal shape of the Hilbert theory without transporting all of its consequences.

## The J-Positive Cone

**Definition.** The **$J$-positive cone** is

$$
\{T : T = T^{\dagger},\ [Tx,x]\geq0 \text{ for every } x\in K\} .
$$

**Proposition (translation to Hilbert positivity).** $T$ is $J$-positive if and only if $T = T^{\dagger}$ and $JT\geq0$ (Hilbert-positive). So the $J$-positive cone is the image under the map $T\mapsto JT$ of the Hilbert positive cone intersected with the $J$-self-adjoint condition.

**Proof.** $[Tx,x] = \langle JTx,x\rangle$, and $JT$ is self-adjoint exactly when $T$ is $J$-self-adjoint, so the condition is the Hilbert-positivity of $JT$.

**Proposition (the cone is larger and contains $J$).** The $J$-positive cone contains the Hilbert positive cone; it strictly contains it when $\kappa>0$; and $J$ itself is $J$-positive, since $[Jx,x] = \langle x,x\rangle\geq0$, while $J$ is not Hilbert-positive when $\kappa>0$.

**Proof.** If $T\geq0$ in the Hilbert sense and $T = T^{\dagger}$ then $JT$ need not be positive; but for $T$ proportional to a $J$-projection commuting with $J$ the two notions agree; the element $J$ has $J^{\dagger} = J$ and $J\cdot J = 1\geq0$, so $J$ is $J$-positive, and its Hilbert spectrum contains $-1$.

**Remark (positivity is J-relative).** The $J$-positive cone depends on the fundamental symmetry and is not comparable with the Hilbert positive cone beyond the containment just computed; in particular the $J$-positive elements do not form a cone that doubles as an operator-theoretic positivity in the Hilbert sense. This is the reason the spectral theory of $J$-self-adjoint operators has no analogue of the spectral theorem's ordering, and it is taken up in *Spectral Theory on Krein Spaces* and *Definitizable Operators and the Krein–Naĭmark Theorem*.

## The Failure of the Real Spectrum

**Proposition (a $J$-self-adjoint operator need not have real spectrum).** In the Krein space $\mathbb{C}^{1,1}$ with $J = \mathrm{diag}(1,-1)$ the operator

$$
T = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}
$$

is $J$-self-adjoint, since $JT = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ is symmetric, and its spectrum is $\{i, -i\}$: non-real.

**Proof.** Direct computation of $JT$ and of the characteristic polynomial $\lambda^{2} + 1$.

**Proposition (conjugate symmetry).** The spectrum of a $J$-self-adjoint operator is symmetric with respect to the real axis: $\lambda\in\sigma(T)$ implies $\bar\lambda\in\sigma(T)$, with the same multiplicity; and the resolvent is $J$-self-adjoint at points where it is defined.

**Proof.** The conjugate of $T$ is similar to $T$: $\bar T = JTJ^{-1}$ for real $J$, so $\sigma(\bar T) = \sigma(T)$; the resolvent statement is $(\lambda - T)^{\dagger} = \bar\lambda - T$.

**Remark (what replaces the spectral theorem).** For a Hilbert-self-adjoint operator the spectrum is real and the spectral theorem produces a functional calculus. For a $J$-self-adjoint operator the spectrum is only conjugate-symmetric, the real points need not be semi-bounded, and complex points occur in conjugate pairs; the spectral theory is therefore a theory of invariant subspaces and root subspaces rather than of projections, and it is the subject of the next articles, *Spectral Theory on Krein Spaces* and *Definitizable Operators and the Krein–Naĭmark Theorem*.

## Worked Cases

### The Fundamental Symmetry

$J$ is $J$-self-adjoint and $J$-unitary, since $J^{\dagger} = JJ^{*}J = J$ and $J^{2} = 1$; its Hilbert spectrum contains $-\lambda$ for each $\lambda$ in the negative part of the fundamental decomposition, which shows how far the indefinite spectral data is from the Hilbert one.

### The Rotated Multiplications

For $A = M_n(\mathbb{C})$ with the indefinite form defined by $J$, the $J$-self-adjoint elements are the solutions of $JT^{*}J = T$, the $J$-unitary ones solve $T^{*}JT = J$, and the trace of a $J$-positive element is real but need not be positive for the Hilbert form; these are the $J$-analogues of the Hermitian matrices and the unitary group, and they generate the $J$-version of the matrix algebra.

### The One-Dimensional Case

For $K$ of dimension one with the definite form the $J$-adjoint is the Hilbert adjoint and the theory reduces to the Hilbert one; the failure of the real spectrum and the enlargement of the cone both require $\kappa>0$, so the indefinite theory is invisible in a definite space.

## Summary

The **$J$-adjoint** on a Krein space with fundamental symmetry $J$ is $T^{\dagger} = JT^{*}J$, characterised by $[Tx,y] = [x,T^{\dagger}y]$ and reversing products; an operator is **$J$-self-adjoint** when $T^{\dagger} = T$, equivalently when $JT$ is Hilbert-self-adjoint, **$J$-isometric** when $T^{\dagger}T = 1$, equivalently when it preserves the form, **$J$-unitary** when $T^{\dagger}T = TT^{\dagger} = 1$, equivalently when it is a surjective form-isometry, **$J$-normal** when $T^{\dagger}T = TT^{\dagger}$, and a **$J$-projection** when $P^{2} = P = P^{\dagger}$, equivalently when $P$ is an orthogonal projection commuting with $J$. The **$J$-positive cone** is $\{T = T^{\dagger} : JT\geq0\}$; it contains the Hilbert positive cone, it strictly contains it when $\kappa>0$, and it contains $J$ itself, so indefinite positivity is genuinely weaker than Hilbert positivity. Unlike a self-adjoint operator, a **$J$-self-adjoint operator need not have real spectrum** — the operator $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ in $\mathbb{C}^{1,1}$ has spectrum $\{i,-i\}$ — the spectrum is only conjugate-symmetric, and the resulting theory of invariant and root subspaces is *Spectral Theory on Krein Spaces* and *Definitizable Operators and the Krein–Naĭmark Theorem*. The space and the symmetry are *Krein Spaces* and *The Fundamental Symmetry*, the positivity is *Krein Algebras* and *The J-Positive Cone and the J-Order*, and the adjoint for the form is *Indefinite Inner Product Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{\dagger} = JT^{*}J$ | The $J$-adjoint |
| $[Tx,y] = [x,T^{\dagger}y]$ | Characterisation of the $J$-adjoint |
| $T^{\dagger} = T \iff JT = (JT)^{*}$ | $J$-self-adjointness |
| $T^{\dagger}T = 1 \iff [Tx,Ty] = [x,y]$ | $J$-isometry |
| $\mathcal{U}_{J}(K)$ | The $J$-unitary group |
| $P^{2} = P = P^{\dagger} \iff PJ = JP$ | $J$-projection |
| $T$ $J$-positive $\iff JT\geq0$ | The $J$-positive cone |
| $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ | $J$-self-adjoint with spectrum $\{i,-i\}$ |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the $J$-adjoint, $J$-unitary operators and the $J$-positive cone.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the linear algebra of $J$-self-adjoint and $J$-unitary operators.
- Peter Jonas, "On the spectral theory of operators on Krein spaces", in *Operator Theory: Advances and Applications* (Birkhäuser), for the spectral consequences.
- Tomas Ya. Azizov and I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the systematic theory.
- Mark G. Kreĭn and Heinz Langer, "On the spectral function of a self-adjoint operator in a space with indefinite metric" (1973), for the spectral function of a $J$-self-adjoint operator.
