# __The Signed Left Multiplication on a Linear Space__

## Introduction

The one-sided companion of the signed sandwich is the **signed left multiplication** $\Lambda^{\alpha}_{a} = L_a\circ\alpha$, the operator $X \mapsto a\alpha(X)$ on $E = \operatorname{End}_F(V)$, obtained from the signed sandwich by taking the right factor to be the identity. It is the composite of the ordinary left multiplication with the grade involution, so its products are ordinary left multiplications, its inverse is again signed, and its fixed elements are computed from the composite; it is the case $b=1$ of the signed sandwich and the one-sided member of the signed family.

*The Signed Sandwich on a Linear Space* supplies the signed sandwich $\Theta^{\alpha}_{a,b}$ and its laws; *Left and Right Multiplication in a Group* and the one-sided operators supply the group-level analogue; *The Adjoint of the Left Multiplication on a Linear Space* supplies the unsigned case with the trace pairing, and *The Signed Adjoint of the Left Multiplication on a Linear Space* the signed adjoint. *The Graded Action on a Module over a Linear Space* treats the module-level variant. No form is used.

Throughout, $F$ is a field with $2 \neq 0$, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, and $\alpha$ is the grade involution of $E$, $\alpha(X) = TXT$ for a linear involution $T$ of $V$, an algebra automorphism of order two.

## The Signed Left Multiplication

**Definition.** For $a \in E$ the **signed left multiplication** is

$$
\Lambda^{\alpha}_{a} = L_a\circ\alpha, \qquad \Lambda^{\alpha}_{a}(X) = a\,\alpha(X) .
$$

**Proposition.** $\Lambda^{\alpha}_{a}$ is the signed sandwich with the right factor equal to the identity, $\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,1}$, and

$$
\Lambda^{\alpha}_{a} = L_a\circ\alpha = \alpha\circ L_{\alpha(a)} ,
$$

so the signed left multiplication is the ordinary left multiplication by $\alpha(a)$ conjugated by $\alpha$.

**Proof.** The first identity is the definition of the sandwich; for the second, $\alpha L_{\alpha(a)}(X) = \alpha(\alpha(a)X) = a\alpha(X) = \Lambda^{\alpha}_{a}(X)$.

**Proposition (composition).** For all $a,b \in E$,

$$
\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b} = L_{a\alpha(b)}, \qquad
L_a\Lambda^{\alpha}_{b} = \Lambda^{\alpha}_{ab}, \qquad
\Lambda^{\alpha}_{a}L_b = R_{\alpha(b)}\Lambda^{\alpha}_{a} .
$$

In particular the composite of two signed left multiplications is an ordinary left multiplication, and the set $\{L_a : a \in E\} \cup \{\Lambda^{\alpha}_{a} : a \in E\}$ is closed under composition.

**Proof.** $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b}(X) = a\alpha(b\alpha(X)) = a\alpha(b)\alpha(\alpha(X)) = a\alpha(b)X = L_{a\alpha(b)}(X)$; $L_a\Lambda^{\alpha}_{b}(X) = ab\alpha(X) = \Lambda^{\alpha}_{ab}(X)$; $\Lambda^{\alpha}_{a}L_b(X) = a\alpha(X)\alpha(b) = R_{\alpha(b)}(\Lambda^{\alpha}_{a}(X))$. The closure is the three identities together.

**Corollary (invertibility and inverse).** $\Lambda^{\alpha}_{a}$ is invertible if and only if $a$ is invertible, and then

$$
\bigl(\Lambda^{\alpha}_{a}\bigr)^{-1} = \Lambda^{\alpha}_{\alpha(a^{-1})} .
$$

**Proof.** Invertibility follows from the factorisation $\Lambda^{\alpha}_{a} = L_a\alpha$ and the invertibility of $\alpha$; the inverse is checked by the composition law: $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{\alpha(a^{-1})} = L_{a\alpha(\alpha(a^{-1}))} = L_{a a^{-1}} = \mathrm{id}$, and likewise on the other side.

**Proposition (fixed elements).** The fixed space of $\Lambda^{\alpha}_{a}$ is

$$
\ker(\Lambda^{\alpha}_{a}-\mathrm{id}) = \{X \in E : a\alpha(X) = X\} ;
$$

equivalently, when $a$ is invertible, $X$ is fixed exactly when $\alpha(X) = a^{-1}X$. For $a=1$ the fixed space is the fixed part $E^{+}$ of $\alpha$, of dimension $p^2+q^2$ in the matrix-unit basis.

**Proof.** The first display is the definition of the eigenvalue-one equation. For $a=1$ it is $\alpha(X)=X$, whose space is $E^{+}$; the dimension is the computation of *Involutive Linear Spaces*.

**Example.** For $T = \operatorname{diag}(1,-1)$ on $F^2$ and $a = \operatorname{diag}(2,3)$, the signed left multiplication on $M_2(F)$ is $X \mapsto aTXT$; its fixed space is computed from the equations above, and the matrix units $E_{ij}$ are eigenvectors with eigenvalue $a_{ii}(-1)^{i+j}$.

## Summary

The signed left multiplication on $E=\operatorname{End}_F(V)$ is $\Lambda^{\alpha}_{a}=L_a\circ\alpha$, the signed sandwich with right factor one, equal to $\alpha\circ L_{\alpha(a)}$. Its product with another is the ordinary left multiplication $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b}=L_{a\alpha(b)}$; it satisfies $L_a\Lambda^{\alpha}_{b}=\Lambda^{\alpha}_{ab}$ and $\Lambda^{\alpha}_{a}L_b=R_{\alpha(b)}\Lambda^{\alpha}_{a}$, so the signed and ordinary left multiplications together form a closed monoid; it is invertible exactly for invertible $a$, with inverse $\Lambda^{\alpha}_{\alpha(a^{-1})}$; and its fixed space is the solution set of $a\alpha(X)=X$, equal to the fixed part $E^{+}$ of $\alpha$ when $a=1$. The adjoint with respect to the trace pairing, the module-level graded variant and the group-level analogue are the companion articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $V$, $E$ | the field, the space, the endomorphism algebra |
| $\alpha$ | the grade involution, $\alpha(X)=TXT$ |
| $L_a$ | the left multiplication, $L_a(X)=aX$ |
| $\Lambda^{\alpha}_{a}=L_a\circ\alpha$ | the signed left multiplication |
| $\Lambda^{\alpha}_{a}=L_a\alpha=\alpha L_{\alpha(a)}$ | the two factorisations |
| $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b}=L_{a\alpha(b)}$ | the composition law |
| $(\Lambda^{\alpha}_{a})^{-1}=\Lambda^{\alpha}_{\alpha(a^{-1})}$ | the inverse |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for one-sided operators on an algebra and the involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for signed one-sided operators.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the left and right multiplications and their products.
