# __The Adjoints and the Polar Decomposition of an Operator at $n=4$__

## Introduction

**An operator on the sixteen-dimensional matrix space has two different adjoints: the plain adjoint for the trace pairing $\beta(X,Y)=\operatorname{tr}(XY)$, which sends $T_{a,b}$ to $T_{b,a}$, and the Hilbert–Schmidt adjoint, which sends $T_{a,b}$ to $T_{a^{\ast},b^{\ast}}$; they agree exactly on the operators with $b=a^{\ast}$, the self-adjoint families are four-dimensional, the isometries are the operators with both factors unitary, and every invertible operator has a polar decomposition inside the $256$-dimensional algebra.**

The article computes the two adjoints, exhibits the operators on which they differ, computes the two self-adjoint families, characterises the isometries by a multiplicative criterion, proves the polar decomposition in the operator algebra, identifies the singular values, and contrasts the decomposition of an operator with the polar decomposition of an element.

It assumes *The Two-Sided Operators and the Segre Cone at $n=4$*, *The Hilbert–Schmidt Form at $n=4$* and *The Length and the Two Ranks at $n=4$*. The model at order two is *The Adjoints and the Polar Decomposition of an Operator at $n=2$*; the element version is *The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$*.

## The Plain Adjoint

**Definition.** The **plain adjoint** of an operator $T$ is the operator $T^{\mathrm{plain}}$ satisfying $\operatorname{tr}(T(X)Y)=\operatorname{tr}(X\,T^{\mathrm{plain}}(Y))$ for all $X,Y$.

**Proposition.** $\beta(X,Y)=\operatorname{tr}(XY)$ is a nondegenerate symmetric bilinear form on the matrix space, so the plain adjoint exists and is unique.

**Proof.** Nondegeneracy of the trace pairing on a full matrix algebra, and the standard duality argument for the existence of an adjoint.

**Theorem.** $\bigl(T_{a,b}\bigr)^{\mathrm{plain}}=T_{b,a}$.

**Proof.** $\operatorname{tr}\bigl(T_{a,b}(X)Y\bigr)=\operatorname{tr}(aXbY)=\operatorname{tr}(X\,bYa)=\operatorname{tr}\bigl(X\,T_{b,a}(Y)\bigr)$ by the cyclicity of the trace.

**Corollary.** The plain adjoint is an involution of the operator algebra: it is linear, reverses the order of a product, and is the identity on the operators $T_{a,a}$.

**Proof.** The formula in the two indices, and the product rule $T_{a,b}T_{c,d}=T_{ac,db}$ reversed.

**Corollary.** The plain adjoint of a single product is again a single product, so the Segre cone is invariant and the length is preserved.

**Proof.** $T_{b,a}$ is a single product, and the coefficient matrix transposes.

## The Hilbert–Schmidt Adjoint

**Definition.** The **Hilbert–Schmidt adjoint** $T^{\ast}$ is the adjoint for $\langle X,Y\rangle=\operatorname{tr}(X^{\ast}Y)$.

**Proposition.** $\langle X,Y\rangle$ is a positive definite Hermitian form, so the Hilbert–Schmidt adjoint exists, is unique, and satisfies $T^{\ast\ast}=T$.

**Proof.** $\operatorname{tr}(X^{\ast}X)$ is the sum of the squared moduli of the entries, hence positive for nonzero $X$.

**Theorem.** $\bigl(T_{a,b}\bigr)^{\ast}=T_{a^{\ast},b^{\ast}}$, where $^{\ast}$ on the right is the conjugate transpose of the matrix of the element.

**Proof.** $\operatorname{tr}\bigl((aXb)^{\ast}Y\bigr)=\operatorname{tr}(b^{\ast}X^{\ast}a^{\ast}Y)=\operatorname{tr}\bigl(X^{\ast}a^{\ast}Yb^{\ast}\bigr)=\operatorname{tr}\bigl(X^{\ast}T_{a^{\ast},b^{\ast}}(Y)\bigr)$.

**Corollary.** The two adjoints coincide exactly when $b=a^{\ast}$, that is on the operators $T_{a,a^{\ast}}$.

**Proof.** Compare the two formulas: $T_{b,a}=T_{a^{\ast},b^{\ast}}$ forces $b=a^{\ast}$ and $a=b^{\ast}$, which are the same condition.

**Corollary.** The two adjoints differ on the generic operator, and the difference is the involution of the algebra used in the pairing, not a different structure of the operator.

**Proof.** The plain adjoint uses the transpose, the Hilbert–Schmidt adjoint the conjugate transpose, and the two differ by the complex conjugation.

**The two involutions.** Both are antilinear involutions of the operator algebra, and their composition is the conjugation of the coefficients, an involution with two eigenspaces.

**Proof.** Each is an antilinear involution, and the composition of two antilinear involutions is linear.

## The Self-Adjoint Family

**Proposition.** The operators self-adjoint for the plain pairing are exactly the $T_{a,a}$, a family of complex dimension $4$; those self-adjoint for the Hilbert–Schmidt pairing are the $T_{a,a^{\ast}}$, also of complex dimension $4$.

**Proof.** $T_{a,b}^{\mathrm{plain}}=T_{a,b}$ forces $b=a$, and $T_{a,b}^{\ast}=T_{a,b}$ forces $b=a^{\ast}$; in each case the free parameter is the element $a$, of four complex dimensions.

**Corollary.** Each family is a real subspace of dimension $8$, and their intersection is the set of $T_{a,a}$ with $a$ self-adjoint as a matrix, of real dimension $4$.

**Proof.** The complex dimension four is a real dimension eight for the first family; the second is the image of an antilinear map and has the same real dimension; the intersection is fixed by the condition $a=a^{\ast}$, and the self-adjoint elements of the biquaternion algebra form a real space of dimension four.

**Corollary.** The operator $T_{\mu\nu}$ is plain self-adjoint exactly when $\mu=\nu$, and then it is a signed permutation with square the identity.

**Proof.** The plain adjoint swaps the two indices.

**The degenerate case.** The plain self-adjoint operators of the basis are $T_{tt},T_{xx},T_{yy},T_{zz}$ and none of the off-diagonal ones, so the four coordinates of the diagonal are the self-adjoint directions.

**Proof.** The index condition $\mu=\nu$.

## The Isometries

**Theorem.** An operator $T_{a,b}$ is an isometry for the Hilbert–Schmidt form exactly when $a$ and $b$ are unitary matrices.

**Proof.** $T_{a,b}^{\ast}T_{a,b}=T_{a^{\ast},b^{\ast}}T_{a,b}=T_{a^{\ast}a,\,bb^{\ast}}$, which is the identity exactly when $a^{\ast}a=\mathrm I_4$ and $bb^{\ast}=\mathrm I_4$.

**Corollary.** The isometries form a subgroup of the operator algebra, isomorphic to $U(4)\times U(4)$, of real dimension $32$.

**Proof.** The product of two isometries is an isometry and the inverse of an isometry is one; the parameter space is the product of the two unitary groups.

**Corollary.** The isometry condition is multiplicative: it is the conjunction of one condition on each factor, and it does not mix them.

**Proof.** The two conditions are independent.

**The plain analogue.** An operator is an isometry for the plain pairing exactly when $b=a^{-1}$, which is a different condition and is defined only for invertible $a$.

**Proof.** $T_{b,a}T_{a,b}=T_{ba,ab}$ equals the identity only when $ba=ab=\mathrm I_4$.

**Corollary.** The two isometry groups are different subgroups of the same dimension $32$, and they meet in the operators with $a$ unitary and $b=a^{-1}$.

**Proof.** The two conditions and their conjunction.

## The Polar Decomposition of the Operator Algebra

**Theorem.** Every invertible operator $T$ in $\operatorname{End}(M_4)$ is uniquely $T=HU$ with $H$ positive definite self-adjoint for the Hilbert–Schmidt form and $U$ an isometry.

**Proof.** Put $H=(TT^{\ast})^{1/2}$, which is positive definite self-adjoint, and $U=H^{-1}T$; then $U^{\ast}U=T^{\ast}H^{-2}T=\mathrm I$; uniqueness follows because $TT^{\ast}=H^{2}$ determines $H$ as the positive square root.

**Corollary.** The polar decomposition is a diffeomorphism $\operatorname{End}^{\times}\to\mathcal{P}\times U(4)\times U(4)$, where $\mathcal{P}$ is the open cone of positive definite self-adjoint operators.

**Proof.** The bijection and the smoothness of $T\mapsto((TT^{\ast})^{1/2},(TT^{\ast})^{-1/2}T)$.

**Corollary.** The polar decomposition of a single product is the product of the polar decompositions of its two factors, because the two factors commute.

**Proof.** $T_{a,b}=L_aR_b$ with $L_a=|L_a|U_a$ and $R_b=|R_b|U_b$ commuting, so $T_{a,b}=(|L_a||R_b|)(U_aU_b)$ with the first factor positive and the second an isometry.

**The operator against the element.** The polar decomposition of an element of $M_4$ is the decomposition of a $4\times4$ matrix into a stretch and a rotation; the polar decomposition of an operator is the same statement in the $256$-dimensional algebra, and the second is not the first applied entrywise.

**Proof.** The two decompositions live in algebras of different dimensions and use different inner products.

## The Singular Values

**Definition.** The **singular values** of an operator $T$ are the eigenvalues of $|T|=(T^{\ast}T)^{1/2}$, counted with multiplicity: sixteen of them.

**Proposition.** The singular values are the square roots of the eigenvalues of $T^{\ast}T$, and the operator is an isometry exactly when all sixteen equal one.

**Proof.** The spectral theorem for the positive self-adjoint operator $T^{\ast}T$.

**Corollary.** For a single product with both factors invertible the singular values are the pairwise products of the singular values of the two matrices.

**Proof.** $T_{a,b}^{\ast}T_{a,b}=T_{a^{\ast}a,bb^{\ast}}$, whose eigenvalues are the products of the eigenvalues of the two positive matrices.

**Corollary.** The product of the sixteen singular values is $|\det T|$, and the largest is the operator norm of $T$ for the Hilbert–Schmidt structure.

**Proof.** The determinant is the product of the eigenvalues, and the largest eigenvalue of $|T|$ is the norm.

**The rank of the operator.** The number of nonzero singular values is the rank of $T$ as a $256\times256$ matrix, which is not the length of $T$ and not the matrix rank of the element.

**Proof.** The three ranks are computed in three different spaces.

## Summary

An operator has two adjoints: the plain adjoint for $\operatorname{tr}(XY)$, which sends $T_{a,b}$ to $T_{b,a}$, and the Hilbert–Schmidt adjoint, which sends it to $T_{a^{\ast},b^{\ast}}$. They agree exactly on the operators $T_{a,a^{\ast}}$, and each self-adjoint family has dimension four over $\mathbb{C}$.

The Hilbert–Schmidt isometries are the operators with both factors unitary, a group isomorphic to $U(4)\times U(4)$ of real dimension $32$; the plain isometries are the operators with $b=a^{-1}$, a different group of the same dimension. Every invertible operator has a unique polar decomposition into a positive self-adjoint part and an isometry, and the decomposition of a single product is the product of the decompositions of its factors.

The singular values of an operator are sixteen in number, their product is the modulus of the determinant, and the number of nonzero ones is the rank of the operator as a $256\times256$ matrix, distinct from the length and from the matrix rank of the element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{\mathrm{plain}}=T_{b,a}$ | the plain adjoint for $\operatorname{tr}(XY)$ |
| $T^{\ast}=T_{a^{\ast},b^{\ast}}$ | the Hilbert–Schmidt adjoint |
| $T_{a,a}$, $\dim4$ | the plain self-adjoint family |
| $U(4)\times U(4)$ | the group of Hilbert–Schmidt isometries |
| $T=HU$ | the polar decomposition in the operator algebra |
| sixteen singular values | the spectrum of $|T|$ |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the polar decomposition and singular values in a general setting.
- [The Hilbert–Schmidt Form at $n=4$](the-hilbert-schmidt-form-at-n-4.html), for the inner product used by the second adjoint.
- [The Two-Sided Operators and the Segre Cone at $n=4$](the-two-sided-operators-and-the-segre-cone-at-n-4.html), for the operators and their products.
- [The Length and the Two Ranks at $n=4$](the-length-and-the-two-ranks-at-n-4.html), for the invariants that the singular values do not compute.
- [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html), for the case at order two.
