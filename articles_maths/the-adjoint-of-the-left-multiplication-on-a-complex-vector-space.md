
# __The Adjoint of the Left Multiplication on a Complex Vector Space__

## Introduction

On the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ of a complex vector space the left multiplication
$$
L_A(X) = AX
$$
is an operator on $E$, and the category's form on $E$ is the **Hermitian trace form** $\langle X, Y\rangle = \operatorname{tr}(X^{\dagger}Y)$, where $X^{\dagger}$ is the adjoint of $X$ for the Hermitian form $h$ of $V$. The **adjoint** of the left multiplication for this form is again a left multiplication, by the adjoint element,
$$
L_A^{*} = L_{A^{\dagger}},
$$
because $\langle AX, Y\rangle = \operatorname{tr}((AX)^{\dagger}Y) = \operatorname{tr}(X^{\dagger}A^{\dagger}Y) = \langle X, A^{\dagger}Y\rangle$; and the same computation gives $R_B^{*} = R_{B^{\dagger}}$ for the right multiplication, so the adjoint of a two-sided multiplication is the two-sided multiplication by the adjoints, $\Phi_{a,b}^{*} = \Phi_{a^{\dagger},b^{\dagger}}$. The explicit formula makes the geometry of the one-sided operators transparent: $L_A$ is self-adjoint exactly when $A$ is Hermitian, normal exactly when $A$ is normal, unitary exactly when $A$ is unitary, and its spectrum is the spectrum of $A$; and the adjoint is compatible with the grade involution, in the sense that the involution carries the adjoint of $L_A$ to the adjoint of $L_{\alpha(A)}$.

The article has three sections: the adjoint of the one-sided and two-sided multiplications; the compatibility of the adjoint with the grade involution; and the self-adjointness, normality and unitarity of the left multiplication. The one-sided and two-sided operators, their algebra and the trace form are *The Left and Right Multiplication Operators on a Complex Vector Space*, and the signed case is *The Signed Adjoint of the Left Multiplication on a Complex Vector Space*, both of this Part; the endomorphism algebra and its trace are *Algebras of Endomorphisms*; the adjoint of a Hermitian operator is *The Adjoint of a Hermitian Operator*, the first article of this group; the Hermitian forms, the unitary group and the spectral theorem are *Hermitian Geometry and the Unitary Group* and *Self-Adjoint Operators and the Spectral Theorem*. None of that is re-derived.

Throughout, $V$ is a finite-dimensional complex vector space with a positive-definite Hermitian form $h$, $E = \operatorname{End}_{\mathbb C}(V)$, $A^{\dagger}$ is the $h$-adjoint, $L_A(X) = AX$, $R_B(X) = XB$, $\Phi_{a,b} = L_aR_b$, $\alpha(X) = TXT$ is the grade involution of a unitary self-adjoint involution $T$, and $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the Hermitian trace form of $E$.

## The Adjoints of the One-Sided and Two-Sided Multiplications

**Proposition (the adjoints).** For all $A, B \in E$,
$$
L_A^{*} = L_{A^{\dagger}}, \qquad R_B^{*} = R_{B^{\dagger}}, \qquad \Phi_{a,b}^{*} = \Phi_{a^{\dagger},b^{\dagger}},
$$
and the assignment is compatible with the composition and the involution of $E$: $(L_AL_B)^{*} = L_{B^{\dagger}}L_{A^{\dagger}}$.

**Proof.** $\langle L_AX, Y\rangle = \operatorname{tr}((AX)^{\dagger}Y) = \operatorname{tr}(X^{\dagger}A^{\dagger}Y) = \langle X, L_{A^{\dagger}}Y\rangle$, using the involution property $(AX)^{\dagger} = X^{\dagger}A^{\dagger}$ and the trace; the right multiplication is the same computation on the other side, $\langle XB, Y\rangle = \operatorname{tr}((XB)^{\dagger}Y) = \operatorname{tr}(B^{\dagger}X^{\dagger}Y) = \langle X, YB^{\dagger}\rangle$ with the trace cyclicity $\operatorname{tr}(B^{\dagger}X^{\dagger}Y) = \operatorname{tr}(X^{\dagger}YB^{\dagger})$; the two-sided case is the composite. The trace form and the involution are *The Left and Right Multiplication Operators on a Complex Vector Space* and *Algebras of Endomorphisms*.

**Corollary (the adjoint of the inner automorphism).** The inner automorphism $\mathrm{Ad}_A = L_AR_{A^{-1}}$ has adjoint $\mathrm{Ad}_A^{*} = \mathrm{Ad}_{A^{\dagger}}$, and $\mathrm{Ad}_A$ is unitary for the trace form exactly when $A$ is unitary, in which case $\mathrm{Ad}_A^{*} = \mathrm{Ad}_A^{-1}$.

**Proof.** $\mathrm{Ad}_A^{*} = (L_AR_{A^{-1}})^{*} = R_{A^{-1}}^{*}L_A^{*} = R_{(A^{-1})^{\dagger}}L_{A^{\dagger}} = R_{(A^{\dagger})^{-1}}L_{A^{\dagger}} = \mathrm{Ad}_{A^{\dagger}}$; the unitarity of $\mathrm{Ad}_A$ is the unitarity of $A$, and then the adjoint is the inverse. The inner automorphisms are *Inner Automorphisms of a Ring* and *Algebras of Endomorphisms*.

## The Compatibility with the Grade Involution

**Proposition (the involution preserves the adjoint).** If $T$ is unitary and self-adjoint, so that $\alpha(X) = TXT$ satisfies $\alpha(X^{\dagger}) = \alpha(X)^{\dagger}$, then
$$
\alpha\,L_A^{*}\,\alpha = L_{\alpha(A)}^{*},
$$
and similarly for the right multiplication; the grade involution carries the adjoint of the left multiplication by $A$ to the adjoint of the left multiplication by $\alpha(A)$.

**Proof.** $\alpha L_B\alpha = L_{\alpha(B)}$, since $\alpha L_B\alpha(X) = \alpha(B\alpha(X)) = \alpha(B)X$; applied to $B = A^{\dagger}$ this gives $\alpha L_A^{*}\alpha = L_{\alpha(A^{\dagger})} = L_{\alpha(A)^{\dagger}} = L_{\alpha(A)}^{*}$, using $\alpha(A^{\dagger}) = \alpha(A)^{\dagger}$, which is the unitarity and self-adjointness of $T$. The involution and its properties are *The Involution on a Complex Vector Space* and *The Signed Adjoint of the Left Multiplication on a Complex Vector Space*.

**Proposition (the adjoint of the sandwich).** The unsigned sandwich $\Phi_{a,b}$ has adjoint $\Phi_{a,b}^{*} = \Phi_{a^{\dagger},b^{\dagger}}$, and its self-adjointness is the pair of conditions $a = a^{\dagger}$ and $b = b^{\dagger}$ up to the commutant; the signed sandwich is the next article.

**Proof.** The adjoint is the composite of the adjoints of the two one-sided factors; $\Phi_{a,b} = L_aR_b$ gives $\Phi_{a,b}^{*} = R_{b^{\dagger}}L_{a^{\dagger}} = \Phi_{a^{\dagger},b^{\dagger}}$ since the two commute; self-adjointness requires $a = a^{\dagger}$ and $b = b^{\dagger}$ when the factors are independent, and the degenerate solutions are the elements of the commutant. This is *The Signed Adjoint Sandwich on a Complex Vector Space*.

## Self-Adjointness, Normality and Unitarity

**Proposition (the operator properties of $L_A$).** The left multiplication $L_A$ is self-adjoint exactly when $A$ is Hermitian, normal exactly when $A$ is normal, and unitary exactly when $A$ is unitary; its spectrum is $\operatorname{Spec}(A)$, and its eigenvectors are the elements $X$ with $AX = \lambda X$.

**Proof.** $L_A^{*} = L_{A^{\dagger}}$, so $L_A^{*} = L_A$ exactly when $A^{\dagger} = A$; normality is $L_A^{*}L_A = L_{A^{\dagger}A} = L_{AA^{\dagger}} = L_AL_A^{*}$, which is $A^{\dagger}A = AA^{\dagger}$; unitarity is $L_A^{*}L_A = L_{A^{\dagger}A} = \mathrm{id}_E$, which is $A^{\dagger}A = \mathrm{id}$. The eigenvalue equation $L_AX = \lambda X$ is $AX = \lambda X$, and the spectrum of the left multiplication is that of $A$. The spectral statements are *Self-Adjoint Operators and the Spectral Theorem*, and the trace form is *The Left and Right Multiplication Operators on a Complex Vector Space*.

**Proposition (the isometries of the trace form).** $L_A$ is an isometry of $\langle\cdot,\cdot\rangle$ exactly when $A$ is unitary; the unitary group of $V$ acts on $E$ by the left multiplications, and the map $A\mapsto L_A$ is a faithful unitary representation of $U(h)$ on $E$, whose adjoint is $A\mapsto A^{\dagger}$.

**Proof.** $\langle L_AX, L_AY\rangle = \operatorname{tr}((AX)^{\dagger}AY) = \operatorname{tr}(X^{\dagger}A^{\dagger}AY)$, which equals $\langle X,Y\rangle$ for all $X,Y$ exactly when $A^{\dagger}A = \mathrm{id}$, that is when $A$ is unitary; the map is multiplicative, injective (it recovers $A = L_A(\mathrm{id})$) and its adjoint is the involution. The unitary representations are *Unitary Representations of a Lie Group*.

**Example (the trace form and the left multiplication).** For $V = \mathbb{C}$ one has $E = \mathbb{C}$ and $L_A$ is multiplication by the complex number $A$ on $\mathbb{C}$ with the form $\langle X,Y\rangle = \bar XY$; the adjoint is multiplication by $\bar A$, the self-adjoint elements are the real numbers, and the unitaries are the phases. For $V = \mathbb{C}^m$ in a unitary frame the involution $X\mapsto X^{\dagger}$ is the conjugate transpose, the trace form is $\operatorname{tr}(X^{\dagger}Y) = \sum_{i,j}\bar X_{ij}Y_{ij}$, and $L_A$ has the matrix $\mathrm{diag}(A,A,\dots,A)$ in the column ordering of the matrix units, so its spectrum is the spectrum of $A$ repeated $m$ times.

## Summary

On the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ with the Hermitian trace form $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$, the adjoint of the left multiplication is $L_A^{*} = L_{A^{\dagger}}$, of the right multiplication $R_B^{*} = R_{B^{\dagger}}$, and of the two-sided multiplication $\Phi_{a,b}^{*} = \Phi_{a^{\dagger},b^{\dagger}}$; the inner automorphism has adjoint $\mathrm{Ad}_A^{*} = \mathrm{Ad}_{A^{\dagger}}$. The grade involution of a unitary self-adjoint involution preserves the adjoint, $\alpha(X^{\dagger}) = \alpha(X)^{\dagger}$, and carries $L_A^{*}$ to $L_{\alpha(A)}^{*}$; these formulas are the unsigned case of the adjoint theory of the signed operators. The left multiplication is self-adjoint, normal or unitary exactly when $A$ is, its spectrum is that of $A$, and $A\mapsto L_A$ is a faithful unitary representation of $U(h)$ on $E$. The one-sided operators and the trace form are *The Left and Right Multiplication Operators on a Complex Vector Space* and *Algebras of Endomorphisms*; the adjoint of a Hermitian operator is *The Adjoint of a Hermitian Operator*; the signed adjoints are *The Signed Adjoint Sandwich on a Complex Vector Space* and *The Signed Adjoint of the Left Multiplication on a Complex Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E=\operatorname{End}_{\mathbb C}(V)$ | the endomorphism algebra |
| $\langle X,Y\rangle=\operatorname{tr}(X^{\dagger}Y)$ | the Hermitian trace form |
| $L_A(X)=AX$, $R_B(X)=XB$ | the one-sided multiplications |
| $L_A^{*}=L_{A^{\dagger}}$ | the adjoint of the left multiplication |
| $\Phi_{a,b}^{*}=\Phi_{a^{\dagger},b^{\dagger}}$ | the adjoint of the two-sided multiplication |
| $\alpha L_A^{*}\alpha=L_{\alpha(A)}^{*}$ | compatibility with the grade involution |
| $A\mapsto L_A$ | the faithful unitary representation of $U(h)$ |

## Further Reading

- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the adjoint, the trace form and the one-sided operators.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2012), for the trace form, the conjugate transpose and the left multiplication.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the left and right multiplications and their adjoints.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the unitary representations and the trace form.
