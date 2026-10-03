
# __Self-Adjoint and Skew Operators with Hermitian Adjoint__

## Introduction

The adjoint $\ast$ turns the algebra $\mathrm{End}_A(S)$ of operators on a Hermitian Clifford module into a **$\ast$-algebra**, and a $\ast$-algebra is cut into two halves by its involution. The operators fixed by the adjoint, $T^{\ast} = T$, are **self-adjoint**; the operators negated by it, $T^{\ast} = -T$, are **skew-adjoint**; and every operator is the sum of a self-adjoint and a skew-adjoint part, $T = \tfrac12(T+T^{\ast}) + \tfrac12(T-T^{\ast})$, whenever $2$ is invertible. The two halves carry the two algebraic structures of the theory: the skew-adjoint operators close under the commutator and form the **Lie algebra** of the unitary group of the form, and the self-adjoint operators close under the anticommutator (the circle product) and form the **Jordan algebra** that describes the symmetric space of the theory.

The article assembles this structure for the form $\langle s,t\rangle = \mathrm{Sc}(s^{\dagger}t)$ of *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint* and for the same form on the algebra, and it computes its two characteristic instances: the left and right regular representations, where self-adjointness of the operator is equivalent to self-adjointness of the element, and the Lie algebra of the unitary slice, where the skew-adjoint operators are exactly the inner derivations. The three product relations of the $\ast$-algebra — the commutator of two self-adjoint operators is skew-adjoint, the commutator of a self-adjoint and a skew-adjoint operator is self-adjoint, and the anticommutator of two self-adjoint operators is self-adjoint — are the algebraic form of the three-fold decomposition of the unitary group, whose geometric reading as a flag manifold is Part IV's, and they are the reason the adjoint theory is exhaustive: because the involution is the only structure that the module form imposes on the operators, the whole theory — the group, the symmetric space on which the self-adjoint half acts, and the spectra — is encoded in the one splitting.

The adjoint is *The Adjoint of the One-Sided Action with Hermitian Adjoint*; the module and its form are *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*; the two-sided operators are *Two-Sided Operators on a Clifford Algebra* and *Mixed Inner Conjugation and Hermitian Adjoint*; the Hermitian sandwich is *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*; the unitary slice, the compact real form and the Lie algebra are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the positivity and the cone are *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint*; the spectral theory of the self-adjoint operators is *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*; the bilinear and Dirac operators are *Bilinear Operators on a Hermitian Module with Hermitian Adjoint*, *Dirac Operators with Hermitian Adjoint* and *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint*; and the application to the orthogonal group is *The Spinor Norm and the Structure of the Orthogonal Group with Inner Conjugation*.

## The $\ast$-Algebra of Operators

### The Adjoint

**Definition.** Let $(S,\langle\,,\rangle)$ be a Hermitian Clifford module with sesquilinear form $\langle s,t\rangle = \mathrm{Sc}(s^{\dagger}t)$, conjugate-linear in $s$ and linear in $t$. For $T\in\mathrm{End}_A(S)$ the **adjoint** $T^{\ast}$ is the operator with

$$
\langle Ts,t\rangle = \langle s,T^{\ast}t\rangle \qquad (s,t\in S),
$$

which exists and is unique because the form is non-degenerate.

**Proposition (the involution).** The adjoint satisfies

$$
(S+T)^{\ast} = S^{\ast}+T^{\ast}, \qquad (ST)^{\ast} = T^{\ast}S^{\ast}, \qquad (T^{\ast})^{\ast} = T, \qquad (\lambda T)^{\ast} = \bar\lambda\,T^{\ast},
$$

so that $\mathrm{End}_A(S)$ is a $\ast$-algebra. The adjoint is **contravariant** for the product, that is, it is an anti-automorphism of order two; this was checked on the two-sided operators of the regular module, where $(TU)^{\ast} = U^{\ast}T^{\ast}$ for general $T,U$.

### Self-Adjoint, Skew-Adjoint and the Decomposition

**Definition.** An operator is **self-adjoint** if $T^{\ast} = T$, **skew-adjoint** if $T^{\ast} = -T$, and **normal** if it commutes with its adjoint, $TT^{\ast} = T^{\ast}T$.

**Theorem (the decomposition).** If $2$ is invertible in the ground ring, every operator is the sum of its **self-adjoint part** and its **skew-adjoint part**,

$$
T = H(T) + K(T), \qquad H(T) = \tfrac12(T+T^{\ast}), \qquad K(T) = \tfrac12(T-T^{\ast}),
$$

with $H(T)^{\ast} = H(T)$ and $K(T)^{\ast} = -K(T)$; the parts are unique, and $T$ is self-adjoint iff $K(T) = 0$ and skew-adjoint iff $H(T) = 0$. So

$$
\mathrm{End}_A(S) = \mathrm{Herm}_A(S)\oplus\mathrm{Skew}_A(S)
$$

as vector spaces, with $\mathrm{Herm}_A(S)$ the self-adjoint operators and $\mathrm{Skew}_A(S)$ the skew-adjoint operators. This was checked for the two-sided operators of the regular module: $H(T)$ self-adjoint, $K(T)$ skew-adjoint, and $H(T)+K(T) = T$.

**Remark (the reality conditions).** Over a real form the self-adjoint and the skew-adjoint operators are the **symmetric** and the **skew-symmetric** operators for the bilinear form; over the complex algebra they are the Hermitian and the anti-Hermitian operators. The involution is the same algebraic object in both cases, and its sign is the only thing the reality condition changes.

## The Two Structures

### The Skew-Adjoint Part is a Lie Algebra

**Theorem (the commutator).** The commutator of two operators satisfies

$$
[S,T]^{\ast} = [T^{\ast},S^{\ast}],
$$

verified on the regular module. Consequently

$$
[\mathrm{Herm},\mathrm{Herm}]\subseteq\mathrm{Skew}, \qquad [\mathrm{Herm},\mathrm{Skew}]\subseteq\mathrm{Herm}, \qquad [\mathrm{Skew},\mathrm{Skew}]\subseteq\mathrm{Skew},
$$

so the skew-adjoint part is closed under the commutator and is a **Lie algebra**, while the commutator couples the two parts with the signs of a **graded Lie algebra**. All three inclusions were checked: with generic self-adjoint operators $H_1,H_2$ and generic skew-adjoint $K_1,K_2$ the commutators $[H_1,H_2]$, $[H_1,K_2]$, $[K_1,K_2]$ landed in $\mathrm{Skew}$, $\mathrm{Herm}$, $\mathrm{Skew}$ respectively.

**Corollary (the Lie algebra of the unitary group).** The skew-adjoint operators form the Lie algebra of the group $U$ of form-preserving operators, the bracket being the commutator, and the exponential $\exp(tK)$ of a skew-adjoint $K$ is a one-parameter family of form-preserving operators. This is the operator form of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*, where the same family is described by the algebraic condition $u^{\dagger}u = 1$.

### The Self-Adjoint Part is a Jordan Algebra

**Theorem (the circle product).** The **circle product** (the anticommutator) $H\bullet H' = \tfrac12(HH'+H'H)$ of two self-adjoint operators is self-adjoint,

$$
H^{\ast} = H,\ H'^{\ast} = H' \ \Longrightarrow \ (H\bullet H')^{\ast} = H\bullet H' ,
$$

and it is commutative and satisfies the Jordan identity, so the self-adjoint part is a **Jordan algebra**. This was checked: $H\bullet H'$ landed in $\mathrm{Herm}$ for generic self-adjoint $H,H'$.

**Proof.** $(HH'+H'H)^{\ast} = H'^{\ast}H^{\ast}+H^{\ast}H'^{\ast} = H'H+HH'$, the same operator.

**Remark (the two halves of the Cartan decomposition).** The splitting $\mathrm{End}_A(S) = \mathrm{Herm}\oplus\mathrm{Skew}$ is the algebraic Cartan decomposition of the $\ast$-algebra: the skew part is the Lie algebra of the group of form-preserving operators, the self-adjoint part is closed under the circle product and is a Jordan algebra, and the commutator couples the two halves with the signs of a graded Lie algebra. The positive part of the self-adjoint half is the Hermitian cone of *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint*. The geometric reading — the self-adjoint half as the tangent space of a symmetric space, the group as its motion group — is made in Part IV, where a tangent space is available.

### Orthogonality and the Hilbert Structure

**Theorem (the two parts are orthogonal).** With respect to the **Hilbert–Schmidt form** $\langle S,T\rangle_{HS} = \mathrm{Sc}(S^{\ast}T)$ on the operators, the real part of the product of a self-adjoint and a skew-adjoint operator vanishes,

$$
\mathrm{Re}\,\langle H,K\rangle_{HS} = 0 \qquad (H^{\ast} = H,\ K^{\ast} = -K),
$$

verified on the regular module. So the splitting $\mathrm{End} = \mathrm{Herm}\oplus\mathrm{Skew}$ is an **orthogonal** decomposition for the Hilbert–Schmidt form; the Hilbert-Schmidt form is positive definite exactly when the module form and the trace form are, that is, in the compact definite case.

## The Regular Representation

### Left and Right Multiplication

**Proposition (self-adjointness of the regular representations).** For $a\in A$ with the Hermitian–Schmidt form $\langle x,y\rangle = \mathrm{Sc}(x^{\dagger}y)$ of *The Blade Form and the Hilbert Structure with Hermitian Adjoint*, let $L_a$ and $R_a$ be the left and the right multiplications. Then

$$
L_a^{\ast} = L_{a^{\dagger}}, \qquad R_a^{\ast} = R_{a^{\dagger}} ,
$$

so $L_a$ and $R_a$ are self-adjoint iff $a^{\dagger} = a$, and skew-adjoint iff $a^{\dagger} = -a$. These identities were checked on the regular module of $\mathrm{Cl}_{1,3}(\mathbb{R})$ in the indefinite form, where $L_a^{\ast} = L_{a^{\dagger}}$ and $R_a^{\ast} = R_{a^{\dagger}}$ for general $a$, and on $\mathrm{Cl}_{0,3}(\mathbb{R})$ in the definite form: the operator $L_a$ is self-adjoint exactly for self-adjoint $a$.

**Corollary (the inner derivations).** The inner derivation $\mathrm{ad}_a = L_a - R_a$, $\mathrm{ad}_a(x) = ax-xa$, has adjoint $\mathrm{ad}_a^{\ast} = \mathrm{ad}_{a^{\dagger}}$; hence $\mathrm{ad}_a$ is self-adjoint iff $a$ is self-adjoint and skew-adjoint iff $a$ is skew-adjoint. The inner derivations by the skew-adjoint elements are the skew-adjoint operators that exponentiate to inner automorphisms, and they are the image in the operator algebra of the Lie algebra of the algebra's own unitary group.

### The Hermitian and the Skew Part of the Algebra

**Definition.** The **Hermitian part** of the algebra is $A^{+} = \{a : a^{\dagger} = a\}$ and the **skew part** is $A^{-} = \{a : a^{\dagger} = -a\}$, so that $A = A^{+}\oplus A^{-}$ for $2$ invertible.

**Proposition (the blade description).** In the orthonormal blade basis the dagger acts on a blade $e_{i_1}\cdots e_{i_k}$ of degree $k$ by the sign $(-1)^{T_k}$, $T_k = k(k+1)/2$, so

$$
A^{+} = \mathrm{span}\{e_{A} : |A|\equiv 0 \text{ or } 3 \pmod 4\}, \qquad A^{-} = \mathrm{span}\{e_{A} : |A|\equiv 1 \text{ or } 2 \pmod 4\},
$$

independently of the signature of $q$; on the fixed degrees $0,1,2,3$ this gives $\dagger = +,-,-,+$. The self-adjoint blades are thus degrees $0$ and $3$ mod $4$, and the grading of the splitting is the mod-$4$ residue of the degree, which is the operator form of the Fierz grade signs of *Bilinear Operators on a Hermitian Module with Hermitian Adjoint*.

**Proof.** $e_A^{\dagger} = (-1)^{T_{|A|}}e_A$ because the dagger is $\alpha\circ\mathrm{rev}$ composed with conjugation, $\mathrm{rev}$ contributes $(-1)^{|A|(|A|-1)/2}$ and $\alpha$ contributes $(-1)^{|A|}$, whose sum is $(-1)^{|A|(|A|+1)/2} = (-1)^{T_{|A|}}$; the residues $T_k \bmod 2$ are $0,1,1,0,\dots$ for $k = 0,1,2,3,\dots$.

## Worked Cases

### The Definite Case $\mathrm{Cl}_{0,3}(\mathbb{R})$

With the dagger positive, the Gram form of the regular module is the identity in the blade basis and the operator adjoint is the transpose. The Hermitian part of the algebra is $A^{+} = \mathrm{span}\{1,\omega\}$ with $\omega = e_1e_2e_3$ the volume element, so the only central Hermitian elements are here; the self-adjoint operators are the transversals of $L_{a^{+}}+R_{b^{+}}$ with $a^{+},b^{+}\in A^{+}$. The skew-adjoint operators contain the inner derivations $\mathrm{ad}_a$ for skew $a$, which are the rotations of the module, and their exponentials are the even unitary elements of the slice of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*.

### The Indefinite Case $\mathrm{Cl}_{1,3}(\mathbb{R})$

With the Minkowski form the Gram matrix is diagonal with entries $+1,-1$ in the blade basis, and the operator adjoint $T^{\ast} = G^{-1}T^{H}G$ is a **twisted** transpose; this is the operator-level reason an indefinite Clifford algebra has self-adjoint operators that the positive-definite picture does not see. The Hermitian part is $A^{+} = \mathrm{span}\{e_A : |A|\equiv0,3\pmod4\}$, of degrees $0,3,4$, which is non-central, so the self-adjoint operators do not commute and the Jordan algebra is non-abelian. The three Cartan inclusions and the Jordan closure were all verified here on generic self-adjoint and skew-adjoint operators of the regular module, and the Hilbert–Schmidt orthogonality held as well.

## Summary

The adjoint $T\mapsto T^{\ast}$, defined by $\langle Ts,t\rangle = \langle s,T^{\ast}t\rangle$, makes $\mathrm{End}_A(S)$ a $\ast$-algebra, contravariant for the product and of order two. The **self-adjoint** operators $T^{\ast} = T$ and the **skew-adjoint** operators $T^{\ast} = -T$ split the operator algebra, $\mathrm{End} = \mathrm{Herm}\oplus\mathrm{Skew}$, with the parts unique and orthogonal for the Hilbert–Schmidt form. The **skew-adjoint** operators form a **Lie algebra** under the commutator, the **self-adjoint** ones a **Jordan algebra** under the circle product, and the commutator couples them by the graded rules $[\mathrm{Herm},\mathrm{Herm}]\subseteq\mathrm{Skew}$, $[\mathrm{Herm},\mathrm{Skew}]\subseteq\mathrm{Herm}$, $[\mathrm{Skew},\mathrm{Skew}]\subseteq\mathrm{Skew}$; all of these were verified on the regular module of $\mathrm{Cl}_{1,3}(\mathbb{R})$.

The regular representations realize the structure on the algebra itself: $L_a^{\ast} = L_{a^{\dagger}}$ and $R_a^{\ast} = R_{a^{\dagger}}$, so $L_a$ is self-adjoint exactly for $a$ self-adjoint, and the inner derivations $\mathrm{ad}_a$ are self-adjoint or skew-adjoint according to the element $a$. The Hermitian part of the algebra is $\mathrm{span}\{e_A : |A|\equiv0,3\pmod4\}$, the dagger acting on a blade by the Fierz sign $(-1)^{T_{|A|}}$, so the splitting of the operators restricts to the mod-four gradation of the blades; the skew-adjoint operators are the Lie algebra of the unitary group, the self-adjoint ones the symmetric space, and the positive self-adjoint elements the Hermitian cone. The spectral theory of the self-adjoint part is the subject of *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle Ts,t\rangle=\langle s,T^{\ast}t\rangle$ | Defining property of the adjoint |
| $(ST)^{\ast}=T^{\ast}S^{\ast}$, $(T^{\ast})^{\ast}=T$ | The involution (anti-automorphism of order two) |
| $H(T)=\tfrac12(T+T^{\ast})$, $K(T)=\tfrac12(T-T^{\ast})$ | Self-adjoint and skew-adjoint parts |
| $\mathrm{End}=\mathrm{Herm}\oplus\mathrm{Skew}$ | The decomposition |
| $[\mathrm{Herm},\mathrm{Herm}]\subseteq\mathrm{Skew}$, $[\mathrm{Herm},\mathrm{Skew}]\subseteq\mathrm{Herm}$, $[\mathrm{Skew},\mathrm{Skew}]\subseteq\mathrm{Skew}$ | Graded Lie structure |
| $H\bullet H'=\tfrac12(HH'+H'H)$ self-adjoint | Jordan structure |
| $L_a^{\ast}=L_{a^{\dagger}}$, $R_a^{\ast}=R_{a^{\dagger}}$ | Regular representations |
| $\mathrm{ad}_a^{\ast}=\mathrm{ad}_{a^{\dagger}}$ | Inner derivations |
| $A^{\pm}=\mathrm{span}\{e_A : |A|\equiv0,3\,/\,1,2\pmod4\}$ | Hermitian and skew part of the algebra |
| $\mathrm{Re}\langle H,K\rangle_{HS}=0$ | Orthogonality of the two parts |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the involution on the algebra of operators, the self-adjoint and skew-adjoint elements and the decomposition.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford Mathematical Monographs (Clarendon Press, 1994), for the Jordan-algebra structure of the self-adjoint part, the circle product and the symmetric cone.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for the Cartan decomposition, the symmetric space and the graded Lie algebra of a $\ast$-algebra.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grade signs, the Hermitian part of a Clifford algebra and the Lie algebras of the classical groups.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the involution, the symmetric and the alternating elements and the associated Lie and Jordan structures.
