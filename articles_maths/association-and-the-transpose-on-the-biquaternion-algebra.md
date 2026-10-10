
# __Association and the Transpose on the Biquaternion Algebra__

## Introduction

Every linear endomorphism of the biquaternion algebra carries an adjoint for each form the algebra possesses, and the corpus uses the two ends of the collection. The **dagger** is the adjoint with respect to the positive definite Hermitian form, and it is the involution of *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and of the Hilbert-algebra series. **Association** is the adjoint with respect to the indefinite general plain bilinear form

$$
\langle\tilde R,\tilde S\rangle=\mathrm{Sc}(\tilde R\tilde S)=\sum_\mu\varepsilon_\mu R_\mu S_\mu
$$

of *The Four Pairings of the Biquaternion Algebra*, and it is the involution that makes a linear function transposable in the sense the source literature uses.

Association is the transpose for the general plain bilinear form, and the two marks agree exactly on the operators that the source literature writes down. Off them the two differ, and the corpus keeps them apart: association is the transpose for the **indefinite** pairing built from the plain product, the dagger is the adjoint for the **positive definite** Hermitian pairing. This article owns the association construction itself, the algebra identities it satisfies on the Conway basis and on the regular operators, the matrix formula by which it is a transpose, its relation to the Hermitian adjoint, and the citation of the general theory of the transpose of a bilinear form.

The construction is a duality of the form and not enveloping algebra. The form is *The Four Pairings of the Biquaternion Algebra*, the Conway operator basis, the regular representations and the bi-module structure are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*, and the Hermitian adjoint is *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*.

## The Pairing That Association Uses

The form is used here, not developed. Its definition, its coefficient Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$, its determinant $\det D=-1$, its inertia $(1,3)$, its realified signature $(4,4)$ and its restriction to the remarkable subspaces are the matter of *The Four Pairings of the Biquaternion Algebra* and of *Remarkable Subspaces under the General Plain Algebra of Biquaternions*. The two facts this article needs are that the form is $\mathbb{C}$-bilinear, symmetric and non-degenerate, and that its Gram matrix in the coefficient basis is $D$; both are read from that article.

**Remark (association uses the plain product, not the norm).** The pairing here is the scalar part of the plain product, of Gram matrix $D$. The companion **general quaternionic bilinear form** $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu$ of *Biquaternion Norm and Invertibility* is the polarisation of the norm, of Gram matrix $\mathrm{I}_4$, and it gives a second transpose, different off the operators that fix the scalar unit and preserve the vector part. The distinction of $D$ and $\mathrm{I}_4$ is the whole of the difference, as *The Four Pairings of the Biquaternion Algebra* records.

## Association

**Definition.** The **associate** $F^{\approx}$ of a $\mathbb{C}$-linear map $F$ of $\mathbb{B}$ is the unique $\mathbb{C}$-linear map with

$$
\langle F(\tilde R),\tilde S\rangle=\langle\tilde R,F^{\approx}(\tilde S)\rangle\qquad\text{for all }\tilde R,\tilde S\in\mathbb{B}.
$$

The form is non-degenerate, so the associate exists and is unique; association is $\mathbb{C}$-linear in $F$, and it is an involution, $(F^{\approx})^{\approx}=F$.

**Proposition (the defining property is a scalar-part identity).** Because $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$, the definition reads

$$
\mathrm{Sc}\bigl(F(\tilde R)\,\tilde S\bigr)=\mathrm{Sc}\bigl(\tilde R\,F^{\approx}(\tilde S)\bigr)\qquad\text{for all }\tilde R,\tilde S\in\mathbb{B}.
$$

*Proof.* Substitute the definition of the form into both sides of the defining equation.

**Proposition (association reverses composition).** For two $\mathbb{C}$-linear maps $F,G$ of $\mathbb{B}$,

$$
(F\circ G)^{\approx}=G^{\approx}\circ F^{\approx}.
$$

*Proof.* For all $\tilde R,\tilde S$, $\langle FG\tilde R,\tilde S\rangle=\langle G\tilde R,F^{\approx}\tilde S\rangle=\langle\tilde R,G^{\approx}F^{\approx}\tilde S\rangle$, so $G^{\approx}F^{\approx}$ satisfies the defining property of $(FG)^{\approx}$, and the associate is unique. Verified numerically on random maps.

## Association on the Conway Basis

**Definition.** On the Conway operator basis $e_n[\,]e_m$ of *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Conway Operator Basis*, the elementary operator is $(e_n[\,]e_m)(\tilde R)=e_n\tilde R e_m$, the argument placed between the two units.

**Proposition (association reverses the factors).** On the Conway basis

$$
\bigl(e_n[\,]e_m\bigr)^{\approx}=e_m[\,]e_n,
\qquad\text{so}\qquad
\Bigl(\sum_{n,m}A_{nm}\,e_n[\,]e_m\Bigr)^{\approx}=\sum_{n,m}A_{nm}\,e_m[\,]e_n,
$$

and in particular $(a[\,]b)^{\approx}=b[\,]a$.

*Proof.* By the definition, $\langle(a[\,]b)\tilde R,\tilde S\rangle=\mathrm{Sc}(a\tilde Rb\tilde S)$. The scalar part is invariant under cyclic permutation, $\mathrm{Sc}(XYZ)=\mathrm{Sc}(YZX)=\mathrm{Sc}(ZXY)$, because $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$, so $\mathrm{Sc}(a\tilde Rb\tilde S)=\mathrm{Sc}(\tilde Rb\tilde Sa)=\langle\tilde R,(b[\,]a)\tilde S\rangle$. The identity is therefore satisfied by $b[\,]a$, and it is unique by non-degeneracy. Verified numerically on the sixteen Conway operators.

**Corollary (the regular operators transpose into one another).** The two regular representations are the edge rows of the Conway basis, $L_a=\sum_n a_n\,e_n[\,]e_0$ and $R_b=\sum_m b_m\,e_0[\,]e_m$, so

$$
L_a^{\approx}=R_a,\qquad R_b^{\approx}=L_b.
$$

*Proof.* Substitute $b=e_0$ in the proposition for the left multiplication and $a=e_0$ for the right multiplication, and use $e_n[\,]e_0$ and $e_0[\,]e_m$ for the two edge rows. Verified numerically on random parameters.

**Remark (the operator pair of the form).** The corollary is the first line of the operator theory of the plain form: association exchanges the two regular representations, so the transpose of a left multiplication is a right multiplication and conversely. The two articles that develop the consequence are *One-Sided Operators on the General Plain Algebra of Biquaternions*, which reads the type, form-preserving and commutant questions of the two families, and *Two-Sided Operators on the General Plain Algebra of Biquaternions*, which reads the products $L_aR_b$, their composition law, their swap adjoint, and the criteria on the product of the two parameters. This article keeps the calculus of the associate itself and does not duplicate them.

**Remark (association is the transpose for the indefinite form).** The roles are the ones of the general theory: the left multiplication by $a$, transposed against the form, is the right multiplication by $a$, and conversely. The dagger of the Hermitian form does the same on the operators, but for the definite pairing, and the two coincide on the operators of the next section.

## The Matrix Formula

**Proposition (the matrix of association).** Let $F$ have matrix $M$ in the coefficient basis $e_0,e_1,e_2,e_3$, so that the coordinates of $F(\tilde R)$ are $M$ applied to the coordinates of $\tilde R$. Then the matrix of the associate is

$$
M^{\approx}=D\,M^{\mathsf T}D,
$$

for $M^{\mathsf T}$ the plain transpose.

*Proof.* Write the form as $\langle\tilde P,\tilde Q\rangle=P^{\mathsf T}DQ$ on the coordinate columns. Then $\langle F\tilde R,\tilde S\rangle=(M R)^{\mathsf T}DQ=R^{\mathsf T}M^{\mathsf T}DQ$ and $\langle\tilde R,F^{\approx}\tilde S\rangle=R^{\mathsf T}D M^{\approx}S$ for all $R,S$, so $M^{\mathsf T}D=D M^{\approx}$, that is $M^{\approx}=D M^{\mathsf T}D$ because $D^{-1}=D$. Verified numerically on random maps, together with the defining identity $\langle F\tilde R,\tilde S\rangle=\langle\tilde R,F^{\approx}\tilde S\rangle$.

**Remark (when association is the plain transpose).** The associate equals the plain transpose exactly when $D M^{\mathsf T}D=M^{\mathsf T}$, that is when $M^{\mathsf T}$ commutes with $D$. The operators that fix the scalar unit $e_0$ and preserve the vector part have the block form $\operatorname{diag}(1,N)$ with $N$ a $3\times3$ matrix; for them $D\operatorname{diag}(1,N)^{\mathsf T}D=\operatorname{diag}(1,N^{\mathsf T})$, because the conjugation by $D$ acts as the sign $-1$ on the two off-diagonal blocks and as the identity on the two diagonal blocks, so the conjugation is invisible and association is the plain transpose. For a general map the two differ.

**Remark (the pairing of the coefficients).** The entries of the matrix $D$ are the pairings $\langle e_i,e_j\rangle=\varepsilon_i\delta_{ij}$ of the coefficient basis, so the formula $D M^{\mathsf T}D$ is the coordinate form of the general statement that the transpose of a bilinear form is taken with the Gram matrix conjugating both sides. The realified algebra carries the matrix $\operatorname{diag}(D,-D)$, whose reading is in *The Realification of the Four Forms*.

## Association and the Hermitian Adjoint

**Proposition (coefficient conjugation).** Let $\bar F$ be the map obtained from $F$ by conjugating every coefficient, and let $F^{*}$ be the adjoint of $F$ with respect to the positive definite Hermitian form $(\tilde R,\tilde S)=\mathrm{Sc}(\tilde R^{*}\tilde S)=\sum_\mu R_{\bar\mu}S_\mu$ of *Biquaternion Norm and Invertibility*, so that $(F\tilde R,\tilde S)=(\tilde R,F^{*}\tilde S)$. Then

$$
\bar F^{\approx}=D\,F^{*}D.
$$

*Proof.* Conjugating the coefficients of $F$ conjugates the entries of its matrix, taking $M$ to $\bar M$, so the matrix of $\bar F^{\approx}$ is $D\bar M^{\mathsf T}D=D\overline{M^{\mathsf T}}D$. The adjoint $F^{*}$ with respect to the Hermitian form has matrix $M^{\dagger}=\overline{M^{\mathsf T}}$, the conjugate transpose: the form $(\tilde R,\tilde S)=\sum_\mu R_{\bar\mu}S_\mu$ is the standard Hermitian pairing conjugate-linear in the first argument, and its adjoint is the conjugate transpose. Hence $D F^{*}D=D\overline{M^{\mathsf T}}D$, which is the matrix of $\bar F^{\approx}$. Verified numerically on random maps.

**Corollary (the collapse on the vector-preserving operators).** On the operators that fix the scalar unit $e_0$ and preserve the vector part — among them the unitary group elements of *Biquaternion Lie Group and Exponential Structure* that the source uses — the matrix has no entries mixing the scalar slot with the vector slots, the conjugation by $D$ is invisible as in the previous section, and the identity collapses to

$$
\bar F^{\approx}=F^{*}=F^{-1}\qquad\text{for unitary }F,
$$

which is the source's relation $G^{-1}=G^{+\approx}=G^{\dagger}$.

*Proof.* For a block matrix $\operatorname{diag}(1,N)$ the conjugate transpose is $\operatorname{diag}(1,N^{\dagger})$ and the conjugation by $D$ leaves it unchanged, so $\bar F^{\approx}=F^{*}$; and for a unitary $F$ the adjoint is the inverse. Verified numerically on the unitary elements and on the block-preserving operators.

**Remark (why the source's rule is safe).** The source's group elements all fix the scalar unit and map the vector part to itself, so the sign matrix $D$ has no visible effect on their block form and the plain transpose, the associate and the Hermitian adjoint agree there; the three are the same involution on the operators the source writes down. For a general linear function the three differ, and the corpus keeps the association and the dagger apart, the first the transpose for the indefinite scalar form and the second the adjoint for the positive Hermitian form.

## The General Family

Association is the biquaternion instance of the general transpose of a bilinear form. For a finite-dimensional vector space with a non-degenerate bilinear form the form identifies the space with its dual, and the transpose of an endomorphism is the endomorphism of the dual read back on the space by the identification; in coordinates it is the conjugation by the Gram matrix, $M\mapsto G^{-1}M^{\mathsf T}G$, of *Bilinear Forms*, §*Isometries*, and of *Quadratic Forms and Polarisation*, §*Isometry of Forms*. Two features separate the biquaternion case from the general one and are why it has its own name in the corpus. The form is the scalar part of the algebra's own product, so its transpose carries the additional algebra identities $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$ and $L_a^{\approx}=R_a$, $R_b^{\approx}=L_b$; and the algebra carries a second, positive definite pairing, the Hermitian one, so a second adjoint, the dagger, competes with the association. The general transpose is developed in the linear-algebra series; the positive definite adjoint is developed in the Hilbert-algebra series; this article is where the two meet on the one algebra.

## Summary

The **associate** $F^{\approx}$ of a $\mathbb{C}$-linear map of the biquaternion algebra is its transpose for the indefinite general plain bilinear form $\langle\tilde R,\tilde S\rangle=\mathrm{Sc}(\tilde R\tilde S)$ of *The Four Pairings of the Biquaternion Algebra*, defined by $\mathrm{Sc}(F\tilde R\,\tilde S)=\mathrm{Sc}(\tilde R\,F^{\approx}\tilde S)$ and equivalently by $\langle F\tilde R,\tilde S\rangle=\langle\tilde R,F^{\approx}\tilde S\rangle$. It reverses composition, $(FG)^{\approx}=G^{\approx}F^{\approx}$, and on the Conway operator basis it reverses the factors, $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$, so the regular operators transpose into one another, $L_a^{\approx}=R_a$ and $R_b^{\approx}=L_b$. Its matrix in the coefficient basis is $M^{\approx}=D M^{\mathsf T}D$, which is the plain transpose exactly for the operators that fix the scalar unit and preserve the vector part; combined with the conjugation of the coefficients it relates the associate to the Hermitian adjoint by $\bar F^{\approx}=D F^{*}D$, an identity that collapses to $\bar F^{\approx}=F^{*}=F^{-1}$ on the vector-preserving unitaries that the source uses. Association is the biquaternion instance of the general transpose of a bilinear form of the linear-algebra series; it is kept apart from the dagger, the adjoint for the positive definite Hermitian form of the Hilbert-algebra series. The enveloping algebra, the Conway operator basis and the bi-module structure are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde R,\tilde S\rangle=\mathrm{Sc}(\tilde R\tilde S)$ | the general plain bilinear form; symmetric, non-degenerate, realified signature $(4,4)$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | its Gram matrix in the coefficient basis |
| $F^{\approx}$ | the associate of $F$; the transpose for the form |
| $M^{\approx}=D M^{\mathsf T}D$ | the matrix of the associate |
| $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$ | association on the Conway basis; $L_a^{\approx}=R_a$, $R_b^{\approx}=L_b$ |
| $(FG)^{\approx}=G^{\approx}F^{\approx}$ | association reverses composition |
| $\bar F^{\approx}=D F^{*}D$ | association combined with coefficient conjugation, against the Hermitian adjoint |

## Further Reading

- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the associate $\approx$ side by side with the three other adjoints of the other three forms, on explicit matrices
- *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for the Conway operator basis, the regular representations and the bi-module structure
- *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the positive definite adjoint the dagger names
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the positive definite form the adjoint uses
- *Bilinear Forms* (`articles_maths/bilinear-forms.md`), §*Isometries*, and *Quadratic Forms and Polarisation* (`articles_maths/quadratic-forms-and-polarisation.md`), §*Isometry of Forms*, for the general transpose of a bilinear form
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form whose duality association is, and the four Gram matrices of the algebra, the adjoints of the four left multiplications and the companion general quaternionic bilinear form of Gram matrix $\mathrm{I}_4$
- *Biquaternion Lie Group and Exponential Structure* (`articles_maths/biquaternion-lie-group-and-exponential-structure.md`), for the unitary elements on which the source's three involutions agree.
