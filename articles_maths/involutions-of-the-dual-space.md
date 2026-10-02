# __Involutions of the Dual Space__

## Introduction

An involution of a linear space carries over to the dual space by transposition, and the article is about that carried involution: the map $T^{*} : V^{*} \to V^{*}$ defined by $T^{*}\varphi = \varphi \circ T$, its order, its type, the identification of its fixed and negated parts as annihilators of the negated and fixed parts of $T$, its matrix in the dual basis, and the way it interacts with the double dual and with the transpose of a linear map. It is the dual counterpart of the involution of the space, and it is the first of the induced involutions of the `*`-theory group.

*Involutive Linear Spaces* introduces the linear involution, the decomposition $V = V_+ \oplus V_-$, the type $(p,q)$, the trace $p-q$ and the determinant $(-1)^{q}$, and it records, among the induced involutions, that the dual map is an involution of the same type; the detailed study of the dual involution is the business of this article, and none of the general theory is repeated. *The Transpose of a Linear Map* establishes the transposition of a linear map, its contravariance, the annihilator description of kernel and image, and the double dual; those results are cited and used. The pairing-based adjoint of an endomorphism, which identifies $V$ with $V^{*}$ at the cost of a pairing, is *The Adjoint of an Endomorphism*, and the two dualities are related in *The Involution on the Dual Operator*.

Throughout, $F$ is a field, $V$ is a finite-dimensional $F$-linear space, $T$ is a linear involution of $V$ — a linear map with $T^2 = \mathrm{id}_V$ — of type $(p,q)$, so that $V = V_+ \oplus V_-$ with $V_+ = \ker(T-\mathrm{id})$ of dimension $p$ and $V_- = \ker(T+\mathrm{id})$ of dimension $q$, and $T^{*} : V^{*} \to V^{*}$ is the transposed map of *The Transpose of a Linear Map*. No form is used; a pairing occurs only as the evaluation of a functional on a vector.

## The Transposed Involution

**Definition.** The **transposed involution** of $T$ is the map $T^{*} : V^{*} \to V^{*}$ with $T^{*}\varphi = \varphi \circ T$, that is, $(T^{*}\varphi)(v) = \varphi(Tv)$.

**Proposition.** $T^{*}$ is linear, it is an involution of $V^{*}$, and it has the same type as $T$:

$$
(T^{*})^2 = \mathrm{id}_{V^{*}}, \qquad \text{type}(T^{*}) = (p,q) .
$$

Moreover the fixed part of $T^{*}$ is the annihilator of the negated part of $T$, and conversely,

$$
(V^{*})_+ = (V_-)^{0}, \qquad (V^{*})_- = (V_+)^{0} .
$$

**Proof.** Linearity is the linearity of the composite $\varphi T$ in $\varphi$. By the composition law of the transpose, $(T^2)^{*} = (T^{*})^2$, and $T^2 = \mathrm{id}$ gives $(T^{*})^2 = \mathrm{id}$. For the fixed part, $T^{*}\varphi = \varphi$ means $\varphi(Tv) = \varphi(v)$ for all $v$; on $V_-$ this reads $\varphi(-v) = \varphi(v)$, that is $\varphi(v) = 0$, and on $V_+$ it reads $\varphi(v) = \varphi(v)$; hence $\varphi$ is fixed exactly when it vanishes on $V_-$, which is the definition of $(V_-)^{0}$. The annihilator of $V_-$ has dimension $\dim_F V - q = p$ by *The Transpose of a Linear Map*, which is the dimension of the fixed part of an involution of type $(p,q)$; the negated part is obtained in the same way.

**Corollary (the fixed dimensions are exchanged).** $\dim_F (V^{*})_+ = p$ and $\dim_F (V^{*})_- = q$, so the trace and the determinant agree,

$$
\operatorname{tr}T^{*} = p - q = \operatorname{tr}T , \qquad \det T^{*} = (-1)^{q} = \det T .
$$

**Proof.** The dimensions are those of the annihilators, computed in the proposition; the trace is the difference of the two dimensions of the type, and the determinant the sign $(-1)^{q}$.

**Example.** For $n=2$ and $T$ of type $(1,1)$, say $T = \operatorname{diag}(1,-1)$ in a basis $e_1,e_2$ with dual basis $\varphi^{1},\varphi^{2}$, the transposed involution is $\operatorname{diag}(1,-1)$ in the dual basis: $T^{*}\varphi^{1} = \varphi^{1}$ because $\varphi^{1}(Te_1) = 1$ and $\varphi^{1}(Te_2) = 0$, and $T^{*}\varphi^{2} = -\varphi^{2}$. Its fixed part is spanned by $\varphi^{1}$, and $(V_-)^{0}$ is spanned by $\varphi^{1}$, as it must be.

## The Matrix in the Dual Basis

Fix a basis $\mathcal{B} = (v_1,\dots,v_n)$ of $V$ in which $T$ is diagonal, $Tv_i = \varepsilon_i v_i$ with $\varepsilon_i = 1$ for $i \le p$ and $\varepsilon_i = -1$ for $i > p$, and let $\mathcal{B}^{*} = (\varphi^{1},\dots,\varphi^{n})$ be the dual basis, $\varphi^{i}(v_j) = \delta^{i}_{j}$.

**Proposition.** $T^{*}\varphi^{i} = \varepsilon_i\varphi^{i}$, so the matrix of $T^{*}$ in the dual basis is $\operatorname{diag}(\varepsilon_1,\dots,\varepsilon_n)$, the transpose of the matrix of $T$; in an arbitrary basis the matrix of $T^{*}$ in the dual basis is the transpose of the matrix of $T$, as *The Transpose of a Linear Map* records.

**Proof.** $(T^{*}\varphi^{i})(v_j) = \varphi^{i}(Tv_j) = \varepsilon_j\delta^{i}_{j} = \varepsilon_i\delta^{i}_{j} = (\varepsilon_i\varphi^{i})(v_j)$ for every $j$; the maps agree on a basis, hence are equal.

**Remark (the dual basis is adapted, not chosen twice).** The basis diagonalising $T$ also diagonalises $T^{*}$, and the eigenvalues are the same because the two maps have the same matrix entries read in different pairs of indices. This is the matrix reason that the type is preserved, and it shows that no new computation is needed for the dual: the transposition exchanges the two eigenvalues of a non-symmetric situation only when the order of the terms is read in the other direction.

## Stable Subspaces and Quotients

**Definition.** A subspace $U \subseteq V$ is **stable** under $T$ when $T(U) \subseteq U$, equivalently when $T(U) = U$, since $T$ is a bijection.

**Proposition (the annihilator of a stable subspace is stable).** If $U$ is stable under $T$, then $U^{0} \subseteq V^{*}$ is stable under $T^{*}$, and the induced involution on the dual of the quotient $V/U$ is identified through the canonical isomorphism $(V/U)^{*} \cong U^{0}$ with the restriction of $T^{*}$ to $U^{0}$.

**Proof.** If $\varphi$ vanishes on $U$ and $u \in U$ then $(T^{*}\varphi)(u) = \varphi(Tu)$ vanishes because $Tu \in U$; hence $T^{*}(U^{0}) \subseteq U^{0}$, and the inclusion is an equality because $T^{*}$ is invertible. The canonical identification $(V/U)^{*} \cong U^{0}$ carries a functional on the quotient to its composite with $V \to V/U$, and the transposition commutes with the quotient map, so the induced involution on $(V/U)^{*}$ is the restriction.

**Corollary.** If $U = V_+$ or $U = V_-$, then the annihilator is the negated or the fixed part of $V^{*}$, and the involution induced on the dual of the complementary quotient has the type read from the other side.

**Proof.** For $U = V_+$ the annihilator is $(V^{*})_-$; for $U = V_-$ it is $(V^{*})_+$. The quotient $V/V_+ \cong V_-$ has dual of dimension $q$, on which $T^{*}$ acts as $-\mathrm{id}$, and the statement follows.

## The Double Dual

**Proposition.** The evaluation map $\mathrm{ev} : V \to V^{**}$ intertwines $T$ and $T^{**}$, that is $T^{**}\,\mathrm{ev} = \mathrm{ev}\,T$; under the identification $V \cong V^{**}$ the double transpose of $T$ is $T$, and the fixed and negated parts of $T^{**}$ are the images under $\mathrm{ev}$ of $V_+$ and $V_-$.

**Proof.** The intertwining is the naturality of the double transpose in *The Transpose of a Linear Map*; the type statement follows because $\mathrm{ev}$ is an isomorphism carrying the decomposition of $V$ to that of $V^{**}$.

**Remark (the involution of the dual is intrinsic).** The description of $(V^{*})_+$ and $(V^{*})_-$ as annihilators uses only $T$ and the evaluation pairing $(v,\varphi) \mapsto \varphi(v)$; no basis and no bilinear pairing on $V$ enters. The dual involution is therefore an invariant of the pair $(V,T)$, and the same construction applies to $V^{**}$ to give back $T$.

## Summary

For a linear involution $T$ of a finite-dimensional space $V$ of type $(p,q)$, the transposed map $T^{*} : V^{*} \to V^{*}$, $T^{*}\varphi = \varphi T$, is a linear involution of the dual of the same type $(p,q)$; its fixed vectors are exactly the functionals vanishing on the negated part $V_-$, and its negated vectors are the functionals vanishing on the fixed part $V_+$, so that $(V^{*})_+ = (V_-)^{0}$ and $(V^{*})_- = (V_+)^{0}$. Its trace and determinant agree with those of $T$. In a basis diagonalising $T$ the transposed involution is diagonalised by the dual basis with the same eigenvalues, and in general its matrix in the dual basis is the transpose of the matrix of $T$. The annihilator of a stable subspace is stable, and the involution induced on the dual of a quotient is the restriction to the annihilator under the canonical identification. The double transpose is $T$ under the evaluation isomorphism, which intertwines the two involutions, and the construction uses no form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the field of scalars |
| $V$ | an $F$-linear space of finite dimension $n$ |
| $V^{*} = \operatorname{Hom}_F(V,F)$ | the dual space |
| $T$ | a linear involution of $V$, $T^2=\mathrm{id}_V$ |
| $(p,q)$ | the type of $T$: $p=\dim V_+$, $q=\dim V_-$ |
| $V_+ = \ker(T-\mathrm{id})$, $V_- = \ker(T+\mathrm{id})$ | fixed and negated parts of $V$ |
| $T^{*} : V^{*}\to V^{*}$, $T^{*}\varphi=\varphi T$ | the transposed involution |
| $(V^{*})_+ = (V_-)^{0}$, $(V^{*})_- = (V_+)^{0}$ | fixed and negated parts of the dual |
| $U^{0}$ | the annihilator of a subspace $U$ |
| $\varphi^{i}$, $\delta^{i}_{j}$ | the dual basis and the Kronecker symbol |
| $\mathrm{ev} : V\to V^{**}$ | the evaluation map |
| $T^{**}$ | the double transpose, equal to $T$ under $\mathrm{ev}$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for duality, the transpose and the double dual.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for dual bases and the transpose of an operator.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (Prentice Hall, 2nd ed. 1971), for annihilators, the dual basis and the rank of the transpose.
- Nathan Jacobson, *Lectures in Abstract Algebra*, volume II: *Linear Algebra* (Van Nostrand, 1953), for involutions of vector spaces and the induced maps on the dual.
- Serge Lang, *Linear Algebra* (Springer, 3rd ed. 1987), for the duality of finite-dimensional spaces and its naturality.
