
# __The Signed Left Multiplication on a Complex Vector Space__

## Introduction

The one-sided companion of the signed sandwich is the **signed left multiplication** on the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$,
$$
\Lambda^{\alpha}_{a} = L_a\circ\alpha, \qquad \Lambda^{\alpha}_{a}(X) = a\,\alpha(X),
$$
obtained by taking the right factor of the signed sandwich $\Theta^{\alpha}_{a,b}(X) = a\alpha(X)b$ to be the identity. It is the composite of the ordinary left multiplication with the grade involution, so it is the case $b = 1$ of the signed sandwich, its products are ordinary left multiplications, its inverse is again signed, and its fixed elements are the solutions of $a\alpha(X) = X$. When the grade involution comes from a **unitary self-adjoint involution** $T$ of a Hermitian space $V$ and the element $a$ is unitary, the signed left multiplication is an isometry of the Hermitian trace form of $E$, so that the one-sided signed operators of the geometry are the isometric ones; the unsigned left multiplication is the case of the trivial involution, and the difference between the two is the sign carried by $\alpha$.

The article has three sections: the signed left multiplication and its laws; the fixed elements and their computation through the involution; and the relation to the unsigned left multiplication, with the isometries. The unsigned and signed sandwiches are *The Signed Sandwich on a Complex Vector Space*, the previous articles of this group; the endomorphism algebra and its trace are *Algebras of Endomorphisms*; the fixed part of an involution and its dimension are *Involutive Linear Spaces*; the unitary group and the involution are *The Unitary and Symplectic Groups* and *Hermitian Geometry and the Unitary Group*. The unsigned case with its adjoint is *The Adjoint of the Left Multiplication on a Complex Vector Space*, the signed adjoint is *The Signed Adjoint of the Left Multiplication on a Complex Vector Space*, and the module-level variant is *The Graded Action on a Module over a Complex Vector Space*, all of this group. The group-level analogue is *The Signed Left Multiplication on a Symmetry Group*.

Throughout, $V$ is a finite-dimensional complex vector space of dimension $n$ with a positive-definite Hermitian form $h$, $E = \operatorname{End}_{\mathbb C}(V)$, $A^{\dagger}$ is the adjoint for $h$, $T$ is a unitary self-adjoint involution of $V$, $\alpha(X) = TXT$ is the grade involution it defines, $L_a(X) = aX$ and $R_b(X) = Xb$ are the one-sided multiplications, $\Lambda^{\alpha}_{a} = L_a\circ\alpha$ is the signed left multiplication, and $\langle X, Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the Hermitian trace form of $E$.

## The Signed Left Multiplication and Its Laws

**Definition.** For $a \in E$ the **signed left multiplication** is
$$
\Lambda^{\alpha}_{a} = L_a\circ\alpha, \qquad \Lambda^{\alpha}_{a}(X) = a\,\alpha(X) .
$$

**Proposition (the two factorisations).** $\Lambda^{\alpha}_{a}$ is the signed sandwich with right factor the identity, $\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,1}$, and
$$
\Lambda^{\alpha}_{a} = L_a\circ\alpha = \alpha\circ L_{\alpha(a)} ,
$$
so the signed left multiplication is the ordinary left multiplication by $\alpha(a)$ conjugated by $\alpha$.

**Proof.** The first identity is the definition of the sandwich with $b = 1$; for the second, $\alpha L_{\alpha(a)}(X) = \alpha(\alpha(a)X) = a\alpha(X) = \Lambda^{\alpha}_{a}(X)$.

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

**Proof.** Invertibility follows from the factorisation $\Lambda^{\alpha}_{a} = L_a\alpha$ and the invertibility of $\alpha$; the inverse is checked by the composition law: $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{\alpha(a^{-1})} = L_{a\alpha(\alpha(a^{-1}))} = L_{aa^{-1}} = \mathrm{id}$, and likewise on the other side.

## The Fixed Elements and the Involution

**Proposition (fixed elements).** The fixed space of $\Lambda^{\alpha}_{a}$ is
$$
\ker(\Lambda^{\alpha}_{a} - \mathrm{id}) = \{X \in E : a\alpha(X) = X\} ;
$$
equivalently, when $a$ is invertible, $X$ is fixed exactly when $\alpha(X) = a^{-1}X$. For $a = 1$ the fixed space is the fixed part $E^{+}$ of $\alpha$, and in a basis of $V$ in which $T$ is diagonal with $p$ entries $+1$ and $q$ entries $-1$, $p+q = n$, its dimension is
$$
\dim E^{+} = p^{2} + q^{2}.
$$

**Proof.** The first display is the eigenvalue-one equation. For $a = 1$ it is $\alpha(X) = X$, whose solution space is $E^{+}$; the dimension is the computation for a diagonal involution: the matrix-unit $E_{ij}$ is fixed exactly when the two signs agree, $(-1)^{i+j} = 1$, which happens for the $p^2$ units with both indices in the $+1$ block and the $q^2$ units with both indices in the $-1$ block. This is *Involutive Linear Spaces*.

**Proposition (the fixed space of a reflection's involution).** If $T = r$ is a unitary reflection of type $(n-1,1)$, with the $-1$ eigenspace spanned by $u$, then the fixed part $E^{+}$ of $\alpha_r$ has dimension $(n-1)^2 + 1$: it consists of the endomorphisms $X$ with $X = rXr$, that is those that preserve the decomposition $V = u^{\perp}\oplus\mathbb{C}u$, act on the hyperplane $u^{\perp}$ by an arbitrary endomorphism and on the line $\mathbb{C}u$ by a scalar.

**Proof.** With $p = n-1$ and $q = 1$ the dimension formula gives $(n-1)^2 + 1$; the description is the block form in the orthogonal decomposition $V = u^{\perp}\oplus\mathbb{C}u$, in which $T = \operatorname{diag}(1,\dots,1,-1)$ and $X = rXr$ means that $X$ is block diagonal for this decomposition with an arbitrary top block and a scalar bottom block.

**Example (matrix units as eigenvectors).** For $T = \operatorname{diag}(1,-1)$ on $\mathbb{C}^2$ and $a = \operatorname{diag}(\lambda, \mu)$ with $\lambda\mu \neq 0$, the signed left multiplication on the two-by-two matrices is $X \mapsto a\,TXT$, and the matrix units $E_{ij}$ are eigenvectors with eigenvalue $a_{ii}(-1)^{i+j}$; the fixed space is spanned by $E_{11}$ and $E_{22}$ and has dimension $2 = 1^2+1^2$, and the off-diagonal units are eigenvectors with eigenvalues $-\lambda$ and $-\mu$.

## The Relation to the Unsigned Left Multiplication and the Isometries

**Proposition (the unsigned case).** The signed left multiplication with $\alpha = \mathrm{id}$ is the ordinary left multiplication, $\Lambda^{\mathrm{id}}_{a} = L_a$, and for the general $\alpha$ the two families are exchanged by the involution,
$$
\Lambda^{\alpha}_{a} = L_a\circ\alpha, \qquad L_{\alpha(a)} = \Lambda^{\alpha}_{a}\circ\alpha ,
$$
the first the definition and the second its consequence $\Lambda^{\alpha}_{a}\alpha = L_a\alpha\alpha = L_a$; the signed family is the ordinary family twisted by $\alpha$, exactly as the signed sandwich is the unsigned sandwich twisted by $\alpha$.

**Proof.** The first identity is the definition; composing it on the right with $\alpha$ and using $\alpha^2 = \mathrm{id}$ gives $\Lambda^{\alpha}_{a}\alpha = L_a$, which after replacing $a$ by $\alpha(a)$ is the second. Setting $\alpha = \mathrm{id}$ returns $L_a$ in both.

**Proposition (the unitary case is isometric).** Let $a = u$ be unitary and let $T$ be unitary and self-adjoint. Then $\Lambda^{\alpha}_{u}$ preserves the Hermitian trace form,
$$
\bigl\langle \Lambda^{\alpha}_{u}(X),\, \Lambda^{\alpha}_{u}(Y)\bigr\rangle = \langle X, Y\rangle ,
$$
and $\Lambda^{\alpha}_{u}$ is invertible with $(\Lambda^{\alpha}_{u})^{-1} = \Lambda^{\alpha}_{\alpha(u^{-1})} = \Lambda^{\alpha}_{u^{\dagger}}$.

**Proof.** $\langle \Lambda_u(X),\Lambda_u(Y)\rangle = \operatorname{tr}((u\alpha(X))^{\dagger}u\alpha(Y)) = \operatorname{tr}(\alpha(X)^{\dagger}u^{\dagger}u\alpha(Y)) = \operatorname{tr}(\alpha(X)^{\dagger}\alpha(Y)) = \operatorname{tr}(\alpha(X^{\dagger}Y)) = \operatorname{tr}(X^{\dagger}Y) = \langle X,Y\rangle$, using $u^{\dagger} = u^{-1}$, $\alpha(Z)^{\dagger} = \alpha(Z^{\dagger})$ (from the unitarity and self-adjointness of $T$) and $\operatorname{tr}(\alpha(Z)) = \operatorname{tr}(TZT) = \operatorname{tr}(Z)$. The inverse is the corollary of the first section, together with $u^{-1} = u^{\dagger}$.

**Remark (the fixed elements in the geometric reading).** The fixed space of $\Lambda^{\alpha}_{a}$ is the set of endomorphisms that $\alpha$ carries to a fixed multiple of $a^{-1}$; for $a = 1$ it is the fixed part $E^{+}$ of the involution, of dimension $p^2+q^2$, and for a reflection's involution of type $(n-1,1)$ it has dimension $(n-1)^2+1$. The signed left multiplication by a unitary is an isometry of the trace form, and its fixed space is nontrivial exactly when the unitary element has an eigenvalue-one direction compatible with the involution, which is the geometric content of the eigenvalue-one equation.

## Summary

On the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ of a complex vector space the signed left multiplication is $\Lambda^{\alpha}_{a} = L_a\circ\alpha$, the signed sandwich with right factor one, equal to $\alpha\circ L_{\alpha(a)}$. Its product with another is the ordinary left multiplication $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b} = L_{a\alpha(b)}$; it satisfies $L_a\Lambda^{\alpha}_{b} = \Lambda^{\alpha}_{ab}$ and $\Lambda^{\alpha}_{a}L_b = R_{\alpha(b)}\Lambda^{\alpha}_{a}$, so the signed and ordinary left multiplications together form a closed monoid; it is invertible exactly for invertible $a$, with inverse $\Lambda^{\alpha}_{\alpha(a^{-1})}$; and its fixed space is the solution set of $a\alpha(X) = X$, equal to the fixed part $E^{+}$ of $\alpha$ when $a = 1$, of dimension $p^2+q^2$ for an involution with $p$ signs $+1$ and $q$ signs $-1$, and of dimension $(n-1)^2+1$ for a reflection's involution. When $T$ is unitary and self-adjoint and $a = u$ is unitary, the signed left multiplication is an isometry of the Hermitian trace form $\langle X,Y\rangle = \operatorname{tr}(X^\dagger Y)$. The unsigned case with its adjoint, the signed adjoint and the module-level graded variant are the companion articles of this group; the abstract laws and the involutive-subspace theory are *The Signed Sandwich on a Complex Vector Space* and *Involutive Linear Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E=\operatorname{End}_{\mathbb C}(V)$, $\alpha(X)=TXT$ | the endomorphism algebra and the grade involution |
| $L_a(X)=aX$, $R_b(X)=Xb$ | the one-sided multiplications |
| $\Lambda^{\alpha}_{a}=L_a\circ\alpha$ | the signed left multiplication |
| $\Lambda^{\alpha}_{a}=L_a\alpha=\alpha L_{\alpha(a)}$ | the two factorisations |
| $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b}=L_{a\alpha(b)}$ | the composition law |
| $(\Lambda^{\alpha}_{a})^{-1}=\Lambda^{\alpha}_{\alpha(a^{-1})}$ | the inverse |
| $\dim E^{+}=p^2+q^2$ | the dimension of the fixed part of an involution |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for one-sided operators on an algebra and the involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for signed one-sided operators.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the left and right multiplications and their products.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the adjoint, the unitary operators and the fixed spaces of involutions.
