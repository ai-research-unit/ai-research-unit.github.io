# __One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

Let $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its Hermitian conjugation ${}^{*}$ and the positive definite complex sesquilinear form $(\tilde T,\tilde V)=\mathrm{Sc}(\tilde{T}^{*}\tilde V)$, whose Gram matrix in the basis $e_{0},e_{1},e_{2},e_{3}$ is the identity. For $\tilde B\in\mathbb{B}$ define the **left** and the **right multiplication**

$$
L_{\tilde B}(\tilde V) = \tilde B\,\tilde V ,\qquad R_{\tilde C}(\tilde V) = \tilde V\,\tilde C .
$$

These are the two one-sided operators of the algebra, and the two-sided operator of the companion article is their product, $\Theta_{\tilde B}=L_{\tilde B}R_{\tilde{B}^{*}}=R_{\tilde{B}^{*}}L_{\tilde B}$ (*Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*).

The article is the parallel of that one, section for section, and the contrast is the point of the pair. **Here the parameter enters linearly**, so the ordinary rules hold: $L$ is a multiplicative and additive assignment, the adjoint of $L_{\tilde B}$ is $L_{\tilde{B}^{*}}$, the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ give the **self-adjoint** and the **skew-adjoint** operators respectively, and the operators of the slice are the isometries. In the two-sided case the same questions have different answers — both sectors give self-adjoint operators, no nonzero operator is skew and the assignment is quadratic — because the sandwich contains the parameter twice. Reading the two articles together isolates exactly what the doubling of the parameter does.

The algebra, the dagger, the sectors and the slice are *Biquaternions as a Vector Space over $\mathbb{C}$*, *The Group of Involutions* and *Introduction to the Six Subspaces*; the general one-sided theory is *One-Sided Operators on a Hilbert Algebra with Hermitian Adjoint*, *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint* and *The Adjoint of the One-Sided Action with Hermitian Adjoint*, whose biquaternion instance this article is. The left and the right multiplications in coordinates are *Biquaternion 4×4 Regular Matrix Element Representation*; the mixed operators with two independent one-sided parameters are *Mixed Inner Conjugation and Hermitian Adjoint*.

## The One-Sided Operators

**Definition.** For $\tilde B,\tilde C\in\mathbb{B}$ the **left multiplication by $\tilde B$** and the **right multiplication by $\tilde C$** are the $\mathbb{C}$-linear operators $L_{\tilde B},R_{\tilde C}\in\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ with

$$
L_{\tilde B}(\tilde V)=\tilde B\,\tilde V,\qquad R_{\tilde C}(\tilde V)=\tilde V\,\tilde C .
$$

**Proposition (linearity in the parameter).** The assignments $\tilde B\mapsto L_{\tilde B}$ and $\tilde C\mapsto R_{\tilde C}$ are $\mathbb{C}$-linear and injective:

$$
L_{\alpha \tilde B+\beta \tilde B'} = \alpha L_{\tilde B} + \beta L_{\tilde B'},\qquad R_{\alpha \tilde C+\beta \tilde C'} = \alpha R_{\tilde C} + \beta R_{\tilde C'},
$$

and $L_{\tilde B}=0$ or $R_{\tilde C}=0$ implies $\tilde B=0$ or $\tilde C=0$.

*Proof.* The two displays are the distributivity of the algebra, and the injectivity follows by evaluating on $e_{0}$.

**Remark (the contrast with the two-sided case).** The parameter enters **once**, so the assignment is linear and additive; in the two-sided case it enters twice, $\Theta_{\alpha \tilde T+\beta \tilde Q}(\tilde V)=\alpha\alpha^{*}\Theta_{\tilde T}(\tilde V)+\beta\beta^{*}\Theta_{\tilde Q}(\tilde V)+(\alpha\beta^{*}\tilde T\tilde V \bar{\tilde Q}+\beta\alpha^{*}\tilde Q\tilde V\tilde{T}^{*})$, which is the failure of additivity. Every difference between this article and its companion traces back to this one fact.

## The Composition Laws

**Theorem (the four composition laws).** For all $\tilde B,\tilde C\in\mathbb{B}$,

$$
L_{\tilde B}L_{\tilde C} = L_{\tilde B\tilde C},\qquad R_{\tilde B}R_{\tilde C} = R_{\tilde C\tilde B},\qquad L_{\tilde B}R_{\tilde C} = R_{\tilde C}L_{\tilde B},\qquad L_{\tilde B}R_{\tilde{B}^{*}} = \Theta_{\tilde B}.
$$

*Proof.* Associativity gives the first two, and the third is the associativity identity $\tilde B\,(\tilde V\,\tilde C)=(\tilde B\,\tilde V)\,\tilde C$; the fourth is the definition of the two-sided operator. All four were verified on random triples.

**Corollary (the two families, and the two-sided family as their product).** The left multiplications form a subalgebra of the operators isomorphic to $\mathbb{B}$ and the right multiplications form a subalgebra anti-isomorphic to $\mathbb{B}$, and the two subalgebras commute inside $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$; the products $L_{\tilde B}R_{\tilde C}$ are the **mixed** operators $\tilde V\mapsto \tilde B\tilde V\tilde C$, of which the two-sided family is the diagonal case $\tilde C=\tilde{B}^{*}$. A general mixed operator has two independent parameters and is a two-sided operator only when $\tilde C=\lambda \tilde{B}^{*}$ for a scalar $\lambda$, in which case it is $\lambda \Theta_{\tilde B}$; the mixed family is the subject of *Mixed Inner Conjugation and Hermitian Adjoint*.

## The Adjoints of the One-Sided Operators

**Theorem (the adjoints).** For all $\tilde B,\tilde C\in\mathbb{B}$,

$$
(L_{\tilde B})^{*} = L_{\tilde{B}^{*}},\qquad (R_{\tilde C})^{*} = R_{\tilde{C}^{*}} .
$$

*Proof.* For $\tilde V,\tilde Q\in\mathbb{B}$, using the anti-involution property of the dagger and the invariance of the scalar part under cyclic permutation,

$$
(L_{\tilde B}\tilde V,\tilde Q) = \mathrm{Sc}\bigl((\tilde B\tilde V)^{\dagger}\tilde Q\bigr) = \mathrm{Sc}\bigl(\tilde{V}^{*}\tilde{B}^{*}\tilde Q\bigr) = \bigl(\tilde V,\ L_{\tilde{B}^{*}}\tilde Q\bigr) ,
$$

and the same computation on the right with $(\tilde V\tilde C)^{\dagger}=\tilde{C}^{*}\tilde{V}^{*}$ gives $(R_{\tilde C}\tilde V,\tilde Q)=(\tilde V,R_{\tilde{C}^{*}}\tilde Q)$. The adjoint is unique, since the form is non-degenerate. Verified on the generators and on random elements.

**Corollary (the dagger is natural for the one-sided operators).** The assignments $\tilde B\mapsto L_{\tilde B}$ and $\tilde C\mapsto R_{\tilde C}$ carry the dagger of the algebra to the adjoint of the operator. Consequently $L$ is a **faithful $*$-representation** of the algebra on the Hilbert space $(\mathbb{B},(\cdot,\cdot))$: it is linear, multiplicative, injective and compatible with the dagger. Since $\mathbb{B}\cong M_{2}(\mathbb{C})$ and $\dim_{\mathbb{C}}\mathbb{B}=4$, the representation is the left regular representation, that is two copies of the standard module $\mathbb{C}^{2}$ of the algebra (*Biquaternion 2×2 Matrix Element Representation*).

**Remark (which half of the dagger is used).** The adjoint of $L_{\tilde B}$ is $L_{\tilde{B}^{*}}$ and **not** $R_{\tilde{B}^{*}}$: the cross identity $(L_{\tilde B}\tilde V,\tilde Q)=(\tilde V,R_{\tilde{B}^{*}}\tilde Q)$ is false in general. In the matrix model the point is that the Hilbert structure of the algebra is the space of matrices with the Hilbert–Schmidt form, and the adjoint of left multiplication is again left multiplication.

## Self-Adjoint, Skew and Unitary One-Sided Operators

**Theorem (the type criteria).** Let $\tilde B\in\mathbb{B}$ and let $L_{\tilde B}$ be the left multiplication. Then

$$
L_{\tilde B}\ \text{self-adjoint} \iff \tilde B\in\mathbb{M}_+,\qquad
L_{\tilde B}\ \text{skew-adjoint} \iff \tilde B\in\mathbb{M}_-,
$$

$$
L_{\tilde B}\ \text{unitary} \iff \tilde B\in U,\qquad
L_{\tilde B}\ \text{an isometry of } (\cdot,\cdot) \iff \tilde B\in U,
$$

and $L_{\tilde B}$ is invertible if and only if $\tilde B\in\mathbb{B}^{\times}$, with inverse $L_{\tilde B^{-1}}$. The same four statements hold for the right multiplication with the same criteria on the parameter.

*Proof.* By the adjoint theorem, $L_{\tilde B}^{*}=L_{\tilde{B}^{*}}$, and the assignment is injective, so $L_{\tilde B}^{*}=L_{\tilde B}$ if and only if $\tilde{B}^{*}=\tilde B$, $L_{\tilde B}^{*}=-L_{\tilde B}$ if and only if $\tilde{B}^{*}=-\tilde B$, and $(L_{\tilde B})^{*}L_{\tilde B}=L_{\tilde{B}^{*}\tilde B}$ is the identity if and only if $\tilde{B}^{*}\tilde B=e_{0}$. The isometry criterion is the same computation, $(L_{\tilde B}\tilde V,L_{\tilde B}\tilde Q)=(\tilde V,\tilde{B}^{*}\tilde B\tilde Q)$, and it coincides with unitarity of the operator. Invertibility is the inverse of an algebra element. All four were verified over random parameters and over both sectors.

**Corollary (the two sectors give the two types).** The Hermitian and the anti-Hermitian elements act by the self-adjoint and by the skew-adjoint operators respectively, and the correspondence is exactly that of the involutions of the algebra:

$$
L_{\mathbb{M}_+} = \text{self-adjoint operators},\qquad L_{\mathbb{M}_-} = \text{skew-adjoint operators}.
$$

This is the sharpest contrast with the companion article, where both sectors give self-adjoint operators and no nonzero operator is skew: there the parameter appears twice, and the sign that separates the sectors is squared away.

**Corollary (the exponential and the unitary group).** Since $L_{\tilde B}^{*}=L_{\tilde{B}^{*}}$, the image of the slice $U$ under $L$ is a group of unitary operators isomorphic to $U(2)$, and the image of the anti-Hermitian subspace $\mathbb{M}_-$ is a space of skew-adjoint operators closed under the commutator, that is the Lie algebra of that unitary group. The exponential of a skew-adjoint one-sided operator is again one-sided: $e^{L_{\tilde B}}=L_{e^{\tilde B}}$ for $\tilde B\in\mathbb{M}_-$, since the exponential series and the linearity of the assignment commute. In the matrix model this is the familiar statement that the anti-Hermitian matrices exponentiate into $U(2)$.

## The Commutant and the Double Centraliser

**Theorem (the double centraliser).** An operator $S\in\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ commutes with every left multiplication if and only if it is a right multiplication, and conversely:

$$
\{\,S : SL_{\tilde B}=L_{\tilde B}S\ \ \forall \tilde B\,\} = \{\,R_{\tilde C} : \tilde C\in\mathbb{B}\,\},\qquad
\{\,S : SR_{\tilde C}=R_{\tilde C}S\ \ \forall \tilde C\,\} = \{\,L_{\tilde B} : \tilde B\in\mathbb{B}\,\}.
$$

*Proof.* Let $S$ commute with all $L_{\tilde B}$ and put $\tilde C=S(e_{0})$. For every $\tilde B$, using $\tilde B=L_{\tilde B}(e_{0})$ and the commutation,

$$
S(\tilde B) = S\bigl(L_{\tilde B}(e_{0})\bigr) = L_{\tilde B}\bigl(S(e_{0})\bigr) = \tilde B\,\tilde C = R_{\tilde C}(\tilde B),
$$

so $S=R_{\tilde C}$; the converse is the third composition law. The second identity is the same argument with the roles exchanged.

**Corollary (the bicommutant is the scalars).** An operator commuting with both families is a scalar multiple of the identity:

$$
\{\,S : SL_{\tilde B}=L_{\tilde B}S\ \text{and}\ SR_{\tilde C}=R_{\tilde C}S\ \ \forall \tilde B,\tilde C\,\} = \mathbb{C}\,\mathrm{id}.
$$

*Proof.* By the theorem $S=R_{\tilde C}$ for some $\tilde C$, and the commutation with every $R_{c}$ reads $R_{c}R_{\tilde C}=R_{\tilde C}R_{c}$, that is $\tilde Cc=c\tilde C$ for all $c$ by the second composition law; so $\tilde C$ is central, $\tilde C=\lambda e_{0}$, and $R_{\lambda e_{0}}=\lambda\,\mathrm{id}$.

**Remark (why the two families are exactly two).** The algebra is central simple, of complex dimension four, and the left regular representation has the same dimension; the double centraliser theorem then says that the left and the right multiplications exhaust each other's commutants, with the centre as the only overlap. There is no room for a third independent family of one-sided operators.

## The Form That Makes the Action Self-Adjoint

**Theorem (the defining property of the form).** The scalar form satisfies, for all $\tilde B,\tilde V,\tilde Q$,

$$
(\tilde B\,\tilde V,\ \tilde Q) = \bigl(\tilde V,\ \tilde{B}^{*}\tilde Q\bigr) ,
$$

and it is, up to a positive scalar, the **only** complex sesquilinear form on $\mathbb{B}$ that is $\mathbb{C}$-linear in the second argument and invariant in the sense that the adjoint of $L_{\tilde B}$ is $L_{\tilde{B}^{*}}$ and the form is positive definite.

*Proof.* The identity is the adjoint theorem. For the uniqueness, let $\phi$ be such a form with matrix $G$ in the basis. The invariance with respect to every $L_{\tilde B}$ reads $G A = A^{\dagger}G$ for every matrix $A=\Phi(\tilde B)$ of the algebra; taking $A$ running over the matrix units forces $G$ to be a scalar matrix, and positivity then forces the scalar to be positive. See *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint* and *The Adjoint of the One-Sided Action with Hermitian Adjoint* for the general statement.

**Corollary (the module picture).** The algebra, seen as a module over itself carrying the form $(\cdot,\cdot)$, is a **Hermitian Clifford module** in the sense of the corpus: the action is by left multiplication and the adjoint of the action is the action of the adjoint element. The two-sided operator is then the operator of the module with both factors, $\Theta_{\tilde B}=L_{\tilde B}R_{\tilde{B}^{*}}=L_{\tilde B}(R_{\tilde B})^{*}$, the product of the action with the adjoint of the *other* action. Note that $L_{\tilde B}L_{\tilde B}^{*}=L_{\tilde B}L_{\tilde{B}^{*}}=L_{\tilde B\tilde{B}^{*}}$ is left multiplication by the Hermitian element $\tilde B\tilde{B}^{*}$, which is **not** $\Theta_{\tilde B}$; the two factors of the sandwich are one left and one right, and never two left.

## Worked Examples

**The identity and the central scalars.** $L_{e_{0}}=R_{e_{0}}=\mathrm{id}$. For a central scalar $\lambda e_{0}$ the two one-sided operators agree, $L_{\lambda e_{0}}=R_{\lambda e_{0}}=\lambda\,\mathrm{id}$, and they are self-adjoint exactly for $\lambda$ real, skew-adjoint exactly for $\lambda$ imaginary, unitary exactly for $\lvert\lambda\rvert=1$. The central circle gives the scalar unitary operators, a subgroup $U(1)$ of the group of unitary operators, to be compared with the kernel $U(1)$ of the two-sided assignment.

**The vector generators.** For $\tilde B=e_{k}$, $k=1,2,3$, one has $e_{k}^{\dagger}=-e_{k}$ and $e_{k}^{2}=-e_{0}$, so $L_{e_{k}}$ is skew-adjoint and $L_{e_{k}}^{2}=L_{-e_{0}}=-\mathrm{id}$: the left multiplication by a vector generator is a complex structure on the algebra, of square minus the identity. This is the operator form of the relations of the Clifford structure (*Biquaternion Clifford Structure*), and the three operators $L_{e_{1}},L_{e_{2}},L_{e_{3}}$ satisfy the anticommutation relations of the generators.

**A parameter in neither sector.** For $\tilde B=e_{1}+ie_{2}$ the dagger acts as $\tilde{B}^{*}=-e_{1}+ie_{2}$, so the Hermitian part of the parameter is $(\tilde B+\tilde{B}^{*})/2=ie_{2}$, which lies in $\mathbb{M}_+$, and the anti-Hermitian part is $(\tilde B-\tilde{B}^{*})/2=e_{1}$, which lies in $\mathbb{M}_-$. Accordingly the operator splits into a self-adjoint and a skew-adjoint part,

$$
L_{\tilde B} = L_{ie_{2}} + L_{e_{1}},
$$

and is therefore of neither of the two types, in agreement with the theorem: the parameter is in neither sector. The example records where the type is decided: by the parameter, through the sector it lies in, and never by the argument.

**A mixed operator that is not two-sided.** The operator $\tilde V\mapsto e_{1}\tilde Ve_{2}=L_{e_{1}}R_{e_{2}}$ is not of the form $\Theta_{\tilde T}$ for any $\tilde T$. Indeed a two-sided operator satisfies $\Theta_{\tilde T}(e_{0})=\tilde T\tilde{T}^{*}\in\mathbb{M}_+$, whereas $L_{e_{1}}R_{e_{2}}(e_{0})=e_{1}e_{2}=e_{3}$, which is anti-Hermitian; so no parameter $\tilde T$ reproduces the operator. In general $L_{\tilde B}R_{\tilde C}$ is two-sided only if $\tilde B\tilde C\in\mathbb{M}_+$, and when $\tilde C=\lambda \tilde{B}^{*}$ with $\lambda=\lvert\mu\rvert^{2}\geq0$ one has $L_{\tilde B}R_{\tilde C}=\Theta_{\mu \tilde B}$. Its adjoint is $L_{e_{1}^{\dagger}}R_{e_{2}^{\dagger}}=L_{-e_{1}}R_{-e_{2}}=L_{e_{1}}R_{e_{2}}$, so this particular mixed operator is self-adjoint, a phenomenon that the two-sided family does not show.

**A check of the composition and the adjoint.** For random $\tilde B,\tilde C$ and random $\tilde V,\tilde Q$, the identities $L_{\tilde B}L_{\tilde C}=L_{\tilde B\tilde C}$, $L_{\tilde B}R_{\tilde C}=R_{\tilde C}L_{\tilde B}$ and $(L_{\tilde B}\tilde V,\tilde Q)=(\tilde V,L_{\tilde{B}^{*}}\tilde Q)$ were verified to machine precision, as were the four type criteria over the four subspaces.

## Summary

The left and the right multiplications $L_{\tilde B}(\tilde V)=\tilde B\tilde V$ and $R_{\tilde C}(\tilde V)=\tilde V\tilde C$ are the one-sided operators of the biquaternion algebra, and the two-sided operator of the companion article is their product $\Theta_{\tilde B}=L_{\tilde B}R_{\tilde{B}^{*}}$. The parameter enters **linearly**, and everything follows: the assignment is additive and injective, the composition laws are $L_{\tilde B}L_{\tilde C}=L_{\tilde B\tilde C}$, $R_{\tilde B}R_{\tilde C}=R_{\tilde C\tilde B}$ and $L_{\tilde B}R_{\tilde C}=R_{\tilde C}L_{\tilde B}$, the adjoints are $(L_{\tilde B})^{*}=L_{\tilde{B}^{*}}$ and $(R_{\tilde C})^{*}=R_{\tilde{C}^{*}}$, so that $L$ is a faithful $*$-representation of the algebra on the Hilbert space of the scalar form, of complex dimension four, that is two copies of the standard module. The **type criteria** are the ones of the involution lattice: $L_{\tilde B}$ is self-adjoint exactly on $\mathbb{M}_+$, skew-adjoint exactly on $\mathbb{M}_-$, unitary and isometric exactly on the slice $U$, and invertible exactly on the group of units; the Lie algebra of the unitary one-sided operators is $L_{\mathbb{M}_-}$ and the exponential stays inside the family, $e^{L_{\tilde B}}=L_{e^{\tilde B}}$. The **double centraliser theorem** holds in two lines: the commutant of the left multiplications is the right multiplications and conversely, the bicommutant is the scalars, and the mixed operators $L_{\tilde B}R_{\tilde C}$ with two independent parameters are the ones that are not two-sided. Finally the scalar form is characterised among the positive definite complex sesquilinear forms by the property that the adjoint of the action is the action of the adjoint element, which is the statement that the algebra is a Hermitian Clifford module over itself. The pair of articles isolates in this way what the doubling of the parameter in the sandwich costs: the additivity, the separation of the two sectors, the existence of skew operators, and the injectivity of the assignment.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra; basis $e_{0},e_{1},e_{2},e_{3}$ |
| ${}^{*}$ | Hermitian conjugation; $\mathbb{M}_+$ fixed, $\mathbb{M}_-$ anti-fixed |
| $(\tilde T,\tilde V)=\mathrm{Sc}(\tilde{T}^{*}\tilde V)$ | The scalar form; Gram matrix the identity |
| $L_{\tilde B}(\tilde V)=\tilde B\tilde V$ | Left multiplication; $\mathbb{C}$-linear and injective in $\tilde B$ |
| $R_{\tilde C}(\tilde V)=\tilde V\tilde C$ | Right multiplication; the anti-homomorphism family |
| $\Theta_{\tilde B}=L_{\tilde B}R_{\tilde{B}^{*}}$ | The two-sided operator, the product of the two |
| $L_{\tilde B}L_{\tilde C}=L_{\tilde B\tilde C}$, $R_{\tilde B}R_{\tilde C}=R_{\tilde C\tilde B}$ | Composition laws |
| $L_{\tilde B}R_{\tilde C}=R_{\tilde C}L_{\tilde B}$ | The two families commute |
| $(L_{\tilde B})^{*}=L_{\tilde{B}^{*}}$, $(R_{\tilde C})^{*}=R_{\tilde{C}^{*}}$ | The adjoints; $L$ is a $*$-representation |
| $U=\{\tilde{T}^{*}\tilde T=e_{0}\}=U(2)$ | The unitary slice; the isometries and the unitary operators |
| $\{S : SL_{\tilde B}=L_{\tilde B}S\ \forall \tilde B\}=R(\mathbb{B})$ | The double centraliser theorem |
| $L_{\tilde B}R_{\tilde C}$ | Mixed operator; two-sided only if $\tilde C=\lambda \tilde{B}^{*}$ |

## Further Reading

- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, the four conjugations and the six subspaces.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), the companion article, with the composition and the type theorems for the product of the two one-sided families.
- *Biquaternion 4×4 Regular Matrix Element Representation* (`articles_maths/biquaternion-4x4-regular-matrix-element-representation.md`), for the left and the right regular representations in matrix form.
- *One-Sided Operators on a Hilbert Algebra with Hermitian Adjoint* (`articles_maths/one-sided-operators-on-a-hilbert-algebra-with-hermitian-adjoint.md`), for the general one-sided theory, the double centraliser and the images as ideals.
- *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint* (`articles_maths/hermitian-modules-over-a-hilbert-algebra-with-hermitian-adjoint.md`), for the module axiom $(\tilde B\cdot s,t)=(s,\tilde{B}^{*}\cdot t)$ used in the last section.
- *The Adjoint of the One-Sided Action with Hermitian Adjoint* (`articles_maths/the-adjoint-of-the-one-sided-action-with-hermitian-adjoint.md`), for the $*$-structure on the operator algebra and the reason a Dirac operator is formally self-adjoint.
- *Mixed Inner Conjugation and Hermitian Adjoint* (`articles_maths/mixed-inner-conjugation-and-hermitian-adjoint.md`), for the operators with two independent one-sided parameters.
- *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint* (`articles_maths/unitary-equivalence-and-congruence-of-operators-with-hermitian-adjoint.md`), for the equivalence relations of the operator families.
