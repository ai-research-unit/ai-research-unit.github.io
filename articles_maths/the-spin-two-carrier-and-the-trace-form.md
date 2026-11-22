# __The Spin-Two Carrier and the Trace Form__

## Introduction

**The subject.** The quintet inherits two forms from the operator space: the complex bilinear trace form $\beta(S,T)=\operatorname{tr}(ST)$, which is symmetric, invariant and indefinite, and the Hermitian form $h(S,T)=\operatorname{tr}(S^{\dagger}T)$, which is positive definite. The article computes both on the carrier, proves that the restriction of $\beta$ is nondegenerate of rank five, and reads its signature $(3,2)$ from the weight basis.

**The order of the article.** The two forms are defined first and their invariance is proved. The restriction to the carrier and the orthogonality of the four carriers follow, then the weight basis, the signature and the comparison with the triplet of the row of the elements.

**It assumes** *Introduction to the Spin-Two Carrier: the Alternating Square* and *The Symmetric and Antisymmetric Parts of the Operator Space*. **The row of the elements is** where the trace form is read on a four-dimensional space; there the carrier of label one is a real three-dimensional space on which the form is definite.

**The result in one line.** On $V_2$ the trace form is nondegenerate of rank five with no radical, its array in the unit weight basis is antidiagonal with the entries $(-1)^{m}$ at the pairs $(m,-m)$, and its signature on the real form is $(3,2)$.

**Boundaries.** The carrier itself, its weight string and its reality type are *Introduction to the Spin-Two Carrier: the Alternating Square*; the ranks realised inside it are *The Spin-Two Carrier and the Rank Strata*; the corresponding form on the septet is *The Spin-Three Carrier and the Hermitian Form*.

## The Two Forms

**Definition.** For two operators of the sixteen the **trace form** and the **Hermitian form** are
$$
\beta(S,T)=\operatorname{tr}(ST),\qquad
h(S,T)=\operatorname{tr}(S^{\dagger}T),
$$
where $\operatorname{tr}$ is the trace of the composite on the four-dimensional algebra and $\dagger$ is the adjoint with respect to the positive definite form $\operatorname{tr}(X^{\star}Y)$ of the algebra.

**Proposition.** The form $\beta$ is complex bilinear, symmetric, nondegenerate and invariant under the copy; the form $h$ is Hermitian and positive definite.

*Proof.* Bilinearity and symmetry are the bilinearity of the product and the cyclicity of the trace. For invariance under the action $S\mapsto[\xi,S]$ of a generator,
$$
\operatorname{tr}([\xi,S]T)+\operatorname{tr}(S[\xi,T])=\operatorname{tr}(\xi ST)-\operatorname{tr}(ST\xi)=0,
$$
the two inner terms cancelling. Nondegeneracy: $\beta(S,T)=0$ for all $T$ forces $S=0$, since $S$ has a nonzero coefficient on some basis product. Positivity of $h$: $\operatorname{tr}(S^{\dagger}S)$ is the sum of the squares of the moduli of the coefficients of $S$ in a basis orthonormal for the form of the algebra, and it vanishes only at zero.

**The reading.** The operator space carries a positive definite form and an indefinite one. Every statement below is made twice, once for each, and the two answers differ exactly on the real form.

## The Restriction to the Quintet

**Proposition.** The four carriers are pairwise orthogonal for $\beta$ and for $h$, and the restrictions of both forms to $V_2$ are nondegenerate.

*Proof.* The carriers are the isotypic components of the operator space for the copy, and an invariant bilinear form pairs two isotypic components of distinct labels trivially, because no map between non-isomorphic irreducible carriers exists. On a single carrier the invariant form is unique up to a scalar, and the scalar is not zero, since $\beta$ is nondegenerate on the whole sixteen and the orthogonal splitting is direct.

**Corollary.** The restriction of $\beta$ to $V_2$ is a symmetric bilinear form of rank five with no radical, and the restriction of $h$ is a positive definite Hermitian form of complex dimension five.

*Proof.* The rank is the dimension, by nondegeneracy; a radical would be a vector orthogonal to the whole carrier, which nondegeneracy forbids. Positivity of $h$ is inherited from the whole space.

**Corollary.** The quadratic form $q(X)=\operatorname{tr}(X^{2})$ is the quadratic form of $\beta$ on the carrier, and it is not definite.

*Proof.* $q$ is the diagonal of $\beta$; indefiniteness follows from the signature computed below, and independently from the element of weight zero, whose value $q$ is positive, against a nilpotent element, whose value is zero.

**The reading.** Orthogonality of the carriers is the operator form of the orthogonality of irreducible summands. It holds for both forms at once, so the two forms are diagonal in the same splitting of the sixteen, and each carrier can be discussed on its own.

## The Weight Basis

**Definition.** The **weight basis** of the carrier is a string $v_2,v_1,v_0,v_{-1},v_{-2}$ of weight vectors, normalised so that $h(v_m,v_m)=1$ and so that the ladder operators act with real positive coefficients.

**Proposition.** In the weight basis the Hermitian form is the identity array, and the trace form is antidiagonal,
$$
\beta(v_m,v_n)=0\ \text{unless}\ n=-m,\qquad
\beta(v_2,v_{-2})=1,\quad \beta(v_1,v_{-1})=-1,\quad \beta(v_0,v_0)=1 .
$$

*Proof.* The form $h$ is invariant and the weight vectors have distinct weights, so distinct weight vectors are orthogonal for $h$; the normalisation makes the diagonal one. The form $\beta$ is invariant and complex bilinear, so it can pair only weights summing to zero, which leaves the diagonal and the two opposite pairs. The values follow from the ladder action: moving one weight vector to its opposite costs the ladder coefficient twice, and the signs alternate with the weight, which gives $(-1)^{m}$ at the pair $(m,-m)$.

**Corollary.** Every weight vector of odd weight is isotropic for $\beta$, and the weight-zero vector is not.

*Proof.* The pairing of $v_m$ with itself vanishes unless $2m=0$, that is unless $m=0$; at $m=0$ the value is one.

**Corollary.** The Hilbert–Schmidt norm of an element $X=\sum_m x_m v_m$ is $\lVert X\rVert^{2}=\sum_m\lvert x_m\rvert^{2}$, and its trace form is $2\sum_{m>0}(-1)^{m}\operatorname{Re}(x_m x_{-m})+x_0^{2}$.

*Proof.* The first identity is the statement that $h$ is the identity array in this basis; the second is the expansion of the antidiagonal pairing.

**The reading.** The two forms are as different as two forms on the same space can be: one is the identity array in the weight basis and the other is antidiagonal. The weight basis is therefore the basis in which the Hermitian form is simplest, and the trace form is simplest in the basis of the real form.

## The Signature

**Theorem.** On the real form of the carrier the trace form is real, symmetric and of signature $(3,2)$.

*Proof.* The real form is the fixed space of the antilinear involution $J_2$ commuting with the copy, and $J_2$ sends $v_m$ to a multiple of $v_{-m}$. The real form is therefore spanned by the weight-zero vector and, for each pair $\pm m$, by the two real combinations of $v_m$ and $v_{-m}$. On such a pair the restriction of $\beta$ has zero diagonal and the entry $(-1)^{m}$ between the two real directions, so its array is
$$
\beta(w,v_m)=0,\qquad \beta(v_m,v_m)=0,\qquad \beta(w,w)=0,\qquad \beta(w,v_m)=(-1)^{m},
$$
and a symmetric form of this shape has one positive and one negative eigenvalue whatever the sign. There are two pairs, at $m=2$ and $m=1$, and each contributes one positive and one negative direction; the weight-zero line contributes one positive direction. The total is three positive and two negative.

**Corollary.** The maximal subspaces on which the trace form is definite have real dimensions three and two, and the form is indefinite.

*Proof.* The count of the theorem, and the existence of an isotropic vector, namely any weight vector of nonzero weight.

**Corollary.** The Hermitian form is positive definite on the same real form, so the carrier is a Hilbert space of real dimension five for $h$ and a space of neutral type for $\beta$.

*Proof.* A restriction of a positive definite form is positive definite; the indefiniteness of $\beta$ is the theorem.

**The reading.** The signature is read from the weight string without a computation: each pair of opposite weights contributes one positive and one negative direction, and the unpaired weight zero contributes one positive. The quintet has two pairs and one unpaired weight, which is why its signature is $(3,2)$ and not $(5,0)$ or $(1,4)$.

## The Comparison with the Triplet of the Elements

**Proposition.** On the carrier of label one in the row of the elements the trace form is definite, and on the triplet of the operator row it is not.

*Proof.* In the row of the elements the carrier of label one is the real span of the three pure units, and for two such vectors $\operatorname{tr}(XY)=-4\langle x,y\rangle$, which is negative definite. In the operator row the triplet has weights $1,0,-1$, hence one pair of opposite weights and one unpaired weight, and the argument of the theorem gives the signature $(2,1)$.

**Corollary.** Definiteness is a property of the carrier in the row in which it is read, not of the label.

*Proof.* The label one occurs in both rows, and the two carriers have forms of different types: negative definite in the row of the elements, of signature $(2,1)$ in the row of the operators.

**The reading.** The comparison isolates what the operator row does to a form. The same construction, applied to the algebra and to its endomorphisms, produces a definite form at the first step and an indefinite one at the second, because the second carrier has an unpaired weight and a pair at once.

## Further Reading

- [Introduction to the Spin-Two Carrier: the Alternating Square](introduction-to-the-spin-two-carrier-the-alternating-square.html), for the carrier and its weights.
- [The Spin-Two Carrier and the Rank Strata](the-spin-two-carrier-and-the-rank-strata.html), for the isotropic cone of the form.
- [The Spin-Three Carrier and the Hermitian Form](the-spin-three-carrier-and-the-hermitian-form.html), for the form on the septet.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the star and the two halves.
- [The Two-Sided Operators and the Segre Cone](the-two-sided-operators-and-the-segre-cone.html), for the trace of a product.
