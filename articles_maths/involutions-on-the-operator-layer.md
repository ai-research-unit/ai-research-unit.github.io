
# __Involutions on the Operator Layer__

## Introduction

The operator layer of a group carries two operations that arise from the inversion: the **adjoint** with respect to the natural pairing, which reverses the order in a product and fixes the operators that preserve the pairing, and the **conjugation** by the inversion, which is an automorphism of the operator algebra and exchanges the left and right translations. This article fixes the natural pairing of the category, defines both operations, proves their elementary properties, and records how they differ. It is the first article of the `* Operator Theory` group of the category and fixes the marks and adjoint conventions that the six articles after it use: *The Group Inversion as an Adjoint*, *The Adjoint of the Left Multiplication on a Group*, *The Signed Adjoint Sandwich on a Group*, *The Signed Adjoint of the Reflection on a Group*, *The Signed Adjoint of the Left Multiplication on a Group* and *The Graded Adjoint Action on a Module over a Group*. The group algebra, the translations and the sandwich are used from *Group Algebras* and from the operator articles *Left and Right Multiplication in a Group* and *The Signed Sandwich on a Group*.

## The Operator Layer and the Natural Pairing

**Convention (the operator layer).** Let $k$ be a field and let $k[G]$ be the group algebra with basis $G$ and finitely supported elements. Write $\operatorname{End}_k(k[G])$ for the $k$-algebra of $k$-linear operators on it, with composition and unit $\mathrm{id}$, and write $L_a,R_b$ for the left and right translations $x\mapsto ax$, $x\mapsto xb$ extended linearly from $G$.

**Definition (the natural pairing).** The **natural pairing** of the category is the bilinear form

$$
\langle\,\cdot\,,\,\cdot\,\rangle : k[G]\times k[G]\longrightarrow k,
\qquad
\Bigl\langle \sum_g x_g\,g,\ \sum_h y_h\,h\Bigr\rangle=\sum_g x_g\,y_g,
$$

so that $\langle g,h\rangle=\delta_{g,h}$ and the basis $G$ is orthonormal.

**Proposition (the pairing is symmetric, nondegenerate and inversion-invariant).** The natural pairing is symmetric and nondegenerate, and $\langle x,y\rangle$ is the coefficient of $e$ in $x\,\iota(y)$ and the coefficient of $e$ in $\iota(x)\,y$; in particular it is invariant under the inversion, $\langle\iota(x),\iota(y)\rangle=\langle x,y\rangle$.

**Proof.** Symmetry and nondegeneracy are immediate from the orthonormality of the basis: a nonzero $x$ has a nonzero coefficient $x_g$ and pairs nontrivially with $g$. For the coefficient form, $x\,\iota(y)=\sum_{g,h}x_g y_h\, gh^{-1}$, whose coefficient at $e$ is $\sum_g x_g y_g$. The inversion statement is $\sum_g x_g y_g$ computed after reindexing both sums by the inversion.

**Definition (adjoint).** For $T\in\operatorname{End}_k(k[G])$ the **adjoint** $T^{*}$ is the operator with

$$
\langle Tx,\,y\rangle=\langle x,\,T^{*}y\rangle\qquad\text{for all } x,y\in k[G].
$$

Existence and uniqueness are the nondegeneracy of the pairing: in the basis $G$ the matrix of $T^{*}$ is the transpose of the matrix of $T$. For a group involution $\sigma$ with linear extension $\Sigma_{\sigma}\in\operatorname{End}_k(k[G])$, the **conjugation by the involution** is

$$
\mathrm{ad}_{\sigma}(T)=\Sigma_{\sigma}\,T\,\Sigma_{\sigma}^{-1}.
$$

## The Adjoint Operation

**Proposition (the adjoint is an involution of the operator algebra).** For all $S,T\in\operatorname{End}_k(k[G])$ and $\lambda\in k$: $\mathrm{id}^{*}=\mathrm{id}$; $(T^{*})^{*}=T$; $(T+\lambda S)^{*}=T^{*}+\lambda S^{*}$; $(\lambda T)^{*}=\lambda T^{*}$; and

$$
(ST)^{*}=T^{*}S^{*}.
$$

Consequently the adjoint is an **anti-involution** of $\operatorname{End}_k(k[G])$ of order two: it reverses the order of composition.

**Proof.** The first four are the transpose in a basis. For the product, $\langle STx,y\rangle=\langle Tx,S^{*}y\rangle=\langle x,T^{*}S^{*}y\rangle$ for all $x,y$, so $(ST)^{*}=T^{*}S^{*}$ by uniqueness of the adjoint. Applying the operation twice returns the transpose of the transpose, which is the original.

**Proposition (the adjoint of an inverse is the inverse of the adjoint).** If $T$ is invertible then $T^{*}$ is invertible and $(T^{-1})^{*}=(T^{*})^{-1}$.

**Proof.** From $(TT^{-1})^{*}=(T^{-1})^{*}T^{*}=\mathrm{id}$ and $(T^{-1}T)^{*}=T^{*}(T^{-1})^{*}=\mathrm{id}$, the operator $T^{*}$ has two-sided inverse $(T^{-1})^{*}$.

**Definition (self-adjoint, skew-adjoint, unitary).** An operator $T$ is **self-adjoint** if $T^{*}=T$, **skew-adjoint** if $T^{*}=-T$, and **unitary** if $T^{*}T=TT^{*}=\mathrm{id}$.

**Proposition (the elementary criteria).** $T$ is unitary if and only if $T$ is invertible with $T^{*}=T^{-1}$; $T$ is self-adjoint if and only if its matrix is symmetric in the basis $G$; $T$ is skew-adjoint if and only if its matrix is skew-symmetric. The identity is self-adjoint and unitary, and the self-adjoint operators and the skew-adjoint operators are the $+1$ and $-1$ eigenspaces of the adjoint.

**Proof.** The unitary criterion is the uniqueness of the inverse. In the orthonormal basis the adjoint is the transpose, so $T^{*}=T$ is symmetry of the matrix and $T^{*}=-T$ is skew-symmetry. The last statement is that the adjoint is an involution, so its fixed elements are the self-adjoint ones and its $(-1)$-eigenspace is the skew-adjoint ones.

## The Inversion on the Operator Layer

**Proposition (the adjoints of the translations).** $(L_a)^{*}=L_{a^{-1}}$ and $(R_b)^{*}=R_{b^{-1}}$. Hence $L_a$ is self-adjoint exactly when $a^{2}=e$, and $R_b$ is self-adjoint exactly when $b^{2}=e$; the left and right translations are unitary for every parameter.

**Proof.** In the basis $G$, $(L_a g)_h=\delta_{h,ag}$; the transpose has $(L_a^{*}h)_g=\delta_{h,ag}=\delta_{g,a^{-1}h}$, giving $L_a^{*}(h)=a^{-1}h$, that is $L_{a^{-1}}$. The same computation with $R_b$ gives $R_{b^{-1}}$. Self-adjointness is then $L_a=L_{a^{-1}}$, which is injectivity of $a\mapsto L_a$ and so $a=a^{-1}$, that is $a^{2}=e$; the same for $R_b$. Unitarity is $L_{a^{-1}}L_a=\mathrm{id}$, which is the composition law of the translations.

**Proposition (the inversion is self-adjoint).** The linear extension $\Sigma_{\iota}$ of the inversion is self-adjoint: $\Sigma_{\iota}^{*}=\Sigma_{\iota}$.

**Proof.** $\langle\Sigma_{\iota}x,y\rangle=\sum_g(\Sigma_{\iota}x)_g\,y_g=\sum_g x_{g^{-1}}y_g$, and $\langle x,\Sigma_{\iota}y\rangle=\sum_g x_g y_{g^{-1}}$; reindexing the first sum by $g\mapsto g^{-1}$ gives the second. So the two agree for all $x,y$. This is the operator-level form of the statement that the inversion is the antipode; the article *The Group Inversion as an Adjoint* develops the pairing between the inversion, the left multiplication and the coalgebra structure of $k[G]$.

**Proposition (the conjugation by the inversion).** $\mathrm{ad}_{\iota}$ is an automorphism of $\operatorname{End}_k(k[G])$ of order two; it respects the adjoint, $\mathrm{ad}_{\iota}(T^{*})=\mathrm{ad}_{\iota}(T)^{*}$; and it exchanges the translations,

$$
\mathrm{ad}_{\iota}(L_a)=R_{a^{-1}}, \qquad \mathrm{ad}_{\iota}(R_b)=L_{b^{-1}}.
$$

**Proof.** Conjugation by an invertible operator is an automorphism of the operator algebra, and $\Sigma_{\iota}^{2}=\mathrm{id}$ gives order two. Since $\Sigma_{\iota}$ is self-adjoint, $\mathrm{ad}_{\iota}(T)^{*}=(\Sigma_{\iota}T\Sigma_{\iota})^{*}=\Sigma_{\iota}^{*}T^{*}\Sigma_{\iota}^{*}=\Sigma_{\iota}T^{*}\Sigma_{\iota}=\mathrm{ad}_{\iota}(T^{*})$. For the translations, $\mathrm{ad}_{\iota}(L_a)(x)=\iota(a\,\iota(x))=x\,a^{-1}=R_{a^{-1}}(x)$.

**Remark (the two operations differ).** The adjoint and the conjugation by the inversion are different operators on the operator layer, and the translations show it: $(L_a)^{*}=L_{a^{-1}}$ while $\mathrm{ad}_{\iota}(L_a)=R_{a^{-1}}$. The two agree on $L_a$ exactly when $a$ is central. This is the operator-level instance of the rule of the general brief that the involution on the elements and the adjoint on the operators are two structures and not one; the agreement, when it holds, is proved and never assumed.

## Summary

The **operator layer** of the group is the algebra $\operatorname{End}_k(k[G])$ of linear operators on the group algebra. The **natural pairing** is $\langle x,y\rangle=\sum_g x_g y_g$, orthonormal on the basis $G$, symmetric and nondegenerate, and invariant under the inversion. The **adjoint** $T^{*}$ is defined by $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$; it is an anti-involution of the operator algebra, $(ST)^{*}=T^{*}S^{*}$ and $(T^{*})^{*}=T$, an invertible operator has invertible adjoint with $(T^{-1})^{*}=(T^{*})^{-1}$, and the self-adjoint, skew-adjoint and unitary operators are the familiar classes.

The inversion contributes two operations: the adjoint of the translations, $(L_a)^{*}=L_{a^{-1}}$ and $(R_b)^{*}=R_{b^{-1}}$, and the conjugation by the linear extension of the inversion, $\mathrm{ad}_{\iota}(T)=\Sigma_{\iota}T\Sigma_{\iota}$, which is an automorphism of order two of the operator algebra, respects the adjoint, and exchanges the translations, $\mathrm{ad}_{\iota}(L_a)=R_{a^{-1}}$ and $\mathrm{ad}_{\iota}(R_b)=L_{b^{-1}}$. The two operations differ, and they agree on a left translation exactly when its parameter is central. The conventions fixed here are used by the six articles of the `* Operator Theory` group that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle x,y\rangle=\sum_g x_g y_g$ | the natural pairing, orthonormal on $G$ |
| $\langle g,h\rangle=\delta_{g,h}$ | orthonormality of the basis |
| $T^{*}$, $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$ | the adjoint of an operator |
| $(ST)^{*}=T^{*}S^{*}$ | the adjoint reverses composition |
| $\Sigma_{\sigma}$ | linear extension of the group involution $\sigma$ |
| $\mathrm{ad}_{\sigma}(T)=\Sigma_{\sigma}T\Sigma_{\sigma}^{-1}$ | conjugation by the involution |
| $(L_a)^{*}=L_{a^{-1}}$, $\mathrm{ad}_{\iota}(L_a)=R_{a^{-1}}$ | the two operations differ |
| $T^{*}T=TT^{*}=\mathrm{id}$ | the unitary condition |

## Further Reading

- Marshall Hall, *The Theory of Groups* (Macmillan, 1959), for the group algebra, the regular representation and the inversion.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the group algebra, its antipode and its coalgebra structure.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the adjoint operation, the unitary group and the distinction between an involution and an adjoint.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, third edition, 2002), for bilinear forms, their adjoints and the unitary group of a form.
