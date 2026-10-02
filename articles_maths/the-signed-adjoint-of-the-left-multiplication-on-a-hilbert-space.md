# __The Signed Adjoint of the Left Multiplication on a Hilbert Space__

## Introduction

The signed left multiplication of the graded Hilbert space is the one-sided operator $\ell_U(T)=U\,\alpha(T)=L_U\circ\alpha$, the left multiplication with the argument twisted by the grade involution. With respect to the Hilbert–Schmidt form of the category its adjoint is again a signed left multiplication,

$$
(\ell_U)^*=\ell_{\alpha(U^*)},\qquad \alpha(U^*)=\alpha(U)^* ,
$$

so the adjoint of the signed left multiplication is the signed left multiplication by the $\alpha$-adjoint of the parameter. The formula is the working example of the general rule that the adjoint of a twisted one-sided operator is the same one-sided operator with the parameter adjoined and the twist re-applied to the parameter; it differs from the unsigned case, where $(L_U)^*=L_{U^*}$ with no twist, exactly by the occurrence of $\alpha$. Because the signed left multiplication is injective in its parameter — its value at the identity is the parameter itself — the formula turns into exact criteria: $\ell_U$ is self-adjoint exactly when $\alpha(U^*)=U$, it is an isometry exactly when $U$ is, and it is unitary exactly when $U$ is. The present article computes the adjoint, the criteria it produces, and the way the two one-sided adjoints assemble the adjoint of the signed sandwich; the unsigned counterpart is *The Adjoint of the Left Multiplication on a Hilbert Space*, and the two-sided case is *The Signed Adjoint Sandwich on a Hilbert Space*.

This article fixes the Hilbert–Schmidt form, the adjoint of the signed left multiplication and its explicit value, the self-adjointness, isometry and unitarity criteria, the relation of the one-sided adjoint to the adjoint of the signed sandwich, and the comparison with the unsigned and the graded-module cases. The signed left multiplication and the signed right multiplication are *The Signed Left Multiplication on a Hilbert Space*; the unsigned adjoint is *The Adjoint of the Left Multiplication on a Hilbert Space*; the two-sided signed adjoint is *The Signed Adjoint Sandwich on a Hilbert Space*, and the reflection case is *The Signed Adjoint of the Reflection on a Hilbert Space*; the module-level statement is *The Graded Adjoint Action on a Module over a Hilbert Space*; the algebraic form is *The Signed Adjoint of the Left Multiplication on a Graded Algebra* (Part II).

Throughout, $H=H^0\oplus H^1$ is a graded Hilbert space over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ with parity operator $\Gamma$, grade involution $\alpha(T)=\Gamma T\Gamma$, and Hilbert–Schmidt form $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$ on $S_2(H)$. The signed left and right multiplications are $\ell_U=L_U\circ\alpha$, $\ell_U(T)=U\alpha(T)$, and $\varrho_V=R_V\circ\alpha$, $\varrho_V(T)=\alpha(T)V$; the unsigned ones are $L_U(T)=UT$ and $R_V(T)=TV$.

## The Adjoint of the Signed Left Multiplication

**Theorem (the adjoint).** For every $U\in B(H)$ the signed left multiplication is bounded on $S_2(H)$ and

$$
(\ell_U)^*=L_{\alpha(U^*)}\circ\alpha=\ell_{\alpha(U^*)},\qquad (\ell_U)^*(T)=\alpha(U^*)\,\alpha(T),
$$

so the adjoint of a signed left multiplication is the signed left multiplication by the $\alpha$-adjoint parameter; the adjoint of the signed right multiplication is, by the same computation, $(\varrho_V)^*=\varrho_{\alpha(V^*)}$.

*Proof.* Write $\ell_U=L_U\alpha$; the adjoint of a composite reverses the order, $(\ell_U)^*=\alpha^*L_U^*$, the grade involution is self-adjoint for the Hilbert–Schmidt form, $\alpha^*=\alpha$, and $L_U^*=L_{U^*}$ by *The Adjoint of the Left Multiplication on a Hilbert Space*; hence $(\ell_U)^*=\alpha L_{U^*}$, which acts by $T\mapsto\alpha(U^*T)=\alpha(U^*)\alpha(T)=\ell_{\alpha(U^*)}T$. The signed right case is $\varrho_V=R_V\alpha$, with the same three ingredients.

**Proposition (the explicit value and the involution).** The involution of the parameter that appears in the adjoint is the composite of the Hilbert adjoint and the grade involution,

$$
U\ \longmapsto\ \alpha(U^*)=\alpha(U)^* ,
$$

which is an involutive antiautomorphism of $B(H)$, $\alpha((UV)^*)=\alpha(U^*)\alpha(V^*)$ reversed as $\alpha(V^*)\alpha(U^*)$; the map $\ell_U\mapsto(\ell_U)^*$ is therefore an involution on the family of signed left multiplications.

*Proof.* $\alpha$ is multiplicative and the adjoint reverses the product, so $\alpha((UV)^*)=\alpha(V^*U^*)=\alpha(V^*)\alpha(U^*)$; the square of $U\mapsto\alpha(U^*)$ is the identity because both $\alpha$ and the adjoint are involutions and they commute, $\alpha(U^*)^*=\alpha(U)$.

**Corollary (contrast with the unsigned case).** For the unsigned left multiplication the adjoint is $(L_U)^*=L_{U^*}$; for the signed one it is $(\ell_U)^*=\ell_{\alpha(U^*)}$. The two agree exactly when $\alpha(U^*)=U^*$, that is, on the parameters fixed by the grade involution, and the discrepancy is the twist of the parameter by $\alpha$.

*Proof.* The unsigned identity is the previous article; the signed one is the theorem; comparing the two, $\ell_{\alpha(U^*)}=\ell_{U^*}$ iff $\alpha(U^*)=U^*$ by the injectivity of the parameter, which is the fixed-point condition.

## Self-Adjointness, Isometry and Unitarity

**Theorem (self-adjointness).** The signed left multiplication is self-adjoint,

$$
(\ell_U)^*=\ell_U,
$$

if and only if

$$
\alpha(U^*)=U .
$$

In particular $\ell_U$ is self-adjoint when $U$ is self-adjoint and even, and it is never self-adjoint for a nonzero odd $U$.

*Proof.* The family is faithful: $\ell_A(I)=A\alpha(I)=A$, so $\ell_A=\ell_C$ iff $A=C$; the criterion is therefore the equality $\ell_{\alpha(U^*)}=\ell_U$, that is $\alpha(U^*)=U$. If $U$ is self-adjoint and even, $\alpha(U^*)=\alpha(U)=U$; if $U$ is odd and nonzero then $\alpha(U^*)=\alpha(U)^*=-U^*$, and $-U^*=U$ would make $U$ skew-adjoint and odd, contradicting $U^*=-\alpha(U)=\alpha(-U)$, so no nonzero odd $U$ satisfies the criterion.

**Theorem (isometry and unitarity).** The signed left multiplication is an isometry of $S_2(H)$ if and only if $U$ is an isometry, and it is unitary if and only if $U$ is unitary; more precisely

$$
(\ell_U)^*\ell_U=L_{\alpha(U^*U)},\qquad \ell_U(\ell_U)^*=L_{UU^*},
$$

so $\ell_U$ is isometric exactly when $\alpha(U^*U)=I$, which is $U^*U=I$ because $\alpha$ is injective, and it is unitary exactly when in addition $UU^*=I$.

*Proof.* By the composition rules of the signed left multiplication, $\ell_{\alpha(U^*)}\ell_U=L_{\alpha(U^*)\alpha(U)}=L_{\alpha(U^*U)}$, and $\ell_U\ell_{\alpha(U^*)}=L_{U\alpha(\alpha(U^*))}=L_{UU^*}$ because $\alpha^2=\mathrm{id}$; the identity of $S_2(H)$ is $L_I$, and $L_{A}=L_I$ iff $A=I$; the injectivity of $\alpha$ identifies $\alpha(U^*U)=I$ with $U^*U=I$.

**Corollary (partial isometries and the absence of projections).** The signed left multiplication is a partial isometry exactly when $U$ is a partial isometry, its initial and final projections being $L_{\alpha(U^*U)}$ and $L_{UU^*}$; it is never an orthogonal projection, since $\ell_U^2=L_{U\alpha(U)}$ equals $\ell_U$ only for $U=I$ and $\ell_I=\alpha$ is not idempotent. The range of $\ell_U$ is $U\,B(H)$ and its kernel is $\alpha(\ker U)$.

*Proof.* The two factors $(\ell_U)^*\ell_U$ and $\ell_U(\ell_U)^*$ are $L_{\alpha(U^*U)}$ and $L_{UU^*}$, which are projections exactly when $UU^*$ and $\alpha(U^*U)$ are, and this is the partial-isometry condition for $\ell_U$ and, $\alpha$ preserving projections, for $U$. For the idempotence, $\ell_U^2=\ell_{U\alpha(U)}=L_{U\alpha(U)}$ and $L_{U\alpha(U)}=L_U$ iff $\alpha(U)=I$ iff $U=I$, while $\ell_I=\alpha$ has $\alpha^2=\mathrm{id}\neq\alpha$; the kernel and range statements are those of *The Signed Left Multiplication on a Hilbert Space*.

## The One-Sided Adjoints and the Sandwich

**Proposition (the adjoint of the sandwich from the one-sided adjoints).** The signed sandwich factors as $S_{A,B}=\ell_AR_{\alpha(B)}=L_A\varrho_B$, and its adjoint is the composite of the two one-sided adjoints in the reverse order,

$$
(S_{A,B})^*=R_{\alpha(B)}^*\ell_A^*=R_{\alpha(B^*)}\ell_{\alpha(A^*)},
$$

which evaluates to $\alpha(A^*)\,\alpha(\cdot)\,\alpha(B^*)$ and is the closed form $S_{\alpha(A^*),\alpha(B^*)}$; the one-sided adjoint of the present article is therefore exactly the left factor of the sandwich adjoint.

*Proof.* The adjoint of a product reverses the order, giving $R_{\alpha(B)}^*\ell_A^*$; the one-sided adjoints are $R_{\alpha(B)}^*=R_{\alpha(B^*)}$ and $\ell_A^*=\ell_{\alpha(A^*)}$; the evaluation is $X\mapsto\alpha(A^*)\alpha(X)\alpha(B^*)$, which is the signed sandwich with parameters $\alpha(A^*)$ and $\alpha(B^*)$, in agreement with *The Signed Adjoint Sandwich on a Hilbert Space*.

**Corollary (the two-sided family is closed and generated).** The adjunction maps the signed left multiplications to signed left multiplications, the signed right multiplications to signed right multiplications, and the signed sandwiches to signed sandwiches; the algebra generated by the signed left and right multiplications is a $*$-algebra of operators on the Hilbert–Schmidt space, and its adjoint closure is the whole of it.

*Proof.* The three closure statements are the three adjoint formulas; an algebra closed under adjunction and under products is a $*$-algebra, and the closure statement is the definition read on the generating families.

**Example (the rank-one computation).** With $\alpha(\xi\otimes\bar\eta)=\Gamma\xi\otimes\overline{\Gamma\eta}$, the signed left multiplication acts on the rank-one operator by $\ell_U(\xi\otimes\bar\eta)=U\Gamma\xi\otimes\overline{\Gamma\eta}$ and the adjoint acts by $\ell_{\alpha(U^*)}(\xi\otimes\bar\eta)=\alpha(U^*)\Gamma\xi\otimes\overline{\Gamma\eta}$; the pairing of two rank-one operators reproduces the identity $\langle\ell_UT,S\rangle_{\mathrm{HS}}=\langle T,\ell_{\alpha(U^*)}S\rangle_{\mathrm{HS}}$, which is the theorem on the rank-one generators.

## Examples and Degenerate Cases

**Proposition (the degenerate case $\alpha=\mathrm{id}$).** If the grading is trivial then $\ell_U=L_U$ and the adjoint theorem reduces to $(L_U)^*=L_{U^*}$; the self-adjointness criterion reduces to $U^*=U$, the isometry criterion to $U^*U=I$, and the signed theory is the unsigned theory of *The Adjoint of the Left Multiplication on a Hilbert Space*.

*Proof.* With $\alpha=\mathrm{id}$ the map $\ell_U$ is $L_U$ by definition, and every formula of the article reduces to the corresponding unsigned one; the reduction of the criteria is the substitution $\alpha=\mathrm{id}$.

**Example (the diagonal graded case).** When $H$ has a homogeneous orthonormal basis and $U$ is diagonal with entries $u_m$, the signed left multiplication has the eigenvalues $\varepsilon_m\varepsilon_nu_m$ on the matrix units $e_m\otimes\bar e_n$, with $\varepsilon_m=(-1)^{|e_m|}$; the adjoint has the conjugate eigenvalues $\varepsilon_m\varepsilon_n\bar u_m$, and the self-adjointness criterion $\alpha(U^*)=U$ reads $\bar u_m=u_m$ for a diagonal parameter, that is, the reality of the diagonal entries.

**Example (the finite-dimensional sign count).** For $H=\mathbb{K}^{p+q}$ with the diagonal grading, an even self-adjoint $U=\operatorname{diag}(A_0,A_0')$ satisfies $\alpha(U^*)=U$ and gives a self-adjoint $\ell_U$, while an odd self-adjoint $U$ gives $\alpha(U^*)=\alpha(U)=-U\neq U$ and never does; the exact set of self-adjoint signed left multiplications is the set of parameters with $\alpha(U^*)=U$, of which the even self-adjoint ones are the standard members.

## Summary

With respect to the Hilbert–Schmidt form, the signed left multiplication $\ell_U=L_U\alpha$ has adjoint $(\ell_U)^*=\ell_{\alpha(U^*)}$, where $\alpha(U^*)=\alpha(U)^*$ is the composite of the Hilbert adjoint with the grade involution; the signed right multiplication has adjoint $(\varrho_V)^*=\varrho_{\alpha(V^*)}$, so each signed one-sided family is closed under adjunction and stays on its side. Because the family is faithful — $\ell_U$ determines $U$ as its value at the identity — the adjoint formula gives exact criteria: $\ell_U$ is self-adjoint exactly when $\alpha(U^*)=U$, an isometry exactly when $U$ is, unitary exactly when $U$ is, and a partial isometry exactly when $U$ is; in particular a nonzero odd parameter never gives a self-adjoint signed left multiplication. The signed sandwich factors as $S_{A,B}=\ell_AR_{\alpha(B)}=L_A\varrho_B$, and its adjoint is assembled from the two one-sided adjoints in the reverse order, giving the closed form $S_{\alpha(A^*),\alpha(B^*)}$; the algebra generated by the signed left and right multiplications is therefore a $*$-algebra on the Hilbert–Schmidt space. When the grading is trivial the article collapses to *The Adjoint of the Left Multiplication on a Hilbert Space*, and the module-level form of the same computation is *The Graded Adjoint Action on a Module over a Hilbert Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\ell_U(T)=U\alpha(T)=L_U\circ\alpha$ | the signed left multiplication |
| $\varrho_V(T)=\alpha(T)V=R_V\circ\alpha$ | the signed right multiplication |
| $(\ell_U)^*=\ell_{\alpha(U^*)}$ | the adjoint of the signed left multiplication |
| $(\varrho_V)^*=\varrho_{\alpha(V^*)}$ | the adjoint of the signed right multiplication |
| $\alpha(U^*)=\alpha(U)^*$ | the adjoint parameter |
| $\alpha(U^*)=U$ | self-adjointness criterion |
| $(\ell_U)^*\ell_U=L_{\alpha(U^*U)}$ | the isometry computation |
| $(S_{A,B})^*=R_{\alpha(B^*)}\ell_{\alpha(A^*)}$ | the sandwich adjoint from the one-sided adjoints |
| $\ell_A(I)=A$ | faithfulness of the parameter |
| $\alpha=\mathrm{id}$ | the degenerate case, signed equals unsigned |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the one-sided multiplications, their adjoints and the composition rules.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the $*$-automorphisms and the twisted multiplications.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the elementary operators and the adjoints of the two-sided operators.
- Barry Simon, *Trace Ideals and Their Applications*, Mathematical Surveys and Monographs 120 (American Mathematical Society, 2nd ed. 2005), for the Hilbert–Schmidt form and the rank-one computations.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the adjoints of the elementary operators and the self-adjointness criteria.
