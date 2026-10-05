# __Involutions of the Endomorphism Algebra__

## Introduction

An involution of the endomorphism algebra $E = \operatorname{End}_F(V)$ is an additive map $E \to E$ of order two that reverses products, and the standard one is the **adjoint** with respect to a non-degenerate pairing on $V$: the endomorphism $A^{*}$ determined by $B(Ax,y) = B(x,A^{*}y)$. This article develops the involutions of $E$ from that example, the laws that make the adjoint an anti-automorphism of order two, the decomposition of $E$ into its self-adjoint and skew-adjoint parts, the matrix description of the involution, and the unitary elements it singles out — the endomorphisms that preserve the pairing.

The pairing-based adjoint of a single endomorphism, its existence and uniqueness, its kernel and image and its relation to the transpose, is *The Adjoint of an Endomorphism*, in the `*`-operator group, and the group that the unitary elements form, with its Lie algebra, is *Unitary Endomorphisms*; this article is the `*`-theory counterpart, and it treats the involution as a structure on the algebra rather than the adjoint as an operator. The transposed involution on the dual, and the comparison of the duality of the dual with the duality of the pairing, are *Involutions of the Dual Space* and *The Involution on the Dual Operator*. The automorphism $X \mapsto T X T^{-1}$ induced by a linear involution, which is an **algebra automorphism** of order two and not an anti-automorphism, belongs to *Involutive Bilinear Algebras*; the two are different kinds of involution of the same algebra and are not conflated here. The forms themselves, their norms and the way they measure, are *Hilbert Algebras*, in Part II, and only the pairing is used here, evaluated to a scalar and never measured.

Throughout, $F$ is a field, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, and $B : V \times V \to F$ is a non-degenerate reflexive pairing: either bilinear with $B(y,x) = \varepsilon B(x,y)$ for a sign $\varepsilon = \pm 1$, or sesquilinear with respect to an involution $\varsigma$ of $F$ with $B(y,x) = \overline{B(x,y)}$ where the bar is $\varsigma$. The case $\varsigma = \mathrm{id}$ is the bilinear case, and a sign $\varsigma(\lambda) = \lambda$ is understood when $\varsigma$ is not mentioned.

## The Adjoint Involution

### Definition and Existence

**Definition.** For $A \in E$ the **adjoint** of $A$ with respect to $B$ is the map $A^{*} : V \to V$ with

$$
B(Ax,y) = B(x,A^{*}y) \qquad \text{for all } x,y \in V .
$$

**Proposition.** The adjoint $A^{*}$ exists, is unique and is linear; the assignment $A \mapsto A^{*}$ is $\varsigma$-semilinear, and it is an involution of the algebra $E$:

$$
(A^{*})^{*} = A, \qquad (A+B)^{*} = A^{*}+B^{*}, \qquad (\lambda A)^{*} = \varsigma(\lambda)A^{*}, \qquad (AB)^{*} = B^{*}A^{*} .
$$

**Proof.** Fix $y$. The map $x \mapsto B(Ax,y)$ is linear, and since $x \mapsto B(x,z)$ is a bijection $V \to V^{*}$ by the non-degeneracy of $B$, there is a unique $A^{*}y$ with $B(x,A^{*}y) = B(Ax,y)$; the uniqueness for each $y$ makes $A^{*}$ a well-defined map. For linearity, $B(x,A^{*}(y+\lambda z)) = B(Ax,y+\lambda z) = B(Ax,y)+\overline{\lambda}B(Ax,z) = B(x,A^{*}y) + \overline{\lambda}B(x,A^{*}z) = B(x, A^{*}y+\overline{\lambda}A^{*}z)$, so $A^{*}(y+\lambda z) = A^{*}y+\overline{\lambda}A^{*}z$ and $A^{*}$ is linear in the bilinear case and satisfies $A^{*}(\lambda y) = \overline{\lambda}A^{*}y$ otherwise. The four laws follow by uniqueness: $B(x,(A^{*})^{*}y) = B(A^{*}x,y) = \overline{B(y,A^{*}x)} = \overline{B(Ay,x)} = B(x,Ay)$; additivity and semilinearity are the definitions; and $B(x,(AB)^{*}y) = B(ABx,y) = B(Bx,A^{*}y) = B(x,B^{*}A^{*}y)$.

**Remark (the kinds).** If $\varsigma = \mathrm{id}$ the involution is **of the first kind**, and it is $F$-linear; if $\varsigma \neq \mathrm{id}$ it is **of the second kind**, and it is conjugate-linear. The reflexive hypothesis is what makes the involution have order two; a general bilinear pairing gives an adjoint with $(A^{*})^{*} = A$ only after the pairing is replaced by its reflexivisation.

### The Fixed and Skew Parts

**Definition.** An endomorphism is **self-adjoint** when $A^{*} = A$, **skew-adjoint** when $A^{*} = -A$, and **normal** when $AA^{*} = A^{*}A$.

**Proposition.** If $\varsigma = \mathrm{id}$ and $2 \neq 0$ in $F$, then $E$ is the direct sum of its self-adjoint and skew-adjoint parts,

$$
E = E^{+} \oplus E^{-}, \qquad E^{\pm} = \{A : A^{*} = \pm A\} ,
$$

and the dimensions are $\dim_F E^{+} = n(n+1)/2$ and $\dim_F E^{-} = n(n-1)/2$ for a symmetric pairing, and the two dimensions exchanged for an antisymmetric one. In the sesquilinear case the self-adjoint elements form an $F^{\varsigma}$-linear space only, and the decomposition is not an $F$-linear decomposition.

**Proof.** For $A \in E$ write $A = \tfrac12(A+A^{*}) + \tfrac12(A-A^{*})$, a sum of a self-adjoint and a skew-adjoint element; the sum is direct because an element that is both satisfies $A = -A$, hence $A = 0$ when $2 \neq 0$. The dimensions are those of the two eigenspaces of the involution $A \mapsto A^{*}$ and are computed in the matrix form below; an antisymmetric pairing exchanges them because the adjoint of $A$ with respect to $-B$ is the negative of its adjoint with respect to $B$.

### The Matrix Form

**Proposition.** Let $\Phi$ be the Gram matrix of $B$, $\Phi_{ij} = B(v_i,v_j)$, in a basis $v_1,\dots,v_n$. Then $\Phi$ is invertible and

$$
[A^{*}] = \Phi^{-1}\,\overline{[A]}^{\mathsf{T}}\,\Phi ,
$$

where the bar applies $\varsigma$ to each entry and the transpose is the matrix transpose. Consequently $\operatorname{tr}A^{*} = \varsigma(\operatorname{tr}A)$ and, in the bilinear case, $\det A^{*} = \det A$.

**Proof.** Writing $B(x,y) = x^{\mathsf{T}}\Phi\overline{y}$ in coordinates and substituting the defining identity gives $A^{\mathsf{T}}\Phi\overline{y} = \Phi\overline{A^{*}y}$ for all $y$, hence $A^{*}= \Phi^{-1}A^{\mathsf{T}}\Phi$ up to the bar; the trace of $\Phi^{-1}A^{\mathsf{T}}\Phi$ is that of $A^{\mathsf{T}}$, and the determinant is the same because the conjugating factors cancel.

**Corollary (the involution is determined by $\Phi$).** Two non-degenerate reflexive pairings give conjugate involutions exactly when their Gram matrices are congruent, $\Phi' = C^{\mathsf{T}}\Phi\overline{C}$ for an invertible $C$; the involution is therefore a function of the congruence class of the pairing.

**Remark (the classification).** Over a field, the involutions of the first kind of the matrix algebra $M_n(F)$ are exactly the maps $A \mapsto \Phi^{-1}A^{\mathsf{T}}\Phi$ with $\Phi$ the Gram matrix of a non-degenerate symmetric or antisymmetric pairing, in the two families **orthogonal** and **symplectic**; the involutions of the second kind arise from sesquilinear pairings and are classified over a field with an involution by the hermitian and the skew-hermitian families. The classification is standard and is *Involutive Rings* and *Central Simple Algebras and the Brauer Group*.

## The Unitary Elements

**Definition.** An endomorphism $A \in E$ is **unitary** for $B$ when $A^{*}A = AA^{*} = \mathrm{id}_V$; equivalently, when $A$ is invertible and $A^{*} = A^{-1}$.

**Proposition.** The unitary elements are exactly the endomorphisms preserving the pairing,

$$
A^{*}A = \mathrm{id} \iff B(Ax,Ay) = B(x,y) \text{ for all } x,y ,
$$

and they form a subgroup $U(V,B)$ of $E^{\times}$; in the bilinear symmetric case it contains $-1$ and the scalars $\lambda$ with $\lambda^{2} = 1$, in the antisymmetric case it contains $1$ and the scalars are $1$ only, and in the sesquilinear case it contains the scalars $\lambda$ with $\lambda\varsigma(\lambda) = 1$.

**Proof.** If $A^{*} = A^{-1}$ then $B(Ax,Ay) = B(x,A^{*}Ay) = B(x,y)$; conversely $B(Ax,Ay)=B(x,y)$ for all $x,y$ gives $B(x,A^{*}Ay) = B(x,y)$, hence $A^{*}A = \mathrm{id}$ by non-degeneracy, and $AA^{*} = \mathrm{id}$ follows because $A$ is invertible, with inverse $A^{*}$. The product of two unitaries is unitary because $(AB)^{*}AB = B^{*}A^{*}AB = B^{*}B = \mathrm{id}$; the identity and inverses are unitary because $(A^{-1})^{*} = (A^{*})^{-1}$. The scalar computation is $(\lambda\mathrm{id})^{*}(\lambda\mathrm{id}) = \varsigma(\lambda)\lambda\,\mathrm{id}$.

**Proposition (the determinant).** In the bilinear case $\det A \det A^{*} = \det(AA^{*}) = 1$ and $\det A^{*} = \det A$, so $\det(A)^{2} = 1$ for a symmetric pairing; for an antisymmetric pairing $\det(A^{*}) = \det(A)$ and one has $\det A = 1$, because the adjoint of a symplectic transformation has determinant $1$ in even dimension.

**Proof.** The first part is multiplicativity of the determinant and $\det A^{*}=\det A$; the antisymmetric case is the standard determinant identity for the symplectic group, quoted from the theory of the classical groups and belonging to *Symmetric Bilinear Algebras* and *Anti-symmetric Bilinear Algebras*.

**Remark (the unitary elements as a set, not yet a group of operators).** This article owns the unitary elements of the involution: the fixed part, the skew part, the matrix description and the preservation criterion. The group structure of $U(V,B)$ as a transformation group, its action on $V$, the subspace it preserves and the Lie algebra of self-adjoint elements under the commutator are *Unitary Endomorphisms*, which follows.

## Summary

A non-degenerate reflexive pairing $B$ on a finite-dimensional space $V$ defines an involution $A \mapsto A^{*}$ of the endomorphism algebra $E = \operatorname{End}_F(V)$ by $B(Ax,y) = B(x,A^{*}y)$; the adjoint exists and is unique, and the assignment is an additive, anti-multiplicative, order-two map, $F$-linear for a bilinear pairing and $\varsigma$-semilinear for a sesquilinear one. Over a field with $2 \neq 0$ and a bilinear pairing the algebra is the direct sum of the self-adjoint and the skew-adjoint parts, of dimensions $n(n+1)/2$ and $n(n-1)/2$ for a symmetric pairing and exchanged for an antisymmetric one; in the sesquilinear case the fixed part is only $F^{\varsigma}$-linear. In a basis the involution is $A \mapsto \Phi^{-1}\overline{A}^{\mathsf{T}}\Phi$ with $\Phi$ the Gram matrix, so it depends on the congruence class of the pairing; the trace and, in the bilinear case, the determinant are preserved. The unitary elements, $A^{*}A = AA^{*} = \mathrm{id}$, are exactly the endomorphisms preserving $B$ and form a subgroup containing the appropriate scalars, with determinant satisfying $\det(A)^{2}=1$ in the symmetric bilinear case and $\det A = 1$ in the antisymmetric case. The classification of the involutions of the matrix algebra, the group structure of the unitary elements and the analytic theory of the forms belong to *Involutive Rings*, *Unitary Endomorphisms* and *Hilbert Algebras* respectively.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $\varsigma$ | the field of scalars and the involution of $F$ of the sesquilinear case |
| $V$, $n$ | the space and its dimension |
| $E = \operatorname{End}_F(V)$ | the endomorphism algebra |
| $B$ | a non-degenerate reflexive pairing on $V$ |
| $A^{*}$ | the adjoint of $A$: $B(Ax,y)=B(x,A^{*}y)$ |
| $(A^{*})^{*}=A$, $(AB)^{*}=B^{*}A^{*}$ | the involution laws |
| $E^{+}$, $E^{-}$ | self-adjoint and skew-adjoint parts, $A^{*}=\pm A$ |
| $\Phi_{ij}=B(v_i,v_j)$ | the Gram matrix |
| $[A^{*}]=\Phi^{-1}\overline{[A]}^{\mathsf{T}}\Phi$ | the matrix form of the involution |
| $U(V,B)$ | the unitary elements, $A^{*}A=AA^{*}=\mathrm{id}$ |
| $\varepsilon$ | the sign of the reflexive bilinear pairing, $B(y,x)=\varepsilon B(x,y)$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for sesquilinear pairings, adjoints and the unitary group.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for involutions of matrix algebras and the classical groups.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the classification of the involutions of a central simple algebra.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the adjoint with respect to a form and the structure of the classical groups.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the orthogonal and symplectic involutions and their determinant behaviour.
