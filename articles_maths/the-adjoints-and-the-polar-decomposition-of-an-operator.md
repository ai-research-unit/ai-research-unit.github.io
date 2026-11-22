# __The Adjoints and the Polar Decomposition of an Operator__

## Introduction

**The subject.** The operator space carries a positive definite form, $\langle S,T\rangle=\operatorname{tr}(S^{\star}T)$, and every operator has an adjoint with respect to it. The article computes the adjoint of the two families and of the products, shows that the adjoint of the operator space commutes with the star of the algebra, and derives the polar decomposition of an invertible operator into a positive factor and a unitary one. For a product the decomposition splits: the positive factor of $T_{a,b}$ is the product of the positive factors of the two parameters, and the unitary factor is the product of their unitary factors.

**The order of the article.** The form and the adjoint come first; the adjoints of the families second; the commutation of the two involutions third. The polar decomposition follows, first in general and then for a product.

**It assumes** *Operators Acting on Two Sides*, *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* and *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*. **The row of the elements is** where the polar decomposition of an element is read; here it is read for an operator, and the product case borrows the decomposition of each parameter.

**The result in one line.** The adjoint is given by $T_{a,b}^{\dagger}=T_{a^{\star},b^{\star}}$, and every invertible operator is $U|T|$ with $|T|$ positive and $U$ unitary; for a product $|T_{a,b}|=T_{|a|,|b^{\star}|}$.

**Boundaries.** The complex-linear involution of the space is *The Symmetric and Antisymmetric Parts of the Operator Space*; the values of the form on a single operator are *The Numerical Range of the Two-Sided Operators*; the products themselves are *The Two-Sided Operators and the Segre Cone*.

## The Form and the Adjoint

**Definition.** For two operators put
$$
\langle S,T\rangle=\operatorname{tr}(S^{\star}T),
$$
where the star is the conjugation of the algebra applied entry by entry in the basis.

**Proposition.** The form is Hermitian, positive definite, and invariant under the adjoint action of the unitary group of the algebra.

*Proof.* Hermitian symmetry is the identity $\overline{\operatorname{tr}(S^{\star}T)}=\operatorname{tr}(T^{\star}S)$; positivity is $\operatorname{tr}(T^{\star}T)=\sum_{\mu}|t_{\mu}|^{2}$ for the sixteen coordinates; invariance is $\operatorname{tr}((US)^{\star}UT)=\operatorname{tr}(S^{\star}T)$ for a unitary $U$.

**Definition.** The **adjoint** of $T$ is the operator $T^{\dagger}$ with $\langle T^{\dagger}S,U\rangle=\langle S,TU\rangle$ for all $S,U$.

**Proposition.** The adjoint exists, is unique, and the map $T\mapsto T^{\dagger}$ is a conjugate-linear involution.

*Proof.* Existence and uniqueness are the Riesz representation of the form. Conjugate linearity: $(\lambda T)^{\dagger}=\bar\lambda T^{\dagger}$. Involution: $\langle T^{\dagger\dagger}S,U\rangle=\langle S,T^{\dagger}U\rangle=\overline{\langle T^{\dagger}U,S\rangle}=\overline{\langle U,TS\rangle}=\langle TS,U\rangle$.

**Proposition.** For the basis operators,
$$
T_{e_\mu,e_\nu}^{\dagger}=T_{e_\mu^{\star},e_\nu^{\star}},
$$
so that the adjoint of a real basis operator is itself up to the sign of the two vector entries.

*Proof.* Compute $\operatorname{tr}(T_{e_\alpha,e_\beta}^{\star}T_{e_\mu,e_\nu})=\operatorname{tr}(T_{e_\alpha^{\star},e_\beta^{\star}}T_{e_\mu,e_\nu})=4\,\mathrm{Sc}(e_\alpha^{\star}e_\mu)\,\mathrm{Sc}(e_\beta^{\star}e_\nu)$ and read the same expression from $T_{e_\mu^{\star},e_\nu^{\star}}$.

**The reading.** The adjoint is read in the basis without any computation: conjugate the two indices. This is the first sign that the operator space and the algebra are the same kind of object, and the identity will be used in every proof below.

## The Adjoints of the Families

**Theorem.** The two families are adjoint-stable, and
$$
L_a^{\dagger}=L_{a^{\star}},\qquad R_b^{\dagger}=R_{b^{\star}},\qquad T_{a,b}^{\dagger}=T_{a^{\star},b^{\star}}.
$$

*Proof.* For the first, $\langle L_aS,U\rangle=\operatorname{tr}(S^{\star}a^{\star}U)=\operatorname{tr}(S^{\star}L_{a^{\star}}U)=\langle S,L_{a^{\star}}U\rangle$. The second is the same on the other side. The third follows from the two, or directly from the basis computation.

**Corollary.** An operator is self-adjoint exactly when it is a real combination of the products of Hermitian parameters, and a product is self-adjoint exactly when both parameters are Hermitian.

*Proof.* The adjoint conjugates both parameters, so a product is fixed exactly when each parameter is fixed, and the products of Hermitian parameters span the fixed space by the basis computation.

**Corollary.** The adjoint of a product is the product of the adjoints in the same order, and the adjoint of a sum is the sum of the adjoints.

*Proof.* Both statements are the conjugate linearity together with the theorem.

**The reading.** The adjoint respects the two sides separately: it never exchanges the left parameter with the right one. This is the difference between the adjoint and the transposition of the sides, which does exchange them and is complex-linear; the two involutions are distinct and both are needed.

## The Two Involutions

**Definition.** The **operator star** of $T$ is $T^{\circledast}(X)=(T(X^{\star}))^{\star}$.

**Proposition.** The operator star is a conjugate-linear involution of the operator space, it commutes with the adjoint, and it agrees with the algebra star on each family.

*Proof.* Conjugate linearity and involution are immediate from the algebra star. For the commutation, apply both sides to a basis operator: each sends $T_{e_\mu,e_\nu}$ to $T_{e_\mu^{\star},e_\nu^{\star}}$ up to the same sign, by the two preceding computations. On the families, $L_a^{\circledast}=L_{a^{\star}}$.

**Corollary.** The four maps $T\mapsto T$, $T\mapsto T^{\dagger}$, $T\mapsto T^{\circledast}$, $T\mapsto T^{\dagger\circledast}$ form a group of order four acting on the operator space.

*Proof.* Both maps are involutions and they commute, so the group they generate has the four listed elements.

**The reading.** The adjoint and the star are two copies of the same conjugation, one read on the operators and one on the algebra. Their commutation is the statement that the two readings do not interfere, and it is what makes the polar decomposition of a product split.

## The Polar Decomposition

**Theorem.** Every invertible operator $T$ has a unique decomposition $T=UP$ with $U$ unitary and $P$ positive definite self-adjoint, and $P=|T|=(T^{\dagger}T)^{1/2}$.

*Proof.* The operator $T^{\dagger}T$ is self-adjoint and positive definite, hence has a positive definite square root $P$, which is invertible; put $U=TP^{-1}$. Then $U^{\dagger}U=P^{-1}T^{\dagger}TP^{-1}=P^{-1}P^{2}P^{-1}=\mathrm{I}$, so $U$ is unitary. Uniqueness: if $T=UP$ then $T^{\dagger}T=P^{2}$, so $P$ is determined as the positive square root, and then $U$ is determined.

**Corollary.** The positive operators are the exponentials of the self-adjoint ones, and the unitary operators are those preserving the form.

*Proof.* A positive definite self-adjoint operator is $\exp H$ with $H$ self-adjoint, by the spectral theorem applied to its logarithm; an operator preserves the form exactly when $U^{\dagger}U=\mathrm{I}$.

**Corollary.** The decomposition is unique up to the phase: the pairs $(UP)$ and $(U\zeta)(\bar\zeta P)$ with $|\zeta|=1$ give the same operator.

*Proof.* The scalar $\zeta$ is unitary and commutes with $P$, and the two products coincide.

**The reading.** The polar decomposition is the operator form of the polar form of a complex number, and it is the same decomposition in the two readings, since the form and the algebra share the star.

## The Decomposition of a Product

**Theorem.** Let $a=u|a|$ and $b=|b^{\star}|v$ be the polar decompositions of the two parameters, with $|a|=(a^{\star}a)^{1/2}$ and $|b^{\star}|=(bb^{\star})^{1/2}$. Then
$$
|T_{a,b}|=T_{|a|,\,|b^{\star}|},\qquad T_{a,b}=(L_uR_v)\,|T_{a,b}| .
$$

*Proof.* Compute $T_{a,b}^{\dagger}T_{a,b}=T_{a^{\star}a,\,bb^{\star}}=T_{|a|^{2},\,|b^{\star}|^{2}}$, whose positive square root is $T_{|a|,|b^{\star}|}$ because the two parameters are Hermitian positive and their eigenvalues are positive. The unitary factor is then $T_{a,b}$ times the inverse of that positive operator, which is $L_uR_v$.

**Corollary.** The eigenvalues of $|T_{a,b}|$ are the products $\alpha_i\beta_j$ of the eigenvalues of $|a|$ and of $|b^{\star}|$, each taken twice.

*Proof.* The two factors commute and are simultaneously diagonalisable, and each has two eigenvalues of multiplicity two.

**Corollary.** A product is positive self-adjoint exactly when both parameters are Hermitian positive, and unitary exactly when both are unitary.

*Proof.* The positive factor is a product of Hermitian parameters, and it is the identity exactly when both are unitary.

**The reading.** The polar decomposition of a product is the product of the polar decompositions of its parameters, with the phases collected on one side. Nothing in the operator needs a new computation: the positive part carries the two moduli, the unitary part the two phases, and the split is the split of the two parameters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle S,T\rangle=\operatorname{tr}(S^{\star}T)$ | the positive definite form |
| $T^{\dagger}$ | the adjoint of the operator |
| $T^{\circledast}(X)=(T(X^{\star}))^{\star}$ | the operator star |
| $T_{a,b}^{\dagger}=T_{a^{\star},b^{\star}}$ | the adjoint of a product |
| $T=U|T|$ | the polar decomposition |
| $|T_{a,b}|=T_{|a|,|b^{\star}|}$ | the modulus of a product |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the star and the norms of a parameter.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the family whose adjoint is computed here.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the complex-linear involution that the adjoint is not.
- [The Numerical Range of the Two-Sided Operators](the-numerical-range-of-the-two-sided-operators.html), for the values of the same form.
