# __The Two Adjoints of the Two Algebras in Examples__

## Introduction

Each of the two general products carries an adjoint calculus, one adjoint for each pairing, and this article gathers the two rules and works them on examples. The plain product gives the transpose of the regular operators with respect to the plain pairing; the quaternionic product gives the conjugate transpose with respect to the quaternion pairing. The article is a synthesis: the operator calculus is *Association and the Transpose on the Quaternion Algebra* and the two operator articles of the general quaternionic block, above this article in this category, and the two forms that define them are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, above this article in this category.

## The Two Adjoint Rules

**Definition.** Let $L_{\tilde x}(\tilde y)=\tilde x\tilde y$ and $R_{\tilde x}(\tilde y)=\tilde y\tilde x$ be the left and the right multiplication of the plain product, and let $\langle\cdot,\cdot\rangle$ be a pairing. The **adjoint** of an operator $T$ is the operator $T^{\dagger}$ with
$$
\langle T\tilde y,\tilde z\rangle=\langle\tilde y,T^{\dagger}\tilde z\rangle \qquad\text{for all }\tilde y,\tilde z .
$$

**Theorem.** For the plain pairing $B(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p\tilde q)$,
$$
L_{\tilde x}^{\dagger}=R_{\tilde x} , \qquad R_{\tilde x}^{\dagger}=L_{\tilde x} ;
$$
for the quaternion pairing $N(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p^{\natural}\tilde q)$,
$$
L_{\tilde x}^{\dagger}=L_{\tilde x^{\natural}} , \qquad R_{\tilde x}^{\dagger}=R_{\tilde x^{\natural}} .
$$

**Proof.** For the plain product, $B(L_{\tilde x}\tilde y,\tilde z)=\operatorname{Sc}(\tilde x\tilde y\tilde z)$ and $B(\tilde y,R_{\tilde x}\tilde z)=\operatorname{Sc}(\tilde y\tilde z\tilde x)$; the two are equal by the invariance of the scalar part under the cyclic permutation of a product, $\operatorname{Sc}(abc)=\operatorname{Sc}(bca)=\operatorname{Sc}(cab)$. The second identity follows by symmetry, or by taking the adjoint of the first. For the quaternionic product, $N(L_{\tilde x}\tilde y,\tilde z)=\operatorname{Sc}((\tilde x\tilde y)^{\natural}\tilde z)=\operatorname{Sc}(\tilde y^{\natural}\tilde x^{\natural}\tilde z)=N(\tilde y,L_{\tilde x^{\natural}}\tilde z)$, using $(\tilde x\tilde y)^{\natural}=\tilde y^{\natural}\tilde x^{\natural}$; the right-hand identity is the same computation with the cyclic order carried the other way, $N(R_{\tilde x}\tilde y,\tilde z)=\operatorname{Sc}((\tilde y\tilde x)^{\natural}\tilde z)=\operatorname{Sc}(\tilde x^{\natural}\tilde y^{\natural}\tilde z)=N(\tilde y,R_{\tilde x^{\natural}}\tilde z)$.

The two rules are one rule: the adjoint of a regular operator is the regular operator whose parameter is the parameter's conjugate, and the conjugation moves from the parameter to the side on which the plain pairing is read, because the plain pairing does not conjugate and the quaternion pairing does.

## Worked Examples

**Example 1 (the two adjoints of $L_{e_1}$).** The left multiplication by $e_1$ sends $\tilde y=y_0e_0+y_1e_1+y_2e_2+y_3e_3$ to $e_1\tilde y=-y_1e_0+y_0e_1-y_3e_2+y_2e_3$. With respect to the plain pairing its adjoint is $R_{e_1}$, no sign, and with respect to the quaternion pairing its adjoint is $L_{e_1^{\natural}}=L_{-e_1}$, the left multiplication by $-e_1$. The two adjoints differ by the sign carried by the conjugation.

**Example 2 (a general element).** For $\tilde x=x_0+\vec x$, the plain adjoint of $L_{\tilde x}$ is $R_{\tilde x}=R_{x_0+\vec x}$, which differs from $L_{\tilde x}$ exactly when $\vec x\neq0$, the plain product being non-commutative; the quaternion adjoint is $L_{\tilde x^{\natural}}=L_{x_0-\vec x}$. The two adjoints coincide, and are both $L_{x_0}$, exactly when $\tilde x$ is real, the scalar line being the centre.

**Example 3 (the matrix model).** In the matrix model of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions*, above this article in this category, the operator $L_{\tilde x}$ is left multiplication by the matrix $S=\mathsf{M}_2(\tilde x)$. The quaternion pairing is the Hermitian pairing $\tfrac12\operatorname{Tr}(S^{\dagger}T)$, and its adjoint is left multiplication by $S^{\dagger}=\mathsf{M}_2(\tilde x^{\natural})$, the **conjugate transpose**. The plain pairing is the bilinear pairing $\tfrac12\operatorname{Tr}(ST)$, and its adjoint is the **transpose** of *Association and the Transpose on the Quaternion Algebra*, $L_{\tilde x}^{\sim}=R_{\tilde x}$, which is right multiplication by $S$. The two names separate in the four real coordinates of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$ of Quaternions*, above this article in this category: there the plain adjoint has matrix $D\mathsf{M}_4(\tilde x)^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$, the matrix transpose conjugated by the signature matrix, whereas the quaternion adjoint carries the plain transpose, $\mathsf{M}_4(\tilde x^{\natural})=\mathsf{M}_4(\tilde x)^{\mathsf T}$. This is the matrix form of the two rules and the reason the quaternion one is named the conjugate transpose.

## Identity Relations

The two rules are the statements that the adjoint of a one-sided multiplication returns the parameter to its own side:
$$
\langle L_{\tilde x}\tilde y,\tilde z\rangle_B=\langle\tilde y,R_{\tilde x}\tilde z\rangle_B , \qquad
\langle L_{\tilde x}\tilde y,\tilde z\rangle_N=\langle\tilde y,L_{\tilde x^{\natural}}\tilde z\rangle_N ,
$$
and the transposition relations of the two-sided operators follow by composing them, the adjoint of the sandwich $\tilde y\mapsto\tilde x\tilde y\tilde z$ swapping the two parameters and conjugating both in the quaternion case. The conjugation preserves the quaternion pairing, $N(\tilde y^{\natural},\tilde z^{\natural})=\overline{N(\tilde y,\tilde z)}=N(\tilde y,\tilde z)$, the pairing being real valued.

## Summary

The plain product has the adjoint rule $L_{\tilde x}^{\dagger}=R_{\tilde x}$ and $R_{\tilde x}^{\dagger}=L_{\tilde x}$ for the plain pairing, the transpose in the matrix model; the quaternionic product has $L_{\tilde x}^{\dagger}=L_{\tilde x^{\natural}}$ and $R_{\tilde x}^{\dagger}=R_{\tilde x^{\natural}}$ for the quaternion pairing, the conjugate transpose in the matrix model. Both rules say that passing to the adjoint conjugates the parameter and keeps it on its own side, the plain pairing conjugating nothing and the quaternion pairing conjugating on its first slot.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{\tilde x}$, $R_{\tilde x}$ | left and right multiplication by $\tilde x$ |
| $\dagger$ | the adjoint with respect to a named pairing |
| $L_{\tilde x}^{\dagger}=R_{\tilde x}$ | the plain adjoint rule |
| $L_{\tilde x}^{\dagger}=L_{\tilde x^{\natural}}$ | the quaternion adjoint rule |
| transpose, conjugate transpose | the two rules in the matrix model |

## Further Reading

- *Association and the Transpose on the Quaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-quaternion-algebra.md`), above this article in this category.
- *Two-Sided Operators on the General Quaternionic Algebra of Quaternions* (`articles_maths/two-sided-operators-on-the-general-quaternionic-algebra-of-quaternioid.md`), above this article in this category.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), above this article in this category.
- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the complex rung.
