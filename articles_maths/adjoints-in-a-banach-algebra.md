
# __Adjoints in a Banach Algebra__

## Introduction

An involution of a Banach algebra is an **adjoint** operation on the elements: it is additive, it reverses the product, it is conjugate-linear and it has order two, and it is the algebra-side analogue of the Hilbert-space adjoint. The elements it fixes are the **self-adjoint** ones, the elements it negates are the **skew** ones, and the elements it inverts on the product are the **unitary** ones; these three classes carry the elementary calculus that the whole `- * Theory` block uses — the adjoint of a product, of an inverse, of a power, of an exponential, of a commutator — and they turn the unit group into the unitary group of the involution. This article gathers the adjoint operation on a Banach algebra and its elementary calculus, the self-adjoint, skew, unitary and normal elements, and the structural statement that the adjoint is an anti-automorphism of the algebra and an isomorphism onto the opposite algebra.

The article assumes the involutive Banach algebra, the $\mathrm{C}^*$-identity, the isometry of the involution, the Gelfand–Naimark theorem and the contractivity of the $*$-homomorphisms from *Involutive Banach Algebras and the Gelfand–Naimark Theorem*; the self-adjoint elements, the positive cone and the order from *Hermitian and Self-Adjoint Elements of a Banach Algebra*; the spectrum, the spectral radius and the functional calculus from *The Spectrum of a Self-Adjoint Element* and *The Functional Calculus of a Self-Adjoint Element*; the abstract involution, the opposite algebra and the unitary elements from *Involutive Linear Algebras* and *Unitary Elements of an Involutive Algebra*; and the operator adjoint from *Operator Algebras*. The grade involution $\alpha$ of the signed block is not used.

Throughout, $A$ is a unital Banach algebra over $\mathbb{C}$ with an involution $a \mapsto a^*$, continuous when a norm statement is made and isometric in the $\mathrm{C}^*$-case; $A^+ = \{a : a^* = a\}$, $A^- = \{a : a^* = -a\}$; an element is **unitary** when $u^*u = uu^* = 1$, **normal** when $a^*a = aa^*$, and **involutive** when $a^2 = 1$ and $a^* = a$; $U(A)$ is the **unitary group** of the involution; and the **opposite algebra** is $A^{\mathrm{op}}$ with the reversed product.

## The Adjoint Operation

**Definition.** The **adjoint** of the involutive Banach algebra $(A,\cdot\,{}^*)$ is the map $a \mapsto a^*$; it is an anti-automorphism of the algebra of order two and a topological isomorphism of $A$ onto $A^{\mathrm{op}}$ when it is continuous.

**Proposition (the calculus of the adjoint).** For all $a,b \in A$,

$$
(ab)^* = b^*a^* , \qquad (a + b)^* = a^* + b^* , \qquad (\lambda a)^* = \bar\lambda a^* , \qquad a^{**} = a ,
$$

and, for $a$ invertible, $(a^{-1})^* = (a^*)^{-1}$, so the adjoint preserves invertibility and $\sigma(a^*) = \overline{\sigma(a)}$. For every integer $n$, $(a^n)^* = (a^*)^n$, and if $a$ is invertible the identity extends to all integers; the adjoint commutes with the exponential, $(e^{a})^* = e^{a^*}$, when the involution is continuous.

**Proof.** The first four identities are the definition of the involution; $(a^{-1})^*(a^*) = (a a^{-1})^* = 1$ and $(a^*)(a^{-1})^* = 1$ give the inverse formula; the power formula is induction on the anti-multiplicativity; the exponential is the norm-convergent series, and a continuous conjugate-linear map commutes with its limits, giving $(e^a)^* = \sum a^{*n}/n! = e^{a^*}$. $\square$

**Theorem (the adjoint exhibits the opposite algebra).** The adjoint is an order-two anti-automorphism of $A$; it is an algebra isomorphism $A \to A^{\mathrm{op}}$ with $a \mapsto a^*$, and it is the certificate that $A$ is isomorphic to its opposite algebra. In particular the involution provides an isomorphism of $A$ with $A^{\mathrm{op}}$ exactly when it is defined, and no algebra carries two essentially different such certificates beyond the automorphisms of $A$.

**Proof.** The anti-multiplicativity is the isomorphism onto the opposite algebra, and the order two is $a^{**} = a$; the converse uniqueness is the standard statement that two isomorphisms onto the opposite algebra differ by an automorphism. $\square$

## Self-Adjoint, Skew and Unitary Elements

**Proposition (the three classes).** The self-adjoint elements satisfy $a^* = a$, the skew elements $a^* = -a$, and $A = A^+ \oplus iA^+$ with $A^- = iA^+$; an element is unitary exactly when $u^* = u^{-1}$, the unitary elements form a subgroup $U(A)$ of the unit group, and the adjoint is an isometry of $U(A)$. If $a$ is skew and the involution is continuous then $e^{a}$ is unitary in the $\mathrm{C}^*$-case, $\lVert e^{a}\rVert = 1$; in a $\mathrm{C}^*$-algebra the unitary group is the exponential image of the skew elements.

**Proof.** $(e^a)^* = e^{a^*} = e^{-a} = (e^a)^{-1}$ for skew $a$, so $e^a$ is unitary, and $\lVert e^a\rVert = 1$ when the algebra is a $\mathrm{C}^*$-algebra because $e^a$ is unitary; the decomposition is *Hermitian and Self-Adjoint Elements of a Banach Algebra*, and the group law is $(uv)^* = v^*u^* = v^{-1}u^{-1} = (uv)^{-1}$. $\square$

**Corollary (normal, positive, involutive).** An element is normal when $a^*a = aa^*$, equivalently when $h = \operatorname{Re}a$ and $k = \operatorname{Im}a$ commute; the positive elements are the self-adjoint $a$ with $a \geq 0$; a self-adjoint $a$ is involutive exactly when $a^2 = 1$, equivalently when $\sigma(a) \subseteq \{-1,1\}$. The Cayley transform $a \mapsto (a-i)(a+i)^{-1}$ sends the self-adjoint elements into the unitary ones.

**Proof.** Normality is the commutation of the real and imaginary parts; the spectrum statement is the spectral mapping theorem for $a \mapsto a^2$; the Cayley transform is the functional calculus applied to the unitary function $(\lambda-i)(\lambda+i)^{-1}$ of modulus one on the real line. $\square$

## Examples

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with the conjugate transpose the adjoint is the transpose-conjugate, the self-adjoint elements are the Hermitian matrices, the skew ones the skew-Hermitian matrices, the unitary ones the unitary group $U(n)$, and the Cayley transform is the standard map from the Hermitian matrices onto the unitary group with the identity removed.

**Example (the function algebra).** For $A = C(X,\mathbb{C})$ the adjoint is $f \mapsto \bar f$, the self-adjoint elements are the real-valued functions, the unitary ones the functions of modulus one, and $e^a$ for a skew $a$ is $e^{i\,\mathrm{Im}\,a}$, a unimodular function.

**Example (the group algebra).** For the group algebra of a finite group with the involution $u_g^* = u_{g^{-1}}$, the adjoint extends the group inversion; the unitaries include the group elements, the self-adjoint elements are the symmetric elements $\sum a_g u_g$ with $a_{g^{-1}} = \overline{a_g}$, and the group is the unitary group of its own algebra.

## The Unitary Group and the Gelfand Transform

**Theorem (the unitary group).** The unitary elements $U(A)$ form a subgroup of the unit group, closed under the adjoint, and inversion is the adjoint; for the norm topology $U(A)$ is a topological group, and in a $\mathrm{C}^*$-algebra it is closed and bounded, hence compact when $A$ is finite-dimensional. The exponential sends the skew part into $U(A)$, and in a $\mathrm{C}^*$-algebra the unitary group is the image of the skew part.

**Proof.** Closure under products and inverses is the calculus of the adjoint, $(uv)^* = v^*u^* = v^{-1}u^{-1} = (uv)^{-1}$; the adjoint is continuous for an isometric involution, so $U(A)$ is a topological group; in a $\mathrm{C}^*$-algebra the unitaries have norm one and form a closed subset of the unit sphere, compact in finite dimension. The exponential statement is the proposition of this article. $\square$

**Proposition (the adjoint and the Gelfand transform).** In a commutative unital $\mathrm{C}^*$-algebra the adjoint corresponds to complex conjugation of the Gelfand transform,

$$
\widehat{a^*} = \overline{\hat a} ,
$$

so the self-adjoint elements are the elements with real-valued transforms, the positive elements those with non-negative transforms and the unitary elements those with unimodular transforms; the Gelfand transform is a `*`-isomorphism onto $C(\operatorname{Max}(A))$ and carries the adjoint calculus to pointwise conjugation.

**Proof.** A character satisfies $\chi(a^*) = \overline{\chi(a)}$ by the reality of the self-adjoint elements under the transform, equivalently by the commutative Gelfand–Naimark theorem of *Involutive Banach Algebras and the Gelfand–Naimark Theorem*; the identification of the three classes is then pointwise. $\square$

## Summary

The adjoint of an involutive Banach algebra is the involution $a \mapsto a^*$, an anti-automorphism of order two and a topological isomorphism onto the opposite algebra; its elementary calculus is $(ab)^* = b^*a^*$, $(a^{-1})^* = (a^*)^{-1}$, $(a^n)^* = (a^*)^n$, $(e^a)^* = e^{a^*}$, and it moves the spectrum by conjugation, $\sigma(a^*) = \overline{\sigma(a)}$. The fixed points are the self-adjoint elements $A^+$, the negated ones the skew elements $A^- = iA^+$, and the elements with $u^* = u^{-1}$ are the unitary ones, forming the unitary group; a skew element exponentiates to a unitary one, and in a $\mathrm{C}^*$-algebra the unitary group is the exponential image of the skew part. An element is normal exactly when its real and imaginary parts commute, the positive elements carry the order of *Hermitian and Self-Adjoint Elements of a Banach Algebra*, and the Cayley transform sends the self-adjoint elements into the unitary ones. The involutions of the operator algebra are *The Involution on the Operator Algebra*, and the spectral theory is *The Spectrum of a Self-Adjoint Element*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a \mapsto a^*$ | The adjoint (involution), an anti-automorphism of order two |
| $A^+$, $A^-$ | Self-adjoint and skew elements, $A = A^+\oplus iA^+$ |
| $u^* = u^{-1}$, $U(A)$ | Unitary elements and the unitary group |
| $(ab)^* = b^*a^*$, $(a^{-1})^* = (a^*)^{-1}$ | The calculus of the adjoint |
| $(e^a)^* = e^{a^*}$ | Adjoint commutes with the exponential |
| $\sigma(a^*) = \overline{\sigma(a)}$ | The adjoint moves the spectrum |
| Normal, positive, involutive | $a^*a = aa^*$; $a \geq 0$; $a^2 = 1$, $a^* = a$ |
| Cayley transform | Self-adjoint into unitary |
| $\widehat{a^*} = \overline{\hat a}$ | The adjoint is conjugation of the Gelfand transform |

## Further Reading

- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the involutions of Banach algebras and the unitary elements.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the adjoint operation and the elementary calculus.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the adjoint of the operators and the unitary group.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the involutions, the self-adjoint and skew elements and the opposite algebra.
- Gérard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for the unitary group and the exponential of the skew elements.
