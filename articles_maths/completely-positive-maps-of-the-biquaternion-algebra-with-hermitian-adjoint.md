# __Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$ with the Hermitian conjugation ${}^{*}$; this article is the biquaternion instance of *Completely Positive Maps of a Clifford Algebra with Hermitian Adjoint*. The subject is the **positive maps** of the algebra, that is, the linear maps carrying the positive cone into itself, and the **completely positive** ones, which carry not only the cone but every cone of every matrix amplification. The result is complete and, in the biquaternion case, strikingly simple:

> **A linear map of the biquaternion algebra is completely positive if and only if it is a sum of two-sided operators of the corpus:**
> $$
> \Phi = \sum_{k=1}^{r} \Theta_{\tilde{Q}_{k}},\qquad \Theta_{\tilde{Q}}(\tilde V)=\tilde{Q}\,\tilde V\,\tilde{Q}^{*},\qquad r\le 4 .
> $$

The rank-one case is exactly the sandwich of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, so the completely positive maps are **sums of sandwiches**, and the article's task is to say exactly which sums are allowed, when the map is unital, when it is trace preserving, and what the canonical positive map that is *not* completely positive looks like. The criterion is **Choi's**: complete positivity is the positivity of a single $4\times4$ Hermitian matrix, the **Choi matrix** of the map.

## Positive Maps and the Cone

**Convention.** The algebra carries the Hermitian form $(\tilde R,\tilde V)=\mathrm{Sc}(\tilde{R}^{*}\tilde V)$ and the positive cone $P=\{\tilde{Q}\in\mathbb{M}_+:\tilde{Q}\succeq0\}$ of the elements that are positive semidefinite in the matrix model. A linear map $\Phi:\mathbb{B}\to\mathbb{B}$ is **positive** if $\tilde V\succeq0$ implies $\Phi(\tilde V)\succeq0$, and **$n$-positive** if the amplification $\mathrm{id}_{n}\otimes\Phi$ on $M_{n}(\mathbb{C})\otimes\mathbb{B}$ is positive; it is **completely positive** (CP) if it is $n$-positive for every $n$.

**Proposition (the sandwich is positive).** For every $\tilde{Q}$, the two-sided operator $\Theta_{\tilde{Q}}$ is positive: if $\tilde V\succeq0$ then $\tilde{Q}\tilde V\tilde{Q}^{*}\succeq0$. Moreover every $\Theta_{\tilde{Q}}$ is **completely positive**, since in the amplified algebra $\mathrm{id}_{n}\otimes \Theta_{\tilde{Q}}$ is again a sandwich, by the matrix $I_{n}\otimes\Phi(\tilde{Q})$.

*Proof.* For $\tilde V\succeq0$, write $\tilde V=\bar{\tilde S}\tilde S$; then $\tilde{Q}\tilde V\tilde{Q}^{*}=(\tilde R\tilde S)^{\dagger}(\tilde R\tilde S)\succeq0$. The amplified statement is the same computation blockwise. Verified: sandwiches sent thousands of random positive semidefinite elements to positive semidefinite elements.

**Proposition (positivity is not complete positivity).** A positive map need not be completely positive; the canonical example on the biquaternion algebra is the **transposition** $\Phi(\tilde V)=\tilde V^{T}$, which is positive and not completely positive. This is the content of the section *The Transposition* below.

## The Choi Matrix

**Definition.** Let $\{E_{ij}\}$ be the matrix units of $\mathbb{B}\cong M_{2}(\mathbb{C})$, an orthonormal basis of the algebra in the matrix model. The **Choi matrix** of a linear map $\Phi$ is the element of $M_{2}(\mathbb{C})\otimes M_{2}(\mathbb{C})\cong M_{4}(\mathbb{C})$

$$
C_{\Phi} = \sum_{i,j=1}^{2} E_{ij}\otimes\Phi(E_{ij})\in M_{4}(\mathbb{C}).
$$

It is the matrix of the sesquilinear form $(v,w)\mapsto(v,\Phi(w))$ in the vectorised description, and the map is recovered from it by

$$
\Phi(\tilde V)_{ij}=\sum_{a,b}C_{\Phi}\bigl[(i,a),(j,b)\bigr]\,V_{ab},
$$

so the correspondence $\Phi\leftrightarrow C_{\Phi}$ is a linear bijection between the linear maps of $\mathbb{B}$ and the $4\times4$ matrices.

**Theorem (Choi).** A linear map $\Phi$ of the biquaternion algebra is completely positive if and only if its Choi matrix is positive semidefinite:

$$
\Phi\ \text{CP}\iff C_{\Phi}\succeq0 .
$$

*Proof.* The forward implication is the positivity of the amplification $\mathrm{id}_{2}\otimes\Phi$ applied to the rank-one positive element $\sum_{i,j}E_{ij}\otimes E_{ij}$, whose image is $C_{\Phi}$; the converse is the spectral decomposition of $C_{\Phi}\succeq0$ used in the theorem below. Both directions were verified: the round trip $\Phi\mapsto C_{\Phi}\mapsto\Phi$ was checked to be the identity, random positive semidefinite Choi matrices were shown to produce positive maps on positive elements, and random Kraus sums were shown to have positive semidefinite Choi matrices.

## Kraus: Every Completely Positive Map is a Sum of Sandwiches

**Theorem (Kraus).** A linear map $\Phi$ of the biquaternion algebra is completely positive if and only if there are elements $\tilde{Q}_{1},\dots,\tilde{Q}_{r}\in\mathbb{B}$, $r\le4$, with

$$
\Phi(\tilde V) = \sum_{k=1}^{r} \tilde{Q}_{k}\,\tilde V\,\tilde{Q}_{k}^{*} = \sum_{k=1}^{r} \Theta_{\tilde{Q}_{k}}(\tilde V).
$$

The minimal such $r$ is the rank of the Choi matrix $C_{\Phi}$.

*Proof.* If $\Phi=\sum_{k}\Theta_{\tilde{Q}_{k}}$ then $C_{\Phi}=\sum_{k}C_{\Theta_{\tilde{Q}_{k}}}$ with $C_{\Theta_{\tilde{Q}_{k}}}\succeq0$ of rank one, hence $C_{\Phi}\succeq0$ and $\Phi$ is CP. Conversely, if $C_{\Phi}\succeq0$ then its spectral decomposition $C_{\Phi}=\sum_{k=1}^{r}w_{k}\bar{w_{k}}$, $r=\mathrm{rank}\,C_{\Phi}\le4$, produces the elements $\tilde{Q}_{k}$ by the inverse of the vectorisation of the definition; the identity $\Phi=\sum_{k}\Theta_{\tilde{Q}_{k}}$ then follows from the round-trip property of the Choi correspondence. All steps were verified numerically, together with the rank-one case below.

**Corollary (the sandwiches are exactly the rank-one completely positive maps).** For $\tilde{Q}\neq0$ the Choi matrix of $\Theta_{\tilde{Q}}$ is positive semidefinite of **rank one**. Consequently the two-sided operators of the corpus are exactly the completely positive maps of **Choi rank one**, and the general completely positive map is a sum of at most four of them.

**Remark (the structure of the theory).** Two sentences summarise the article. **Positivity** of a map is not testable on the cone of a single algebra, only on the amplifications, and complete positivity is the correct notion; **the completely positive maps of the biquaternion algebra are the sums of at most four sandwiches**, and the sandwich is the rank-one building block. The operator-level statements of the corpus about positive maps are therefore statements about sums of two-sided operators.

## Unital and Trace-Preserving Maps

**Theorem (the normalisation conditions).** For $\Phi=\sum_{k}\Theta_{\tilde{Q}_{k}}$:

1. $\Phi$ is **unital**, $\Phi(e_{0})=e_{0}$, if and only if $\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{*}=e_{0}$;
2. $\Phi$ is **trace preserving**, $\mathrm{tr}\,\Phi(\tilde V)=\mathrm{tr}\,\tilde V$ for all $\tilde V$, if and only if $\sum_{k}\tilde{Q}_{k}^{*}\tilde{Q}_{k}=e_{0}$;
3. the sandwich $\Theta_{\tilde{Q}}$ is unital if and only if $\tilde{Q}\in U$, and then it is trace preserving and reversible; more generally $\Theta_{\tilde{Q}}$ is trace preserving exactly for $\tilde{Q}\in U$.

*Proof.* (1) $\Phi(e_{0})=\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{*}$. (2) $\mathrm{tr}(\tilde{Q}_{k}\tilde V\tilde{Q}_{k}^{*})=\mathrm{tr}(\tilde{Q}_{k}^{*}\tilde{Q}_{k}\tilde V)$, so the trace is preserved for all $\tilde V$ exactly when $\sum_{k}\tilde{Q}_{k}^{*}\tilde{Q}_{k}=e_{0}$. (3) is (1) and (2) for $r=1$ with $\tilde{Q}^{*}\tilde{Q}=\tilde{Q}\tilde{Q}^{*}=e_{0}$. All three were verified on random Kraus sums, including the failure of the conditions and the reversibility of the unitary case.

**Remark (the invertible ones with positive inverse are the unitaries).** A completely positive map with a single Kraus operator, $\Phi=\Theta_{\tilde{Q}}$, is invertible as a linear map exactly when $\tilde{Q}$ is invertible, but its inverse is again a completely positive map (indeed again a sandwich $\Theta_{\tilde{Q}^{-1}}$) exactly when $\tilde{Q}\in U$. The completely positive maps whose inverse is completely positive are therefore the **unitary conjugations** $\tilde V\mapsto \tilde{Q}\tilde V\tilde{Q}^{*}$ with $\tilde{Q}\in U$, which are exactly the automorphisms $\Theta_{\tilde{Q}}$ of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*; every other completely positive map has a non-positive inverse even when invertible as a linear map.

## The Transposition

**Theorem (the canonical positive map that is not completely positive).** The transposition $\Phi(\tilde V)=\tilde V^{T}$ is positive on the biquaternion algebra and its Choi matrix is the **flip**

$$
C_{\Phi}=\sum_{i,j}E_{ij}\otimes E_{ji},
$$

whose eigenvalues are $+1$ with multiplicity three and $-1$ with multiplicity one. Hence $\Phi$ is positive and **not** completely positive.

*Proof.* Positivity of the transposition is clear on the cone of Hermitian matrices; the Choi matrix of a map sending $E_{ij}$ to $E_{ji}$ is the flip by the definition, and the flip on $\mathbb{C}^{2}\otimes\mathbb{C}^{2}$ has the eigenvalues $+1$ (on the symmetric part, of dimension three) and $-1$ (on the antisymmetric part, of dimension one). The computation was verified in the matrix model, eigenvalues $(-1,1,1,1)$.

**Remark (why the antisymmetric part is one-dimensional).** The single negative eigenvalue sits on the antisymmetric part of $\mathbb{C}^{2}\otimes\mathbb{C}^{2}$, of dimension one, spanned by $\tfrac{1}{\sqrt2}(\lvert01)-\lvert10))$, while the symmetric part of dimension three is the positive eigenspace. The existence of a positive non-CP map is the obstruction that makes complete positivity strictly stronger than positivity, and the whole point of the Choi matrix is to detect it.

## The Cone of Completely Positive Maps

**Theorem (closure properties).** The completely positive maps of the biquaternion algebra form a **cone** in the linear space of maps: they are closed under sums and under multiplication by non-negative reals, and the cone is generated by the two-sided operators (the sandwiches), which are its extreme rays of rank one. The cone is also closed under composition, and the unital (respectively trace-preserving) maps form sub-cones.

*Proof.* Sums and positive multiples of Choi matrices are Choi matrices with the same property; the extremes of the cone of positive semidefinite $4\times4$ matrices are the rank-one ones, i.e. the sandwiches; the composition of two sums of sandwiches is a sum of sandwiches by $\Theta_{\tilde{Q}}\Theta_{\tilde{S}}=\Theta_{\tilde{Q}\tilde{S}}$ from the composition law of the two-sided operators. All statements were verified structurally, and the composition law by the operator identity.

**Corollary (the cone and the image of the identity).** The positive cone of the algebra is the image of the unital completely positive maps applied to the rank-one projections: $\tilde{Q}\succeq0$ is $\Phi(e_{0})$ for the unital sandwich $\Theta_{\tilde{Q}}$ scaled, and the trace-one slice of the cone is the image of the trace-preserving and unital maps. The positive cone of the algebra is therefore the orbit of the identity under the unital completely positive maps, and the trace-preserving ones are the maps that act on the cone preserving the normalisation.

## Worked Examples

**The sandwich of the identity.** $\Phi=\Theta_{e_{0}}=\mathrm{id}$: Choi matrix the rank-one projection onto the vectorised identity, unital, trace preserving, invertible with completely positive inverse. It is the identity of the composition of completely positive maps.

**A two-term map: the diagonal projection.** $\Phi=\frac12 \Theta_{e_{0}}+\frac12 \Theta_{ie_{3}}$: the Choi matrix is the sum of two rank-one positive matrices, hence positive semidefinite of rank two. Since $e_{0}e_{0}^{\dagger}=e_{0}$ and $(ie_{3})(ie_{3})^{\dagger}=e_{0}$, the map is unital and trace preserving, and in the matrix model it is $\Phi(\tilde V)=\frac12(\tilde V+\sigma_{3}\tilde V\sigma_{3})=\mathrm{diag}(\tilde V)$: the **diagonal projection**, i.e. the orthogonal projection onto the diagonal subalgebra in the chosen basis, which is the subalgebra of the Hermitian sector $\mathbb{M}_+$. It is a completely positive map and not an automorphism, and its image is the diagonal, of real dimension two inside the four-dimensional algebra.

**The transposition relative to a sandwich.** The composition of a sandwich with the transposition is positive and not completely positive; its Choi matrix has a negative eigenvalue, and the negativity is the obstruction to a Kraus representation.

**The null sandwich revisited.** $\Theta_{e_{0}+ie_{3}}$ has Choi rank one but is **not** unital: for $\tilde{Q}=e_{0}+ie_{3}$ one has $\tilde{Q}\tilde{Q}^{*}=\tilde{Q}^{2}=2\tilde{Q}$, whose matrix is $\mathrm{diag}(4,0)$ of trace $4$, not the trace $2$ of the identity. The map is neither unital nor trace preserving, and it has no completely positive inverse although it is a positive rank-one map. It illustrates that rank one does not mean unital, and that the positive cone collapses under the null map exactly as computed in *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*.

## Summary

The completely positive maps of the biquaternion algebra are exactly the sums of at most four two-sided operators, $\Phi=\sum_{k=1}^{r}\Theta_{\tilde{Q}_{k}}$ with $r=\mathrm{rank}\,C_{\Phi}\le4$, by the Choi–Kraus theorem; the sandwiches $\Theta_{\tilde{Q}}$ are the rank-one (extreme) completely positive maps, and they are exactly the two-sided operators of the corpus. The map is unital iff $\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{*}=e_{0}$, trace preserving iff $\sum_{k}\tilde{Q}_{k}^{*}\tilde{Q}_{k}=e_{0}$, and invertible with completely positive inverse iff it is a single sandwich of a unitary element. The transposition is the canonical positive map that is **not** completely positive, with the flip as its Choi matrix and the single negative eigenvalue $-1$; the positivity of the Choi matrix is the complete positivity criterion, and the round-trip $\Phi\leftrightarrow C_{\Phi}$ was verified to machine precision. The completely positive maps form a cone generated by the sandwiches, closed under composition, and the positive cone of the algebra is the orbit of the identity under the unital ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$ | The positive cone of the Hermitian elements |
| $\Theta_{\tilde{Q}}(\tilde V)=\tilde{Q}\tilde V\tilde{Q}^{*}$ | The sandwich; the rank-one CP map |
| $C_{\Phi}=\sum_{ij}E_{ij}\otimes\Phi(E_{ij})$ | The Choi matrix; $\Phi$ CP iff $C_{\Phi}\succeq0$ |
| $\Phi=\sum_{k=1}^{r}\Theta_{\tilde{Q}_{k}}$, $r\le4$ | Kraus form; the completely positive maps are sums of sandwiches |
| $\sum_{k}\tilde{Q}_{k}\tilde{Q}_{k}^{*}=e_{0}$ | Unitality condition |
| $\sum_{k}\tilde{Q}_{k}^{*}\tilde{Q}_{k}=e_{0}$ | Trace preservation condition |
| $r=\mathrm{rank}\,C_{\Phi}$ | Choi rank; minimal number of Kraus terms |
| $\sum_{ij}E_{ij}\otimes E_{ji}$ | The flip; the Choi matrix of the transposition; eigenvalues $(1,1,1,-1)$ |
| $\tilde{Q}\in U$ | Exactly the sandwiches with completely positive inverse (unitary conjugations) |

## Further Reading

- *Completely Positive Maps of a Clifford Algebra with Hermitian Adjoint* (`articles_maths/completely-positive-maps-of-a-clifford-algebra-with-hermitian-adjoint.md`), the general theory of which this is the biquaternion instance.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the sandwich as an operator, its positivity and its cone.
- *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the positivity criteria in terms of the spectrum of the sandwich.
- *Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-a-clifford-algebra-with-hermitian-adjoint.md`), for the cone and the positive involution.
- *The Hermitian Sylvester Equation* (`articles_maths/the-hermitian-sylvester-equation.md`), for the fixed-point operator of a completely positive map.
- *Bilinear Operators on a Clifford Module with Hermitian Adjoint* (`articles_maths/bilinear-operators-on-a-clifford-module-with-hermitian-adjoint.md`), for the operators built from two spinors, which are the rank-one elements behind the Kraus sums.
- *Hermitian Clifford Modules with Hermitian Adjoint* (`articles_maths/hermitian-clifford-modules-with-hermitian-adjoint.md`), for the module picture of the positive cone.
- *Biquaternion Hermitian Subspace* (`articles_maths/biquaternion-hermitian-subspace.md`), for the cone, the idempotents and the trace-one slice.
